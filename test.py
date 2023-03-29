#test for main branch
import time

class testClass:

    def test_function():
        phases = int(input("Test phases: "))
        print("! Test is starting execution ! ")
        try:
            for i in range(phases):
                print("   Test phase " + str(i+1) + " running...")
                time.sleep(1)
            print("! Test completed !")

        except:
            print("Something went wrong, please check input !")

#This is edited locally.
if __name__ == __name__:
    testClass.test_function()
    
    




