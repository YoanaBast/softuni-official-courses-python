# 3. Chat Codes
#
# Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes.
# He starts by creating a program for only four messages.
#
# Create a program that receives the n number of messages sent. On the following n lines, it will receive integer numbers.
# For each number, the program should print a different message:

n_msg_sent = int(input())
for n in range(n_msg_sent):
    input_n = int(input())

# · If the number is 88 - "Hello"
    if input_n == 88:
        print("Hello")
        continue
# · If the number is 86 - "How are you?"
    if input_n == 86:
        print("How are you?")
        continue
# · If the number is not 88 nor 86, and it is below 88 - "GREAT!"
    if (input_n != 86) and (input_n != 88) and (input_n < 88):
        print("GREAT!")
        continue
# · If the number is over 88 - "Bye."
    if 88 < input_n:
        print("Bye.")
        continue