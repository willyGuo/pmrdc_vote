from django.contrib import admin
from myapp.models import student, requisition,clereply_db, NewsUnit, Vote, AddressInfo,Type,Type2, worktype, Category, Category2, Category3
from myapp.views import vote
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter =('cName', 'cSex')
    search_fields = ('cName',)
    ordering =('id',)

class requisitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName','cNumber', 'cdatestart','cFunction','cdateend','cProjectname', 'cCusetername', 'cProjectcode',\
         'cLocation', 'cContent', 'cSchedule','cSpecial',\
        'cLastproject', 'cType', 'cCotpye','cProjecttype', 'cStage', 'cNoted', 'title', 'uploadedFile', 'dateTimeOfUpload', 'cStatus')
    list_filter =('cName', )
    search_fields = ('cName',)
    ordering =('id',)
class clereply_dbAdmin(admin.ModelAdmin):
    list_display = ('product', 'checklist', 'producttype', 'productscoreline')
    list_filter =('product', 'checklist')
    search_fields = ('product',)
    ordering =('id',)

class NewsUnit_dbAdmin(admin.ModelAdmin):
    list_display = ('catego', 'nickname', 'title', 'message', 'pubtime', 'enabled', 'press')
    list_filter =('catego', 'nickname')
    search_fields = ('catego',)
    ordering =('id',)

class cVote_dbAdmin(admin.ModelAdmin):
    list_display = ('id',"cName","cVotenumber", "cVotetime", "cVoteselect")
    list_filter = ("cName","cVoteselect")
    search_fields = ("cName",)
    ordering = ("cName",)

class AddressInfo_dbAdmin(admin.ModelAdmin):
    list_display = ('id','address')
    search_fields = ('address',)
    ordering = ("id",)

class Type_dbAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    ordering = ("id",)

class Type2_dbAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    ordering = ("id",)

class worktype_dbAdmin(admin.ModelAdmin):
    list_display = ('id', 'Worktype_number', 'Worktype_name')
    search_fields = ('Worktype_number',)
    ordering = ("id",)

class Category_dbAdmin(admin.ModelAdmin):
    list_display = ('id', 'Catid', 'Bigcate', 'Category_name')
    search_fields = ('Catid',)
    ordering = ("id",)    

class Category2_dbAdmin(admin.ModelAdmin):
    list_display = ('id', 'Catid', 'Bigcate', 'Category_name')
    search_fields = ('Catid',)
    ordering = ("id",)    

class Category3_dbAdmin(admin.ModelAdmin):
    list_display = ('id', 'Catid', 'Bigcate', 'Category_name')
    search_fields = ('Catid',)
    ordering = ("id",)    


admin.site.register(student,studentAdmin)
admin.site.register(requisition,requisitionAdmin)
admin.site.register(clereply_db,clereply_dbAdmin)
admin.site.register(NewsUnit,NewsUnit_dbAdmin)
admin.site.register(Vote, cVote_dbAdmin)
admin.site.register(AddressInfo, AddressInfo_dbAdmin)
admin.site.register(Type, Type_dbAdmin)
admin.site.register(Type2, Type2_dbAdmin)
admin.site.register(worktype, worktype_dbAdmin)
admin.site.register(Category, Category_dbAdmin)
admin.site.register(Category2, Category2_dbAdmin)
admin.site.register(Category3, Category3_dbAdmin)





