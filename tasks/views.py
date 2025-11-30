from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .utils import calculate_priority
from datetime import date

@api_view(['POST'])
def analyze_tasks(request):
    """
    Accept list of tasks, calculate priority, return sorted list
    """
    serializer = TaskSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    result = []

    for item in serializer.validated_data:
        dependencies_data = item.pop('dependencies', [])  # remove dependencies temporarily
        task = Task.objects.create(**item)  # create task first
        if dependencies_data:
            task.dependencies.set(dependencies_data)  # set ManyToManyField properly
        score = calculate_priority(task)
        result.append({**TaskSerializer(task).data, "priority_score": score})

    # Sort descending by priority
    result.sort(key=lambda x: x['priority_score'], reverse=True)
    return Response(result)


@api_view(['GET'])
def suggest_tasks(request):
    """
    Return top 3 tasks for today
    """
    tasks = Task.objects.all()
    scored_tasks = []
    for task in tasks:
        score = calculate_priority(task)
        scored_tasks.append((task, score))

    scored_tasks.sort(key=lambda x: x[1], reverse=True)
    top_tasks = scored_tasks[:3]

    suggestions = []
    for task, score in top_tasks:
        days_left = (task.due_date - date.today()).days if task.due_date else "No due date"
        suggestions.append({
            "title": task.title,
            "priority_score": score,
            "reason": f"Importance: {task.importance}, Due in {days_left} days"
        })

    return Response(suggestions)