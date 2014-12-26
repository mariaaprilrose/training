from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #Places the fields in separate boxes for field management
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    inlines = [ChoiceInline]
    #shows the following info, and tells the order of fields for a poll row
    list_display = ('question', 'pub_date', 'was_published_recently') 
    #sidebar for filter
    list_filter = ['pub_date'] 
    #search bar for fields
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)

