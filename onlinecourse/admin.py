from django.contrib import admin

# Import models
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission
)


# Choice inline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Question inline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Lesson inline
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Course admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']


# Lesson admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
