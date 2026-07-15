import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Incident {
  id: number;
  title: string;
  category: string;
  severity: string;
  description?: string;
  location?: string;
  incident_datetime: string;
  status: string;
  reporter_id: number;
  assigned_to_id?: number;
  created_at: string;
  updated_at: string;
}

export interface CreateIncidentPayload {
  title: string;
  category: string;
  severity: string;
  description?: string;
  location?: string;
  incident_datetime: string;
}

@Injectable({ providedIn: 'root' })
export class IncidentService {
  private baseUrl = '/api/incidents';

  constructor(private http: HttpClient) {}

  /** GET /api/incidents — fetch all incidents (supervisor/admin only) */
  getAllIncidents(): Observable<Incident[]> {
    // TODO: implement
    return this.http.get<Incident[]>(this.baseUrl);
  }

  /** GET /api/incidents/mine — fetch incidents filed by the current user */
  getMyIncidents(): Observable<Incident[]> {
    // TODO: implement
    return this.http.get<Incident[]>(`${this.baseUrl}/mine`);
  }

  /** GET /api/incidents/:id — fetch full detail of a single incident */
  getIncidentById(id: number): Observable<Incident> {
    // TODO: implement
    return this.http.get<Incident>(`${this.baseUrl}/${id}`);
  }

  /** POST /api/incidents — submit a new incident report */
  createIncident(payload: CreateIncidentPayload): Observable<Incident> {
    // TODO: implement
    return this.http.post<Incident>(this.baseUrl, payload);
  }
}
