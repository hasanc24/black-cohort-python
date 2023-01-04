#!/user/bin/env python 3.7 

message = input ("Enter a message: ")

print("First character: ", message [0])
print("Last character:", message [-1])
print("Middle character:", message[int(len(message) / 2)])
print("Even index character:", message [0::2])
print("Odd index character:", message [1::2])
print("Reversed message:", message [::-1])