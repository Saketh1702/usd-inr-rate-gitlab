import os
import sys
import requests
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

# load .env locally
load_dotenv()

API_KEY    = os.getenv("EXCHANGE_API_KEY")
BASE       = "USD"
TARGET     = "INR"
ENDPOINT   = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{BASE}/{TARGET}"

def fetch_rate():
    if not API_KEY:
        sys.exit("❌ No EXCHANGE_API_KEY in environment")
    resp = requests.get(ENDPOINT)
    resp.raise_for_status()
    data = resp.json()
    if data.get("result") != "success":
        sys.exit(f"❌ API error: {data.get('error-type')}")
    return data["conversion_rate"], data["time_last_update_utc"]

def render_readme(rate, updated_utc):
    env = Environment(loader=FileSystemLoader("template"))
    tmpl = env.get_template("README.md.template")
    content = tmpl.render(
        rate=f"{rate:.4f}",
        updated_utc=updated_utc
    )
    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    rate, updated_utc = fetch_rate()
    render_readme(rate, updated_utc)
