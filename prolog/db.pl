% this is our super awesome database 
loves(noor, snickers).
loves(nessa, sneakers).
loves(nessa, mango).

shoes(sneakers).
chocolate(snickers).

food(snickers).
food(mango).

loves_chocolate(X) :- loves(X,Y),chocolate(Y),write('Loves chocolate').

eats_food(X):-
	loves(X, Y),food(Y).

male(bob).
male(roger).
female(lulu).
female(bobette).
female(rosette).
female(momo).

parent(bob,roger).
parent(bob, lulu).
parent(roger, bobette).

parent(bobette, roger).
parent(lulu, roger).
parent(bobette, momo).
parent(lulu, momo).

is_grandparent(X, Y):-
	parent(X,Z),parent(Z,Y).

mom_of(M):-
	female(M),parent(M,C),
	write(M),write(' is the mother of '),tab(1), write(C),nl.

are_siblings(A,B):-
	parent(X,A),parent(X,B),
	write(X),write(' is the parent of both '),write(A),write(B),nl.
	

are_coparents(X, Y):-
	parent(X,Z),parent(Y,Z),
	format('~w ~w ~s of ~w ~n',[X,Y,"are co-parents",Z]).

% anonymous variable 

what_grade(5):-
	write('Go to kindergarten').
what_grade(20):-
	write(' get out of your parents house').
what_grade(Others):-
	Others > 22,write('not in school');
	Others > 17,Others < 23,write('in college');
	Others > 14, Others < 18,write('in high school').

% structure is going to have a functor

has(albert, olive).
owns(Albert, pet(cat, olive)).


% recursion
related(X,Y) :-
	parent(X,Z),
	related(Z,Y).

is_even(X):-
	0 is X mod 2 , format('~w is even',[X]);
	1 is X mod 2 , format('~w is odd', [X]).

say_hi :-
	write('What is your name ?'),
	read(X),
	format('Hi, ~w',[X]).

count_to_10(10):- write(10), nl.

count_to_10(N):- 
	write(N),nl,
	M is N+1,
	count_to_10(M).



