import graphene
from graphene_django.types import DjangoObjectType

from .models import Reporter, Article


class ReporterType(DjangoObjectType):
    class Meta:
        model = Reporter


class Query(graphene.ObjectType):
    reporter = graphene.Field(ReporterType, id=graphene.String())
    reporters = graphene.List(ReporterType)

    def resolve_reporter(self, info, **kwargs):
        id = kwargs.get("id")
        return Reporter.objects.filter(id=id).first()

    def resolve_reporters(self, info, **kwargs):
        return Reporter.objects.all()


schema = graphene.Schema(query=Query)
