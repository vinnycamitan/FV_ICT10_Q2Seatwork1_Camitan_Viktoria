
from pyscript import document, display

club_members = [
    "Angela Lee",
    "Allen Camitan",
    "Rhyzza Fallore",
    "Nicole Semana",
    "Jhoana Evangelista "
    
]

def check_name(event):
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()

    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    message = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are a certified member of the ICT club.ּ֯ . ❥ ּ֯꒱"
    ][is_member]

    document.querySelector("#result").innerText = message
