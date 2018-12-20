print(bytes(range(255)))

# bytes(str, encoding) = str.encode()
print(bytes("啊", encoding="UTF8"))
# b'\xe5\x95\x8a'
print('啊'.encode(encoding="UTF8"))
# b'\xe5\x95\x8a'

print(b'abcdef'.replace(b'a', b'e'))
# b'ebcdef'
print(b'abc'.find(b'b'))
# 1

# 类方法 bytes.fromhex(string)
print(bytes.fromhex('e5 95 8a'))
# hex()
print('啊'.encode(encoding="UTF8").hex())
# e5958a
# 索引
print(b'abcdef'[2])
# 99



