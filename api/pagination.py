from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# The page number pagination class includes the no of attributes that may be overwrriden to modify the pagination style
class CustomPagination(PageNumberPagination):
    # These are all the attributes u can modify in ur custom pagination
    page_size_query_param = 'page_size'
    page_query_param = 'page-num' # here only we can pass employees as well
    max_page_size = 1

    def get_paginated_response(self, data):
            return Response({
                  'next': self.get_next_link(),
                  'previous': self.get_previous_link(),
                  'count': self.page.paginator.count,
                  'page_size': self.page_size,
                  'results': data
            })
    
