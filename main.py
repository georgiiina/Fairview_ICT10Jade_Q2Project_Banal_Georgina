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