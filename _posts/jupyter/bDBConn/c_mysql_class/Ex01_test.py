"""
    [ 절차 ]
        1. 데이타베이스 Connection 생성
        2. 커서 생성 ( 커서 : sql 명령어를 실행시켜 주는 객체 )
        3. sql 문장 만들기
        4. sql 문장 실행
        5. 커밋 ( 트랜젝션의 내용을 DB에 반영함 )
        6. Connection 닫기
"""

import MySQLdb as ms
import csv

conn = ms.connect(host='localhost', user='scott', passwd='tiger', db='pythondb')
cur = conn.cursor()
sql = """
        CREATE TABLE IF NOT EXISTS emp(
        empno integer,
        ename varchar(20),
        job varchar(20),
        mgr integer,
        hiredate date,
        sal float,
        comm float,
        deptno integer
        )
    """
cur.execute(sql)
conn.commit()
conn.close()