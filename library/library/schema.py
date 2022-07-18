from graphene import Schema, ObjectType
import catalog.schema


class Query(catalog.schema.Query, ObjectType):
    pass


class Mutation(ObjectType):
    pass


schema  = Schema(query= Query)