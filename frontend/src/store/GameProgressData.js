import { axiosLocalInstance } from './httpHeader';
import { cookie } from 'cookie.js';


const state = {
  Stepper: 1,
  PlayerList: [],
  SelectedPlayers: [],
  RoundsData: [
    {
      lancelot_change: false,
      WinOrLoss: false,
      VoteResultFailNumber: null,
      TestCarOne: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      TestCarTwo: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      FinalCar: {
        Initiator: '',
        CarPlayers: []
      }
    }, 
    {
      lancelot_change: false,
      WinOrLoss: false,
      VoteResultFailNumber: null,
      TestCarOne: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      TestCarTwo: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      FinalCar: {
        Initiator: '',
        CarPlayers: []
      }
    }, 
    {
      lancelot_change: false,
      WinOrLoss: false,
      VoteResultFailNumber: null,
      TestCarOne: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      TestCarTwo: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      FinalCar: {
        Initiator: '',
        CarPlayers: []
      }
    }, 
    {
      lancelot_change: false,
      WinOrLoss: false,
      VoteResultFailNumber: null,
      TestCarOne: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      TestCarTwo: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      FinalCar: {
        Initiator: '',
        CarPlayers: []
      }
    }, 
    {
      lancelot_change: false,
      WinOrLoss: false,
      VoteResultFailNumber: null,
      TestCarOne: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      TestCarTwo: {
        Initiator: '',
        CarPlayers: [],
        VoteForYes: [],
      },
      FinalCar: {
        Initiator: '',
        CarPlayers: []
      }
    }
  ],
  PlayerRoles: {},
  WinOrLoss: false,
  AfterMatch: {},

  
  Players_inloading: false,
  current_user: ''
};

const mutations = {
  UPDATE_STEP(state, payload){
    // console.log('step update', payload);
    state.Stepper = payload;
  },
  SAVE_SELECTED_PLAYERS (state, payload){
    state.SelectedPlayers = payload;
  },
  UPDATE_ALL_PLAYERS(state, playload){
    state.PlayerList = playload;
    state.Players_inloading = false;
  },
  UPDATE_ROUNDDATA(state, payload){
    var round_data = payload.RoundInfo;
    var RoundIndex = payload.RoundIndex - 1;
    state.RoundsData[RoundIndex] = round_data;
  },
  UPDATE_ENDGAME(state, payload){
    state.PlayerRoles = payload.Charactors;
    state.WinOrLoss = payload.WinOrLoss;
    state.AfterMatch = {
      Kill: payload.Kill,
      ClaimPai: payload.ClaimPai,
    };
  },
  POST_SAVE_RESULT(state){
    axiosLocalInstance({
      url: 'sibyl/api/SaveGameRecord/',
      method: 'POST',
      headers:{
        'X-CSRFTOKEN':cookie.get('csrftoken'),
      },
      data: {
        Recoder: state.current_user,
        SelectedPlayers: state.SelectedPlayers, 
        RoundsData: state.RoundsData,
        PlayerRoles: state.PlayerRoles,
        WinOrLoss: state.WinOrLoss,
        AfterMatch: state.AfterMatch,
      }
    }).then(function (response){
      console.log(response.data);
    })
  },
  UPDATE_CURRENT_USER(state){
    axiosLocalInstance({
      url: 'sibyl/api/GetUsername/',
      method: 'GET',
    }).then(function (response){
      // console.log(response.data);
      state.current_user = response.data;
    })
  }
};

const actions = {
  updateStep (context, payload) {
    context.commit('UPDATE_STEP', payload);
  },
  saveSelectedPlayers (context, payload){
    context.commit('SAVE_SELECTED_PLAYERS', payload);
  },
  get_all_player_list (context) {
    state.Players_inloading = true;
    axiosLocalInstance({
      url: 'sibyl/api/GetAllPlayers/',
      method: 'GET',
    }).then(function (response){
      // console.log(response.data);
      context.commit('UPDATE_ALL_PLAYERS', response.data);
    })
  },
  save_each_round (context, payload){
    context.commit('UPDATE_ROUNDDATA', payload)
  },
  save_end_game (context, payload){
    context.commit('UPDATE_ENDGAME', payload);
    context.commit('POST_SAVE_RESULT');
  },
  upate_current_user (context){
    context.commit('UPDATE_CURRENT_USER');
  }
};

const getters = {
  get_stepper: state => state.Stepper,
  get_PlayerList: state => state.PlayerList,
  get_SelectedPlayer: state => state.SelectedPlayers,
  get_play_loading: state => state.Players_inloading,
  get_current_user: state => state.current_user,
};

const GameProgressData ={
  namespaced: true,
  state,
  mutations,
  actions,
  getters
}

export default GameProgressData;