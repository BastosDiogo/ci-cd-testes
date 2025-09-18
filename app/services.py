from generic_class import GenericAPI

class EmailService(GenericAPI):
    def start(self):
        return "Email service started"

    def shutdown(self):
        return "Email service stopped"


class MisconfiguredService(GenericAPI):
    def start(self):
        return "Misconfigured start"

     # Invalid at runtime
    shutdown = "not a method"
