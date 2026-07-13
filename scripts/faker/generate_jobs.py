print("Program Started")

from faker import Faker
import pandas as pd
import random
fake = Faker()
job_titles = [
    "Data Engineer",
    "Data Analyst",
    "QA Engineer",
    "ML Engineer",
    "DevOps Engineer",
    "Cloud Engineer",
    "Business Analyst",
    "Data Architect",
    "Software Engineer",
    "BI Developer"
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

NUM_JOBS = 100
jobs = []
for job_id in range(1, NUM_JOBS+1):
  job = {
        "job_id": job_id,
        "job_title": random.choice(job_titles),
        "job_description": fake.paragraph(nb_sentences=3),
        "job_location": random.choice(locations),
        "minimum_experience": random.randint(0, 3),
        "maximum_experience": random.randint(4, 8),
        "required_education": random.choice(education_levels),
        "required_skills": ", ".join(random.sample(skills_pool, 4)),
        "job_posted_date": fake.date_between(start_date="-60d", end_date='today'),
        "job_closed_date": None,
        "allocated_salary": random.randint(70000, 180000)
    }
  jobs.append(job)
jobs_df = pd.DataFrame(jobs)
jobs_df.to_csv("data/job_posting.csv", index=False)
print("Job Posting CSV generated successfully!")