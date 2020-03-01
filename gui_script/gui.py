from tkinter import Tk, Label, StringVar, OptionMenu, \
                    Button, LEFT, filedialog
from os import system, getcwd

LANG_CODE_DICT = {u"中文(繁體)": "cmn-hant-tw", 
                  u"中文(简体)": "cmn-hans-cn",
                  u"粵語"      : "yue-hant-hk",
                  u"English"   : "en-us", 
                  u"日本語"    : "ja-jp",
                  u"한국어"    : "ko-kr"}

def convert_lang(lang_code):
    return LANG_CODE_DICT[lang_code]
    
def execute():
    if file_name.get() == '' or file_name.get() == u'請選擇一個影片檔！':
        file_name.set(u'請選擇一個影片檔！')
        file_name_label.config(fg="red")
    else:
        lang = convert_lang(lang_code.get())
        system("start cmd /c autosub -i %s -S %s"%(file_name.get(), lang))
    
def choose_file():
    file_name.set('')
    file_name_label.config(fg="black")
    file_name_ = filedialog.askopenfilename(initialdir = getcwd(), 
                                            title = "選取影片檔案", 
                                            filetypes = (("mp4 files","*.mp4"),("all files","*.*")))
    file_name.set(file_name_)

root = Tk()
root.title(u"自動字幕生成幫手")
root.geometry("300x240+200+200")
root.resizable(False, False)

lang_label = Label(text=u'選取影片語言')
lang_label.config(font=("Courier", 12))
lang_label.place(x=30, y=20)
lang_code = StringVar(root)
lang_code.set(u"中文(繁體)")
lang = OptionMenu(root, lang_code, *LANG_CODE_DICT.keys())
lang.config(font=("Courier", 12), width=8)
lang.place(x=20, y=50)

file_button = Button(text=u'選取影片檔案', command=choose_file)
file_button.config(font=("Courier", 12))
file_button.place(x=24, y=110)
file_name = StringVar()
file_name.set('')
file_name_label = Label(root, textvariable=file_name, 
                           justify=LEFT, wraplengt=250)
file_name_label.place(x=20, y=150)

file_button = Button(text=u'開始', command=execute)
file_button.config(font=("Courier", 30))
file_button.place(x=160, y=50)

root.mainloop()