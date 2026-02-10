lst = list(map(int, input("Enter numbers separated by spaces: ").split()))

lst.sort()
print("Ascending:", lst)

lst.sort(reverse=True)
print("Descending:", lst)
