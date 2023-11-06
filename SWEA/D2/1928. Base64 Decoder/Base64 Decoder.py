T = int(input())
    
decode_str = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '0','1','2','3','4','5','6','7','8','9','+','/'
]
decode_dict = {key:idx for idx, key in enumerate(decode_str)}
 
for i in range(T):
    sen = input()
    decode_result = ''
 
    for word in sen:
        num = decode_dict[word]
        decode_result += str(bin(num)[2:]).zfill(6)
   
    base64_decode_result = ''
 
    for idx in range(len(sen)*6//8):
        base64_encode_result = int(decode_result[idx*8:idx*8+8],2)
        base64_decode_result += chr(base64_encode_result)
 
    print(f"#{i + 1} {base64_decode_result}")