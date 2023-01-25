# Galois Theory and

# Insolvability of the Quintic

#

## Shaastra Workshop

#  

---

#
## Module 1 
# Introduction to 
# Abstract Algebra
#

---

## Why abstract algebra?

Abstract algebra might seem
very vague and might sound like
a mathematical curiosity

But be assured that they have
wide-ranging applications

---

## Why abstract algebra?

### Error control coding

In coding theory, group codes
are a type of code

They are a fundamental part
of coding theory

---

## Why abstract algebra?

### 3D Modelling

Quaternions are used extensively
in 3D modelling

Quaternions are an example of an
algebraic structure called \textbf{ring}

---

## Why abstract algebra?

### Chemistry

Chemists use Group theory to
analyze the symmetries of lattices

Group theory is an elegant way
to capture symmetries, as for
describing symmetries, the nature 
of the molecule does not matter

---

### What is abstract algebra?

Abstract algebra consists of algebraic structures

An algebraic structure is a set, with
some operations, and some axioms (rules)

Some examples are groups, rings, and fields 

---

### The idea of homomorphism

A homomorphism is a structure-preserving
map between two algebraic structures

Consider a structure $A$, with some
operation $\cdot$, another structure $B$
with some operation $\times$

$f : A \to B$ is a homomorphism
iff $f(a \cdot b) = f(a) \times f(b) \forall a, b \in A$

---

# Vector space

$V$ is a set over a field $K$

Abelian Group over addition, i.e. closure,
associativity, identity, inverse, commutativity
Compatibility of scalar and field 
multiplication $a (b \vec c) = (ab) \vec c, a, b \in K, \vec c \in V$
Scalar identity = 1
Distributive laws

---


# 
## Reading Assignment
# 

Intuition and Applications
of Category Theory

#

---

#
## Module 2
#  
# Group Theory
#

---

### Example 1

$\mathbb{Z}$ under $+$

- Addition of two integers
results in an integer (closure)

- Addition of integers is
associative, $a + (b + c) = (a + b) + c$

- 0 is the additive identity

- $\forall a \in \mathbb{Z}, \exists a^{-1}: a + a^{-1} = 0$

---

### What is a group?

It consists of a set $S$ with binary operation $\odot$

- The set is closed under $\odot$

- It is associative $(a \odot b) \odot c = a \odot (b \odot c)$

- There exists an identity e: $a \odot e = a \forall a \in S$

- Inverse existence: $\forall a \exists a^{-1} : a a^{-1} = e$

---

### Example 2

$\{ 1, w, w^2 \}$ under $\times$

- It is closed (by observation)

- It is associative (by associativity
of multiplication of complex numbers)

- There exists a multiplicative identity $1$

- There exists a multiplicative inverse
$1^{-1} = 1$, $w^{-1} = w^2, (w^2)^{-1} = w$

---

### Abelian Group

#
#

Groups which are commutative
are called Abelian Groups

#

Eg. $(\mathbb{Z}, +), (\mathbb{R}, +)$

#

---

### Example of non-Group

$(\mathbb{R}, \times)$

- It is closed

- It is associative

- Identity element 1 exists

- Inverse exits for all non-zero elements
But, $0$ does not have multiplicative inverse!

$R^* = R - \{0 \}$ is a group under $\times$

--- 

### Groups and Symmetries

#
## Go to 
## Image
#
#

---

### Dihedral Group of order 6

# Insert Cayley Diagram

---

### Subgroup

A subset of a group which is also
a group is a subgroup

$H \subseteq G$ and H is a group
$\implies$ H is a subgroup

Eg. $\mathbb{R}^+$ is a subgroup
of $\mathbb{R}^*$ under $*$

---

### Subgroups of Dihedral group

Subgroups of $D_6$ are

$\{e\}$
$\{e, a\}$
$\{e, r, r^2\}$
$D_6$ itself

---

# Motivation: Cosets

# Insert image

---

### Normal subgroup

A subgroup is said to be normal
iff its left and right cosets
are equal (denoted by $H \triangleleft G$)

For $D_6$, $\{e\}$, $\{e, r, r^2\}$,
$D_6$ are normal subgroups

$\{e, a\}$ is \textbf{not} normal!

---

### Exercise

Prove that all left cosets
of a subgroup have the same size

\textbf{Method: } Prove that 
there is a bijection between
a subgroup and its left coset

---

### Index of a subgroup

Index of a subgroup H in G
is the number of left cosets,
and is denoted by $[G : H]$

Note that the
number of left cosets =
number of right cosets

---

## Theorem 1: Lagrange's theorem

$$|G| = [G: H] |H|$$

### Proof

All cosets are of equal size

The number of cosets is $[G : H]$

Number of elements in each coset is $|H|$

Total number of elements in the group
has to be product of the above two

---

### Quotient Group

For $N \lefttriangle G$, consider
cosets of N. The set of cosets is 
called a quotient group.

Consider $C_2 \lefttriangle C_6$.

$C_6 / C_2 = \{ \{0, 3\}, \{1, 4\}, \{2, 5\} \}$

The set of left cosets
has the same structure as $C_3$

---

#
## Module 3
#  
# Frieze Groups
#

---

### Add images

---


#
## Module 4
#  
# Ring Theory
#

---

### Definition of a Ring

A ring is a set $R$ with two binary operations
$+$ and $\times$, such that
$1 \in R$
$x, y \in R$ \implies $x + y, xy, -x \in R$

Note that a multiplicative inverse
does not have to exist

---

### Example 1

$\{a + b i : a, b \in \mathbb{Z} \}$

It is clearly a group under addition

It is closed under multiplication

It is associative under multiplication

1 is the identity element

Except $\pm 1, \pm i$, no other element
has multiplicative inverse

---

### Rethinking about Polynomials

A polynomial is a function that
takes in some t as input and returns
some $f(t) = a_n t^n + a_{n - 1} t^{n - 1} + \dots + a_0$

A polynomial in the indeterminate t
is the expression $a_n t^n + a_{n - 1} t^{n - 1} + \dots + a_0$

$t$ is just a placeholder.

Degree of polynomial is largest $n: a_n \ne 0$

---

### Polynomial Rings

A polynomial over a ring R is denoted by $R[t]$.
It consists of all polynomials with coefficients in
R. The degree can be anything

- Polynomials are clearly a group under addition

- It is closed under multiplication

- There is a multiplicative identity,
the 1 polynomial

---

### Irreducibility of Polynomials

A polynomial over a subring R of $\mathbb{C}$
is reducible if it can be written as a product
of two polynomials in R of smaller degree

All polynomials of degree 0 or 1
are irreducible

They are analogous to primes!

---

### Examples of irreducible polynomials

Consider $t^2 + 2$

It is irreducible over $\mathbb{Z}$. To prove,
let $t^2 + 2 = (at + b)(ct + d)$,
$a, b, c, d, \in \mathbb{Z}$.

Now, $ac = 1$ \implies $a = c = 1$, or $a = c = -1$.

Also, $bc + ad = 0 \implies b + d = 0$.
Also, $2 = bd \implies -2 = d^2$.

---

### Zeroes of a Polynomial

For a polynomial $f \in R [t]$,
$\alpha \in R$ is said to be a zero iff
$f(\alpha) = 0$

Example

$\sqrt 2 i $ is a zero of $t^2 + 2i \in \mathbb C[t]$
$-\sqrt 2 i $ is a zero of $t^2 + 2i \in \mathbb C[t]$

---

#
## Module 5
#  
# Field Theory
#

---

### What is a field?

A field is a ring in which
multiplication is commutative and
inverses exist for all elements other
than $0$, the additive identity

$\mathbb{Q}, \mathbb{R}, \mathbb C$ are fields
$a + b\sqrt{2}, a, b \in \mathbb Q$ is a field

---

### Motivation

Consider the polynomial $f = t^2 - 2 \in \mathbb Q [t]$
This polynomial is irreducible over $\mathbb Q$,
but it is reducible in $\mathbb R$

Consider a set $S = {a + b \sqrt{2}: a, b \in Q}$
This set S is a field!

Also note that $f$ is reducible over $S$

---

## Field extension

A field extension $f: A \to B$ is an
injective homomorphism, where $A, B \in \mathbb C$

The homomorphism is usually unambigious

### Example

The identity map in $\mathbb Q \to \mathbb R$
The identity map in $\mathbb R \to \mathbb C$


---

### Generator of a field

A field $F$ is said to be generated by
a set $S$ if it is the intersection
of all subfields that contain $S$

It is considered the 'smallest'
subfield containing $S$

$\mathbb Q (\sqrt 2)$ is the field
generated by $\{\sqrt{2}\}$

---

### Field extension as a vector space

Consider the set $\mathbb Q (\sqrt 2)$.
This consists of $w = a + \sqrt 2 b, a, b, \in \mathbb Q$

Think of $w$ as a degree 2 vector space,with 
basis $\{ 1, \sqrt 2 \}$, and field $\mathbb Q$

In general, the degree of a field extension
$L$ over $K$ is the degree of the vector space $L$,
over the field $K$ and is denoted by $[L : K]$

---

## Theorem 2: Tower Law

For subfields $K \subseteq L \subseteq M$, $[M : K] = [M : L][L : K]$

### Proof

Let $x_i$ be a basis for $L$ in $K$
let $y_j$ be a basis for $M$ in $L$

Our aim is to prove that
$x_i y_j$ is a basis for $M$ in $K$

We have to prove linear
independence and spanning

---

### Linear independence

Let $\sum_{ij} k_{ij} x_i y_j \in M$

As $M$ is linearly independent in $L$,
$\sum_j (\sum_i k_{ij} x_i) y_j = 0 \implies \sum_i {k_{ij} x_i} = 0$

As $L$ is linearly independent in $K$,
$\sum_i {k_{ij} x_i} = 0 \implies k_{ij} = 0 \forall i, j$

---

### Spanning

Let $x \in M$

As $y_j$ spans $M$,
$x = \sum_j \lambda_j y_j$

As $x_i$ spans $L$,
$y_j = \sum \lambda_i x_i$

$x = \sum_{ij} \lambda_{ij} x_i y_j$,
where $\lambda_{ij} = \lambda_i \lambda_j$

---

### Detailed example: $\mathbb Q (\sqrt 2, i)$

It consists of numbers of the form
$\alpha = a + b \sqrt 2 + c i + d \sqrt 2 i, a, b, c, d, \in \mathbb Q$

$\mathbb Q (\sqrt 2, i)$ is an extension of $\mathbb Q (\sqrt 2)$
$\mathbb Q (\sqrt 2, i)$ is an extension of $\mathbb Q (i)$
$\mathbb Q (\sqrt 2, i)$ is an extension of $\mathbb Q (\sqrt 2 i)$

Exercise: Prove that $\alpha^{-1} \in \mathbb Q (\sqrt 2, i)$

By tower law, degree is 4

---

### Subfield

A field $K$ is said to be a subfield
of a field $L$ if $K \subset L$

$\mathbb Q$ is a subfield of $\mathbb Q (\sqrt 2)$

$\mathbb Q$ is a subfield of $\mathbb Q (\sqrt [4] 2)$

$\mathbb R$ is a subfield of $\mathbb C$

