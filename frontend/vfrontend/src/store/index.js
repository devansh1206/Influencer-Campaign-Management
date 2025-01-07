import { createStore } from "vuex";

export default createStore({
  state: {
    user: JSON.parse(localStorage.getItem("user")) || null, // Load from localStorage
    token: localStorage.getItem("token") || null,
  },
  getters: {},
  mutations: {
    setUser(state, data) {
      state.user = data.user_data;
      localStorage.setItem("user", JSON.stringify(state.user)); // Save user to localStorage
      state.token = data.token;
      localStorage.setItem("token", state.token); // Save token to localStorage
    },
    clearUser(state) {
      state.user = null;
      localStorage.removeItem("user"); // Clear from localStorage
    },
    clearToken(state) {
      state.token = null;
      localStorage.removeItem("token");
    },
    set_sponsor_campaigns(state, sponsor_campaigns){
      state.user.sponsor_campaign = sponsor_campaigns;

      localStorage.setItem("user", state.user);
    }
  },
  actions: {
    // Example: Login action
    logout({ commit }) {
      commit("clearUser");
      commit("clearToken");
    },
  },
  modules: {},
});

// store/index.js
// export default new Vuex.Store({
//   state: {
//     user: JSON.parse(localStorage.getItem("user")) || null, // Load from localStorage
//     token: localStorage.getItem("token") || null,
//   },
//   mutations: {
//     setUser(state, user) {
//       state.user = user;
//       localStorage.setItem("user", JSON.stringify(user)); // Save user to localStorage
//     },
//     setToken(state, token) {
//       state.token = token;
//       localStorage.setItem("token", token); // Save token to localStorage
//     },
//     clearUser(state) {
//       state.user = null;
//       localStorage.removeItem("user"); // Clear from localStorage
//     },
//     clearToken(state) {
//       state.token = null;
//       localStorage.removeItem("token");
//     }
//   },
//   actions: {
//     // Example: Login action
//     login({ commit }, { user, token }) {
//       commit("setUser", user);
//       commit("setToken", token);
//     },
//     logout({ commit }) {
//       commit("clearUser");
//       commit("clearToken");
//     }
//   },
// });
