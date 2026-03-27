import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const { question } = await request.json();
    if (!question || typeof question !== "string") {
      return NextResponse.json(
        { error: "question is required" },
        { status: 400 },
      );
    }

    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();
    if (!response.ok) {
      return NextResponse.json(
        { error: data?.detail || "Backend chat request failed." },
        { status: response.status },
      );
    }

    return NextResponse.json({ answer: data.response });
  } catch {
    return NextResponse.json(
      { error: "Failed to process chat request." },
      { status: 500 },
    );
  }
}
