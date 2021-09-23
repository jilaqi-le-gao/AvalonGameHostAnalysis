const state = {
  Stepper: 1,
  PlayerList: ['wj', 'gl', 'gxw', 'gyk', 'pdl', 'lyc', 'ljk'],
  SelectedPlayers: [],
  TotalWins: 0,
  TtoalLoss: 0,
  RoundOne: {},
  RoundTwo: {},
  RoundThree: {},
  RoundFour: {},
  RoundFive: {},
  PlayerRoles: {},
  AfterMatch: {},
};

const mutations = {
  UPDATE_STEP(state, payload){
    state.Stepper = payload;
  },
  SAVE_SELECTED_PLAYERS (state, payload){
    state.SelectedPlayers = payload;
  },
};

const actions = {
  updateStep (context, payload) {
    context.commit('UPDATE_STEP', payload);
  },
  saveSelectedPlayers (context, payload){
    context.commit('SAVE_SELECTED_PLAYERS', payload);
  },
};

const getters = {
  get_stepper: state => state.Stepper,
  get_PlayerList: state => state.PlayerList,
  get_SelectedPlayer: state => state.SelectedPlayers,
};

const GameProgressData ={
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}

export default GameProgressData;