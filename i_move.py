from abc import ABC, abstractmethod

class IMove(ABC):
    
    @abstractmethod
    def move(self): 
        pass


