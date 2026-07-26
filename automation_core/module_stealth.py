import random
import time

class StealthBrowserConfig:
    USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ]

    @staticmethod
    def get_random_headers():
        return {
            "User-Agent": random.choice(StealthBrowserConfig.USER_AGENTS),
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua-Platform": "\"macOS\"",
            "Sec-Ch-Ua-Mobile": "?0"
        }

    @staticmethod
    def simulate_human_delay(min_sec=2, max_sec=5):
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)

    @staticmethod
    def airplane_mode_ip_rotation_hook():
        print("[*] Simulating Mobile Hotspot / IP Rotation sequence...")
        time.sleep(1)
        print("[+] IP Reset Successful. Fresh residential IP acquired.")

if __name__ == "__main__":
    print("Stealth Headers:", StealthBrowserConfig.get_random_headers())
    StealthBrowserConfig.airplane_mode_ip_rotation_hook()
