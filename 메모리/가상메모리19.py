foods = ["햄버거", "샐러드", "비스킷"]

# foods는 변수 또는 참조자

print(id(foods)) # random access memory를 사용하기 때문에 번호는 계속 변화한다
print(hex(id(foods)))

mv = memoryview(b"happy day")

print(mv)

print(mv[0])
print(mv[1])