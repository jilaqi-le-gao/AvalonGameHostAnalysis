import axios from 'axios';


const axiosLocalInstance = axios.create({
  baseURL: "/avalon",   // /proxy
});


export {axiosLocalInstance};