---
layout: post
title: function
category: oracle
tags: [java, oracle, function]
comments: false
---

# [function]()

## function
~~~sql
-- [숫자형 함수]
-- 사원명, 급여, 월급(급여/12)를 출력하되 월급은 십단위에서 반올림하여 출력
SELECT ename, sal, round(sal / 12, -2) "월급"
FROM emp;

-- 사원명, 급여, 세금(급여의 3.3%)를 원단위 절삭하고 출력
SELECT ename, sal, trunc(sal * 0.033, -1) "세금"
FROM emp;

-- 공백 제거
SELECT  '-' || TRIM(' 이순신 ')|| '-' AS col1,
        '-'|| LTRIM(' 이순신 ') || '-' AS col2,
        '-'|| RTRIM(' 이순신 ') || '-' AS col3 
FROM dual;

-- 가상테이블(dual)을 이용한 오늘 날짜 
SELECT sysdate FROM dual;

-- [문자형 함수]
-- 1. smith의정보를 사원번호, 성명, 담당업무(소문자) 출력
SELECT * FROM emp;
SELECT empno, ename, LOWER(job) AS job 
FROM emp
WHERE ename = 'SMITH';

-- 2. 사원번호, 사원명(첫글자만 대문자), 담당업무(첫글자만대문자)로 출력
SELECT empno, INITCAP(ename), INITCAP(job) AS job
FROM emp;
          
-- 3. 이름의 첫글자가 ‘K’보다크고 ‘Y’보다 작은 사원의 정보( 사원번호, 이름, 업무, 급여, 부서번호)를 출력하되 이름순으로 정렬
SELECT empno, ename, job, sal, deptno 
FROM emp
WHERE SUBSTR(ename, 1, 1) > 'K' AND SUBSTR(ename, 1, 1) < 'Y'
ORDER BY ename;
          
-- 4. 이름이 5글자 이상인사원들을 출력
SELECT *
FROM emp
WHERE LENGTH(ename) >= 5;

-- 5. 이름을 15자로 맞추고글자는 왼쪽에 오른쪽에는 ‘*’로 채운다
SELECT  RPAD(ename, 15, '*') AS ename
FROM emp;
 
-- 6. 월급은 10자로 맞추고숫자는 오른쪽에 왼쪽엔 ‘-‘로 채운다
SELECT  LPAD(sal, 10, '-') AS sal
FROM emp;

-- 7. 월급을 숫자에서 ‘영일이삼사오육칠팔구’ 글자로 대체 : TRANSLATE
SELECT TRANSLATE(sal, '0123456789', '영일이삼사오육칠팔구')
FROM emp;

-- 8. 월급의 숫자에서 0을‘$’로 바꾸어 출력 : REPLACE
SELECT REPLACE(sal, 0, '$')
FROM emp;

-- [날짜형 함수]
-- 1. 현재까지 근무일 수가 많은 사람 순으로 출력
SELECT * FROM emp;
SELECT *
FROM emp
ORDER BY sysdate - nvl(hiredate, sysdate) DESC;

-- 2. 현재 날짜에서 돌아오는 ‘화’요일의 날짜 구하기
SELECT next_day(sysdate, '화')
FROM dual;

-- 3. 현재 날짜에서 해당 월의 마지막 날짜 구하기
SELECT last_day(sysdate)
FROM dual;

-- 4. 현재까지 근무일 수가 몇 주 몇 일인가를 출력
SELECT ename, hiredate, sysdate-hiredate AS total_day,
TRUNC((sysdate - hiredate) / 7) AS weeks, CEIL(MOD(sysdate - hiredate, 7)) days
FROM emp;

-- 5. 10번 부서의 사원의 현재까지의 근무 월수를 계산
SELECT ename, TRUNC(months_between(sysdate, hiredate))
FROM emp
WHERE deptno = 10;

-- [변환함수]
-- 1. 입사일자에서 입사년도를 출력
SELECT ename, hiredate, to_char(hiredate, 'YYYY') AS hireyear
FROM emp;

-- 2. 입사일자에서 입사월을 출력
SELECT ename, hiredate, to_char(hiredate, 'YYYY-MM') AS hiremonths
FROM emp;

-- 3. 입사일자에서 입사일을 출력
SELECT ename, hiredate, to_char(hiredate, 'DD') AS hireday
FROM emp;

-- 4. 1981년도에 입사한 사원 검색
SELECT ename, hiredate
FROM emp
WHERE to_char(hiredate, 'YYYY') = 1981 ;

-- 5. 5월에 입사한 사원 검색
SELECT ename, hiredate
FROM emp
WHERE to_char(hiredate, 'MM') = 5;

SELECT * FROM emp;
-- 6. 입사일자를 ‘1999년 1월 1일’ 형식으로 출력
SELECT ename, to_char(hiredate, 'YYYY"년" MM"월" DD"일"') AS hiredate
FROM emp;

-- [조건함수]
CREATE TABLE info(
    hakbun  char(4),
    name    varchar2(10),
    jumin   char(14),
    gender  varchar2(10),
    age     number(3)
);
INSERT INTO info(hakbun, name, jumin, gender, age) VALUES ('9000', '홍길동', '801212-1234567', '남자', 26);
INSERT INTO info(hakbun, name, jumin, gender, age) VALUES ('8000', '송혜교', '921212-2234567', '여자', 26);
INSERT INTO info(hakbun, name, jumin, gender, age) VALUES ('7000', '홍길순', '801212-2345678', '여자', 26);
INSERT INTO info(hakbun, name, jumin, gender, age) VALUES ('6000', '홍길자', '801212-1134567', '남자', 26);

DROP TABLE info;
SELECT * FROM info;

-- 주민번호에서 성별 구하기
SELECT decode(substr(jumin, 8, 1), 1, '남자', 3, '남자', '여자') AS gender
FROM info;

-- 부서번호가 10이면 영업부, 20이면 관리부, 30이면 IT부 그 외는 기술부로 출력
SELECT decode(deptno, 10, '영업부', 20, '관리부', 30, 'IT부', '기술부') AS deptno
FROM emp;

SELECT * FROM emp;

-- 업무(job)이 analyst이면 급여 증가가 10%이고 clerk이면 15%, manager이면 20%인 경우 사원번호, 사원명, 업무, 급여, 증가한 급여를 출력
SELECT empno, ename, job, sal, 
CASE job  
WHEN 'ANALYST' THEN sal * 1.1
WHEN 'CLERK'   THEN sal * 1.15
WHEN 'MANAGER' THEN sal * 1.2
ELSE sal END plussal
FROM emp;

SELECT * FROM emp;
SELECT ROWNUM empno, ename FROM emp WHERE ROWNUM <= 5;

-- 1. 업무가 ‘SALESMAN’인 사람들의 월급의 평균, 총합, 최소값, 최대값을 구하기
SELECT avg(sal) avg, sum(sal) sum, min(sal) min, max(sal) max
FROM emp
WHERE job = 'SALESMAN';

-- 집계함수는 NULL값도 처리해준다.
INSERT INTO emp(empno, ename, job) VALUES(9988, '홍홍이', 'SALESMAN'); 

-- 2. 커미션(COMM)을 받는 사람들의 수는
SELECT COUNT(comm) cnt
FROM emp
WHERE nvl(comm, 0) <> 0;

-- [데이터 그룹]
/*
    SELECT columns  
    FROM  table_name  
    WHERE condition
    GROUP BY group_by_expression
    HAVING condition
    ORDER BY column;
 */
-- 1. 부서별로인원수, 평균급여, 최저급여, 최고급여, 급여의 합을 구하기
-- GROUP BY는 그룹핑하는 컬럼과 직계함수만 가능하다.
SELECT deptno, job, count(*) cnt, round(avg(sal)) avg, min(sal) min, max(sal) max, sum(sal) sum  
FROM  emp 
GROUP BY deptno, job;

-- 2. 부서별로인원수, 평균급여, 최저급여, 최고급여, 급여의 합을 구하기 (부서별 급여의 합이 높은 순으로)
SELECT deptno, count(*) cnt, round(avg(sal)) avg, min(sal) min, max(sal) max, sum(sal) sum   
FROM  emp 
GROUP BY deptno
ORDER BY sum DESC;

 -- 3. 부서별업무별 그룹하여 부서번호, 업무, 인원수, 급여의 평균, 급여의 합을 구하기
SELECT deptno, job, count(*) cnt, round(avg(sal)) avg, min(sal) min, max(sal) max, sum(sal) sum  
FROM  emp 
GROUP BY deptno, job
ORDER BY deptno;

-- 4. 급여가 최대 2900 이상인 부서에 대해 부서번호, 평균 급여, 급여의 합을 출력
SELECT deptno, round(avg(sal)) avg, sum(sal) sum
FROM emp
GROUP BY deptno
HAVING max(sal) >= 2900;
 

-- 5. 업무별 급여의 평균이 3000이상인 업무에 대해 업무명, 평균 급여, 급여의 합을 출력
SELECT job, round(avg(sal)) avg, sum(sal) sum
FROM emp
GROUP BY job
HAVING round(avg(sal)) >= 3000;
 

-- 6. 전체 합계 급여가 5000를초과하는 각 업무에 대해서 업무와 급여 합계를 출력(단, SALESMAN은제외하고 급여 합계가 높은 순으로 정렬)
SELECT job, sum(sal) sum
FROM emp
WHERE job <> 'SALESMAN'
GROUP BY job
HAVING sum(sal) > 5000
ORDER BY sum DESC;
 
-- 7. 업무별최고 급여와 최소 급여의 차이를 구하라
SELECT job, max(sal) - min(sal) AS sal_gap
FROM emp
GROUP BY job; 
 
-- 8. 부서 인원이 4명보다 많은 부서의 부서번호, 인원수, 급여의 합을 출력 
SELECT  deptno, count(*) cnt, sum(sal) sum
FROM emp
GROUP BY deptno
HAVING count(*) > 4;

-- [GROUP BY 절에 사용하는 함수]
-- ROLLUP : 결과에 그룹별 합계 정보를 추가
-- CUBE : 그룹핑 된 컬럼의 합계 정보를 추가
SELECT job, sum(sal) sum FROM emp GROUP BY job;
SELECT job, sum(sal) sum FROM emp GROUP BY rollup(job);
SELECT job, sum(sal) sum FROM emp GROUP BY cube(job);

-- [연습문제] employees
-- 1. 2003년에 입사한 사원들의 사번, 이름, 입사일을 출력
SELECT * FROM employees;
SELECT employee_id, (first_name || ' ' || Last_name) full_name, hire_date  
FROM employees
WHERE hire_date >= '03/01/01' AND hire_date <= '03/12/31';

-- 2. 업무가 FI_ACCOUNT / FI_MGR / SA_MAN / SA_REP 인 사원들의 정보를 출력
SELECT *
FROM employees
WHERE job_id IN ('FI_ACCOUNT', 'FI_MGR', 'SA_MAN', 'SA_REP');

-- 3. 커미션을 받는 사원들의 명단을 출력
SELECT *
FROM employees
WHERE nvl(commission_pct, 0) != 0;

-- 4. 업무가 SA_MAN 또는 SA_REP이면 "판매부서"를 그 외는 "그 외 부서"라고 출력
SELECT decode(job_id, 'SA_MAN', '판매부서', 'SA_REP', '판매부서', '그 외 부서') AS job_id
FROM employees
ORDER BY job_id DESC;
~~~

