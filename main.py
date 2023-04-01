from api.posts import PostListRes
from api.users import RegisterRes, LoginRes
from app.app2 import main_app


@main_app.route('/', defaults={'path': ''})
@main_app.route('/u/<path:path>')
@main_app.route('/a/<path:path>')
def root(path):
    return main_app.send_static_file('index.html')


main_app.api.add_resource(RegisterRes, '/api/register')
main_app.api.add_resource(LoginRes, '/api/login')
main_app.api.add_resource(PostListRes, '/api/posts/')

if __name__ == '__main__':
    main_app.run()
