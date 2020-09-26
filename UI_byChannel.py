import functions.youtube_api as yb
import tkinter as tk


window = tk.Tk()
window.title('Python Youtube comments')
window['background'] = 'red'

tk.Label(window, text="API Key").grid(row=0)
tk.Label(window, text="Channel ID").grid(row=1)
tk.Label(window, text="Order").grid(row=2)

key = tk.Entry(window)
channelId = tk.Entry(window)
order = tk.Entry(window)


def enter():
  lb['text'] = 'Loading...'
  yb.commentsByChannel(key.get(), channelId.get(), order.get())
  lb['text'] = 'Finished.'
  print('Finished.')

key.grid(row=0, column=1)
channelId.grid(row=1, column=1)
order.grid(row=2, column=1)

quitBtn = tk.Button(window, width=5, text="Quit", command=window.quit).grid(row=3,
                                                  column=1,
                                                  sticky=tk.W,
                                                  pady=2)

bt = tk.Button(window, width=5, text="Enter", command=enter).grid(row=3,
                                                  column=2,
                                                  sticky=tk.W,
                                                  pady=2)
lb = tk.Label(window, text='Insert your data')
lb.grid(row=4, column=1)

window.mainloop()