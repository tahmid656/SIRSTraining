export interface LoginPayload {
  username: string;
  password: string;
}

export interface AuthUser {
  id: number;
  username: string;
  email: string;
  role: 'reporter' | 'investigator' | 'admin';
}

export interface LoginResponse {
  access_token: string;
  user: AuthUser;
}