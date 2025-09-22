class CelerySettings:
    task_serializer = "json"
    result_serializer = "json"
    accept_content = ["json"]
    task_routes = {
        "pi.calculate": {"queue": "pi"},
    }
    result_expires = 3600