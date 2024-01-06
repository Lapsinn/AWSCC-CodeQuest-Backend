def main():
    with open('names.txt', 'r') as read:
        names = read.readlines()
        names.sort()

    with open('names_1.txt', 'w') as write:
        write.writelines(names)

if __name__ == '__main__':
    main()
