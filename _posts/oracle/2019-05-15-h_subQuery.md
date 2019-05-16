---
layout: post
title: subQuery
category: oracle
tags: [java, oracle, subQuery]
comments: false
---

# [subQuery]()

## SubQuery
~~~sql
-- 1. 연도별로 입사자들의 최소급여, 최대 급여, 급여의 총합 그리고 평균 급여를 구하시오
SELECT to_char(hire_date, 'YYYY') year, min(salary) minsal, max(salary) maxsal, sum(salary) sumsal, round(avg(salary)) avgsal 
FROM employees 
GROUP BY to_char(hire_date, 'YYYY') 
ORDER BY year;

-- 2. 부서별 평균 급여가 $10,000 이상인 부서만 구하시오. ( 평균급여가 높은 순으로 )
SELECT d.department_name depart, round(avg(e.salary)) sal
FROM employees e INNER JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING avg(e.salary) >= 10000 
ORDER BY avg(e.salary) DESC;

-- 3. 부서별 최대 급여를 구하시오.  해당되는 부서번호는 10번과 20번임
SELECT department_id depart, max(salary) maxsal
FROM employees
WHERE department_id = 10 OR department_id = 20
GROUP BY department_id;

-- 4. 이름의 성이 'King' 사원의 사번과 부서명을 출력 ( employees, departments )
SELECT e.employee_id "사번", d.department_name "부서명"
FROM employees e INNER JOIN departments d
ON e.department_id = d.department_id
WHERE e.last_name = 'King';

-- 5. 이름의 성이 'King' 사원의 사번과 부서명 그리고 업무명을 출력 ( employees, departments, jobs )
SELECT * FROM jobs;
SELECT e.employee_id "사번", d.department_name "부서명", j.job_title "업무명"
FROM employees e INNER JOIN departments d
ON e.department_id = d.department_id
INNER JOIN jobs j
ON e.job_id = j.job_id
WHERE e.last_name = 'King';

-- 6. 2007년 상반기에 입사한 사원들의 사번과 이름, 입사일 그리고 부서명을 출력 (*) Grant는 아직 부서가 배정받지 못한 상태이지만 Grant도 출력되려면
SELECT e.employee_id "사번", e.first_name || e.last_name "이름", e.hire_date "입사일", d.department_name "부서명"
FROM employees e LEFT OUTER JOIN departments d
ON (e.department_id = d.department_id) AND 
(to_char(e.hire_date, 'YYYY-MM-DD') >= '2007-01-01' AND to_char(e.hire_date, 'YYYY-MM-DD') < '2007-07-01');

-- 7. 'Executive' 부서에서 사원과 해당 사원의 관리자 이름을 출력 (*) 관리자가 없는 사원인 'King'이 출력되려면
SELECT e.employee_id id, d.department_name depart, e.first_name || e.last_name "사원", e2.first_name || e2.last_name "관리자"
FROM employees e LEFT OUTER JOIN employees e2
ON (e.manager_id = e2.employee_id) LEFT OUTER JOIN departments d
ON (e.department_id = d.department_id)
WHERE d.department_name = 'Executive';

-- 1. 업무 별로 최소 급여를 받는 사원의 정보를 사원번호, 이름, 담당업무, 급여를 출력
-- 업무별로 최소 급여
SELECT * FROM emp;
SELECT job, min(sal) FROM emp GROUP BY job;

SELECT empno, ename, job, sal
FROM emp 
WHERE (job, sal) IN (SELECT job, min(sal) FROM emp GROUP BY job);

-- 2. 10번 부서사원들의 업무와 동일한 직원들 검색
SELECT job FROM emp WHERE deptno = 10;

SELECT *
FROM emp
WHERE job IN (SELECT job FROM emp WHERE deptno = 10);
-- ANY는 조건중에 하나라도 만족하면 된다.
-- WHERE job = ANY (SELECT job FROM emp WHERE deptno = 10);
-- ALL은 조건 모두 만족해야한다.
-- WHERE job = ALL (SELECT job FROM emp WHERE deptno = 10);

-- 3. 적어도 한명의 사원으로부터 보고를 받을 수 있는 사원의 정보를 사원번호, 이름, 업무를 출력
SELECT * FROM emp;
SELECT e.empno, e.ename, e.job
FROM emp e
WHERE EXISTS (SELECT * FROM emp e2 WHERE e.empno = e2.mgr);

-- 부하직원이 없는 사원들을 검색
SELECT *
FROM emp e
WHERE NOT EXISTS (SELECT * FROM emp e2 WHERE e.empno = e2.mgr);

-- 부서별 급여 통계 테이블 생성
create table stat_salary(
             stat_date  date not null,      -- 날짜
             dept_no    number,             -- 부서
             emp_count  number,             -- 사원수
             tot_salary number,             -- 급여총액
             avg_salary number);            -- 급여평균

-- (2) 날짜와 부서번호 입력
INSERT INTO stat_salary(stat_date, dept_no)
SELECT sysdate, deptno FROM dept;

SELECT * FROM stat_salary;

-- (3) 사원수, 급여총액, 평균급여 입력
UPDATE stat_salary s 
SET (s.emp_count, s.tot_salary, s.avg_salary)
= (SELECT count(*), sum(sal), avg(sal) FROM emp e WHERE e.deptno = s.dept_no GROUP BY deptno);

CREATE TABLE emp_copy AS SELECT * FROM emp;
SELECT * FROM emp_copy;

-- 1. SCOTT의 업무와 급여로 JONES의 업무와 급여를 수정
UPDATE emp_copy e
SET (e.job, e.sal) = (SELECT e2.job, e2.sal FROM emp e2 WHERE e2.ename = 'SCOTT')
WHERE e.ename = 'JONES';

-- 2. 부서명이 sales인 사원의 정보를 삭제
SELECT * FROM dept;

DELETE FROM emp_copy
WHERE deptno = (SELECT deptno FROM dept WHERE dname = 'SALES');

-- 3. King에게 보고하는 모든 사원의 이름과 급여를 출력
SELECT e.ename, e.sal
FROM emp e
WHERE e.mgr = (SELECT e2.empno FROM emp e2 WHERE e2.ename = 'KING');

-- 4. 월급이 30번 부서의 최저 월급보다 많은 사원들을 출력
SELECT * FROM emp;
SELECT min(sal) FROM emp e2 WHERE deptno = 30;

SELECT *
FROM emp_copy e
WHERE e.sal > (SELECT min(sal) FROM emp_copy e2 WHERE deptno = 30);

-- 5. 10번 부서의 직원들 중 30번 부서의 사원과 같은 업무를 맡고 있는 사원의 이름과 업무를 출력
SELECT job FROM emp WHERe deptno = 30;

SELECT e.deptno, e.ename, e.job
FROM emp_copy e
WHERE e.deptno = 10 AND e.job IN (SELECT e2.job FROM emp_copy e2 WHERE e2.deptno = 30);

-- [연습]
-- 1. 업무가 jones와 같거나 월급이 ford의 월급 이상인 사원의 정보를 이름, 업무, 부서번호, 급여를 출력(단, 업무별, 월급이 많은 순으로)
SELECT deptno, ename, job, sal
FROM emp 
WHERE job = (SELECT job FROM emp WHERE ename = 'JONES') OR sal >= (SELECT sal FROM emp WHERE ename = 'FORD')
ORDER BY job ASC, sal DESC;

-- 2. scott 또는 ward와 월급이 같은 사원의 정보를 이름, 업무, 급여를 출력
SELECT ename, job, sal
FROM emp
WHERE sal = ANY (SELECT sal FROM emp WHERE ename IN ('SCOTT', 'WARD'));

-- 3. chicago에서 근무하는 사원과 같은 업무를 하는 사원의 이름, 업무를 출력
SELECT ename, job
FROM emp
WHERE job IN (SELECT DISTINCT e.job FROM emp e INNER JOIN dept d ON e.deptno = d.deptno WHERE loc = 'CHICAGO')
ORDER BY job;

-- 4. 부서별로 월급이 평균 월급보다 높은 사원을 부서번호, 이름, 급여를 출력
SELECT e.deptno, e.ename, e.sal
FROM emp e INNER JOIN (SELECT deptno, round(avg(sal)) avg FROM emp GROUP BY deptno) e2
ON e.deptno = e2.deptno
WHERE e.sal > e2.avg;

-- 5. 말단 사원의 사번, 이름, 업무, 부서번호를 출력
SELECT empno, ename, job, deptno
FROM emp
WHERE hiredate = (SELECT max(hiredate) FROM emp);
~~~