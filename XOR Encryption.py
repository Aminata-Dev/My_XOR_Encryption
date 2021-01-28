def encrypt(char, key):
    ascii_char = ord(char)
    binary_id_char = str(bin(ascii_char)[2:])
    #loop to take the char back to a byte
    while len(binary_id_char) < 8:
        binary_id_char = '0' + binary_id_char
    decrypted_binary_char = ''
    #Application of the XOR truth table :
    for i in range(8):
        #I turned the key and the binary char to XOR them from the right to the left in order to add normally into the "decrypted_binary_char" variable the corresponding bit
        if (key[::-1][i] == '1' and binary_id_char[::-1][i] == '1') or (key[::-1][i] == '0' and binary_id_char[::-1][i] == '0'):
            decrypted_binary_char += '0'
        if (key[::-1][i] == '1' and binary_id_char[::-1][i] == '0') or (key[::-1][i] == '0' and binary_id_char[::-1][i] == '1'):
            decrypted_binary_char += '1'
    encrypted_integer_char = int(decrypted_binary_char[::-1], 2) #Converting the binary to int ( ascii value )
    encrypted_text = chr(encrypted_integer_char) #converting the int ( ascii ) to character
    return encrypted_text


message = str(input("Enter the text to encode \U0001F510 : "))
cipher = '10100111' #must contain 8 bits !
encrypted_text = ''
decrypted_text = ''

# calling the function encrypt for each characters in message
for characters in message:
    if characters == ' ': #adding spaces as they are
        encrypted_text += ' '
    encrypted_text += encrypt(characters, cipher)

# calling the function encrypt for each characters in encrypted_text ( "reXOR" )
for characters in encrypted_text:
    if characters == ' ': #adding spaces as they are
        decrypted_text += ' '
    decrypted_text += encrypt(characters, cipher)

print("-" * 80 +"\n\U0001F511 The encoded message is : " + encrypted_text + "\n\U0001F513 The decoded message is : " + decrypted_text)
