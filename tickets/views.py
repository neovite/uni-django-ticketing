import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import *
from users.models import User


""" For customer """


@login_required
def customer_actions(request):
    return render(request, "ticket/ticket_actions.html")


@login_required
def ticket_details(request, ID):
    ticket = Ticket.objects.get(ticket_number=ID)
    t = User.objects.get(username=ticket.created_by)
    tickets_per_user = t.created_by.all()
    context = {
        "ticket": ticket,
        "tickets_per_user": tickets_per_user,
    }
    return render(request, "ticket/ticket_details.html", context)


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = "Pending"
            var.save()
            messages.success(
                request,
                "your ticket has been successfully submitted. an engineer would be assigned soon.",
            )
            return redirect("dashboard")
        else:
            messages.warning(request, "something went wrong please try again.")
            return redirect("create-ticket")

    else:
        form = CreateTicketForm()
        context = {"form": form}
        return render(request, "ticket/create_ticket.html", context)


@login_required
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if ticket.ticket_status == "Pending":
        if request.method == "POST":
            form = UpdateTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                messages.info(request, "your ticket has been successfully updated.")
                return redirect("dashboard")
            else:
                messages.warning(request, "something went wrong please try again.")
        else:
            form = UpdateTicketForm(instance=ticket)
            context = {"form": form}
            return render(request, "ticket/update_ticket.html", context)
    else:
        messages.warning(request, "Ticket cannot be updated in this status.")
        return redirect("all-tickets")


@login_required
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        if ticket.ticket_status == "Pending":
            ticket.delete()
            messages.success(request, "Ticket successfully deleted.")
        else:
            messages.error(request, "Cannot delete ticket: status is not pending.")
            return redirect("ticket-list")
    else:
        return render(request, "confirm_delete_ticket.html", {"ticket": ticket})


@login_required
def all_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by("-date_created")
    context = {"tickets": tickets}
    return render(request, "ticket/all_tickets.html", context)


"""" For engineer """


@login_required
def engineer_actions(request):
    return render(request, "ticket/engineer_ticket_actions.html")


@login_required
def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status="Pending")
    context = {"tickets": tickets}
    return render(request, "ticket/ticket_queue.html", context)


@login_required
def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if ticket.ticket_status == "Pending":
        ticket.assigned_to = request.user
        ticket.ticket_status = "Active"
        ticket.accepted_date = datetime.datetime.now()
        ticket.save()
        messages.success(
            request, "ticket has been accepted, please resolve as soon as possible."
        )
        return redirect("workspace")
    else:
        messages.warning(
            request, "ticket status is not pending and can not be accepted."
        )
        return redirect("ticket-queue")


@login_required
def close_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = "Completed"
    ticket.is_resolved = True
    ticket.closed_date = datetime.datetime.now()
    ticket.save()
    messages.success(request, "ticket has been successfully resolved.")
    return redirect("closed-tickets")


@login_required
def workspace(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved=False)
    context = {"tickets": tickets}
    return render(request, "ticket/workspace.html", context)


@login_required
def closed_tickets(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved=True)
    context = {"tickets": tickets}
    return render(request, "ticket/closed_tickets.html", context)
