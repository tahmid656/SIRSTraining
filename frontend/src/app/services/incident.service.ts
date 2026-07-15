import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Incident, CreateIncidentPayload, CreateIncidentResponse } from '../models/incident.model';

@Injectable({ providedIn: 'root' })
export class IncidentService {
  private baseUrl = '/api/incidents';

  constructor(private http: HttpClient) {}

  getById(id: number): Observable<Incident> {
    return this.http.get<Incident>(`${this.baseUrl}/${id}`);
  }

  create(payload: CreateIncidentPayload): Observable<CreateIncidentResponse> {
    return this.http.post<CreateIncidentResponse>(this.baseUrl, payload);
  }
}
