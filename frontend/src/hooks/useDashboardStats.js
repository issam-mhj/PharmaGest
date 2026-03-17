import { useQuery } from "@tanstack/react-query";

import { fetchMedicamentAlertes, fetchMedicaments } from "../api/medicamentsApi";
import { fetchVentes } from "../api/ventesApi";

const formatTodayDate = () => {
  const today = new Date();
  const yyyy = today.getFullYear();
  const mm = String(today.getMonth() + 1).padStart(2, "0");
  const dd = String(today.getDate()).padStart(2, "0");
  return `${yyyy}-${mm}-${dd}`;
};

export const useDashboardStats = () => {
  const today = formatTodayDate();

  const medicamentsQuery = useQuery({
    queryKey: ["dashboard", "medicaments-count"],
    queryFn: () => fetchMedicaments({ page_size: 1 }),
  });

  const alertsQuery = useQuery({
    queryKey: ["dashboard", "medicaments-alerts"],
    queryFn: fetchMedicamentAlertes,
  });

  const ventesTodayQuery = useQuery({
    queryKey: ["dashboard", "ventes-today", today],
    queryFn: () => fetchVentes({ date_vente_debut: today, date_vente_fin: today }),
  });

  const recentSalesQuery = useQuery({
    queryKey: ["dashboard", "ventes-recentes"],
    queryFn: () => fetchVentes({ page_size: 5 }),
  });

  return {
    medicamentsCount: medicamentsQuery.data?.count || 0,
    alertsCount: alertsQuery.data?.length || 0,
    ventesTodayCount: ventesTodayQuery.data?.count || 0,
    alerts: alertsQuery.data || [],
    recentSales: recentSalesQuery.data?.results || [],
    loading:
      medicamentsQuery.isLoading ||
      alertsQuery.isLoading ||
      ventesTodayQuery.isLoading ||
      recentSalesQuery.isLoading,
  };
};