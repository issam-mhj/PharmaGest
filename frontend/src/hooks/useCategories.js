import { useQuery } from "@tanstack/react-query";

import { fetchCategories } from "../api/categoriesApi";

export const useCategories = () => {
  const query = useQuery({
    queryKey: ["categories", "all"],
    queryFn: () => fetchCategories({ page_size: 100 }),
  });

  return {
    categories: query.data?.results || [],
    loading: query.isLoading,
    error: query.error,
  };
};