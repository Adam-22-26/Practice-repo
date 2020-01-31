def main():


    try:
        file = open("hello.txt", 'w')
        file.write("hello this is a new written")
        
        file = open("hello.txt", 'r')
        print(file.read())
    finally:
        file.close()
    
    try:
        def some(x):
            somes = ''
            somes = 'hi ' + x
            return somes
        
            
        print(some('adam'))
    except None:
        
        print("False")
    primary = {            
            "red": [255, 0 , 0],
            "green": [0, 255, 0],
            "blue": [0, 0,255]
            }
    primary["blue"] = "blue blue han hahaha"
    primary["gray"] = "syempre kulay gray ito"
    print(primary["blue"])
    print(primary["gray"])
    print(primary["red"])
    tuples = {0: "adam", 1 : "marcaida"}
    tuples[0]= "marcaida"
    print(tuples[0])
    cubes = [i for i in range(20) if i%3 == 0]
    
    print(cubes)
    #print(primary["yellow":  [0, 2, 55])
    print("{0}{1}{0}".format("abra", "cad"))
    nums = [255, 0 , 2]
    
if __name__ == "__main__":
    main()