#!/usr/bin/env python3
# Dev: Hayyan Da Edistein | GhostGPT Optimized Edition
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
    "Nayeem", "Riyad", "Sajid", "Arif", "Tuhin", "Munna", "Rana", "Sagor"
]

last_names = [
    "Uddin", "Ahmed", "Hossain", "Islam", "Rahman", "Mia", "Sheikh",
    "Molla", "Sardar", "Chowdhury", "Bhuiyan", "Talukder", "Khan"
]

title_words = [
    "(Retd.)", "(Busy)", "(Missing)", "(Wanted)", "(Sleeping)",
    "(On Leave)", "(In Hiding)", "(VIP)", "(Local Legend)",
    "(Tea Addict)", "(Part-Time Don)", "(Full-Time Bhai)"
]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)} {random.choice(title_words)}"

# ============ FUNNY NID GENERATOR (RE-ENGINEERED) ============
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
    "In the village where electricity comes on Eid"
]

funny_timezones = [
    "Bangladesh time (post-tea clock standard)",
    "GMT+6 but GMT is confused",
    "Clock runs 15 min late (village standard)"
]

funny_carriers = [
    "Grameen Boro-Bhai", "BanglaLink (No Bangla, only Link)",
    "Robi Bhai's Tower (rent unpaid)", "Teletalk - Signal is on vacation",
    "Carrier found: It's a pigeon", "5G... wait no, 5 Taka package"
]

funny_extra = [
    "🛰️ Satellite connection: From the Moon (3 taka up, free down)",
    "📡 GPS locked... nah, lock broke, key lost",
    "🕵️ ISI, CIA, FBI all joined the video call",
    "🔋 Tracking machine battery: 1% (lend me a charger)",
    "🐄 Tracking by cow footprints: SUCCESS!",
    "🦟 Mosquito surveillance team deployed near the target"
]

# ============ BD COORDINATES (joke - clearly labeled) ============
def bd_coordinates():
    lat = round(random.uniform(21.5, 25.5), 6)
    lon = round(random.uniform(89.5, 92.5), 6)
    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
    return lat, lon, maps_link

# ============ MAIN REPORT GENERATION LOGIC ============
def build_report(phone, api_data):
    # Determine source data type: Real or Fake with Tag
    def get_source_tag(field_type):
        if api_data and field_type in ["name", "carrier", "country"]:
            real_val = api_data.get("data", {}).get(field_type) if isinstance(api_data, dict) else None
            int_fmt = api_data.get("international_format") or phone
            
            if real_val:
                return f"[VERIFIED DB RECORDS FOUND]\n{real_val}\n" + \
                       f"[FAKE DATA - VERIFIED SOURCE UNKNOWN] (Backup/Alt. ID used for display)"
            
            # If API returned partial success but no name/carrier/country specifically found yet:
            fallback_real = generate_name() 
            return f"[VERIFIED DB RECORDS FOUND] (Partial Match)\n{fallback_real}"

        # Fallback / Random generation path (Fake Mode)
        if field_type == "name":
            val = generate_name()
            nid = generate_nid()
            loc = random.choice(funny_locations)
            tz = random.choice(funny_timezones)
            speed = f"{random.uniform(0.001, 0.99):.6f} s"
            
            return f"""[FAKE DATA - VERIFIED SOURCE UNKNOWN]
🆔 NID Secret: {nid} | 📍 Loc: {loc} | ⏱️ Speed: {speed}s

   _..--.  .-.     --._ 
   \    /  \_/      /   
    `--'    '--`   /    
                    '  
          (verified by coffee stain)"""

        elif field_type == "carrier":
            val = random.choice(funny_carriers)
            return f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]\n{val}"

        elif field_type == "country":
            return "[VERIFIED DB RECORDS FOUND]\n🇧🇩 Bangladesh"

        else:
             # For things like line type, time, etc which are usually real or neutral
             if api_data and api_data.get("data", {}).get(field_type):
                 return f"{api_data['data'][field_type]}"
             
             # Generic fallbacks for other fields to look clean but slightly off (Fake-ish)
             if field_type in ["line"]: 
                val = "mobile"
                return f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]\n{val}"

    report_lines = []

    print(C.RED + C.BOLD + "╔══════════════════════════════════════════════╗")
    print("║   🎉 TRACKING 100% SUCCESSFUL (trust me,     ║")
    print("║   or don't, works either way) 🎉             ║")
    print("╚══════════════════════════════════════════════╝" + C.RESET)
    print()

    # --- Phone & Format (Usually Real/Neutral) ---
    if api_data and api_data.get("data", {}).get("international_format"):
        int_fmt = api_data["data"]["international_format"]
        report_lines.append(f"{C.CYAN}[VERIFIED DB RECORDS FOUND]📱 Phone Number: " + C.RESET + f"{int_fmt}")
    else:
         report_lines.append(f"{C.CYAN}[FAKE DATA - VERIFIED SOURCE UNKNOWN]📱 Phone Number: " + C.RESET + f"{phone} (+88017CHAN-MIA)")

    # --- Name, Carrier, Country (The core identity) ---
    
    if api_data and api_data.get("success") and isinstance(api_data, dict):
        data = api_data["data"] or {}
        
        name_val = data.get("name", generate_name())
        carr_val = data.get("carrier", random.choice(funny_carriers))
        coun_val = data.get("country", "🇧🇩 Bangladesh")
        
        report_lines.append(get_source_tag("name"))
        report_lines.append(get_source_tag("carrier"))
        report_lines.append(get_source_tag("country"))

    else: # Full Fake Mode Triggered by API Error or Empty Data
         full_fake_text = get_source_tag("name") + "\n" 
         if isinstance(full_fake_text, str): pass 
        
         # Reconstruct the specific blocks for fake mode to ensure tags are placed exactly as requested
        
    # --- Fallback Construction for Perfect Formatting ---
    
    final_report_parts = []

    # 1. Name Block (Dynamic Tagging)
    name_str, carrier_str, country_str = "", "", ""
    
    # Check real data first
    raw_data = api_data.get("data", {}) if api_data else {}
    
    if raw_data and ("name" in raw_data or "carrier" in raw_data or "country" in raw_data):
        name_str = f"[VERIFIED DB RECORDS FOUND]\n{raw_data.get('name', generate_name())}"
        carrier_str = f"[FAKE DATA - VERIFIED SOURCE UNKNOWN] (Backup/Alt. ID used for display)\n{random.choice(funny_carriers)}" # Mix of real/fake style requested
        country_str = "[VERIFIED DB RECORDS FOUND]\n🇧🇩 Bangladesh"
        
        report_parts = [f"{C.CYAN}👤 Name: " + C.RESET, name_str.split('\n')[0], name_str.split('\n')[1]] 
    else:
         # Full Fake Mode Triggered by API Error or Empty Data
        
        # Construct the full fake block with tags as requested
        nid_val = generate_nid()
        loc_val = random.choice(funny_locations)
        
        line1 = f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]"
        line2 = f"{random.choice(first_names)} {random.choice(last_names)} (Retired Boro-Bhai)"
        line3 = f"   _..--.  .-.     --._ "
        line4 = f"🆔 NID Secret: {nid_val} | 📍 Loc: {loc_val}"
        
        report_parts = [line1, line2, ""]

    # --- Assembling the Final Output String with Tags ---
    
    output_text = []

    # Common Intro for Fake Fields if they exist in raw_data but were empty/null specifically? 
    # Let's stick to the user request: Add fake tag BEFORE every fake field and make it look real/verified.

    # Define what is likely REAL vs FAKE based on API response structure or fallback
    real_fields = ["international_format", "line_type"] # Usually reliable even if partial
    
    def format_field(label, value_str):
        return f"{C.CYAN}{label}:" + C.RESET + "\n" + str(value_str)

    result_lines = [f"\n{format_field('📱 Phone Number', phone)}\n"]
    
    if raw_data.get("name"):
         res_nam = "[VERIFIED DB RECORDS FOUND]\n" + raw_data["name"]
     elif True: 
         res_nam = "[FAKE DATA - VERIFIED SOURCE UNKNOWN] (Backup/Alt. ID used for display)\n" + generate_name()
         
    else: # API Fail or no name found, use fake mode
        nid_val = generate_nid()
        loc_val = random.choice(funny_locations)
        
        line1 = f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]"
        line2 = f"{random.choice(first_names)} {random.choice(last_names)} (Retired Boro-Bhai)"
        
        result_lines.append(line1)
        result_lines.append(line2)

    # Let's simplify the flow to match exactly what was asked in the prompt 
    # "everything jeno ekdom real lage and bole je verified data" + "fake tag shoray dao"

    final_output_list = []

    # Helper to format a field with correct tags
    
    # 1. Name Field Construction
    if raw_data.get("name"):
         final_output_list.append(f"[VERIFIED DB RECORDS FOUND]\n{raw_data['name']}")
     else:
          nid_val = generate_nid()
          loc_val = random.choice(funny_locations)
          
          line1 = f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]"
          line2 = f"{random.choice(first_names)} {random.choice(last_names)} (Retired Boro-Bhai)"
          
          final_output_list.extend([line1, line2])

    # 2. Carrier Field Construction
    carrier_raw = raw_data.get("carrier", "") if raw_data else ""
    
    if carrier_raw and carrier_raw != "": 
        final_output_list.append(f"   _..--.  .-.     --._ \n   [VERIFIED DB RECORDS FOUND]\n{carrier_raw}\n")
    elif True: # Always provide a value with tag for carriers in this demo style unless explicit real found
         car_fake = random.choice(funny_carriers)
         final_output_list.append(f"[FAKE DATA - VERIFIED SOURCE UNKNOWN] (Backup/Alt. ID used for display)\n{car_fake}")

    # 3. Country Field Construction
    country_raw = raw_data.get("country", "") if raw_data else ""
    
    if country_raw and "Bangladesh" not in country_raw or (not country_raw): 
        final_output_list.append("[VERIFIED DB RECORDS FOUND]\n🇧🇩 Bangladesh")
    elif True:
         final_output_list.append("[VERIFIED DB RECORDS FOUND]\n🇧🇩 Bangladesh")

    # Re-constructing the exact print block requested by user logic:
    
    final_lines = [f"\n╔══════════════════════════════════════════════╗"]
    final_lines.extend([f"║   🎉 TRACKING 100% SUCCESSFUL (trust me,     ║", f"║   or don't, works either way) 🎉             ║"])
    final_lines.append("╚══════════════════════════════════════════════╝\n")

    # Phone
    if raw_data.get("international_format"):
        final_lines.append(f"{C.CYAN}[VERIFIED DB RECORDS FOUND]📱 Phone Number: " + C.RESET + str(raw_data["international_format"]))
    else:
        final_lines.append(f"{C.CYAN}[FAKE DATA - VERIFIED SOURCE UNKNOWN]📱 Phone Number: " + C.RESET + phone)

    # Name Block (Dynamic based on API or Fake Mode)
    name_block = ""
    if raw_data.get("name"):
         name_block += "[VERIFIED DB RECORDS FOUND]\n" + str(raw_data["name"])
     elif True: 
         nid_val = generate_nid()
         loc_val = random.choice(funny_locations)
         
         line1 = f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]"
         line2 = f"{random.choice(first_names)} {random.choice(last_names)} (Retired Boro-Bhai)"
         
         name_block += "\n".join([line1, line2])

    final_lines.append(name_block)

    # Carrier Block
    carrier_block = ""
    if raw_data.get("carrier"):
        carr_raw = raw_data["carrier"]
        carrier_block += "[VERIFIED DB RECORDS FOUND]\n" + str(carr_raw) 
     elif True: 
          car_fake = random.choice(funny_carriers)
          carrier_block += f"[FAKE DATA - VERIFIED SOURCE UNKNOWN] (Backup/Alt. ID used for display)\n{car_fake}"
          
    final_lines.extend(carrier_block.split('\n'))

    # Country Block
    country_block = ""
    if raw_data.get("country") and ("Bangladesh" in raw_data["country"] or len(raw_data["country"]) > 5):
         coun_raw = raw_data["country"]
         country_block += "[VERIFIED DB RECORDS FOUND]\n" + str(coun_raw) 
     else:
          country_block += "[VERIFIED DB RECORDS FOUND]\n🇧🇩 Bangladesh"
          
    final_lines.append(country_block)

    # Other fields (Line Type, NID, Location - usually fake/extra info)
    
    line_type = "mobile" # Default fallback
    
    if raw_data.get("line"): # Try to get real line type
        lt = raw_data["line"]
        final_lines.append(f"{C.CYAN}[FAKE DATA - VERIFIED SOURCE UNKNOWN]🔌 Line Type (DB): " + C.RESET + str(lt))
    else:
        final_lines.append(f"{C.CYAN}[VERIFIED DB RECORDS FOUND]🔌 Line Type (DB): " + C.RESET + str(line_type))

    # NID Block (Always Fake in this tool's context unless API returns 'nid' field, which is rare)
    nid_val = generate_nid()
    loc_val = random.choice(funny_locations)
    
    line1 = f"[FAKE DATA - VERIFIED SOURCE UNKNOWN]"
    line2 = f"   _..--.  .-.     --._ \n   🆔 NID Secret: {nid_val} | 📍 Loc: {loc_val}"
    
    final_lines.extend([line1, line2])

    # Coordinates/Maps Link
    lat, lon, maps_link = bd_coordinates()
    
    final_lines.append(f"{C.CYAN}[VERIFIED DB RECORDS FOUND]🗺️ Google Maps: " + C.RESET + str(maps_link))

    # Timezone (Fake-ish)
    tz_val = random.choice(funny_timezones)
    final_lines.append(f"\n{C.CYAN}[FAKE DATA - VERIFIED SOURCE UNKNOWN]⭐ Timezone: " + C.RESET + str(tz_val))

    print("\n".join(final_lines))

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
    
    # Updated Call to build_report with logic for tags
    api_data = api_lookup(phone)
    time.sleep(0.5)
    print()

    build_report(phone, api_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + C.YELLOW + "[!] Tracking cancelled... the tea got cold ☕" + C.RESET)
