print("PRIORITY SCHEDULING (Lower value = Higher priority)")

# Take input
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    pid = "P" + str(i + 1)
    arrival = int(input(f"Enter arrival time of process {pid}: "))
    burst = int(input(f"Enter burst time of process {pid}: "))
    priority = int(input(f"Enter priority of process {pid} (1=high): "))
    processes.append([pid, arrival, burst, priority])

# step 1
processes.sort(key=lambda x: x[1])
# step 2
current_time = 0
remaining_processes = processes.copy()
completed = []
ET, WT, TAT = {}, {}, {}

while remaining_processes:
    
    available_processes = [p for p in remaining_processes if p[1] <= current_time]

    if available_processes:
        # Select process with highest priority (lowest priority value)
        available_processes.sort(key=lambda x: x[3])
        process = available_processes.pop(0)
        pid, arrival, burst, priority = process

        # Compute exit time, TAT, WT
        exit_time = current_time + burst
        tat = exit_time - arrival  # Turnaround Time
        wt = tat - burst           # Waiting Time

        completed.append((pid, arrival, burst, priority, exit_time, tat, wt))

        current_time = exit_time
        remaining_processes.remove(process)
    else:
        current_time += 1  # CPU idle

avg_tat = sum(p[5] for p in completed) / n
avg_wt = sum(p[6] for p in completed) / n

# Print final results
print("\nProcess\tAT\tBT\tP\tCT\tTAT\tWT")
for p in completed:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}\t{p[6]}")

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
