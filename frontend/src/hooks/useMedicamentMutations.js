import { useMutation, useQueryClient } from "@tanstack/react-query";

import { archiveMedicament, createMedicament, updateMedicament } from "../api/medicamentsApi";

export const useMedicamentMutations = () => {
  const queryClient = useQueryClient();

  const invalidateMedicaments = () => queryClient.invalidateQueries({ queryKey: ["medicaments"] });

  const createMutation = useMutation({
    mutationFn: createMedicament,
    onSuccess: invalidateMedicaments,
  });

  const updateMutation = useMutation({
    mutationFn: updateMedicament,
    onSuccess: invalidateMedicaments,
  });

  const archiveMutation = useMutation({
    mutationFn: archiveMedicament,
    onSuccess: invalidateMedicaments,
  });

  return {
    createMedicament: createMutation.mutateAsync,
    updateMedicament: updateMutation.mutateAsync,
    archiveMedicament: archiveMutation.mutateAsync,
    creating: createMutation.isPending,
    updating: updateMutation.isPending,
    archiving: archiveMutation.isPending,
  };
};