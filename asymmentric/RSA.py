from Crypto.Util.number import *

class RSA:

    def __init__(self,p,q,e):
       self.p = p #getprime 512byte
       self.q = q #getprime 512byte
       self.e = e
       self.phi = (p-1)*(q-1)
       self.d = pow(e,-1,self.phi)
       self.n = p*q
       
    def encrypt(self, m):
        return pow(m,self.e,self.n)

    def decrypt(self, c):
        return pow(c,self.d,self.n)

p = getStrongPrime(512)
q = getStrongPrime(512)

e = 0x10001

rsa = RSA(p, q, e)

plaintext = b'LSM{Th1s_1s_my_rsa_c0d3}'

encrypt = rsa.encrypt(bytes_to_long(plaintext))
print("encrypt : ",long_to_bytes(encrypt))

decrypt = rsa.decrypt(encrypt)
print("decrypt : ",long_to_bytes(decrypt))


