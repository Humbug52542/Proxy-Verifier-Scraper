import requests

def scrape_proxies():
    urls = [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://www.proxy-list.download/api/v1/get?type=http"
    ]
    proxies_set = set()  # renamed from 'all'
    for u in urls:
        try:
            r = requests.get(u, timeout=5)
            if r.ok:
                proxies_set.update(r.text.strip().splitlines())
        except requests.RequestException:
            pass
    return list(proxies_set)
