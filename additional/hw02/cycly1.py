#list comprehension
limit = int(input("Enter the limit >> "))
total_sum = sum([x for x in range(limit +1) if x % 3 == 0 or x % 5 ==0])
print(total_sum)