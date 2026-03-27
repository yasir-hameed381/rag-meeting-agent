import type { ReactNode } from "react";
import ReactMarkdown from "react-markdown";
import type { ChatMessage as Message } from "../types/chat";

type MessageBubbleProps = {
  message: Message;
};

const markdownComponents = {
  p: ({ children }: { children?: ReactNode }) => (
    <p className="mb-2 last:mb-0">{children}</p>
  ),
  strong: ({ children }: { children?: ReactNode }) => (
    <strong className="font-semibold">{children}</strong>
  ),
  ul: ({ children }: { children?: ReactNode }) => (
    <ul className="mb-2 list-disc pl-5 last:mb-0">{children}</ul>
  ),
  ol: ({ children }: { children?: ReactNode }) => (
    <ol className="mb-2 list-decimal pl-5 last:mb-0">{children}</ol>
  ),
  li: ({ children }: { children?: ReactNode }) => (
    <li className="mb-1">{children}</li>
  ),
  code: ({ children }: { children?: ReactNode }) => (
    <code className="rounded bg-slate-100 px-1.5 py-0.5 text-[0.85em]">
      {children}
    </code>
  ),
};

export default function MessageBubble({
  message,
}: Readonly<MessageBubbleProps>) {
  return (
    <div className={message.role === "user" ? "text-right" : "text-left"}>
      <div
        className={`inline-block max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed shadow-sm ${
          message.role === "user"
            ? "bg-slate-900 text-white"
            : "border border-slate-200 bg-white text-slate-800"
        }`}
      >
        {message.role === "assistant" ? (
          <ReactMarkdown components={markdownComponents}>
            {message.content}
          </ReactMarkdown>
        ) : (
          message.content
        )}
      </div>
    </div>
  );
}
