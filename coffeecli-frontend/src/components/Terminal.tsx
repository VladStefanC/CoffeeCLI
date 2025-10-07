import React, { useState, useRef, useEffect, type JSX, use } from "react";
import { COMMANDS } from "./commands";



interface Line {
  type: "input" | "output";
  text: string | JSX.Element;
}

export default function Terminal() {
  const [lines, setLines] = useState<Line[]>([
    { type: "output", text: "Welcome to CoffeeCLI ☕" },
    { type: "output", text: "Type 'help' to get started." },
  ]);
  const [input, setInput] = useState("");
  const terminalEndRef = useRef<HTMLDivElement>(null);

  // Scrolls to bottom when new lines appear
  /*
  useEffect(() => {
    const el = terminalEndRef.current;
    if (!el || !el.parentElement) return;

    requestAnimationFrame(() => {
      el.parentElement.scrollTo({
        top: el.parentElement.scrollHeight,
        behavior: lines.length > 0 ? "smooth" : "auto",
      });
    });
  }, [lines]);*/

  useEffect(() => {
    terminalEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [lines]);




  /* Handles command input */
  const handleCommand = (cmd: string) => {
    const trimmed = cmd.toLowerCase().trim();

    if (trimmed === "clear") {
      setLines([]);
      return;
    }

    const CommandComponent = COMMANDS[trimmed] || COMMANDS["default"];

    setLines((prev) => [ 
      ...prev,
      { type: "input", text: `coffee@cli:~$ ${cmd}` },
      { type: "output", text: <CommandComponent />  }, 
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
      className="relative font-mono text-orange-400 p-6 text-left flex-grow w-full overflow-y-auto scrollbar-hide"
      style={{ whiteSpace: "pre-wrap" }}
      ref={terminalEndRef}
    >
      <div className="flex flex-col min-h-full justify-end">
        {lines.map((line, i) => (
          <div key={i}>{line.text}</div>
        ))}
        
        <div className="flex mt-2">
          <span className="text-orange-500">coffee@cli:~$&nbsp;</span>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={onKeyDown}
            className="bg-transparent text-orange-400 outline-none w-full caret-orange-400"
            autoFocus
          />
        </div>
      </div>
      <div ref={terminalEndRef} />
    </div>
  );
}
