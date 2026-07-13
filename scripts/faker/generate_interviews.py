
from faker import Faker
import pandas as pd
import random

fake = Faker()
# Read Applications

applications_df = pd.read_csv("data/ats_application.csv")

# Initialize

interviews = []

interview_id = 1

rounds = [
    "HR",
    "Technical Round 1",
    "Technical Round 2",
    "Hiring Manager"
]

statuses = [
    "Completed",
    "Rejected",
    "Selected",
    "No Show"
]

# Generate Interviews

for _, application in applications_df.iterrows():

    # Around 35% of applications receive interviews
    if random.random() <= 0.35:

        interview_status = random.choice(statuses)

        interview_date = fake.date_time_between(
            start_date=pd.to_datetime(
                application["application_date"]
            ),
            end_date="now"
        )

        # Rating only if interview happened
        if interview_status == "No Show":

            rating = None
            feedback = None

        else:

            rating = round(
                random.uniform(1.0,5.0),
                1
            )

            feedback = fake.sentence(
                nb_words=12
            )

        interview = {

            "interview_id": interview_id,

            "application_id":
                application["application_id"],

            "interview_round":
                random.choice(rounds),

            "interview_status":
                interview_status,

            "interview_date":
                interview_date,

            "rating":
                rating,

            "feedback":
                feedback
        }

        interviews.append(interview)

        interview_id += 1

# Save CSV

interviews_df = pd.DataFrame(interviews)

interviews_df.to_csv(
    "data/interview.csv",
    index=False
)

print("Interview CSV Generated Successfully!")