from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Reaction

class ReactionView(ViewSet):
  
  def retrieve(self, request, pk):
    reaction = Reaction.objects.get(pk=pk)
    serializer = ReactionSerializer(reaction)
    return Response(serializer.data)
  
  def list(self, request):
    reactions = Reaction.objects.all()
    serializer = ReactionSerializer(reactions, many = True)
    return Response(serializer.data)
  
  def create(self, request):
    
    reaction = Reaction.objects.create(
      label=request.data["label"],
      image_url=request.data["image_url"]
    )
    serializer = ReactionSerializer(reaction)
    return Response(serializer.data)

# def get_all_reactions():
#     with sqlite3.connect("./db.sqlite3") as conn:
      
#       conn.row_factory = sqlite3.Row
#       db_cursor = conn.cursor()
      
#       db_cursor.execute("""
#       SELECT
#           r.id,
#           r.label,
#           r.image_url,
#       FROM Reactions r
#       """)
      
#       reactions = []
      
#       dataset = db_cursor.fetchall()
      
#       for row in dataset:
        
#           reaction = Reaction(row['id'], row['label'], row['image_url'])
          
#           reactions.append(reaction.__dict__)
          
#       return json.dumps(reactions)
    
# def get_single_reaction(id):
#   with sqlite3.connect("./db.sqlite3") as conn:
    
#     conn.row_factory = sqlite3.Row
#     db_cursor = conn.cursor()
    
#     db_cursor.execute("""
#     SELECT
#         r.id,
#         r.label,
#         r.image_url
#     FROM Reactions r
#     WHERE r.id = ?
#     """, ( id ))
    
#     data = db_cursor.fetchone()
    
#     reaction = Reaction(data['id'], data['label'], data['image_url'])
    
#     return json.dumps(reaction.__dict__)
  
# def create_reaction(new_reaction):
#   with sqlite3.connect("./db.sqlite3") as conn:
#     db_cursor = conn.cursor()
    
#     db_cursor.execute("""
#     INSERT INTO Reactions
#         ( id, label, image_url )
#     VALUES ( ?, ?, ? );
#     """, ( new_reaction['id'], new_reaction['label'], new_reaction['image_url'] ))
    
#     id = db_cursor.lastrowid
    
#     new_reaction['id'] = id
    
#     return json.dumps(new_reaction)
  
# def delete_reaction(id):
#   with sqlite3.connect("./db.dwlite3") as conn:
#     db_cursor = conn.cursor()
    
#     db_cursor.execute("""
#     DELETE FROM Reactions
#     WHERE id = ?
#     """, ( id, ))
    
# def update_reaction(id, new_reaction):
#   with sqlite3.connect("./db.sqlite3") as conn:
#     db_cursor = conn.cursor()
    
#     db_cursor.execute("""
#     UPDATE Reactions
#     SET
#         id = ?,
#         label = ?,
#         image_url = ?
#     WHERE id = ?
#     """, ( new_reaction['id'], new_reaction['label'], new_reaction['image_url'], id,  ))
    
#     rows_affected = db_cursor.rowcount
    
#     if rows_affected == 0:
#         return False
#     else:
#         return True
