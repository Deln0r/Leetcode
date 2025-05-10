import React, { useState } from "react";

function SearchBar() {
    const [query, setQuery] = useState("");
    const fruits = ["apple", "banana", "cherry", "mango", "blueberry"];
    const results = fruits.filter((fruit) =>
        fruit.toLowerCase().includes(query.toLowerCase())
    );

    return (
        <div>
            <h1>Fruit Search</h1>

            <input
                type="text"
                value={query}
                placeholder="Search for a fruit"
                onChange={(e) => setQuery(e.target.value)}
            />

            <ul>
                {results.length > 0 ? (
                    results.map((fruit) => (
                        <li key={fruit}>{fruit}</li>
                    ))
                ) : (
                    <li>No results found</li>
                )}
            </ul>
        </div>
    )
}

export default SearchBar;