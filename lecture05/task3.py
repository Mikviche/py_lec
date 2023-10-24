import dices as d
while True:
    input_dices = input("Enter dices in format <N1dM1 N2dM2 ...>  (note that N<100): ")
    if all(map(d.check, input_dices.split())):
        break
    else:
        print("Wrong input, try again.")
        continue

probstable = {}
for dice in input_dices.split():
    a = d.probs(d.convert(dice),"e")
    print(a)