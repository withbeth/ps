
# Constraints
# 1 <= n(num of grades) <= 60
# 0 <= grades[i] <= 100
def gradingStudents(grades):
    return list(map(get_grade, grades))


def get_grade(grade):
    if is_failing_grade(grade):
        return grade
    return round_grade(grade)


def round_grade(origin):
    final = get_final_grade(origin)
    if can_round_grade(origin, final):
        return final
    return origin


def get_final_grade(origin):
    return origin + 5 - (origin % 5)


def can_round_grade(origin, final):
    return final - origin < 3


def is_failing_grade(origin):
    return origin < 38
