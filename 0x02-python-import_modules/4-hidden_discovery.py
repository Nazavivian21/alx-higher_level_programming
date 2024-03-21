#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    a = dir(hidden_4)
    for i in a:
        if i[0:2] == '__':
            continue
        print(i)
