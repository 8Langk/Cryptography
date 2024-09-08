shift_schedule = [1, 1, 2, 2,
                  2, 2, 2, 2,
                  1, 2, 2, 2,
                  2, 2, 2, 1]

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]


PC_2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]


IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

EXPAND= [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]

S_BOX = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]


P_BOX = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25
]
IP_INVERSE= [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9, 49, 17, 57, 25
]


def byteToBin(origin_array):
    bin_array = []
    for ch in origin_array:
        bin_array.append(format(ch,'08b'))
    
    return ''.join(bin_array)

def permutation(ptable, parray):
    permutation_array = []
    for index in ptable:
        permutation_array.append(parray[index-1])
    return ''.join(permutation_array)

        
#generate 16 round key  
def generateRoundKey(key):
    bin_key = byteToBin(key)
    p_key = permutation(PC_1, bin_key)
    
    #left, right separtate
    c = p_key[:28]
    d = p_key[28:] 
    
    round_key = []
    
    for lshift_num in shift_schedule:
        c = c[lshift_num:] + c[:lshift_num]
        d = d[lshift_num:] + d[:lshift_num]
        
        cd = c+d
        
        round_key.append(permutation(PC_2, cd))
        
    return round_key
    
    
def encryption(key, input_data): 
    
    round_key = generateRoundKey(key)
    
    #Initial permutation plaintext
    p_input = permutation(IP, byteToBin(input_data))
    
    
    l = p_input[:32]
    r = p_input[32:]
    
    # DES_encryption round
    for roundIndex in range(16):

        expand_r = permutation(EXPAND, r)
        
        #48bit xor with key
        xor= ''
        for xorIndex in range(48):
            xor += str(int(round_key[roundIndex][xorIndex])^int(expand_r[xorIndex]))
            
        # divide 6 group from xor_result
        sixGroup = [xor[i:i+6] for i in range(0, 48, 6)]
        
        # s_box substitution
        s = ''
        for bIndex in range(8):
            rows = sixGroup[bIndex][0]+sixGroup[bIndex][-1]
            cols = sixGroup[bIndex][1:-1]
            s_box = S_BOX[bIndex][int(rows,2)][int(cols,2)]
            s += format(s_box, "04b")
        
        # permutation substitution 
        p_sub = permutation(P_BOX, s)
             
        
        new_r= ''
        for xorIndex in range(32):
            new_r += str(int(l[xorIndex])^int(p_sub[xorIndex]))
        l=r
        r=new_r
   
    final_round = r+l
    ciphertext = permutation(IP_INVERSE, final_round)
   
    return ''.join([f"{int(ciphertext[i:i+8], 2):02x}" for i in range(0,len(ciphertext),8)])
    
    
def decryption(key, encrypt):
    round_key = generateRoundKey(key)
    
    #Initial permutation plaintext
    p_encrypt = permutation(IP, byteToBin(encrypt))
    
    l = p_encrypt[:32]
    r = p_encrypt[32:]
    
    for roundIndex in range(16):

        expand_r = permutation(EXPAND, r)
        
        #48bit xor with key
        xor= ''
        for xorIndex in range(48):
            xor += str(int(round_key[15-roundIndex][xorIndex])^int(expand_r[xorIndex]))
            
        # divide 6 group from xor_result
        sixGroup = [xor[i:i+6] for i in range(0, 48, 6)]
        
        # s_box substitution
        s = ''
        for bIndex in range(8):
            rows = sixGroup[bIndex][0]+sixGroup[bIndex][-1]
            cols = sixGroup[bIndex][1:-1]
            s_box = S_BOX[bIndex][int(rows,2)][int(cols,2)]
            s += format(s_box, "04b")
        
        # permutation substitution 
        p_sub = permutation(P_BOX, s)
             
        
        new_r= ''
        for xorIndex in range(32):
            new_r += str(int(l[xorIndex])^int(p_sub[xorIndex]))
        l=r
        r=new_r
   
    final_round = r+l
    ciphertext = permutation(IP_INVERSE, final_round)
   
    return ''.join([f"{int(ciphertext[i:i+8], 2):02x}" for i in range(0,len(ciphertext),8)])
    
    
if __name__ == "__main__":
    
    input_data=b'he11o_w0r1d!@@@@'
    #input_data = b'\x01#Eg\x89\xab\xcd\xef'
    key = b'abcdefgh'
    ciphertext = ''
    for i in range(0,len(input_data),8):
        chunk = input_data[i:i+8]
        ciphertext += encryption(key, chunk)
    
    print(f"encryption : {ciphertext}")
    
    ciphertext = bytes.fromhex(ciphertext)
    plaintext = ''
    for i in range(0,len(ciphertext),8):
        chunk = ciphertext[i:i+8]
        plaintext += decryption(key, chunk)
    
    print(f"decryption : {bytes.fromhex(plaintext)}")
    
    
    
