import localStorage from "@/utils/localStorage";
// import axiosInstance from "@/services/axiosInstance";

export default {
  login: (name) => {
    localStorage.set("userToken", name);
  },
};
