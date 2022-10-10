#Example1
def functionName1():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    functionTry1(var1, var2);

def functionTry1(var1, var2):
    try: 
        var3 = int(var1)+int(var2)
        print("{} + {} = {}".format(var1, var2, var3))
    except ValueError as e: 
        print("{}: You did not provide a numeric value".format(e))
    except:
        print("Unknown error")
    finally:
        print("Final message");

#Example2
def functionName2():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1,var2;

def functionTry2():
    go = True
    while go:
        var1,var2 = functionName2()
        try: 
            var3 = int(var1)+int(var2)
            go = False
        except ValueError as e: 
            print("{}: You did not provide a numeric value".format(e))
        except:
            print("Unknown error")
    print("{} + {} = {}".format(var1, var2, var3))

        
if __name__ == "__main__":
    functionTry2();  #change to functionName1 to see Example1
