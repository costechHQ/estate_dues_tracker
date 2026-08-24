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

    elif choice == "2":
        members_id = input("Enter member ID: ")
        month = input("Enter payment month: ")
        amount = input("Enter amount: ")

        try:
            amount = float(amount)
        except ValueError:
            print("Amount must be a number.")
            continue

        success = record_payment(
            members,
            members_id,
            month,
            amount
        )

        if success:
            save_data(members)
            log_event(
                f"Payment recorded: {members_id} - {month} - NGN{amount}"
            )
            print("Payment recorded successfully.")
        else:
            print("Member ID not found.")

    elif choice == "3":
        if not members:
            print("No members registered.")
        else:
            for member_id, member in members.items():
                print(
                    f"{members_id} - "
                    f"{member['name']} - "
                    f"{member['phone']}"
                )

    elif choice == "4":
        results = check_dues_status(members)

        if not results:
            print("No members registered.")
        else:
            for member_id, status in results.items():
                print(
                    f"{members_id} - "
                    f"{members[member_id]['name']}"
                    f"{status}"
                )

    elif choice == "5":
        member_id = input("Enter member ID: ")

        history = get_payment_history(members, member_id)

        if history is None:
            print("Member ID not found.")
        elif not history:
            print("This member has no payment history.")
        else:
            print(f"\nPayment history for {members[member_id]['name']}")

            for payment in history:
                print(
                    f"Month: {payment['month']} | "
                    f"Amount: NGN{payment['amount']}"
                )

    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-6.")