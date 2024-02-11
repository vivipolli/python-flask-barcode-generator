from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import CreateTagController

class TagCreatorView:
    '''
      responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        create_tag_controller = CreateTagController()

        body = http_request.body
        product_code = body["product_code"]

        formatted_response = create_tag_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
