from collections import Counter
import streamlit as st
import time

st.markdown(f"<h1 style='text-align:center; color:#352a3b;'>💖 LOVE CALCULATOR 💖</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(255, 192, 203, 0.8), rgba(255, 192, 203, 0.3));
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)




name1 = st.text_input("👤 Your Name", key="you").lower()
name2 = st.text_input("💘 Their Name", key="crush").lower()

if st.button("💘 Calculate Love") :
    if name1 != "" or name2 != "" :

        combo = f"{name1} loves {name2}"
        counts = Counter(combo) 

        used = set()
        number_list = []

        for ch in combo:
            if ch not in used and ch != " ":
                number_list.append(counts[ch])
                used.add(ch)
    
        st.write("")
        st.write("-" * 10)
        st.write("behind the scene/process")

        st.write("")
        st.write("".join([str(n) for n in number_list]))

        while len(number_list) > 2 :
            new_list = []
            

            while len(number_list) > 1 :
                first = number_list.pop(0)
                last = number_list.pop()
                new_list.extend([int(d) for d in str(first + last)])

            if number_list:
                new_list.append(number_list.pop())
            
            
            number_list = new_list
            st.write("".join([str(n) for n in number_list]))
        st.write("-" * 10 )
        st.write("")

        with st.spinner('Analyzing hearts... 💓'):
             time.sleep(3)


        final = "".join([str(n) for n in number_list])
        
        st.markdown(f"<h2 style='text-align: center; color: pink;'>Your love is {final}% true 💖</h2>", unsafe_allow_html=True)
        st.progress(int(final)) 
        if final >= "60" :
            st.success("Made for each other")
            st.balloons()
        elif "60" > final >= "30":
            st.write("Might be a true love")
        else :
            st.warning("Too low")

    else:
        st.error("Enter names")

st.markdown("""
<hr>
<h5 style='text-align:center; ;'>Made with 💘 by <b>HEISENDEV</b></h5>
""", unsafe_allow_html=True)
