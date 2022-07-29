import streamlit as st


pokemon_catolog = {
    "Bulbasaur": {
        "file": "bulbasaur.png",
        "type": "Grass Poison",
    },
    "Ivysaur": {
        "file": "ivysaur.png",
        "type": "Grass Poison",
    },
    "Venusaur": {
        "file": "venusaur.png",
        "type": "Grass Poison",
    },
    "Grandmasaur": {
        "file": "venusaur.png",
        "type": "Fire Dark",
    },
    "Charmander": {
        "file": "charmander.png",
        "type": "Fire",
    },
    "Charmeleon": {
        "file": "charmeleon.png",
        "type": "Fire",
    },
    "Charizard": {
        "file": "charizard.png",
        "type": "Fire Flying",
    },
    "Lumberaxe": {
        "file": "lumberaxe.png",
        "type": "Grass",
    },
}


def main():
    st.title("Henry's Pokedex")
    with st.sidebar:
        pokemon = st.radio("Select Pokemon", pokemon_catolog.keys(), key="pokemon")
    st.title(pokemon)
    st.image(pokemon_catolog[pokemon]["file"])
    st.markdown(f"Type: **{pokemon_catolog[pokemon]['type']}**")


main()
