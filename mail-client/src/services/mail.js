import axiosInstance from "@/services/axiosInstance";

export default {
  getAll: () => {
    localStorage.get("/list");
  },
  open: (messageID) => {
    localStorage.get(`/open/${messageID}`);
  },
  delete: (messageID) => {
    axiosInstance.delete(`/delete/${messageID}`);
  },
  send: (sender, receiver, subject, content) => {
    axiosInstance.post("/send", {
      sender,
      receiver,
      subject,
      content,
    });
  },
  forward: (messageID, sender, receiver) => {
    axiosInstance.post("/forward", {
      messageID,
      sender,
      receiver,
    });
  },
  reply: (messageID, content) => {
    axiosInstance.post("/reply", {
      messageID,
      content,
    });
  },
};
