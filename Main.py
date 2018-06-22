#coding=UTF-8

import  sys
import  rsa
import genkey

savedStdout = sys.stdout  #保存标准输出流
with open('out.txt', 'w+') as file:
        sys.stdout = file  #标准输出重定向至文件
        dist = genkey.GenerateKey(1024)
        print(dist)
        print("nlen: ",len(str(bin(dist["n"]))))

        M = "I Love You! 我爱你 Я люблю тебя. "*1
        C = rsa.Encrypt(dist,M,"UTF-8")
        Mr = rsa.Decrypt(dist,C,"UTF-8")

        print(C)
        print(Mr)

