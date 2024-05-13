import subprocess
import tkinter as tk
from tkinter import messagebox

def get_desired_dpi():

  root = tk.Tk()
  root.title("Set Mouse DPI")

  label = tk.Label(root, text="Enter desired DPI (Dots Per Inch):")
  label.pack()

 
  dpi_entry = tk.Entry(root)
  dpi_entry.pack()

  def handle_ok():
    try:
      desired_dpi = int(dpi_entry.get())
      if desired_dpi <= 0:
        raise ValueError("DPI must be a positive integer.")
      root.destroy()  
      return desired_dpi
    except ValueError:
      messagebox.showerror("Error", "Invalid DPI value. Please enter a positive integer.")

 #handles ok function
  ok_button = tk.Button(root, text="OK", command=handle_ok)
  ok_button.pack()

  root.mainloop()  
  return None  

def set_mouse_speed(desired_dpi):
 
 
  conversion_factor = 10  

  
  target_speed = int(desired_dpi / conversion_factor)

  target_speed = max(1, min(target_speed, 255))  # Limit to 1-255

 
  subprocess.run(["xset", "m", f"{target_speed}"])
  messagebox.showinfo("Success", "Mouse speed adjusted (may not be exact DPI).")

if __name__ == "__main__":
  desired_dpi = get_desired_dpi()
  if desired_dpi:
    set_mouse_speed(desired_dpi)
