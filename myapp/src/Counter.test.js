import { render, screen } from '@testing-library/react';
import { Counter } from "./Counter";

test('counter test', () => {
    render(<Counter />);
    const plus = screen.getByText("+");
    expect(plus).toBeInTheDocument();
});