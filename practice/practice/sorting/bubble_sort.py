def bubble_sort(ip):
    for i in range(len(ip)):
        for j in range(i, len(ip)):
            if ip[i] > ip[j]:
                temp = ip[i]
                ip[i] = ip[j]
                ip[j] = temp
    return ip
print bubble_sort([3, 2, 6, 1, 8, 3, 5, 2, 8, 22, 11])