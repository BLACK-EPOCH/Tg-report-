import time
import random

def show_logo():
    logo = r"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

███████╗██████╗░░█████╗░░█████╗░██╗░░██╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
█████╗░░██████╔╝██║░░██║██║░░╚═╝███████║
██╔══╝░░██╔═══╝░██║░░██║██║░░██╗██╔══██║
███████╗██║░░░░░╚█████╔╝╚█████╔╝██║░░██║
╚══════╝╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝
"""
    print(logo)

def display_loading_effect(duration=3, message="Initializing system"):
    """লোডিং ইফেক্ট দ্রুত প্রদর্শন"""
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in ['.', '..', '...']:
            print(f"\r{message}{char}", end='', flush=True)
            time.sleep(0.5)
    print("\r", end='')

def is_valid_telegram_link(link):
    """টেলিগ্রাম লিংক যাচাই"""
    return link.startswith("https://t.me/") or link.startswith("http://t.me/")

def simulate_report_attacks(report_type, link):
    """রিপোর্ট সিমুলেশন"""
    print(f"\n🚀 Starting Telegram {report_type} Report Attack on: {link}\n")
    time.sleep(1)

    report_categories = [
        "🔴 Spam Report",
        "🛑 Abusive Content Report",
        "⚠️ Fake Account Report",
        "🚫 Copyright Violation Report",
        "🔒 Phishing/Malware Report",
        "📵 Unauthorized Selling Report",
        "❌ Violence/Harassment Report",
        "⚡ Scam Report",
        "🔥 Terrorism Propaganda Report",
    ]

    for _ in range(500):
        category = random.choice(report_categories)
        print(f"{category} sent successfully!")
        time.sleep(random.uniform(0.1, 0.2))

def main():
    show_logo()  # লোগো দেখানো

    print("=" * 50)
    print("          🛡️ Telegram Report Tool 🛡️           ")
    print("                 Version: 5.1                   ")
    print("=" * 50)

    display_loading_effect(duration=3, message="Initializing system")

    print("\nChoose an attack target:")
    print("1. Telegram Channel Report")
    print("2. Telegram Group Report")
    print("-" * 50)

    choice = input("Enter your choice (1/2): ").strip()
    if choice == '1':
        report_type = "Channel"
        print("\n🛡️ Target selected: Telegram Channel Report Attack\n")
    elif choice == '2':
        report_type = "Group"
        print("\n🛡️ Target selected: Telegram Group Report Attack\n")
    else:
        print("\n❌ Invalid choice. Exiting program.\n")
        return

    while True:
        link = input(f"Enter the Telegram {report_type} link (e.g., https://t.me/example): ").strip()
        if is_valid_telegram_link(link):
            print("\n✅ Valid Telegram link detected!\n")
            break
        else:
            print("❌ Invalid link. Please enter a valid Telegram link starting with 'https://t.me/'.\n")

    display_loading_effect(duration=3, message="Preparing to launch reports")
    simulate_report_attacks(report_type, link)

# ✅ সঠিকভাবে এন্ট্রি পয়েন্ট
if __name__ == "__main__":
    main()
