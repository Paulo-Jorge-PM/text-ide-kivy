#include <stdio.h>
#include <sqlite3.h>

int c = 0;

char *words(char *word) {

/* return "teste"; */


sqlite3 *db;
sqlite3_stmt *stmt;
int count = 0;

sqlite3_open("words.sqlite", &db);

if (db == NULL)
{
	printf("Failed to open DB\n");
	return "Erro";
}


if(sqlite3_prepare_v2(db, "SELECT * FROM words WHERE word LIKE 'pau%'", -1, &stmt, NULL) != SQLITE_OK) {
    sqlite3_close(db);
    printf("Can't retrieve data: %s\n", sqlite3_errmsg(db));
    return("erro");
}


 /* while(sqlite3_step(stmt) == SQLITE_ROW)
  {*/
    /*printf("%16s | %32s\n",
           sqlite3_column_text(stmt, 0),
           sqlite3_column_text(stmt, 1));*/
    
 /*   count++;
  }*/



	/*printf("%s", word);*/
	
	sqlite3_finalize(stmt);

	sqlite3_close(db);

	/*getc(stdin);*/

	return "done";
}

/*int main() {
words("pau");
return 0;
}*/
