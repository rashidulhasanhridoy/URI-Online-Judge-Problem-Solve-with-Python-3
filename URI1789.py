def main():
    while True:
        numbers = []
        try:
            l = int(input())
        except:
            break
        x = input()
        numbers = x.split()
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        if max(numbers) < 10:
            print("1")
        elif max(numbers) >= 20:
            print("3")
        elif max(numbers) >= 10 or max(numbers) < 20:
            print("2")
if __name__ == '__main__':
    main()