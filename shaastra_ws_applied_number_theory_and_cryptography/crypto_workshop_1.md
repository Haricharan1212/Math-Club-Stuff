#   

# Number Theory

# and Cryptography

#

## Shaastra Workshop

#  

---

#
## Module 1 
# Introduction to 
# Number Theory
#

---

# Definition of $a | b$

We say that $a | b$ (a divides b) iff
$\exists k$ such that $ak = b$

### Some examples
$5 | 10 \rightarrow k = 2$ 
$4 | -12 \rightarrow k = -3$
$3 \nmid 10 \rightarrow$ No such k

--- 

## Mathematical Definition
## of Prime

It is a number greater than 1 that
is not a product of two smaller numbers

#

For prime p, $a | p \implies a = 1$ or $a = p$

---

## An example

$3 | 9, 3 | 12, 3 | 123$
Then, $3  | (9 + 12 + 123)$
Also, $3 | (2 \times 9 + 4 \times 12 + 5 \times 123)$
$3 | (c_1 \times 9 + c_2 \times 12 + c_3 \times 123) \forall c_1, c_2, c_3$ 

---

# Theorem 1

If $a | b_i \forall i$, $a | \sum_i c_i b_i \forall c_i$ 

### Proof
$a | b_i \implies \exists k_i : a k_i = b_i$ for some $k_i$
$\sum_i c_i b_i = \sum_i c_i a k_i = a \left (\sum_i c_i k_i \right )$
$\sum_i c_i b_i = ak$ for $k = \left ( \sum_i c_i k_i \right ) \square$

---

## Greatest Common Divisor (GCD)
$\gcd(a, b)$: Greatest number which divides both a and b
# 
$\gcd(3, 9) = 3$
$\gcd(6, 9) = 3$
$\gcd(20, 15) = 5$

---

### We say that $c = \gcd(a, b)$ iff:
- \textbf{Common Divisor} Condition: $d | a$ and $d | b$ 
- \textbf{Greatest} Condition: $c | a$ and $c | b \implies c \le d$

### Example: $\gcd (12, 18) = 6$
- $1 | 12$ and $1 | 18 \implies 1 \le 6$
- $2 | 12$ and $2 | 18 \implies 2 \le 6$
- $3 | 12$ and $3 | 18 \implies 3 \le 6$
- $6 | 12$ and $6 | 18 \implies6 \le 6$

---

## Co-prime numbers

#

Iff $\gcd(a, b) = 1$,
$a$ and $b$ are said to be
co-prime or relatively prime

# 

---

#

## Intuition for
## Modular Arithmetic

#

---

# Insert Clock image

--- 
### Modular Arithmetic

$a \equiv b \pmod n$
(a is congruent to b modulo n)
iff $n | (a - b)$

$13 \equiv 3 \pmod 5$ because $13 - 3 = 10$, $5 | 10$
$49 \equiv 0 \pmod 7$ because $49 - 0 = 49$, $7 | 49$
$-4 \equiv 2 \pmod 6$ because $-4 - 2 = -6$, $6 | -6$

---

# Theorem 2: Cancellation Law

If $ar \equiv br \pmod p$ and $\gcd(p, r) = 1$, $a \equiv b \pmod p$

### Proof

$ar \equiv br \pmod p \implies p | (ar - br)$

$ar \equiv br \pmod p \implies p | (a - b)$, as $p \nmid r$

$a \equiv b \pmod p$

---

# Theorem 3: Division Theorem

For any a, b, $\exists$ unique $q, r: a = bq + r, 0 \le r < q$

### Proof

Try it Yourself!!

Sidenote: r is called the \textbf{remainder} or \textbf{residue}
and is represented by $r = a \% q$

---

## Interesting Problem:

You have a large number of two Rupee coins
and a large number of five Rupee coins.
How can you create Rupees 17?

### Mathematical Reformulation

Find integers s, t, such that
$2s + 5t = 17$
This is a Linear Diophantine Equation (LDE)

---

### Observations about LDE

$2s + 5t = 17$
### 
If $(s_0, t_0)$ are solutions, 
$(s_0 + 5 \theta, s_0 - 2 \theta)$ is also a solution for integer $\theta$

If we find one solution,
we can generate infinitely many solutions!!

---

### Modular Inverse and Diophantine Equations

If $\gcd(a, p) = 1$, $\exists x: ax \equiv 1 \pmod p$
x is called the modular inverse of a

($x = a^{-1}$)

$\implies p | (ax - 1)$

$kp = ax - 1$

$\boxed{ax - kp = 1}$

$\rightarrow$ Example of Linear Diophantine Equation

---

## Theorem 4: Uniqueness of Inverse

Given $\gcd(a, n) = 1$, $a^{-1}$ is unique $\pmod n$

## Proof:
By contradiction, assume $ax \equiv ay \equiv 1 \pmod{n}$

$\implies a(x - y) \equiv 0 \pmod n$

$\implies n | a(x - y)$

$\implies n | (x - y)$ [as $\gcd(n, a) = 1$]

$\implies x \equiv y \pmod{n}$

---

#
# Question:
# How to solve Linear
# Diophantine Equations?
#

---

# 
# Euclids Division Algorithm
# for GCD
# 

---

## Theorem 5: 

$\gcd(a, b) = \gcd(b, a \% b)$

For instance,
$\gcd(32, 24) = \gcd(24, 8) = 8$

$\gcd(42, 27) = \gcd(27, 15)$

$= \gcd(15, 12) = \gcd(12, 3) = 3$

---

## Theorem 5: 
$\gcd(a, b) = \gcd(b, r)$, where $r = a \% b$
## Proof:

### i) Proof of common divisor

Let $g = \gcd(a, b)$

$a = kb + r$
$g | a, g | b \implies g|r$

So, r is a common divisor for b, r

---

## Theorem 5: 
$\gcd(a, b) = \gcd(b, r)$, where $r = a \% b$
## Proof:

### ii) Proof that it is greatest
Consider $c: c | a, c | b$

$\implies c | r$
Also, $c \le g$, by definition

So, g is $\gcd(b, r)$!

---

## Euclid\'s Division Algorithm

Aim: find $\gcd(39, 15)$

$39 = 15 \times 2 + 9$ 

$15 = 9 \times 1 + 6$ $[\gcd(39, 15) = \gcd(15, 9)]$

$9 = 6 \times 1 + 3$ $[\gcd(15, 9) = \gcd(9, 6)]$

$6 = 3 \times 2 + 0$ $[\gcd(9, 6) = \gcd(6, 3) = 3]$

$\boxed{\gcd(39, 15) = 3}$

---

# Insert Python
# implementation of Algo

---

## Euclid\'s Division Algorithm

Aim: find $\gcd(5, 14)$

$14 = 5 \times 2 + 4$ 

$5 = 4 \times 1 + 1$

$4 = 1 \times 4 + 0$

$\boxed{\gcd(5, 14) = 1}$

---

## Extended Euclidean Algorithm

Aim: Find $5^{-1} \pmod{14}$

Reformulation: Find $x, k: 5x - 14k = 1$

### Rearrange at Each Step!

$14 = 5 \times 2 + 4 \implies 4 = 14 - 5 \times 2$ 

$5 = 4 \times 1 + 1 \implies \boxed{1} = 5 - 4 \times 1 = \boxed{3 \times 5 - 1 \times 14}$

$4 = 1 \times 4 + 0 \rightarrow$ Ignore this line :(

$5^{-1} \equiv 3 \pmod{14}$

---

## Interesting Problem:

You have a large number of two Rupee coins
and a large number of five Rupee coins.
How can you create Rupees 17?

### Mathematical Reformulation

Find integers s, t, such that $2s + 5t = 17$

---

### Mathematical Reformulation

Find integers s, t, such that $2s + 5t = 17$

Try solving it on your own now!
You need two things:
- Extended Euclidean Algorithm
- If $(s_0, t_0)$ are solutions, 
$(s_0 + 5 \theta, s_0 - 2 \theta),  \theta \in \mathbb{Z}$ is solution

Solutions are: $(1, 3)$ and $(6, 1)$

---

#
## Module 2 
# Proving Two
# Interesting Theorems
#

---

## Motivation

# Insert table
# And put a bunch of values

---

## Theorem 6: Wilson\'s Theorem
$(p - 1)! \equiv -1 \pmod{p}$

### Proof:

\textbf{Lemma:}
Solutions to $x^2 = 1 \pmod p$
are $1 \pmod p$ and $(p - 1) \pmod p$

Proof of Lemma: Substitute and check!

---
## Theorem 6: Wilson\'s Theorem
$(p - 1)! \equiv -1 \pmod{p}$

### Proof:

$(p - 1)! = 1 \times 2 \times 3 \times \dots \times (p - 1)$

Now, pairs of a number and its inverse
can be cancelled out

Only $1$ and $p - 1$ cannot be cancelled out,
as they are their own inverses

---
## Theorem 6: Wilson\'s Theorem
$(p - 1)! \equiv -1 \pmod{p}$

### Proof:

$(p - 1)! \equiv 1 \times 2 \times 3 \times \dots \times (p - 1) \pmod p$

Cancel out corresponding terms

$(p - 1)! \equiv 1 \times (p - 1) \pmod p$

$(p - 1)! \equiv -1 \pmod p$

---

#

### Wilson\'s theorem is a
## Primality Test!

(Although usually better methods are used)

#

---

## Motivation

# Insert table
# And put a bunch of values

---

## Theorem 7: Fermat\'s Little Theorem

If $\gcd(a, p) = 1$, $a^{p - 1} \equiv 1 \pmod p$

### Proof:

Consider the set
$S = \{1, 2, \dots, (p - 1)\}$

Multiply each of these numbers with $a$ and take $\% p$

$T = \{a \% p , 2a \% p, \dots, (p - 1)a \% p \}$

---

### Lemma: $S \rightarrow T$ is an injection

By contradiction, for $r, s \in S, r \ne s$

Consider $ar \% p$, $as \% p \in T$

Let $ar \% p = as \% p$

$\implies ar \equiv as \pmod p$

$\implies p | (r - s)$ (as $p \nmid a$)

$2 - p \le r - s \le p - 2$ $\implies \boxed{r - s = 0}$

---

## Theorem 7: Fermat\'s Little Theorem

If $\gcd(a, p) = 1$, $a^{p - 1} \equiv 1 \pmod p$

### Proof:

Number of elements in $S$ = Number of elements in $T$

If it\'s an injection, it\'s a bijection!

$\implies S \rightarrow T$ is a bijection

$\implies$ $S$ is a permutation of $T$

---

## Theorem 7: Fermat\'s Little Theorem

If $\gcd(a, p) = 1$, $a^{p - 1} \equiv 1 \pmod p$

### Proof:

Product of all elements in $S$ = Product of all elements in $T$

$1 \times 2 \times \dots \times (p - 1) \equiv a \times 2a \times \dots \times (p - 1)a \mod p$

$(p - 1)! \equiv a^{p - 1} (p - 1)! \pmod p$

$\gcd((p - 1)!, p) = 1$

By cancellation law, $1 \equiv a^{p - 1} \pmod p$

---

#
## Module 3
# Euler\'s Totient Function
# and Euler\'s Theorem
#

---

## Euler Totient Function $\varphi (n)$

$\varphi(n)$ is defined as the number of integers
coprime to and lesser than $n$

\textbf{Example: $\varphi(9)$}

Consider $1, 2, 3, 4, 5, 6, 7, 8$

Co-prime integers less than $9$:

$1, 2, \not 3, 4, 5, \not 6, 7, 8$

$\varphi(9) = 6$

---

## $\varphi(n)$ for some common numbers

- prime $\varphi(p) = p - 1$
- semiprime $\varphi(pq) = (p - 1)(q - 1)$

\textbf{Proof:}

Numbers \textit{not} co-prime to pq are numbers
divisible by p or q $\rightarrow p + q - 1$

$\phi(pq)$ would be $pq - (p + q - 1)$

- Exercise: Prove $\phi(n) = n \Pi_{p | n} \left (1 - \frac 1p \right )$

---

## Theorem 8: Euler\'s Theorem

If $\gcd(a, n) = 1$, $a^{\varphi(n)} \equiv 1 \pmod n$

### Example

Consider $n = 9, a = 4$

$S = \{1, 2, 4, 5, 7, 8\}$

Multiply each number by $4$ and take $\%9$

$T = \{4, 8, 7, 2, 1, 5\}$

Again, note that $S$ is a permutation of $T$

---

## Theorem 8: Euler\'s Theorem

If $\gcd(a, n) = 1$, $a^{\varphi(n)} \equiv 1 \pmod n$

### Example

Using a similar logic,

$1 \times 2 \times 4 \times \dots \times 8 \equiv (4 \times 1) (4 \times 2) (4 \times 4) \dots (4 \times 8) \pmod 9$

$1 \equiv 4^6 \pmod 9$

As a verification, $4^6 = 4096 \equiv 1 \pmod 9$

---

## Theorem 8: Euler\'s Theorem

If $\gcd(a, n) = 1$, $a^{\varphi(n)} \equiv 1 \pmod n$

### Proof is left as exercise!

- Consider the set $S$ of integers coprime to $n$ 
- Set $T \rightarrow$ multiply elements of $S$ by $a$ and $\%n$
- Prove that $T$ is a permutation of $S$
- Product of elements in $S$ = Product of elements in $T$
- Use cancellation law

---

## Theorem 8: Euler\'s Theorem

If $\gcd(a, n) = 1$, $a^{\varphi(n)} \equiv 1 \pmod n$

### Sidenote

If $n$ is prime, $\varphi(n) = n - 1$

If $\gcd(a, n) = 1$, $a^{n - 1} \equiv 1 \pmod n$

So Fermat\'s Little Theorem is a special case of 
Euler\'s theorem for prime $n$


---

#
## Module 4
# Two Hard
# Math and CS Problems
#

---

## Factoring Semiprimes

A semiprime is a product of two primes

Factorization is not hard,
it is actually trivial

The problem is that it is \textbf{inefficient}

All classical algorithms for factorizing primes
take a long time to run

---

## Factoring Semiprimes

- If 2019, Fabrice Boudot \textit{et al.} factored a 240-digit number
using 900 core-years of computing power

- In 2020, a 250 digit number was factorized
using 2700 core-years of computing power

- IITM\'s Computing Facilities put together would take 
few thousand years to factor big semiprimes

---

## Factoring Semiprimes

And the problem is worse

Say 100 years down the line,
we get much better computers

We can just use bigger semiprimes,
say 1000-digit semiprimes!

---

## Factoring Semiprimes

Say factoring 200-digit numbers takes
1000 years time

Factoring 1000-digit numbers does not
take 5000 years time

### It takes much more time!

---

## Naive algorithm for factorization

# Insert Python Code
# Sieve of Eratosthenes

---

## Sieve of Eratosthenes

#

Say we had a 250-digit number

Factoring it would take checking
upto 125-digit numbers

### Which is highly impractical!

#

---

## Discrete Logarithm Problem

Logarithm problem

$2^x = 3$, what is $x$?

Discrete Logarithm problem

$2^x = 3 \pmod 5$, what is $x$?

---

## Discrete Logarithm Problem

$\boxed{\alpha^x \equiv \beta \pmod p}$

Given $\alpha, \beta, p$, what is $x$?

Computing the discrete logarithm is hard
because there are no known efficient algorithms

---

#
## Module 5
# Introduction to
# Cryptology
#

---

## Motivation

Say Alice have a message m = 'Hello, world'

How can she send this to her friend Bob securely?

Her enemy Eve is listening across the line

She has to encrypt the message

---

## Motivation

# Insert Diagram of Above Communication line

---

## Motivation

### Example: Caesar Cipher

Julius Caesar used this to encrypt information

$\rightarrow$ Simple substitution cipher

# Insert table showing substitution, with shift 5

---

## Motivation

### Example: Caesar Cipher

Say message m = 'hello world'
The encypted message, c = e(m) = 'mjqqt btwqi'

# 

---

## Motivation

### Caesar Cipher Decryption

The encypted message, c = e(m) = 'mjqqt btwqi'

The decrypted message, d(c) = d(e(m)) = 'hello world'

Note that $d(e(m)) = m$ always

d(c) is the decryption function
e(m) is the encryption function

---

#

#

# Breaking the Caesar Cipher

One naive method: Brute Force

#

---

# Show python code
# demonstrating Brute Force

---

## Informal Definitions

- Cryptology: Science of Secure Communications
- Cryptography: Constructing protocols that prevent 
third-parties from reading messages
- Cryptanalysis: Breaching Cryptographic protocols
- Encryption: message m $\rightarrow$ encrypted message c
- Decryption: encrypted message c $\rightarrow$ message m
- Key: Something required to encrypt or decrypt m

---

## Symmetric Encryption

Alice and Bob know exactly the same things (keys)

They use that key to send messages between themselves

Caesar Cipher is a symmetric encryption
as both the sender and receiver know the
shift (5 in the previous case)

---

## Asymmetric Encryption

Alice and Bob know different things

They use that key to send messages

Examples: Coming up in session 2!

#

---

# Insert Flowchart
# of Cryptology

---

## Prime Number Generation

An Important requirement in cryptography
is generating large primes

- Generate a large random number
- Check if it is divisible by the first 100 primes
- Do a primality test like Miller-Rabin test

