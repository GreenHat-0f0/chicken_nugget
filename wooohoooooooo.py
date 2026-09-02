testtt = {
    "apple" : 1,
    "banana" : 2,
    "pair" : 3
}
print(testtt)
print(testtt["apple"])
testtt.update({"banana":5})
testtt.update({"cucumber":6})
print(testtt)
testtt.pop("pair")
print(testtt)
kkkk = testtt.keys()
print(kkkk)
print(testtt.values())
testtt["bainainao"] = testtt.pop("banana")
print(testtt)
print(dir(testtt))