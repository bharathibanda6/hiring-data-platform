from faker import Faker
import pandas as pd
import random
fake = Faker()

# Read existing CSVs

jobs_df = pd.read_csv("data/job_posting.csv")
candidates_df = pd.read_csv("data/candidate.csv")

# Initialize variables

applications = []

application_id = 1

# Prevent the same candidate applying twice to the same job
used_applications = set()

# Loop through every Job

for _, job in jobs_df.iterrows():

    job_id = job["job_id"]

    # Each job receives a random number of applications
    num_applications = random.randint(20, 80)

    # Job posted date
    posted_date = pd.to_datetime(job["job_posted_date"])

    # Create Applications
    for _ in range(num_applications):

        # Pick one random candidate
        candidate = candidates_df.sample(1).iloc[0]

        candidate_id = candidate["candidate_id"]

        # Skip duplicate applications
        if (candidate_id, job_id) in used_applications:
            continue

        used_applications.add((candidate_id, job_id))

        application = {
            "application_id": application_id,
            "job_id": job_id,
            "candidate_id": candidate_id,

            # Candidate can only apply after job is posted
            "application_date": fake.date_between(
                start_date=posted_date.date(),
                end_date="today"
            ),

            "application_status": random.choice([
                "Applied",
                "Under Review",
                "Interview",
                "Rejected"
            ]),

            "application_source": random.choice([
                "LinkedIn",
                "Indeed",
                "Company Website",
                "Referral",
                "Dice"
            ])
        }

        applications.append(application)

        application_id += 1
 
# Save CSV
applications_df = pd.DataFrame(applications)

applications_df.to_csv(
    "data/ats_application.csv",
    index=False
)
print(applications_df["candidate_id"].nunique())
print("ATS Application CSV generated successfully!")