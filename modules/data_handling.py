import json


class DataHandler:
    def __init__(self):
        self.path = 'resources/clipboard_data.json'

        if not self.file_exists():
            with open(self.path, mode='w', encoding='utf-8') as f:
                json.dump({'text':'', 'timestamp':None}, f, ensure_ascii=False)


    def retrieve(self):
        with open(self.path, mode='r', encoding='utf-8') as f:
            content = json.load(f)

        return content

    def save(self, data):
        with open(self.path, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return 0

    def clear(self, data):
        with open(self.path, mode='w', encoding='utf-8') as f:
            json.dump({'text':'', 'timestamp':None}, f, ensure_ascii=False)

        return 0


    def file_exists(self):
        try:
            with open(self.path, mode='r'):
                return True
        except FileNotFoundError:
            return False