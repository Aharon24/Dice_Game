import random as rd

def dice_game():
    
    a = rd.randint(1,6) 
    b = rd.randint(1,6)
    ra_dom =  a + b 
    print(f"the sam of this is {a} + {b} = {ra_dom} " )
    

    if ra_dom == 7 or ra_dom == 11 :
        print("you won !",ra_dom)

    elif ra_dom == 3 or ra_dom == 2  or ra_dom == 12 :
        print( "craps !  Casino wins ", ra_dom)
        
    else :
        print("Now your  gobal number is",ra_dom)
        

        while True :
            a1 = rd.randint(1,6)
            b1 = rd.randint(1,6)
            ra_dom1 = a1 + b1
            print(f"the sum of dice is {ra_dom1}")
            if ra_dom1 == 7:
                print("You Lose",ra_dom1)
                return
            
            elif  ra_dom == ra_dom1:
                print(f"The sum of dice is ! {a1} + {b1} = {ra_dom1}" )
                print("You Won !", ra_dom1 )
                return

dice_game()

    
