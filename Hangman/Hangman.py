import random
import os


def data():

    DATA=[]
    with open("./data.txt","r",encoding="utf-8") as f:
        
        for word in f:
            DATA.append(word)
        #print(DATA[170])
    return random.choice(DATA)

def menu():
    print("""
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
""")

    print("\n \t Try to guess the word")

def run():
    word=data()
    word=word
    size=len(word)-1
    word_to_guess=[]
    lives=5
    guess=False
    good=0
    menu()
    #print(word)
    
    
    for i in range (size):    
        word_to_guess.append("_")
    
    word_as_list=list(word_to_guess)
    word_to_guess=(" ".join(word_to_guess))
    print(word_to_guess)

    while "_" in word_as_list and lives >0:
        
        
        letter=input("Type a letter: ")
        
        for i in range(size):
            if word[i] == letter:
                              
                word_as_list[i]=letter
        
        if letter in word:
            good+=1
        else:
            lives=lives-1

        if good == size:
            guess==True
        os.system("cls")  
        word_to_guess=(" ".join(word_as_list))
        print("Lives: ", lives)
        print(word_to_guess)
        
    if "_" not in word_as_list:
        print("""
 .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. |  
| |  ____  ____  | || |     ____     | || | _____  _____ | |  
| | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| |  
| |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | |  
| |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | |  
| |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | |  
| |   |______|   | || |   `.____.'   | || |    `.__.'    | |  
| |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'   
 .----------------.  .----------------.  .-----------------.  
| .--------------. || .--------------. || .--------------. |  
| | _____  _____ | || |     ____     | || | ____  _____  | |  
| ||_   _||_   _|| || |   .'    `.   | || ||_   \|_   _| | |  
| |  | | /\ | |  | || |  /  .--.  \  | || |  |   \ | |   | |  
| |  | |/  \| |  | || |  | |    | |  | || |  | |\ \| |   | |  
| |  |   /\   |  | || |  \  `--'  /  | || | _| |_\   |_  | |  
| |  |__/  \__|  | || |   `.____.'   | || ||_____|\____| | |  
| |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'   
""")
    if lives<=0:
        os.system("cls")
        print("""
 .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. |  
| |    ______    | || |      __      | || | ____    ____ | || |  _________   | |  
| |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |  
| | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |  
| | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |  
| | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |  
| |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |  
| |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'   
 .----------------.  .----------------.  .----------------.  .----------------.   
| .--------------. || .--------------. || .--------------. || .--------------. |  
| |     ____     | || | ____   ____  | || |  _________   | || |  _______     | |  
| |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |  
| |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |  
| |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |  
| |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |  
| |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | |  
| |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'   
""")



if __name__=="__main__":
    run()