import time


def scan_ip(ip):
    print(f"scanning initiated for : {ip}")
    # scanning logic here
    time.sleep(2)
    print(f"completed scanning for : {ip}")


def main():
    scan_ip('10.0.0.1')
    scan_ip('10.0.0.2')
    scan_ip('10.0.0.3')
    scan_ip('10.0.0.4')
    scan_ip('10.0.0.5')


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:0.2f} seconds.")
