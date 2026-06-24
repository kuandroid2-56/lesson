import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MyPlaywright")
        self.geometry("800x600")
        self.minsize(400, 300)

        self._center_window()
        self._build_ui()

    def _center_window(self):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w, h = 800, 600
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        main = ttk.Frame(self, padding=16)
        main.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main, text="Welcome", font=("Helvetica", 18)).pack(pady=(0, 8))

        ttk.Label(main, text="Enter something:").pack(anchor=tk.W)
        self.entry = ttk.Entry(main)
        self.entry.pack(fill=tk.X, pady=(2, 8))

        self.label = ttk.Label(main, text="")
        self.label.pack()

        ttk.Button(main, text="Submit", command=self._on_submit).pack(pady=8)

        self.status = ttk.Label(self, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

    def _on_submit(self):
        text = self.entry.get()
        self.label.config(text=f"You entered: {text}" if text else "Nothing entered")
        self.status.config(text=f"Submitted: {text or '(empty)'}")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
