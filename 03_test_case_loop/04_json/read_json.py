from pathlib import Path
import json

file_path = Path(__file__).parent / "test_cases.json"

with open(file_path, "r", encoding="utf-8") as file:
    test_cases = json.load(file)

total_cases = len(test_cases)

print(f"Total Test Cases: {total_cases}\n")

for test_case in test_cases:
    print(f"{test_case['test_id']} | {test_case['title']} | Priority: {test_case['priority']}")


print()

def check_result(test_case):
    result = test_case["expected"] == test_case["actual"]
    return result

total_cnt = 0
total_pass = 0
total_fail = 0

for test_case in test_cases:
    total_cnt += 1
    result = check_result(test_case)

    if result:
        total_pass += 1
        print(f"{test_case['test_id']} | Result: PASS")
        
    else:
        total_fail += 1
        print(f"{test_case['test_id']} | Result: FAIL")


print(f"\nTotal Test Cases: {total_cnt}")
print(f"Total Passed: {total_pass}")
print(f"Total Failed: {total_fail}")
