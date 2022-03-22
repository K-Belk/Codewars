function wave(str){
    let result = []
    for(let i = 0; i < str.length; i++) {
      if(str[i] != ' ') {
        let build = str.split('')
        build[i] = build[i].toUpperCase()
        build = build.join('')
        result.push(build)
      }
    }
    return result
  }

  wave("hello") // ["Hello", "hEllo", "heLlo", "helLo", "hellO"]