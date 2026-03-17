import axiosInstance from "./axiosConfig";

export const fetchVentes = async (params = {}) => {
  const response = await axiosInstance.get("/ventes/", { params });
  return response.data;
};

export const fetchVenteDetail = async (id) => {
  const response = await axiosInstance.get(`/ventes/${id}/`);
  return response.data;
};

export const createVente = async (payload) => {
  const response = await axiosInstance.post("/ventes/", payload);
  return response.data;
};

export const cancelVente = async (id) => {
  const response = await axiosInstance.post(`/ventes/${id}/annuler/`, {});
  return response.data;
};
