import localStorage from "@/utils/localStorage";

export default {
  login: (name) => {
    localStorage.set("userToken", name);
  },
  logout: () => {
    localStorage.delete("userToken");
  },
};
