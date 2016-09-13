function render(template, data) {
    var patt = /\{([^}]+)\}/g; // matches {key}
    return template.replace(patt, function(_, key) {
                            return data[key];
                            });
}