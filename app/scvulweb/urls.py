from django.urls import path
from scvulweb.tool_type.views import Tool_Type, add_Tool_Type, edit_Tool_Type
from scvulweb.appweb.views import Site, add_Site, edit_Site, delete_Site
from scvulweb.test_site.views import Test_Site, add_test_site, all_Test
from scvulweb.tests.views import detail_Test, add_Test, delete_Test, edit_Test

from scvulweb.report_tool.views import report_tool_test_add

urlpatterns = [
    # site
    path('listar_appwebs/', Site, name='site_list'),
    path('registrar_appweb/', add_Site, name='site_add'),
    path('editar_appweb/<int:id_site>', edit_Site, name='site_edit'),
    path('eliminar_appweb/<int:id_site>', delete_Site, name='site_delete'),


    # tool_type
    path('listar_herramientas/', Tool_Type, name='tool_type_list'),
    path('registrar_herramienta/', add_Tool_Type, name='add_Tool_Type'),
    path('editar_herramienta/<int:id>/', edit_Tool_Type, name='edit_Tool_Type'),

    # test_site
    path('listar_pruebas_appweb/', Test_Site, name='test_site_list'),
    path('registrar_pruebas_sitio/', add_test_site, name='add_test_site'),
    path('todas_pruebas_sitio/<int:id_test_s>', all_Test, name='all_test_site'),

    
    # test
    path('detalle_prueba/<int:id_test>', detail_Test, name='detail_test'),
    path('todas_pruebas_sitio/<int:id_test_s>/registrar_prueba', add_Test, name='add_test'),
    path('todas_pruebas_sitio/<int:id_test_s>/eliminar_prueba/<int:id_test>', delete_Test, name='delete_test'),
    path('todas_pruebas_sitio/<int:id_test_s>/editar_prueba/<int:id_test>', edit_Test, name='edit_test'),

    #report_tool
    path('registrar_reporte_herramientas/<int:id_test>', report_tool_test_add, name='report_tool_test_add'),


]


