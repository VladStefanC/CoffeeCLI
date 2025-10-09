import { Help } from "./Help";
import { Recipes } from "./Recipes";
import Login from "./Login";
import Logout from "./Logout";
import { Register } from "./Register";
import { Favorites } from "./Favorites";
import { NotFound } from "./NotFound";

// This is a lookup table for terminal commands
export const COMMANDS: Record<string, React.FC> = {
  help: Help,
  recipes: Recipes,
  login: Login,
  logout : Logout,
  register: Register,
  favorites: Favorites,
  default: NotFound,
};