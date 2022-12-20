
ItemsInCart = 0

if ItemsInCart != 2:  #    raise Exception("products cart count not matching")
    pass

assert(ItemsInCart == 0)


#try, catch  block

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Somehow i reached this block because there is failure in try block")


#actuall error messgage instead of customised message
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)


#finally
finally:
    print("cleaning up resources")

