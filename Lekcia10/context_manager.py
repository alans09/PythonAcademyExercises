import time

# with open("data.txt", "r") as fp:
#     print(fp.readlines())


class Timer():
    def __enter__(self):
        self.start = time.time()
        print("Zaciname")
        return 1

    def __exit__(self, *args):
        self.end = time.time() - self.start
        print(f"Trvanie: {self.end}")




for l in range(5):
    with Timer() as i:
        print(i)
        time.sleep(0.3)

### contextlib.contextmanager  (cela kniznica s context managermi)
### everything before yield is  __enter__  all after   is __exit__