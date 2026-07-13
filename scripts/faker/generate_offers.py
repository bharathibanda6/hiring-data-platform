
from faker import Faker
import pandas as pd
import random

fake = Faker()

# Read CSVs

interviews_df = pd.read_csv("data/interview.csv")

offers = []

offer_id = 1

# Keep only Selected interviews

selected_interviews = interviews_df[
    interviews_df["interview_status"] == "Selected"
]

# Generate Offers

for _, interview in selected_interviews.iterrows():

    # Around 80% receive offers
    if random.random() <= 0.80:

        offer_sent = fake.date_between(
            start_date=pd.to_datetime(
                interview["interview_date"]
            ).date(),
            end_date="today"
        )

        offer_status = random.choice([
            "Accepted",
            "Rejected",
            "Pending"
        ])

        # Pending offers don't have a response yet
        if offer_status == "Pending":

            response_date = None

        else:

            response_date = fake.date_between(
                start_date=offer_sent,
                end_date="+30d"
            )

        offer = {

            "offer_id": offer_id,

            "application_id":
                interview["application_id"],

            "offered_ctc":
                random.randint(
                    70000,
                    180000
                ),

            "offer_sent_date":
                offer_sent,

            "offer_response_date":
                response_date,

            "offer_status":
                offer_status

        }

        offers.append(offer)

        offer_id += 1

# Save CSV

offers_df = pd.DataFrame(offers)

offers_df.to_csv(
    "data/offer.csv",
    index=False
)

print("Offer CSV Generated Successfully!")