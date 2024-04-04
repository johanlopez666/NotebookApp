from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"
    creation_date: datetime = field(default_factory=datetime.now)
    tags: list[str] = field(default_factory=list)

    def str(self) -> str:
        return (f"Code: {self.code}\n"
                f"Creation date: {self.creation_date}\n"
                f"{self.title}: {self.text}")

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


class Notebook:
    def init(self):
        self.notes: dict[int, Note] = {}

    def add_note(self, title: str, text: str, importance: str):
        code = len(self.notes) + 1
        self.notes[code] = Note(code, title, text, importance)
        return code

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes.values() if note.importance in [Note.HIGH, Note.MEDIUM]]

    def tags_note_count(self) -> dict[str, int]:
        tag_count: dict[str, int] = {}
        for note in self.notes.values():
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count
