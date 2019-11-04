from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,HiddenField,SubmitField,SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(label='标题', validators=[DataRequired(message='标题不能为空')],
                         render_kw={
                             'placeholder': u'请输入标题'
                         }
                         )
    typeId = SelectField(label='文章类型',choices=[('1','测试分类1'),('2','测试分类2')])
    content = TextAreaField(label='内容', validators=[DataRequired()])
    submit = SubmitField(label='提交')

class PostForms(FlaskForm):
    #...
    body_html = HiddenField()