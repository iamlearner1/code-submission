from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor
    language = models.CharField(max_length=5, choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali')])

    def get_translation(self, lang):
        """Retrieve cached translation or generate if missing"""
        cache_key = f"faq_{self.id}_lang_{lang}"
        translation = cache.get(cache_key)
        
        if not translation:
            translator = Translator()
            translation = translator.translate(self.question, src='en', dest=lang).text
            cache.set(cache_key, translation, timeout=86400)  # Cache for 1 day
        
        return translation

    def __str__(self):
        return self.question
