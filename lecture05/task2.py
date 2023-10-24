import dices as d

while True:
    input_dice = input("Enter dices in format NdM: ")
    if d.check(input_dice):
        break
    else:
        print("Wrong input, try again")
        continue


probstable = d.probs(d.convert(input_dice))

for i in probstable:
    print(f"{i:3}: {f'{round(probstable[i],3):.3f}':6} %")


