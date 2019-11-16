import base64

tickets = [
    {
        "name": "Eurostar",
        "destinationLabel": "Paris - Gare du Nord",
        "startDateTime": "2019-11-18T12:48:00Z",
        "ticket": base64.b64encode(open("data/ticket_one.png", "rb").read()).decode()
    },
    {
        "name": "Flixbus",
        "destinationLabel": "Munich",
        "startDateTime": "2019-11-18T15:26:00Z",
        "ticket": base64.b64encode(open("data/ticket_two.png", "rb").read()).decode()
    }
]