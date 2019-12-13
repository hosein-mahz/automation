# from patient.viewses  import viewspatient as views_viewspatient
# from patient.viewses  import viewsContact as views_viewsContact
# from patient.viewses  import viewsRecord as views_viewsRecord
# from patient.viewses  import viewsRefrence as views_viewsRefrence

from django.contrib                import admin
from django.urls                   import include, path
from rest_framework                import routers
from patient.viewses.viewsRefrence  import RefrenceViewSet
from patient.viewses.viewspatient   import patientViewSet
from patient.viewses.viewsRecord    import RecordViewSet
from patient.viewses.viewsContact   import ContactViewSet

from physicing.views                import physicingViewSet

from clinical.viewses.viewsClinical_record import Clinical_recordViewSet
from clinical.viewses.viewsmedecine_order import medecine_orderViewSet
from clinical.viewses.viewstreatment_order import treatment_orderViewSet

from ParaClininical.viewses.viewsOperation_record import Operation_recordViewSet


router = routers.DefaultRouter()
router.register(r'refrence', RefrenceViewSet)
router.register(r'patient', patientViewSet)
router.register(r'record', RecordViewSet)
router.register(r'contact', ContactViewSet)

router.register(r'physicing', physicingViewSet)

router.register(r'Clinical_Record',Clinical_recordViewSet )
router.register(r'Medecine_Order',medecine_orderViewSet   )
router.register(r'Treatment_Order',treatment_orderViewSet )

router.register(r'Operation_record',Operation_recordViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
    # url(r'^api-auth/', include('rest_framework.urls'))

    # # 
    # # 
    # #  views_viewspatient
    # # 
    # # 

    # path('patient'                  , views_viewspatient.getAll)    ,
    # path('patient/get/<int:__id>'   , views_viewspatient.getSingle) ,
    # path('patient/create/'          , views_viewspatient.create)    ,
    # path('patient/delete/<int:_id>' , views_viewspatient.delete)    ,
    # path('patient/update/<int:_id>' , views_viewspatient.update)    ,

    # # 
    # # 
    # #   views_viewsContact  
    # # 
    # # 

    # path('Contact'                  , views_viewsContact.getAll)    ,
    # path('Contact/get/<int:__id>'   , views_viewsContact.getSingle) ,
    # path('Contact/create/'          , views_viewsContact.create)    ,
    # path('Contact/delete/<int:_id>' , views_viewsContact.delete)    ,
    # path('Contact/update/<int:_id>' , views_viewsContact.update)    ,

    # # 
    # # 
    # #   views_viewsRecord  
    # # 
    # # 

    # path('Record'                  , views_viewsRecord.getAll)    ,
    # path('Record/get/<int:__id>'   , views_viewsRecord.getSingle) ,
    # path('Record/create/'          , views_viewsRecord.create)    ,
    # path('Record/delete/<int:_id>' , views_viewsRecord.delete)    ,
    # path('Record/update/<int:_id>' , views_viewsRecord.update)    ,


    # # 
    # # 
    # #   views_viewsRefrence  
    # # 
    # # 

    # path('Refrence'                  , views_viewsRefrence.getAll)    ,
    # path('Refrence/get/<int:__id>'   , views_viewsRefrence.getSingle) ,
    # path('Refrence/create/'          , views_viewsRefrence.create)    ,
    # path('Refrence/delete/<int:_id>' , views_viewsRefrence.delete)    ,
    # path('Refrence/update/<int:_id>' , views_viewsRefrence.update)    ,


]
