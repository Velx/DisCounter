import axios from 'axios'

const instance = axios.create({
// .. where we make our configurations
  baseURL: (process.env.NODE_ENV === 'development') ? 'http://0.0.0.0:8000/api/' : 'api.discounter.pp.ua/api/'
});

export default instance;