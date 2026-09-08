#!/usr/bin/env python3
import random
import time
import os
import sys

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
"""

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

# ============ FUNNY FAKE DATA ============
funny_names = [
    "Mojor Ali (Retd.)", "Chan Mia", "Gopal Singh's Cousin",
    "Hasu's Grandpa", "Rahim Setu Owner (Fake)", "Don Munna Bahini's Tea Boy",
    "Bishwanath's Tuku", "Shahjan Mama (Rickshaw Puller Union)"
]

funny_nids = [
    "1994-GORU-0733", "0000-PAGLA-0001", "Adam's Era Card",
    "NID got lost while searching", "555-PAGLA-420",
    "Never registered, empty space"
]

funny_locations = [
    "Next to Khalid's uncle's laundry shop, left at the banyan tree",
    "Dhaka 1000+ (checked on internet, it matched!)",
    "Sher-e-Bangla Stadium Toilet No. 3",
    "On the roof next to your house, behind the rose pot 👀",
    "Google Maps went out for tea"
]

funny_carriers = [
    "Grameen Boro-Bhai", "BanglaLink (No Bangla, only Link)",
    "Robi Bhai's Tower (rent unpaid)", "Teletalk - Signal is on vacation",
    "Signal: 4 bars (excluding tip-wallas)"
]

funny_extra = [
    "🛰️ Satellite connection: From the Moon 🌕 (3 taka up, free down)",
    "📡 GPS locked... nah, lock broke, key lost",
    "🕵️ ISI, CIA, FBI all joined the video call",
    "🔋 Tracking machine battery: 1% (lend me a charger)",
    "🐄 Tracking by cow footprints: SUCCESS!"
]

# ============ MAIN ============
def main():
    clear()
    print(C.GREEN + C.BOLD + BANNER + C.RESET)

    slow_line("[*] Loading super secret spy system...", 0.05, C.MAGENTA)
    slow_line("[*] Hacker mode ON... [███░░░░░░░] 30%", 0.03, C.YELLOW)
    slow_line("[*] Having tea... [██████████] 100% DONE ✅", 0.03, C.GREEN)
    print()

    phone = input(C.BOLD + C.CYAN + "📞 Enter mobile number (e.g: +88017xxxx): " + C.RESET).strip()

    if not phone:
        phone = "+88017CHAN-MIA"

    print()
    slow_line("[*] Sending signal to satellite...", 0.06, C.MAGENTA)
    for dot in ["...", "..", "."]:
        sys.stdout.write(dot)
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

    print(C.RED + C.BOLD + "╔══════════════════════════════════════════════╗")
    print("║   🎉 TRACKING 100% SUCCESSFUL (trust me,     ║")
    print("║   or don't, works either way) 🎉             ║")
    print("╚══════════════════════════════════════════════╝" + C.RESET)
    print()

    report = [
        ("📱 Phone Number    : ", phone),
        ("👤 Name            : ", random.choice(funny_names)),
        ("🆔 NID             : ", random.choice(funny_nids)),
        ("📍 Location        : ", random.choice(funny_locations)),
        ("📶 Operator        : ", random.choice(funny_carriers)),
        ("⭐ Timezone        : ", "Bangladesh time (post-tea clock standard)"),
        ("🌍 Country         : ", "Bangladesh (Earth, Solar System, Milky Way)"),
        ("🗺️ Google Maps     : ", "Link sent, don't tell anyone 😏 (there was no link)"),
        ("⚡ Speed           : ", "0.0000001 seconds (world record!)"),
        ("🕒 Time            : ", time.strftime("%Y-%m-%d %H:%M:%S")),
    ]

    for label, value in report:
        typewrite(label + str(value), 0.02, C.CYAN)
        time.sleep(0.15)

    print()
    slow_line("➕ Bonus info:", 0.04, C.GREEN)
    for _ in range(3):
        slow_line("  " + random.choice(funny_extra), 0.025, C.YELLOW)

    print()
    print(C.BOLD + C.RED + "⚠️  WARNING: Not a single word in this report is true." + C.RESET)
    print(C.BOLD + C.YELLOW + "😂 For fun/prank only. Not for scamming anyone!" + C.RESET)
    print(C.BOLD + C.GREEN + "Show your friends, take a screenshot, done! 🤣" + C.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + C.YELLOW + "[!] Tracking cancelled... the tea got cold ☕" + C.RESET)
