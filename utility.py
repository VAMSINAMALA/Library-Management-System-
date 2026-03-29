def input_is_valid(msg, start=0, end=None):
    while True:
        inp = input(msg)

        # ❌ not a number
        if not inp.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        inp = int(inp)

        # ✅ check range if provided
        if start is not None and end is not None:
            if start <= inp <= end:
                return inp
            else:
                print(f"Enter a number between {start} and {end}")
        else:
            return inp