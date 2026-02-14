def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),   # ✅ এখানে ঠিক করা হয়েছে
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
