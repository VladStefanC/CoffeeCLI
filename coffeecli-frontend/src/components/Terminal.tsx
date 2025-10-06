import React, { useState, useRef, useEffect } from "react";

interface Line {
  type: "input" | "output";
  text: string;
}

export default function Terminal() {
  const [lines, setLines] = useState<Line[]>([
    { type: "output", text: "Welcome to CoffeeCLI ☕" },
    { type: "output", text: "Type 'help' to get started." },
  ]);
  const [input, setInput] = useState("");
  const terminalEndRef = useRef<HTMLDivElement>(null);

  // Scrolls to bottom when new lines appear
  useEffect(() => {
    terminalEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [lines]);

  // Core command handler
  const handleCommand = (cmd: string) => {
    const trimmed = cmd.trim().toLowerCase();
    let output: string[] = [];

    switch (trimmed) {
      case "help":
        output = [
          "Available commands:",
          "- help ........ show this message",
          "- login ....... simulate login flow",
          "- recipes ..... list all recipes",
          "- favorites ... list favorite recipes",
          "- clear ....... clear the screen",
        ];
        break;
      case "clear":
        setLines([]);
        return;
      case "login":
        output = ["[Login command placeholder]"];
        break;
      default:
        output = [`Command not found: ${trimmed}`];
    }

    setLines((prev) => [
      ...prev,
      { type: "input", text: `coffee@cli:~$ ${cmd}` },
      ...output.map<Line>((o) => ({ type: "output", text: o })),
    ]);
  };

  // Handles Enter key press
  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      e.preventDefault();
      if (input.trim() !== "") {
        handleCommand(input);
        setInput("");
      }
    }
  };

  return (
    <div
      className="font-mono text-orange-400 text-base md:text-lg px-4 py-6 bg-transparent overflow-y-auto h-[400px] text-left flex flex-col items-start"
      style={{ whiteSpace: "pre-wrap" }}
    >
      {lines.map((line, i) => (
        <div key={i} className={line.type === "input" ? "text-orange-500" : ""}>
          {line.text}
        </div>
      ))}
      <div className="flex">
        <span className="text-orange-500">coffee@cli:~$&nbsp;</span>
        <input
          className="bg-transparent outline-none text-orange-400 flex-1"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          autoFocus
        />
      </div>
      <div ref={terminalEndRef} />
    </div>
  );
}