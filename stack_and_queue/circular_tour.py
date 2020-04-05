def circular_tour(arr):
    queue = [i for i in range(len(arr))]

    end = len(arr)-1
    curr = 0
    petrol, distance = 0, 0
    start_index = 0
    while end != start_index:
        curr = queue.pop(0)
        x, distance = arr[curr]
        petrol += x
        queue.append(curr)
        if petrol < distance:
            petrol, distance = 0, 0
            end = curr
            start_index = curr
    return end


print(circular_tour([(4, 6), (6, 5), (7, 3), (4, 5)]))