from faker import Faker
import pandas as pd
import random

fake = Faker()

# Read CSV

offers_df = pd.read_csv("data/offer.csv")

# Keep only Accepted Offers

accepted_offers = offers_df[
    offers_df["offer_status"] == "Accepted"
]

# Initialize

employees = []

departments = [
    "Engineering",
    "Data Engineering",
    "Quality Assurance",
    "Cloud",
    "Business Intelligence"
]

designations = [
    "Data Engineer I",
    "QA Engineer",
    "Cloud Engineer",
    "BI Developer",
    "Software Engineer"
]

employee_number = 10001

# Generate Employees

for _, offer in accepted_offers.iterrows():

    joining_date = fake.date_between(
        start_date=pd.to_datetime(
            offer["offer_response_date"]
        ).date(),
        end_date="+30d"
    )

    employee = {

        "employee_id":
            f"EMP{employee_number}",

        "application_id":
            offer["application_id"],

        "joining_date":
            joining_date,

        "manager_id":
            f"EMP{random.randint(10001,10050)}",

        "department":
            random.choice(departments),

        "designation":
            random.choice(designations)

    }

    employees.append(employee)

    employee_number += 1

# Save CSV

employees_df = pd.DataFrame(employees)

employees_df.to_csv(
    "data/hrms.csv",
    index=False
)

print("HRMS Employee CSV Generated Successfully!")
