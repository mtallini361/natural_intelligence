# Definition 2.7 (Group)

Consider a set $G$ and an operation $\otimes : G \times G \to G$ defined on $G$. Then $G := (G, \otimes)$ is called a **group** if the following hold:

1. **Closure** of $G$ under $\otimes$: for all $x, y \in G$, we have $x \otimes y \in G$
2. **Associativity**: For all $x, y, z \in G$, we have $(x \otimes y) \otimes z = x \otimes (y \otimes z)$
3. **Neutral element**: There exists an element $e \in G$ such that for all $x \in G$, we have $x \otimes e = x$ and $e \otimes x = x$
4. **Inverse element**: For all $x \in G$, there exists a $y \in G$ such that $x \otimes y = e$ and $y \otimes x = e$, where $e$ is the neutral element. We often write $x^{-1}$ to denote the inverse element of $x$.

**Abelian group**: If additionally $\forall x, y \in G : x \otimes y = y \otimes x$, then $G = (G, \otimes)$ is an **Abelian group** (commutative).

---

## Exercise 2.1

We consider $(\mathbb{R} \setminus \{-1\}, \star)$, where

$$a \star b := ab + a + b, \quad a, b \in \mathbb{R} \setminus \{-1\} \tag{2.134}$$

### a. Show that $(\mathbb{R} \setminus \{-1\}, \star)$ is an Abelian group.

Assume for contradiction that $(\mathbb{R} \setminus \{-1\}, \star)$ is *not* Abelian — i.e., there exist $a, b \in \mathbb{R} \setminus \{-1\}$ such that $a \star b \neq b \star a$:

$$ab + a + b \neq ba + b + a$$
$$ab \neq ba$$

This is a contradiction since multiplication of real numbers is commutative. Therefore $(\mathbb{R} \setminus \{-1\}, \star)$ is an Abelian group. $\blacksquare$

### b. Solve $3 \star x \star x = 15$ in $(\mathbb{R} \setminus \{-1\}, \star)$

$$3 \star x \star x = 15$$
$$(3 \star x) \star x = 15$$
$$(3x + 3 + x) \star x = 15$$
$$(4x + 3) \star x = 15$$
$$(4x + 3)x + (4x + 3) + x = 15$$
$$4x^2 + 3x + 4x + 3 + x = 15$$
$$4x^2 + 8x + 3 = 15$$
$$4x^2 + 8x - 12 = 0$$
$$x^2 + 2x - 3 = 0$$
$$(x + 3)(x - 1) = 0$$

$$\boxed{x = -3 \quad \text{or} \quad x = 1}$$

---

## Exercise 2.2

Let $n \in \mathbb{N} \setminus \{0\}$. Let $k, x \in \mathbb{Z}$. We define the **congruence class** $\bar{k}$ of the integer $k$ as the set

$$\bar{k} = \{x \in \mathbb{Z} \mid x - k = 0 \pmod{n}\}$$
$$= \{x \in \mathbb{Z} \mid \exists\, a \in \mathbb{Z} : (x - k = n \cdot a)\}$$

We now define $\mathbb{Z}/n\mathbb{Z}$ (sometimes written $\mathbb{Z}_n$) as the set of all congruence classes modulo $n$. Euclidean division implies that this set is a finite set containing $n$ elements:

$$\mathbb{Z}_n = \{\bar{0}, \bar{1}, \ldots, \overline{n-1}\}$$

For all $a, b \in \mathbb{Z}_n$, we define

$$a \oplus b := \overline{a + b}$$

### a. Show that $(\mathbb{Z}_n, \oplus)$ is a group. Is it Abelian?

Assume $(\mathbb{Z}_n, \oplus)$ is not a group

Assume $(\mathbb{Z}_n, \oplus)$ is not closed under $\mathbb{Z}_n$ 

- if $\overline{a}$ and $\overline{b}$ are elements of $\mathbb{Z}_n$ then a and b are elements of $\mathbb{Z}$

- if a and b are elements of $\mathbb{Z}$ and + is closed under $\mathbb{Z}$ then a + b is an element of $\mathbb{Z}$

- if a + b is an element of $\mathbb{Z}$ then $\overline{a + b}$ is an element of $\mathbb{Z}_n$

- This contradicts our assumption that $\overline{a + b}$ is not an element of $\mathbb{Z}$

Assume $(\mathbb{Z}_n, \oplus)$ is not Associative

- if $\overline{a}$, $\overline{b}$, $\overline{c}$ then $\overline{a + b}$ $\oplus$ $\overline{c}$ &ne; $\overline{a}$ $\oplus$ $\overline{b + c}$

- if a, b, c $\in$ $\mathbb{Z}$ and + is closed under $\mathbb{Z}$ then x, y $\in$ $\mathbb{Z}$ where x = a + b and y = b + c

- if x, y $\in$ $\mathbb{Z}$ then  $\overline{x}$ $\oplus$ $\overline{c}$ &ne; $\overline{a}$ $\oplus$ $\overline{y}$

- if $\overline{x}$ $\oplus$ $\overline{c}$ &ne; $\overline{a}$ $\oplus$ $\overline{y}$ then $\overline{x + c}$ &ne; $\overline{a + y}$

- if $\overline{x + c}$ &ne; $\overline{a + y}$ then $\overline{(a + b) + c}$ &ne; $\overline{a + (b + c)}$

- if + is closed under $\mathbb{Z}$ then $\overline{(a + b) + c}$ &ne; $\overline{a + (b + c)}$ is equivalent to $\overline{a + b + c}$ &ne; $\overline{a + b + c}$

- this contradicts our assumption that $(\mathbb{Z}_n, \oplus)$ is not Associative

### b. We now define another operation $\otimes$ for all $a$ and $b$ in $\mathbb{Z}_n$ as

$$a \otimes b = \overline{a \times b} \tag{2.135}$$

where $a \times b$ represents the usual multiplication in $\mathbb{Z}$.

Let $n = 5$. Draw the times table of the elements of $\mathbb{Z}_5 \setminus \{\bar{0}\}$ under $\otimes$, i.e., calculate the products $a \otimes b$ for all $a$ and $b$ in $\mathbb{Z}_5 \setminus \{\bar{0}\}$.

Hence, show that $\mathbb{Z}_5 \setminus \{\bar{0}\}$ is closed under $\otimes$ and possesses a neutral element for $\otimes$. Display the inverse of all elements in $\mathbb{Z}_5 \setminus \{\bar{0}\}$ under $\otimes$. Conclude that $(\mathbb{Z}_5 \setminus \{\bar{0}\}, \otimes)$ is an Abelian group.

### c. Show that $(\mathbb{Z}_8 \setminus \{\bar{0}\}, \otimes)$ is not a group.

### d. We recall that the Bézout theorem states that two integers $a$ and $b$ are relatively prime (i.e., $\gcd(a, b) = 1$) if and only if there exist two integers $u$ and $v$ such that $au + bv = 1$. Show that $(\mathbb{Z}_n \setminus \{\bar{0}\}, \otimes)$ is a group if and only if $n \in \mathbb{N} \setminus \{0\}$ is prime.
