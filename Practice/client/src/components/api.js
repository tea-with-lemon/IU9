class Api {
    fetch(url,options){
        const headers = {
            'Content-Type': 'application/json'
        };
        return fetch(url,{
            headers,
            ...options
        }).then(this._checkStatus)
            .then(response => response.json())
    }

    _checkStatus(response){
        if(response.status>=200 && response.status<=300){
            return response
        }else{
            let error = new Error(response.statusText);
            error.response = response;
            throw error;
        }
    }
}

export default Api;