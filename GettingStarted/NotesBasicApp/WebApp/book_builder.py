from note import Note


class BookBuilder:
    def __init__(self):
        self.notes = []


    def create_note(self, title, conent):
        new_note = Note(title, conent)
        self.notes.append(new_note)


    def get_notes(self):
        return self.notes
        