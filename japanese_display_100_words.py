import tkinter as tk
import random
import pandas as pd
import os
import win32api

#I thought I could get idle time with my Python program
# but easier to do with WIndows scheduler and bat script
# def getIdleTime():

#   last_active = win32api.GetLastInputInfo()
#   now = win32api.GetTickCount()
#   elapsed_seconds = (now - last_active)/1000



# --- data ---
# a csv file with japanese words, translations and examples

#get the path of this python script (that's where the csv is located)
this_file_path = os.path.dirname(os.path.realpath(__file__))
#change current working dir to this path
os.chdir(this_file_path)
# cwd = os.getcwd()
# print(cwd)

#open csv file that's in the same folder, drop any NaNa
data = pd.read_csv('japaneseWords_1000.csv',index_col=None).dropna()

def concat_and_add_new_line(listOfItems):
  stringForDisplay = '\n'.join(map(str, listOfItems)) 
  return(stringForDisplay)

#some entries are too long and appear outside of the screen
#if an entry is too long, break it into lines

def split_if_too_long(items): 
  noLongWordsList = []
  for item in items:
    if(len(item) > 15):
      #newItem = item.replace(", ", "\n")
      newItem = item.replace(" ", "\n")
    else:  
      newItem = item
    noLongWordsList.append(newItem)
  return noLongWordsList


  stringForDisplay = '\n'.join(map(str, listOfItems)) 
  return(stringForDisplay)


def change_text_on_click(event): #Enter key
    change_text()

def screen_exit(event):
    root.destroy() #terminates the mainloop and deletes all widgets on pressing Esc key


def change_text():
    #select a random row from the dataframe
    random_row = data.sample(n=1)

    #create 3 lists to display a word with 2 examples
    wordsRaw =random_row.values.tolist()[0][0:3]
    wordsRightLength = split_if_too_long(wordsRaw)
    word = concat_and_add_new_line(wordsRightLength)

    

    #in the future:
    # if text too long split into lines

    sentence1_raw =random_row.values.tolist()[0][3:6]
    sentence1 = concat_and_add_new_line(sentence1_raw)

    sentence2_raw =random_row.values.tolist()[0][6:10]
    sentence2 = concat_and_add_new_line(sentence2_raw) 

    # change text 
    c.itemconfig(w, text=word)
    c.itemconfig(sen1, text=sentence1)
    c.itemconfig(sen2, text=sentence2)

    
# --- main ---

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind("<Return>",change_text_on_click)
root.bind("<Escape>",screen_exit)

c = tk.Canvas(root, bg='black')
c.pack(expand=1, fill=tk.BOTH)
w = c.create_text(
          400, 500,
                  anchor=tk.CENTER,
                  #font=("Calibri",50,"italic"), 
                  font=("Calibri",70),
                  fill='white',
                  width=root.winfo_screenwidth()*0.8,
                  text='' # empty string
                  )

sen1 = c.create_text(
          1250, 300,
                  anchor=tk.CENTER,
                  #font=("Calibri",50,"italic"), 
                  font=("Calibri",50),
                  fill='orange',
                  width=root.winfo_screenwidth()*0.8,
                  text='' # empty string
                  )


sen2 = c.create_text(
          1250, 800,
                  anchor=tk.CENTER,
                  #font=("Calibri",50,"italic"), 
                  font=("Calibri",50),
                  fill='orange',
                  width=root.winfo_screenwidth()*0.8,
                  text='' # empty string
                  )
# set first text
change_text()

root.mainloop() #root is the object that has the mainloop method
#waiting for events and updating the GUI. But this method is blocking the code after it.