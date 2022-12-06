def main():
    handle = open("input.txt")
    for line in handle:
        mystring = line.strip()
        for i in range(4, len(mystring)+1):
            if len(set(mystring[i-4:i])) == 4:
                print("star1", i)
                break
        for i in range(14, len(mystring)+1):
            if len(set(mystring[i-14:i])) == 14:
                print("star2", i)
                break


main()
quit()
