from os import system, name
from time import sleep

def welcome():
    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    
━━━━┏━┓┏━┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━━━┓━━━━┏┓━━━━━━━━━━━━━━━━━━━━━━━
━━━━┃┃┗┛┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┏━━┛━━━━┃┃━━━━━━━━━━━━━━━━━━━━━━━
━━━━┃┏┓┏┓┃━━━━┏━━┓━━━━┏━━┓━━━━┏━━┓━━━━┏┓━┏┓━━━━━┃┗━━┓━━━━┃┃━━━━━┏━━┓━━━━┏┓┏┓┏┓━━━━
━━━━┃┃┃┃┃┃━━━━┃┏┓┃━━━━┃┏┓┃━━━━┃┏┓┃━━━━┃┃━┃┃━━━━━┃┏━━┛━━━━┃┃━━━━━┃┏┓┃━━━━┃┗┛┗┛┃━━━━
━━━━┃┃┃┃┃┃━━━━┃┗┛┃━━━━┃┃┃┃━━━━┃┃━┫━━━━┃┗━┛┃━━━━┏┛┗┓━━━━━━┃┗┓━━━━┃┗┛┃━━━━┗┓┏┓┏┛━━━━
━━━━┗┛┗┛┗┛━━━━┗━━┛━━━━┗┛┗┛━━━━┗━━┛━━━━┗━┓┏┛━━━━┗━━┛━━━━━━┗━┛━━━━┗━━┛━━━━━┗┛┗┛━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

def help_menu():
    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 1.Add new item ━━━━━━━━━━━━━━━━━ 7.Sort by category asc ━━━━━━━━━━━━━━━━━━━━━
━━━━ 2.Show all ━━━━━━━━━━━━━━━━━━━━━ 8.Sort by category dsc ━━━━━━━━━━━━━━━━━━━━━
━━━━ 3.Sort by date asc ━━━━━━━━━━━━━ 9.Sort by cost asc ━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 4.Sort by date dsc ━━━━━━━━━━━━ 10.Sort by cost dsc ━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 5.Sort by name asc ━━━━━━━━━━━━ 11.Delete item ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 6.Sort by name dsc ━━━━━━━━━━━━ 12.Delete all data ━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 0.Exit app ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def exit_view():
    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━┏━━━┓━━━━┏━━━┓━━━━┏━━━┓━━━━━━━━┏┓━━┏┓━━━━┏━━━┓━━━━┏┓━┏┓━━━━┏┓━━━━━━━━━━━━━
━━━━━━━━┃┏━┓┃━━━━┃┏━━┛━━━━┃┏━━┛━━━━━━━━┃┗┓┏┛┃━━━━┃┏━┓┃━━━━┃┃━┃┃━━━━┃┃━━━━━━━━━━━━━
━━━━━━━━┃┗━━┓━━━━┃┗━━┓━━━━┃┗━━┓━━━━━━━━┗┓┗┛┏┛━━━━┃┃━┃┃━━━━┃┃━┃┃━━━━┃┃━━━━━━━━━━━━━
━━━━━━━━┗━━┓┃━━━━┃┏━━┛━━━━┃┏━━┛━━━━━━━━━┗┓┏┛━━━━━┃┃━┃┃━━━━┃┃━┃┃━━━━┗┛━━━━━━━━━━━━━
━━━━━━━━┃┗━┛┃━━━━┃┗━━┓━━━━┃┗━━┓━━━━━━━━━━┃┃━━━━━━┃┗━┛┃━━━━┃┗━┛┃━━━━┏┓━━━━━━━━━━━━━
━━━━━━━━┗━━━┛━━━━┗━━━┛━━━━┗━━━┛━━━━━━━━━━┗┛━━━━━━┗━━━┛━━━━┗━━━┛━━━━┗┛━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def categories_help():
    print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ Choose your category ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 1.Food ━━━━━━━━━━━━━━━━━━━━━━━━ 4.Public transport ━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 2.Apparels ━━━━━━━━━━━━━━━━━━━━ 5.Healthcare ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 3.Car maintenance ━━━━━━━━━━━━━ 6.Entertainment ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ 0.Back to main menu ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def data_result_header():
    print("""
━━━━ Below ALL RECORDS listed in chronological order ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━ Num ━━ Category ━━━━━━━━━ Product name ━━━━━━ Cost ━━━━━ Date ━━━━━━━━━━━━━━━""")

def delete_one_header():
    print("""
━━━━ You are going to delete ONE RECORD from the database ━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def delete_all_header():
    print("""
━━━━ You are going to delete ALL RECORDS from the database ━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def go_futher_footer():
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n...press \'Enter\' to go futher')


def clean_terminal():
    if name == 'nt':
        _ = system('cls')  # for windows
    else:
        _ = system('clear')  # for mac and linux(here, os.name is 'posix')
