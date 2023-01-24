import time
class testClass: 

    def test_function():
        phases = int(input("Test phases: "))
        print("! Test is starting execution ! ")
        for i in range(phases):
            print("   Test phase " + str(i) + " running...")
            time.sleep(1)
        print("! Test completed !")

if __name__ ==  __name__:
    testClass.test_function()

