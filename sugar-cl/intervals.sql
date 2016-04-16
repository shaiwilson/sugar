--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.1
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: intervals; Type: TABLE; Schema: public; Owner: shai
--

CREATE TABLE intervals (
    id integer NOT NULL,
    date date,
    start_time time without time zone,
    end_time time without time zone
);


ALTER TABLE intervals OWNER TO shai;

--
-- Name: intervals_id_seq; Type: SEQUENCE; Schema: public; Owner: shai
--

CREATE SEQUENCE intervals_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE intervals_id_seq OWNER TO shai;

--
-- Name: intervals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shai
--

ALTER SEQUENCE intervals_id_seq OWNED BY intervals.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: shai
--

CREATE TABLE students (
    username character varying(30)
);


ALTER TABLE students OWNER TO shai;

--
-- Name: id; Type: DEFAULT; Schema: public; Owner: shai
--

ALTER TABLE ONLY intervals ALTER COLUMN id SET DEFAULT nextval('intervals_id_seq'::regclass);


--
-- Data for Name: intervals; Type: TABLE DATA; Schema: public; Owner: shai
--

COPY intervals (id, date, start_time, end_time) FROM stdin;
\.


--
-- Name: intervals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shai
--

SELECT pg_catalog.setval('intervals_id_seq', 1, false);


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: shai
--

COPY students (username) FROM stdin;
\.


--
-- Name: intervals_pkey; Type: CONSTRAINT; Schema: public; Owner: shai
--

ALTER TABLE ONLY intervals
    ADD CONSTRAINT intervals_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

