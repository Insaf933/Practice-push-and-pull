numbers = [-12, 4, 12, 25, 67]
    while True:
     num = int(input("Enter a number (or -99 to quit): "))
     if num == -99:
          break
    index = 0
    while index<len(numbers) and numbers[index]<v:
        index +=1
        numbers.insert(index,num)
        print(numbers)