import csv
import time
from datetime import datetime
from MoneyFlow_util import *

class Moneyflow:
    menu = {
        1: 'Add new item',
        2: 'Show all',
        3: 'Sort by date asc',
        4: 'Sort by date dsc',
        5: 'Sort by name asc',
        6: 'Sort by name dsc',
        7: 'Sort by category asc',
        8: 'Sort by category dsc',
        9: 'Sort by cost asc',
        10: 'Sort by cost dsc',
        11: 'Delete item',
        12: 'Delete all data',
        0: 'Exit',
    }

    categories = {
        1: 'Food',
        2: 'Apparels',
        3: 'Car maintenance',
        4: 'Public transport',
        5: 'Healthcare',
        6: 'Entertainment'
    }


def add_new_item(user_category):
    record_id = last_row_id() + 1
    f = open('DAT/MoneyFlow.csv', 'a')
    category = Moneyflow.categories[user_category]
    print('Catergory: ' + category)
    product_name = input('Product name: ')
    cost = input('Cost: ')
    fixed_date = datetime.today().strftime('%Y-%m-%d')
    f.write(f'{record_id}, {category}, {product_name}, {cost}, {fixed_date}\n')
    f.close()

def parse_data():
    data = []
    f = open('DAT/MoneyFlow.csv', 'r')
    for line in f.read().split('\n'):
        element = line.strip().split(',')
        final_element = []
        # print(element)
        if len(line) > 0:
            for member in element:
                cleared_member = member.strip()
                final_element.append(cleared_member)
            data.append(final_element)
    # print(data)
    f.close()
    return data

def rewrite_data(new_list):
    f = open('DAT/MoneyFlow.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerows(new_list)
    f.close()

def last_row_id():
    data = parse_data()
    if len(data) == 0:
        return 0
    return int(data[-1][0])  # курсор находится на пустой строке, поэтому data[-2][ ]

def show_all(point):
    if point == 2:
        data = parse_data()
    elif point == 3:
        data = sort_by_date_asc()
    elif point == 4:
        data = sort_by_date_dsc()
    elif point == 5:
        data = sort_by_name_asc()
    elif point == 6:
        data = sort_by_name_dsc()
    elif point == 7:
        data = sort_by_category_asc()
    elif point == 8:
        data = sort_by_category_dsc()
    elif point == 9:
        data = sort_by_cost_asc()
    elif point == 10:
        data = sort_by_cost_dsc()
    tab1 = '    '
    if len(data) > 0:
        for record in data:
            print('{} {:<6} {:<18} {:<19} {:<10} {:<10}'.format(tab1, record[0], record[1], record[2], record[3], record[4]))
    else:
        print('...your table is EMPTY')

# def show_all():
#     data = parse_data()
#     tab1 = '    '
#     if len(data) > 0:
#         for record in data:
#             print('{} {:<6} {:<18} {:<19} {:<10} {:<10}'.format(tab1, record[0], record[1], record[2], record[3], record[4]))
#     else:
#         print('...your table is EMPTY')


def sort_by_date_asc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (p[4]))
    return data_sorted_by_date

# def show_sorted_by_date_asc():
#     data_src = sort_by_date_asc()
#     tab1 = '    '
#     if len(data_src) > 0:
#         for record in data_src:
#             print('{} {:<6} {:<18} {:<19} {:<10} {:<10}'.format(tab1, record[0], record[1], record[2], record[3], record[4]))
#     else:
#         print('...your table is EMPTY')

def sort_by_date_dsc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (p[4]), reverse=True)
    return data_sorted_by_date

# def show_sorted_by_date_dsc():
#     data_src = sort_by_date_dsc()
#     tab1 = '    '
#     if len(data_src) > 0:
#         for record in data_src:
#             print('{} {:<6} {:<18} {:<19} {:<10} {:<10}'.format(tab1, record[0], record[1], record[2], record[3], record[4]))
#     else:
#         print('...your table is EMPTY')

def sort_by_category_asc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (p[1]))
    return data_sorted_by_date

# def show_sorted_by_category_asc():
#     data_src = sort_by_category_asc()
#     tab1 = '    '
#     if len(data_src) > 0:
#         for record in data_src:
#             print('{} {:<6} {:<18} {:<19} {:<10} {:<10}'.format(tab1, record[0], record[1], record[2], record[3], record[4]))
#     else:
#         print('...your table is EMPTY')

def sort_by_category_dsc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (p[1]), reverse=True)
    return data_sorted_by_date

# def show_sorted_by_category_dsc():
#     data_src = sort_by_category_dsc()
#     tab1 = '    '
#     if len(data_src) > 0:
#         for record in data_src:
#             print('{} {:<6} {:<18} {:<19} {:<10} {:<10}'.format(tab1, record[0], record[1], record[2], record[3], record[4]))
#     else:
#         print('...your table is EMPTY')

def sort_by_name_asc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (p[2]))
    return data_sorted_by_date

def sort_by_name_dsc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (p[2]), reverse=True)
    return data_sorted_by_date

def sort_by_cost_asc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (float(p[3])))
    return data_sorted_by_date

def sort_by_cost_dsc():
    data = parse_data()
    data_sorted_by_date = sorted(data, key=lambda p: (float(p[3])), reverse=True)
    return data_sorted_by_date

def delete_item(index):
    date = parse_data()
    buffer = list()
    for record in date:
        if int(record[0]) == index:
            print('WE FOUND this record')
            confirm = input('...are you sure to DELETE this record? [y/n]  ')
            if confirm.lower() == 'y':
                for record in date:
                    if int(record[0]) != index:
                        buffer.append(record)
                rewrite_data(buffer)
                time.sleep(2)
                print('We DELETED the record SUCCESSFULLY, now everything is up to date.')
                time.sleep(2)
                return
            else:
                print('...CHECK YOUR INPUT and try one more time from main menu')
                return
    print('NO DATA found with this record number')


def delete_all_data():
    confirm = input('...are you sure to DELETE ALL DATA? [y/n]  ')
    if confirm.lower() == 'y':
        f = open('DAT/MoneyFlow.csv', 'w+')
        f.truncate(0)
        print('We DELETED ALL RECORDS SUCCESSFULLY, now csv file is empty.')
        f.close()
    else:
        print('...CHECK YOUR INPUT and try one more time from main menu')
        return