if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            index = int(command[1])
            element = int(command[2])
            my_list.insert(index, element)
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            element = int(command[1])
            my_list.remove(element)
        elif command[0] == "append":
            element = int(command[1])
            my_list.append(element)
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()