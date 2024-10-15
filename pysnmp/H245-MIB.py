# SNMP MIB module (H245-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H245-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:37 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(MmH323EndpointType,
 MmTAddressTag,
 mmH245Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmH323EndpointType",
    "MmTAddressTag",
    "mmH245Root")

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
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h245 = ModuleIdentity(
    (0, 0, 8, 341, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H245Configuration_ObjectIdentity = ObjectIdentity
h245Configuration = _H245Configuration_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 1)
)
_H245ConfigurationTable_Object = MibTable
h245ConfigurationTable = _H245ConfigurationTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h245ConfigurationTable.setStatus("current")
_H245ConfigurationTableEntry_Object = MibTableRow
h245ConfigurationTableEntry = _H245ConfigurationTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1)
)
h245ConfigurationTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h245ConfigurationTableEntry.setStatus("current")
_H245ConfigT101Timer_Type = Integer32
_H245ConfigT101Timer_Object = MibTableColumn
h245ConfigT101Timer = _H245ConfigT101Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 1),
    _H245ConfigT101Timer_Type()
)
h245ConfigT101Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT101Timer.setStatus("current")
_H245ConfigT102Timer_Type = Integer32
_H245ConfigT102Timer_Object = MibTableColumn
h245ConfigT102Timer = _H245ConfigT102Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 2),
    _H245ConfigT102Timer_Type()
)
h245ConfigT102Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT102Timer.setStatus("current")
_H245ConfigT103Timer_Type = Integer32
_H245ConfigT103Timer_Object = MibTableColumn
h245ConfigT103Timer = _H245ConfigT103Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 3),
    _H245ConfigT103Timer_Type()
)
h245ConfigT103Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT103Timer.setStatus("current")
_H245ConfigT104Timer_Type = Integer32
_H245ConfigT104Timer_Object = MibTableColumn
h245ConfigT104Timer = _H245ConfigT104Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 4),
    _H245ConfigT104Timer_Type()
)
h245ConfigT104Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT104Timer.setStatus("current")
_H245ConfigT105Timer_Type = Integer32
_H245ConfigT105Timer_Object = MibTableColumn
h245ConfigT105Timer = _H245ConfigT105Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 5),
    _H245ConfigT105Timer_Type()
)
h245ConfigT105Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT105Timer.setStatus("current")
_H245ConfigT106Timer_Type = Integer32
_H245ConfigT106Timer_Object = MibTableColumn
h245ConfigT106Timer = _H245ConfigT106Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 6),
    _H245ConfigT106Timer_Type()
)
h245ConfigT106Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT106Timer.setStatus("current")
_H245ConfigT107Timer_Type = Integer32
_H245ConfigT107Timer_Object = MibTableColumn
h245ConfigT107Timer = _H245ConfigT107Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 7),
    _H245ConfigT107Timer_Type()
)
h245ConfigT107Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT107Timer.setStatus("current")
_H245ConfigT108Timer_Type = Integer32
_H245ConfigT108Timer_Object = MibTableColumn
h245ConfigT108Timer = _H245ConfigT108Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 8),
    _H245ConfigT108Timer_Type()
)
h245ConfigT108Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT108Timer.setStatus("current")
_H245ConfigT109Timer_Type = Integer32
_H245ConfigT109Timer_Object = MibTableColumn
h245ConfigT109Timer = _H245ConfigT109Timer_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 9),
    _H245ConfigT109Timer_Type()
)
h245ConfigT109Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigT109Timer.setStatus("current")
_H245ConfigN100Counter_Type = Integer32
_H245ConfigN100Counter_Object = MibTableColumn
h245ConfigN100Counter = _H245ConfigN100Counter_Object(
    (0, 0, 8, 341, 1, 3, 1, 1, 1, 1, 10),
    _H245ConfigN100Counter_Type()
)
h245ConfigN100Counter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h245ConfigN100Counter.setStatus("current")
_H245ControlChannel_ObjectIdentity = ObjectIdentity
h245ControlChannel = _H245ControlChannel_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 2)
)
_H245ControlChannelStatsTable_Object = MibTable
h245ControlChannelStatsTable = _H245ControlChannelStatsTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h245ControlChannelStatsTable.setStatus("current")
_H245ControlChannelStatsTableEntry_Object = MibTableRow
h245ControlChannelStatsTableEntry = _H245ControlChannelStatsTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1)
)
h245ControlChannelStatsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h245ControlChannelStatsTableEntry.setStatus("current")
_H245ControlChannelNumberOfListenPorts_Type = Integer32
_H245ControlChannelNumberOfListenPorts_Object = MibTableColumn
h245ControlChannelNumberOfListenPorts = _H245ControlChannelNumberOfListenPorts_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 1),
    _H245ControlChannelNumberOfListenPorts_Type()
)
h245ControlChannelNumberOfListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelNumberOfListenPorts.setStatus("current")
_H245ControlChannelMaxConnections_Type = Integer32
_H245ControlChannelMaxConnections_Object = MibTableColumn
h245ControlChannelMaxConnections = _H245ControlChannelMaxConnections_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 2),
    _H245ControlChannelMaxConnections_Type()
)
h245ControlChannelMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMaxConnections.setStatus("current")
_H245ControlChannelNumberOfListenFails_Type = Integer32
_H245ControlChannelNumberOfListenFails_Object = MibTableColumn
h245ControlChannelNumberOfListenFails = _H245ControlChannelNumberOfListenFails_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 3),
    _H245ControlChannelNumberOfListenFails_Type()
)
h245ControlChannelNumberOfListenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelNumberOfListenFails.setStatus("current")
_H245ControlChannelNumberOfActiveConnections_Type = Integer32
_H245ControlChannelNumberOfActiveConnections_Object = MibTableColumn
h245ControlChannelNumberOfActiveConnections = _H245ControlChannelNumberOfActiveConnections_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 4),
    _H245ControlChannelNumberOfActiveConnections_Type()
)
h245ControlChannelNumberOfActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelNumberOfActiveConnections.setStatus("current")
_H245ControlChannelMasterSlaveMaxRetries_Type = Integer32
_H245ControlChannelMasterSlaveMaxRetries_Object = MibTableColumn
h245ControlChannelMasterSlaveMaxRetries = _H245ControlChannelMasterSlaveMaxRetries_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 5),
    _H245ControlChannelMasterSlaveMaxRetries_Type()
)
h245ControlChannelMasterSlaveMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveMaxRetries.setStatus("current")
_H245ControlChannelConnectionAttemptsFail_Type = Counter32
_H245ControlChannelConnectionAttemptsFail_Object = MibTableColumn
h245ControlChannelConnectionAttemptsFail = _H245ControlChannelConnectionAttemptsFail_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 6),
    _H245ControlChannelConnectionAttemptsFail_Type()
)
h245ControlChannelConnectionAttemptsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelConnectionAttemptsFail.setStatus("current")
_H245ControlChanneMasterSlavelDeterminations_Type = Counter32
_H245ControlChanneMasterSlavelDeterminations_Object = MibTableColumn
h245ControlChanneMasterSlavelDeterminations = _H245ControlChanneMasterSlavelDeterminations_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 7),
    _H245ControlChanneMasterSlavelDeterminations_Type()
)
h245ControlChanneMasterSlavelDeterminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChanneMasterSlavelDeterminations.setStatus("current")
_H245ControlChannelMasterSlaveAcks_Type = Counter32
_H245ControlChannelMasterSlaveAcks_Object = MibTableColumn
h245ControlChannelMasterSlaveAcks = _H245ControlChannelMasterSlaveAcks_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 8),
    _H245ControlChannelMasterSlaveAcks_Type()
)
h245ControlChannelMasterSlaveAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveAcks.setStatus("current")
_H245ControlChannelMasterSlaveRejects_Type = Counter32
_H245ControlChannelMasterSlaveRejects_Object = MibTableColumn
h245ControlChannelMasterSlaveRejects = _H245ControlChannelMasterSlaveRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 9),
    _H245ControlChannelMasterSlaveRejects_Type()
)
h245ControlChannelMasterSlaveRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveRejects.setStatus("current")
_H245ControlChannelMasterSlaveT106Rejects_Type = Counter32
_H245ControlChannelMasterSlaveT106Rejects_Object = MibTableColumn
h245ControlChannelMasterSlaveT106Rejects = _H245ControlChannelMasterSlaveT106Rejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 10),
    _H245ControlChannelMasterSlaveT106Rejects_Type()
)
h245ControlChannelMasterSlaveT106Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveT106Rejects.setStatus("current")
_H245ControlChannelMasterSlaveMSDRejects_Type = Counter32
_H245ControlChannelMasterSlaveMSDRejects_Object = MibTableColumn
h245ControlChannelMasterSlaveMSDRejects = _H245ControlChannelMasterSlaveMSDRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 11),
    _H245ControlChannelMasterSlaveMSDRejects_Type()
)
h245ControlChannelMasterSlaveMSDRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveMSDRejects.setStatus("current")
_H245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects_Type = Counter32
_H245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects_Object = MibTableColumn
h245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects = _H245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 12),
    _H245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects_Type()
)
h245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects.setStatus("current")
_H245ControlChannelMasterSlaveMaxCounterRejects_Type = Counter32
_H245ControlChannelMasterSlaveMaxCounterRejects_Object = MibTableColumn
h245ControlChannelMasterSlaveMaxCounterRejects = _H245ControlChannelMasterSlaveMaxCounterRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 13),
    _H245ControlChannelMasterSlaveMaxCounterRejects_Type()
)
h245ControlChannelMasterSlaveMaxCounterRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveMaxCounterRejects.setStatus("current")
_H245ControlChannelMasterSlaveReleases_Type = Counter32
_H245ControlChannelMasterSlaveReleases_Object = MibTableColumn
h245ControlChannelMasterSlaveReleases = _H245ControlChannelMasterSlaveReleases_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 14),
    _H245ControlChannelMasterSlaveReleases_Type()
)
h245ControlChannelMasterSlaveReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveReleases.setStatus("current")
_H245ControlChannelNumberOfTunnels_Type = Integer32
_H245ControlChannelNumberOfTunnels_Object = MibTableColumn
h245ControlChannelNumberOfTunnels = _H245ControlChannelNumberOfTunnels_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 1, 1, 15),
    _H245ControlChannelNumberOfTunnels_Type()
)
h245ControlChannelNumberOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelNumberOfTunnels.setStatus("current")
_H245ControlChannelMasterSlaveTable_Object = MibTable
h245ControlChannelMasterSlaveTable = _H245ControlChannelMasterSlaveTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveTable.setStatus("current")
_H245ControlChannelMasterSlaveTableEntry_Object = MibTableRow
h245ControlChannelMasterSlaveTableEntry = _H245ControlChannelMasterSlaveTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1)
)
h245ControlChannelMasterSlaveTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245ControlChannelSrcAddressTag"),
    (0, "H245-MIB", "h245ControlChannelSrcTransporTAddress"),
    (0, "H245-MIB", "h245ControlChannelDesTAddressTag"),
    (0, "H245-MIB", "h245ControlChannelDestTransporTAddress"),
)
if mibBuilder.loadTexts:
    h245ControlChannelMasterSlaveTableEntry.setStatus("current")
_H245ControlChannelSrcAddressTag_Type = MmTAddressTag
_H245ControlChannelSrcAddressTag_Object = MibTableColumn
h245ControlChannelSrcAddressTag = _H245ControlChannelSrcAddressTag_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 1),
    _H245ControlChannelSrcAddressTag_Type()
)
h245ControlChannelSrcAddressTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245ControlChannelSrcAddressTag.setStatus("current")
_H245ControlChannelSrcTransporTAddress_Type = TAddress
_H245ControlChannelSrcTransporTAddress_Object = MibTableColumn
h245ControlChannelSrcTransporTAddress = _H245ControlChannelSrcTransporTAddress_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 2),
    _H245ControlChannelSrcTransporTAddress_Type()
)
h245ControlChannelSrcTransporTAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245ControlChannelSrcTransporTAddress.setStatus("current")
_H245ControlChannelDesTAddressTag_Type = MmTAddressTag
_H245ControlChannelDesTAddressTag_Object = MibTableColumn
h245ControlChannelDesTAddressTag = _H245ControlChannelDesTAddressTag_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 3),
    _H245ControlChannelDesTAddressTag_Type()
)
h245ControlChannelDesTAddressTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245ControlChannelDesTAddressTag.setStatus("current")
_H245ControlChannelDestTransporTAddress_Type = TAddress
_H245ControlChannelDestTransporTAddress_Object = MibTableColumn
h245ControlChannelDestTransporTAddress = _H245ControlChannelDestTransporTAddress_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 4),
    _H245ControlChannelDestTransporTAddress_Type()
)
h245ControlChannelDestTransporTAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245ControlChannelDestTransporTAddress.setStatus("current")
_H245ControlChannelIndex_Type = Integer32
_H245ControlChannelIndex_Object = MibTableColumn
h245ControlChannelIndex = _H245ControlChannelIndex_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 5),
    _H245ControlChannelIndex_Type()
)
h245ControlChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelIndex.setStatus("current")


class _H245ControlChannelMSDState_Type(Integer32):
    """Custom type h245ControlChannelMSDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 3),
          ("incomingWaitingResponse", 2),
          ("master", 4),
          ("outgoingWaitingResponse", 1),
          ("slave", 5))
    )


_H245ControlChannelMSDState_Type.__name__ = "Integer32"
_H245ControlChannelMSDState_Object = MibTableColumn
h245ControlChannelMSDState = _H245ControlChannelMSDState_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 6),
    _H245ControlChannelMSDState_Type()
)
h245ControlChannelMSDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelMSDState.setStatus("current")
_H245ControlChannelTerminalType_Type = MmH323EndpointType
_H245ControlChannelTerminalType_Object = MibTableColumn
h245ControlChannelTerminalType = _H245ControlChannelTerminalType_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 7),
    _H245ControlChannelTerminalType_Type()
)
h245ControlChannelTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelTerminalType.setStatus("current")
_H245ControlChannelNumberOfMSDRetries_Type = Integer32
_H245ControlChannelNumberOfMSDRetries_Object = MibTableColumn
h245ControlChannelNumberOfMSDRetries = _H245ControlChannelNumberOfMSDRetries_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 8),
    _H245ControlChannelNumberOfMSDRetries_Type()
)
h245ControlChannelNumberOfMSDRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelNumberOfMSDRetries.setStatus("current")
_H245ControlChannelIsTunneling_Type = TruthValue
_H245ControlChannelIsTunneling_Object = MibTableColumn
h245ControlChannelIsTunneling = _H245ControlChannelIsTunneling_Object(
    (0, 0, 8, 341, 1, 3, 1, 2, 2, 1, 9),
    _H245ControlChannelIsTunneling_Type()
)
h245ControlChannelIsTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ControlChannelIsTunneling.setStatus("current")
_H245CapExchange_ObjectIdentity = ObjectIdentity
h245CapExchange = _H245CapExchange_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 3)
)
_H245CapExchangeStatsTable_Object = MibTable
h245CapExchangeStatsTable = _H245CapExchangeStatsTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h245CapExchangeStatsTable.setStatus("current")
_H245CapExchangeStatsTableEntry_Object = MibTableRow
h245CapExchangeStatsTableEntry = _H245CapExchangeStatsTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1)
)
h245CapExchangeStatsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h245CapExchangeStatsTableEntry.setStatus("current")
_H245CapExchangeSets_Type = Counter32
_H245CapExchangeSets_Object = MibTableColumn
h245CapExchangeSets = _H245CapExchangeSets_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 1),
    _H245CapExchangeSets_Type()
)
h245CapExchangeSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeSets.setStatus("current")
_H245CapExchangeAcks_Type = Counter32
_H245CapExchangeAcks_Object = MibTableColumn
h245CapExchangeAcks = _H245CapExchangeAcks_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 2),
    _H245CapExchangeAcks_Type()
)
h245CapExchangeAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeAcks.setStatus("current")
_H245CapExchangeRejects_Type = Counter32
_H245CapExchangeRejects_Object = MibTableColumn
h245CapExchangeRejects = _H245CapExchangeRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 3),
    _H245CapExchangeRejects_Type()
)
h245CapExchangeRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeRejects.setStatus("current")
_H245CapExchangeRejectUnspecified_Type = Counter32
_H245CapExchangeRejectUnspecified_Object = MibTableColumn
h245CapExchangeRejectUnspecified = _H245CapExchangeRejectUnspecified_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 4),
    _H245CapExchangeRejectUnspecified_Type()
)
h245CapExchangeRejectUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeRejectUnspecified.setStatus("current")
_H245CapExchangeRejectUndefinedTableEntryUsed_Type = Counter32
_H245CapExchangeRejectUndefinedTableEntryUsed_Object = MibTableColumn
h245CapExchangeRejectUndefinedTableEntryUsed = _H245CapExchangeRejectUndefinedTableEntryUsed_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 5),
    _H245CapExchangeRejectUndefinedTableEntryUsed_Type()
)
h245CapExchangeRejectUndefinedTableEntryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeRejectUndefinedTableEntryUsed.setStatus("current")
_H245CapExchangeRejectDescriptorCapacityExceeded_Type = Counter32
_H245CapExchangeRejectDescriptorCapacityExceeded_Object = MibTableColumn
h245CapExchangeRejectDescriptorCapacityExceeded = _H245CapExchangeRejectDescriptorCapacityExceeded_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 6),
    _H245CapExchangeRejectDescriptorCapacityExceeded_Type()
)
h245CapExchangeRejectDescriptorCapacityExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeRejectDescriptorCapacityExceeded.setStatus("current")
_H245CapExchangeRejectTableEntryCapacityExeeded_Type = Counter32
_H245CapExchangeRejectTableEntryCapacityExeeded_Object = MibTableColumn
h245CapExchangeRejectTableEntryCapacityExeeded = _H245CapExchangeRejectTableEntryCapacityExeeded_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 7),
    _H245CapExchangeRejectTableEntryCapacityExeeded_Type()
)
h245CapExchangeRejectTableEntryCapacityExeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeRejectTableEntryCapacityExeeded.setStatus("current")
_H245CapExchangeReleases_Type = Counter32
_H245CapExchangeReleases_Object = MibTableColumn
h245CapExchangeReleases = _H245CapExchangeReleases_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 1, 1, 8),
    _H245CapExchangeReleases_Type()
)
h245CapExchangeReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeReleases.setStatus("current")
_H245CapExchangeCapabilityTable_Object = MibTable
h245CapExchangeCapabilityTable = _H245CapExchangeCapabilityTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h245CapExchangeCapabilityTable.setStatus("current")
_H245CapExchangeCapabilityTableEntry_Object = MibTableRow
h245CapExchangeCapabilityTableEntry = _H245CapExchangeCapabilityTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1)
)
h245CapExchangeCapabilityTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245ControlChannelIndex"),
    (0, "H245-MIB", "h245CapExchangeDirection"),
)
if mibBuilder.loadTexts:
    h245CapExchangeCapabilityTableEntry.setStatus("current")


class _H245CapExchangeDirection_Type(Integer32):
    """Custom type h245CapExchangeDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_H245CapExchangeDirection_Type.__name__ = "Integer32"
_H245CapExchangeDirection_Object = MibTableColumn
h245CapExchangeDirection = _H245CapExchangeDirection_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 1),
    _H245CapExchangeDirection_Type()
)
h245CapExchangeDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245CapExchangeDirection.setStatus("current")


class _H245CapExchangeState_Type(Integer32):
    """Custom type h245CapExchangeState based on Integer32"""
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
        *(("acked", 2),
          ("reject", 3),
          ("release", 4),
          ("sent", 1))
    )


_H245CapExchangeState_Type.__name__ = "Integer32"
_H245CapExchangeState_Object = MibTableColumn
h245CapExchangeState = _H245CapExchangeState_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 2),
    _H245CapExchangeState_Type()
)
h245CapExchangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeState.setStatus("current")


class _H245CapExchangeProtocolId_Type(OctetString):
    """Custom type h245CapExchangeProtocolId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_H245CapExchangeProtocolId_Type.__name__ = "OctetString"
_H245CapExchangeProtocolId_Object = MibTableColumn
h245CapExchangeProtocolId = _H245CapExchangeProtocolId_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 3),
    _H245CapExchangeProtocolId_Type()
)
h245CapExchangeProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeProtocolId.setStatus("current")


class _H245CapExchangeRejectCause_Type(Integer32):
    """Custom type h245CapExchangeRejectCause based on Integer32"""
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
        *(("descriptorCapacityExceeded", 3),
          ("tableEntryCapacityExceeded", 4),
          ("undefinedTableEntryUsed", 2),
          ("unspecified", 1))
    )


_H245CapExchangeRejectCause_Type.__name__ = "Integer32"
_H245CapExchangeRejectCause_Object = MibTableColumn
h245CapExchangeRejectCause = _H245CapExchangeRejectCause_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 4),
    _H245CapExchangeRejectCause_Type()
)
h245CapExchangeRejectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeRejectCause.setStatus("current")
_H245CapExchangeMultiplexCapability_Type = DisplayString
_H245CapExchangeMultiplexCapability_Object = MibTableColumn
h245CapExchangeMultiplexCapability = _H245CapExchangeMultiplexCapability_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 5),
    _H245CapExchangeMultiplexCapability_Type()
)
h245CapExchangeMultiplexCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeMultiplexCapability.setStatus("current")
_H245CapExchangeCapability_Type = DisplayString
_H245CapExchangeCapability_Object = MibTableColumn
h245CapExchangeCapability = _H245CapExchangeCapability_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 6),
    _H245CapExchangeCapability_Type()
)
h245CapExchangeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeCapability.setStatus("current")
_H245CapExchangeCapabilityDescriptors_Type = DisplayString
_H245CapExchangeCapabilityDescriptors_Object = MibTableColumn
h245CapExchangeCapabilityDescriptors = _H245CapExchangeCapabilityDescriptors_Object(
    (0, 0, 8, 341, 1, 3, 1, 3, 2, 1, 7),
    _H245CapExchangeCapabilityDescriptors_Type()
)
h245CapExchangeCapabilityDescriptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245CapExchangeCapabilityDescriptors.setStatus("current")
_H245LogChannels_ObjectIdentity = ObjectIdentity
h245LogChannels = _H245LogChannels_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 4)
)
_H245LogChannelsChannelTable_Object = MibTable
h245LogChannelsChannelTable = _H245LogChannelsChannelTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h245LogChannelsChannelTable.setStatus("current")
_H245LogChannelsChannelTableEntry_Object = MibTableRow
h245LogChannelsChannelTableEntry = _H245LogChannelsChannelTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1, 1)
)
h245LogChannelsChannelTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245ControlChannelIndex"),
    (0, "H245-MIB", "h245LogChannelsChannelNumber"),
    (0, "H245-MIB", "h245LogChannelsChannelDirection"),
)
if mibBuilder.loadTexts:
    h245LogChannelsChannelTableEntry.setStatus("current")
_H245LogChannelsChannelNumber_Type = Integer32
_H245LogChannelsChannelNumber_Object = MibTableColumn
h245LogChannelsChannelNumber = _H245LogChannelsChannelNumber_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1, 1, 1),
    _H245LogChannelsChannelNumber_Type()
)
h245LogChannelsChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245LogChannelsChannelNumber.setStatus("current")


class _H245LogChannelsChannelDirection_Type(Integer32):
    """Custom type h245LogChannelsChannelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2))
    )


_H245LogChannelsChannelDirection_Type.__name__ = "Integer32"
_H245LogChannelsChannelDirection_Object = MibTableColumn
h245LogChannelsChannelDirection = _H245LogChannelsChannelDirection_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1, 1, 2),
    _H245LogChannelsChannelDirection_Type()
)
h245LogChannelsChannelDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245LogChannelsChannelDirection.setStatus("current")
_H245LogChannelsIndex_Type = Integer32
_H245LogChannelsIndex_Object = MibTableColumn
h245LogChannelsIndex = _H245LogChannelsIndex_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1, 1, 3),
    _H245LogChannelsIndex_Type()
)
h245LogChannelsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsIndex.setStatus("current")


class _H245LogChannelsChannelState_Type(Integer32):
    """Custom type h245LogChannelsChannelState based on Integer32"""
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
        *(("awaitingConfirmation", 4),
          ("awaitingEstablishment", 1),
          ("awaitingRelease", 3),
          ("established", 2))
    )


_H245LogChannelsChannelState_Type.__name__ = "Integer32"
_H245LogChannelsChannelState_Object = MibTableColumn
h245LogChannelsChannelState = _H245LogChannelsChannelState_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1, 1, 4),
    _H245LogChannelsChannelState_Type()
)
h245LogChannelsChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsChannelState.setStatus("current")


class _H245LogChannelsMediaTableType_Type(Integer32):
    """Custom type h245LogChannelsMediaTableType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47)
        )
    )
    namedValues = NamedValues(
        *(("audioNonStandard", 7),
          ("conferenceCapability", 40),
          ("dataNonStandard", 27),
          ("dsm-cc", 29),
          ("dsvdControl", 35),
          ("g711Alaw56k", 9),
          ("g711Alaw64k", 8),
          ("g711Ulaw56k", 11),
          ("g711Ulaw64k", 10),
          ("g722-48k", 14),
          ("g722-56k", 13),
          ("g722-64k", 12),
          ("g7231", 15),
          ("g7231AnnexCCapability", 23),
          ("g728", 16),
          ("g729", 17),
          ("g729AnnexA", 18),
          ("g729AnnexAwAnnexB", 22),
          ("g729wAnnexB", 21),
          ("gsmEnhancedFullRate", 26),
          ("gsmFullRate", 24),
          ("gsmHalfRate", 25),
          ("h222", 45),
          ("h222DataPartitioning", 36),
          ("h223", 46),
          ("h224", 33),
          ("h225", 44),
          ("h233EncryptionCapability", 39),
          ("h235SecurityCapability", 41),
          ("h261VideoCapability", 3),
          ("h262VideoCapability", 4),
          ("h263VideoCapability", 5),
          ("is11172AudioCapability", 19),
          ("is11172VideoCapability", 6),
          ("is13818AudioCapability", 20),
          ("maxPendingReplacementFor", 42),
          ("nlpid", 34),
          ("nonStandard", 1),
          ("t120", 28),
          ("t140", 38),
          ("t30fax", 37),
          ("t434", 32),
          ("t84", 31),
          ("userData", 30),
          ("userInputCapability", 43),
          ("v76", 47),
          ("videoNonStandard", 2))
    )


_H245LogChannelsMediaTableType_Type.__name__ = "Integer32"
_H245LogChannelsMediaTableType_Object = MibTableColumn
h245LogChannelsMediaTableType = _H245LogChannelsMediaTableType_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 1, 1, 5),
    _H245LogChannelsMediaTableType_Type()
)
h245LogChannelsMediaTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsMediaTableType.setStatus("current")
_H245LogChannelsH225Table_Object = MibTable
h245LogChannelsH225Table = _H245LogChannelsH225Table_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h245LogChannelsH225Table.setStatus("current")
_H245LogChannelsH225TableEntry_Object = MibTableRow
h245LogChannelsH225TableEntry = _H245LogChannelsH225TableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1)
)
h245LogChannelsH225TableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245LogChannelsIndex"),
)
if mibBuilder.loadTexts:
    h245LogChannelsH225TableEntry.setStatus("current")
_H245LogChannelsSessionId_Type = Integer32
_H245LogChannelsSessionId_Object = MibTableColumn
h245LogChannelsSessionId = _H245LogChannelsSessionId_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 1),
    _H245LogChannelsSessionId_Type()
)
h245LogChannelsSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsSessionId.setStatus("current")
_H245LogChannelsAssociateSessionId_Type = Integer32
_H245LogChannelsAssociateSessionId_Object = MibTableColumn
h245LogChannelsAssociateSessionId = _H245LogChannelsAssociateSessionId_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 2),
    _H245LogChannelsAssociateSessionId_Type()
)
h245LogChannelsAssociateSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsAssociateSessionId.setStatus("current")
_H245LogChannelsMediaChannel_Type = TAddress
_H245LogChannelsMediaChannel_Object = MibTableColumn
h245LogChannelsMediaChannel = _H245LogChannelsMediaChannel_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 3),
    _H245LogChannelsMediaChannel_Type()
)
h245LogChannelsMediaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsMediaChannel.setStatus("current")
_H245LogChannelsMediaGuaranteedDelivery_Type = TruthValue
_H245LogChannelsMediaGuaranteedDelivery_Object = MibTableColumn
h245LogChannelsMediaGuaranteedDelivery = _H245LogChannelsMediaGuaranteedDelivery_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 4),
    _H245LogChannelsMediaGuaranteedDelivery_Type()
)
h245LogChannelsMediaGuaranteedDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsMediaGuaranteedDelivery.setStatus("current")
_H245LogChannelsMediaControlChannel_Type = TAddress
_H245LogChannelsMediaControlChannel_Object = MibTableColumn
h245LogChannelsMediaControlChannel = _H245LogChannelsMediaControlChannel_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 5),
    _H245LogChannelsMediaControlChannel_Type()
)
h245LogChannelsMediaControlChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsMediaControlChannel.setStatus("current")
_H245LogChannelsMediaControlGuaranteedDelivery_Type = TruthValue
_H245LogChannelsMediaControlGuaranteedDelivery_Object = MibTableColumn
h245LogChannelsMediaControlGuaranteedDelivery = _H245LogChannelsMediaControlGuaranteedDelivery_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 6),
    _H245LogChannelsMediaControlGuaranteedDelivery_Type()
)
h245LogChannelsMediaControlGuaranteedDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsMediaControlGuaranteedDelivery.setStatus("current")
_H245LogChannelsSilenceSuppression_Type = TruthValue
_H245LogChannelsSilenceSuppression_Object = MibTableColumn
h245LogChannelsSilenceSuppression = _H245LogChannelsSilenceSuppression_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 7),
    _H245LogChannelsSilenceSuppression_Type()
)
h245LogChannelsSilenceSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsSilenceSuppression.setStatus("current")


class _H245LogChannelsDestination_Type(OctetString):
    """Custom type h245LogChannelsDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_H245LogChannelsDestination_Type.__name__ = "OctetString"
_H245LogChannelsDestination_Object = MibTableColumn
h245LogChannelsDestination = _H245LogChannelsDestination_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 8),
    _H245LogChannelsDestination_Type()
)
h245LogChannelsDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsDestination.setStatus("current")
_H245LogChannelsDynamicRTPPayloadType_Type = Integer32
_H245LogChannelsDynamicRTPPayloadType_Object = MibTableColumn
h245LogChannelsDynamicRTPPayloadType = _H245LogChannelsDynamicRTPPayloadType_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 9),
    _H245LogChannelsDynamicRTPPayloadType_Type()
)
h245LogChannelsDynamicRTPPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsDynamicRTPPayloadType.setStatus("current")
_H245LogChannelsH261aVideoPacketization_Type = TruthValue
_H245LogChannelsH261aVideoPacketization_Object = MibTableColumn
h245LogChannelsH261aVideoPacketization = _H245LogChannelsH261aVideoPacketization_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 10),
    _H245LogChannelsH261aVideoPacketization_Type()
)
h245LogChannelsH261aVideoPacketization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsH261aVideoPacketization.setStatus("current")


class _H245LogChannelsRTPPayloadDescriptor_Type(OctetString):
    """Custom type h245LogChannelsRTPPayloadDescriptor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H245LogChannelsRTPPayloadDescriptor_Type.__name__ = "OctetString"
_H245LogChannelsRTPPayloadDescriptor_Object = MibTableColumn
h245LogChannelsRTPPayloadDescriptor = _H245LogChannelsRTPPayloadDescriptor_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 11),
    _H245LogChannelsRTPPayloadDescriptor_Type()
)
h245LogChannelsRTPPayloadDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsRTPPayloadDescriptor.setStatus("current")
_H245LogChannelsRTPPayloadType_Type = Integer32
_H245LogChannelsRTPPayloadType_Object = MibTableColumn
h245LogChannelsRTPPayloadType = _H245LogChannelsRTPPayloadType_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 12),
    _H245LogChannelsRTPPayloadType_Type()
)
h245LogChannelsRTPPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsRTPPayloadType.setStatus("current")
_H245LogChannelsTransportCapability_Type = DisplayString
_H245LogChannelsTransportCapability_Object = MibTableColumn
h245LogChannelsTransportCapability = _H245LogChannelsTransportCapability_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 13),
    _H245LogChannelsTransportCapability_Type()
)
h245LogChannelsTransportCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsTransportCapability.setStatus("current")
_H245LogChannelsRedundancyEncoding_Type = DisplayString
_H245LogChannelsRedundancyEncoding_Object = MibTableColumn
h245LogChannelsRedundancyEncoding = _H245LogChannelsRedundancyEncoding_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 14),
    _H245LogChannelsRedundancyEncoding_Type()
)
h245LogChannelsRedundancyEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsRedundancyEncoding.setStatus("current")


class _H245LogChannelsSrcTerminalLabel_Type(OctetString):
    """Custom type h245LogChannelsSrcTerminalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_H245LogChannelsSrcTerminalLabel_Type.__name__ = "OctetString"
_H245LogChannelsSrcTerminalLabel_Object = MibTableColumn
h245LogChannelsSrcTerminalLabel = _H245LogChannelsSrcTerminalLabel_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 2, 1, 15),
    _H245LogChannelsSrcTerminalLabel_Type()
)
h245LogChannelsSrcTerminalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChannelsSrcTerminalLabel.setStatus("current")
_H245LogChannelOpenLogicalChannelTable_Object = MibTable
h245LogChannelOpenLogicalChannelTable = _H245LogChannelOpenLogicalChannelTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    h245LogChannelOpenLogicalChannelTable.setStatus("current")
_H245LogChannelOpenLogicalChannelTableEntry_Object = MibTableRow
h245LogChannelOpenLogicalChannelTableEntry = _H245LogChannelOpenLogicalChannelTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1)
)
h245LogChannelOpenLogicalChannelTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h245LogChannelOpenLogicalChannelTableEntry.setStatus("current")
_H245LogChanOpenLogChanTotalRequests_Type = Counter32
_H245LogChanOpenLogChanTotalRequests_Object = MibTableColumn
h245LogChanOpenLogChanTotalRequests = _H245LogChanOpenLogChanTotalRequests_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 1),
    _H245LogChanOpenLogChanTotalRequests_Type()
)
h245LogChanOpenLogChanTotalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanTotalRequests.setStatus("current")
_H245LogChanOpenLogChanAcks_Type = Counter32
_H245LogChanOpenLogChanAcks_Object = MibTableColumn
h245LogChanOpenLogChanAcks = _H245LogChanOpenLogChanAcks_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 2),
    _H245LogChanOpenLogChanAcks_Type()
)
h245LogChanOpenLogChanAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanAcks.setStatus("current")
_H245LogChanOpenLogChanConfirms_Type = Counter32
_H245LogChanOpenLogChanConfirms_Object = MibTableColumn
h245LogChanOpenLogChanConfirms = _H245LogChanOpenLogChanConfirms_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 3),
    _H245LogChanOpenLogChanConfirms_Type()
)
h245LogChanOpenLogChanConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanConfirms.setStatus("current")
_H245LogChanOpenLogChanRejects_Type = Counter32
_H245LogChanOpenLogChanRejects_Object = MibTableColumn
h245LogChanOpenLogChanRejects = _H245LogChanOpenLogChanRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 4),
    _H245LogChanOpenLogChanRejects_Type()
)
h245LogChanOpenLogChanRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejects.setStatus("current")
_H245LogChanOpenLogChanRejectUnspecified_Type = Counter32
_H245LogChanOpenLogChanRejectUnspecified_Object = MibTableColumn
h245LogChanOpenLogChanRejectUnspecified = _H245LogChanOpenLogChanRejectUnspecified_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 5),
    _H245LogChanOpenLogChanRejectUnspecified_Type()
)
h245LogChanOpenLogChanRejectUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectUnspecified.setStatus("current")
_H245LogChanOpenLogChanRejectUnsuitableReverseParameters_Type = Counter32
_H245LogChanOpenLogChanRejectUnsuitableReverseParameters_Object = MibTableColumn
h245LogChanOpenLogChanRejectUnsuitableReverseParameters = _H245LogChanOpenLogChanRejectUnsuitableReverseParameters_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 6),
    _H245LogChanOpenLogChanRejectUnsuitableReverseParameters_Type()
)
h245LogChanOpenLogChanRejectUnsuitableReverseParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectUnsuitableReverseParameters.setStatus("current")
_H245LogChanOpenLogChanRejectDataTypeNotSupported_Type = Counter32
_H245LogChanOpenLogChanRejectDataTypeNotSupported_Object = MibTableColumn
h245LogChanOpenLogChanRejectDataTypeNotSupported = _H245LogChanOpenLogChanRejectDataTypeNotSupported_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 7),
    _H245LogChanOpenLogChanRejectDataTypeNotSupported_Type()
)
h245LogChanOpenLogChanRejectDataTypeNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectDataTypeNotSupported.setStatus("current")
_H245LogChanOpenLogChanRejectDataTypeNotAvailable_Type = Counter32
_H245LogChanOpenLogChanRejectDataTypeNotAvailable_Object = MibTableColumn
h245LogChanOpenLogChanRejectDataTypeNotAvailable = _H245LogChanOpenLogChanRejectDataTypeNotAvailable_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 8),
    _H245LogChanOpenLogChanRejectDataTypeNotAvailable_Type()
)
h245LogChanOpenLogChanRejectDataTypeNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectDataTypeNotAvailable.setStatus("current")
_H245LogChanOpenLogChanRejectUnknownDataType_Type = Counter32
_H245LogChanOpenLogChanRejectUnknownDataType_Object = MibTableColumn
h245LogChanOpenLogChanRejectUnknownDataType = _H245LogChanOpenLogChanRejectUnknownDataType_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 9),
    _H245LogChanOpenLogChanRejectUnknownDataType_Type()
)
h245LogChanOpenLogChanRejectUnknownDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectUnknownDataType.setStatus("current")
_H245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported_Type = Counter32
_H245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported_Object = MibTableColumn
h245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported = _H245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 10),
    _H245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported_Type()
)
h245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported.setStatus("current")
_H245LogChanOpenLogChanRejectMulticastChannelNotAllowed_Type = Counter32
_H245LogChanOpenLogChanRejectMulticastChannelNotAllowed_Object = MibTableColumn
h245LogChanOpenLogChanRejectMulticastChannelNotAllowed = _H245LogChanOpenLogChanRejectMulticastChannelNotAllowed_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 11),
    _H245LogChanOpenLogChanRejectMulticastChannelNotAllowed_Type()
)
h245LogChanOpenLogChanRejectMulticastChannelNotAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectMulticastChannelNotAllowed.setStatus("current")
_H245LogChanOpenLogChanRejectInsuffientBandwdith_Type = Counter32
_H245LogChanOpenLogChanRejectInsuffientBandwdith_Object = MibTableColumn
h245LogChanOpenLogChanRejectInsuffientBandwdith = _H245LogChanOpenLogChanRejectInsuffientBandwdith_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 12),
    _H245LogChanOpenLogChanRejectInsuffientBandwdith_Type()
)
h245LogChanOpenLogChanRejectInsuffientBandwdith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectInsuffientBandwdith.setStatus("current")
_H245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed_Type = Counter32
_H245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed_Object = MibTableColumn
h245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed = _H245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 13),
    _H245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed_Type()
)
h245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed.setStatus("current")
_H245LogChanOpenLogChanRejectInvalidSessionID_Type = Counter32
_H245LogChanOpenLogChanRejectInvalidSessionID_Object = MibTableColumn
h245LogChanOpenLogChanRejectInvalidSessionID = _H245LogChanOpenLogChanRejectInvalidSessionID_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 14),
    _H245LogChanOpenLogChanRejectInvalidSessionID_Type()
)
h245LogChanOpenLogChanRejectInvalidSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectInvalidSessionID.setStatus("current")
_H245LogChanOpenLogChanRejectMasterSlaveConflict_Type = Counter32
_H245LogChanOpenLogChanRejectMasterSlaveConflict_Object = MibTableColumn
h245LogChanOpenLogChanRejectMasterSlaveConflict = _H245LogChanOpenLogChanRejectMasterSlaveConflict_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 15),
    _H245LogChanOpenLogChanRejectMasterSlaveConflict_Type()
)
h245LogChanOpenLogChanRejectMasterSlaveConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectMasterSlaveConflict.setStatus("current")
_H245LogChanOpenLogChanRejectWaitForCommunicationMode_Type = Counter32
_H245LogChanOpenLogChanRejectWaitForCommunicationMode_Object = MibTableColumn
h245LogChanOpenLogChanRejectWaitForCommunicationMode = _H245LogChanOpenLogChanRejectWaitForCommunicationMode_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 16),
    _H245LogChanOpenLogChanRejectWaitForCommunicationMode_Type()
)
h245LogChanOpenLogChanRejectWaitForCommunicationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectWaitForCommunicationMode.setStatus("current")
_H245LogChanOpenLogChanRejectInvalidDependentChannel_Type = Counter32
_H245LogChanOpenLogChanRejectInvalidDependentChannel_Object = MibTableColumn
h245LogChanOpenLogChanRejectInvalidDependentChannel = _H245LogChanOpenLogChanRejectInvalidDependentChannel_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 17),
    _H245LogChanOpenLogChanRejectInvalidDependentChannel_Type()
)
h245LogChanOpenLogChanRejectInvalidDependentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanOpenLogChanRejectInvalidDependentChannel.setStatus("current")
_H245LogChansOpenLogChanRejectReplacementForRejected_Type = Counter32
_H245LogChansOpenLogChanRejectReplacementForRejected_Object = MibTableColumn
h245LogChansOpenLogChanRejectReplacementForRejected = _H245LogChansOpenLogChanRejectReplacementForRejected_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 3, 1, 18),
    _H245LogChansOpenLogChanRejectReplacementForRejected_Type()
)
h245LogChansOpenLogChanRejectReplacementForRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChansOpenLogChanRejectReplacementForRejected.setStatus("current")
_H245LogChannelCloseLogicalChannelTable_Object = MibTable
h245LogChannelCloseLogicalChannelTable = _H245LogChannelCloseLogicalChannelTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    h245LogChannelCloseLogicalChannelTable.setStatus("current")
_H245LogChannelCloseLogicalChannelTableEntry_Object = MibTableRow
h245LogChannelCloseLogicalChannelTableEntry = _H245LogChannelCloseLogicalChannelTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1)
)
h245LogChannelCloseLogicalChannelTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h245LogChannelCloseLogicalChannelTableEntry.setStatus("current")
_H245LogChanCloseLogChannels_Type = Counter32
_H245LogChanCloseLogChannels_Object = MibTableColumn
h245LogChanCloseLogChannels = _H245LogChanCloseLogChannels_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1, 1),
    _H245LogChanCloseLogChannels_Type()
)
h245LogChanCloseLogChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanCloseLogChannels.setStatus("current")
_H245LogChanCloseLogChanAcks_Type = Counter32
_H245LogChanCloseLogChanAcks_Object = MibTableColumn
h245LogChanCloseLogChanAcks = _H245LogChanCloseLogChanAcks_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1, 2),
    _H245LogChanCloseLogChanAcks_Type()
)
h245LogChanCloseLogChanAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanCloseLogChanAcks.setStatus("current")
_H245LogChanCloseLogChanRequests_Type = Counter32
_H245LogChanCloseLogChanRequests_Object = MibTableColumn
h245LogChanCloseLogChanRequests = _H245LogChanCloseLogChanRequests_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1, 3),
    _H245LogChanCloseLogChanRequests_Type()
)
h245LogChanCloseLogChanRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanCloseLogChanRequests.setStatus("current")
_H245LogChanCloseLogChanRequestsAcks_Type = Counter32
_H245LogChanCloseLogChanRequestsAcks_Object = MibTableColumn
h245LogChanCloseLogChanRequestsAcks = _H245LogChanCloseLogChanRequestsAcks_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1, 4),
    _H245LogChanCloseLogChanRequestsAcks_Type()
)
h245LogChanCloseLogChanRequestsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanCloseLogChanRequestsAcks.setStatus("current")
_H245LogChanCloseLogChanRequestRejects_Type = Counter32
_H245LogChanCloseLogChanRequestRejects_Object = MibTableColumn
h245LogChanCloseLogChanRequestRejects = _H245LogChanCloseLogChanRequestRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1, 5),
    _H245LogChanCloseLogChanRequestRejects_Type()
)
h245LogChanCloseLogChanRequestRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanCloseLogChanRequestRejects.setStatus("current")
_H245LogChanCloseLogChanRequestReleases_Type = Counter32
_H245LogChanCloseLogChanRequestReleases_Object = MibTableColumn
h245LogChanCloseLogChanRequestReleases = _H245LogChanCloseLogChanRequestReleases_Object(
    (0, 0, 8, 341, 1, 3, 1, 4, 4, 1, 6),
    _H245LogChanCloseLogChanRequestReleases_Type()
)
h245LogChanCloseLogChanRequestReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245LogChanCloseLogChanRequestReleases.setStatus("current")
_H245Conference_ObjectIdentity = ObjectIdentity
h245Conference = _H245Conference_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 5)
)
_H245ConferenceTerminalTable_Object = MibTable
h245ConferenceTerminalTable = _H245ConferenceTerminalTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h245ConferenceTerminalTable.setStatus("current")
_H245ConferenceTerminalTableEntry_Object = MibTableRow
h245ConferenceTerminalTableEntry = _H245ConferenceTerminalTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1)
)
h245ConferenceTerminalTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245ConferenceConferenceId"),
    (0, "H245-MIB", "h245ConferenceTerminalLabel"),
)
if mibBuilder.loadTexts:
    h245ConferenceTerminalTableEntry.setStatus("current")


class _H245ConferenceConferenceId_Type(OctetString):
    """Custom type h245ConferenceConferenceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H245ConferenceConferenceId_Type.__name__ = "OctetString"
_H245ConferenceConferenceId_Object = MibTableColumn
h245ConferenceConferenceId = _H245ConferenceConferenceId_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1, 1),
    _H245ConferenceConferenceId_Type()
)
h245ConferenceConferenceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245ConferenceConferenceId.setStatus("current")


class _H245ConferenceTerminalLabel_Type(OctetString):
    """Custom type h245ConferenceTerminalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_H245ConferenceTerminalLabel_Type.__name__ = "OctetString"
_H245ConferenceTerminalLabel_Object = MibTableColumn
h245ConferenceTerminalLabel = _H245ConferenceTerminalLabel_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1, 2),
    _H245ConferenceTerminalLabel_Type()
)
h245ConferenceTerminalLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245ConferenceTerminalLabel.setStatus("current")
_H245ConferenceControlChannelIndex_Type = Integer32
_H245ConferenceControlChannelIndex_Object = MibTableColumn
h245ConferenceControlChannelIndex = _H245ConferenceControlChannelIndex_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1, 3),
    _H245ConferenceControlChannelIndex_Type()
)
h245ConferenceControlChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceControlChannelIndex.setStatus("current")
_H245ConferenceBroadcaster_Type = TruthValue
_H245ConferenceBroadcaster_Object = MibTableColumn
h245ConferenceBroadcaster = _H245ConferenceBroadcaster_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1, 4),
    _H245ConferenceBroadcaster_Type()
)
h245ConferenceBroadcaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceBroadcaster.setStatus("current")
_H245ConferenceConferenceChair_Type = TruthValue
_H245ConferenceConferenceChair_Object = MibTableColumn
h245ConferenceConferenceChair = _H245ConferenceConferenceChair_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1, 5),
    _H245ConferenceConferenceChair_Type()
)
h245ConferenceConferenceChair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceConferenceChair.setStatus("current")
_H245ConferenceMultipoint_Type = TruthValue
_H245ConferenceMultipoint_Object = MibTableColumn
h245ConferenceMultipoint = _H245ConferenceMultipoint_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 1, 1, 6),
    _H245ConferenceMultipoint_Type()
)
h245ConferenceMultipoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceMultipoint.setStatus("current")
_H245ConferenceStatsTable_Object = MibTable
h245ConferenceStatsTable = _H245ConferenceStatsTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    h245ConferenceStatsTable.setStatus("current")
_H245ConferenceStatsTableEntry_Object = MibTableRow
h245ConferenceStatsTableEntry = _H245ConferenceStatsTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1)
)
h245ConferenceStatsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h245ConferenceStatsTableEntry.setStatus("current")
_H245ConferenceBroadcastMyLogicalChannel_Type = Counter32
_H245ConferenceBroadcastMyLogicalChannel_Object = MibTableColumn
h245ConferenceBroadcastMyLogicalChannel = _H245ConferenceBroadcastMyLogicalChannel_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 1),
    _H245ConferenceBroadcastMyLogicalChannel_Type()
)
h245ConferenceBroadcastMyLogicalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceBroadcastMyLogicalChannel.setStatus("current")
_H245ConferenceCancelBroadcastMyLogicalChannel_Type = Counter32
_H245ConferenceCancelBroadcastMyLogicalChannel_Object = MibTableColumn
h245ConferenceCancelBroadcastMyLogicalChannel = _H245ConferenceCancelBroadcastMyLogicalChannel_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 2),
    _H245ConferenceCancelBroadcastMyLogicalChannel_Type()
)
h245ConferenceCancelBroadcastMyLogicalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceCancelBroadcastMyLogicalChannel.setStatus("current")
_H245ConferenceSendThisSource_Type = Counter32
_H245ConferenceSendThisSource_Object = MibTableColumn
h245ConferenceSendThisSource = _H245ConferenceSendThisSource_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 3),
    _H245ConferenceSendThisSource_Type()
)
h245ConferenceSendThisSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceSendThisSource.setStatus("current")
_H245ConferenceCancelSendThisSource_Type = Counter32
_H245ConferenceCancelSendThisSource_Object = MibTableColumn
h245ConferenceCancelSendThisSource = _H245ConferenceCancelSendThisSource_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 4),
    _H245ConferenceCancelSendThisSource_Type()
)
h245ConferenceCancelSendThisSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceCancelSendThisSource.setStatus("current")
_H245ConferenceDropConference_Type = Counter32
_H245ConferenceDropConference_Object = MibTableColumn
h245ConferenceDropConference = _H245ConferenceDropConference_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 5),
    _H245ConferenceDropConference_Type()
)
h245ConferenceDropConference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceDropConference.setStatus("current")
_H245ConferenceEqualiseDelay_Type = Counter32
_H245ConferenceEqualiseDelay_Object = MibTableColumn
h245ConferenceEqualiseDelay = _H245ConferenceEqualiseDelay_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 6),
    _H245ConferenceEqualiseDelay_Type()
)
h245ConferenceEqualiseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceEqualiseDelay.setStatus("current")
_H245ConferenceZeroDelay_Type = Counter32
_H245ConferenceZeroDelay_Object = MibTableColumn
h245ConferenceZeroDelay = _H245ConferenceZeroDelay_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 7),
    _H245ConferenceZeroDelay_Type()
)
h245ConferenceZeroDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceZeroDelay.setStatus("current")
_H245ConferenceMultipointModeCommand_Type = Counter32
_H245ConferenceMultipointModeCommand_Object = MibTableColumn
h245ConferenceMultipointModeCommand = _H245ConferenceMultipointModeCommand_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 8),
    _H245ConferenceMultipointModeCommand_Type()
)
h245ConferenceMultipointModeCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceMultipointModeCommand.setStatus("current")
_H245ConferenceCancelMultipointModeCommand_Type = Counter32
_H245ConferenceCancelMultipointModeCommand_Object = MibTableColumn
h245ConferenceCancelMultipointModeCommand = _H245ConferenceCancelMultipointModeCommand_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 9),
    _H245ConferenceCancelMultipointModeCommand_Type()
)
h245ConferenceCancelMultipointModeCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceCancelMultipointModeCommand.setStatus("current")
_H245ConferenceVideoFreezePicture_Type = Counter32
_H245ConferenceVideoFreezePicture_Object = MibTableColumn
h245ConferenceVideoFreezePicture = _H245ConferenceVideoFreezePicture_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 10),
    _H245ConferenceVideoFreezePicture_Type()
)
h245ConferenceVideoFreezePicture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceVideoFreezePicture.setStatus("current")
_H245ConferenceVideoFastUpdatePicture_Type = Counter32
_H245ConferenceVideoFastUpdatePicture_Object = MibTableColumn
h245ConferenceVideoFastUpdatePicture = _H245ConferenceVideoFastUpdatePicture_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 11),
    _H245ConferenceVideoFastUpdatePicture_Type()
)
h245ConferenceVideoFastUpdatePicture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceVideoFastUpdatePicture.setStatus("current")
_H245ConferenceVideoFastUpdateGOB_Type = Counter32
_H245ConferenceVideoFastUpdateGOB_Object = MibTableColumn
h245ConferenceVideoFastUpdateGOB = _H245ConferenceVideoFastUpdateGOB_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 12),
    _H245ConferenceVideoFastUpdateGOB_Type()
)
h245ConferenceVideoFastUpdateGOB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceVideoFastUpdateGOB.setStatus("current")
_H245ConferenceVideoTemporalSpatialTradeOff_Type = Counter32
_H245ConferenceVideoTemporalSpatialTradeOff_Object = MibTableColumn
h245ConferenceVideoTemporalSpatialTradeOff = _H245ConferenceVideoTemporalSpatialTradeOff_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 13),
    _H245ConferenceVideoTemporalSpatialTradeOff_Type()
)
h245ConferenceVideoTemporalSpatialTradeOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceVideoTemporalSpatialTradeOff.setStatus("current")
_H245ConferenceVideoSendSyncEveryGOB_Type = Counter32
_H245ConferenceVideoSendSyncEveryGOB_Object = MibTableColumn
h245ConferenceVideoSendSyncEveryGOB = _H245ConferenceVideoSendSyncEveryGOB_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 14),
    _H245ConferenceVideoSendSyncEveryGOB_Type()
)
h245ConferenceVideoSendSyncEveryGOB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceVideoSendSyncEveryGOB.setStatus("current")
_H245ConferenceVideoFastUpdateMB_Type = Counter32
_H245ConferenceVideoFastUpdateMB_Object = MibTableColumn
h245ConferenceVideoFastUpdateMB = _H245ConferenceVideoFastUpdateMB_Object(
    (0, 0, 8, 341, 1, 3, 1, 5, 2, 1, 15),
    _H245ConferenceVideoFastUpdateMB_Type()
)
h245ConferenceVideoFastUpdateMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245ConferenceVideoFastUpdateMB.setStatus("current")
_H245Misc_ObjectIdentity = ObjectIdentity
h245Misc = _H245Misc_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 6)
)
_H245MiscRoundTripDelayTable_Object = MibTable
h245MiscRoundTripDelayTable = _H245MiscRoundTripDelayTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    h245MiscRoundTripDelayTable.setStatus("current")
_H245MiscRoundTripDelayTableEntry_Object = MibTableRow
h245MiscRoundTripDelayTableEntry = _H245MiscRoundTripDelayTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1)
)
h245MiscRoundTripDelayTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245ControlChannelIndex"),
)
if mibBuilder.loadTexts:
    h245MiscRoundTripDelayTableEntry.setStatus("current")


class _H245MiscRTDState_Type(Integer32):
    """Custom type h245MiscRTDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("waiting", 2))
    )


_H245MiscRTDState_Type.__name__ = "Integer32"
_H245MiscRTDState_Object = MibTableColumn
h245MiscRTDState = _H245MiscRTDState_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1, 1),
    _H245MiscRTDState_Type()
)
h245MiscRTDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscRTDState.setStatus("current")
_H245MiscT105TimerExpired_Type = TruthValue
_H245MiscT105TimerExpired_Object = MibTableColumn
h245MiscT105TimerExpired = _H245MiscT105TimerExpired_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1, 2),
    _H245MiscT105TimerExpired_Type()
)
h245MiscT105TimerExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscT105TimerExpired.setStatus("current")
_H245MiscLastRTDRequestSent_Type = Integer32
_H245MiscLastRTDRequestSent_Object = MibTableColumn
h245MiscLastRTDRequestSent = _H245MiscLastRTDRequestSent_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1, 3),
    _H245MiscLastRTDRequestSent_Type()
)
h245MiscLastRTDRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscLastRTDRequestSent.setStatus("current")
_H245MiscLastRTDRequestRcvd_Type = Integer32
_H245MiscLastRTDRequestRcvd_Object = MibTableColumn
h245MiscLastRTDRequestRcvd = _H245MiscLastRTDRequestRcvd_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1, 4),
    _H245MiscLastRTDRequestRcvd_Type()
)
h245MiscLastRTDRequestRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscLastRTDRequestRcvd.setStatus("current")
_H245MiscLastRTDResponseSent_Type = Integer32
_H245MiscLastRTDResponseSent_Object = MibTableColumn
h245MiscLastRTDResponseSent = _H245MiscLastRTDResponseSent_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1, 5),
    _H245MiscLastRTDResponseSent_Type()
)
h245MiscLastRTDResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscLastRTDResponseSent.setStatus("current")
_H245MiscLastRTDResponseRcvd_Type = Integer32
_H245MiscLastRTDResponseRcvd_Object = MibTableColumn
h245MiscLastRTDResponseRcvd = _H245MiscLastRTDResponseRcvd_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 1, 1, 6),
    _H245MiscLastRTDResponseRcvd_Type()
)
h245MiscLastRTDResponseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscLastRTDResponseRcvd.setStatus("current")
_H245MiscMaintenanceLoopTable_Object = MibTable
h245MiscMaintenanceLoopTable = _H245MiscMaintenanceLoopTable_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    h245MiscMaintenanceLoopTable.setStatus("current")
_H245MiscMaintenanceLoopTableEntry_Object = MibTableRow
h245MiscMaintenanceLoopTableEntry = _H245MiscMaintenanceLoopTableEntry_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1)
)
h245MiscMaintenanceLoopTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H245-MIB", "h245ControlChannelIndex"),
    (0, "H245-MIB", "h245MiscMaintenanceLoopDirection"),
)
if mibBuilder.loadTexts:
    h245MiscMaintenanceLoopTableEntry.setStatus("current")


class _H245MiscMaintenanceLoopDirection_Type(Integer32):
    """Custom type h245MiscMaintenanceLoopDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_H245MiscMaintenanceLoopDirection_Type.__name__ = "Integer32"
_H245MiscMaintenanceLoopDirection_Object = MibTableColumn
h245MiscMaintenanceLoopDirection = _H245MiscMaintenanceLoopDirection_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 1),
    _H245MiscMaintenanceLoopDirection_Type()
)
h245MiscMaintenanceLoopDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h245MiscMaintenanceLoopDirection.setStatus("current")


class _H245MiscMLState_Type(Integer32):
    """Custom type h245MiscMLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("looped", 3),
          ("notLooped", 1),
          ("waiting", 2))
    )


_H245MiscMLState_Type.__name__ = "Integer32"
_H245MiscMLState_Object = MibTableColumn
h245MiscMLState = _H245MiscMLState_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 2),
    _H245MiscMLState_Type()
)
h245MiscMLState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscMLState.setStatus("current")
_H245MiscNumberOfRequests_Type = Counter32
_H245MiscNumberOfRequests_Object = MibTableColumn
h245MiscNumberOfRequests = _H245MiscNumberOfRequests_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 3),
    _H245MiscNumberOfRequests_Type()
)
h245MiscNumberOfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscNumberOfRequests.setStatus("current")
_H245MiscNumberOfAcks_Type = Counter32
_H245MiscNumberOfAcks_Object = MibTableColumn
h245MiscNumberOfAcks = _H245MiscNumberOfAcks_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 4),
    _H245MiscNumberOfAcks_Type()
)
h245MiscNumberOfAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscNumberOfAcks.setStatus("current")


class _H245MiscLastMLRequestOrAckType_Type(Integer32):
    """Custom type h245MiscLastMLRequestOrAckType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("awaitingResponse", 3),
          ("looped", 1),
          ("notLooped", 2))
    )


_H245MiscLastMLRequestOrAckType_Type.__name__ = "Integer32"
_H245MiscLastMLRequestOrAckType_Object = MibTableColumn
h245MiscLastMLRequestOrAckType = _H245MiscLastMLRequestOrAckType_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 5),
    _H245MiscLastMLRequestOrAckType_Type()
)
h245MiscLastMLRequestOrAckType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscLastMLRequestOrAckType.setStatus("current")
_H245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber_Type = Integer32
_H245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber_Object = MibTableColumn
h245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber = _H245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 6),
    _H245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber_Type()
)
h245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber.setStatus("current")
_H245MiscNumberOfRejects_Type = Counter32
_H245MiscNumberOfRejects_Object = MibTableColumn
h245MiscNumberOfRejects = _H245MiscNumberOfRejects_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 7),
    _H245MiscNumberOfRejects_Type()
)
h245MiscNumberOfRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscNumberOfRejects.setStatus("current")


class _H245MiscLastRejectType_Type(Integer32):
    """Custom type h245MiscLastRejectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log-channel-loop", 3),
          ("media-loop", 2),
          ("system-loop", 1))
    )


_H245MiscLastRejectType_Type.__name__ = "Integer32"
_H245MiscLastRejectType_Object = MibTableColumn
h245MiscLastRejectType = _H245MiscLastRejectType_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 8),
    _H245MiscLastRejectType_Type()
)
h245MiscLastRejectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscLastRejectType.setStatus("current")


class _H245MiscErrorCode_Type(Integer32):
    """Custom type h245MiscErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("can-not-perform-loop", 1)
    )


_H245MiscErrorCode_Type.__name__ = "Integer32"
_H245MiscErrorCode_Object = MibTableColumn
h245MiscErrorCode = _H245MiscErrorCode_Object(
    (0, 0, 8, 341, 1, 3, 1, 6, 2, 1, 9),
    _H245MiscErrorCode_Type()
)
h245MiscErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h245MiscErrorCode.setStatus("current")
_H245MIBConformance_ObjectIdentity = ObjectIdentity
h245MIBConformance = _H245MIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 7)
)
_H245MIBGroups_ObjectIdentity = ObjectIdentity
h245MIBGroups = _H245MIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 3, 1, 7, 1)
)

# Managed Objects groups

h245ConfigurationGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 3, 1, 7, 1, 1)
)
h245ConfigurationGroup.setObjects(
      *(("H245-MIB", "h245ConfigT101Timer"),
        ("H245-MIB", "h245ConfigT102Timer"),
        ("H245-MIB", "h245ConfigT103Timer"),
        ("H245-MIB", "h245ConfigT104Timer"),
        ("H245-MIB", "h245ConfigT105Timer"),
        ("H245-MIB", "h245ConfigT106Timer"),
        ("H245-MIB", "h245ConfigT107Timer"),
        ("H245-MIB", "h245ConfigT108Timer"),
        ("H245-MIB", "h245ConfigT109Timer"),
        ("H245-MIB", "h245ConfigN100Counter"))
)
if mibBuilder.loadTexts:
    h245ConfigurationGroup.setStatus("current")

h245ControlChannelGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 3, 1, 7, 1, 2)
)
h245ControlChannelGroup.setObjects(
      *(("H245-MIB", "h245ControlChannelNumberOfListenPorts"),
        ("H245-MIB", "h245ControlChannelMaxConnections"),
        ("H245-MIB", "h245ControlChannelNumberOfListenFails"),
        ("H245-MIB", "h245ControlChannelNumberOfActiveConnections"),
        ("H245-MIB", "h245ControlChannelMasterSlaveMaxRetries"),
        ("H245-MIB", "h245ControlChannelConnectionAttemptsFail"),
        ("H245-MIB", "h245ControlChanneMasterSlavelDeterminations"),
        ("H245-MIB", "h245ControlChannelMasterSlaveAcks"),
        ("H245-MIB", "h245ControlChannelMasterSlaveRejects"),
        ("H245-MIB", "h245ControlChannelMasterSlaveT106Rejects"),
        ("H245-MIB", "h245ControlChannelMasterSlaveMSDRejects"),
        ("H245-MIB", "h245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects"),
        ("H245-MIB", "h245ControlChannelMasterSlaveMaxCounterRejects"),
        ("H245-MIB", "h245ControlChannelMasterSlaveReleases"),
        ("H245-MIB", "h245ControlChannelNumberOfTunnels"),
        ("H245-MIB", "h245ControlChannelIndex"),
        ("H245-MIB", "h245ControlChannelMSDState"),
        ("H245-MIB", "h245ControlChannelTerminalType"),
        ("H245-MIB", "h245ControlChannelNumberOfMSDRetries"))
)
if mibBuilder.loadTexts:
    h245ControlChannelGroup.setStatus("current")

h245CapExchangeGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 3, 1, 7, 1, 3)
)
h245CapExchangeGroup.setObjects(
      *(("H245-MIB", "h245CapExchangeSets"),
        ("H245-MIB", "h245CapExchangeAcks"),
        ("H245-MIB", "h245CapExchangeRejects"),
        ("H245-MIB", "h245CapExchangeRejectUnspecified"),
        ("H245-MIB", "h245CapExchangeRejectUndefinedTableEntryUsed"),
        ("H245-MIB", "h245CapExchangeRejectDescriptorCapacityExceeded"),
        ("H245-MIB", "h245CapExchangeRejectTableEntryCapacityExeeded"),
        ("H245-MIB", "h245CapExchangeReleases"),
        ("H245-MIB", "h245CapExchangeState"),
        ("H245-MIB", "h245CapExchangeProtocolId"),
        ("H245-MIB", "h245CapExchangeRejectCause"),
        ("H245-MIB", "h245CapExchangeMultiplexCapability"),
        ("H245-MIB", "h245CapExchangeCapability"),
        ("H245-MIB", "h245CapExchangeCapabilityDescriptors"))
)
if mibBuilder.loadTexts:
    h245CapExchangeGroup.setStatus("current")

h245LogChannelsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 3, 1, 7, 1, 4)
)
h245LogChannelsGroup.setObjects(
      *(("H245-MIB", "h245LogChannelsIndex"),
        ("H245-MIB", "h245LogChannelsChannelState"),
        ("H245-MIB", "h245LogChannelsMediaTableType"),
        ("H245-MIB", "h245LogChannelsSessionId"),
        ("H245-MIB", "h245LogChannelsAssociateSessionId"),
        ("H245-MIB", "h245LogChannelsMediaChannel"),
        ("H245-MIB", "h245LogChannelsMediaGuaranteedDelivery"),
        ("H245-MIB", "h245LogChannelsMediaControlChannel"),
        ("H245-MIB", "h245LogChannelsMediaControlGuaranteedDelivery"),
        ("H245-MIB", "h245LogChannelsSilenceSuppression"),
        ("H245-MIB", "h245LogChannelsDestination"),
        ("H245-MIB", "h245LogChannelsDynamicRTPPayloadType"),
        ("H245-MIB", "h245LogChannelsH261aVideoPacketization"),
        ("H245-MIB", "h245LogChannelsRTPPayloadDescriptor"),
        ("H245-MIB", "h245LogChannelsRTPPayloadType"),
        ("H245-MIB", "h245LogChannelsTransportCapability"),
        ("H245-MIB", "h245LogChannelsRedundancyEncoding"),
        ("H245-MIB", "h245LogChannelsSrcTerminalLabel"),
        ("H245-MIB", "h245LogChanOpenLogChanTotalRequests"),
        ("H245-MIB", "h245LogChanOpenLogChanAcks"),
        ("H245-MIB", "h245LogChanOpenLogChanConfirms"),
        ("H245-MIB", "h245LogChanOpenLogChanRejects"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectUnspecified"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectUnsuitableReverseParameters"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectDataTypeNotSupported"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectDataTypeNotAvailable"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectUnknownDataType"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectMulticastChannelNotAllowed"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectInsuffientBandwdith"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectInvalidSessionID"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectMasterSlaveConflict"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectWaitForCommunicationMode"),
        ("H245-MIB", "h245LogChanOpenLogChanRejectInvalidDependentChannel"),
        ("H245-MIB", "h245LogChansOpenLogChanRejectReplacementForRejected"),
        ("H245-MIB", "h245LogChanCloseLogChannels"),
        ("H245-MIB", "h245LogChanCloseLogChanAcks"),
        ("H245-MIB", "h245LogChanCloseLogChanRequests"),
        ("H245-MIB", "h245LogChanCloseLogChanRequestsAcks"),
        ("H245-MIB", "h245LogChanCloseLogChanRequestRejects"),
        ("H245-MIB", "h245LogChanCloseLogChanRequestReleases"))
)
if mibBuilder.loadTexts:
    h245LogChannelsGroup.setStatus("current")

h245ConferenceGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 3, 1, 7, 1, 5)
)
h245ConferenceGroup.setObjects(
      *(("H245-MIB", "h245ConferenceControlChannelIndex"),
        ("H245-MIB", "h245ConferenceBroadcaster"),
        ("H245-MIB", "h245ConferenceConferenceChair"),
        ("H245-MIB", "h245ConferenceMultipoint"),
        ("H245-MIB", "h245ConferenceBroadcastMyLogicalChannel"),
        ("H245-MIB", "h245ConferenceCancelBroadcastMyLogicalChannel"),
        ("H245-MIB", "h245ConferenceSendThisSource"),
        ("H245-MIB", "h245ConferenceCancelSendThisSource"),
        ("H245-MIB", "h245ConferenceDropConference"),
        ("H245-MIB", "h245ConferenceEqualiseDelay"),
        ("H245-MIB", "h245ConferenceZeroDelay"),
        ("H245-MIB", "h245ConferenceMultipointModeCommand"),
        ("H245-MIB", "h245ConferenceCancelMultipointModeCommand"),
        ("H245-MIB", "h245ConferenceVideoFreezePicture"),
        ("H245-MIB", "h245ConferenceVideoFastUpdatePicture"),
        ("H245-MIB", "h245ConferenceVideoFastUpdateGOB"),
        ("H245-MIB", "h245ConferenceVideoTemporalSpatialTradeOff"),
        ("H245-MIB", "h245ConferenceVideoSendSyncEveryGOB"),
        ("H245-MIB", "h245ConferenceVideoFastUpdateMB"))
)
if mibBuilder.loadTexts:
    h245ConferenceGroup.setStatus("current")

h245MiscGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 3, 1, 7, 1, 6)
)
h245MiscGroup.setObjects(
      *(("H245-MIB", "h245MiscRTDState"),
        ("H245-MIB", "h245MiscT105TimerExpired"),
        ("H245-MIB", "h245MiscLastRTDRequestSent"),
        ("H245-MIB", "h245MiscLastRTDRequestRcvd"),
        ("H245-MIB", "h245MiscLastRTDResponseSent"),
        ("H245-MIB", "h245MiscLastRTDResponseRcvd"),
        ("H245-MIB", "h245MiscMLState"),
        ("H245-MIB", "h245MiscNumberOfRequests"),
        ("H245-MIB", "h245MiscNumberOfAcks"),
        ("H245-MIB", "h245MiscLastMLRequestOrAckType"),
        ("H245-MIB", "h245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber"),
        ("H245-MIB", "h245MiscNumberOfRejects"),
        ("H245-MIB", "h245MiscLastRejectType"),
        ("H245-MIB", "h245MiscErrorCode"))
)
if mibBuilder.loadTexts:
    h245MiscGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h245MIBCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    h245MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H245-MIB",
    **{"h245": h245,
       "h245Configuration": h245Configuration,
       "h245ConfigurationTable": h245ConfigurationTable,
       "h245ConfigurationTableEntry": h245ConfigurationTableEntry,
       "h245ConfigT101Timer": h245ConfigT101Timer,
       "h245ConfigT102Timer": h245ConfigT102Timer,
       "h245ConfigT103Timer": h245ConfigT103Timer,
       "h245ConfigT104Timer": h245ConfigT104Timer,
       "h245ConfigT105Timer": h245ConfigT105Timer,
       "h245ConfigT106Timer": h245ConfigT106Timer,
       "h245ConfigT107Timer": h245ConfigT107Timer,
       "h245ConfigT108Timer": h245ConfigT108Timer,
       "h245ConfigT109Timer": h245ConfigT109Timer,
       "h245ConfigN100Counter": h245ConfigN100Counter,
       "h245ControlChannel": h245ControlChannel,
       "h245ControlChannelStatsTable": h245ControlChannelStatsTable,
       "h245ControlChannelStatsTableEntry": h245ControlChannelStatsTableEntry,
       "h245ControlChannelNumberOfListenPorts": h245ControlChannelNumberOfListenPorts,
       "h245ControlChannelMaxConnections": h245ControlChannelMaxConnections,
       "h245ControlChannelNumberOfListenFails": h245ControlChannelNumberOfListenFails,
       "h245ControlChannelNumberOfActiveConnections": h245ControlChannelNumberOfActiveConnections,
       "h245ControlChannelMasterSlaveMaxRetries": h245ControlChannelMasterSlaveMaxRetries,
       "h245ControlChannelConnectionAttemptsFail": h245ControlChannelConnectionAttemptsFail,
       "h245ControlChanneMasterSlavelDeterminations": h245ControlChanneMasterSlavelDeterminations,
       "h245ControlChannelMasterSlaveAcks": h245ControlChannelMasterSlaveAcks,
       "h245ControlChannelMasterSlaveRejects": h245ControlChannelMasterSlaveRejects,
       "h245ControlChannelMasterSlaveT106Rejects": h245ControlChannelMasterSlaveT106Rejects,
       "h245ControlChannelMasterSlaveMSDRejects": h245ControlChannelMasterSlaveMSDRejects,
       "h245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects": h245ControlChannelNumberOfMasterSlaveInconsistentFieldRejects,
       "h245ControlChannelMasterSlaveMaxCounterRejects": h245ControlChannelMasterSlaveMaxCounterRejects,
       "h245ControlChannelMasterSlaveReleases": h245ControlChannelMasterSlaveReleases,
       "h245ControlChannelNumberOfTunnels": h245ControlChannelNumberOfTunnels,
       "h245ControlChannelMasterSlaveTable": h245ControlChannelMasterSlaveTable,
       "h245ControlChannelMasterSlaveTableEntry": h245ControlChannelMasterSlaveTableEntry,
       "h245ControlChannelSrcAddressTag": h245ControlChannelSrcAddressTag,
       "h245ControlChannelSrcTransporTAddress": h245ControlChannelSrcTransporTAddress,
       "h245ControlChannelDesTAddressTag": h245ControlChannelDesTAddressTag,
       "h245ControlChannelDestTransporTAddress": h245ControlChannelDestTransporTAddress,
       "h245ControlChannelIndex": h245ControlChannelIndex,
       "h245ControlChannelMSDState": h245ControlChannelMSDState,
       "h245ControlChannelTerminalType": h245ControlChannelTerminalType,
       "h245ControlChannelNumberOfMSDRetries": h245ControlChannelNumberOfMSDRetries,
       "h245ControlChannelIsTunneling": h245ControlChannelIsTunneling,
       "h245CapExchange": h245CapExchange,
       "h245CapExchangeStatsTable": h245CapExchangeStatsTable,
       "h245CapExchangeStatsTableEntry": h245CapExchangeStatsTableEntry,
       "h245CapExchangeSets": h245CapExchangeSets,
       "h245CapExchangeAcks": h245CapExchangeAcks,
       "h245CapExchangeRejects": h245CapExchangeRejects,
       "h245CapExchangeRejectUnspecified": h245CapExchangeRejectUnspecified,
       "h245CapExchangeRejectUndefinedTableEntryUsed": h245CapExchangeRejectUndefinedTableEntryUsed,
       "h245CapExchangeRejectDescriptorCapacityExceeded": h245CapExchangeRejectDescriptorCapacityExceeded,
       "h245CapExchangeRejectTableEntryCapacityExeeded": h245CapExchangeRejectTableEntryCapacityExeeded,
       "h245CapExchangeReleases": h245CapExchangeReleases,
       "h245CapExchangeCapabilityTable": h245CapExchangeCapabilityTable,
       "h245CapExchangeCapabilityTableEntry": h245CapExchangeCapabilityTableEntry,
       "h245CapExchangeDirection": h245CapExchangeDirection,
       "h245CapExchangeState": h245CapExchangeState,
       "h245CapExchangeProtocolId": h245CapExchangeProtocolId,
       "h245CapExchangeRejectCause": h245CapExchangeRejectCause,
       "h245CapExchangeMultiplexCapability": h245CapExchangeMultiplexCapability,
       "h245CapExchangeCapability": h245CapExchangeCapability,
       "h245CapExchangeCapabilityDescriptors": h245CapExchangeCapabilityDescriptors,
       "h245LogChannels": h245LogChannels,
       "h245LogChannelsChannelTable": h245LogChannelsChannelTable,
       "h245LogChannelsChannelTableEntry": h245LogChannelsChannelTableEntry,
       "h245LogChannelsChannelNumber": h245LogChannelsChannelNumber,
       "h245LogChannelsChannelDirection": h245LogChannelsChannelDirection,
       "h245LogChannelsIndex": h245LogChannelsIndex,
       "h245LogChannelsChannelState": h245LogChannelsChannelState,
       "h245LogChannelsMediaTableType": h245LogChannelsMediaTableType,
       "h245LogChannelsH225Table": h245LogChannelsH225Table,
       "h245LogChannelsH225TableEntry": h245LogChannelsH225TableEntry,
       "h245LogChannelsSessionId": h245LogChannelsSessionId,
       "h245LogChannelsAssociateSessionId": h245LogChannelsAssociateSessionId,
       "h245LogChannelsMediaChannel": h245LogChannelsMediaChannel,
       "h245LogChannelsMediaGuaranteedDelivery": h245LogChannelsMediaGuaranteedDelivery,
       "h245LogChannelsMediaControlChannel": h245LogChannelsMediaControlChannel,
       "h245LogChannelsMediaControlGuaranteedDelivery": h245LogChannelsMediaControlGuaranteedDelivery,
       "h245LogChannelsSilenceSuppression": h245LogChannelsSilenceSuppression,
       "h245LogChannelsDestination": h245LogChannelsDestination,
       "h245LogChannelsDynamicRTPPayloadType": h245LogChannelsDynamicRTPPayloadType,
       "h245LogChannelsH261aVideoPacketization": h245LogChannelsH261aVideoPacketization,
       "h245LogChannelsRTPPayloadDescriptor": h245LogChannelsRTPPayloadDescriptor,
       "h245LogChannelsRTPPayloadType": h245LogChannelsRTPPayloadType,
       "h245LogChannelsTransportCapability": h245LogChannelsTransportCapability,
       "h245LogChannelsRedundancyEncoding": h245LogChannelsRedundancyEncoding,
       "h245LogChannelsSrcTerminalLabel": h245LogChannelsSrcTerminalLabel,
       "h245LogChannelOpenLogicalChannelTable": h245LogChannelOpenLogicalChannelTable,
       "h245LogChannelOpenLogicalChannelTableEntry": h245LogChannelOpenLogicalChannelTableEntry,
       "h245LogChanOpenLogChanTotalRequests": h245LogChanOpenLogChanTotalRequests,
       "h245LogChanOpenLogChanAcks": h245LogChanOpenLogChanAcks,
       "h245LogChanOpenLogChanConfirms": h245LogChanOpenLogChanConfirms,
       "h245LogChanOpenLogChanRejects": h245LogChanOpenLogChanRejects,
       "h245LogChanOpenLogChanRejectUnspecified": h245LogChanOpenLogChanRejectUnspecified,
       "h245LogChanOpenLogChanRejectUnsuitableReverseParameters": h245LogChanOpenLogChanRejectUnsuitableReverseParameters,
       "h245LogChanOpenLogChanRejectDataTypeNotSupported": h245LogChanOpenLogChanRejectDataTypeNotSupported,
       "h245LogChanOpenLogChanRejectDataTypeNotAvailable": h245LogChanOpenLogChanRejectDataTypeNotAvailable,
       "h245LogChanOpenLogChanRejectUnknownDataType": h245LogChanOpenLogChanRejectUnknownDataType,
       "h245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported": h245LogChanOpenLogChanRejectDataTypeALCombinationNotSupported,
       "h245LogChanOpenLogChanRejectMulticastChannelNotAllowed": h245LogChanOpenLogChanRejectMulticastChannelNotAllowed,
       "h245LogChanOpenLogChanRejectInsuffientBandwdith": h245LogChanOpenLogChanRejectInsuffientBandwdith,
       "h245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed": h245LogChanOpenLogChanRejectSeparateStackEstablishmentFailed,
       "h245LogChanOpenLogChanRejectInvalidSessionID": h245LogChanOpenLogChanRejectInvalidSessionID,
       "h245LogChanOpenLogChanRejectMasterSlaveConflict": h245LogChanOpenLogChanRejectMasterSlaveConflict,
       "h245LogChanOpenLogChanRejectWaitForCommunicationMode": h245LogChanOpenLogChanRejectWaitForCommunicationMode,
       "h245LogChanOpenLogChanRejectInvalidDependentChannel": h245LogChanOpenLogChanRejectInvalidDependentChannel,
       "h245LogChansOpenLogChanRejectReplacementForRejected": h245LogChansOpenLogChanRejectReplacementForRejected,
       "h245LogChannelCloseLogicalChannelTable": h245LogChannelCloseLogicalChannelTable,
       "h245LogChannelCloseLogicalChannelTableEntry": h245LogChannelCloseLogicalChannelTableEntry,
       "h245LogChanCloseLogChannels": h245LogChanCloseLogChannels,
       "h245LogChanCloseLogChanAcks": h245LogChanCloseLogChanAcks,
       "h245LogChanCloseLogChanRequests": h245LogChanCloseLogChanRequests,
       "h245LogChanCloseLogChanRequestsAcks": h245LogChanCloseLogChanRequestsAcks,
       "h245LogChanCloseLogChanRequestRejects": h245LogChanCloseLogChanRequestRejects,
       "h245LogChanCloseLogChanRequestReleases": h245LogChanCloseLogChanRequestReleases,
       "h245Conference": h245Conference,
       "h245ConferenceTerminalTable": h245ConferenceTerminalTable,
       "h245ConferenceTerminalTableEntry": h245ConferenceTerminalTableEntry,
       "h245ConferenceConferenceId": h245ConferenceConferenceId,
       "h245ConferenceTerminalLabel": h245ConferenceTerminalLabel,
       "h245ConferenceControlChannelIndex": h245ConferenceControlChannelIndex,
       "h245ConferenceBroadcaster": h245ConferenceBroadcaster,
       "h245ConferenceConferenceChair": h245ConferenceConferenceChair,
       "h245ConferenceMultipoint": h245ConferenceMultipoint,
       "h245ConferenceStatsTable": h245ConferenceStatsTable,
       "h245ConferenceStatsTableEntry": h245ConferenceStatsTableEntry,
       "h245ConferenceBroadcastMyLogicalChannel": h245ConferenceBroadcastMyLogicalChannel,
       "h245ConferenceCancelBroadcastMyLogicalChannel": h245ConferenceCancelBroadcastMyLogicalChannel,
       "h245ConferenceSendThisSource": h245ConferenceSendThisSource,
       "h245ConferenceCancelSendThisSource": h245ConferenceCancelSendThisSource,
       "h245ConferenceDropConference": h245ConferenceDropConference,
       "h245ConferenceEqualiseDelay": h245ConferenceEqualiseDelay,
       "h245ConferenceZeroDelay": h245ConferenceZeroDelay,
       "h245ConferenceMultipointModeCommand": h245ConferenceMultipointModeCommand,
       "h245ConferenceCancelMultipointModeCommand": h245ConferenceCancelMultipointModeCommand,
       "h245ConferenceVideoFreezePicture": h245ConferenceVideoFreezePicture,
       "h245ConferenceVideoFastUpdatePicture": h245ConferenceVideoFastUpdatePicture,
       "h245ConferenceVideoFastUpdateGOB": h245ConferenceVideoFastUpdateGOB,
       "h245ConferenceVideoTemporalSpatialTradeOff": h245ConferenceVideoTemporalSpatialTradeOff,
       "h245ConferenceVideoSendSyncEveryGOB": h245ConferenceVideoSendSyncEveryGOB,
       "h245ConferenceVideoFastUpdateMB": h245ConferenceVideoFastUpdateMB,
       "h245Misc": h245Misc,
       "h245MiscRoundTripDelayTable": h245MiscRoundTripDelayTable,
       "h245MiscRoundTripDelayTableEntry": h245MiscRoundTripDelayTableEntry,
       "h245MiscRTDState": h245MiscRTDState,
       "h245MiscT105TimerExpired": h245MiscT105TimerExpired,
       "h245MiscLastRTDRequestSent": h245MiscLastRTDRequestSent,
       "h245MiscLastRTDRequestRcvd": h245MiscLastRTDRequestRcvd,
       "h245MiscLastRTDResponseSent": h245MiscLastRTDResponseSent,
       "h245MiscLastRTDResponseRcvd": h245MiscLastRTDResponseRcvd,
       "h245MiscMaintenanceLoopTable": h245MiscMaintenanceLoopTable,
       "h245MiscMaintenanceLoopTableEntry": h245MiscMaintenanceLoopTableEntry,
       "h245MiscMaintenanceLoopDirection": h245MiscMaintenanceLoopDirection,
       "h245MiscMLState": h245MiscMLState,
       "h245MiscNumberOfRequests": h245MiscNumberOfRequests,
       "h245MiscNumberOfAcks": h245MiscNumberOfAcks,
       "h245MiscLastMLRequestOrAckType": h245MiscLastMLRequestOrAckType,
       "h245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber": h245MiscMLMediaOrLogicalChannelLoopRejectChannelNumber,
       "h245MiscNumberOfRejects": h245MiscNumberOfRejects,
       "h245MiscLastRejectType": h245MiscLastRejectType,
       "h245MiscErrorCode": h245MiscErrorCode,
       "h245MIBConformance": h245MIBConformance,
       "h245MIBGroups": h245MIBGroups,
       "h245ConfigurationGroup": h245ConfigurationGroup,
       "h245ControlChannelGroup": h245ControlChannelGroup,
       "h245CapExchangeGroup": h245CapExchangeGroup,
       "h245LogChannelsGroup": h245LogChannelsGroup,
       "h245ConferenceGroup": h245ConferenceGroup,
       "h245MiscGroup": h245MiscGroup,
       "h245MIBCompliance": h245MIBCompliance}
)
