import requests
from datetime import datetime
from datetime import timedelta
import ctypes
import tkinter as tk
import re


def gui():
    # graphical user interface for user for more friendly appearance
    def get_input():
        main(cpv_entry.get().strip())

    # event for binding Enter key to do same as clicking Search
    def shortcut(event):
        if event.keysym == "Return":
            get_input()

    root = tk.Tk()

    # Tittle
    root.geometry("400x500")
    root.title("eZam API")
    label = tk.Label(root, text="eZam API", font=("Arial Bold", 18))
    label.pack(padx=20, pady=20)

    # information for user what to do
    introduction = tk.Label(root, text="Please enter the CPV code you are looking for", font=("Arial", 12))
    introduction.pack(padx=10, pady=20)

    # box to enter number
    cpv_entry = tk.Entry(root)
    cpv_entry.bind("<KeyPress>", shortcut)
    cpv_entry.pack()

    # button to run searching engine
    search_button = tk.Button(root, text="Search for deal!", font=("Arial Bold", 10), command=get_input)
    search_button.pack(padx=10, pady=10)

    root.mainloop()


today = datetime.today()


def making_link(cpv):
    # time of week used to check if there's a newer deal than w week old
    # (time to submit your application is usually about 2 weeks)
    week = timedelta(days=7)
    last_week = today - week

    # converting today time to format used in eZam service
    t_y = today.strftime('%Y')
    t_m = today.strftime('%m')
    t_d = today.strftime('%d')

    # converting time a week ago to format used in eZam service
    lw_y = last_week.strftime('%Y')
    lw_m = last_week.strftime('%m')
    lw_d = last_week.strftime('%d')

    ending = t_y + "-" + t_m + "-" + t_d + "T23:59:59"
    starting = lw_y + "-" + lw_m + "-" + lw_d + "T00:00:00"
    # cpv is code which specify a kind of work to be made in deal

    # link to access eZam API
    link = ("https://ezamowienia.gov.pl/mo-board/api/v1/notice?NoticeType=ContractNotice&TenderType=1.1.1&CpvCode=" +
            cpv + "&PublicationDateFrom=" + starting + "&PublicationDateTo=" + ending + "&PageSize=100")
    return link


def error_box(er):
    ctypes.windll.user32.MessageBoxW(0, er)


def message_box(xlist):
    # showing box with a massage to user
    if not xlist:
        ctypes.windll.user32.MessageBoxW(0, "There's nothing new...", "eZam actualization")
    else:
        ctypes.windll.user32.MessageBoxW(0,
                                         "There's new deal:\n\n"+"\n".join(map(str, xlist)),
                                         "eZam actualization",
                                         )


names_of_deals = []


def appending_deals(data):

    def getting_deals():
        return deal["orderObject"]

    # making a list of deals then return info
    for deal in data:
        names_of_deals.append(getting_deals())
    return names_of_deals


def main(cpv):
    if not cpv:
        # if empty
        error_box("Please enter the CPV code")
    elif re.search("[0-9]{8}-[0-9]", cpv):
        # checking if cpv has correct structure
        try:  # checking if eZam is available
            data = requests.get(making_link(cpv), timeout=2)
            data.raise_for_status()
            message_box(appending_deals(data.json()))
        except requests.exceptions.Timeout:
            error_box("Connection to eZam timeout")
        except requests.exceptions.RequestException as error:
            error_box(f"{error} error")
    else:
        error_box(f'"{cpv}" is not valid CPV code\n CPV code should be made of 8 digits, dash and 1 digit\n'
                  f'Like this: 42111100-1')


if __name__ == '__main__':
    gui()
