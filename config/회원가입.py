import pymysql  
import re  

def print_double_line():
    print("======================================")

def print_single_line():
    print("--------------------------------------")

# 메뉴 페이지를 출력하는 함수
def show_menu_page():
    print_title("메뉴")  
    print("I: 회원 정보를 등록합니다.")  
    print("S: 회원을 LIKE 검색합니다.")  
    print("Q: 프로그램을 종료합니다.")  
    print_tail()  

def print_title(title):
    print()  
    print_double_line()  
    print(title)  
    print_single_line()  


def print_tail():
    print_double_line()
def print_line(character, length):
    print(character * length)

def show_menu_page():
    print_line("=", 30)
    print("메뉴")
    print_line("-", 30)
    print("I: 회원 정보를 등록합니다.")
    print("S: 회원을 LIKE 검색합니다.")
    print("Q: 프로그램을 종료합니다.")
    print_line("=", 30)

show_menu_page()