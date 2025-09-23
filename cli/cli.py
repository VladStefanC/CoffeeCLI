import httpx 

API_URL = "http://127.0.0.1:8000"

def fetch(endpoint: str, params: dict | None = None) : 
    url = f"{API_URL}{endpoint}"
    r = httpx.get(url, params=params)
    r.raise_for_status()
    return r.json()

def show_all():
    data = fetch("/recipes")
    if not data :
        print("No recipes found.")
        return
    for i,r in enumerate(data, start= 1):
        print(f"{i}. {r['name']} ({r['method']}) - {r['brew_time']} - {r['ingredients']} - {r['steps']}")
        
def filter_by_method():
    method = input("Enter brewing method (e.g., AeroPress, Cold Brew, French Press, V60): ").strip()
    if not method:
        print("No method entered.")
        return
    data = fetch("/recipes/search", params={"method": method})
    if not data : 
        print(f"No recipes found for method: {method}")
        return
    for i,r in enumerate(data, start= 1):
        print(f"{i}. {r['name']} ({r['method']}) - {r['brew_time']}")
        


def menu():
    print("Coffee Recipe CLI")
    print("=================")
    print("1. List all recipes")
    print("2. Search recipes")
   #print("3. Get random recipe (no Cold Brew)")
    print("0. Exit")
    
    choice = input("Choose an option: ")
    return choice.strip()

def main():
    while True:
        choice = menu()
        if choice == "1":
            show_all()
        elif choice == "2":
            filter_by_method()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    