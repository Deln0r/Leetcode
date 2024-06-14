Нужно описать модель библиотеки. Есть 3 сущности: "Автор", "Книга", "Читатель"

Физически книга только одна и может быть только у одного читателя. Нужно составить таблицы для библиотеки так что бы это учесть.











Есть таблица на 1 миллиард записей, которая активно используется в продашкне. Нужно сделать датафикс, который модифицирует 10 миллионов строк. Как бы ты подошел к решению задачи?




CREATE TABLE Author (
    Author_ID INT PRIMARY KEY,
    Name VARCHAR(255)
);

CREATE TABLE Book (
    Book_ID INT PRIMARY KEY,
    Title VARCHAR(255),
    Reader_ID INT,
    FOREIGN KEY (Reader_ID) REFERENCES Reader(Reader_ID),
);

CREATE TABLE Reader (
    Reader_ID INT PRIMARY KEY,
    Name VARCHAR(255)
);

CREATE TABLE Book_Author (
    Book_ID INT,
    Author_ID INT,
    PRIMARY KEY (Book_ID, Author_ID),
    FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID),
    FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID)
);

-- Написать запрос - выбрать названия всех книг которые на руках
SELECT Book.Title
FROM Book
WHERE Book.Reader_ID IS NOT NULL;



-- Написать запрос - выбрать названия всех книг в библиотеке у которых больше 3 авторов



SELECT b.Title
FROM Book b
JOIN Book_Author ba ON b.Book_ID = ba.Book_ID
GROUP BY b.Book_ID
HAVING COUNT(ba.Author_ID) > 3;


-- Написать запрос - выбрать имена топ 3 читаемых авторов на данный момент

SELECT a.Name, COUNT(b.BOOK_ID) AS NUM_BOOKS
FROM Author a
JOIN Book_Author ba ON a.Author_ID = ba.Author_ID
JOIN Book b ON ba.Book_ID = b.Book_ID
WHERE b.Reader_ID IS NOT NULL
GROUP BY a.Author_ID
ORDER BY NUM_BOOKS DESC
LINIT 3;



Дана закодированная строка следующего формата: k[encoded_text]
Здесь k это число повторений строки encoded_text.

Строка гарантированно имеет корректный формат: нет лишних пробелов, скобки всегда правильные и тд.

Необходимо декодировать строку

Input:  "3[a]2[bc]"
Output: "aaabcbc"

Input:  "3[a2[c]]"
Output: "accaccacc"

Input:  "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

def decode_string (s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char = "[":
            stack.append(current_string)
            stack.append(current_number)
            current_string = ""
            current_number = 0
        elif char = "]":
            num = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + num * current_string
        else:
            current_string += char
    return current_string

######################

Что выведет:
type X struct {
    V int
}

func (x X) S() {
    fmt.Println(x.V)
}

func main() {
    x := X{123}
    defer x.S()
    x.V = 456
}

########################

type Foo struct{}

func (f *Foo) A() {}
func (f *Foo) B() {}
func (f *Foo) C() {}

type AB interface {
	A()
	B()
}

type BC interface {
	B()
	C()
}

func main() {
	var f AB = &Foo{}
	y := f.(BC) // сработает ли такой type-assertion?
    y.A() // а этот вызов?
}


###################

Нужно написать простую библиотеку in-memory cache.
Для простоты считаем, что у нас бесконечная память и нам не нужно задумываться об удалении ключей из него.
Реализация должна удовлетворять интерфейсу:


type Cache interface {
    Set(k, v string)
    Get(k string) (v string, ok bool)
}

##
type Cache interface {
    Set (key string, value string)
    Get (key string) (v string, ok bool)
}

type InMemoryCache struct {
    cache map[string]string
    mux sync.RWMutex
}

func NewInMemoryCache() *InMemoryCache {
    return &InMemoryCache{
        cache: make(map[string]string)
    }
}

func (c *InMemoryCache) Set (key string, value string) {
    c.mux.Lock()
    defer c.mux.Unlock()
    c.cache[key] = value
}

func (c *InMemoryCache) Get (key string) (v string, ok bool) {
    c.mux.RLock()
    defer c.mux.RUnlock()
    value, exists := c.cache[key]
    return value, exists
}