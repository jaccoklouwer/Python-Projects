from enum import Enum

class Side(Enum):
    none = 0
    left = 1
    right = 2

class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        try:
            if self._left is not None and self._right is None:
                return Side.left
            if self._right is not None and self._left is None:
                return Side.right
            if self._left._left is not None and self._right is None:
                return Side.left
            if self._right._right is not None and self._left is None:
                return Side.right
            return Side.none
        except Exception as e:
            print(e)
       

left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)