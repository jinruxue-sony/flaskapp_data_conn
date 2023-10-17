import redshift_connector
import pandas as pd 

class Schema:
    def __init__(self):
        self.conn = redshift_connector.connect(
        host='ethics-ehcid.crghso7btmpa.us-east-1.redshift.amazonaws.com',
        database='ethics_ehcid',
        port=5439,
        user='jinru_xue',
        password=''
        )

        self.cursor=self.conn.cursor()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS fhibe.todo_test (
          Title VARCHAR,
          Description character varying,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER 
        );
        """
        self.cursor.execute(query)
    def create_user_table(self):
        # create user table in similar fashion
        # come on give it a try it's okay if you make mistakes
        pass

class ToDoModel:
    TABLENAME = "fhibe.todo_test"

    def __init__(self):
        self.conn = redshift_connector.connect(
        host='ethics-ehcid.crghso7btmpa.us-east-1.redshift.amazonaws.com',
        database='ethics_ehcid',
        port=5439,
        user='jinru_xue',
        password=''
        )
        self.conn.rollback()
        self.conn.autocommit = True
        self.cursor=self.conn.cursor()
        
    def create(self, text, description, due_date, user_id):
        self.conn.rollback()
        self.conn.autocommit = True
        query = f"""insert into fhibe.todo_test(Title, Description, _is_done, _is_deleted, duedate, userid) values ('{text}', '{description}', False, False, '{due_date}', '{user_id}');"""
        
        self.cursor.execute(query)
        # return result 
        # uncomment above line and check what error occurs and why
        return 'Success'
   # Similarly add functions to select, delete and update todo
    def read_table(self):
        self.cursor.execute(f"""select * from {self.TABLENAME}""")
        result: pd.DataFrame = self.cursor.fetch_dataframe()
        return result
    
    def update_table(self, vendor, df):
        images_ls = tuple(df['images'])
        images_ls = str(images_ls)
        update_query = f"""UPDATE fhibe_qa.large_human_splits_expanded_{vendor} SET is_submitted = True
        WHERE images in {images_ls}"""
        self.cursor.execute(update_query)

        return 'Success'