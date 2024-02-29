# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, Length

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])

class UpdateForm(FlaskForm):
    firstname     = StringField('Firstname',
                         id='firstname_update',
                         validators=[Length(max=64)])
    lastname      = StringField('Lastname',
                         id='lastname_update',
                         validators=[Length(max=64)])
    address       = StringField('Address',
                         id='address_update',
                         validators=[Length(max=64)])
    city          = StringField('City',
                         id='city_update',
                         validators=[Length(max=64)])
    country       = StringField('Country',
                         id='country_update',
                         validators=[Length(max=64)])
    po_box        = StringField('po_box',
                         id='po_box_update',
                         validators=[Length(max=64)])
    short_desc    = StringField('ShortDesc',
                         id='short_update',
                         validators=[Length(max=100)])
    long_desc     = StringField('LongDesc',
                         id='long_update',
                         validators=[Length(max=200)])
