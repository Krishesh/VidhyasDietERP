from django.contrib import admin

from diet.models import BodyComposition, DietChart, LogBook, PackageSchedule, Graph, DietPlan

# Register your models here.


admin.site.register(BodyComposition)
admin.site.register(DietChart)
admin.site.register(LogBook)
admin.site.register(PackageSchedule)
admin.site.register(Graph)
admin.site.register(DietPlan)
