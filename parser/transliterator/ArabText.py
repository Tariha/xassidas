import alphabet
from _types.linked_queue import LinkedQueue


class ArabicText(LinkedQueue):

  class ArabicTextChar:
      def __init__(self, parent, node):
        self._node = node
        self._parent = parent

      def char(self):
          return self._node._ele

      def __eq__(self, other):
          return self.char() == other

      def __str__(self):
          return self.char()

      def next(self, val=None):
          if not val:
              return self._parent.after(self)
          ele = self
          while val!=0 and ele.next():
              ele = ele.next()
              val -= 1
          return ele

      def prev(self, val=None):
          if not val:
              return self._parent.before(self)
          ele = self
          while val!=0 and ele.prev():
              ele = ele.prev()
              val -= 1
          return ele

      def is_blank(self):
          return self == ' '

      def is_start(self):
          return self._node is self._parent._head

      def is_mid(self):
          try:
              return (not self.is_word_start()) and (not self.next().is_blank())
          except:
              return False

      def is_end(self):
          return self._node is self._parent._tail

      def is_word_start(self):
          return self.prev() == u" " or (not self.prev())

      def preceeded(self, n):
          out = u""
          ele = self
          while n!=0 and ele.prev():
              out += ele.prev().char()
              ele = ele.prev()
              n -= 1
          return out

      def succeeded(self, n):
          out = u""
          ele = self
          while n!=0 and ele.next():
              out += ele.next().char()
              ele = ele.next()
              n -= 1
          return out

      def is_followed_by_sun(self):
          lam_node = self.next()
          if lam_node.next().is_followed_by_shadda():
              return lam_node.next().char()
          return False

      def is_followed_by_shadda(self):
          return self.next() == alphabet.SHADDA

      def is_fatha_followed_by_alif(self):
          try:
              return self == alphabet.FATHA and self.next().is_alif()
          except:
              return False

      def is_kasra_followed_by_ya(self):
          return self == alphabet.KASRA and self.next() == alphabet.YA

      def is_damma_followed_by_waw(self):
          return self == alphabet.DAMMA and self.next() == alphabet.WAW

  def __init__(self, text):
      super().__init__()
      for c in text:
        self.enqueue(c)

  def _make_position(self, node):
      if node is None:
            return None
      return self.ArabicTextChar(self, node)

  def first(self):
      return self._make_position(self._head)

  def after(self, p):
      return self._make_position(p._node._next)

  def before(self, p):
      return self._make_position(p._node._prev)

  def __iter__(self):
      cursor = self.first()
      while cursor is not None:
          self.cursor = cursor
          yield cursor
          cursor = self.after(cursor)
