import algorithm
import streamlit as st

#
def runAlgorithm(username, numOfRecs):
    algorithm.algo(username, numOfRecs)



def main():
    # title of the streamlit project
    st.title("AniMate")

    # allows the user to input their anilist username
    with st.form(key='my_form'):
        username = st.text_input("What is your Anilist username?")
        numOfRecs = st.text_input("How many shows do you want recommended?")
        button = st.form_submit_button('Submit')

    # starts the program with the given credential
    if button:
        runAlgorithm(username, numOfRecs)


if __name__ == "__main__":
    main()
