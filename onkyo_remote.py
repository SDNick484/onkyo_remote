import eiscp
import tkinter as tk

RECEIVER_IP = '192.168.1.208'
#RECEIVER_IP = None

def main():
    window = tk.Tk()
    window.wm_title("Onkyo Remote") #Makes the title that will appear in the top left
    window.config(background = "#000000")

    # POWER ON
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Power On", bg = "green", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('power on') )
    frame.grid(row=0, column=0, padx=5, pady=5)

    ## Input Select 
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Label( master = window, text="Power")
    frame.grid(row=0, column=1, padx=5, pady=15)

    # POWER OFF
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Power Off", bg = "red",  relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('power off') )
    frame.grid(row=0, column=2, padx=5, pady=5)

    ## Input Select 
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Label( master = window, text="Input Select")
    frame.grid(row=1, column=1, padx=5, pady=15)

    # BD/DVD
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="Bluray", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector bd') )
    frame.grid(row=2, column=0, padx=5, pady=5)

    # CBL/SAT
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Cable", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector cbl') )
    frame.grid(row=2, column=1, padx=5, pady=5)

    # STRMBOX
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Stream", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector strm-box') )
    frame.grid(row=2, column=2, padx=5, pady=5)

    # PC
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="PC", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector pc') )
    frame.grid(row=3, column=0, padx=5, pady=5)

    # GAME
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Game", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector game') )
    frame.grid(row=3, column=1, padx=5, pady=5)

    # NET
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Net", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector net') )
    frame.grid(row=3, column=2, padx=5, pady=5)

    # BLUETOOTH
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="Bluetooth", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector bluetooth') )
    frame.grid(row=4, column=0, padx=5, pady=5)

    # USB
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="USB", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector usb') )
    frame.grid(row=4, column=1, padx=5, pady=5)

    # AUX
    window.columnconfigure(2, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Aux", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('input-selector aux') )
    frame.grid(row=4, column=2, padx=5, pady=5)

    ## Listening Mode
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Label( master = window, text="Listening Mode")
    frame.grid(row=5, column=1, padx=5, pady=15)

    # Stereo
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="Stereo", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('listening-mode stereo') )
    frame.grid(row=6, column=0, padx=5, pady=5)

    # Direct
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="Direct", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('listening-mode direct') )
    frame.grid(row=6, column=1, padx=5, pady=5)

    # Surroud
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="Surround", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('listening-mode surround') )
    frame.grid(row=6, column=2, padx=5, pady=5)

    # Atmos
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="Atmos", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('listening-mode dolby-atmos') )
    frame.grid(row=7, column=0, padx=5, pady=5)

    # DTS-X
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Button( master=window, text="DTS-X", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('listening-mode dts-x') )
    frame.grid(row=7, column=2, padx=5, pady=5)

    ## Volume
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    frame = tk.Label( master = window, text="Volume")
    frame.grid(row=8, column=1, padx=5, pady=15)

    # VOL DOWN
    window.columnconfigure(4, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Vol Dn", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('master-volume level-down') )
    frame.grid(row=9, column=0, padx=5, pady=5)

    # VOL UP
    window.columnconfigure(4, weight=1)
    window.rowconfigure(0, weight=1)
    frame = tk.Button( master=window, text="Vol Up", relief=tk.RAISED, borderwidth=1, height = 2, width = 5, command = lambda : receiver.command('master-volume level-up') )
    frame.grid(row=9, column=2, padx=5, pady=5)

    window.mainloop()


if __name__ == "__main__":

    ### Check if receiver's IP is set
    if not RECEIVER_IP:
        print("Please udpate onkyo_remote.py with your receive's IP")
        quit()

    ### Set up device
    receiver = eiscp.eISCP( RECEIVER_IP )

    main()


receiver.disconnect()
