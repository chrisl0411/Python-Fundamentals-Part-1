#  File: Ciphers.py
#  Description: HW12: Substitution Ciphers
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: XXXXXXXXXX
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 11/6/18
#  Date Last Modified: 11/8/18

#encode function encodes a plaintext and returns a ciphertext using key
def encode(key,plaintext):
    ciphertext = " "
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter.isalpha():
            letterOrd = ord(letter)
            if letter.isupper():
                letterIndex = letterOrd-65
                cipherLetter = key[letterIndex]
                ciphertext = ciphertext + cipherLetter.upper()
            else:
                letterIndex = letterOrd-97
                cipherLetter = key[letterIndex]
                ciphertext = ciphertext + cipherLetter
        elif letter == " ":
            ciphertext = ciphertext + " "
        else:
            ciphertext = ciphertext + letter

    return ciphertext

#decode function decodes ciphertext and returns the plaintext using a key
def decode(key,ciphertext):
    plaintext = " "
    for i in range(len(ciphertext)):
        cLetter = ciphertext[i]
        if cLetter.isalpha():
            for j in range(len(key)):
                keyLetter = key[j]
                if cLetter.lower() == keyLetter:
                    if cLetter.isupper():
                        plainLetter = chr(j+65)
                        plaintext = plaintext + plainLetter.upper()
                    else:
                        plainLetter = chr(j+97)
                        plaintext = plaintext + plainLetter
        elif cLetter == " ":
            plaintext = plaintext + " "
        else:
            plaintext = plaintext + cLetter
        
    return plaintext

###main function takes in plaintextMessages and codedMessages lists and uses encode and decode functions
def main():
    
    plaintextMessages = [
        ["This is the plaintext message.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Let the Wookiee win!",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["I used to think I was indecisive, but now I'm not too sure.",
         "mqncdaigyhkxflujzervptobws"],
        ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
         "bludcmhojaifxrkzenpsgqtywv"] ]

    for item in plaintextMessages:
        key = item[1]
        plaintext = item[0]
        print(format("plaintext:","<13s")+plaintext)
        ciphertext = encode(key,plaintext)
        print(format("encoded:","<12s")+ciphertext)
        decodetext = decode(key,ciphertext)
        print(format("re-decoded:","<11s")+decodetext)
        print("")

    codedMessages = [
        ["Uijt jt uif dpefe nfttbhf.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
         "mqncdaigyhkxflujzervptobws"] ]

    for item in codedMessages:
        key = item[1]
        ciphertext = item[0]
        print(format("encoded:","<10s")+ciphertext)
        plaintext = decode(key,ciphertext)
        print(format("decoded:","<9s")+plaintext)
        print("")
        
main()
