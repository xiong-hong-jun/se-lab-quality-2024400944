package com.example.calculator;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication
public class CalculatorProjectApplication {

    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(CalculatorProjectApplication.class, args);

        // 测试 Calculator 是否被 Spring 管理
        Calculator calculator = context.getBean(Calculator.class);
        System.out.println("2 + 3 = " + calculator.add(2, 3));
        System.out.println("6 / 2 = " + calculator.divide(6, 2));
    }
}