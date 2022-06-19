from nasse import Response
from nasse.models import Dynamic, Endpoint, Error, Login, Param, Return
from schemas.types import Granularity
from stats.errors import get_errors_count
from stats.timings import get_timings
from translatepy.server.server import app


base = Endpoint(
    section="Stats",
    errors=Error(name="DATABASE_DISABLED", description="When the server disabled any database interaction", code=501),
    params=Param(name="granularity", description="The granularity of the stats", type=Granularity, required=False),
    login=Login(no_login=True)
)


@app.route("/stats/timings", endpoint=Endpoint(
    endpoint=base,
    description="Get all timings",
    name="Timings Stats"
))
def timings_handler(granularity: Granularity = "hour"):
    return Response(
        data=get_timings(granularity)
    )


@app.route("/stats/errors", endpoint=Endpoint(
    endpoint=base,
    description="Get all errors count for each service",
    name="Erros Stats"
))
def timings_handler(granularity: Granularity = "hour"):
    return Response(
        data=get_errors_count(granularity)
    )
