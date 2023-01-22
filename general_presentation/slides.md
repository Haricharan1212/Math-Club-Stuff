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

#
# Exercise: 
#
## Write code in a programming language
## that implements GCD
#

---

## Euclid\'s Division Algorithm

Aim: find $\gcd(5, 14)$

$14 = 5 \times 2 + 4$ 

$5 = 4 \times 1 + 1$

$4 = 1 \times 4 + 0$

$\boxed{\gcd(5, 14) = 1}$

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