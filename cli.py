from db import init_db, add_entry
import json
from datetime import datetime


def main():
    init_db()  # Initialize database

    print("=== Daily Progress Tracker ===")
    date = datetime.now().strftime("%Y-%m-%d")

    # Collect data
    fields = {
        "python": {
            "time_spent": int(input("Python mins spent: ") or "0"),
            "topics": input("Topics (comma-separated): ").split(","),
            "self_rating": int(input("Self-rating (1-10): "))
        }
    }

    # Save to DB
    add_entry(date, json.dumps(fields))
    print(f"✅ Entry saved for {date}!")


if __name__ == "__main__":
    main()