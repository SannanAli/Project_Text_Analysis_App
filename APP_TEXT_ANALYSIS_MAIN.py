import streamlit as st
from app_home import home
import streamlit.components.v1 as stc


HTML_BANNER = """
    <div style="background-color:#3872fb;padding:10px;border-radius:10px;border-style:ridge;">
    <h1 style="color:white;text-align:center;">Text Analysis NLP App </h1>
    </div>
    """
def main():

    # st.title(':red[TEXT ANALYSIS NLP] :point_down:')

    stc.html(HTML_BANNER)

    menu = [ 'HOME',"ABOUT"]
    choices = st.sidebar.selectbox('Menu',menu)

    if choices == 'HOME':
        home()
    else:
        st.title(':blue[ABOUT]')

    





if __name__ == '__main__':
    main()