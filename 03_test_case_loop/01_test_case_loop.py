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
count = 0
pass_count = 0
fail_count = 0

for test_case in test_cases:
    result = test_case["expected"] == test_case["actual"]
    count += 1
    if result:
        pass_count += 1
        print(f"{test_case['test_id']} | Expected: {test_case['expected']} | Actual: {test_case['actual']} | Result: PASS")
    else:
        fail_count += 1
        print(f"{test_case['test_id']} | Expected: {test_case['expected']} | Actual: {test_case['actual']} | Result: FAIL")

print(f"\n총 테스트: {count}")
print(f"Pass: {pass_count}")
print(f"Fail: {fail_count}")

#def run_test(test_case):
#    result = test_case["expected"] == test_case["actual"]

#    if result:
#        print("PASS")
#    else:
#        print("FAIL")

#run_test(test_cases[0])

def check_result(test_case):
    result = test_case["expected"] == test_case["actual"]

    return result

for test_case in test_cases:
    result = check_result(test_case)

    if result:
        print("PASS")
    else:
        print("FAIL")