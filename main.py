try:
    from pyscript import document
except ImportError:
    from js import document

from html import escape


non_metals = {
    "Hydrogen": ("H", 1, "1.008"),
    "Helium": ("He", 2, "4.0026"),
    "Carbon": ("C", 6, "12.011"),
    "Nitrogen": ("N", 7, "14.007"),
    "Oxygen": ("O", 8, "15.999"),
    "Fluorine": ("F", 9, "18.998"),
    "Neon": ("Ne", 10, "20.180"),
    "Phosphorus": ("P", 15, "30.974"),
    "Sulfur": ("S", 16, "32.06"),
    "Chlorine": ("Cl", 17, "35.45"),
    "Argon": ("Ar", 18, "39.948"),
    "Selenium": ("Se", 34, "78.971"),
    "Bromine": ("Br", 35, "79.904"),
    "Krypton": ("Kr", 36, "83.798"),
    "Iodine": ("I", 53, "126.90"),
    "Xenon": ("Xe", 54, "131.29"),
    "Radon": ("Rn", 86, "[222]"),
}


def find_element(event=None):
    result = document.getElementById("result")
    result.innerHTML = ""

    entered_element = document.getElementById("element").value.strip()
    element1 = next(
        (
            name
            for name, details in non_metals.items()
            if details[0].lower() == entered_element.lower()
        ),
        entered_element.title(),
    )

    if element1 not in non_metals:
        result.innerHTML = (
            f"<b>Element</b> {escape(entered_element or '—')}<br>"
            "<b>Status</b> Element not found"
        )
        return

    symbol, atomic_number, atomic_mass = non_metals[element1]

    result.innerHTML = f"""
        <b>Symbol</b> {symbol}<br>
        <b>Element</b> {element1}<br>
        <b>Atomic Number</b> {atomic_number}<br>
        <b>Atomic Mass</b> {atomic_mass}
    """
