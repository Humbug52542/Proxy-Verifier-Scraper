from scraper import scrape_proxies
from verifier import verify_proxies

def main():
    proxies = scrape_proxies()
    print(f"Scraped {len(proxies)} proxies.")
    if not proxies:
        print("No proxies scraped, exiting.")
        return
    try:
        good = verify_proxies(proxies)
    except Exception as e:
        print(f"Error verifying proxies: {e}")
        return
    print(f"{len(good)} working proxies saved.")
    with open("working.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(good))

if __name__ == "__main__":
    main()
# ProxyVerifierScraper/main.py
