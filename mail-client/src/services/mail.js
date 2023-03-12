import axiosInstance from "@/services/axiosInstance";

export default {
  getAll: () => {
    return axiosInstance.get("/list");
  },
  getByReceiver: (receiver) => {
    return axiosInstance.get(`/listByReceiver/${receiver}`);
  },
  open: (messageID) => {
    return axiosInstance.get(`/open/${messageID}`);
  },
  delete: (messageID) => {
    return axiosInstance.delete(`/delete/${messageID}`);
  },
  send: (sender, receiver, subject, content) => {
    return axiosInstance.post("/send", {
      sender,
      receiver,
      subject,
      content,
    });
  },
  forward: (messageID, sender, receiver) => {
    return axiosInstance.post("/forward", {
      messageID,
      sender,
      receiver,
    });
  },
  reply: (messageID, content) => {
    return axiosInstance.post("/reply", {
      messageID,
      content,
    });
  },
};
