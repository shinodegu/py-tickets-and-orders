from django.db.models import QuerySet
from db.models import Order, Ticket, User
from django.db import transaction
from datetime import datetime


def create_order(
        tickets: list[dict],
        username: str,
        date: datetime = None) -> None:
    with transaction.atomic():
        user = User.objects.get(username=username)

        order_data = {"user": user}
        if date:
            order_data["created_at"] = date
        order = Order.objects.create(**order_data)

        ticket_objects = [
            Ticket(
                row=ticket["row"],
                seat=ticket["seat"],
                movie_session_id=ticket["movie_session"],
                order=order,
            )
            for ticket in tickets
        ]
        Ticket.objects.bulk_create(ticket_objects)


def get_orders(username: str = None) -> QuerySet:
    if username:
        return Order.objects.filter(user__username=username)
    else:
        return Order.objects.all()
