class Observable:
    def __init__(self, value):
        self._value = value
        self._observers = []

    def __setitem__(self, key, value):
        if value is not self._value[key]:
            print('set: {}={}'.format(key, value))
            self._value[key] = value
            self.notify_observers(key=key, value=value)

    def __getitem__(self, key):
        return self._value[key]

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)


class Observer:
    def __init__(self, observable, cls, *args, **kwargs):
        self._instance = cls(*args, **kwargs)
        observable.register_observer(self)

    def update(self, observable, *args, **kwargs):
        print('update: {}={}'.format(kwargs['key'], kwargs['value']))
        if (kwargs['key'] == 'title'):
            if hasattr(self.instance.master, 'title'):
                self.instance.master.title(kwargs['value'])
            if hasattr(self.instance, 'text'):
                self.instance['text'] = kwargs['value']

    @property
    def instance(self):
        return self._instance
