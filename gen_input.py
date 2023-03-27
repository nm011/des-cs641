from os import urandom
from pwn import *

# f = open("input_0.txt","a")
f = open("input_1.txt","a")

xor_pt = (
0x4008000004000000,
0x0020000800000400
)

mapping = {}
for i in range(16):
    num = '{:0>4}'.format(format(i,"b"))
    mapping[num] = chr(ord('f')+int(num,2))

# hex_value = xor_pt[0]   #for characteristic 40 08 00 ..., writing to file input_0.txt 
hex_value = xor_pt[1]     #writing to input_1.txt
bin_value = '{0:064b}'.format(hex_value)

final_permutation = [ 
	40,8,48,16,56,24,64,32, 
	39,7,47,15,55,23,63,31, 
	38,6,46,14,54,22,62,30, 
	37,5,45,13,53,21,61,29, 
	36,4,44,12,52,20,60,28, 
	35,3,43,11,51,19,59,27, 
	34,2,42,10,50,18,58,26, 
	33,1,41,9,49,17,57,25 
]

for i in range(280):
    r8 = urandom(8).hex()
    r8w = hex(int(r8,16)^hex_value)
    c = '{0:064b}'.format(int(r8,16))
    cw = '{0:064b}'.format(int(r8w,16))
    fp_c = ''
    fp_cw = ''

    for i in range(64):
        fp_c+=(c[final_permutation[i]-1])
        fp_cw+=(cw[final_permutation[i]-1])
    
    for i in range(0,64,4):
        f.write(mapping[fp_c[i:i+4]])
    f.write('\n')
    
    for i in range(0,64,4):
        f.write(mapping[fp_cw[i:i+4]])
    f.write('\n')