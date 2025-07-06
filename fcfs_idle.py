print("FIRST COME FIRST SERVE SCHEDULING")
n = int(input("Enter number of processes: "))
d = dict()

# Input arrival and burst times
for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process " + str(i + 1) + ": "))
    b = int(input("Enter burst time of process " + str(i + 1) + ": "))
    d[key] = [a, b]

# Sort processes by arrival time
d = sorted(d.items(), key=lambda item: item[1][0])

ET = []
for i in range(len(d)):
    if i == 0:
        ET.append(d[i][1][0] + d[i][1][1])
    else:
        if d[i][1][0] > ET[i - 1]:
            ET.append(d[i][1][0] + d[i][1][1])
        else:
            ET.append(ET[i - 1] + d[i][1][1])

TAT = [ET[i] - d[i][1][0] for i in range(n)]
WT = [TAT[i] - d[i][1][1] for i in range(n)]
avg_WT = sum(WT) / n

# Output results
print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
for i in range(n):
    print("  ", d[i][0], "   |   ", d[i][1][0], "   |   ", d[i][1][1],
          "  |  ", ET[i], "  |     ", TAT[i], "    |  ", WT[i])
print("Average Waiting Time:", avg_WT)
