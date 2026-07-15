import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { IncidentService } from '../services/incident.service';
import { Incident } from '../models/incident.model';

@Component({
  selector: 'app-incident-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './incident-detail.component.html',
  styleUrl: './incident-detail.component.css'
})
export class IncidentDetailComponent implements OnInit {
  incident: Incident | null = null;
  loading = true;
  error: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private incidentService: IncidentService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    if (!id) {
      this.error = 'Invalid incident ID.';
      this.loading = false;
      return;
    }

    this.incidentService.getById(id).subscribe({
      next: (data) => {
        this.incident = data;
        this.loading = false;
      },
      error: (err) => {
        this.loading = false;
        if (err.status === 404) {
          this.error = 'Incident not found.';
        } else if (err.status === 403) {
          this.error = 'You do not have permission to view this incident.';
        } else {
          this.error = 'Failed to load incident details.';
        }
      }
    });
  }

  getSeverityClass(): string {
    return this.incident ? `severity-${this.incident.severity}` : '';
  }

  goBack(): void {
    this.router.navigate(['/submit-report']);
  }
}
