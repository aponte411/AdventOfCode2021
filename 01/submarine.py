def main():

    with open('input.txt','r') as f:
        data = [int(depth.split('\n')[0]) for depth in f.readlines()]

    increasing_depths = [d2 > d1 for d1, d2 in zip(data, data[1:]) ]
    print(f"Total number of increases: {sum(increasing_depths)}")

    windows = [a+b+c for a, b, c in zip(data,data[1:], data[2:]) ]
    increasing_windows = [w2 > w1 for w1, w2 in zip(windows, windows[1:])]
    print(f"Total number of number of increasing windows: {sum(increasing_windows)}")

if __name__ == "__main__":
    main()
