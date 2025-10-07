import api from "./axios";

export async function getRecipes() {
    const response = await api.get("/recipes");
    return response.data;
}