def record_payment(members, members_id, month, amount):
    if members_id not in members:
        return False

    payment = {
        "month": month,
        "amount": amount
    }

    members[members_id]["payements"].append(payment)
    return True

def get_payment_history(members, member_id):
    if member_id not in members:
        return None

    return members[member_id]["payments"]

from datetime import datetime

def check_dues_status(members):
    current_month = datetime.now().strftime("%B")

    results = {}

    for member_id, member in members.items():
        paid = any(
            payment["month"].lower() == current_month.lower()
            for payment in member["payments"]
        )

        results[member_id] = "Paid" if paid else "Not Paid"
        return results