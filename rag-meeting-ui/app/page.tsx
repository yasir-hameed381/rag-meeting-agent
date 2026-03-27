import ChatBox from "./components/ChatBox";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 to-white p-6">
      <div className="mx-auto mb-6 w-full max-w-3xl">
        <h1 className="text-3xl font-semibold tracking-tight text-slate-900">
          AI Meeting Assistant
        </h1>
        <p className="mt-2 text-sm text-slate-600">
          Ask questions or book meetings in one chat.
        </p>
      </div>
      <ChatBox />
    </main>
  );
}
