import os
import tkinter as tk
from tkinter import filedialog, messagebox
from app import coder, decode


def create_archiver_app(root):
    """
    Основна функція, яка створює архіватор без використання глобальних змінних.
    """
    current_file_path = None

    def open_file_compress(compress=False):
        """
        Функція для вибору та відкриття файлу.
        """
        nonlocal current_file_path
        file_path = filedialog.askopenfilename(
            title="Виберіть файл для архівації або розархівації",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    text_box.delete("1.0", tk.END)

                    if compress:
                        encoded_content = content.split("'")
                        encoded_content = [item for item in encoded_content if item]
                        decoded_content = decode(encoded_content)

                        if decoded_content is None:
                            messagebox.showerror("Помилка", "Не вдалося розархівувати файл.")
                            return

                        text_box.insert("1.0", decoded_content)
                    else:
                        text_box.insert("1.0", content)

                    current_file_path = file_path
                    messagebox.showinfo("Файл відкрито", f"Файл '{file_path}' успішно завантажено.")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалось відкрити файл: {str(e)}")

    def compress_file():
        """
        Функція для архівації файлу та виведення інформації про розмір.
        """
        nonlocal current_file_path
        if not current_file_path:
            messagebox.showwarning("Попередження", "Спочатку виберіть файл для архівації.")
            return

        save_path = filedialog.asksaveasfilename(
            title="Зберегти архів як...",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not save_path:
            return

        try:
            original_size = os.path.getsize(current_file_path)

            with open(current_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            compressed_content = coder(content)

            if compressed_content is None:
                messagebox.showerror("Помилка", "Не вдалося заархівувати файл.")
                return

            with open(save_path, 'w', encoding='utf-8') as archive_file:
                archive_file.write("'".join(compressed_content))

            compressed_size = os.path.getsize(save_path)

            reduction_percent = ((original_size - compressed_size) / original_size) * 100

            messagebox.showinfo(
                "Архівація",
                f"Файл успішно заархівовано та збережено як '{save_path}'.\n"
                f"Оригінальний розмір: {original_size} байт\n"
                f"Розмір заархівованого файлу: {compressed_size} байт\n"
                f"Зменшення на {reduction_percent:.2f}%."
            )

        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалось заархівувати файл: {str(e)}")

    def open_file_decompress():
        """
        Функція для вибору файлу для розархівації.
        """
        open_file_compress(True)

    def decompress_file():
        """
        Функція для розархівації файлу.
        """
        nonlocal current_file_path
        if not current_file_path:
            messagebox.showwarning("Попередження", "Спочатку виберіть файл для розархівації.")
            return

        save_path = filedialog.asksaveasfilename(
            title="Зберегти розархівований файл як...",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not save_path:
            return

        try:
            with open(current_file_path, 'r', encoding='utf-8') as file:
                encoded_content = file.read().split("'")
                encoded_content = [item for item in encoded_content if item]

            decoded_content = decode(encoded_content)

            if decoded_content is None:
                messagebox.showerror("Помилка", "Не вдалося розархівувати файл.")
                return

            with open(save_path, 'w', encoding='utf-8') as decompressed_file:
                decompressed_file.write(decoded_content)

            messagebox.showinfo("Розархівація", f"Файл успішно розархівовано та збережено як '{save_path}'.")

        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалось розархівувати файл: {str(e)}")


    text_box = tk.Text(root, wrap=tk.WORD, width=60, height=20)
    text_box.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    open_button = tk.Button(btn_frame, text="Відкрити файл для архівування", command=open_file_compress)
    open_button.grid(row=1, column=0, pady=10, padx=10)

    open_button = tk.Button(btn_frame, text="Відкрити файл для розархівування", command=open_file_decompress)
    open_button.grid(row=1, column=1, pady=10, padx=10)

    compress_button = tk.Button(btn_frame, text="Архівувати", command=compress_file)
    compress_button.grid(row=0, column=0, padx=10, stick='we')

    decompress_button = tk.Button(btn_frame, text="Розархівувати", command=decompress_file)
    decompress_button.grid(row=0, column=1, padx=10, stick='we')


root = tk.Tk()
root.title("Файловий архіватор")

create_archiver_app(root)

root.mainloop()
