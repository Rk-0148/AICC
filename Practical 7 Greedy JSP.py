def schedule_jobs(jobs):
    # Sort the jobs in decreasing order of their profits
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    result = [False] * n  # Result array to store the scheduled jobs
    slots = [False] * n  # Array to keep track of available time slots

    for i in range(n):
        # Find a suitable time slot for the current job
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if not slots[j]:
                result[j] = jobs[i][0]
                slots[j] = True
                break

    # Print the scheduled jobs
    print("Scheduled Jobs:")
    for i in range(n):
        if result[i]:
            print(result[i])

# Example usage
jobs = [
    ('Job1', 2, 100),  # (Job Name, Deadline, Profit)
    ('Job2', 1, 50),
    ('Job3', 2, 10),
    ('Job4', 1, 20),
    ('Job5', 3, 30)
]

schedule_jobs(jobs)
