import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configurare stil Brutal
st.set_page_config(page_title="Evaluare Brutală", layout="centered")
st.markdown("<style>body {background-color: #111; color: white;}</style>", unsafe_allow_html=True)

st.title("🛡️ EVALUARE BRUTALĂ: IMAGINE & PROGRES")
st.write("Scop: Maximizarea impactului estetic. Nu confort emoțional.")

# Instrucțiuni de sistem bazate pe documentul tău
SYSTEM_PROMPT = """
Ești un evaluator de imagine brutal. Respectă aceste reguli:
1. Adevărul are prioritate absolută. Mediocritatea este semnalată explicit.
2. Analizează: Coerență freză, barbă, haine, postură.
3. Checklist obligatoriu: 
   - Ce este clar sub standard? 
   - Ce este mediocru?
   - Ce funcționează dar poate fi optimizat?
   - Ce trebuie eliminat complet?
4. Scor general (1-10) fără indulgență.
5. Verdict: MAI BINE / LA FEL / MAI RĂU față de data trecută (dacă e cazul).
"""

api_key = st.text_input("Introdu Google API Key (Gratuit de pe AI Studio):", type="password")

col1, col2, col3 = st.columns(3)
with col1: f1 = st.file_uploader("Poza Față")
with col2: f2 = st.file_uploader("Poza Profil")
with col3: f3 = st.file_uploader("Poza 3/4")

if st.button("EXECUTĂ ANALIZA"):
    if not api_key:
        st.error("Lipsește cheia API!")
    elif not (f1 and f2 and f3):
        st.warning("Încarcă toate cele 3 unghiuri obligatorii.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        imgs = [Image.open(f1), Image.open(f2), Image.open(f3)]
        response = model.generate_content([SYSTEM_PROMPT] + imgs)
        st.markdown("---")
        st.subheader("VERDICT PROFESIONAL")
        st.write(response.text)
