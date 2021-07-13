"""la page d'events"""
import logging
import importlib
import streamlit as st
import awesome_streamlit as ast
from .pyCode.events import mainEvent
from pathlib import Path
import os
from .preprocessing import Arabycia, remove_stopwords, to_lowercase, remove_punctuation
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
import arabic_reshaper #pip install arabic_reshaper
from bidi.algorithm import get_display #pip install python-bidi
from stop_words import get_stop_words

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

def write():
    """Writes content to the app"""
    
    col1, col2 = st.beta_columns([3,1])
    col1.info("To Extract and Analyze the text content of Events Page   [[ ump.ma/events ]](http://www.ump.ma/fr/events) Click the next button")
    col2.write("")

    if (col2.button('Extraction et Analyse')):
        if Path('ar_event.txt').is_file() & Path('fr_event.txt').is_file() & Path('out_ar_event.txt').is_file() & Path('out_fr_event.txt').is_file() & Path('wordcloud_ar_event.png').is_file() & Path('wordcloud_fr_event.png').is_file() & Path('out_ar_event1.txt').is_file() & Path('out_fr_event1.txt').is_file():
            os.remove("ar_event.txt")
            os.remove("fr_event.txt")
            os.remove("out_ar_event1.txt")
            os.remove("out_fr_event1.txt")
            os.remove("out_ar_event.txt")
            os.remove("out_fr_event.txt")
            os.remove("wordcloud_ar_event.png")
            os.remove("wordcloud_fr_event.png")
        mainEvent()

        arabycia1 = Arabycia()
        file = open("ar_event.txt","r",encoding="utf-8") 
        text = file.read(386000000)  
        arabycia1.set_raw_text(text)
        print("Tokenization")
        s = arabycia1.tokenization(text)
        print(s)
        print("###########################")
        print("Whitout stopWords")
        s = remove_stopwords(s)
        s=remove_punctuation(s)
        s=to_lowercase(s)
        print(s)

        #mots = open("mots_elimines_ar.txt","r",encoding="utf-8") 
        #texte = mots.read(386000000)
        #for i in s:
        #    if i in texte:
        #        s.remove(i)
        #print(s)

        out1 = open("out_ar_event1.txt","w",encoding="utf-8") 
        with out1 as temp_file:
            for i in s:
                temp_file.write("%s " %i)
        out1.close()

        mots = open("mots_elimines.txt","r",encoding="utf-8") 
        texte = mots.read(386000000)
        texte=texte.split()
        print(texte)
        print("succes")

        mots = open("out_ar_event1.txt","r",encoding="utf-8") 
        file = mots.read(386000000)

        pretreated=file

        out2 = open("out_ar_event.txt","w",encoding="utf-8") 

        with out2 as temp_file:
                for i in texte:
                    pretreated=pretreated.replace(i,"")
                temp_file.write("%s " %pretreated)
        out2.close()

        print("###########################")
        print("Stemming")
        s1 = arabycia1.stemming(text)
        print(s1)
        print("###########################")
        print("Lemmatization")
        s1 = arabycia1.lemmatization(text)
        print(s1)
        print("###########################")
        print("Segmentation")
        s1 = arabycia1.segmentation(text)
        print(s1)
        print("###########################")
        print("stem")
        s1 = arabycia1.stem("اتفاق")
        print(s1)
        print("###########################")
        arabycia1.set_raw_text(text)
        search_result = arabycia1.text_search("فكر") 
        print(search_result)

        ######

        arabycia2 = Arabycia()
        file = open("fr_event.txt","r",encoding="utf-8") 
        text = file.read(386000000)  
        arabycia2.set_raw_text(text)
        print("Tokenization")
        s = arabycia2.tokenization(text)
        print(s)
        print("###########################")
        print("Whitout stopWords")
        s = remove_stopwords(s)
        s=remove_punctuation(s)
        s=to_lowercase(s)
        print(s)

        #mots = open("mots_elimines_fr.txt","r",encoding="utf-8") 
        #texte = mots.read(386000000)
        #for i in s:
        #    if i in texte:
        #        s.remove(i)
        #print(s)

        out3 = open("out_fr_event1.txt","w",encoding="utf-8") 
        with out3 as temp_file:
            for i in s:
                temp_file.write("%s " %i)
        out3.close()

        mots = open("mots_elimines.txt","r",encoding="utf-8") 
        texte = mots.read(386000000)
        texte=texte.split()
        print(texte)
        print("succes")

        mots = open("out_fr_event1.txt","r",encoding="utf-8") 
        file = mots.read(386000000)

        pretreated=file

        out4 = open("out_fr_event.txt","w",encoding="utf-8") 

        with out4 as temp_file:
                for i in texte:
                    pretreated=pretreated.replace(i,"")
                temp_file.write("%s " %pretreated)
        out4.close()

        print("###########################")
        print("Stemming")
        s1 = arabycia2.stemming(text)
        print(s1)
        print("###########################")
        print("Lemmatization")
        s1 = arabycia2.lemmatization(text)
        print(s1)
        print("###########################")
        print("Segmentation")
        s1 = arabycia2.segmentation(text)
        print(s1)
        print("###########################")
        print("stem")
        s1 = arabycia2.stem("اتفاق")
        print(s1)
        print("###########################")
        arabycia2.set_raw_text(text)
        search_result = arabycia2.text_search("فكر") 
        print(search_result)

        print("fin process")

        os.chdir(sys.path[0])

        #read text
        f1 = open('ar_event_out.txt' , mode='r', encoding='utf-8')
        text1 = arabic_reshaper.reshape(f1.read())
        text1 = get_display(text1)

        f2 = open('fr_event_out.txt' , mode='r', encoding='utf-8')
        text2 = arabic_reshaper.reshape(f2.read())
        text2 = get_display(text2)

        #page = wikipedia.page("Natural Languge Processing")
        arabicstop = get_stop_words('arabic')
        stopwords1 = set(arabicstop)
        stopwords2 = set(STOPWORDS)
        stopwords1.update(['وجدة','محمد','الجامعة','الأول','بوجدة']) #éliminer les mots
        stopwords2.update(['oujda','président','région','cette','afin','scientifique','universitaire','ainsi', 'leur', 'and', 'to','entre','luniversité','mohammed','premier','comme','monsieur','savoir','maroc','ump', 'université']) #éliminer les mots
        clean_text1 = str([word1 for word1 in text1.split() if word1 not in stopwords1])
        clean_text2 = str([word2 for word2 in text2.split() if word2 not in stopwords2])


        wc1 = WordCloud(
                font_path='arial', #le nom du font arabe
                background_color='white',
                stopwords=stopwords1,
                height = 600,
                width=400,
                #min_font_size=14,
        )
        wc1.generate(text1)

        wc2 = WordCloud(
                background_color='white',
                stopwords=stopwords2,
                height = 600,
                width=400,
                #min_font_size=14,
        )
        wc2.generate(text2)

        #store to file
        wc1.to_file('wordcloud_ar_event.png')
        wc2.to_file('wordcloud_fr_event.png')


        #col2.success("Extraction réalisée!")
    else:
        col2.write("")

    #if Path('ar_event.txt').is_file() & Path('fr_event.txt').is_file() & Path('out_ar_event.txt').is_file() & Path('out_fr_event.txt').is_file() & Path('wordcloud_ar_event.png').is_file() & Path('wordcloud_fr_event.png').is_file() & Path('out_ar_event1.txt').is_file() & Path('out_fr_event1.txt').is_file() :
    #    col2.success("  Extraction déjà réalisée")
    #else:
    #    col2.warning("  Extraction non réalisée")


    col1, col2 = st.beta_columns([1,1])

    with col1:
        if Path('wordcloud_ar_event.png').is_file():
            st.image("wordcloud_ar_event.png")

    with col2:
        if Path('wordcloud_ar_event.png').is_file():
            st.image("wordcloud_fr_event.png")

if __name__ == "__mainEvent__":
    write()