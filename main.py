import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() #リセット

        self.title("my app")
        self.geometry("800x600") #画面の大きさを指定
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.LoadingList_frame = LoadingListFrame(self) #frameworkを作成して現在のクラスに追加
        self.LoadingList_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="new")#ここで位置を指定

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")

class LoadingListFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        item_list=[["item1","item2","item3"],[1,3,5]]

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, width=300, height=200)
        self.scrollable_frame.pack()

        # アイテムリストを2列にして表示
        for row, (col1_item, col2_item) in enumerate(zip(item_list[0], item_list[1])):
            # 左列のアイテムを表示
            col1_label = customtkinter.CTkLabel(self.scrollable_frame, text=str(col1_item))
            col1_label.grid(row=row, column=0, padx=10, pady=5)  # 左側 (column=0)

            # 右列のアイテムを表示
            col2_label = customtkinter.CTkLabel(self.scrollable_frame, text=str(col2_item))
            col2_label.grid(row=row, column=1, padx=10, pady=5)  # 右側 (column=1)
        


app = App()
app.mainloop()

