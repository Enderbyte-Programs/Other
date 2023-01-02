def func1():
    print ("please put the starting number in the in the input box above")
    input_a = input()  
    input_a = int(input_a) 
    print ("please put the number that you divided by")
    input_b = input()
    input_b = int(input_b)
    print ("Please put the answer you got")
    input_c = input()
    input_c = int(input_c)
    print ("press enter to check answer")
    input_d = input()
    if input_c == input_a/input_b:
        print ("Yay! You got it right")
        print ("thank you for using this program")
    else:
        print ("try again :(")
        print ("tpye 'yes' to view the correct answer")
        input_k = input()
        if input_k == "yes":
            input_f = input_a/input_b
            input_g = input_c-input_f
            print (input_g)
            print (input_f)
        else:
            print ("thank you for using this program")

input_j = "yes"
while input_j == "yes":
    func1()
    print ("would you like to do this again?")
    input_j = input() 
