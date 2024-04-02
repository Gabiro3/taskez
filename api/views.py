from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# -- CRUD OPERATIONS FOR TASKS -- #

@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.filter(host=request.user.id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        data = request.data.copy()
        
        # Set the host field to the current user
        data['host'] = request.user.id # Assuming request.user is the current authenticated user

        # Create a serializer instance with the modified data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the task's host matches the request user's ID
    # if task.host != request.user.id:
    #     return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 # -- END OF CRUD OPERATIONS FOR TASKS --#
   
@api_view(['GET'])
def getUser(request, email):
    try:
        user = Client.objects.get(email=email)  # Use get() instead of filter() to get a single instance
        serializer = ClientSerializer(user)
        return Response(serializer.data)
    except Client.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

# -- CRUD OPERATIIONS FOR GROUPS -- #

@api_view(['POST'])
def create_group(request):
    if request.method == 'POST':
        data = request.data.copy()
        
        # Set the admin field to the current user
        data['admin'] = request.user.id  # Assuming request.user is the current authenticated user

        # Create a serializer instance with the modified data
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_groups(request):
    groups = Group.objects.filter(participants=request.user.id)
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_group(request, pk):
    if request.user.is_anonymous:
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user != group.admin:
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_group(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the group's admin matches the request user's ID
    if group.admin != request.user:
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# --- CRUD OPERATIONS FOR INVITATIONS -- #
@api_view(['POST'])
def create_invitation(request):
    if request.method == 'POST':
        # Ensure the invitor is the current user (request.user)
        invitor_id = request.user.id
        
        # Get the invitee's ID from the request data
        invitee_id = request.data.get('invitee')
        get_user = Client.objects.filter(id=invitee_id)
        if not invitee_id:
            return Response({"error": "Invitee ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new invitation
        invitation_data = {'invitor': invitor_id, 'invitee': invitee_id}
        serializer = InvitationSerializer(data=invitation_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def view_invitations(request):
    invitations = Invitation.objects.filter(invitee=request.user.id)
    serializer = InvitationSerializer(invitations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['DELETE'])
def delete_invitation(request, pk):
    try:
        invitation = Invitation.objects.get(pk=pk)
    except Invitation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the invitor matches the request user's ID
    if invitation.invitor_id != request.user.id:
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'DELETE':
        invitation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['PUT'])
def accept_invitation(request, pk):
    try:
        invitation = Invitation.objects.get(pk=pk)
    except Invitation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the invitee matches the request user
    if invitation.invitee != request.user:
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        invitation.accepted = True
        invitation.save()
        return Response({"message": "Invitation accepted"}, status=status.HTTP_200_OK)