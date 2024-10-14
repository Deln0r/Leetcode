package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Name struct {
	fname string // Имя
	lname string // Фамилия
}

func main() {
	var filename string
	fmt.Print("Введите имя текстового файла: ")
	fmt.Scan(&filename)

	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Ошибка при открытии файла:", err)
		return
	}
	defer file.Close()

	var names []Name

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) < 2 {
			fmt.Println("Неверный формат строки:", line)
			continue
		}
		name := Name{
			fname: parts[0],
			lname: parts[1],
		}
		names = append(names, name)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Ошибка при чтении файла:", err)
		return
	}

	fmt.Println("Считанные имена и фамилии:")
	for _, name := range names {
		fmt.Printf("Имя: %s, Фамилия: %s\n", name.fname, name.lname)
	}
}
