# SNMP MIB module (H3C-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:39 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cIfExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40)
)
h3cIfExt.setRevisions(
        ("2009-05-06 19:36",
         "2004-11-13 19:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cIfExtScalarGroup_ObjectIdentity = ObjectIdentity
h3cIfExtScalarGroup = _H3cIfExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1)
)
_H3cIfStatGlobalFlowInterval_Type = Integer32
_H3cIfStatGlobalFlowInterval_Object = MibScalar
h3cIfStatGlobalFlowInterval = _H3cIfStatGlobalFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1, 1),
    _H3cIfStatGlobalFlowInterval_Type()
)
h3cIfStatGlobalFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfStatGlobalFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfStatGlobalFlowInterval.setUnits("seconds")
_H3cIfExtGroup_ObjectIdentity = ObjectIdentity
h3cIfExtGroup = _H3cIfExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2)
)
_H3cIfStat_ObjectIdentity = ObjectIdentity
h3cIfStat = _H3cIfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1)
)
_H3cIfStatScalarGroup_ObjectIdentity = ObjectIdentity
h3cIfStatScalarGroup = _H3cIfStatScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 1)
)
_H3cIfStatTable_ObjectIdentity = ObjectIdentity
h3cIfStatTable = _H3cIfStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2)
)
_H3cIfFlowStatTable_Object = MibTable
h3cIfFlowStatTable = _H3cIfFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfFlowStatTable.setStatus("current")
_H3cIfStatEntry_Object = MibTableRow
h3cIfStatEntry = _H3cIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1)
)
h3cIfStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfStatEntry.setStatus("current")
_H3cIfStatFlowInterval_Type = Integer32
_H3cIfStatFlowInterval_Object = MibTableColumn
h3cIfStatFlowInterval = _H3cIfStatFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 1),
    _H3cIfStatFlowInterval_Type()
)
h3cIfStatFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfStatFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfStatFlowInterval.setUnits("seconds")
_H3cIfStatFlowInBits_Type = Unsigned32
_H3cIfStatFlowInBits_Object = MibTableColumn
h3cIfStatFlowInBits = _H3cIfStatFlowInBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 2),
    _H3cIfStatFlowInBits_Type()
)
h3cIfStatFlowInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowInBits.setStatus("current")
_H3cIfStatFlowOutBits_Type = Unsigned32
_H3cIfStatFlowOutBits_Object = MibTableColumn
h3cIfStatFlowOutBits = _H3cIfStatFlowOutBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 3),
    _H3cIfStatFlowOutBits_Type()
)
h3cIfStatFlowOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowOutBits.setStatus("current")
_H3cIfStatFlowInPkts_Type = Unsigned32
_H3cIfStatFlowInPkts_Object = MibTableColumn
h3cIfStatFlowInPkts = _H3cIfStatFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 4),
    _H3cIfStatFlowInPkts_Type()
)
h3cIfStatFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowInPkts.setStatus("current")
_H3cIfStatFlowOutPkts_Type = Unsigned32
_H3cIfStatFlowOutPkts_Object = MibTableColumn
h3cIfStatFlowOutPkts = _H3cIfStatFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 5),
    _H3cIfStatFlowOutPkts_Type()
)
h3cIfStatFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowOutPkts.setStatus("current")
_H3cIfStatFlowInBytes_Type = Unsigned32
_H3cIfStatFlowInBytes_Object = MibTableColumn
h3cIfStatFlowInBytes = _H3cIfStatFlowInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 6),
    _H3cIfStatFlowInBytes_Type()
)
h3cIfStatFlowInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowInBytes.setStatus("current")
_H3cIfStatFlowOutBytes_Type = Unsigned32
_H3cIfStatFlowOutBytes_Object = MibTableColumn
h3cIfStatFlowOutBytes = _H3cIfStatFlowOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 7),
    _H3cIfStatFlowOutBytes_Type()
)
h3cIfStatFlowOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatFlowOutBytes.setStatus("current")
_H3cIfSpeedStatTable_Object = MibTable
h3cIfSpeedStatTable = _H3cIfSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIfSpeedStatTable.setStatus("current")
_H3cIfSpeedStatEntry_Object = MibTableRow
h3cIfSpeedStatEntry = _H3cIfSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1)
)
h3cIfSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfSpeedStatEntry.setStatus("current")
_H3cIfSpeedStatInterval_Type = Integer32
_H3cIfSpeedStatInterval_Object = MibTableColumn
h3cIfSpeedStatInterval = _H3cIfSpeedStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 1),
    _H3cIfSpeedStatInterval_Type()
)
h3cIfSpeedStatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInterval.setUnits("seconds")
_H3cIfSpeedStatInPkts_Type = Unsigned32
_H3cIfSpeedStatInPkts_Object = MibTableColumn
h3cIfSpeedStatInPkts = _H3cIfSpeedStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 2),
    _H3cIfSpeedStatInPkts_Type()
)
h3cIfSpeedStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInPkts.setStatus("current")
_H3cIfSpeedStatOutPkts_Type = Unsigned32
_H3cIfSpeedStatOutPkts_Object = MibTableColumn
h3cIfSpeedStatOutPkts = _H3cIfSpeedStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 3),
    _H3cIfSpeedStatOutPkts_Type()
)
h3cIfSpeedStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatOutPkts.setStatus("current")
_H3cIfSpeedStatInBytes_Type = Unsigned32
_H3cIfSpeedStatInBytes_Object = MibTableColumn
h3cIfSpeedStatInBytes = _H3cIfSpeedStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 4),
    _H3cIfSpeedStatInBytes_Type()
)
h3cIfSpeedStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatInBytes.setStatus("current")
_H3cIfSpeedStatOutBytes_Type = Unsigned32
_H3cIfSpeedStatOutBytes_Object = MibTableColumn
h3cIfSpeedStatOutBytes = _H3cIfSpeedStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 5),
    _H3cIfSpeedStatOutBytes_Type()
)
h3cIfSpeedStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfSpeedStatOutBytes.setStatus("current")
_H3cIfControl_ObjectIdentity = ObjectIdentity
h3cIfControl = _H3cIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2)
)
_H3cRTParentIfTable_Object = MibTable
h3cRTParentIfTable = _H3cRTParentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cRTParentIfTable.setStatus("current")
_H3cRTParentIfEntry_Object = MibTableRow
h3cRTParentIfEntry = _H3cRTParentIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1)
)
h3cRTParentIfEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cRTParentIfIndex"),
)
if mibBuilder.loadTexts:
    h3cRTParentIfEntry.setStatus("current")
_H3cRTParentIfIndex_Type = Integer32
_H3cRTParentIfIndex_Object = MibTableColumn
h3cRTParentIfIndex = _H3cRTParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 1),
    _H3cRTParentIfIndex_Type()
)
h3cRTParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRTParentIfIndex.setStatus("current")
_H3cRTMinSubIfOrdinal_Type = Integer32
_H3cRTMinSubIfOrdinal_Object = MibTableColumn
h3cRTMinSubIfOrdinal = _H3cRTMinSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 2),
    _H3cRTMinSubIfOrdinal_Type()
)
h3cRTMinSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTMinSubIfOrdinal.setStatus("current")
_H3cRTMaxSubIfOrdinal_Type = Integer32
_H3cRTMaxSubIfOrdinal_Object = MibTableColumn
h3cRTMaxSubIfOrdinal = _H3cRTMaxSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 3),
    _H3cRTMaxSubIfOrdinal_Type()
)
h3cRTMaxSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTMaxSubIfOrdinal.setStatus("current")
_H3cRTSubIfTable_Object = MibTable
h3cRTSubIfTable = _H3cRTSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2)
)
if mibBuilder.loadTexts:
    h3cRTSubIfTable.setStatus("current")
_H3cRTSubIfEntry_Object = MibTableRow
h3cRTSubIfEntry = _H3cRTSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1)
)
h3cRTSubIfEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cRTSubIfParentIfIndex"),
    (0, "H3C-IF-EXT-MIB", "h3cRTSubIfOrdinal"),
)
if mibBuilder.loadTexts:
    h3cRTSubIfEntry.setStatus("current")
_H3cRTSubIfParentIfIndex_Type = Integer32
_H3cRTSubIfParentIfIndex_Object = MibTableColumn
h3cRTSubIfParentIfIndex = _H3cRTSubIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 1),
    _H3cRTSubIfParentIfIndex_Type()
)
h3cRTSubIfParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRTSubIfParentIfIndex.setStatus("current")
_H3cRTSubIfOrdinal_Type = Integer32
_H3cRTSubIfOrdinal_Object = MibTableColumn
h3cRTSubIfOrdinal = _H3cRTSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 2),
    _H3cRTSubIfOrdinal_Type()
)
h3cRTSubIfOrdinal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cRTSubIfOrdinal.setStatus("current")
_H3cRTSubIfSubIfIndex_Type = Integer32
_H3cRTSubIfSubIfIndex_Object = MibTableColumn
h3cRTSubIfSubIfIndex = _H3cRTSubIfSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 3),
    _H3cRTSubIfSubIfIndex_Type()
)
h3cRTSubIfSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTSubIfSubIfIndex.setStatus("current")


class _H3cRTSubIfSubIfDesc_Type(DisplayString):
    """Custom type h3cRTSubIfSubIfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cRTSubIfSubIfDesc_Type.__name__ = "DisplayString"
_H3cRTSubIfSubIfDesc_Object = MibTableColumn
h3cRTSubIfSubIfDesc = _H3cRTSubIfSubIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 4),
    _H3cRTSubIfSubIfDesc_Type()
)
h3cRTSubIfSubIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cRTSubIfSubIfDesc.setStatus("current")
_H3cRTSubIfRowStatus_Type = RowStatus
_H3cRTSubIfRowStatus_Object = MibTableColumn
h3cRTSubIfRowStatus = _H3cRTSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 5),
    _H3cRTSubIfRowStatus_Type()
)
h3cRTSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cRTSubIfRowStatus.setStatus("current")
_H3cIfLinkModeTable_Object = MibTable
h3cIfLinkModeTable = _H3cIfLinkModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3)
)
if mibBuilder.loadTexts:
    h3cIfLinkModeTable.setStatus("current")
_H3cIfLinkModeEntry_Object = MibTableRow
h3cIfLinkModeEntry = _H3cIfLinkModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1)
)
h3cIfLinkModeEntry.setIndexNames(
    (0, "H3C-IF-EXT-MIB", "h3cIfLinkModeIndex"),
)
if mibBuilder.loadTexts:
    h3cIfLinkModeEntry.setStatus("current")
_H3cIfLinkModeIndex_Type = Integer32
_H3cIfLinkModeIndex_Object = MibTableColumn
h3cIfLinkModeIndex = _H3cIfLinkModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 1),
    _H3cIfLinkModeIndex_Type()
)
h3cIfLinkModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfLinkModeIndex.setStatus("current")


class _H3cIfLinkMode_Type(Integer32):
    """Custom type h3cIfLinkMode based on Integer32"""
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


_H3cIfLinkMode_Type.__name__ = "Integer32"
_H3cIfLinkMode_Object = MibTableColumn
h3cIfLinkMode = _H3cIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 2),
    _H3cIfLinkMode_Type()
)
h3cIfLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfLinkMode.setStatus("current")
_H3cIfLinkModeSwitchSupport_Type = TruthValue
_H3cIfLinkModeSwitchSupport_Object = MibTableColumn
h3cIfLinkModeSwitchSupport = _H3cIfLinkModeSwitchSupport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 3),
    _H3cIfLinkModeSwitchSupport_Type()
)
h3cIfLinkModeSwitchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfLinkModeSwitchSupport.setStatus("current")
_H3cIfInterfaces_ObjectIdentity = ObjectIdentity
h3cIfInterfaces = _H3cIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3)
)
_H3cIfPhysicalNumber_Type = Integer32
_H3cIfPhysicalNumber_Object = MibScalar
h3cIfPhysicalNumber = _H3cIfPhysicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 1),
    _H3cIfPhysicalNumber_Type()
)
h3cIfPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfPhysicalNumber.setStatus("current")
_H3cIfTable_Object = MibTable
h3cIfTable = _H3cIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2)
)
if mibBuilder.loadTexts:
    h3cIfTable.setStatus("current")
_H3cIfEntry_Object = MibTableRow
h3cIfEntry = _H3cIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1)
)
h3cIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfEntry.setStatus("current")
_H3cIfUpDownTimes_Type = Integer32
_H3cIfUpDownTimes_Object = MibTableColumn
h3cIfUpDownTimes = _H3cIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 1),
    _H3cIfUpDownTimes_Type()
)
h3cIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfUpDownTimes.setStatus("current")
_H3cIfMtu_Type = Integer32
_H3cIfMtu_Object = MibTableColumn
h3cIfMtu = _H3cIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 2),
    _H3cIfMtu_Type()
)
h3cIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfMtu.setStatus("current")


class _H3cIfBandwidthRate_Type(Integer32):
    """Custom type h3cIfBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cIfBandwidthRate_Type.__name__ = "Integer32"
_H3cIfBandwidthRate_Object = MibTableColumn
h3cIfBandwidthRate = _H3cIfBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 3),
    _H3cIfBandwidthRate_Type()
)
h3cIfBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfBandwidthRate.setStatus("current")


class _H3cIfDiscardPktRate_Type(Integer32):
    """Custom type h3cIfDiscardPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cIfDiscardPktRate_Type.__name__ = "Integer32"
_H3cIfDiscardPktRate_Object = MibTableColumn
h3cIfDiscardPktRate = _H3cIfDiscardPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 4),
    _H3cIfDiscardPktRate_Type()
)
h3cIfDiscardPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfDiscardPktRate.setStatus("current")
_H3cIfStatusKeepTime_Type = TimeTicks
_H3cIfStatusKeepTime_Object = MibTableColumn
h3cIfStatusKeepTime = _H3cIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 5),
    _H3cIfStatusKeepTime_Type()
)
h3cIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfStatusKeepTime.setStatus("current")
_H3cIfInNUcastPkts_Type = Counter64
_H3cIfInNUcastPkts_Object = MibTableColumn
h3cIfInNUcastPkts = _H3cIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 6),
    _H3cIfInNUcastPkts_Type()
)
h3cIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfInNUcastPkts.setStatus("current")
_H3cIfOutNUcastPkts_Type = Counter64
_H3cIfOutNUcastPkts_Object = MibTableColumn
h3cIfOutNUcastPkts = _H3cIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 7),
    _H3cIfOutNUcastPkts_Type()
)
h3cIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfOutNUcastPkts.setStatus("current")
_H3cIfExtTrap_ObjectIdentity = ObjectIdentity
h3cIfExtTrap = _H3cIfExtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3)
)
_H3cIfExtTrapPrex_ObjectIdentity = ObjectIdentity
h3cIfExtTrapPrex = _H3cIfExtTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0)
)
_H3cIfExtTrapObject_ObjectIdentity = ObjectIdentity
h3cIfExtTrapObject = _H3cIfExtTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1)
)
_H3cIfExtTrapCfgTable_Object = MibTable
h3cIfExtTrapCfgTable = _H3cIfExtTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfExtTrapCfgTable.setStatus("current")
_H3cIfExtTrapCfgEntry_Object = MibTableRow
h3cIfExtTrapCfgEntry = _H3cIfExtTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1)
)
h3cIfExtTrapCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfExtTrapCfgEntry.setStatus("current")


class _H3cIfBandwidthUpperLimit_Type(Integer32):
    """Custom type h3cIfBandwidthUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cIfBandwidthUpperLimit_Type.__name__ = "Integer32"
_H3cIfBandwidthUpperLimit_Object = MibTableColumn
h3cIfBandwidthUpperLimit = _H3cIfBandwidthUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1, 1),
    _H3cIfBandwidthUpperLimit_Type()
)
h3cIfBandwidthUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfBandwidthUpperLimit.setStatus("current")


class _H3cIfDiscardPktRateUpperLimit_Type(Integer32):
    """Custom type h3cIfDiscardPktRateUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cIfDiscardPktRateUpperLimit_Type.__name__ = "Integer32"
_H3cIfDiscardPktRateUpperLimit_Object = MibTableColumn
h3cIfDiscardPktRateUpperLimit = _H3cIfDiscardPktRateUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1, 2),
    _H3cIfDiscardPktRateUpperLimit_Type()
)
h3cIfDiscardPktRateUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfDiscardPktRateUpperLimit.setStatus("current")

# Managed Objects groups


# Notification objects

h3cIfBandwidthUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 1)
)
h3cIfBandwidthUsageHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfBandwidthRate"),
        ("H3C-IF-EXT-MIB", "h3cIfBandwidthUpperLimit"))
)
if mibBuilder.loadTexts:
    h3cIfBandwidthUsageHigh.setStatus(
        "current"
    )

h3cIfDiscardPktRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 2)
)
h3cIfDiscardPktRateHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("H3C-IF-EXT-MIB", "h3cIfDiscardPktRate"),
        ("H3C-IF-EXT-MIB", "h3cIfDiscardPktRateUpperLimit"))
)
if mibBuilder.loadTexts:
    h3cIfDiscardPktRateHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-IF-EXT-MIB",
    **{"h3cIfExt": h3cIfExt,
       "h3cIfExtScalarGroup": h3cIfExtScalarGroup,
       "h3cIfStatGlobalFlowInterval": h3cIfStatGlobalFlowInterval,
       "h3cIfExtGroup": h3cIfExtGroup,
       "h3cIfStat": h3cIfStat,
       "h3cIfStatScalarGroup": h3cIfStatScalarGroup,
       "h3cIfStatTable": h3cIfStatTable,
       "h3cIfFlowStatTable": h3cIfFlowStatTable,
       "h3cIfStatEntry": h3cIfStatEntry,
       "h3cIfStatFlowInterval": h3cIfStatFlowInterval,
       "h3cIfStatFlowInBits": h3cIfStatFlowInBits,
       "h3cIfStatFlowOutBits": h3cIfStatFlowOutBits,
       "h3cIfStatFlowInPkts": h3cIfStatFlowInPkts,
       "h3cIfStatFlowOutPkts": h3cIfStatFlowOutPkts,
       "h3cIfStatFlowInBytes": h3cIfStatFlowInBytes,
       "h3cIfStatFlowOutBytes": h3cIfStatFlowOutBytes,
       "h3cIfSpeedStatTable": h3cIfSpeedStatTable,
       "h3cIfSpeedStatEntry": h3cIfSpeedStatEntry,
       "h3cIfSpeedStatInterval": h3cIfSpeedStatInterval,
       "h3cIfSpeedStatInPkts": h3cIfSpeedStatInPkts,
       "h3cIfSpeedStatOutPkts": h3cIfSpeedStatOutPkts,
       "h3cIfSpeedStatInBytes": h3cIfSpeedStatInBytes,
       "h3cIfSpeedStatOutBytes": h3cIfSpeedStatOutBytes,
       "h3cIfControl": h3cIfControl,
       "h3cRTParentIfTable": h3cRTParentIfTable,
       "h3cRTParentIfEntry": h3cRTParentIfEntry,
       "h3cRTParentIfIndex": h3cRTParentIfIndex,
       "h3cRTMinSubIfOrdinal": h3cRTMinSubIfOrdinal,
       "h3cRTMaxSubIfOrdinal": h3cRTMaxSubIfOrdinal,
       "h3cRTSubIfTable": h3cRTSubIfTable,
       "h3cRTSubIfEntry": h3cRTSubIfEntry,
       "h3cRTSubIfParentIfIndex": h3cRTSubIfParentIfIndex,
       "h3cRTSubIfOrdinal": h3cRTSubIfOrdinal,
       "h3cRTSubIfSubIfIndex": h3cRTSubIfSubIfIndex,
       "h3cRTSubIfSubIfDesc": h3cRTSubIfSubIfDesc,
       "h3cRTSubIfRowStatus": h3cRTSubIfRowStatus,
       "h3cIfLinkModeTable": h3cIfLinkModeTable,
       "h3cIfLinkModeEntry": h3cIfLinkModeEntry,
       "h3cIfLinkModeIndex": h3cIfLinkModeIndex,
       "h3cIfLinkMode": h3cIfLinkMode,
       "h3cIfLinkModeSwitchSupport": h3cIfLinkModeSwitchSupport,
       "h3cIfInterfaces": h3cIfInterfaces,
       "h3cIfPhysicalNumber": h3cIfPhysicalNumber,
       "h3cIfTable": h3cIfTable,
       "h3cIfEntry": h3cIfEntry,
       "h3cIfUpDownTimes": h3cIfUpDownTimes,
       "h3cIfMtu": h3cIfMtu,
       "h3cIfBandwidthRate": h3cIfBandwidthRate,
       "h3cIfDiscardPktRate": h3cIfDiscardPktRate,
       "h3cIfStatusKeepTime": h3cIfStatusKeepTime,
       "h3cIfInNUcastPkts": h3cIfInNUcastPkts,
       "h3cIfOutNUcastPkts": h3cIfOutNUcastPkts,
       "h3cIfExtTrap": h3cIfExtTrap,
       "h3cIfExtTrapPrex": h3cIfExtTrapPrex,
       "h3cIfBandwidthUsageHigh": h3cIfBandwidthUsageHigh,
       "h3cIfDiscardPktRateHigh": h3cIfDiscardPktRateHigh,
       "h3cIfExtTrapObject": h3cIfExtTrapObject,
       "h3cIfExtTrapCfgTable": h3cIfExtTrapCfgTable,
       "h3cIfExtTrapCfgEntry": h3cIfExtTrapCfgEntry,
       "h3cIfBandwidthUpperLimit": h3cIfBandwidthUpperLimit,
       "h3cIfDiscardPktRateUpperLimit": h3cIfDiscardPktRateUpperLimit}
)
