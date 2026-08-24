members = {
    # "M001": {
    #     "name": "Christopher Simon",
    #     "phone": "07032303470",
    #     "payments": []
    # }
}

def register_member(name, phone):
    member_id = f"M{len(members) + 1:03d}"

    members[member_id] = {
        "name": name,
        "phone": phone,
        "payments": []
    }
    return member_id