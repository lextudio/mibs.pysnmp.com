# SNMP MIB module (RADIUSCLIENTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIUSCLIENTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:31 2024
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

(radiusClientExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "radiusClientExt")

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


# MODULE-IDENTITY

radiusClientExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApRadiusClientExtInvalidServerAddresses_Type = Counter32
_ApRadiusClientExtInvalidServerAddresses_Object = MibScalar
apRadiusClientExtInvalidServerAddresses = _ApRadiusClientExtInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 2),
    _ApRadiusClientExtInvalidServerAddresses_Type()
)
apRadiusClientExtInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtInvalidServerAddresses.setStatus("current")
_ApRadiusClientExtIdentifier_Type = DisplayString
_ApRadiusClientExtIdentifier_Object = MibScalar
apRadiusClientExtIdentifier = _ApRadiusClientExtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 3),
    _ApRadiusClientExtIdentifier_Type()
)
apRadiusClientExtIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtIdentifier.setStatus("current")


class _ApRadiusClientExtDeadTimer_Type(Integer32):
    """Custom type apRadiusClientExtDeadTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApRadiusClientExtDeadTimer_Type.__name__ = "Integer32"
_ApRadiusClientExtDeadTimer_Object = MibScalar
apRadiusClientExtDeadTimer = _ApRadiusClientExtDeadTimer_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 4),
    _ApRadiusClientExtDeadTimer_Type()
)
apRadiusClientExtDeadTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusClientExtDeadTimer.setStatus("current")


class _ApRadiusClientExtProbe_Type(Integer32):
    """Custom type apRadiusClientExtProbe based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApRadiusClientExtProbe_Type.__name__ = "Integer32"
_ApRadiusClientExtProbe_Object = MibScalar
apRadiusClientExtProbe = _ApRadiusClientExtProbe_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 5),
    _ApRadiusClientExtProbe_Type()
)
apRadiusClientExtProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusClientExtProbe.setStatus("current")


class _ApRadiusClientExtRetransmitLimit_Type(Integer32):
    """Custom type apRadiusClientExtRetransmitLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ApRadiusClientExtRetransmitLimit_Type.__name__ = "Integer32"
_ApRadiusClientExtRetransmitLimit_Object = MibScalar
apRadiusClientExtRetransmitLimit = _ApRadiusClientExtRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 6),
    _ApRadiusClientExtRetransmitLimit_Type()
)
apRadiusClientExtRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusClientExtRetransmitLimit.setStatus("current")


class _ApRadiusClientExtTimeout_Type(Integer32):
    """Custom type apRadiusClientExtTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApRadiusClientExtTimeout_Type.__name__ = "Integer32"
_ApRadiusClientExtTimeout_Object = MibScalar
apRadiusClientExtTimeout = _ApRadiusClientExtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 7),
    _ApRadiusClientExtTimeout_Type()
)
apRadiusClientExtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusClientExtTimeout.setStatus("current")


class _ApRadiusClientExtSourceIpAddress_Type(IpAddress):
    """Custom type apRadiusClientExtSourceIpAddress based on IpAddress"""
    defaultValue = 10


_ApRadiusClientExtSourceIpAddress_Object = MibScalar
apRadiusClientExtSourceIpAddress = _ApRadiusClientExtSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 8),
    _ApRadiusClientExtSourceIpAddress_Type()
)
apRadiusClientExtSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadiusClientExtSourceIpAddress.setStatus("current")
_ApRadiusClientExtServerTable_Object = MibTable
apRadiusClientExtServerTable = _ApRadiusClientExtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9)
)
if mibBuilder.loadTexts:
    apRadiusClientExtServerTable.setStatus("current")
_ApRadiusClientExtServerEntry_Object = MibTableRow
apRadiusClientExtServerEntry = _ApRadiusClientExtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1)
)
apRadiusClientExtServerEntry.setIndexNames(
    (0, "RADIUSCLIENTEXT-MIB", "apRadiusClientExtAddress"),
)
if mibBuilder.loadTexts:
    apRadiusClientExtServerEntry.setStatus("current")
_ApRadiusClientExtAddress_Type = IpAddress
_ApRadiusClientExtAddress_Object = MibTableColumn
apRadiusClientExtAddress = _ApRadiusClientExtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 1),
    _ApRadiusClientExtAddress_Type()
)
apRadiusClientExtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAddress.setStatus("current")
_ApRadiusClientExtRoundTripTime_Type = TimeTicks
_ApRadiusClientExtRoundTripTime_Object = MibTableColumn
apRadiusClientExtRoundTripTime = _ApRadiusClientExtRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 2),
    _ApRadiusClientExtRoundTripTime_Type()
)
apRadiusClientExtRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtRoundTripTime.setStatus("current")
_ApRadiusClientExtAccessRequests_Type = Counter32
_ApRadiusClientExtAccessRequests_Object = MibTableColumn
apRadiusClientExtAccessRequests = _ApRadiusClientExtAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 3),
    _ApRadiusClientExtAccessRequests_Type()
)
apRadiusClientExtAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccessRequests.setStatus("current")
_ApRadiusClientExtAccessRetransmissions_Type = Counter32
_ApRadiusClientExtAccessRetransmissions_Object = MibTableColumn
apRadiusClientExtAccessRetransmissions = _ApRadiusClientExtAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 4),
    _ApRadiusClientExtAccessRetransmissions_Type()
)
apRadiusClientExtAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccessRetransmissions.setStatus("current")
_ApRadiusClientExtAccessAccepts_Type = Counter32
_ApRadiusClientExtAccessAccepts_Object = MibTableColumn
apRadiusClientExtAccessAccepts = _ApRadiusClientExtAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 5),
    _ApRadiusClientExtAccessAccepts_Type()
)
apRadiusClientExtAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccessAccepts.setStatus("current")
_ApRadiusClientExtAccessRejects_Type = Counter32
_ApRadiusClientExtAccessRejects_Object = MibTableColumn
apRadiusClientExtAccessRejects = _ApRadiusClientExtAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 6),
    _ApRadiusClientExtAccessRejects_Type()
)
apRadiusClientExtAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccessRejects.setStatus("current")
_ApRadiusClientExtAccessChallenges_Type = Counter32
_ApRadiusClientExtAccessChallenges_Object = MibTableColumn
apRadiusClientExtAccessChallenges = _ApRadiusClientExtAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 7),
    _ApRadiusClientExtAccessChallenges_Type()
)
apRadiusClientExtAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccessChallenges.setStatus("current")
_ApRadiusClientExtMalformedAccessResponses_Type = Counter32
_ApRadiusClientExtMalformedAccessResponses_Object = MibTableColumn
apRadiusClientExtMalformedAccessResponses = _ApRadiusClientExtMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 8),
    _ApRadiusClientExtMalformedAccessResponses_Type()
)
apRadiusClientExtMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtMalformedAccessResponses.setStatus("current")
_ApRadiusClientExtAuthenticationBadAuthenticators_Type = Counter32
_ApRadiusClientExtAuthenticationBadAuthenticators_Object = MibTableColumn
apRadiusClientExtAuthenticationBadAuthenticators = _ApRadiusClientExtAuthenticationBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 9),
    _ApRadiusClientExtAuthenticationBadAuthenticators_Type()
)
apRadiusClientExtAuthenticationBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAuthenticationBadAuthenticators.setStatus("current")
_ApRadiusClientExtAuthenticationPendingRequests_Type = Counter32
_ApRadiusClientExtAuthenticationPendingRequests_Object = MibTableColumn
apRadiusClientExtAuthenticationPendingRequests = _ApRadiusClientExtAuthenticationPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 10),
    _ApRadiusClientExtAuthenticationPendingRequests_Type()
)
apRadiusClientExtAuthenticationPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAuthenticationPendingRequests.setStatus("current")
_ApRadiusClientExtAuthenticationTimeouts_Type = Counter32
_ApRadiusClientExtAuthenticationTimeouts_Object = MibTableColumn
apRadiusClientExtAuthenticationTimeouts = _ApRadiusClientExtAuthenticationTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 11),
    _ApRadiusClientExtAuthenticationTimeouts_Type()
)
apRadiusClientExtAuthenticationTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAuthenticationTimeouts.setStatus("current")
_ApRadiusClientExtAccountingRequests_Type = Counter32
_ApRadiusClientExtAccountingRequests_Object = MibTableColumn
apRadiusClientExtAccountingRequests = _ApRadiusClientExtAccountingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 12),
    _ApRadiusClientExtAccountingRequests_Type()
)
apRadiusClientExtAccountingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccountingRequests.setStatus("current")
_ApRadiusClientExtAccountingRetransmissions_Type = Counter32
_ApRadiusClientExtAccountingRetransmissions_Object = MibTableColumn
apRadiusClientExtAccountingRetransmissions = _ApRadiusClientExtAccountingRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 13),
    _ApRadiusClientExtAccountingRetransmissions_Type()
)
apRadiusClientExtAccountingRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccountingRetransmissions.setStatus("current")
_ApRadiusClientExtAccountingResponses_Type = Counter32
_ApRadiusClientExtAccountingResponses_Object = MibTableColumn
apRadiusClientExtAccountingResponses = _ApRadiusClientExtAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 14),
    _ApRadiusClientExtAccountingResponses_Type()
)
apRadiusClientExtAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccountingResponses.setStatus("current")
_ApRadiusClientExtMalformedAccountingResponses_Type = Counter32
_ApRadiusClientExtMalformedAccountingResponses_Object = MibTableColumn
apRadiusClientExtMalformedAccountingResponses = _ApRadiusClientExtMalformedAccountingResponses_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 15),
    _ApRadiusClientExtMalformedAccountingResponses_Type()
)
apRadiusClientExtMalformedAccountingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtMalformedAccountingResponses.setStatus("current")
_ApRadiusClientExtAccountingBadAuthenticators_Type = Counter32
_ApRadiusClientExtAccountingBadAuthenticators_Object = MibTableColumn
apRadiusClientExtAccountingBadAuthenticators = _ApRadiusClientExtAccountingBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 16),
    _ApRadiusClientExtAccountingBadAuthenticators_Type()
)
apRadiusClientExtAccountingBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccountingBadAuthenticators.setStatus("current")
_ApRadiusClientExtAccountingPendingRequests_Type = Counter32
_ApRadiusClientExtAccountingPendingRequests_Object = MibTableColumn
apRadiusClientExtAccountingPendingRequests = _ApRadiusClientExtAccountingPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 17),
    _ApRadiusClientExtAccountingPendingRequests_Type()
)
apRadiusClientExtAccountingPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccountingPendingRequests.setStatus("current")
_ApRadiusClientExtAccountingTimeouts_Type = Counter32
_ApRadiusClientExtAccountingTimeouts_Object = MibTableColumn
apRadiusClientExtAccountingTimeouts = _ApRadiusClientExtAccountingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 18),
    _ApRadiusClientExtAccountingTimeouts_Type()
)
apRadiusClientExtAccountingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtAccountingTimeouts.setStatus("current")
_ApRadiusClientExtUnknownType_Type = Counter32
_ApRadiusClientExtUnknownType_Object = MibTableColumn
apRadiusClientExtUnknownType = _ApRadiusClientExtUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 9, 1, 19),
    _ApRadiusClientExtUnknownType_Type()
)
apRadiusClientExtUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadiusClientExtUnknownType.setStatus("current")
_ApRadiusClientExtTable_Object = MibTable
apRadiusClientExtTable = _ApRadiusClientExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10)
)
if mibBuilder.loadTexts:
    apRadiusClientExtTable.setStatus("current")
_ApRadiusClientExtRadServerEntry_Object = MibTableRow
apRadiusClientExtRadServerEntry = _ApRadiusClientExtRadServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10, 1)
)
apRadiusClientExtRadServerEntry.setIndexNames(
    (0, "RADIUSCLIENTEXT-MIB", "apRadiusClientExtRadServerIpAddress"),
)
if mibBuilder.loadTexts:
    apRadiusClientExtRadServerEntry.setStatus("current")
_ApRadiusClientExtRadServerIpAddress_Type = IpAddress
_ApRadiusClientExtRadServerIpAddress_Object = MibTableColumn
apRadiusClientExtRadServerIpAddress = _ApRadiusClientExtRadServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10, 1, 1),
    _ApRadiusClientExtRadServerIpAddress_Type()
)
apRadiusClientExtRadServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apRadiusClientExtRadServerIpAddress.setStatus("current")


class _ApRadiusClientExtRadServerAuthPort_Type(Integer32):
    """Custom type apRadiusClientExtRadServerAuthPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApRadiusClientExtRadServerAuthPort_Type.__name__ = "Integer32"
_ApRadiusClientExtRadServerAuthPort_Object = MibTableColumn
apRadiusClientExtRadServerAuthPort = _ApRadiusClientExtRadServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10, 1, 2),
    _ApRadiusClientExtRadServerAuthPort_Type()
)
apRadiusClientExtRadServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apRadiusClientExtRadServerAuthPort.setStatus("current")


class _ApRadiusClientExtRadServerAcctPort_Type(Integer32):
    """Custom type apRadiusClientExtRadServerAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApRadiusClientExtRadServerAcctPort_Type.__name__ = "Integer32"
_ApRadiusClientExtRadServerAcctPort_Object = MibTableColumn
apRadiusClientExtRadServerAcctPort = _ApRadiusClientExtRadServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10, 1, 3),
    _ApRadiusClientExtRadServerAcctPort_Type()
)
apRadiusClientExtRadServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apRadiusClientExtRadServerAcctPort.setStatus("current")


class _ApRadiusClientExtRadServerSecret_Type(DisplayString):
    """Custom type apRadiusClientExtRadServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApRadiusClientExtRadServerSecret_Type.__name__ = "DisplayString"
_ApRadiusClientExtRadServerSecret_Object = MibTableColumn
apRadiusClientExtRadServerSecret = _ApRadiusClientExtRadServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10, 1, 4),
    _ApRadiusClientExtRadServerSecret_Type()
)
apRadiusClientExtRadServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apRadiusClientExtRadServerSecret.setStatus("current")
_ApRadiusClientExtStatus_Type = RowStatus
_ApRadiusClientExtStatus_Object = MibTableColumn
apRadiusClientExtStatus = _ApRadiusClientExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 12, 10, 1, 5),
    _ApRadiusClientExtStatus_Type()
)
apRadiusClientExtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apRadiusClientExtStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUSCLIENTEXT-MIB",
    **{"radiusClientExtMIB": radiusClientExtMIB,
       "apRadiusClientExtInvalidServerAddresses": apRadiusClientExtInvalidServerAddresses,
       "apRadiusClientExtIdentifier": apRadiusClientExtIdentifier,
       "apRadiusClientExtDeadTimer": apRadiusClientExtDeadTimer,
       "apRadiusClientExtProbe": apRadiusClientExtProbe,
       "apRadiusClientExtRetransmitLimit": apRadiusClientExtRetransmitLimit,
       "apRadiusClientExtTimeout": apRadiusClientExtTimeout,
       "apRadiusClientExtSourceIpAddress": apRadiusClientExtSourceIpAddress,
       "apRadiusClientExtServerTable": apRadiusClientExtServerTable,
       "apRadiusClientExtServerEntry": apRadiusClientExtServerEntry,
       "apRadiusClientExtAddress": apRadiusClientExtAddress,
       "apRadiusClientExtRoundTripTime": apRadiusClientExtRoundTripTime,
       "apRadiusClientExtAccessRequests": apRadiusClientExtAccessRequests,
       "apRadiusClientExtAccessRetransmissions": apRadiusClientExtAccessRetransmissions,
       "apRadiusClientExtAccessAccepts": apRadiusClientExtAccessAccepts,
       "apRadiusClientExtAccessRejects": apRadiusClientExtAccessRejects,
       "apRadiusClientExtAccessChallenges": apRadiusClientExtAccessChallenges,
       "apRadiusClientExtMalformedAccessResponses": apRadiusClientExtMalformedAccessResponses,
       "apRadiusClientExtAuthenticationBadAuthenticators": apRadiusClientExtAuthenticationBadAuthenticators,
       "apRadiusClientExtAuthenticationPendingRequests": apRadiusClientExtAuthenticationPendingRequests,
       "apRadiusClientExtAuthenticationTimeouts": apRadiusClientExtAuthenticationTimeouts,
       "apRadiusClientExtAccountingRequests": apRadiusClientExtAccountingRequests,
       "apRadiusClientExtAccountingRetransmissions": apRadiusClientExtAccountingRetransmissions,
       "apRadiusClientExtAccountingResponses": apRadiusClientExtAccountingResponses,
       "apRadiusClientExtMalformedAccountingResponses": apRadiusClientExtMalformedAccountingResponses,
       "apRadiusClientExtAccountingBadAuthenticators": apRadiusClientExtAccountingBadAuthenticators,
       "apRadiusClientExtAccountingPendingRequests": apRadiusClientExtAccountingPendingRequests,
       "apRadiusClientExtAccountingTimeouts": apRadiusClientExtAccountingTimeouts,
       "apRadiusClientExtUnknownType": apRadiusClientExtUnknownType,
       "apRadiusClientExtTable": apRadiusClientExtTable,
       "apRadiusClientExtRadServerEntry": apRadiusClientExtRadServerEntry,
       "apRadiusClientExtRadServerIpAddress": apRadiusClientExtRadServerIpAddress,
       "apRadiusClientExtRadServerAuthPort": apRadiusClientExtRadServerAuthPort,
       "apRadiusClientExtRadServerAcctPort": apRadiusClientExtRadServerAcctPort,
       "apRadiusClientExtRadServerSecret": apRadiusClientExtRadServerSecret,
       "apRadiusClientExtStatus": apRadiusClientExtStatus}
)
