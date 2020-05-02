class TablesManager():
    def __init__(self, client):
        self.client = client
        self.max_ids = {}