import api from "./api";

export async function getRecipes() {
    const response = await api.get("/recipes");
    return response.data;
}