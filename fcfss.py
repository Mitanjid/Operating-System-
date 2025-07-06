# FCFS Scheduling for given input

processes = [
    ["P1", 0, 2],
    ["P2", 1, 2],
    ["P3", 5, 3],
    ["P4", 6, 4]
]

# Sort by arrival time
processes.sort(key=lambda x: x[1])

completion_time = []
turnaround_time = []
waiting_time = []

time = 0

for p in processes:
    name, arrival, burst = p

    if time < arrival:
        time = arrival  # CPU waits for the process to arrive

    ct = time + burst
    completion_time.append(ct)

    tat = ct - arrival
    turnaround_time.append(tat)

    wt = tat - burst
    waiting_time.append(wt)

    time = ct  # update current time

# Display the results
print("Process | Arrival | Burst | Completion | Turn Around | Waiting")
for i in range(len(processes)):
    p = processes[i]
    print("  {:>5} |   {:>6} | {:>5} |     {:>8} |     {:>9} |   {:>6}"
          .format(p[0], p[1], p[2], completion_time[i], turnaround_time[i], waiting_time[i]))

avg_wt = sum(waiting_time) / len(waiting_time)
print("\nAverage Waiting Time: {:.2f}".format(avg_wt))
