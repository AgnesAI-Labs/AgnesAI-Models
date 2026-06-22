import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AGNES_API_KEY,
  baseURL: "https://apihub.agnes-ai.com/v1",
});

const response = await client.chat.completions.create({
  model: "agnes-2.0-flash",
  messages: [
    {
      role: "user",
      content: "Write a short checklist for testing an API integration.",
    },
  ],
});

console.log(response.choices[0].message.content);

