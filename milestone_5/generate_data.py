from faker import Faker
import csv

def generate_data(n: int):
    data_list = []
    
    def create_person():
        from faker.providers import DynamicProvider

        departments_provider = DynamicProvider(
            provider_name="departments_provider",
            elements=['finance', 'marketing', 'operations management', 'human resources', 'information technology'],
        )
        fake = Faker()
        fake.add_provider(departments_provider)
        dict_person = {"Name": fake.name(),
                    "birth_date": fake.date_of_birth(minimum_age = 23, maximum_age = 55).strftime('%Y-%m-%d'),
                    "department": fake.departments_provider(),
                    "hiring_date": fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d')}
        return dict_person
    
    with open('database.csv', 'w+') as file:
        file.write('Name,birth_date,department,hiring_date\n')

    for i in range(n):
        create_person()
        with open('database.csv', 'a') as file:
            fieldnames = ['Name', 'birth_date', 'department', 'hiring_date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writerow(create_person())

        data_list.append(create_person())
    return data_list

# n = int(input("Enter number of people: "))
print(generate_data(25))