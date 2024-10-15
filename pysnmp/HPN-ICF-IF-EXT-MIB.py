# SNMP MIB module (HPN-ICF-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:32 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

hpnicfIfExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40)
)
hpnicfIfExt.setRevisions(
        ("2009-05-06 19:36",
         "2004-11-13 19:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfIfExtScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfIfExtScalarGroup = _HpnicfIfExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 1)
)
_HpnicfIfStatGlobalFlowInterval_Type = Integer32
_HpnicfIfStatGlobalFlowInterval_Object = MibScalar
hpnicfIfStatGlobalFlowInterval = _HpnicfIfStatGlobalFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 1, 1),
    _HpnicfIfStatGlobalFlowInterval_Type()
)
hpnicfIfStatGlobalFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfStatGlobalFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfIfStatGlobalFlowInterval.setUnits("seconds")
_HpnicfIfExtGroup_ObjectIdentity = ObjectIdentity
hpnicfIfExtGroup = _HpnicfIfExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2)
)
_HpnicfIfStat_ObjectIdentity = ObjectIdentity
hpnicfIfStat = _HpnicfIfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1)
)
_HpnicfIfStatScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfIfStatScalarGroup = _HpnicfIfStatScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 1)
)
_HpnicfIfStatTable_ObjectIdentity = ObjectIdentity
hpnicfIfStatTable = _HpnicfIfStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2)
)
_HpnicfIfFlowStatTable_Object = MibTable
hpnicfIfFlowStatTable = _HpnicfIfFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfFlowStatTable.setStatus("current")
_HpnicfIfFlowStatEntry_Object = MibTableRow
hpnicfIfFlowStatEntry = _HpnicfIfFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1)
)
hpnicfIfFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfFlowStatEntry.setStatus("current")
_HpnicfIfStatFlowInterval_Type = Integer32
_HpnicfIfStatFlowInterval_Object = MibTableColumn
hpnicfIfStatFlowInterval = _HpnicfIfStatFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 1),
    _HpnicfIfStatFlowInterval_Type()
)
hpnicfIfStatFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowInterval.setUnits("seconds")
_HpnicfIfStatFlowInBits_Type = Unsigned32
_HpnicfIfStatFlowInBits_Object = MibTableColumn
hpnicfIfStatFlowInBits = _HpnicfIfStatFlowInBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 2),
    _HpnicfIfStatFlowInBits_Type()
)
hpnicfIfStatFlowInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowInBits.setStatus("current")
_HpnicfIfStatFlowOutBits_Type = Unsigned32
_HpnicfIfStatFlowOutBits_Object = MibTableColumn
hpnicfIfStatFlowOutBits = _HpnicfIfStatFlowOutBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 3),
    _HpnicfIfStatFlowOutBits_Type()
)
hpnicfIfStatFlowOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowOutBits.setStatus("current")
_HpnicfIfStatFlowInPkts_Type = Unsigned32
_HpnicfIfStatFlowInPkts_Object = MibTableColumn
hpnicfIfStatFlowInPkts = _HpnicfIfStatFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 4),
    _HpnicfIfStatFlowInPkts_Type()
)
hpnicfIfStatFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowInPkts.setStatus("current")
_HpnicfIfStatFlowOutPkts_Type = Unsigned32
_HpnicfIfStatFlowOutPkts_Object = MibTableColumn
hpnicfIfStatFlowOutPkts = _HpnicfIfStatFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 5),
    _HpnicfIfStatFlowOutPkts_Type()
)
hpnicfIfStatFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowOutPkts.setStatus("current")
_HpnicfIfStatFlowInBytes_Type = Unsigned32
_HpnicfIfStatFlowInBytes_Object = MibTableColumn
hpnicfIfStatFlowInBytes = _HpnicfIfStatFlowInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 6),
    _HpnicfIfStatFlowInBytes_Type()
)
hpnicfIfStatFlowInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowInBytes.setStatus("current")
_HpnicfIfStatFlowOutBytes_Type = Unsigned32
_HpnicfIfStatFlowOutBytes_Object = MibTableColumn
hpnicfIfStatFlowOutBytes = _HpnicfIfStatFlowOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 1, 1, 7),
    _HpnicfIfStatFlowOutBytes_Type()
)
hpnicfIfStatFlowOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowOutBytes.setStatus("current")
_HpnicfIfSpeedStatTable_Object = MibTable
hpnicfIfSpeedStatTable = _HpnicfIfSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatTable.setStatus("current")
_HpnicfIfSpeedStatEntry_Object = MibTableRow
hpnicfIfSpeedStatEntry = _HpnicfIfSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2, 1)
)
hpnicfIfSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatEntry.setStatus("current")
_HpnicfIfSpeedStatInterval_Type = Integer32
_HpnicfIfSpeedStatInterval_Object = MibTableColumn
hpnicfIfSpeedStatInterval = _HpnicfIfSpeedStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2, 1, 1),
    _HpnicfIfSpeedStatInterval_Type()
)
hpnicfIfSpeedStatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatInterval.setUnits("seconds")
_HpnicfIfSpeedStatInPkts_Type = Unsigned32
_HpnicfIfSpeedStatInPkts_Object = MibTableColumn
hpnicfIfSpeedStatInPkts = _HpnicfIfSpeedStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2, 1, 2),
    _HpnicfIfSpeedStatInPkts_Type()
)
hpnicfIfSpeedStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatInPkts.setStatus("current")
_HpnicfIfSpeedStatOutPkts_Type = Unsigned32
_HpnicfIfSpeedStatOutPkts_Object = MibTableColumn
hpnicfIfSpeedStatOutPkts = _HpnicfIfSpeedStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2, 1, 3),
    _HpnicfIfSpeedStatOutPkts_Type()
)
hpnicfIfSpeedStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatOutPkts.setStatus("current")
_HpnicfIfSpeedStatInBytes_Type = Unsigned32
_HpnicfIfSpeedStatInBytes_Object = MibTableColumn
hpnicfIfSpeedStatInBytes = _HpnicfIfSpeedStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2, 1, 4),
    _HpnicfIfSpeedStatInBytes_Type()
)
hpnicfIfSpeedStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatInBytes.setStatus("current")
_HpnicfIfSpeedStatOutBytes_Type = Unsigned32
_HpnicfIfSpeedStatOutBytes_Object = MibTableColumn
hpnicfIfSpeedStatOutBytes = _HpnicfIfSpeedStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 2, 1, 5),
    _HpnicfIfSpeedStatOutBytes_Type()
)
hpnicfIfSpeedStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfSpeedStatOutBytes.setStatus("current")
_HpnicfIfHCFlowStatTable_Object = MibTable
hpnicfIfHCFlowStatTable = _HpnicfIfHCFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfHCFlowStatTable.setStatus("current")
_HpnicfIfHCFlowStatEntry_Object = MibTableRow
hpnicfIfHCFlowStatEntry = _HpnicfIfHCFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1)
)
hpnicfIfHCFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfHCFlowStatEntry.setStatus("current")
_HpnicfIfStatFlowHCInBits_Type = CounterBasedGauge64
_HpnicfIfStatFlowHCInBits_Object = MibTableColumn
hpnicfIfStatFlowHCInBits = _HpnicfIfStatFlowHCInBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1, 1),
    _HpnicfIfStatFlowHCInBits_Type()
)
hpnicfIfStatFlowHCInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowHCInBits.setStatus("current")
_HpnicfIfStatFlowHCOutBits_Type = CounterBasedGauge64
_HpnicfIfStatFlowHCOutBits_Object = MibTableColumn
hpnicfIfStatFlowHCOutBits = _HpnicfIfStatFlowHCOutBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1, 2),
    _HpnicfIfStatFlowHCOutBits_Type()
)
hpnicfIfStatFlowHCOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowHCOutBits.setStatus("current")
_HpnicfIfStatFlowHCInPkts_Type = CounterBasedGauge64
_HpnicfIfStatFlowHCInPkts_Object = MibTableColumn
hpnicfIfStatFlowHCInPkts = _HpnicfIfStatFlowHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1, 3),
    _HpnicfIfStatFlowHCInPkts_Type()
)
hpnicfIfStatFlowHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowHCInPkts.setStatus("current")
_HpnicfIfStatFlowHCOutPkts_Type = CounterBasedGauge64
_HpnicfIfStatFlowHCOutPkts_Object = MibTableColumn
hpnicfIfStatFlowHCOutPkts = _HpnicfIfStatFlowHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1, 4),
    _HpnicfIfStatFlowHCOutPkts_Type()
)
hpnicfIfStatFlowHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowHCOutPkts.setStatus("current")
_HpnicfIfStatFlowHCInBytes_Type = CounterBasedGauge64
_HpnicfIfStatFlowHCInBytes_Object = MibTableColumn
hpnicfIfStatFlowHCInBytes = _HpnicfIfStatFlowHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1, 5),
    _HpnicfIfStatFlowHCInBytes_Type()
)
hpnicfIfStatFlowHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowHCInBytes.setStatus("current")
_HpnicfIfStatFlowHCOutBytes_Type = CounterBasedGauge64
_HpnicfIfStatFlowHCOutBytes_Object = MibTableColumn
hpnicfIfStatFlowHCOutBytes = _HpnicfIfStatFlowHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 1, 2, 3, 1, 6),
    _HpnicfIfStatFlowHCOutBytes_Type()
)
hpnicfIfStatFlowHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatFlowHCOutBytes.setStatus("current")
_HpnicfIfControl_ObjectIdentity = ObjectIdentity
hpnicfIfControl = _HpnicfIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2)
)
_HpnicfRTParentIfTable_Object = MibTable
hpnicfRTParentIfTable = _HpnicfRTParentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfRTParentIfTable.setStatus("current")
_HpnicfRTParentIfEntry_Object = MibTableRow
hpnicfRTParentIfEntry = _HpnicfRTParentIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 1, 1)
)
hpnicfRTParentIfEntry.setIndexNames(
    (0, "HPN-ICF-IF-EXT-MIB", "hpnicfRTParentIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRTParentIfEntry.setStatus("current")
_HpnicfRTParentIfIndex_Type = Integer32
_HpnicfRTParentIfIndex_Object = MibTableColumn
hpnicfRTParentIfIndex = _HpnicfRTParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 1, 1, 1),
    _HpnicfRTParentIfIndex_Type()
)
hpnicfRTParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRTParentIfIndex.setStatus("current")
_HpnicfRTMinSubIfOrdinal_Type = Integer32
_HpnicfRTMinSubIfOrdinal_Object = MibTableColumn
hpnicfRTMinSubIfOrdinal = _HpnicfRTMinSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 1, 1, 2),
    _HpnicfRTMinSubIfOrdinal_Type()
)
hpnicfRTMinSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTMinSubIfOrdinal.setStatus("current")
_HpnicfRTMaxSubIfOrdinal_Type = Integer32
_HpnicfRTMaxSubIfOrdinal_Object = MibTableColumn
hpnicfRTMaxSubIfOrdinal = _HpnicfRTMaxSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 1, 1, 3),
    _HpnicfRTMaxSubIfOrdinal_Type()
)
hpnicfRTMaxSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTMaxSubIfOrdinal.setStatus("current")
_HpnicfRTSubIfTable_Object = MibTable
hpnicfRTSubIfTable = _HpnicfRTSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfRTSubIfTable.setStatus("current")
_HpnicfRTSubIfEntry_Object = MibTableRow
hpnicfRTSubIfEntry = _HpnicfRTSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2, 1)
)
hpnicfRTSubIfEntry.setIndexNames(
    (0, "HPN-ICF-IF-EXT-MIB", "hpnicfRTSubIfParentIfIndex"),
    (0, "HPN-ICF-IF-EXT-MIB", "hpnicfRTSubIfOrdinal"),
)
if mibBuilder.loadTexts:
    hpnicfRTSubIfEntry.setStatus("current")
_HpnicfRTSubIfParentIfIndex_Type = Integer32
_HpnicfRTSubIfParentIfIndex_Object = MibTableColumn
hpnicfRTSubIfParentIfIndex = _HpnicfRTSubIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2, 1, 1),
    _HpnicfRTSubIfParentIfIndex_Type()
)
hpnicfRTSubIfParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRTSubIfParentIfIndex.setStatus("current")
_HpnicfRTSubIfOrdinal_Type = Integer32
_HpnicfRTSubIfOrdinal_Object = MibTableColumn
hpnicfRTSubIfOrdinal = _HpnicfRTSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2, 1, 2),
    _HpnicfRTSubIfOrdinal_Type()
)
hpnicfRTSubIfOrdinal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRTSubIfOrdinal.setStatus("current")
_HpnicfRTSubIfSubIfIndex_Type = Integer32
_HpnicfRTSubIfSubIfIndex_Object = MibTableColumn
hpnicfRTSubIfSubIfIndex = _HpnicfRTSubIfSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2, 1, 3),
    _HpnicfRTSubIfSubIfIndex_Type()
)
hpnicfRTSubIfSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTSubIfSubIfIndex.setStatus("current")


class _HpnicfRTSubIfSubIfDesc_Type(DisplayString):
    """Custom type hpnicfRTSubIfSubIfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfRTSubIfSubIfDesc_Type.__name__ = "DisplayString"
_HpnicfRTSubIfSubIfDesc_Object = MibTableColumn
hpnicfRTSubIfSubIfDesc = _HpnicfRTSubIfSubIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2, 1, 4),
    _HpnicfRTSubIfSubIfDesc_Type()
)
hpnicfRTSubIfSubIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRTSubIfSubIfDesc.setStatus("current")
_HpnicfRTSubIfRowStatus_Type = RowStatus
_HpnicfRTSubIfRowStatus_Object = MibTableColumn
hpnicfRTSubIfRowStatus = _HpnicfRTSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 2, 1, 5),
    _HpnicfRTSubIfRowStatus_Type()
)
hpnicfRTSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRTSubIfRowStatus.setStatus("current")
_HpnicfIfLinkModeTable_Object = MibTable
hpnicfIfLinkModeTable = _HpnicfIfLinkModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfLinkModeTable.setStatus("current")
_HpnicfIfLinkModeEntry_Object = MibTableRow
hpnicfIfLinkModeEntry = _HpnicfIfLinkModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 3, 1)
)
hpnicfIfLinkModeEntry.setIndexNames(
    (0, "HPN-ICF-IF-EXT-MIB", "hpnicfIfLinkModeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfLinkModeEntry.setStatus("current")
_HpnicfIfLinkModeIndex_Type = Integer32
_HpnicfIfLinkModeIndex_Object = MibTableColumn
hpnicfIfLinkModeIndex = _HpnicfIfLinkModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 3, 1, 1),
    _HpnicfIfLinkModeIndex_Type()
)
hpnicfIfLinkModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfLinkModeIndex.setStatus("current")


class _HpnicfIfLinkMode_Type(Integer32):
    """Custom type hpnicfIfLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgeMode", 1),
          ("routeMode", 2))
    )


_HpnicfIfLinkMode_Type.__name__ = "Integer32"
_HpnicfIfLinkMode_Object = MibTableColumn
hpnicfIfLinkMode = _HpnicfIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 3, 1, 2),
    _HpnicfIfLinkMode_Type()
)
hpnicfIfLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfLinkMode.setStatus("current")
_HpnicfIfLinkModeSwitchSupport_Type = TruthValue
_HpnicfIfLinkModeSwitchSupport_Object = MibTableColumn
hpnicfIfLinkModeSwitchSupport = _HpnicfIfLinkModeSwitchSupport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 2, 3, 1, 3),
    _HpnicfIfLinkModeSwitchSupport_Type()
)
hpnicfIfLinkModeSwitchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfLinkModeSwitchSupport.setStatus("current")
_HpnicfIfInterfaces_ObjectIdentity = ObjectIdentity
hpnicfIfInterfaces = _HpnicfIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3)
)
_HpnicfIfPhysicalNumber_Type = Integer32
_HpnicfIfPhysicalNumber_Object = MibScalar
hpnicfIfPhysicalNumber = _HpnicfIfPhysicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 1),
    _HpnicfIfPhysicalNumber_Type()
)
hpnicfIfPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfPhysicalNumber.setStatus("current")
_HpnicfIfTable_Object = MibTable
hpnicfIfTable = _HpnicfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfTable.setStatus("current")
_HpnicfIfEntry_Object = MibTableRow
hpnicfIfEntry = _HpnicfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1)
)
hpnicfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfEntry.setStatus("current")
_HpnicfIfUpDownTimes_Type = Integer32
_HpnicfIfUpDownTimes_Object = MibTableColumn
hpnicfIfUpDownTimes = _HpnicfIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 1),
    _HpnicfIfUpDownTimes_Type()
)
hpnicfIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfUpDownTimes.setStatus("current")
_HpnicfIfMtu_Type = Integer32
_HpnicfIfMtu_Object = MibTableColumn
hpnicfIfMtu = _HpnicfIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 2),
    _HpnicfIfMtu_Type()
)
hpnicfIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfMtu.setStatus("current")


class _HpnicfIfBandwidthRate_Type(Integer32):
    """Custom type hpnicfIfBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfIfBandwidthRate_Type.__name__ = "Integer32"
_HpnicfIfBandwidthRate_Object = MibTableColumn
hpnicfIfBandwidthRate = _HpnicfIfBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 3),
    _HpnicfIfBandwidthRate_Type()
)
hpnicfIfBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfBandwidthRate.setStatus("current")


class _HpnicfIfDiscardPktRate_Type(Integer32):
    """Custom type hpnicfIfDiscardPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfIfDiscardPktRate_Type.__name__ = "Integer32"
_HpnicfIfDiscardPktRate_Object = MibTableColumn
hpnicfIfDiscardPktRate = _HpnicfIfDiscardPktRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 4),
    _HpnicfIfDiscardPktRate_Type()
)
hpnicfIfDiscardPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfDiscardPktRate.setStatus("current")
_HpnicfIfStatusKeepTime_Type = TimeTicks
_HpnicfIfStatusKeepTime_Object = MibTableColumn
hpnicfIfStatusKeepTime = _HpnicfIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 5),
    _HpnicfIfStatusKeepTime_Type()
)
hpnicfIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfStatusKeepTime.setStatus("current")
_HpnicfIfInNUcastPkts_Type = Counter64
_HpnicfIfInNUcastPkts_Object = MibTableColumn
hpnicfIfInNUcastPkts = _HpnicfIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 6),
    _HpnicfIfInNUcastPkts_Type()
)
hpnicfIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfInNUcastPkts.setStatus("current")
_HpnicfIfOutNUcastPkts_Type = Counter64
_HpnicfIfOutNUcastPkts_Object = MibTableColumn
hpnicfIfOutNUcastPkts = _HpnicfIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 7),
    _HpnicfIfOutNUcastPkts_Type()
)
hpnicfIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfOutNUcastPkts.setStatus("current")
_HpnicfIfIsPoe_Type = TruthValue
_HpnicfIfIsPoe_Object = MibTableColumn
hpnicfIfIsPoe = _HpnicfIfIsPoe_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 8),
    _HpnicfIfIsPoe_Type()
)
hpnicfIfIsPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfIsPoe.setStatus("current")


class _HpnicfIfOperStatus_Type(Integer32):
    """Custom type hpnicfIfOperStatus based on Integer32"""
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
        *(("admindown", 4),
          ("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_HpnicfIfOperStatus_Type.__name__ = "Integer32"
_HpnicfIfOperStatus_Object = MibTableColumn
hpnicfIfOperStatus = _HpnicfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 9),
    _HpnicfIfOperStatus_Type()
)
hpnicfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfOperStatus.setStatus("current")
_HpnicfIfDownTimes_Type = Integer32
_HpnicfIfDownTimes_Object = MibTableColumn
hpnicfIfDownTimes = _HpnicfIfDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 2, 3, 2, 1, 10),
    _HpnicfIfDownTimes_Type()
)
hpnicfIfDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfDownTimes.setStatus("current")
_HpnicfIfExtTrap_ObjectIdentity = ObjectIdentity
hpnicfIfExtTrap = _HpnicfIfExtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3)
)
_HpnicfIfExtTrapPrex_ObjectIdentity = ObjectIdentity
hpnicfIfExtTrapPrex = _HpnicfIfExtTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 0)
)
_HpnicfIfExtTrapObject_ObjectIdentity = ObjectIdentity
hpnicfIfExtTrapObject = _HpnicfIfExtTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 1)
)
_HpnicfIfExtTrapCfgTable_Object = MibTable
hpnicfIfExtTrapCfgTable = _HpnicfIfExtTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfExtTrapCfgTable.setStatus("current")
_HpnicfIfExtTrapCfgEntry_Object = MibTableRow
hpnicfIfExtTrapCfgEntry = _HpnicfIfExtTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 1, 1, 1)
)
hpnicfIfExtTrapCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfExtTrapCfgEntry.setStatus("current")


class _HpnicfIfBandwidthUpperLimit_Type(Integer32):
    """Custom type hpnicfIfBandwidthUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfIfBandwidthUpperLimit_Type.__name__ = "Integer32"
_HpnicfIfBandwidthUpperLimit_Object = MibTableColumn
hpnicfIfBandwidthUpperLimit = _HpnicfIfBandwidthUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 1, 1, 1, 1),
    _HpnicfIfBandwidthUpperLimit_Type()
)
hpnicfIfBandwidthUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfBandwidthUpperLimit.setStatus("current")


class _HpnicfIfDiscardPktRateUpperLimit_Type(Integer32):
    """Custom type hpnicfIfDiscardPktRateUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfIfDiscardPktRateUpperLimit_Type.__name__ = "Integer32"
_HpnicfIfDiscardPktRateUpperLimit_Object = MibTableColumn
hpnicfIfDiscardPktRateUpperLimit = _HpnicfIfDiscardPktRateUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 1, 1, 1, 2),
    _HpnicfIfDiscardPktRateUpperLimit_Type()
)
hpnicfIfDiscardPktRateUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfDiscardPktRateUpperLimit.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfIfBandwidthUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 0, 1)
)
hpnicfIfBandwidthUsageHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HPN-ICF-IF-EXT-MIB", "hpnicfIfBandwidthRate"),
        ("HPN-ICF-IF-EXT-MIB", "hpnicfIfBandwidthUpperLimit"))
)
if mibBuilder.loadTexts:
    hpnicfIfBandwidthUsageHigh.setStatus(
        "current"
    )

hpnicfIfDiscardPktRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40, 3, 0, 2)
)
hpnicfIfDiscardPktRateHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HPN-ICF-IF-EXT-MIB", "hpnicfIfDiscardPktRate"),
        ("HPN-ICF-IF-EXT-MIB", "hpnicfIfDiscardPktRateUpperLimit"))
)
if mibBuilder.loadTexts:
    hpnicfIfDiscardPktRateHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IF-EXT-MIB",
    **{"hpnicfIfExt": hpnicfIfExt,
       "hpnicfIfExtScalarGroup": hpnicfIfExtScalarGroup,
       "hpnicfIfStatGlobalFlowInterval": hpnicfIfStatGlobalFlowInterval,
       "hpnicfIfExtGroup": hpnicfIfExtGroup,
       "hpnicfIfStat": hpnicfIfStat,
       "hpnicfIfStatScalarGroup": hpnicfIfStatScalarGroup,
       "hpnicfIfStatTable": hpnicfIfStatTable,
       "hpnicfIfFlowStatTable": hpnicfIfFlowStatTable,
       "hpnicfIfFlowStatEntry": hpnicfIfFlowStatEntry,
       "hpnicfIfStatFlowInterval": hpnicfIfStatFlowInterval,
       "hpnicfIfStatFlowInBits": hpnicfIfStatFlowInBits,
       "hpnicfIfStatFlowOutBits": hpnicfIfStatFlowOutBits,
       "hpnicfIfStatFlowInPkts": hpnicfIfStatFlowInPkts,
       "hpnicfIfStatFlowOutPkts": hpnicfIfStatFlowOutPkts,
       "hpnicfIfStatFlowInBytes": hpnicfIfStatFlowInBytes,
       "hpnicfIfStatFlowOutBytes": hpnicfIfStatFlowOutBytes,
       "hpnicfIfSpeedStatTable": hpnicfIfSpeedStatTable,
       "hpnicfIfSpeedStatEntry": hpnicfIfSpeedStatEntry,
       "hpnicfIfSpeedStatInterval": hpnicfIfSpeedStatInterval,
       "hpnicfIfSpeedStatInPkts": hpnicfIfSpeedStatInPkts,
       "hpnicfIfSpeedStatOutPkts": hpnicfIfSpeedStatOutPkts,
       "hpnicfIfSpeedStatInBytes": hpnicfIfSpeedStatInBytes,
       "hpnicfIfSpeedStatOutBytes": hpnicfIfSpeedStatOutBytes,
       "hpnicfIfHCFlowStatTable": hpnicfIfHCFlowStatTable,
       "hpnicfIfHCFlowStatEntry": hpnicfIfHCFlowStatEntry,
       "hpnicfIfStatFlowHCInBits": hpnicfIfStatFlowHCInBits,
       "hpnicfIfStatFlowHCOutBits": hpnicfIfStatFlowHCOutBits,
       "hpnicfIfStatFlowHCInPkts": hpnicfIfStatFlowHCInPkts,
       "hpnicfIfStatFlowHCOutPkts": hpnicfIfStatFlowHCOutPkts,
       "hpnicfIfStatFlowHCInBytes": hpnicfIfStatFlowHCInBytes,
       "hpnicfIfStatFlowHCOutBytes": hpnicfIfStatFlowHCOutBytes,
       "hpnicfIfControl": hpnicfIfControl,
       "hpnicfRTParentIfTable": hpnicfRTParentIfTable,
       "hpnicfRTParentIfEntry": hpnicfRTParentIfEntry,
       "hpnicfRTParentIfIndex": hpnicfRTParentIfIndex,
       "hpnicfRTMinSubIfOrdinal": hpnicfRTMinSubIfOrdinal,
       "hpnicfRTMaxSubIfOrdinal": hpnicfRTMaxSubIfOrdinal,
       "hpnicfRTSubIfTable": hpnicfRTSubIfTable,
       "hpnicfRTSubIfEntry": hpnicfRTSubIfEntry,
       "hpnicfRTSubIfParentIfIndex": hpnicfRTSubIfParentIfIndex,
       "hpnicfRTSubIfOrdinal": hpnicfRTSubIfOrdinal,
       "hpnicfRTSubIfSubIfIndex": hpnicfRTSubIfSubIfIndex,
       "hpnicfRTSubIfSubIfDesc": hpnicfRTSubIfSubIfDesc,
       "hpnicfRTSubIfRowStatus": hpnicfRTSubIfRowStatus,
       "hpnicfIfLinkModeTable": hpnicfIfLinkModeTable,
       "hpnicfIfLinkModeEntry": hpnicfIfLinkModeEntry,
       "hpnicfIfLinkModeIndex": hpnicfIfLinkModeIndex,
       "hpnicfIfLinkMode": hpnicfIfLinkMode,
       "hpnicfIfLinkModeSwitchSupport": hpnicfIfLinkModeSwitchSupport,
       "hpnicfIfInterfaces": hpnicfIfInterfaces,
       "hpnicfIfPhysicalNumber": hpnicfIfPhysicalNumber,
       "hpnicfIfTable": hpnicfIfTable,
       "hpnicfIfEntry": hpnicfIfEntry,
       "hpnicfIfUpDownTimes": hpnicfIfUpDownTimes,
       "hpnicfIfMtu": hpnicfIfMtu,
       "hpnicfIfBandwidthRate": hpnicfIfBandwidthRate,
       "hpnicfIfDiscardPktRate": hpnicfIfDiscardPktRate,
       "hpnicfIfStatusKeepTime": hpnicfIfStatusKeepTime,
       "hpnicfIfInNUcastPkts": hpnicfIfInNUcastPkts,
       "hpnicfIfOutNUcastPkts": hpnicfIfOutNUcastPkts,
       "hpnicfIfIsPoe": hpnicfIfIsPoe,
       "hpnicfIfOperStatus": hpnicfIfOperStatus,
       "hpnicfIfDownTimes": hpnicfIfDownTimes,
       "hpnicfIfExtTrap": hpnicfIfExtTrap,
       "hpnicfIfExtTrapPrex": hpnicfIfExtTrapPrex,
       "hpnicfIfBandwidthUsageHigh": hpnicfIfBandwidthUsageHigh,
       "hpnicfIfDiscardPktRateHigh": hpnicfIfDiscardPktRateHigh,
       "hpnicfIfExtTrapObject": hpnicfIfExtTrapObject,
       "hpnicfIfExtTrapCfgTable": hpnicfIfExtTrapCfgTable,
       "hpnicfIfExtTrapCfgEntry": hpnicfIfExtTrapCfgEntry,
       "hpnicfIfBandwidthUpperLimit": hpnicfIfBandwidthUpperLimit,
       "hpnicfIfDiscardPktRateUpperLimit": hpnicfIfDiscardPktRateUpperLimit}
)
