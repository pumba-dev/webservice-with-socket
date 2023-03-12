export default {
  namespaced: true,
  state: {
    notifyList: [],
  },
  getters: {
    getAll(state) {
      return state.notifyList;
    },
  },
  mutations: {
    setNotifyList(state, payload) {
      state.notifyList = payload;
    },
    addNotify(state, payload) {
      state.notifyList.push(payload);
    },
    removeNotify(state, payload) {
      state.notifyList.splice(payload, 1);
    },
    removeFirstNotify(state) {
      state.notifyList.shift();
    },
  },
  actions: {
    create({ commit }, payload) {
      const notify = payload.type ? payload : { type: "right", ...payload };

      commit("addNotify", notify);

      setTimeout(() => {
        commit("removeFirstNotify");
      }, 5000);
    },
    remove({ commit }, notifyIndex) {
      commit("removeNotify", notifyIndex);
    },
    removeFirst({ commit }) {
      commit("removeFirstNotify");
    },
    removeAll({ commit }) {
      commit("setnotifyList", []);
    },
  },
};
