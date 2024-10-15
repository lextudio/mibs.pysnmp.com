# SNMP MIB module (WWP-RADIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-RADIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:22 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpRadiusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11)
)
wwpRadiusClientMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpRadiusClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpRadiusClientMIBObjects = _WwpRadiusClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1)
)
_WwpRadiusClient_ObjectIdentity = ObjectIdentity
wwpRadiusClient = _WwpRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1)
)


class _WwpRadiusClientTimeout_Type(Integer32):
    """Custom type wwpRadiusClientTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WwpRadiusClientTimeout_Type.__name__ = "Integer32"
_WwpRadiusClientTimeout_Object = MibScalar
wwpRadiusClientTimeout = _WwpRadiusClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 1),
    _WwpRadiusClientTimeout_Type()
)
wwpRadiusClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpRadiusClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpRadiusClientTimeout.setUnits("seconds")


class _WwpRadiusClientRetries_Type(Integer32):
    """Custom type wwpRadiusClientRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpRadiusClientRetries_Type.__name__ = "Integer32"
_WwpRadiusClientRetries_Object = MibScalar
wwpRadiusClientRetries = _WwpRadiusClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 2),
    _WwpRadiusClientRetries_Type()
)
wwpRadiusClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpRadiusClientRetries.setStatus("current")
_WwpRadiusServerTable_Object = MibTable
wwpRadiusServerTable = _WwpRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpRadiusServerTable.setStatus("current")
_WwpRadiusServerEntry_Object = MibTableRow
wwpRadiusServerEntry = _WwpRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1)
)
wwpRadiusServerEntry.setIndexNames(
    (0, "WWP-RADIUS-CLIENT-MIB", "wwpRadiusServerId"),
)
if mibBuilder.loadTexts:
    wwpRadiusServerEntry.setStatus("current")


class _WwpRadiusServerId_Type(Integer32):
    """Custom type wwpRadiusServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpRadiusServerId_Type.__name__ = "Integer32"
_WwpRadiusServerId_Object = MibTableColumn
wwpRadiusServerId = _WwpRadiusServerId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 1),
    _WwpRadiusServerId_Type()
)
wwpRadiusServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusServerId.setStatus("current")
_WwpRadiusServerIpAddr_Type = IpAddress
_WwpRadiusServerIpAddr_Object = MibTableColumn
wwpRadiusServerIpAddr = _WwpRadiusServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 2),
    _WwpRadiusServerIpAddr_Type()
)
wwpRadiusServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpRadiusServerIpAddr.setStatus("current")


class _WwpRadiusServerAuthPort_Type(Integer32):
    """Custom type wwpRadiusServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpRadiusServerAuthPort_Type.__name__ = "Integer32"
_WwpRadiusServerAuthPort_Object = MibTableColumn
wwpRadiusServerAuthPort = _WwpRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 3),
    _WwpRadiusServerAuthPort_Type()
)
wwpRadiusServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpRadiusServerAuthPort.setStatus("current")
_WwpRadiusClientRoundTripTime_Type = TimeTicks
_WwpRadiusClientRoundTripTime_Object = MibTableColumn
wwpRadiusClientRoundTripTime = _WwpRadiusClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 4),
    _WwpRadiusClientRoundTripTime_Type()
)
wwpRadiusClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientRoundTripTime.setStatus("current")
_WwpRadiusClientAccessRequests_Type = Counter32
_WwpRadiusClientAccessRequests_Object = MibTableColumn
wwpRadiusClientAccessRequests = _WwpRadiusClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 5),
    _WwpRadiusClientAccessRequests_Type()
)
wwpRadiusClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientAccessRequests.setStatus("current")
_WwpRadiusClientAccessRetransmissions_Type = Counter32
_WwpRadiusClientAccessRetransmissions_Object = MibTableColumn
wwpRadiusClientAccessRetransmissions = _WwpRadiusClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 6),
    _WwpRadiusClientAccessRetransmissions_Type()
)
wwpRadiusClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientAccessRetransmissions.setStatus("current")
_WwpRadiusClientAccessAccepts_Type = Counter32
_WwpRadiusClientAccessAccepts_Object = MibTableColumn
wwpRadiusClientAccessAccepts = _WwpRadiusClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 7),
    _WwpRadiusClientAccessAccepts_Type()
)
wwpRadiusClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientAccessAccepts.setStatus("current")
_WwpRadiusClientAccessRejects_Type = Counter32
_WwpRadiusClientAccessRejects_Object = MibTableColumn
wwpRadiusClientAccessRejects = _WwpRadiusClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 8),
    _WwpRadiusClientAccessRejects_Type()
)
wwpRadiusClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientAccessRejects.setStatus("current")
_WwpRadiusClientAccessChallenges_Type = Counter32
_WwpRadiusClientAccessChallenges_Object = MibTableColumn
wwpRadiusClientAccessChallenges = _WwpRadiusClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 9),
    _WwpRadiusClientAccessChallenges_Type()
)
wwpRadiusClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientAccessChallenges.setStatus("current")
_WwpRadiusClientMalformedAccessResponses_Type = Counter32
_WwpRadiusClientMalformedAccessResponses_Object = MibTableColumn
wwpRadiusClientMalformedAccessResponses = _WwpRadiusClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 10),
    _WwpRadiusClientMalformedAccessResponses_Type()
)
wwpRadiusClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientMalformedAccessResponses.setStatus("current")
_WwpRadiusClientBadAuthenticators_Type = Counter32
_WwpRadiusClientBadAuthenticators_Object = MibTableColumn
wwpRadiusClientBadAuthenticators = _WwpRadiusClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 11),
    _WwpRadiusClientBadAuthenticators_Type()
)
wwpRadiusClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientBadAuthenticators.setStatus("current")
_WwpRadiusClientPendingRequests_Type = Gauge32
_WwpRadiusClientPendingRequests_Object = MibTableColumn
wwpRadiusClientPendingRequests = _WwpRadiusClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 12),
    _WwpRadiusClientPendingRequests_Type()
)
wwpRadiusClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientPendingRequests.setStatus("current")
_WwpRadiusClientTimeouts_Type = Counter32
_WwpRadiusClientTimeouts_Object = MibTableColumn
wwpRadiusClientTimeouts = _WwpRadiusClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 13),
    _WwpRadiusClientTimeouts_Type()
)
wwpRadiusClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientTimeouts.setStatus("current")
_WwpRadiusClientUnknownTypes_Type = Counter32
_WwpRadiusClientUnknownTypes_Object = MibTableColumn
wwpRadiusClientUnknownTypes = _WwpRadiusClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 14),
    _WwpRadiusClientUnknownTypes_Type()
)
wwpRadiusClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientUnknownTypes.setStatus("current")
_WwpRadiusClientPacketsDropped_Type = Counter32
_WwpRadiusClientPacketsDropped_Object = MibTableColumn
wwpRadiusClientPacketsDropped = _WwpRadiusClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 15),
    _WwpRadiusClientPacketsDropped_Type()
)
wwpRadiusClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpRadiusClientPacketsDropped.setStatus("current")
_WwpRadiusServerStatus_Type = RowStatus
_WwpRadiusServerStatus_Object = MibTableColumn
wwpRadiusServerStatus = _WwpRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 3, 1, 16),
    _WwpRadiusServerStatus_Type()
)
wwpRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpRadiusServerStatus.setStatus("current")


class _WwpRadiusClientAuthKey_Type(OctetString):
    """Custom type wwpRadiusClientAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 127),
    )


_WwpRadiusClientAuthKey_Type.__name__ = "OctetString"
_WwpRadiusClientAuthKey_Object = MibScalar
wwpRadiusClientAuthKey = _WwpRadiusClientAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 1, 1, 4),
    _WwpRadiusClientAuthKey_Type()
)
wwpRadiusClientAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpRadiusClientAuthKey.setStatus("current")
_WwpRadiusClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpRadiusClientMIBNotificationPrefix = _WwpRadiusClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 2)
)
_WwpRadiusClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpRadiusClientMIBNotifications = _WwpRadiusClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 2, 0)
)
_WwpRadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpRadiusClientMIBConformance = _WwpRadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 3)
)
_WwpRadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpRadiusClientMIBCompliances = _WwpRadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 3, 1)
)
_WwpRadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpRadiusClientMIBGroups = _WwpRadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 11, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-RADIUS-CLIENT-MIB",
    **{"wwpRadiusClientMIB": wwpRadiusClientMIB,
       "wwpRadiusClientMIBObjects": wwpRadiusClientMIBObjects,
       "wwpRadiusClient": wwpRadiusClient,
       "wwpRadiusClientTimeout": wwpRadiusClientTimeout,
       "wwpRadiusClientRetries": wwpRadiusClientRetries,
       "wwpRadiusServerTable": wwpRadiusServerTable,
       "wwpRadiusServerEntry": wwpRadiusServerEntry,
       "wwpRadiusServerId": wwpRadiusServerId,
       "wwpRadiusServerIpAddr": wwpRadiusServerIpAddr,
       "wwpRadiusServerAuthPort": wwpRadiusServerAuthPort,
       "wwpRadiusClientRoundTripTime": wwpRadiusClientRoundTripTime,
       "wwpRadiusClientAccessRequests": wwpRadiusClientAccessRequests,
       "wwpRadiusClientAccessRetransmissions": wwpRadiusClientAccessRetransmissions,
       "wwpRadiusClientAccessAccepts": wwpRadiusClientAccessAccepts,
       "wwpRadiusClientAccessRejects": wwpRadiusClientAccessRejects,
       "wwpRadiusClientAccessChallenges": wwpRadiusClientAccessChallenges,
       "wwpRadiusClientMalformedAccessResponses": wwpRadiusClientMalformedAccessResponses,
       "wwpRadiusClientBadAuthenticators": wwpRadiusClientBadAuthenticators,
       "wwpRadiusClientPendingRequests": wwpRadiusClientPendingRequests,
       "wwpRadiusClientTimeouts": wwpRadiusClientTimeouts,
       "wwpRadiusClientUnknownTypes": wwpRadiusClientUnknownTypes,
       "wwpRadiusClientPacketsDropped": wwpRadiusClientPacketsDropped,
       "wwpRadiusServerStatus": wwpRadiusServerStatus,
       "wwpRadiusClientAuthKey": wwpRadiusClientAuthKey,
       "wwpRadiusClientMIBNotificationPrefix": wwpRadiusClientMIBNotificationPrefix,
       "wwpRadiusClientMIBNotifications": wwpRadiusClientMIBNotifications,
       "wwpRadiusClientMIBConformance": wwpRadiusClientMIBConformance,
       "wwpRadiusClientMIBCompliances": wwpRadiusClientMIBCompliances,
       "wwpRadiusClientMIBGroups": wwpRadiusClientMIBGroups}
)
