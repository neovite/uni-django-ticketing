from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date_created",
        "ticket_status",
        "created_by",
        "assigned_to",
        "is_resolved",
    )


admin.site.register(Ticket, TicketAdmin)
