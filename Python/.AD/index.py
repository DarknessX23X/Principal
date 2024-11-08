from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from pyad import *
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

pyad.set_defaults(
    ldap_server='192.168.0.53',
    domain='kazzo1.sys',
    username='administrador@kazzo1.sys',
    password='Tec2024K@3,14colli'
)

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    #user = ADUser.from_cn(user_id)
    #return User(user.get_attribute('cn'), user.get_attribute('cn'), user.get_attribute('password')[0])
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = load_user(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return 'Nome de usuário ou senha inválidos'

    # Obter usuários do Active Directory
    users = []
    ldap_server = '192.168.0.53'
    domain = 'kazzo1.sys'
    username = 'administrador@kazzo1.sys'
    password = 'Tec2024K@3,14colli'

    # Conecta ao AD
    pyad.set_defaults(ldap_server=ldap_server, domain=domain, username=username, password=password)

    # Cria um objeto ADContainer para a unidade organizacional "Usuarios"
    container = pyad.adcontainer.ADContainer.from_dn('ou=Usuarios,dc=kazzo1,dc=sys')

    # Lista os usuários do AD
    usuarios = container.get_children()

# Imprime a lista de usuários
    for user in usuarios:
        print(user.get_attribute('sAMAccountName'))

    return render_template('login.html', users=users)


@app.route('/')
@login_required
def home():
    return 'Bem-vindo, {}!'.format(current_user.username)


if __name__ == '__main__':
    app.run(debug=True)