import React, { useState, useRef, useEffect, type JSX } from "react";
import { COMMANDS } from "./commands";
import { useAuth } from "../context/AuthContext";
import { useTypingEffect } from "../hooks/useTypingEffect";



interface Line {
  type: "input" | "output";
  text: string | JSX.Element;
}

export default function Terminal() {
  const { user } = useAuth();

  const promptName = user?.username || "guest";
  const animatedPrompt = useTypingEffect(promptName,150)

  const [lines, setLines] = useState<Line[]>([
    { type: "output", text: "Welcome to CoffeeCLI ☕" },
    { type: "output", text: "Type 'help' to get started." },
  ]);
  const [input, setInput] = useState("");
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const bottomRef = useRef<HTMLDivElement>(null);

  // Scrolls to bottom when new lines appear
  
  useEffect(() => {
    const bottom = bottomRef.current;
    const behavior = lines.length > 0 ? "smooth" : "auto";

    if (bottom) {
      requestAnimationFrame(() => {
        bottom.scrollIntoView({ behavior, block: "end" });
      });
    }
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
      { type: "input", text: `${promptName}@coffeecli:~$ ${cmd}` },
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
      ref={scrollContainerRef}
    >
       
      <div className="flex flex-col min-h-full justify-end">
        {lines.map((line, i) => (
          <div key={i}>{line.text}</div>
        ))}
        
        <div className="flex mt-2">
          
          <span className="text-orange-400">
            {user ? (
              <span className="text-green-400">{animatedPrompt}</span>
            ) : ( 
              <span className="text-zinc-500">quest</span>
            )}
            @coffeecli:~$
          </span>


         
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={onKeyDown}
            className="bg-transparent text-orange-400 outline-none w-full caret-orange-400"
            autoFocus
          />
        </div>
        <div ref={bottomRef} />
      </div>
     
    </div>
    
  );
}
