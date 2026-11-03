# Python 기본 문법 및 QA 테스트 결과 비교 연습

name = "QA Learner"
target_job = "QA"
study_language = "Python"
experience_year = 1

test_id = "TC001"
expected = "PASS"
actual = "FAIL"

result = expected == actual

print(f"Test ID: {test_id}")
print(f"Expected: {expected}")
print(f"Actual: {actual}")

if result:
    print("Test Result: PASS")
else:
    print("Test Result: FAIL")