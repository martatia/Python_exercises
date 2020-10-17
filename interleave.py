# Tehtävä:
# Write function interleave that gets arbitrary number of lists as parameters. 
# You may assume that all the lists have equal length. 
# The function should return one list containing all the elements from the input lists interleaved.

def interleave(*lists):
    lista=[]
    for value in zip(*lists):
        for x in value:
            lista.append(x)
    return lista

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()