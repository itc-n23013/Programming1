def f(*args, separator="."):
    return separator.join(args)


print(f("3_choume", "ozato", "okinawa", "okinawa", "japan", separator=" "))
