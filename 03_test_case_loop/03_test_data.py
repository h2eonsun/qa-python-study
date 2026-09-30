test_cases = [
    {
        "test_id" : "TC001",
        "title" : "Login Success",
        "priority" : "High",
        "expected" : "PASS",
        "actual" : "PASS"
    },
    {
        "test_id" : "TC002",
        "title" : "Login Failure",
        "priority" : "High",
        "expected" : "PASS",
        "actual" : "FAIL"
    },
    {
        "test_id" : "TC003",
        "title" : "Logout Success",
        "priority" : "Medium",
        "expected" : "FAIL",
        "actual" : "FAIL"
    },
    {
        "test_id" : "TC004",
        "title" : "Password Reset",
        "priority" : "Low",
        "expected" : "PASS",
        "actual" : "PASS"
    }
]

def check_result(test_case):
    result = test_case["expected"] == test_case["actual"]
    return result

for test_case in test_cases:
    if check_result(test_case):
        print(f"{test_case['test_id']} | {test_case['title']} | Priority: {test_case['priority']} | Result: PASS")
    else:
        print(f"{test_case['test_id']} | {test_case['title']} | Priority: {test_case['priority']} | Result: FAIL")


for test_case in test_cases:
    if "test_id" in test_case and "expected" in test_case and "actual" in test_case:
        print(f"{test_case['test_id']}: Data OK")
    else:
        print("Invalid Test Data")

test_cnt = 0

for test_case in test_cases:
    test_cnt += 1
    if test_cnt == 1:
        print(test_case["test_id"])
        print(test_case["title"])
        print(test_case["priority"])
        print()
    elif test_cnt == 3:
        print(test_case["actual"])
        print()
    else:
        continue

test_cnt -= 1
print(f"Total: {test_cnt}")

