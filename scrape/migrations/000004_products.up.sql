create table if not exists products (
	id bigserial primary key,
	name text not null,
    picture text not null,
	created_at timestamptz not null default now(),
	updated_at timestamptz not null default now(),
	deleted_at timestamptz
);