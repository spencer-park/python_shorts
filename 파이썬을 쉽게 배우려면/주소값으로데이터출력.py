import struct

# 예시로 문자열을 정의하고 메모리 주소값을 출력
s = 'Hello, world!'
print(id(s))

# 문자열의 메모리 주소값과 문자열 데이터 값을 출력
address = id(s)
value = struct.unpack('P', struct.pack('p', bytes(address)))[0]
print(address, value)
