# Complete the solve function below.
def solve(s):
    for substring in s.split():
        s = s.replace(substring, substring.capitalize())
    return s

