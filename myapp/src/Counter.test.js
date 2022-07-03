import { render, screen, fireEvent } from '@testing-library/react';
import { Counter } from "./Counter";

describe('Counter Test', () => {
    it('matches snapshot', () => {
        render(<Counter />);
        screen.getByText('0');
    });

    it('shows the props correctly', () => {
        render(<Counter />);
        const number = screen.getByText('0');
        const plus = screen.getByText("+");
        const minus = screen.getByText("-");

        fireEvent.click(plus);
        expect(number).toHaveTextContent('1');

        fireEvent.click(minus);
        fireEvent.click(minus);
        fireEvent.click(minus);
        expect(number).toHaveTextContent('-2');
    });
});