def get_average(marks):
    if not marks:
        return 0
    return int(sum(marks) / len(marks))