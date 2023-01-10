create table if not exists users (
	id bigserial primary key,
	name text not null,
	email text not null,
	phone text,
	created_at timestamptz not null default now(),
	updated_at timestamptz not null default now(),
	deleted_at timestamptz,
);

create unique index if not exists uniq_email_not_deleted on users(email) where (deleted_at is null);
create index if not exists idx_email on users(email);