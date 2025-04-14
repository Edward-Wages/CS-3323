

Page
2
of 3
#lang racket
;Edward Wages - 113540137 - Homework 5
;Due 4/1/2025
;Each operation is formatted as follows: a comment stating where the operation
starts, followed by a helper method, with the main method
;located just under the helper method
;; Helper Functions
(define (remove-trailing-zeros lst) ;Removes the zeros from the sublists
(let ((rev (reverse lst))) ;Start by reversing the list
(reverse
(cond ((null? rev) '()) ;Checking to see if the reversed list is null
((zero? (car rev)) (remove-trailing-zeros (reverse (cdr
rev)))) ;recursively call the function on the reverse of the cdr of rev
(else rev)
)
)
)
)
(define (remove-trailing-empty-sublists lst)
(let ((rev (reverse lst)))
(reverse
(cond ((null? rev) '())
((null? (car rev)) (remove-trailing-empty-sublists (reverse (cdr rev))))
(else rev)
)
)
)
)
;; Polynomial Addition
(define (poly_add_helper c1 c2) ;Helper function which does the adding in the
sublists
(cond ((null? c1) c2) ;Whenever one of the lists is null, we can just return the
opposite sublist
((null? c2) c1)
(else (cons (+ (car c1) (car c2)) ;adds the values in the specific position
of the sublist
(poly_add_helper (cdr c1) (cdr c2));Recrusively call the
function on the rest of the sublist
)
)
)
)
(define (poly_add p1 p2)
(let ((raw-result ;setting up raw-result for later use
(cond ((null? p1) p2) ;if one polynomial list is empty then we can stop
here
((null? p2) p1)
(else (cons (poly_add_helper (car p1) (car p2)) ;Otherwise we will
call our helper function on the first sublist & continue there
(poly_add (cdr p1) (cdr p2))))))) ;Recursively call the
rest of the polynomial list
(remove-trailing-empty-sublists (map remove-trailing-zeros raw-result) ;Call
the trimming methods to clean up the result
)
)
)
;; Polynomial Subtraction
(define (poly_sub_helper c1 c2) ;Functions pretty similarly to addition, therefore
will only comment sparingly when necessary
(cond
((null? c1) (map - c2)) ; Whenever c1 is empty, we are essentially doing 0 -
c2, so we return the necessary operation
((null? c2) c1)
(else (cons (- (car c1) (car c2))
(poly_sub_helper (cdr c1) (cdr c2))
)
)
)
)
(define (poly_sub p1 p2)
(let ((raw-result
(cond
((null? p1) (map (lambda (lst) (map - lst)) p2)) ;If apol is empty; we
can just return what is basically 0 - bpol
((null? p2) p1)
(else (cons (poly_sub_helper (car p1) (car p2))
(poly_sub (cdr p1) (cdr p2))
)
)
)
)
)
(remove-trailing-empty-sublists
(map remove-trailing-zeros raw-result)
)
)
)
;; Polynomial Multiplication
(define (poly_mult_coeff c1 c2)
(cond ((null? c1) '()) ;If either polynomial is null, we can just return an
empty list as representative of multiplying by zero
((null? c2) '())
(else
(remove-trailing-zeros
(poly_add_helper
(map (lambda (x) (* (car c1) x)) c2) ;Multiplies the values
in the sublists
(cons 0 (poly_mult_coeff (cdr c1) c2)) ;Recursively call to
the rest of the sublist
)
)
)
)
)
(define (poly_mul p1 p2)
(cond
((or (null? p1) (null? p2)) '()) ;returns an empty list if any polynomials are
null
(else (remove-trailing-empty-sublists
(poly_add
(map (lambda (term) (poly_mult_coeff (car p1) term)) p2) ;Calls the
helper method to multiply within the sub list
(cons '() (poly_mul (cdr p1) p2))
)
)
)
)
)
;; Polynomial Differentiation
(define (deriv_coeff c)
(if (null? c)
'() ;The derivation of 0 is still zero, so we can return an empty list
(let ((power 0)) ;The power tells us what to do once we reach the current
position within the sublist
(remove-trailing-zeros
(map (lambda (coeff)
(set! power (+ power 1)) ;incrementing power
(* power coeff))
(cdr c)
)
)
)
)
)
(define (poly_derx p)
(remove-trailing-empty-sublists ;Essentially just calls the helper method &
removes the trailing values from the result
(map deriv_coeff p)
)
)
