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
