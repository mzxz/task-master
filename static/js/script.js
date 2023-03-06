function validate(input){
    if(/^\s/.test(input.value))
        input.value = '';
}


module.exports = validate;