import pandas as pd
import streamlit as st

grey = '\u2014' 
nl = '\n'
grid_layout = """
<style>
.text-annotation-container {
    display: grid;
    grid-template-columns: 3fr 1fr;
    gap: 1rem;
    align-items: start;
}
.text-section {
    padding: 1rem;
}
.annotation-section {
    padding: 1rem;
    position: sticky;
    top: 0;
}
.annotation-empty {
    background-color: #f5f5f5;
    color: #999;
    font-style: italic;
}
</style>
"""

@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename)
    return data

@st.cache_data
def read_annotes(filename):
    data = pd.read_csv(filename)
    return data