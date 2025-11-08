def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    result = []
    for index, score in enumerate(student_scores):
        result.append(f'{index + 1}. {student_names[index]}: {score}')

    return result


#p = student_ranking(['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose'],[100, 98, 92, 86, 70, 68, 67, 60])
#print(p)

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for info in student_info:
        if info[1] == 100:
            return info
    return []

p = perfect_score([['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]])
print(p)
p = perfect_score([])
print(p)
p = perfect_score([['Rui', 60], ['Joci', 58], ['Sara', 91], ['Kora', 93], ['Alex', 42],['Jan', 81], ['Lilliana', 40], ['John', 60], ['Bern', 28], ['Vlad', 55]])
print(p)
p = perfect_score([['Yoshi', 52], ['Jan', 86], ['Raiana', 100], ['Betty', 60],['Joci', 100], ['Kora', 81], ['Bern', 41], ['Rose', 94]])
print(p)