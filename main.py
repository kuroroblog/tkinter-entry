import tkinter as tk


class Application(tk.Frame):
    # 氏名入力用変数
    entryName = None
    # パスワード入力用変数
    entryPassword = None

    # クリアボタンがクリックされた場合に実行される関数
    # 氏名、パスワードの入力データをクリアする。
    def clearCommand(self):
        # delete : 氏名情報の削除を行う。
        # 第一引数 : 削除する文字列の開始位置(0番目からスタート)
        # 第二引数 : 削除する文字列の最終位置
        # tk.END : 文字列の最終位置
        self.entryName.delete(0, tk.END)

        # delete : パスワード情報の削除を行う。
        # 第一引数 : 削除する文字列の開始位置(0番目からスタート)
        # 第二引数 : 削除する文字列の最終位置
        # tk.END : 文字列の最終位置
        self.entryPassword.delete(0, tk.END)

        print('名前とパスワードをクリアしました。')

    # 追加ボタンがクリックされた場合に、氏名入力の末尾に"Bob"を追加入力する関数
    def addNameBobButton(self):
        # insert : 文字列の挿入を行う。
        # 第一引数 : 追加文字列の挿入開始位置(0番目からスタート)
        # tk.END : 文字列の最終位置
        # 第二引数 : 追加する文字列情報
        self.entryName.insert(tk.END, "Bob")

    # パスワード確認ボタンがクリックされた場合に実行される関数
    def getPassword(self):
        # get : 現在入力されているパスワード情報を表示する関数
        print('パスワード : ' + self.entryPassword.get())

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        ############################################## frame Widget START ##############################################

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        ############################################## frame Widget END ##############################################

        ############################################## entry Widget START ##############################################

        # frame Widget(Frame)を親要素として、氏名用のentry Widgetを作成する。
        # width : 幅の設定
        self.entryName = tk.Entry(frame, width=15)

        # frame Widget(Frame)を親要素とした場合に、氏名用のentry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.entryName.pack()

        # 氏名の入力先へデフォルトで格納したい文字列の挿入。
        # 第一引数 : 文字列の挿入開始位置(0番目からスタート)
        # 第二引数 : 挿入文字列
        self.entryName.insert(0, "氏名")

        # frame Widget(Frame)を親要素として、パスワード用のentry Widgetを作成する。
        # width : 幅の設定
        self.entryPassword = tk.Entry(frame, width=15)

        # frame Widget(Frame)を親要素とした場合に、パスワード用のentry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.entryPassword.pack()

        # パスワードの入力先へデフォルトで格納したい文字列の挿入。
        # 第一引数 : 文字列の挿入開始位置(0番目からスタート)
        # 第二引数 : 挿入文字列
        self.entryPassword.insert(0, "パスワード")

        ############################################## entry Widget END ##############################################

        ############################################## button Widget START ##############################################

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        confirmPasswordButton = tk.Button(frame, text="パスワード確認", width=15, command=self.getPassword)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        confirmPasswordButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        addNameBobButton = tk.Button(frame, text="追加", command=self.addNameBobButton)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        addNameBobButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        clearButton = tk.Button(frame, text="クリア", command=self.clearCommand)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        clearButton.pack(side=tk.LEFT)

        ############################################## button Widget END ##############################################

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
