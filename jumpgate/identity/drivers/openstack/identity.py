from jumpgate.shared.drivers.responder import setup_responder


def setup_routes(app, disp):
    return setup_responder(app, disp)
