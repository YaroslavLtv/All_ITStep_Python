import random

stats = []
fireball = [12, 15, 28, 10, 5]
lightning = [7, 13, 15, 30, 10]
silence = [23, 10, 12, 7, 18]
fire_ward = [20, 23, 14, 6, 17]

attributes = 5
for i in range(attributes):
    r = random.randint(60, 80)
    stats.append(r)

print(stats)
select = int(input("Select: ")) - 1  # Якщо селект = 0, то в наступному рядку звертаємось до
# елемента в списку
# під номером, котрий міститься у змінній select
stats[select] = stats[select] + random.randint(5, 15)

for i in range(attributes):
    if i == select:
        continue
    stats[i] = stats[i] - random.randint(5, 15)
print(stats)

while True:
    choice = input("[f] - fireball, [l] - lightning, [s] - silence, [fw] - fire ward: ")
    if choice == "f":
        for i in range(attributes):
            if stats[i] - fireball[i] >= 0:
                stats[i] = stats[i] - fireball[i]
            else:
                print("Not enough skills!")
        print(stats)
    if choice == "l":
        for i in range(attributes):
            if stats[i] - lightning[i] >= 0:
                stats[i] = stats[i] - lightning[i]
            else:
                print("Not enough skills!")
        print(stats)
    if choice == "s":
        for i in range(attributes):
            if stats[i] - silence[i] >= 0:
                stats[i] = stats[i] - silence[i]
            else:
                print("Not enough skills!")
        print(stats)
    if choice == "fw":
        for i in range(attributes):
            if stats[i] - fire_ward[i] >= 0:
                stats[i] = stats[i] - fire_ward[i]
            else:
                print("Not enough skills!")
        print(stats)