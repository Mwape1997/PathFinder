import argparse
import os

list = []  # list of paths


def nesting(path):  # counts nesting of paths
    count = 0
    head = tail = path
    while head and tail:
        head, tail = os.path.split(head)
        count = count + 1
    return count


def longest_path(paths):
    return max(paths, key=nesting) # return the longest path


def deepest_path(search_path):
    if os.path.isdir(search_path):  #check if the given path is an actual directory
        for root, dirs, files in os.walk(search_path):
            for name in dirs:
                directory = os.path.join(root, name)
                list.append(directory)
        output = longest_path(list)  # supply directories to longest path algorithm
        print()
        result = output.rsplit('/', 1)[1]  # split the string from the right and get everything after the last occurrence of the character
        print(result)
    else:
        print("No directories in this path!")   #return error message if the path is not valid

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # crease a parser
    parser.add_argument('--path', type=str, required=True)  # add the argument
    args = parser.parse_args()  # parse the argument
    # print(longest_path(args.path) )
    deepest_path(args.path)  # call the deepest path algorithm and supply path
