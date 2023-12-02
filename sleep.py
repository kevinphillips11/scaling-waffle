import time

def sleep_for_5_minutes():
    print("Sleeping for 5 minutes...")
    time.sleep(300)  # 300 seconds = 5 minutes
    print("Waking up after 5 minutes!")

if __name__ == "__main__":
    sleep_for_5_minutes()
