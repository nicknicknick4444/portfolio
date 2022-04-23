from datetime import datetime


def convert_date(d):
    datey_conv = datetime.strptime(d, "%Y-%m-%d").date()
    print("YOOOO!", datey_conv, type(datey_conv))
    return datey_conv
