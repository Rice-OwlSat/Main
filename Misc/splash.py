def show_splash():
    try:
        with open("/splash", "r") as f:
            text = f.read()
        print(text)
    except Exception as e:
        print("Splash error:", e)
