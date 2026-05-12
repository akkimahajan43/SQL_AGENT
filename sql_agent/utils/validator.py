def validate_query(query):

    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "ALTER",
        "TRUNCATE",
        "INSERT"
    ]

    query_upper = query.upper()

    for word in blocked:

        if word in query_upper:
            return False

    return True