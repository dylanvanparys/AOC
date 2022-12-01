with open('input.txt', 'r') as f:
    raw = f.read()
rows = raw.split('\n')

grouped_calories = []

calories_entry = 0
for row in rows:
    if row != '':
        calories_entry += int(row)
    else:
        grouped_calories.append(calories_entry)
        calories_entry = 0
grouped_calories.append(calories_entry)

print("")
print(max(grouped_calories))
print(grouped_calories.index(max(grouped_calories)))
print(len(grouped_calories))
print("")
print(sum(sorted(grouped_calories)[::-1][0:3]))
