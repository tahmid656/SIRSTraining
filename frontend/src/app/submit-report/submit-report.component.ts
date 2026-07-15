import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { IncidentService } from '../services/incident.service';

@Component({
  selector: 'app-submit-report',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './submit-report.component.html',
  styleUrl: './submit-report.component.css'
})
export class SubmitReportComponent {
  form: FormGroup;
  submitting = false;
  error: string | null = null;
  success: string | null = null;

  severities = [
    { value: 'high', label: 'High — immediate response required' },
    { value: 'medium', label: 'Medium — response within 24h' },
    { value: 'low', label: 'Low — routine logging' },
  ];

  categories = [
    'Security Breach',
    'Equipment Malfunction',
    'Personnel Conduct',
    'Safety Hazard',
    'Other',
  ];

  constructor(
    private fb: FormBuilder,
    private incidentService: IncidentService,
    private router: Router
  ) {
    this.form = this.fb.group({
      title: ['', Validators.required],
      severity: ['', Validators.required],
      category: ['', Validators.required],
      incident_datetime: ['', Validators.required],
      location: [''],
      description: ['', Validators.required],
      personnel_involved: [''],
    });
  }

  onSubmit(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    this.submitting = true;
    this.error = null;
    this.success = null;

    this.incidentService.create(this.form.value).subscribe({
      next: (res) => {
        this.submitting = false;
        this.success = res.message;
        this.form.reset();
      },
      error: (err) => {
        this.submitting = false;
        this.error = err?.error?.error || 'Failed to submit report. Please try again.';
      }
    });
  }
}
