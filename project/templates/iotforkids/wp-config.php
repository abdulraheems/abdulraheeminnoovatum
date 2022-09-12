<?php
define( 'WP_CACHE', true );
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'u389999004_Pd8D7' );

/** MySQL database username */
define( 'DB_USER', 'u389999004_5K9uH' );

/** MySQL database password */
define( 'DB_PASSWORD', '0tcDxSKDfz' );

/** MySQL hostname */
define( 'DB_HOST', 'mysql' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          '~I.c g,)FfNp;ORs2112/3V^mEa]r!}d^lp<x:k<rM_>$jaf9b{2(pgrrOD_u6}v' );
define( 'SECURE_AUTH_KEY',   'm|9- blh@ytKNi>*&iDQkDgRL,s,?|K=M*tl)gbNWE<k9/ID2//NhGtt3Ia|KaLS' );
define( 'LOGGED_IN_KEY',     'tXqb#~x#)%< u)ZvfhF~xqn+`S0xVzq2pj=KZ:Zdk)*cAo]^SYYQ|XBC`5<v KLM' );
define( 'NONCE_KEY',         ';Nzz#$pjw;O&;L#Jarg+(2xCG9`a26Nt(B(V8Q0%Il?uI}>o7#uQvvh])/xbX9L;' );
define( 'AUTH_SALT',         'SqjvKn46oU@qW}_@fs4=/(I0^TWA2bSVb29}zg,W74#{OdD>gciMF|k3H1b<m|`n' );
define( 'SECURE_AUTH_SALT',  'V2@675*;ByIog: VOZ|6m`j4|%-[NEW;;t9e~pA`4h2a|iN]{b]r0* Da0odfEq!' );
define( 'LOGGED_IN_SALT',    '@yCe((7~*[91Jq*H*.]$Q?n y:Wgo9HI_++:,5`n;Y^6C]uDBayO|%7MR`(M9vE^' );
define( 'NONCE_SALT',        '|;47ig^!k0;#B2phYW1%gb? <2c:;;o#Y+tTP9mmXg|P22(kZW)z0@E$?2]kE_uS' );
define( 'WP_CACHE_KEY_SALT', 'rGu@-k60q}xYySpoJtnfZz;<ylUT@!)By ~4^W4$^P[K:q`s~;i53&d(6um|@rI^' );

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';




define( 'WP_AUTO_UPDATE_CORE', true );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', dirname( __FILE__ ) . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
