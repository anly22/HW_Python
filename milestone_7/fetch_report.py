import requests
import json
import argparse

SERVER_URL = 'http://127.0.0.1:5000'

parser = argparse.ArgumentParser(description = "Report for {department} department for {month} fetched.")
parser.add_argument("month", type = str, help = "Month to report by (for example: april)")
parser.add_argument("department", type = str, help = "Department (for example: marketing)")
args = parser.parse_args()

month = args.month
department = args.department

def birthdays(month, department):
    response = requests.get(f'{SERVER_URL}/birthdays', params={'month': month, 'department': department})
    if response.status_code == 200:
        births_by_dep = response.json()
        print(f'Report about birthdays for {department} department for {month} fetched.')
        print(f"Total: {births_by_dep['total']}\nEmployees:\n - {births_by_dep['employees']['birthday']}, {births_by_dep['employees']['name']}")
    else:
        print(f"No birthdays in {month} in {department} department")


def anniversaries(month, department):
    response = requests.get(f'{SERVER_URL}/anniversaries', params={'month': month, 'department': department})
    if response.status_code == 200:
        anniversaries_by_dep = response.json()
        print(f'Report about anniversaries for {department} department for {month} fetched.')
        print(f"Total: {anniversaries_by_dep['total']}\nEmployees:\n - {anniversaries_by_dep['employees']['anniversary']}, {anniversaries_by_dep['employees']['name']}")
    else:
        print(f"No anniversaries in {month} in {department} department")
  

birthdays(month, department)
anniversaries(month, department)

# birthdays('july', 'finance') 
# anniversaries('july', 'finance')

# python fetch_report.py october QA #july finance