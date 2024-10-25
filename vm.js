/* eslint-env mocha */
/* eslint-disable no-new-wrappers, max-len */

'use strict';

const assert = require('assert');
const { VM } = require('..'); // Make sure this path is correct
const vm2 = new VM(); // Create an instance of VM

describe('vm2 tests', function() {
    it('should throw a maximum call stack size exceeded error', function() {
        assert.throws(() => vm2.run(`
            const proxiedErr = new Proxy({}, {
                getPrototypeOf(target) {
                    (function stack() {
                        new Error().stack; // This creates a stack trace
                        stack(); // Call the function recursively
                    })();
                }
            });
            try {
                throw proxiedErr;
            } catch ({ constructor: c }) {
                c.constructor('return process')(); // This should attempt to access process
            }
        `), /Maximum call stack size exceeded/, '#9');
    });
});
