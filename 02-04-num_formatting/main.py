x = 9876.54321

print(format(x, ".2f"))

print(format(x, ">10.1f"))

print(format(x, "<10.1f"))

print(format(x, "^10.1f"))

print(format(x, ","))
print(format(x, "0,.1f"))

print(format(x, "e"))
print(format(x, "0.2E"))

separators = {ord("."): ",", ord(","): "."}
print(format(x, ",").translate(separators))
