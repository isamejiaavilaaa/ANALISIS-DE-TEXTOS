import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Inicializamos el traductor
translator = Translator()

# Título de la aplicación
st.title('Análisis de Sentimientos y Corrección de Textos')

# Subtítulo en la barra lateral con explicaciones de polaridad y subjetividad
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
        **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

        **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo 
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Analizar Polaridad y Subjetividad en un texto
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text_input = st.text_area('Escribe el texto a analizar:')
    if text_input:
        # Traduce el texto si no está en inglés
        try:
            translation = translator.translate(text_input, dest='en')
            translated_text = translation.text
            st.write("Texto traducido para el análisis (Inglés): ", translated_text)
        except Exception as e:
            st.error(f"Error al traducir: {str(e)}")
            translated_text = text_input

        # Usa TextBlob para analizar el texto
        blob = TextBlob(translated_text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Mostrar los resultados
        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        # Interpretación de la polaridad
        if polarity >= 0.5:
            st.write('Es un sentimiento **Positivo** 😊')
        elif polarity <= -0.5:
            st.write('Es un sentimiento **Negativo** 😔')
        else:
            st.write('Es un sentimiento **Neutral** 😐')

        # Interpretación de la subjetividad
        if subjectivity > 0.5:
            st.write("El texto tiene un alto grado de **subjetividad**.")
        else:
            st.write("El texto es más **objetivo** que subjetivo.")

# Corrección gramatical de textos en inglés
with st.expander('Corrección en inglés'):
    text_to_correct = st.text_area('Escribe el texto para corregir (en inglés):', key='correct')
    if text_to_correct:
        blob2 = TextBlob(text_to_correct)
        corrected_text = blob2.correct()
        st.write("Texto corregido:", corrected_text)
