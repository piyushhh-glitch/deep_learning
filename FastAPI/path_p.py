from fastapi import FastAPI

app=FastAPI()

customer_risk_profiles={
    101:{"name":"Ravi Kumar", "risk":"low","score":0.12},
    102:{"name":"Raj Thube","risk":"high","score":0.89},
    103:{"name":"Parth Sawang","risk":"medium","score":0.5}
}

@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id:int):
    if customer_id not in customer_risk_profiles:
        return {"error":f"{customer_id}, not found"}

    profile=customer_risk_profiles[customer_id]

    return {
        "Customer_id":customer_id,
        "Name":profile["name"],
        "Risk":profile["risk"],
        "Score":profile["score"]

    }

@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name:str,customer_id:int):
    return {
        "Model_Name":model_name,
        "Customer_id":customer_id,
        "Risk":"High"
    }
    