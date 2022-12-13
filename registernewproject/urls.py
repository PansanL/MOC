from django.urls import path
from .views import insertData,allproject,home,Access_Project,insert_file_Solar,DeleteSolarFile,Approve_Solar_File,Dashboard,UpdateFileVersion,UpdateFileVersion_insert,DeleteSolarFile_Version2,DeleteSolarFile_Version3,DeleteSolarFile_Version4,DeleteSolarFile_Version5
from .views import insert_file_Test,DeleteTestFile,Approve_Test_File,UpdateFileVersion_Test,UpdateFileVersion_insert_Test,DeleteTestFile_Version2,DeleteTestFile_Version3,DeleteTestFile_Version4,DeleteTestFile_Version5,logging
from .views import insert_file_MLFAULT, DeleteMLFAULTFile ,Approve_MLFAULT_File ,UpdateFileVersion_MLFAULT ,UpdateFileVersion_insert_MLFAULT ,DeleteMLFAULTFile_Version2 ,DeleteMLFAULTFile_Version3 ,DeleteMLFAULTFile_Version4 ,DeleteMLFAULTFile_Version5
from .views import insert_file_CheckSheet_Sub1, DeleteCheckSheet_Sub1File ,Approve_CheckSheet_Sub1_File ,UpdateFileVersion_CheckSheet_Sub1 ,UpdateFileVersion_insert_CheckSheet_Sub1 ,DeleteCheckSheet_Sub1File_Version2 ,DeleteCheckSheet_Sub1File_Version3 ,DeleteCheckSheet_Sub1File_Version4 ,DeleteCheckSheet_Sub1File_Version5


urlpatterns = [
    path('insertData/',insertData,name="insertData"),
    path('allproject/',allproject,name="allproject"), 
    path('home/',home,name="home"),
    path('Dashboard/',Dashboard,name="Dashboard"),
    path('allproject/<int:id>/',Access_Project,name="Access_Project"),
    path('logging/',logging,name="logging"),
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Smart Check Sheet for Substation #1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #
    path('insert_file_Solar/',insert_file_Solar,name="insert_file_Solar"),
    path('DeleteSolarFile/<int:id>/',DeleteSolarFile,name="DeleteSolarFile"),
    path('DeleteSolarFile_Version2/<int:id>/',DeleteSolarFile_Version2,name="DeleteSolarFile_Version2"),
    path('DeleteSolarFile_Version3/<int:id>/',DeleteSolarFile_Version3,name="DeleteSolarFile_Version3"),
    path('DeleteSolarFile_Version4/<int:id>/',DeleteSolarFile_Version4,name="DeleteSolarFile_Version4"),
    path('DeleteSolarFile_Version5/<int:id>/',DeleteSolarFile_Version5,name="DeleteSolarFile_Version5"),
    path('Approve_Solar_File/<int:id>/',Approve_Solar_File,name="Approve_Solar_File"),
    path('UpdateFileVersion/<int:id>/',UpdateFileVersion,name="UpdateFileVersion"),
    path('UpdateFileVersion_insert/<int:id>/',UpdateFileVersion_insert,name="UpdateFileVersion_insert"),

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> As-build drawing P5 package  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

    path('insert_file_Test/',insert_file_Test,name="insert_file_Test"),
    path('DeleteTestFile/<int:id>/',DeleteTestFile,name="DeleteTestFile"),
    path('Approve_Test_File/<int:id>/',Approve_Test_File,name="Approve_Test_File"),
    path('UpdateFileVersion_Test/<int:id>/',UpdateFileVersion_Test,name="UpdateFileVersion_Test"),
    path('UpdateFileVersion_insert_Test/<int:id>/',UpdateFileVersion_insert_Test,name="UpdateFileVersion_insert_Test"),
    path('DeleteTestFile_Version2/<int:id>/',DeleteTestFile_Version2,name="DeleteTestFile_Version2"),
    path('DeleteTestFile_Version3/<int:id>/',DeleteTestFile_Version3,name="DeleteTestFile_Version3"),
    path('DeleteTestFile_Version4/<int:id>/',DeleteTestFile_Version4,name="DeleteTestFile_Version4"),
    path('DeleteTestFile_Version5/<int:id>/',DeleteTestFile_Version5,name="DeleteTestFile_Version5"),
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ML Fault Detection <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

    path('insert_file_MLFAULT/',insert_file_MLFAULT,name="insert_file_MLFAULT"),
    path('DeleteMLFAULTFile/<int:id>/',DeleteMLFAULTFile,name="DeleteMLFAULTFile"),
    path('Approve_MLFAULT_File/<int:id>/',Approve_MLFAULT_File,name="Approve_MLFAULT_File"),
    path('UpdateFileVersion_MLFAULT/<int:id>/',UpdateFileVersion_MLFAULT,name="UpdateFileVersion_MLFAULT"),
    path('UpdateFileVersion_insert_MLFAULT/<int:id>/',UpdateFileVersion_insert_MLFAULT,name="UpdateFileVersion_insert_MLFAULT"),
    path('DeleteMLFAULTFile_Version2/<int:id>/',DeleteMLFAULTFile_Version2,name="DeleteMLFAULTFile_Version2"),
    path('DeleteMLFAULTFile_Version3/<int:id>/',DeleteMLFAULTFile_Version3,name="DeleteMLFAULTFile_Version3"),
    path('DeleteMLFAULTFile_Version4/<int:id>/',DeleteMLFAULTFile_Version4,name="DeleteMLFAULTFile_Version4"),
    path('DeleteMLFAULTFile_Version5/<int:id>/',DeleteMLFAULTFile_Version5,name="DeleteMLFAULTFile_Version5"),

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Smart Check Sheet for Substation #1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

    path('insert_file_CheckSheet_Sub1/',insert_file_CheckSheet_Sub1,name="insert_file_CheckSheet_Sub1"),
    path('DeleteCheckSheet_Sub1File/<int:id>/',DeleteCheckSheet_Sub1File,name="DeleteCheckSheet_Sub1File"),
    path('Approve_CheckSheet_Sub1_File/<int:id>/',Approve_CheckSheet_Sub1_File,name="Approve_CheckSheet_Sub1_File"),
    path('UpdateFileVersion_CheckSheet_Sub1/<int:id>/',UpdateFileVersion_CheckSheet_Sub1,name="UpdateFileVersion_CheckSheet_Sub1"),
    path('UpdateFileVersion_insert_CheckSheet_Sub1/<int:id>/',UpdateFileVersion_insert_CheckSheet_Sub1,name="UpdateFileVersion_insert_CheckSheet_Sub1"),
    path('DeleteCheckSheet_Sub1File_Version2/<int:id>/',DeleteCheckSheet_Sub1File_Version2,name="DeleteCheckSheet_Sub1File_Version2"),
    path('DeleteCheckSheet_Sub1File_Version3/<int:id>/',DeleteCheckSheet_Sub1File_Version3,name="DeleteCheckSheet_Sub1File_Version3"),
    path('DeleteCheckSheet_Sub1File_Version4/<int:id>/',DeleteCheckSheet_Sub1File_Version4,name="DeleteCheckSheet_Sub1File_Version4"),
    path('DeleteCheckSheet_Sub1File_Version5/<int:id>/',DeleteCheckSheet_Sub1File_Version5,name="DeleteCheckSheet_Sub1File_Version5"),
    
    
]