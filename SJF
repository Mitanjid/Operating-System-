print ("Shortest job first Schedulinng")
n = int(input("Enter number of processes: "))
d = dict()

for i in range(n):
    key = "P" + str(i + 1)
    at = int(input(f"Enter arrival time of {key}: "))
    bt = int(input(f"Enter burst time of {key}: "))
    d[key] = [at, bt]

    processes = [(k, v[0], v[1]) for k, v in d.items()]
completed = []

ET = []  
TAT = []    
WT = []   
time = 0

while len(completed) < n:
    
    ready = [p for p in processes if p[1] <= time and p[0] not in completed]
    
    if not ready:
        time += 1
        continue
    
   
    ready.sort(key=lambda x: x[2])
    current = ready[0]
    
    time += current[2]
    ET.append(time)
    TAT.append(time - current[1])
    WT.append(TAT[-1] - current[2])
    completed.append(current[0])
print("\nProcess | Arrival | Burst | Exit | TAT | WT |")
for i in range(n):
    p = [p for p in processes if p[0] == completed[i]][0]
    print(f"   {p[0]}   |  {p[1]}      | {p[2]}     |   {ET[i]}  |   {TAT[i]} |   {WT[i]} | ")

print(f"\nAverage Turnaround Time:",sum(TAT)/n)
print(f"Average Waiting Time:", sum(WT)/n)
