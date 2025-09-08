# Find smallest and largest numbers entered by the user
nums = []

while True:
    n = input("Enter a number (or press Enter to stop): ")
    if n == "":
        break
    nums.append(float(n))

if nums:
    print("Smallest:", min(nums))
    print("Largest:", max(nums))
else:
    print("No numbers entered.")
