def build_rating(results):
    """Sort students by score in descending order."""
    return sorted(results, key=lambda student: student[1], reverse=True)


def calculate_success_rate(results):
    """Calculate percentage of students who passed the test."""
    if not results:
        return 0

    passed_students = 0

    for name, score in results:
        if score >= 60:
            passed_students += 1

    return passed_students / len(results) * 100


def calculate_average_score(results):
    """Calculate average test score."""
    if not results:
        return 0

    total = 0

    for name, score in results:
        total += score

    return total / len(results)
