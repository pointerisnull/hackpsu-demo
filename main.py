from chat import gpt_api
from window import *

def main():
    print("Welcome to the Cook'n'Eat, your digital cookbook assistant!")

    # Prompt user for ingredients
    open("ingredients.txt", "a")
    file = open("ingredients.txt", "r")
    ingredients = file.read()
    file.close()
    # Prompt user for cooking utensils
    open("appliances.txt", "a")
    file = open("appliances.txt", "r")
    utensils = file.read()
    file.close()

    api_key = "redacted"
    chatbot = gpt_api(api_key);
    chatbot.update(ingredients, utensils);
    chatbot.debug_print();

    root = tk.Tk()          # Create the main window
    app = Window(root, chatbot)      # Instantiate the Window class
    root.mainloop()         # Run the application

    """
    prompt = "\nWould you like to edit your pantry, see all possible meal prep options, or make a specific meal? (type (p) (l) or (s), or (q) to exit): "
    while True:
        # Prompt user for action
        action = input(prompt).strip().lower()
        if   action == 'p':
            ingredients = input("Please enter all the ingredients you have (separated by commas): ")
            file = open("ingredients.txt", "w")
            file.write(ingredients)
            file.close()
            
            utensils = input("Please enter all of the appliances you have (separated by commas): ")
            file = open("appliances.txt", "w")
            file.write(utensils)
            file.close()
        elif action == 'q':
            print("Exiting the application. Goodbye!")
            break
        elif action == 'l':
            print("Here are some meal prep options based on your ingredients and appliances:")
            response = chatbot.prompt_list();
            print(response)
            # Placeholder for meal prep options logic
        elif action == 's':
            meal = input("What would you like to make? ")
            # Placeholder for specific meal logic
            response = chatbot.prompt_specific(meal);
            print("Here's the recipe for {meal}:\n")
            print(response)
            
        else:
            print("Invalid input. Please type 'options', 'specific', or 'quit'.")
    """
if __name__ == "__main__":
    main()
