
import { useEffect, useState, useMemo, useRef } from "react";
import api from "../../api/api";

interface Recipe {
  id: number;
  name: string;
  method: string;
  brew_time: string;
  steps: string;
}

export function Recipes() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState<Recipe | null>(null);
  const [selectedIndex, setSelectedIndex] = useState(0); // 👈 highlighted recipe index
  const listRef = useRef<HTMLUListElement | null>(null);

  const [filterName, setFilterName] = useState("");
  const [filterMethod, setFilterMethod] = useState("");
  const [filterTime, setFilterTime] = useState("");

  useEffect(() => {
    api
      .get("/recipes")
      .then((res) => setRecipes(res.data))
      .catch((err) => console.error("Error fetching recipes:", err))
      .finally(() => setLoading(false));
  }, []);

  function parseBrewTime(timeStr: string): number {
    if (!timeStr) return 0;
    const match = timeStr.match(/(\d+)(?::(\d+))?(-(\d+)(?::(\d+))?)?/);
    if (!match) return 0;
    const min = parseInt(match[1]) || 0;
    const sec = parseInt(match[2] || "0");
    const start = min + sec / 60;
    const endMin = parseInt(match[4] || match[1]) || 0;
    const endSec = parseInt(match[5] || "0");
    const end = endMin + endSec / 60;
    return (start + end) / 2;
  }

  const filteredRecipes = useMemo(() => {
    return recipes.filter((r) => {
      const matchName = r.name.toLowerCase().includes(filterName.toLowerCase());
      const matchMethod = r.method.toLowerCase().includes(filterMethod.toLowerCase());
      let matchTime = true;
      const timeValue = parseBrewTime(r.brew_time);
      if (filterTime === "short") matchTime = timeValue <= 5;
      if (filterTime === "medium") matchTime = timeValue > 5 && timeValue <= 10;
      if (filterTime === "long") matchTime = timeValue > 10;
      return matchName && matchMethod && matchTime;
    });
  }, [recipes, filterName, filterMethod, filterTime]);

  const handleSelectRecipe = async (id: number) => {
    try {
      const res = await api.get(`/recipes/${id}`, { withCredentials: true });
      setSelected(res.data);
    } catch (error) {
      console.error("Error fetching recipe details:", error);
    }
  };


  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!filteredRecipes.length) return;

      if (e.key === "ArrowDown") {
        e.preventDefault();
        setSelectedIndex((prev) => (prev + 1) % filteredRecipes.length);
      }

      if (e.key === "ArrowUp") {
        e.preventDefault();
        setSelectedIndex((prev) =>
          prev === 0 ? filteredRecipes.length - 1 : prev - 1
        );
      }

      if (e.key === "Enter") {
        const recipe = filteredRecipes[selectedIndex];
        if (recipe) handleSelectRecipe(recipe.id);
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [filteredRecipes, selectedIndex]);

  if (loading) return <div>Loading recipes...</div>;
  if (!recipes.length) return <div>No recipes found.</div>;

  return (
    <div className="text-left">
      <strong>☕ Filter Recipes:</strong>
      <div className="flex gap-2 mt-2 mb-4">
        <input
          type="text"
          placeholder="Filter by name..."
          value={filterName}
          onChange={(e) => setFilterName(e.target.value)}
          className="bg-zinc-900 border border-zinc-700 rounded px-2 py-1 text-orange-400"
        />
        <input
          type="text"
          placeholder="Filter by method..."
          value={filterMethod}
          onChange={(e) => setFilterMethod(e.target.value)}
          className="bg-zinc-900 border border-zinc-700 rounded px-2 py-1 text-orange-400"
        />
        <select
          value={filterTime}
          onChange={(e) => setFilterTime(e.target.value)}
          className="bg-zinc-900 border border-zinc-700 rounded px-2 py-1 text-orange-400"
        >
          <option value="">All times</option>
          <option value="short">≤ 3 min</option>
          <option value="medium">≤ 5 min</option>
          <option value="long">≥ 10 min</option>
        </select>
      </div>

      <strong>Available Coffee Recipes:</strong>
      <ul ref={listRef} className="list-disc ml-4 mt-2">
        {filteredRecipes.map((recipe, i) => (
          <li
            key={recipe.id}
            onClick={() => handleSelectRecipe(recipe.id)}
            className={`cursor-pointer ${
              i === selectedIndex ? "text-orange-300" : "hover:text-orange-400"
            }`}
          >
            <code>{recipe.name}</code> — {recipe.method} ({recipe.brew_time} min)
          </li>
        ))}
      </ul>

      {selected && selected.steps && (
        <div className="mt-4 border-t border-zinc-700 pt-2">
          <strong>Steps for {selected.name}:</strong>
          <ol className="list-decimal ml-6 mt-2">
            {selected.steps
              .split(/[.,\n]/)
              .filter((s) => s.trim() !== "")
              .map((step: string, idx: number) => (
                <li key={idx}>{step.trim()}</li>
              ))}
          </ol>
        </div>
      )}
    </div>
  );
}