import time
from MoneyFlow_view import *
from MoneyFlow_model import *
from MoneyFlow_util import *


def menu_handler():
    clean_terminal()
    point = main_menu_handler()
    while point != 0:
        if point == 1:  # 1.Add new item
            add_new_item(category_menu_handler())
            point = main_menu_handler()
        elif point == 2:  # 2.Show all
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 3:  # 3.Sort by date asc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 4:  # 4.Sort by date dsc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 5:  # 5.Sort by name asc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 6:  # 6.Sort by name dsc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 7:  # 7.Sort by category asc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 8:  # 8.Sort by category dsc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 9:  # 9.Sort by cost asc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 10:  # 10.Sort by cost dsc
            show_all_handler(point)
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 11:  # 11.Delete item
            delete_one_handler()
            go_futher_footer()
            input()
            point = main_menu_handler()
        elif point == 12:  # 12.Delete all data
            delete_all_handler()
            go_futher_footer()
            input()
            point = main_menu_handler()
    exit_menu_handler()  # 0.Exit app


def main_menu_handler():
    clean_terminal()
    help_menu()
    point = check_user_input(Moneyflow.menu, 'Pick up some point from the menu: ')
    return point

def category_menu_handler():
    clean_terminal()
    categories_help()
    category = check_user_input(Moneyflow.categories, 'Category from the menu: ')
    return category

def show_all_handler(point):
    clean_terminal()
    data_result_header()
    show_all(point)

def delete_one_handler():
    clean_terminal()
    delete_one_header()
    delete_item(check_item_delete())

def delete_all_handler():
    clean_terminal()
    delete_all_header()
    delete_all_data()

def exit_menu_handler():
    clean_terminal()
    exit_view()
    time.sleep(2)

welcome()
time.sleep(2)
menu_handler()







