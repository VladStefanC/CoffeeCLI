import { Help } from "./Help";
import { Recipes } from "./Recipes";
import Login from "./Login";
import { Register } from "./Register";
import { Favorites } from "./Favorites";
import { NotFound } from "./NotFound";

// This is a lookup table for terminal commands
export const COMMANDS: Record<string, React.FC> = {
  help: Help,
  recipes: Recipes,
  login: Login,
  register: Register,
  favorites: Favorites,
  default: NotFound,
};