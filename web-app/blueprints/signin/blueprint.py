from flask import Blueprint,render_template

signin_page = Blueprint('sigin_page',__name__)


@signin_page.route('/signin')
def display():
    """
    View function for displaying the sign-in page
    Parameter:
        NONE
    :return:
        render template
    """
    return render_template("signin.html")