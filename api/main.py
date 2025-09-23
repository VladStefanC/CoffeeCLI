from fastapi import FastAPI
from typing import Optional
from recipes import recipes
import math
import random

app = FastAPI()

def parse_brew_time(time_str : str) -> int:
    #parse brew time string and return time in seconds
    if "-" in time_str:
        
        time_str = time_str.split("-")[-1].strip()
    
    if "h" in time_str:
        hours = int(time_str.replace("h", "").strip())
        return hours * 3600
    
    if ":" in time_str:
        minutes, seconds = time_str.split(":")
        return int(minutes) * 60 + int(seconds)

    return int(time_str) * 60 

@app.get("/")
def read_root():
    return {"message" : "Coffee API is alive!"}

@app.get("/recipes")
def list_recipes():
    return recipes 

@app.get("/recipes/search")
def query_recipes(method: Optional[str] = None, name: Optional[str] = None, max_time: Optional[int] = None):
    results = recipes  # start with full list
    if method:
        results = [r for r in results if r["method"].casefold() == method.casefold()]
     
    if name:
        search_words = name.strip().casefold().split()
        results = [
            r for r in results
            if all(word in r["name"].casefold() for word in search_words)
        ]
       
    
    if max_time: 
        limit = max_time * 60  # convert minutes to seconds
        results = [r for r in results if parse_brew_time(r["brew_time"]) <= limit ]
    
    

    return results


@app.get("/random-recipe")
def random_recipe():
    no_cold_brew = [] 
    for r in recipes:
        if r["method"].casefold() != "Cold Brew".casefold():
            no_cold_brew.append(r)
    random_index = random.randint(0, len(no_cold_brew) - 1)
    return no_cold_brew[random_index]


    return {"error": "No recipes available"}
            
    