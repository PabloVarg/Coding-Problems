"""" This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26,
and an encoded message, count the number of ways
it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed """

# Algorithm
def numberofways(code):
    if '0' in code:
       return 0

    max = 26 # Value of z
    count = 1
    for x in range(1, len(code)):
        if int(code[x-1:x+1]) < max:
            count += 1
    return count

# Test
code = input('Write your secret code: ')
print('We can decode your message in', numberofways(code), 'way(s)')
