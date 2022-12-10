class Test:
    @property
    def testovich(self):
        print('11')

    @testovich.setter
    def testovich(self):
        print('hey')

Test.testovich