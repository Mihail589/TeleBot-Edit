from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter.ttk import Notebook
import os
from tkinter import messagebox as mb
import json
class PyPhotoEditir:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.image_tabs = Notebook(self.root)
        with open("db.json", "r", encoding="UTF-8") as file:
            self.confg = json.load(file)
            print(self.confg)
        self.opened_images = []
        self.init()

    def init(self):
        self.root.title("PhotoMagic")
        self.image_tabs.enable_traversal()
        self.root.bind("<Escape>", self._close)

    def run(self):
        self.draw_menu()
        self.draw_widgets()

        self.root.mainloop()

    def draw_menu(self):
        menu_bar = Menu(self.root)
        new_bar = Menu(self.root)
        pod = Menu(self.root)
        pod2 = Menu(self.root)
        pod3 = Menu(self.root)
        fille_menu = Menu(menu_bar, tearoff=0)
        pod4 = Menu(pod2, tearoff=0)
        pod6 = Menu(pod3, tearoff=0)
        if self.confg["lang"] == "en":
            fille_menu.add_command(label="Open", command=self.opem_new_images)
            menu_bar.add_cascade(label="Fille", menu=fille_menu)
            self.root.configure(menu=menu_bar)
            fille_menu.add_command(label="Save as", command=self.save_image_as)
            pod4.add_command(label="ru", command=self.rus)
            pod4.add_command(label="en", command=self.eng)
            pod6.add_command(label="while", command=self.whiles)
            pod6.add_command(label="black", command=self.blacks)
            fille_menu.add_cascade(label="Settings", menu=pod)
            pod.add_cascade(label="Language", menu=pod4)
        if self.confg["lang"] == "ru":
            new_mvenu = Menu(new_bar, tearoff=0)
            new_mvenu.add_command(label="Открыть", command=self.opem_new_images)
            new_bar.add_cascade(label="Файл", menu=new_mvenu)
            self.root.configure(menu=new_bar)
            new_mvenu.add_command(label="Сохранить как", command=self.save_image_as)
            pod4.add_command(label="Русский", command=self.rus)
            pod4.add_command(label="Англиский", command=self.eng)
            pod6.add_command(label="Белый", command=self.whiles)
            pod6.add_command(label="Черный", command=self.blacks)
            new_mvenu.add_cascade(label="Настроики", menu=pod)
            pod.add_cascade(label="Язык", menu=pod4)

    def opem_new_images(self):
        image_paths = fd.askopenfilenames(filetypes=(("Images", "*.jpeg;*.jpg;*.png"),))
        for image_path in image_paths:
            self.add_new_image(image_path)

    def add_new_image(self, image_path):
        image = Image.open(image_path)
        image_tk = ImageTk.PhotoImage(image)
        self.opened_images.append([image_path, image])
        image_tab = Frame(self.image_tabs)
        image_label = Label(image_tab, image=image_tk)
        image_label.image = image_tk
        image_label.pack(side="bottom", fill="both", expand="yes")
        self.image_tabs.add(image_tab, text=image_path.split('/')[-1])
        self.image_tabs.select(image_tab)

    def draw_widgets(self):
        self.image_tabs.pack(fill="both", expand=1)
    def rus(self):
        ru ="ru"
        with open("db.json", "a", encoding="UTF-8") as file:
            self.confg = self.confg[1] = 'ru'
            file.write(json.dump(self.confg))
    def eng(self):
        pass
    def whiles(self):
        pass
    def blacks(self):
        pass
    def save_image_as(self):
        curent_tab = self.image_tabs.select()
        if not curent_tab:
            return
        teb_namber = self.image_tabs.index(curent_tab)

        old_path, old_ext = os.path.splitext(self.opened_images[teb_namber][0])
        new_path = fd.asksaveasfile(initialdir=old_path, filetypes=(("Images", "*.jpeg;*.jpg;*.png"),))
        if not new_path:
            return
        new_path, new_ext = os.path.splitext(new_path)
        if not new_ext:
            new_ext = old_ext
        elif old_ext != new_ext:
            mb.showerror("Incorrect extesion", f"Got incorrect extension: {new_ext}. Old was: {old_ext}")
            return
        image = self.opened_images[teb_namber][1]
        image.save(new_path, new_ext)
        image.close()
        del self.opened_images[teb_namber]
        self.image_tabs.forget(curent_tab)

        self.add_new_image(new_path + new_ext)
    def _close(self, event):
        self.root.quit()


if __name__ == '__main__':
    PyPhotoEditir().run()