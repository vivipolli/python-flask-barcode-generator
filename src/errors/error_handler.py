from src.views.http_types.http_response import HttpResponse
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "error": [{
                    "title": error.name,
                    "detal": error.message
                }]
            }
        )

    return HttpResponse(
      status_code=500,
      body={
        "error": [{
            "title": "Server error",
            "detail": str(error)
          }]
      }
    )
