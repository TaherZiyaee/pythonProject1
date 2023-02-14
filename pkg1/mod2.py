def func3(n: int):
    print(pow(n, 3))


def func4(s: str):
    print(s.lower())

print(__name__)
if __name__ == "__main__":
    func3(3)
    func4("SHAYAN")
    print("END")