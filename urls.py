from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
def i18n_javascript(request):
  return admin.site.i18n_javascript(request)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from geekdom.manager.views import *

handler403 = 'manager.views.error_403handler'
handler404 = 'manager.views.error_404handler'
handler500 = 'manager.views.error_500handler'

admin.autodiscover()

urlpatterns = patterns('',

    (r'^accounts/', include('userena.urls')),

    # homepage
    url(r'^$', homepage, {'kiosk':False}),

    # member views
    url(r'^members/$', homepage, {'kiosk':False}),
    url(r'^check_me_in/$', user_checkin),
    url(r'^check_me_out/$', user_checkout),
    url(r'^logout/$', logout_user),

    url(r'^search/$', search, {'kiosk':False}),
    url(r'^kiosk/search/$', search, {'kiosk':True}),

    # event views
    url(r'^events/$', all_events, {'kiosk':False,}),
    url(r'^events/(?P<event_id>[\d]+)/$', view_event),


    # kiosk views
    url(r'^kiosk1/$', homepage, {'kiosk':True,}),
    url(r'^kiosk2/$', all_events, {'kiosk':True,}),


    ###############
    # admin views #
    ###############

    url(r'^manager/$', all_members),
    url(r'^manager/members/$', all_members),
    url(r'^manager/members/(?P<user_id>[\d]+)/$', view_member),
    url(r'^manager/members/(?P<user_id>[\d]+)/edit/$', edit_member),
    url(r'^manager/members/new$', new_member),

    url(r'^manager/members/incomplete/$', members_with_incomplete_profiles),
    url(r'^manager/members/missing_stuff/$', members_who_are_missing_stuff),
    url(r'^manager/members/office_num/$', members_missing_office_num),
    url(r'^manager/members/email_list/$', member_email_list),
    url(r'^manager/members/email_list/(?P<mt_id>[\d]+)/$', member_email_list),
    url(r'^manager/members/by_room/$', members_by_room),
    url(r'^manager/members/general_stats/$', general_member_stats),


    ######################
    # django admin views #
    ######################

    url(r'^admin/jsi18n', i18n_javascript),
    url(r'^admin/', include(admin.site.urls)),

    # added for django-admin-tools
    url(r'^admin_tools/', include('admin_tools.urls')),



)
