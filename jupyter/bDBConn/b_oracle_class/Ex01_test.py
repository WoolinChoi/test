"""
    [ 절차 ]
        1. 데이타베이스 Connection 생성
        2. 커서 생성 ( 커서 : sql 명령어를 실행시켜 주는 객체 )
        3. sql 문장 만들기
        4. sql 문장 실행
        5. 커밋 ( 트랜젝션의 내용을 DB에 반영함 )
        6. Connection 닫기
"""

import cx_Oracle as oci
conn = oci.connect("scott/tiger@192.168.0.170:1521/orcl")
# print(conn.version)    # 버전확인
cur = conn.cursor()
sql = "SELECT * FROM emp"
cur.execute(sql)
datas = cur.fetchall()
for row in datas:
    print(row[0], row[1], row[5])
cur.close()
conn.close()
