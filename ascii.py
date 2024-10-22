def decrypt(message : [int])-> str:  # On utilise eval pour interpréter la liste comme entrée
   text = "".join([chr(num) for num in message])
   print(text)

if __name__ == '__main__':
   decrypt( [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99, 101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 101, 32, 33])