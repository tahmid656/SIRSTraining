export interface Incident {
  id: number;
  title: string;
  category: string;
  severity: string;
  description: string | null;
  location: string | null;
  incident_datetime: string;
  personnel_involved: string | null;
  status: string;
  reporter_id: number | null;
  assigned_to_id: number | null;
  created_at: string;
  updated_at: string;
}

export interface CreateIncidentPayload {
  title: string;
  category: string;
  severity: string;
  incident_datetime: string;
  location?: string;
  description?: string;
  personnel_involved?: string;
}

export interface CreateIncidentResponse {
  id: number;
  status: string;
  message: string;
}
