# SNMP MIB module (ETS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ETS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:58 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiEts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiEtsSystem_ObjectIdentity = ObjectIdentity
aiEtsSystem = _AiEtsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 17, 1)
)


class _AiCardType_Type(Integer32):
    """Custom type aiCardType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headEndCard", 1),
          ("remoteEndCard", 2))
    )


_AiCardType_Type.__name__ = "Integer32"
_AiCardType_Object = MibScalar
aiCardType = _AiCardType_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 1, 1),
    _AiCardType_Type()
)
aiCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCardType.setStatus("current")


class _AiPollRetryLimit_Type(Integer32):
    """Custom type aiPollRetryLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AiPollRetryLimit_Type.__name__ = "Integer32"
_AiPollRetryLimit_Object = MibScalar
aiPollRetryLimit = _AiPollRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 1, 2),
    _AiPollRetryLimit_Type()
)
aiPollRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiPollRetryLimit.setStatus("current")


class _AiHealthMessageInterval_Type(Integer32):
    """Custom type aiHealthMessageInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_AiHealthMessageInterval_Type.__name__ = "Integer32"
_AiHealthMessageInterval_Object = MibScalar
aiHealthMessageInterval = _AiHealthMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 1, 3),
    _AiHealthMessageInterval_Type()
)
aiHealthMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHealthMessageInterval.setStatus("current")


class _AiReconnectionTimeOutPeriod_Type(Integer32):
    """Custom type aiReconnectionTimeOutPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AiReconnectionTimeOutPeriod_Type.__name__ = "Integer32"
_AiReconnectionTimeOutPeriod_Object = MibScalar
aiReconnectionTimeOutPeriod = _AiReconnectionTimeOutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 1, 4),
    _AiReconnectionTimeOutPeriod_Type()
)
aiReconnectionTimeOutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiReconnectionTimeOutPeriod.setStatus("current")
_AiEtsConnectionTable_Object = MibTable
aiEtsConnectionTable = _AiEtsConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 2)
)
if mibBuilder.loadTexts:
    aiEtsConnectionTable.setStatus("current")
_AiEtsConnectionEntry_Object = MibTableRow
aiEtsConnectionEntry = _AiEtsConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 2, 1)
)
aiEtsConnectionEntry.setIndexNames(
    (0, "ETS-MIB", "aiConnectionIndex"),
)
if mibBuilder.loadTexts:
    aiEtsConnectionEntry.setStatus("current")


class _AiConnectionIndex_Type(Integer32):
    """Custom type aiConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AiConnectionIndex_Type.__name__ = "Integer32"
_AiConnectionIndex_Object = MibTableColumn
aiConnectionIndex = _AiConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 2, 1, 1),
    _AiConnectionIndex_Type()
)
aiConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiConnectionIndex.setStatus("current")
_AiIpAddress_Type = IpAddress
_AiIpAddress_Object = MibTableColumn
aiIpAddress = _AiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 2, 1, 2),
    _AiIpAddress_Type()
)
aiIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiIpAddress.setStatus("current")


class _AiConnectionStatus_Type(Integer32):
    """Custom type aiConnectionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activeConnection", 3),
          ("connecting", 2),
          ("noActiveConnection", 1),
          ("suspended", 4))
    )


_AiConnectionStatus_Type.__name__ = "Integer32"
_AiConnectionStatus_Object = MibTableColumn
aiConnectionStatus = _AiConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 2, 1, 3),
    _AiConnectionStatus_Type()
)
aiConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiConnectionStatus.setStatus("current")
_AiE2aLinkTable_Object = MibTable
aiE2aLinkTable = _AiE2aLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3)
)
if mibBuilder.loadTexts:
    aiE2aLinkTable.setStatus("current")
_AiE2aLinkEntry_Object = MibTableRow
aiE2aLinkEntry = _AiE2aLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1)
)
aiE2aLinkEntry.setIndexNames(
    (0, "ETS-MIB", "aiE2aLinkIndex"),
)
if mibBuilder.loadTexts:
    aiE2aLinkEntry.setStatus("current")


class _AiE2aLinkIndex_Type(Integer32):
    """Custom type aiE2aLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AiE2aLinkIndex_Type.__name__ = "Integer32"
_AiE2aLinkIndex_Object = MibTableColumn
aiE2aLinkIndex = _AiE2aLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 1),
    _AiE2aLinkIndex_Type()
)
aiE2aLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiE2aLinkIndex.setStatus("current")


class _AiProvisioned_Type(Integer32):
    """Custom type aiProvisioned based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notProvisioned", 1),
          ("provisioned", 2))
    )


_AiProvisioned_Type.__name__ = "Integer32"
_AiProvisioned_Object = MibTableColumn
aiProvisioned = _AiProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 2),
    _AiProvisioned_Type()
)
aiProvisioned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiProvisioned.setStatus("current")


class _AiLinkStatus_Type(Integer32):
    """Custom type aiLinkStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkOffLine", 2),
          ("linkOnLine", 1))
    )


_AiLinkStatus_Type.__name__ = "Integer32"
_AiLinkStatus_Object = MibTableColumn
aiLinkStatus = _AiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 3),
    _AiLinkStatus_Type()
)
aiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLinkStatus.setStatus("current")


class _AiBaudRate_Type(Integer32):
    """Custom type aiBaudRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e2aBaud1200", 2),
          ("e2aBaud600", 1))
    )


_AiBaudRate_Type.__name__ = "Integer32"
_AiBaudRate_Object = MibTableColumn
aiBaudRate = _AiBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 4),
    _AiBaudRate_Type()
)
aiBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiBaudRate.setStatus("current")


class _AiProtocol_Type(Integer32):
    """Custom type aiProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protocolE2", 1),
          ("protocolE2A", 2))
    )


_AiProtocol_Type.__name__ = "Integer32"
_AiProtocol_Object = MibTableColumn
aiProtocol = _AiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 5),
    _AiProtocol_Type()
)
aiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiProtocol.setStatus("current")


class _AiTxMessages_Type(Integer32):
    """Custom type aiTxMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiTxMessages_Type.__name__ = "Integer32"
_AiTxMessages_Object = MibTableColumn
aiTxMessages = _AiTxMessages_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 6),
    _AiTxMessages_Type()
)
aiTxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTxMessages.setStatus("current")


class _AiTxWords_Type(Integer32):
    """Custom type aiTxWords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiTxWords_Type.__name__ = "Integer32"
_AiTxWords_Object = MibTableColumn
aiTxWords = _AiTxWords_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 7),
    _AiTxWords_Type()
)
aiTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTxWords.setStatus("current")


class _AiTxErrors_Type(Integer32):
    """Custom type aiTxErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiTxErrors_Type.__name__ = "Integer32"
_AiTxErrors_Object = MibTableColumn
aiTxErrors = _AiTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 8),
    _AiTxErrors_Type()
)
aiTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTxErrors.setStatus("current")


class _AiRxMessages_Type(Integer32):
    """Custom type aiRxMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiRxMessages_Type.__name__ = "Integer32"
_AiRxMessages_Object = MibTableColumn
aiRxMessages = _AiRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 9),
    _AiRxMessages_Type()
)
aiRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRxMessages.setStatus("current")


class _AiRxWords_Type(Integer32):
    """Custom type aiRxWords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiRxWords_Type.__name__ = "Integer32"
_AiRxWords_Object = MibTableColumn
aiRxWords = _AiRxWords_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 10),
    _AiRxWords_Type()
)
aiRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRxWords.setStatus("current")


class _AiRxErrors_Type(Integer32):
    """Custom type aiRxErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiRxErrors_Type.__name__ = "Integer32"
_AiRxErrors_Object = MibTableColumn
aiRxErrors = _AiRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 11),
    _AiRxErrors_Type()
)
aiRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRxErrors.setStatus("current")


class _AiRxTimeouts_Type(Integer32):
    """Custom type aiRxTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiRxTimeouts_Type.__name__ = "Integer32"
_AiRxTimeouts_Object = MibTableColumn
aiRxTimeouts = _AiRxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 12),
    _AiRxTimeouts_Type()
)
aiRxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRxTimeouts.setStatus("current")


class _AiFlushes_Type(Integer32):
    """Custom type aiFlushes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiFlushes_Type.__name__ = "Integer32"
_AiFlushes_Object = MibTableColumn
aiFlushes = _AiFlushes_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 3, 1, 13),
    _AiFlushes_Type()
)
aiFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiFlushes.setStatus("current")
_AiE2aRtuTable_Object = MibTable
aiE2aRtuTable = _AiE2aRtuTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4)
)
if mibBuilder.loadTexts:
    aiE2aRtuTable.setStatus("current")
_AiE2aRtuEntry_Object = MibTableRow
aiE2aRtuEntry = _AiE2aRtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1)
)
aiE2aRtuEntry.setIndexNames(
    (0, "ETS-MIB", "aiE2aRtuIndex"),
)
if mibBuilder.loadTexts:
    aiE2aRtuEntry.setStatus("current")


class _AiE2aRtuIndex_Type(Integer32):
    """Custom type aiE2aRtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AiE2aRtuIndex_Type.__name__ = "Integer32"
_AiE2aRtuIndex_Object = MibTableColumn
aiE2aRtuIndex = _AiE2aRtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 1),
    _AiE2aRtuIndex_Type()
)
aiE2aRtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiE2aRtuIndex.setStatus("current")


class _AiE2aLink_Type(Integer32):
    """Custom type aiE2aLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AiE2aLink_Type.__name__ = "Integer32"
_AiE2aLink_Object = MibTableColumn
aiE2aLink = _AiE2aLink_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 2),
    _AiE2aLink_Type()
)
aiE2aLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiE2aLink.setStatus("current")


class _AiRtuAddress_Type(Integer32):
    """Custom type aiRtuAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AiRtuAddress_Type.__name__ = "Integer32"
_AiRtuAddress_Object = MibTableColumn
aiRtuAddress = _AiRtuAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 3),
    _AiRtuAddress_Type()
)
aiRtuAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRtuAddress.setStatus("current")


class _AiRtuType_Type(Integer32):
    """Custom type aiRtuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e2aAprRtu", 2),
          ("e2aDasRtu", 3),
          ("e2aSacRtu", 1))
    )


_AiRtuType_Type.__name__ = "Integer32"
_AiRtuType_Object = MibTableColumn
aiRtuType = _AiRtuType_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 4),
    _AiRtuType_Type()
)
aiRtuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRtuType.setStatus("current")


class _AiCommunicationState_Type(Integer32):
    """Custom type aiCommunicationState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtuOffLine", 1),
          ("rtuOnLine", 2))
    )


_AiCommunicationState_Type.__name__ = "Integer32"
_AiCommunicationState_Object = MibTableColumn
aiCommunicationState = _AiCommunicationState_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 5),
    _AiCommunicationState_Type()
)
aiCommunicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCommunicationState.setStatus("current")


class _AiInitialPoll_Type(Integer32):
    """Custom type aiInitialPoll based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiInitialPoll_Type.__name__ = "Integer32"
_AiInitialPoll_Object = MibTableColumn
aiInitialPoll = _AiInitialPoll_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 6),
    _AiInitialPoll_Type()
)
aiInitialPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInitialPoll.setStatus("current")


class _AiEtsConnectionIndex_Type(Integer32):
    """Custom type aiEtsConnectionIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AiEtsConnectionIndex_Type.__name__ = "Integer32"
_AiEtsConnectionIndex_Object = MibTableColumn
aiEtsConnectionIndex = _AiEtsConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 7),
    _AiEtsConnectionIndex_Type()
)
aiEtsConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiEtsConnectionIndex.setStatus("current")


class _AiE2aRequests_Type(Integer32):
    """Custom type aiE2aRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiE2aRequests_Type.__name__ = "Integer32"
_AiE2aRequests_Object = MibTableColumn
aiE2aRequests = _AiE2aRequests_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 8),
    _AiE2aRequests_Type()
)
aiE2aRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiE2aRequests.setStatus("current")


class _AiE2aResponses_Type(Integer32):
    """Custom type aiE2aResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiE2aResponses_Type.__name__ = "Integer32"
_AiE2aResponses_Object = MibTableColumn
aiE2aResponses = _AiE2aResponses_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 9),
    _AiE2aResponses_Type()
)
aiE2aResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiE2aResponses.setStatus("current")


class _AiPollRequests_Type(Integer32):
    """Custom type aiPollRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiPollRequests_Type.__name__ = "Integer32"
_AiPollRequests_Object = MibTableColumn
aiPollRequests = _AiPollRequests_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 10),
    _AiPollRequests_Type()
)
aiPollRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiPollRequests.setStatus("current")


class _AiPollResponses_Type(Integer32):
    """Custom type aiPollResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiPollResponses_Type.__name__ = "Integer32"
_AiPollResponses_Object = MibTableColumn
aiPollResponses = _AiPollResponses_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 11),
    _AiPollResponses_Type()
)
aiPollResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiPollResponses.setStatus("current")


class _AiLatchingRequests_Type(Integer32):
    """Custom type aiLatchingRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiLatchingRequests_Type.__name__ = "Integer32"
_AiLatchingRequests_Object = MibTableColumn
aiLatchingRequests = _AiLatchingRequests_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 12),
    _AiLatchingRequests_Type()
)
aiLatchingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLatchingRequests.setStatus("current")


class _AiLatchingResponses_Type(Integer32):
    """Custom type aiLatchingResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiLatchingResponses_Type.__name__ = "Integer32"
_AiLatchingResponses_Object = MibTableColumn
aiLatchingResponses = _AiLatchingResponses_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 13),
    _AiLatchingResponses_Type()
)
aiLatchingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLatchingResponses.setStatus("current")


class _AiMomentaryRequests_Type(Integer32):
    """Custom type aiMomentaryRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiMomentaryRequests_Type.__name__ = "Integer32"
_AiMomentaryRequests_Object = MibTableColumn
aiMomentaryRequests = _AiMomentaryRequests_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 14),
    _AiMomentaryRequests_Type()
)
aiMomentaryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMomentaryRequests.setStatus("current")


class _AiMomentaryResponses_Type(Integer32):
    """Custom type aiMomentaryResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiMomentaryResponses_Type.__name__ = "Integer32"
_AiMomentaryResponses_Object = MibTableColumn
aiMomentaryResponses = _AiMomentaryResponses_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 15),
    _AiMomentaryResponses_Type()
)
aiMomentaryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMomentaryResponses.setStatus("current")


class _AiTestRequests_Type(Integer32):
    """Custom type aiTestRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiTestRequests_Type.__name__ = "Integer32"
_AiTestRequests_Object = MibTableColumn
aiTestRequests = _AiTestRequests_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 16),
    _AiTestRequests_Type()
)
aiTestRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTestRequests.setStatus("current")


class _AiTestResponses_Type(Integer32):
    """Custom type aiTestResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiTestResponses_Type.__name__ = "Integer32"
_AiTestResponses_Object = MibTableColumn
aiTestResponses = _AiTestResponses_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 17),
    _AiTestResponses_Type()
)
aiTestResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTestResponses.setStatus("current")


class _AiUnknownRequests_Type(Integer32):
    """Custom type aiUnknownRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiUnknownRequests_Type.__name__ = "Integer32"
_AiUnknownRequests_Object = MibTableColumn
aiUnknownRequests = _AiUnknownRequests_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 18),
    _AiUnknownRequests_Type()
)
aiUnknownRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiUnknownRequests.setStatus("current")


class _AiUnknownResponses_Type(Integer32):
    """Custom type aiUnknownResponses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiUnknownResponses_Type.__name__ = "Integer32"
_AiUnknownResponses_Object = MibTableColumn
aiUnknownResponses = _AiUnknownResponses_Object(
    (1, 3, 6, 1, 4, 1, 539, 17, 4, 1, 19),
    _AiUnknownResponses_Type()
)
aiUnknownResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiUnknownResponses.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETS-MIB",
    **{"aii": aii,
       "aiEts": aiEts,
       "aiEtsSystem": aiEtsSystem,
       "aiCardType": aiCardType,
       "aiPollRetryLimit": aiPollRetryLimit,
       "aiHealthMessageInterval": aiHealthMessageInterval,
       "aiReconnectionTimeOutPeriod": aiReconnectionTimeOutPeriod,
       "aiEtsConnectionTable": aiEtsConnectionTable,
       "aiEtsConnectionEntry": aiEtsConnectionEntry,
       "aiConnectionIndex": aiConnectionIndex,
       "aiIpAddress": aiIpAddress,
       "aiConnectionStatus": aiConnectionStatus,
       "aiE2aLinkTable": aiE2aLinkTable,
       "aiE2aLinkEntry": aiE2aLinkEntry,
       "aiE2aLinkIndex": aiE2aLinkIndex,
       "aiProvisioned": aiProvisioned,
       "aiLinkStatus": aiLinkStatus,
       "aiBaudRate": aiBaudRate,
       "aiProtocol": aiProtocol,
       "aiTxMessages": aiTxMessages,
       "aiTxWords": aiTxWords,
       "aiTxErrors": aiTxErrors,
       "aiRxMessages": aiRxMessages,
       "aiRxWords": aiRxWords,
       "aiRxErrors": aiRxErrors,
       "aiRxTimeouts": aiRxTimeouts,
       "aiFlushes": aiFlushes,
       "aiE2aRtuTable": aiE2aRtuTable,
       "aiE2aRtuEntry": aiE2aRtuEntry,
       "aiE2aRtuIndex": aiE2aRtuIndex,
       "aiE2aLink": aiE2aLink,
       "aiRtuAddress": aiRtuAddress,
       "aiRtuType": aiRtuType,
       "aiCommunicationState": aiCommunicationState,
       "aiInitialPoll": aiInitialPoll,
       "aiEtsConnectionIndex": aiEtsConnectionIndex,
       "aiE2aRequests": aiE2aRequests,
       "aiE2aResponses": aiE2aResponses,
       "aiPollRequests": aiPollRequests,
       "aiPollResponses": aiPollResponses,
       "aiLatchingRequests": aiLatchingRequests,
       "aiLatchingResponses": aiLatchingResponses,
       "aiMomentaryRequests": aiMomentaryRequests,
       "aiMomentaryResponses": aiMomentaryResponses,
       "aiTestRequests": aiTestRequests,
       "aiTestResponses": aiTestResponses,
       "aiUnknownRequests": aiUnknownRequests,
       "aiUnknownResponses": aiUnknownResponses}
)
