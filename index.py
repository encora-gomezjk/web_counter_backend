from ariadne.asgi import GraphQL
from ariadne import make_executable_schema
from starlette.middleware.cors import CORSMiddleware


from api.type_definitions import type_defs
from api.queries import query

schema = make_executable_schema(type_defs, query)

app = CORSMiddleware(GraphQL(schema), allow_origins=['*'], allow_methods=("GET", "POST", "OPTIONS"))
