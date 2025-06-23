def main():
    length = str(input())
    array = [int(v) for v in input().split(" ")]

    if len(array) <= 1:
        print(0)
        return

    result = 0
    for i in range(1, len(array)):
        prev = array[i-1]
        difference = prev - array[i]
        
        if difference > 0:
            array[i] += difference
            result += difference

    print(result)

main()