import re
import requests
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    feats = []

    # 1. IP in URL
    feats.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)

    # 2. URL length
    feats.append(1 if len(url) > 54 else 0)

    # 3. HTTPS
    feats.append(1 if url.startswith("https") else 0)

    # 4. @ symbol
    feats.append(1 if "@" in url else 0)

    # 5. Hyphen in domain
    feats.append(1 if "-" in parsed.netloc else 0)

    # 6. Subdomains count
    feats.append(1 if parsed.netloc.count('.') > 2 else 0)

    # 7. Double slash redirect
    feats.append(1 if url.rfind('//') > 7 else 0)

    # 8. Shortening service
    shorteners = ['bit.ly', 'tinyurl', 'goo.gl']
    feats.append(1 if any(s in url for s in shorteners) else 0)

    # 9. HTTP response
    try:
        r = requests.get(url, timeout=3)
        feats.append(1 if r.status_code != 200 else 0)
    except:
        feats.append(1)

    # 10. Suspicious words
    suspicious = ['login', 'verify', 'bank', 'secure', 'account']
    feats.append(1 if any(w in url.lower() for w in suspicious) else 0)

    return feats