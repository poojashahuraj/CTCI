def computeLargestArea(hist, N):
    stack = []
    max_area = 0
    idx = 0
    while idx < N:
        # if stack is empty or top element of stack is less than index element
        # basically stack is having the smallest element at the bottom of the stack.
        if not stack or hist[stack[-1]] <= hist[idx]:
            stack.append(idx)
            idx += 1
        else:

            height_idx = stack.pop()

            depth = idx
            if stack:
                depth = idx - stack[-1] - 1

            area = hist[height_idx] * depth
            max_area = max(area, max_area)

    while stack:
        height_idx = stack.pop()

        depth = idx
        if stack:
            depth = idx - stack[-1] - 1

        area = hist[height_idx] * depth
        max_area = max(area, max_area)

    return max_area


def main():
    N = 5
    hist = [1,2,3,4,5]
    print computeLargestArea(hist, N)


if __name__ == '__main__':
    main()