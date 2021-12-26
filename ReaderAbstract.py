class ReaderAbstract():
    def __init__(self):
        if type(self) is ReaderAbstract:
            raise Exception('Base is an abstract class and cannot be instantiated directly')
        # Any initialization code
        print('In the __init__  method of the Base class: ReaderAbstract')

    # filepath is the path of the input file to be read.
    def extractdata(self, filepath):
        if type(self) is ReaderAbstract:
            raise Exception('extractdata is an abstract class and cannot be instantiated directly')
        # Any initialization code
        print('In the extractdata method of the Base class: ReaderAbstract')
