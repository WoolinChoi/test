"""
    [ 절차 ]
        1. 데이타베이스 Connection 생성
        2. 커서 생성 ( 커서 : sql 명령어를 실행시켜 주는 객체 )
        3. sql 문장 만들기
        4. sql 문장 실행
        5. 커밋 ( 트랜젝션의 내용을 DB에 반영함 )
        6. Connection 닫기
"""

import sqlite3
import csv

def createDBtable(db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = """
            CREATE TABLE if not exists supply(
            supplier_name text,
            invoice_number integer,
            part_number integer,
            cost integer,
            purchase_date date
            )
        """
    cur.execute(sql)
    conn.commit()
    conn.close()

def saveDBtable(db, data):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = "INSERT INTO supply(supplier_name, invoice_number, part_number, cost, purchase_date) VALUES (?, ?, ?, ?, ?)"
    cur.execute(sql, data)
    conn.commit()
    conn.close()

def viewDBdata(db, table):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = "SELECT * FROM {0}".format(table)
    cur.execute(sql)
    # for table in cur:
    #     print(table)
    rows = cur.fetchall()
    print(rows)
    for row in rows:
        print(row)
    conn.close()


if __name__ == '__main__':

    db_name = '../db/supplyDB.db'

    # (1) DB에 테이블 생성
    # createDBtable(db_name)

    # ------------------------------------------------------
    # (2) csv파일을 읽어서 DB에 테이블 입력
    # file_name = '../files/supply.csv'
    # file = csv.reader(open(file_name, 'r'), delimiter=',')
    # header = next(file, None)    # 한 줄을 읽어서 아무일도 하지 않는다.
    # print(header)
    # for row in file:
    #     # print(type(row))
    #     saveDBtable(db_name, row)

    # ------------------------------------------------------
    # (3) DB에 저장되어 있는 테이블값 출력
    viewDBdata(db_name, 'supply') # 디비명, 테이블명
