package com.example.tools;

import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.SystemMessage;

public class ToolCallingAgentExample {

    public interface TeachingAssistant {

        @SystemMessage("You are a teaching assistant. Use the provided tools whenever the user "
                + "asks for a sum, a temperature, or the weather. Call every relevant tool "
                + "and include all of the results in your final answer.")
        String chat(String userMessage);
    }

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-flash")
                .build();

        TeachingAssistant assistant = AiServices.builder(TeachingAssistant.class)
                .chatModel(model)
                .tools(new Tools())
                .build();

        String question = "Using your tools: add 7 and 5, tell me the temperature in Tehran, "
                + "and get the weather in Paris. Report all three results.";
        System.out.println("User: " + question);
        System.out.println("Assistant: " + assistant.chat(question));
    }
}
