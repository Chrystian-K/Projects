d = {"a": 10, "b":2, "c":22}
tmp = list()
for k,v in d.items():
    tmp.append((v,k))

print(tmp)
tmp = sorted(tmp, reverse=False)
print(tmp)