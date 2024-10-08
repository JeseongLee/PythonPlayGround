def find_dog(sound):
    if sound == "mm":
        return("dog")
    else:
        return("not dog " + sound)

sound = "na"
find_result = find_dog(sound)

print(find_result)
sound = "mm"
find_result = find_dog(sound)
print(find_result)