import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="00:00:000", font=("Arial", 60), fg="black", bg="white")
        self.time_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.start_button = tk.Button(root, text="START", command=self.start_stopwatch, fg="white", bg="green")
        self.start_button.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        self.pause_button = tk.Button(root, text="PAUSE", command=self.pause_stopwatch, state=tk.DISABLED, fg="white", bg="red")
        self.pause_button.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        self.reset_button = tk.Button(root, text="RESET", command=self.reset_stopwatch, state=tk.DISABLED, fg="white", bg="blue")
        self.reset_button.grid(row=1, column=2, padx=5, pady=10, sticky="ew")

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)

    def pause_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.root.after_cancel(self.update_timer)
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)

    def reset_stopwatch(self):
        self.is_running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:000")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            milliseconds = int((self.elapsed_time % 1) * 1000)
            time_str = f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}"
            self.time_label.config(text=time_str)
            self.root.after(1, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stopwatch")
    
    window_width = 400  # Adjust the width as needed
    window_height = 200  # Adjust the height as needed

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    app = StopwatchApp(root)
    root.mainloop()
