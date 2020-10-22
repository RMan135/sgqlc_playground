import json
from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint
from schema import Query

endpoint = HTTPEndpoint(url='https://rickandmortyapi.com/graphql/')

query = Operation(Query)


query.characters(page=2)

# query.character(id="1")



result = endpoint(query=query)

print(json.dumps(result, indent=2))

#print(query)


data = query + result

# print(f'{data.character.name} is a {data.character.species}.')

for c in data.characters.results:
    print(f'{c.name} is a {c.species}.')