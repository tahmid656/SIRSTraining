import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CreateIncidentPayload, CreateIncidentResponse } from '../models/incident.model';

@Injectable({ providedIn: 'root' })
export class IncidentService {
  private baseUrl = '/api/incidents';

  constructor(private http: HttpClient) {}

  create(payload: CreateIncidentPayload): Observable<CreateIncidentResponse> {
    return this.http.post<CreateIncidentResponse>(this.baseUrl, payload);
  }
}
