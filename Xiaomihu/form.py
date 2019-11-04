from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,HiddenField,SubmitField,SelectField
from wtforms.validators import DataRequired,Email


class AdminForm(FlaskForm):
    title = StringField(label='标题', validators=[DataRequired(message='标题不能为空')],
                         render_kw={
                             'placeholder': u'请输入标题'
                         }
                         )
    typeId = SelectField(label='文章类型',choices=[('1','测试分类1'),('2','测试分类2')])
    content = TextAreaField(label='内容', validators=[DataRequired()])
    submit = SubmitField(label='提交')

class MessageForm(FlaskForm):
    content = TextAreaField(label='留言内容', validators=[DataRequired()],
                            render_kw={
                                'placeholder': u'你也来说两句吧！点击这里输入留言内容'
                            }
                            )
    name = StringField(label='昵称', validators=[DataRequired()],
                       render_kw={
                           'placeholder': u'Your Name'
                       }
                       )
    email = StringField(label='邮箱', validators=[Email(message='无效的邮箱格式'),DataRequired()],
                        render_kw={
                            'placeholder': u'Your Email'
                        }
                        )
    submit = SubmitField(label='提交')
