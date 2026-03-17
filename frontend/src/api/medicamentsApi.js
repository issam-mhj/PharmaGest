import axiosInstance from "./axiosConfig";

export const fetchMedicaments = async (params = {}) => {
  const response = await axiosInstance.get("/medicaments/", { params });
  return response.data;
};

export const fetchMedicamentAlertes = async () => {
  const response = await axiosInstance.get("/medicaments/alertes/");
  return response.data;
};

export const createMedicament = async (payload) => {
  const response = await axiosInstance.post("/medicaments/", payload);
  return response.data;
};

export const updateMedicament = async ({ id, payload }) => {
  const response = await axiosInstance.patch(`/medicaments/${id}/`, payload);
  return response.data;
};

export const archiveMedicament = async (id) => {
  await axiosInstance.delete(`/medicaments/${id}/`);
};
