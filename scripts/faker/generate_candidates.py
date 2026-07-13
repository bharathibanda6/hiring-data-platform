from faker import Faker
import pandas as pd
import random
fake = Faker()
companies = [
    "Amazon",
    "Microsoft",
    "Google",
    "Meta",
    "Apple",
    "Oracle",
    "IBM",
    "Accenture",
    "Infosys",
    "TCS",
    "Wipro",
    "Deloitte",
    "Cognizant",
    "Capgemini",
    "EY"
]
candidate_job_titles = [
    "Data Engineer",
    "Data Analyst",
    "Software Engineer",
    "Cloud Engineer",
    "QA Engineer",
    "BI Developer",
    "DevOps Engineer",
    "ETL Developer",
    "Database Developer",
    "ML Engineer"
]
locations = [
    "Austin",
    "Dallas",
    "Houston",
    "Seattle",
    "New York",
    "Chicago"
]
education_levels = [
    "Bachelor's",
    "Master's",
    "PhD"
]
visa_statuses = [
    "US Citizen",
    "Green Card",
    "H1B",
    "OPT",
    "CPT"
]
skills_pool = [
    "Python",
    "SQL",
    "AWS",
    "Azure",
    "Spark",
    "Kafka",
    "Airflow",
    "Snowflake",
    "Databricks",
    "Power BI",
    "Terraform",
    "Docker",
    "Kubernetes",
    "Git"
]
NUM_CANDIDATES = 1000
candidates = []
for candidate_id in range(1, NUM_CANDIDATES + 1):
    candidate = {
        "candidate_id": candidate_id,
        "first_name": fake.first_name(),
        "middle_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email_id": fake.email(),
        "phone": fake.phone_number(),
        "current_location": random.choice(locations),
        "highest_education": random.choice(education_levels),
        "current_company": random.choice(companies),
        "current_job_title": random.choice(candidate_job_titles),
        "years_of_experience": round(random.uniform(0, 12), 1),
        "visa_status": random.choice(visa_statuses),
        "willing_to_relocate": random.choice([True, False]),
        "skills": ", ".join(random.sample(skills_pool, random.randint(3, 6)))
    }
    candidates.append(candidate)

candidates_df = pd.DataFrame(candidates)
candidates_df.to_csv("data/candidate.csv", index=False)
print(candidates_df.shape)
print("Candidate CSV generated successfully!")
