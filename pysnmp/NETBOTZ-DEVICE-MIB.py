# SNMP MIB module (NETBOTZ-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETBOTZ-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:34 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(netBotz_device,) = mibBuilder.importSymbols(
    "NETBOTZ-MIB",
    "netBotz-device")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetBotz_dev_host_Type = DisplayString
_NetBotz_dev_host_Object = MibScalar
netBotz_dev_host = _NetBotz_dev_host_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 1),
    _NetBotz_dev_host_Type()
)
netBotz_dev_host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_host.setStatus("mandatory")
_NetBotz_dev_domain_Type = DisplayString
_NetBotz_dev_domain_Object = MibScalar
netBotz_dev_domain = _NetBotz_dev_domain_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 2),
    _NetBotz_dev_domain_Type()
)
netBotz_dev_domain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_domain.setStatus("mandatory")
_NetBotz_dev_ip_Type = IpAddress
_NetBotz_dev_ip_Object = MibScalar
netBotz_dev_ip = _NetBotz_dev_ip_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 3),
    _NetBotz_dev_ip_Type()
)
netBotz_dev_ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_ip.setStatus("mandatory")
_NetBotz_dev_netmask_Type = IpAddress
_NetBotz_dev_netmask_Object = MibScalar
netBotz_dev_netmask = _NetBotz_dev_netmask_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 4),
    _NetBotz_dev_netmask_Type()
)
netBotz_dev_netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_netmask.setStatus("mandatory")
_NetBotz_dev_gateway_Type = IpAddress
_NetBotz_dev_gateway_Object = MibScalar
netBotz_dev_gateway = _NetBotz_dev_gateway_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 5),
    _NetBotz_dev_gateway_Type()
)
netBotz_dev_gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_gateway.setStatus("mandatory")
_NetBotz_dev_primarydns_Type = IpAddress
_NetBotz_dev_primarydns_Object = MibScalar
netBotz_dev_primarydns = _NetBotz_dev_primarydns_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 6),
    _NetBotz_dev_primarydns_Type()
)
netBotz_dev_primarydns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_primarydns.setStatus("mandatory")
_NetBotz_dev_secondarydns_Type = IpAddress
_NetBotz_dev_secondarydns_Object = MibScalar
netBotz_dev_secondarydns = _NetBotz_dev_secondarydns_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 7),
    _NetBotz_dev_secondarydns_Type()
)
netBotz_dev_secondarydns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_secondarydns.setStatus("mandatory")
_NetBotz_dev_smtp_Type = DisplayString
_NetBotz_dev_smtp_Object = MibScalar
netBotz_dev_smtp = _NetBotz_dev_smtp_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 8),
    _NetBotz_dev_smtp_Type()
)
netBotz_dev_smtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_smtp.setStatus("mandatory")
_NetBotz_dev_smtpport_Type = Integer32
_NetBotz_dev_smtpport_Object = MibScalar
netBotz_dev_smtpport = _NetBotz_dev_smtpport_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 9),
    _NetBotz_dev_smtpport_Type()
)
netBotz_dev_smtpport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_smtpport.setStatus("mandatory")
_NetBotz_dev_popport_Type = Integer32
_NetBotz_dev_popport_Object = MibScalar
netBotz_dev_popport = _NetBotz_dev_popport_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 10),
    _NetBotz_dev_popport_Type()
)
netBotz_dev_popport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_popport.setStatus("mandatory")
_NetBotz_dev_loglevel_Type = Integer32
_NetBotz_dev_loglevel_Object = MibScalar
netBotz_dev_loglevel = _NetBotz_dev_loglevel_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 11),
    _NetBotz_dev_loglevel_Type()
)
netBotz_dev_loglevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_loglevel.setStatus("mandatory")
_NetBotz_dev_logaddress_Type = IpAddress
_NetBotz_dev_logaddress_Object = MibScalar
netBotz_dev_logaddress = _NetBotz_dev_logaddress_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 12),
    _NetBotz_dev_logaddress_Type()
)
netBotz_dev_logaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_logaddress.setStatus("mandatory")
_NetBotz_dev_logport_Type = Integer32
_NetBotz_dev_logport_Object = MibScalar
netBotz_dev_logport = _NetBotz_dev_logport_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 13),
    _NetBotz_dev_logport_Type()
)
netBotz_dev_logport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_logport.setStatus("mandatory")
_NetBotz_dev_primaryemail_Type = DisplayString
_NetBotz_dev_primaryemail_Object = MibScalar
netBotz_dev_primaryemail = _NetBotz_dev_primaryemail_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 14),
    _NetBotz_dev_primaryemail_Type()
)
netBotz_dev_primaryemail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_primaryemail.setStatus("mandatory")
_NetBotz_dev_secondaryemail_Type = DisplayString
_NetBotz_dev_secondaryemail_Object = MibScalar
netBotz_dev_secondaryemail = _NetBotz_dev_secondaryemail_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 15),
    _NetBotz_dev_secondaryemail_Type()
)
netBotz_dev_secondaryemail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_secondaryemail.setStatus("mandatory")
_NetBotz_dev_pager_Type = DisplayString
_NetBotz_dev_pager_Object = MibScalar
netBotz_dev_pager = _NetBotz_dev_pager_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 16),
    _NetBotz_dev_pager_Type()
)
netBotz_dev_pager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_pager.setStatus("mandatory")
_NetBotz_dev_serialno_Type = DisplayString
_NetBotz_dev_serialno_Object = MibScalar
netBotz_dev_serialno = _NetBotz_dev_serialno_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 17),
    _NetBotz_dev_serialno_Type()
)
netBotz_dev_serialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_dev_serialno.setStatus("mandatory")
_NetBotz_dev_pop_Type = DisplayString
_NetBotz_dev_pop_Object = MibScalar
netBotz_dev_pop = _NetBotz_dev_pop_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 18),
    _NetBotz_dev_pop_Type()
)
netBotz_dev_pop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_dev_pop.setStatus("mandatory")
_NetBotz_dev_version_Type = DisplayString
_NetBotz_dev_version_Object = MibScalar
netBotz_dev_version = _NetBotz_dev_version_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 19),
    _NetBotz_dev_version_Type()
)
netBotz_dev_version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_dev_version.setStatus("mandatory")
_NetBotz_dev_registered_Type = Integer32
_NetBotz_dev_registered_Object = MibScalar
netBotz_dev_registered = _NetBotz_dev_registered_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 20),
    _NetBotz_dev_registered_Type()
)
netBotz_dev_registered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_dev_registered.setStatus("mandatory")
_NetBotz_default_applet_Type = Integer32
_NetBotz_default_applet_Object = MibScalar
netBotz_default_applet = _NetBotz_default_applet_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 21),
    _NetBotz_default_applet_Type()
)
netBotz_default_applet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_default_applet.setStatus("mandatory")
_NetBotz_guibar_color_Type = Integer32
_NetBotz_guibar_color_Object = MibScalar
netBotz_guibar_color = _NetBotz_guibar_color_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 22),
    _NetBotz_guibar_color_Type()
)
netBotz_guibar_color.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_guibar_color.setStatus("mandatory")
_NetBotz_locale_Type = DisplayString
_NetBotz_locale_Object = MibScalar
netBotz_locale = _NetBotz_locale_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 23),
    _NetBotz_locale_Type()
)
netBotz_locale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_locale.setStatus("mandatory")
_NetBotz_timezone_Type = DisplayString
_NetBotz_timezone_Object = MibScalar
netBotz_timezone = _NetBotz_timezone_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 24),
    _NetBotz_timezone_Type()
)
netBotz_timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_timezone.setStatus("mandatory")
_NetBotz_24hourpreferred_Type = Integer32
_NetBotz_24hourpreferred_Object = MibScalar
netBotz_24hourpreferred = _NetBotz_24hourpreferred_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 25),
    _NetBotz_24hourpreferred_Type()
)
netBotz_24hourpreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_24hourpreferred.setStatus("mandatory")
_NetBotz_utc_clock_Type = Integer32
_NetBotz_utc_clock_Object = MibScalar
netBotz_utc_clock = _NetBotz_utc_clock_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 26),
    _NetBotz_utc_clock_Type()
)
netBotz_utc_clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_utc_clock.setStatus("mandatory")
_NetBotz_ismetric_Type = Integer32
_NetBotz_ismetric_Object = MibScalar
netBotz_ismetric = _NetBotz_ismetric_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 27),
    _NetBotz_ismetric_Type()
)
netBotz_ismetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotz_ismetric.setStatus("mandatory")
_NetBotz_alert_url_Type = DisplayString
_NetBotz_alert_url_Object = MibScalar
netBotz_alert_url = _NetBotz_alert_url_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 28),
    _NetBotz_alert_url_Type()
)
netBotz_alert_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_url.setStatus("mandatory")
_NetBotz_picture_alert_url_Type = DisplayString
_NetBotz_picture_alert_url_Object = MibScalar
netBotz_picture_alert_url = _NetBotz_picture_alert_url_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 29),
    _NetBotz_picture_alert_url_Type()
)
netBotz_picture_alert_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_picture_alert_url.setStatus("mandatory")
_NetBotz_sensor_data_url_Type = DisplayString
_NetBotz_sensor_data_url_Object = MibScalar
netBotz_sensor_data_url = _NetBotz_sensor_data_url_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 30),
    _NetBotz_sensor_data_url_Type()
)
netBotz_sensor_data_url.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url.setStatus("mandatory")
_NetBotz_alert_url_logon_Type = DisplayString
_NetBotz_alert_url_logon_Object = MibScalar
netBotz_alert_url_logon = _NetBotz_alert_url_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 31),
    _NetBotz_alert_url_logon_Type()
)
netBotz_alert_url_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_alert_url_logon.setStatus("mandatory")
_NetBotz_picture_alert_url_logon_Type = DisplayString
_NetBotz_picture_alert_url_logon_Object = MibScalar
netBotz_picture_alert_url_logon = _NetBotz_picture_alert_url_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 32),
    _NetBotz_picture_alert_url_logon_Type()
)
netBotz_picture_alert_url_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_picture_alert_url_logon.setStatus("mandatory")
_NetBotz_sensor_data_url_logon_Type = DisplayString
_NetBotz_sensor_data_url_logon_Object = MibScalar
netBotz_sensor_data_url_logon = _NetBotz_sensor_data_url_logon_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 33),
    _NetBotz_sensor_data_url_logon_Type()
)
netBotz_sensor_data_url_logon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url_logon.setStatus("mandatory")
_NetBotz_sensor_data_url_period_Type = Integer32
_NetBotz_sensor_data_url_period_Object = MibScalar
netBotz_sensor_data_url_period = _NetBotz_sensor_data_url_period_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 34),
    _NetBotz_sensor_data_url_period_Type()
)
netBotz_sensor_data_url_period.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url_period.setStatus("mandatory")
_NetBotz_sensor_data_url_flags_Type = Integer32
_NetBotz_sensor_data_url_flags_Object = MibScalar
netBotz_sensor_data_url_flags = _NetBotz_sensor_data_url_flags_Object(
    (1, 3, 6, 1, 4, 1, 5528, 50, 35),
    _NetBotz_sensor_data_url_flags_Type()
)
netBotz_sensor_data_url_flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBotz_sensor_data_url_flags.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETBOTZ-DEVICE-MIB",
    **{"netBotz-dev-host": netBotz_dev_host,
       "netBotz-dev-domain": netBotz_dev_domain,
       "netBotz-dev-ip": netBotz_dev_ip,
       "netBotz-dev-netmask": netBotz_dev_netmask,
       "netBotz-dev-gateway": netBotz_dev_gateway,
       "netBotz-dev-primarydns": netBotz_dev_primarydns,
       "netBotz-dev-secondarydns": netBotz_dev_secondarydns,
       "netBotz-dev-smtp": netBotz_dev_smtp,
       "netBotz-dev-smtpport": netBotz_dev_smtpport,
       "netBotz-dev-popport": netBotz_dev_popport,
       "netBotz-dev-loglevel": netBotz_dev_loglevel,
       "netBotz-dev-logaddress": netBotz_dev_logaddress,
       "netBotz-dev-logport": netBotz_dev_logport,
       "netBotz-dev-primaryemail": netBotz_dev_primaryemail,
       "netBotz-dev-secondaryemail": netBotz_dev_secondaryemail,
       "netBotz-dev-pager": netBotz_dev_pager,
       "netBotz-dev-serialno": netBotz_dev_serialno,
       "netBotz-dev-pop": netBotz_dev_pop,
       "netBotz-dev-version": netBotz_dev_version,
       "netBotz-dev-registered": netBotz_dev_registered,
       "netBotz-default-applet": netBotz_default_applet,
       "netBotz-guibar-color": netBotz_guibar_color,
       "netBotz-locale": netBotz_locale,
       "netBotz-timezone": netBotz_timezone,
       "netBotz-24hourpreferred": netBotz_24hourpreferred,
       "netBotz-utc-clock": netBotz_utc_clock,
       "netBotz-ismetric": netBotz_ismetric,
       "netBotz-alert-url": netBotz_alert_url,
       "netBotz-picture-alert-url": netBotz_picture_alert_url,
       "netBotz-sensor-data-url": netBotz_sensor_data_url,
       "netBotz-alert-url-logon": netBotz_alert_url_logon,
       "netBotz-picture-alert-url-logon": netBotz_picture_alert_url_logon,
       "netBotz-sensor-data-url-logon": netBotz_sensor_data_url_logon,
       "netBotz-sensor-data-url-period": netBotz_sensor_data_url_period,
       "netBotz-sensor-data-url-flags": netBotz_sensor_data_url_flags}
)
