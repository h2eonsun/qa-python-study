test_cases = [
    {
        "test_id": "TC001",
        "expected": "PASS",
        "actual": "PASS"
    },
    {
        "test_id": "TC002",
        "expected": "PASS",
        "actual": "FAIL"
    },
    {
        "test_id": "TC003",
        "expected": "FAIL",
        "actual": "FAIL"
    },
    {
        "test_id": "TC004",
        "expected": "PASS",
        "actual": "PASS"
    }
]

def check_result(test_case):
    result = test_case['expected'] == test_case['actual']
    return result

for test_case in test_cases:
    result = check_result(test_case)

    if result:
        print(f"{test_case['test_id']} | Result: PASS")
    else:
        print(f"{test_case['test_id']} | Result: FAIL")