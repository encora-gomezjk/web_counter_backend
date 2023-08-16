from ariadne import gql

type_defs = gql(
   """
   scalar CountResult

   type Query {
       count_words(text: String!): CountResult
   }
   """
)
