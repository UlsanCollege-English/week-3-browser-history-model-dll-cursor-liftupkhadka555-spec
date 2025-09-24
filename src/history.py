# /src/history.py

class _N:
    __slots__ = ("url", "prev", "next")

    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.head = None   # first visited page
        self.tail = None   # last visited page
        self.cur = None    # current cursor

    def current(self):
        """Return the current URL or None if empty."""
        return self.cur.url if self.cur else None

    def visit(self, url):
        """If not at the end, drop all forward entries, then append url and move cursor."""
        node = _N(url)

        if self.cur is None:
            # empty history
            self.head = self.tail = self.cur = node
        else:
            # cut off forward history
            self.cur.next = None
            self.tail = self.cur

            # link new node
            node.prev = self.cur
            self.cur.next = node
            self.cur = self.tail = node

    def back(self, steps=1):
        """Move cursor back by up to 'steps'. Return current URL."""
        while steps > 0 and self.cur and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url if self.cur else None

    def forward(self, steps=1):
        """Move cursor forward by up to 'steps'. Return current URL."""
        while steps > 0 and self.cur and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url if self.cur else None
