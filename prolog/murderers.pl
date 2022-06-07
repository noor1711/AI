/*Ok so our facts are going to be 
 man, woman */
% each room and weapon are to be assigned to a unique person

man(george).
man(john).
man(robert).

woman(barbara).
woman(christine).
woman(yolanda).

% a person can be a man or a woman
person(X):- woman(X).
person(Y):- man(Y).

%  the same person can’t be in different rooms
not_same(A, B, C, D, E, F):-
	person(A),person(B),person(C),person(D),person(E),person(F),
	\+A=B, \+A=C, \+A=D, \+A=E, \+A=F, 
	\+B=C, \+B=D, \+B=E, \+B=F, 
	\+C=D, \+C=E, \+C=F, 
	\+D=E, \+D=F, 
	\+E=F.

% lets start with the clues.
/* Clue 1: The man in the kitchen was not found with the rope, knife, or bag. Which weapon,
then, which was not the firearm, was found in the kitchen? */

one(Rope, Knife, Bag, Firearm, Kitchen):-
	man(Kitchen), % the listing of man should contain kitchen var
	\+Kitchen=Knife,
	\+Kitchen=Bag,
	\+Kitchen=Rope,
	\+Kitchen=Firearm.

/*CLUE 2:Barbara was either in the study or the bathroom; Yolanda was in the other. Which room was Barbara found in?*/
two(Study,Bathroom):-
	Study=barbara, Bathroom=yolanda.

two(Study,Bathroom):-
	Study=yolanda, Bathroom=barbara.


/* Clue 3: The person with the bag, who was not Barbara nor George, was not in the bathroom nor the dining room. Who had the bag in the room with them? */


three(Bag, Bathroom, Diningroom):-
	\+Bag=barbara,\+Bag=george,
	\+Bag=Bathroom,\+Bag=Diningroom.

/*Clue 4: The woman with the rope was found in the study. Who had the rope? */

four(Study, Rope):-
	woman(Study),Rope=Study.

/* Clue 5: The weapon in the living room was found with either John or George. What weapon was in the living room?*/

five(Livingroom):-
	Livingroom=john.
five(Livingroom):-
	Livingroom=george.


/* Clue 6: The knife was not in the dining room. So where was the knife? */
six(Knife,Diningroom):-
	\+knife=Diningroom.


/* Clue 7: Yolanda was not with the weapon found in the study nor the pantry. What weapon was found with Yolanda? */

seven(Study,Pantry):-
	\+yolanda=Study,\+yolanda=Pantry.


/*Clue 8: The firearm was in the room with George. In which room was the firearm found?*/

eight(Firearm):-
	Firearm=george.

/*It was discovered that Mr. Boddy was gassed in the pantry. The suspect found in that room was the murderer. Who, then, do you point the finger towards?*/

who_done_it(X):-
	not_same(Bathroom,Diningroom,Kitchen,Livingroom,Pantry,Study),
	not_same(Bag,Firearm,Gas,Knife,Poison,Rope),
	one(Rope, Knife, Bag, Firearm, Kitchen),
	two(Study,Bathroom),
	three(Bag, Bathroom, Diningroom),
	four(Study, Rope),
	five(Livingroom),
	six(Knife,Diningroom),
	seven(Study,Pantry),
	eight(Firearm),
	X = Gas, X = Pantry,
	format('~n~n~w is the murderer~n~n~n',[X]),												
pretty_print(Bathroom,Diningroom,Kitchen,Livingroom,Pantry,Study,Bag,Firearm,Gas,Knife,Poison,Rope).

pretty_print(Bathroom,Diningroom,Kitchen,Livingroom,Pantry,Study,Bag,Firearm,Gas,Knife,Poison,Rope):-
write('People : Rooms'),nl,
format('~w : Bathroom~n',[Bathroom]),
format('~w : Dining Room~n',[Diningroom]),
format('~w : Kitchen~n',[Kitchen]),
format('~w : Living Room~n',[Livingroom]),
format('~w : Pantry~n',[Pantry]),
format('~w : Study~n',[Study]),nl,nl,
write('People : Weapons'),nl,
format('~w : Bag.~n',[Bag]),
format('~w : Firearm.~n',[Firearm]),
format('~w : Gas.~n',[Gas]),
format('~w : Knife.~n',[Knife]),
format('~w : Poison.~n',[Poison]),
format('~w : Rope.~n',[Rope]),nl,nl.

