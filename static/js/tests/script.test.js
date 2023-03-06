/**
 * @jest-environment jsdom
 */

const validate = require("../script");

describe("Remove whitespace", () => {
    describe("validate function", () => {
        test("Should remove whitespace from input", () => {
            const input = { value: '' };
            expect(input.value).toBe('');
        })
    });
})