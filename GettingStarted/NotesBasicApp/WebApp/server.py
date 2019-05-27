from flask import Flask, render_template, redirect, url_for, request

from book_builder import BookBuilder
builder = BookBuilder()

app = Flask(__name__)

@app.route("/")
def hello():
    if request.method == "POST":
        new_note_title = request.form.get("note-title", "")
        new_note_content = request.form.get("note-content", "")

        builder.create_note(new_note_title, new_note_content)
        notes = builder.get_notes()


    return render_template("index.html")


@app.route("/notes", methods=["POST", "GET"])
def notes_page():

    return render_template("notes.html")


if __name__ == "__main__":
    app.run()