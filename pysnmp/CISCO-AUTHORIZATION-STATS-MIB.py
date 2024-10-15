# SNMP MIB module (CISCO-AUTHORIZATION-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AUTHORIZATION-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoAuthorizationStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 343)
)
ciscoAuthorizationStatsMibModule.setRevisions(
        ("2006-11-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CStatsAuthorization_ObjectIdentity = ObjectIdentity
cStatsAuthorization = _CStatsAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1)
)
_CAuthorizationGlobal_ObjectIdentity = ObjectIdentity
cAuthorizationGlobal = _CAuthorizationGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 1)
)
_CAuthorizationStatsTable_Object = MibTable
cAuthorizationStatsTable = _CAuthorizationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2)
)
if mibBuilder.loadTexts:
    cAuthorizationStatsTable.setStatus("current")
_CAuthorizationStatsEntry_Object = MibTableRow
cAuthorizationStatsEntry = _CAuthorizationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1)
)
cAuthorizationStatsEntry.setIndexNames(
    (0, "CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizServerIndex"),
)
if mibBuilder.loadTexts:
    cAuthorizationStatsEntry.setStatus("current")


class _CAuthorizServerIndex_Type(Integer32):
    """Custom type cAuthorizServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CAuthorizServerIndex_Type.__name__ = "Integer32"
_CAuthorizServerIndex_Object = MibTableColumn
cAuthorizServerIndex = _CAuthorizServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 1),
    _CAuthorizServerIndex_Type()
)
cAuthorizServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAuthorizServerIndex.setStatus("current")
_CAuthorizServerAddressType_Type = InetAddressType
_CAuthorizServerAddressType_Object = MibTableColumn
cAuthorizServerAddressType = _CAuthorizServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 2),
    _CAuthorizServerAddressType_Type()
)
cAuthorizServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizServerAddressType.setStatus("current")
_CAuthorizServerAddress_Type = InetAddress
_CAuthorizServerAddress_Object = MibTableColumn
cAuthorizServerAddress = _CAuthorizServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 3),
    _CAuthorizServerAddress_Type()
)
cAuthorizServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizServerAddress.setStatus("current")
_CAuthorizClientServerPortNum_Type = CiscoPort
_CAuthorizClientServerPortNum_Object = MibTableColumn
cAuthorizClientServerPortNum = _CAuthorizClientServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 4),
    _CAuthorizClientServerPortNum_Type()
)
cAuthorizClientServerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientServerPortNum.setStatus("current")
_CAuthorizClientRoundTripTime_Type = TimeInterval
_CAuthorizClientRoundTripTime_Object = MibTableColumn
cAuthorizClientRoundTripTime = _CAuthorizClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 5),
    _CAuthorizClientRoundTripTime_Type()
)
cAuthorizClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientRoundTripTime.setStatus("current")
_CAuthorizClientAccessRequests_Type = Counter32
_CAuthorizClientAccessRequests_Object = MibTableColumn
cAuthorizClientAccessRequests = _CAuthorizClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 6),
    _CAuthorizClientAccessRequests_Type()
)
cAuthorizClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientAccessRequests.setStatus("current")
_CAuthorizClientAccessRetrans_Type = Counter32
_CAuthorizClientAccessRetrans_Object = MibTableColumn
cAuthorizClientAccessRetrans = _CAuthorizClientAccessRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 7),
    _CAuthorizClientAccessRetrans_Type()
)
cAuthorizClientAccessRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientAccessRetrans.setStatus("current")
_CAuthorizClientAccessAccepts_Type = Counter32
_CAuthorizClientAccessAccepts_Object = MibTableColumn
cAuthorizClientAccessAccepts = _CAuthorizClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 8),
    _CAuthorizClientAccessAccepts_Type()
)
cAuthorizClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientAccessAccepts.setStatus("current")
_CAuthorizClientAccessRejects_Type = Counter32
_CAuthorizClientAccessRejects_Object = MibTableColumn
cAuthorizClientAccessRejects = _CAuthorizClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 9),
    _CAuthorizClientAccessRejects_Type()
)
cAuthorizClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientAccessRejects.setStatus("current")
_CAuthorizClientAccessChallenges_Type = Counter32
_CAuthorizClientAccessChallenges_Object = MibTableColumn
cAuthorizClientAccessChallenges = _CAuthorizClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 10),
    _CAuthorizClientAccessChallenges_Type()
)
cAuthorizClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientAccessChallenges.setStatus("current")
_CAuthorizClientMalAccessResps_Type = Counter32
_CAuthorizClientMalAccessResps_Object = MibTableColumn
cAuthorizClientMalAccessResps = _CAuthorizClientMalAccessResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 11),
    _CAuthorizClientMalAccessResps_Type()
)
cAuthorizClientMalAccessResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientMalAccessResps.setStatus("current")
_CAuthorizClientBadAuthenticates_Type = Counter32
_CAuthorizClientBadAuthenticates_Object = MibTableColumn
cAuthorizClientBadAuthenticates = _CAuthorizClientBadAuthenticates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 12),
    _CAuthorizClientBadAuthenticates_Type()
)
cAuthorizClientBadAuthenticates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientBadAuthenticates.setStatus("current")
_CAuthorizClientPendingRequests_Type = Gauge32
_CAuthorizClientPendingRequests_Object = MibTableColumn
cAuthorizClientPendingRequests = _CAuthorizClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 13),
    _CAuthorizClientPendingRequests_Type()
)
cAuthorizClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientPendingRequests.setStatus("current")
_CAuthorizClientTimeouts_Type = Counter32
_CAuthorizClientTimeouts_Object = MibTableColumn
cAuthorizClientTimeouts = _CAuthorizClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 14),
    _CAuthorizClientTimeouts_Type()
)
cAuthorizClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientTimeouts.setStatus("current")
_CAuthorizClientUnknownTypes_Type = Counter32
_CAuthorizClientUnknownTypes_Object = MibTableColumn
cAuthorizClientUnknownTypes = _CAuthorizClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 15),
    _CAuthorizClientUnknownTypes_Type()
)
cAuthorizClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizClientUnknownTypes.setStatus("current")


class _CAuthorizServerGroupId_Type(Integer32):
    """Custom type cAuthorizServerGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CAuthorizServerGroupId_Type.__name__ = "Integer32"
_CAuthorizServerGroupId_Object = MibTableColumn
cAuthorizServerGroupId = _CAuthorizServerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 1, 2, 1, 16),
    _CAuthorizServerGroupId_Type()
)
cAuthorizServerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAuthorizServerGroupId.setStatus("current")
_CAuthorizationMIBConformance_ObjectIdentity = ObjectIdentity
cAuthorizationMIBConformance = _CAuthorizationMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 2)
)
_CAuthorizationMIBCompliances_ObjectIdentity = ObjectIdentity
cAuthorizationMIBCompliances = _CAuthorizationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 2, 1)
)
_CAuthorizationGroup_ObjectIdentity = ObjectIdentity
cAuthorizationGroup = _CAuthorizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 2, 2)
)

# Managed Objects groups

cAuthorizationClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 2, 2, 1)
)
cAuthorizationClientMIBGroup.setObjects(
      *(("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizServerAddressType"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizServerAddress"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientServerPortNum"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientRoundTripTime"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientAccessRequests"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientAccessRetrans"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientAccessAccepts"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientAccessRejects"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientAccessChallenges"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientMalAccessResps"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientBadAuthenticates"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientPendingRequests"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientTimeouts"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizClientUnknownTypes"),
        ("CISCO-AUTHORIZATION-STATS-MIB", "cAuthorizServerGroupId"))
)
if mibBuilder.loadTexts:
    cAuthorizationClientMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cAuthorizationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 343, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cAuthorizationMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AUTHORIZATION-STATS-MIB",
    **{"ciscoAuthorizationStatsMibModule": ciscoAuthorizationStatsMibModule,
       "cStatsAuthorization": cStatsAuthorization,
       "cAuthorizationGlobal": cAuthorizationGlobal,
       "cAuthorizationStatsTable": cAuthorizationStatsTable,
       "cAuthorizationStatsEntry": cAuthorizationStatsEntry,
       "cAuthorizServerIndex": cAuthorizServerIndex,
       "cAuthorizServerAddressType": cAuthorizServerAddressType,
       "cAuthorizServerAddress": cAuthorizServerAddress,
       "cAuthorizClientServerPortNum": cAuthorizClientServerPortNum,
       "cAuthorizClientRoundTripTime": cAuthorizClientRoundTripTime,
       "cAuthorizClientAccessRequests": cAuthorizClientAccessRequests,
       "cAuthorizClientAccessRetrans": cAuthorizClientAccessRetrans,
       "cAuthorizClientAccessAccepts": cAuthorizClientAccessAccepts,
       "cAuthorizClientAccessRejects": cAuthorizClientAccessRejects,
       "cAuthorizClientAccessChallenges": cAuthorizClientAccessChallenges,
       "cAuthorizClientMalAccessResps": cAuthorizClientMalAccessResps,
       "cAuthorizClientBadAuthenticates": cAuthorizClientBadAuthenticates,
       "cAuthorizClientPendingRequests": cAuthorizClientPendingRequests,
       "cAuthorizClientTimeouts": cAuthorizClientTimeouts,
       "cAuthorizClientUnknownTypes": cAuthorizClientUnknownTypes,
       "cAuthorizServerGroupId": cAuthorizServerGroupId,
       "cAuthorizationMIBConformance": cAuthorizationMIBConformance,
       "cAuthorizationMIBCompliances": cAuthorizationMIBCompliances,
       "cAuthorizationMIBCompliance": cAuthorizationMIBCompliance,
       "cAuthorizationGroup": cAuthorizationGroup,
       "cAuthorizationClientMIBGroup": cAuthorizationClientMIBGroup}
)
