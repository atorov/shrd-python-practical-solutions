data = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
print(len(data))
print(int.from_bytes(data, "little"))
print(int.from_bytes(data, "big"))

x = 9234234123412341232538756899712343991
print(x.to_bytes(32, "little"))
print(x.to_bytes(32, "big"))
