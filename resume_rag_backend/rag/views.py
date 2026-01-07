# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ResumeSerializer
from .agent import agent
from langchain.messages import HumanMessage, AIMessage

class ResumeView(APIView):
    """
    API endpoint to process user input and get a response from the AI agent.
    """

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            user_input = serializer.validated_data.get("input")
            print(user_input)

            try:
                # Call the agent with a HumanMessage
                ai_response = agent().invoke({"input":user_input})
                
                # ai_response is usually a string; return it directly
                return Response({"answer": ai_response["messages"].content}, status=status.HTTP_200_OK)

            except Exception as e:
                # Catch any errors from the agent
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        # Return validation errors if serializer is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
