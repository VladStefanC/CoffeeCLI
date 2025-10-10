--
-- PostgreSQL database dump
--

\restrict 17ejfXyIQyaZcP8al4cwr2wUjDMoo8HAIeWmsc3fkFCryPpFmaRqvRUfeHMuHh6

-- Dumped from database version 14.19 (Homebrew)
-- Dumped by pg_dump version 14.19 (Homebrew)

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
-- Name: favorites; Type: TABLE; Schema: public; Owner: coffeeuser
--

CREATE TABLE public.favorites (
    user_id uuid NOT NULL,
    recipe_id integer NOT NULL
);


ALTER TABLE public.favorites OWNER TO coffeeuser;

--
-- Name: recipes; Type: TABLE; Schema: public; Owner: coffeeuser
--

CREATE TABLE public.recipes (
    id integer NOT NULL,
    method character varying(50) NOT NULL,
    name character varying(120) NOT NULL,
    ingredients text NOT NULL,
    steps text NOT NULL,
    brew_time character varying(50) NOT NULL,
    user_id uuid
);


ALTER TABLE public.recipes OWNER TO coffeeuser;

--
-- Name: recipes_id_seq; Type: SEQUENCE; Schema: public; Owner: coffeeuser
--

CREATE SEQUENCE public.recipes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipes_id_seq OWNER TO coffeeuser;

--
-- Name: recipes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: coffeeuser
--

ALTER SEQUENCE public.recipes_id_seq OWNED BY public.recipes.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: coffeeuser
--

CREATE TABLE public.users (
    username character varying(100),
    id uuid NOT NULL,
    email character varying(320) NOT NULL,
    hashed_password character varying(1024) NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    is_verified boolean NOT NULL
);


ALTER TABLE public.users OWNER TO coffeeuser;

--
-- Name: recipes id; Type: DEFAULT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.recipes ALTER COLUMN id SET DEFAULT nextval('public.recipes_id_seq'::regclass);


--
-- Data for Name: favorites; Type: TABLE DATA; Schema: public; Owner: coffeeuser
--

COPY public.favorites (user_id, recipe_id) FROM stdin;
64a458fc-0010-4f85-8041-9071dbd2423c	3
64a458fc-0010-4f85-8041-9071dbd2423c	4
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: coffeeuser
--

COPY public.recipes (id, method, name, ingredients, steps, brew_time, user_id) FROM stdin;
1	AeroPress	Classic AeroPress	15g medium-fine coffee, 220ml water	Add coffee, bloom 30s with 50ml water, stir, add rest of water, press after 2:30	2:30-3:00	\N
2	AeroPress	Inverted AeroPress	17g medium coffee, 240ml water	Assemble upside-down, add coffee + water, stir, steep 1:30, flip and press	2:00-2:30	\N
3	Cold Brew	Overnight Cold Brew	60g coarse coffee, 1L cold water	Mix coffee + water in jar, steep 12–16 hours, strain through filter	12h-16h	\N
4	Cold Brew	Japanese Iced Coffee (Flash Brew)	20g medium coffee, 150ml hot water, 150g ice	Brew coffee directly over ice in Chemex or V60, stir, serve	3:00-4:00	\N
5	French Press	Classic French Press	30g coarse coffee, 500ml water	Add coffee + water, stir, steep 4 min, plunge slowly	4:00	\N
6	French Press	French Press Bloom Method	18g coarse coffee, 300ml water	Bloom with 60ml for 30s, add rest of water, steep 3:30, plunge	4:00	\N
7	V60	Standard V60	15g medium-fine coffee, 250ml water	Bloom 30s with 50ml, pour in circles in 3 stages, finish ~2:30-3:00	2:30-3:00	\N
8	V60	Light Roast V60	18g coffee, 300ml water	Bloom 45s with 60ml, pour in 4 stages, finish ~3:30	3:30-4:00	\N
9	AeroPress	Competition Style AeroPress	18g medium-fine coffee, 230ml water at 92°C	Preheat brewer, bloom 30s with 60ml, stir 10x, add remaining water, plunge starting at 1:45 over 45s	2:30	\N
10	AeroPress	AeroPress Short Concentrate	20g fine coffee, 120ml water	Bloom 20s with 40ml, stir, add rest, steep 1:00, press firmly for syrupy shot	1:30	\N
11	AeroPress	AeroPress Bypass Brew	17g medium coffee, 120ml brew water, 80ml bypass water	Bloom 30s with 40ml, stir 8x, plunge at 1:20, top up with bypass water in mug	2:00	\N
12	AeroPress	AeroPress Metal Filter Brew	16g medium coffee, 220ml water	Use metal filter, bloom 30s with 50ml, steep 1:30, swirl, press lightly over 45s	2:30	\N
13	V60	V60 Bloom & Pulse	17g medium-fine coffee, 255ml water at 94°C	Bloom 40s with 45ml, pulse pour 40ml every 20s, finish by 2:50 with gentle swirl	3:00	\N
14	V60	V60 Rao Spin Method	20g medium coffee, 300ml water	Bloom 45s with 60ml, add remaining water in two 120ml pours with Rao spins, finish at 3:15	3:15	\N
15	V60	V60 Bypass Sweet	16g medium coffee, 220ml brew water, 30ml bypass water	Bloom 30s with 40ml, pour to 220ml by 2:30, add bypass water to cup, swirl before serving	2:45	\N
16	V60	V60 Iced Concentrate	24g medium-fine coffee, 200ml hot water, 120g ice	Place ice in server, bloom 30s with 50ml, finish pours by 2:50, swirl to chill	3:00	\N
17	French Press	French Press 3-Stage Stir	28g coarse coffee, 450ml water at 96°C	Bloom 45s with 100ml, break crust at 2:00, skim foam, steep to 4:30 then plunge slowly	4:30	\N
18	French Press	French Press No-Stir Sweet	32g coarse coffee, 500ml water	Add coffee then water gently, steep 6 min without stirring, use spoon to break crust, plunge at 6:30	6:30	\N
19	French Press	French Press Metal Mesh Double Filter	30g coarse coffee, 480ml water	Bloom 30s with 80ml, add rest, steep 4 min, plunge, pour through paper filter for clean cup	4:30	\N
20	French Press	French Press Bold Roast	34g coarse coffee, 520ml water	Stir after pouring water, steep 5 min, plunge halfway, wait 30s, finish plunge	5:30	\N
21	Cold Brew	Cold Brew Concentrate	120g coarse coffee, 1L cold water	Combine coffee + water in jar, stir, steep 16-18 hours refrigerated, strain and dilute 1:1	16h-18h	\N
22	Cold Brew	Cold Brew with Citrus	70g coarse coffee, 1L water, 2 strips orange zest	Add coffee + zest + water, steep 14 hours in fridge, strain, serve over ice	14h	\N
23	Cold Brew	Nitro-Style Cold Brew	80g coarse coffee, 900ml water	Steep 18 hours, strain, shake vigorously or use whipped cream dispenser for texture	18h	\N
24	Cold Brew	Quick Steep Cold Brew	50g coarse coffee, 600ml water	Steep 8 hours at room temp, strain through paper filter, chill before serving	8h	\N
0	V60	Vlads V60 Recipe	16.5 Corse Coffee grounds and 270ml water	Bloom coffee with 30 grams of water at 91C temperature for 30 seconds and stir, pur continously 240 grams of water. Wait to sit and enjoy!	2:30-4:00	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: coffeeuser
--

COPY public.users (username, id, email, hashed_password, is_active, is_superuser, is_verified) FROM stdin;
VladC	64a458fc-0010-4f85-8041-9071dbd2423c	vlad@coffee.cli	$argon2id$v=19$m=65536,t=3,p=4$eKIDBo5O3QgLauPo/StNUQ$Ts64tLjfFbTdpOwLqJTv9lgerod1hNKj+mrAEyJGRxE	t	f	f
usernametest	87121efb-4e82-4555-9d8e-7b007f851e69	VladCoffeeCli@coffee.com	$argon2id$v=19$m=65536,t=3,p=4$8NPZCjkSrgrHMqrbs75Y4A$ikDt/CoBEl6TC+HqZv/7qEVXqdGUVl8apBAMznXM8xM	t	f	f
vlad	1fe02a81-a0e6-4d99-9975-b1912fb7d173	ciorescuvladstefan0@gmail.com	$argon2id$v=19$m=65536,t=3,p=4$kXQ0PFHMP6zLwGmiieG41Q$qqYlAnMUrWAHKkrw2InsgR13+uhuVZw57B3LT+YE3XE	t	f	f
test	56688bb5-fb45-4ad6-a1ee-fbf61aa42f48	test@mail.com	$argon2id$v=19$m=65536,t=3,p=4$Axin8KGQLrJlkPn4FdqCQg$W7c2yVOYQpxKypTRdw03GHMTpYVhfOgDeHnADiGpQOI	t	f	f
Sweezy	f16a121f-b86d-4603-bec6-9330a0e04fb7	ciorescuvlastefan@gmail.com	$argon2id$v=19$m=65536,t=3,p=4$S9aWNefWxq1lUj9mVOXm/g$TvgiRsTyRq650GG6ZxKH/IIzW1DWJLaj9B07Yct3aR0	t	f	f
test123	a6f6b989-6f6b-4a07-bcd1-753b3e701678	test123@mail.com	$argon2id$v=19$m=65536,t=3,p=4$/DcLeR86vZTdtBLjjvIevQ$r+s+Qt+edOsBKoDH8aboX1cN5U/i845xpsugiOD+RXk	t	f	f
\.


--
-- Name: recipes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: coffeeuser
--

SELECT pg_catalog.setval('public.recipes_id_seq', 24, true);


--
-- Name: favorites favorites_pkey; Type: CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_pkey PRIMARY KEY (user_id, recipe_id);


--
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: ix_recipes_id; Type: INDEX; Schema: public; Owner: coffeeuser
--

CREATE INDEX ix_recipes_id ON public.recipes USING btree (id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: coffeeuser
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: favorites favorites_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: favorites favorites_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: recipes recipes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: coffeeuser
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

\unrestrict 17ejfXyIQyaZcP8al4cwr2wUjDMoo8HAIeWmsc3fkFCryPpFmaRqvRUfeHMuHh6

