const state = {
  Stepper: 1,
  PlayerList: ['wj', 'gl', 'gxw', 'gyk', 'pdl', 'lyc', 'ljk'],

};

const mutations = {
  UPDATE_STEP(state, payload){
    state.Stepper = payload;
  },
};

const actions = {
  updateStep (context, payload) {
    context.commit('UPDATE_STEP', payload);
  },
};

const getters = {
  get_stepper: state => state.Stepper,
  get_PlayerList: state => state.PlayerList,
};

const GameProgressData ={
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}

export default GameProgressData;