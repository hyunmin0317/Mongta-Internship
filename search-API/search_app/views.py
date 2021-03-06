from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elasticsearch import Elasticsearch


class SearchView(APIView):

    def get(self, request):
        es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

        # 검색어
        search_word = request.GET.get('search')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})

        docs = es.search(
            index='dictionary',
            body={
                "query": {
                    "multi_match": {
                        "query": search_word,
                        "fields": [
                            "Restaurant",
                            "Review"
                        ]
                    }
                }
            })

        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response(data_list)