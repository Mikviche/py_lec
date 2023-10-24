import dices as d

while True:
    input_dice = input("Enter dices in format <NdM> (note that N<100): ")
    if d.check(input_dice):
        break
    else:
        print("Wrong input, try again")
        continue

dice = d.convert(input_dice)
probstable = d.probs(dice,"p")

for i in probstable:
    print(f"{i:3}: {f'{round(probstable[i],3):.3f}':6} %")


