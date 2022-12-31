# <--------Import statements-------->
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

# <--------Initializing Flask App-------->
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
API_AUTH = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMmFhOGQzNTgzODVhYjZlYzA0MDgwYTdjOGU3MmQ3OSIsInN1YiI6IjYzNzEwYWQ4Nzk4ZTA2MDA3ODg1YWFhZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.poOUW9FnkZZ4dx10yxlDG-8rCQbKMT_5puxcD9SAK6Q'


# <--------Creating Flask Form-------->
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Paste the location link of the Coffee Shop', validators=[URL()])
    opening_time = StringField('Enter the opening time', validators=[DataRequired()])
    closing_time = StringField('Enter the closing time', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Give a rating 1 to 5',
        choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
        validators=[DataRequired()]
    )
    wifi_strength = SelectField(
        "What's the strength of th WiFi?",
        choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
        validators=[DataRequired()]
    )
    power_rating = SelectField(
        "Give the rating for power",
        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


# <--------Flask Routes-------->
@app.route("/")
def home():
    return render_template("index.html")


# <--------To add new cafes to the list-------->
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.opening_time.data},"
                           f"{form.closing_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_strength.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows = []
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')  # Here the delimiter is "," (Comma Separated Values)
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
