name = "박현선"
target_job = "QA"
study_language = "Python"
experience_year = 1

print(name)
print(type(name), end="\n\n")
print(target_job)
print(type(target_job), end="\n\n")
print(study_language)
print(type(study_language), end="\n\n")
print(experience_year)
print(type(experience_year), end="\n\n")

Test_ID = "TC001"
Expected = "PASS"
Actual = "FAIL"

result = Expected == Actual
print(f"Test Result: {result}")