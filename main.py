from pyscript import document


showcase_pages = {
    "Homepage (Seatwork 1)": "Club Member Checker",
    "Element Checker (Skills Test)": "Non-Metal Elements Info Finder",
    "School Club Members (Drill 2)": "Club Roster & Members",
    "Meet the Creator (Project)": "About Georgina Banal"
}


creator_profile = {
    "Name": "Georgina Florence B. Banal",
    "Section": "Grade 10 - Jade (OBMC Fairview)",
    "Hobbies": "Volleyball, Dance, Baking, Sleeping, Reading",
    "Dream": "Aviation / Aircraft Mechanic",
    "Favorite Quote": "She believed she could, so she did."
}


def load_creator_info():
    """Populates creator profile details and item count using dict and len()."""
  
    document.querySelector("#creator_name").innerText = creator_profile["Name"]
    document.querySelector("#creator_section").innerText = creator_profile["Section"]
    document.querySelector("#creator_hobbies").innerText = creator_profile["Hobbies"]
    document.querySelector("#creator_dream").innerText = creator_profile["Dream"]
    document.querySelector("#creator_quote").innerText = f"\"{creator_profile['Favorite Quote']}\""

  
    profile_total = len(creator_profile)
    document.querySelector("#creator_count").innerText = f"Profile Items: {profile_total}"


# Create a dictionary of non-metallic elements
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "HE": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "NE": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "CL": ("Chlorine", 17, 35.45)
}

# Create an event function
def periodic(e):
    element_Name = document.getElementById("element_input").value.strip().upper()

    # Look up dictionary
    var2 = non_metals.get(element_Name, ("Element not found", "-", "-"))

    # Display result
    document.getElementById("div_name").innerHTML = f"""
        Symbol: {element_Name}<br>
        Element: {var2[0]}<br>
        Atomic Number: {var2[1]}<br>
        Atomic Mass: {var2[2]}
    """

def checkmember(e):
    
    club_members = ["georgina banal", "adriana averilla", "isaias berdin", "cameron bufford", "carlos david"]
    
    first_name = document.getElementById("firstname").value.strip().lower()
    last_name = document.getElementById("lastname").value.strip().lower()
    full_name = f"{first_name} {last_name}"
    
    confirm_member = full_name in club_members
    
    message = ('Unfortunately, your name is not on the list.' , 'Congratulations! You are now part of the Theatre club. "Movies will make you famous... but theatre will make you good." — Terrence Mann')
    
    document.getElementById("output1").innerHTML = message[confirm_member]


def add_member(e):
    document.getElementById("output1").innerHTML = ""

    # Sets for each brand
    grade7 = {'Giorgio Armani', 'Thierry Hermès', 'Coco Chanel', 'Jeanne Lanvin'}
    grade8 = {'Yves Saint Laurent', 'Charles Lewis Tiffany', 'Sotirio Bulgari', 'Louis Vuitton'}
    grade9 = {'Cristóbal Balenciaga', 'Mario Prada', 'Guccio Gucci', 'Christian Dior'}
    grade10 = {'Pierre Balmain', 'Adele Fendi', 'Hubert de Givenchy', 'Valentino Garavani'}

    # Retrieve input values for first name and last name
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    # Combine first and last name and create a new set
    new_member_set = {f"{first_name} {last_name}"}

    # Combine all sets and the new member using union set operators (|)
    all_members_set = grade7 | grade8 | grade9 | grade10 | new_member_set

    total_members = len(all_members_set)

    member_list = "<br>".join(sorted(all_members_set))

    # Output
    document.getElementById("output1").innerHTML = f'All members:<br>{member_list}'
    display(f'Total members: {total_members}', target="output1")