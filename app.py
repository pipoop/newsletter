import streamlit as st
from database import connect_2_db
from pymongo import MongoClient
import re


# Define a function for
# for validating an Email
def check(email):

    # Make a regular expression
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return "Valid Email"


def main():    
    st.set_page_config(page_title="AI newsletter", page_icon=":penguin:")
    st.title('Register for AI newsletter :penguin:')
    st.subheader('Join waiting list to test out new AI products')

    st.markdown("Demo by [Qiang Li](https://www.linkedin.com/in/qianglil/). All rights reserved.")

    # this markdown is for hiding "github" button
    st.markdown("<style>#MainMenu{visibility:hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<style>footer{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<style>header{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{display: none;} 
    </style>
    """,
    unsafe_allow_html=True
    )

    email = st.text_input("Please enter your email address")
    if st.button('Submit'):
        if check(email):    # for validating an Email
            # check if email is new
            users = connect_2_db()
            find_user = users.find_one({"email": email})
            if find_user:
                st.info("You have already registered for newsletter. Thank you!")
            else:
                users.insert_one({"email": email})
                st.success('Congratulations! You have successfully registered AI newsletter!')
        else:
            st.warning("Invalid Email")


if __name__ == '__main__':
    main()