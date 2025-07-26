import numpy as np
print("can we play dice?")
ans = input("enter yes or no:")
if(ans == 'yes'):
    print("lets start!")
    dice = np.random.randint(1,7,size = 2)
    print("you rolled :",dice[0],dice[1])
if(ans == 'no'):
    print("thanks for playing!")


