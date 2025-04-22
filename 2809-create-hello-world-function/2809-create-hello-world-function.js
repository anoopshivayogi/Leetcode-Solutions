/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    let f = function hello() {
        return "Hello World";
        
    }
    return f;
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */