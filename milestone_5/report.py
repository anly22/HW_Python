from typing import List
import csv
import argparse
 
def report(filename: str, month: str):

    data = []
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter=",")
        
        headers = next(reader)
        for col in reader:
            data.append(col)
                
    birth_by_dep = {} 
    hiring_by_dep = {}

    def month_to_num(monthname: str):
        MonthNums = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
        month_num = MonthNums[monthname]

        return month_num


    dict_by_key = {}

    def count_by_id(di, key_date, key_id):
        date = (di[key_date])
        m_n = month_to_num(month)
        if int(date[5:7]) == m_n:
            if di[key_id] in dict_by_key:
                dict_by_key[di[key_id]] += 1
            else:
                dict_by_key[di[key_id]] = 1
        return dict_by_key

    def total_count(li: List[int]) -> int:
        total_count = 0
        for i in li:
            total_count += i
        return total_count

    print(f'Report for {month} generated')
    print('\nBirthdays: \nBy department:')
    for person in data:
        birth_by_dep = count_by_id(person, 'birth_date', 'department')

    for key, value in birth_by_dep.items():
        print(f"- {key}: {value}")

    total_for_birth = total_count(list(birth_by_dep.values()))
    print('Total: ', total_for_birth)

    print('\nAnniversaries: \nBy department:')
    for person in data:
        hiring_by_dep = count_by_id(person, 'hiring_date', 'department')

    for key, value in hiring_by_dep.items():
        print(f"- {key}: {value}")

    total_for_anniversaries = total_count(list(hiring_by_dep.values()))
    print('Total: ', total_for_anniversaries)

parser = argparse.ArgumentParser(description = "Generating of report by the month")
parser.add_argument("filename", type = str, help = "Name of file with database (for example: database.csv)")
parser.add_argument("month", type = str, help = "Month to report by (for example: april)")
args = parser.parse_args()

filename = args.filename
month = args.month

report(filename, month)