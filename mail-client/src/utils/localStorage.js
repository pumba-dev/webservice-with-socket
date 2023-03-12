export default {
  set: (key, value) => {
    localStorage.setItem(key, JSON.stringify(value));
  },
  get: (key) => {
    const value = localStorage.getItem(key);
    if (value) return JSON.parse(value);
    else return null;
  },
  delete: (key) => {
    const value = localStorage.getItem(key);
    if (value) {
      localStorage.removeItem(key);
      return true;
    }
    return false;
  },
};
