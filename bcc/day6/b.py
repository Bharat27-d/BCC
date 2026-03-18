n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

total = 0

for i in range(n - 1):
    diff = abs(arr[i] - arr[i + 1])
    total += diff

print("Total distance:", total)