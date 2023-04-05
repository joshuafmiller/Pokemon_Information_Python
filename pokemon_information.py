
while True:

    import requests

    #getting the user input and creating the url
    user_input = input("What pokemon would you like information about? Type exit to leave program.  ")
    url = f"https://pokeapi.co/api/v2/pokemon/{user_input}"

    #making the api request and converting to lowercase/removing whitespace to avoid any errors
    #converting response to a dict

    #exit option

    if user_input.strip() == "":
        print("No information provided, please try again")
        continue

    if user_input.lower().strip() == "exit":
        print("Exiting program...")
        break


    req = requests.get(url.lower().strip())

    if req.status_code == 200 and url != "https://pokeapi.co/api/v2/pokemon/":
        pokemon = req.json()

        #showing output to the user
        print(f"Pokemon name: {pokemon['name']}")
        print(f"Pokemon weight: {pokemon['weight']}")
        print(f"Pokemon height: {pokemon['height']}")
        print("This pokemon appeared in the following games:")

        #looping through the dictionary to pull nested data and dump it into an empty list
        #the goal here is to pull just the name of the game this pokemon was present in
        games = pokemon['game_indices']

        i = 1 
        for version in games:
            print(f"{i}. {version['version']['name']}")
            i = i+1


    else:
        print("Please enter a valid pokemon name")

