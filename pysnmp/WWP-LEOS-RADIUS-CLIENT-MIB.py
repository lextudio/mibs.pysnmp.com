# SNMP MIB module (WWP-LEOS-RADIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-RADIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:05 2024
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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosRadiusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20)
)
wwpLeosRadiusClientMIB.setRevisions(
        ("2012-04-26 00:00",
         "2012-04-05 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadiusString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosRadiusClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClientMIBObjects = _WwpLeosRadiusClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1)
)
_WwpLeosRadiusClient_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClient = _WwpLeosRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1)
)


class _WwpLeosRadiusAdminState_Type(Integer32):
    """Custom type wwpLeosRadiusAdminState based on Integer32"""
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


_WwpLeosRadiusAdminState_Type.__name__ = "Integer32"
_WwpLeosRadiusAdminState_Object = MibScalar
wwpLeosRadiusAdminState = _WwpLeosRadiusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 1),
    _WwpLeosRadiusAdminState_Type()
)
wwpLeosRadiusAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusAdminState.setStatus("current")


class _WwpLeosRadiusOperState_Type(Integer32):
    """Custom type wwpLeosRadiusOperState based on Integer32"""
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


_WwpLeosRadiusOperState_Type.__name__ = "Integer32"
_WwpLeosRadiusOperState_Object = MibScalar
wwpLeosRadiusOperState = _WwpLeosRadiusOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 2),
    _WwpLeosRadiusOperState_Type()
)
wwpLeosRadiusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusOperState.setStatus("current")


class _WwpLeosRadiusClientTimeout_Type(Integer32):
    """Custom type wwpLeosRadiusClientTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosRadiusClientTimeout_Type.__name__ = "Integer32"
_WwpLeosRadiusClientTimeout_Object = MibScalar
wwpLeosRadiusClientTimeout = _WwpLeosRadiusClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 3),
    _WwpLeosRadiusClientTimeout_Type()
)
wwpLeosRadiusClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientTimeout.setUnits("seconds")


class _WwpLeosRadiusClientRetries_Type(Integer32):
    """Custom type wwpLeosRadiusClientRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosRadiusClientRetries_Type.__name__ = "Integer32"
_WwpLeosRadiusClientRetries_Object = MibScalar
wwpLeosRadiusClientRetries = _WwpLeosRadiusClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 4),
    _WwpLeosRadiusClientRetries_Type()
)
wwpLeosRadiusClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientRetries.setStatus("current")
_WwpLeosRadiusClientAuthKey_Type = RadiusString
_WwpLeosRadiusClientAuthKey_Object = MibScalar
wwpLeosRadiusClientAuthKey = _WwpLeosRadiusClientAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 5),
    _WwpLeosRadiusClientAuthKey_Type()
)
wwpLeosRadiusClientAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientAuthKey.setStatus("current")
_WwpLeosRadiusClientServerTable_Object = MibTable
wwpLeosRadiusClientServerTable = _WwpLeosRadiusClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerTable.setStatus("current")
_WwpLeosRadiusClientServerEntry_Object = MibTableRow
wwpLeosRadiusClientServerEntry = _WwpLeosRadiusClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1)
)
wwpLeosRadiusClientServerEntry.setIndexNames(
    (0, "WWP-LEOS-RADIUS-CLIENT-MIB", "wwpLeosRadiusClientServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerEntry.setStatus("current")


class _WwpLeosRadiusClientServerIndex_Type(Integer32):
    """Custom type wwpLeosRadiusClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosRadiusClientServerIndex_Type.__name__ = "Integer32"
_WwpLeosRadiusClientServerIndex_Object = MibTableColumn
wwpLeosRadiusClientServerIndex = _WwpLeosRadiusClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 1),
    _WwpLeosRadiusClientServerIndex_Type()
)
wwpLeosRadiusClientServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerIndex.setStatus("current")
_WwpLeosRadiusClientServerAddr_Type = DisplayString
_WwpLeosRadiusClientServerAddr_Object = MibTableColumn
wwpLeosRadiusClientServerAddr = _WwpLeosRadiusClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 2),
    _WwpLeosRadiusClientServerAddr_Type()
)
wwpLeosRadiusClientServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAddr.setStatus("current")
_WwpLeosRadiusClientServerResolvedAddr_Type = IpAddress
_WwpLeosRadiusClientServerResolvedAddr_Object = MibTableColumn
wwpLeosRadiusClientServerResolvedAddr = _WwpLeosRadiusClientServerResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 3),
    _WwpLeosRadiusClientServerResolvedAddr_Type()
)
wwpLeosRadiusClientServerResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerResolvedAddr.setStatus("current")


class _WwpLeosRadiusClientServerPriority_Type(Integer32):
    """Custom type wwpLeosRadiusClientServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosRadiusClientServerPriority_Type.__name__ = "Integer32"
_WwpLeosRadiusClientServerPriority_Object = MibTableColumn
wwpLeosRadiusClientServerPriority = _WwpLeosRadiusClientServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 4),
    _WwpLeosRadiusClientServerPriority_Type()
)
wwpLeosRadiusClientServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerPriority.setStatus("current")


class _WwpLeosRadiusClientServerAuthPort_Type(Integer32):
    """Custom type wwpLeosRadiusClientServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRadiusClientServerAuthPort_Type.__name__ = "Integer32"
_WwpLeosRadiusClientServerAuthPort_Object = MibTableColumn
wwpLeosRadiusClientServerAuthPort = _WwpLeosRadiusClientServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 5),
    _WwpLeosRadiusClientServerAuthPort_Type()
)
wwpLeosRadiusClientServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAuthPort.setStatus("current")
_WwpLeosRadiusClientServerRoundTripTime_Type = TimeTicks
_WwpLeosRadiusClientServerRoundTripTime_Object = MibTableColumn
wwpLeosRadiusClientServerRoundTripTime = _WwpLeosRadiusClientServerRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 6),
    _WwpLeosRadiusClientServerRoundTripTime_Type()
)
wwpLeosRadiusClientServerRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerRoundTripTime.setStatus("current")
_WwpLeosRadiusClientServerAccessRequests_Type = Counter32
_WwpLeosRadiusClientServerAccessRequests_Object = MibTableColumn
wwpLeosRadiusClientServerAccessRequests = _WwpLeosRadiusClientServerAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 7),
    _WwpLeosRadiusClientServerAccessRequests_Type()
)
wwpLeosRadiusClientServerAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAccessRequests.setStatus("current")
_WwpLeosRadiusClientServerAccessRetransmissions_Type = Counter32
_WwpLeosRadiusClientServerAccessRetransmissions_Object = MibTableColumn
wwpLeosRadiusClientServerAccessRetransmissions = _WwpLeosRadiusClientServerAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 8),
    _WwpLeosRadiusClientServerAccessRetransmissions_Type()
)
wwpLeosRadiusClientServerAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAccessRetransmissions.setStatus("current")
_WwpLeosRadiusClientServerAccessAccepts_Type = Counter32
_WwpLeosRadiusClientServerAccessAccepts_Object = MibTableColumn
wwpLeosRadiusClientServerAccessAccepts = _WwpLeosRadiusClientServerAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 9),
    _WwpLeosRadiusClientServerAccessAccepts_Type()
)
wwpLeosRadiusClientServerAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAccessAccepts.setStatus("current")
_WwpLeosRadiusClientServerAccessRejects_Type = Counter32
_WwpLeosRadiusClientServerAccessRejects_Object = MibTableColumn
wwpLeosRadiusClientServerAccessRejects = _WwpLeosRadiusClientServerAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 10),
    _WwpLeosRadiusClientServerAccessRejects_Type()
)
wwpLeosRadiusClientServerAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAccessRejects.setStatus("current")
_WwpLeosRadiusClientServerAccessChallenges_Type = Counter32
_WwpLeosRadiusClientServerAccessChallenges_Object = MibTableColumn
wwpLeosRadiusClientServerAccessChallenges = _WwpLeosRadiusClientServerAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 11),
    _WwpLeosRadiusClientServerAccessChallenges_Type()
)
wwpLeosRadiusClientServerAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerAccessChallenges.setStatus("current")
_WwpLeosRadiusClientServerMalformedAccessResponses_Type = Counter32
_WwpLeosRadiusClientServerMalformedAccessResponses_Object = MibTableColumn
wwpLeosRadiusClientServerMalformedAccessResponses = _WwpLeosRadiusClientServerMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 12),
    _WwpLeosRadiusClientServerMalformedAccessResponses_Type()
)
wwpLeosRadiusClientServerMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerMalformedAccessResponses.setStatus("current")
_WwpLeosRadiusClientServerBadAuthenticators_Type = Counter32
_WwpLeosRadiusClientServerBadAuthenticators_Object = MibTableColumn
wwpLeosRadiusClientServerBadAuthenticators = _WwpLeosRadiusClientServerBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 13),
    _WwpLeosRadiusClientServerBadAuthenticators_Type()
)
wwpLeosRadiusClientServerBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerBadAuthenticators.setStatus("current")
_WwpLeosRadiusClientServerPendingRequests_Type = Gauge32
_WwpLeosRadiusClientServerPendingRequests_Object = MibTableColumn
wwpLeosRadiusClientServerPendingRequests = _WwpLeosRadiusClientServerPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 14),
    _WwpLeosRadiusClientServerPendingRequests_Type()
)
wwpLeosRadiusClientServerPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerPendingRequests.setStatus("current")
_WwpLeosRadiusClientServerTimeouts_Type = Counter32
_WwpLeosRadiusClientServerTimeouts_Object = MibTableColumn
wwpLeosRadiusClientServerTimeouts = _WwpLeosRadiusClientServerTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 15),
    _WwpLeosRadiusClientServerTimeouts_Type()
)
wwpLeosRadiusClientServerTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerTimeouts.setStatus("current")
_WwpLeosRadiusClientServerUnknownTypes_Type = Counter32
_WwpLeosRadiusClientServerUnknownTypes_Object = MibTableColumn
wwpLeosRadiusClientServerUnknownTypes = _WwpLeosRadiusClientServerUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 16),
    _WwpLeosRadiusClientServerUnknownTypes_Type()
)
wwpLeosRadiusClientServerUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerUnknownTypes.setStatus("current")
_WwpLeosRadiusClientServerPacketsDropped_Type = Counter32
_WwpLeosRadiusClientServerPacketsDropped_Object = MibTableColumn
wwpLeosRadiusClientServerPacketsDropped = _WwpLeosRadiusClientServerPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 17),
    _WwpLeosRadiusClientServerPacketsDropped_Type()
)
wwpLeosRadiusClientServerPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerPacketsDropped.setStatus("current")
_WwpLeosRadiusClientServerStatus_Type = RowStatus
_WwpLeosRadiusClientServerStatus_Object = MibTableColumn
wwpLeosRadiusClientServerStatus = _WwpLeosRadiusClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 18),
    _WwpLeosRadiusClientServerStatus_Type()
)
wwpLeosRadiusClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerStatus.setStatus("current")


class _WwpLeosRadiusClientServerApplication_Type(Integer32):
    """Custom type wwpLeosRadiusClientServerApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("dot1x", 2),
          ("userLogin", 1))
    )


_WwpLeosRadiusClientServerApplication_Type.__name__ = "Integer32"
_WwpLeosRadiusClientServerApplication_Object = MibTableColumn
wwpLeosRadiusClientServerApplication = _WwpLeosRadiusClientServerApplication_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 19),
    _WwpLeosRadiusClientServerApplication_Type()
)
wwpLeosRadiusClientServerApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerApplication.setStatus("current")
_WwpLeosRadiusClientServerResolvedInetAddrType_Type = InetAddressType
_WwpLeosRadiusClientServerResolvedInetAddrType_Object = MibTableColumn
wwpLeosRadiusClientServerResolvedInetAddrType = _WwpLeosRadiusClientServerResolvedInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 20),
    _WwpLeosRadiusClientServerResolvedInetAddrType_Type()
)
wwpLeosRadiusClientServerResolvedInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerResolvedInetAddrType.setStatus("current")
_WwpLeosRadiusClientServerResolvedInetAddress_Type = InetAddress
_WwpLeosRadiusClientServerResolvedInetAddress_Object = MibTableColumn
wwpLeosRadiusClientServerResolvedInetAddress = _WwpLeosRadiusClientServerResolvedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 21),
    _WwpLeosRadiusClientServerResolvedInetAddress_Type()
)
wwpLeosRadiusClientServerResolvedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientServerResolvedInetAddress.setStatus("current")
_WwpLeosRadiusClientAuthKeyUnset_Type = TruthValue
_WwpLeosRadiusClientAuthKeyUnset_Object = MibScalar
wwpLeosRadiusClientAuthKeyUnset = _WwpLeosRadiusClientAuthKeyUnset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 7),
    _WwpLeosRadiusClientAuthKeyUnset_Type()
)
wwpLeosRadiusClientAuthKeyUnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientAuthKeyUnset.setStatus("current")
_WwpLeosRadiusClientAuthSecretUnset_Type = TruthValue
_WwpLeosRadiusClientAuthSecretUnset_Object = MibScalar
wwpLeosRadiusClientAuthSecretUnset = _WwpLeosRadiusClientAuthSecretUnset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 8),
    _WwpLeosRadiusClientAuthSecretUnset_Type()
)
wwpLeosRadiusClientAuthSecretUnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientAuthSecretUnset.setStatus("current")


class _WwpLeosRadiusClientSearchType_Type(Integer32):
    """Custom type wwpLeosRadiusClientSearchType based on Integer32"""
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


_WwpLeosRadiusClientSearchType_Type.__name__ = "Integer32"
_WwpLeosRadiusClientSearchType_Object = MibScalar
wwpLeosRadiusClientSearchType = _WwpLeosRadiusClientSearchType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 10),
    _WwpLeosRadiusClientSearchType_Type()
)
wwpLeosRadiusClientSearchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosRadiusClientSearchType.setStatus("current")
_WwpLeosRadiusClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClientMIBNotificationPrefix = _WwpLeosRadiusClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 2)
)
_WwpLeosRadiusClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClientMIBNotifications = _WwpLeosRadiusClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 2, 0)
)
_WwpLeosRadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClientMIBConformance = _WwpLeosRadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 3)
)
_WwpLeosRadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClientMIBCompliances = _WwpLeosRadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 3, 1)
)
_WwpLeosRadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosRadiusClientMIBGroups = _WwpLeosRadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-RADIUS-CLIENT-MIB",
    **{"RadiusString": RadiusString,
       "wwpLeosRadiusClientMIB": wwpLeosRadiusClientMIB,
       "wwpLeosRadiusClientMIBObjects": wwpLeosRadiusClientMIBObjects,
       "wwpLeosRadiusClient": wwpLeosRadiusClient,
       "wwpLeosRadiusAdminState": wwpLeosRadiusAdminState,
       "wwpLeosRadiusOperState": wwpLeosRadiusOperState,
       "wwpLeosRadiusClientTimeout": wwpLeosRadiusClientTimeout,
       "wwpLeosRadiusClientRetries": wwpLeosRadiusClientRetries,
       "wwpLeosRadiusClientAuthKey": wwpLeosRadiusClientAuthKey,
       "wwpLeosRadiusClientServerTable": wwpLeosRadiusClientServerTable,
       "wwpLeosRadiusClientServerEntry": wwpLeosRadiusClientServerEntry,
       "wwpLeosRadiusClientServerIndex": wwpLeosRadiusClientServerIndex,
       "wwpLeosRadiusClientServerAddr": wwpLeosRadiusClientServerAddr,
       "wwpLeosRadiusClientServerResolvedAddr": wwpLeosRadiusClientServerResolvedAddr,
       "wwpLeosRadiusClientServerPriority": wwpLeosRadiusClientServerPriority,
       "wwpLeosRadiusClientServerAuthPort": wwpLeosRadiusClientServerAuthPort,
       "wwpLeosRadiusClientServerRoundTripTime": wwpLeosRadiusClientServerRoundTripTime,
       "wwpLeosRadiusClientServerAccessRequests": wwpLeosRadiusClientServerAccessRequests,
       "wwpLeosRadiusClientServerAccessRetransmissions": wwpLeosRadiusClientServerAccessRetransmissions,
       "wwpLeosRadiusClientServerAccessAccepts": wwpLeosRadiusClientServerAccessAccepts,
       "wwpLeosRadiusClientServerAccessRejects": wwpLeosRadiusClientServerAccessRejects,
       "wwpLeosRadiusClientServerAccessChallenges": wwpLeosRadiusClientServerAccessChallenges,
       "wwpLeosRadiusClientServerMalformedAccessResponses": wwpLeosRadiusClientServerMalformedAccessResponses,
       "wwpLeosRadiusClientServerBadAuthenticators": wwpLeosRadiusClientServerBadAuthenticators,
       "wwpLeosRadiusClientServerPendingRequests": wwpLeosRadiusClientServerPendingRequests,
       "wwpLeosRadiusClientServerTimeouts": wwpLeosRadiusClientServerTimeouts,
       "wwpLeosRadiusClientServerUnknownTypes": wwpLeosRadiusClientServerUnknownTypes,
       "wwpLeosRadiusClientServerPacketsDropped": wwpLeosRadiusClientServerPacketsDropped,
       "wwpLeosRadiusClientServerStatus": wwpLeosRadiusClientServerStatus,
       "wwpLeosRadiusClientServerApplication": wwpLeosRadiusClientServerApplication,
       "wwpLeosRadiusClientServerResolvedInetAddrType": wwpLeosRadiusClientServerResolvedInetAddrType,
       "wwpLeosRadiusClientServerResolvedInetAddress": wwpLeosRadiusClientServerResolvedInetAddress,
       "wwpLeosRadiusClientAuthKeyUnset": wwpLeosRadiusClientAuthKeyUnset,
       "wwpLeosRadiusClientAuthSecretUnset": wwpLeosRadiusClientAuthSecretUnset,
       "wwpLeosRadiusClientSearchType": wwpLeosRadiusClientSearchType,
       "wwpLeosRadiusClientMIBNotificationPrefix": wwpLeosRadiusClientMIBNotificationPrefix,
       "wwpLeosRadiusClientMIBNotifications": wwpLeosRadiusClientMIBNotifications,
       "wwpLeosRadiusClientMIBConformance": wwpLeosRadiusClientMIBConformance,
       "wwpLeosRadiusClientMIBCompliances": wwpLeosRadiusClientMIBCompliances,
       "wwpLeosRadiusClientMIBGroups": wwpLeosRadiusClientMIBGroups}
)
