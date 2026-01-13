def check(tup):
    new = tup[0]
    fp = open("data.txt", "r")
    old = fp.readline()
    try:
        if int(old) == new:
            fp.close()
            return False 
        else:
            if new == -1:
                fp.close()
                return False
            if new > old:
                fp.close()
                update(new)
                return True
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Forcefully updating to fetched content!")
        fp.close()
        update(new)
        return True

def update(val):
    fp = open("data.txt", "w")
    fp.write(str(val))
    fp.close