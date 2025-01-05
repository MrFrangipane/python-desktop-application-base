from desktopapplicationbase.actions.handlers.abstract import ActionAbstractHandler


class TriggerSimpleHandler(ActionAbstractHandler):

    def __init__(self, callable_: callable):
        super().__init__()
        self.callable = callable_

    def triggered(self):
        self.callable()
