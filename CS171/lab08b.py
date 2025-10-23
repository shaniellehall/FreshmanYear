def loadScores(filename):
    scores = {}
    try:
        file = open(filename, "r")
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        return None
    
    for line in data:
        parts = line.strip().split(",")
        if len(parts) != 3:
            continue
        studentId, assignment, grade = parts
        grade = float(grade)
        if studentId not in scores:
            scores[studentId] = {} 
        if assignment not in scores[studentId] or grade > scores[studentId][assignment]:
            scores[studentId][assignment] = grade
    return scores

def averageScores(scores):
    averages = {}
    
    for student, assignments in scores.items():
        grades = list(assignments.values())
        if len(grades) > 1:
            grades.remove(min(grades))
        averages[student] = sum(grades) / len(grades)
    return averages
  
if __name__ == "__main__":
    loadedScores = loadScores("auto.txt")
    print(loadedScores)
    if loadedScores is not None:
        print(averageScores(loadedScores))