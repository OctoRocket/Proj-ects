import pickle

class message:
    message = input("Type what you want to be turned into saved data (string): ")
    while True:
        try:
            number = int(input("Type what you want to be turned into saved data (int): "))
            break
        except:
            print("Try again!")
    dictionary = {"Message": message, "Number": number}

message_1 = message()
output = pickle.dumps(message_1)
print(f"Output:\n{output}\n")