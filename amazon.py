"""
A script that, given data from the user by way of a GUI,
generates a URL and opens that in a new browser tab if a browser is open,
otherwise, opens a new browser window (default browser).

If no data is given, the script opens 'www.amazon.com'.

All of the entry boxes are optional.
"""
import tkinter as tk
from webbrowser import open_new_tab as ont

print("\033c")


class Winder:
    """
    Creates all tkinter widgets except for the Radio- and Checkbuttons.
    """

    def __init__(self):
        # Create main window, and give it a title.
        self.root = tk.Tk()
        self.root.title("Amazon sorter")

        # Create the frame used for the input devices.
        self.entries = tk.Frame(self.root)
        self.entries.grid(row=0, column=0)

        # Create the variables for the prime and condition inputs.
        self.check = tk.IntVar()
        self.condition = tk.IntVar()

        # Create all the Entry boxes (all labeled).
        tk.Label(self.entries, text="Search Criteria:", font=("Droid Sans", 20)).grid(
            row=0, column=0, columnspan=3
        )
        self.eser = tk.Entry(self.entries, width=60, font=("Droid Sans", 20))
        self.eser.grid(row=1, column=0, columnspan=3)
        tk.Label(self.entries, text="Brand:", font=("Droid Sans", 20)).grid(
            row=2, column=0
        )
        self.eser1 = tk.Entry(self.entries, width=20, font=("Droid Sans", 20))
        self.eser1.grid(row=3, column=0)
        tk.Label(self.entries, text="Star Rating:", font=("Droid Sans", 20)).grid(
            row=2, column=1
        )
        self.eser2 = tk.Entry(self.entries, width=20, font=("Droid Sans", 20))
        self.eser2.grid(row=3, column=1)
        tk.Label(self.entries, text="Price Range:", font=("Droid Sans", 20)).grid(
            row=2, column=2
        )
        self.eser3 = tk.Entry(self.entries, width=20, font=("Droid Sans", 20))
        self.eser3.grid(row=3, column=2)
        search = tk.Button(self.root, text="Search", command=self.get_data)
        search.grid(row=6, column=0, columnspan=3)

    def get_data(self):
        """
        Format data into a URL and open as a new tab.
        """

        def prices(data):
            """
            Get the data for the price range.
            """
            # If there is data to be had:
            if data:
                # Initialize the variable.
                test = "&rh=p_36%3A"

                # For every price in the entry box:
                for item in data.replace(" ", "").split("-"):
                    # Add it to the URL.
                    test += str(int(item) * 100) + "-"
                # Strip any erroneous '-'s.
                test = test.strip("-")
            # If there is no data to be had, simply don't add anything to the URL.
            else:
                test = ""

            # Return the data.
            return test

        def star(data):
            """
            Get the data for the average user rating.
            """
            # If there is data to be had:
            if data:
                # Format the text.
                test = "&rh=p_72%3A26616"
                test += str(17011 + (-(int(data) * 1000)) + 5000)
            # If there is no data to be had, simply don't add anything to the URL.
            else:
                test = ""
            # Return the data
            return test

        def brand(data):
            """
            Get the data for the branding.
            """
            # If there is data to be had:
            if data:
                # Initialize the variable.
                test = "&rh=p_89%3A"

                # If there are more than one brands listed:
                if len(data.split(",")) > 1:
                    # Add each one to the URL.
                    for item in data.replace(" ", "").split(","):
                        test += item + "%7C"
                    # strip erroneous '%7C's
                    test = test.strip("%7C")
                # Otherwise, append the whole thing to the URL.
                else:
                    test += "&rh=p_89%3A" + data
            # If there is no data to be had, simply don't add anything to the URL.
            else:
                test = ""
            # Return the data.
            return test

        def n_used():
            """
            Get the radio button's value to see if the user
            wants the items returned to be new or used.
            """
            # Initialize the variable.
            test = ""
            # If the user selects the 'new' option, append that code to the URL.
            if not self.condition:
                test = "&rh=p_n_condition-type%3A6461716011"
            # Otherwise, append the Used option to the URL.
            else:
                test = "&rh=p_n_condition-type%3A6461718011"

            # Return the data.
            return test

        # Get most of the data:
        criteria = self.eser.get()
        brands = self.eser1.get()
        stars = self.eser2.get()
        price = self.eser3.get()

        # Initialize the Prime variable
        prime = ""
        # If Prime is selected, add its code to the URL.
        if self.check.get() == 1:
            prime = "&rh=p_85%3A2470955011"

        # Make the huge URL:
        urller = (
            "https://www.amazon.com/s?k="
            + criteria.replace(" ", "+")
            + prices(price)
            + star(stars)
            + brand(brands)
            + prime
            + n_used()
        )

        # And open it!!!
        ont(urller)


def main():
    """
    Create the Checkbutton and Radiobuttons, as well as start mainloop.
    """
    # Create the window
    root = Winder()

    # Create the checkbutton.
    check = tk.Checkbutton(
        root.entries,
        text="Prime",
        selectimage=tk.PhotoImage(name="check.gif"),
        font=("Droid Sans", 20),
        variable=root.check,
    )
    check.grid(row=4, column=0, rowspan=2)
    check.deselect()

    # CReate the Radiobuttons
    new = tk.Radiobutton(
        root.root, text="New", font=("Droid Sans", 15), variable=root.condition, value=0
    )
    new.grid(row=4, column=2, columnspan=2)
    used = tk.Radiobutton(
        root.root,
        text="Used",
        font=("Droid Sans", 15),
        variable=root.condition,
        value=1,
    )
    used.grid(row=5, column=2, columnspan=2)
    new.select()
    used.deselect()

    # Add the Amazon logo.

    img = tk.PhotoImage(file="amazon.gif")

    logo = tk.Label(root.root, image=img)
    logo.grid(row=7, column=0, columnspan=3)

    # Mainloop.
    root.root.mainloop()


if __name__ == "__main__":
    main()
