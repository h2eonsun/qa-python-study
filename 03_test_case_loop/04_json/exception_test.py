from pathlib import Path
import json
import sys

file_path = Path(__file__).parent / "test_cases.json"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        test_cases = json.load(file)
except FileNotFoundError:
    print("Test data file not found")
    sys.exit(1)
except json.JSONDecodeError:
    print("Invalid JSON format in test data file")
    sys.exit(1)


def check_result(test_case):
    result = test_case["expected"] == test_case["actual"]
    return result


for test_case in test_cases:
    try:
        if check_result(test_case):
            print(f"{test_case['test_id']} | PASS")
        else:
            print(f"{test_case['test_id']} | FAIL")

    except KeyError as e:
        missing_key = e.args[0]

        if missing_key == "test_id":
            print(f"Missing 'test_id' in test case: {test_case}")
        else:
            print(f"{test_case['test_id']} | TEST DATA ERROR")
