class Resource:

    def __init__(self, name, total, allocated):
        self._name = name
        self._total = total

        if not (total >= 0 and allocated >= 0):
            raise ValueError(f"Total and allocated need to be initialized as positive values")

        if allocated <= total:
            self._allocated = allocated
        else:
            raise ValueError(f"Allocated can not be greater than total {self.total}")


    # name, total and allocated are read-only. can not be changed directly after creation.
    @property
    def name(self):
        return self._name

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return f"Instance belongs to `{(str(type(self).__name__).lower())}` class"

    def claim(self, value):
        if not (type(value) is int and value >0):
            raise ValueError(f"Can only claim a positive integer amount.")

        if value <= (self.total - self.allocated):
            self._allocated += value
        else:
            raise ValueError(f"Can not claim up to more than the total. {self.total - self.allocated}"
                             f" available")

    def freeup(self, value):
        if not (type(value) is int and value >0):
            raise ValueError(f"Can only free up a positive integer amount.")

        if value <= self.allocated:
            self._allocated -= value
        else:
            raise ValueError(f"Can not free more than allocated. {self.allocated}")

    def died(self, value):
        if not (type(value) is int and value >0):
            raise ValueError(f"Can only remove a positive integer amount.")

        if value <= self.total:
            self._total -= value
            self._allocated = min(self.total, self.allocated)
        else:
            raise ValueError(f"Can not remove more than the total. {self.total}")

    def purchased(self, value):
        if not (type(value) is int and value >0):
            raise ValueError(f"Can only purchase a positive integer amount.")

        self._total += value

    def __str__(self):
        return f"{self.name} instance with attributes {self.__dict__}"

    def __repr__(self):
        return f"{self.name} instance of the {type(self)} at memory address {hex(id(self))}"

class Cpu(Resource):

    def __init__(self, name, total, allocated, cores, socket, power_watts):
        super().__init__(name, total, allocated)
        if (type(cores) is int) and (type(power_watts) is int):
            self.cores = cores
            self.power = power_watts
        else:
            raise TypeError(f"Cores and power in watts need to be integer")

        if type(socket) is str:
            self.socket = socket
        else:
            raise TypeError(f"Socket needs to be a string value")

new = Cpu("cpu1", 200, 98, 4 , "dds", 22)

#
# new.claim(2)
# new.freeup(111)
# new.died(1)
# new.purchased(50)
# print(new.category)
print(new.__dict__)