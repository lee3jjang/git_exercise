from db.schema import schema
from graphene_django.utils.testing import GraphQLTestCase


class ReporterTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_reporters(self):
        response = self.query(
            """
            query Reporters {
                reporters {
                    fullName
                }
            }
            """
        )

        self.assertResponseNoErrors(response)
