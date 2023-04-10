# ### Exercises: Level 2

# 1. Join A and B
# 1. Find A intersection B
# 1. Is A subset of B
# 1. Are A and B disjoint sets
# 1. Join A with B and B with A
# 1. What is the symmetric difference between A and B
# 1. Delete the sets completely
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

joining = A.union(B)
print("The join is", joining)
inter = A.intersection(B)
print("The intersection is", inter)

print("Is A and B disjoint", A.isdisjoint(B))

print("Joining A with B", A.union(B))
print("Joining B with A", B.union(A))

print("Checking symetric difference", A.symmetric_difference(B))

del A
del B