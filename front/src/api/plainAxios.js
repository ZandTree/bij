import axios from 'axios'
let baseUrl = 'http://172.105.72.101:8000'



const simpleAPI = axios.create({
    baseURL: baseUrl,
    headers:{
      Accept:"application/json",
      'Content-Type': 'application/json',
      
    }
  })

  
export default  simpleAPI
