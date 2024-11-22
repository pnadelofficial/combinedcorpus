import streamlit as st
import utils

st.title("Connected Corpus")
st.subheader("A connected corpus of Plato's *Republic*")

lang_selector = st.selectbox("Select a language", ["English", "Greek"])
book_selector = st.selectbox("Select a book", range(1,11), format_func=lambda x: f"Book {x}")

st.session_state['df'] = utils.get_data(f"data/{lang_selector.lower()}/republic_{book_selector}.csv")
st.session_state['annotes'] = utils.read_annotes("data/republic_annotations.csv")

st.markdown(utils.grid_layout, unsafe_allow_html=True)

for i, row in st.session_state['df'].iterrows():
    st.markdown(f"""
    <div class="text-annotation-container">
        <div class="text-section">
            <h3>{row['section']}</h3>
            <p>{row['text']}</p>
        </div>
        <div class="annotation-section">
            <h3>{row['section']}</h3>
            <p>{utils.grey if row['section'] not in st.session_state['annotes']['section'].values 
               else utils.nl.join([r for r in st.session_state['annotes'][st.session_state['annotes']['section'] == row['section']]['annotation']])}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)