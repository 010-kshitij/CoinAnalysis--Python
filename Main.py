import Tkinter
import ScrolledText

# Directory Imports
from App import App
from CoinValues import CoinValues
import analyze_coin



# Initialize Application
app = App()

# Initialize Components
label_btc_price = dict()
label_bcc_price = dict()
label_dash_price = dict()
label_doge_price = dict()
label_eth_price = dict()
label_ltc_price = dict()
label_nxt_price = dict()
label_str_price = dict()
label_nem_price = dict()
label_xrp_price = dict()

# Coin Selector Variable
main_coin = Tkinter.StringVar(None, 'BTC')
coin = Tkinter.StringVar()
output_frame = Tkinter.Frame()
output = ScrolledText.ScrolledText(
            master=output_frame,
            wrap='word',  # wrap text at full words only
            width=25,  # characters
            height=20,  # text lines
        )
output.grid(row=0)
limit_entry = Tkinter.Entry(app.window)
limit_entry.insert(Tkinter.END, "30")
limit_entry.config(width=10)
limit_option_value = Tkinter.StringVar()
limit_option_value.set("daily")
limit_option_menu = ["daily", "minute"]
# limit_option = Tkinter.OptionMenu(app.window)
limit_option = apply(Tkinter.OptionMenu, (app.window, limit_option_value) + tuple(limit_option_menu))
limit_option.grid(row=11, column=2)


# Coin Selector Command
def do_analyze_coin():
    global app, coin, output, output_frame
    result = analyze_coin.analyze(maincoin=main_coin.get().upper(), othercoin=coin.get().upper(), window=app.window, track_type=limit_option_value.get(), limit=limit_entry.get()) 

    output.insert('insert', result)
    output_frame.grid(row=1, column=6,rowspan=100)

# Ticking Function to get values for price table
def get_coin_values():
    # Get the coin values for the price table
    coinValues = CoinValues().get()

    # Setting Price
    label_btc_price['price'].config(text=('({} {})'.format(coinValues['BTC'][2], coinValues['BTC'][3])))
    label_bcc_price['price'].config(text=('({} {})'.format(coinValues['BCH'][2], coinValues['BCH'][3])))
    label_dash_price['price'].config(text=('({} {})'.format(coinValues['DASH'][2], coinValues['DASH'][3])))
    label_doge_price['price'].config(text=('({} {})'.format(coinValues['DOGE'][2], coinValues['DOGE'][3])))
    label_eth_price['price'].config(text=('({} {})'.format(coinValues['ETH'][2], coinValues['ETH'][3])))
    label_ltc_price['price'].config(text=('({} {})'.format(coinValues['LTC'][2], coinValues['LTC'][3])))
    label_nxt_price['price'].config(text=('({} {})'.format(coinValues['NXT'][2], coinValues['NXT'][3])))
    # label_str_price['price'].config(text=('({} {})'.format(coinValues['STR'][2], coinValues['STR'][3])))
    label_nem_price['price'].config(text=('({} {})'.format(coinValues['XEM'][2], coinValues['XEM'][3])))
    label_xrp_price['price'].config(text=('({} {})'.format(coinValues['XRP'][2], coinValues['XRP'][3])))

    # Setting Percent 
    if coinValues['BTC'][4][0] == '+':
        label_btc_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['BTC'][4]))
    else:
        label_btc_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['BTC'][4]))

    if coinValues['BCH'][4][0] == '+':
        label_bcc_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['BCH'][4]))
    else:
        label_bcc_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['BCH'][4]))

    if coinValues['DASH'][4][0] == '+':
        label_dash_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['DASH'][4]))
    else:
        label_dash_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['DASH'][4]))

    if coinValues['DOGE'][4][0] == '+':
        label_doge_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['DOGE'][4]))
    else:
        label_doge_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['DOGE'][4]))

    if coinValues['ETH'][4][0] == '+':
        label_eth_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['ETH'][4]))
    else:
        label_eth_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['ETH'][4]))

    if coinValues['LTC'][4][0] == '+':
        label_ltc_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['LTC'][4]))
    else:
        label_ltc_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['LTC'][4]))

    if coinValues['NXT'][4][0] == '+':
        label_nxt_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['NXT'][4]))
    else:
        label_nxt_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['NXT'][4]))

    # label_str_price['percent'].config(text=('{}'.format(coinValues['STR'][4])))
    if coinValues['XEM'][4][0] == '+':
        label_nem_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['XEM'][4]))
    else:
        label_nem_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['XEM'][4]))

    if coinValues['XRP'][4][0] == '+':
        label_xrp_price['percent'].config(fg="#00ff00", text=u'\u25b2 {}'.format(coinValues['XRP'][4]))
    else:
        label_xrp_price['percent'].config(fg="#ff0000", text=u'\u25bc {}'.format(coinValues['XRP'][4]))

    # Reschedule this function
    app.window.after(60000, get_coin_values)


# 
# The main function
# 
def main():
    global app, limit_entry
    global label_btc_price, label_bcc_price, label_dash_price, label_doge_price, label_eth_price, label_ltc_price, label_nxt_price, label_str_price, label_nem_price, label_xrp_price

    # Create Window Header
    app.create_header()

    # Get labels for price table 
    label_btc_price['text'] = app.create_price_table_label("BTC")
    label_btc_price['price'] = app.create_price_table_label("(0.0002)")
    label_btc_price['percent'] = app.create_price_table_label("2.4%")

    label_bcc_price['text'] = app.create_price_table_label("BCC")
    label_bcc_price['price'] = app.create_price_table_label("(0.0002)")
    label_bcc_price['percent'] = app.create_price_table_label("2.4%")

    label_dash_price['text'] = app.create_price_table_label("DASH")
    label_dash_price['price'] = app.create_price_table_label("(0.0002)")
    label_dash_price['percent'] = app.create_price_table_label("2.4%")

    label_doge_price['text'] = app.create_price_table_label("DOGE")
    label_doge_price['price'] = app.create_price_table_label("(0.0002)")
    label_doge_price['percent'] = app.create_price_table_label("2.4%")

    label_eth_price['text'] = app.create_price_table_label("ETH")
    label_eth_price['price'] = app.create_price_table_label("(0.0002)")
    label_eth_price['percent'] = app.create_price_table_label("2.4%")

    label_ltc_price['text'] = app.create_price_table_label("LTC")
    label_ltc_price['price'] = app.create_price_table_label("(0.0002)")
    label_ltc_price['percent'] = app.create_price_table_label("2.4%")

    label_nxt_price['text'] = app.create_price_table_label("NXT")
    label_nxt_price['price'] = app.create_price_table_label("(0.0002)")
    label_nxt_price['percent'] = app.create_price_table_label("2.4%")

    label_str_price['text'] = app.create_price_table_label("STR")
    label_str_price['price'] = app.create_price_table_label("(0.0002)")
    label_str_price['percent'] = app.create_price_table_label("2.4%")

    label_nem_price['text'] = app.create_price_table_label("NEM")
    label_nem_price['price'] = app.create_price_table_label("(0.0002)")
    label_nem_price['percent'] = app.create_price_table_label("2.4%")

    label_xrp_price['text'] = app.create_price_table_label("XRP")
    label_xrp_price['price'] = app.create_price_table_label("(0.0002)")
    label_xrp_price['percent'] = app.create_price_table_label("2.4%")

    # Load labels for price table
    app.load_price_table_label(label_btc_price['text'], rown=1, columnn=0)
    app.load_price_table_label(label_btc_price['price'], rown=1, columnn=1)
    app.load_price_table_label(label_btc_price['percent'], rown=1, columnn=2)

    app.load_price_table_label(label_bcc_price['text'], rown=2, columnn=0)
    app.load_price_table_label(label_bcc_price['price'], rown=2, columnn=1)
    app.load_price_table_label(label_bcc_price['percent'], rown=2, columnn=2)

    app.load_price_table_label(label_dash_price['text'], rown=3, columnn=0)
    app.load_price_table_label(label_dash_price['price'], rown=3, columnn=1)
    app.load_price_table_label(label_dash_price['percent'], rown=3, columnn=2)

    app.load_price_table_label(label_doge_price['text'], rown=4, columnn=0)
    app.load_price_table_label(label_doge_price['price'], rown=4, columnn=1)
    app.load_price_table_label(label_doge_price['percent'], rown=4, columnn=2)

    app.load_price_table_label(label_eth_price['text'], rown=5, columnn=0)
    app.load_price_table_label(label_eth_price['price'], rown=5, columnn=1)
    app.load_price_table_label(label_eth_price['percent'], rown=5, columnn=2)

    app.load_price_table_label(label_ltc_price['text'], rown=6, columnn=0)
    app.load_price_table_label(label_ltc_price['price'], rown=6, columnn=1)
    app.load_price_table_label(label_ltc_price['percent'], rown=6, columnn=2)

    app.load_price_table_label(label_nxt_price['text'], rown=7, columnn=0)
    app.load_price_table_label(label_nxt_price['price'], rown=7, columnn=1)
    app.load_price_table_label(label_nxt_price['percent'], rown=7, columnn=2)

    app.load_price_table_label(label_str_price['text'], rown=8, columnn=0)
    app.load_price_table_label(label_str_price['price'], rown=8, columnn=1)
    app.load_price_table_label(label_str_price['percent'], rown=8, columnn=2)

    app.load_price_table_label(label_nem_price['text'], rown=9, columnn=0)
    app.load_price_table_label(label_nem_price['price'], rown=9, columnn=1)
    app.load_price_table_label(label_nem_price['percent'], rown=9, columnn=2)

    app.load_price_table_label(label_xrp_price['text'], rown=10, columnn=0)
    app.load_price_table_label(label_xrp_price['price'], rown=10, columnn=1)
    app.load_price_table_label(label_xrp_price['percent'], rown=10, columnn=2)

    # Get checkboxes for Main Coin Selector
    checkbox_btc_main = Tkinter.Radiobutton(app.window, text="BTC", variable=main_coin, value="btc", command=do_analyze_coin)
    checkbox_bcc_main = Tkinter.Radiobutton(app.window, text="BCC", variable=main_coin, value="bcc", command=do_analyze_coin)
    checkbox_dash_main = Tkinter.Radiobutton(app.window, text="DASH", variable=main_coin, value="dash", command=do_analyze_coin)
    checkbox_doge_main = Tkinter.Radiobutton(app.window, text="DOGE", variable=main_coin, value="doge", command=do_analyze_coin)
    checkbox_eth_main = Tkinter.Radiobutton(app.window, text="ETH", variable=main_coin, value="eth", command=do_analyze_coin)
    checkbox_ltc_main = Tkinter.Radiobutton(app.window, text="LTC", variable=main_coin, value="ltc", command=do_analyze_coin)
    checkbox_nxt_main = Tkinter.Radiobutton(app.window, text="NXT", variable=main_coin, value="nxt", command=do_analyze_coin)
    checkbox_str_main = Tkinter.Radiobutton(app.window, text="STR", variable=main_coin, value="str", command=do_analyze_coin)
    checkbox_nem_main = Tkinter.Radiobutton(app.window, text="NEM", variable=main_coin, value="xem", command=do_analyze_coin)
    checkbox_xrp_main = Tkinter.Radiobutton(app.window, text="XRP", variable=main_coin, value="xrp", command=do_analyze_coin)

    # Get checkboxes for Coin Selector
    checkbox_btc = Tkinter.Radiobutton(app.window, text="BTC", variable=coin, value="btc", command=do_analyze_coin)
    checkbox_bcc = Tkinter.Radiobutton(app.window, text="BCC", variable=coin, value="bcc", command=do_analyze_coin)
    checkbox_dash = Tkinter.Radiobutton(app.window, text="DASH", variable=coin, value="dash", command=do_analyze_coin)
    checkbox_doge = Tkinter.Radiobutton(app.window, text="DOGE", variable=coin, value="doge", command=do_analyze_coin)
    checkbox_eth = Tkinter.Radiobutton(app.window, text="ETH", variable=coin, value="eth", command=do_analyze_coin)
    checkbox_ltc = Tkinter.Radiobutton(app.window, text="LTC", variable=coin, value="ltc", command=do_analyze_coin)
    checkbox_nxt = Tkinter.Radiobutton(app.window, text="NXT", variable=coin, value="nxt", command=do_analyze_coin)
    checkbox_str = Tkinter.Radiobutton(app.window, text="STR", variable=coin, value="str", command=do_analyze_coin)
    checkbox_nem = Tkinter.Radiobutton(app.window, text="NEM", variable=coin, value="xem", command=do_analyze_coin)
    checkbox_xrp = Tkinter.Radiobutton(app.window, text="XRP", variable=coin, value="xrp", command=do_analyze_coin)

    # Load Coin selector Button
    app.load_coin_selector_checkbox(checkbox_btc_main, rown=1, columnn=3)
    app.load_coin_selector_checkbox(checkbox_bcc_main, rown=2, columnn=3)
    app.load_coin_selector_checkbox(checkbox_dash_main, rown=3, columnn=3)
    app.load_coin_selector_checkbox(checkbox_doge_main, rown=4, columnn=3)
    app.load_coin_selector_checkbox(checkbox_eth_main, rown=5, columnn=3)
    app.load_coin_selector_checkbox(checkbox_ltc_main, rown=6, columnn=3)
    app.load_coin_selector_checkbox(checkbox_nxt_main, rown=7, columnn=3)
    app.load_coin_selector_checkbox(checkbox_str_main, rown=8, columnn=3)
    app.load_coin_selector_checkbox(checkbox_nem_main, rown=9, columnn=3)
    app.load_coin_selector_checkbox(checkbox_xrp_main, rown=10, columnn=3)

    # Load Coin selector Button
    app.load_coin_selector_checkbox(checkbox_btc, rown=1, columnn=4)
    app.load_coin_selector_checkbox(checkbox_bcc, rown=2, columnn=4)
    app.load_coin_selector_checkbox(checkbox_dash, rown=3, columnn=4)
    app.load_coin_selector_checkbox(checkbox_doge, rown=4, columnn=4)
    app.load_coin_selector_checkbox(checkbox_eth, rown=5, columnn=4)
    app.load_coin_selector_checkbox(checkbox_ltc, rown=6, columnn=4)
    app.load_coin_selector_checkbox(checkbox_nxt, rown=7, columnn=4)
    app.load_coin_selector_checkbox(checkbox_str, rown=8, columnn=4)
    app.load_coin_selector_checkbox(checkbox_nem, rown=9, columnn=4)
    app.load_coin_selector_checkbox(checkbox_xrp, rown=10, columnn=4)

    # Create Option Menu for duration
    limit_option_value
    Tkinter.Label(text="Limit (Max. 2000) : ").grid(row=11, column=0)
    limit_entry.grid(row=11, column=1)


    # Load the window
    app.window.after(1000, get_coin_values)
    app.load()


if __name__ == "__main__":
    main()
