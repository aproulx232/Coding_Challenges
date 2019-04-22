
"""Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

def count_decode( msg ):
    print("msg: ", msg)
    # for each digit, if not last go to last
    # if 1 digit, 1, way,
    # if 2 digit if less than 26, add another way, move back 1 digit
    len_msg = len(msg)
    if msg == 0:
        return 0
    elif len_msg == 1  or len_msg ==0 :
        return 1
    elif len_msg >= 2:
        if int( msg[:2]) < 27 and int( msg[:2]) != 10 and int( msg[:2]) != 20:
            return  count_decode(msg[1:]) + count_decode(msg[2:])
        elif int(msg[:2]) == 10 or int(msg[:2]) == 20:
            return  count_decode(msg[2:])
        else:
            return count_decode(msg[1:])

print("count: ", count_decode('1')) # a
print("count: ", count_decode('11')) # aa k
print("count: ", count_decode('10')) # j
print("count: ", count_decode('111')) # ka ak aaa
print("count: ", count_decode('101')) # ja
print("count: ", count_decode('1111')) #aaaa aak aka kaa kk
print("count: ", count_decode('11111')) #aaaaa kaaa kka kak akaa akk aaak aaka