package com.example.tools;

import dev.langchain4j.agent.tool.P;
import dev.langchain4j.agent.tool.Tool;

import java.util.logging.Logger;

public class TeachingTools {

    private static final Logger LOG = Logger.getLogger(TeachingTools.class.getName());

    @Tool("Add two numbers and return their sum.")
    public int add(@P(name = "a", description = "The first number to add") int a,
                   @P(name = "b", description = "The second number to add") int b) {
        LOG.info(() -> "TOOL add called with a=" + a + ", b=" + b);
        int result = a + b;
        LOG.info(() -> "TOOL add returned " + result);
        return result;
    }

    @Tool("Return a fixed demo temperature for a given city.")
    public String getTemperature(@P(name = "city", description = "The city to get the temperature for") String city) {
        LOG.info(() -> "TOOL getTemperature called with city=" + city);
        String result = "It is always 25 C in " + city + ".";
        LOG.info(() -> "TOOL getTemperature returned " + result);
        return result;
    }

    @Tool("Get weather for a given city.")
    public String getWeather(@P(name = "city", description = "The city to get the weather for") String city) {
        LOG.info(() -> "TOOL getWeather called with city=" + city);
        String result = "It's always sunny in " + city + "!";
        LOG.info(() -> "TOOL getWeather returned " + result);
        return result;
    }
}
