from flask_assets import Bundle

common_css = Bundle(
    'main/css/vendor/bootstrap.css',
    'main/css/vendor/fontawesome-all.css',
    'main/css/main.css',
    filters='cssmin',
    output='public/css/common.css'
)

common_js = Bundle(
    'main/js/vendor/jquery.js',
    'main/js/vendor/popper.js',
    'main/js/vendor/bootstrap.js',
    Bundle(
        'main/js/main.js',
        filters='jsmin'
    ),
    output='public/js/common.js'
)

admin_js = Bundle(
    Bundle(
        'admin-view/js/admin.js',
        filters='jsmin'
    ),
    output='public/js/admin.js'

)

useredit_js = Bundle(
    Bundle(
        'admin-view/js/useredit.js',
        filters='jsmin'
    ),
    output='public/js/useredit.js'

)

user_css = Bundle(
    'user-view/css/user.css',
    filters='cssmin',
    output='public/css/user.css'
)

script_js = Bundle(
    Bundle(
        'user-view/js/script.js',
        filters='jsmin'
    ),
    output='public/js/script.js'
)
