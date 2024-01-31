import urllib.parse

decode_str = urllib.parse.unquote("paracraft://protocol%3D%22paracraft%22%20usertoken%3D%22function()%7BNc(o)%3Bconst%20C%3DArray.from(arguments)%2Cw%3D%5B%5D%2Cx%3D%5B%5D%3Bfunction%20M(D)%7Bw.push(D)%7Dfunction%20I(D)%7Bx.push(D)%7DRs(d%2C%7Bargs%3AC%2Cname%3AR%2Cstore%3AE%2Cafter%3AM%2ConError%3AI%7D)%3Blet%20O%3Btry%7BO%3DT.apply(this%26%26this.%24id%3D%3D%3Dt%3Fthis%3AE%2CC)%7Dcatch(D)%7Bthrow%20Rs(x%2CD)%2CD%7Dreturn%20O%20instanceof%20Promise%3FO.then(D%3D%3E(Rs(w%2CD)%2CD)).catch(D%3D%3E(Rs(x%2CD)%2CPromise.reject(D)))%3A(Rs(w%2CO)%2CO)%7D%22%20cmd%2Floadworld%2075309%20")

print(decode_str)