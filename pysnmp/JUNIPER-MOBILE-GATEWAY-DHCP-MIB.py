# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:45 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(jnxMobileGatewayMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMobileGatewayMibRoot")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMbgDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8)
)
jnxMbgDhcpMib.setRevisions(
        ("2011-03-30 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgDhcpNotifications_ObjectIdentity = ObjectIdentity
jnxMbgDhcpNotifications = _JnxMbgDhcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 0)
)
_JnxMbgDhcpObjects_ObjectIdentity = ObjectIdentity
jnxMbgDhcpObjects = _JnxMbgDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1)
)
_JnxMbgDhcpNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgDhcpNotificationVars = _JnxMbgDhcpNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1)
)
_JnxMbgDhcpServerIP_Type = IpAddress
_JnxMbgDhcpServerIP_Object = MibScalar
jnxMbgDhcpServerIP = _JnxMbgDhcpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 1),
    _JnxMbgDhcpServerIP_Type()
)
jnxMbgDhcpServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgDhcpServerIP.setStatus("current")
_JnxMbgDhcpLogicalSystemName_Type = DisplayString
_JnxMbgDhcpLogicalSystemName_Object = MibScalar
jnxMbgDhcpLogicalSystemName = _JnxMbgDhcpLogicalSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 2),
    _JnxMbgDhcpLogicalSystemName_Type()
)
jnxMbgDhcpLogicalSystemName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgDhcpLogicalSystemName.setStatus("current")
_JnxMbgDhcpRoutingInstanceName_Type = DisplayString
_JnxMbgDhcpRoutingInstanceName_Object = MibScalar
jnxMbgDhcpRoutingInstanceName = _JnxMbgDhcpRoutingInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 3),
    _JnxMbgDhcpRoutingInstanceName_Type()
)
jnxMbgDhcpRoutingInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgDhcpRoutingInstanceName.setStatus("current")
_JnxMbgDhcpProfileName_Type = DisplayString
_JnxMbgDhcpProfileName_Object = MibScalar
jnxMbgDhcpProfileName = _JnxMbgDhcpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 4),
    _JnxMbgDhcpProfileName_Type()
)
jnxMbgDhcpProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgDhcpProfileName.setStatus("current")
_JnxMbgDhcpPoolName_Type = DisplayString
_JnxMbgDhcpPoolName_Object = MibScalar
jnxMbgDhcpPoolName = _JnxMbgDhcpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 5),
    _JnxMbgDhcpPoolName_Type()
)
jnxMbgDhcpPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgDhcpPoolName.setStatus("current")
_JnxMbgDhcpReachability_Type = TruthValue
_JnxMbgDhcpReachability_Object = MibScalar
jnxMbgDhcpReachability = _JnxMbgDhcpReachability_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 1, 1, 6),
    _JnxMbgDhcpReachability_Type()
)
jnxMbgDhcpReachability.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgDhcpReachability.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgDhcpServerReachability = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 0, 1)
)
jnxMbgDhcpServerReachability.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpServerIP"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpLogicalSystemName"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpRoutingInstanceName"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpProfileName"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpReachability"))
)
if mibBuilder.loadTexts:
    jnxMbgDhcpServerReachability.setStatus(
        "current"
    )

jnxMbgDhcpAddrPoolExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 8, 0, 2)
)
jnxMbgDhcpAddrPoolExhaust.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpServerIP"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpLogicalSystemName"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpRoutingInstanceName"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpProfileName"),
        ("JUNIPER-MOBILE-GATEWAY-DHCP-MIB", "jnxMbgDhcpPoolName"))
)
if mibBuilder.loadTexts:
    jnxMbgDhcpAddrPoolExhaust.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-DHCP-MIB",
    **{"jnxMbgDhcpMib": jnxMbgDhcpMib,
       "jnxMbgDhcpNotifications": jnxMbgDhcpNotifications,
       "jnxMbgDhcpServerReachability": jnxMbgDhcpServerReachability,
       "jnxMbgDhcpAddrPoolExhaust": jnxMbgDhcpAddrPoolExhaust,
       "jnxMbgDhcpObjects": jnxMbgDhcpObjects,
       "jnxMbgDhcpNotificationVars": jnxMbgDhcpNotificationVars,
       "jnxMbgDhcpServerIP": jnxMbgDhcpServerIP,
       "jnxMbgDhcpLogicalSystemName": jnxMbgDhcpLogicalSystemName,
       "jnxMbgDhcpRoutingInstanceName": jnxMbgDhcpRoutingInstanceName,
       "jnxMbgDhcpProfileName": jnxMbgDhcpProfileName,
       "jnxMbgDhcpPoolName": jnxMbgDhcpPoolName,
       "jnxMbgDhcpReachability": jnxMbgDhcpReachability}
)
