from io_utils import read_test_results, save_report
from analysis import build_rating, calculate_success_rate, calculate_average_score


INPUT_FILE = "data/input.txt"
OUTPUT_FILE = "data/output.txt"


def main():
    results = read_test_results(INPUT_FILE)

    rating = build_rating(results)
    success_rate = calculate_success_rate(results)
    average_score = calculate_average_score(results)

    report = "Analysis of test results\n"
    report += "-" * 30 + "\n"
    report += "Student rating:\n"

    for position, student in enumerate(rating, start=1):
        name, score = student
        report += f"{position}. {name} - {score} points\n"

    report += "\n"
    report += f"Average score: {average_score:.2f}\n"
    report += f"Success rate: {success_rate:.2f}%\n"

    print(report)
    save_report(OUTPUT_FILE, report)


if __name__ == "__main__":
    main()
