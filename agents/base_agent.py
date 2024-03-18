from abc import abstractmethod

class BaseAgent:
    def __init__(self):
        pass

    @abstractmethod
    def run(self) -> str:
        '''
        The agent starts its execution from the given file and ultimately
        return a flag when succesful. 
        '''
        pass