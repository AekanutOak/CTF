from base64 import b32decode

char_to_morse = { 'A':'._', 'B':'_...',
                    'C':'_._.', 'D':'_..', 'E':'.',
                    'F':'.._.', 'G':'__.', 'H':'....',
                    'I':'..', 'J':'.___', 'K':'_._',
                    'L':'._..', 'M':'__', 'N':'_.',
                    'O':'___', 'P':'.__.', 'Q':'__._',
                    'R':'._.', 'S':'...', 'T':'_',
                    'U':'.._', 'V':'..._', 'W':'.__',
                    'X':'_.._', 'Y':'_.__', 'Z':'__..',
                    '1':'.____', '2':'..___', '3':'...__',
                    '4':'...._', '5':'.....', '6':'_....',
                    '7':'__...', '8':'___..', '9':'____.',
                    '0':'_____', ', ':'__..__', '.':'._._._',
                    '?':'..__..', '/':'_.._.', '_':'_...._',
                    '(':'_.__.', ')':'_.__._'}

morse_to_char = {}
for key,value in char_to_morse.items():
    morse_to_char[value] = key

secret = open("./problem3.txt").read()
secret = secret.split()
secret = ''.join([morse_to_char[c] for c in secret])
secret = b32decode(secret)
secret = b32decode(secret)
secret = b32decode(secret).decode()
print(secret)

# Add { } to get the legitimate flag format
