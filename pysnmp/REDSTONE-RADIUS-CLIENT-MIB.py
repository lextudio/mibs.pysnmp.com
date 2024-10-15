# SNMP MIB module (REDSTONE-RADIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-RADIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:45 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsRadiusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19)
)
rsRadiusClientMIB.setRevisions(
        ("1999-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsRadiusClientObjects_ObjectIdentity = ObjectIdentity
rsRadiusClientObjects = _RsRadiusClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1)
)
_RsRadiusGeneralClient_ObjectIdentity = ObjectIdentity
rsRadiusGeneralClient = _RsRadiusGeneralClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1)
)
_RsRadiusClientIdentifier_Type = DisplayString
_RsRadiusClientIdentifier_Object = MibScalar
rsRadiusClientIdentifier = _RsRadiusClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1, 1),
    _RsRadiusClientIdentifier_Type()
)
rsRadiusClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusClientIdentifier.setStatus("current")


class _RsRadiusClientAlgorithm_Type(Integer32):
    """Custom type rsRadiusClientAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("roundRobin", 1))
    )


_RsRadiusClientAlgorithm_Type.__name__ = "Integer32"
_RsRadiusClientAlgorithm_Object = MibScalar
rsRadiusClientAlgorithm = _RsRadiusClientAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 1, 2),
    _RsRadiusClientAlgorithm_Type()
)
rsRadiusClientAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsRadiusClientAlgorithm.setStatus("current")
_RsRadiusAuthClient_ObjectIdentity = ObjectIdentity
rsRadiusAuthClient = _RsRadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2)
)
_RsRadiusAuthClientInvalidServerAddresses_Type = Counter32
_RsRadiusAuthClientInvalidServerAddresses_Object = MibScalar
rsRadiusAuthClientInvalidServerAddresses = _RsRadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 1),
    _RsRadiusAuthClientInvalidServerAddresses_Type()
)
rsRadiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientInvalidServerAddresses.setStatus("current")
_RsRadiusAuthClientServerTable_Object = MibTable
rsRadiusAuthClientServerTable = _RsRadiusAuthClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rsRadiusAuthClientServerTable.setStatus("current")
_RsRadiusAuthClientServerEntry_Object = MibTableRow
rsRadiusAuthClientServerEntry = _RsRadiusAuthClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1)
)
rsRadiusAuthClientServerEntry.setIndexNames(
    (0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerAddress"),
)
if mibBuilder.loadTexts:
    rsRadiusAuthClientServerEntry.setStatus("current")
_RsRadiusAuthClientServerAddress_Type = IpAddress
_RsRadiusAuthClientServerAddress_Object = MibTableColumn
rsRadiusAuthClientServerAddress = _RsRadiusAuthClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 1),
    _RsRadiusAuthClientServerAddress_Type()
)
rsRadiusAuthClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRadiusAuthClientServerAddress.setStatus("current")
_RsRadiusAuthClientServerPortNumber_Type = Integer32
_RsRadiusAuthClientServerPortNumber_Object = MibTableColumn
rsRadiusAuthClientServerPortNumber = _RsRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 2),
    _RsRadiusAuthClientServerPortNumber_Type()
)
rsRadiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientServerPortNumber.setStatus("current")
_RsRadiusAuthClientRoundTripTime_Type = TimeTicks
_RsRadiusAuthClientRoundTripTime_Object = MibTableColumn
rsRadiusAuthClientRoundTripTime = _RsRadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 3),
    _RsRadiusAuthClientRoundTripTime_Type()
)
rsRadiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientRoundTripTime.setStatus("current")
_RsRadiusAuthClientAccessRequests_Type = Counter32
_RsRadiusAuthClientAccessRequests_Object = MibTableColumn
rsRadiusAuthClientAccessRequests = _RsRadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 4),
    _RsRadiusAuthClientAccessRequests_Type()
)
rsRadiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientAccessRequests.setStatus("current")
_RsRadiusAuthClientAccessRetransmissions_Type = Counter32
_RsRadiusAuthClientAccessRetransmissions_Object = MibTableColumn
rsRadiusAuthClientAccessRetransmissions = _RsRadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 5),
    _RsRadiusAuthClientAccessRetransmissions_Type()
)
rsRadiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientAccessRetransmissions.setStatus("current")
_RsRadiusAuthClientAccessAccepts_Type = Counter32
_RsRadiusAuthClientAccessAccepts_Object = MibTableColumn
rsRadiusAuthClientAccessAccepts = _RsRadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 6),
    _RsRadiusAuthClientAccessAccepts_Type()
)
rsRadiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientAccessAccepts.setStatus("current")
_RsRadiusAuthClientAccessRejects_Type = Counter32
_RsRadiusAuthClientAccessRejects_Object = MibTableColumn
rsRadiusAuthClientAccessRejects = _RsRadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 7),
    _RsRadiusAuthClientAccessRejects_Type()
)
rsRadiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientAccessRejects.setStatus("current")
_RsRadiusAuthClientAccessChallenges_Type = Counter32
_RsRadiusAuthClientAccessChallenges_Object = MibTableColumn
rsRadiusAuthClientAccessChallenges = _RsRadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 8),
    _RsRadiusAuthClientAccessChallenges_Type()
)
rsRadiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientAccessChallenges.setStatus("current")
_RsRadiusAuthClientMalformedAccessResponses_Type = Counter32
_RsRadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
rsRadiusAuthClientMalformedAccessResponses = _RsRadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 9),
    _RsRadiusAuthClientMalformedAccessResponses_Type()
)
rsRadiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientMalformedAccessResponses.setStatus("current")
_RsRadiusAuthClientBadAuthenticators_Type = Counter32
_RsRadiusAuthClientBadAuthenticators_Object = MibTableColumn
rsRadiusAuthClientBadAuthenticators = _RsRadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 10),
    _RsRadiusAuthClientBadAuthenticators_Type()
)
rsRadiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientBadAuthenticators.setStatus("current")
_RsRadiusAuthClientPendingRequests_Type = Gauge32
_RsRadiusAuthClientPendingRequests_Object = MibTableColumn
rsRadiusAuthClientPendingRequests = _RsRadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 11),
    _RsRadiusAuthClientPendingRequests_Type()
)
rsRadiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientPendingRequests.setStatus("current")
_RsRadiusAuthClientTimeouts_Type = Counter32
_RsRadiusAuthClientTimeouts_Object = MibTableColumn
rsRadiusAuthClientTimeouts = _RsRadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 12),
    _RsRadiusAuthClientTimeouts_Type()
)
rsRadiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientTimeouts.setStatus("current")
_RsRadiusAuthClientUnknownTypes_Type = Counter32
_RsRadiusAuthClientUnknownTypes_Object = MibTableColumn
rsRadiusAuthClientUnknownTypes = _RsRadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 13),
    _RsRadiusAuthClientUnknownTypes_Type()
)
rsRadiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientUnknownTypes.setStatus("current")
_RsRadiusAuthClientPacketsDropped_Type = Counter32
_RsRadiusAuthClientPacketsDropped_Object = MibTableColumn
rsRadiusAuthClientPacketsDropped = _RsRadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 2, 1, 14),
    _RsRadiusAuthClientPacketsDropped_Type()
)
rsRadiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientPacketsDropped.setStatus("current")
_RsRadiusAuthClientCfgServerTable_Object = MibTable
rsRadiusAuthClientCfgServerTable = _RsRadiusAuthClientCfgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgServerTable.setStatus("current")
_RsRadiusAuthClientCfgServerEntry_Object = MibTableRow
rsRadiusAuthClientCfgServerEntry = _RsRadiusAuthClientCfgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1)
)
rsRadiusAuthClientCfgServerEntry.setIndexNames(
    (0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerAddress"),
)
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgServerEntry.setStatus("current")
_RsRadiusAuthClientCfgServerAddress_Type = IpAddress
_RsRadiusAuthClientCfgServerAddress_Object = MibTableColumn
rsRadiusAuthClientCfgServerAddress = _RsRadiusAuthClientCfgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 1),
    _RsRadiusAuthClientCfgServerAddress_Type()
)
rsRadiusAuthClientCfgServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgServerAddress.setStatus("current")


class _RsRadiusAuthClientCfgServerPortNumber_Type(Integer32):
    """Custom type rsRadiusAuthClientCfgServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsRadiusAuthClientCfgServerPortNumber_Type.__name__ = "Integer32"
_RsRadiusAuthClientCfgServerPortNumber_Object = MibTableColumn
rsRadiusAuthClientCfgServerPortNumber = _RsRadiusAuthClientCfgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 2),
    _RsRadiusAuthClientCfgServerPortNumber_Type()
)
rsRadiusAuthClientCfgServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgServerPortNumber.setStatus("current")


class _RsRadiusAuthClientCfgKey_Type(DisplayString):
    """Custom type rsRadiusAuthClientCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsRadiusAuthClientCfgKey_Type.__name__ = "DisplayString"
_RsRadiusAuthClientCfgKey_Object = MibTableColumn
rsRadiusAuthClientCfgKey = _RsRadiusAuthClientCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 3),
    _RsRadiusAuthClientCfgKey_Type()
)
rsRadiusAuthClientCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgKey.setStatus("current")


class _RsRadiusAuthClientCfgTimeoutInterval_Type(Integer32):
    """Custom type rsRadiusAuthClientCfgTimeoutInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_RsRadiusAuthClientCfgTimeoutInterval_Type.__name__ = "Integer32"
_RsRadiusAuthClientCfgTimeoutInterval_Object = MibTableColumn
rsRadiusAuthClientCfgTimeoutInterval = _RsRadiusAuthClientCfgTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 4),
    _RsRadiusAuthClientCfgTimeoutInterval_Type()
)
rsRadiusAuthClientCfgTimeoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgTimeoutInterval.setUnits("seconds")


class _RsRadiusAuthClientCfgRetries_Type(Integer32):
    """Custom type rsRadiusAuthClientCfgRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsRadiusAuthClientCfgRetries_Type.__name__ = "Integer32"
_RsRadiusAuthClientCfgRetries_Object = MibTableColumn
rsRadiusAuthClientCfgRetries = _RsRadiusAuthClientCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 5),
    _RsRadiusAuthClientCfgRetries_Type()
)
rsRadiusAuthClientCfgRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgRetries.setStatus("current")


class _RsRadiusAuthClientCfgMaxPendingRequests_Type(Integer32):
    """Custom type rsRadiusAuthClientCfgMaxPendingRequests based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_RsRadiusAuthClientCfgMaxPendingRequests_Type.__name__ = "Integer32"
_RsRadiusAuthClientCfgMaxPendingRequests_Object = MibTableColumn
rsRadiusAuthClientCfgMaxPendingRequests = _RsRadiusAuthClientCfgMaxPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 6),
    _RsRadiusAuthClientCfgMaxPendingRequests_Type()
)
rsRadiusAuthClientCfgMaxPendingRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgMaxPendingRequests.setStatus("current")
_RsRadiusAuthClientCfgRowStatus_Type = RowStatus
_RsRadiusAuthClientCfgRowStatus_Object = MibTableColumn
rsRadiusAuthClientCfgRowStatus = _RsRadiusAuthClientCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 7),
    _RsRadiusAuthClientCfgRowStatus_Type()
)
rsRadiusAuthClientCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgRowStatus.setStatus("current")


class _RsRadiusAuthClientCfgPrecedence_Type(Integer32):
    """Custom type rsRadiusAuthClientCfgPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsRadiusAuthClientCfgPrecedence_Type.__name__ = "Integer32"
_RsRadiusAuthClientCfgPrecedence_Object = MibTableColumn
rsRadiusAuthClientCfgPrecedence = _RsRadiusAuthClientCfgPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 8),
    _RsRadiusAuthClientCfgPrecedence_Type()
)
rsRadiusAuthClientCfgPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgPrecedence.setStatus("current")


class _RsRadiusAuthClientCfgDeadTime_Type(Integer32):
    """Custom type rsRadiusAuthClientCfgDeadTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RsRadiusAuthClientCfgDeadTime_Type.__name__ = "Integer32"
_RsRadiusAuthClientCfgDeadTime_Object = MibTableColumn
rsRadiusAuthClientCfgDeadTime = _RsRadiusAuthClientCfgDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 2, 3, 1, 9),
    _RsRadiusAuthClientCfgDeadTime_Type()
)
rsRadiusAuthClientCfgDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    rsRadiusAuthClientCfgDeadTime.setUnits("minutes")
_RsRadiusAcctClient_ObjectIdentity = ObjectIdentity
rsRadiusAcctClient = _RsRadiusAcctClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3)
)
_RsRadiusAcctClientInvalidServerAddresses_Type = Counter32
_RsRadiusAcctClientInvalidServerAddresses_Object = MibScalar
rsRadiusAcctClientInvalidServerAddresses = _RsRadiusAcctClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 1),
    _RsRadiusAcctClientInvalidServerAddresses_Type()
)
rsRadiusAcctClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientInvalidServerAddresses.setStatus("current")
_RsRadiusAcctClientServerTable_Object = MibTable
rsRadiusAcctClientServerTable = _RsRadiusAcctClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rsRadiusAcctClientServerTable.setStatus("current")
_RsRadiusAcctClientServerEntry_Object = MibTableRow
rsRadiusAcctClientServerEntry = _RsRadiusAcctClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1)
)
rsRadiusAcctClientServerEntry.setIndexNames(
    (0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerAddress"),
)
if mibBuilder.loadTexts:
    rsRadiusAcctClientServerEntry.setStatus("current")
_RsRadiusAcctClientServerAddress_Type = IpAddress
_RsRadiusAcctClientServerAddress_Object = MibTableColumn
rsRadiusAcctClientServerAddress = _RsRadiusAcctClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 1),
    _RsRadiusAcctClientServerAddress_Type()
)
rsRadiusAcctClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRadiusAcctClientServerAddress.setStatus("current")
_RsRadiusAcctClientServerPortNumber_Type = Integer32
_RsRadiusAcctClientServerPortNumber_Object = MibTableColumn
rsRadiusAcctClientServerPortNumber = _RsRadiusAcctClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 2),
    _RsRadiusAcctClientServerPortNumber_Type()
)
rsRadiusAcctClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientServerPortNumber.setStatus("current")
_RsRadiusAcctClientRoundTripTime_Type = TimeTicks
_RsRadiusAcctClientRoundTripTime_Object = MibTableColumn
rsRadiusAcctClientRoundTripTime = _RsRadiusAcctClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 3),
    _RsRadiusAcctClientRoundTripTime_Type()
)
rsRadiusAcctClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientRoundTripTime.setStatus("current")
_RsRadiusAcctClientRequests_Type = Counter32
_RsRadiusAcctClientRequests_Object = MibTableColumn
rsRadiusAcctClientRequests = _RsRadiusAcctClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 4),
    _RsRadiusAcctClientRequests_Type()
)
rsRadiusAcctClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientRequests.setStatus("current")
_RsRadiusAcctClientRetransmissions_Type = Counter32
_RsRadiusAcctClientRetransmissions_Object = MibTableColumn
rsRadiusAcctClientRetransmissions = _RsRadiusAcctClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 5),
    _RsRadiusAcctClientRetransmissions_Type()
)
rsRadiusAcctClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientRetransmissions.setStatus("current")
_RsRadiusAcctClientResponses_Type = Counter32
_RsRadiusAcctClientResponses_Object = MibTableColumn
rsRadiusAcctClientResponses = _RsRadiusAcctClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 6),
    _RsRadiusAcctClientResponses_Type()
)
rsRadiusAcctClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientResponses.setStatus("current")
_RsRadiusAcctClientMalformedResponses_Type = Counter32
_RsRadiusAcctClientMalformedResponses_Object = MibTableColumn
rsRadiusAcctClientMalformedResponses = _RsRadiusAcctClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 7),
    _RsRadiusAcctClientMalformedResponses_Type()
)
rsRadiusAcctClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientMalformedResponses.setStatus("current")
_RsRadiusAcctClientBadAuthenticators_Type = Counter32
_RsRadiusAcctClientBadAuthenticators_Object = MibTableColumn
rsRadiusAcctClientBadAuthenticators = _RsRadiusAcctClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 8),
    _RsRadiusAcctClientBadAuthenticators_Type()
)
rsRadiusAcctClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientBadAuthenticators.setStatus("current")
_RsRadiusAcctClientPendingRequests_Type = Gauge32
_RsRadiusAcctClientPendingRequests_Object = MibTableColumn
rsRadiusAcctClientPendingRequests = _RsRadiusAcctClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 9),
    _RsRadiusAcctClientPendingRequests_Type()
)
rsRadiusAcctClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientPendingRequests.setStatus("current")
_RsRadiusAcctClientTimeouts_Type = Counter32
_RsRadiusAcctClientTimeouts_Object = MibTableColumn
rsRadiusAcctClientTimeouts = _RsRadiusAcctClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 10),
    _RsRadiusAcctClientTimeouts_Type()
)
rsRadiusAcctClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientTimeouts.setStatus("current")
_RsRadiusAcctClientUnknownTypes_Type = Counter32
_RsRadiusAcctClientUnknownTypes_Object = MibTableColumn
rsRadiusAcctClientUnknownTypes = _RsRadiusAcctClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 11),
    _RsRadiusAcctClientUnknownTypes_Type()
)
rsRadiusAcctClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientUnknownTypes.setStatus("current")
_RsRadiusAcctClientPacketsDropped_Type = Counter32
_RsRadiusAcctClientPacketsDropped_Object = MibTableColumn
rsRadiusAcctClientPacketsDropped = _RsRadiusAcctClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 2, 1, 12),
    _RsRadiusAcctClientPacketsDropped_Type()
)
rsRadiusAcctClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientPacketsDropped.setStatus("current")
_RsRadiusAcctClientCfgServerTable_Object = MibTable
rsRadiusAcctClientCfgServerTable = _RsRadiusAcctClientCfgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgServerTable.setStatus("current")
_RsRadiusAcctClientCfgServerEntry_Object = MibTableRow
rsRadiusAcctClientCfgServerEntry = _RsRadiusAcctClientCfgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1)
)
rsRadiusAcctClientCfgServerEntry.setIndexNames(
    (0, "REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerAddress"),
)
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgServerEntry.setStatus("current")
_RsRadiusAcctClientCfgServerAddress_Type = IpAddress
_RsRadiusAcctClientCfgServerAddress_Object = MibTableColumn
rsRadiusAcctClientCfgServerAddress = _RsRadiusAcctClientCfgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 1),
    _RsRadiusAcctClientCfgServerAddress_Type()
)
rsRadiusAcctClientCfgServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgServerAddress.setStatus("current")


class _RsRadiusAcctClientCfgServerPortNumber_Type(Integer32):
    """Custom type rsRadiusAcctClientCfgServerPortNumber based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsRadiusAcctClientCfgServerPortNumber_Type.__name__ = "Integer32"
_RsRadiusAcctClientCfgServerPortNumber_Object = MibTableColumn
rsRadiusAcctClientCfgServerPortNumber = _RsRadiusAcctClientCfgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 2),
    _RsRadiusAcctClientCfgServerPortNumber_Type()
)
rsRadiusAcctClientCfgServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgServerPortNumber.setStatus("current")


class _RsRadiusAcctClientCfgKey_Type(DisplayString):
    """Custom type rsRadiusAcctClientCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RsRadiusAcctClientCfgKey_Type.__name__ = "DisplayString"
_RsRadiusAcctClientCfgKey_Object = MibTableColumn
rsRadiusAcctClientCfgKey = _RsRadiusAcctClientCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 3),
    _RsRadiusAcctClientCfgKey_Type()
)
rsRadiusAcctClientCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgKey.setStatus("current")


class _RsRadiusAcctClientCfgTimeoutInterval_Type(Integer32):
    """Custom type rsRadiusAcctClientCfgTimeoutInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_RsRadiusAcctClientCfgTimeoutInterval_Type.__name__ = "Integer32"
_RsRadiusAcctClientCfgTimeoutInterval_Object = MibTableColumn
rsRadiusAcctClientCfgTimeoutInterval = _RsRadiusAcctClientCfgTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 4),
    _RsRadiusAcctClientCfgTimeoutInterval_Type()
)
rsRadiusAcctClientCfgTimeoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgTimeoutInterval.setUnits("seconds")


class _RsRadiusAcctClientCfgRetries_Type(Integer32):
    """Custom type rsRadiusAcctClientCfgRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RsRadiusAcctClientCfgRetries_Type.__name__ = "Integer32"
_RsRadiusAcctClientCfgRetries_Object = MibTableColumn
rsRadiusAcctClientCfgRetries = _RsRadiusAcctClientCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 5),
    _RsRadiusAcctClientCfgRetries_Type()
)
rsRadiusAcctClientCfgRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgRetries.setStatus("current")


class _RsRadiusAcctClientCfgMaxPendingRequests_Type(Integer32):
    """Custom type rsRadiusAcctClientCfgMaxPendingRequests based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_RsRadiusAcctClientCfgMaxPendingRequests_Type.__name__ = "Integer32"
_RsRadiusAcctClientCfgMaxPendingRequests_Object = MibTableColumn
rsRadiusAcctClientCfgMaxPendingRequests = _RsRadiusAcctClientCfgMaxPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 6),
    _RsRadiusAcctClientCfgMaxPendingRequests_Type()
)
rsRadiusAcctClientCfgMaxPendingRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgMaxPendingRequests.setStatus("current")
_RsRadiusAcctClientCfgRowStatus_Type = RowStatus
_RsRadiusAcctClientCfgRowStatus_Object = MibTableColumn
rsRadiusAcctClientCfgRowStatus = _RsRadiusAcctClientCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 7),
    _RsRadiusAcctClientCfgRowStatus_Type()
)
rsRadiusAcctClientCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgRowStatus.setStatus("current")


class _RsRadiusAcctClientCfgPrecedence_Type(Integer32):
    """Custom type rsRadiusAcctClientCfgPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsRadiusAcctClientCfgPrecedence_Type.__name__ = "Integer32"
_RsRadiusAcctClientCfgPrecedence_Object = MibTableColumn
rsRadiusAcctClientCfgPrecedence = _RsRadiusAcctClientCfgPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 8),
    _RsRadiusAcctClientCfgPrecedence_Type()
)
rsRadiusAcctClientCfgPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgPrecedence.setStatus("current")


class _RsRadiusAcctClientCfgDeadTime_Type(Integer32):
    """Custom type rsRadiusAcctClientCfgDeadTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RsRadiusAcctClientCfgDeadTime_Type.__name__ = "Integer32"
_RsRadiusAcctClientCfgDeadTime_Object = MibTableColumn
rsRadiusAcctClientCfgDeadTime = _RsRadiusAcctClientCfgDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 1, 3, 3, 1, 9),
    _RsRadiusAcctClientCfgDeadTime_Type()
)
rsRadiusAcctClientCfgDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    rsRadiusAcctClientCfgDeadTime.setUnits("minutes")
_RsRadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
rsRadiusClientMIBConformance = _RsRadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2)
)
_RsRadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
rsRadiusClientMIBCompliances = _RsRadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1)
)
_RsRadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
rsRadiusClientMIBGroups = _RsRadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2)
)

# Managed Objects groups

rsRadiusGeneralClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 1)
)
rsRadiusGeneralClientGroup.setObjects(
      *(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusClientIdentifier"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusClientAlgorithm"))
)
if mibBuilder.loadTexts:
    rsRadiusGeneralClientGroup.setStatus("current")

rsRadiusAuthClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 2)
)
rsRadiusAuthClientGroup.setObjects(
      *(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientInvalidServerAddresses"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientServerPortNumber"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientRoundTripTime"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRequests"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRetransmissions"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessAccepts"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessRejects"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientAccessChallenges"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientMalformedAccessResponses"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientBadAuthenticators"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientPendingRequests"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientTimeouts"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientUnknownTypes"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientPacketsDropped"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgServerPortNumber"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgKey"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgTimeoutInterval"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgRetries"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgMaxPendingRequests"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgRowStatus"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgPrecedence"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAuthClientCfgDeadTime"))
)
if mibBuilder.loadTexts:
    rsRadiusAuthClientGroup.setStatus("current")

rsRadiusAcctClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 2, 3)
)
rsRadiusAcctClientGroup.setObjects(
      *(("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientInvalidServerAddresses"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientServerPortNumber"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRoundTripTime"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRequests"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientRetransmissions"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientResponses"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientMalformedResponses"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientBadAuthenticators"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientPendingRequests"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientTimeouts"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientUnknownTypes"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientPacketsDropped"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgServerPortNumber"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgKey"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgTimeoutInterval"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgRetries"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgMaxPendingRequests"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgRowStatus"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgPrecedence"),
        ("REDSTONE-RADIUS-CLIENT-MIB", "rsRadiusAcctClientCfgDeadTime"))
)
if mibBuilder.loadTexts:
    rsRadiusAcctClientGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsRadiusAuthClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsRadiusAuthClientCompliance.setStatus(
        "current"
    )

rsRadiusAcctClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 19, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rsRadiusAcctClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-RADIUS-CLIENT-MIB",
    **{"rsRadiusClientMIB": rsRadiusClientMIB,
       "rsRadiusClientObjects": rsRadiusClientObjects,
       "rsRadiusGeneralClient": rsRadiusGeneralClient,
       "rsRadiusClientIdentifier": rsRadiusClientIdentifier,
       "rsRadiusClientAlgorithm": rsRadiusClientAlgorithm,
       "rsRadiusAuthClient": rsRadiusAuthClient,
       "rsRadiusAuthClientInvalidServerAddresses": rsRadiusAuthClientInvalidServerAddresses,
       "rsRadiusAuthClientServerTable": rsRadiusAuthClientServerTable,
       "rsRadiusAuthClientServerEntry": rsRadiusAuthClientServerEntry,
       "rsRadiusAuthClientServerAddress": rsRadiusAuthClientServerAddress,
       "rsRadiusAuthClientServerPortNumber": rsRadiusAuthClientServerPortNumber,
       "rsRadiusAuthClientRoundTripTime": rsRadiusAuthClientRoundTripTime,
       "rsRadiusAuthClientAccessRequests": rsRadiusAuthClientAccessRequests,
       "rsRadiusAuthClientAccessRetransmissions": rsRadiusAuthClientAccessRetransmissions,
       "rsRadiusAuthClientAccessAccepts": rsRadiusAuthClientAccessAccepts,
       "rsRadiusAuthClientAccessRejects": rsRadiusAuthClientAccessRejects,
       "rsRadiusAuthClientAccessChallenges": rsRadiusAuthClientAccessChallenges,
       "rsRadiusAuthClientMalformedAccessResponses": rsRadiusAuthClientMalformedAccessResponses,
       "rsRadiusAuthClientBadAuthenticators": rsRadiusAuthClientBadAuthenticators,
       "rsRadiusAuthClientPendingRequests": rsRadiusAuthClientPendingRequests,
       "rsRadiusAuthClientTimeouts": rsRadiusAuthClientTimeouts,
       "rsRadiusAuthClientUnknownTypes": rsRadiusAuthClientUnknownTypes,
       "rsRadiusAuthClientPacketsDropped": rsRadiusAuthClientPacketsDropped,
       "rsRadiusAuthClientCfgServerTable": rsRadiusAuthClientCfgServerTable,
       "rsRadiusAuthClientCfgServerEntry": rsRadiusAuthClientCfgServerEntry,
       "rsRadiusAuthClientCfgServerAddress": rsRadiusAuthClientCfgServerAddress,
       "rsRadiusAuthClientCfgServerPortNumber": rsRadiusAuthClientCfgServerPortNumber,
       "rsRadiusAuthClientCfgKey": rsRadiusAuthClientCfgKey,
       "rsRadiusAuthClientCfgTimeoutInterval": rsRadiusAuthClientCfgTimeoutInterval,
       "rsRadiusAuthClientCfgRetries": rsRadiusAuthClientCfgRetries,
       "rsRadiusAuthClientCfgMaxPendingRequests": rsRadiusAuthClientCfgMaxPendingRequests,
       "rsRadiusAuthClientCfgRowStatus": rsRadiusAuthClientCfgRowStatus,
       "rsRadiusAuthClientCfgPrecedence": rsRadiusAuthClientCfgPrecedence,
       "rsRadiusAuthClientCfgDeadTime": rsRadiusAuthClientCfgDeadTime,
       "rsRadiusAcctClient": rsRadiusAcctClient,
       "rsRadiusAcctClientInvalidServerAddresses": rsRadiusAcctClientInvalidServerAddresses,
       "rsRadiusAcctClientServerTable": rsRadiusAcctClientServerTable,
       "rsRadiusAcctClientServerEntry": rsRadiusAcctClientServerEntry,
       "rsRadiusAcctClientServerAddress": rsRadiusAcctClientServerAddress,
       "rsRadiusAcctClientServerPortNumber": rsRadiusAcctClientServerPortNumber,
       "rsRadiusAcctClientRoundTripTime": rsRadiusAcctClientRoundTripTime,
       "rsRadiusAcctClientRequests": rsRadiusAcctClientRequests,
       "rsRadiusAcctClientRetransmissions": rsRadiusAcctClientRetransmissions,
       "rsRadiusAcctClientResponses": rsRadiusAcctClientResponses,
       "rsRadiusAcctClientMalformedResponses": rsRadiusAcctClientMalformedResponses,
       "rsRadiusAcctClientBadAuthenticators": rsRadiusAcctClientBadAuthenticators,
       "rsRadiusAcctClientPendingRequests": rsRadiusAcctClientPendingRequests,
       "rsRadiusAcctClientTimeouts": rsRadiusAcctClientTimeouts,
       "rsRadiusAcctClientUnknownTypes": rsRadiusAcctClientUnknownTypes,
       "rsRadiusAcctClientPacketsDropped": rsRadiusAcctClientPacketsDropped,
       "rsRadiusAcctClientCfgServerTable": rsRadiusAcctClientCfgServerTable,
       "rsRadiusAcctClientCfgServerEntry": rsRadiusAcctClientCfgServerEntry,
       "rsRadiusAcctClientCfgServerAddress": rsRadiusAcctClientCfgServerAddress,
       "rsRadiusAcctClientCfgServerPortNumber": rsRadiusAcctClientCfgServerPortNumber,
       "rsRadiusAcctClientCfgKey": rsRadiusAcctClientCfgKey,
       "rsRadiusAcctClientCfgTimeoutInterval": rsRadiusAcctClientCfgTimeoutInterval,
       "rsRadiusAcctClientCfgRetries": rsRadiusAcctClientCfgRetries,
       "rsRadiusAcctClientCfgMaxPendingRequests": rsRadiusAcctClientCfgMaxPendingRequests,
       "rsRadiusAcctClientCfgRowStatus": rsRadiusAcctClientCfgRowStatus,
       "rsRadiusAcctClientCfgPrecedence": rsRadiusAcctClientCfgPrecedence,
       "rsRadiusAcctClientCfgDeadTime": rsRadiusAcctClientCfgDeadTime,
       "rsRadiusClientMIBConformance": rsRadiusClientMIBConformance,
       "rsRadiusClientMIBCompliances": rsRadiusClientMIBCompliances,
       "rsRadiusAuthClientCompliance": rsRadiusAuthClientCompliance,
       "rsRadiusAcctClientCompliance": rsRadiusAcctClientCompliance,
       "rsRadiusClientMIBGroups": rsRadiusClientMIBGroups,
       "rsRadiusGeneralClientGroup": rsRadiusGeneralClientGroup,
       "rsRadiusAuthClientGroup": rsRadiusAuthClientGroup,
       "rsRadiusAcctClientGroup": rsRadiusAcctClientGroup}
)
