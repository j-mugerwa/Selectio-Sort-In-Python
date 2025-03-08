import time

def selection_sort_bandwidth(computers):
    n = len(computers)
    
    print("\n Sorting computers based on bandwidth requirement (Lowest to Highest)...\n")
    time.sleep(1)
    
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if computers[j][1] < computers[min_index][1]:
                min_index = j
        
        # Swap the computers if needed
        if min_index != i:
            computers[i], computers[min_index] = computers[min_index], computers[i]

        # Display step-by-step sorting progress
        print(f"Step {i + 1}: {[(comp[0], comp[1]) for comp in computers]}")
        time.sleep(1)

    return computers

# Get user input
print("Bandwidth Allocation Optimization using Selection Sort \n")
num_computers = int(input("Enter the number of computers competing for bandwidth: "))

computers = []
for i in range(num_computers):
    bandwidth = int(input(f"Enter bandwidth required by Computer {i + 1} (in Mbps): "))
    computers.append((f"Computer {i + 1}", bandwidth))

# Display initial state
print("\n Initial Bandwidth Requests:")
for comp in computers:
    print(f"{comp[0]} ➝ {comp[1]} Mbps")

# Apply selection sort
sorted_computers = selection_sort_bandwidth(computers)

# Display final sorted list
print("\n Optimized Bandwidth Allocation (Sorted Order):")
for comp in sorted_computers:
    print(f"{comp[0]} ➝ {comp[1]} Mbps")

print("\n Now, bandwidth can be allocated efficiently, starting from computers with the lowest demand!")
