// %Rules sum([], 0).

sum([X|Tail], Sum) :- sum(Tail, Sum2), Sum is X + Sum2.

// Query ?- sum([1, 2, 0, -90, 45, 39], Sum)