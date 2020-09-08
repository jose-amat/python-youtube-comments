import functions.youtube_api as yb
import tkinter as tk


window = tk.Tk()
window.title('Python Youtube comments')
window['background'] = 'red'

tk.Label(window, text="API Key").grid(row=0)
tk.Label(window, text="Video URL").grid(row=1)

key = tk.Entry(window)
url = tk.Entry(window)


def enter():
  lb['text'] = 'Loading...'
  yb.youtubeComments(key.get(), url.get())
  lb['text'] = 'Finished.'
  print('Finished.')

key.grid(row=0, column=1)
url.grid(row=1, column=1)

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