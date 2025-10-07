import axios from "axios";
import {useEffect, useState} from "react";


export function Recipes() {
    const [recipes, setRecipes] = useState<{id: number; name: string; method: string }[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('http://localhost:8000/recipes')
        .then(res => setRecipes(res.data))
        .catch(err => console.error("Error fetching recipes:", err))
        .finally(() => setLoading(false));
    }, []);

    if (loading) return <div>Loading recipes...</div>;
    if (!recipes.length) return <div>No recipes found.</div>;

    return (
        <div>
            <strong>Available Coffee Recipes:</strong>
            <ul className="list-disc ml-4 mt-2">
                {recipes.map(recipe => (
                    <li key={recipe.id}>
                        <code>{recipe.name}</code> - <span>{recipe.method}</span>
                    </li>
                ))}
            </ul>
        </div>
    );
}
