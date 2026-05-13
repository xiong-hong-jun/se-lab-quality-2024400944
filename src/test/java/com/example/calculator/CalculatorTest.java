package com.example.calculator;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {

    private Calculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }

    // ========== 传统测试部分 ==========

    @Test
    void testAdd() {
        assertEquals(5, calculator.add(2, 3));
        assertEquals(0, calculator.add(-1, 1));
        assertEquals(0, calculator.add(0, 0));
        assertEquals(-5, calculator.add(-2, -3));
    }

    @Test
    void testSubtract() {
        assertEquals(2, calculator.subtract(5, 3));
        assertEquals(-5, calculator.subtract(0, 5));
        assertEquals(10, calculator.subtract(10, 0));
        assertEquals(-8, calculator.subtract(-5, 3));
    }

    @Test
    void testMultiply() {
        assertEquals(6, calculator.multiply(2, 3));
        assertEquals(-6, calculator.multiply(-2, 3));
        assertEquals(0, calculator.multiply(0, 5));
        assertEquals(6, calculator.multiply(-2, -3));
    }

    // ========== TDD 实现除法部分 ==========

    @Test
    void testDivideNormal() {
        assertEquals(3.0, calculator.divide(6, 2));
        assertEquals(2.5, calculator.divide(5, 2));
        assertEquals(-3.0, calculator.divide(-6, 2));
        assertEquals(0.0, calculator.divide(0, 5));
    }

    @Test
    void testDivideByZero() {
        // 验证除数为0时抛出 IllegalArgumentException
        IllegalArgumentException exception = assertThrows(
                IllegalArgumentException.class,
                () -> calculator.divide(1, 0)
        );
        assertEquals("Cannot divide by zero", exception.getMessage());

        // 另一种写法
        assertThrows(IllegalArgumentException.class, () -> calculator.divide(100, 0));
    }
}