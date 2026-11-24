package com.example;

import dev.langchain4j.model.chat.ChatModel;
import dev.langchain4j.model.openai.OpenAiChatModel;

public class DeepSeekExample {

    public static void main(String[] args) {
        ChatModel model = OpenAiChatModel.builder()
                .baseUrl("https://api.deepseek.com")
                .apiKey(System.getenv("DEEPSEEK_API_KEY"))
                .modelName("deepseek-chat")
                .build();

        System.out.println(model.chat("Say hello from DeepSeek in one sentence."));
    }
}
