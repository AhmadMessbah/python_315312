if (re.match(r"^[1-9]{7}$", id)
        and re.match(r"^[a-zA-z\s]{2,20}$", name)
        and re.match(r"^[a-zA-z\s]{2,20}$", brand)
        and re.match(r"^[a-zA-z\s]{2,20}$", model)
        and re.match(r"^[1-9a-zA-Z]{20}$", barcode)
        and type(buy_price) == int and type(sell_price) == int):