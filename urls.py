from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
def i18n_javascript(request):
  return admin.site.i18n_javascript(request)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from geekdom.manager.views import *

from geekdom.manager.forms import HackedProfileForm
from userena.views import profile_edit

handler403 = 'manager.views.error_403handler'
handler404 = 'manager.views.error_404handler'
handler500 = 'manager.views.error_500handler'

admin.autodiscover()

urlpatterns = patterns('',

    (r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
    
    # homepage
    url(r'^$', homepage, {'kiosk':False}),

    url(r'^accounts/', include('userena.urls')),

    url(r'^accounts/(?P<username>[\.\w]+)/edit/$',
       profile_edit,
       {'edit_profile_form' : HackedProfileForm}),

    # member views
    url(r'^members/$', homepage),
    url(r'^check_me_in/$', user_checkin),
    url(r'^check_me_out/$', user_checkout),
    url(r'^logout/$', logout_user),

    url(r'^search/$', search),

    # event views
    url(r'^events/$', all_events),
    url(r'^events/new$', new_event),
    url(r'^events/(?P<event_id>[\d]+)/$', view_event),


    # kiosk views
    url(r'^kiosk/$', homepage, {'kiosk':True,}),
    url(r'^kiosk/(?P<user_id>[\d]+)/$', kiosk_user_view),
    url(r'^kiosk/events/$', all_events, {'kiosk':True,}),
    url(r'^kiosk/search/$', search, {'kiosk':True}),
    
    # flomio callback views
    url(r'^flomio-checkin/$', flomio_toggle_check_in),    




    ###############
    # admin views #
    ###############

    url(r'^leaderboards/$', all_leaderboards),
    url(r'^leaderboards/checkins$', checkin_leaderboard),




    ###############
    # admin views #
    ###############

    url(r'^manager/$', all_members),
    url(r'^manager/members/$', all_members),
    url(r'^manager/members/(?P<user_id>[\d]+)/$', view_member),
    url(r'^manager/members/(?P<user_id>[\d]+)/edit/$', edit_member),
    url(r'^manager/members/new$', new_member),

    url(r'^manager/members/email_list/$', member_email_list),
    url(r'^manager/members/email_list/(?P<mt_id>[\d]+)/$', member_email_list),
    url(r'^manager/members/by_room/$', members_by_room),
    url(r'^manager/members/general_stats/$', general_member_stats),

    url(r'^manager/reports/skills$', tabular_member_report),
    url(r'^manager/reports/membertypes$', tabular_member_report_member_types),

    



    ######################
    # django admin views #
    ######################

    url(r'^admin/jsi18n', i18n_javascript),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    # makes sure that if a flatpage exists, you're able to grab it
    (r'^', include('django.contrib.flatpages.urls')),


)
