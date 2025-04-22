/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    let f = function() {
        return "Hello World";
        
    }
    return f;
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */