name = "박현선"
target_job = "QA"
study_language = "Python"
experience_year = 1

#print(name)
#print(type(name), end="\n\n")
#print(target_job)
#print(type(target_job), end="\n\n")
#print(study_language)
#print(type(study_language), end="\n\n")
#print(experience_year)
#print(type(experience_year), end="\n\n")

test_id = "TC001"
expected = "PASS"
actual = "FAIL"

result = expected == actual

#print(f"Test ID: {test_id}")
#print(f"Test Result: {result}")

print(f"Test ID: {test_id}")
print(f"Expected: {expected}")
print(f"Actual: {actual}")
#print(f"Test Result: {result}")
if result:
    print("Test Result: PASS")
else:
    print("Test Result: FAIL")

response_time = 850

if response_time <= 1000:
    print("Test Result: PASS")
elif response_time <= 2000:
    print("Test Result: SLOW")
else:
    print("Test Result: FAIL")

status_code = 200

#if status_code == 200 and response_time <= 1000:
    #print("PASS")
#else:
    #print("FAIL")

if status_code == 200:
    if response_time <= 1000:
        print("PASS")
    else:
        print("FAIL - Slow Response")
else:
    print("FAIL - Status Code")

# 다른 사람이 읽었을 때 테스트 의도가 보이는 코드 !


#test_cases = ["TC001", "TC002", "TC003"]

#for test_case in test_cases:
#    print(f"Running: {test_case}")


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
    }
]

for test_case in test_cases:
    result = test_case["expected"] == test_case["actual"]
    if result:
        print(f"{test_case['test_id']}: PASS")
    else:
        print(f"{test_case['test_id']}: FAIL")