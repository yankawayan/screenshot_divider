from tkinter import *
from tkinter import ttk

#Comboboxの選択項目用リスト
cb_job = ['会社員', '会社役員', '学生', 'アルバイト', '自宅警備', 'その他']

#ウィンドウを作成
root = Tk()

#ウィンドウサイズを指定
root.geometry("320x240")

#ウィンドウタイトルを指定
root.title('入力フォーム')

frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

#名前
label1 = ttk.Label(frame1, text='お名前', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

#住所
label2 = ttk.Label(frame1, text='住所', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

#職業
label3 = ttk.Label(frame1, text='職業', padding=(5, 2))
label3.grid(row=2, column=0, sticky=E)


#名前
name = StringVar()
name_txt = ttk.Entry(
    frame1,
    textvariable=name,
    width=20)
name_txt.grid(row=0, column=1)

#住所
address = StringVar()
address_txt = ttk.Entry(
    frame1,
    textvariable=address,
    width=20)
address_txt.grid(row=1, column=1)

#職業
# Combobox
job = StringVar()
job_cb = ttk.Combobox(
    frame1, 
    textvariable=job, 
    values=cb_job, 
    width=20)
job_cb.set(cb_job[0])
job_cb.bind(
    '<<ComboboxSelected>>')
job_cb.grid(row=2, column=1)

# Button
button1 = ttk.Button(
    frame1, text='OK', 
    command=lambda: print("%s, %s, %s" % (name.get(), address.get(), job.get())))
button1.grid(row=3, column=1)

#ウィンドウ表示継続
root.mainloop()