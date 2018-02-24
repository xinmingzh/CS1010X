
def ip_format(ip_address):
    # Fill in your code here
    bit1to4 = [ip_address[:8], ip_address[8:17], ip_address[17:25], ip_address[25:]]
    no1 = 0

    
    for j in range(4):
        current_bit = bit1to4[j]
        for i in range(1,9):
            current_bit = bit1to4[j]
            if current_bit % 10 == 1:
                no1[j] += 2**i
            current_bit = current_bit // 10

ip_address = '11001011100001001110010110000000'
bit1to4 = [ip_address[:8], ip_address[8:16], ip_address[16:24], ip_address[24:]]
no = 0
result = ''

for i in range(4):
    for j in range(8):
        if bit1to4[i][j] == '1':
            no += 2**(7-j)
    result = result + str(no) + '.'
    no = 0
result = result[:-1]
print(result)

# print(bit1to4)
# print(bit1to4[1][8])

# print(ip_format('00000011100000001111111111111111'))
