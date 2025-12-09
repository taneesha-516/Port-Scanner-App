import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

def start_scan_thread():
    target = entry_ip.get()
    
    if not target:
        messagebox.showerror("Error", "Please enter an IP address.")
        return

    #disable button to prevent spamming
    scan_button.config(state=tk.DISABLED)
    output_area.delete(1.0, tk.END)
    
    #to safely update GUI from main thread
    root.after(0, update_output, f"Starting scan on {target}...\n")
    
    t = threading.Thread(target=scan_ports, args=(target,))
    t.daemon = True  #closes thread when the app closes
    t.start()

def scan_ports(target_ip):
    try:
        
        for port in range(1, 1000):
            #AF_INET tells we're using IPv4 and SOCK_STREAM tells we're establishing a TCP connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.05) 
            result = s.connect_ex((target_ip, port))
            #if result=1 then either connection failed or has met an exception

            if result == 0:
                root.after(0, update_output, f"[+] Port {port} is OPEN\n")
            
            s.close()
            
        root.after(0, update_output, "Scan Completed\n")

    except Exception as e:
        root.after(0, update_output, f"Error: {e}\n")
    
    finally:
        # Re-enable the button safely
        root.after(0, lambda: scan_button.config(state=tk.NORMAL))

def update_output(message):
    output_area.insert(tk.END, message)
    output_area.see(tk.END) # Auto-scroll

#GUI Setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Port Scanner")
    root.geometry("400x500")

    #Input label
    label_ip = tk.Label(root, text="Enter Target IP:", font=("Times New Roman", 12))
    label_ip.pack(pady=10)

    #Input box
    entry_ip = tk.Entry(root, font=("Times New Roman", 12))
    entry_ip.insert(0, "127.0.0.1")
    entry_ip.pack(pady=5)

    #Button
    scan_button = tk.Button(root, text="Start Scan", font=("Times New Roman", 12, "bold"), 
                            bg="blue", fg="white", command=start_scan_thread)
    scan_button.pack(pady=10)

    #Output area
    output_area = scrolledtext.ScrolledText(root, width=40, height=20, font=("Consolas", 10))
    output_area.pack(pady=10, padx=10)

    root.mainloop()