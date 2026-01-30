class Verb:
    def __init__(self, default_response, synonyms=[]) -> None:
        self.default_response = default_response
        self.synonyms = synonyms

    def get_default_response(self):
        return self.default_response

    def get_synonyms(self):
        return self.synonyms
