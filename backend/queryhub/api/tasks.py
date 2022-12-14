import operator
from functools import reduce
from django.db.models import Q
from datetime import date, timedelta


def TextSearch(search, obj):
    obj = obj.filter(
        Q(
            reduce(
                operator.or_,
                (Q(lineage__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.or_,
                (Q(division__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.or_,
                (Q(clade__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.or_,
                (Q(strain__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.or_,
                (Q(aadeletions__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.or_,
                (Q(nextclade_pango__icontains=x) for x in search),
            )
        )
        | Q(
            reduce(
                operator.or_,
                (Q(aasubstitutions__icontains=x) for x in search),
            )
        )
    ).distinct()
    return obj


def AdvancedFilter(
    obj,
    days,
    date,
    clade,
    strain,
    lineage,
    present,
    division,
    aadeletions,
    nextclade_pango,
    aasubstitutions,
):
    if days and present == False:
        last_date = QueryHubModel.objects.values("date").latest("date")
        day = last_date["date"] - timedelta(days=int(days))
        obj = obj.filter(date__gte=day)
    if days and present == True:
        day = datetime.date.today() - timedelta(days=int(days))
        obj = obj.filter(date__gte=day)
    if date:
        obj = obj.filter(date=date)
    if clade:
        obj = obj.filter(clade__in=clade)
    if strain:
        obj = obj.filter(strain__in=strain)
    if lineage:
        obj = obj.filter(lineage__in=lineage)
    if division:
        obj = obj.filter(division__in=division)
    if nextclade_pango:
        obj = obj.filter(nextclade_pango__in=nextclade_pango)
    if aadeletions:
        obj = obj.filter(
            reduce(
                operator.and_,
                (Q(aadeletions__icontains=x) for x in aadeletions),
            )
        )
    if aasubstitutions:
        obj = obj.filter(
            reduce(
                operator.and_,
                (Q(aasubstitutions__icontains=x) for x in aasubstitutions),
            )
        )
    return obj
