from faker import Faker
import pandas as pd

fake = Faker()
count = 0

firstName = []
lastName = []
country = []
job = []

while count < 1000:
    firstName.append(fake.first_name())
    lastName.append(fake.last_name())
    country.append(fake.country())
    job.append(fake.job())

    count += 1

data = {'First Name': firstName,
        'Last Name': lastName,
        'Country': country,
        'Job': job,
        }

df = pd.DataFrame(data)

df.to_excel('./data.xlsx')
