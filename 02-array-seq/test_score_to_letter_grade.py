import bisect

breakpoints = [60, 70, 80, 90]
grades = 'FDCBA'

def grade(score):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == "__main__":
    scores = [55, 60, 65, 70, 75, 80, 85, 90, 95]
    print(scores)
    print([grade(score) for score in scores])