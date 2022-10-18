logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""



def starting():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    want_play = input("Type 'yes' to starting or type 'no' to end \n").lower()
    
    while want_play == 'yes':
        print(f"{logo} \n")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encript_text = []
        decript_text = []

        if direction == 'encode':
            encrypt(text_input=text,shift=shift,encript_text=encript_text,decript_text=decript_text,alphabet=alphabet)
        else:
            decrypt(text_input=text,shift=shift,encript_text=encript_text,decript_text=decript_text,alphabet=alphabet)

        want_play = input("Type 'yes' to start again type 'no' to end \n").lower()


def encrypt(text_input,shift,encript_text:list,decript_text:list,alphabet:list):
    # text_encript=''.join(text_input)
    decript_text.clear()
    for index in range(len(text_input)):
        if text_input[index] in alphabet:
           result = alphabet.index(text_input[index])
           if result >= 25:
                result = -1
           encript_text.append(alphabet[result + shift])
    
    print(''.join(encript_text))

def decrypt(text_input,shift,encript_text:list,decript_text:list,alphabet:list):
    encript_text.clear()
    for index in range(len(text_input)):
        if text_input[index] in alphabet:
           result = alphabet.index(text_input[index])
           if result >= 25:
                result = -1
           decript_text.append(alphabet[result - shift])

    print(''.join(decript_text))

if __name__=='__main__':
    starting()