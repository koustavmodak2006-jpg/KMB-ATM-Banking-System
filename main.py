from tkinter import *
import time
import json
from datetime import datetime

# ─────────────────────────────────────────────
#  TERMINAL LOGGER
# ─────────────────────────────────────────────

CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

def _ts():
    return datetime.now().strftime("%H:%M:%S")

def _bar(char="─", width=52):
    return char * width

def banner_startup():
    print(f"\n{CYAN}{BOLD}")
    print("╔══════════════════════════════════════════════════╗")
    print("║     ██╗  ██╗███╗   ███╗██████╗                 ║")
    print("║     ██║ ██╔╝████╗ ████║██╔══██╗                ║")
    print("║     █████╔╝ ██╔████╔██║██║  ██║                ║")
    print("║     ██╔═██╗ ██║╚██╔╝██║██║  ██║                ║")
    print("║     ██║  ██╗██║ ╚═╝ ██║██████╔╝                ║")
    print("║     ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝                 ║")
    print("║          ATM SIMULATOR  v1.0  by Som            ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"{RESET}")

def log_lang_selected(lang):
    print(f"{BLUE}[{_ts()}] 🌐  LANGUAGE SELECTED{RESET}")
    print(f"  └─ Language : {BOLD}{lang}{RESET}")
    print(f"  {_bar()}")

def log_kmd_entered(kmd, valid):
    if valid:
        print(f"{GREEN}[{_ts()}] ✅  KMD VALIDATED{RESET}")
        print(f"  └─ KMD ID   : {BOLD}{kmd}{RESET}")
    else:
        print(f"{RED}[{_ts()}] ❌  INVALID KMD{RESET}")
        print(f"  └─ Attempted: {BOLD}{kmd}{RESET}")
    print(f"  {_bar()}")

def log_option_selected(option):
    icons = {"WITHDRAW": "💸", "DEPOSIT": "📥", "BALANCE": "📊"}
    icon = icons.get(option, "🔘")
    print(f"{YELLOW}[{_ts()}] {icon}  OPTION SELECTED{RESET}")
    print(f"  └─ Action   : {BOLD}{option}{RESET}")
    print(f"  {_bar()}")

def log_amount_entered(amount, mode):
    print(f"{MAGENTA}[{_ts()}] 🔢  AMOUNT ENTERED{RESET}")
    print(f"  ├─ Mode     : {mode}")
    print(f"  └─ Amount   : {BOLD}₹ {amount}{RESET}")
    print(f"  {_bar()}")

def log_pin_attempt(success):
    if success:
        print(f"{GREEN}[{_ts()}] 🔓  PIN CORRECT — ACCESS GRANTED{RESET}")
    else:
        print(f"{RED}[{_ts()}] 🔒  PIN INCORRECT — ACCESS DENIED{RESET}")
    print(f"  {_bar()}")

def log_withdraw(kmd, amount, balance_before, balance_after, success):
    if success:
        print(f"{GREEN}[{_ts()}] 💸  WITHDRAWAL SUCCESSFUL{RESET}")
        print(f"  ├─ Account  : {BOLD}{kmd}{RESET}")
        print(f"  ├─ Amount   : {BOLD}₹ {amount}{RESET}")
        print(f"  ├─ Before   : ₹ {balance_before}")
        print(f"  └─ After    : ₹ {balance_after}")
    else:
        print(f"{RED}[{_ts()}] ⚠️   WITHDRAWAL FAILED{RESET}")
        print(f"  ├─ Account  : {BOLD}{kmd}{RESET}")
        print(f"  └─ Reason   : Insufficient balance")
    print(f"  {_bar()}")

def log_deposit(kmd, amount, balance_before, balance_after):
    print(f"{GREEN}[{_ts()}] 📥  DEPOSIT SUCCESSFUL{RESET}")
    print(f"  ├─ Account  : {BOLD}{kmd}{RESET}")
    print(f"  ├─ Amount   : {BOLD}₹ {amount}{RESET}")
    print(f"  ├─ Before   : ₹ {balance_before}")
    print(f"  └─ After    : ₹ {balance_after}")
    print(f"  {_bar()}")

def log_balance_enquiry(kmd, balance):
    print(f"{CYAN}[{_ts()}] 📊  BALANCE ENQUIRY{RESET}")
    print(f"  ├─ Account  : {BOLD}{kmd}{RESET}")
    print(f"  └─ Balance  : {BOLD}₹ {balance}{RESET}")
    print(f"  {_bar()}")

def log_session_end(kmd):
    print(f"\n{CYAN}[{_ts()}] 👋  SESSION ENDED{RESET}")
    print(f"  └─ Account  : {kmd if kmd else 'N/A'}")
    print(f"\n{CYAN}" + "═" * 52 + f"{RESET}\n")

def log_keypress(key):
    print(f"{MAGENTA}[{_ts()}] ⌨️   KEY PRESS  →  {BOLD}{key}{RESET}")

def log_clear(field, remaining):
    val = f"'{remaining}'" if remaining else "(empty)"
    print(f"{YELLOW}[{_ts()}] 🔙  CLEAR       →  field now {val}{RESET}")

# ─────────────────────────────────────────────
#  ATM APPLICATION
# ─────────────────────────────────────────────

with open("account.json", "r") as file:
    data = json.load(file)

banner_startup()

window = Tk()
window.title("ATM")
window.config(height=600, width=400)

canvas = Canvas(height=640, width=500, highlightthickness=0)
canvas.grid(row=0, column=0)

atm_screen     = PhotoImage(file="./images/back.png")
img_on_canvas  = canvas.create_image(250, 325, image=atm_screen)
lang_choice    = PhotoImage(file="./images/lang.png")
lang_canvas    = canvas.create_image(250, 325, image=lang_choice)
canvas.coords(lang_canvas, 253, 201)

option_choice  = PhotoImage(file="./images/choice.png")
amount_choice  = PhotoImage(file="./images/amount.png")
wait_time      = PhotoImage(file="./images/wait.png")
thanks_image   = PhotoImage(file="./images/thank.png")
kmd_id_image   = PhotoImage(file="./images/kmb_id.png")
continue_      = PhotoImage(file="./images/continue.png")
deposit_img    = PhotoImage(file="./images/deposit_money.png")
yes            = PhotoImage(file="./images/yes.png")
deposit_success = PhotoImage(file="./images/deposit_success.png")

page          = 0
cash_withdraw = ""
given         = 0
PIN           = ""
KMD           = ""
Deposit_Money = ""
PageName      = ""

but_1_img    = PhotoImage(file="./images/1.png")
but_2_img    = PhotoImage(file="./images/2.png")
but_3_img    = PhotoImage(file="./images/3.png")
but_4_img    = PhotoImage(file="./images/4.png")
but_5_img    = PhotoImage(file="./images/5.png")
but_6_img    = PhotoImage(file="./images/6.png")
but_7_img    = PhotoImage(file="./images/7.png")
but_8_img    = PhotoImage(file="./images/8.png")
but_9_img    = PhotoImage(file="./images/9.png")
but_0_img    = PhotoImage(file="./images/0.png")
but_clr_img  = PhotoImage(file="./images/clr.png")
but_exit_img = PhotoImage(file="./images/exit.png")
but_ent_img  = PhotoImage(file="./images/enter.png")
but_doubz    = PhotoImage(file="./images/doub0.png")
pin_canvas_image      = PhotoImage(file="./images/pin.png")
balance_querry_image  = PhotoImage(file="./images/Balan_enq.png")
invalid_image         = PhotoImage(file="./images/invalid.png")
balance               = PhotoImage(file="./images/balance.png")

# ─────────────────────────────────────────────
#  DIGIT INPUT HANDLER  (replaces b_1…b_0)
# ─────────────────────────────────────────────

def _input_digit(digit):
    """Central handler for every digit / double-zero button."""
    global KMD, cash_withdraw, Deposit_Money, PIN

    log_keypress(digit)

    if page == 1:
        KMD += digit
        canvas.itemconfig(kmd_pin, text=int(KMD))

    elif page == 3:
        if PageName == "WITHDRAW_PAGE":
            cash_withdraw += digit
            canvas.itemconfig(cash, text=int(cash_withdraw))
        elif PageName == "DEPOSIT_PAGE":
            Deposit_Money += digit
            canvas.itemconfig(deposit_amt, text=int(Deposit_Money))

    elif page == 4:
        PIN += digit
        canvas.itemconfig(pin, text=int(PIN))

def b_1():  _input_digit("1")
def b_2():  _input_digit("2")
def b_3():  _input_digit("3")
def b_4():  _input_digit("4")
def b_5():  _input_digit("5")
def b_6():  _input_digit("6")
def b_7():  _input_digit("7")
def b_8():  _input_digit("8")
def b_9():  _input_digit("9")
def b_0():  _input_digit("0")
def b_00(): _input_digit("00")

# ─────────────────────────────────────────────
#  CLEAR
# ─────────────────────────────────────────────

def clear():
    global KMD, cash_withdraw, Deposit_Money, PIN

    if page == 1:
        KMD = KMD[:-1]
        canvas.itemconfig(kmd_pin, text=int(KMD) if KMD else "")
        log_clear("KMD", KMD)

    elif page == 3:
        if PageName == "WITHDRAW_PAGE":
            cash_withdraw = cash_withdraw[:-1]
            canvas.itemconfig(cash, text=int(cash_withdraw) if cash_withdraw else "")
            log_clear("Withdraw amount", cash_withdraw)
        elif PageName == "DEPOSIT_PAGE":
            Deposit_Money = Deposit_Money[:-1]
            canvas.itemconfig(deposit_amt, text=int(Deposit_Money) if Deposit_Money else "")
            log_clear("Deposit amount", Deposit_Money)

    elif page == 4:
        PIN = PIN[:-1]
        canvas.itemconfig(pin, text=int(PIN) if PIN else "")
        log_clear("PIN", PIN)

# ─────────────────────────────────────────────
#  BUTTONS
# ─────────────────────────────────────────────

button_1    = Button(image=but_1_img,    highlightthickness=0, command=b_1)
button_1.place(x=25,  y=437)
button_2    = Button(image=but_2_img,    highlightthickness=0, command=b_2)
button_2.place(x=121, y=437)
button_3    = Button(image=but_3_img,    highlightthickness=0, command=b_3)
button_3.place(x=215, y=437)
button_4    = Button(image=but_4_img,    highlightthickness=0, command=b_4)
button_4.place(x=25,  y=487)
button_5    = Button(image=but_5_img,    highlightthickness=0, command=b_5)
button_5.place(x=121, y=487)
button_6    = Button(image=but_6_img,    highlightthickness=0, command=b_6)
button_6.place(x=215, y=487)
button_7    = Button(image=but_7_img,    highlightthickness=0, command=b_7)
button_7.place(x=25,  y=535)
button_8    = Button(image=but_8_img,    highlightthickness=0, command=b_8)
button_8.place(x=121, y=535)
button_9    = Button(image=but_9_img,    highlightthickness=0, command=b_9)
button_9.place(x=215, y=535)
button_0    = Button(image=but_0_img,    highlightthickness=0, command=b_0)
button_0.place(x=25,  y=584)
button_clr  = Button(image=but_clr_img,  highlightthickness=0, command=clear)
button_clr.place(x=339, y=437)
button_exit = Button(image=but_exit_img, highlightthickness=0, command="exit")
button_exit.place(x=339, y=486)
button_ent  = Button(image=but_ent_img,  highlightthickness=0, command="enter")
button_ent.place(x=339, y=535)
button_double_zero = Button(image=but_doubz, highlightthickness=0, command=b_00)
button_double_zero.place(x=121, y=584)

# ─────────────────────────────────────────────
#  KMD VALIDATION
# ─────────────────────────────────────────────

def kmd_validation():
    global page, KMD, kmd_text, continue_button
    kmd_text = canvas.itemcget(kmd_pin, "text")

    if kmd_text in data:
        log_kmd_entered(kmd_text, valid=True)
        page += 1
        eng()
    else:
        log_kmd_entered(KMD, valid=False)
        page = page + 0.1
        if page == 1.1:
            canvas.delete(kmd_id_canvas)
            kmd_id_validation.destroy()
            invalid_canvas = canvas.create_image(250, 325, image=invalid_image)
            canvas.coords(invalid_canvas, 253, 201)
            continue_button = Button(image=continue_, highlightthickness=0, command=eng)
            continue_button.place(x=335, y=305)
            page = 0
            KMD = ""

# ─────────────────────────────────────────────
#  LANGUAGE / MAIN MENU
# ─────────────────────────────────────────────

def eng():
    global kmd_id_canvas, kmd_pin, kmd_id_validation, page, KMD
    global withdraw_money, withdraw, deposit, bal_enq
    global deposit_money, balance_enquerry, option_canvas, deposit_

    if page == 0:
        log_lang_selected("English")
        try:
            continue_button.destroy()
            canvas.delete(invalid_canvas)
            kmd_id_validation.destroy()
            KMD = ""
        except:
            pass
        canvas.delete(lang_canvas)
        eng_lang.destroy()
        hindi_lang.destroy()
        tamil_lang.destroy()
        kmd_id_canvas = canvas.create_image(250, 325, image=kmd_id_image)
        canvas.coords(kmd_id_canvas, 253, 200)
        page += 1
        kmd_pin = canvas.create_text(250, 213, text="", font=("Arial", 20, "bold"), fill="black")
        kmd_id_validation = Button(image=continue_, highlightthickness=0, command=kmd_validation)
        kmd_id_validation.place(x=330, y=305)

    if page == 2:
        try:
            kmd_id_validation.destroy()
        except:
            pass
        option_canvas = canvas.create_image(250, 325, image=option_choice)
        canvas.coords(option_canvas, 253, 200)

        withdraw   = PhotoImage(file="./images/withdraw.png")
        withdraw_money = Button(image=withdraw, highlightthickness=0, command=withdraw_function)
        withdraw_money.place(x=324, y=208)

        deposit_   = PhotoImage(file="./images/deposit.png")
        deposit_money = Button(image=deposit_, highlightthickness=0, command=deposit_function)
        deposit_money.place(x=324, y=255)

        bal_enq    = PhotoImage(file="./images/bal_enq.png")
        balance_enquerry = Button(image=bal_enq, highlightthickness=0, command=balance_querry)
        balance_enquerry.place(x=74, y=164)

def hin():
    log_lang_selected("Hindi")
    eng()

def tam():
    log_lang_selected("Tamil")
    eng()

# ─────────────────────────────────────────────
#  OPTION HANDLERS
# ─────────────────────────────────────────────

def balance_querry():
    global page
    log_option_selected("BALANCE")
    page += 1
    canvas.delete(option_canvas)
    withdraw_money.destroy()
    deposit_money.destroy()
    balance_enquerry.destroy()
    pin_page()

def deposit_function():
    global deposit_page, continue_button_deposit, deposit_amt, PageName, page
    log_option_selected("DEPOSIT")
    page += 1
    PageName = "DEPOSIT_PAGE"
    canvas.delete(option_canvas)
    withdraw_money.destroy()
    deposit_money.destroy()
    balance_enquerry.destroy()
    deposit_page = canvas.create_image(250, 325, image=deposit_img)
    canvas.coords(deposit_page, 253, 200)
    deposit_amt = canvas.create_text(250, 272, text="0", font=("Arial", 18, "normal"), fill="green")
    continue_button_deposit = Button(image=continue_, highlightthickness=0, command=_on_deposit_continue)
    continue_button_deposit.place(x=333, y=305)

def _on_deposit_continue():
    if Deposit_Money:
        log_amount_entered(Deposit_Money, "DEPOSIT")
    pin_page()

def withdraw_function():
    global page, amount_canvas, cash, total, PageName
    log_option_selected("WITHDRAW")
    PageName = "WITHDRAW_PAGE"
    page += 1
    canvas.delete(option_canvas)
    withdraw_money.destroy()
    deposit_money.destroy()
    balance_enquerry.destroy()
    amount_canvas = canvas.create_image(250, 325, image=amount_choice)
    canvas.coords(amount_canvas, 253, 201)
    if page == 3:
        cash  = canvas.create_text(260, 203, text="0", font=("Arial", 14, "normal"))
        total = Button(image=yes, highlightthickness=0, command=_on_withdraw_confirm)
        total.place(x=320, y=255)

def _on_withdraw_confirm():
    if cash_withdraw:
        log_amount_entered(cash_withdraw, "WITHDRAW")
    pin_page()

# ─────────────────────────────────────────────
#  PIN PAGE
# ─────────────────────────────────────────────

def pin_page():
    global page, pin, pin_canvas, withdraw_page
    page += 1
    try:
        canvas.delete(amount_canvas)
        total.destroy()
    except:
        pass
    try:
        continue_button_deposit.destroy()
        canvas.delete(deposit_page)
    except:
        pass
    pin_canvas = canvas.create_image(250, 325, image=pin_canvas_image)
    canvas.coords(pin_canvas, 253, 200)
    if page == 4:
        pin = canvas.create_text(250, 175, text="", font=("Arial", 18, "normal"))
        withdraw_page = Button(image=yes, highlightthickness=0, command=pin_validation)
        withdraw_page.place(x=320, y=255)

# ─────────────────────────────────────────────
#  PIN VALIDATION
# ─────────────────────────────────────────────

def pin_validation():
    global invalid_canvas, continue_button, page, cash_withdraw, PIN, Deposit_Money
    pin_text = canvas.itemcget(pin, "text")

    if pin_text and int(data[kmd_text]["pin"]) == int(pin_text):
        log_pin_attempt(success=True)
        total_cash()
    else:
        log_pin_attempt(success=False)
        page = page + 0.1
        if page == 4.1:
            canvas.delete(pin_canvas)
            withdraw_page.destroy()
            invalid_canvas = canvas.create_image(250, 325, image=invalid_image)
            canvas.coords(invalid_canvas, 253, 201)
            continue_button = Button(image=continue_, highlightthickness=0, command=eng)
            continue_button.place(x=335, y=305)
            page = 0
            cash_withdraw = ""
            Deposit_Money = ""
            PIN = ""

# ─────────────────────────────────────────────
#  TRANSACTION PROCESSING
# ─────────────────────────────────────────────

def total_cash():
    global page, given, balance_amt
    page += 1
    canvas.delete(pin_canvas)
    withdraw_page.destroy()

    # ── DEPOSIT ──────────────────────────────
    if Deposit_Money != "" and cash_withdraw == "":
        bal_before = data[kmd_text]["balance"]
        data[kmd_text]["balance"] += int(Deposit_Money)
        log_deposit(kmd_text, int(Deposit_Money), bal_before, data[kmd_text]["balance"])
        with open("account.json", "w") as file:
            json.dump(data, file, indent=4)

        deposit_balance = canvas.create_image(250, 325, image=deposit_success)
        canvas.coords(deposit_balance, 253, 201)
        canvas.create_text(263, 231, text=Deposit_Money, font=("Arial", 14, "bold"), fill="green")
        canvas.create_text(260, 308, text=KMD, font=("Arial", 16, "bold"), fill="green")

    # ── BALANCE ENQUIRY ───────────────────────
    elif Deposit_Money == "" and cash_withdraw == "":
        log_balance_enquiry(KMD, data[KMD]["balance"])

        balance_amt = canvas.create_image(250, 325, image=balance)
        canvas.coords(balance_amt, 253, 201)
        canvas.create_text(263, 245, text=data[KMD]["balance"], font=("Arial", 24, "bold"), fill="green")
        canvas.create_text(280, 300, text=KMD, font=("Arial", 12, "bold"), fill="green")
        continue_button = Button(image=continue_, highlightthickness=0, command="exit")
        continue_button.place(x=335, y=315)

    # ── WITHDRAWAL ────────────────────────────
    else:
        wait_canvas = canvas.create_image(250, 325, image=wait_time)
        canvas.coords(wait_canvas, 253, 201)
        text_id = canvas.create_text(380, 139, text="0", font=("Arial", 18, "bold"), fill="red")

        bal_before = data[kmd_text]["balance"]

        while given < int(cash_withdraw) and data[KMD]["balance"] > given:
            time.sleep(0.5)
            given += 500
            canvas.itemconfig(text_id, text=f"-{str(given)}")
            window.update()

        success = given > 0
        data[kmd_text]["balance"] -= given
        with open("account.json", "w") as file:
            json.dump(data, file, indent=4)

        log_withdraw(kmd_text, cash_withdraw, bal_before, data[kmd_text]["balance"], success)

        time.sleep(1)
        log_session_end(kmd_text)

        canvas.delete(wait_canvas)
        thanks_canvas = canvas.create_image(250, 325, image=thanks_image)
        canvas.coords(thanks_canvas, 253, 201)

# ─────────────────────────────────────────────
#  LANGUAGE BUTTONS  (initial screen)
# ─────────────────────────────────────────────

english    = PhotoImage(file="./images/eng.png")
hindi      = PhotoImage(file="./images/hindi.png")
tamil      = PhotoImage(file="./images/tamil.png")
eng_lang   = Button(image=english,  highlightthickness=0, command=eng)
hindi_lang = Button(image=hindi,    highlightthickness=0, command=hin)
tamil_lang = Button(image=tamil,    highlightthickness=0, command=tam)
eng_lang.place(x=303,  y=165)
hindi_lang.place(x=303, y=213)
tamil_lang.place(x=303, y=261)

window.mainloop()