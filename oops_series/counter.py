class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1 

    @classmethod
    def show_count(cls):
        print(f"total count is: {cls.count}")

c1 = Counter()
c2 = Counter()
c2 = Counter()
c2 = Counter()
Counter.show_count()