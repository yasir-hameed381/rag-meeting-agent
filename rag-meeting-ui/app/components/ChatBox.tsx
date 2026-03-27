"use client";

import { useMemo, useState } from "react";
import type { ChatMessage as Message } from "../types/chat";
import MessageBubble from "./MessageBubble";

type UiMessage = Message & { id: string };

export default function ChatBox() {
  const [messages, setMessages] = useState<UiMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const canSend = useMemo(
    () => input.trim().length > 0 && !loading,
    [input, loading],
  );

  const buildMessage = (role: Message["role"], content: string): UiMessage => ({
    id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    role,
    content,
  });

  const sendMessage = async () => {
    if (!canSend) return;
    const question = input.trim();

    const userMessage = buildMessage("user", question);

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data?.error || "Unable to get a response right now.");
      }

      const botMessage = buildMessage(
        "assistant",
        data.answer || "No response",
      );

      setMessages((prev) => [...prev, botMessage]);
    } catch {
      setMessages((prev) => [
        ...prev,
        buildMessage("assistant", "❌ Error connecting to server"),
      ]);
    }

    setLoading(false);
  };

  return (
    <section className="mx-auto w-full max-w-3xl overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
      <header className="border-b border-slate-100 px-5 py-4">
        <p className="text-sm font-medium text-slate-800">Meeting Chat</p>
        <p className="mt-1 text-xs text-slate-500">
          Try: "Book a meeting tomorrow at 3 PM"
        </p>
      </header>

      <div className="h-[520px] space-y-3 overflow-y-auto bg-slate-50/70 px-5 py-4">
        {messages.map((msg) => (
          <MessageBubble key={msg.id} message={msg} />
        ))}

        {loading && <p className="text-sm text-slate-500">Thinking...</p>}
        {!messages.length && !loading && (
          <p className="text-sm text-slate-500">
            Start with a meeting request like "Book tomorrow at 3 PM".
          </p>
        )}
      </div>

      <form
        className="flex gap-2 border-t border-slate-100 bg-white p-4"
        onSubmit={(event) => {
          event.preventDefault();
          void sendMessage();
        }}
      >
        <input
          className="flex-1 rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-sm text-slate-900 outline-none transition focus:border-slate-900 focus:ring-2 focus:ring-slate-200"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask or book a meeting..."
          disabled={loading}
          aria-label="Message input"
        />
        <button
          type="submit"
          disabled={!canSend}
          className="rounded-xl bg-slate-900 px-5 py-2.5 text-sm font-medium text-white transition hover:bg-slate-800 disabled:cursor-not-allowed disabled:bg-slate-300"
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </form>
    </section>
  );
}
