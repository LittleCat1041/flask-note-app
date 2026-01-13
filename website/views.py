from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        #Gets the note from the HTML 
        note = request.form.get('note') 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            #บันทึก Note โดยระบุ user_id ของผู้ใช้ที่ Login อยู่ในขณะนั้น (current_user)
            #เพื่อให้มั่นใจว่า Note นี้จะเป็นของผู้ใช้นั้นเพียงคนเดียว
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data.decode('utf-8'))
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


