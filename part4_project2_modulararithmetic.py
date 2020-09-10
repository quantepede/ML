from functools import total_ordering

@total_ordering
class Mod:
    def __init__(self, value, mod):
        self._value = value % mod
        self._mod = mod

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, other):

        # guarantees that mod of self.value is taken every time it is set
        if isinstance(other, int):
            self._value = other % self.mod
        else:
            raise ValueError(f"Value ({other}) needs to be an integer value")

    @property
    def mod(self):
        return self._mod

    @mod.setter
    def mod(self, other):
        if isinstance(other, int) and other > 0:
            self._mod = other
        else:
            raise ValueError(f"Mod ({other}) needs to be a positive integer value")


    def __neg__(self):
        return Mod(-self.value, self.mod)

    def __add__(self, other):
        if isinstance(other, Mod) and self.mod == other.mod:
            return Mod(self.value + other.value, self.mod)
        elif isinstance(other, int):
            return Mod(self.value + other, self.mod)
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):

        if isinstance(other, Mod) and self.mod == other.mod:
            # print(f"iadd called with ({self}) and ({other})")
            self.value = self.value + other.value
            return self
        elif isinstance(other, int):
            # print(f"iadd called with ({self}) and ({other})")
            self.value = self.value + other
            return self
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")



    def __sub__(self, other):
        if isinstance(other, Mod) and self.mod == other.mod:
            return self.value - other.value
        elif isinstance(other, int):
            return self.value - other
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):

        if isinstance(other, Mod) and self.mod == other.mod:
            self.value = self.value - other.value
            return self
        elif isinstance(other, int):
            self.value = self.value - other
            return self
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")




    def __mul__(self, other):
        if isinstance(other, Mod) and self.mod == other.mod:
            return self.value * other.value
        elif isinstance(other, int):
            return self.value * other
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):

        if isinstance(other, Mod) and self.mod == other.mod:
            self.value = self.value * other.value
            return self
        elif isinstance(other, int):
            self.value = self.value * other
            return self
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")




    def __pow__(self, power, modulo=None):
        if isinstance(power, Mod) and self.mod == power.mod:
            return self.value ** power.value
        elif isinstance(power, int):
            return self.value ** power
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")

    def __rpow__(self, other):
        return self ** other

    def __ipow__(self, other):

        if isinstance(other, Mod) and self.mod == other.mod:
            self.value = self.value ** other.value
            return self
        elif isinstance(other, int):
            self.value = self.value ** other
            return self
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")



    def __eq__(self, other):
        if isinstance(other, Mod) and self.mod == other.mod:
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == (other % self.mod)
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")


    def __lt__(self, other):
        if isinstance(other, Mod) and self.mod == other.mod:
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < (other % self.mod)
        else:
            raise ValueError(f"Other needs to be an integer or a Mod object with the same modulus ({self.mod})")

    def __hash__(self):
        return hash((self.value, self.mod))

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"Mod object created with modulo ({self.mod}) and residue ({self.value})"

new = Mod(15,11)
new2 = 10
# print(new.value)
# print(new.value, new.mod)
# print(new == new2)
# print(hash(new), hash(new2))
# print(int(new2), int(new))
# print(new)
# print(new-new2)
# print(new+new2)
# print(new*new2)
# print(new**new2)
#
# print(new2-new)
# print(new2+new)
# print(new2*new)
# print(new2**new)
#
# print(type(new), type(new+new2), id(new), id(new2), id(new+new2), id(new2+new))

# print(new)

new3 = Mod(21,11)
print(new3.value)
# new3 **= new2
new *= new3
print(new.value)
print((-new).value)
#
# print(new3 <= new2)
print(Mod(3,12)+Mod(25,2))