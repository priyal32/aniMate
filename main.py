import algorithm
import streamlit as st


# Replace these with your actual values
# client_id = 16520
# client_secret = 'dGG4W6p85SiLxywWPClXtKgY36WwIpCf2cAv9u48'
# redirect_uri = 'http://localhost:8501/callback'  # Adjust based on your setup
#
# app = Flask(__name__)
# access_token = '';
# @app.route('/')
# def index():
#     # Redirect the user to AniList for authorization
#     auth_url = f'https://anilist.co/api/v2/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
#     return redirect(auth_url)
#
#
# @app.route('/callback')
# def callback():
#     # Extract the authorization code from the callback URL
#     authorization_code = request.args.get('code')
#
#     # Exchange the authorization code for an access token
#     token_url = 'https://anilist.co/api/v2/oauth/token'
#     token_response = requests.post(
#         token_url,
#         data={
#             'client_id': client_id,
#             'client_secret': client_secret,
#             'grant_type': 'authorization_code',
#             'redirect_uri': redirect_uri,
#             'code': authorization_code
#         }
#     )
#
#     if token_response.status_code == 200:
#         # Parse the response JSON
#         token_data = token_response.json()
#
#         # Extract the access token
#         global access_token;
#         access_token = token_data.get('access_token')
#
#         # Use the access token as needed
#         print(f'Access Token: {access_token}')
#
#         return 'Access Token Obtained Successfully!'
#     else:
#         return f'Error: {token_response.status_code} - {token_response.text}'
#
#
#
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
