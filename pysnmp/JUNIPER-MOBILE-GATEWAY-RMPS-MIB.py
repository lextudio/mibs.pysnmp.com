# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-RMPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-RMPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:48 2024
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(jnxMbgGwName,) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxMbgRMPSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7)
)
jnxMbgRMPSMib.setRevisions(
        ("2011-03-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgRMPSNotifications_ObjectIdentity = ObjectIdentity
jnxMbgRMPSNotifications = _JnxMbgRMPSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 0)
)
_JnxMbgRMPSObjects_ObjectIdentity = ObjectIdentity
jnxMbgRMPSObjects = _JnxMbgRMPSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 1)
)
_JnxMbgRMPSNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgRMPSNotificationVars = _JnxMbgRMPSNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 1, 5)
)
_JnxMbgRMPSClientIdentifier_Type = DisplayString
_JnxMbgRMPSClientIdentifier_Object = MibScalar
jnxMbgRMPSClientIdentifier = _JnxMbgRMPSClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 1, 5, 1),
    _JnxMbgRMPSClientIdentifier_Type()
)
jnxMbgRMPSClientIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgRMPSClientIdentifier.setStatus("current")


class _JnxMbgRMPSClientStatus_Type(Integer32):
    """Custom type jnxMbgRMPSClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inService", 0),
          ("outOfService", 1))
    )


_JnxMbgRMPSClientStatus_Type.__name__ = "Integer32"
_JnxMbgRMPSClientStatus_Object = MibScalar
jnxMbgRMPSClientStatus = _JnxMbgRMPSClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 1, 5, 2),
    _JnxMbgRMPSClientStatus_Type()
)
jnxMbgRMPSClientStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgRMPSClientStatus.setStatus("current")


class _JnxMbgRMPSServiceStatus_Type(Integer32):
    """Custom type jnxMbgRMPSServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 0))
    )


_JnxMbgRMPSServiceStatus_Type.__name__ = "Integer32"
_JnxMbgRMPSServiceStatus_Object = MibScalar
jnxMbgRMPSServiceStatus = _JnxMbgRMPSServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 1, 5, 3),
    _JnxMbgRMPSServiceStatus_Type()
)
jnxMbgRMPSServiceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgRMPSServiceStatus.setStatus("current")


class _JnxMbgRMPSClientRedundancyRole_Type(Integer32):
    """Custom type jnxMbgRMPSClientRedundancyRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("primary", 1),
          ("secondary", 2),
          ("standalone", 3))
    )


_JnxMbgRMPSClientRedundancyRole_Type.__name__ = "Integer32"
_JnxMbgRMPSClientRedundancyRole_Object = MibScalar
jnxMbgRMPSClientRedundancyRole = _JnxMbgRMPSClientRedundancyRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 1, 5, 4),
    _JnxMbgRMPSClientRedundancyRole_Type()
)
jnxMbgRMPSClientRedundancyRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgRMPSClientRedundancyRole.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgRMPSServiceStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 0, 1)
)
jnxMbgRMPSServiceStatusChange.setObjects(
    ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSServiceStatus")
)
if mibBuilder.loadTexts:
    jnxMbgRMPSServiceStatusChange.setStatus(
        "current"
    )

jnxMbgRMPSClientStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 0, 2)
)
jnxMbgRMPSClientStatusChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgRMPSClientStatusChange.setStatus(
        "deprecated"
    )

jnxMbgRMPSClientInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 0, 3)
)
jnxMbgRMPSClientInfo.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientStatus"),
        ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientRedundancyRole"))
)
if mibBuilder.loadTexts:
    jnxMbgRMPSClientInfo.setStatus(
        "deprecated"
    )

jnxMbgRMPSClientStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 7, 0, 4)
)
jnxMbgRMPSClientStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientIdentifier"),
        ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientRedundancyRole"),
        ("JUNIPER-MOBILE-GATEWAY-RMPS-MIB", "jnxMbgRMPSClientStatus"))
)
if mibBuilder.loadTexts:
    jnxMbgRMPSClientStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-RMPS-MIB",
    **{"jnxMbgRMPSMib": jnxMbgRMPSMib,
       "jnxMbgRMPSNotifications": jnxMbgRMPSNotifications,
       "jnxMbgRMPSServiceStatusChange": jnxMbgRMPSServiceStatusChange,
       "jnxMbgRMPSClientStatusChange": jnxMbgRMPSClientStatusChange,
       "jnxMbgRMPSClientInfo": jnxMbgRMPSClientInfo,
       "jnxMbgRMPSClientStateChange": jnxMbgRMPSClientStateChange,
       "jnxMbgRMPSObjects": jnxMbgRMPSObjects,
       "jnxMbgRMPSNotificationVars": jnxMbgRMPSNotificationVars,
       "jnxMbgRMPSClientIdentifier": jnxMbgRMPSClientIdentifier,
       "jnxMbgRMPSClientStatus": jnxMbgRMPSClientStatus,
       "jnxMbgRMPSServiceStatus": jnxMbgRMPSServiceStatus,
       "jnxMbgRMPSClientRedundancyRole": jnxMbgRMPSClientRedundancyRole}
)
