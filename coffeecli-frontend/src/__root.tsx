import { Outlet, Link, createRootRoute } from "@tanstack/react-router";

export const Route = createRootRoute({
  component: RootLayout,
});

function RootLayout() {
  return (
    <div className="min-h-screen bg-zinc-950 text-white">
      <nav className="p-4 border-b border-zinc-700 flex justify-between items-center">
        <h1 className="text-2xl font-mono text-emerald-400">☕ CoffeeCLI</h1>
        <div className="space-x-4">
        <Link to="/">Home</Link>
        <Link to="/recipes">Recipes</Link>
        <Link to="/favorites">Favorites</Link>
        <Link to="/login">Login</Link>
        </div>
      </nav>

      <main className="p-8 font-mono">
        <Outlet /> {/* Children routes render here */}
      </main>
    </div>
  );
}