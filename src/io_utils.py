def read_test_results(file_path):
    """Read student test results from a file."""
    results = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) == 2:
                name = parts[0]
                score = int(parts[1])
                results.append((name, score))

    return results


def save_report(file_path, text):
    """Save analysis report to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
