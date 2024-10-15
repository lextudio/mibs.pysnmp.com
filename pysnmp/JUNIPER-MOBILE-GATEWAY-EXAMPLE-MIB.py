# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:46 2024
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

(jnxExampleMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxExampleMibRoot")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMobileGatewayExampleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2)
)
jnxMobileGatewayExampleMib.setRevisions(
        ("2010-11-22 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMobileGatewayExampleObjects_ObjectIdentity = ObjectIdentity
jnxMobileGatewayExampleObjects = _JnxMobileGatewayExampleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1)
)
_JnxMobileGatewayExampleSyncStats_ObjectIdentity = ObjectIdentity
jnxMobileGatewayExampleSyncStats = _JnxMobileGatewayExampleSyncStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1)
)
_JnxMobileGatewayTotalRequests_Type = Counter64
_JnxMobileGatewayTotalRequests_Object = MibScalar
jnxMobileGatewayTotalRequests = _JnxMobileGatewayTotalRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 1),
    _JnxMobileGatewayTotalRequests_Type()
)
jnxMobileGatewayTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalRequests.setStatus("current")
_JnxMobileGatewayTotalAccepts_Type = Counter64
_JnxMobileGatewayTotalAccepts_Object = MibScalar
jnxMobileGatewayTotalAccepts = _JnxMobileGatewayTotalAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 2),
    _JnxMobileGatewayTotalAccepts_Type()
)
jnxMobileGatewayTotalAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalAccepts.setStatus("current")
_JnxMobileGatewayTotalRejects_Type = Counter64
_JnxMobileGatewayTotalRejects_Object = MibScalar
jnxMobileGatewayTotalRejects = _JnxMobileGatewayTotalRejects_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 3),
    _JnxMobileGatewayTotalRejects_Type()
)
jnxMobileGatewayTotalRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalRejects.setStatus("current")
_JnxMobileGatewayTotalChallenges_Type = Counter64
_JnxMobileGatewayTotalChallenges_Object = MibScalar
jnxMobileGatewayTotalChallenges = _JnxMobileGatewayTotalChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 1, 4),
    _JnxMobileGatewayTotalChallenges_Type()
)
jnxMobileGatewayTotalChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalChallenges.setStatus("current")
_JnxMobileGatewayExampleAsyncStats_ObjectIdentity = ObjectIdentity
jnxMobileGatewayExampleAsyncStats = _JnxMobileGatewayExampleAsyncStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2)
)
_JnxMobileGatewayTotalRequestTimeouts_Type = Counter64
_JnxMobileGatewayTotalRequestTimeouts_Object = MibScalar
jnxMobileGatewayTotalRequestTimeouts = _JnxMobileGatewayTotalRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 1),
    _JnxMobileGatewayTotalRequestTimeouts_Type()
)
jnxMobileGatewayTotalRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalRequestTimeouts.setStatus("current")
_JnxMobileGatewayTotalRequestTxErrors_Type = Counter64
_JnxMobileGatewayTotalRequestTxErrors_Object = MibScalar
jnxMobileGatewayTotalRequestTxErrors = _JnxMobileGatewayTotalRequestTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 2),
    _JnxMobileGatewayTotalRequestTxErrors_Type()
)
jnxMobileGatewayTotalRequestTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalRequestTxErrors.setStatus("current")
_JnxMobileGatewayTotalResponseErrors_Type = Counter64
_JnxMobileGatewayTotalResponseErrors_Object = MibScalar
jnxMobileGatewayTotalResponseErrors = _JnxMobileGatewayTotalResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 3),
    _JnxMobileGatewayTotalResponseErrors_Type()
)
jnxMobileGatewayTotalResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalResponseErrors.setStatus("current")
_JnxMobileGatewayTotalPendingRequests_Type = Counter64
_JnxMobileGatewayTotalPendingRequests_Object = MibScalar
jnxMobileGatewayTotalPendingRequests = _JnxMobileGatewayTotalPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 2, 4),
    _JnxMobileGatewayTotalPendingRequests_Type()
)
jnxMobileGatewayTotalPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayTotalPendingRequests.setStatus("current")
_JnxMobileGatewayProfileTable_Object = MibTable
jnxMobileGatewayProfileTable = _JnxMobileGatewayProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    jnxMobileGatewayProfileTable.setStatus("current")
_JnxMobileGatewayProfileEntry_Object = MibTableRow
jnxMobileGatewayProfileEntry = _JnxMobileGatewayProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1)
)
jnxMobileGatewayProfileEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayProfileName"),
)
if mibBuilder.loadTexts:
    jnxMobileGatewayProfileEntry.setStatus("current")
_JnxMobileGatewayProfileName_Type = DisplayString
_JnxMobileGatewayProfileName_Object = MibTableColumn
jnxMobileGatewayProfileName = _JnxMobileGatewayProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1, 1),
    _JnxMobileGatewayProfileName_Type()
)
jnxMobileGatewayProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMobileGatewayProfileName.setStatus("current")
_JnxMobileGatewayProfileDescription_Type = DisplayString
_JnxMobileGatewayProfileDescription_Object = MibTableColumn
jnxMobileGatewayProfileDescription = _JnxMobileGatewayProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1, 2),
    _JnxMobileGatewayProfileDescription_Type()
)
jnxMobileGatewayProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayProfileDescription.setStatus("current")
_JnxMobileGatewayProfileType_Type = Integer32
_JnxMobileGatewayProfileType_Object = MibTableColumn
jnxMobileGatewayProfileType = _JnxMobileGatewayProfileType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 3, 1, 3),
    _JnxMobileGatewayProfileType_Type()
)
jnxMobileGatewayProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMobileGatewayProfileType.setStatus("current")
_JnxMobileGatewayExampleNotificationVars_ObjectIdentity = ObjectIdentity
jnxMobileGatewayExampleNotificationVars = _JnxMobileGatewayExampleNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4)
)
_JnxMobileGatewayExampleServerName_Type = DisplayString
_JnxMobileGatewayExampleServerName_Object = MibScalar
jnxMobileGatewayExampleServerName = _JnxMobileGatewayExampleServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4, 1),
    _JnxMobileGatewayExampleServerName_Type()
)
jnxMobileGatewayExampleServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMobileGatewayExampleServerName.setStatus("current")
_JnxMobileGatewayExampleServicePicName_Type = DisplayString
_JnxMobileGatewayExampleServicePicName_Object = MibScalar
jnxMobileGatewayExampleServicePicName = _JnxMobileGatewayExampleServicePicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4, 2),
    _JnxMobileGatewayExampleServicePicName_Type()
)
jnxMobileGatewayExampleServicePicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMobileGatewayExampleServicePicName.setStatus("current")
_JnxMobileGatewayExampleServerState_Type = DisplayString
_JnxMobileGatewayExampleServerState_Object = MibScalar
jnxMobileGatewayExampleServerState = _JnxMobileGatewayExampleServerState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 1, 4, 3),
    _JnxMobileGatewayExampleServerState_Type()
)
jnxMobileGatewayExampleServerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMobileGatewayExampleServerState.setStatus("current")
_JnxMobileGatewayExampleNotifications_ObjectIdentity = ObjectIdentity
jnxMobileGatewayExampleNotifications = _JnxMobileGatewayExampleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 2)
)

# Managed Objects groups


# Notification objects

jnxMobileGatewayExampleServerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 5, 2, 2, 1)
)
jnxMobileGatewayExampleServerStatus.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayExampleServerName"),
        ("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayExampleServicePicName"),
        ("JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB", "jnxMobileGatewayExampleServerState"))
)
if mibBuilder.loadTexts:
    jnxMobileGatewayExampleServerStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-EXAMPLE-MIB",
    **{"jnxMobileGatewayExampleMib": jnxMobileGatewayExampleMib,
       "jnxMobileGatewayExampleObjects": jnxMobileGatewayExampleObjects,
       "jnxMobileGatewayExampleSyncStats": jnxMobileGatewayExampleSyncStats,
       "jnxMobileGatewayTotalRequests": jnxMobileGatewayTotalRequests,
       "jnxMobileGatewayTotalAccepts": jnxMobileGatewayTotalAccepts,
       "jnxMobileGatewayTotalRejects": jnxMobileGatewayTotalRejects,
       "jnxMobileGatewayTotalChallenges": jnxMobileGatewayTotalChallenges,
       "jnxMobileGatewayExampleAsyncStats": jnxMobileGatewayExampleAsyncStats,
       "jnxMobileGatewayTotalRequestTimeouts": jnxMobileGatewayTotalRequestTimeouts,
       "jnxMobileGatewayTotalRequestTxErrors": jnxMobileGatewayTotalRequestTxErrors,
       "jnxMobileGatewayTotalResponseErrors": jnxMobileGatewayTotalResponseErrors,
       "jnxMobileGatewayTotalPendingRequests": jnxMobileGatewayTotalPendingRequests,
       "jnxMobileGatewayProfileTable": jnxMobileGatewayProfileTable,
       "jnxMobileGatewayProfileEntry": jnxMobileGatewayProfileEntry,
       "jnxMobileGatewayProfileName": jnxMobileGatewayProfileName,
       "jnxMobileGatewayProfileDescription": jnxMobileGatewayProfileDescription,
       "jnxMobileGatewayProfileType": jnxMobileGatewayProfileType,
       "jnxMobileGatewayExampleNotificationVars": jnxMobileGatewayExampleNotificationVars,
       "jnxMobileGatewayExampleServerName": jnxMobileGatewayExampleServerName,
       "jnxMobileGatewayExampleServicePicName": jnxMobileGatewayExampleServicePicName,
       "jnxMobileGatewayExampleServerState": jnxMobileGatewayExampleServerState,
       "jnxMobileGatewayExampleNotifications": jnxMobileGatewayExampleNotifications,
       "jnxMobileGatewayExampleServerStatus": jnxMobileGatewayExampleServerStatus}
)
