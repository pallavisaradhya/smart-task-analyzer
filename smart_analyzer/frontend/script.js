document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const taskInput = document.getElementById("taskInput").value;
    let tasks;

    // Validate JSON
    try {
        tasks = JSON.parse(taskInput);
    } catch {
        alert("Invalid JSON format!");
        return;
    }

    // Send to backend
    try {
        const response = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(tasks)
        });

        if (!response.ok) {
            const data = await response.json();
            throw new Error(JSON.stringify(data));
        }

        const result = await response.json();
        displayTasks(result);
    } catch (error) {
        alert("Failed to fetch tasks from server: " + error);
    }
});

function displayTasks(tasks) {
    const output = document.getElementById("output");
    output.innerHTML = "";

    tasks.forEach(task => {
        const div = document.createElement("div");
        div.innerHTML = `
            <strong>${task.title}</strong> - Priority: ${task.priority_score} <br>
            Due: ${task.due_date}, Effort: ${task.estimated_hours}, Importance: ${task.importance} <br>
        `;
        output.appendChild(div);
    });
}