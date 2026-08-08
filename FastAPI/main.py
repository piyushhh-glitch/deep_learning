from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"My first api is working"}

@app.get("/about")
def about():
    return {"This is a women safety app"}

@app.get("/contact")
def contact():
    return {"Contact number":"881990000"}

@app.get("/customer")
def get_customer(customer_id:int)->int:
    return {
        "customer_id":customer_id,
        "name":"ravi",
        "status":"active"
    }