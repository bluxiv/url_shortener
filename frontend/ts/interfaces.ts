export interface Page {
  count: number;
  next: null;
  previous: null;
  results: Link[] | Visit[];
}

export interface Link {
  url: string;
  short_code: string;
  short_url: string;
  created_at: Date;
  visit_count: number;
  last_visit_at?: Date;
}

export interface Visit {
  timestamp: Date;
  ip_address: string;
  user_agent: string;
}
