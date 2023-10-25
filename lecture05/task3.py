import dices as d
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

probstable = d.probs(dices)
for i in probstable:
    print(f"{i:3}: {f'{round(probstable[i],3):.3f}':6} %")

