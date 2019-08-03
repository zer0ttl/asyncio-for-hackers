import requests
import time


def fetch(url):
    resp = requests.get(url)
    return resp.headers['Content-Length']


def main():
    url = 'https://www.ietf.org/rfc/rfc{}.txt'
    for i in range(2000, 2010):
        print(f"{url.format(i)} --> Content-Length :{fetch(url.format(i))}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:0.2f} seconds.")
