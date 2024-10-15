# SNMP MIB module (AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:24 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(PaeControlledPortStatus,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledPortStatus")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swAuthCtrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwAuthenCtrl_ObjectIdentity = ObjectIdentity
swAuthenCtrl = _SwAuthenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1)
)


class _AuthProtocol_Type(Integer32):
    """Custom type authProtocol based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authProtocolLocal", 2),
          ("authProtocolNone", 1),
          ("authProtocolRadius", 3),
          ("authProtocolRadiusChap", 5),
          ("authProtocolRadiusEap", 4),
          ("authProtocolTacacs", 6))
    )


_AuthProtocol_Type.__name__ = "Integer32"
_AuthProtocol_Object = MibScalar
authProtocol = _AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 1),
    _AuthProtocol_Type()
)
authProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authProtocol.setStatus("current")


class _SwAuthMode_Type(Integer32):
    """Custom type swAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macBase", 2),
          ("none", 3),
          ("portBase", 1))
    )


_SwAuthMode_Type.__name__ = "Integer32"
_SwAuthMode_Object = MibScalar
swAuthMode = _SwAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 2),
    _SwAuthMode_Type()
)
swAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMode.setStatus("current")
_SwRadiusCtrl_ObjectIdentity = ObjectIdentity
swRadiusCtrl = _SwRadiusCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2)
)


class _SwRadiusDeadTime_Type(Unsigned32):
    """Custom type swRadiusDeadTime based on Unsigned32"""
    defaultValue = 1


_SwRadiusDeadTime_Object = MibScalar
swRadiusDeadTime = _SwRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 1),
    _SwRadiusDeadTime_Type()
)
swRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusDeadTime.setStatus("current")


class _SwRadiusTimeout_Type(Unsigned32):
    """Custom type swRadiusTimeout based on Unsigned32"""
    defaultValue = 10


_SwRadiusTimeout_Object = MibScalar
swRadiusTimeout = _SwRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 2),
    _SwRadiusTimeout_Type()
)
swRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusTimeout.setStatus("current")


class _SwRadiusRetransmitAttempts_Type(Unsigned32):
    """Custom type swRadiusRetransmitAttempts based on Unsigned32"""
    defaultValue = 2


_SwRadiusRetransmitAttempts_Object = MibScalar
swRadiusRetransmitAttempts = _SwRadiusRetransmitAttempts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 3),
    _SwRadiusRetransmitAttempts_Type()
)
swRadiusRetransmitAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusRetransmitAttempts.setStatus("current")
_SwRadiusServerTable_Object = MibTable
swRadiusServerTable = _SwRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4)
)
if mibBuilder.loadTexts:
    swRadiusServerTable.setStatus("current")
_SwRadiusServerEntry_Object = MibTableRow
swRadiusServerEntry = _SwRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1)
)
swRadiusServerEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    swRadiusServerEntry.setStatus("current")


class _SwRadiusServerIndex_Type(Integer32):
    """Custom type swRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swRadiusServerIndex-first", 1),
          ("swRadiusServerIndex-second", 2),
          ("swRadiusServerIndex-third", 3))
    )


_SwRadiusServerIndex_Type.__name__ = "Integer32"
_SwRadiusServerIndex_Object = MibTableColumn
swRadiusServerIndex = _SwRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 1),
    _SwRadiusServerIndex_Type()
)
swRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerIndex.setStatus("current")
_SwRadiusServerIpAddr_Type = IpAddress
_SwRadiusServerIpAddr_Object = MibTableColumn
swRadiusServerIpAddr = _SwRadiusServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 2),
    _SwRadiusServerIpAddr_Type()
)
swRadiusServerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRadiusServerIpAddr.setStatus("current")


class _SwRadiusServerKey_Type(OctetString):
    """Custom type swRadiusServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwRadiusServerKey_Type.__name__ = "OctetString"
_SwRadiusServerKey_Object = MibTableColumn
swRadiusServerKey = _SwRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 3),
    _SwRadiusServerKey_Type()
)
swRadiusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRadiusServerKey.setStatus("current")


class _SwRadiusAuthPortNumber_Type(Unsigned32):
    """Custom type swRadiusAuthPortNumber based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwRadiusAuthPortNumber_Type.__name__ = "Unsigned32"
_SwRadiusAuthPortNumber_Object = MibTableColumn
swRadiusAuthPortNumber = _SwRadiusAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 4),
    _SwRadiusAuthPortNumber_Type()
)
swRadiusAuthPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRadiusAuthPortNumber.setStatus("current")


class _SwRadiusAcctPortNumber_Type(Unsigned32):
    """Custom type swRadiusAcctPortNumber based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwRadiusAcctPortNumber_Type.__name__ = "Unsigned32"
_SwRadiusAcctPortNumber_Object = MibTableColumn
swRadiusAcctPortNumber = _SwRadiusAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 5),
    _SwRadiusAcctPortNumber_Type()
)
swRadiusAcctPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRadiusAcctPortNumber.setStatus("current")
_SwRadiusServerStatus_Type = RowStatus
_SwRadiusServerStatus_Object = MibTableColumn
swRadiusServerStatus = _SwRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 6),
    _SwRadiusServerStatus_Type()
)
swRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRadiusServerStatus.setStatus("current")
_SwRadiusAuthInfo_ObjectIdentity = ObjectIdentity
swRadiusAuthInfo = _SwRadiusAuthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3)
)


class _SwRadiusAuthClientIdentifier_Type(OctetString):
    """Custom type swRadiusAuthClientIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SwRadiusAuthClientIdentifier_Type.__name__ = "OctetString"
_SwRadiusAuthClientIdentifier_Object = MibScalar
swRadiusAuthClientIdentifier = _SwRadiusAuthClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 1),
    _SwRadiusAuthClientIdentifier_Type()
)
swRadiusAuthClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientIdentifier.setStatus("obsolete")
_SwRadiusAuthClientInvalidServerAddresses_Type = Counter32
_SwRadiusAuthClientInvalidServerAddresses_Object = MibScalar
swRadiusAuthClientInvalidServerAddresses = _SwRadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 2),
    _SwRadiusAuthClientInvalidServerAddresses_Type()
)
swRadiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientInvalidServerAddresses.setStatus("obsolete")
_SwRadiusAuthServerTable_Object = MibTable
swRadiusAuthServerTable = _SwRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3)
)
if mibBuilder.loadTexts:
    swRadiusAuthServerTable.setStatus("obsolete")
_SwRadiusAuthServerEntry_Object = MibTableRow
swRadiusAuthServerEntry = _SwRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1)
)
swRadiusAuthServerEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    swRadiusAuthServerEntry.setStatus("obsolete")
_SwRadiusAuthServerIndex_Type = Integer32
_SwRadiusAuthServerIndex_Object = MibTableColumn
swRadiusAuthServerIndex = _SwRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 1),
    _SwRadiusAuthServerIndex_Type()
)
swRadiusAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthServerIndex.setStatus("obsolete")
_SwRadiusAuthServerAddress_Type = IpAddress
_SwRadiusAuthServerAddress_Object = MibTableColumn
swRadiusAuthServerAddress = _SwRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 2),
    _SwRadiusAuthServerAddress_Type()
)
swRadiusAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthServerAddress.setStatus("obsolete")


class _SwRadiusAuthClientServerPortNumber_Type(Unsigned32):
    """Custom type swRadiusAuthClientServerPortNumber based on Unsigned32"""
    defaultValue = 1812


_SwRadiusAuthClientServerPortNumber_Object = MibTableColumn
swRadiusAuthClientServerPortNumber = _SwRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 3),
    _SwRadiusAuthClientServerPortNumber_Type()
)
swRadiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientServerPortNumber.setStatus("obsolete")
_SwRadiusAuthClientRoundTripTime_Type = Counter32
_SwRadiusAuthClientRoundTripTime_Object = MibTableColumn
swRadiusAuthClientRoundTripTime = _SwRadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 4),
    _SwRadiusAuthClientRoundTripTime_Type()
)
swRadiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientRoundTripTime.setStatus("obsolete")
_SwRadiusAuthClientAccessRequests_Type = Counter32
_SwRadiusAuthClientAccessRequests_Object = MibTableColumn
swRadiusAuthClientAccessRequests = _SwRadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 5),
    _SwRadiusAuthClientAccessRequests_Type()
)
swRadiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessRequests.setStatus("obsolete")
_SwRadiusAuthClientAccessRetransmissions_Type = Counter32
_SwRadiusAuthClientAccessRetransmissions_Object = MibTableColumn
swRadiusAuthClientAccessRetransmissions = _SwRadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 6),
    _SwRadiusAuthClientAccessRetransmissions_Type()
)
swRadiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessRetransmissions.setStatus("obsolete")
_SwRadiusAuthClientAccessAccepts_Type = Counter32
_SwRadiusAuthClientAccessAccepts_Object = MibTableColumn
swRadiusAuthClientAccessAccepts = _SwRadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 7),
    _SwRadiusAuthClientAccessAccepts_Type()
)
swRadiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessAccepts.setStatus("obsolete")
_SwRadiusAuthClientAccessRejects_Type = Counter32
_SwRadiusAuthClientAccessRejects_Object = MibTableColumn
swRadiusAuthClientAccessRejects = _SwRadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 8),
    _SwRadiusAuthClientAccessRejects_Type()
)
swRadiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessRejects.setStatus("obsolete")
_SwRadiusAuthClientAccessChallenges_Type = Counter32
_SwRadiusAuthClientAccessChallenges_Object = MibTableColumn
swRadiusAuthClientAccessChallenges = _SwRadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 9),
    _SwRadiusAuthClientAccessChallenges_Type()
)
swRadiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessChallenges.setStatus("obsolete")
_SwRadiusAuthClientMalformedAccessResponses_Type = Counter32
_SwRadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
swRadiusAuthClientMalformedAccessResponses = _SwRadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 10),
    _SwRadiusAuthClientMalformedAccessResponses_Type()
)
swRadiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientMalformedAccessResponses.setStatus("obsolete")
_SwRadiusAuthClientBadAuthenticators_Type = Counter32
_SwRadiusAuthClientBadAuthenticators_Object = MibTableColumn
swRadiusAuthClientBadAuthenticators = _SwRadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 11),
    _SwRadiusAuthClientBadAuthenticators_Type()
)
swRadiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientBadAuthenticators.setStatus("obsolete")
_SwRadiusAuthClientPendingRequests_Type = Counter32
_SwRadiusAuthClientPendingRequests_Object = MibTableColumn
swRadiusAuthClientPendingRequests = _SwRadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 12),
    _SwRadiusAuthClientPendingRequests_Type()
)
swRadiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientPendingRequests.setStatus("obsolete")
_SwRadiusAuthClientTimeouts_Type = Counter32
_SwRadiusAuthClientTimeouts_Object = MibTableColumn
swRadiusAuthClientTimeouts = _SwRadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 13),
    _SwRadiusAuthClientTimeouts_Type()
)
swRadiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientTimeouts.setStatus("obsolete")
_SwRadiusAuthClientUnknownTypes_Type = Counter32
_SwRadiusAuthClientUnknownTypes_Object = MibTableColumn
swRadiusAuthClientUnknownTypes = _SwRadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 14),
    _SwRadiusAuthClientUnknownTypes_Type()
)
swRadiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientUnknownTypes.setStatus("obsolete")
_SwRadiusAuthClientPacketsDropped_Type = Counter32
_SwRadiusAuthClientPacketsDropped_Object = MibTableColumn
swRadiusAuthClientPacketsDropped = _SwRadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 15),
    _SwRadiusAuthClientPacketsDropped_Type()
)
swRadiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientPacketsDropped.setStatus("obsolete")
_SwRadiusAccountingCtrl_ObjectIdentity = ObjectIdentity
swRadiusAccountingCtrl = _SwRadiusAccountingCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4)
)


class _SwRadiusAcctUpdateInterval_Type(Unsigned32):
    """Custom type swRadiusAcctUpdateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwRadiusAcctUpdateInterval_Type.__name__ = "Unsigned32"
_SwRadiusAcctUpdateInterval_Object = MibScalar
swRadiusAcctUpdateInterval = _SwRadiusAcctUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 1),
    _SwRadiusAcctUpdateInterval_Type()
)
swRadiusAcctUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctUpdateInterval.setStatus("current")
_SwRadiusAcctSuppressNullUserName_Type = TruthValue
_SwRadiusAcctSuppressNullUserName_Object = MibScalar
swRadiusAcctSuppressNullUserName = _SwRadiusAcctSuppressNullUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 2),
    _SwRadiusAcctSuppressNullUserName_Type()
)
swRadiusAcctSuppressNullUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctSuppressNullUserName.setStatus("current")
_SwRadiusAcctServiceTable_Object = MibTable
swRadiusAcctServiceTable = _SwRadiusAcctServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3)
)
if mibBuilder.loadTexts:
    swRadiusAcctServiceTable.setStatus("current")
_SwRadiusAcctServiceEntry_Object = MibTableRow
swRadiusAcctServiceEntry = _SwRadiusAcctServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1)
)
swRadiusAcctServiceEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusAcctServiceIndex"),
)
if mibBuilder.loadTexts:
    swRadiusAcctServiceEntry.setStatus("current")


class _SwRadiusAcctServiceIndex_Type(Integer32):
    """Custom type swRadiusAcctServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acctServiceIndex-exec", 2),
          ("acctServiceIndex-network", 1),
          ("acctServiceIndex-system", 3))
    )


_SwRadiusAcctServiceIndex_Type.__name__ = "Integer32"
_SwRadiusAcctServiceIndex_Object = MibTableColumn
swRadiusAcctServiceIndex = _SwRadiusAcctServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 1),
    _SwRadiusAcctServiceIndex_Type()
)
swRadiusAcctServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctServiceIndex.setStatus("current")


class _SwRadiusAcctServiceMethod_Type(Integer32):
    """Custom type swRadiusAcctServiceMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swRadiusAcctServiceMethodNone", 1),
          ("swRadiusAcctServiceMethodRadius", 2))
    )


_SwRadiusAcctServiceMethod_Type.__name__ = "Integer32"
_SwRadiusAcctServiceMethod_Object = MibTableColumn
swRadiusAcctServiceMethod = _SwRadiusAcctServiceMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 2),
    _SwRadiusAcctServiceMethod_Type()
)
swRadiusAcctServiceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctServiceMethod.setStatus("current")


class _SwRadiusAcctServiceMode_Type(Integer32):
    """Custom type swRadiusAcctServiceMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radiusAcctServiceModeNone", 1),
          ("radiusAcctServiceModeStartStop", 2),
          ("radiusAcctServiceModeStopOnly", 3))
    )


_SwRadiusAcctServiceMode_Type.__name__ = "Integer32"
_SwRadiusAcctServiceMode_Object = MibTableColumn
swRadiusAcctServiceMode = _SwRadiusAcctServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 3),
    _SwRadiusAcctServiceMode_Type()
)
swRadiusAcctServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctServiceMode.setStatus("current")
_SwRadiusAccountingInfo_ObjectIdentity = ObjectIdentity
swRadiusAccountingInfo = _SwRadiusAccountingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5)
)


class _SwRadiusAcctClientIdentifier_Type(OctetString):
    """Custom type swRadiusAcctClientIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SwRadiusAcctClientIdentifier_Type.__name__ = "OctetString"
_SwRadiusAcctClientIdentifier_Object = MibScalar
swRadiusAcctClientIdentifier = _SwRadiusAcctClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 1),
    _SwRadiusAcctClientIdentifier_Type()
)
swRadiusAcctClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientIdentifier.setStatus("obsolete")
_SwRadiusAcctClientInvalidServerAddresses_Type = Counter32
_SwRadiusAcctClientInvalidServerAddresses_Object = MibScalar
swRadiusAcctClientInvalidServerAddresses = _SwRadiusAcctClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 2),
    _SwRadiusAcctClientInvalidServerAddresses_Type()
)
swRadiusAcctClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientInvalidServerAddresses.setStatus("obsolete")
_SwRadiusAcctServerTable_Object = MibTable
swRadiusAcctServerTable = _SwRadiusAcctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3)
)
if mibBuilder.loadTexts:
    swRadiusAcctServerTable.setStatus("obsolete")
_SwRadiusAcctServerEntry_Object = MibTableRow
swRadiusAcctServerEntry = _SwRadiusAcctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1)
)
swRadiusAcctServerEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    swRadiusAcctServerEntry.setStatus("obsolete")
_SwRadiusAcctServerIndex_Type = Integer32
_SwRadiusAcctServerIndex_Object = MibTableColumn
swRadiusAcctServerIndex = _SwRadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 1),
    _SwRadiusAcctServerIndex_Type()
)
swRadiusAcctServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctServerIndex.setStatus("obsolete")
_SwRadiusAcctServerAddress_Type = IpAddress
_SwRadiusAcctServerAddress_Object = MibTableColumn
swRadiusAcctServerAddress = _SwRadiusAcctServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 2),
    _SwRadiusAcctServerAddress_Type()
)
swRadiusAcctServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctServerAddress.setStatus("obsolete")


class _SwRadiusAcctClientServerPortNumber_Type(Unsigned32):
    """Custom type swRadiusAcctClientServerPortNumber based on Unsigned32"""
    defaultValue = 1813


_SwRadiusAcctClientServerPortNumber_Object = MibTableColumn
swRadiusAcctClientServerPortNumber = _SwRadiusAcctClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 3),
    _SwRadiusAcctClientServerPortNumber_Type()
)
swRadiusAcctClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientServerPortNumber.setStatus("obsolete")
_SwRadiusAcctClientRoundTripTime_Type = Counter32
_SwRadiusAcctClientRoundTripTime_Object = MibTableColumn
swRadiusAcctClientRoundTripTime = _SwRadiusAcctClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 4),
    _SwRadiusAcctClientRoundTripTime_Type()
)
swRadiusAcctClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientRoundTripTime.setStatus("obsolete")
_SwRadiusAcctClientRequests_Type = Counter32
_SwRadiusAcctClientRequests_Object = MibTableColumn
swRadiusAcctClientRequests = _SwRadiusAcctClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 5),
    _SwRadiusAcctClientRequests_Type()
)
swRadiusAcctClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientRequests.setStatus("obsolete")
_SwRadiusAcctClientRetransmissions_Type = Counter32
_SwRadiusAcctClientRetransmissions_Object = MibTableColumn
swRadiusAcctClientRetransmissions = _SwRadiusAcctClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 6),
    _SwRadiusAcctClientRetransmissions_Type()
)
swRadiusAcctClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientRetransmissions.setStatus("obsolete")
_SwRadiusAcctClientResponses_Type = Counter32
_SwRadiusAcctClientResponses_Object = MibTableColumn
swRadiusAcctClientResponses = _SwRadiusAcctClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 7),
    _SwRadiusAcctClientResponses_Type()
)
swRadiusAcctClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientResponses.setStatus("obsolete")
_SwRadiusAcctClientMalformedResponses_Type = Counter32
_SwRadiusAcctClientMalformedResponses_Object = MibTableColumn
swRadiusAcctClientMalformedResponses = _SwRadiusAcctClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 8),
    _SwRadiusAcctClientMalformedResponses_Type()
)
swRadiusAcctClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientMalformedResponses.setStatus("obsolete")
_SwRadiusAcctClientBadAuthenticators_Type = Counter32
_SwRadiusAcctClientBadAuthenticators_Object = MibTableColumn
swRadiusAcctClientBadAuthenticators = _SwRadiusAcctClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 9),
    _SwRadiusAcctClientBadAuthenticators_Type()
)
swRadiusAcctClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientBadAuthenticators.setStatus("obsolete")
_SwRadiusAcctClientPendingRequests_Type = Counter32
_SwRadiusAcctClientPendingRequests_Object = MibTableColumn
swRadiusAcctClientPendingRequests = _SwRadiusAcctClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 10),
    _SwRadiusAcctClientPendingRequests_Type()
)
swRadiusAcctClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientPendingRequests.setStatus("obsolete")
_SwRadiusAcctClientTimeouts_Type = Counter32
_SwRadiusAcctClientTimeouts_Object = MibTableColumn
swRadiusAcctClientTimeouts = _SwRadiusAcctClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 11),
    _SwRadiusAcctClientTimeouts_Type()
)
swRadiusAcctClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientTimeouts.setStatus("obsolete")
_SwRadiusAcctClientUnknownTypes_Type = Counter32
_SwRadiusAcctClientUnknownTypes_Object = MibTableColumn
swRadiusAcctClientUnknownTypes = _SwRadiusAcctClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 12),
    _SwRadiusAcctClientUnknownTypes_Type()
)
swRadiusAcctClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientUnknownTypes.setStatus("obsolete")
_SwRadiusAcctClientPacketsDropped_Type = Counter32
_SwRadiusAcctClientPacketsDropped_Object = MibTableColumn
swRadiusAcctClientPacketsDropped = _SwRadiusAcctClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5, 3, 1, 13),
    _SwRadiusAcctClientPacketsDropped_Type()
)
swRadiusAcctClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctClientPacketsDropped.setStatus("obsolete")
_SwMacAuthBaseStatsInfo_ObjectIdentity = ObjectIdentity
swMacAuthBaseStatsInfo = _SwMacAuthBaseStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6)
)
_SwMacAuthStateTable_Object = MibTable
swMacAuthStateTable = _SwMacAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1)
)
if mibBuilder.loadTexts:
    swMacAuthStateTable.setStatus("current")
_SwMacAuthStateEntry_Object = MibTableRow
swMacAuthStateEntry = _SwMacAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1)
)
swMacAuthStateEntry.setIndexNames(
    (0, "AUTH-MIB", "swPaeMacAddr"),
    (0, "AUTH-MIB", "swPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthStateEntry.setStatus("current")
_SwPaeMacAddr_Type = MacAddress
_SwPaeMacAddr_Object = MibTableColumn
swPaeMacAddr = _SwPaeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 1),
    _SwPaeMacAddr_Type()
)
swPaeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPaeMacAddr.setStatus("current")
_SwPaePortNumber_Type = InterfaceIndex
_SwPaePortNumber_Object = MibTableColumn
swPaePortNumber = _SwPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 2),
    _SwPaePortNumber_Type()
)
swPaePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPaePortNumber.setStatus("current")


class _SwAuthPaeState_Type(Integer32):
    """Custom type swAuthPaeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_SwAuthPaeState_Type.__name__ = "Integer32"
_SwAuthPaeState_Object = MibTableColumn
swAuthPaeState = _SwAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 3),
    _SwAuthPaeState_Type()
)
swAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthPaeState.setStatus("current")


class _SwAuthBackendAuthState_Type(Integer32):
    """Custom type swAuthBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_SwAuthBackendAuthState_Type.__name__ = "Integer32"
_SwAuthBackendAuthState_Object = MibTableColumn
swAuthBackendAuthState = _SwAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 4),
    _SwAuthBackendAuthState_Type()
)
swAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAuthState.setStatus("current")
_SwAuthAuthControlledPortStatus_Type = PaeControlledPortStatus
_SwAuthAuthControlledPortStatus_Object = MibTableColumn
swAuthAuthControlledPortStatus = _SwAuthAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 5),
    _SwAuthAuthControlledPortStatus_Type()
)
swAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthControlledPortStatus.setStatus("current")
_SwMacAuthStatsTable_Object = MibTable
swMacAuthStatsTable = _SwMacAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2)
)
if mibBuilder.loadTexts:
    swMacAuthStatsTable.setStatus("current")
_SwMacAuthStatsEntry_Object = MibTableRow
swMacAuthStatsEntry = _SwMacAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1)
)
swMacAuthStatsEntry.setIndexNames(
    (0, "AUTH-MIB", "swAuthStatsPaeMacAddr"),
    (0, "AUTH-MIB", "swAuthStatsPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthStatsEntry.setStatus("current")
_SwAuthStatsPaeMacAddr_Type = MacAddress
_SwAuthStatsPaeMacAddr_Object = MibTableColumn
swAuthStatsPaeMacAddr = _SwAuthStatsPaeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 1),
    _SwAuthStatsPaeMacAddr_Type()
)
swAuthStatsPaeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthStatsPaeMacAddr.setStatus("current")
_SwAuthStatsPaePortNumber_Type = InterfaceIndex
_SwAuthStatsPaePortNumber_Object = MibTableColumn
swAuthStatsPaePortNumber = _SwAuthStatsPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 2),
    _SwAuthStatsPaePortNumber_Type()
)
swAuthStatsPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthStatsPaePortNumber.setStatus("current")
_SwAuthEapolFramesRx_Type = Counter32
_SwAuthEapolFramesRx_Object = MibTableColumn
swAuthEapolFramesRx = _SwAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 3),
    _SwAuthEapolFramesRx_Type()
)
swAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolFramesRx.setStatus("current")
_SwAuthEapolFramesTx_Type = Counter32
_SwAuthEapolFramesTx_Object = MibTableColumn
swAuthEapolFramesTx = _SwAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 4),
    _SwAuthEapolFramesTx_Type()
)
swAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolFramesTx.setStatus("current")
_SwAuthEapolStartFramesRx_Type = Counter32
_SwAuthEapolStartFramesRx_Object = MibTableColumn
swAuthEapolStartFramesRx = _SwAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 5),
    _SwAuthEapolStartFramesRx_Type()
)
swAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolStartFramesRx.setStatus("current")
_SwAuthEapolLogoffFramesRx_Type = Counter32
_SwAuthEapolLogoffFramesRx_Object = MibTableColumn
swAuthEapolLogoffFramesRx = _SwAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 6),
    _SwAuthEapolLogoffFramesRx_Type()
)
swAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolLogoffFramesRx.setStatus("current")
_SwAuthEapolRespIdFramesRx_Type = Counter32
_SwAuthEapolRespIdFramesRx_Object = MibTableColumn
swAuthEapolRespIdFramesRx = _SwAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 7),
    _SwAuthEapolRespIdFramesRx_Type()
)
swAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolRespIdFramesRx.setStatus("current")
_SwAuthEapolRespFramesRx_Type = Counter32
_SwAuthEapolRespFramesRx_Object = MibTableColumn
swAuthEapolRespFramesRx = _SwAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 8),
    _SwAuthEapolRespFramesRx_Type()
)
swAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolRespFramesRx.setStatus("current")
_SwAuthEapolReqIdFramesTx_Type = Counter32
_SwAuthEapolReqIdFramesTx_Object = MibTableColumn
swAuthEapolReqIdFramesTx = _SwAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 9),
    _SwAuthEapolReqIdFramesTx_Type()
)
swAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolReqIdFramesTx.setStatus("current")
_SwAuthEapolReqFramesTx_Type = Counter32
_SwAuthEapolReqFramesTx_Object = MibTableColumn
swAuthEapolReqFramesTx = _SwAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 10),
    _SwAuthEapolReqFramesTx_Type()
)
swAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolReqFramesTx.setStatus("current")
_SwAuthInvalidEapolFramesRx_Type = Counter32
_SwAuthInvalidEapolFramesRx_Object = MibTableColumn
swAuthInvalidEapolFramesRx = _SwAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 11),
    _SwAuthInvalidEapolFramesRx_Type()
)
swAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthInvalidEapolFramesRx.setStatus("current")
_SwAuthEapLengthErrorFramesRx_Type = Counter32
_SwAuthEapLengthErrorFramesRx_Object = MibTableColumn
swAuthEapLengthErrorFramesRx = _SwAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 12),
    _SwAuthEapLengthErrorFramesRx_Type()
)
swAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapLengthErrorFramesRx.setStatus("current")
_SwAuthLastEapolFrameVersion_Type = Unsigned32
_SwAuthLastEapolFrameVersion_Object = MibTableColumn
swAuthLastEapolFrameVersion = _SwAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 13),
    _SwAuthLastEapolFrameVersion_Type()
)
swAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthLastEapolFrameVersion.setStatus("current")
_SwAuthLastEapolFrameSource_Type = MacAddress
_SwAuthLastEapolFrameSource_Object = MibTableColumn
swAuthLastEapolFrameSource = _SwAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 14),
    _SwAuthLastEapolFrameSource_Type()
)
swAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthLastEapolFrameSource.setStatus("current")
_SwMacAuthDiagTable_Object = MibTable
swMacAuthDiagTable = _SwMacAuthDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3)
)
if mibBuilder.loadTexts:
    swMacAuthDiagTable.setStatus("current")
_SwMacAuthDiagEntry_Object = MibTableRow
swMacAuthDiagEntry = _SwMacAuthDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1)
)
swMacAuthDiagEntry.setIndexNames(
    (0, "AUTH-MIB", "swAuthDiagPaeMacAddr"),
    (0, "AUTH-MIB", "swAuthDiagPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthDiagEntry.setStatus("current")
_SwAuthDiagPaeMacAddr_Type = MacAddress
_SwAuthDiagPaeMacAddr_Object = MibTableColumn
swAuthDiagPaeMacAddr = _SwAuthDiagPaeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 1),
    _SwAuthDiagPaeMacAddr_Type()
)
swAuthDiagPaeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthDiagPaeMacAddr.setStatus("current")
_SwAuthDiagPaePortNumber_Type = InterfaceIndex
_SwAuthDiagPaePortNumber_Object = MibTableColumn
swAuthDiagPaePortNumber = _SwAuthDiagPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 2),
    _SwAuthDiagPaePortNumber_Type()
)
swAuthDiagPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthDiagPaePortNumber.setStatus("current")
_SwAuthEntersConnecting_Type = Counter32
_SwAuthEntersConnecting_Object = MibTableColumn
swAuthEntersConnecting = _SwAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 3),
    _SwAuthEntersConnecting_Type()
)
swAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEntersConnecting.setStatus("current")
_SwAuthEapLogoffsWhileConnecting_Type = Counter32
_SwAuthEapLogoffsWhileConnecting_Object = MibTableColumn
swAuthEapLogoffsWhileConnecting = _SwAuthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 4),
    _SwAuthEapLogoffsWhileConnecting_Type()
)
swAuthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapLogoffsWhileConnecting.setStatus("current")
_SwAuthEntersAuthenticating_Type = Counter32
_SwAuthEntersAuthenticating_Object = MibTableColumn
swAuthEntersAuthenticating = _SwAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 5),
    _SwAuthEntersAuthenticating_Type()
)
swAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEntersAuthenticating.setStatus("current")
_SwAuthAuthSuccessWhileAuthenticating_Type = Counter32
_SwAuthAuthSuccessWhileAuthenticating_Object = MibTableColumn
swAuthAuthSuccessWhileAuthenticating = _SwAuthAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 6),
    _SwAuthAuthSuccessWhileAuthenticating_Type()
)
swAuthAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthSuccessWhileAuthenticating.setStatus("current")
_SwAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_SwAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
swAuthAuthTimeoutsWhileAuthenticating = _SwAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 7),
    _SwAuthAuthTimeoutsWhileAuthenticating_Type()
)
swAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_SwAuthAuthFailWhileAuthenticating_Type = Counter32
_SwAuthAuthFailWhileAuthenticating_Object = MibTableColumn
swAuthAuthFailWhileAuthenticating = _SwAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 8),
    _SwAuthAuthFailWhileAuthenticating_Type()
)
swAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthFailWhileAuthenticating.setStatus("current")
_SwAuthAuthReauthsWhileAuthenticating_Type = Counter32
_SwAuthAuthReauthsWhileAuthenticating_Object = MibTableColumn
swAuthAuthReauthsWhileAuthenticating = _SwAuthAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 9),
    _SwAuthAuthReauthsWhileAuthenticating_Type()
)
swAuthAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthReauthsWhileAuthenticating.setStatus("current")
_SwAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_SwAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
swAuthAuthEapStartsWhileAuthenticating = _SwAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 10),
    _SwAuthAuthEapStartsWhileAuthenticating_Type()
)
swAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_SwAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_SwAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
swAuthAuthEapLogoffWhileAuthenticating = _SwAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 11),
    _SwAuthAuthEapLogoffWhileAuthenticating_Type()
)
swAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_SwAuthAuthReauthsWhileAuthenticated_Type = Counter32
_SwAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
swAuthAuthReauthsWhileAuthenticated = _SwAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 12),
    _SwAuthAuthReauthsWhileAuthenticated_Type()
)
swAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthReauthsWhileAuthenticated.setStatus("current")
_SwAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_SwAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
swAuthAuthEapStartsWhileAuthenticated = _SwAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 13),
    _SwAuthAuthEapStartsWhileAuthenticated_Type()
)
swAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_SwAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_SwAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
swAuthAuthEapLogoffWhileAuthenticated = _SwAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 14),
    _SwAuthAuthEapLogoffWhileAuthenticated_Type()
)
swAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_SwAuthBackendResponses_Type = Counter32
_SwAuthBackendResponses_Object = MibTableColumn
swAuthBackendResponses = _SwAuthBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 15),
    _SwAuthBackendResponses_Type()
)
swAuthBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendResponses.setStatus("current")
_SwAuthBackendAccessChallenges_Type = Counter32
_SwAuthBackendAccessChallenges_Object = MibTableColumn
swAuthBackendAccessChallenges = _SwAuthBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 16),
    _SwAuthBackendAccessChallenges_Type()
)
swAuthBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAccessChallenges.setStatus("current")
_SwAuthBackendOtherRequestsToSupplicant_Type = Counter32
_SwAuthBackendOtherRequestsToSupplicant_Object = MibTableColumn
swAuthBackendOtherRequestsToSupplicant = _SwAuthBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 17),
    _SwAuthBackendOtherRequestsToSupplicant_Type()
)
swAuthBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendOtherRequestsToSupplicant.setStatus("current")
_SwAuthBackendNonNakResponsesFromSupplicant_Type = Counter32
_SwAuthBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
swAuthBackendNonNakResponsesFromSupplicant = _SwAuthBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 18),
    _SwAuthBackendNonNakResponsesFromSupplicant_Type()
)
swAuthBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendNonNakResponsesFromSupplicant.setStatus("current")
_SwAuthBackendAuthSuccesses_Type = Counter32
_SwAuthBackendAuthSuccesses_Object = MibTableColumn
swAuthBackendAuthSuccesses = _SwAuthBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 19),
    _SwAuthBackendAuthSuccesses_Type()
)
swAuthBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAuthSuccesses.setStatus("current")
_SwAuthBackendAuthFails_Type = Counter32
_SwAuthBackendAuthFails_Object = MibTableColumn
swAuthBackendAuthFails = _SwAuthBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 20),
    _SwAuthBackendAuthFails_Type()
)
swAuthBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAuthFails.setStatus("current")
_SwMacAuthSessionStatsTable_Object = MibTable
swMacAuthSessionStatsTable = _SwMacAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4)
)
if mibBuilder.loadTexts:
    swMacAuthSessionStatsTable.setStatus("current")
_SwMacAuthSessionStatsEntry_Object = MibTableRow
swMacAuthSessionStatsEntry = _SwMacAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1)
)
swMacAuthSessionStatsEntry.setIndexNames(
    (0, "AUTH-MIB", "swAuthSessionStatsPaeMacAddr"),
    (0, "AUTH-MIB", "swAuthSessionStatsPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthSessionStatsEntry.setStatus("current")
_SwAuthSessionStatsPaeMacAddr_Type = MacAddress
_SwAuthSessionStatsPaeMacAddr_Object = MibTableColumn
swAuthSessionStatsPaeMacAddr = _SwAuthSessionStatsPaeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 1),
    _SwAuthSessionStatsPaeMacAddr_Type()
)
swAuthSessionStatsPaeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthSessionStatsPaeMacAddr.setStatus("current")
_SwAuthSessionStatsPaePortNumber_Type = InterfaceIndex
_SwAuthSessionStatsPaePortNumber_Object = MibTableColumn
swAuthSessionStatsPaePortNumber = _SwAuthSessionStatsPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 2),
    _SwAuthSessionStatsPaePortNumber_Type()
)
swAuthSessionStatsPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthSessionStatsPaePortNumber.setStatus("current")
_SwAuthSessionOctetsRx_Type = Counter64
_SwAuthSessionOctetsRx_Object = MibTableColumn
swAuthSessionOctetsRx = _SwAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 3),
    _SwAuthSessionOctetsRx_Type()
)
swAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionOctetsRx.setStatus("current")
_SwAuthSessionOctetsTx_Type = Counter64
_SwAuthSessionOctetsTx_Object = MibTableColumn
swAuthSessionOctetsTx = _SwAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 4),
    _SwAuthSessionOctetsTx_Type()
)
swAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionOctetsTx.setStatus("current")
_SwAuthSessionFramesRx_Type = Counter32
_SwAuthSessionFramesRx_Object = MibTableColumn
swAuthSessionFramesRx = _SwAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 5),
    _SwAuthSessionFramesRx_Type()
)
swAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionFramesRx.setStatus("current")
_SwAuthSessionFramesTx_Type = Counter32
_SwAuthSessionFramesTx_Object = MibTableColumn
swAuthSessionFramesTx = _SwAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 6),
    _SwAuthSessionFramesTx_Type()
)
swAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionFramesTx.setStatus("current")
_SwAuthSessionId_Type = SnmpAdminString
_SwAuthSessionId_Object = MibTableColumn
swAuthSessionId = _SwAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 7),
    _SwAuthSessionId_Type()
)
swAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionId.setStatus("current")


class _SwAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type swAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("remoteAuthServer", 1))
    )


_SwAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_SwAuthSessionAuthenticMethod_Object = MibTableColumn
swAuthSessionAuthenticMethod = _SwAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 8),
    _SwAuthSessionAuthenticMethod_Type()
)
swAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionAuthenticMethod.setStatus("current")
_SwAuthSessionTime_Type = TimeTicks
_SwAuthSessionTime_Object = MibTableColumn
swAuthSessionTime = _SwAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 9),
    _SwAuthSessionTime_Type()
)
swAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionTime.setStatus("current")


class _SwAuthSessionTerminateCause_Type(Integer32):
    """Custom type swAuthSessionTerminateCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 5),
          ("notTerminatedYet", 999),
          ("portAdminDisabled", 7),
          ("portFailure", 2),
          ("portReInit", 6),
          ("reauthFailed", 4),
          ("supplicantLogoff", 1),
          ("supplicantRestart", 3))
    )


_SwAuthSessionTerminateCause_Type.__name__ = "Integer32"
_SwAuthSessionTerminateCause_Object = MibTableColumn
swAuthSessionTerminateCause = _SwAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 10),
    _SwAuthSessionTerminateCause_Type()
)
swAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionTerminateCause.setStatus("current")
_SwAuthSessionUserName_Type = SnmpAdminString
_SwAuthSessionUserName_Object = MibTableColumn
swAuthSessionUserName = _SwAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 11),
    _SwAuthSessionUserName_Type()
)
swAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionUserName.setStatus("current")
_SwRadiusCommand_ObjectIdentity = ObjectIdentity
swRadiusCommand = _SwRadiusCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 7)
)
_SwRadiusForceDownPortNumber_Type = Unsigned32
_SwRadiusForceDownPortNumber_Object = MibScalar
swRadiusForceDownPortNumber = _SwRadiusForceDownPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 7, 1),
    _SwRadiusForceDownPortNumber_Type()
)
swRadiusForceDownPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusForceDownPortNumber.setStatus("current")
_SwRadiusForceDownMacAddr_Type = MacAddress
_SwRadiusForceDownMacAddr_Object = MibScalar
swRadiusForceDownMacAddr = _SwRadiusForceDownMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 7, 2),
    _SwRadiusForceDownMacAddr_Type()
)
swRadiusForceDownMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusForceDownMacAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUTH-MIB",
    **{"swAuthCtrl": swAuthCtrl,
       "swAuthenCtrl": swAuthenCtrl,
       "authProtocol": authProtocol,
       "swAuthMode": swAuthMode,
       "swRadiusCtrl": swRadiusCtrl,
       "swRadiusDeadTime": swRadiusDeadTime,
       "swRadiusTimeout": swRadiusTimeout,
       "swRadiusRetransmitAttempts": swRadiusRetransmitAttempts,
       "swRadiusServerTable": swRadiusServerTable,
       "swRadiusServerEntry": swRadiusServerEntry,
       "swRadiusServerIndex": swRadiusServerIndex,
       "swRadiusServerIpAddr": swRadiusServerIpAddr,
       "swRadiusServerKey": swRadiusServerKey,
       "swRadiusAuthPortNumber": swRadiusAuthPortNumber,
       "swRadiusAcctPortNumber": swRadiusAcctPortNumber,
       "swRadiusServerStatus": swRadiusServerStatus,
       "swRadiusAuthInfo": swRadiusAuthInfo,
       "swRadiusAuthClientIdentifier": swRadiusAuthClientIdentifier,
       "swRadiusAuthClientInvalidServerAddresses": swRadiusAuthClientInvalidServerAddresses,
       "swRadiusAuthServerTable": swRadiusAuthServerTable,
       "swRadiusAuthServerEntry": swRadiusAuthServerEntry,
       "swRadiusAuthServerIndex": swRadiusAuthServerIndex,
       "swRadiusAuthServerAddress": swRadiusAuthServerAddress,
       "swRadiusAuthClientServerPortNumber": swRadiusAuthClientServerPortNumber,
       "swRadiusAuthClientRoundTripTime": swRadiusAuthClientRoundTripTime,
       "swRadiusAuthClientAccessRequests": swRadiusAuthClientAccessRequests,
       "swRadiusAuthClientAccessRetransmissions": swRadiusAuthClientAccessRetransmissions,
       "swRadiusAuthClientAccessAccepts": swRadiusAuthClientAccessAccepts,
       "swRadiusAuthClientAccessRejects": swRadiusAuthClientAccessRejects,
       "swRadiusAuthClientAccessChallenges": swRadiusAuthClientAccessChallenges,
       "swRadiusAuthClientMalformedAccessResponses": swRadiusAuthClientMalformedAccessResponses,
       "swRadiusAuthClientBadAuthenticators": swRadiusAuthClientBadAuthenticators,
       "swRadiusAuthClientPendingRequests": swRadiusAuthClientPendingRequests,
       "swRadiusAuthClientTimeouts": swRadiusAuthClientTimeouts,
       "swRadiusAuthClientUnknownTypes": swRadiusAuthClientUnknownTypes,
       "swRadiusAuthClientPacketsDropped": swRadiusAuthClientPacketsDropped,
       "swRadiusAccountingCtrl": swRadiusAccountingCtrl,
       "swRadiusAcctUpdateInterval": swRadiusAcctUpdateInterval,
       "swRadiusAcctSuppressNullUserName": swRadiusAcctSuppressNullUserName,
       "swRadiusAcctServiceTable": swRadiusAcctServiceTable,
       "swRadiusAcctServiceEntry": swRadiusAcctServiceEntry,
       "swRadiusAcctServiceIndex": swRadiusAcctServiceIndex,
       "swRadiusAcctServiceMethod": swRadiusAcctServiceMethod,
       "swRadiusAcctServiceMode": swRadiusAcctServiceMode,
       "swRadiusAccountingInfo": swRadiusAccountingInfo,
       "swRadiusAcctClientIdentifier": swRadiusAcctClientIdentifier,
       "swRadiusAcctClientInvalidServerAddresses": swRadiusAcctClientInvalidServerAddresses,
       "swRadiusAcctServerTable": swRadiusAcctServerTable,
       "swRadiusAcctServerEntry": swRadiusAcctServerEntry,
       "swRadiusAcctServerIndex": swRadiusAcctServerIndex,
       "swRadiusAcctServerAddress": swRadiusAcctServerAddress,
       "swRadiusAcctClientServerPortNumber": swRadiusAcctClientServerPortNumber,
       "swRadiusAcctClientRoundTripTime": swRadiusAcctClientRoundTripTime,
       "swRadiusAcctClientRequests": swRadiusAcctClientRequests,
       "swRadiusAcctClientRetransmissions": swRadiusAcctClientRetransmissions,
       "swRadiusAcctClientResponses": swRadiusAcctClientResponses,
       "swRadiusAcctClientMalformedResponses": swRadiusAcctClientMalformedResponses,
       "swRadiusAcctClientBadAuthenticators": swRadiusAcctClientBadAuthenticators,
       "swRadiusAcctClientPendingRequests": swRadiusAcctClientPendingRequests,
       "swRadiusAcctClientTimeouts": swRadiusAcctClientTimeouts,
       "swRadiusAcctClientUnknownTypes": swRadiusAcctClientUnknownTypes,
       "swRadiusAcctClientPacketsDropped": swRadiusAcctClientPacketsDropped,
       "swMacAuthBaseStatsInfo": swMacAuthBaseStatsInfo,
       "swMacAuthStateTable": swMacAuthStateTable,
       "swMacAuthStateEntry": swMacAuthStateEntry,
       "swPaeMacAddr": swPaeMacAddr,
       "swPaePortNumber": swPaePortNumber,
       "swAuthPaeState": swAuthPaeState,
       "swAuthBackendAuthState": swAuthBackendAuthState,
       "swAuthAuthControlledPortStatus": swAuthAuthControlledPortStatus,
       "swMacAuthStatsTable": swMacAuthStatsTable,
       "swMacAuthStatsEntry": swMacAuthStatsEntry,
       "swAuthStatsPaeMacAddr": swAuthStatsPaeMacAddr,
       "swAuthStatsPaePortNumber": swAuthStatsPaePortNumber,
       "swAuthEapolFramesRx": swAuthEapolFramesRx,
       "swAuthEapolFramesTx": swAuthEapolFramesTx,
       "swAuthEapolStartFramesRx": swAuthEapolStartFramesRx,
       "swAuthEapolLogoffFramesRx": swAuthEapolLogoffFramesRx,
       "swAuthEapolRespIdFramesRx": swAuthEapolRespIdFramesRx,
       "swAuthEapolRespFramesRx": swAuthEapolRespFramesRx,
       "swAuthEapolReqIdFramesTx": swAuthEapolReqIdFramesTx,
       "swAuthEapolReqFramesTx": swAuthEapolReqFramesTx,
       "swAuthInvalidEapolFramesRx": swAuthInvalidEapolFramesRx,
       "swAuthEapLengthErrorFramesRx": swAuthEapLengthErrorFramesRx,
       "swAuthLastEapolFrameVersion": swAuthLastEapolFrameVersion,
       "swAuthLastEapolFrameSource": swAuthLastEapolFrameSource,
       "swMacAuthDiagTable": swMacAuthDiagTable,
       "swMacAuthDiagEntry": swMacAuthDiagEntry,
       "swAuthDiagPaeMacAddr": swAuthDiagPaeMacAddr,
       "swAuthDiagPaePortNumber": swAuthDiagPaePortNumber,
       "swAuthEntersConnecting": swAuthEntersConnecting,
       "swAuthEapLogoffsWhileConnecting": swAuthEapLogoffsWhileConnecting,
       "swAuthEntersAuthenticating": swAuthEntersAuthenticating,
       "swAuthAuthSuccessWhileAuthenticating": swAuthAuthSuccessWhileAuthenticating,
       "swAuthAuthTimeoutsWhileAuthenticating": swAuthAuthTimeoutsWhileAuthenticating,
       "swAuthAuthFailWhileAuthenticating": swAuthAuthFailWhileAuthenticating,
       "swAuthAuthReauthsWhileAuthenticating": swAuthAuthReauthsWhileAuthenticating,
       "swAuthAuthEapStartsWhileAuthenticating": swAuthAuthEapStartsWhileAuthenticating,
       "swAuthAuthEapLogoffWhileAuthenticating": swAuthAuthEapLogoffWhileAuthenticating,
       "swAuthAuthReauthsWhileAuthenticated": swAuthAuthReauthsWhileAuthenticated,
       "swAuthAuthEapStartsWhileAuthenticated": swAuthAuthEapStartsWhileAuthenticated,
       "swAuthAuthEapLogoffWhileAuthenticated": swAuthAuthEapLogoffWhileAuthenticated,
       "swAuthBackendResponses": swAuthBackendResponses,
       "swAuthBackendAccessChallenges": swAuthBackendAccessChallenges,
       "swAuthBackendOtherRequestsToSupplicant": swAuthBackendOtherRequestsToSupplicant,
       "swAuthBackendNonNakResponsesFromSupplicant": swAuthBackendNonNakResponsesFromSupplicant,
       "swAuthBackendAuthSuccesses": swAuthBackendAuthSuccesses,
       "swAuthBackendAuthFails": swAuthBackendAuthFails,
       "swMacAuthSessionStatsTable": swMacAuthSessionStatsTable,
       "swMacAuthSessionStatsEntry": swMacAuthSessionStatsEntry,
       "swAuthSessionStatsPaeMacAddr": swAuthSessionStatsPaeMacAddr,
       "swAuthSessionStatsPaePortNumber": swAuthSessionStatsPaePortNumber,
       "swAuthSessionOctetsRx": swAuthSessionOctetsRx,
       "swAuthSessionOctetsTx": swAuthSessionOctetsTx,
       "swAuthSessionFramesRx": swAuthSessionFramesRx,
       "swAuthSessionFramesTx": swAuthSessionFramesTx,
       "swAuthSessionId": swAuthSessionId,
       "swAuthSessionAuthenticMethod": swAuthSessionAuthenticMethod,
       "swAuthSessionTime": swAuthSessionTime,
       "swAuthSessionTerminateCause": swAuthSessionTerminateCause,
       "swAuthSessionUserName": swAuthSessionUserName,
       "swRadiusCommand": swRadiusCommand,
       "swRadiusForceDownPortNumber": swRadiusForceDownPortNumber,
       "swRadiusForceDownMacAddr": swRadiusForceDownMacAddr}
)
