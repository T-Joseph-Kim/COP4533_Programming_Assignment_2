from collections import OrderedDict, deque
from pathlib import Path
import sys


def fifo_misses(k, requests):
    cache = set()
    order = deque()
    misses = 0

    for x in requests:
        if x in cache:
            continue

        misses += 1
        if len(cache) == k:
            victim = order.popleft()
            cache.remove(victim)

        cache.add(x)
        order.append(x)

    return misses


def parse_input(data):
    nums = list(map(int, data.split()))
    if len(nums) < 2:
        raise ValueError("Input must contain at least k and m.")

    k, m = nums[0], nums[1]
    req = nums[2:]

    if k < 1:
        raise ValueError("k must be >= 1.")
    if len(req) != m:
        raise ValueError(f"Expected {m} requests, found {len(req)}.")

    return k, req


def load_input_data():
    argv = sys.argv[1:]
    if argv:
        base_dir = Path(__file__).resolve().parent.parent
        requested = Path(argv[0])

        candidates = [
            requested,
            Path("data") / requested.name,
            base_dir / "data" / requested.name
        ]
        for candidate in candidates:
            if candidate.is_file():
                return candidate.read_text(encoding="utf-8").strip()
        raise FileNotFoundError(f"Input file not found: {argv[0]}")

    piped = sys.stdin.read().strip()
    if piped:
        return piped

    base_dir = Path(__file__).resolve().parent.parent
    default_input = base_dir / "data" / "input.txt"
    if default_input.is_file():
        return default_input.read_text(encoding="utf-8").strip()

    return ""


def main():
    data = load_input_data()
    if not data:
        return

    k, requests = parse_input(data)
    fifo = fifo_misses(k, requests)
    print(f"FIFO  : {fifo}")


if __name__ == "__main__":
    main()
