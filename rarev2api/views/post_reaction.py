import sqlite3
import json
from models import (
  Post_Reaction,
  Reaction
)

def get_all_post_reactions():
    with sqlite3.connect("./db.sqlite3") as conn:
      
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      
      db_cursor.execute("""
      SELECT
          pr.id,
          pr.user_id,
          pr.reaction_id,
          pr.post_id,
          r.id,
          r.label,
          r.image_url
      FROM PostReactions pr
      JOIN Reactions r
          on r.id = pr.reaction_id
      """)
      
      post_reactions = []
      
      dataset = db_cursor.fetchall()
      
      for row in dataset:
          post_reaction = Post_Reaction( row['id'], row['user_id'], row ['reaction_id'], row['post_id'] )
          
          reaction = Reaction( row['id'], row['label'], row['image_url'] )
          
          post_reaction.reaction = reaction.__dict__
          post_reactions.append(post_reaction.__dict__)
          
      return json.dumps(post_reactions)
    
def get_single_post_reaction(id):
  with sqlite3.connect("./db.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        p.id,
        p.user_id,
        p.reaction_id,
        p.post_id
    FROM PostReactions p
    WHERE p.id = ?
    """, ( id, ))
    
    data = db_cursor.fetchone()
    
    post_reaction = Post_Reaction( data['id'], data['user_id'], data['reaction_id'], data['post_id'] )
    
    return json.dumps(post_reaction.__dict__)
  
def create_post_reaction(new_post_reaction):
  
  with sqlite3.connect("./db.sqlite3") as conn:
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    INSERT INTO PostReactions
        ( id, user_id, reaction_id, post_id )
    VALUES ( ?, ?, ?, ? );
    """, new_post_reaction['id'], new_post_reaction['user_id'], new_post_reaction['reaction_id'], new_post_reaction['post_id'] )
    
    id = db_cursor.lastrowid
    
    new_post_reaction['id'] = id
  
  return json.dumps(new_post_reaction)

def delete_post_reaction(id):
  
  with sqlite3.connect("./db.sqlite3") as conn:
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    DELETE FROM PostReactions
    WHERE id = ?
    """, ( id, ))

def update_post_reaction(id, new_post_reaction):
  
  with sqlite3.connect("./db.sqlite3") as conn:
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    UPDATE PostReactions
    SET
        id = ?,
        user_id = ?,
        reaction_id = ?,
        post_id = ?
    WHERE id = ?
    """, ( new_post_reaction['id'], new_post_reaction['user_id'], new_post_reaction['reaction_id'], new_post_reaction['post_id'], id, ))
    
    rows_affected = db_cursor.rowcount
    
    if rows_affected == 0:
        return False
    else:
        return True
      
def get_reactions_by_post(post_id):
  
  with sqlite3.connect("./db.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT * FROM PostReactions pr
    JOIN Posts p on pr.post_id = p.id
    WHERE pr.post_id = (?)
    """, (post_id, ))
    
    post_reactions = []
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      post_reaction = Post_Reaction( row['id'], row['user_id'], row['reaction_id'], row['post_id'])
      post_reactions.append(post_reaction.__dict__)
      
      return json.dumps(post_reactions)
