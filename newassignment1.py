"""
# WAP to print the sum of odd and even numbers using user input range 
start=int(input("Enter a number:"))
end=int(input("Enter a number:"))
even_sum=0
odd_sum=0
for num in range(start,end+1):
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num
print("Sum of odd numbers:",even_sum)
print("Sum of odd numbers:",odd_sum)

# WAP to print the two roots of a user inputed equations using Shridhar Acharya formula
a=float(input("Enter coefficient of A:"))
b=float(input("Enter coefficient of B:"))
c=float(input("Enter coefficient of C:"))
d = b**2-4*a*c
if d >=0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots of the equation are:", root1, "and", root2)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(d)) / (2*a)
    print("The roots of the equation are complex:", f"{real_part} + {imaginary_part}i", "and", f"{real_part} - {imaginary_part}i")

def find_max_min(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left], arr[left]
    
    # Base case: only two elements
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[right], arr[left]
        else:
            return arr[left], arr[right]

    # Divide step: find the middle index
    mid = (left + right) // 2

    # Recursively find max and min in left and right halves
    max1, min1 = find_max_min(arr, left, mid)
    max2, min2 = find_max_min(arr, mid + 1, right)

    # Combine step: find overall max and min
    return max(max1, max2), min(min1, min2)

# Example usage
arr = [3, 1, 8, 5, 2, 7, 6, 4]
max_element, min_element = find_max_min(arr, 0, len(arr) - 1)

print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")
"""
start=int(input("Enter a number:"))
end=int(input("Enter a number:"))
even_sum=0
odd_sum=0
for num in range(start,end+1):
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num
print("Sum of even numbers:",even_sum)
print("Sum of odd numbers:",odd_sum)