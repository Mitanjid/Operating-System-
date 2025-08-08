n = int(input("Enter number of processes: "))
processes = []

# Input process data: PID, AT, BT, CT, TAT, WT
for i in range(n):
    at = int(input(f"Enter arrival time of P{i+1}: "))
    bt = int(input(f"Enter burst time of P{i+1}: "))
    processes.append([i+1, at, bt, 0, 0, 0])  # PID, AT, BT, CT, TAT, WT

time_quantum = int(input("Enter time quantum: "))

queue = []
time = 0
remain_bt = [p[2] for p in processes]  # Remaining burst time
visited = [False] * n
completed = 0

while completed < n:
    for i in range(n):
        if processes[i][1] <= time and remain_bt[i] > 0 and not visited[i]:
            queue.append(i)
            visited[i] = True

    if queue:
        idx = queue.pop(0)
        exec_time = min(time_quantum, remain_bt[idx])
        time += exec_time
        remain_bt[idx] -= exec_time

        # Enqueue new arrivals during execution
        for i in range(n):
            if processes[i][1] <= time and remain_bt[i] > 0 and not visited[i]:
                queue.append(i)
                visited[i] = True

        if remain_bt[idx] > 0:
            queue.append(idx)
        else:
            processes[idx][3] = time  # CT
            processes[idx][4] = processes[idx][3] - processes[idx][1]  # TAT
            processes[idx][5] = processes[idx][4] - processes[idx][2]  # WT
            completed += 1
    else:
        time += 1  # If no process in queue, move time forward

# Print results
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")

# Optional: Calculate average TAT and WT
avg_tat = sum(p[4] for p in processes) / n
avg_wt = sum(p[5] for p in processes) / n
print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
