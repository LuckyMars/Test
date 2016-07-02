#解密加密来源https://gold.xitu.io/entry/575fae92df0eea0062c5a1dc
#原始文章http://www.blog.pythonlibrary.org/2016/05/18/python-3-an-intro-to-encryption/
#字符串转换http://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3
#http://lixingcong.github.io/2016/03/06/convert-data-in-python/
from Cryptodome.Cipher import DES
key = 'abcdefgh'
print(key.encode('utf-8'))
keyEN = key.encode('utf-8')
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

des = DES.new(keyEN, DES.MODE_ECB)
text = 'Python rocks!'
padded_text = pad(text)
textEN = bytes(padded_text, 'utf-8')
encrypted_text = des.encrypt(textEN)
print(encrypted_text)
# print(encrypted_text.encode('utf-8'))
print(str(bytes(encrypted_text))[2:-1])
okokss = '>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'
print(bytes(map(ord,okokss)))
PPPPDD=bytes(map(ord,okokss))
DDD = des.decrypt(PPPPDD)
print(DDD.decode('utf-8'))