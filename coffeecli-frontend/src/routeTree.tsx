// src/routeTree.tsx

import { createRootRoute, createRoute, createRouter, Outlet } from "@tanstack/react-router";

// import your page components
import Home from "./routes/index";
import Login from "./routes/login";
import Recipes from "./routes/recipes";
import Favorites from "./routes/favorites";

// Root layout route
export const rootRoute = createRootRoute({
  component: RootLayout,
});

export default function RootLayout() {
  return (
    <div className="wave-bg min-h-screen bg-gradient-to-br from-zinc-900 via-orange-500 to-zinc-900 flex items-center justify-center overflow-hidden">
      {/* Animated background overlay */}
      <div className="absolute inset-0 animate-gradient-slow opacity-30"></div>

      {/* Terminal window */}
      <div className="relative z-10 w-[1400px] h-[900px] max-h-[90%] max-w-[90%] rounded-xl border border-zinc-700 bg-zinc-900/80 backdrop-blur-md shadow-2xl">
        {/* Top bar with macOS dots */}
        <div className="flex items-center justify-between border-b border-zinc-700 px-4 py-2">
          <div className="flex space-x-2">
            <div className="w-3 h-3 bg-red-500 rounded-full"></div>
            <div className="w-3 h-3 bg-yellow-500 rounded-full"></div>
            <div className="w-3 h-3 bg-green-500 rounded-full"></div>
          </div>
          <h1 className="text-orange-400 font-mono text-lg">☕ coffee@cli</h1>
        </div>

        {/* The main terminal area */}
      <main className="p-6 font-mono text-orange-400 text-sm flex justify-start items-start text-left h-[calc(100%-3rem)] w-full overflow-y-auto scrollbar-hide">
        <div className="h-full w-full">
          <Outlet />
        </div>
      </main>
      </div>
    </div>
  );
}

// Child routes
export const homeRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/",
  component: Home,
});

export const loginRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/login",
  component: Login,
});

export const recipesRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/recipes",
  component: Recipes,
});

export const favoritesRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/favorites",
  component: Favorites,
});

export const routeTree = rootRoute.addChildren([
  homeRoute,
  loginRoute,
  recipesRoute,
  favoritesRoute,
]);

export const router = createRouter({
  routeTree,
});