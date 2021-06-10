from DB.DBConnection import DBConnection

# INTEGER PRIMARY KEY 代表id key是固定的 不可以重疊，若移除PRIMARY KEY 則可重疊多個id
necessary_table_to_create = {
    "MovieData_Table":
        """
            CREATE TABLE MovieData_Table
            (
                adult	TEXT,
                belongs_to_collection	TEXT,
                budget	INTEGER,
                genres	TEXT,
                id	INTEGER,
                imdb_id	TEXT,
                original_language	TEXT,
                original_title	TEXT,
                overview	TEXT,
                popularity	REAL,
                production_companies	TEXT,
                production_countries	TEXT,
                release_date	TEXT,
                runtime	REAL,
                spoken_languages	TEXT,
                status	TEXT,
                tagline	TEXT,
                title	TEXT,
                video	TEXT,
                vote_average	REAL,
                vote_count	REAL,
                year	INTEGER,
                cast	TEXT,
                crew	TEXT,
                keywords	TEXT
            );
        """,

    "MovieID_map_Table":
        """
            CREATE TABLE MovieID_map_Table
            (
                id	REAL,
                movieId	INTEGER,
                title	TEXT
            );
        """,
        "Ratings_Table":
        """
            CREATE TABLE Ratings_Table
            (
                userId	INTEGER,
                movieId	INTEGER,
                rating	REAL,
                timestamp	INTEGER
            );
        """,
        "User_info_Table":
        """
            CREATE TABLE User_info_Table
            (
                userId INTEGER PRIMARY KEY,
                userName VARCHAR(255)         
            );
        """,
}


class DBInitializer:
    def execute(self):
        existing_tables = self.get_existing_tables()
        self.__create_inexist_table(existing_tables)

    def get_existing_tables(self):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
            records = cursor.fetchall()

        return [single_row["tbl_name"] for single_row in records]

    def __create_inexist_table(self, existing_tables):
        for necessary_table, table_creating_command in necessary_table_to_create.items():
            if necessary_table not in existing_tables:
                self.create_table_with_specefied_command(table_creating_command)

    def create_table_with_specefied_command(self, command):
        with DBConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()