import { api } from "./axios";

// -- Question

const question = {
  list: (param) => {
    return api.get("/api/question/list", { params: param });
  },
  detail: (param) => {
    return api.get("/api/question/detail", { params: param }); // question_id
  },
  create: (param) => {
    return api.post("/api/question/create", param);
  },
  update: (param) => {
    return api.put("/api/question/update", param);
  },
  delete: (param) => {
    return api.delete("/api/question/delete", { params: param });
  },
  vote: (param) => {
    return api.post("/api/question/vote", param);
  }
}

// -- Answer

const answer = {
  create : (param) => {
    return api.post("/api/answer/create", param); // question_id
  },
  detail : (param) => {
    return api.get("/api/answer/detail", { params: param }); // answer_id
  },
  update : (param) => {
    return api.put("/api/answer/update", param);
  },
  delete : (param) => {
    return api.delete("/api/answer/delete", { params: param });
  },
  vote : (param) => {
    return api.post("/api/answer/vote", param);
  }
}

// -- Users

const user = {
  create: (param) => {
    return api.post("/api/user/create", param);
  },
  login: (param) => {
    return api.post("/api/user/login", param);
  }
}

// -- Levarage

const leverage = {
  calculater: (param) => {
    return api.post("/api/engine/leverage/calculater", param);
  }
}

export {question, answer, user, leverage}
