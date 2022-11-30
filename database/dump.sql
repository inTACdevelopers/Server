--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Ubuntu 13.7-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.7 (Ubuntu 13.7-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: posts; Type: TABLE; Schema: public; Owner: intac_net_ru_usr
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    description character varying(200) NOT NULL,
    seller_contact character varying(255) NOT NULL,
    from_user integer NOT NULL,
    file_path character varying(512) NOT NULL,
    creation_time character varying(255) NOT NULL,
    likes bigint DEFAULT 0 NOT NULL,
    weight double precision DEFAULT 0 NOT NULL
);


ALTER TABLE public.posts OWNER TO intac_net_ru_usr;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: intac_net_ru_usr
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_id_seq OWNER TO intac_net_ru_usr;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: intac_net_ru_usr
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: intac_net_ru_usr
--

CREATE TABLE public.users (
    id integer NOT NULL,
    login character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    surname character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    company character varying(255),
    birth_date character varying(255),
    token character varying(512)
);


ALTER TABLE public.users OWNER TO intac_net_ru_usr;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: intac_net_ru_usr
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO intac_net_ru_usr;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: intac_net_ru_usr
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: posts file_path; Type: CONSTRAINT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT file_path UNIQUE (file_path);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: users users_login_key; Type: CONSTRAINT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_login_key UNIQUE (login);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: posts user; Type: FK CONSTRAINT; Schema: public; Owner: intac_net_ru_usr
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT "user" FOREIGN KEY (from_user) REFERENCES public.users(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO intac_net_ru_grp;


--
-- PostgreSQL database dump complete
--

