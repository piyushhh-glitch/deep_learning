from fastapi import FastAPI

app=FastAPI()

all_customers=[
  {"id": 1, "name": "Aarav Sharma", "city": "Pune", "risk": "low"},
  {"id": 2, "name": "Priya Mehta", "city": "Mumbai", "risk": "high"},
  {"id": 3, "name": "Rahul Verma", "city": "Delhi", "risk": "medium"},
  {"id": 4, "name": "Sneha Patil", "city": "Bangalore", "risk": "medium"},
  {"id": 5, "name": "Arjun Kapoor", "city": "Hyderabad", "risk": "high"},
  {"id": 6, "name": "Neha Joshi", "city": "Bangalore", "risk": "medium"}
]

@app.get("/customer")
def get_customers(city:str,risk:str):
    filtered=[
        c for c in all_customers
        if c["city"]==city and c["risk"]==risk
    ]

    return {
        "city":city,
        "risk":risk,
        "count":len(filtered),
        "result":filtered
    }