import dices as d
import random as rd
while True:
    input_dices = input("Enter dices in format <N1dM1 N2dM2 ...>  (note that N<100): ")
    if all(map(d.check, input_dices.split())):
        break
    else:
        print("Wrong input, try again.")
        continue

dices = []
for dice in input_dices.split():
    dices.append(d.convert(dice))

print("Probabilities for dice values sums:")
probstable = d.probs(dices)
for i in probstable:
    print(f"{i:3}: {f'{round(probstable[i],3):.3f}':6} %")

print("Your roll:")
for dice in dices:
    for _ in range(1,dice[0]+1):
        print(f"d{dice[1]:<3}-> {rd.randint(1,dice[1])}")

