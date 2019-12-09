def get_wires():
    with open('data.txt') as f:
        return list(f.readline().rstrip().split(',')), list(f.readline().rstrip().split(','))


