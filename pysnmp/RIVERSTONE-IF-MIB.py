# SNMP MIB module (RIVERSTONE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:45 2024
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

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(RsQueuePolicy,) = mibBuilder.importSymbols(
    "RIVERSTONE-TC-MIB",
    "RsQueuePolicy")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rsIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60)
)
rsIfMIB.setRevisions(
        ("2002-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIfMIBObjects_ObjectIdentity = ObjectIdentity
rsIfMIBObjects = _RsIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1)
)
_RsIfStatsTable_Object = MibTable
rsIfStatsTable = _RsIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1)
)
if mibBuilder.loadTexts:
    rsIfStatsTable.setStatus("current")
_RsIfStatsEntry_Object = MibTableRow
rsIfStatsEntry = _RsIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1)
)
rsIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsIfStatsEntry.setStatus("current")


class _RsIfStatsCapability_Type(Bits):
    """Custom type rsIfStatsCapability based on Bits"""
    namedValues = NamedValues(
        *(("ifDownTransitions", 3),
          ("ifInBridgedOctets", 5),
          ("ifInCorrelatedLayer1Errors", 4),
          ("ifInInvalidMacEncap", 12),
          ("ifInIpTableMisses", 11),
          ("ifInL2TableMisses", 7),
          ("ifInLocalFrames", 6),
          ("ifInRoutedCpuPackets", 10),
          ("ifInRoutedOctets", 8),
          ("ifInRoutedSwitchedPackets", 9),
          ("ifInVlanTableDiscards", 13),
          ("ifOutBridgedOctets", 14),
          ("ifOutRoutedOctets", 15),
          ("ifOutVlanTableDiscards", 16),
          ("ifTotalDownTime", 1),
          ("ifTotalUpTime", 0),
          ("ifUpTransitions", 2))
    )

_RsIfStatsCapability_Type.__name__ = "Bits"
_RsIfStatsCapability_Object = MibTableColumn
rsIfStatsCapability = _RsIfStatsCapability_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 1),
    _RsIfStatsCapability_Type()
)
rsIfStatsCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfStatsCapability.setStatus("current")
_RsIfQueuePolicy_Type = RsQueuePolicy
_RsIfQueuePolicy_Object = MibTableColumn
rsIfQueuePolicy = _RsIfQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 2),
    _RsIfQueuePolicy_Type()
)
rsIfQueuePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfQueuePolicy.setStatus("current")
_RsIfMru_Type = Integer32
_RsIfMru_Object = MibTableColumn
rsIfMru = _RsIfMru_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 3),
    _RsIfMru_Type()
)
rsIfMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfMru.setStatus("current")
if mibBuilder.loadTexts:
    rsIfMru.setUnits("octets")
_RsIfForceEtherIIState_Type = TruthValue
_RsIfForceEtherIIState_Object = MibTableColumn
rsIfForceEtherIIState = _RsIfForceEtherIIState_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 4),
    _RsIfForceEtherIIState_Type()
)
rsIfForceEtherIIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfForceEtherIIState.setStatus("current")
_RsIfTotalUpTime_Type = Counter32
_RsIfTotalUpTime_Object = MibTableColumn
rsIfTotalUpTime = _RsIfTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 5),
    _RsIfTotalUpTime_Type()
)
rsIfTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfTotalUpTime.setStatus("current")
if mibBuilder.loadTexts:
    rsIfTotalUpTime.setUnits("seconds")
_RsIfTotalDownTime_Type = Counter32
_RsIfTotalDownTime_Object = MibTableColumn
rsIfTotalDownTime = _RsIfTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 6),
    _RsIfTotalDownTime_Type()
)
rsIfTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfTotalDownTime.setStatus("current")
if mibBuilder.loadTexts:
    rsIfTotalDownTime.setUnits("seconds")
_RsIfUpTransitions_Type = Counter32
_RsIfUpTransitions_Object = MibTableColumn
rsIfUpTransitions = _RsIfUpTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 7),
    _RsIfUpTransitions_Type()
)
rsIfUpTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfUpTransitions.setStatus("current")
_RsIfDownTransitions_Type = Counter32
_RsIfDownTransitions_Object = MibTableColumn
rsIfDownTransitions = _RsIfDownTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 8),
    _RsIfDownTransitions_Type()
)
rsIfDownTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfDownTransitions.setStatus("current")
_RsIfInCorrelatedLayer1Errors_Type = Counter32
_RsIfInCorrelatedLayer1Errors_Object = MibTableColumn
rsIfInCorrelatedLayer1Errors = _RsIfInCorrelatedLayer1Errors_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 9),
    _RsIfInCorrelatedLayer1Errors_Type()
)
rsIfInCorrelatedLayer1Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInCorrelatedLayer1Errors.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInCorrelatedLayer1Errors.setUnits("frames")
_RsIfInBridgedOctets_Type = Counter64
_RsIfInBridgedOctets_Object = MibTableColumn
rsIfInBridgedOctets = _RsIfInBridgedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 10),
    _RsIfInBridgedOctets_Type()
)
rsIfInBridgedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInBridgedOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInBridgedOctets.setUnits("octets")
_RsIfInLocalFrames_Type = Counter64
_RsIfInLocalFrames_Object = MibTableColumn
rsIfInLocalFrames = _RsIfInLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 11),
    _RsIfInLocalFrames_Type()
)
rsIfInLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInLocalFrames.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInLocalFrames.setUnits("frames")
_RsIfInL2TableMisses_Type = Counter64
_RsIfInL2TableMisses_Object = MibTableColumn
rsIfInL2TableMisses = _RsIfInL2TableMisses_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 12),
    _RsIfInL2TableMisses_Type()
)
rsIfInL2TableMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInL2TableMisses.setStatus("current")
_RsIfInRoutedOctets_Type = Counter64
_RsIfInRoutedOctets_Object = MibTableColumn
rsIfInRoutedOctets = _RsIfInRoutedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 13),
    _RsIfInRoutedOctets_Type()
)
rsIfInRoutedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInRoutedOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInRoutedOctets.setUnits("octets")
_RsIfInRoutedSwitchedPackets_Type = Counter64
_RsIfInRoutedSwitchedPackets_Object = MibTableColumn
rsIfInRoutedSwitchedPackets = _RsIfInRoutedSwitchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 14),
    _RsIfInRoutedSwitchedPackets_Type()
)
rsIfInRoutedSwitchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInRoutedSwitchedPackets.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInRoutedSwitchedPackets.setUnits("packets")
_RsIfInRoutedCpuPackets_Type = Counter64
_RsIfInRoutedCpuPackets_Object = MibTableColumn
rsIfInRoutedCpuPackets = _RsIfInRoutedCpuPackets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 15),
    _RsIfInRoutedCpuPackets_Type()
)
rsIfInRoutedCpuPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInRoutedCpuPackets.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInRoutedCpuPackets.setUnits("packets")
_RsIfInIpTableMisses_Type = Counter64
_RsIfInIpTableMisses_Object = MibTableColumn
rsIfInIpTableMisses = _RsIfInIpTableMisses_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 16),
    _RsIfInIpTableMisses_Type()
)
rsIfInIpTableMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInIpTableMisses.setStatus("current")
_RsIfInInvalidMacEncap_Type = Counter32
_RsIfInInvalidMacEncap_Object = MibTableColumn
rsIfInInvalidMacEncap = _RsIfInInvalidMacEncap_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 17),
    _RsIfInInvalidMacEncap_Type()
)
rsIfInInvalidMacEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInInvalidMacEncap.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInInvalidMacEncap.setUnits("frames")
_RsIfInVlanTableDiscards_Type = Counter32
_RsIfInVlanTableDiscards_Object = MibTableColumn
rsIfInVlanTableDiscards = _RsIfInVlanTableDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 18),
    _RsIfInVlanTableDiscards_Type()
)
rsIfInVlanTableDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInVlanTableDiscards.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInVlanTableDiscards.setUnits("frames")
_RsIfOutBridgedOctets_Type = Counter64
_RsIfOutBridgedOctets_Object = MibTableColumn
rsIfOutBridgedOctets = _RsIfOutBridgedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 19),
    _RsIfOutBridgedOctets_Type()
)
rsIfOutBridgedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutBridgedOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutBridgedOctets.setUnits("octets")
_RsIfOutRoutedOctets_Type = Counter64
_RsIfOutRoutedOctets_Object = MibTableColumn
rsIfOutRoutedOctets = _RsIfOutRoutedOctets_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 20),
    _RsIfOutRoutedOctets_Type()
)
rsIfOutRoutedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutRoutedOctets.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutRoutedOctets.setUnits("octets")
_RsIfOutVlanTableDiscards_Type = Counter32
_RsIfOutVlanTableDiscards_Object = MibTableColumn
rsIfOutVlanTableDiscards = _RsIfOutVlanTableDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 1, 1, 21),
    _RsIfOutVlanTableDiscards_Type()
)
rsIfOutVlanTableDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutVlanTableDiscards.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutVlanTableDiscards.setUnits("frames")
_RsIfGaugeTable_Object = MibTable
rsIfGaugeTable = _RsIfGaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2)
)
if mibBuilder.loadTexts:
    rsIfGaugeTable.setStatus("current")
_RsIfGaugeEntry_Object = MibTableRow
rsIfGaugeEntry = _RsIfGaugeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1)
)
rsIfGaugeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsIfGaugeEntry.setStatus("current")


class _RsIfGaugeCapability_Type(Bits):
    """Custom type rsIfGaugeCapability based on Bits"""
    namedValues = NamedValues(
        *(("ifInOneMinBitsPerSec", 0),
          ("ifInOneMinBroadcastPkts", 5),
          ("ifInOneMinMulticastPkts", 4),
          ("ifInOneMinPktsDiscards", 1),
          ("ifInOneMinPktsErrors", 2),
          ("ifInOneMinUnicastPkts", 3),
          ("ifOutOneMinBitsPerSec", 6),
          ("ifOutOneMinBroadcastPkts", 11),
          ("ifOutOneMinMulticastPkts", 10),
          ("ifOutOneMinPktsDiscards", 7),
          ("ifOutOneMinPktsErrors", 8),
          ("ifOutOneMinUnicastPkts", 9))
    )

_RsIfGaugeCapability_Type.__name__ = "Bits"
_RsIfGaugeCapability_Object = MibTableColumn
rsIfGaugeCapability = _RsIfGaugeCapability_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 1),
    _RsIfGaugeCapability_Type()
)
rsIfGaugeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfGaugeCapability.setStatus("current")
_RsIfInOneMinBitsPerSec_Type = Gauge32
_RsIfInOneMinBitsPerSec_Object = MibTableColumn
rsIfInOneMinBitsPerSec = _RsIfInOneMinBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 2),
    _RsIfInOneMinBitsPerSec_Type()
)
rsIfInOneMinBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInOneMinBitsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInOneMinBitsPerSec.setUnits("bits per second")
_RsIfInOneMinPktsDiscards_Type = Gauge32
_RsIfInOneMinPktsDiscards_Object = MibTableColumn
rsIfInOneMinPktsDiscards = _RsIfInOneMinPktsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 3),
    _RsIfInOneMinPktsDiscards_Type()
)
rsIfInOneMinPktsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInOneMinPktsDiscards.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInOneMinPktsDiscards.setUnits("packets")
_RsIfInOneMinPktsErrors_Type = Gauge32
_RsIfInOneMinPktsErrors_Object = MibTableColumn
rsIfInOneMinPktsErrors = _RsIfInOneMinPktsErrors_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 4),
    _RsIfInOneMinPktsErrors_Type()
)
rsIfInOneMinPktsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInOneMinPktsErrors.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInOneMinPktsErrors.setUnits("packets")
_RsIfInOneMinUnicastPkts_Type = Gauge32
_RsIfInOneMinUnicastPkts_Object = MibTableColumn
rsIfInOneMinUnicastPkts = _RsIfInOneMinUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 5),
    _RsIfInOneMinUnicastPkts_Type()
)
rsIfInOneMinUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInOneMinUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInOneMinUnicastPkts.setUnits("packets")
_RsIfInOneMinMulticastPkts_Type = Gauge32
_RsIfInOneMinMulticastPkts_Object = MibTableColumn
rsIfInOneMinMulticastPkts = _RsIfInOneMinMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 6),
    _RsIfInOneMinMulticastPkts_Type()
)
rsIfInOneMinMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInOneMinMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInOneMinMulticastPkts.setUnits("packets")
_RsIfInOneMinBroadcastPkts_Type = Gauge32
_RsIfInOneMinBroadcastPkts_Object = MibTableColumn
rsIfInOneMinBroadcastPkts = _RsIfInOneMinBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 7),
    _RsIfInOneMinBroadcastPkts_Type()
)
rsIfInOneMinBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInOneMinBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rsIfInOneMinBroadcastPkts.setUnits("packets")
_RsIfOutOneMinBitsPerSec_Type = Gauge32
_RsIfOutOneMinBitsPerSec_Object = MibTableColumn
rsIfOutOneMinBitsPerSec = _RsIfOutOneMinBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 8),
    _RsIfOutOneMinBitsPerSec_Type()
)
rsIfOutOneMinBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutOneMinBitsPerSec.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutOneMinBitsPerSec.setUnits("bits per second")
_RsIfOutOneMinPktsDiscards_Type = Gauge32
_RsIfOutOneMinPktsDiscards_Object = MibTableColumn
rsIfOutOneMinPktsDiscards = _RsIfOutOneMinPktsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 9),
    _RsIfOutOneMinPktsDiscards_Type()
)
rsIfOutOneMinPktsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutOneMinPktsDiscards.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutOneMinPktsDiscards.setUnits("packets")
_RsIfOutOneMinPktsErrors_Type = Gauge32
_RsIfOutOneMinPktsErrors_Object = MibTableColumn
rsIfOutOneMinPktsErrors = _RsIfOutOneMinPktsErrors_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 10),
    _RsIfOutOneMinPktsErrors_Type()
)
rsIfOutOneMinPktsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutOneMinPktsErrors.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutOneMinPktsErrors.setUnits("packets")
_RsIfOutOneMinUnicastPkts_Type = Gauge32
_RsIfOutOneMinUnicastPkts_Object = MibTableColumn
rsIfOutOneMinUnicastPkts = _RsIfOutOneMinUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 11),
    _RsIfOutOneMinUnicastPkts_Type()
)
rsIfOutOneMinUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutOneMinUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutOneMinUnicastPkts.setUnits("packets")
_RsIfOutOneMinMulticastPkts_Type = Gauge32
_RsIfOutOneMinMulticastPkts_Object = MibTableColumn
rsIfOutOneMinMulticastPkts = _RsIfOutOneMinMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 12),
    _RsIfOutOneMinMulticastPkts_Type()
)
rsIfOutOneMinMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutOneMinMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutOneMinMulticastPkts.setUnits("packets")
_RsIfOutOneMinBroadcastPkts_Type = Gauge32
_RsIfOutOneMinBroadcastPkts_Object = MibTableColumn
rsIfOutOneMinBroadcastPkts = _RsIfOutOneMinBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 1, 2, 1, 13),
    _RsIfOutOneMinBroadcastPkts_Type()
)
rsIfOutOneMinBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutOneMinBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    rsIfOutOneMinBroadcastPkts.setUnits("packets")
_RsIfConformance_ObjectIdentity = ObjectIdentity
rsIfConformance = _RsIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 2)
)
_RsIfCompliances_ObjectIdentity = ObjectIdentity
rsIfCompliances = _RsIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 1)
)
_RsIfGroups_ObjectIdentity = ObjectIdentity
rsIfGroups = _RsIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 2)
)

# Managed Objects groups

rsIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 2, 1)
)
rsIfStatsGroup.setObjects(
      *(("RIVERSTONE-IF-MIB", "rsIfStatsCapability"),
        ("RIVERSTONE-IF-MIB", "rsIfQueuePolicy"),
        ("RIVERSTONE-IF-MIB", "rsIfMru"),
        ("RIVERSTONE-IF-MIB", "rsIfForceEtherIIState"),
        ("RIVERSTONE-IF-MIB", "rsIfTotalUpTime"),
        ("RIVERSTONE-IF-MIB", "rsIfTotalDownTime"),
        ("RIVERSTONE-IF-MIB", "rsIfUpTransitions"),
        ("RIVERSTONE-IF-MIB", "rsIfDownTransitions"),
        ("RIVERSTONE-IF-MIB", "rsIfInCorrelatedLayer1Errors"),
        ("RIVERSTONE-IF-MIB", "rsIfInLocalFrames"),
        ("RIVERSTONE-IF-MIB", "rsIfInRoutedSwitchedPackets"),
        ("RIVERSTONE-IF-MIB", "rsIfInRoutedCpuPackets"),
        ("RIVERSTONE-IF-MIB", "rsIfInBridgedOctets"),
        ("RIVERSTONE-IF-MIB", "rsIfInRoutedOctets"),
        ("RIVERSTONE-IF-MIB", "rsIfInL2TableMisses"),
        ("RIVERSTONE-IF-MIB", "rsIfInIpTableMisses"),
        ("RIVERSTONE-IF-MIB", "rsIfInInvalidMacEncap"),
        ("RIVERSTONE-IF-MIB", "rsIfInVlanTableDiscards"),
        ("RIVERSTONE-IF-MIB", "rsIfOutBridgedOctets"),
        ("RIVERSTONE-IF-MIB", "rsIfOutRoutedOctets"),
        ("RIVERSTONE-IF-MIB", "rsIfOutVlanTableDiscards"))
)
if mibBuilder.loadTexts:
    rsIfStatsGroup.setStatus("current")

rsIfGaugeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 2, 2)
)
rsIfGaugeGroup.setObjects(
      *(("RIVERSTONE-IF-MIB", "rsIfGaugeCapability"),
        ("RIVERSTONE-IF-MIB", "rsIfInOneMinBitsPerSec"),
        ("RIVERSTONE-IF-MIB", "rsIfInOneMinPktsDiscards"),
        ("RIVERSTONE-IF-MIB", "rsIfInOneMinPktsErrors"),
        ("RIVERSTONE-IF-MIB", "rsIfInOneMinUnicastPkts"),
        ("RIVERSTONE-IF-MIB", "rsIfInOneMinMulticastPkts"),
        ("RIVERSTONE-IF-MIB", "rsIfInOneMinBroadcastPkts"),
        ("RIVERSTONE-IF-MIB", "rsIfOutOneMinBitsPerSec"),
        ("RIVERSTONE-IF-MIB", "rsIfOutOneMinPktsDiscards"),
        ("RIVERSTONE-IF-MIB", "rsIfOutOneMinPktsErrors"),
        ("RIVERSTONE-IF-MIB", "rsIfOutOneMinUnicastPkts"),
        ("RIVERSTONE-IF-MIB", "rsIfOutOneMinMulticastPkts"),
        ("RIVERSTONE-IF-MIB", "rsIfOutOneMinBroadcastPkts"))
)
if mibBuilder.loadTexts:
    rsIfGaugeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 60, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-IF-MIB",
    **{"rsIfMIB": rsIfMIB,
       "rsIfMIBObjects": rsIfMIBObjects,
       "rsIfStatsTable": rsIfStatsTable,
       "rsIfStatsEntry": rsIfStatsEntry,
       "rsIfStatsCapability": rsIfStatsCapability,
       "rsIfQueuePolicy": rsIfQueuePolicy,
       "rsIfMru": rsIfMru,
       "rsIfForceEtherIIState": rsIfForceEtherIIState,
       "rsIfTotalUpTime": rsIfTotalUpTime,
       "rsIfTotalDownTime": rsIfTotalDownTime,
       "rsIfUpTransitions": rsIfUpTransitions,
       "rsIfDownTransitions": rsIfDownTransitions,
       "rsIfInCorrelatedLayer1Errors": rsIfInCorrelatedLayer1Errors,
       "rsIfInBridgedOctets": rsIfInBridgedOctets,
       "rsIfInLocalFrames": rsIfInLocalFrames,
       "rsIfInL2TableMisses": rsIfInL2TableMisses,
       "rsIfInRoutedOctets": rsIfInRoutedOctets,
       "rsIfInRoutedSwitchedPackets": rsIfInRoutedSwitchedPackets,
       "rsIfInRoutedCpuPackets": rsIfInRoutedCpuPackets,
       "rsIfInIpTableMisses": rsIfInIpTableMisses,
       "rsIfInInvalidMacEncap": rsIfInInvalidMacEncap,
       "rsIfInVlanTableDiscards": rsIfInVlanTableDiscards,
       "rsIfOutBridgedOctets": rsIfOutBridgedOctets,
       "rsIfOutRoutedOctets": rsIfOutRoutedOctets,
       "rsIfOutVlanTableDiscards": rsIfOutVlanTableDiscards,
       "rsIfGaugeTable": rsIfGaugeTable,
       "rsIfGaugeEntry": rsIfGaugeEntry,
       "rsIfGaugeCapability": rsIfGaugeCapability,
       "rsIfInOneMinBitsPerSec": rsIfInOneMinBitsPerSec,
       "rsIfInOneMinPktsDiscards": rsIfInOneMinPktsDiscards,
       "rsIfInOneMinPktsErrors": rsIfInOneMinPktsErrors,
       "rsIfInOneMinUnicastPkts": rsIfInOneMinUnicastPkts,
       "rsIfInOneMinMulticastPkts": rsIfInOneMinMulticastPkts,
       "rsIfInOneMinBroadcastPkts": rsIfInOneMinBroadcastPkts,
       "rsIfOutOneMinBitsPerSec": rsIfOutOneMinBitsPerSec,
       "rsIfOutOneMinPktsDiscards": rsIfOutOneMinPktsDiscards,
       "rsIfOutOneMinPktsErrors": rsIfOutOneMinPktsErrors,
       "rsIfOutOneMinUnicastPkts": rsIfOutOneMinUnicastPkts,
       "rsIfOutOneMinMulticastPkts": rsIfOutOneMinMulticastPkts,
       "rsIfOutOneMinBroadcastPkts": rsIfOutOneMinBroadcastPkts,
       "rsIfConformance": rsIfConformance,
       "rsIfCompliances": rsIfCompliances,
       "rsIfCompliance": rsIfCompliance,
       "rsIfGroups": rsIfGroups,
       "rsIfStatsGroup": rsIfStatsGroup,
       "rsIfGaugeGroup": rsIfGaugeGroup}
)
