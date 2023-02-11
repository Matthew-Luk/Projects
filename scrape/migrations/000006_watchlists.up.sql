create table if not exists watchlists (
	id bigserial primary key,
    products array not null,
	created_at timestamptz not null default now(),
	updated_at timestamptz not null default now(),
	deleted_at timestamptz
);