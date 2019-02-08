#include <stdio.h>
#include <sqlite3.h>
#include <string.h>

char dbname= "words.sqlite";
char sql;



sqlite3 * db;
sqlite3_stmt *stmt;
char message[255];

char * word;






int main(void)
{


sqlite3 *db;
sqlite3_stmt *stmt;

sqlite3_open("words.sqlite", &db);

if (db == NULL)
{
	printf("Failed to open DB\n");
	return 1;
}


printf("Performing query...\n");
sqlite3_prepare_v2(db, "select * from expenses", -1, &stmt, NULL);



        /* open the database */
        int result=sqlite3_open(dbname,&db) ;
        if (result != SQLITE_OK) {
                printf("Failed to open database %s\n\r",sqlite3_errstr(result)) ;
                sqlite3_close(db) ;
                return 1;
        }
        printf("Opened db %s OK\n\r",dbname) ;

        /* prepare the sql, leave stmt ready for loop */
        sql = "SELECT word FROM words WHERE word LIKE 'paulo%' limit 500";
        result = sqlite3_prepare_v2(db, sql, strlen(sql)+1, &stmt, NULL) ;
        if (result != SQLITE_OK) {
                printf("Failed to prepare database %s\n\r",sqlite3_errstr(result)) ;
                sqlite3_close(db) ;
                return 2;
        }

        printf("SQL prepared ok\n\r") ;

        /* allocate memory for decsription and venue */
        /* word = (char *)malloc(100) ; */

        /* loop reading each row until step returns anything other than SQLITE_ROW */
        do {
                result = sqlite3_step (stmt) ;
                if (result == SQLITE_ROW) { /* can read data */
                         strcpy(word, (char *)sqlite3_column_text(stmt,1)) ;
                         printf("Palavra teste: \n\r") ;
                }
       } while (result == SQLITE_ROW) ;

    /* finish off */
        sqlite3_close(db) ;
        /* free(word) ; */
        return 0;
}
