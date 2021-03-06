print 'in url 3'
from django.conf.urls import patterns, url
from drivingtest import views
from django.conf import settings
from django.contrib import admin

# UNDERNEATH your urlpatterns definition, add the following two lines:
admin.autodiscover()
urlpatterns = patterns('',
        url(r'^omckv$', views.omckv2, name='index'),
         url(r'^$', views.omckv2, name='index'),
        #url(r'^ul$', views.index, name='index'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^add_owncontact/$', views.add_owncontact, name='add_owncontact'),
        url(r'^add_file/$', views.add_file, name='add_file'),
        url(r'^upload_file/$', views.upload_file, name='upload_file'),
        url(r'^search_product/$', views.search_product, name='search_product'),
        url(r'^auto/$', views.auto_create_owncontact, name='auto_create_owncontact'),
        
        #################OMCKV2####################
        url(r'^omckv2/tram_table/$',  views.tram_table, name='tram_table'),
        
        
        url(r'^omckv2/edit_site/$',  views.edit_site, name='tram_table'),
        url(r'^omckv2/ntpform/$',  views.ntpform, name='tram_table'),
        
        url(r'^omckv2/suggestion/$', views.suggestion, name='suggestion'),
        
        url(r'^omckv2/lenh-suggestion/$', views.lenh_suggestion, name='suggestion'),
        url(r'^omckv2/upload_excel_file/$', views.upload_excel_file, name='upload_file'),
        url(r'^omckv2/mll_table/$', views.mll_table, name='suggestion'),
        url(r'^omckv2/search_history/$', views.search_history, name='suggestion'),
        url(r'^omckv2/edit_history_search/$', views.edit_history_search, name='suggestion'),
        url(r'^omckv2/edit_command/$',views.edit_command, name='edit_command_entry'),
        url(r'^omckv2/show_excel/$',views.show_excel, name='edit_command_entry'),
        #url(r'^omckv2/get_csv/$',views.get_csv, name='edit_command_entry'),
        url(r'^omckv2/config_ca_filter_mll_table/$',  views.config_ca_filter_mll_table, name='add_command'),
        url(r'^omckv2/load_empty_mll_form/$',  views.load_empty_mll_form, name='add_command'),
        
        url(r'^omckv2/qldt/$',  views.quan_ly_doi_tac, name='add_command'),
        url(r'^omckv2/testcontext/$',  views.testcontext, name='add_command'),
        url(r'^omckv2/doitac_table_sort/$',  views.doitac_table_sort, name='add_command'),
        url(r'^omckv2/edit_doi_tac_table_save/$',  views.edit_doi_tac_table_save, name='add_command'),
        url(r'^omckv2/add_command/$',  views.add_command, name='add_command'),
        url(r'^omckv2/handlemodal/(?P<form_name>\w+)/(?P<entry_id>\w+)/$', views.handlemodal, name='suggestion'),
        url(r'^omckv2/handelCommentForMLLForm/(?P<entry_id>\w+)/',  views.handelCommentForMLLForm, name='add_command'),
        #url(r'^show_detail_tram/$', views.show_detail_tram, name='show_detail_tram'),
        url(r'^omckv2/detail_tram_compact_with_search_table/$', views.detail_tram_compact_with_search_table, name='show_detail_tram'),
        url(r'^omckv2/$',  views.omckv2, name='omckv2'),
        url(r'^omckv2/luu_mll_form/$',  views.luu_mll_form, name='omckv2'),
        url(r'^omckv2/mll_form/$',  views.mll_form, name='omckv2'),
        url(r'^omckv2/download-script/$',  views.download_script, name='omckv2'),
        url(r'^omckv2/mll_filter/$',  views.mll_filter, name='omckv2'),
        
        url(r'^omckv2/lenh_table/$',  views.lenh_table, name='tram_table'),
        url(r'^omckv2/delete_mll/$',  views.delete_mll, name='tram_table'),
        url(r'^omckv2/autocomplete/$',  views.autocomplete, name='tram_table'),
        url(r'^omckv2/config_ca/$',  views.config_ca, name='tram_table'),
        url(r'^omckv2/load_form_config_ca/$',  views.load_form_config_ca, name='tram_table'),
        url(r'^omckv2/download_script_ntp/$',  views.download_script_ntp, name='tram_table'),
        url(r'^omckv2/get_contact_form/$',  views.get_contact_form, name='tram_table'),
        
        
        url(r'^omckv2/registers/$', views.register, name='register'), # ADD NEW PATTERN! 
        
        
        
        
        
        
        
        
        
        #url(r'^omckv2/trangthai/$',views.QuanLyTrangThai.as_view(),name='abc'),
        url(r'^select_forum/$',  views.select_forum, name='select_forum'),
        url(r'^get-thongbao/$',  views.get_thongbao, name='get-thongbao'),
        url(r'^init/$',  views.init, name='init'),
        url(r'^leech/$',  views.leech, name='leech'),
        url(r'^importul/$',  views.importul, name='importul'),
        url(r'^stop-post/$',  views.stop_post, name='stop-post'),
        
        
        url(r'^get_description/$',  views.get_description, name='tao-object'),
        url(r'^edit_entry/(?P<entry_id>\d+)/$',  views.edit_entry, name='edit_entry'),
        
        url(r'^delete/$', views.delete_db, name='delete_db'),
        url(r'^edit_owncontact/$', views.edit_owncontact, name='edit_OwnContact'),
        url(r'^add_linhkien/$', views.add_linhkien, name='add_linhkien'),
        
        url(r'^edit_linhkien/(?P<linhkien_encode_url>.+)/$', views.edit_linhkien, name='edit_linhkien'),
        
        url(r'^edit_category/(?P<cate_encode_url>.+)/$', views.edit_category, name='edit_category'),
        
        
        url(r'^sanpham/(?P<linhkien_encode_url>.+)/$', views.detail_linhkien, name='detail_linhkien'),

        #url(r'^detail/(?P<linhkien_id>\d+)/$', views.detail_linhkien, name='detail_linhkien'),
        #url(r'^category/(?P<cate_id>\d+)/$', views.category, name='category'),
        url(r'^category/(?P<cate_encode_url>.+)/$', views.category, name='category'),
        url(r'^login/$',views.user_login,name="user_login"),
        url(r'^logout/$',views.user_logout,name="user_logout"),
        url(r'^pagination/$',views.pagination_handle,name="pagination_handle"),
        url(r'^about/$',views.about,name="about"),
                   
        )
if settings.DEBUG:
    urlpatterns += patterns( 
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
 
    
    
    