import pymysql
import re
# 사용자로부터 메시지를 받아서 유효한 입력을 확인하는 함수
def check_input(message, valid_inputs):
    while True:
        i = input(message + " >>> ").upper()
        if i in valid_inputs:
            return i
        else:
            print("잘못된 입력입니다. 확인 후 다시 입력해 주세요.")

# 메뉴 페이지 출력 함수
def show_menu_page():
    print("======================================")
    print("메뉴")
    print("--------------------------------------")
    print("I: 회원 정보를 등록합니다.")
    print("S: 회원을 LIKE 검색합니다.")
    print("Q: 프로그램을 종료합니다.")
    print("======================================")

# 회원 정보 등록 함수
def do_insert():
    print("======================================")
    print("회원 등록")
    print("--------------------------------------")
    name = input("이름 : ")
    age = int(input("나이 : "))
    email = input("이메일 : ")
    query = "INSERT INTO members (member_name, member_age, member_email) VALUES (%s, %s, %s)"
    with pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="tkdwogn", db="sampledb", cursorclass=pymysql.cursors.DictCursor) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (name, age, email))
        print("회원 정보를 정상적으로 등록했습니다.")

# 회원 검색 및 상세 조회 함수
def do_search():
    print("======================================")
    print("회원 검색")
    print("--------------------------------------")
    name = input("이름 : ")
    query = "SELECT * FROM members WHERE member_name LIKE %s"
    with pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="tkdwogn", db="sampledb", cursorclass=pymysql.cursors.DictCursor) as connection:
        cursor = connection.cursor()
        cursor.execute(query, ("%"+name+"%",))
        members = cursor.fetchall()
        print(f"검색 결과 (총 {len(members)}건)")
        if not members:
            print("일치하는 결과가 없습니다.")
        else:
            for member in members:
                print(f"{member['member_id']} : {member['member_name']}")
            member_id = input("상세 정보를 조회할 회원 번호를 입력하세요: ")
            query = "SELECT * FROM members WHERE member_id = %s"
            cursor.execute(query, (member_id,))
            member = cursor.fetchone()
            print("======================================")
            print(f"ID: {member['member_id']}")
            print(f"이름: {member['member_name']}")
            print(f"나이: {member['member_age']}")
            print(f"이메일: {member['member_email']}")

# 회원 정보 수정 함수
def do_update(member_id):
    print("======================================")
    print("회원 정보 수정")
    print("--------------------------------------")
    age = int(input("변경할 나이 : "))
    email = input("변경할 이메일 : ")
    query = "UPDATE members SET member_age = %s, member_email = %s WHERE member_id = %s"
    with pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="tkdwogn", db="sampledb", cursorclass=pymysql.cursors.DictCursor) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (age, email, member_id))
        print("회원 정보를 정상적으로 수정했습니다.")

# 회원 정보 삭제 함수
def do_delete(member_id):
    print("======================================")
    print("회원 정보 삭제")
    print("--------------------------------------")
    query = "DELETE FROM members WHERE member_id = %s"
    with pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="tkdwogn", db="sampledb", cursorclass=pymysql.cursors.DictCursor) as connection:
        cursor = connection.cursor()
        cursor.execute(query, (member_id,))
        print("회원 정보를 정상적으로 삭제했습니다.")

def main():
    while True:
        show_menu_page()
        menu = check_input("메뉴를 선택하세요. (I: 등록 / S: 검색 / Q: 종료)", "ISQ")
        if menu == "Q":
            print("프로그램을 종료합니다.")
            break
        elif menu == "I":
            do_insert()
        elif menu == "S":
            do_search()

if __name__ == "__main__":
    main()