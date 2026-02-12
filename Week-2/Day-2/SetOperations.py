print("Enter elements of Set A (space separated): ")
setA = set(map(int, input().split()))

print("Enter elements of Set B (space separated): ")
setB = set(map(int, input().split()))

print("\n SET OPERATIONS ")
print("Set A:", setA)
print("Set B:", setB)

print("\nUnion (A ∪ B):", setA.union(setB))
print("Intersection (A ∩ B):", setA.intersection(setB))
print("Difference (A - B):", setA.difference(setB))
print("Difference (B - A):", setB.difference(setA))
print("Symmetric Difference:", setA.symmetric_difference(setB))

print("Is A subset of B?", setA.issubset(setB))
print("Is A superset of B?", setA.issuperset(setB))
print("Are A and B disjoint?", setA.isdisjoint(setB))
