from abc import ABCMeta, abstractclassmethod


class AutoTest(metaclass=ABCMeta):
    """
    Define an abstract factory as a test interface.
    """
    @classmethod
    @abstractclassmethod
    def run(cls):
        pass


class CreateTest(metaclass=ABCMeta):
    """
    Define an abstract factory as a create interface.
    """
    @classmethod
    @abstractclassmethod
    def create(cls):
        pass

