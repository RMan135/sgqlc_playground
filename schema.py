import sgqlc.types


schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

class CacheControlScope(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('PUBLIC', 'PRIVATE')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String

class Upload(sgqlc.types.Scalar):
    __schema__ = schema



########################################################################
# Input Objects
########################################################################
class FilterCharacter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'status', 'species', 'type', 'gender')
    name = sgqlc.types.Field(String, graphql_name='name')
    status = sgqlc.types.Field(String, graphql_name='status')
    species = sgqlc.types.Field(String, graphql_name='species')
    type = sgqlc.types.Field(String, graphql_name='type')
    gender = sgqlc.types.Field(String, graphql_name='gender')


class FilterEpisode(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'episode')
    name = sgqlc.types.Field(String, graphql_name='name')
    episode = sgqlc.types.Field(String, graphql_name='episode')


class FilterLocation(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('name', 'type', 'dimension')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')
    dimension = sgqlc.types.Field(String, graphql_name='dimension')



########################################################################
# Output Objects and Interfaces
########################################################################
class Character(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'image', 'episode', 'created')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    status = sgqlc.types.Field(String, graphql_name='status')
    species = sgqlc.types.Field(String, graphql_name='species')
    type = sgqlc.types.Field(String, graphql_name='type')
    gender = sgqlc.types.Field(String, graphql_name='gender')
    origin = sgqlc.types.Field('Location', graphql_name='origin')
    location = sgqlc.types.Field('Location', graphql_name='location')
    image = sgqlc.types.Field(String, graphql_name='image')
    episode = sgqlc.types.Field(sgqlc.types.list_of('Episode'), graphql_name='episode')
    created = sgqlc.types.Field(String, graphql_name='created')


class Characters(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('info', 'results')
    info = sgqlc.types.Field('Info', graphql_name='info')
    results = sgqlc.types.Field(sgqlc.types.list_of(Character), graphql_name='results')


class Episode(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'air_date', 'episode', 'characters', 'created')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    air_date = sgqlc.types.Field(String, graphql_name='air_date')
    episode = sgqlc.types.Field(String, graphql_name='episode')
    characters = sgqlc.types.Field(sgqlc.types.list_of(Character), graphql_name='characters')
    created = sgqlc.types.Field(String, graphql_name='created')


class Episodes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('info', 'results')
    info = sgqlc.types.Field('Info', graphql_name='info')
    results = sgqlc.types.Field(sgqlc.types.list_of(Episode), graphql_name='results')


class Info(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('count', 'pages', 'next', 'prev')
    count = sgqlc.types.Field(Int, graphql_name='count')
    pages = sgqlc.types.Field(Int, graphql_name='pages')
    next = sgqlc.types.Field(Int, graphql_name='next')
    prev = sgqlc.types.Field(Int, graphql_name='prev')


class Location(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'type', 'dimension', 'residents', 'created')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')
    dimension = sgqlc.types.Field(String, graphql_name='dimension')
    residents = sgqlc.types.Field(sgqlc.types.list_of(Character), graphql_name='residents')
    created = sgqlc.types.Field(String, graphql_name='created')


class Locations(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('info', 'results')
    info = sgqlc.types.Field(Info, graphql_name='info')
    results = sgqlc.types.Field(sgqlc.types.list_of(Location), graphql_name='results')


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('character', 'characters', 'characters_by_ids', 'location', 'locations', 'locations_by_ids', 'episode', 'episodes', 'episodes_by_ids')
    character = sgqlc.types.Field(Character, graphql_name='character', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    characters = sgqlc.types.Field(Characters, graphql_name='characters', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(FilterCharacter, graphql_name='filter', default=None)),
))
    )
    characters_by_ids = sgqlc.types.Field(sgqlc.types.list_of(Character), graphql_name='charactersByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    location = sgqlc.types.Field(Location, graphql_name='location', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    locations = sgqlc.types.Field(Locations, graphql_name='locations', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(FilterLocation, graphql_name='filter', default=None)),
))
    )
    locations_by_ids = sgqlc.types.Field(sgqlc.types.list_of(Location), graphql_name='locationsByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    episode = sgqlc.types.Field(Episode, graphql_name='episode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    episodes = sgqlc.types.Field(Episodes, graphql_name='episodes', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(Int, graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(FilterEpisode, graphql_name='filter', default=None)),
))
    )
    episodes_by_ids = sgqlc.types.Field(sgqlc.types.list_of(Episode), graphql_name='episodesByIds', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = None
schema.subscription_type = None

