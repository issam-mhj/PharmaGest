import axiosInstance from "./axiosConfig";

export const fetchCategories = async (params = {}) => {
  const response = await axiosInstance.get("/categories/", { params });
  return response.data;
};