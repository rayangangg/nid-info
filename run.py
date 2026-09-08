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
    "মোজোর আলী (অব.)", "চান মিয়া", "গোপাল সিংহের চাচাতো ভাই",
    "হাসুর দাদু", "রহিম সেতুর মালিক (ভুয়া)", "ডন মুন্না বাহিনীর চায়ের বয়",
    "বিশ্বনাথের টুকু", "শাহজাহান মামা (রিকশা চালক সমিতি)"
]

funny_nids = [
    "১৯৯৪-গরু-০৭৩৩", "০০০০-নাং-০০০১", "আদমের সময়ের কার্ড",
    "NID খুঁজতে খুঁজতে হারিয়ে গেছে", "৫৫৫-পাগলা-৪২০",
    "ভর্তি হইনাই, খালি জায়গা"
]

funny_locations = [
    "খালেদার চাচার ধোপার দোকানের ঠিক পাশে, বাঁ হাতে গেলে বটগাছ",
    "ঢাকা ১০০০+ (ইন্টারনেটে দেখছি মিলে গেছে!)",
    "শেরেবাংলা স্টেডিয়ামের লেট্রিন নং ৩",
    "তোমার পাশের বাসার ছাদে, গোলাপ ফুলের টবের আড়ালে 👀",
    "গুগল ম্যাপস এখন চা খেতে গেছে"
]

funny_carriers = [
    "গ্রামীণ বড়ভাই", "বাংলালিংক (বাংলা না, লিংক আছে)",
    "রবি ভাইয়ের টাওয়ার ভাড়া বাকি", "টেলিটক - সিগন্যাল আজকাল ছুটিতে",
    "সিগন্যাল: ৪ বার (বার টিপার লোক বাদে)"
]

funny_extra = [
    "🛰️ স্যাটেলাইট কানেকশন: চাঁদ থেকে 🌕 (উঠতে ৩ টাকা, নামতে ফ্রি)",
    "📡 GPS লক করা হয়েছে... উঁহু, লক হয়নাই, তালা হারিয়ে গেছে",
    "🕵️ আইএসআই, সিআইএ, ফেডেরাল ব্যুরো সবাই মিশে গেছে ভিডিও কলে",
    "🔋 ট্র্যাকিং মেশিনের ব্যাটারি: ১% (চার্জার ধার দাও)",
    "🐄 গরুর পায়ের ছাপ অনুযায়ী ট্র্যাকিং: সফল!"
]

# ============ MAIN ============
def main():
    clear()
    print(C.GREEN + C.BOLD + BANNER + C.RESET)

    slow_line("[*] সুপার সিক্রেট গোপন স্পাই সিস্টেম লোড হচ্ছে...", 0.05, C.MAGENTA)
    slow_line("[*] হ্যাকার মোড চালু... [███░░░░░░░] ৩০%", 0.03, C.YELLOW)
    slow_line("[*] চা খেয়ে নিচ্ছি... [██████████] ১০০% ✅", 0.03, C.GREEN)
    print()

    phone = input(C.BOLD + C.CYAN + "📞 আপনার মোবাইল নম্বর দিন (যেমন: +88017xxxx): " + C.RESET).strip()

    if not phone:
        phone = "+88017চাচা-মিয়া"

    print()
    slow_line("[*] স্যাটেলাইটে সিগন্যাল পাঠানো হচ্ছে...", 0.06, C.MAGENTA)
    for dot in ["...", "..", "."]:
        sys.stdout.write(dot)
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

    print(C.RED + C.BOLD + "╔══════════════════════════════════════════════╗")
    print("║     🎉 ট্র্যাকিং ১০০% সফল (নিশ্চিত, বিশ্বাস   ║")
    print("║     করবেন না তবেও চলবে) 🎉                  ║")
    print("╚══════════════════════════════════════════════╝" + C.RESET)
    print()

    report = [
        ("📱 ফোন নাম্বার      : ", phone),
        ("👤 নাম              : ", random.choice(funny_names)),
        ("🆔 NID              : ", random.choice(funny_nids)),
        ("📍 লোকেশন           : ", random.choice(funny_locations)),
        ("📶 অপারেটর          : ", random.choice(funny_carriers)),
        ("⭐ টাইমজোন          : ", "বাংলাদেশ সময় (চায়ের পরের ঘড়া অনুযায়ী)"),
        ("🌍 দেশ              : ", "বাংলাদেশ (পৃথিবী, সৌরজগত, মিল্কিওয়ে)"),
        ("🗺️ Google Maps      : ", "লিংক পাঠালাম, কাউকে বলবেন না 😏 (লিংকটা আসলে ছিল না)"),
        ("⚡ স্পিড             : ", "০.০০০০০০১ সেকেন্ড (বিশ্বরেকর্ড!)"),
        ("🕒 সময়              : ", time.strftime("%Y-%m-%d %H:%M:%S")),
    ]

    for label, value in report:
        typewrite(label + str(value), 0.02, C.CYAN)
        time.sleep(0.15)

    print()
    slow_line("➕ বোনাস তথ্য:", 0.04, C.GREEN)
    for _ in range(3):
        slow_line("  " + random.choice(funny_extra), 0.025, C.YELLOW)

    print()
    print(C.BOLD + C.RED + "⚠️  সতর্কতা: এই রিপোর্টের একটা শব্দও সত্যি না।" + C.RESET)
    print(C.BOLD + C.YELLOW + "😂 এটা শুধু মজা/প্র্যাংকের জন্য। কারো সাথে ঠকানোর জন্য না!" + C.RESET)
    print(C.BOLD + C.GREEN + "বন্ধুকে দেখিয়ে হাসুন, স্ক্রিনশট নিন, শেষ! 🤣" + C.RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + C.YELLOW + "[!] ট্র্যাকিং বাতিল... কারণ চা ঠান্ডা হয়ে গেছে ☕" + C.RESET)
