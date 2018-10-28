# MINERAL CATALOG v2


# Just Did

1. Start Project 8 from end of Project 6.
2. Search by Group functionality somewhat deployed as of Project 6!
	- Search by Group functionality needs to be adjusted to Project 8 specs. [x]
3. Make templates match (or exceed) sample files.  (Mostly) deployed as of Project 6.
4. Allow text search.
	- EXTRA: FULL Text search.
5. Allow filter by first letter of mineral name.
6. Allow filter by group.
7. In Progress: Filter by category.



# Pre-Existing Errors to Debug [x]
1. What I thought was a CSS error turned out to be an issue in Chrome's cache, somehow. 
2. Homepage is now mineral list with A minerals selected.  Slideshow not in use.


# To Do:
1. Allow filtering by the first letter of the mineral name. [x]
	- Add links for each letter of the alphabet. [x]
	- This should be added to the layout template so that it appears on every page.[x]
	- When a letter is clicked, a list of minerals that start with that letter should be displayed in the list view.[x]
	- The letter of the alphabet currently being displayed should be bolded.[x]
	- In the details view, no letter should be bolded.[x]
	- On the homepage, select ‘A’ by default.[x]

2. Allow text search. [x]
	- Add a search box and button.[x]
	- The search box and button should be implemented as a form.[x]
	- When the search button is clicked, the site will search for minerals whose name contains the search text.[x]
	- The names of the minerals that match the search will be displayed in the list view.[x]
	- Add the search form to the layout template so that searching can be performed from any page in the site.[x]

3. Allow filtering by group. [x]
	- Add the ability to filter the list of minerals by adding links to these groups on the left side of the layout template.[x]
	- Clicking a group name, displays a list of all of the minerals in the database that are in that group. [x]
	- The group name being displayed should be bolded. [x]
	- In the details view, no group name should be bolded. [x]
	- Group List view now renders to mineral list template.  Group List template is now deprecated.

4. Optimize database queries [] <---- Mostly done.  Just need to finish category list.
	- Apply django-debug-toolbar to project. [x] <---- That felt clumsy and haphazard but at least it happened!!!!
	- Use the django-debug-toolbar to check that queries to the database take no longer than 10ms to complete. [x]

5. Unit test the app. []
	- Write unit tests to test that each view is displaying the correct information.[]
	- Write unit tests to test that the models,[] classes,[] and other functions behave as expected.[]

6. Make the templates match the style used in the example files.[x]
	- Look at the example HTML files and global.css to determine the styles used in the pages.[x]

7. Coding Style[]
	- Make sure your coding style complies with PEP 8.[]


# To Exceed Expectations! (Definitely Do These)
1. Allow full-text search[x]
	- Instead of only searching the mineral names, the site will search all fields in the database and display the names of the minerals that contain the search text. [x]
	- Add option to restrict/expand text search? Not an element of the original assignment.[]

2. Add more ways to filter.[]
	- Instead of just filtering by first letter and group, add one or more additional filters.[](Use category and color attributes.)
	- These should behave like the group filter.[]
	- Example filters are color and crystal habit, but you can choose to add filtering for any property you like.
	- Hint: the filters can act like canned search queries. [more of the same, definitely do this, to a point!]
	- Attempting right side category list.  Afterwards, goto unit testing.[]