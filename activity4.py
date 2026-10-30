scores = [80, 70, 90, 60, 85, 75]
groups = [[], []]
totals = [0, 0]

for score in sorted(scores, reverse=True):
    if totals[0] <= totals[1]:
        groups[0].append(score)
        totals[0] += score
    else:
        groups[1].append(score)
        totals[1] += score

print("Group 1:", groups[0])
print("Group 2:", groups[1])
print("Group 1 Total:", totals[0])
print("Group 2 Total:", totals[1])
