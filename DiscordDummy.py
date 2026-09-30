import sys
import os
import tkinter as tk

if getattr(sys, 'frozen', False):
    app_path = sys.executable
    # exe化された実行時の基準フォルダ（一時フォルダまたはexeのある場所）
    base_dir = os.path.dirname(sys.executable)
else:
    app_path = __file__
    base_dir = os.path.dirname(os.path.abspath(__file__))

app_title = os.path.splitext(os.path.basename(app_path))[0]

root = tk.Tk()
root.title(app_title)
root.geometry("380x200")
root.configure(bg="#2b2d31")
root.resizable(False, False)

# ウィンドウやタスクバーにアイコンを反映（app.ico が同階層にある場合）
icon_path = os.path.join(base_dir, "app.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# --- 以下デザイン部分 ---
card = tk.Frame(root, bg="#313338", highlightbackground="#1e1f22", highlightthickness=1)
card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=160)

accent_bar = tk.Frame(card, bg="#5865F2", height=4)
accent_bar.pack(fill="x", side="top")

title_label = tk.Label(
    card,
    text=app_title,
    font=("Segoe UI", 16, "bold"),
    fg="#f2f3f5",
    bg="#313338"
)
title_label.pack(pady=(25, 5))

sub_label = tk.Label(
    card,
    text="• Status: Running",
    font=("Segoe UI", 9),
    fg="#23a55a",
    bg="#313338"
)
sub_label.pack(pady=(0, 15))

def on_enter(e):
    end_button.config(bg="#4752C4")

def on_leave(e):
    end_button.config(bg="#5865F2")

end_button = tk.Button(
    card,
    text="END",
    command=root.destroy,
    font=("Segoe UI", 10, "bold"),
    fg="#ffffff",
    bg="#5865F2",
    activebackground="#3b428a",
    activeforeground="#ffffff",
    bd=0,
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=6
)
end_button.pack()

end_button.bind("<Enter>", on_enter)
end_button.bind("<Leave>", on_leave)

root.mainloop()