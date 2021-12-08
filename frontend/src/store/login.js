import { axiosLocalInstance } from './httpHeader';

const state = {
  csrftoken: null,
  login_fail: false,
};

const mutations = {
  UPDATE_CSRFTOKEN (state, payload){
    state.csrftoken = payload;
  },
  LOGINFAIL (state){
    state.login_fail = true;
  },
  CLOSELOGINFAIL (state){
    state.login_fail = false;
  }
};

const actions = {
  getSaveCsrftoken (context){
    axiosLocalInstance.get('/sibyl/auth/').then(function (response){
      context.commit('UPDATE_CSRFTOKEN', response.data.csrftoken);
    });
  },
  loginUser (context, payload){
    var form_data = new FormData();
    form_data.append('username', payload.username);
    form_data.append('password', payload.password);
    form_data.append('csrfmiddlewaretoken', state.csrftoken);
    // form_data.append('next', ??)
    axiosLocalInstance({
      url: '/sibyl/login/',
      method: 'POST',
      data: form_data,
    }).then(function (response){
      console.log(response);
      if (response.request.responseURL != window.location.href){
        console.log(response.request.responseURL);
        window.location.href = response.request.responseURL;
      }else{
        console.log('login failed');
        context.commit('LOGINFAIL');
      }
    })
  },
  closeLoginFail (context) {
    context.commit('CLOSELOGINFAIL')
  },
};

const getters = {
  get_login_fail: state => state.login_fail,
};

const loginModule = {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};

export default loginModule;