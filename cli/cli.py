import httpx
from ascii_art_coffee import ASCII_ARTS

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

console = Console()

ERROR_STYLE = "bold red"


def print_error(message: str) -> None:
    console.print(f"[{ERROR_STYLE}]{message}[/{ERROR_STYLE}]")

API_URL = "http://127.0.0.1:8000"

def print_banner():
    banner = r"""
    
  ____ ___  _____ _____ _____ _____    ____ _     ___ 
 / ___/ _ \|  ___|  ___| ____| ____|  / ___| |   |_ _|
| |  | | | | |_  | |_  |  _| |  _|   | |   | |    | | 
| |__| |_| |  _| |  _| | |___| |___  | |___| |___ | | 
 \____\___/|_|   |_|   |_____|_____|  \____|_____|___|  
                                                                                                                  
    """
    text = Text(banner, style = "bold green")
    console.print(text)
    

def fetch(endpoint: str, params: dict | None = None):
    url = f"{API_URL}{endpoint}"
    try:
        r = httpx.get(url, params=params, timeout=5)
        r.raise_for_status()
        return r.json()
    except httpx.ConnectError:
        print_error("[Error] Could not connect to the API server. Is it running?")
        console.print("Returning to main menu...", style="yellow")
        return None
    except httpx.HTTPStatusError as e:
        print_error(f"[Error] Server returned status {e.response.status_code}")
        return None
    except Exception as e:
        print_error(f"[Error] Unexpected error: {e}")
        return None
        
def print_recipe_table(data=None):
    if data is None:
        data = fetch('/recipes')

    table = Table(title="Coffee Recipes", show_header=True, header_style="bold light_salmon3")
    table.add_column("#", style="light_salmon3", no_wrap=True)
    table.add_column("Name", style="bold white")
    table.add_column("Method", style="green")
    table.add_column("Brew Time", style="light_salmon3")
    
    for i, r in enumerate(data, start=1):
        table.add_row(str(i), r['name'], r['method'], r['brew_time'])

    console.print(table)
    

def print_recipe_details(r):
    content = (
        f"[bold light_salmon3]{r['name']}[/bold light_salmon3]\n"
        f"Method: [green]{r['method']}[/green]\n"
        f"Brew Time: [yellow]{r['brew_time']}[/yellow]\n\n"
        f"[bold]Ingredients:[/bold]\n{r['ingredients']}\n\n"
        f"[bold]Steps:[/bold]\n{r['steps']}"
    )
    console.print(Panel(content, title="Recipe Details", border_style="blue"))
def show_all():
    print_recipe_table()
    

def filter_by_method():
    method = Prompt.ask(f"[green] Enter brewing method[/green] [light_salmon3](AeroPress, Cold Brew, French Press, V60)[/light_salmon3]")
    if not method:
        print_error("No method entered.")
        return
    data = fetch("/recipes/search", params={"method": method})
    if not data : 
        print_error(f"No recipes found for method: {method}")
        console.print("Returning to main menu...", style="yellow")
        return
    print_recipe_table(data)
    
    while True:
        detail = Prompt.ask(f"[green]Enter recipe number for details or q to quit: [/green]").strip()
        if detail.casefold() == "q":
            break
        if not detail.isdigit() or not (1 <= int(detail) <= len(data)):
            print_error("Invalid input. Please enter a valid recipe number or 'q' to quit.")
            continue
        index = int(detail) - 1
        r = data[index]
        print_recipe_details(r)

        
        
def filter_by_name():
    name = Prompt.ask(f"[green]Enter part of the recipe name to search: [/green]").strip()
    if not name:
        print_error("No name entered.")
        return
    data = fetch("/recipes/search", params={"name": name})
    if not data : 
        print_error(f"No recipes found with name containing: {name}")
        console.print("Returning to main menu...", style="yellow")
        return
    print_recipe_table(data)
        
    while True:
        detail = Prompt.ask(f"[green]Enter recipe number for details or q to quit: [/green]").strip()
        if detail.casefold() == "q":
            break
        if not detail.isdigit() or not (1 <= int(detail) <= len(data)):
            print_error("Invalid input. Please enter a valid recipe number or 'q' to quit.")
            continue
        index = int(detail) - 1
        r = data[index]
        print_recipe_details(r)
        
def filter_by_brew_time():
    input_time = Prompt.ask(f"[green]Enter maximum brew time in minutes: [/green]").strip()
    if not input_time.isdigit():
        print_error("Invalid input. Please enter a number.")
        return
    max_time = int(input_time) 
    data = fetch("/recipes/search", params={"max_time": max_time})
    if not data : 
        print_error(f"No recipes found with brew time under: {max_time} minutes")
        console.print("Returning to main menu...", style="yellow")
        return
    print_recipe_table(data)
        
    while True:
        detail = Prompt.ask(f"[green]Enter recipe number for details or q to quit: [green]").strip()
        if detail.casefold() == "q":
            break
        if not detail.isdigit() or not (1 <= int(detail) <= len(data)):
            print_error("Invalid input. Please enter a valid recipe number or 'q' to quit.")
            continue
        index = int(detail) - 1
        r = data[index]
        print_recipe_details(r)
        
    
    
        
def get_random_recipe():
    while True:
        r = fetch("/random-recipe")
        if not r:
            print_error("No recipe found.")
            console.print("Returning to main menu...", style="yellow")
            return

        # show the recipe nicely
        print_recipe_details(r)

        again = Prompt.ask("[green]Get another random recipe? (y/n)[/green]").strip().casefold()
        if again == "y":
            continue
        elif again == "n":
            return
        else:
            print_error("Invalid input. Please enter 'y' or 'n'.")
        
        

"""
def show_ascii_art():
    print("Coffee ASCII Art Gallery")
    print("========================")
    for i, art in enumerate(ASCII_ARTS, start=1):
        print(f"{i}. {art['title']}")
    print("0. Back")

    selection = input(f"[green]Choose an art to print (number or name): [/green]").strip()
    if selection == "0":
        return

    chosen = None
    if selection.isdigit():
        index = int(selection)
        if 1 <= index <= len(ASCII_ARTS):
            chosen = ASCII_ARTS[index - 1]
    else:
        normalized = selection.casefold()
        for art in ASCII_ARTS:
            if normalized in {art["key"], art["title"].casefold()}:
                chosen = art
                break

    if not chosen:
        print_error("No matching ASCII art found. Try again from the menu.")
        console.print("Returning to main menu...", style="yellow")
        return

    print("---")
    print(chosen["art"])
    print("---")
"""

def menu():
    console.print(Panel.fit(
        "[bold green]Coffee Recipe CLI[/bold green]\n[green]Choose an option below:[/green]",
        border_style="green"
    ))
    console.print("[1] List all recipes", style="light_salmon3")
    console.print("[2] Search recipes by method", style="light_salmon3")
    console.print("[3] Search recipes by name", style="light_salmon3")
    console.print("[4] Search recipes by max brew time", style="light_salmon3")
    console.print("[5] Get random recipe (no Cold Brew)", style="light_salmon3")
   # console.print("[6] Print coffee ASCII art", style="light_salmon3")
    console.print("[0] Exit", style="red")
    
    choice = input("> ")
    return choice.strip()

    
    

def main():
    while True:
        choice = menu()
        if choice == "1":
            show_all()
        elif choice == "2":
            filter_by_method()
        elif choice == "3":
            filter_by_name()
        elif choice == "4":
            filter_by_brew_time()
        elif choice == "5":
            get_random_recipe()
        #elif choice == "6":
       #     show_ascii_art()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print_error("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    print_banner()
    main()
    
