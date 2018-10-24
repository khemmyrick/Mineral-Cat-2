# MINERAL CATALOG v2

#Just Did
1. Start Project 8 from end of Project 6.
2. Search by Group functionality somewhat deployed as of Project 6!
	- Search by Group functionality needs to be adjusted to Project 8 specs. []
3. Make templates match (or exceed) sample files.  (Mostly) deployed as of Project 6.
	- Get CSS working with both Opera AND Chrome?
4. Allow text search.
	- EXTRA: FULL Text search.



# Pre-Existing Errors to Debug
1. (Surprise discovery) P6 CSS Works (mostly) as intended in Opera 56 but not Chrome 69.
2. (Known known) JavaScript Slideshow as-is is objectively un-aesthetic. [Unless I think of somewhere else to put it, deprecate with non-list homepage]


# To Do:
1. Allow filtering by the first letter of the mineral name. []
	- Add links for each letter of the alphabet. [x]
	- This should be added to the layout template so that it appears on every page.[]<---(This specifically is surprisingly difficult)
	- When a letter is clicked, a list of minerals that start with that letter should be displayed in the list view.[x]
	- The letter of the alphabet currently being displayed should be bolded.[]
	- In the details view, no letter should be bolded.[]
	- On the homepage, select ‘A’ by default.[](So, the Homepage should be mineral_list with A selected... no seperate homepage needed)

2. Allow text search. [x]
	- Add a search box and button.[x]
	- The search box and button should be implemented as a form.[x]
	- When the search button is clicked, the site will search for minerals whose name contains the search text.[x]
	- The names of the minerals that match the search will be displayed in the list view.[x]
	- Add the search form to the layout template so that searching can be performed from any page in the site.[x]

3. Allow filtering by group. []
	- Add the ability to filter the list of minerals by adding links to these groups on the left side of the layout template. []
	- Clicking a group name, displays a list of all of the minerals in the database that are in that group. []
	- The group name being displayed should be bolded. []
	- In the details view, no group name should be bolded. []

4. Optimize database queries [] <---- This might be the hard part.
	- Use the django-debug-toolbar to check that queries to the database take no longer than 10ms to complete.

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

2. Add more ways to filter.[]
	- Instead of just filtering by first letter and group, add one or more additional filters.[]
	- These should behave like the group filter.[]
	- Example filters are color and crystal habit, but you can choose to add filtering for any property you like.
	- Hint: the filters can act like canned search queries. [more of the same, definitely do this, to a point!]