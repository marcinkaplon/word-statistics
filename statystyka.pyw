#-*- coding: utf8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
import re

def openfile():
    txt_file_path=askopenfilename(title="Wybierz plik",filetypes =[("pliki tekstowe", ".txt")])
    with open(txt_file_path, 'r',encoding="utf-8") as file:
        text_file = file.read()
    end.delete("1.0", END)
    end.insert("1.0",text_file)
    run_program()   
        
    
def run_program():
    text=end.get("1.0", END)
    # liczba znaków
    num_chars = number_of_chars(text) 
    # liczba słów
    num_words = number_of_words(text)
    # liczba zdań
    num_sentences = number_of_sentences(text)
    # liczba małych liter
    num_lower_letters = number_of_lower_letters(text)
    # liczba wielkich liter
    num_upper_letters = number_of_upper_letters(text)
    # liczba znaków specjalnych
    num_special_chars = number_of_special_chars(text, ["?", "!", ";", "]", "["])
    # liczba samogłosek
    num_vowels = number_of_vowels(text, ["a", "i", "o", "u", "e", "y", "ą", "ę"])
    # liczba spółgłosek
    num_consonants = number_of_consonants(text, ["b", "c", "ć", "d", "f", "g", "h", "j","k","l","ł","m","n","p","q","r","s","ś","t","v","w","x","z","ż","ź"])
    # palindromy
    palindromes = znajdz_palindrom(text)

def number_of_chars(text):
    change_stats(output_znaki, len(text)-1) #liczba znaków
    return len(text)-1

def number_of_words(text):
    if len(text)-1==0:
        wordslen=0
    else:
        words = re.findall(r"[\w']+", text)
        wordslen=len(words)
    change_stats(output_slowa, wordslen) #długość listy
    return wordslen

def number_of_sentences(text):
    alphabet="aąbcćdeęfghijklłmnoópqrsśtuvxyzźż"
    if len(text)-1==0:
        sentenceslen=0
    else:
        sentences = re.split(r'[.!?]+', text) #importuje re
        sentenceslen=len(sentences)
        for i in sentences:
            if not re.search('[a-zA-Z]', i):
                sentenceslen= sentenceslen-1
    change_stats(output_zdania, sentenceslen)
    return sentenceslen


def number_of_lower_letters(text):
    change_stats(output_mlitery, sum(letter.islower() for letter in text))
    return sum(letter.islower() for letter in text)


def number_of_upper_letters(text):
    change_stats(output_dlitery, sum(letter.isupper() for letter in text))

def number_of_special_chars(text, special_chars_list):
    change_stats(output_specznaki, sum(letter in special_chars_list for letter in text))
    return sum(letter in special_chars_list for letter in text)

def number_of_vowels(text, special_chars_list):
    text=text.lower()
    change_stats(output_samogloski, sum(letter in special_chars_list for letter in text))
    return sum(letter in special_chars_list for letter in text)

def number_of_consonants(text, special_chars_list):
    text=text.lower()
    change_stats(output_spolgloski, sum(letter in special_chars_list for letter in text))
    return sum(letter in special_chars_list for letter in text)

def jest_palindromem(word):
    word = word.lower()
    return len(word) > 1 and word == word[::-1]


def znajdz_palindrom(text):
    result = []
    words = text.replace(","," ").replace("."," ").replace("?"," ").replace("!"," ").replace(":"," ").replace(";"," ").replace("/"," ").replace(")"," ").replace("("," ").split()
    for w in words:
        if jest_palindromem(w):
            result.append(w)
    change_stats(output_palindromy, result)
    return result

def change_stats(stat, new_text):
    stat.configure(state="normal")
    stat.delete("1.0", END)
    stat.insert("1.0", new_text)
    stat.configure(state="disabled")
    return

#=====PĘTLA GŁÓWNA PROGRAMU=====#

root = Tk(className="Statystyka wyrazów")
root.resizable(width=False, height=True)
root.minsize(1,510)
root["background"]="black"

text1 = Label(root, text="Statystyka wyrazów",background="black",foreground="white", font=("Tahoma", 20))
text1.grid(row=0, columnspan=4)


#===TEKST===#

text_znaki = Label(root, text="Liczba znaków: ", background="black", foreground="white")
text_znaki.grid(row=2, column=0, sticky=W,pady=2, padx=5)

output_znaki = Text(root, width=9, height=1, background="black", foreground="white")
output_znaki.grid(row=2, column=1, sticky=W, pady=2)
output_znaki.insert(1.0, "0")
output_znaki.configure(state="disabled", relief="flat")

text_slowa = Label(root, text="Liczba słów: ", background="black", foreground="white")
text_slowa.grid(row=2, column=2, sticky=W,pady=2, padx=5)

output_slowa = Text(root, width=9, height=1, background="black", foreground="white")
output_slowa.grid(row=2, column=3, sticky=W, pady=2)
output_slowa.insert(1.0, "0")
output_slowa.configure(state="disabled", relief="flat")

text_zdania = Label(root, text="Liczba zdań: ", background="black", foreground="white")
text_zdania.grid(row=3, column=0, sticky=W,pady=2, padx=5)

output_zdania = Text(root, width=9, height=1, background="black", foreground="white")
output_zdania.grid(row=3, column=1, sticky=W, pady=2)
output_zdania.insert(1.0, "0")
output_zdania.configure(state="disabled", relief="flat")

text_specznaki = Label(root, text="Liczba znaków specjalnych: ", background="black", foreground="white")
text_specznaki.grid(row=3, column=2, sticky=W,pady=2, padx=5)

output_specznaki = Text(root, width=9, height=1, background="black", foreground="white")
output_specznaki.grid(row=3, column=3, sticky=W, pady=2)
output_specznaki.insert(1.0, "0")
output_specznaki.configure(state="disabled", relief="flat")

text_dlitery = Label(root, text="Liczba dużych liter: ", background="black", foreground="white")
text_dlitery.grid(row=4, column=0, sticky=W,pady=2, padx=5)

output_dlitery = Text(root, width=9, height=1, background="black", foreground="white")
output_dlitery.grid(row=4, column=1, sticky=W, pady=2)
output_dlitery.insert(1.0, "0")
output_dlitery.configure(state="disabled", relief="flat")

text_mlitery = Label(root, text="Liczba małych liter: ", background="black", foreground="white")
text_mlitery.grid(row=4, column=2, sticky=W,pady=2, padx=5)

output_mlitery = Text(root, width=9, height=1, background="black", foreground="white")
output_mlitery.grid(row=4, column=3, sticky=W, pady=2)
output_mlitery.insert(1.0, "0")
output_mlitery.configure(state="disabled", relief="flat")

text_spolgloski = Label(root, text="Liczba spółgłosek: ", background="black", foreground="white")
text_spolgloski.grid(row=5, column=0, sticky=W,pady=2, padx=5)

output_spolgloski = Text(root, width=9, height=1, background="black", foreground="white")
output_spolgloski.grid(row=5, column=1, sticky=W, pady=2)
output_spolgloski.insert(1.0, "0")
output_spolgloski.configure(state="disabled", relief="flat")

text_samogloski = Label(root, text="Liczba samogłosek: ", background="black", foreground="white")
text_samogloski.grid(row=5, column=2, sticky=W,pady=2, padx=5)

output_samogloski = Text(root, width=9, height=1, background="black", foreground="white")
output_samogloski.grid(row=5, column=3, sticky=W, pady=2)
output_samogloski.insert(1.0, "0")
output_samogloski.configure(state="disabled", relief="flat")

text_palindromy = Label(root, text="Jednowyrazowe palindromy:", background="black", foreground="white")
text_palindromy.grid(row=13, columnspan=4, sticky=W,pady=2, padx=5)

output_palindromy = Text(root, width=65, height=4, background="black", foreground="white")
output_palindromy.grid(row=14, columnspan=4, sticky=W, padx=5)
output_palindromy.insert(1.0, "")
output_palindromy.configure(state="disabled", relief="flat")


#===RAMKA===#
frame=Frame(root,borderwidth=4)
frame.grid(row=1, columnspan=4, sticky="E")
frame.config(background="#0c254d")

short_description="Wprowadź tekst poniżej albo wybierz plik, klikając \"Przeglądaj\"."

text2 = Label(frame, text=short_description, background="#0c254d", foreground="white")
text2.grid(sticky=W, row=0, columnspan=2, padx=10, pady=5)

end = Text(frame, wrap=WORD, width=65, height=12, background="#0c254d", foreground="white")
end.grid(row=1, columnspan=2, sticky=S, padx=10, pady=5)
end.config(insertbackground="white")

button_browse=Button(frame, text="Przeglądaj",command=openfile)
button_browse.grid(row=2, column=0, sticky=W, padx=10)

button_calculate=Button(frame, text="Licz statystyki", command=run_program)
button_calculate.grid(row=2, column=1, sticky=E, padx=10)

root.mainloop()


