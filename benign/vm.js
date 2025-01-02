const assert = require('assert');
const { VM } = require('vm2');

function runTest() {
    const vm2 = new VM();
    assert.throws(() => {
        vm2.run(`
            const proxiedErr = new Proxy({}, {
                getPrototypeOf(target) {
                    (function stack() {
                        new Error().stack;
                        stack();
                    })();
                }
            });
            try {
                throw proxiedErr;
            } catch ({ constructor: c }) {
                c.constructor('return process')();
            }
        `);
    }, /Maximum call stack size exceeded/, 'Expected a maximum call stack size exceeded error');
    console.log('Test passed');
}

runTest();
