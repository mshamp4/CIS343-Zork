from observer.observer import Observer

class Observable(object):

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
	
    def update_observers(self):
        for observer in self.observers:
            observer.update(self)
	
