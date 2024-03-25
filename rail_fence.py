def encrypt(text,key):
    
    rail = [['\n' for i in range(len(text))] for j in range(key)]

    direction_down = False ; col = 0 ; row = 0

    for i in range(len(text)):

        if row == 0 or row == key-1:
            direction_down = not direction_down

        rail[row][col] = text[i]
        col+=1

        if direction_down:
            row+=1
        else:
            row-=1        
    
    cipher = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                cipher.append(rail[i][j])

    return ''.join(cipher)

def decrypt(cipher,key):
        
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]

    direction_down = None ; col = 0 ; row = 0

    for i in range(len(cipher)):

        if row == 0 or row == key-1:
            direction_down = not direction_down

        rail[row][col] = '+'
        col+=1

        if direction_down:
            row+=1
        else:
            row-=1  
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '+' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    direction_down = False ; col = 0 ; row = 0 ; text = []

    for i in range(len(cipher)):

        if row == 0 or row == key-1:
            direction_down = not direction_down

        if rail[row][col] != '+':
            text.append(rail[row][col])
            col+=1

        if direction_down:
            row+=1
        else:
            row-=1        

    return ''.join(text)

if __name__ == '__main__':

    print(encrypt('attack at once',3))
    print(decrypt('dnhaweedtees alf  tl',3))     
   
