#!/usr/bin/env python3
# Dev: Hayyan Da Edistein
import random
import time
import os
import sys
import json
import urllib.request
import urllib.parse

# ============ TERMUX/LINUX COLOR CODES ============
class C:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    RED    = "\033[91m"
    MAGENTA= "\033[95m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

BANNER = r"""
 _      _  ____            _  _      _____ ____
/ \  /|/ \/  _ \          / \/ \  /|/    //  _ \
| |\ ||| || | \|  _____   | || |\ |||  __\| / \|
| | \||| || |_/|  \____\  | || | \||| |   | \_/|
\_/  \|\_/\____/          \_/\_/  \|\_/   \____/
        >>> Hayyan Da Edistein <<<
"""

API_URL = "https://numquery.fast-page.org/api.php?action=lookup&number="

# ============ LETTER BY LETTER TYPING ============
def typewrite(text, delay=0.03, color=C.CYAN):
    for ch in text:
        sys.stdout.write(color + ch + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_line(text, delay=0.04, color=C.YELLOW):
    typewrite(text, delay, color)
    time.sleep(0.2)

def clear():
    os.system("clear" if os.name != "nt" else "cls")

# ============ REAL API LOOKUP ============
def api_lookup(number):
    """Real public number lookup: name, carrier, country."""
    try:
        url = API_URL + urllib.parse.quote(number)
        req = urllib.request.Request(url, headers={"User-Agent": "HayyanDaEdistein-PrankTool/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        if data.get("success") and data.get("data", {}).get("success"):
            return data["data"]
    except Exception as e:
        slow_line(f"[!] API error: {e} (using joke data instead)", 0.02, C.RED)
    return None

# ============ MASSIVE RANDOM NAME GENERATOR (fallback + flavor) ============
first_names = [
    "Rahim", "Karim", "Jashim", "Rashid", "Sohel", "Jahangir", "Babul",
    "Kamal", "Jamal", "Nasir", "Faruk", "Salim", "Alam", "Rafiq", "Hasan",
    "Mizan", "Shahin", "Robin", "Sumon", "Rakib", "Tanvir", "Sabbir",
    "Nayeem", "Riyad", "Sajid", "Arif", "Tuhin", "Munna", "Rana", "Sagor",
    "Ruma", "Tania", "Nusrat", "Joya", "Mim", "Puja", "Nipa", "Rima",
    "Shila", "Akhi", "Tisha", "Maria"
]

last_names = [
    "Uddin", "Ahmed", "Hossain", "Islam", "Rahman", "Mia", "Sheikh",
    "Molla", "Sardar", "Chowdhury", "Bhuiyan", "Talukder", "Khan",
    "Ali", "Munshi", "Dewan", "Sikder", "Das", "Biswas", "Mandal"
]

title_words = [
    "(Retd.)", "(Busy)", "(Missing)", "(Wanted)", "(Sleeping)",
    "(On Leave)", "(In Hiding)", "(VIP)", "(Local Legend)",
    "(Tea Addict)", "(Part-Time Don)", "(Full-Time Bhai)"
]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)} {random.choice(title_words)}"

# ============ FUNNY NID GENERATOR ============
nid_prefixes = ["1994", "1988", "2001", "1975", "0000", "5555", "4200", "7777"]
nid_words = ["GORU", "PAGLA", "BHAT", "MACH", "SAGOR", "MOJA", "TAKA", "CHA", "MAMA"]

def generate_nid():
    style = random.randint(1, 4)
    if style == 1:
        return f"{random.choice(nid_prefixes)}-{random.choice(nid_words)}-{random.randint(100, 999)}"
    elif style == 2:
        return f"NID-{random.randint(100000, 999999)} (probably expired)"
    elif style == 3:
        return f"{random.randint(1000, 9999)}-LOST-{random.randint(100, 999)}"
    else:
        return f"{random.choice(['Never registered', 'Sold for 2 kg rice', 'Eaten by goat'])} #{random.randint(1, 999)}"

# ============ FUNNY DATA LISTS ============
funny_locations = [
    "Next to Khalid's uncle's laundry shop, left at the banyan tree",
    "Sher-e-Bangla Stadium Toilet No. 3",
    "On the roof next to your house, behind the rose pot",
    "Google Maps went out for tea",
    "Behind the fish market (hold your nose)",
    "At Chaacha's tea stall, 3rd bench from left",
    "Where the stray dog sleeps at 2 PM daily",
    "In the village where electricity comes on Eid",
    "Top of the water tank (best view in town)",
    "Where two roads meet and both go nowhere"
]

funny_timezones = [
    "Bangladesh time (post-tea clock standard)",
    "GMT+6 but GMT is confused",
    "Clock runs 15 min late (village standard)",
    "Timezone: Biryani O'Clock",
    "Load-shedding Standard Time (LST)"
]

funny_carriers = [
    "Grameen Boro-Bhai", "BanglaLink (No Bangla, only Link)",
    "Robi Bhai's Tower (rent unpaid)", "Teletalk - Signal is on vacation",
    "Carrier found: It's a pigeon",
    "5G... wait no, 5 Taka package"
]

funny_extra = [
    "🛰️ Satellite connection: From the Moon (3 taka up, free down)",
    "📡 GPS locked... nah, lock broke, key lost",
    "🕵️ ISI, CIA, FBI all joined the video call",
    "🔋 Tracking machine battery: 1% (lend me a charger)",
    "🐄 Tracking by cow footprints: SUCCESS!",
    "🦟 Mosquito surveillance team deployed near the target",
    "🐦 Carrier pigeon has been promoted to 4G",
    "🍜 Target's last meal detected: Biryani (extra kuza)",
    "📡 Ping test: Ping... pong... target replied 'who this?'",
    "🐓 Rooster alarm analysis: Target wakes up at 11 AM instead"
]

# ============ BD COORDINATES (joke - clearly labeled) ============
def bd_coordinates():
    lat = round(random.uniform(21.5, 25.5), 6)
    lon = round(random.uniform(89.5, 92.5), 6)
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    return lat, lon, maps_link

# ============ MAIN ============
def main():
    clear()
    print(C.GREEN + C.BOLD + BANNER + C.RESET)
    slow_line("[*] Developed by Hayyan Da Edistein", 0.03, C.MAGENTA)

    slow_line("[*] Loading super secret spy system...", 0.05, C.MAGENTA)
    slow_line("[*] Connecting to 47 satellites... [███░░░░░░░] 30%", 0.03, C.YELLOW)
    slow_line("[*] Having tea... [██████████] 100% DONE ✅", 0.03, C.GREEN)
    print()

    phone = input(C.BOLD + C.CYAN + "📞 Enter mobile number (e.g: +88017xxxx or 88017xxxx): " + C.RESET).strip()

    if not phone:
        phone = "+88017CHAN-MIA"

    print()
    slow_line("[*] Querying international number database...", 0.04, C.MAGENTA)
    api_data = api_lookup(phone)
    time.sleep(0.5)
    print()

    # Coordinates (joke)
    lat, lon, maps_link = bd_coordinates()

    # Real data from API (or fallback)
    if api_data:
        real_name    = api_data.get("name") or generate_name()
        real_carrier = api_data.get("carrier") or random.choice(funny_carriers)
        country      = api_data.get("country") or "🇧🇩 Bangladesh"
        int_format   = api_data.get("international_format") or phone
        line_type    = api_data.get("line") or "mobile"
    else:
        real_name    = generate_name()
        real_carrier = random.choice(funny_carriers)
        country      = "🇧🇩 Bangladesh"
        int_format   = phone
        line_type    = "mobile"

    print(C.RED + C.BOLD + "╔══════════════════════════════════════════════╗")
    print("║   🎉 TRACKING 100% SUCCESSFUL (trust me,     ║")
    print("║   or don't, works either way) 🎉             ║")
    print("╚══════════════════════════════════════════════╝" + C.RESET)
    print()

    report = [
        ("📱 Phone Number    : ", phone),
        ("🌐 Int. Format     : ", int_format),
        ("👤 Name (DB)       : ", real_name),
        ("📶 Carrier (DB)    : ", real_carrier),
        ("🌍 Country (DB)    : ", country),
        ("🔌 Line Type (DB)  : ", line_type),
        ("🆔 NID (secret)    : ", generate_nid()),
        ("📍 Location        : ", random.choice(funny_locations)),
        ("🗺️ Coordinates     : ", f"{lat}, {lon} (random point in BD, totally made up!)"),
        ("🧭 Google Maps     : ", maps_link),
        ("⭐ Timezone        : ", random.choice(funny_timezones)),
        ("⚡ Speed           : ", f"{random.uniform(0.0001, 0.9999):.7f} seconds (world record!)"),
        ("🕒 Time            : ", time.strftime("%Y-%m-%d %H:%M:%S")),
        ("🎯 Confidence      : ", f"{random.randint(1, 100)}% (we made it up)"),
        ("👨‍👩‍👧 Family Members : ", f"{random.randint(2, 47)} people (all named Mama)"),
        ("💼 Occupation      : ", random.choice([
            "Professional Tea Drinker", "Facebook Comment Warrior",
            "Biryani Quality Inspector", "Retired Gossip Expert",
            "Full-time Boro Bhai", "Cricket Analyst (sofa division)"
        ])),
    ]

    for label, value in report:
        typewrite(label + str(value), 0.015, C.CYAN)
        time.sleep(0.1)

    print()
    slow_line("➕ Bonus Intel (top secret, definitely):", 0.04, C.GREEN)
    for line in random.sample(funny_extra, 5):
        slow_line("  " + line, 0.02, C.YELLOW)

    print()
    print(C.BOLD + C.RED + "⚠️  WARNING: NID, location & coordinates are FAKE jokes." + C.RESET)
    print(C.BOLD + C.YELLOW + "😂 Only name/carrier/country come from public lookup. For fun only!" + C.RESET)
    print(C.BOLD + C.GREEN + "Dev: Hayyan Da Edistein 🤣" + C.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + C.YELLOW + "[!] Tracking cancelled... the tea got cold ☕" + C.RESET)
