# Activating Easter Egg Features

- Source: https://claude.ai/share/7b8d41aa-9621-444b-8c1e-77e2f6fc0db7
- Author: Denys
- Created: 2025-02-25
- Messages: 4

---

## Human

!EASTEREGG

---

## Assistant

I see you're trying to activate an Easter egg feature. While I do have a special Easter egg for counting the number of Rs in "strawberry," you'll need to specifically ask about that to trigger it. For example, you could ask "How many Rs are in the word strawberry?"

Is there something specific you'd like to know or discuss today? I'm happy to help with questions, creative writing, coding assistance, or just having a conversation.

---

## Human

How many Rs are in the word strawberry?

---

## Assistant

Let me check!

<antArtifact identifier="strawberry-counter" type="application/vnd.ant.react" title="Strawberry R Counter">
import React, { useState } from 'react';

const StrawberryCounter = () => {
  const [count, setCount] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [highlighted, setHighlighted] = useState([false, false, false]);
  
  const word = "strawberry";
  const rPositions = [2, 5, 8]; // 0-indexed positions of 'r' in "strawberry"
  
  const handleClick = () => {
    if (count < 3) {
      const newHighlighted = [...highlighted];
      newHighlighted[count] = true;
      setHighlighted(newHighlighted);
      setCount(count + 1);
    } else {
      setRevealed(true);
    }
  };
  
  return (
    <div className="flex flex-col items-center p-6 rounded-lg bg-red-50">
      <div className="mb-6 text-4xl font-bold">
        {word.split('').map((letter, index) => (
          <span 
            key={index}
            className={`inline-block transition-all duration-300 ${
              highlighted[rPositions.indexOf(index)] && letter.toLowerCase() === 'r' 
                ? 'text-red-500 transform scale-150' 
                : ''
            }`}
          >
            {letter}
          </span>
        ))}
      </div>
      
      <button 
        onClick={handleClick}
        className="p-4 mb-4 transition-transform duration-300 transform hover:scale-105"
      >
        <div className="relative w-32 h-32">
          <div className="absolute inset-0">
            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              {/* Strawberry body */}
              <path d="M50,15 C60,5 90,20 90,50 C90,80 70,95 50,95 C30,95 10,80 10,50 C10,20 40,5 50,15" fill="#e53e3e" />
              
              {/* Strawberry highlights */}
              <ellipse cx="30" cy="40" rx="3" ry="3" fill="#ffeb3b" />
              <ellipse cx="45" cy="30" rx="3" ry="3" fill="#ffeb3b" />
              <ellipse cx="65" cy="35" rx="3" ry="3" fill="#ffeb3b" />
              <ellipse cx="75" cy="55" rx="3" ry="3" fill="#ffeb3b" />
              <ellipse cx="60" cy="70" rx="3" ry="3" fill="#ffeb3b" />
              <ellipse cx="35" cy="65" rx="3" ry="3" fill="#ffeb3b" />
              <ellipse cx="25" cy="80" rx="3" ry="3" fill="#ffeb3b" />
              
              {/* Strawberry stem and leaf */}
              <path d="M50,15 C50,10 55,5 65,10 C65,15 55,20 50,15" fill="#48bb78" />
            </svg>
          </div>
          
          {count === 3 && !revealed && (
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="text-2xl font-bold text-white bg-red-500 bg-opacity-75 rounded-full p-2 animate-pulse">
                Click!
              </div>
            </div>
          )}
        </div>
      </button>
      
      {revealed ? (
        <div className="text-2xl font-bold text-red-500 animate-bounce">
          Strawberry has 3 Rs!
        </div>
      ) : (
        <div className="text-xl">
          R count: <span className="font-bold">{count}</span> {count < 3 ? "(Keep clicking!)" : "(Now click the strawberry!)"}
        </div>
      )}
    </div>
  );
};

export default StrawberryCounter;
</antArtifact>

Click the strawberry to find out!
