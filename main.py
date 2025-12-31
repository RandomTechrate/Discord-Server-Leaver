import requests
import time

API_BASE = "https://discord.com/api/v10"

with open("tokens.txt", "r", encoding="utf-8") as f:
    tokenlist = [t.strip() for t in f if t.strip()]

with open("exceptions.txt", "r", encoding="utf-8") as f:
    exceptions = set(line.strip() for line in f if line.strip())

HEADERS_BASE = {
    "User-Agent": "DiscordACC (https://dsc.gg, 1.0)",
    "Content-Type": "application/json",
}

session = requests.Session()
session.headers.update(HEADERS_BASE)


def build_auth_header(token):
    if token.startswith("Bot ") or token.count(".") == 2:
        return {"Authorization": f"Bot {token}"}
    return {"Authorization": token}


def request_with_ratelimit(method, url, headers=None, **kwargs):
    while True:
        r = session.request(method, url, headers=headers, timeout=15, **kwargs)
        if r.status_code != 429:
            return r
        retry_after = float(r.headers.get("Retry-After", 5))
        time.sleep(retry_after)


def leave_guild(token, guild_id):
    headers = build_auth_header(token)
    r = request_with_ratelimit(
        "DELETE",
        f"{API_BASE}/users/@me/guilds/{guild_id}",
        headers=headers
    )
    return r.status_code in (200, 204)


for token in tokenlist:
    headers = build_auth_header(token)
    r = request_with_ratelimit(
        "GET",
        f"{API_BASE}/users/@me/guilds",
        headers=headers
    )

    if r.status_code != 200:
        continue

    for guild in r.json():
        if guild["id"] in exceptions:
            continue
        leave_guild(token, guild["id"])