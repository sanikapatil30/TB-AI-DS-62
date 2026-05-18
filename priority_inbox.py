import requests
from datetime import datetime
import heapq

API_URL = "http://4.224.186.213/evaluation-service/notifications"

HEADERS = {
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}

WEIGHT = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

TOP_N = 10

def fetch_notifications():
    response = requests.get(API_URL, headers=HEADERS)
    print("Status:", response.status_code)
    if response.status_code == 200:
        return response.json().get("notifications", [])
    else:
        print("Error:", response.text)
        return []

def get_score(n):
    w = WEIGHT.get(n["Type"], 0)
    t = datetime.strptime(n["Timestamp"], "%Y-%m-%d %H:%M:%S").timestamp()
    return (w, t)

def main():
    notifications = fetch_notifications()
    if not notifications:
        print("No notifications found.")
        return

    sorted_notifs = sorted(notifications, key=get_score, reverse=True)
    top10 = sorted_notifs[:TOP_N]

    print(f"\n TOP {TOP_N} PRIORITY NOTIFICATIONS\n")
    print(f"{'#':<4} {'Type':<12} {'Message':<35} {'Timestamp'}")
    print("-" * 75)
    for i, n in enumerate(top10, 1):
        print(f"{i:<4} {n['Type']:<12} {n['Message']:<35} {n['Timestamp']}")

if __name__ == "__main__":
    main()