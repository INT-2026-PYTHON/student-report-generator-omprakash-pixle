"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass
    student_totals={}
    student_counts={}
    for record in records:
        name=record.get("name")
        score=record.get("score",0)
        if name:
            student_totals[name]=student_totals.get(name,0)+score
            student_counts[name]=student_counts.get(name,0)+1
        averages={}
        for name,total in student_totals.items():
            averages[name]=round(total/student_counts[name],2)
        return averages
def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass
    subjects=set()
    for record in records:
        subject=record.get("subject")
        if subject:
            subjects.add(subject)
    return subjects   
def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass
    averages=average_per_student(records)
    if not averages:
        return("",0.0)
    top_students=max(averages,key=averages.get)
    return(top_students,averages[top_students])
def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass
    passed=[]
    for student in records:
        grades=student["grades"]
        if grades:
            avg=sum(grades)/len(grades)
            if avg>=threshold:
                passed.append(student["name"])
    return sorted(passed)