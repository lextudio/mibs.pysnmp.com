# SNMP MIB module (CIENA-CES-RADIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-RADIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:06 2024
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

(cienaCesStatistics,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesStatistics")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

cienaCesRadiusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3)
)
cienaCesRadiusClientMIB.setRevisions(
        ("2016-02-17 00:00",
         "2015-07-22 00:00",
         "2015-06-22 00:00",
         "2014-06-12 00:00",
         "2014-01-02 00:00",
         "2012-04-17 00:00",
         "2010-05-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadiusString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 64),
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesRadiusClientMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientMIBObjects = _CienaCesRadiusClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1)
)
_CienaCesRadiusClient_ObjectIdentity = ObjectIdentity
cienaCesRadiusClient = _CienaCesRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1)
)
_CienaCesRadiusClientGlobal_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientGlobal = _CienaCesRadiusClientGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1)
)
_CienaCesRadiusAdminState_Type = CienaGlobalState
_CienaCesRadiusAdminState_Object = MibScalar
cienaCesRadiusAdminState = _CienaCesRadiusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 1),
    _CienaCesRadiusAdminState_Type()
)
cienaCesRadiusAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusAdminState.setStatus("current")
_CienaCesRadiusOperState_Type = CienaGlobalState
_CienaCesRadiusOperState_Object = MibScalar
cienaCesRadiusOperState = _CienaCesRadiusOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 2),
    _CienaCesRadiusOperState_Type()
)
cienaCesRadiusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusOperState.setStatus("current")


class _CienaCesRadiusClientTimeout_Type(Integer32):
    """Custom type cienaCesRadiusClientTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesRadiusClientTimeout_Type.__name__ = "Integer32"
_CienaCesRadiusClientTimeout_Object = MibScalar
cienaCesRadiusClientTimeout = _CienaCesRadiusClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 3),
    _CienaCesRadiusClientTimeout_Type()
)
cienaCesRadiusClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusClientTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    cienaCesRadiusClientTimeout.setUnits("seconds")


class _CienaCesRadiusClientRetries_Type(Integer32):
    """Custom type cienaCesRadiusClientRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesRadiusClientRetries_Type.__name__ = "Integer32"
_CienaCesRadiusClientRetries_Object = MibScalar
cienaCesRadiusClientRetries = _CienaCesRadiusClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 4),
    _CienaCesRadiusClientRetries_Type()
)
cienaCesRadiusClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusClientRetries.setStatus("deprecated")
_CienaCesRadiusClientAuthKey_Type = RadiusString
_CienaCesRadiusClientAuthKey_Object = MibScalar
cienaCesRadiusClientAuthKey = _CienaCesRadiusClientAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 5),
    _CienaCesRadiusClientAuthKey_Type()
)
cienaCesRadiusClientAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusClientAuthKey.setStatus("deprecated")
_CienaCesRadiusClientAuthKeyUnset_Type = TruthValue
_CienaCesRadiusClientAuthKeyUnset_Object = MibScalar
cienaCesRadiusClientAuthKeyUnset = _CienaCesRadiusClientAuthKeyUnset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 6),
    _CienaCesRadiusClientAuthKeyUnset_Type()
)
cienaCesRadiusClientAuthKeyUnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusClientAuthKeyUnset.setStatus("deprecated")


class _CienaCesRadiusClientSearchType_Type(Integer32):
    """Custom type cienaCesRadiusClientSearchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cached", 1),
          ("priority", 2))
    )


_CienaCesRadiusClientSearchType_Type.__name__ = "Integer32"
_CienaCesRadiusClientSearchType_Object = MibScalar
cienaCesRadiusClientSearchType = _CienaCesRadiusClientSearchType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 1, 7),
    _CienaCesRadiusClientSearchType_Type()
)
cienaCesRadiusClientSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusClientSearchType.setStatus("deprecated")
_CienaCesRadiusClientServer_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientServer = _CienaCesRadiusClientServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2)
)
_CienaCesRadiusClientServerTable_Object = MibTable
cienaCesRadiusClientServerTable = _CienaCesRadiusClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerTable.setStatus("deprecated")
_CienaCesRadiusClientServerEntry_Object = MibTableRow
cienaCesRadiusClientServerEntry = _CienaCesRadiusClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1)
)
cienaCesRadiusClientServerEntry.setIndexNames(
    (0, "CIENA-CES-RADIUS-CLIENT-MIB", "cienaCesRadiusClientServerIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerEntry.setStatus("deprecated")


class _CienaCesRadiusClientServerIndex_Type(Integer32):
    """Custom type cienaCesRadiusClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesRadiusClientServerIndex_Type.__name__ = "Integer32"
_CienaCesRadiusClientServerIndex_Object = MibTableColumn
cienaCesRadiusClientServerIndex = _CienaCesRadiusClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 1),
    _CienaCesRadiusClientServerIndex_Type()
)
cienaCesRadiusClientServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerIndex.setStatus("deprecated")
_CienaCesRadiusClientServerAddr_Type = DisplayString
_CienaCesRadiusClientServerAddr_Object = MibTableColumn
cienaCesRadiusClientServerAddr = _CienaCesRadiusClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 2),
    _CienaCesRadiusClientServerAddr_Type()
)
cienaCesRadiusClientServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAddr.setStatus("deprecated")
_CienaCesRadiusClientServerResolvedAddr_Type = IpAddress
_CienaCesRadiusClientServerResolvedAddr_Object = MibTableColumn
cienaCesRadiusClientServerResolvedAddr = _CienaCesRadiusClientServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 3),
    _CienaCesRadiusClientServerResolvedAddr_Type()
)
cienaCesRadiusClientServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerResolvedAddr.setStatus("deprecated")
_CienaCesRadiusClientServerPriority_Type = Integer32
_CienaCesRadiusClientServerPriority_Object = MibTableColumn
cienaCesRadiusClientServerPriority = _CienaCesRadiusClientServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 4),
    _CienaCesRadiusClientServerPriority_Type()
)
cienaCesRadiusClientServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerPriority.setStatus("deprecated")


class _CienaCesRadiusClientServerAuthPort_Type(Integer32):
    """Custom type cienaCesRadiusClientServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRadiusClientServerAuthPort_Type.__name__ = "Integer32"
_CienaCesRadiusClientServerAuthPort_Object = MibTableColumn
cienaCesRadiusClientServerAuthPort = _CienaCesRadiusClientServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 5),
    _CienaCesRadiusClientServerAuthPort_Type()
)
cienaCesRadiusClientServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAuthPort.setStatus("deprecated")
_CienaCesRadiusClientServerRoundTripTime_Type = TimeTicks
_CienaCesRadiusClientServerRoundTripTime_Object = MibTableColumn
cienaCesRadiusClientServerRoundTripTime = _CienaCesRadiusClientServerRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 6),
    _CienaCesRadiusClientServerRoundTripTime_Type()
)
cienaCesRadiusClientServerRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerRoundTripTime.setStatus("deprecated")
_CienaCesRadiusClientServerAccessRequests_Type = Counter32
_CienaCesRadiusClientServerAccessRequests_Object = MibTableColumn
cienaCesRadiusClientServerAccessRequests = _CienaCesRadiusClientServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 7),
    _CienaCesRadiusClientServerAccessRequests_Type()
)
cienaCesRadiusClientServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAccessRequests.setStatus("deprecated")
_CienaCesRadiusClientServerAccessRetransmissions_Type = Counter32
_CienaCesRadiusClientServerAccessRetransmissions_Object = MibTableColumn
cienaCesRadiusClientServerAccessRetransmissions = _CienaCesRadiusClientServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 8),
    _CienaCesRadiusClientServerAccessRetransmissions_Type()
)
cienaCesRadiusClientServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAccessRetransmissions.setStatus("deprecated")
_CienaCesRadiusClientServerAccessAccepts_Type = Counter32
_CienaCesRadiusClientServerAccessAccepts_Object = MibTableColumn
cienaCesRadiusClientServerAccessAccepts = _CienaCesRadiusClientServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 9),
    _CienaCesRadiusClientServerAccessAccepts_Type()
)
cienaCesRadiusClientServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAccessAccepts.setStatus("deprecated")
_CienaCesRadiusClientServerAccessRejects_Type = Counter32
_CienaCesRadiusClientServerAccessRejects_Object = MibTableColumn
cienaCesRadiusClientServerAccessRejects = _CienaCesRadiusClientServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 10),
    _CienaCesRadiusClientServerAccessRejects_Type()
)
cienaCesRadiusClientServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAccessRejects.setStatus("deprecated")
_CienaCesRadiusClientServerAccessChallenges_Type = Counter32
_CienaCesRadiusClientServerAccessChallenges_Object = MibTableColumn
cienaCesRadiusClientServerAccessChallenges = _CienaCesRadiusClientServerAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 11),
    _CienaCesRadiusClientServerAccessChallenges_Type()
)
cienaCesRadiusClientServerAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerAccessChallenges.setStatus("deprecated")
_CienaCesRadiusClientServerMalformedAccessResponses_Type = Counter32
_CienaCesRadiusClientServerMalformedAccessResponses_Object = MibTableColumn
cienaCesRadiusClientServerMalformedAccessResponses = _CienaCesRadiusClientServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 12),
    _CienaCesRadiusClientServerMalformedAccessResponses_Type()
)
cienaCesRadiusClientServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerMalformedAccessResponses.setStatus("deprecated")
_CienaCesRadiusClientServerBadAuthenticators_Type = Counter32
_CienaCesRadiusClientServerBadAuthenticators_Object = MibTableColumn
cienaCesRadiusClientServerBadAuthenticators = _CienaCesRadiusClientServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 13),
    _CienaCesRadiusClientServerBadAuthenticators_Type()
)
cienaCesRadiusClientServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerBadAuthenticators.setStatus("deprecated")
_CienaCesRadiusClientServerPendingRequests_Type = Gauge32
_CienaCesRadiusClientServerPendingRequests_Object = MibTableColumn
cienaCesRadiusClientServerPendingRequests = _CienaCesRadiusClientServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 14),
    _CienaCesRadiusClientServerPendingRequests_Type()
)
cienaCesRadiusClientServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerPendingRequests.setStatus("deprecated")
_CienaCesRadiusClientServerTimeouts_Type = Counter32
_CienaCesRadiusClientServerTimeouts_Object = MibTableColumn
cienaCesRadiusClientServerTimeouts = _CienaCesRadiusClientServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 15),
    _CienaCesRadiusClientServerTimeouts_Type()
)
cienaCesRadiusClientServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerTimeouts.setStatus("deprecated")
_CienaCesRadiusClientServerUnknownTypes_Type = Counter32
_CienaCesRadiusClientServerUnknownTypes_Object = MibTableColumn
cienaCesRadiusClientServerUnknownTypes = _CienaCesRadiusClientServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 16),
    _CienaCesRadiusClientServerUnknownTypes_Type()
)
cienaCesRadiusClientServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerUnknownTypes.setStatus("deprecated")
_CienaCesRadiusClientServerPacketsDropped_Type = Counter32
_CienaCesRadiusClientServerPacketsDropped_Object = MibTableColumn
cienaCesRadiusClientServerPacketsDropped = _CienaCesRadiusClientServerPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 17),
    _CienaCesRadiusClientServerPacketsDropped_Type()
)
cienaCesRadiusClientServerPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerPacketsDropped.setStatus("deprecated")


class _CienaCesRadiusClientServerApplication_Type(Integer32):
    """Custom type cienaCesRadiusClientServerApplication based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("userLogin", 1))
    )


_CienaCesRadiusClientServerApplication_Type.__name__ = "Integer32"
_CienaCesRadiusClientServerApplication_Object = MibTableColumn
cienaCesRadiusClientServerApplication = _CienaCesRadiusClientServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 18),
    _CienaCesRadiusClientServerApplication_Type()
)
cienaCesRadiusClientServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerApplication.setStatus("deprecated")
_CienaCesRadiusClientServerStatus_Type = RowStatus
_CienaCesRadiusClientServerStatus_Object = MibTableColumn
cienaCesRadiusClientServerStatus = _CienaCesRadiusClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 2, 1, 1, 19),
    _CienaCesRadiusClientServerStatus_Type()
)
cienaCesRadiusClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusClientServerStatus.setStatus("deprecated")
_CienaCesRadiusUserLogin_ObjectIdentity = ObjectIdentity
cienaCesRadiusUserLogin = _CienaCesRadiusUserLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3)
)
_CienaCesRadiusUserLoginGlobal_ObjectIdentity = ObjectIdentity
cienaCesRadiusUserLoginGlobal = _CienaCesRadiusUserLoginGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 1)
)


class _CienaCesRadiusUserLoginTimeout_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesRadiusUserLoginTimeout_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginTimeout_Object = MibScalar
cienaCesRadiusUserLoginTimeout = _CienaCesRadiusUserLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 1, 1),
    _CienaCesRadiusUserLoginTimeout_Type()
)
cienaCesRadiusUserLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginTimeout.setUnits("seconds")


class _CienaCesRadiusUserLoginRetries_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesRadiusUserLoginRetries_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginRetries_Object = MibScalar
cienaCesRadiusUserLoginRetries = _CienaCesRadiusUserLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 1, 2),
    _CienaCesRadiusUserLoginRetries_Type()
)
cienaCesRadiusUserLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginRetries.setStatus("current")
_CienaCesRadiusUserLoginAuthKey_Type = RadiusString
_CienaCesRadiusUserLoginAuthKey_Object = MibScalar
cienaCesRadiusUserLoginAuthKey = _CienaCesRadiusUserLoginAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 1, 3),
    _CienaCesRadiusUserLoginAuthKey_Type()
)
cienaCesRadiusUserLoginAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAuthKey.setStatus("current")


class _CienaCesRadiusUserLoginSearchType_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginSearchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cached", 1),
          ("priority", 2))
    )


_CienaCesRadiusUserLoginSearchType_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginSearchType_Object = MibScalar
cienaCesRadiusUserLoginSearchType = _CienaCesRadiusUserLoginSearchType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 1, 4),
    _CienaCesRadiusUserLoginSearchType_Type()
)
cienaCesRadiusUserLoginSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginSearchType.setStatus("current")


class _CienaCesRadiusUserLoginAuthSecret_Type(OctetString):
    """Custom type cienaCesRadiusUserLoginAuthSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 259),
    )


_CienaCesRadiusUserLoginAuthSecret_Type.__name__ = "OctetString"
_CienaCesRadiusUserLoginAuthSecret_Object = MibScalar
cienaCesRadiusUserLoginAuthSecret = _CienaCesRadiusUserLoginAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 1, 5),
    _CienaCesRadiusUserLoginAuthSecret_Type()
)
cienaCesRadiusUserLoginAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAuthSecret.setStatus("current")
_CienaCesRadiusUserLoginTable_Object = MibTable
cienaCesRadiusUserLoginTable = _CienaCesRadiusUserLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginTable.setStatus("current")
_CienaCesRadiusUserLoginEntry_Object = MibTableRow
cienaCesRadiusUserLoginEntry = _CienaCesRadiusUserLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1)
)
cienaCesRadiusUserLoginEntry.setIndexNames(
    (0, "CIENA-CES-RADIUS-CLIENT-MIB", "cienaCesRadiusUserLoginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginEntry.setStatus("current")


class _CienaCesRadiusUserLoginIndex_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesRadiusUserLoginIndex_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginIndex_Object = MibTableColumn
cienaCesRadiusUserLoginIndex = _CienaCesRadiusUserLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 1),
    _CienaCesRadiusUserLoginIndex_Type()
)
cienaCesRadiusUserLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginIndex.setStatus("current")
_CienaCesRadiusUserLoginResolvedInetAddrType_Type = InetAddressType
_CienaCesRadiusUserLoginResolvedInetAddrType_Object = MibTableColumn
cienaCesRadiusUserLoginResolvedInetAddrType = _CienaCesRadiusUserLoginResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 2),
    _CienaCesRadiusUserLoginResolvedInetAddrType_Type()
)
cienaCesRadiusUserLoginResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginResolvedInetAddrType.setStatus("current")
_CienaCesRadiusUserLoginResolvedInetAddress_Type = InetAddress
_CienaCesRadiusUserLoginResolvedInetAddress_Object = MibTableColumn
cienaCesRadiusUserLoginResolvedInetAddress = _CienaCesRadiusUserLoginResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 3),
    _CienaCesRadiusUserLoginResolvedInetAddress_Type()
)
cienaCesRadiusUserLoginResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginResolvedInetAddress.setStatus("current")
_CienaCesRadiusUserLoginAddr_Type = DisplayString
_CienaCesRadiusUserLoginAddr_Object = MibTableColumn
cienaCesRadiusUserLoginAddr = _CienaCesRadiusUserLoginAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 4),
    _CienaCesRadiusUserLoginAddr_Type()
)
cienaCesRadiusUserLoginAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAddr.setStatus("current")
_CienaCesRadiusUserLoginPriority_Type = Integer32
_CienaCesRadiusUserLoginPriority_Object = MibTableColumn
cienaCesRadiusUserLoginPriority = _CienaCesRadiusUserLoginPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 5),
    _CienaCesRadiusUserLoginPriority_Type()
)
cienaCesRadiusUserLoginPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginPriority.setStatus("current")


class _CienaCesRadiusUserLoginAuthPort_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRadiusUserLoginAuthPort_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAuthPort_Object = MibTableColumn
cienaCesRadiusUserLoginAuthPort = _CienaCesRadiusUserLoginAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 6),
    _CienaCesRadiusUserLoginAuthPort_Type()
)
cienaCesRadiusUserLoginAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAuthPort.setStatus("current")
_CienaCesRadiusUserLoginClearStatistics_Type = TruthValue
_CienaCesRadiusUserLoginClearStatistics_Object = MibTableColumn
cienaCesRadiusUserLoginClearStatistics = _CienaCesRadiusUserLoginClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 7),
    _CienaCesRadiusUserLoginClearStatistics_Type()
)
cienaCesRadiusUserLoginClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginClearStatistics.setStatus("current")
_CienaCesRadiusUserLoginRoundTripTime_Type = TimeTicks
_CienaCesRadiusUserLoginRoundTripTime_Object = MibTableColumn
cienaCesRadiusUserLoginRoundTripTime = _CienaCesRadiusUserLoginRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 8),
    _CienaCesRadiusUserLoginRoundTripTime_Type()
)
cienaCesRadiusUserLoginRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginRoundTripTime.setStatus("current")
_CienaCesRadiusUserLoginRequests_Type = Counter32
_CienaCesRadiusUserLoginRequests_Object = MibTableColumn
cienaCesRadiusUserLoginRequests = _CienaCesRadiusUserLoginRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 9),
    _CienaCesRadiusUserLoginRequests_Type()
)
cienaCesRadiusUserLoginRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginRequests.setStatus("current")
_CienaCesRadiusUserLoginRetransmissions_Type = Counter32
_CienaCesRadiusUserLoginRetransmissions_Object = MibTableColumn
cienaCesRadiusUserLoginRetransmissions = _CienaCesRadiusUserLoginRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 10),
    _CienaCesRadiusUserLoginRetransmissions_Type()
)
cienaCesRadiusUserLoginRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginRetransmissions.setStatus("current")
_CienaCesRadiusUserLoginAccessAccepts_Type = Counter32
_CienaCesRadiusUserLoginAccessAccepts_Object = MibTableColumn
cienaCesRadiusUserLoginAccessAccepts = _CienaCesRadiusUserLoginAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 11),
    _CienaCesRadiusUserLoginAccessAccepts_Type()
)
cienaCesRadiusUserLoginAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAccessAccepts.setStatus("current")
_CienaCesRadiusUserLoginAccessRejects_Type = Counter32
_CienaCesRadiusUserLoginAccessRejects_Object = MibTableColumn
cienaCesRadiusUserLoginAccessRejects = _CienaCesRadiusUserLoginAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 12),
    _CienaCesRadiusUserLoginAccessRejects_Type()
)
cienaCesRadiusUserLoginAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAccessRejects.setStatus("current")
_CienaCesRadiusUserLoginAccessChallenges_Type = Counter32
_CienaCesRadiusUserLoginAccessChallenges_Object = MibTableColumn
cienaCesRadiusUserLoginAccessChallenges = _CienaCesRadiusUserLoginAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 13),
    _CienaCesRadiusUserLoginAccessChallenges_Type()
)
cienaCesRadiusUserLoginAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAccessChallenges.setStatus("current")
_CienaCesRadiusUserLoginAccountingResponses_Type = Counter32
_CienaCesRadiusUserLoginAccountingResponses_Object = MibTableColumn
cienaCesRadiusUserLoginAccountingResponses = _CienaCesRadiusUserLoginAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 14),
    _CienaCesRadiusUserLoginAccountingResponses_Type()
)
cienaCesRadiusUserLoginAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAccountingResponses.setStatus("current")
_CienaCesRadiusUserLoginMalformedResponses_Type = Counter32
_CienaCesRadiusUserLoginMalformedResponses_Object = MibTableColumn
cienaCesRadiusUserLoginMalformedResponses = _CienaCesRadiusUserLoginMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 15),
    _CienaCesRadiusUserLoginMalformedResponses_Type()
)
cienaCesRadiusUserLoginMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginMalformedResponses.setStatus("current")
_CienaCesRadiusUserLoginBadAuthenticators_Type = Counter32
_CienaCesRadiusUserLoginBadAuthenticators_Object = MibTableColumn
cienaCesRadiusUserLoginBadAuthenticators = _CienaCesRadiusUserLoginBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 16),
    _CienaCesRadiusUserLoginBadAuthenticators_Type()
)
cienaCesRadiusUserLoginBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginBadAuthenticators.setStatus("current")
_CienaCesRadiusUserLoginTimeouts_Type = Counter32
_CienaCesRadiusUserLoginTimeouts_Object = MibTableColumn
cienaCesRadiusUserLoginTimeouts = _CienaCesRadiusUserLoginTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 17),
    _CienaCesRadiusUserLoginTimeouts_Type()
)
cienaCesRadiusUserLoginTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginTimeouts.setStatus("current")
_CienaCesRadiusUserLoginUnknownTypes_Type = Counter32
_CienaCesRadiusUserLoginUnknownTypes_Object = MibTableColumn
cienaCesRadiusUserLoginUnknownTypes = _CienaCesRadiusUserLoginUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 18),
    _CienaCesRadiusUserLoginUnknownTypes_Type()
)
cienaCesRadiusUserLoginUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginUnknownTypes.setStatus("current")
_CienaCesRadiusUserLoginPacketsDropped_Type = Counter32
_CienaCesRadiusUserLoginPacketsDropped_Object = MibTableColumn
cienaCesRadiusUserLoginPacketsDropped = _CienaCesRadiusUserLoginPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 19),
    _CienaCesRadiusUserLoginPacketsDropped_Type()
)
cienaCesRadiusUserLoginPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginPacketsDropped.setStatus("current")
_CienaCesRadiusUserLoginStatus_Type = RowStatus
_CienaCesRadiusUserLoginStatus_Object = MibTableColumn
cienaCesRadiusUserLoginStatus = _CienaCesRadiusUserLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 3, 2, 1, 20),
    _CienaCesRadiusUserLoginStatus_Type()
)
cienaCesRadiusUserLoginStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginStatus.setStatus("current")
_CienaCesRadiusDot1xAuth_ObjectIdentity = ObjectIdentity
cienaCesRadiusDot1xAuth = _CienaCesRadiusDot1xAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4)
)
_CienaCesRadiusDot1xAuthGlobal_ObjectIdentity = ObjectIdentity
cienaCesRadiusDot1xAuthGlobal = _CienaCesRadiusDot1xAuthGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1)
)


class _CienaCesRadiusDot1xAuthTimeout_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAuthTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesRadiusDot1xAuthTimeout_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAuthTimeout_Object = MibScalar
cienaCesRadiusDot1xAuthTimeout = _CienaCesRadiusDot1xAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1, 1),
    _CienaCesRadiusDot1xAuthTimeout_Type()
)
cienaCesRadiusDot1xAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthTimeout.setUnits("seconds")


class _CienaCesRadiusDot1xAuthRetries_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAuthRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesRadiusDot1xAuthRetries_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAuthRetries_Object = MibScalar
cienaCesRadiusDot1xAuthRetries = _CienaCesRadiusDot1xAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1, 2),
    _CienaCesRadiusDot1xAuthRetries_Type()
)
cienaCesRadiusDot1xAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthRetries.setStatus("current")
_CienaCesRadiusDot1xAuthAuthKey_Type = RadiusString
_CienaCesRadiusDot1xAuthAuthKey_Object = MibScalar
cienaCesRadiusDot1xAuthAuthKey = _CienaCesRadiusDot1xAuthAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1, 3),
    _CienaCesRadiusDot1xAuthAuthKey_Type()
)
cienaCesRadiusDot1xAuthAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAuthKey.setStatus("current")


class _CienaCesRadiusDot1xAuthSearchType_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAuthSearchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBalance", 2),
          ("priority", 1))
    )


_CienaCesRadiusDot1xAuthSearchType_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAuthSearchType_Object = MibScalar
cienaCesRadiusDot1xAuthSearchType = _CienaCesRadiusDot1xAuthSearchType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1, 4),
    _CienaCesRadiusDot1xAuthSearchType_Type()
)
cienaCesRadiusDot1xAuthSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthSearchType.setStatus("current")


class _CienaCesRadiusDot1xAuthGreylistTimeout_Type(Unsigned32):
    """Custom type cienaCesRadiusDot1xAuthGreylistTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 14400),
    )


_CienaCesRadiusDot1xAuthGreylistTimeout_Type.__name__ = "Unsigned32"
_CienaCesRadiusDot1xAuthGreylistTimeout_Object = MibScalar
cienaCesRadiusDot1xAuthGreylistTimeout = _CienaCesRadiusDot1xAuthGreylistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1, 5),
    _CienaCesRadiusDot1xAuthGreylistTimeout_Type()
)
cienaCesRadiusDot1xAuthGreylistTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthGreylistTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthGreylistTimeout.setUnits("seconds")


class _CienaCesRadiusDot1xAuthAuthSecret_Type(OctetString):
    """Custom type cienaCesRadiusDot1xAuthAuthSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 259),
    )


_CienaCesRadiusDot1xAuthAuthSecret_Type.__name__ = "OctetString"
_CienaCesRadiusDot1xAuthAuthSecret_Object = MibScalar
cienaCesRadiusDot1xAuthAuthSecret = _CienaCesRadiusDot1xAuthAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 1, 6),
    _CienaCesRadiusDot1xAuthAuthSecret_Type()
)
cienaCesRadiusDot1xAuthAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAuthSecret.setStatus("current")
_CienaCesRadiusDot1xAuthTable_Object = MibTable
cienaCesRadiusDot1xAuthTable = _CienaCesRadiusDot1xAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthTable.setStatus("current")
_CienaCesRadiusDot1xAuthEntry_Object = MibTableRow
cienaCesRadiusDot1xAuthEntry = _CienaCesRadiusDot1xAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1)
)
cienaCesRadiusDot1xAuthEntry.setIndexNames(
    (0, "CIENA-CES-RADIUS-CLIENT-MIB", "cienaCesRadiusDot1xAuthIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthEntry.setStatus("current")


class _CienaCesRadiusDot1xAuthIndex_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAuthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesRadiusDot1xAuthIndex_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAuthIndex_Object = MibTableColumn
cienaCesRadiusDot1xAuthIndex = _CienaCesRadiusDot1xAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 1),
    _CienaCesRadiusDot1xAuthIndex_Type()
)
cienaCesRadiusDot1xAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthIndex.setStatus("current")
_CienaCesRadiusDot1xAuthResolvedInetAddrType_Type = InetAddressType
_CienaCesRadiusDot1xAuthResolvedInetAddrType_Object = MibTableColumn
cienaCesRadiusDot1xAuthResolvedInetAddrType = _CienaCesRadiusDot1xAuthResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 2),
    _CienaCesRadiusDot1xAuthResolvedInetAddrType_Type()
)
cienaCesRadiusDot1xAuthResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthResolvedInetAddrType.setStatus("current")
_CienaCesRadiusDot1xAuthResolvedInetAddress_Type = InetAddress
_CienaCesRadiusDot1xAuthResolvedInetAddress_Object = MibTableColumn
cienaCesRadiusDot1xAuthResolvedInetAddress = _CienaCesRadiusDot1xAuthResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 3),
    _CienaCesRadiusDot1xAuthResolvedInetAddress_Type()
)
cienaCesRadiusDot1xAuthResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthResolvedInetAddress.setStatus("current")
_CienaCesRadiusDot1xAuthAddr_Type = DisplayString
_CienaCesRadiusDot1xAuthAddr_Object = MibTableColumn
cienaCesRadiusDot1xAuthAddr = _CienaCesRadiusDot1xAuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 4),
    _CienaCesRadiusDot1xAuthAddr_Type()
)
cienaCesRadiusDot1xAuthAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAddr.setStatus("current")
_CienaCesRadiusDot1xAuthPriority_Type = Integer32
_CienaCesRadiusDot1xAuthPriority_Object = MibTableColumn
cienaCesRadiusDot1xAuthPriority = _CienaCesRadiusDot1xAuthPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 5),
    _CienaCesRadiusDot1xAuthPriority_Type()
)
cienaCesRadiusDot1xAuthPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthPriority.setStatus("current")


class _CienaCesRadiusDot1xAuthAuthPort_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAuthAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRadiusDot1xAuthAuthPort_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAuthAuthPort_Object = MibTableColumn
cienaCesRadiusDot1xAuthAuthPort = _CienaCesRadiusDot1xAuthAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 6),
    _CienaCesRadiusDot1xAuthAuthPort_Type()
)
cienaCesRadiusDot1xAuthAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAuthPort.setStatus("current")
_CienaCesRadiusDot1xAuthClearStatistics_Type = TruthValue
_CienaCesRadiusDot1xAuthClearStatistics_Object = MibTableColumn
cienaCesRadiusDot1xAuthClearStatistics = _CienaCesRadiusDot1xAuthClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 7),
    _CienaCesRadiusDot1xAuthClearStatistics_Type()
)
cienaCesRadiusDot1xAuthClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthClearStatistics.setStatus("current")


class _CienaCesRadiusDot1xAuthGreylistTimeRemaining_Type(Unsigned32):
    """Custom type cienaCesRadiusDot1xAuthGreylistTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_CienaCesRadiusDot1xAuthGreylistTimeRemaining_Type.__name__ = "Unsigned32"
_CienaCesRadiusDot1xAuthGreylistTimeRemaining_Object = MibTableColumn
cienaCesRadiusDot1xAuthGreylistTimeRemaining = _CienaCesRadiusDot1xAuthGreylistTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 8),
    _CienaCesRadiusDot1xAuthGreylistTimeRemaining_Type()
)
cienaCesRadiusDot1xAuthGreylistTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthGreylistTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthGreylistTimeRemaining.setUnits("seconds")
_CienaCesRadiusDot1xAuthRoundTripTime_Type = TimeTicks
_CienaCesRadiusDot1xAuthRoundTripTime_Object = MibTableColumn
cienaCesRadiusDot1xAuthRoundTripTime = _CienaCesRadiusDot1xAuthRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 9),
    _CienaCesRadiusDot1xAuthRoundTripTime_Type()
)
cienaCesRadiusDot1xAuthRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthRoundTripTime.setStatus("current")
_CienaCesRadiusDot1xAuthRequests_Type = Counter32
_CienaCesRadiusDot1xAuthRequests_Object = MibTableColumn
cienaCesRadiusDot1xAuthRequests = _CienaCesRadiusDot1xAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 10),
    _CienaCesRadiusDot1xAuthRequests_Type()
)
cienaCesRadiusDot1xAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthRequests.setStatus("current")
_CienaCesRadiusDot1xAuthRetransmissions_Type = Counter32
_CienaCesRadiusDot1xAuthRetransmissions_Object = MibTableColumn
cienaCesRadiusDot1xAuthRetransmissions = _CienaCesRadiusDot1xAuthRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 11),
    _CienaCesRadiusDot1xAuthRetransmissions_Type()
)
cienaCesRadiusDot1xAuthRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthRetransmissions.setStatus("current")
_CienaCesRadiusDot1xAuthAccessAccepts_Type = Counter32
_CienaCesRadiusDot1xAuthAccessAccepts_Object = MibTableColumn
cienaCesRadiusDot1xAuthAccessAccepts = _CienaCesRadiusDot1xAuthAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 12),
    _CienaCesRadiusDot1xAuthAccessAccepts_Type()
)
cienaCesRadiusDot1xAuthAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAccessAccepts.setStatus("current")
_CienaCesRadiusDot1xAuthAccessRejects_Type = Counter32
_CienaCesRadiusDot1xAuthAccessRejects_Object = MibTableColumn
cienaCesRadiusDot1xAuthAccessRejects = _CienaCesRadiusDot1xAuthAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 13),
    _CienaCesRadiusDot1xAuthAccessRejects_Type()
)
cienaCesRadiusDot1xAuthAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAccessRejects.setStatus("current")
_CienaCesRadiusDot1xAuthAccessChallenges_Type = Counter32
_CienaCesRadiusDot1xAuthAccessChallenges_Object = MibTableColumn
cienaCesRadiusDot1xAuthAccessChallenges = _CienaCesRadiusDot1xAuthAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 14),
    _CienaCesRadiusDot1xAuthAccessChallenges_Type()
)
cienaCesRadiusDot1xAuthAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAccessChallenges.setStatus("current")
_CienaCesRadiusDot1xAuthAccountingResponses_Type = Counter32
_CienaCesRadiusDot1xAuthAccountingResponses_Object = MibTableColumn
cienaCesRadiusDot1xAuthAccountingResponses = _CienaCesRadiusDot1xAuthAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 15),
    _CienaCesRadiusDot1xAuthAccountingResponses_Type()
)
cienaCesRadiusDot1xAuthAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthAccountingResponses.setStatus("current")
_CienaCesRadiusDot1xAuthMalformedResponses_Type = Counter32
_CienaCesRadiusDot1xAuthMalformedResponses_Object = MibTableColumn
cienaCesRadiusDot1xAuthMalformedResponses = _CienaCesRadiusDot1xAuthMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 16),
    _CienaCesRadiusDot1xAuthMalformedResponses_Type()
)
cienaCesRadiusDot1xAuthMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthMalformedResponses.setStatus("current")
_CienaCesRadiusDot1xAuthBadAuthenticators_Type = Counter32
_CienaCesRadiusDot1xAuthBadAuthenticators_Object = MibTableColumn
cienaCesRadiusDot1xAuthBadAuthenticators = _CienaCesRadiusDot1xAuthBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 17),
    _CienaCesRadiusDot1xAuthBadAuthenticators_Type()
)
cienaCesRadiusDot1xAuthBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthBadAuthenticators.setStatus("current")
_CienaCesRadiusDot1xAuthTimeouts_Type = Counter32
_CienaCesRadiusDot1xAuthTimeouts_Object = MibTableColumn
cienaCesRadiusDot1xAuthTimeouts = _CienaCesRadiusDot1xAuthTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 18),
    _CienaCesRadiusDot1xAuthTimeouts_Type()
)
cienaCesRadiusDot1xAuthTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthTimeouts.setStatus("current")
_CienaCesRadiusDot1xAuthUnknownTypes_Type = Counter32
_CienaCesRadiusDot1xAuthUnknownTypes_Object = MibTableColumn
cienaCesRadiusDot1xAuthUnknownTypes = _CienaCesRadiusDot1xAuthUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 19),
    _CienaCesRadiusDot1xAuthUnknownTypes_Type()
)
cienaCesRadiusDot1xAuthUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthUnknownTypes.setStatus("current")
_CienaCesRadiusDot1xAuthPacketsDropped_Type = Counter32
_CienaCesRadiusDot1xAuthPacketsDropped_Object = MibTableColumn
cienaCesRadiusDot1xAuthPacketsDropped = _CienaCesRadiusDot1xAuthPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 20),
    _CienaCesRadiusDot1xAuthPacketsDropped_Type()
)
cienaCesRadiusDot1xAuthPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthPacketsDropped.setStatus("current")
_CienaCesRadiusDot1xAuthStatus_Type = RowStatus
_CienaCesRadiusDot1xAuthStatus_Object = MibTableColumn
cienaCesRadiusDot1xAuthStatus = _CienaCesRadiusDot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 4, 2, 1, 21),
    _CienaCesRadiusDot1xAuthStatus_Type()
)
cienaCesRadiusDot1xAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAuthStatus.setStatus("current")
_CienaCesRadiusDot1xAcct_ObjectIdentity = ObjectIdentity
cienaCesRadiusDot1xAcct = _CienaCesRadiusDot1xAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5)
)
_CienaCesRadiusDot1xAcctGlobal_ObjectIdentity = ObjectIdentity
cienaCesRadiusDot1xAcctGlobal = _CienaCesRadiusDot1xAcctGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1)
)


class _CienaCesRadiusDot1xAcctAdminState_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAcctAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesRadiusDot1xAcctAdminState_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAcctAdminState_Object = MibScalar
cienaCesRadiusDot1xAcctAdminState = _CienaCesRadiusDot1xAcctAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 1),
    _CienaCesRadiusDot1xAcctAdminState_Type()
)
cienaCesRadiusDot1xAcctAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAdminState.setStatus("current")


class _CienaCesRadiusDot1xAcctTimeout_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAcctTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesRadiusDot1xAcctTimeout_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAcctTimeout_Object = MibScalar
cienaCesRadiusDot1xAcctTimeout = _CienaCesRadiusDot1xAcctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 2),
    _CienaCesRadiusDot1xAcctTimeout_Type()
)
cienaCesRadiusDot1xAcctTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctTimeout.setUnits("seconds")


class _CienaCesRadiusDot1xAcctRetries_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAcctRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesRadiusDot1xAcctRetries_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAcctRetries_Object = MibScalar
cienaCesRadiusDot1xAcctRetries = _CienaCesRadiusDot1xAcctRetries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 3),
    _CienaCesRadiusDot1xAcctRetries_Type()
)
cienaCesRadiusDot1xAcctRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctRetries.setStatus("current")
_CienaCesRadiusDot1xAcctAuthKey_Type = RadiusString
_CienaCesRadiusDot1xAcctAuthKey_Object = MibScalar
cienaCesRadiusDot1xAcctAuthKey = _CienaCesRadiusDot1xAcctAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 4),
    _CienaCesRadiusDot1xAcctAuthKey_Type()
)
cienaCesRadiusDot1xAcctAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAuthKey.setStatus("current")


class _CienaCesRadiusDot1xAcctSearchType_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAcctSearchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadBalance", 2),
          ("priority", 1))
    )


_CienaCesRadiusDot1xAcctSearchType_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAcctSearchType_Object = MibScalar
cienaCesRadiusDot1xAcctSearchType = _CienaCesRadiusDot1xAcctSearchType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 5),
    _CienaCesRadiusDot1xAcctSearchType_Type()
)
cienaCesRadiusDot1xAcctSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctSearchType.setStatus("current")


class _CienaCesRadiusDot1xAcctGreylistTimeout_Type(Unsigned32):
    """Custom type cienaCesRadiusDot1xAcctGreylistTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 14400),
    )


_CienaCesRadiusDot1xAcctGreylistTimeout_Type.__name__ = "Unsigned32"
_CienaCesRadiusDot1xAcctGreylistTimeout_Object = MibScalar
cienaCesRadiusDot1xAcctGreylistTimeout = _CienaCesRadiusDot1xAcctGreylistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 6),
    _CienaCesRadiusDot1xAcctGreylistTimeout_Type()
)
cienaCesRadiusDot1xAcctGreylistTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctGreylistTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctGreylistTimeout.setUnits("seconds")


class _CienaCesRadiusDot1xAcctAuthSecret_Type(OctetString):
    """Custom type cienaCesRadiusDot1xAcctAuthSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 259),
    )


_CienaCesRadiusDot1xAcctAuthSecret_Type.__name__ = "OctetString"
_CienaCesRadiusDot1xAcctAuthSecret_Object = MibScalar
cienaCesRadiusDot1xAcctAuthSecret = _CienaCesRadiusDot1xAcctAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 1, 7),
    _CienaCesRadiusDot1xAcctAuthSecret_Type()
)
cienaCesRadiusDot1xAcctAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAuthSecret.setStatus("current")
_CienaCesRadiusDot1xAcctTable_Object = MibTable
cienaCesRadiusDot1xAcctTable = _CienaCesRadiusDot1xAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctTable.setStatus("current")
_CienaCesRadiusDot1xAcctEntry_Object = MibTableRow
cienaCesRadiusDot1xAcctEntry = _CienaCesRadiusDot1xAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1)
)
cienaCesRadiusDot1xAcctEntry.setIndexNames(
    (0, "CIENA-CES-RADIUS-CLIENT-MIB", "cienaCesRadiusDot1xAcctIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctEntry.setStatus("current")


class _CienaCesRadiusDot1xAcctIndex_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAcctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesRadiusDot1xAcctIndex_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAcctIndex_Object = MibTableColumn
cienaCesRadiusDot1xAcctIndex = _CienaCesRadiusDot1xAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 1),
    _CienaCesRadiusDot1xAcctIndex_Type()
)
cienaCesRadiusDot1xAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctIndex.setStatus("current")
_CienaCesRadiusDot1xAcctResolvedInetAddrType_Type = InetAddressType
_CienaCesRadiusDot1xAcctResolvedInetAddrType_Object = MibTableColumn
cienaCesRadiusDot1xAcctResolvedInetAddrType = _CienaCesRadiusDot1xAcctResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 2),
    _CienaCesRadiusDot1xAcctResolvedInetAddrType_Type()
)
cienaCesRadiusDot1xAcctResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctResolvedInetAddrType.setStatus("current")
_CienaCesRadiusDot1xAcctResolvedInetAddress_Type = InetAddress
_CienaCesRadiusDot1xAcctResolvedInetAddress_Object = MibTableColumn
cienaCesRadiusDot1xAcctResolvedInetAddress = _CienaCesRadiusDot1xAcctResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 3),
    _CienaCesRadiusDot1xAcctResolvedInetAddress_Type()
)
cienaCesRadiusDot1xAcctResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctResolvedInetAddress.setStatus("current")
_CienaCesRadiusDot1xAcctAddr_Type = DisplayString
_CienaCesRadiusDot1xAcctAddr_Object = MibTableColumn
cienaCesRadiusDot1xAcctAddr = _CienaCesRadiusDot1xAcctAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 4),
    _CienaCesRadiusDot1xAcctAddr_Type()
)
cienaCesRadiusDot1xAcctAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAddr.setStatus("current")
_CienaCesRadiusDot1xAcctPriority_Type = Integer32
_CienaCesRadiusDot1xAcctPriority_Object = MibTableColumn
cienaCesRadiusDot1xAcctPriority = _CienaCesRadiusDot1xAcctPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 5),
    _CienaCesRadiusDot1xAcctPriority_Type()
)
cienaCesRadiusDot1xAcctPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctPriority.setStatus("current")


class _CienaCesRadiusDot1xAcctAuthPort_Type(Integer32):
    """Custom type cienaCesRadiusDot1xAcctAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRadiusDot1xAcctAuthPort_Type.__name__ = "Integer32"
_CienaCesRadiusDot1xAcctAuthPort_Object = MibTableColumn
cienaCesRadiusDot1xAcctAuthPort = _CienaCesRadiusDot1xAcctAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 6),
    _CienaCesRadiusDot1xAcctAuthPort_Type()
)
cienaCesRadiusDot1xAcctAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAuthPort.setStatus("current")
_CienaCesRadiusDot1xAcctClearStatistics_Type = TruthValue
_CienaCesRadiusDot1xAcctClearStatistics_Object = MibTableColumn
cienaCesRadiusDot1xAcctClearStatistics = _CienaCesRadiusDot1xAcctClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 7),
    _CienaCesRadiusDot1xAcctClearStatistics_Type()
)
cienaCesRadiusDot1xAcctClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctClearStatistics.setStatus("current")


class _CienaCesRadiusDot1xAcctGreylistTimeRemaining_Type(Unsigned32):
    """Custom type cienaCesRadiusDot1xAcctGreylistTimeRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_CienaCesRadiusDot1xAcctGreylistTimeRemaining_Type.__name__ = "Unsigned32"
_CienaCesRadiusDot1xAcctGreylistTimeRemaining_Object = MibTableColumn
cienaCesRadiusDot1xAcctGreylistTimeRemaining = _CienaCesRadiusDot1xAcctGreylistTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 8),
    _CienaCesRadiusDot1xAcctGreylistTimeRemaining_Type()
)
cienaCesRadiusDot1xAcctGreylistTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctGreylistTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctGreylistTimeRemaining.setUnits("seconds")
_CienaCesRadiusDot1xAcctRoundTripTime_Type = TimeTicks
_CienaCesRadiusDot1xAcctRoundTripTime_Object = MibTableColumn
cienaCesRadiusDot1xAcctRoundTripTime = _CienaCesRadiusDot1xAcctRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 9),
    _CienaCesRadiusDot1xAcctRoundTripTime_Type()
)
cienaCesRadiusDot1xAcctRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctRoundTripTime.setStatus("current")
_CienaCesRadiusDot1xAcctRequests_Type = Counter32
_CienaCesRadiusDot1xAcctRequests_Object = MibTableColumn
cienaCesRadiusDot1xAcctRequests = _CienaCesRadiusDot1xAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 10),
    _CienaCesRadiusDot1xAcctRequests_Type()
)
cienaCesRadiusDot1xAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctRequests.setStatus("current")
_CienaCesRadiusDot1xAcctRetransmissions_Type = Counter32
_CienaCesRadiusDot1xAcctRetransmissions_Object = MibTableColumn
cienaCesRadiusDot1xAcctRetransmissions = _CienaCesRadiusDot1xAcctRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 11),
    _CienaCesRadiusDot1xAcctRetransmissions_Type()
)
cienaCesRadiusDot1xAcctRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctRetransmissions.setStatus("current")
_CienaCesRadiusDot1xAcctAccessAccepts_Type = Counter32
_CienaCesRadiusDot1xAcctAccessAccepts_Object = MibTableColumn
cienaCesRadiusDot1xAcctAccessAccepts = _CienaCesRadiusDot1xAcctAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 12),
    _CienaCesRadiusDot1xAcctAccessAccepts_Type()
)
cienaCesRadiusDot1xAcctAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAccessAccepts.setStatus("current")
_CienaCesRadiusDot1xAcctAccessRejects_Type = Counter32
_CienaCesRadiusDot1xAcctAccessRejects_Object = MibTableColumn
cienaCesRadiusDot1xAcctAccessRejects = _CienaCesRadiusDot1xAcctAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 13),
    _CienaCesRadiusDot1xAcctAccessRejects_Type()
)
cienaCesRadiusDot1xAcctAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAccessRejects.setStatus("current")
_CienaCesRadiusDot1xAcctAccessChallenges_Type = Counter32
_CienaCesRadiusDot1xAcctAccessChallenges_Object = MibTableColumn
cienaCesRadiusDot1xAcctAccessChallenges = _CienaCesRadiusDot1xAcctAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 14),
    _CienaCesRadiusDot1xAcctAccessChallenges_Type()
)
cienaCesRadiusDot1xAcctAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAccessChallenges.setStatus("current")
_CienaCesRadiusDot1xAcctAccountingResponses_Type = Counter32
_CienaCesRadiusDot1xAcctAccountingResponses_Object = MibTableColumn
cienaCesRadiusDot1xAcctAccountingResponses = _CienaCesRadiusDot1xAcctAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 15),
    _CienaCesRadiusDot1xAcctAccountingResponses_Type()
)
cienaCesRadiusDot1xAcctAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctAccountingResponses.setStatus("current")
_CienaCesRadiusDot1xAcctMalformedResponses_Type = Counter32
_CienaCesRadiusDot1xAcctMalformedResponses_Object = MibTableColumn
cienaCesRadiusDot1xAcctMalformedResponses = _CienaCesRadiusDot1xAcctMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 16),
    _CienaCesRadiusDot1xAcctMalformedResponses_Type()
)
cienaCesRadiusDot1xAcctMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctMalformedResponses.setStatus("current")
_CienaCesRadiusDot1xAcctBadAuthenticators_Type = Counter32
_CienaCesRadiusDot1xAcctBadAuthenticators_Object = MibTableColumn
cienaCesRadiusDot1xAcctBadAuthenticators = _CienaCesRadiusDot1xAcctBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 17),
    _CienaCesRadiusDot1xAcctBadAuthenticators_Type()
)
cienaCesRadiusDot1xAcctBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctBadAuthenticators.setStatus("current")
_CienaCesRadiusDot1xAcctTimeouts_Type = Counter32
_CienaCesRadiusDot1xAcctTimeouts_Object = MibTableColumn
cienaCesRadiusDot1xAcctTimeouts = _CienaCesRadiusDot1xAcctTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 18),
    _CienaCesRadiusDot1xAcctTimeouts_Type()
)
cienaCesRadiusDot1xAcctTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctTimeouts.setStatus("current")
_CienaCesRadiusDot1xAcctUnknownTypes_Type = Counter32
_CienaCesRadiusDot1xAcctUnknownTypes_Object = MibTableColumn
cienaCesRadiusDot1xAcctUnknownTypes = _CienaCesRadiusDot1xAcctUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 19),
    _CienaCesRadiusDot1xAcctUnknownTypes_Type()
)
cienaCesRadiusDot1xAcctUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctUnknownTypes.setStatus("current")
_CienaCesRadiusDot1xAcctPacketsDropped_Type = Counter32
_CienaCesRadiusDot1xAcctPacketsDropped_Object = MibTableColumn
cienaCesRadiusDot1xAcctPacketsDropped = _CienaCesRadiusDot1xAcctPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 20),
    _CienaCesRadiusDot1xAcctPacketsDropped_Type()
)
cienaCesRadiusDot1xAcctPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctPacketsDropped.setStatus("current")
_CienaCesRadiusDot1xAcctStatus_Type = RowStatus
_CienaCesRadiusDot1xAcctStatus_Object = MibTableColumn
cienaCesRadiusDot1xAcctStatus = _CienaCesRadiusDot1xAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 5, 2, 1, 21),
    _CienaCesRadiusDot1xAcctStatus_Type()
)
cienaCesRadiusDot1xAcctStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusDot1xAcctStatus.setStatus("current")
_CienaCesRadiusUserLoginAcct_ObjectIdentity = ObjectIdentity
cienaCesRadiusUserLoginAcct = _CienaCesRadiusUserLoginAcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6)
)
_CienaCesRadiusUserLoginAcctGlobal_ObjectIdentity = ObjectIdentity
cienaCesRadiusUserLoginAcctGlobal = _CienaCesRadiusUserLoginAcctGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1)
)


class _CienaCesRadiusUserLoginAcctAdminState_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAcctAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCesRadiusUserLoginAcctAdminState_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAcctAdminState_Object = MibScalar
cienaCesRadiusUserLoginAcctAdminState = _CienaCesRadiusUserLoginAcctAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1, 1),
    _CienaCesRadiusUserLoginAcctAdminState_Type()
)
cienaCesRadiusUserLoginAcctAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAdminState.setStatus("current")


class _CienaCesRadiusUserLoginAcctTimeout_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAcctTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CienaCesRadiusUserLoginAcctTimeout_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAcctTimeout_Object = MibScalar
cienaCesRadiusUserLoginAcctTimeout = _CienaCesRadiusUserLoginAcctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1, 2),
    _CienaCesRadiusUserLoginAcctTimeout_Type()
)
cienaCesRadiusUserLoginAcctTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctTimeout.setUnits("seconds")


class _CienaCesRadiusUserLoginAcctRetries_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAcctRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CienaCesRadiusUserLoginAcctRetries_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAcctRetries_Object = MibScalar
cienaCesRadiusUserLoginAcctRetries = _CienaCesRadiusUserLoginAcctRetries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1, 3),
    _CienaCesRadiusUserLoginAcctRetries_Type()
)
cienaCesRadiusUserLoginAcctRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctRetries.setStatus("current")
_CienaCesRadiusUserLoginAcctAuthKey_Type = RadiusString
_CienaCesRadiusUserLoginAcctAuthKey_Object = MibScalar
cienaCesRadiusUserLoginAcctAuthKey = _CienaCesRadiusUserLoginAcctAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1, 4),
    _CienaCesRadiusUserLoginAcctAuthKey_Type()
)
cienaCesRadiusUserLoginAcctAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAuthKey.setStatus("current")


class _CienaCesRadiusUserLoginAcctSearchType_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAcctSearchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cached", 1),
          ("priority", 2))
    )


_CienaCesRadiusUserLoginAcctSearchType_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAcctSearchType_Object = MibScalar
cienaCesRadiusUserLoginAcctSearchType = _CienaCesRadiusUserLoginAcctSearchType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1, 5),
    _CienaCesRadiusUserLoginAcctSearchType_Type()
)
cienaCesRadiusUserLoginAcctSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctSearchType.setStatus("current")


class _CienaCesRadiusUserLoginAcctAuthSecret_Type(OctetString):
    """Custom type cienaCesRadiusUserLoginAcctAuthSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 259),
    )


_CienaCesRadiusUserLoginAcctAuthSecret_Type.__name__ = "OctetString"
_CienaCesRadiusUserLoginAcctAuthSecret_Object = MibScalar
cienaCesRadiusUserLoginAcctAuthSecret = _CienaCesRadiusUserLoginAcctAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 1, 6),
    _CienaCesRadiusUserLoginAcctAuthSecret_Type()
)
cienaCesRadiusUserLoginAcctAuthSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAuthSecret.setStatus("current")
_CienaCesRadiusUserLoginAcctTable_Object = MibTable
cienaCesRadiusUserLoginAcctTable = _CienaCesRadiusUserLoginAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctTable.setStatus("current")
_CienaCesRadiusUserLoginAcctEntry_Object = MibTableRow
cienaCesRadiusUserLoginAcctEntry = _CienaCesRadiusUserLoginAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1)
)
cienaCesRadiusUserLoginAcctEntry.setIndexNames(
    (0, "CIENA-CES-RADIUS-CLIENT-MIB", "cienaCesRadiusUserLoginAcctIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctEntry.setStatus("current")


class _CienaCesRadiusUserLoginAcctIndex_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAcctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesRadiusUserLoginAcctIndex_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAcctIndex_Object = MibTableColumn
cienaCesRadiusUserLoginAcctIndex = _CienaCesRadiusUserLoginAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 1),
    _CienaCesRadiusUserLoginAcctIndex_Type()
)
cienaCesRadiusUserLoginAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctIndex.setStatus("current")
_CienaCesRadiusUserLoginAcctResolvedInetAddrType_Type = InetAddressType
_CienaCesRadiusUserLoginAcctResolvedInetAddrType_Object = MibTableColumn
cienaCesRadiusUserLoginAcctResolvedInetAddrType = _CienaCesRadiusUserLoginAcctResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 2),
    _CienaCesRadiusUserLoginAcctResolvedInetAddrType_Type()
)
cienaCesRadiusUserLoginAcctResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctResolvedInetAddrType.setStatus("current")
_CienaCesRadiusUserLoginAcctResolvedInetAddress_Type = InetAddress
_CienaCesRadiusUserLoginAcctResolvedInetAddress_Object = MibTableColumn
cienaCesRadiusUserLoginAcctResolvedInetAddress = _CienaCesRadiusUserLoginAcctResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 3),
    _CienaCesRadiusUserLoginAcctResolvedInetAddress_Type()
)
cienaCesRadiusUserLoginAcctResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctResolvedInetAddress.setStatus("current")
_CienaCesRadiusUserLoginAcctAddr_Type = DisplayString
_CienaCesRadiusUserLoginAcctAddr_Object = MibTableColumn
cienaCesRadiusUserLoginAcctAddr = _CienaCesRadiusUserLoginAcctAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 4),
    _CienaCesRadiusUserLoginAcctAddr_Type()
)
cienaCesRadiusUserLoginAcctAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAddr.setStatus("current")
_CienaCesRadiusUserLoginAcctPriority_Type = Integer32
_CienaCesRadiusUserLoginAcctPriority_Object = MibTableColumn
cienaCesRadiusUserLoginAcctPriority = _CienaCesRadiusUserLoginAcctPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 5),
    _CienaCesRadiusUserLoginAcctPriority_Type()
)
cienaCesRadiusUserLoginAcctPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctPriority.setStatus("current")


class _CienaCesRadiusUserLoginAcctAuthPort_Type(Integer32):
    """Custom type cienaCesRadiusUserLoginAcctAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRadiusUserLoginAcctAuthPort_Type.__name__ = "Integer32"
_CienaCesRadiusUserLoginAcctAuthPort_Object = MibTableColumn
cienaCesRadiusUserLoginAcctAuthPort = _CienaCesRadiusUserLoginAcctAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 6),
    _CienaCesRadiusUserLoginAcctAuthPort_Type()
)
cienaCesRadiusUserLoginAcctAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAuthPort.setStatus("current")
_CienaCesRadiusUserLoginAcctClearStatistics_Type = TruthValue
_CienaCesRadiusUserLoginAcctClearStatistics_Object = MibTableColumn
cienaCesRadiusUserLoginAcctClearStatistics = _CienaCesRadiusUserLoginAcctClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 7),
    _CienaCesRadiusUserLoginAcctClearStatistics_Type()
)
cienaCesRadiusUserLoginAcctClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctClearStatistics.setStatus("current")
_CienaCesRadiusUserLoginAcctRoundTripTime_Type = TimeTicks
_CienaCesRadiusUserLoginAcctRoundTripTime_Object = MibTableColumn
cienaCesRadiusUserLoginAcctRoundTripTime = _CienaCesRadiusUserLoginAcctRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 8),
    _CienaCesRadiusUserLoginAcctRoundTripTime_Type()
)
cienaCesRadiusUserLoginAcctRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctRoundTripTime.setStatus("current")
_CienaCesRadiusUserLoginAcctRequests_Type = Counter32
_CienaCesRadiusUserLoginAcctRequests_Object = MibTableColumn
cienaCesRadiusUserLoginAcctRequests = _CienaCesRadiusUserLoginAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 9),
    _CienaCesRadiusUserLoginAcctRequests_Type()
)
cienaCesRadiusUserLoginAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctRequests.setStatus("current")
_CienaCesRadiusUserLoginAcctRetransmissions_Type = Counter32
_CienaCesRadiusUserLoginAcctRetransmissions_Object = MibTableColumn
cienaCesRadiusUserLoginAcctRetransmissions = _CienaCesRadiusUserLoginAcctRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 10),
    _CienaCesRadiusUserLoginAcctRetransmissions_Type()
)
cienaCesRadiusUserLoginAcctRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctRetransmissions.setStatus("current")
_CienaCesRadiusUserLoginAcctAccessAccepts_Type = Counter32
_CienaCesRadiusUserLoginAcctAccessAccepts_Object = MibTableColumn
cienaCesRadiusUserLoginAcctAccessAccepts = _CienaCesRadiusUserLoginAcctAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 11),
    _CienaCesRadiusUserLoginAcctAccessAccepts_Type()
)
cienaCesRadiusUserLoginAcctAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAccessAccepts.setStatus("current")
_CienaCesRadiusUserLoginAcctAccessRejects_Type = Counter32
_CienaCesRadiusUserLoginAcctAccessRejects_Object = MibTableColumn
cienaCesRadiusUserLoginAcctAccessRejects = _CienaCesRadiusUserLoginAcctAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 12),
    _CienaCesRadiusUserLoginAcctAccessRejects_Type()
)
cienaCesRadiusUserLoginAcctAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAccessRejects.setStatus("current")
_CienaCesRadiusUserLoginAcctAccessChallenges_Type = Counter32
_CienaCesRadiusUserLoginAcctAccessChallenges_Object = MibTableColumn
cienaCesRadiusUserLoginAcctAccessChallenges = _CienaCesRadiusUserLoginAcctAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 13),
    _CienaCesRadiusUserLoginAcctAccessChallenges_Type()
)
cienaCesRadiusUserLoginAcctAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAccessChallenges.setStatus("current")
_CienaCesRadiusUserLoginAcctAccountingResponses_Type = Counter32
_CienaCesRadiusUserLoginAcctAccountingResponses_Object = MibTableColumn
cienaCesRadiusUserLoginAcctAccountingResponses = _CienaCesRadiusUserLoginAcctAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 14),
    _CienaCesRadiusUserLoginAcctAccountingResponses_Type()
)
cienaCesRadiusUserLoginAcctAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctAccountingResponses.setStatus("current")
_CienaCesRadiusUserLoginAcctMalformedResponses_Type = Counter32
_CienaCesRadiusUserLoginAcctMalformedResponses_Object = MibTableColumn
cienaCesRadiusUserLoginAcctMalformedResponses = _CienaCesRadiusUserLoginAcctMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 15),
    _CienaCesRadiusUserLoginAcctMalformedResponses_Type()
)
cienaCesRadiusUserLoginAcctMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctMalformedResponses.setStatus("current")
_CienaCesRadiusUserLoginAcctBadAuthenticators_Type = Counter32
_CienaCesRadiusUserLoginAcctBadAuthenticators_Object = MibTableColumn
cienaCesRadiusUserLoginAcctBadAuthenticators = _CienaCesRadiusUserLoginAcctBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 16),
    _CienaCesRadiusUserLoginAcctBadAuthenticators_Type()
)
cienaCesRadiusUserLoginAcctBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctBadAuthenticators.setStatus("current")
_CienaCesRadiusUserLoginAcctTimeouts_Type = Counter32
_CienaCesRadiusUserLoginAcctTimeouts_Object = MibTableColumn
cienaCesRadiusUserLoginAcctTimeouts = _CienaCesRadiusUserLoginAcctTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 17),
    _CienaCesRadiusUserLoginAcctTimeouts_Type()
)
cienaCesRadiusUserLoginAcctTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctTimeouts.setStatus("current")
_CienaCesRadiusUserLoginAcctUnknownTypes_Type = Counter32
_CienaCesRadiusUserLoginAcctUnknownTypes_Object = MibTableColumn
cienaCesRadiusUserLoginAcctUnknownTypes = _CienaCesRadiusUserLoginAcctUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 18),
    _CienaCesRadiusUserLoginAcctUnknownTypes_Type()
)
cienaCesRadiusUserLoginAcctUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctUnknownTypes.setStatus("current")
_CienaCesRadiusUserLoginAcctPacketsDropped_Type = Counter32
_CienaCesRadiusUserLoginAcctPacketsDropped_Object = MibTableColumn
cienaCesRadiusUserLoginAcctPacketsDropped = _CienaCesRadiusUserLoginAcctPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 19),
    _CienaCesRadiusUserLoginAcctPacketsDropped_Type()
)
cienaCesRadiusUserLoginAcctPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctPacketsDropped.setStatus("current")
_CienaCesRadiusUserLoginAcctStatus_Type = RowStatus
_CienaCesRadiusUserLoginAcctStatus_Object = MibTableColumn
cienaCesRadiusUserLoginAcctStatus = _CienaCesRadiusUserLoginAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 1, 1, 6, 2, 1, 20),
    _CienaCesRadiusUserLoginAcctStatus_Type()
)
cienaCesRadiusUserLoginAcctStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cienaCesRadiusUserLoginAcctStatus.setStatus("current")
_CienaCesRadiusClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientMIBNotificationPrefix = _CienaCesRadiusClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 2)
)
_CienaCesRadiusClientMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientMIBNotifications = _CienaCesRadiusClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 2, 0)
)
_CienaCesRadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientMIBConformance = _CienaCesRadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 3)
)
_CienaCesRadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientMIBCompliances = _CienaCesRadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 3, 1)
)
_CienaCesRadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesRadiusClientMIBGroups = _CienaCesRadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 3, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-RADIUS-CLIENT-MIB",
    **{"RadiusString": RadiusString,
       "cienaCesRadiusClientMIB": cienaCesRadiusClientMIB,
       "cienaCesRadiusClientMIBObjects": cienaCesRadiusClientMIBObjects,
       "cienaCesRadiusClient": cienaCesRadiusClient,
       "cienaCesRadiusClientGlobal": cienaCesRadiusClientGlobal,
       "cienaCesRadiusAdminState": cienaCesRadiusAdminState,
       "cienaCesRadiusOperState": cienaCesRadiusOperState,
       "cienaCesRadiusClientTimeout": cienaCesRadiusClientTimeout,
       "cienaCesRadiusClientRetries": cienaCesRadiusClientRetries,
       "cienaCesRadiusClientAuthKey": cienaCesRadiusClientAuthKey,
       "cienaCesRadiusClientAuthKeyUnset": cienaCesRadiusClientAuthKeyUnset,
       "cienaCesRadiusClientSearchType": cienaCesRadiusClientSearchType,
       "cienaCesRadiusClientServer": cienaCesRadiusClientServer,
       "cienaCesRadiusClientServerTable": cienaCesRadiusClientServerTable,
       "cienaCesRadiusClientServerEntry": cienaCesRadiusClientServerEntry,
       "cienaCesRadiusClientServerIndex": cienaCesRadiusClientServerIndex,
       "cienaCesRadiusClientServerAddr": cienaCesRadiusClientServerAddr,
       "cienaCesRadiusClientServerResolvedAddr": cienaCesRadiusClientServerResolvedAddr,
       "cienaCesRadiusClientServerPriority": cienaCesRadiusClientServerPriority,
       "cienaCesRadiusClientServerAuthPort": cienaCesRadiusClientServerAuthPort,
       "cienaCesRadiusClientServerRoundTripTime": cienaCesRadiusClientServerRoundTripTime,
       "cienaCesRadiusClientServerAccessRequests": cienaCesRadiusClientServerAccessRequests,
       "cienaCesRadiusClientServerAccessRetransmissions": cienaCesRadiusClientServerAccessRetransmissions,
       "cienaCesRadiusClientServerAccessAccepts": cienaCesRadiusClientServerAccessAccepts,
       "cienaCesRadiusClientServerAccessRejects": cienaCesRadiusClientServerAccessRejects,
       "cienaCesRadiusClientServerAccessChallenges": cienaCesRadiusClientServerAccessChallenges,
       "cienaCesRadiusClientServerMalformedAccessResponses": cienaCesRadiusClientServerMalformedAccessResponses,
       "cienaCesRadiusClientServerBadAuthenticators": cienaCesRadiusClientServerBadAuthenticators,
       "cienaCesRadiusClientServerPendingRequests": cienaCesRadiusClientServerPendingRequests,
       "cienaCesRadiusClientServerTimeouts": cienaCesRadiusClientServerTimeouts,
       "cienaCesRadiusClientServerUnknownTypes": cienaCesRadiusClientServerUnknownTypes,
       "cienaCesRadiusClientServerPacketsDropped": cienaCesRadiusClientServerPacketsDropped,
       "cienaCesRadiusClientServerApplication": cienaCesRadiusClientServerApplication,
       "cienaCesRadiusClientServerStatus": cienaCesRadiusClientServerStatus,
       "cienaCesRadiusUserLogin": cienaCesRadiusUserLogin,
       "cienaCesRadiusUserLoginGlobal": cienaCesRadiusUserLoginGlobal,
       "cienaCesRadiusUserLoginTimeout": cienaCesRadiusUserLoginTimeout,
       "cienaCesRadiusUserLoginRetries": cienaCesRadiusUserLoginRetries,
       "cienaCesRadiusUserLoginAuthKey": cienaCesRadiusUserLoginAuthKey,
       "cienaCesRadiusUserLoginSearchType": cienaCesRadiusUserLoginSearchType,
       "cienaCesRadiusUserLoginAuthSecret": cienaCesRadiusUserLoginAuthSecret,
       "cienaCesRadiusUserLoginTable": cienaCesRadiusUserLoginTable,
       "cienaCesRadiusUserLoginEntry": cienaCesRadiusUserLoginEntry,
       "cienaCesRadiusUserLoginIndex": cienaCesRadiusUserLoginIndex,
       "cienaCesRadiusUserLoginResolvedInetAddrType": cienaCesRadiusUserLoginResolvedInetAddrType,
       "cienaCesRadiusUserLoginResolvedInetAddress": cienaCesRadiusUserLoginResolvedInetAddress,
       "cienaCesRadiusUserLoginAddr": cienaCesRadiusUserLoginAddr,
       "cienaCesRadiusUserLoginPriority": cienaCesRadiusUserLoginPriority,
       "cienaCesRadiusUserLoginAuthPort": cienaCesRadiusUserLoginAuthPort,
       "cienaCesRadiusUserLoginClearStatistics": cienaCesRadiusUserLoginClearStatistics,
       "cienaCesRadiusUserLoginRoundTripTime": cienaCesRadiusUserLoginRoundTripTime,
       "cienaCesRadiusUserLoginRequests": cienaCesRadiusUserLoginRequests,
       "cienaCesRadiusUserLoginRetransmissions": cienaCesRadiusUserLoginRetransmissions,
       "cienaCesRadiusUserLoginAccessAccepts": cienaCesRadiusUserLoginAccessAccepts,
       "cienaCesRadiusUserLoginAccessRejects": cienaCesRadiusUserLoginAccessRejects,
       "cienaCesRadiusUserLoginAccessChallenges": cienaCesRadiusUserLoginAccessChallenges,
       "cienaCesRadiusUserLoginAccountingResponses": cienaCesRadiusUserLoginAccountingResponses,
       "cienaCesRadiusUserLoginMalformedResponses": cienaCesRadiusUserLoginMalformedResponses,
       "cienaCesRadiusUserLoginBadAuthenticators": cienaCesRadiusUserLoginBadAuthenticators,
       "cienaCesRadiusUserLoginTimeouts": cienaCesRadiusUserLoginTimeouts,
       "cienaCesRadiusUserLoginUnknownTypes": cienaCesRadiusUserLoginUnknownTypes,
       "cienaCesRadiusUserLoginPacketsDropped": cienaCesRadiusUserLoginPacketsDropped,
       "cienaCesRadiusUserLoginStatus": cienaCesRadiusUserLoginStatus,
       "cienaCesRadiusDot1xAuth": cienaCesRadiusDot1xAuth,
       "cienaCesRadiusDot1xAuthGlobal": cienaCesRadiusDot1xAuthGlobal,
       "cienaCesRadiusDot1xAuthTimeout": cienaCesRadiusDot1xAuthTimeout,
       "cienaCesRadiusDot1xAuthRetries": cienaCesRadiusDot1xAuthRetries,
       "cienaCesRadiusDot1xAuthAuthKey": cienaCesRadiusDot1xAuthAuthKey,
       "cienaCesRadiusDot1xAuthSearchType": cienaCesRadiusDot1xAuthSearchType,
       "cienaCesRadiusDot1xAuthGreylistTimeout": cienaCesRadiusDot1xAuthGreylistTimeout,
       "cienaCesRadiusDot1xAuthAuthSecret": cienaCesRadiusDot1xAuthAuthSecret,
       "cienaCesRadiusDot1xAuthTable": cienaCesRadiusDot1xAuthTable,
       "cienaCesRadiusDot1xAuthEntry": cienaCesRadiusDot1xAuthEntry,
       "cienaCesRadiusDot1xAuthIndex": cienaCesRadiusDot1xAuthIndex,
       "cienaCesRadiusDot1xAuthResolvedInetAddrType": cienaCesRadiusDot1xAuthResolvedInetAddrType,
       "cienaCesRadiusDot1xAuthResolvedInetAddress": cienaCesRadiusDot1xAuthResolvedInetAddress,
       "cienaCesRadiusDot1xAuthAddr": cienaCesRadiusDot1xAuthAddr,
       "cienaCesRadiusDot1xAuthPriority": cienaCesRadiusDot1xAuthPriority,
       "cienaCesRadiusDot1xAuthAuthPort": cienaCesRadiusDot1xAuthAuthPort,
       "cienaCesRadiusDot1xAuthClearStatistics": cienaCesRadiusDot1xAuthClearStatistics,
       "cienaCesRadiusDot1xAuthGreylistTimeRemaining": cienaCesRadiusDot1xAuthGreylistTimeRemaining,
       "cienaCesRadiusDot1xAuthRoundTripTime": cienaCesRadiusDot1xAuthRoundTripTime,
       "cienaCesRadiusDot1xAuthRequests": cienaCesRadiusDot1xAuthRequests,
       "cienaCesRadiusDot1xAuthRetransmissions": cienaCesRadiusDot1xAuthRetransmissions,
       "cienaCesRadiusDot1xAuthAccessAccepts": cienaCesRadiusDot1xAuthAccessAccepts,
       "cienaCesRadiusDot1xAuthAccessRejects": cienaCesRadiusDot1xAuthAccessRejects,
       "cienaCesRadiusDot1xAuthAccessChallenges": cienaCesRadiusDot1xAuthAccessChallenges,
       "cienaCesRadiusDot1xAuthAccountingResponses": cienaCesRadiusDot1xAuthAccountingResponses,
       "cienaCesRadiusDot1xAuthMalformedResponses": cienaCesRadiusDot1xAuthMalformedResponses,
       "cienaCesRadiusDot1xAuthBadAuthenticators": cienaCesRadiusDot1xAuthBadAuthenticators,
       "cienaCesRadiusDot1xAuthTimeouts": cienaCesRadiusDot1xAuthTimeouts,
       "cienaCesRadiusDot1xAuthUnknownTypes": cienaCesRadiusDot1xAuthUnknownTypes,
       "cienaCesRadiusDot1xAuthPacketsDropped": cienaCesRadiusDot1xAuthPacketsDropped,
       "cienaCesRadiusDot1xAuthStatus": cienaCesRadiusDot1xAuthStatus,
       "cienaCesRadiusDot1xAcct": cienaCesRadiusDot1xAcct,
       "cienaCesRadiusDot1xAcctGlobal": cienaCesRadiusDot1xAcctGlobal,
       "cienaCesRadiusDot1xAcctAdminState": cienaCesRadiusDot1xAcctAdminState,
       "cienaCesRadiusDot1xAcctTimeout": cienaCesRadiusDot1xAcctTimeout,
       "cienaCesRadiusDot1xAcctRetries": cienaCesRadiusDot1xAcctRetries,
       "cienaCesRadiusDot1xAcctAuthKey": cienaCesRadiusDot1xAcctAuthKey,
       "cienaCesRadiusDot1xAcctSearchType": cienaCesRadiusDot1xAcctSearchType,
       "cienaCesRadiusDot1xAcctGreylistTimeout": cienaCesRadiusDot1xAcctGreylistTimeout,
       "cienaCesRadiusDot1xAcctAuthSecret": cienaCesRadiusDot1xAcctAuthSecret,
       "cienaCesRadiusDot1xAcctTable": cienaCesRadiusDot1xAcctTable,
       "cienaCesRadiusDot1xAcctEntry": cienaCesRadiusDot1xAcctEntry,
       "cienaCesRadiusDot1xAcctIndex": cienaCesRadiusDot1xAcctIndex,
       "cienaCesRadiusDot1xAcctResolvedInetAddrType": cienaCesRadiusDot1xAcctResolvedInetAddrType,
       "cienaCesRadiusDot1xAcctResolvedInetAddress": cienaCesRadiusDot1xAcctResolvedInetAddress,
       "cienaCesRadiusDot1xAcctAddr": cienaCesRadiusDot1xAcctAddr,
       "cienaCesRadiusDot1xAcctPriority": cienaCesRadiusDot1xAcctPriority,
       "cienaCesRadiusDot1xAcctAuthPort": cienaCesRadiusDot1xAcctAuthPort,
       "cienaCesRadiusDot1xAcctClearStatistics": cienaCesRadiusDot1xAcctClearStatistics,
       "cienaCesRadiusDot1xAcctGreylistTimeRemaining": cienaCesRadiusDot1xAcctGreylistTimeRemaining,
       "cienaCesRadiusDot1xAcctRoundTripTime": cienaCesRadiusDot1xAcctRoundTripTime,
       "cienaCesRadiusDot1xAcctRequests": cienaCesRadiusDot1xAcctRequests,
       "cienaCesRadiusDot1xAcctRetransmissions": cienaCesRadiusDot1xAcctRetransmissions,
       "cienaCesRadiusDot1xAcctAccessAccepts": cienaCesRadiusDot1xAcctAccessAccepts,
       "cienaCesRadiusDot1xAcctAccessRejects": cienaCesRadiusDot1xAcctAccessRejects,
       "cienaCesRadiusDot1xAcctAccessChallenges": cienaCesRadiusDot1xAcctAccessChallenges,
       "cienaCesRadiusDot1xAcctAccountingResponses": cienaCesRadiusDot1xAcctAccountingResponses,
       "cienaCesRadiusDot1xAcctMalformedResponses": cienaCesRadiusDot1xAcctMalformedResponses,
       "cienaCesRadiusDot1xAcctBadAuthenticators": cienaCesRadiusDot1xAcctBadAuthenticators,
       "cienaCesRadiusDot1xAcctTimeouts": cienaCesRadiusDot1xAcctTimeouts,
       "cienaCesRadiusDot1xAcctUnknownTypes": cienaCesRadiusDot1xAcctUnknownTypes,
       "cienaCesRadiusDot1xAcctPacketsDropped": cienaCesRadiusDot1xAcctPacketsDropped,
       "cienaCesRadiusDot1xAcctStatus": cienaCesRadiusDot1xAcctStatus,
       "cienaCesRadiusUserLoginAcct": cienaCesRadiusUserLoginAcct,
       "cienaCesRadiusUserLoginAcctGlobal": cienaCesRadiusUserLoginAcctGlobal,
       "cienaCesRadiusUserLoginAcctAdminState": cienaCesRadiusUserLoginAcctAdminState,
       "cienaCesRadiusUserLoginAcctTimeout": cienaCesRadiusUserLoginAcctTimeout,
       "cienaCesRadiusUserLoginAcctRetries": cienaCesRadiusUserLoginAcctRetries,
       "cienaCesRadiusUserLoginAcctAuthKey": cienaCesRadiusUserLoginAcctAuthKey,
       "cienaCesRadiusUserLoginAcctSearchType": cienaCesRadiusUserLoginAcctSearchType,
       "cienaCesRadiusUserLoginAcctAuthSecret": cienaCesRadiusUserLoginAcctAuthSecret,
       "cienaCesRadiusUserLoginAcctTable": cienaCesRadiusUserLoginAcctTable,
       "cienaCesRadiusUserLoginAcctEntry": cienaCesRadiusUserLoginAcctEntry,
       "cienaCesRadiusUserLoginAcctIndex": cienaCesRadiusUserLoginAcctIndex,
       "cienaCesRadiusUserLoginAcctResolvedInetAddrType": cienaCesRadiusUserLoginAcctResolvedInetAddrType,
       "cienaCesRadiusUserLoginAcctResolvedInetAddress": cienaCesRadiusUserLoginAcctResolvedInetAddress,
       "cienaCesRadiusUserLoginAcctAddr": cienaCesRadiusUserLoginAcctAddr,
       "cienaCesRadiusUserLoginAcctPriority": cienaCesRadiusUserLoginAcctPriority,
       "cienaCesRadiusUserLoginAcctAuthPort": cienaCesRadiusUserLoginAcctAuthPort,
       "cienaCesRadiusUserLoginAcctClearStatistics": cienaCesRadiusUserLoginAcctClearStatistics,
       "cienaCesRadiusUserLoginAcctRoundTripTime": cienaCesRadiusUserLoginAcctRoundTripTime,
       "cienaCesRadiusUserLoginAcctRequests": cienaCesRadiusUserLoginAcctRequests,
       "cienaCesRadiusUserLoginAcctRetransmissions": cienaCesRadiusUserLoginAcctRetransmissions,
       "cienaCesRadiusUserLoginAcctAccessAccepts": cienaCesRadiusUserLoginAcctAccessAccepts,
       "cienaCesRadiusUserLoginAcctAccessRejects": cienaCesRadiusUserLoginAcctAccessRejects,
       "cienaCesRadiusUserLoginAcctAccessChallenges": cienaCesRadiusUserLoginAcctAccessChallenges,
       "cienaCesRadiusUserLoginAcctAccountingResponses": cienaCesRadiusUserLoginAcctAccountingResponses,
       "cienaCesRadiusUserLoginAcctMalformedResponses": cienaCesRadiusUserLoginAcctMalformedResponses,
       "cienaCesRadiusUserLoginAcctBadAuthenticators": cienaCesRadiusUserLoginAcctBadAuthenticators,
       "cienaCesRadiusUserLoginAcctTimeouts": cienaCesRadiusUserLoginAcctTimeouts,
       "cienaCesRadiusUserLoginAcctUnknownTypes": cienaCesRadiusUserLoginAcctUnknownTypes,
       "cienaCesRadiusUserLoginAcctPacketsDropped": cienaCesRadiusUserLoginAcctPacketsDropped,
       "cienaCesRadiusUserLoginAcctStatus": cienaCesRadiusUserLoginAcctStatus,
       "cienaCesRadiusClientMIBNotificationPrefix": cienaCesRadiusClientMIBNotificationPrefix,
       "cienaCesRadiusClientMIBNotifications": cienaCesRadiusClientMIBNotifications,
       "cienaCesRadiusClientMIBConformance": cienaCesRadiusClientMIBConformance,
       "cienaCesRadiusClientMIBCompliances": cienaCesRadiusClientMIBCompliances,
       "cienaCesRadiusClientMIBGroups": cienaCesRadiusClientMIBGroups}
)
