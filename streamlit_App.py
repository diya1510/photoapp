import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title='photoapp', page_icon=":camera:",layout="wide")


with st.sidebar:
    sltd = option_menu(
        menu_title="Navigation",
        options=["Main","Photo","Video"],
        icons=["info-circle","camera2","film"],
        menu_icon = "grid"

    )
if sltd == "Main":
    st.subheader("Welcome to photoapp :camera: ")
    st.title("Webapp to upload Photos and Videos ")
    def load_lottie(url):
        r= requests.get(url)
        if r.status_code != 200:
          return None 
        return r.json()
    
    lottie_coding = load_lottie("https://assets7.lottiefiles.com/packages/lf20_GxMZME.json")
     
    st_lottie(lottie_coding,height=400)
    st.write('''
    This webapp is created by me, Pratyasha Panda of Department of Information Technology, First Year.
    This webapp allows the user to either upload the desired Photo or Video from Local files or from Webcam directly.
    This is the first time I've created an webapp using Streamlit so your feedbacks and critiques are highly welcomed.
    
    Kindly select Photo or Video from the Navigation Menu to proceed with the webapp.
    
    ''')

if sltd == "Photo":
    st.title("Upload Photo 🎞 ")
    st.markdown("---")
    sltd = option_menu(
        menu_title="Choose the path to proceed ",
        options=["Upload from Local Files","Capture using Webcam"],
        icons=["file-earmark-image","webcam"],
        menu_icon ="circle-square",
        orientation="horizontal"
     )

    if sltd == "Upload from Local Files":
        st.write("Upload Photo from Local Files :open_file_folder: ")
        image=st.file_uploader("Select the Photo you want to upload ",type=["png","jpg","jpeg"])
        cpton=st.text_input("Enter Caption for selected Photo :page_with_curl: ",)

        if image is not None:
            st.image(image,caption=cpton)

    if sltd == "Capture using Webcam" :
        st.write("Capture Photo using Webcam :technologist: ")
        img=st.camera_input("Click Photo")
        cpton=st.text_input("Enter Caption for Captured Photo :page_with_curl: ")
        if img is not None:
            st.image(img,caption=cpton)

    


if sltd == "Video":
    st.title("Upload Video🎬 ") 
    st.markdown("---")
    st.write("Upload Video from Files :open_file_folder: ")
    video=st.file_uploader("Select the Video you want to upload ",type=["mkv","mp4","mpeg"])
    cptn =st.text_input("Enter Caption for selected Video :page_with_curl:")

    if video is not None:
        st.video(video,caption=cptn)
