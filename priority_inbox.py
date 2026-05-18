import requests
from datetime import datetime
import heapq

API_URL = "http://4.224.186.213/evaluation-service/notifications"

HEADERS = {
   "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzYW5pa2FwNTk5OEBnbWFpbC5jb20iLCJleHAiOjE3NzkxMDMxMzQsImlhdCI6MTc3OTEwMjIzNCwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6IjRmMThlNWRlLTYyNGEtNGRlZS1iMmNhLWE3MGI3NzBmZjgwYiIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6InNhbmlrYSBwYXRpbCIsInN1YiI6IjFlNmEwZWNlLWM0ZDMtNGFjMy04M2U3LTdmN2M5MTYyYjY5MiJ9LCJlbWFpbCI6InNhbmlrYXA1OTk4QGdtYWlsLmNvbSIsIm5hbWUiOiJzYW5pa2EgcGF0aWwiLCJyb2xsTm8iOiJ0Yi1haVx1MDAyNmRzLTYyIiwiYWNjZXNzQ29kZSI6ImZ6RVFTUSIsImNsaWVudElEIjoiMWU2YTBlY2UtYzRkMy00YWMzLTgzZTctN2Y3YzkxNjJiNjkyIiwiY2xpZW50U2VjcmV0IjoidHRNVHR6YUVwY0dZZ1JUYyJ9.eT5HhRuNxoRHjpxZ1VoM7HrOE8Ew7rodt5Hin7yiJVY"
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