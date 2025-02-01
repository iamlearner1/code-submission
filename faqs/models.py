from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Translations
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    answer_hi = RichTextField(blank=True, null=True)

    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Auto-translate question and answer before saving."""
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text

        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text

        super().save(*args, **kwargs)

    def get_translation(self, lang_code):
        """Retrieve the translated question and answer dynamically."""
        translations = {
            "hi": (self.question_hi, self.answer_hi),
            "bn": (self.question_bn, self.answer_bn),
        }
        return translations.get(lang_code, (self.question, self.answer))  # Default to English

    def __str__(self):
        return self.question
