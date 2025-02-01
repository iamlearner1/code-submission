from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "get_hindi_question", "get_bengali_question")
    search_fields = ("question", "question_hi", "question_bn")

    def get_hindi_question(self, obj):
        return obj.question_hi or "Not Translated"
    get_hindi_question.short_description = "Hindi Question"

    def get_bengali_question(self, obj):
        return obj.question_bn or "Not Translated"
    get_bengali_question.short_description = "Bengali Question"

admin.site.register(FAQ, FAQAdmin)
