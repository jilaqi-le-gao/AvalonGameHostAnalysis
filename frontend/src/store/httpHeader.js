import axios from 'axios';


const axiosLocalInstance = axios.create({
  baseURL: "/avalon",   // /proxy    /avalon
});


export {axiosLocalInstance};