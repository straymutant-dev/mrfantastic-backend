from django.contrib import admin
from django.contrib.admin import AdminSite

# Custom nav order: your content apps first, Django's built-in auth admin last
APP_ORDER = ['shop', 'orders', 'portfolio', 'auth']

def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)
    app_list = sorted(
        app_dict.values(),
        key=lambda x: APP_ORDER.index(x['app_label']) if x['app_label'] in APP_ORDER else len(APP_ORDER)
    )
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])
    return app_list

AdminSite.get_app_list = get_app_list