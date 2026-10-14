def department_summary(employees: list):
    """Return headcount and average salary per department."""
    totals = {}
    for employee in employees:
        department = employee["department"]
        data = totals.get(department, {"headcount": 0, "total_salary": 0.0})
        data["headcount"] += 1
        data["total_salary"] += employee["salary"]
        totals[department] = data

    summary = {}
    for department, data in totals.items():
        summary[department] = {"headcount": data["headcount"], "average_salary": data["total_salary"] / data["headcount"]}

    return summary
    
