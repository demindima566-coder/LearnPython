from random import random, choice

import logging

from my_decorator import retry

exceptions = (ValueError, OSError)

#logging
logging.basicConfig (
    level=logging.INFO, format = "%(asctime)s | %(levelname)s | %(message)s"
)

@retry(count=5)
def random_exception() -> float:
    if (d := random()) > 0.5:
        raise choice(exceptions)
    return d


if __name__ == "__main__":
    for _ in range(100):
        try:
            result = random_exception()
            logging.info(f"result: {result}")
            print("result", result)
        except Exception as e:
            logging.error(f"Unhandled exception: {e}")