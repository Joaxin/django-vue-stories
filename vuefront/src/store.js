import Vue from "vue";
import Vuex from "vuex";
import messageService from "@/services/messageService";

Vue.use(Vuex);

export default new Vuex.Store({
  namespaced: true,
  state: {
    messages: [],
    form: {
      id: 0,
      author: "mxh-cp-stories",
      content: "",
      tags: [],
      inputVisible: false,
      inputValue: "",
      is_public: false
    }
  },
  getters: {
    messages: state => {
      return state.messages;
    },
    form: state => {
      return state.form;
    }
  },
  mutations: {
    setMessages(state, messages) {
      state.messages = messages;
    },
    addMessage(state, message) {
      state.messages.push(message);
    },
    getMessage(state, message) {
      state.form.id = message.id;
      state.form.content = message.content;
      state.form.author = message.author;
      state.form.tags = message.tags;
    },
    putMessage(state, msgId, message) {
      let msgs = state.messages.splice(msgId, 1, message);
      state.messages = msgs;
    },
    patchMessage(state, msgId, message) {
      let msgs = state.messages.splice(msgId, 1, message);
      state.messages = msgs;
    },
    deleteMessage(state, msgId) {
      state.messages = state.messages.filter(obj => obj.id !== msgId);
    }
  },
  actions: {
    getMessages({ commit }) {
      messageService.fetchMessages().then(messages => {
        commit("setMessages", messages);
      });
    },
    getMessage({ commit }, msgId) {
      messageService.getMessage(msgId).then(message => {
        commit("getMessage", message);
      });
    },
    addMessage({ commit }, message) {
      messageService.postMessage(message).then(() => {
        commit("addMessage", message);
      });
    },
    putMessage({ commit }, message) {
      messageService.putMessage(message.id, message);
      commit("putMessage", message.id, message);
    },
    patchMessage({ commit }, message) {
      messageService.patchMessage(message.id, message);
      commit("patchMessage", message.id, message);
    },
    deleteMessage({ commit }, msgId) {
      messageService.deleteMessage(msgId);
      commit("deleteMessage", msgId);
    }
  }
});
