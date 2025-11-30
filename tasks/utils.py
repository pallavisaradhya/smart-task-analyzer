from datetime import date

def calculate_priority(task):
    """
    Calculate a priority score for a task based on:
    - Urgency (due date)
    - Importance
    - Effort (less effort = higher score)
    - Dependencies (tasks blocking others)
    """
    score = 0

    # Urgency
    days_left = (task.due_date - date.today()).days
    if days_left < 0:
        urgency_score = 10  # past due
    else:
        urgency_score = max(0, 10 - days_left / 2)
    score += urgency_score * 0.4

    # Importance
    score += task.importance * 0.3

    # Effort: less effort = higher score
    score += max(0, 10 - task.estimated_hours) * 0.2

    # Dependencies: tasks that block others
    num_dependents = task.task_set.count()
    score += num_dependents * 0.1

    return round(score, 2)