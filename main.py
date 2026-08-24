from estate_tracker.storage import load_data, save_data
import estate_tracker.members as member_manager
from estate_tracker.payments import (record_payment, get_payment_history, check_dues_status)
from estate_tracker.logger import log_event

members = load_data()

while True:
    print("\n=== ESTATE UNION DUES TRACKER ===")
    print("1. Register member")
    print("2. Record payment")
    print("3. View members")
    print("4. Check dues status")
    print("5. View payment history")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter member name: ")
        phone = input("Enter phone number: ")

        members_id = member_manager.register_member(name, phone)

        save_data(member_manager.members)
        members = member_manager.members

        log_event(f"Registered member: {members_id} - {name}")

        print(f"Member registered successfully. ID: {members_id}")
