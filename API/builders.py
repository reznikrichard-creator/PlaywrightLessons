


def make_booking(**overides): 
    booking = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
        }

    booking.update(overides)
    return booking

# make_booking()
# make_booking(
#     first="Liquids"
#     )