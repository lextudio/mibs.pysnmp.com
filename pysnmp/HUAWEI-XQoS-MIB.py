# SNMP MIB module (HUAWEI-XQoS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-XQoS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:47 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwXQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BaType(Integer32, TextualConvention):
    status = "current"
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
        *(("dscp", 2),
          ("hqosDscp", 6),
          ("hqosIpPri", 8),
          ("hqosMplsExp", 7),
          ("hqosVlan8021p", 5),
          ("ipPri", 4),
          ("mplsExp", 3),
          ("vlan8021p", 1),
          ("vlan8021pInbound", 9))
    )



class XQosQueueType(Integer32, TextualConvention):
    status = "current"
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("ef", 6))
    )



class ResetFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 2),
          ("reset", 1))
    )



class CosType(Integer32, TextualConvention):
    status = "current"
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("all", 9),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("queue10", 10),
          ("queue11", 11),
          ("queue12", 12),
          ("queue13", 13),
          ("queue14", 14),
          ("queue15", 15),
          ("queue16", 16),
          ("queue17", 17),
          ("queue18", 18),
          ("queue19", 19),
          ("queue20", 20),
          ("queue21", 21),
          ("queue22", 22),
          ("queue23", 23),
          ("queue24", 24))
    )



class CarAction(Integer32, TextualConvention):
    status = "current"
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
        *(("discard", 2),
          ("pass", 1),
          ("remark", 6),
          ("remark8021p", 7),
          ("remarkDscp", 4),
          ("remarkIpPrec", 3),
          ("remarkMplsExp", 5))
    )



class DirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class UrpfCtrlType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )



class SampleType(Integer32, TextualConvention):
    status = "current"
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
        *(("fix-packets", 1),
          ("fix-time", 2),
          ("random-packets", 3),
          ("random-time", 4))
    )



class IPCARRuleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Acl", 1),
          ("ipv4DstIp", 3),
          ("ipv4SrcIp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwQoS_ObjectIdentity = ObjectIdentity
hwQoS = _HwQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32)
)
_HwXQoSObjects_ObjectIdentity = ObjectIdentity
hwXQoSObjects = _HwXQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1)
)
_HwXQoSBaObjects_ObjectIdentity = ObjectIdentity
hwXQoSBaObjects = _HwXQoSBaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1)
)
_HwXQoSBaCfgInfoTable_Object = MibTable
hwXQoSBaCfgInfoTable = _HwXQoSBaCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwXQoSBaCfgInfoTable.setStatus("current")
_HwXQoSBaCfgInfoEntry_Object = MibTableRow
hwXQoSBaCfgInfoEntry = _HwXQoSBaCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 1, 1)
)
hwXQoSBaCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBaCfgInfoEntry.setStatus("current")
_HwXQoSBaIndex_Type = Integer32
_HwXQoSBaIndex_Object = MibTableColumn
hwXQoSBaIndex = _HwXQoSBaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 1, 1, 1),
    _HwXQoSBaIndex_Type()
)
hwXQoSBaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaIndex.setStatus("current")


class _HwXQoSBaName_Type(OctetString):
    """Custom type hwXQoSBaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HwXQoSBaName_Type.__name__ = "OctetString"
_HwXQoSBaName_Object = MibTableColumn
hwXQoSBaName = _HwXQoSBaName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 1, 1, 2),
    _HwXQoSBaName_Type()
)
hwXQoSBaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaName.setStatus("current")
_HwXQoSBaRowStatus_Type = RowStatus
_HwXQoSBaRowStatus_Object = MibTableColumn
hwXQoSBaRowStatus = _HwXQoSBaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 1, 1, 3),
    _HwXQoSBaRowStatus_Type()
)
hwXQoSBaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaRowStatus.setStatus("current")
_HwXQoSBa8021pPhbCfgInfoTable_Object = MibTable
hwXQoSBa8021pPhbCfgInfoTable = _HwXQoSBa8021pPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbCfgInfoTable.setStatus("current")
_HwXQoSBa8021pPhbCfgInfoEntry_Object = MibTableRow
hwXQoSBa8021pPhbCfgInfoEntry = _HwXQoSBa8021pPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2, 1)
)
hwXQoSBa8021pPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBa8021pPhbIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbCfgInfoEntry.setStatus("current")
_HwXQoSBa8021pPhbIndex_Type = Integer32
_HwXQoSBa8021pPhbIndex_Object = MibTableColumn
hwXQoSBa8021pPhbIndex = _HwXQoSBa8021pPhbIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2, 1, 1),
    _HwXQoSBa8021pPhbIndex_Type()
)
hwXQoSBa8021pPhbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbIndex.setStatus("current")
_HwXQoSBa8021pPhbPri_Type = Integer32
_HwXQoSBa8021pPhbPri_Object = MibTableColumn
hwXQoSBa8021pPhbPri = _HwXQoSBa8021pPhbPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2, 1, 2),
    _HwXQoSBa8021pPhbPri_Type()
)
hwXQoSBa8021pPhbPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbPri.setStatus("current")
_HwXQoSBa8021pPhbCos_Type = Integer32
_HwXQoSBa8021pPhbCos_Object = MibTableColumn
hwXQoSBa8021pPhbCos = _HwXQoSBa8021pPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2, 1, 3),
    _HwXQoSBa8021pPhbCos_Type()
)
hwXQoSBa8021pPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbCos.setStatus("current")
_HwXQoSBa8021pPhbColour_Type = Integer32
_HwXQoSBa8021pPhbColour_Object = MibTableColumn
hwXQoSBa8021pPhbColour = _HwXQoSBa8021pPhbColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2, 1, 4),
    _HwXQoSBa8021pPhbColour_Type()
)
hwXQoSBa8021pPhbColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbColour.setStatus("current")
_HwXQoSBa8021pPhbRowStatus_Type = RowStatus
_HwXQoSBa8021pPhbRowStatus_Object = MibTableColumn
hwXQoSBa8021pPhbRowStatus = _HwXQoSBa8021pPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 2, 1, 5),
    _HwXQoSBa8021pPhbRowStatus_Type()
)
hwXQoSBa8021pPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbRowStatus.setStatus("current")
_HwXQoSBa8021pMapCfgInfoTable_Object = MibTable
hwXQoSBa8021pMapCfgInfoTable = _HwXQoSBa8021pMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapCfgInfoTable.setStatus("current")
_HwXQoSBa8021pMapCfgInfoEntry_Object = MibTableRow
hwXQoSBa8021pMapCfgInfoEntry = _HwXQoSBa8021pMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3, 1)
)
hwXQoSBa8021pMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBa8021pMapIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapCfgInfoEntry.setStatus("current")
_HwXQoSBa8021pMapIndex_Type = Integer32
_HwXQoSBa8021pMapIndex_Object = MibTableColumn
hwXQoSBa8021pMapIndex = _HwXQoSBa8021pMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3, 1, 1),
    _HwXQoSBa8021pMapIndex_Type()
)
hwXQoSBa8021pMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapIndex.setStatus("current")
_HwXQoSBa8021pMapCos_Type = Integer32
_HwXQoSBa8021pMapCos_Object = MibTableColumn
hwXQoSBa8021pMapCos = _HwXQoSBa8021pMapCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3, 1, 2),
    _HwXQoSBa8021pMapCos_Type()
)
hwXQoSBa8021pMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapCos.setStatus("current")
_HwXQoSBa8021pMapColour_Type = Integer32
_HwXQoSBa8021pMapColour_Object = MibTableColumn
hwXQoSBa8021pMapColour = _HwXQoSBa8021pMapColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3, 1, 3),
    _HwXQoSBa8021pMapColour_Type()
)
hwXQoSBa8021pMapColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapColour.setStatus("current")
_HwXQoSBa8021pMapPri_Type = Integer32
_HwXQoSBa8021pMapPri_Object = MibTableColumn
hwXQoSBa8021pMapPri = _HwXQoSBa8021pMapPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3, 1, 4),
    _HwXQoSBa8021pMapPri_Type()
)
hwXQoSBa8021pMapPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapPri.setStatus("current")
_HwXQoSBa8021pMapRowStatus_Type = RowStatus
_HwXQoSBa8021pMapRowStatus_Object = MibTableColumn
hwXQoSBa8021pMapRowStatus = _HwXQoSBa8021pMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 3, 1, 5),
    _HwXQoSBa8021pMapRowStatus_Type()
)
hwXQoSBa8021pMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapRowStatus.setStatus("current")
_HwXQoSBaDscpPhbCfgInfoTable_Object = MibTable
hwXQoSBaDscpPhbCfgInfoTable = _HwXQoSBaDscpPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbCfgInfoTable.setStatus("current")
_HwXQoSBaDscpPhbCfgInfoEntry_Object = MibTableRow
hwXQoSBaDscpPhbCfgInfoEntry = _HwXQoSBaDscpPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4, 1)
)
hwXQoSBaDscpPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaDscpPhbIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbCfgInfoEntry.setStatus("current")
_HwXQoSBaDscpPhbIndex_Type = Integer32
_HwXQoSBaDscpPhbIndex_Object = MibTableColumn
hwXQoSBaDscpPhbIndex = _HwXQoSBaDscpPhbIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4, 1, 1),
    _HwXQoSBaDscpPhbIndex_Type()
)
hwXQoSBaDscpPhbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbIndex.setStatus("current")
_HwXQoSBaDscpPhbPri_Type = Integer32
_HwXQoSBaDscpPhbPri_Object = MibTableColumn
hwXQoSBaDscpPhbPri = _HwXQoSBaDscpPhbPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4, 1, 2),
    _HwXQoSBaDscpPhbPri_Type()
)
hwXQoSBaDscpPhbPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbPri.setStatus("current")
_HwXQoSBaDscpPhbCos_Type = Integer32
_HwXQoSBaDscpPhbCos_Object = MibTableColumn
hwXQoSBaDscpPhbCos = _HwXQoSBaDscpPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4, 1, 3),
    _HwXQoSBaDscpPhbCos_Type()
)
hwXQoSBaDscpPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbCos.setStatus("current")
_HwXQoSBaDscpPhbColour_Type = Integer32
_HwXQoSBaDscpPhbColour_Object = MibTableColumn
hwXQoSBaDscpPhbColour = _HwXQoSBaDscpPhbColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4, 1, 4),
    _HwXQoSBaDscpPhbColour_Type()
)
hwXQoSBaDscpPhbColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbColour.setStatus("current")
_HwXQoSBaDscpPhbRowStatus_Type = RowStatus
_HwXQoSBaDscpPhbRowStatus_Object = MibTableColumn
hwXQoSBaDscpPhbRowStatus = _HwXQoSBaDscpPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 4, 1, 5),
    _HwXQoSBaDscpPhbRowStatus_Type()
)
hwXQoSBaDscpPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbRowStatus.setStatus("current")
_HwXQoSBaDscpMapCfgInfoTable_Object = MibTable
hwXQoSBaDscpMapCfgInfoTable = _HwXQoSBaDscpMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapCfgInfoTable.setStatus("current")
_HwXQoSBaDscpMapCfgInfoEntry_Object = MibTableRow
hwXQoSBaDscpMapCfgInfoEntry = _HwXQoSBaDscpMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5, 1)
)
hwXQoSBaDscpMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaDscpMapIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapCfgInfoEntry.setStatus("current")
_HwXQoSBaDscpMapIndex_Type = Integer32
_HwXQoSBaDscpMapIndex_Object = MibTableColumn
hwXQoSBaDscpMapIndex = _HwXQoSBaDscpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5, 1, 1),
    _HwXQoSBaDscpMapIndex_Type()
)
hwXQoSBaDscpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapIndex.setStatus("current")
_HwXQoSBaDscpMapCos_Type = Integer32
_HwXQoSBaDscpMapCos_Object = MibTableColumn
hwXQoSBaDscpMapCos = _HwXQoSBaDscpMapCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5, 1, 2),
    _HwXQoSBaDscpMapCos_Type()
)
hwXQoSBaDscpMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapCos.setStatus("current")
_HwXQoSBaDscpMapColour_Type = Integer32
_HwXQoSBaDscpMapColour_Object = MibTableColumn
hwXQoSBaDscpMapColour = _HwXQoSBaDscpMapColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5, 1, 3),
    _HwXQoSBaDscpMapColour_Type()
)
hwXQoSBaDscpMapColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapColour.setStatus("current")
_HwXQoSBaDscpMapPri_Type = Integer32
_HwXQoSBaDscpMapPri_Object = MibTableColumn
hwXQoSBaDscpMapPri = _HwXQoSBaDscpMapPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5, 1, 4),
    _HwXQoSBaDscpMapPri_Type()
)
hwXQoSBaDscpMapPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapPri.setStatus("current")
_HwXQoSBaDscpMapRowStatus_Type = RowStatus
_HwXQoSBaDscpMapRowStatus_Object = MibTableColumn
hwXQoSBaDscpMapRowStatus = _HwXQoSBaDscpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 5, 1, 5),
    _HwXQoSBaDscpMapRowStatus_Type()
)
hwXQoSBaDscpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapRowStatus.setStatus("current")
_HwXQoSBaExpPhbCfgInfoTable_Object = MibTable
hwXQoSBaExpPhbCfgInfoTable = _HwXQoSBaExpPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbCfgInfoTable.setStatus("current")
_HwXQoSBaExpPhbCfgInfoEntry_Object = MibTableRow
hwXQoSBaExpPhbCfgInfoEntry = _HwXQoSBaExpPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6, 1)
)
hwXQoSBaExpPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaExpPhbIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbCfgInfoEntry.setStatus("current")
_HwXQoSBaExpPhbIndex_Type = Integer32
_HwXQoSBaExpPhbIndex_Object = MibTableColumn
hwXQoSBaExpPhbIndex = _HwXQoSBaExpPhbIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6, 1, 1),
    _HwXQoSBaExpPhbIndex_Type()
)
hwXQoSBaExpPhbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbIndex.setStatus("current")
_HwXQoSBaExpPhbPri_Type = Integer32
_HwXQoSBaExpPhbPri_Object = MibTableColumn
hwXQoSBaExpPhbPri = _HwXQoSBaExpPhbPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6, 1, 2),
    _HwXQoSBaExpPhbPri_Type()
)
hwXQoSBaExpPhbPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbPri.setStatus("current")
_HwXQoSBaExpPhbCos_Type = Integer32
_HwXQoSBaExpPhbCos_Object = MibTableColumn
hwXQoSBaExpPhbCos = _HwXQoSBaExpPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6, 1, 3),
    _HwXQoSBaExpPhbCos_Type()
)
hwXQoSBaExpPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbCos.setStatus("current")
_HwXQoSBaExpPhbColour_Type = Integer32
_HwXQoSBaExpPhbColour_Object = MibTableColumn
hwXQoSBaExpPhbColour = _HwXQoSBaExpPhbColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6, 1, 4),
    _HwXQoSBaExpPhbColour_Type()
)
hwXQoSBaExpPhbColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbColour.setStatus("current")
_HwXQoSBaExpPhbRowStatus_Type = RowStatus
_HwXQoSBaExpPhbRowStatus_Object = MibTableColumn
hwXQoSBaExpPhbRowStatus = _HwXQoSBaExpPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 6, 1, 5),
    _HwXQoSBaExpPhbRowStatus_Type()
)
hwXQoSBaExpPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbRowStatus.setStatus("current")
_HwXQoSBaExpMapCfgInfoTable_Object = MibTable
hwXQoSBaExpMapCfgInfoTable = _HwXQoSBaExpMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwXQoSBaExpMapCfgInfoTable.setStatus("current")
_HwXQoSBaExpMapCfgInfoEntry_Object = MibTableRow
hwXQoSBaExpMapCfgInfoEntry = _HwXQoSBaExpMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7, 1)
)
hwXQoSBaExpMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaExpMapIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBaExpMapCfgInfoEntry.setStatus("current")
_HwXQoSBaExpMapIndex_Type = Integer32
_HwXQoSBaExpMapIndex_Object = MibTableColumn
hwXQoSBaExpMapIndex = _HwXQoSBaExpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7, 1, 1),
    _HwXQoSBaExpMapIndex_Type()
)
hwXQoSBaExpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaExpMapIndex.setStatus("current")
_HwXQoSBaExpMapCos_Type = Integer32
_HwXQoSBaExpMapCos_Object = MibTableColumn
hwXQoSBaExpMapCos = _HwXQoSBaExpMapCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7, 1, 2),
    _HwXQoSBaExpMapCos_Type()
)
hwXQoSBaExpMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaExpMapCos.setStatus("current")
_HwXQoSBaExpMapColour_Type = Integer32
_HwXQoSBaExpMapColour_Object = MibTableColumn
hwXQoSBaExpMapColour = _HwXQoSBaExpMapColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7, 1, 3),
    _HwXQoSBaExpMapColour_Type()
)
hwXQoSBaExpMapColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaExpMapColour.setStatus("current")
_HwXQoSBaExpMapPri_Type = Integer32
_HwXQoSBaExpMapPri_Object = MibTableColumn
hwXQoSBaExpMapPri = _HwXQoSBaExpMapPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7, 1, 4),
    _HwXQoSBaExpMapPri_Type()
)
hwXQoSBaExpMapPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaExpMapPri.setStatus("current")
_HwXQoSBaExpMapRowStatus_Type = RowStatus
_HwXQoSBaExpMapRowStatus_Object = MibTableColumn
hwXQoSBaExpMapRowStatus = _HwXQoSBaExpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 7, 1, 5),
    _HwXQoSBaExpMapRowStatus_Type()
)
hwXQoSBaExpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaExpMapRowStatus.setStatus("current")
_HwXQoSIfDiffDomainTable_Object = MibTable
hwXQoSIfDiffDomainTable = _HwXQoSIfDiffDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainTable.setStatus("current")
_HwXQoSIfDiffDomainEntry_Object = MibTableRow
hwXQoSIfDiffDomainEntry = _HwXQoSIfDiffDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8, 1)
)
hwXQoSIfDiffDomainEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainVlanId"),
)
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainEntry.setStatus("current")
_HwXQoSIfDiffDomainIfIndex_Type = Integer32
_HwXQoSIfDiffDomainIfIndex_Object = MibTableColumn
hwXQoSIfDiffDomainIfIndex = _HwXQoSIfDiffDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8, 1, 1),
    _HwXQoSIfDiffDomainIfIndex_Type()
)
hwXQoSIfDiffDomainIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainIfIndex.setStatus("current")


class _HwXQoSIfDiffDomainVlanId_Type(Integer32):
    """Custom type hwXQoSIfDiffDomainVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSIfDiffDomainVlanId_Type.__name__ = "Integer32"
_HwXQoSIfDiffDomainVlanId_Object = MibTableColumn
hwXQoSIfDiffDomainVlanId = _HwXQoSIfDiffDomainVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8, 1, 2),
    _HwXQoSIfDiffDomainVlanId_Type()
)
hwXQoSIfDiffDomainVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainVlanId.setStatus("current")


class _HwXQoSIfDiffDomainName_Type(OctetString):
    """Custom type hwXQoSIfDiffDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSIfDiffDomainName_Type.__name__ = "OctetString"
_HwXQoSIfDiffDomainName_Object = MibTableColumn
hwXQoSIfDiffDomainName = _HwXQoSIfDiffDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8, 1, 3),
    _HwXQoSIfDiffDomainName_Type()
)
hwXQoSIfDiffDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainName.setStatus("current")
_HwXQoSIfDiffDomainRowStatus_Type = RowStatus
_HwXQoSIfDiffDomainRowStatus_Object = MibTableColumn
hwXQoSIfDiffDomainRowStatus = _HwXQoSIfDiffDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8, 1, 4),
    _HwXQoSIfDiffDomainRowStatus_Type()
)
hwXQoSIfDiffDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainRowStatus.setStatus("current")


class _HwXQoSIfDiffDomainVlanId2_Type(Integer32):
    """Custom type hwXQoSIfDiffDomainVlanId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSIfDiffDomainVlanId2_Type.__name__ = "Integer32"
_HwXQoSIfDiffDomainVlanId2_Object = MibTableColumn
hwXQoSIfDiffDomainVlanId2 = _HwXQoSIfDiffDomainVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 8, 1, 5),
    _HwXQoSIfDiffDomainVlanId2_Type()
)
hwXQoSIfDiffDomainVlanId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainVlanId2.setStatus("current")
_HwXQoSIfTrust8021pTable_Object = MibTable
hwXQoSIfTrust8021pTable = _HwXQoSIfTrust8021pTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pTable.setStatus("current")
_HwXQoSIfTrust8021pEntry_Object = MibTableRow
hwXQoSIfTrust8021pEntry = _HwXQoSIfTrust8021pEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 9, 1)
)
hwXQoSIfTrust8021pEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfTrust8021pIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfTrust8021pVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pEntry.setStatus("current")
_HwXQoSIfTrust8021pIfIndex_Type = Integer32
_HwXQoSIfTrust8021pIfIndex_Object = MibTableColumn
hwXQoSIfTrust8021pIfIndex = _HwXQoSIfTrust8021pIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 9, 1, 1),
    _HwXQoSIfTrust8021pIfIndex_Type()
)
hwXQoSIfTrust8021pIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pIfIndex.setStatus("current")


class _HwXQoSIfTrust8021pVlanID_Type(Integer32):
    """Custom type hwXQoSIfTrust8021pVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSIfTrust8021pVlanID_Type.__name__ = "Integer32"
_HwXQoSIfTrust8021pVlanID_Object = MibTableColumn
hwXQoSIfTrust8021pVlanID = _HwXQoSIfTrust8021pVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 9, 1, 2),
    _HwXQoSIfTrust8021pVlanID_Type()
)
hwXQoSIfTrust8021pVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pVlanID.setStatus("current")


class _HwXQoSIfTrust8021pAction_Type(Integer32):
    """Custom type hwXQoSIfTrust8021pAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distrust", 1),
          ("trust", 2))
    )


_HwXQoSIfTrust8021pAction_Type.__name__ = "Integer32"
_HwXQoSIfTrust8021pAction_Object = MibTableColumn
hwXQoSIfTrust8021pAction = _HwXQoSIfTrust8021pAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 9, 1, 3),
    _HwXQoSIfTrust8021pAction_Type()
)
hwXQoSIfTrust8021pAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pAction.setStatus("current")
_HwXQoSIfTrust8021pRowStatus_Type = RowStatus
_HwXQoSIfTrust8021pRowStatus_Object = MibTableColumn
hwXQoSIfTrust8021pRowStatus = _HwXQoSIfTrust8021pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 9, 1, 4),
    _HwXQoSIfTrust8021pRowStatus_Type()
)
hwXQoSIfTrust8021pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pRowStatus.setStatus("current")
_HwXQoSBaAtmQosPhbCfgInfoTable_Object = MibTable
hwXQoSBaAtmQosPhbCfgInfoTable = _HwXQoSBaAtmQosPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbCfgInfoTable.setStatus("current")
_HwXQoSBaAtmQosPhbCfgInfoEntry_Object = MibTableRow
hwXQoSBaAtmQosPhbCfgInfoEntry = _HwXQoSBaAtmQosPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10, 1)
)
hwXQoSBaAtmQosPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaAtmQosPhbServType"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaAtmQosPhbClp"),
)
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbCfgInfoEntry.setStatus("current")
_HwXQoSBaAtmQosPhbServType_Type = Integer32
_HwXQoSBaAtmQosPhbServType_Object = MibTableColumn
hwXQoSBaAtmQosPhbServType = _HwXQoSBaAtmQosPhbServType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10, 1, 1),
    _HwXQoSBaAtmQosPhbServType_Type()
)
hwXQoSBaAtmQosPhbServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbServType.setStatus("current")
_HwXQoSBaAtmQosPhbClp_Type = Integer32
_HwXQoSBaAtmQosPhbClp_Object = MibTableColumn
hwXQoSBaAtmQosPhbClp = _HwXQoSBaAtmQosPhbClp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10, 1, 2),
    _HwXQoSBaAtmQosPhbClp_Type()
)
hwXQoSBaAtmQosPhbClp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbClp.setStatus("current")
_HwXQoSBaAtmQosPhbCos_Type = Integer32
_HwXQoSBaAtmQosPhbCos_Object = MibTableColumn
hwXQoSBaAtmQosPhbCos = _HwXQoSBaAtmQosPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10, 1, 3),
    _HwXQoSBaAtmQosPhbCos_Type()
)
hwXQoSBaAtmQosPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbCos.setStatus("current")
_HwXQoSBaAtmQosPhbColour_Type = Integer32
_HwXQoSBaAtmQosPhbColour_Object = MibTableColumn
hwXQoSBaAtmQosPhbColour = _HwXQoSBaAtmQosPhbColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10, 1, 4),
    _HwXQoSBaAtmQosPhbColour_Type()
)
hwXQoSBaAtmQosPhbColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbColour.setStatus("current")
_HwXQoSBaAtmQosPhbRowStatus_Type = RowStatus
_HwXQoSBaAtmQosPhbRowStatus_Object = MibTableColumn
hwXQoSBaAtmQosPhbRowStatus = _HwXQoSBaAtmQosPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 10, 1, 5),
    _HwXQoSBaAtmQosPhbRowStatus_Type()
)
hwXQoSBaAtmQosPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosPhbRowStatus.setStatus("current")
_HwXQoSBaAtmQosMapCfgInfoTable_Object = MibTable
hwXQoSBaAtmQosMapCfgInfoTable = _HwXQoSBaAtmQosMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapCfgInfoTable.setStatus("current")
_HwXQoSBaAtmQosMapCfgInfoEntry_Object = MibTableRow
hwXQoSBaAtmQosMapCfgInfoEntry = _HwXQoSBaAtmQosMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11, 1)
)
hwXQoSBaAtmQosMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaAtmQosMapIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapCfgInfoEntry.setStatus("current")
_HwXQoSBaAtmQosMapIndex_Type = Integer32
_HwXQoSBaAtmQosMapIndex_Object = MibTableColumn
hwXQoSBaAtmQosMapIndex = _HwXQoSBaAtmQosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11, 1, 1),
    _HwXQoSBaAtmQosMapIndex_Type()
)
hwXQoSBaAtmQosMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapIndex.setStatus("current")
_HwXQoSBaAtmQosMapCos_Type = Integer32
_HwXQoSBaAtmQosMapCos_Object = MibTableColumn
hwXQoSBaAtmQosMapCos = _HwXQoSBaAtmQosMapCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11, 1, 2),
    _HwXQoSBaAtmQosMapCos_Type()
)
hwXQoSBaAtmQosMapCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapCos.setStatus("current")
_HwXQoSBaAtmQosMapColour_Type = Integer32
_HwXQoSBaAtmQosMapColour_Object = MibTableColumn
hwXQoSBaAtmQosMapColour = _HwXQoSBaAtmQosMapColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11, 1, 3),
    _HwXQoSBaAtmQosMapColour_Type()
)
hwXQoSBaAtmQosMapColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapColour.setStatus("current")
_HwXQoSBaAtmQosMapClp_Type = Integer32
_HwXQoSBaAtmQosMapClp_Object = MibTableColumn
hwXQoSBaAtmQosMapClp = _HwXQoSBaAtmQosMapClp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11, 1, 4),
    _HwXQoSBaAtmQosMapClp_Type()
)
hwXQoSBaAtmQosMapClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapClp.setStatus("current")
_HwXQoSBaAtmQosMapRowStatus_Type = RowStatus
_HwXQoSBaAtmQosMapRowStatus_Object = MibTableColumn
hwXQoSBaAtmQosMapRowStatus = _HwXQoSBaAtmQosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 11, 1, 5),
    _HwXQoSBaAtmQosMapRowStatus_Type()
)
hwXQoSBaAtmQosMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaAtmQosMapRowStatus.setStatus("current")
_HwXQoSAtmPvcDiffDomainTable_Object = MibTable
hwXQoSAtmPvcDiffDomainTable = _HwXQoSAtmPvcDiffDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hwXQoSAtmPvcDiffDomainTable.setStatus("current")
_HwXQoSAtmPvcDiffDomainEntry_Object = MibTableRow
hwXQoSAtmPvcDiffDomainEntry = _HwXQoSAtmPvcDiffDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12, 1)
)
hwXQoSAtmPvcDiffDomainEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvcDiffDomainIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvcVpi"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvcVci"),
)
if mibBuilder.loadTexts:
    hwXQoSAtmPvcDiffDomainEntry.setStatus("current")
_HwXQoSAtmPvcDiffDomainIfIndex_Type = Integer32
_HwXQoSAtmPvcDiffDomainIfIndex_Object = MibTableColumn
hwXQoSAtmPvcDiffDomainIfIndex = _HwXQoSAtmPvcDiffDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12, 1, 1),
    _HwXQoSAtmPvcDiffDomainIfIndex_Type()
)
hwXQoSAtmPvcDiffDomainIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcDiffDomainIfIndex.setStatus("current")
_HwXQoSAtmPvcVpi_Type = Integer32
_HwXQoSAtmPvcVpi_Object = MibTableColumn
hwXQoSAtmPvcVpi = _HwXQoSAtmPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12, 1, 2),
    _HwXQoSAtmPvcVpi_Type()
)
hwXQoSAtmPvcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcVpi.setStatus("current")
_HwXQoSAtmPvcVci_Type = Integer32
_HwXQoSAtmPvcVci_Object = MibTableColumn
hwXQoSAtmPvcVci = _HwXQoSAtmPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12, 1, 3),
    _HwXQoSAtmPvcVci_Type()
)
hwXQoSAtmPvcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcVci.setStatus("current")


class _HwXQoSAtmPvcDiffDomainName_Type(OctetString):
    """Custom type hwXQoSAtmPvcDiffDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSAtmPvcDiffDomainName_Type.__name__ = "OctetString"
_HwXQoSAtmPvcDiffDomainName_Object = MibTableColumn
hwXQoSAtmPvcDiffDomainName = _HwXQoSAtmPvcDiffDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12, 1, 4),
    _HwXQoSAtmPvcDiffDomainName_Type()
)
hwXQoSAtmPvcDiffDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcDiffDomainName.setStatus("current")
_HwXQoSAtmPvcDiffDomainRowStatus_Type = RowStatus
_HwXQoSAtmPvcDiffDomainRowStatus_Object = MibTableColumn
hwXQoSAtmPvcDiffDomainRowStatus = _HwXQoSAtmPvcDiffDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 12, 1, 5),
    _HwXQoSAtmPvcDiffDomainRowStatus_Type()
)
hwXQoSAtmPvcDiffDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcDiffDomainRowStatus.setStatus("current")
_HwXQoSAtmPvpDiffDomainTable_Object = MibTable
hwXQoSAtmPvpDiffDomainTable = _HwXQoSAtmPvpDiffDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hwXQoSAtmPvpDiffDomainTable.setStatus("current")
_HwXQoSAtmPvpDiffDomainEntry_Object = MibTableRow
hwXQoSAtmPvpDiffDomainEntry = _HwXQoSAtmPvpDiffDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 13, 1)
)
hwXQoSAtmPvpDiffDomainEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvpDiffDomainIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvpVpi"),
)
if mibBuilder.loadTexts:
    hwXQoSAtmPvpDiffDomainEntry.setStatus("current")
_HwXQoSAtmPvpDiffDomainIfIndex_Type = Integer32
_HwXQoSAtmPvpDiffDomainIfIndex_Object = MibTableColumn
hwXQoSAtmPvpDiffDomainIfIndex = _HwXQoSAtmPvpDiffDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 13, 1, 1),
    _HwXQoSAtmPvpDiffDomainIfIndex_Type()
)
hwXQoSAtmPvpDiffDomainIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAtmPvpDiffDomainIfIndex.setStatus("current")
_HwXQoSAtmPvpVpi_Type = Integer32
_HwXQoSAtmPvpVpi_Object = MibTableColumn
hwXQoSAtmPvpVpi = _HwXQoSAtmPvpVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 13, 1, 2),
    _HwXQoSAtmPvpVpi_Type()
)
hwXQoSAtmPvpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAtmPvpVpi.setStatus("current")


class _HwXQoSAtmPvpDiffDomainName_Type(OctetString):
    """Custom type hwXQoSAtmPvpDiffDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSAtmPvpDiffDomainName_Type.__name__ = "OctetString"
_HwXQoSAtmPvpDiffDomainName_Object = MibTableColumn
hwXQoSAtmPvpDiffDomainName = _HwXQoSAtmPvpDiffDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 13, 1, 3),
    _HwXQoSAtmPvpDiffDomainName_Type()
)
hwXQoSAtmPvpDiffDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvpDiffDomainName.setStatus("current")
_HwXQoSAtmPvpDiffDomainRowStatus_Type = RowStatus
_HwXQoSAtmPvpDiffDomainRowStatus_Object = MibTableColumn
hwXQoSAtmPvpDiffDomainRowStatus = _HwXQoSAtmPvpDiffDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 13, 1, 4),
    _HwXQoSAtmPvpDiffDomainRowStatus_Type()
)
hwXQoSAtmPvpDiffDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvpDiffDomainRowStatus.setStatus("current")
_HwXQoSBaPhbCfgInfoTable_Object = MibTable
hwXQoSBaPhbCfgInfoTable = _HwXQoSBaPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hwXQoSBaPhbCfgInfoTable.setStatus("current")
_HwXQoSBaPhbCfgInfoEntry_Object = MibTableRow
hwXQoSBaPhbCfgInfoEntry = _HwXQoSBaPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14, 1)
)
hwXQoSBaPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaPhbType"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaPhbPri"),
)
if mibBuilder.loadTexts:
    hwXQoSBaPhbCfgInfoEntry.setStatus("current")
_HwXQoSBaPhbType_Type = BaType
_HwXQoSBaPhbType_Object = MibTableColumn
hwXQoSBaPhbType = _HwXQoSBaPhbType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14, 1, 1),
    _HwXQoSBaPhbType_Type()
)
hwXQoSBaPhbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSBaPhbType.setStatus("current")
_HwXQoSBaPhbPri_Type = Integer32
_HwXQoSBaPhbPri_Object = MibTableColumn
hwXQoSBaPhbPri = _HwXQoSBaPhbPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14, 1, 2),
    _HwXQoSBaPhbPri_Type()
)
hwXQoSBaPhbPri.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSBaPhbPri.setStatus("current")
_HwXQoSBaPhbCos_Type = Integer32
_HwXQoSBaPhbCos_Object = MibTableColumn
hwXQoSBaPhbCos = _HwXQoSBaPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14, 1, 3),
    _HwXQoSBaPhbCos_Type()
)
hwXQoSBaPhbCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaPhbCos.setStatus("current")


class _HwXQoSBaPhbColour_Type(Integer32):
    """Custom type hwXQoSBaPhbColour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSBaPhbColour_Type.__name__ = "Integer32"
_HwXQoSBaPhbColour_Object = MibTableColumn
hwXQoSBaPhbColour = _HwXQoSBaPhbColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14, 1, 4),
    _HwXQoSBaPhbColour_Type()
)
hwXQoSBaPhbColour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaPhbColour.setStatus("current")
_HwXQoSBaPhbRowStatus_Type = RowStatus
_HwXQoSBaPhbRowStatus_Object = MibTableColumn
hwXQoSBaPhbRowStatus = _HwXQoSBaPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 14, 1, 5),
    _HwXQoSBaPhbRowStatus_Type()
)
hwXQoSBaPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaPhbRowStatus.setStatus("current")
_HwXQoSBaMapCfgInfoTable_Object = MibTable
hwXQoSBaMapCfgInfoTable = _HwXQoSBaMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    hwXQoSBaMapCfgInfoTable.setStatus("current")
_HwXQoSBaMapCfgInfoEntry_Object = MibTableRow
hwXQoSBaMapCfgInfoEntry = _HwXQoSBaMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15, 1)
)
hwXQoSBaMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaMapType"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaMapCos"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaMapColour"),
)
if mibBuilder.loadTexts:
    hwXQoSBaMapCfgInfoEntry.setStatus("current")
_HwXQoSBaMapType_Type = BaType
_HwXQoSBaMapType_Object = MibTableColumn
hwXQoSBaMapType = _HwXQoSBaMapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15, 1, 1),
    _HwXQoSBaMapType_Type()
)
hwXQoSBaMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSBaMapType.setStatus("current")
_HwXQoSBaMapCos_Type = Integer32
_HwXQoSBaMapCos_Object = MibTableColumn
hwXQoSBaMapCos = _HwXQoSBaMapCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15, 1, 2),
    _HwXQoSBaMapCos_Type()
)
hwXQoSBaMapCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSBaMapCos.setStatus("current")


class _HwXQoSBaMapColour_Type(Integer32):
    """Custom type hwXQoSBaMapColour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSBaMapColour_Type.__name__ = "Integer32"
_HwXQoSBaMapColour_Object = MibTableColumn
hwXQoSBaMapColour = _HwXQoSBaMapColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15, 1, 3),
    _HwXQoSBaMapColour_Type()
)
hwXQoSBaMapColour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSBaMapColour.setStatus("current")
_HwXQoSBaMapPri_Type = Integer32
_HwXQoSBaMapPri_Object = MibTableColumn
hwXQoSBaMapPri = _HwXQoSBaMapPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15, 1, 4),
    _HwXQoSBaMapPri_Type()
)
hwXQoSBaMapPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaMapPri.setStatus("current")
_HwXQoSBaMapRowStatus_Type = RowStatus
_HwXQoSBaMapRowStatus_Object = MibTableColumn
hwXQoSBaMapRowStatus = _HwXQoSBaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 15, 1, 5),
    _HwXQoSBaMapRowStatus_Type()
)
hwXQoSBaMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSBaMapRowStatus.setStatus("current")
_HwXQoSIfTrustTable_Object = MibTable
hwXQoSIfTrustTable = _HwXQoSIfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hwXQoSIfTrustTable.setStatus("current")
_HwXQoSIfTrustEntry_Object = MibTableRow
hwXQoSIfTrustEntry = _HwXQoSIfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1)
)
hwXQoSIfTrustEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfTrustIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfTrustVlanID1"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfTrustVlanID2"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaType"),
)
if mibBuilder.loadTexts:
    hwXQoSIfTrustEntry.setStatus("current")
_HwXQoSIfTrustIfIndex_Type = Integer32
_HwXQoSIfTrustIfIndex_Object = MibTableColumn
hwXQoSIfTrustIfIndex = _HwXQoSIfTrustIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1, 1),
    _HwXQoSIfTrustIfIndex_Type()
)
hwXQoSIfTrustIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfTrustIfIndex.setStatus("current")


class _HwXQoSIfTrustVlanID1_Type(Integer32):
    """Custom type hwXQoSIfTrustVlanID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfTrustVlanID1_Type.__name__ = "Integer32"
_HwXQoSIfTrustVlanID1_Object = MibTableColumn
hwXQoSIfTrustVlanID1 = _HwXQoSIfTrustVlanID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1, 2),
    _HwXQoSIfTrustVlanID1_Type()
)
hwXQoSIfTrustVlanID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfTrustVlanID1.setStatus("current")


class _HwXQoSIfTrustVlanID2_Type(Integer32):
    """Custom type hwXQoSIfTrustVlanID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfTrustVlanID2_Type.__name__ = "Integer32"
_HwXQoSIfTrustVlanID2_Object = MibTableColumn
hwXQoSIfTrustVlanID2 = _HwXQoSIfTrustVlanID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1, 3),
    _HwXQoSIfTrustVlanID2_Type()
)
hwXQoSIfTrustVlanID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfTrustVlanID2.setStatus("current")
_HwXQoSBaType_Type = BaType
_HwXQoSBaType_Object = MibTableColumn
hwXQoSBaType = _HwXQoSBaType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1, 4),
    _HwXQoSBaType_Type()
)
hwXQoSBaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSBaType.setStatus("current")


class _HwXQoSIfTrustAction_Type(Integer32):
    """Custom type hwXQoSIfTrustAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distrust", 1),
          ("trust", 2))
    )


_HwXQoSIfTrustAction_Type.__name__ = "Integer32"
_HwXQoSIfTrustAction_Object = MibTableColumn
hwXQoSIfTrustAction = _HwXQoSIfTrustAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1, 5),
    _HwXQoSIfTrustAction_Type()
)
hwXQoSIfTrustAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfTrustAction.setStatus("current")
_HwXQoSIfTrustRowStatus_Type = RowStatus
_HwXQoSIfTrustRowStatus_Object = MibTableColumn
hwXQoSIfTrustRowStatus = _HwXQoSIfTrustRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 16, 1, 6),
    _HwXQoSIfTrustRowStatus_Type()
)
hwXQoSIfTrustRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfTrustRowStatus.setStatus("current")
_HwXQoSDeiTable_Object = MibTable
hwXQoSDeiTable = _HwXQoSDeiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hwXQoSDeiTable.setStatus("current")
_HwXQoSDeiEntry_Object = MibTableRow
hwXQoSDeiEntry = _HwXQoSDeiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17, 1)
)
hwXQoSDeiEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSDeiIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSDeiVlanID1"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSDeiVlanID2"),
)
if mibBuilder.loadTexts:
    hwXQoSDeiEntry.setStatus("current")
_HwXQoSDeiIfIndex_Type = Integer32
_HwXQoSDeiIfIndex_Object = MibTableColumn
hwXQoSDeiIfIndex = _HwXQoSDeiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17, 1, 1),
    _HwXQoSDeiIfIndex_Type()
)
hwXQoSDeiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSDeiIfIndex.setStatus("current")


class _HwXQoSDeiVlanID1_Type(Integer32):
    """Custom type hwXQoSDeiVlanID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSDeiVlanID1_Type.__name__ = "Integer32"
_HwXQoSDeiVlanID1_Object = MibTableColumn
hwXQoSDeiVlanID1 = _HwXQoSDeiVlanID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17, 1, 2),
    _HwXQoSDeiVlanID1_Type()
)
hwXQoSDeiVlanID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSDeiVlanID1.setStatus("current")


class _HwXQoSDeiVlanID2_Type(Integer32):
    """Custom type hwXQoSDeiVlanID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSDeiVlanID2_Type.__name__ = "Integer32"
_HwXQoSDeiVlanID2_Object = MibTableColumn
hwXQoSDeiVlanID2 = _HwXQoSDeiVlanID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17, 1, 3),
    _HwXQoSDeiVlanID2_Type()
)
hwXQoSDeiVlanID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSDeiVlanID2.setStatus("current")


class _HwXQoSIfEnableDeiAction_Type(Integer32):
    """Custom type hwXQoSIfEnableDeiAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("unenabled", 2))
    )


_HwXQoSIfEnableDeiAction_Type.__name__ = "Integer32"
_HwXQoSIfEnableDeiAction_Object = MibTableColumn
hwXQoSIfEnableDeiAction = _HwXQoSIfEnableDeiAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17, 1, 4),
    _HwXQoSIfEnableDeiAction_Type()
)
hwXQoSIfEnableDeiAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfEnableDeiAction.setStatus("current")
_HwXQoSDeiRowStatus_Type = RowStatus
_HwXQoSDeiRowStatus_Object = MibTableColumn
hwXQoSDeiRowStatus = _HwXQoSDeiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 17, 1, 5),
    _HwXQoSDeiRowStatus_Type()
)
hwXQoSDeiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSDeiRowStatus.setStatus("current")
_HwXQoSRemarkTable_Object = MibTable
hwXQoSRemarkTable = _HwXQoSRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hwXQoSRemarkTable.setStatus("current")
_HwXQoSRemarkEntry_Object = MibTableRow
hwXQoSRemarkEntry = _HwXQoSRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18, 1)
)
hwXQoSRemarkEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSRemarkIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSRemarkVlanID1"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSRemarkVlanID2"),
)
if mibBuilder.loadTexts:
    hwXQoSRemarkEntry.setStatus("current")
_HwXQoSRemarkIfIndex_Type = Integer32
_HwXQoSRemarkIfIndex_Object = MibTableColumn
hwXQoSRemarkIfIndex = _HwXQoSRemarkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18, 1, 1),
    _HwXQoSRemarkIfIndex_Type()
)
hwXQoSRemarkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSRemarkIfIndex.setStatus("current")


class _HwXQoSRemarkVlanID1_Type(Integer32):
    """Custom type hwXQoSRemarkVlanID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSRemarkVlanID1_Type.__name__ = "Integer32"
_HwXQoSRemarkVlanID1_Object = MibTableColumn
hwXQoSRemarkVlanID1 = _HwXQoSRemarkVlanID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18, 1, 2),
    _HwXQoSRemarkVlanID1_Type()
)
hwXQoSRemarkVlanID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSRemarkVlanID1.setStatus("current")


class _HwXQoSRemarkVlanID2_Type(Integer32):
    """Custom type hwXQoSRemarkVlanID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSRemarkVlanID2_Type.__name__ = "Integer32"
_HwXQoSRemarkVlanID2_Object = MibTableColumn
hwXQoSRemarkVlanID2 = _HwXQoSRemarkVlanID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18, 1, 3),
    _HwXQoSRemarkVlanID2_Type()
)
hwXQoSRemarkVlanID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSRemarkVlanID2.setStatus("current")


class _HwXQoSIfEnableRemarkAction_Type(Integer32):
    """Custom type hwXQoSIfEnableRemarkAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("unenabled", 2))
    )


_HwXQoSIfEnableRemarkAction_Type.__name__ = "Integer32"
_HwXQoSIfEnableRemarkAction_Object = MibTableColumn
hwXQoSIfEnableRemarkAction = _HwXQoSIfEnableRemarkAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18, 1, 4),
    _HwXQoSIfEnableRemarkAction_Type()
)
hwXQoSIfEnableRemarkAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfEnableRemarkAction.setStatus("current")
_HwXQoSRemarkRowStatus_Type = RowStatus
_HwXQoSRemarkRowStatus_Object = MibTableColumn
hwXQoSRemarkRowStatus = _HwXQoSRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 18, 1, 5),
    _HwXQoSRemarkRowStatus_Type()
)
hwXQoSRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSRemarkRowStatus.setStatus("current")
_HwXQoSPhbEnableTable_Object = MibTable
hwXQoSPhbEnableTable = _HwXQoSPhbEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hwXQoSPhbEnableTable.setStatus("current")
_HwXQoSPhbEnableEntry_Object = MibTableRow
hwXQoSPhbEnableEntry = _HwXQoSPhbEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 19, 1)
)
hwXQoSPhbEnableEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPhbEnableIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPhbEnableVlanID1"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPhbEnableVlanID2"),
)
if mibBuilder.loadTexts:
    hwXQoSPhbEnableEntry.setStatus("current")
_HwXQoSPhbEnableIfIndex_Type = Integer32
_HwXQoSPhbEnableIfIndex_Object = MibTableColumn
hwXQoSPhbEnableIfIndex = _HwXQoSPhbEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 19, 1, 1),
    _HwXQoSPhbEnableIfIndex_Type()
)
hwXQoSPhbEnableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSPhbEnableIfIndex.setStatus("current")


class _HwXQoSPhbEnableVlanID1_Type(Integer32):
    """Custom type hwXQoSPhbEnableVlanID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSPhbEnableVlanID1_Type.__name__ = "Integer32"
_HwXQoSPhbEnableVlanID1_Object = MibTableColumn
hwXQoSPhbEnableVlanID1 = _HwXQoSPhbEnableVlanID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 19, 1, 2),
    _HwXQoSPhbEnableVlanID1_Type()
)
hwXQoSPhbEnableVlanID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSPhbEnableVlanID1.setStatus("current")


class _HwXQoSPhbEnableVlanID2_Type(Integer32):
    """Custom type hwXQoSPhbEnableVlanID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSPhbEnableVlanID2_Type.__name__ = "Integer32"
_HwXQoSPhbEnableVlanID2_Object = MibTableColumn
hwXQoSPhbEnableVlanID2 = _HwXQoSPhbEnableVlanID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 19, 1, 3),
    _HwXQoSPhbEnableVlanID2_Type()
)
hwXQoSPhbEnableVlanID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSPhbEnableVlanID2.setStatus("current")
_HwXQoSPhbEnableRowStatus_Type = RowStatus
_HwXQoSPhbEnableRowStatus_Object = MibTableColumn
hwXQoSPhbEnableRowStatus = _HwXQoSPhbEnableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 19, 1, 4),
    _HwXQoSPhbEnableRowStatus_Type()
)
hwXQoSPhbEnableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPhbEnableRowStatus.setStatus("current")
_HwXQoSCommonInboundTable_Object = MibTable
hwXQoSCommonInboundTable = _HwXQoSCommonInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hwXQoSCommonInboundTable.setStatus("current")
_HwXQoSCommonInboundEntry_Object = MibTableRow
hwXQoSCommonInboundEntry = _HwXQoSCommonInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20, 1)
)
hwXQoSCommonInboundEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCommonInboundPhbIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCommonInboundEntry.setStatus("current")
_HwXQoSCommonInboundPhbIndex_Type = Integer32
_HwXQoSCommonInboundPhbIndex_Object = MibTableColumn
hwXQoSCommonInboundPhbIndex = _HwXQoSCommonInboundPhbIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20, 1, 1),
    _HwXQoSCommonInboundPhbIndex_Type()
)
hwXQoSCommonInboundPhbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCommonInboundPhbIndex.setStatus("current")


class _HwXQoSCommonInboundPhbCos_Type(Integer32):
    """Custom type hwXQoSCommonInboundPhbCos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSCommonInboundPhbCos_Type.__name__ = "Integer32"
_HwXQoSCommonInboundPhbCos_Object = MibTableColumn
hwXQoSCommonInboundPhbCos = _HwXQoSCommonInboundPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20, 1, 2),
    _HwXQoSCommonInboundPhbCos_Type()
)
hwXQoSCommonInboundPhbCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCommonInboundPhbCos.setStatus("current")


class _HwXQoSCommonInboundPhbColor_Type(Integer32):
    """Custom type hwXQoSCommonInboundPhbColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSCommonInboundPhbColor_Type.__name__ = "Integer32"
_HwXQoSCommonInboundPhbColor_Object = MibTableColumn
hwXQoSCommonInboundPhbColor = _HwXQoSCommonInboundPhbColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20, 1, 3),
    _HwXQoSCommonInboundPhbColor_Type()
)
hwXQoSCommonInboundPhbColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCommonInboundPhbColor.setStatus("current")


class _HwXQoSCommonInboundPhbPri_Type(Integer32):
    """Custom type hwXQoSCommonInboundPhbPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSCommonInboundPhbPri_Type.__name__ = "Integer32"
_HwXQoSCommonInboundPhbPri_Object = MibTableColumn
hwXQoSCommonInboundPhbPri = _HwXQoSCommonInboundPhbPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20, 1, 4),
    _HwXQoSCommonInboundPhbPri_Type()
)
hwXQoSCommonInboundPhbPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCommonInboundPhbPri.setStatus("current")
_HwXQoSCommonInboundRowStatus_Type = RowStatus
_HwXQoSCommonInboundRowStatus_Object = MibTableColumn
hwXQoSCommonInboundRowStatus = _HwXQoSCommonInboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 20, 1, 50),
    _HwXQoSCommonInboundRowStatus_Type()
)
hwXQoSCommonInboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCommonInboundRowStatus.setStatus("current")
_HwXQoSPppInboundTable_Object = MibTable
hwXQoSPppInboundTable = _HwXQoSPppInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 21)
)
if mibBuilder.loadTexts:
    hwXQoSPppInboundTable.setStatus("current")
_HwXQoSPppInboundEntry_Object = MibTableRow
hwXQoSPppInboundEntry = _HwXQoSPppInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 21, 1)
)
hwXQoSPppInboundEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSPppInboundEntry.setStatus("current")


class _HwXQoSPppInboundCos_Type(Integer32):
    """Custom type hwXQoSPppInboundCos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSPppInboundCos_Type.__name__ = "Integer32"
_HwXQoSPppInboundCos_Object = MibTableColumn
hwXQoSPppInboundCos = _HwXQoSPppInboundCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 21, 1, 1),
    _HwXQoSPppInboundCos_Type()
)
hwXQoSPppInboundCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPppInboundCos.setStatus("current")


class _HwXQoSPppInboundColor_Type(Integer32):
    """Custom type hwXQoSPppInboundColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSPppInboundColor_Type.__name__ = "Integer32"
_HwXQoSPppInboundColor_Object = MibTableColumn
hwXQoSPppInboundColor = _HwXQoSPppInboundColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 21, 1, 2),
    _HwXQoSPppInboundColor_Type()
)
hwXQoSPppInboundColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPppInboundColor.setStatus("current")
_HwXQoSPppInboundRowStatus_Type = RowStatus
_HwXQoSPppInboundRowStatus_Object = MibTableColumn
hwXQoSPppInboundRowStatus = _HwXQoSPppInboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 21, 1, 50),
    _HwXQoSPppInboundRowStatus_Type()
)
hwXQoSPppInboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPppInboundRowStatus.setStatus("current")
_HwXQoSServiceclassTable_Object = MibTable
hwXQoSServiceclassTable = _HwXQoSServiceclassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 22)
)
if mibBuilder.loadTexts:
    hwXQoSServiceclassTable.setStatus("current")
_HwXQoSServiceclassEntry_Object = MibTableRow
hwXQoSServiceclassEntry = _HwXQoSServiceclassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 22, 1)
)
hwXQoSServiceclassEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSServiceclassPort"),
)
if mibBuilder.loadTexts:
    hwXQoSServiceclassEntry.setStatus("current")
_HwXQoSServiceclassPort_Type = InterfaceIndex
_HwXQoSServiceclassPort_Object = MibTableColumn
hwXQoSServiceclassPort = _HwXQoSServiceclassPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 22, 1, 1),
    _HwXQoSServiceclassPort_Type()
)
hwXQoSServiceclassPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSServiceclassPort.setStatus("current")


class _HwXQoSServiceclass_Type(Integer32):
    """Custom type hwXQoSServiceclass based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSServiceclass_Type.__name__ = "Integer32"
_HwXQoSServiceclass_Object = MibTableColumn
hwXQoSServiceclass = _HwXQoSServiceclass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 22, 1, 2),
    _HwXQoSServiceclass_Type()
)
hwXQoSServiceclass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSServiceclass.setStatus("current")
_HwXQoSServiceclassRowStatus_Type = RowStatus
_HwXQoSServiceclassRowStatus_Object = MibTableColumn
hwXQoSServiceclassRowStatus = _HwXQoSServiceclassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 22, 1, 50),
    _HwXQoSServiceclassRowStatus_Type()
)
hwXQoSServiceclassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSServiceclassRowStatus.setStatus("current")
_HwXQoSPhbTable_Object = MibTable
hwXQoSPhbTable = _HwXQoSPhbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 23)
)
if mibBuilder.loadTexts:
    hwXQoSPhbTable.setStatus("current")
_HwXQoSPhbEntry_Object = MibTableRow
hwXQoSPhbEntry = _HwXQoSPhbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 23, 1)
)
hwXQoSPhbEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPhbPort"),
)
if mibBuilder.loadTexts:
    hwXQoSPhbEntry.setStatus("current")
_HwXQoSPhbPort_Type = InterfaceIndex
_HwXQoSPhbPort_Object = MibTableColumn
hwXQoSPhbPort = _HwXQoSPhbPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 23, 1, 1),
    _HwXQoSPhbPort_Type()
)
hwXQoSPhbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPhbPort.setStatus("current")


class _HwXQoSPhbEnable_Type(Integer32):
    """Custom type hwXQoSPhbEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwXQoSPhbEnable_Type.__name__ = "Integer32"
_HwXQoSPhbEnable_Object = MibTableColumn
hwXQoSPhbEnable = _HwXQoSPhbEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 23, 1, 2),
    _HwXQoSPhbEnable_Type()
)
hwXQoSPhbEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPhbEnable.setStatus("current")
_HwXQoSPhbRowStatus_Type = RowStatus
_HwXQoSPhbRowStatus_Object = MibTableColumn
hwXQoSPhbRowStatus = _HwXQoSPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 23, 1, 50),
    _HwXQoSPhbRowStatus_Type()
)
hwXQoSPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPhbRowStatus.setStatus("current")
_HwXQoSFieldDeiTable_Object = MibTable
hwXQoSFieldDeiTable = _HwXQoSFieldDeiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 24)
)
if mibBuilder.loadTexts:
    hwXQoSFieldDeiTable.setStatus("current")
_HwXQoSFieldDeiEntry_Object = MibTableRow
hwXQoSFieldDeiEntry = _HwXQoSFieldDeiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 24, 1)
)
hwXQoSFieldDeiEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSFieldDeiInterface"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSFieldDeiVlanId"),
)
if mibBuilder.loadTexts:
    hwXQoSFieldDeiEntry.setStatus("current")
_HwXQoSFieldDeiInterface_Type = InterfaceIndex
_HwXQoSFieldDeiInterface_Object = MibTableColumn
hwXQoSFieldDeiInterface = _HwXQoSFieldDeiInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 24, 1, 1),
    _HwXQoSFieldDeiInterface_Type()
)
hwXQoSFieldDeiInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSFieldDeiInterface.setStatus("current")


class _HwXQoSFieldDeiVlanId_Type(Integer32):
    """Custom type hwXQoSFieldDeiVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSFieldDeiVlanId_Type.__name__ = "Integer32"
_HwXQoSFieldDeiVlanId_Object = MibTableColumn
hwXQoSFieldDeiVlanId = _HwXQoSFieldDeiVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 24, 1, 2),
    _HwXQoSFieldDeiVlanId_Type()
)
hwXQoSFieldDeiVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSFieldDeiVlanId.setStatus("current")


class _HwXQoSFieldDeiEnabled_Type(Integer32):
    """Custom type hwXQoSFieldDeiEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwXQoSFieldDeiEnabled_Type.__name__ = "Integer32"
_HwXQoSFieldDeiEnabled_Object = MibTableColumn
hwXQoSFieldDeiEnabled = _HwXQoSFieldDeiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 24, 1, 3),
    _HwXQoSFieldDeiEnabled_Type()
)
hwXQoSFieldDeiEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSFieldDeiEnabled.setStatus("current")
_HwXQoSFieldDeiRowStatus_Type = RowStatus
_HwXQoSFieldDeiRowStatus_Object = MibTableColumn
hwXQoSFieldDeiRowStatus = _HwXQoSFieldDeiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 24, 1, 50),
    _HwXQoSFieldDeiRowStatus_Type()
)
hwXQoSFieldDeiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSFieldDeiRowStatus.setStatus("current")
_HwXQoSPicForwardingTable_Object = MibTable
hwXQoSPicForwardingTable = _HwXQoSPicForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 25)
)
if mibBuilder.loadTexts:
    hwXQoSPicForwardingTable.setStatus("current")
_HwXQoSPicForwardingEntry_Object = MibTableRow
hwXQoSPicForwardingEntry = _HwXQoSPicForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 25, 1)
)
hwXQoSPicForwardingEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPicForwardingInterface"),
)
if mibBuilder.loadTexts:
    hwXQoSPicForwardingEntry.setStatus("current")
_HwXQoSPicForwardingInterface_Type = InterfaceIndex
_HwXQoSPicForwardingInterface_Object = MibTableColumn
hwXQoSPicForwardingInterface = _HwXQoSPicForwardingInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 25, 1, 1),
    _HwXQoSPicForwardingInterface_Type()
)
hwXQoSPicForwardingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPicForwardingInterface.setStatus("current")


class _HwXQoSPicForwarding8021pValue_Type(Integer32):
    """Custom type hwXQoSPicForwarding8021pValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwXQoSPicForwarding8021pValue_Type.__name__ = "Integer32"
_HwXQoSPicForwarding8021pValue_Object = MibTableColumn
hwXQoSPicForwarding8021pValue = _HwXQoSPicForwarding8021pValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 25, 1, 2),
    _HwXQoSPicForwarding8021pValue_Type()
)
hwXQoSPicForwarding8021pValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPicForwarding8021pValue.setStatus("current")


class _HwXQoSPicForwardingPriority_Type(Integer32):
    """Custom type hwXQoSPicForwardingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("high", 1)
    )


_HwXQoSPicForwardingPriority_Type.__name__ = "Integer32"
_HwXQoSPicForwardingPriority_Object = MibTableColumn
hwXQoSPicForwardingPriority = _HwXQoSPicForwardingPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 25, 1, 3),
    _HwXQoSPicForwardingPriority_Type()
)
hwXQoSPicForwardingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPicForwardingPriority.setStatus("current")
_HwXQoSPicForwardingRowStatus_Type = RowStatus
_HwXQoSPicForwardingRowStatus_Object = MibTableColumn
hwXQoSPicForwardingRowStatus = _HwXQoSPicForwardingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 25, 1, 50),
    _HwXQoSPicForwardingRowStatus_Type()
)
hwXQoSPicForwardingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPicForwardingRowStatus.setStatus("current")
_HwXQoSCarTable_Object = MibTable
hwXQoSCarTable = _HwXQoSCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26)
)
if mibBuilder.loadTexts:
    hwXQoSCarTable.setStatus("current")
_HwXQoSCarEntry_Object = MibTableRow
hwXQoSCarEntry = _HwXQoSCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1)
)
hwXQoSCarEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarInterfaceIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarDirection"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSCarEntry.setStatus("current")
_HwXQoSCarInterfaceIndex_Type = InterfaceIndex
_HwXQoSCarInterfaceIndex_Object = MibTableColumn
hwXQoSCarInterfaceIndex = _HwXQoSCarInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 1),
    _HwXQoSCarInterfaceIndex_Type()
)
hwXQoSCarInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarInterfaceIndex.setStatus("current")


class _HwXQoSCarDirection_Type(Integer32):
    """Custom type hwXQoSCarDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwXQoSCarDirection_Type.__name__ = "Integer32"
_HwXQoSCarDirection_Object = MibTableColumn
hwXQoSCarDirection = _HwXQoSCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 2),
    _HwXQoSCarDirection_Type()
)
hwXQoSCarDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarDirection.setStatus("current")


class _HwXQoSCarVlanID_Type(Integer32):
    """Custom type hwXQoSCarVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSCarVlanID_Type.__name__ = "Integer32"
_HwXQoSCarVlanID_Object = MibTableColumn
hwXQoSCarVlanID = _HwXQoSCarVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 3),
    _HwXQoSCarVlanID_Type()
)
hwXQoSCarVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarVlanID.setStatus("current")


class _HwXQoSCarCirValue_Type(Integer32):
    """Custom type hwXQoSCarCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwXQoSCarCirValue_Type.__name__ = "Integer32"
_HwXQoSCarCirValue_Object = MibTableColumn
hwXQoSCarCirValue = _HwXQoSCarCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 4),
    _HwXQoSCarCirValue_Type()
)
hwXQoSCarCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarCirValue.setStatus("current")


class _HwXQoSCarPirValue_Type(Integer32):
    """Custom type hwXQoSCarPirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(100, 10000000),
    )


_HwXQoSCarPirValue_Type.__name__ = "Integer32"
_HwXQoSCarPirValue_Object = MibTableColumn
hwXQoSCarPirValue = _HwXQoSCarPirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 5),
    _HwXQoSCarPirValue_Type()
)
hwXQoSCarPirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarPirValue.setStatus("current")


class _HwXQoSCarCbsValue_Type(Integer32):
    """Custom type hwXQoSCarCbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 33554432),
    )


_HwXQoSCarCbsValue_Type.__name__ = "Integer32"
_HwXQoSCarCbsValue_Object = MibTableColumn
hwXQoSCarCbsValue = _HwXQoSCarCbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 6),
    _HwXQoSCarCbsValue_Type()
)
hwXQoSCarCbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarCbsValue.setStatus("current")


class _HwXQoSCarPbsValue_Type(Integer32):
    """Custom type hwXQoSCarPbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33554432),
    )


_HwXQoSCarPbsValue_Type.__name__ = "Integer32"
_HwXQoSCarPbsValue_Object = MibTableColumn
hwXQoSCarPbsValue = _HwXQoSCarPbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 7),
    _HwXQoSCarPbsValue_Type()
)
hwXQoSCarPbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarPbsValue.setStatus("current")


class _HwXQoSCarGreenAction_Type(Integer32):
    """Custom type hwXQoSCarGreenAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("null", 3),
          ("pass", 1))
    )


_HwXQoSCarGreenAction_Type.__name__ = "Integer32"
_HwXQoSCarGreenAction_Object = MibTableColumn
hwXQoSCarGreenAction = _HwXQoSCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 8),
    _HwXQoSCarGreenAction_Type()
)
hwXQoSCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarGreenAction.setStatus("current")


class _HwXQoSCarGreenServiceClass_Type(Integer32):
    """Custom type hwXQoSCarGreenServiceClass based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("null", 9))
    )


_HwXQoSCarGreenServiceClass_Type.__name__ = "Integer32"
_HwXQoSCarGreenServiceClass_Object = MibTableColumn
hwXQoSCarGreenServiceClass = _HwXQoSCarGreenServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 9),
    _HwXQoSCarGreenServiceClass_Type()
)
hwXQoSCarGreenServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarGreenServiceClass.setStatus("current")


class _HwXQoSCarGreenColor_Type(Integer32):
    """Custom type hwXQoSCarGreenColor based on Integer32"""
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
        *(("green", 1),
          ("null", 4),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSCarGreenColor_Type.__name__ = "Integer32"
_HwXQoSCarGreenColor_Object = MibTableColumn
hwXQoSCarGreenColor = _HwXQoSCarGreenColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 10),
    _HwXQoSCarGreenColor_Type()
)
hwXQoSCarGreenColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarGreenColor.setStatus("current")


class _HwXQoSCarYellowAction_Type(Integer32):
    """Custom type hwXQoSCarYellowAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("null", 3),
          ("pass", 1))
    )


_HwXQoSCarYellowAction_Type.__name__ = "Integer32"
_HwXQoSCarYellowAction_Object = MibTableColumn
hwXQoSCarYellowAction = _HwXQoSCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 11),
    _HwXQoSCarYellowAction_Type()
)
hwXQoSCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarYellowAction.setStatus("current")


class _HwXQoSCarYellowServiceClass_Type(Integer32):
    """Custom type hwXQoSCarYellowServiceClass based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("null", 9))
    )


_HwXQoSCarYellowServiceClass_Type.__name__ = "Integer32"
_HwXQoSCarYellowServiceClass_Object = MibTableColumn
hwXQoSCarYellowServiceClass = _HwXQoSCarYellowServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 12),
    _HwXQoSCarYellowServiceClass_Type()
)
hwXQoSCarYellowServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarYellowServiceClass.setStatus("current")


class _HwXQoSCarYellowColor_Type(Integer32):
    """Custom type hwXQoSCarYellowColor based on Integer32"""
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
        *(("green", 1),
          ("null", 4),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSCarYellowColor_Type.__name__ = "Integer32"
_HwXQoSCarYellowColor_Object = MibTableColumn
hwXQoSCarYellowColor = _HwXQoSCarYellowColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 13),
    _HwXQoSCarYellowColor_Type()
)
hwXQoSCarYellowColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarYellowColor.setStatus("current")


class _HwXQoSCarRedAction_Type(Integer32):
    """Custom type hwXQoSCarRedAction based on Integer32"""
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
        *(("discard", 2),
          ("null", 3),
          ("pass", 1))
    )


_HwXQoSCarRedAction_Type.__name__ = "Integer32"
_HwXQoSCarRedAction_Object = MibTableColumn
hwXQoSCarRedAction = _HwXQoSCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 14),
    _HwXQoSCarRedAction_Type()
)
hwXQoSCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarRedAction.setStatus("current")


class _HwXQoSCarRedServiceClass_Type(Integer32):
    """Custom type hwXQoSCarRedServiceClass based on Integer32"""
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
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6),
          ("null", 9))
    )


_HwXQoSCarRedServiceClass_Type.__name__ = "Integer32"
_HwXQoSCarRedServiceClass_Object = MibTableColumn
hwXQoSCarRedServiceClass = _HwXQoSCarRedServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 15),
    _HwXQoSCarRedServiceClass_Type()
)
hwXQoSCarRedServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarRedServiceClass.setStatus("current")


class _HwXQoSCarRedColor_Type(Integer32):
    """Custom type hwXQoSCarRedColor based on Integer32"""
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
        *(("green", 1),
          ("null", 4),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSCarRedColor_Type.__name__ = "Integer32"
_HwXQoSCarRedColor_Object = MibTableColumn
hwXQoSCarRedColor = _HwXQoSCarRedColor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 16),
    _HwXQoSCarRedColor_Type()
)
hwXQoSCarRedColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarRedColor.setStatus("current")
_HwXQoSCarRowStatus_Type = RowStatus
_HwXQoSCarRowStatus_Object = MibTableColumn
hwXQoSCarRowStatus = _HwXQoSCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 26, 1, 50),
    _HwXQoSCarRowStatus_Type()
)
hwXQoSCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarRowStatus.setStatus("current")
_HwXQoSPortShapingTable_Object = MibTable
hwXQoSPortShapingTable = _HwXQoSPortShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 27)
)
if mibBuilder.loadTexts:
    hwXQoSPortShapingTable.setStatus("current")
_HwXQoSPortShapingEntry_Object = MibTableRow
hwXQoSPortShapingEntry = _HwXQoSPortShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 27, 1)
)
hwXQoSPortShapingEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPortShapingInterface"),
)
if mibBuilder.loadTexts:
    hwXQoSPortShapingEntry.setStatus("current")
_HwXQoSPortShapingInterface_Type = InterfaceIndex
_HwXQoSPortShapingInterface_Object = MibTableColumn
hwXQoSPortShapingInterface = _HwXQoSPortShapingInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 27, 1, 1),
    _HwXQoSPortShapingInterface_Type()
)
hwXQoSPortShapingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortShapingInterface.setStatus("current")


class _HwXQoSPortShapingValue_Type(OctetString):
    """Custom type hwXQoSPortShapingValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HwXQoSPortShapingValue_Type.__name__ = "OctetString"
_HwXQoSPortShapingValue_Object = MibTableColumn
hwXQoSPortShapingValue = _HwXQoSPortShapingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 27, 1, 2),
    _HwXQoSPortShapingValue_Type()
)
hwXQoSPortShapingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPortShapingValue.setStatus("current")


class _HwXQoSPortShapingPbsValue_Type(Integer32):
    """Custom type hwXQoSPortShapingPbsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262144),
    )


_HwXQoSPortShapingPbsValue_Type.__name__ = "Integer32"
_HwXQoSPortShapingPbsValue_Object = MibTableColumn
hwXQoSPortShapingPbsValue = _HwXQoSPortShapingPbsValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 27, 1, 3),
    _HwXQoSPortShapingPbsValue_Type()
)
hwXQoSPortShapingPbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPortShapingPbsValue.setStatus("current")
_HwXQoSPortShapingRowStatus_Type = RowStatus
_HwXQoSPortShapingRowStatus_Object = MibTableColumn
hwXQoSPortShapingRowStatus = _HwXQoSPortShapingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 27, 1, 50),
    _HwXQoSPortShapingRowStatus_Type()
)
hwXQoSPortShapingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPortShapingRowStatus.setStatus("current")
_HwXQoSQueueTable_Object = MibTable
hwXQoSQueueTable = _HwXQoSQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28)
)
if mibBuilder.loadTexts:
    hwXQoSQueueTable.setStatus("current")
_HwXQoSQueueEntry_Object = MibTableRow
hwXQoSQueueEntry = _HwXQoSQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1)
)
hwXQoSQueueEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQueueInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSQueueEntry.setStatus("current")
_HwXQoSQueueInterfaceIndex_Type = InterfaceIndex
_HwXQoSQueueInterfaceIndex_Object = MibTableColumn
hwXQoSQueueInterfaceIndex = _HwXQoSQueueInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1, 1),
    _HwXQoSQueueInterfaceIndex_Type()
)
hwXQoSQueueInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQueueInterfaceIndex.setStatus("current")


class _HwXQoSQueueServiceClass_Type(Integer32):
    """Custom type hwXQoSQueueServiceClass based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSQueueServiceClass_Type.__name__ = "Integer32"
_HwXQoSQueueServiceClass_Object = MibTableColumn
hwXQoSQueueServiceClass = _HwXQoSQueueServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1, 2),
    _HwXQoSQueueServiceClass_Type()
)
hwXQoSQueueServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSQueueServiceClass.setStatus("current")


class _HwXQoSQueueCirValue_Type(Integer32):
    """Custom type hwXQoSQueueCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwXQoSQueueCirValue_Type.__name__ = "Integer32"
_HwXQoSQueueCirValue_Object = MibTableColumn
hwXQoSQueueCirValue = _HwXQoSQueueCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1, 3),
    _HwXQoSQueueCirValue_Type()
)
hwXQoSQueueCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSQueueCirValue.setStatus("current")


class _HwXQoSQueueCirPercentage_Type(Integer32):
    """Custom type hwXQoSQueueCirPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwXQoSQueueCirPercentage_Type.__name__ = "Integer32"
_HwXQoSQueueCirPercentage_Object = MibTableColumn
hwXQoSQueueCirPercentage = _HwXQoSQueueCirPercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1, 4),
    _HwXQoSQueueCirPercentage_Type()
)
hwXQoSQueueCirPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSQueueCirPercentage.setStatus("current")


class _HwXQoSQueueDirection_Type(Integer32):
    """Custom type hwXQoSQueueDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwXQoSQueueDirection_Type.__name__ = "Integer32"
_HwXQoSQueueDirection_Object = MibTableColumn
hwXQoSQueueDirection = _HwXQoSQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1, 5),
    _HwXQoSQueueDirection_Type()
)
hwXQoSQueueDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSQueueDirection.setStatus("current")
_HwXQoSQueueRowStatus_Type = RowStatus
_HwXQoSQueueRowStatus_Object = MibTableColumn
hwXQoSQueueRowStatus = _HwXQoSQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 28, 1, 6),
    _HwXQoSQueueRowStatus_Type()
)
hwXQoSQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSQueueRowStatus.setStatus("current")
_HwXQoSCarStatisticsTable_Object = MibTable
hwXQoSCarStatisticsTable = _HwXQoSCarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29)
)
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsTable.setStatus("current")
_HwXQoSCarStatisticsEntry_Object = MibTableRow
hwXQoSCarStatisticsEntry = _HwXQoSCarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1)
)
hwXQoSCarStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsInterfaceIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsDirection"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsVlanid"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsSlotNumber"),
)
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsEntry.setStatus("current")
_HwXQoSCarStatisticsInterfaceIndex_Type = InterfaceIndex
_HwXQoSCarStatisticsInterfaceIndex_Object = MibTableColumn
hwXQoSCarStatisticsInterfaceIndex = _HwXQoSCarStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 1),
    _HwXQoSCarStatisticsInterfaceIndex_Type()
)
hwXQoSCarStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsInterfaceIndex.setStatus("current")


class _HwXQoSCarStatisticsDirection_Type(Integer32):
    """Custom type hwXQoSCarStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwXQoSCarStatisticsDirection_Type.__name__ = "Integer32"
_HwXQoSCarStatisticsDirection_Object = MibTableColumn
hwXQoSCarStatisticsDirection = _HwXQoSCarStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 2),
    _HwXQoSCarStatisticsDirection_Type()
)
hwXQoSCarStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsDirection.setStatus("current")


class _HwXQoSCarStatisticsVlanid_Type(Integer32):
    """Custom type hwXQoSCarStatisticsVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwXQoSCarStatisticsVlanid_Type.__name__ = "Integer32"
_HwXQoSCarStatisticsVlanid_Object = MibTableColumn
hwXQoSCarStatisticsVlanid = _HwXQoSCarStatisticsVlanid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 3),
    _HwXQoSCarStatisticsVlanid_Type()
)
hwXQoSCarStatisticsVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsVlanid.setStatus("current")


class _HwXQoSCarStatisticsSlotNumber_Type(Integer32):
    """Custom type hwXQoSCarStatisticsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwXQoSCarStatisticsSlotNumber_Type.__name__ = "Integer32"
_HwXQoSCarStatisticsSlotNumber_Object = MibTableColumn
hwXQoSCarStatisticsSlotNumber = _HwXQoSCarStatisticsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 4),
    _HwXQoSCarStatisticsSlotNumber_Type()
)
hwXQoSCarStatisticsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsSlotNumber.setStatus("current")


class _HwXQoSCarStatisticsReset_Type(Integer32):
    """Custom type hwXQoSCarStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwXQoSCarStatisticsReset_Type.__name__ = "Integer32"
_HwXQoSCarStatisticsReset_Object = MibTableColumn
hwXQoSCarStatisticsReset = _HwXQoSCarStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 5),
    _HwXQoSCarStatisticsReset_Type()
)
hwXQoSCarStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsReset.setStatus("current")
_HwXQoSCarStatisticsPassPackets_Type = Counter64
_HwXQoSCarStatisticsPassPackets_Object = MibTableColumn
hwXQoSCarStatisticsPassPackets = _HwXQoSCarStatisticsPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 6),
    _HwXQoSCarStatisticsPassPackets_Type()
)
hwXQoSCarStatisticsPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsPassPackets.setStatus("current")
_HwXQoSCarStatisticsPassBytes_Type = Counter64
_HwXQoSCarStatisticsPassBytes_Object = MibTableColumn
hwXQoSCarStatisticsPassBytes = _HwXQoSCarStatisticsPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 7),
    _HwXQoSCarStatisticsPassBytes_Type()
)
hwXQoSCarStatisticsPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsPassBytes.setStatus("current")
_HwXQoSCarStatisticsDropPackets_Type = Counter64
_HwXQoSCarStatisticsDropPackets_Object = MibTableColumn
hwXQoSCarStatisticsDropPackets = _HwXQoSCarStatisticsDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 8),
    _HwXQoSCarStatisticsDropPackets_Type()
)
hwXQoSCarStatisticsDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsDropPackets.setStatus("current")
_HwXQoSCarStatisticsDropBytes_Type = Counter64
_HwXQoSCarStatisticsDropBytes_Object = MibTableColumn
hwXQoSCarStatisticsDropBytes = _HwXQoSCarStatisticsDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 9),
    _HwXQoSCarStatisticsDropBytes_Type()
)
hwXQoSCarStatisticsDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsDropBytes.setStatus("current")
_HwXQoSCarStatisticsPassPacketsRate_Type = Counter64
_HwXQoSCarStatisticsPassPacketsRate_Object = MibTableColumn
hwXQoSCarStatisticsPassPacketsRate = _HwXQoSCarStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 10),
    _HwXQoSCarStatisticsPassPacketsRate_Type()
)
hwXQoSCarStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsPassPacketsRate.setStatus("current")
_HwXQoSCarStatisticsPassBytesRate_Type = Counter64
_HwXQoSCarStatisticsPassBytesRate_Object = MibTableColumn
hwXQoSCarStatisticsPassBytesRate = _HwXQoSCarStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 11),
    _HwXQoSCarStatisticsPassBytesRate_Type()
)
hwXQoSCarStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsPassBytesRate.setStatus("current")
_HwXQoSCarStatisticsDropPacketsRate_Type = Counter64
_HwXQoSCarStatisticsDropPacketsRate_Object = MibTableColumn
hwXQoSCarStatisticsDropPacketsRate = _HwXQoSCarStatisticsDropPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 12),
    _HwXQoSCarStatisticsDropPacketsRate_Type()
)
hwXQoSCarStatisticsDropPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsDropPacketsRate.setStatus("current")
_HwXQoSCarStatisticsDropBytesRate_Type = Counter64
_HwXQoSCarStatisticsDropBytesRate_Object = MibTableColumn
hwXQoSCarStatisticsDropBytesRate = _HwXQoSCarStatisticsDropBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 29, 1, 13),
    _HwXQoSCarStatisticsDropBytesRate_Type()
)
hwXQoSCarStatisticsDropBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsDropBytesRate.setStatus("current")
_HwXQoSCpRateLimitTable_Object = MibTable
hwXQoSCpRateLimitTable = _HwXQoSCpRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30)
)
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitTable.setStatus("current")
_HwXQoSCpRateLimitEntry_Object = MibTableRow
hwXQoSCpRateLimitEntry = _HwXQoSCpRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1)
)
hwXQoSCpRateLimitEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitPeVidValue"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitCeVidBegin"),
)
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitEntry.setStatus("current")
_HwXQoSCpRateLimitIfIndex_Type = InterfaceIndex
_HwXQoSCpRateLimitIfIndex_Object = MibTableColumn
hwXQoSCpRateLimitIfIndex = _HwXQoSCpRateLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 1),
    _HwXQoSCpRateLimitIfIndex_Type()
)
hwXQoSCpRateLimitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitIfIndex.setStatus("current")


class _HwXQoSCpRateLimitPeVidValue_Type(Integer32):
    """Custom type hwXQoSCpRateLimitPeVidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwXQoSCpRateLimitPeVidValue_Type.__name__ = "Integer32"
_HwXQoSCpRateLimitPeVidValue_Object = MibTableColumn
hwXQoSCpRateLimitPeVidValue = _HwXQoSCpRateLimitPeVidValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 2),
    _HwXQoSCpRateLimitPeVidValue_Type()
)
hwXQoSCpRateLimitPeVidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitPeVidValue.setStatus("current")


class _HwXQoSCpRateLimitCeVidBegin_Type(Integer32):
    """Custom type hwXQoSCpRateLimitCeVidBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwXQoSCpRateLimitCeVidBegin_Type.__name__ = "Integer32"
_HwXQoSCpRateLimitCeVidBegin_Object = MibTableColumn
hwXQoSCpRateLimitCeVidBegin = _HwXQoSCpRateLimitCeVidBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 3),
    _HwXQoSCpRateLimitCeVidBegin_Type()
)
hwXQoSCpRateLimitCeVidBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitCeVidBegin.setStatus("current")


class _HwXQoSCpRateLimitCeVidEnd_Type(Integer32):
    """Custom type hwXQoSCpRateLimitCeVidEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwXQoSCpRateLimitCeVidEnd_Type.__name__ = "Integer32"
_HwXQoSCpRateLimitCeVidEnd_Object = MibTableColumn
hwXQoSCpRateLimitCeVidEnd = _HwXQoSCpRateLimitCeVidEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 4),
    _HwXQoSCpRateLimitCeVidEnd_Type()
)
hwXQoSCpRateLimitCeVidEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitCeVidEnd.setStatus("current")


class _HwXQoSCpRateLimitType_Type(Integer32):
    """Custom type hwXQoSCpRateLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("igmp", 1)
    )


_HwXQoSCpRateLimitType_Type.__name__ = "Integer32"
_HwXQoSCpRateLimitType_Object = MibTableColumn
hwXQoSCpRateLimitType = _HwXQoSCpRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 5),
    _HwXQoSCpRateLimitType_Type()
)
hwXQoSCpRateLimitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitType.setStatus("current")


class _HwXQoSCpRateLimitIgmpCir_Type(Integer32):
    """Custom type hwXQoSCpRateLimitIgmpCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 1000000),
    )


_HwXQoSCpRateLimitIgmpCir_Type.__name__ = "Integer32"
_HwXQoSCpRateLimitIgmpCir_Object = MibTableColumn
hwXQoSCpRateLimitIgmpCir = _HwXQoSCpRateLimitIgmpCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 6),
    _HwXQoSCpRateLimitIgmpCir_Type()
)
hwXQoSCpRateLimitIgmpCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitIgmpCir.setStatus("current")


class _HwXQoSCpRateLimitIgmpCbs_Type(Integer32):
    """Custom type hwXQoSCpRateLimitIgmpCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 33554432),
    )


_HwXQoSCpRateLimitIgmpCbs_Type.__name__ = "Integer32"
_HwXQoSCpRateLimitIgmpCbs_Object = MibTableColumn
hwXQoSCpRateLimitIgmpCbs = _HwXQoSCpRateLimitIgmpCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 7),
    _HwXQoSCpRateLimitIgmpCbs_Type()
)
hwXQoSCpRateLimitIgmpCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitIgmpCbs.setStatus("current")
_HwXQoSCpRateLimitRowStatus_Type = RowStatus
_HwXQoSCpRateLimitRowStatus_Object = MibTableColumn
hwXQoSCpRateLimitRowStatus = _HwXQoSCpRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 30, 1, 50),
    _HwXQoSCpRateLimitRowStatus_Type()
)
hwXQoSCpRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitRowStatus.setStatus("current")
_HwXQoSPortQueueStatisticsTable_Object = MibTable
hwXQoSPortQueueStatisticsTable = _HwXQoSPortQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31)
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsTable.setStatus("current")
_HwXQoSPortQueueStatisticsEntry_Object = MibTableRow
hwXQoSPortQueueStatisticsEntry = _HwXQoSPortQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1)
)
hwXQoSPortQueueStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsInterfaceIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDirection"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsEntry.setStatus("current")
_HwXQoSPortQueueStatisticsInterfaceIndex_Type = InterfaceIndex
_HwXQoSPortQueueStatisticsInterfaceIndex_Object = MibTableColumn
hwXQoSPortQueueStatisticsInterfaceIndex = _HwXQoSPortQueueStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 1),
    _HwXQoSPortQueueStatisticsInterfaceIndex_Type()
)
hwXQoSPortQueueStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsInterfaceIndex.setStatus("current")


class _HwXQoSPortQueueStatisticsDirection_Type(Integer32):
    """Custom type hwXQoSPortQueueStatisticsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwXQoSPortQueueStatisticsDirection_Type.__name__ = "Integer32"
_HwXQoSPortQueueStatisticsDirection_Object = MibTableColumn
hwXQoSPortQueueStatisticsDirection = _HwXQoSPortQueueStatisticsDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 2),
    _HwXQoSPortQueueStatisticsDirection_Type()
)
hwXQoSPortQueueStatisticsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDirection.setStatus("current")


class _HwXQoSPortQueueStatisticsQueueIndex_Type(Integer32):
    """Custom type hwXQoSPortQueueStatisticsQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSPortQueueStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwXQoSPortQueueStatisticsQueueIndex_Object = MibTableColumn
hwXQoSPortQueueStatisticsQueueIndex = _HwXQoSPortQueueStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 3),
    _HwXQoSPortQueueStatisticsQueueIndex_Type()
)
hwXQoSPortQueueStatisticsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsQueueIndex.setStatus("current")


class _HwXQoSPortQueueStatisticsReset_Type(Integer32):
    """Custom type hwXQoSPortQueueStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwXQoSPortQueueStatisticsReset_Type.__name__ = "Integer32"
_HwXQoSPortQueueStatisticsReset_Object = MibTableColumn
hwXQoSPortQueueStatisticsReset = _HwXQoSPortQueueStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 4),
    _HwXQoSPortQueueStatisticsReset_Type()
)
hwXQoSPortQueueStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsReset.setStatus("current")
_HwXQoSPortQueueStatisticsTotalPassPackets_Type = Counter64
_HwXQoSPortQueueStatisticsTotalPassPackets_Object = MibTableColumn
hwXQoSPortQueueStatisticsTotalPassPackets = _HwXQoSPortQueueStatisticsTotalPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 5),
    _HwXQoSPortQueueStatisticsTotalPassPackets_Type()
)
hwXQoSPortQueueStatisticsTotalPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsTotalPassPackets.setStatus("current")
_HwXQoSPortQueueStatisticsTotalPassBytes_Type = Counter64
_HwXQoSPortQueueStatisticsTotalPassBytes_Object = MibTableColumn
hwXQoSPortQueueStatisticsTotalPassBytes = _HwXQoSPortQueueStatisticsTotalPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 6),
    _HwXQoSPortQueueStatisticsTotalPassBytes_Type()
)
hwXQoSPortQueueStatisticsTotalPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsTotalPassBytes.setStatus("current")
_HwXQoSPortQueueStatisticsTotalDiscardPackets_Type = Counter64
_HwXQoSPortQueueStatisticsTotalDiscardPackets_Object = MibTableColumn
hwXQoSPortQueueStatisticsTotalDiscardPackets = _HwXQoSPortQueueStatisticsTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 7),
    _HwXQoSPortQueueStatisticsTotalDiscardPackets_Type()
)
hwXQoSPortQueueStatisticsTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsTotalDiscardPackets.setStatus("current")
_HwXQoSPortQueueStatisticsTotalDiscardBytes_Type = Counter64
_HwXQoSPortQueueStatisticsTotalDiscardBytes_Object = MibTableColumn
hwXQoSPortQueueStatisticsTotalDiscardBytes = _HwXQoSPortQueueStatisticsTotalDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 8),
    _HwXQoSPortQueueStatisticsTotalDiscardBytes_Type()
)
hwXQoSPortQueueStatisticsTotalDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsTotalDiscardBytes.setStatus("current")
_HwXQoSPortQueueStatisticsDropTailDiscardPackets_Type = Counter64
_HwXQoSPortQueueStatisticsDropTailDiscardPackets_Object = MibTableColumn
hwXQoSPortQueueStatisticsDropTailDiscardPackets = _HwXQoSPortQueueStatisticsDropTailDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 9),
    _HwXQoSPortQueueStatisticsDropTailDiscardPackets_Type()
)
hwXQoSPortQueueStatisticsDropTailDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDropTailDiscardPackets.setStatus("current")
_HwXQoSPortQueueStatisticsDropTailDiscardBytes_Type = Counter64
_HwXQoSPortQueueStatisticsDropTailDiscardBytes_Object = MibTableColumn
hwXQoSPortQueueStatisticsDropTailDiscardBytes = _HwXQoSPortQueueStatisticsDropTailDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 10),
    _HwXQoSPortQueueStatisticsDropTailDiscardBytes_Type()
)
hwXQoSPortQueueStatisticsDropTailDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDropTailDiscardBytes.setStatus("current")
_HwXQoSPortQueueStatisticsWredDiscardPackets_Type = Counter64
_HwXQoSPortQueueStatisticsWredDiscardPackets_Object = MibTableColumn
hwXQoSPortQueueStatisticsWredDiscardPackets = _HwXQoSPortQueueStatisticsWredDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 11),
    _HwXQoSPortQueueStatisticsWredDiscardPackets_Type()
)
hwXQoSPortQueueStatisticsWredDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsWredDiscardPackets.setStatus("current")
_HwXQoSPortQueueStatisticsWredDiscardBytes_Type = Counter64
_HwXQoSPortQueueStatisticsWredDiscardBytes_Object = MibTableColumn
hwXQoSPortQueueStatisticsWredDiscardBytes = _HwXQoSPortQueueStatisticsWredDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 12),
    _HwXQoSPortQueueStatisticsWredDiscardBytes_Type()
)
hwXQoSPortQueueStatisticsWredDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsWredDiscardBytes.setStatus("current")
_HwXQoSPortQueueStatisticsPassPacketsRate_Type = Counter64
_HwXQoSPortQueueStatisticsPassPacketsRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsPassPacketsRate = _HwXQoSPortQueueStatisticsPassPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 13),
    _HwXQoSPortQueueStatisticsPassPacketsRate_Type()
)
hwXQoSPortQueueStatisticsPassPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsPassPacketsRate.setStatus("current")
_HwXQoSPortQueueStatisticsPassBytesRate_Type = Counter64
_HwXQoSPortQueueStatisticsPassBytesRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsPassBytesRate = _HwXQoSPortQueueStatisticsPassBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 14),
    _HwXQoSPortQueueStatisticsPassBytesRate_Type()
)
hwXQoSPortQueueStatisticsPassBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsPassBytesRate.setStatus("current")
_HwXQoSPortQueueStatisticsDiscardPacketsRate_Type = Counter64
_HwXQoSPortQueueStatisticsDiscardPacketsRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsDiscardPacketsRate = _HwXQoSPortQueueStatisticsDiscardPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 15),
    _HwXQoSPortQueueStatisticsDiscardPacketsRate_Type()
)
hwXQoSPortQueueStatisticsDiscardPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDiscardPacketsRate.setStatus("current")
_HwXQoSPortQueueStatisticsDiscardBytesRate_Type = Counter64
_HwXQoSPortQueueStatisticsDiscardBytesRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsDiscardBytesRate = _HwXQoSPortQueueStatisticsDiscardBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 16),
    _HwXQoSPortQueueStatisticsDiscardBytesRate_Type()
)
hwXQoSPortQueueStatisticsDiscardBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDiscardBytesRate.setStatus("current")
_HwXQoSPortQueueStatisticsDropTailDiscardPacketsRate_Type = Counter64
_HwXQoSPortQueueStatisticsDropTailDiscardPacketsRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsDropTailDiscardPacketsRate = _HwXQoSPortQueueStatisticsDropTailDiscardPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 17),
    _HwXQoSPortQueueStatisticsDropTailDiscardPacketsRate_Type()
)
hwXQoSPortQueueStatisticsDropTailDiscardPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDropTailDiscardPacketsRate.setStatus("current")
_HwXQoSPortQueueStatisticsDropTailDiscardBytesRate_Type = Counter64
_HwXQoSPortQueueStatisticsDropTailDiscardBytesRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsDropTailDiscardBytesRate = _HwXQoSPortQueueStatisticsDropTailDiscardBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 18),
    _HwXQoSPortQueueStatisticsDropTailDiscardBytesRate_Type()
)
hwXQoSPortQueueStatisticsDropTailDiscardBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsDropTailDiscardBytesRate.setStatus("current")
_HwXQoSPortQueueStatisticsWredDiscardPacketsRate_Type = Counter64
_HwXQoSPortQueueStatisticsWredDiscardPacketsRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsWredDiscardPacketsRate = _HwXQoSPortQueueStatisticsWredDiscardPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 19),
    _HwXQoSPortQueueStatisticsWredDiscardPacketsRate_Type()
)
hwXQoSPortQueueStatisticsWredDiscardPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsWredDiscardPacketsRate.setStatus("current")
_HwXQoSPortQueueStatisticsWredDiscardBytesRate_Type = Counter64
_HwXQoSPortQueueStatisticsWredDiscardBytesRate_Object = MibTableColumn
hwXQoSPortQueueStatisticsWredDiscardBytesRate = _HwXQoSPortQueueStatisticsWredDiscardBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 31, 1, 20),
    _HwXQoSPortQueueStatisticsWredDiscardBytesRate_Type()
)
hwXQoSPortQueueStatisticsWredDiscardBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsWredDiscardBytesRate.setStatus("current")
_HwXQoSMulBa8021pPhbCfgInfoTable_Object = MibTable
hwXQoSMulBa8021pPhbCfgInfoTable = _HwXQoSMulBa8021pPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 32)
)
if mibBuilder.loadTexts:
    hwXQoSMulBa8021pPhbCfgInfoTable.setStatus("current")
_HwXQoSMulBa8021pPhbCfgInfoEntry_Object = MibTableRow
hwXQoSMulBa8021pPhbCfgInfoEntry = _HwXQoSMulBa8021pPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 32, 1)
)
hwXQoSMulBa8021pPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSMulBa8021pPhbIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSMulBa8021pPri"),
)
if mibBuilder.loadTexts:
    hwXQoSMulBa8021pPhbCfgInfoEntry.setStatus("current")
_HwXQoSMulBa8021pPhbIndex_Type = Integer32
_HwXQoSMulBa8021pPhbIndex_Object = MibTableColumn
hwXQoSMulBa8021pPhbIndex = _HwXQoSMulBa8021pPhbIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 32, 1, 1),
    _HwXQoSMulBa8021pPhbIndex_Type()
)
hwXQoSMulBa8021pPhbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSMulBa8021pPhbIndex.setStatus("current")


class _HwXQoSMulBa8021pPri_Type(Integer32):
    """Custom type hwXQoSMulBa8021pPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSMulBa8021pPri_Type.__name__ = "Integer32"
_HwXQoSMulBa8021pPri_Object = MibTableColumn
hwXQoSMulBa8021pPri = _HwXQoSMulBa8021pPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 32, 1, 2),
    _HwXQoSMulBa8021pPri_Type()
)
hwXQoSMulBa8021pPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSMulBa8021pPri.setStatus("current")


class _HwXQoSMulBa8021pPhbCos_Type(Integer32):
    """Custom type hwXQoSMulBa8021pPhbCos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSMulBa8021pPhbCos_Type.__name__ = "Integer32"
_HwXQoSMulBa8021pPhbCos_Object = MibTableColumn
hwXQoSMulBa8021pPhbCos = _HwXQoSMulBa8021pPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 32, 1, 3),
    _HwXQoSMulBa8021pPhbCos_Type()
)
hwXQoSMulBa8021pPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSMulBa8021pPhbCos.setStatus("current")
_HwXQoSMulBa8021pPhbRowStatus_Type = RowStatus
_HwXQoSMulBa8021pPhbRowStatus_Object = MibTableColumn
hwXQoSMulBa8021pPhbRowStatus = _HwXQoSMulBa8021pPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 32, 1, 50),
    _HwXQoSMulBa8021pPhbRowStatus_Type()
)
hwXQoSMulBa8021pPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSMulBa8021pPhbRowStatus.setStatus("current")
_HwXQoSMulDscpPhbCfgInfoTable_Object = MibTable
hwXQoSMulDscpPhbCfgInfoTable = _HwXQoSMulDscpPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 33)
)
if mibBuilder.loadTexts:
    hwXQoSMulDscpPhbCfgInfoTable.setStatus("current")
_HwXQoSMulDscpPhbCfgInfoEntry_Object = MibTableRow
hwXQoSMulDscpPhbCfgInfoEntry = _HwXQoSMulDscpPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 33, 1)
)
hwXQoSMulDscpPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSMulBaDscpPhbIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSMulBaDscpPri"),
)
if mibBuilder.loadTexts:
    hwXQoSMulDscpPhbCfgInfoEntry.setStatus("current")
_HwXQoSMulBaDscpPhbIndex_Type = Integer32
_HwXQoSMulBaDscpPhbIndex_Object = MibTableColumn
hwXQoSMulBaDscpPhbIndex = _HwXQoSMulBaDscpPhbIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 33, 1, 1),
    _HwXQoSMulBaDscpPhbIndex_Type()
)
hwXQoSMulBaDscpPhbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSMulBaDscpPhbIndex.setStatus("current")


class _HwXQoSMulBaDscpPri_Type(Integer32):
    """Custom type hwXQoSMulBaDscpPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwXQoSMulBaDscpPri_Type.__name__ = "Integer32"
_HwXQoSMulBaDscpPri_Object = MibTableColumn
hwXQoSMulBaDscpPri = _HwXQoSMulBaDscpPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 33, 1, 2),
    _HwXQoSMulBaDscpPri_Type()
)
hwXQoSMulBaDscpPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSMulBaDscpPri.setStatus("current")


class _HwXQoSMulBaDscpPhbCos_Type(Integer32):
    """Custom type hwXQoSMulBaDscpPhbCos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSMulBaDscpPhbCos_Type.__name__ = "Integer32"
_HwXQoSMulBaDscpPhbCos_Object = MibTableColumn
hwXQoSMulBaDscpPhbCos = _HwXQoSMulBaDscpPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 33, 1, 3),
    _HwXQoSMulBaDscpPhbCos_Type()
)
hwXQoSMulBaDscpPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSMulBaDscpPhbCos.setStatus("current")
_HwXQoSMulBaDscpPhbRowStatus_Type = RowStatus
_HwXQoSMulBaDscpPhbRowStatus_Object = MibTableColumn
hwXQoSMulBaDscpPhbRowStatus = _HwXQoSMulBaDscpPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 33, 1, 50),
    _HwXQoSMulBaDscpPhbRowStatus_Type()
)
hwXQoSMulBaDscpPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSMulBaDscpPhbRowStatus.setStatus("current")
_HwXQoSBaUserPriPhbCfgInfoTable_Object = MibTable
hwXQoSBaUserPriPhbCfgInfoTable = _HwXQoSBaUserPriPhbCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34)
)
if mibBuilder.loadTexts:
    hwXQoSBaUserPriPhbCfgInfoTable.setStatus("current")
_HwXQoSBaUserPriPhbCfgInfoEntry_Object = MibTableRow
hwXQoSBaUserPriPhbCfgInfoEntry = _HwXQoSBaUserPriPhbCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34, 1)
)
hwXQoSBaUserPriPhbCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSDSUserPriIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSUserPriPhbPri"),
)
if mibBuilder.loadTexts:
    hwXQoSBaUserPriPhbCfgInfoEntry.setStatus("current")
_HwXQoSDSUserPriIndex_Type = Integer32
_HwXQoSDSUserPriIndex_Object = MibTableColumn
hwXQoSDSUserPriIndex = _HwXQoSDSUserPriIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34, 1, 1),
    _HwXQoSDSUserPriIndex_Type()
)
hwXQoSDSUserPriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSDSUserPriIndex.setStatus("current")


class _HwXQoSUserPriPhbPri_Type(Integer32):
    """Custom type hwXQoSUserPriPhbPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSUserPriPhbPri_Type.__name__ = "Integer32"
_HwXQoSUserPriPhbPri_Object = MibTableColumn
hwXQoSUserPriPhbPri = _HwXQoSUserPriPhbPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34, 1, 2),
    _HwXQoSUserPriPhbPri_Type()
)
hwXQoSUserPriPhbPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSUserPriPhbPri.setStatus("current")


class _HwXQoSUserPriPhbCos_Type(Integer32):
    """Custom type hwXQoSUserPriPhbCos based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSUserPriPhbCos_Type.__name__ = "Integer32"
_HwXQoSUserPriPhbCos_Object = MibTableColumn
hwXQoSUserPriPhbCos = _HwXQoSUserPriPhbCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34, 1, 3),
    _HwXQoSUserPriPhbCos_Type()
)
hwXQoSUserPriPhbCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSUserPriPhbCos.setStatus("current")


class _HwXQoSUserPriPhbColour_Type(Integer32):
    """Custom type hwXQoSUserPriPhbColour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_HwXQoSUserPriPhbColour_Type.__name__ = "Integer32"
_HwXQoSUserPriPhbColour_Object = MibTableColumn
hwXQoSUserPriPhbColour = _HwXQoSUserPriPhbColour_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34, 1, 4),
    _HwXQoSUserPriPhbColour_Type()
)
hwXQoSUserPriPhbColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSUserPriPhbColour.setStatus("current")
_HwXQoSUserPriPhbRowStatus_Type = RowStatus
_HwXQoSUserPriPhbRowStatus_Object = MibTableColumn
hwXQoSUserPriPhbRowStatus = _HwXQoSUserPriPhbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 34, 1, 50),
    _HwXQoSUserPriPhbRowStatus_Type()
)
hwXQoSUserPriPhbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSUserPriPhbRowStatus.setStatus("current")
_HwXQoSAAATrustCfgInfoTable_Object = MibTable
hwXQoSAAATrustCfgInfoTable = _HwXQoSAAATrustCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 35)
)
if mibBuilder.loadTexts:
    hwXQoSAAATrustCfgInfoTable.setStatus("current")
_HwXQoSAAATrustCfgInfoEntry_Object = MibTableRow
hwXQoSAAATrustCfgInfoEntry = _HwXQoSAAATrustCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 35, 1)
)
hwXQoSAAATrustCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAaaDomainName"),
)
if mibBuilder.loadTexts:
    hwXQoSAAATrustCfgInfoEntry.setStatus("current")


class _HwXQoSAaaDomainName_Type(OctetString):
    """Custom type hwXQoSAaaDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSAaaDomainName_Type.__name__ = "OctetString"
_HwXQoSAaaDomainName_Object = MibTableColumn
hwXQoSAaaDomainName = _HwXQoSAaaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 35, 1, 1),
    _HwXQoSAaaDomainName_Type()
)
hwXQoSAaaDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAaaDomainName.setStatus("current")


class _HwXQoSAAADsDomainName_Type(OctetString):
    """Custom type hwXQoSAAADsDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HwXQoSAAADsDomainName_Type.__name__ = "OctetString"
_HwXQoSAAADsDomainName_Object = MibTableColumn
hwXQoSAAADsDomainName = _HwXQoSAAADsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 35, 1, 2),
    _HwXQoSAAADsDomainName_Type()
)
hwXQoSAAADsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSAAADsDomainName.setStatus("current")
_HwXQoSAAADsRowStatus_Type = RowStatus
_HwXQoSAAADsRowStatus_Object = MibTableColumn
hwXQoSAAADsRowStatus = _HwXQoSAAADsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 35, 1, 50),
    _HwXQoSAAADsRowStatus_Type()
)
hwXQoSAAADsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAAADsRowStatus.setStatus("current")
_HwXQoSAAATrust8021pInfoTable_Object = MibTable
hwXQoSAAATrust8021pInfoTable = _HwXQoSAAATrust8021pInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 36)
)
if mibBuilder.loadTexts:
    hwXQoSAAATrust8021pInfoTable.setStatus("current")
_HwXQoSAAATrust8021pInfoEntry_Object = MibTableRow
hwXQoSAAATrust8021pInfoEntry = _HwXQoSAAATrust8021pInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 36, 1)
)
hwXQoSAAATrust8021pInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAaaDomainName"),
)
if mibBuilder.loadTexts:
    hwXQoSAAATrust8021pInfoEntry.setStatus("current")


class _HwXQoSAAADs8021P_Type(Integer32):
    """Custom type hwXQoSAAADs8021P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwXQoSAAADs8021P_Type.__name__ = "Integer32"
_HwXQoSAAADs8021P_Object = MibTableColumn
hwXQoSAAADs8021P = _HwXQoSAAADs8021P_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 36, 1, 1),
    _HwXQoSAAADs8021P_Type()
)
hwXQoSAAADs8021P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSAAADs8021P.setStatus("current")
_HwXQoSAAADs8021pRowStatus_Type = RowStatus
_HwXQoSAAADs8021pRowStatus_Object = MibTableColumn
hwXQoSAAADs8021pRowStatus = _HwXQoSAAADs8021pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 36, 1, 50),
    _HwXQoSAAADs8021pRowStatus_Type()
)
hwXQoSAAADs8021pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAAADs8021pRowStatus.setStatus("current")
_HwXQoSQppbPolicyStatisticsTable_Object = MibTable
hwXQoSQppbPolicyStatisticsTable = _HwXQoSQppbPolicyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37)
)
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyStatisticsTable.setStatus("current")
_HwXQoSQppbPolicyStatisticsEntry_Object = MibTableRow
hwXQoSQppbPolicyStatisticsEntry = _HwXQoSQppbPolicyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1)
)
hwXQoSQppbPolicyStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyLocalID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyDirection"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyStatisticsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyStatisticsEntry.setStatus("current")
_HwXQoSQppbPolicyLocalID_Type = Integer32
_HwXQoSQppbPolicyLocalID_Object = MibTableColumn
hwXQoSQppbPolicyLocalID = _HwXQoSQppbPolicyLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 1),
    _HwXQoSQppbPolicyLocalID_Type()
)
hwXQoSQppbPolicyLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyLocalID.setStatus("current")


class _HwXQoSQppbPolicyDirection_Type(Integer32):
    """Custom type hwXQoSQppbPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwXQoSQppbPolicyDirection_Type.__name__ = "Integer32"
_HwXQoSQppbPolicyDirection_Object = MibTableColumn
hwXQoSQppbPolicyDirection = _HwXQoSQppbPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 2),
    _HwXQoSQppbPolicyDirection_Type()
)
hwXQoSQppbPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyDirection.setStatus("current")
_HwXQoSQppbPolicyStatisticsInterfaceIndex_Type = InterfaceIndex
_HwXQoSQppbPolicyStatisticsInterfaceIndex_Object = MibTableColumn
hwXQoSQppbPolicyStatisticsInterfaceIndex = _HwXQoSQppbPolicyStatisticsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 3),
    _HwXQoSQppbPolicyStatisticsInterfaceIndex_Type()
)
hwXQoSQppbPolicyStatisticsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyStatisticsInterfaceIndex.setStatus("current")


class _HwXQoSQppbPolicyStatisticsReset_Type(Integer32):
    """Custom type hwXQoSQppbPolicyStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwXQoSQppbPolicyStatisticsReset_Type.__name__ = "Integer32"
_HwXQoSQppbPolicyStatisticsReset_Object = MibTableColumn
hwXQoSQppbPolicyStatisticsReset = _HwXQoSQppbPolicyStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 4),
    _HwXQoSQppbPolicyStatisticsReset_Type()
)
hwXQoSQppbPolicyStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyStatisticsReset.setStatus("current")
_HwXQoSQppbPolicyMatchedPackets_Type = Counter64
_HwXQoSQppbPolicyMatchedPackets_Object = MibTableColumn
hwXQoSQppbPolicyMatchedPackets = _HwXQoSQppbPolicyMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 5),
    _HwXQoSQppbPolicyMatchedPackets_Type()
)
hwXQoSQppbPolicyMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyMatchedPackets.setStatus("current")
_HwXQoSQppbPolicyMatchedBytes_Type = Counter64
_HwXQoSQppbPolicyMatchedBytes_Object = MibTableColumn
hwXQoSQppbPolicyMatchedBytes = _HwXQoSQppbPolicyMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 6),
    _HwXQoSQppbPolicyMatchedBytes_Type()
)
hwXQoSQppbPolicyMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyMatchedBytes.setStatus("current")
_HwXQoSQppbPolicyPassedPackets_Type = Counter64
_HwXQoSQppbPolicyPassedPackets_Object = MibTableColumn
hwXQoSQppbPolicyPassedPackets = _HwXQoSQppbPolicyPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 7),
    _HwXQoSQppbPolicyPassedPackets_Type()
)
hwXQoSQppbPolicyPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyPassedPackets.setStatus("current")
_HwXQoSQppbPolicyPassedBytes_Type = Counter64
_HwXQoSQppbPolicyPassedBytes_Object = MibTableColumn
hwXQoSQppbPolicyPassedBytes = _HwXQoSQppbPolicyPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 8),
    _HwXQoSQppbPolicyPassedBytes_Type()
)
hwXQoSQppbPolicyPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyPassedBytes.setStatus("current")
_HwXQoSQppbPolicyDropedPackets_Type = Counter64
_HwXQoSQppbPolicyDropedPackets_Object = MibTableColumn
hwXQoSQppbPolicyDropedPackets = _HwXQoSQppbPolicyDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 9),
    _HwXQoSQppbPolicyDropedPackets_Type()
)
hwXQoSQppbPolicyDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyDropedPackets.setStatus("current")
_HwXQoSQppbPolicyDropedBytes_Type = Counter64
_HwXQoSQppbPolicyDropedBytes_Object = MibTableColumn
hwXQoSQppbPolicyDropedBytes = _HwXQoSQppbPolicyDropedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 10),
    _HwXQoSQppbPolicyDropedBytes_Type()
)
hwXQoSQppbPolicyDropedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyDropedBytes.setStatus("current")
_HwXQoSQppbPolicyMatchPacketsRate_Type = Counter64
_HwXQoSQppbPolicyMatchPacketsRate_Object = MibTableColumn
hwXQoSQppbPolicyMatchPacketsRate = _HwXQoSQppbPolicyMatchPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 11),
    _HwXQoSQppbPolicyMatchPacketsRate_Type()
)
hwXQoSQppbPolicyMatchPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyMatchPacketsRate.setStatus("current")
_HwXQoSQppbPolicyMatchBytesRate_Type = Counter64
_HwXQoSQppbPolicyMatchBytesRate_Object = MibTableColumn
hwXQoSQppbPolicyMatchBytesRate = _HwXQoSQppbPolicyMatchBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 37, 1, 12),
    _HwXQoSQppbPolicyMatchBytesRate_Type()
)
hwXQoSQppbPolicyMatchBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyMatchBytesRate.setStatus("current")
_HwXQoSIfPhbEnableTable_Object = MibTable
hwXQoSIfPhbEnableTable = _HwXQoSIfPhbEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 38)
)
if mibBuilder.loadTexts:
    hwXQoSIfPhbEnableTable.setStatus("current")
_HwXQoSIfPhbEnableEntry_Object = MibTableRow
hwXQoSIfPhbEnableEntry = _HwXQoSIfPhbEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 38, 1)
)
hwXQoSIfPhbEnableEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfPhbEnableIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfPhbEnableVlanId"),
)
if mibBuilder.loadTexts:
    hwXQoSIfPhbEnableEntry.setStatus("current")
_HwXQoSIfPhbEnableIfIndex_Type = Integer32
_HwXQoSIfPhbEnableIfIndex_Object = MibTableColumn
hwXQoSIfPhbEnableIfIndex = _HwXQoSIfPhbEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 38, 1, 1),
    _HwXQoSIfPhbEnableIfIndex_Type()
)
hwXQoSIfPhbEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfPhbEnableIfIndex.setStatus("current")


class _HwXQoSIfPhbEnableVlanId_Type(Integer32):
    """Custom type hwXQoSIfPhbEnableVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSIfPhbEnableVlanId_Type.__name__ = "Integer32"
_HwXQoSIfPhbEnableVlanId_Object = MibTableColumn
hwXQoSIfPhbEnableVlanId = _HwXQoSIfPhbEnableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 38, 1, 2),
    _HwXQoSIfPhbEnableVlanId_Type()
)
hwXQoSIfPhbEnableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfPhbEnableVlanId.setStatus("current")


class _HwXQoSIfPhbEnableDomainName_Type(OctetString):
    """Custom type hwXQoSIfPhbEnableDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSIfPhbEnableDomainName_Type.__name__ = "OctetString"
_HwXQoSIfPhbEnableDomainName_Object = MibTableColumn
hwXQoSIfPhbEnableDomainName = _HwXQoSIfPhbEnableDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 38, 1, 3),
    _HwXQoSIfPhbEnableDomainName_Type()
)
hwXQoSIfPhbEnableDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfPhbEnableDomainName.setStatus("current")
_HwXQoSIfPhbEnableRowStatus_Type = RowStatus
_HwXQoSIfPhbEnableRowStatus_Object = MibTableColumn
hwXQoSIfPhbEnableRowStatus = _HwXQoSIfPhbEnableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 38, 1, 4),
    _HwXQoSIfPhbEnableRowStatus_Type()
)
hwXQoSIfPhbEnableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfPhbEnableRowStatus.setStatus("current")
_HwXQoSIfRemarkDscpTable_Object = MibTable
hwXQoSIfRemarkDscpTable = _HwXQoSIfRemarkDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 39)
)
if mibBuilder.loadTexts:
    hwXQoSIfRemarkDscpTable.setStatus("current")
_HwXQoSIfRemarkDscpEntry_Object = MibTableRow
hwXQoSIfRemarkDscpEntry = _HwXQoSIfRemarkDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 39, 1)
)
hwXQoSIfRemarkDscpEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfRemarkDscpIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfRemarkDscpEntry.setStatus("current")
_HwXQoSIfRemarkDscpIfIndex_Type = Integer32
_HwXQoSIfRemarkDscpIfIndex_Object = MibTableColumn
hwXQoSIfRemarkDscpIfIndex = _HwXQoSIfRemarkDscpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 39, 1, 1),
    _HwXQoSIfRemarkDscpIfIndex_Type()
)
hwXQoSIfRemarkDscpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfRemarkDscpIfIndex.setStatus("current")
_HwXQoSIfRemarkDscpRowStatus_Type = RowStatus
_HwXQoSIfRemarkDscpRowStatus_Object = MibTableColumn
hwXQoSIfRemarkDscpRowStatus = _HwXQoSIfRemarkDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 1, 39, 1, 2),
    _HwXQoSIfRemarkDscpRowStatus_Type()
)
hwXQoSIfRemarkDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfRemarkDscpRowStatus.setStatus("current")
_HwXQoSIfActionObjects_ObjectIdentity = ObjectIdentity
hwXQoSIfActionObjects = _HwXQoSIfActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2)
)
_HwXQoSIfCarCfgInfoTable_Object = MibTable
hwXQoSIfCarCfgInfoTable = _HwXQoSIfCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwXQoSIfCarCfgInfoTable.setStatus("current")
_HwXQoSIfCarCfgInfoEntry_Object = MibTableRow
hwXQoSIfCarCfgInfoEntry = _HwXQoSIfCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1)
)
hwXQoSIfCarCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarVlanID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarDirection"),
)
if mibBuilder.loadTexts:
    hwXQoSIfCarCfgInfoEntry.setStatus("current")
_HwXQoSIfCarCfgIfIndex_Type = Integer32
_HwXQoSIfCarCfgIfIndex_Object = MibTableColumn
hwXQoSIfCarCfgIfIndex = _HwXQoSIfCarCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 1),
    _HwXQoSIfCarCfgIfIndex_Type()
)
hwXQoSIfCarCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarCfgIfIndex.setStatus("current")


class _HwXQoSIfCarVlanID_Type(Integer32):
    """Custom type hwXQoSIfCarVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfCarVlanID_Type.__name__ = "Integer32"
_HwXQoSIfCarVlanID_Object = MibTableColumn
hwXQoSIfCarVlanID = _HwXQoSIfCarVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 2),
    _HwXQoSIfCarVlanID_Type()
)
hwXQoSIfCarVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarVlanID.setStatus("current")
_HwXQoSIfCarDirection_Type = DirectionType
_HwXQoSIfCarDirection_Object = MibTableColumn
hwXQoSIfCarDirection = _HwXQoSIfCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 3),
    _HwXQoSIfCarDirection_Type()
)
hwXQoSIfCarDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarDirection.setStatus("current")
_HwXQoSIfCarCir_Type = Integer32
_HwXQoSIfCarCir_Object = MibTableColumn
hwXQoSIfCarCir = _HwXQoSIfCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 4),
    _HwXQoSIfCarCir_Type()
)
hwXQoSIfCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarCir.setStatus("current")
_HwXQoSIfCarCbs_Type = Integer32
_HwXQoSIfCarCbs_Object = MibTableColumn
hwXQoSIfCarCbs = _HwXQoSIfCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 5),
    _HwXQoSIfCarCbs_Type()
)
hwXQoSIfCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarCbs.setStatus("current")


class _HwXQoSIfCarEbs_Type(Integer32):
    """Custom type hwXQoSIfCarEbs based on Integer32"""
    defaultValue = 0


_HwXQoSIfCarEbs_Object = MibTableColumn
hwXQoSIfCarEbs = _HwXQoSIfCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 6),
    _HwXQoSIfCarEbs_Type()
)
hwXQoSIfCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarEbs.setStatus("current")
_HwXQoSIfCarPir_Type = Integer32
_HwXQoSIfCarPir_Object = MibTableColumn
hwXQoSIfCarPir = _HwXQoSIfCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 7),
    _HwXQoSIfCarPir_Type()
)
hwXQoSIfCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarPir.setStatus("current")
_HwXQoSIfCarPbs_Type = Integer32
_HwXQoSIfCarPbs_Object = MibTableColumn
hwXQoSIfCarPbs = _HwXQoSIfCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 8),
    _HwXQoSIfCarPbs_Type()
)
hwXQoSIfCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarPbs.setStatus("current")


class _HwXQoSIfCarGreenAction_Type(CarAction):
    """Custom type hwXQoSIfCarGreenAction based on CarAction"""


_HwXQoSIfCarGreenAction_Object = MibTableColumn
hwXQoSIfCarGreenAction = _HwXQoSIfCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 9),
    _HwXQoSIfCarGreenAction_Type()
)
hwXQoSIfCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenAction.setStatus("current")


class _HwXQoSIfCarGreenRemarkValue_Type(Integer32):
    """Custom type hwXQoSIfCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSIfCarGreenRemarkValue_Type.__name__ = "Integer32"
_HwXQoSIfCarGreenRemarkValue_Object = MibTableColumn
hwXQoSIfCarGreenRemarkValue = _HwXQoSIfCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 10),
    _HwXQoSIfCarGreenRemarkValue_Type()
)
hwXQoSIfCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenRemarkValue.setStatus("current")
_HwXQoSIfCarYellowAction_Type = CarAction
_HwXQoSIfCarYellowAction_Object = MibTableColumn
hwXQoSIfCarYellowAction = _HwXQoSIfCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 11),
    _HwXQoSIfCarYellowAction_Type()
)
hwXQoSIfCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowAction.setStatus("current")


class _HwXQoSIfCarYellowRemarkValue_Type(Integer32):
    """Custom type hwXQoSIfCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSIfCarYellowRemarkValue_Type.__name__ = "Integer32"
_HwXQoSIfCarYellowRemarkValue_Object = MibTableColumn
hwXQoSIfCarYellowRemarkValue = _HwXQoSIfCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 12),
    _HwXQoSIfCarYellowRemarkValue_Type()
)
hwXQoSIfCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowRemarkValue.setStatus("current")


class _HwXQoSIfCarRedAction_Type(CarAction):
    """Custom type hwXQoSIfCarRedAction based on CarAction"""


_HwXQoSIfCarRedAction_Object = MibTableColumn
hwXQoSIfCarRedAction = _HwXQoSIfCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 13),
    _HwXQoSIfCarRedAction_Type()
)
hwXQoSIfCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedAction.setStatus("current")


class _HwXQoSIfCarRedRemarkValue_Type(Integer32):
    """Custom type hwXQoSIfCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSIfCarRedRemarkValue_Type.__name__ = "Integer32"
_HwXQoSIfCarRedRemarkValue_Object = MibTableColumn
hwXQoSIfCarRedRemarkValue = _HwXQoSIfCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 14),
    _HwXQoSIfCarRedRemarkValue_Type()
)
hwXQoSIfCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedRemarkValue.setStatus("current")
_HwXQoSIfCarRowStatus_Type = RowStatus
_HwXQoSIfCarRowStatus_Object = MibTableColumn
hwXQoSIfCarRowStatus = _HwXQoSIfCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 1, 1, 15),
    _HwXQoSIfCarRowStatus_Type()
)
hwXQoSIfCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfCarRowStatus.setStatus("current")
_HwXQoSIfMirrorCfgInfoTable_Object = MibTable
hwXQoSIfMirrorCfgInfoTable = _HwXQoSIfMirrorCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwXQoSIfMirrorCfgInfoTable.setStatus("current")
_HwXQoSIfMirrorCfgInfoEntry_Object = MibTableRow
hwXQoSIfMirrorCfgInfoEntry = _HwXQoSIfMirrorCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2, 1)
)
hwXQoSIfMirrorCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMirrorCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMirrorCfgVlanID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMirrorDirection"),
)
if mibBuilder.loadTexts:
    hwXQoSIfMirrorCfgInfoEntry.setStatus("current")
_HwXQoSIfMirrorCfgIfIndex_Type = Integer32
_HwXQoSIfMirrorCfgIfIndex_Object = MibTableColumn
hwXQoSIfMirrorCfgIfIndex = _HwXQoSIfMirrorCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2, 1, 1),
    _HwXQoSIfMirrorCfgIfIndex_Type()
)
hwXQoSIfMirrorCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorCfgIfIndex.setStatus("current")


class _HwXQoSIfMirrorCfgVlanID_Type(Integer32):
    """Custom type hwXQoSIfMirrorCfgVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfMirrorCfgVlanID_Type.__name__ = "Integer32"
_HwXQoSIfMirrorCfgVlanID_Object = MibTableColumn
hwXQoSIfMirrorCfgVlanID = _HwXQoSIfMirrorCfgVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2, 1, 2),
    _HwXQoSIfMirrorCfgVlanID_Type()
)
hwXQoSIfMirrorCfgVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorCfgVlanID.setStatus("current")
_HwXQoSIfMirrorDirection_Type = DirectionType
_HwXQoSIfMirrorDirection_Object = MibTableColumn
hwXQoSIfMirrorDirection = _HwXQoSIfMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2, 1, 3),
    _HwXQoSIfMirrorDirection_Type()
)
hwXQoSIfMirrorDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorDirection.setStatus("current")


class _HwXQoSIfMirrorObserveIndex_Type(Integer32):
    """Custom type hwXQoSIfMirrorObserveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwXQoSIfMirrorObserveIndex_Type.__name__ = "Integer32"
_HwXQoSIfMirrorObserveIndex_Object = MibTableColumn
hwXQoSIfMirrorObserveIndex = _HwXQoSIfMirrorObserveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2, 1, 4),
    _HwXQoSIfMirrorObserveIndex_Type()
)
hwXQoSIfMirrorObserveIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorObserveIndex.setStatus("current")
_HwXQoSIfMirrorRowStatus_Type = RowStatus
_HwXQoSIfMirrorRowStatus_Object = MibTableColumn
hwXQoSIfMirrorRowStatus = _HwXQoSIfMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 2, 1, 5),
    _HwXQoSIfMirrorRowStatus_Type()
)
hwXQoSIfMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorRowStatus.setStatus("current")
_HwXQoSIfUrpfCfgInfoTable_Object = MibTable
hwXQoSIfUrpfCfgInfoTable = _HwXQoSIfUrpfCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwXQoSIfUrpfCfgInfoTable.setStatus("current")
_HwXQoSIfUrpfCfgInfoEntry_Object = MibTableRow
hwXQoSIfUrpfCfgInfoEntry = _HwXQoSIfUrpfCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3, 1)
)
hwXQoSIfUrpfCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfUrpfCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfUrpfCfgVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfUrpfCfgInfoEntry.setStatus("current")
_HwXQoSIfUrpfCfgIfIndex_Type = Integer32
_HwXQoSIfUrpfCfgIfIndex_Object = MibTableColumn
hwXQoSIfUrpfCfgIfIndex = _HwXQoSIfUrpfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3, 1, 1),
    _HwXQoSIfUrpfCfgIfIndex_Type()
)
hwXQoSIfUrpfCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfCfgIfIndex.setStatus("current")


class _HwXQoSIfUrpfCfgVlanID_Type(Integer32):
    """Custom type hwXQoSIfUrpfCfgVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfUrpfCfgVlanID_Type.__name__ = "Integer32"
_HwXQoSIfUrpfCfgVlanID_Object = MibTableColumn
hwXQoSIfUrpfCfgVlanID = _HwXQoSIfUrpfCfgVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3, 1, 2),
    _HwXQoSIfUrpfCfgVlanID_Type()
)
hwXQoSIfUrpfCfgVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfCfgVlanID.setStatus("current")
_HwXQoSIfUrpfCtrlType_Type = UrpfCtrlType
_HwXQoSIfUrpfCtrlType_Object = MibTableColumn
hwXQoSIfUrpfCtrlType = _HwXQoSIfUrpfCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3, 1, 3),
    _HwXQoSIfUrpfCtrlType_Type()
)
hwXQoSIfUrpfCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfCtrlType.setStatus("current")


class _HwXQoSIfUrpfAllowDefault_Type(Integer32):
    """Custom type hwXQoSIfUrpfAllowDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_HwXQoSIfUrpfAllowDefault_Type.__name__ = "Integer32"
_HwXQoSIfUrpfAllowDefault_Object = MibTableColumn
hwXQoSIfUrpfAllowDefault = _HwXQoSIfUrpfAllowDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3, 1, 4),
    _HwXQoSIfUrpfAllowDefault_Type()
)
hwXQoSIfUrpfAllowDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfAllowDefault.setStatus("current")
_HwXQoSIfUrpfRowStatus_Type = RowStatus
_HwXQoSIfUrpfRowStatus_Object = MibTableColumn
hwXQoSIfUrpfRowStatus = _HwXQoSIfUrpfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 3, 1, 5),
    _HwXQoSIfUrpfRowStatus_Type()
)
hwXQoSIfUrpfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfRowStatus.setStatus("current")
_HwXQoSIfSamplingCfgInfoTable_Object = MibTable
hwXQoSIfSamplingCfgInfoTable = _HwXQoSIfSamplingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwXQoSIfSamplingCfgInfoTable.setStatus("current")
_HwXQoSIfSamplingCfgInfoEntry_Object = MibTableRow
hwXQoSIfSamplingCfgInfoEntry = _HwXQoSIfSamplingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1)
)
hwXQoSIfSamplingCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSamplingIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSamplingVlanID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSamplingDirection"),
)
if mibBuilder.loadTexts:
    hwXQoSIfSamplingCfgInfoEntry.setStatus("current")
_HwXQoSIfSamplingIfIndex_Type = Integer32
_HwXQoSIfSamplingIfIndex_Object = MibTableColumn
hwXQoSIfSamplingIfIndex = _HwXQoSIfSamplingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1, 1),
    _HwXQoSIfSamplingIfIndex_Type()
)
hwXQoSIfSamplingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfSamplingIfIndex.setStatus("current")


class _HwXQoSIfSamplingVlanID_Type(Integer32):
    """Custom type hwXQoSIfSamplingVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfSamplingVlanID_Type.__name__ = "Integer32"
_HwXQoSIfSamplingVlanID_Object = MibTableColumn
hwXQoSIfSamplingVlanID = _HwXQoSIfSamplingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1, 2),
    _HwXQoSIfSamplingVlanID_Type()
)
hwXQoSIfSamplingVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfSamplingVlanID.setStatus("current")
_HwXQoSIfSamplingDirection_Type = DirectionType
_HwXQoSIfSamplingDirection_Object = MibTableColumn
hwXQoSIfSamplingDirection = _HwXQoSIfSamplingDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1, 3),
    _HwXQoSIfSamplingDirection_Type()
)
hwXQoSIfSamplingDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfSamplingDirection.setStatus("current")
_HwXQoSIfSamplingType_Type = SampleType
_HwXQoSIfSamplingType_Object = MibTableColumn
hwXQoSIfSamplingType = _HwXQoSIfSamplingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1, 4),
    _HwXQoSIfSamplingType_Type()
)
hwXQoSIfSamplingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSamplingType.setStatus("current")


class _HwXQoSIfSamplingNum_Type(Integer32):
    """Custom type hwXQoSIfSamplingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwXQoSIfSamplingNum_Type.__name__ = "Integer32"
_HwXQoSIfSamplingNum_Object = MibTableColumn
hwXQoSIfSamplingNum = _HwXQoSIfSamplingNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1, 5),
    _HwXQoSIfSamplingNum_Type()
)
hwXQoSIfSamplingNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSamplingNum.setStatus("current")
_HwXQoSIfSamplingRowStatus_Type = RowStatus
_HwXQoSIfSamplingRowStatus_Object = MibTableColumn
hwXQoSIfSamplingRowStatus = _HwXQoSIfSamplingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 4, 1, 6),
    _HwXQoSIfSamplingRowStatus_Type()
)
hwXQoSIfSamplingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSamplingRowStatus.setStatus("current")
_HwXQoSIfLrCfgInfoTable_Object = MibTable
hwXQoSIfLrCfgInfoTable = _HwXQoSIfLrCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwXQoSIfLrCfgInfoTable.setStatus("current")
_HwXQoSIfLrCfgInfoEntry_Object = MibTableRow
hwXQoSIfLrCfgInfoEntry = _HwXQoSIfLrCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1)
)
hwXQoSIfLrCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfLrCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfLrCfgVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfLrCfgInfoEntry.setStatus("current")
_HwXQoSIfLrCfgIfIndex_Type = Integer32
_HwXQoSIfLrCfgIfIndex_Object = MibTableColumn
hwXQoSIfLrCfgIfIndex = _HwXQoSIfLrCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 1),
    _HwXQoSIfLrCfgIfIndex_Type()
)
hwXQoSIfLrCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrCfgIfIndex.setStatus("current")


class _HwXQoSIfLrCfgVlanID_Type(Integer32):
    """Custom type hwXQoSIfLrCfgVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfLrCfgVlanID_Type.__name__ = "Integer32"
_HwXQoSIfLrCfgVlanID_Object = MibTableColumn
hwXQoSIfLrCfgVlanID = _HwXQoSIfLrCfgVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 2),
    _HwXQoSIfLrCfgVlanID_Type()
)
hwXQoSIfLrCfgVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrCfgVlanID.setStatus("current")
_HwXQoSIfLrCir_Type = Integer32
_HwXQoSIfLrCir_Object = MibTableColumn
hwXQoSIfLrCir = _HwXQoSIfLrCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 3),
    _HwXQoSIfLrCir_Type()
)
hwXQoSIfLrCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfLrCir.setStatus("current")
_HwXQoSIfLrRowStatus_Type = RowStatus
_HwXQoSIfLrRowStatus_Object = MibTableColumn
hwXQoSIfLrRowStatus = _HwXQoSIfLrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 4),
    _HwXQoSIfLrRowStatus_Type()
)
hwXQoSIfLrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfLrRowStatus.setStatus("current")
_HwXQoSIfLrCbs_Type = Integer32
_HwXQoSIfLrCbs_Object = MibTableColumn
hwXQoSIfLrCbs = _HwXQoSIfLrCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 5),
    _HwXQoSIfLrCbs_Type()
)
hwXQoSIfLrCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfLrCbs.setStatus("current")
_HwXQoSIfInPhyBandwidth_Type = Integer32
_HwXQoSIfInPhyBandwidth_Object = MibTableColumn
hwXQoSIfInPhyBandwidth = _HwXQoSIfInPhyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 6),
    _HwXQoSIfInPhyBandwidth_Type()
)
hwXQoSIfInPhyBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfInPhyBandwidth.setStatus("current")
_HwXQoSIfOutPhyBandwidth_Type = Integer32
_HwXQoSIfOutPhyBandwidth_Object = MibTableColumn
hwXQoSIfOutPhyBandwidth = _HwXQoSIfOutPhyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 7),
    _HwXQoSIfOutPhyBandwidth_Type()
)
hwXQoSIfOutPhyBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfOutPhyBandwidth.setStatus("current")


class _HwXQoSIfInActualBandwidth_Type(OctetString):
    """Custom type hwXQoSIfInActualBandwidth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSIfInActualBandwidth_Type.__name__ = "OctetString"
_HwXQoSIfInActualBandwidth_Object = MibTableColumn
hwXQoSIfInActualBandwidth = _HwXQoSIfInActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 8),
    _HwXQoSIfInActualBandwidth_Type()
)
hwXQoSIfInActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfInActualBandwidth.setStatus("current")


class _HwXQoSIfOutActualBandwidth_Type(OctetString):
    """Custom type hwXQoSIfOutActualBandwidth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSIfOutActualBandwidth_Type.__name__ = "OctetString"
_HwXQoSIfOutActualBandwidth_Object = MibTableColumn
hwXQoSIfOutActualBandwidth = _HwXQoSIfOutActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 5, 1, 9),
    _HwXQoSIfOutActualBandwidth_Type()
)
hwXQoSIfOutActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfOutActualBandwidth.setStatus("current")
_HwXQoSIfQueueCfgInfoTable_Object = MibTable
hwXQoSIfQueueCfgInfoTable = _HwXQoSIfQueueCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwXQoSIfQueueCfgInfoTable.setStatus("current")
_HwXQoSIfQueueCfgInfoEntry_Object = MibTableRow
hwXQoSIfQueueCfgInfoEntry = _HwXQoSIfQueueCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1)
)
hwXQoSIfQueueCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueCfgVlanID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueDirection"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueCfgCosType"),
)
if mibBuilder.loadTexts:
    hwXQoSIfQueueCfgInfoEntry.setStatus("current")
_HwXQoSIfQueueCfgIfIndex_Type = Integer32
_HwXQoSIfQueueCfgIfIndex_Object = MibTableColumn
hwXQoSIfQueueCfgIfIndex = _HwXQoSIfQueueCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 1),
    _HwXQoSIfQueueCfgIfIndex_Type()
)
hwXQoSIfQueueCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueCfgIfIndex.setStatus("current")


class _HwXQoSIfQueueCfgVlanID_Type(Integer32):
    """Custom type hwXQoSIfQueueCfgVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfQueueCfgVlanID_Type.__name__ = "Integer32"
_HwXQoSIfQueueCfgVlanID_Object = MibTableColumn
hwXQoSIfQueueCfgVlanID = _HwXQoSIfQueueCfgVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 2),
    _HwXQoSIfQueueCfgVlanID_Type()
)
hwXQoSIfQueueCfgVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueCfgVlanID.setStatus("current")
_HwXQoSIfQueueDirection_Type = DirectionType
_HwXQoSIfQueueDirection_Object = MibTableColumn
hwXQoSIfQueueDirection = _HwXQoSIfQueueDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 3),
    _HwXQoSIfQueueDirection_Type()
)
hwXQoSIfQueueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueDirection.setStatus("current")
_HwXQoSIfQueueCfgCosType_Type = CosType
_HwXQoSIfQueueCfgCosType_Object = MibTableColumn
hwXQoSIfQueueCfgCosType = _HwXQoSIfQueueCfgCosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 4),
    _HwXQoSIfQueueCfgCosType_Type()
)
hwXQoSIfQueueCfgCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueCfgCosType.setStatus("current")
_HwXQoSIfQueuePriority_Type = Integer32
_HwXQoSIfQueuePriority_Object = MibTableColumn
hwXQoSIfQueuePriority = _HwXQoSIfQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 5),
    _HwXQoSIfQueuePriority_Type()
)
hwXQoSIfQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfQueuePriority.setStatus("current")
_HwXQoSIfQueueCir_Type = Integer32
_HwXQoSIfQueueCir_Object = MibTableColumn
hwXQoSIfQueueCir = _HwXQoSIfQueueCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 6),
    _HwXQoSIfQueueCir_Type()
)
hwXQoSIfQueueCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfQueueCir.setStatus("current")
_HwXQoSIfQueuePir_Type = Integer32
_HwXQoSIfQueuePir_Object = MibTableColumn
hwXQoSIfQueuePir = _HwXQoSIfQueuePir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 7),
    _HwXQoSIfQueuePir_Type()
)
hwXQoSIfQueuePir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfQueuePir.setStatus("current")
_HwXQoSIfQueueWeight_Type = Integer32
_HwXQoSIfQueueWeight_Object = MibTableColumn
hwXQoSIfQueueWeight = _HwXQoSIfQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 8),
    _HwXQoSIfQueueWeight_Type()
)
hwXQoSIfQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfQueueWeight.setStatus("current")


class _HwXQoSIfQueueMode_Type(Integer32):
    """Custom type hwXQoSIfQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("drr", 6),
          ("pq", 1),
          ("wfq", 4),
          ("wrr", 3))
    )


_HwXQoSIfQueueMode_Type.__name__ = "Integer32"
_HwXQoSIfQueueMode_Object = MibTableColumn
hwXQoSIfQueueMode = _HwXQoSIfQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 9),
    _HwXQoSIfQueueMode_Type()
)
hwXQoSIfQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfQueueMode.setStatus("current")
_HwXQoSIfQueueRowStatus_Type = RowStatus
_HwXQoSIfQueueRowStatus_Object = MibTableColumn
hwXQoSIfQueueRowStatus = _HwXQoSIfQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 6, 1, 10),
    _HwXQoSIfQueueRowStatus_Type()
)
hwXQoSIfQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfQueueRowStatus.setStatus("current")
_HwXQoSIfObserveCfgInfoTable_Object = MibTable
hwXQoSIfObserveCfgInfoTable = _HwXQoSIfObserveCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwXQoSIfObserveCfgInfoTable.setStatus("current")
_HwXQoSIfObserveCfgInfoEntry_Object = MibTableRow
hwXQoSIfObserveCfgInfoEntry = _HwXQoSIfObserveCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 7, 1)
)
hwXQoSIfObserveCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfObserveIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfObserveCfgInfoEntry.setStatus("current")
_HwXQoSIfObserveIndex_Type = Integer32
_HwXQoSIfObserveIndex_Object = MibTableColumn
hwXQoSIfObserveIndex = _HwXQoSIfObserveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 7, 1, 1),
    _HwXQoSIfObserveIndex_Type()
)
hwXQoSIfObserveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfObserveIndex.setStatus("current")
_HwXQoSIfObserveIfIndex_Type = Integer32
_HwXQoSIfObserveIfIndex_Object = MibTableColumn
hwXQoSIfObserveIfIndex = _HwXQoSIfObserveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 7, 1, 2),
    _HwXQoSIfObserveIfIndex_Type()
)
hwXQoSIfObserveIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfObserveIfIndex.setStatus("current")
_HwXQoSIfObserveRowStatus_Type = RowStatus
_HwXQoSIfObserveRowStatus_Object = MibTableColumn
hwXQoSIfObserveRowStatus = _HwXQoSIfObserveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 7, 1, 3),
    _HwXQoSIfObserveRowStatus_Type()
)
hwXQoSIfObserveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfObserveRowStatus.setStatus("current")
_HwXQoSIfWredCfgInfoTable_Object = MibTable
hwXQoSIfWredCfgInfoTable = _HwXQoSIfWredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hwXQoSIfWredCfgInfoTable.setStatus("current")
_HwXQoSIfWredCfgInfoEntry_Object = MibTableRow
hwXQoSIfWredCfgInfoEntry = _HwXQoSIfWredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1)
)
hwXQoSIfWredCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfWredQueueIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfWredDirection"),
)
if mibBuilder.loadTexts:
    hwXQoSIfWredCfgInfoEntry.setStatus("current")


class _HwXQoSIfWredQueueIndex_Type(Integer32):
    """Custom type hwXQoSIfWredQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIfWredQueueIndex_Type.__name__ = "Integer32"
_HwXQoSIfWredQueueIndex_Object = MibTableColumn
hwXQoSIfWredQueueIndex = _HwXQoSIfWredQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 1),
    _HwXQoSIfWredQueueIndex_Type()
)
hwXQoSIfWredQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredQueueIndex.setStatus("current")
_HwXQoSIfWredDirection_Type = DirectionType
_HwXQoSIfWredDirection_Object = MibTableColumn
hwXQoSIfWredDirection = _HwXQoSIfWredDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 2),
    _HwXQoSIfWredDirection_Type()
)
hwXQoSIfWredDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredDirection.setStatus("current")


class _HwXQoSIfWredType_Type(Integer32):
    """Custom type hwXQoSIfWredType based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("ip-Prec", 1))
    )


_HwXQoSIfWredType_Type.__name__ = "Integer32"
_HwXQoSIfWredType_Object = MibTableColumn
hwXQoSIfWredType = _HwXQoSIfWredType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 3),
    _HwXQoSIfWredType_Type()
)
hwXQoSIfWredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfWredType.setStatus("current")
_HwXQoSIfWredLowlimit_Type = Integer32
_HwXQoSIfWredLowlimit_Object = MibTableColumn
hwXQoSIfWredLowlimit = _HwXQoSIfWredLowlimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 4),
    _HwXQoSIfWredLowlimit_Type()
)
hwXQoSIfWredLowlimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfWredLowlimit.setStatus("current")
_HwXQoSIfWredHighlimit_Type = Integer32
_HwXQoSIfWredHighlimit_Object = MibTableColumn
hwXQoSIfWredHighlimit = _HwXQoSIfWredHighlimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 5),
    _HwXQoSIfWredHighlimit_Type()
)
hwXQoSIfWredHighlimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfWredHighlimit.setStatus("current")


class _HwXQoSIfWredDiscardProbability_Type(Integer32):
    """Custom type hwXQoSIfWredDiscardProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwXQoSIfWredDiscardProbability_Type.__name__ = "Integer32"
_HwXQoSIfWredDiscardProbability_Object = MibTableColumn
hwXQoSIfWredDiscardProbability = _HwXQoSIfWredDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 6),
    _HwXQoSIfWredDiscardProbability_Type()
)
hwXQoSIfWredDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfWredDiscardProbability.setStatus("current")


class _HwXQoSIfWredHighDiscardProbability_Type(Integer32):
    """Custom type hwXQoSIfWredHighDiscardProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwXQoSIfWredHighDiscardProbability_Type.__name__ = "Integer32"
_HwXQoSIfWredHighDiscardProbability_Object = MibTableColumn
hwXQoSIfWredHighDiscardProbability = _HwXQoSIfWredHighDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 7),
    _HwXQoSIfWredHighDiscardProbability_Type()
)
hwXQoSIfWredHighDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfWredHighDiscardProbability.setStatus("current")
_HwXQoSIfWredRowStatus_Type = RowStatus
_HwXQoSIfWredRowStatus_Object = MibTableColumn
hwXQoSIfWredRowStatus = _HwXQoSIfWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 8, 1, 8),
    _HwXQoSIfWredRowStatus_Type()
)
hwXQoSIfWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfWredRowStatus.setStatus("current")
_HwXQoSIf8021PMapCfgInfoTable_Object = MibTable
hwXQoSIf8021PMapCfgInfoTable = _HwXQoSIf8021PMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hwXQoSIf8021PMapCfgInfoTable.setStatus("current")
_HwXQoSIf8021PMapCfgInfoEntry_Object = MibTableRow
hwXQoSIf8021PMapCfgInfoEntry = _HwXQoSIf8021PMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 9, 1)
)
hwXQoSIf8021PMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIf8021PMap8021PValue"),
)
if mibBuilder.loadTexts:
    hwXQoSIf8021PMapCfgInfoEntry.setStatus("current")


class _HwXQoSIf8021PMap8021PValue_Type(Integer32):
    """Custom type hwXQoSIf8021PMap8021PValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIf8021PMap8021PValue_Type.__name__ = "Integer32"
_HwXQoSIf8021PMap8021PValue_Object = MibTableColumn
hwXQoSIf8021PMap8021PValue = _HwXQoSIf8021PMap8021PValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 9, 1, 1),
    _HwXQoSIf8021PMap8021PValue_Type()
)
hwXQoSIf8021PMap8021PValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIf8021PMap8021PValue.setStatus("current")


class _HwXQoSIf8021PMapLocalPrecedence_Type(Integer32):
    """Custom type hwXQoSIf8021PMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIf8021PMapLocalPrecedence_Type.__name__ = "Integer32"
_HwXQoSIf8021PMapLocalPrecedence_Object = MibTableColumn
hwXQoSIf8021PMapLocalPrecedence = _HwXQoSIf8021PMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 9, 1, 2),
    _HwXQoSIf8021PMapLocalPrecedence_Type()
)
hwXQoSIf8021PMapLocalPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIf8021PMapLocalPrecedence.setStatus("current")
_HwXQoSIf8021PMapRowStatus_Type = RowStatus
_HwXQoSIf8021PMapRowStatus_Object = MibTableColumn
hwXQoSIf8021PMapRowStatus = _HwXQoSIf8021PMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 9, 1, 3),
    _HwXQoSIf8021PMapRowStatus_Type()
)
hwXQoSIf8021PMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIf8021PMapRowStatus.setStatus("current")
_HwXQoSIfMplsExpMapCfgInfoTable_Object = MibTable
hwXQoSIfMplsExpMapCfgInfoTable = _HwXQoSIfMplsExpMapCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hwXQoSIfMplsExpMapCfgInfoTable.setStatus("current")
_HwXQoSIfMplsExpMapCfgInfoEntry_Object = MibTableRow
hwXQoSIfMplsExpMapCfgInfoEntry = _HwXQoSIfMplsExpMapCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 10, 1)
)
hwXQoSIfMplsExpMapCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMplsExpMapIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMplsExpMapInbound"),
)
if mibBuilder.loadTexts:
    hwXQoSIfMplsExpMapCfgInfoEntry.setStatus("current")
_HwXQoSIfMplsExpMapIfIndex_Type = Integer32
_HwXQoSIfMplsExpMapIfIndex_Object = MibTableColumn
hwXQoSIfMplsExpMapIfIndex = _HwXQoSIfMplsExpMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 10, 1, 1),
    _HwXQoSIfMplsExpMapIfIndex_Type()
)
hwXQoSIfMplsExpMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMplsExpMapIfIndex.setStatus("current")


class _HwXQoSIfMplsExpMapInbound_Type(Integer32):
    """Custom type hwXQoSIfMplsExpMapInbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIfMplsExpMapInbound_Type.__name__ = "Integer32"
_HwXQoSIfMplsExpMapInbound_Object = MibTableColumn
hwXQoSIfMplsExpMapInbound = _HwXQoSIfMplsExpMapInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 10, 1, 2),
    _HwXQoSIfMplsExpMapInbound_Type()
)
hwXQoSIfMplsExpMapInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMplsExpMapInbound.setStatus("current")


class _HwXQoSIfMplsExpMapOutbound_Type(Integer32):
    """Custom type hwXQoSIfMplsExpMapOutbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIfMplsExpMapOutbound_Type.__name__ = "Integer32"
_HwXQoSIfMplsExpMapOutbound_Object = MibTableColumn
hwXQoSIfMplsExpMapOutbound = _HwXQoSIfMplsExpMapOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 10, 1, 3),
    _HwXQoSIfMplsExpMapOutbound_Type()
)
hwXQoSIfMplsExpMapOutbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfMplsExpMapOutbound.setStatus("current")
_HwXQoSIfMplsExpMapRowStatus_Type = RowStatus
_HwXQoSIfMplsExpMapRowStatus_Object = MibTableColumn
hwXQoSIfMplsExpMapRowStatus = _HwXQoSIfMplsExpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 10, 1, 4),
    _HwXQoSIfMplsExpMapRowStatus_Type()
)
hwXQoSIfMplsExpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfMplsExpMapRowStatus.setStatus("current")
_HwXQoSIfDefaultPriorityCfgInfoTable_Object = MibTable
hwXQoSIfDefaultPriorityCfgInfoTable = _HwXQoSIfDefaultPriorityCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hwXQoSIfDefaultPriorityCfgInfoTable.setStatus("current")
_HwXQoSIfDefaultPriorityCfgInfoEntry_Object = MibTableRow
hwXQoSIfDefaultPriorityCfgInfoEntry = _HwXQoSIfDefaultPriorityCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 11, 1)
)
hwXQoSIfDefaultPriorityCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfDefaultPriorityIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfDefaultPriorityVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfDefaultPriorityCfgInfoEntry.setStatus("current")
_HwXQoSIfDefaultPriorityIfIndex_Type = Integer32
_HwXQoSIfDefaultPriorityIfIndex_Object = MibTableColumn
hwXQoSIfDefaultPriorityIfIndex = _HwXQoSIfDefaultPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 11, 1, 1),
    _HwXQoSIfDefaultPriorityIfIndex_Type()
)
hwXQoSIfDefaultPriorityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfDefaultPriorityIfIndex.setStatus("current")


class _HwXQoSIfDefaultPriorityVlanID_Type(Integer32):
    """Custom type hwXQoSIfDefaultPriorityVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSIfDefaultPriorityVlanID_Type.__name__ = "Integer32"
_HwXQoSIfDefaultPriorityVlanID_Object = MibTableColumn
hwXQoSIfDefaultPriorityVlanID = _HwXQoSIfDefaultPriorityVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 11, 1, 2),
    _HwXQoSIfDefaultPriorityVlanID_Type()
)
hwXQoSIfDefaultPriorityVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfDefaultPriorityVlanID.setStatus("current")


class _HwXQoSIfDefaultPriorityValue_Type(Integer32):
    """Custom type hwXQoSIfDefaultPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIfDefaultPriorityValue_Type.__name__ = "Integer32"
_HwXQoSIfDefaultPriorityValue_Object = MibTableColumn
hwXQoSIfDefaultPriorityValue = _HwXQoSIfDefaultPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 11, 1, 3),
    _HwXQoSIfDefaultPriorityValue_Type()
)
hwXQoSIfDefaultPriorityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfDefaultPriorityValue.setStatus("current")
_HwXQoSIfDefaultPriorityRowStatus_Type = RowStatus
_HwXQoSIfDefaultPriorityRowStatus_Object = MibTableColumn
hwXQoSIfDefaultPriorityRowStatus = _HwXQoSIfDefaultPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 11, 1, 4),
    _HwXQoSIfDefaultPriorityRowStatus_Type()
)
hwXQoSIfDefaultPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfDefaultPriorityRowStatus.setStatus("current")
_HwXQoSIfSoftCarTable_Object = MibTable
hwXQoSIfSoftCarTable = _HwXQoSIfSoftCarTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hwXQoSIfSoftCarTable.setStatus("current")
_HwXQoSIfSoftCarEntry_Object = MibTableRow
hwXQoSIfSoftCarEntry = _HwXQoSIfSoftCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 12, 1)
)
hwXQoSIfSoftCarEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSoftCarIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSoftCarDirection"),
)
if mibBuilder.loadTexts:
    hwXQoSIfSoftCarEntry.setStatus("current")
_HwXQoSIfSoftCarIfIndex_Type = Integer32
_HwXQoSIfSoftCarIfIndex_Object = MibTableColumn
hwXQoSIfSoftCarIfIndex = _HwXQoSIfSoftCarIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 12, 1, 1),
    _HwXQoSIfSoftCarIfIndex_Type()
)
hwXQoSIfSoftCarIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfSoftCarIfIndex.setStatus("current")
_HwXQoSIfSoftCarDirection_Type = DirectionType
_HwXQoSIfSoftCarDirection_Object = MibTableColumn
hwXQoSIfSoftCarDirection = _HwXQoSIfSoftCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 12, 1, 2),
    _HwXQoSIfSoftCarDirection_Type()
)
hwXQoSIfSoftCarDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfSoftCarDirection.setStatus("current")


class _HwXQoSIfSoftCarCarIndex_Type(Integer32):
    """Custom type hwXQoSIfSoftCarCarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwXQoSIfSoftCarCarIndex_Type.__name__ = "Integer32"
_HwXQoSIfSoftCarCarIndex_Object = MibTableColumn
hwXQoSIfSoftCarCarIndex = _HwXQoSIfSoftCarCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 12, 1, 3),
    _HwXQoSIfSoftCarCarIndex_Type()
)
hwXQoSIfSoftCarCarIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSoftCarCarIndex.setStatus("current")
_HwXQoSIfSoftCarRowStatus_Type = RowStatus
_HwXQoSIfSoftCarRowStatus_Object = MibTableColumn
hwXQoSIfSoftCarRowStatus = _HwXQoSIfSoftCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 12, 1, 4),
    _HwXQoSIfSoftCarRowStatus_Type()
)
hwXQoSIfSoftCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSoftCarRowStatus.setStatus("current")
_HwXQoSIfLocalPrecedenceQueueMapTable_Object = MibTable
hwXQoSIfLocalPrecedenceQueueMapTable = _HwXQoSIfLocalPrecedenceQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hwXQoSIfLocalPrecedenceQueueMapTable.setStatus("current")
_HwXQoSIfLocalPrecedenceQueueMapEntry_Object = MibTableRow
hwXQoSIfLocalPrecedenceQueueMapEntry = _HwXQoSIfLocalPrecedenceQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 13, 1)
)
hwXQoSIfLocalPrecedenceQueueMapEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfLocPreQueMapIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfLocPreQueMapPreValue"),
)
if mibBuilder.loadTexts:
    hwXQoSIfLocalPrecedenceQueueMapEntry.setStatus("current")
_HwXQoSIfLocPreQueMapIfIndex_Type = Integer32
_HwXQoSIfLocPreQueMapIfIndex_Object = MibTableColumn
hwXQoSIfLocPreQueMapIfIndex = _HwXQoSIfLocPreQueMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 13, 1, 1),
    _HwXQoSIfLocPreQueMapIfIndex_Type()
)
hwXQoSIfLocPreQueMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLocPreQueMapIfIndex.setStatus("current")


class _HwXQoSIfLocPreQueMapPreValue_Type(Integer32):
    """Custom type hwXQoSIfLocPreQueMapPreValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSIfLocPreQueMapPreValue_Type.__name__ = "Integer32"
_HwXQoSIfLocPreQueMapPreValue_Object = MibTableColumn
hwXQoSIfLocPreQueMapPreValue = _HwXQoSIfLocPreQueMapPreValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 13, 1, 2),
    _HwXQoSIfLocPreQueMapPreValue_Type()
)
hwXQoSIfLocPreQueMapPreValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLocPreQueMapPreValue.setStatus("current")
_HwXQoSIfLocPreQueMapCosType_Type = CosType
_HwXQoSIfLocPreQueMapCosType_Object = MibTableColumn
hwXQoSIfLocPreQueMapCosType = _HwXQoSIfLocPreQueMapCosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 13, 1, 3),
    _HwXQoSIfLocPreQueMapCosType_Type()
)
hwXQoSIfLocPreQueMapCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfLocPreQueMapCosType.setStatus("current")
_HwXQoSIfLocPreQueMapRowStatus_Type = RowStatus
_HwXQoSIfLocPreQueMapRowStatus_Object = MibTableColumn
hwXQoSIfLocPreQueMapRowStatus = _HwXQoSIfLocPreQueMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 13, 1, 4),
    _HwXQoSIfLocPreQueMapRowStatus_Type()
)
hwXQoSIfLocPreQueMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfLocPreQueMapRowStatus.setStatus("current")
_HwXQoSIfScheduleModeCfgInfoTable_Object = MibTable
hwXQoSIfScheduleModeCfgInfoTable = _HwXQoSIfScheduleModeCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hwXQoSIfScheduleModeCfgInfoTable.setStatus("current")
_HwXQoSIfScheduleModeCfgInfoEntry_Object = MibTableRow
hwXQoSIfScheduleModeCfgInfoEntry = _HwXQoSIfScheduleModeCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 14, 1)
)
hwXQoSIfScheduleModeCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfScheduleModeIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfScheduleModeCfgInfoEntry.setStatus("current")
_HwXQoSIfScheduleModeIfIndex_Type = Integer32
_HwXQoSIfScheduleModeIfIndex_Object = MibTableColumn
hwXQoSIfScheduleModeIfIndex = _HwXQoSIfScheduleModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 14, 1, 1),
    _HwXQoSIfScheduleModeIfIndex_Type()
)
hwXQoSIfScheduleModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfScheduleModeIfIndex.setStatus("current")


class _HwXQoSIfModeType_Type(Integer32):
    """Custom type hwXQoSIfModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pq", 2),
          ("pqWfq", 1),
          ("wfq", 3))
    )


_HwXQoSIfModeType_Type.__name__ = "Integer32"
_HwXQoSIfModeType_Object = MibTableColumn
hwXQoSIfModeType = _HwXQoSIfModeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 14, 1, 2),
    _HwXQoSIfModeType_Type()
)
hwXQoSIfModeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfModeType.setStatus("current")
_HwXQoSIfScheduleModeRowStatus_Type = RowStatus
_HwXQoSIfScheduleModeRowStatus_Object = MibTableColumn
hwXQoSIfScheduleModeRowStatus = _HwXQoSIfScheduleModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 14, 1, 3),
    _HwXQoSIfScheduleModeRowStatus_Type()
)
hwXQoSIfScheduleModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfScheduleModeRowStatus.setStatus("current")
_HwXQoSIfHQOSPriCfgInfoTable_Object = MibTable
hwXQoSIfHQOSPriCfgInfoTable = _HwXQoSIfHQOSPriCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hwXQoSIfHQOSPriCfgInfoTable.setStatus("current")
_HwXQoSIfHQOSPriCfgInfoEntry_Object = MibTableRow
hwXQoSIfHQOSPriCfgInfoEntry = _HwXQoSIfHQOSPriCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 15, 1)
)
hwXQoSIfHQOSPriCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfHqosPriIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfHQOSPriCfgInfoEntry.setStatus("current")
_HwXQoSIfHqosPriIfIndex_Type = Integer32
_HwXQoSIfHqosPriIfIndex_Object = MibTableColumn
hwXQoSIfHqosPriIfIndex = _HwXQoSIfHqosPriIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 15, 1, 1),
    _HwXQoSIfHqosPriIfIndex_Type()
)
hwXQoSIfHqosPriIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfHqosPriIfIndex.setStatus("current")


class _HwXQoSIfHqosPriority_Type(Integer32):
    """Custom type hwXQoSIfHqosPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSIfHqosPriority_Type.__name__ = "Integer32"
_HwXQoSIfHqosPriority_Object = MibTableColumn
hwXQoSIfHqosPriority = _HwXQoSIfHqosPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 15, 1, 2),
    _HwXQoSIfHqosPriority_Type()
)
hwXQoSIfHqosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfHqosPriority.setStatus("current")
_HwXQoSIfHqosPriRowStatus_Type = RowStatus
_HwXQoSIfHqosPriRowStatus_Object = MibTableColumn
hwXQoSIfHqosPriRowStatus = _HwXQoSIfHqosPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 15, 1, 3),
    _HwXQoSIfHqosPriRowStatus_Type()
)
hwXQoSIfHqosPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfHqosPriRowStatus.setStatus("current")
_HwXQoSIfOutboundMulticastCfgInfoTable_Object = MibTable
hwXQoSIfOutboundMulticastCfgInfoTable = _HwXQoSIfOutboundMulticastCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 16)
)
if mibBuilder.loadTexts:
    hwXQoSIfOutboundMulticastCfgInfoTable.setStatus("current")
_HwXQoSIfOutboundMulticastCfgInfoEntry_Object = MibTableRow
hwXQoSIfOutboundMulticastCfgInfoEntry = _HwXQoSIfOutboundMulticastCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 16, 1)
)
hwXQoSIfOutboundMulticastCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfOutMulticastIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfOutboundMulticastCfgInfoEntry.setStatus("current")
_HwXQoSIfOutMulticastIfIndex_Type = Integer32
_HwXQoSIfOutMulticastIfIndex_Object = MibTableColumn
hwXQoSIfOutMulticastIfIndex = _HwXQoSIfOutMulticastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 16, 1, 1),
    _HwXQoSIfOutMulticastIfIndex_Type()
)
hwXQoSIfOutMulticastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfOutMulticastIfIndex.setStatus("current")


class _HwXQoSIfUnicastWeightValue_Type(Integer32):
    """Custom type hwXQoSIfUnicastWeightValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwXQoSIfUnicastWeightValue_Type.__name__ = "Integer32"
_HwXQoSIfUnicastWeightValue_Object = MibTableColumn
hwXQoSIfUnicastWeightValue = _HwXQoSIfUnicastWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 16, 1, 2),
    _HwXQoSIfUnicastWeightValue_Type()
)
hwXQoSIfUnicastWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfUnicastWeightValue.setStatus("current")


class _HwXQoSIfMulticastWeightValue_Type(Integer32):
    """Custom type hwXQoSIfMulticastWeightValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwXQoSIfMulticastWeightValue_Type.__name__ = "Integer32"
_HwXQoSIfMulticastWeightValue_Object = MibTableColumn
hwXQoSIfMulticastWeightValue = _HwXQoSIfMulticastWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 16, 1, 3),
    _HwXQoSIfMulticastWeightValue_Type()
)
hwXQoSIfMulticastWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfMulticastWeightValue.setStatus("current")
_HwXQoSIfOutMulticastRowStatus_Type = RowStatus
_HwXQoSIfOutMulticastRowStatus_Object = MibTableColumn
hwXQoSIfOutMulticastRowStatus = _HwXQoSIfOutMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 16, 1, 4),
    _HwXQoSIfOutMulticastRowStatus_Type()
)
hwXQoSIfOutMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfOutMulticastRowStatus.setStatus("current")
_HwXQoSIfSredCfgInfoTable_Object = MibTable
hwXQoSIfSredCfgInfoTable = _HwXQoSIfSredCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17)
)
if mibBuilder.loadTexts:
    hwXQoSIfSredCfgInfoTable.setStatus("current")
_HwXQoSIfSredCfgInfoEntry_Object = MibTableRow
hwXQoSIfSredCfgInfoEntry = _HwXQoSIfSredCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1)
)
hwXQoSIfSredCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSredQueueIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfSredCfgInfoEntry.setStatus("current")


class _HwXQoSIfSredQueueIndex_Type(Integer32):
    """Custom type hwXQoSIfSredQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSIfSredQueueIndex_Type.__name__ = "Integer32"
_HwXQoSIfSredQueueIndex_Object = MibTableColumn
hwXQoSIfSredQueueIndex = _HwXQoSIfSredQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1, 1),
    _HwXQoSIfSredQueueIndex_Type()
)
hwXQoSIfSredQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfSredQueueIndex.setStatus("current")
_HwXQoSIfSredRedStartDiscardPoint_Type = Integer32
_HwXQoSIfSredRedStartDiscardPoint_Object = MibTableColumn
hwXQoSIfSredRedStartDiscardPoint = _HwXQoSIfSredRedStartDiscardPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1, 2),
    _HwXQoSIfSredRedStartDiscardPoint_Type()
)
hwXQoSIfSredRedStartDiscardPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSredRedStartDiscardPoint.setStatus("current")


class _HwXQoSIfSredRedDiscardProbability_Type(Integer32):
    """Custom type hwXQoSIfSredRedDiscardProbability based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("drop1", 1),
          ("drop2", 2),
          ("drop3", 3),
          ("drop4", 4),
          ("drop5", 5),
          ("drop6", 6),
          ("drop7", 7),
          ("drop8", 8))
    )


_HwXQoSIfSredRedDiscardProbability_Type.__name__ = "Integer32"
_HwXQoSIfSredRedDiscardProbability_Object = MibTableColumn
hwXQoSIfSredRedDiscardProbability = _HwXQoSIfSredRedDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1, 3),
    _HwXQoSIfSredRedDiscardProbability_Type()
)
hwXQoSIfSredRedDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSredRedDiscardProbability.setStatus("current")
_HwXQoSIfSredYellowStartDiscardPoint_Type = Integer32
_HwXQoSIfSredYellowStartDiscardPoint_Object = MibTableColumn
hwXQoSIfSredYellowStartDiscardPoint = _HwXQoSIfSredYellowStartDiscardPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1, 4),
    _HwXQoSIfSredYellowStartDiscardPoint_Type()
)
hwXQoSIfSredYellowStartDiscardPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSredYellowStartDiscardPoint.setStatus("current")


class _HwXQoSIfSredYellowDiscardProbability_Type(Integer32):
    """Custom type hwXQoSIfSredYellowDiscardProbability based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("drop1", 1),
          ("drop2", 2),
          ("drop3", 3),
          ("drop4", 4),
          ("drop5", 5),
          ("drop6", 6),
          ("drop7", 7),
          ("drop8", 8))
    )


_HwXQoSIfSredYellowDiscardProbability_Type.__name__ = "Integer32"
_HwXQoSIfSredYellowDiscardProbability_Object = MibTableColumn
hwXQoSIfSredYellowDiscardProbability = _HwXQoSIfSredYellowDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1, 5),
    _HwXQoSIfSredYellowDiscardProbability_Type()
)
hwXQoSIfSredYellowDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSredYellowDiscardProbability.setStatus("current")
_HwXQoSIfSredRowStatus_Type = RowStatus
_HwXQoSIfSredRowStatus_Object = MibTableColumn
hwXQoSIfSredRowStatus = _HwXQoSIfSredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 17, 1, 6),
    _HwXQoSIfSredRowStatus_Type()
)
hwXQoSIfSredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfSredRowStatus.setStatus("current")
_HwXQosAtmTrafficQueueTable_Object = MibTable
hwXQosAtmTrafficQueueTable = _HwXQosAtmTrafficQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 18)
)
if mibBuilder.loadTexts:
    hwXQosAtmTrafficQueueTable.setStatus("current")
_HwXQosAtmTrafficQueueEntry_Object = MibTableRow
hwXQosAtmTrafficQueueEntry = _HwXQosAtmTrafficQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 18, 1)
)
hwXQosAtmTrafficQueueEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmTrafficQueueIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQosAtmTrafficQueueEntry.setStatus("current")
_HwXQoSAtmTrafficQueueIfIndex_Type = Unsigned32
_HwXQoSAtmTrafficQueueIfIndex_Object = MibTableColumn
hwXQoSAtmTrafficQueueIfIndex = _HwXQoSAtmTrafficQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 18, 1, 1),
    _HwXQoSAtmTrafficQueueIfIndex_Type()
)
hwXQoSAtmTrafficQueueIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSAtmTrafficQueueIfIndex.setStatus("current")
_HwXQoSAtmTrafficQueueServiceClass_Type = Integer32
_HwXQoSAtmTrafficQueueServiceClass_Object = MibTableColumn
hwXQoSAtmTrafficQueueServiceClass = _HwXQoSAtmTrafficQueueServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 18, 1, 2),
    _HwXQoSAtmTrafficQueueServiceClass_Type()
)
hwXQoSAtmTrafficQueueServiceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmTrafficQueueServiceClass.setStatus("current")
_HwXQoSAtmTrafficQueueRowStatus_Type = RowStatus
_HwXQoSAtmTrafficQueueRowStatus_Object = MibTableColumn
hwXQoSAtmTrafficQueueRowStatus = _HwXQoSAtmTrafficQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 18, 1, 3),
    _HwXQoSAtmTrafficQueueRowStatus_Type()
)
hwXQoSAtmTrafficQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmTrafficQueueRowStatus.setStatus("current")
_HwXQoSAtmPvcServiceTypeTable_Object = MibTable
hwXQoSAtmPvcServiceTypeTable = _HwXQoSAtmPvcServiceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19)
)
if mibBuilder.loadTexts:
    hwXQoSAtmPvcServiceTypeTable.setStatus("current")
_HwXQoSAtmPvcServiceTypeEntry_Object = MibTableRow
hwXQoSAtmPvcServiceTypeEntry = _HwXQoSAtmPvcServiceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1)
)
hwXQoSAtmPvcServiceTypeEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvcServiceTypeVpiIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvcServiceTypeVciIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSAtmPvcServiceTypeIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSAtmPvcServiceTypeEntry.setStatus("current")
_HwXQoSAtmPvcServiceTypeIfIndex_Type = Unsigned32
_HwXQoSAtmPvcServiceTypeIfIndex_Object = MibTableColumn
hwXQoSAtmPvcServiceTypeIfIndex = _HwXQoSAtmPvcServiceTypeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 1),
    _HwXQoSAtmPvcServiceTypeIfIndex_Type()
)
hwXQoSAtmPvcServiceTypeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcServiceTypeIfIndex.setStatus("current")
_HwXQoSAtmPvcServiceTypeVpiIndex_Type = Unsigned32
_HwXQoSAtmPvcServiceTypeVpiIndex_Object = MibTableColumn
hwXQoSAtmPvcServiceTypeVpiIndex = _HwXQoSAtmPvcServiceTypeVpiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 2),
    _HwXQoSAtmPvcServiceTypeVpiIndex_Type()
)
hwXQoSAtmPvcServiceTypeVpiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcServiceTypeVpiIndex.setStatus("current")
_HwXQoSAtmPvcServiceTypeVciIndex_Type = Unsigned32
_HwXQoSAtmPvcServiceTypeVciIndex_Object = MibTableColumn
hwXQoSAtmPvcServiceTypeVciIndex = _HwXQoSAtmPvcServiceTypeVciIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 3),
    _HwXQoSAtmPvcServiceTypeVciIndex_Type()
)
hwXQoSAtmPvcServiceTypeVciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcServiceTypeVciIndex.setStatus("current")
_HwXQoSAtmPvcNameServiceTypeIndex_Type = OctetString
_HwXQoSAtmPvcNameServiceTypeIndex_Object = MibTableColumn
hwXQoSAtmPvcNameServiceTypeIndex = _HwXQoSAtmPvcNameServiceTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 4),
    _HwXQoSAtmPvcNameServiceTypeIndex_Type()
)
hwXQoSAtmPvcNameServiceTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcNameServiceTypeIndex.setStatus("current")
_HwXQoSAtmPvcServiceType_Type = Integer32
_HwXQoSAtmPvcServiceType_Object = MibTableColumn
hwXQoSAtmPvcServiceType = _HwXQoSAtmPvcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 5),
    _HwXQoSAtmPvcServiceType_Type()
)
hwXQoSAtmPvcServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcServiceType.setStatus("current")
_HwXQoSAtmPvcPcr_Type = Integer32
_HwXQoSAtmPvcPcr_Object = MibTableColumn
hwXQoSAtmPvcPcr = _HwXQoSAtmPvcPcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 6),
    _HwXQoSAtmPvcPcr_Type()
)
hwXQoSAtmPvcPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcPcr.setStatus("current")
_HwXQoSAtmPvcCdvt_Type = Integer32
_HwXQoSAtmPvcCdvt_Object = MibTableColumn
hwXQoSAtmPvcCdvt = _HwXQoSAtmPvcCdvt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 7),
    _HwXQoSAtmPvcCdvt_Type()
)
hwXQoSAtmPvcCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcCdvt.setStatus("current")
_HwXQoSAtmPvcVbrScr_Type = Integer32
_HwXQoSAtmPvcVbrScr_Object = MibTableColumn
hwXQoSAtmPvcVbrScr = _HwXQoSAtmPvcVbrScr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 8),
    _HwXQoSAtmPvcVbrScr_Type()
)
hwXQoSAtmPvcVbrScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcVbrScr.setStatus("current")
_HwXQoSAtmPvcVbrMbs_Type = Integer32
_HwXQoSAtmPvcVbrMbs_Object = MibTableColumn
hwXQoSAtmPvcVbrMbs = _HwXQoSAtmPvcVbrMbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 9),
    _HwXQoSAtmPvcVbrMbs_Type()
)
hwXQoSAtmPvcVbrMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcVbrMbs.setStatus("current")
_HwXQoSAtmPvcRowStatus_Type = RowStatus
_HwXQoSAtmPvcRowStatus_Object = MibTableColumn
hwXQoSAtmPvcRowStatus = _HwXQoSAtmPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 19, 1, 10),
    _HwXQoSAtmPvcRowStatus_Type()
)
hwXQoSAtmPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSAtmPvcRowStatus.setStatus("current")
_HwXQoSIfShapingCfgInfoTable_Object = MibTable
hwXQoSIfShapingCfgInfoTable = _HwXQoSIfShapingCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20)
)
if mibBuilder.loadTexts:
    hwXQoSIfShapingCfgInfoTable.setStatus("current")
_HwXQoSIfShapingCfgInfoEntry_Object = MibTableRow
hwXQoSIfShapingCfgInfoEntry = _HwXQoSIfShapingCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20, 1)
)
hwXQoSIfShapingCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfShapingIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfShapingQueueIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfShapingCfgInfoEntry.setStatus("current")
_HwXQoSIfShapingIfIndex_Type = Integer32
_HwXQoSIfShapingIfIndex_Object = MibTableColumn
hwXQoSIfShapingIfIndex = _HwXQoSIfShapingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20, 1, 1),
    _HwXQoSIfShapingIfIndex_Type()
)
hwXQoSIfShapingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfShapingIfIndex.setStatus("current")


class _HwXQoSIfShapingQueueIndex_Type(Integer32):
    """Custom type hwXQoSIfShapingQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSIfShapingQueueIndex_Type.__name__ = "Integer32"
_HwXQoSIfShapingQueueIndex_Object = MibTableColumn
hwXQoSIfShapingQueueIndex = _HwXQoSIfShapingQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20, 1, 2),
    _HwXQoSIfShapingQueueIndex_Type()
)
hwXQoSIfShapingQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfShapingQueueIndex.setStatus("current")
_HwXQoSIfShapingQueueCir_Type = Integer32
_HwXQoSIfShapingQueueCir_Object = MibTableColumn
hwXQoSIfShapingQueueCir = _HwXQoSIfShapingQueueCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20, 1, 3),
    _HwXQoSIfShapingQueueCir_Type()
)
hwXQoSIfShapingQueueCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfShapingQueueCir.setStatus("current")
_HwXQoSIfShapingQueuePir_Type = Integer32
_HwXQoSIfShapingQueuePir_Object = MibTableColumn
hwXQoSIfShapingQueuePir = _HwXQoSIfShapingQueuePir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20, 1, 4),
    _HwXQoSIfShapingQueuePir_Type()
)
hwXQoSIfShapingQueuePir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfShapingQueuePir.setStatus("current")
_HwXQoSIfShapingRowStatus_Type = RowStatus
_HwXQoSIfShapingRowStatus_Object = MibTableColumn
hwXQoSIfShapingRowStatus = _HwXQoSIfShapingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 20, 1, 5),
    _HwXQoSIfShapingRowStatus_Type()
)
hwXQoSIfShapingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfShapingRowStatus.setStatus("current")
_HwXQoSIfPppoeCfgInfoTable_Object = MibTable
hwXQoSIfPppoeCfgInfoTable = _HwXQoSIfPppoeCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21)
)
if mibBuilder.loadTexts:
    hwXQoSIfPppoeCfgInfoTable.setStatus("current")
_HwXQoSIfPppoeCfgInfoEntry_Object = MibTableRow
hwXQoSIfPppoeCfgInfoEntry = _HwXQoSIfPppoeCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21, 1)
)
hwXQoSIfPppoeCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfPppoeIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfPppoeMatchType"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfPppoeSourceMac"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfPppoeDestMac"),
)
if mibBuilder.loadTexts:
    hwXQoSIfPppoeCfgInfoEntry.setStatus("current")


class _HwXQoSIfPppoeIfIndex_Type(Integer32):
    """Custom type hwXQoSIfPppoeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwXQoSIfPppoeIfIndex_Type.__name__ = "Integer32"
_HwXQoSIfPppoeIfIndex_Object = MibTableColumn
hwXQoSIfPppoeIfIndex = _HwXQoSIfPppoeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21, 1, 1),
    _HwXQoSIfPppoeIfIndex_Type()
)
hwXQoSIfPppoeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfPppoeIfIndex.setStatus("current")


class _HwXQoSIfPppoeMatchType_Type(Integer32):
    """Custom type hwXQoSIfPppoeMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwXQoSIfPppoeMatchType_Type.__name__ = "Integer32"
_HwXQoSIfPppoeMatchType_Object = MibTableColumn
hwXQoSIfPppoeMatchType = _HwXQoSIfPppoeMatchType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21, 1, 2),
    _HwXQoSIfPppoeMatchType_Type()
)
hwXQoSIfPppoeMatchType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfPppoeMatchType.setStatus("current")
_HwXQoSIfPppoeSourceMac_Type = MacAddress
_HwXQoSIfPppoeSourceMac_Object = MibTableColumn
hwXQoSIfPppoeSourceMac = _HwXQoSIfPppoeSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21, 1, 3),
    _HwXQoSIfPppoeSourceMac_Type()
)
hwXQoSIfPppoeSourceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfPppoeSourceMac.setStatus("current")
_HwXQoSIfPppoeDestMac_Type = MacAddress
_HwXQoSIfPppoeDestMac_Object = MibTableColumn
hwXQoSIfPppoeDestMac = _HwXQoSIfPppoeDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21, 1, 4),
    _HwXQoSIfPppoeDestMac_Type()
)
hwXQoSIfPppoeDestMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfPppoeDestMac.setStatus("current")
_HwXQoSIfPppoeRowStatus_Type = RowStatus
_HwXQoSIfPppoeRowStatus_Object = MibTableColumn
hwXQoSIfPppoeRowStatus = _HwXQoSIfPppoeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 21, 1, 5),
    _HwXQoSIfPppoeRowStatus_Type()
)
hwXQoSIfPppoeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfPppoeRowStatus.setStatus("current")
_HwXQoSIfScheduleCfgInfoTable_Object = MibTable
hwXQoSIfScheduleCfgInfoTable = _HwXQoSIfScheduleCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 22)
)
if mibBuilder.loadTexts:
    hwXQoSIfScheduleCfgInfoTable.setStatus("current")
_HwXQoSIfScheduleCfgInfoEntry_Object = MibTableRow
hwXQoSIfScheduleCfgInfoEntry = _HwXQoSIfScheduleCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 22, 1)
)
hwXQoSIfScheduleCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfScheduleIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfScheduleCfgInfoEntry.setStatus("current")


class _HwXQoSIfScheduleIfIndex_Type(Integer32):
    """Custom type hwXQoSIfScheduleIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwXQoSIfScheduleIfIndex_Type.__name__ = "Integer32"
_HwXQoSIfScheduleIfIndex_Object = MibTableColumn
hwXQoSIfScheduleIfIndex = _HwXQoSIfScheduleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 22, 1, 1),
    _HwXQoSIfScheduleIfIndex_Type()
)
hwXQoSIfScheduleIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfScheduleIfIndex.setStatus("current")


class _HwXQoSIfScheduleProfile_Type(OctetString):
    """Custom type hwXQoSIfScheduleProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSIfScheduleProfile_Type.__name__ = "OctetString"
_HwXQoSIfScheduleProfile_Object = MibTableColumn
hwXQoSIfScheduleProfile = _HwXQoSIfScheduleProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 22, 1, 2),
    _HwXQoSIfScheduleProfile_Type()
)
hwXQoSIfScheduleProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfScheduleProfile.setStatus("current")
_HwXQoSIfScheduleRowStatus_Type = RowStatus
_HwXQoSIfScheduleRowStatus_Object = MibTableColumn
hwXQoSIfScheduleRowStatus = _HwXQoSIfScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 22, 1, 51),
    _HwXQoSIfScheduleRowStatus_Type()
)
hwXQoSIfScheduleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfScheduleRowStatus.setStatus("current")
_HwXQoSIfIPCarCfgInfoTable_Object = MibTable
hwXQoSIfIPCarCfgInfoTable = _HwXQoSIfIPCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23)
)
if mibBuilder.loadTexts:
    hwXQoSIfIPCarCfgInfoTable.setStatus("current")
_HwXQoSIfIPCarCfgInfoEntry_Object = MibTableRow
hwXQoSIfIPCarCfgInfoEntry = _HwXQoSIfIPCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1)
)
hwXQoSIfIPCarCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfIPCarCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfIPCarDirection"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIPCarRuleIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfIPCarCfgInfoEntry.setStatus("current")
_HwXQoSIfIPCarCfgIfIndex_Type = Integer32
_HwXQoSIfIPCarCfgIfIndex_Object = MibTableColumn
hwXQoSIfIPCarCfgIfIndex = _HwXQoSIfIPCarCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 1),
    _HwXQoSIfIPCarCfgIfIndex_Type()
)
hwXQoSIfIPCarCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarCfgIfIndex.setStatus("current")
_HwXQoSIfIPCarDirection_Type = DirectionType
_HwXQoSIfIPCarDirection_Object = MibTableColumn
hwXQoSIfIPCarDirection = _HwXQoSIfIPCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 2),
    _HwXQoSIfIPCarDirection_Type()
)
hwXQoSIfIPCarDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarDirection.setStatus("current")
_HwXQoSIPCarRuleIndex_Type = Integer32
_HwXQoSIPCarRuleIndex_Object = MibTableColumn
hwXQoSIPCarRuleIndex = _HwXQoSIPCarRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 3),
    _HwXQoSIPCarRuleIndex_Type()
)
hwXQoSIPCarRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIPCarRuleIndex.setStatus("current")
_HwXQoSIPCarRuleType_Type = IPCARRuleType
_HwXQoSIPCarRuleType_Object = MibTableColumn
hwXQoSIPCarRuleType = _HwXQoSIPCarRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 4),
    _HwXQoSIPCarRuleType_Type()
)
hwXQoSIPCarRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIPCarRuleType.setStatus("current")
_HwXBQoSIPCarIntValue_Type = Unsigned32
_HwXBQoSIPCarIntValue_Object = MibTableColumn
hwXBQoSIPCarIntValue = _HwXBQoSIPCarIntValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 5),
    _HwXBQoSIPCarIntValue_Type()
)
hwXBQoSIPCarIntValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXBQoSIPCarIntValue.setStatus("current")
_HwXQoSIfIPCarStartIp_Type = IpAddress
_HwXQoSIfIPCarStartIp_Object = MibTableColumn
hwXQoSIfIPCarStartIp = _HwXQoSIfIPCarStartIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 6),
    _HwXQoSIfIPCarStartIp_Type()
)
hwXQoSIfIPCarStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarStartIp.setStatus("current")
_HwXQoSIfIPCarEndIp_Type = IpAddress
_HwXQoSIfIPCarEndIp_Object = MibTableColumn
hwXQoSIfIPCarEndIp = _HwXQoSIfIPCarEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 7),
    _HwXQoSIfIPCarEndIp_Type()
)
hwXQoSIfIPCarEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarEndIp.setStatus("current")
_HwXQoSIfIPCarCir_Type = Integer32
_HwXQoSIfIPCarCir_Object = MibTableColumn
hwXQoSIfIPCarCir = _HwXQoSIfIPCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 8),
    _HwXQoSIfIPCarCir_Type()
)
hwXQoSIfIPCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarCir.setStatus("current")
_HwXQoSIfIPCarCbs_Type = Integer32
_HwXQoSIfIPCarCbs_Object = MibTableColumn
hwXQoSIfIPCarCbs = _HwXQoSIfIPCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 9),
    _HwXQoSIfIPCarCbs_Type()
)
hwXQoSIfIPCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarCbs.setStatus("current")


class _HwXQoSIfIPCarEbs_Type(Integer32):
    """Custom type hwXQoSIfIPCarEbs based on Integer32"""
    defaultValue = 0


_HwXQoSIfIPCarEbs_Object = MibTableColumn
hwXQoSIfIPCarEbs = _HwXQoSIfIPCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 10),
    _HwXQoSIfIPCarEbs_Type()
)
hwXQoSIfIPCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarEbs.setStatus("current")
_HwXQoSIfIPCarPir_Type = Integer32
_HwXQoSIfIPCarPir_Object = MibTableColumn
hwXQoSIfIPCarPir = _HwXQoSIfIPCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 11),
    _HwXQoSIfIPCarPir_Type()
)
hwXQoSIfIPCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarPir.setStatus("current")
_HwXQoSIfIPCarPbs_Type = Integer32
_HwXQoSIfIPCarPbs_Object = MibTableColumn
hwXQoSIfIPCarPbs = _HwXQoSIfIPCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 12),
    _HwXQoSIfIPCarPbs_Type()
)
hwXQoSIfIPCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarPbs.setStatus("current")


class _HwXQoSIfIPCarGreenAction_Type(CarAction):
    """Custom type hwXQoSIfIPCarGreenAction based on CarAction"""


_HwXQoSIfIPCarGreenAction_Object = MibTableColumn
hwXQoSIfIPCarGreenAction = _HwXQoSIfIPCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 13),
    _HwXQoSIfIPCarGreenAction_Type()
)
hwXQoSIfIPCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarGreenAction.setStatus("current")


class _HwXQoSIfIPCarGreenRemarkValue_Type(Integer32):
    """Custom type hwXQoSIfIPCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSIfIPCarGreenRemarkValue_Type.__name__ = "Integer32"
_HwXQoSIfIPCarGreenRemarkValue_Object = MibTableColumn
hwXQoSIfIPCarGreenRemarkValue = _HwXQoSIfIPCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 14),
    _HwXQoSIfIPCarGreenRemarkValue_Type()
)
hwXQoSIfIPCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarGreenRemarkValue.setStatus("current")


class _HwXQoSIfIPCarYellowAction_Type(CarAction):
    """Custom type hwXQoSIfIPCarYellowAction based on CarAction"""


_HwXQoSIfIPCarYellowAction_Object = MibTableColumn
hwXQoSIfIPCarYellowAction = _HwXQoSIfIPCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 15),
    _HwXQoSIfIPCarYellowAction_Type()
)
hwXQoSIfIPCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarYellowAction.setStatus("current")


class _HwXQoSIfIPCarYellowRemarkValue_Type(Integer32):
    """Custom type hwXQoSIfIPCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSIfIPCarYellowRemarkValue_Type.__name__ = "Integer32"
_HwXQoSIfIPCarYellowRemarkValue_Object = MibTableColumn
hwXQoSIfIPCarYellowRemarkValue = _HwXQoSIfIPCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 16),
    _HwXQoSIfIPCarYellowRemarkValue_Type()
)
hwXQoSIfIPCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarYellowRemarkValue.setStatus("current")


class _HwXQoSIfIPCarRedAction_Type(CarAction):
    """Custom type hwXQoSIfIPCarRedAction based on CarAction"""


_HwXQoSIfIPCarRedAction_Object = MibTableColumn
hwXQoSIfIPCarRedAction = _HwXQoSIfIPCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 17),
    _HwXQoSIfIPCarRedAction_Type()
)
hwXQoSIfIPCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarRedAction.setStatus("current")


class _HwXQoSIfIPCarRedRemarkValue_Type(Integer32):
    """Custom type hwXQoSIfIPCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSIfIPCarRedRemarkValue_Type.__name__ = "Integer32"
_HwXQoSIfIPCarRedRemarkValue_Object = MibTableColumn
hwXQoSIfIPCarRedRemarkValue = _HwXQoSIfIPCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 18),
    _HwXQoSIfIPCarRedRemarkValue_Type()
)
hwXQoSIfIPCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarRedRemarkValue.setStatus("current")


class _HwXQoSIfIPCarAggregation_Type(Integer32):
    """Custom type hwXQoSIfIPCarAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregationCar", 1),
          ("noneAggregationCar", 2))
    )


_HwXQoSIfIPCarAggregation_Type.__name__ = "Integer32"
_HwXQoSIfIPCarAggregation_Object = MibTableColumn
hwXQoSIfIPCarAggregation = _HwXQoSIfIPCarAggregation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 19),
    _HwXQoSIfIPCarAggregation_Type()
)
hwXQoSIfIPCarAggregation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarAggregation.setStatus("current")
_HwXQoSIfIPCarRowStatus_Type = RowStatus
_HwXQoSIfIPCarRowStatus_Object = MibTableColumn
hwXQoSIfIPCarRowStatus = _HwXQoSIfIPCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 2, 23, 1, 20),
    _HwXQoSIfIPCarRowStatus_Type()
)
hwXQoSIfIPCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSIfIPCarRowStatus.setStatus("current")
_HwXQoSCpcarObjects_ObjectIdentity = ObjectIdentity
hwXQoSCpcarObjects = _HwXQoSCpcarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3)
)
_HwXQoSCpcarCfgInfoTable_Object = MibTable
hwXQoSCpcarCfgInfoTable = _HwXQoSCpcarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwXQoSCpcarCfgInfoTable.setStatus("current")
_HwXQoSCpcarCfgInfoEntry_Object = MibTableRow
hwXQoSCpcarCfgInfoEntry = _HwXQoSCpcarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 1, 1)
)
hwXQoSCpcarCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpcarIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCpcarCfgInfoEntry.setStatus("current")
_HwXQoSCpcarIndex_Type = Integer32
_HwXQoSCpcarIndex_Object = MibTableColumn
hwXQoSCpcarIndex = _HwXQoSCpcarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 1, 1, 1),
    _HwXQoSCpcarIndex_Type()
)
hwXQoSCpcarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarIndex.setStatus("current")


class _HwXQoSCpcarName_Type(OctetString):
    """Custom type hwXQoSCpcarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSCpcarName_Type.__name__ = "OctetString"
_HwXQoSCpcarName_Object = MibTableColumn
hwXQoSCpcarName = _HwXQoSCpcarName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 1, 1, 2),
    _HwXQoSCpcarName_Type()
)
hwXQoSCpcarName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpcarName.setStatus("current")
_HwXQoSCpcarRowStatus_Type = RowStatus
_HwXQoSCpcarRowStatus_Object = MibTableColumn
hwXQoSCpcarRowStatus = _HwXQoSCpcarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 1, 1, 3),
    _HwXQoSCpcarRowStatus_Type()
)
hwXQoSCpcarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpcarRowStatus.setStatus("current")
_HwXQoSCpCarFilterCfgInfoTable_Object = MibTable
hwXQoSCpCarFilterCfgInfoTable = _HwXQoSCpCarFilterCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwXQoSCpCarFilterCfgInfoTable.setStatus("current")
_HwXQoSCpCarFilterCfgInfoEntry_Object = MibTableRow
hwXQoSCpCarFilterCfgInfoEntry = _HwXQoSCpCarFilterCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 2, 1)
)
hwXQoSCpCarFilterCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpcarIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCpCarFilterCfgInfoEntry.setStatus("current")


class _HwXQoSCpCarFilterAction_Type(Integer32):
    """Custom type hwXQoSCpCarFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("pass", 1))
    )


_HwXQoSCpCarFilterAction_Type.__name__ = "Integer32"
_HwXQoSCpCarFilterAction_Object = MibTableColumn
hwXQoSCpCarFilterAction = _HwXQoSCpCarFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 2, 1, 1),
    _HwXQoSCpCarFilterAction_Type()
)
hwXQoSCpCarFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarFilterAction.setStatus("current")
_HwXQoSCpCarFilterRowStatus_Type = RowStatus
_HwXQoSCpCarFilterRowStatus_Object = MibTableColumn
hwXQoSCpCarFilterRowStatus = _HwXQoSCpCarFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 2, 1, 2),
    _HwXQoSCpCarFilterRowStatus_Type()
)
hwXQoSCpCarFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarFilterRowStatus.setStatus("current")
_HwXQoSCpCarCfgInfoTable_Object = MibTable
hwXQoSCpCarCfgInfoTable = _HwXQoSCpCarCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwXQoSCpCarCfgInfoTable.setStatus("current")
_HwXQoSCpCarCfgInfoEntry_Object = MibTableRow
hwXQoSCpCarCfgInfoEntry = _HwXQoSCpCarCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1)
)
hwXQoSCpCarCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpcarIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCpCarCfgInfoEntry.setStatus("current")


class _HwXQoSCpCarSlotId_Type(Integer32):
    """Custom type hwXQoSCpCarSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwXQoSCpCarSlotId_Type.__name__ = "Integer32"
_HwXQoSCpCarSlotId_Object = MibTableColumn
hwXQoSCpCarSlotId = _HwXQoSCpCarSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 1),
    _HwXQoSCpCarSlotId_Type()
)
hwXQoSCpCarSlotId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotId.setStatus("current")


class _HwXQoSCpCarCir_Type(Integer32):
    """Custom type hwXQoSCpCarCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 10000000),
    )


_HwXQoSCpCarCir_Type.__name__ = "Integer32"
_HwXQoSCpCarCir_Object = MibTableColumn
hwXQoSCpCarCir = _HwXQoSCpCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 2),
    _HwXQoSCpCarCir_Type()
)
hwXQoSCpCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarCir.setStatus("current")


class _HwXQoSCpCarCbs_Type(Integer32):
    """Custom type hwXQoSCpCarCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 19375000),
    )


_HwXQoSCpCarCbs_Type.__name__ = "Integer32"
_HwXQoSCpCarCbs_Object = MibTableColumn
hwXQoSCpCarCbs = _HwXQoSCpCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 3),
    _HwXQoSCpCarCbs_Type()
)
hwXQoSCpCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarCbs.setStatus("current")


class _HwXQoSCpCarEbs_Type(Integer32):
    """Custom type hwXQoSCpCarEbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 19375000),
    )


_HwXQoSCpCarEbs_Type.__name__ = "Integer32"
_HwXQoSCpCarEbs_Object = MibTableColumn
hwXQoSCpCarEbs = _HwXQoSCpCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 4),
    _HwXQoSCpCarEbs_Type()
)
hwXQoSCpCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarEbs.setStatus("current")


class _HwXQoSCpCarPir_Type(Integer32):
    """Custom type hwXQoSCpCarPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 10000000),
    )


_HwXQoSCpCarPir_Type.__name__ = "Integer32"
_HwXQoSCpCarPir_Object = MibTableColumn
hwXQoSCpCarPir = _HwXQoSCpCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 5),
    _HwXQoSCpCarPir_Type()
)
hwXQoSCpCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarPir.setStatus("current")


class _HwXQoSCpCarPbs_Type(Integer32):
    """Custom type hwXQoSCpCarPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 4000000),
    )


_HwXQoSCpCarPbs_Type.__name__ = "Integer32"
_HwXQoSCpCarPbs_Object = MibTableColumn
hwXQoSCpCarPbs = _HwXQoSCpCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 6),
    _HwXQoSCpCarPbs_Type()
)
hwXQoSCpCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarPbs.setStatus("current")


class _HwXQoSCpCarGreenAction_Type(CarAction):
    """Custom type hwXQoSCpCarGreenAction based on CarAction"""


_HwXQoSCpCarGreenAction_Object = MibTableColumn
hwXQoSCpCarGreenAction = _HwXQoSCpCarGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 7),
    _HwXQoSCpCarGreenAction_Type()
)
hwXQoSCpCarGreenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarGreenAction.setStatus("current")


class _HwXQoSCpCarGreenRemarkValue_Type(Integer32):
    """Custom type hwXQoSCpCarGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSCpCarGreenRemarkValue_Type.__name__ = "Integer32"
_HwXQoSCpCarGreenRemarkValue_Object = MibTableColumn
hwXQoSCpCarGreenRemarkValue = _HwXQoSCpCarGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 8),
    _HwXQoSCpCarGreenRemarkValue_Type()
)
hwXQoSCpCarGreenRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarGreenRemarkValue.setStatus("current")
_HwXQoSCpCarYellowAction_Type = CarAction
_HwXQoSCpCarYellowAction_Object = MibTableColumn
hwXQoSCpCarYellowAction = _HwXQoSCpCarYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 9),
    _HwXQoSCpCarYellowAction_Type()
)
hwXQoSCpCarYellowAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarYellowAction.setStatus("current")


class _HwXQoSCpCarYellowRemarkValue_Type(Integer32):
    """Custom type hwXQoSCpCarYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSCpCarYellowRemarkValue_Type.__name__ = "Integer32"
_HwXQoSCpCarYellowRemarkValue_Object = MibTableColumn
hwXQoSCpCarYellowRemarkValue = _HwXQoSCpCarYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 10),
    _HwXQoSCpCarYellowRemarkValue_Type()
)
hwXQoSCpCarYellowRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarYellowRemarkValue.setStatus("current")


class _HwXQoSCpCarRedAction_Type(CarAction):
    """Custom type hwXQoSCpCarRedAction based on CarAction"""


_HwXQoSCpCarRedAction_Object = MibTableColumn
hwXQoSCpCarRedAction = _HwXQoSCpCarRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 11),
    _HwXQoSCpCarRedAction_Type()
)
hwXQoSCpCarRedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarRedAction.setStatus("current")


class _HwXQoSCpCarRedRemarkValue_Type(Integer32):
    """Custom type hwXQoSCpCarRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSCpCarRedRemarkValue_Type.__name__ = "Integer32"
_HwXQoSCpCarRedRemarkValue_Object = MibTableColumn
hwXQoSCpCarRedRemarkValue = _HwXQoSCpCarRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 12),
    _HwXQoSCpCarRedRemarkValue_Type()
)
hwXQoSCpCarRedRemarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarRedRemarkValue.setStatus("current")
_HwXQoSCpCarRowStatus_Type = RowStatus
_HwXQoSCpCarRowStatus_Object = MibTableColumn
hwXQoSCpCarRowStatus = _HwXQoSCpCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 3, 1, 13),
    _HwXQoSCpCarRowStatus_Type()
)
hwXQoSCpCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpCarRowStatus.setStatus("current")
_HwXQoSCpApplyPolicyTable_Object = MibTable
hwXQoSCpApplyPolicyTable = _HwXQoSCpApplyPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwXQoSCpApplyPolicyTable.setStatus("current")
_HwXQoSCpApplyPolicyEntry_Object = MibTableRow
hwXQoSCpApplyPolicyEntry = _HwXQoSCpApplyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 4, 1)
)
hwXQoSCpApplyPolicyEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpcarIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCpApplyPolicyEntry.setStatus("current")


class _HwXQoSCpApplyPolicyName_Type(OctetString):
    """Custom type hwXQoSCpApplyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSCpApplyPolicyName_Type.__name__ = "OctetString"
_HwXQoSCpApplyPolicyName_Object = MibTableColumn
hwXQoSCpApplyPolicyName = _HwXQoSCpApplyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 4, 1, 1),
    _HwXQoSCpApplyPolicyName_Type()
)
hwXQoSCpApplyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpApplyPolicyName.setStatus("current")
_HwXQoSCpApplyPolicyRowStatus_Type = RowStatus
_HwXQoSCpApplyPolicyRowStatus_Object = MibTableColumn
hwXQoSCpApplyPolicyRowStatus = _HwXQoSCpApplyPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 4, 1, 2),
    _HwXQoSCpApplyPolicyRowStatus_Type()
)
hwXQoSCpApplyPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSCpApplyPolicyRowStatus.setStatus("current")
_HwXQoSCpCarActionTable_Object = MibTable
hwXQoSCpCarActionTable = _HwXQoSCpCarActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hwXQoSCpCarActionTable.setStatus("current")
_HwXQoSCpCarActionEntry_Object = MibTableRow
hwXQoSCpCarActionEntry = _HwXQoSCpCarActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1)
)
hwXQoSCpCarActionEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpCarActionSlotIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpCarActionPacketType"),
)
if mibBuilder.loadTexts:
    hwXQoSCpCarActionEntry.setStatus("current")
_HwXQoSCpCarActionSlotIndex_Type = Integer32
_HwXQoSCpCarActionSlotIndex_Object = MibTableColumn
hwXQoSCpCarActionSlotIndex = _HwXQoSCpCarActionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 1),
    _HwXQoSCpCarActionSlotIndex_Type()
)
hwXQoSCpCarActionSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionSlotIndex.setStatus("current")
_HwXQoSCpCarActionPacketType_Type = Integer32
_HwXQoSCpCarActionPacketType_Object = MibTableColumn
hwXQoSCpCarActionPacketType = _HwXQoSCpCarActionPacketType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 2),
    _HwXQoSCpCarActionPacketType_Type()
)
hwXQoSCpCarActionPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionPacketType.setStatus("current")


class _HwXQoSCpCarActionPacketTypeName_Type(OctetString):
    """Custom type hwXQoSCpCarActionPacketTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSCpCarActionPacketTypeName_Type.__name__ = "OctetString"
_HwXQoSCpCarActionPacketTypeName_Object = MibTableColumn
hwXQoSCpCarActionPacketTypeName = _HwXQoSCpCarActionPacketTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 3),
    _HwXQoSCpCarActionPacketTypeName_Type()
)
hwXQoSCpCarActionPacketTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionPacketTypeName.setStatus("current")


class _HwXQoSCpCarActionType_Type(Bits):
    """Custom type hwXQoSCpCarActionType based on Bits"""
    namedValues = NamedValues(
        *(("car", 2),
          ("discard", 1),
          ("pass", 0),
          ("traffic-policy", 3))
    )

_HwXQoSCpCarActionType_Type.__name__ = "Bits"
_HwXQoSCpCarActionType_Object = MibTableColumn
hwXQoSCpCarActionType = _HwXQoSCpCarActionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 4),
    _HwXQoSCpCarActionType_Type()
)
hwXQoSCpCarActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionType.setStatus("current")


class _HwXQoSCpCarActionPolicyName_Type(OctetString):
    """Custom type hwXQoSCpCarActionPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwXQoSCpCarActionPolicyName_Type.__name__ = "OctetString"
_HwXQoSCpCarActionPolicyName_Object = MibTableColumn
hwXQoSCpCarActionPolicyName = _HwXQoSCpCarActionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 5),
    _HwXQoSCpCarActionPolicyName_Type()
)
hwXQoSCpCarActionPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionPolicyName.setStatus("current")


class _HwXQoSCpCarActionCarCir_Type(Integer32):
    """Custom type hwXQoSCpCarActionCarCir based on Integer32"""
    defaultValue = -1


_HwXQoSCpCarActionCarCir_Object = MibTableColumn
hwXQoSCpCarActionCarCir = _HwXQoSCpCarActionCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 6),
    _HwXQoSCpCarActionCarCir_Type()
)
hwXQoSCpCarActionCarCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionCarCir.setStatus("current")


class _HwXQoSCpCarActionCarCbs_Type(Integer32):
    """Custom type hwXQoSCpCarActionCarCbs based on Integer32"""
    defaultValue = -1


_HwXQoSCpCarActionCarCbs_Object = MibTableColumn
hwXQoSCpCarActionCarCbs = _HwXQoSCpCarActionCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 7),
    _HwXQoSCpCarActionCarCbs_Type()
)
hwXQoSCpCarActionCarCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionCarCbs.setStatus("current")


class _HwXQoSCpCarActionCarEbs_Type(Integer32):
    """Custom type hwXQoSCpCarActionCarEbs based on Integer32"""
    defaultValue = -1


_HwXQoSCpCarActionCarEbs_Object = MibTableColumn
hwXQoSCpCarActionCarEbs = _HwXQoSCpCarActionCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 8),
    _HwXQoSCpCarActionCarEbs_Type()
)
hwXQoSCpCarActionCarEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionCarEbs.setStatus("current")


class _HwXQoSCpCarActionCarPir_Type(Integer32):
    """Custom type hwXQoSCpCarActionCarPir based on Integer32"""
    defaultValue = -1


_HwXQoSCpCarActionCarPir_Object = MibTableColumn
hwXQoSCpCarActionCarPir = _HwXQoSCpCarActionCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 9),
    _HwXQoSCpCarActionCarPir_Type()
)
hwXQoSCpCarActionCarPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionCarPir.setStatus("current")


class _HwXQoSCpCarActionCarPbs_Type(Integer32):
    """Custom type hwXQoSCpCarActionCarPbs based on Integer32"""
    defaultValue = -1


_HwXQoSCpCarActionCarPbs_Object = MibTableColumn
hwXQoSCpCarActionCarPbs = _HwXQoSCpCarActionCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 10),
    _HwXQoSCpCarActionCarPbs_Type()
)
hwXQoSCpCarActionCarPbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionCarPbs.setStatus("current")
_HwXQoSCpCarActionGreenAction_Type = CarAction
_HwXQoSCpCarActionGreenAction_Object = MibTableColumn
hwXQoSCpCarActionGreenAction = _HwXQoSCpCarActionGreenAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 11),
    _HwXQoSCpCarActionGreenAction_Type()
)
hwXQoSCpCarActionGreenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionGreenAction.setStatus("current")


class _HwXQoSCpCarActionGreenRemarkValue_Type(Integer32):
    """Custom type hwXQoSCpCarActionGreenRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSCpCarActionGreenRemarkValue_Type.__name__ = "Integer32"
_HwXQoSCpCarActionGreenRemarkValue_Object = MibTableColumn
hwXQoSCpCarActionGreenRemarkValue = _HwXQoSCpCarActionGreenRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 12),
    _HwXQoSCpCarActionGreenRemarkValue_Type()
)
hwXQoSCpCarActionGreenRemarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionGreenRemarkValue.setStatus("current")
_HwXQoSCpCarActionYellowAction_Type = CarAction
_HwXQoSCpCarActionYellowAction_Object = MibTableColumn
hwXQoSCpCarActionYellowAction = _HwXQoSCpCarActionYellowAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 13),
    _HwXQoSCpCarActionYellowAction_Type()
)
hwXQoSCpCarActionYellowAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionYellowAction.setStatus("current")


class _HwXQoSCpCarActionYellowRemarkValue_Type(Integer32):
    """Custom type hwXQoSCpCarActionYellowRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSCpCarActionYellowRemarkValue_Type.__name__ = "Integer32"
_HwXQoSCpCarActionYellowRemarkValue_Object = MibTableColumn
hwXQoSCpCarActionYellowRemarkValue = _HwXQoSCpCarActionYellowRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 14),
    _HwXQoSCpCarActionYellowRemarkValue_Type()
)
hwXQoSCpCarActionYellowRemarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionYellowRemarkValue.setStatus("current")
_HwXQoSCpCarActionRedAction_Type = CarAction
_HwXQoSCpCarActionRedAction_Object = MibTableColumn
hwXQoSCpCarActionRedAction = _HwXQoSCpCarActionRedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 15),
    _HwXQoSCpCarActionRedAction_Type()
)
hwXQoSCpCarActionRedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionRedAction.setStatus("current")


class _HwXQoSCpCarActionRedRemarkValue_Type(Integer32):
    """Custom type hwXQoSCpCarActionRedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_HwXQoSCpCarActionRedRemarkValue_Type.__name__ = "Integer32"
_HwXQoSCpCarActionRedRemarkValue_Object = MibTableColumn
hwXQoSCpCarActionRedRemarkValue = _HwXQoSCpCarActionRedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 16),
    _HwXQoSCpCarActionRedRemarkValue_Type()
)
hwXQoSCpCarActionRedRemarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionRedRemarkValue.setStatus("current")


class _HwXQoSCpCarActionSetDefault_Type(Integer32):
    """Custom type hwXQoSCpCarActionSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwXQoSCpCarActionSetDefault_Type.__name__ = "Integer32"
_HwXQoSCpCarActionSetDefault_Object = MibTableColumn
hwXQoSCpCarActionSetDefault = _HwXQoSCpCarActionSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 3, 5, 1, 17),
    _HwXQoSCpCarActionSetDefault_Type()
)
hwXQoSCpCarActionSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSCpCarActionSetDefault.setStatus("current")
_HwXQoSStatisticsObjects_ObjectIdentity = ObjectIdentity
hwXQoSStatisticsObjects = _HwXQoSStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4)
)
_HwXQoSCpcarStaticsObjects_ObjectIdentity = ObjectIdentity
hwXQoSCpcarStaticsObjects = _HwXQoSCpcarStaticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2)
)
_HwXQoSCpcarRunInfoTable_Object = MibTable
hwXQoSCpcarRunInfoTable = _HwXQoSCpcarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hwXQoSCpcarRunInfoTable.setStatus("current")
_HwXQoSCpcarRunInfoEntry_Object = MibTableRow
hwXQoSCpcarRunInfoEntry = _HwXQoSCpcarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1)
)
hwXQoSCpcarRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpcarIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCpcarRunInfoEntry.setStatus("current")
_HwXQoSCpcarPassedPackets_Type = Counter64
_HwXQoSCpcarPassedPackets_Object = MibTableColumn
hwXQoSCpcarPassedPackets = _HwXQoSCpcarPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1, 1),
    _HwXQoSCpcarPassedPackets_Type()
)
hwXQoSCpcarPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarPassedPackets.setStatus("current")
_HwXQoSCpcarPassededBytes_Type = Counter64
_HwXQoSCpcarPassededBytes_Object = MibTableColumn
hwXQoSCpcarPassededBytes = _HwXQoSCpcarPassededBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1, 2),
    _HwXQoSCpcarPassededBytes_Type()
)
hwXQoSCpcarPassededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarPassededBytes.setStatus("current")
_HwXQoSCpcarTotalPackets_Type = Counter64
_HwXQoSCpcarTotalPackets_Object = MibTableColumn
hwXQoSCpcarTotalPackets = _HwXQoSCpcarTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1, 3),
    _HwXQoSCpcarTotalPackets_Type()
)
hwXQoSCpcarTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarTotalPackets.setStatus("current")
_HwXQoSCpcarTotalBytes_Type = Counter64
_HwXQoSCpcarTotalBytes_Object = MibTableColumn
hwXQoSCpcarTotalBytes = _HwXQoSCpcarTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1, 4),
    _HwXQoSCpcarTotalBytes_Type()
)
hwXQoSCpcarTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarTotalBytes.setStatus("current")
_HwXQoSCpcarDiscardedPackets_Type = Counter64
_HwXQoSCpcarDiscardedPackets_Object = MibTableColumn
hwXQoSCpcarDiscardedPackets = _HwXQoSCpcarDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1, 5),
    _HwXQoSCpcarDiscardedPackets_Type()
)
hwXQoSCpcarDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarDiscardedPackets.setStatus("current")
_HwXQoSCpcarDiscardedBytes_Type = Counter64
_HwXQoSCpcarDiscardedBytes_Object = MibTableColumn
hwXQoSCpcarDiscardedBytes = _HwXQoSCpcarDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 1, 1, 6),
    _HwXQoSCpcarDiscardedBytes_Type()
)
hwXQoSCpcarDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpcarDiscardedBytes.setStatus("current")
_HwXQoSCpCarSlotStatTable_Object = MibTable
hwXQoSCpCarSlotStatTable = _HwXQoSCpCarSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatTable.setStatus("current")
_HwXQoSCpCarSlotStatEntry_Object = MibTableRow
hwXQoSCpCarSlotStatEntry = _HwXQoSCpCarSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1)
)
hwXQoSCpCarSlotStatEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpCarSlotStatSlotIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpCarSlotStatPacketType"),
)
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatEntry.setStatus("current")
_HwXQoSCpCarSlotStatSlotIndex_Type = Integer32
_HwXQoSCpCarSlotStatSlotIndex_Object = MibTableColumn
hwXQoSCpCarSlotStatSlotIndex = _HwXQoSCpCarSlotStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 1),
    _HwXQoSCpCarSlotStatSlotIndex_Type()
)
hwXQoSCpCarSlotStatSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatSlotIndex.setStatus("current")
_HwXQoSCpCarSlotStatPacketType_Type = Integer32
_HwXQoSCpCarSlotStatPacketType_Object = MibTableColumn
hwXQoSCpCarSlotStatPacketType = _HwXQoSCpCarSlotStatPacketType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 2),
    _HwXQoSCpCarSlotStatPacketType_Type()
)
hwXQoSCpCarSlotStatPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatPacketType.setStatus("current")
_HwXQoSCpCarSlotStatDiscardedPackets_Type = Counter64
_HwXQoSCpCarSlotStatDiscardedPackets_Object = MibTableColumn
hwXQoSCpCarSlotStatDiscardedPackets = _HwXQoSCpCarSlotStatDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 3),
    _HwXQoSCpCarSlotStatDiscardedPackets_Type()
)
hwXQoSCpCarSlotStatDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatDiscardedPackets.setStatus("current")
_HwXQoSCpCarSlotStatDiscardedBytes_Type = Counter64
_HwXQoSCpCarSlotStatDiscardedBytes_Object = MibTableColumn
hwXQoSCpCarSlotStatDiscardedBytes = _HwXQoSCpCarSlotStatDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 4),
    _HwXQoSCpCarSlotStatDiscardedBytes_Type()
)
hwXQoSCpCarSlotStatDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatDiscardedBytes.setStatus("current")
_HwXQoSCpCarSlotStatPassedPackets_Type = Counter64
_HwXQoSCpCarSlotStatPassedPackets_Object = MibTableColumn
hwXQoSCpCarSlotStatPassedPackets = _HwXQoSCpCarSlotStatPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 5),
    _HwXQoSCpCarSlotStatPassedPackets_Type()
)
hwXQoSCpCarSlotStatPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatPassedPackets.setStatus("current")
_HwXQoSCpCarSlotStatPassededBytes_Type = Counter64
_HwXQoSCpCarSlotStatPassededBytes_Object = MibTableColumn
hwXQoSCpCarSlotStatPassededBytes = _HwXQoSCpCarSlotStatPassededBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 6),
    _HwXQoSCpCarSlotStatPassededBytes_Type()
)
hwXQoSCpCarSlotStatPassededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatPassededBytes.setStatus("current")
_HwXQoSCpCarSlotStatTotalPackets_Type = Counter64
_HwXQoSCpCarSlotStatTotalPackets_Object = MibTableColumn
hwXQoSCpCarSlotStatTotalPackets = _HwXQoSCpCarSlotStatTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 7),
    _HwXQoSCpCarSlotStatTotalPackets_Type()
)
hwXQoSCpCarSlotStatTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatTotalPackets.setStatus("current")
_HwXQoSCpCarSlotStatTotalBytes_Type = Counter64
_HwXQoSCpCarSlotStatTotalBytes_Object = MibTableColumn
hwXQoSCpCarSlotStatTotalBytes = _HwXQoSCpCarSlotStatTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 2, 2, 1, 8),
    _HwXQoSCpCarSlotStatTotalBytes_Type()
)
hwXQoSCpCarSlotStatTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpCarSlotStatTotalBytes.setStatus("current")
_HwXQoSIfStatisticsObjects_ObjectIdentity = ObjectIdentity
hwXQoSIfStatisticsObjects = _HwXQoSIfStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3)
)
_HwXQoSIfCarRunInfoTable_Object = MibTable
hwXQoSIfCarRunInfoTable = _HwXQoSIfCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hwXQoSIfCarRunInfoTable.setStatus("current")
_HwXQoSIfCarRunInfoEntry_Object = MibTableRow
hwXQoSIfCarRunInfoEntry = _HwXQoSIfCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1)
)
hwXQoSIfCarRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfCarRunInfoEntry.setStatus("current")
_HwXQoSIfCarIndex_Type = Integer32
_HwXQoSIfCarIndex_Object = MibTableColumn
hwXQoSIfCarIndex = _HwXQoSIfCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 1),
    _HwXQoSIfCarIndex_Type()
)
hwXQoSIfCarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarIndex.setStatus("current")


class _HwXQoSIfVlanID_Type(Integer32):
    """Custom type hwXQoSIfVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfVlanID_Type.__name__ = "Integer32"
_HwXQoSIfVlanID_Object = MibTableColumn
hwXQoSIfVlanID = _HwXQoSIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 2),
    _HwXQoSIfVlanID_Type()
)
hwXQoSIfVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfVlanID.setStatus("current")
_HwXQoSIfCarGreenPassedPackets_Type = Counter64
_HwXQoSIfCarGreenPassedPackets_Object = MibTableColumn
hwXQoSIfCarGreenPassedPackets = _HwXQoSIfCarGreenPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 3),
    _HwXQoSIfCarGreenPassedPackets_Type()
)
hwXQoSIfCarGreenPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenPassedPackets.setStatus("current")
_HwXQoSIfCarGreenPassedBytes_Type = Counter64
_HwXQoSIfCarGreenPassedBytes_Object = MibTableColumn
hwXQoSIfCarGreenPassedBytes = _HwXQoSIfCarGreenPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 4),
    _HwXQoSIfCarGreenPassedBytes_Type()
)
hwXQoSIfCarGreenPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenPassedBytes.setStatus("current")
_HwXQoSIfCarGreenRemarkedPackets_Type = Counter64
_HwXQoSIfCarGreenRemarkedPackets_Object = MibTableColumn
hwXQoSIfCarGreenRemarkedPackets = _HwXQoSIfCarGreenRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 5),
    _HwXQoSIfCarGreenRemarkedPackets_Type()
)
hwXQoSIfCarGreenRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenRemarkedPackets.setStatus("current")
_HwXQoSIfCarGreenRemarkedBytes_Type = Counter64
_HwXQoSIfCarGreenRemarkedBytes_Object = MibTableColumn
hwXQoSIfCarGreenRemarkedBytes = _HwXQoSIfCarGreenRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 6),
    _HwXQoSIfCarGreenRemarkedBytes_Type()
)
hwXQoSIfCarGreenRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenRemarkedBytes.setStatus("current")
_HwXQoSIfCarGreenDiscardedPackets_Type = Counter64
_HwXQoSIfCarGreenDiscardedPackets_Object = MibTableColumn
hwXQoSIfCarGreenDiscardedPackets = _HwXQoSIfCarGreenDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 7),
    _HwXQoSIfCarGreenDiscardedPackets_Type()
)
hwXQoSIfCarGreenDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenDiscardedPackets.setStatus("current")
_HwXQoSIfCarGreenDiscardedBytes_Type = Counter64
_HwXQoSIfCarGreenDiscardedBytes_Object = MibTableColumn
hwXQoSIfCarGreenDiscardedBytes = _HwXQoSIfCarGreenDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 8),
    _HwXQoSIfCarGreenDiscardedBytes_Type()
)
hwXQoSIfCarGreenDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarGreenDiscardedBytes.setStatus("current")
_HwXQoSIfCarYellowPassedPackets_Type = Counter64
_HwXQoSIfCarYellowPassedPackets_Object = MibTableColumn
hwXQoSIfCarYellowPassedPackets = _HwXQoSIfCarYellowPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 9),
    _HwXQoSIfCarYellowPassedPackets_Type()
)
hwXQoSIfCarYellowPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowPassedPackets.setStatus("current")
_HwXQoSIfCarYellowPassedBytes_Type = Counter64
_HwXQoSIfCarYellowPassedBytes_Object = MibTableColumn
hwXQoSIfCarYellowPassedBytes = _HwXQoSIfCarYellowPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 10),
    _HwXQoSIfCarYellowPassedBytes_Type()
)
hwXQoSIfCarYellowPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowPassedBytes.setStatus("current")
_HwXQoSIfCarYellowRemarkedPackets_Type = Counter64
_HwXQoSIfCarYellowRemarkedPackets_Object = MibTableColumn
hwXQoSIfCarYellowRemarkedPackets = _HwXQoSIfCarYellowRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 11),
    _HwXQoSIfCarYellowRemarkedPackets_Type()
)
hwXQoSIfCarYellowRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowRemarkedPackets.setStatus("current")
_HwXQoSIfCarYellowRemarkedBytes_Type = Counter64
_HwXQoSIfCarYellowRemarkedBytes_Object = MibTableColumn
hwXQoSIfCarYellowRemarkedBytes = _HwXQoSIfCarYellowRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 12),
    _HwXQoSIfCarYellowRemarkedBytes_Type()
)
hwXQoSIfCarYellowRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowRemarkedBytes.setStatus("current")
_HwXQoSIfCarYellowDiscardedPackets_Type = Counter64
_HwXQoSIfCarYellowDiscardedPackets_Object = MibTableColumn
hwXQoSIfCarYellowDiscardedPackets = _HwXQoSIfCarYellowDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 13),
    _HwXQoSIfCarYellowDiscardedPackets_Type()
)
hwXQoSIfCarYellowDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowDiscardedPackets.setStatus("current")
_HwXQoSIfCarYellowDiscardedBytes_Type = Counter64
_HwXQoSIfCarYellowDiscardedBytes_Object = MibTableColumn
hwXQoSIfCarYellowDiscardedBytes = _HwXQoSIfCarYellowDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 14),
    _HwXQoSIfCarYellowDiscardedBytes_Type()
)
hwXQoSIfCarYellowDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarYellowDiscardedBytes.setStatus("current")
_HwXQoSIfCarRedPassedPackets_Type = Counter64
_HwXQoSIfCarRedPassedPackets_Object = MibTableColumn
hwXQoSIfCarRedPassedPackets = _HwXQoSIfCarRedPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 15),
    _HwXQoSIfCarRedPassedPackets_Type()
)
hwXQoSIfCarRedPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedPassedPackets.setStatus("current")
_HwXQoSIfCarRedPassedBytes_Type = Counter64
_HwXQoSIfCarRedPassedBytes_Object = MibTableColumn
hwXQoSIfCarRedPassedBytes = _HwXQoSIfCarRedPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 16),
    _HwXQoSIfCarRedPassedBytes_Type()
)
hwXQoSIfCarRedPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedPassedBytes.setStatus("current")
_HwXQoSIfCarRedRemarkedPackets_Type = Counter64
_HwXQoSIfCarRedRemarkedPackets_Object = MibTableColumn
hwXQoSIfCarRedRemarkedPackets = _HwXQoSIfCarRedRemarkedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 17),
    _HwXQoSIfCarRedRemarkedPackets_Type()
)
hwXQoSIfCarRedRemarkedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedRemarkedPackets.setStatus("current")
_HwXQoSIfCarRedRemarkedBytes_Type = Counter64
_HwXQoSIfCarRedRemarkedBytes_Object = MibTableColumn
hwXQoSIfCarRedRemarkedBytes = _HwXQoSIfCarRedRemarkedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 18),
    _HwXQoSIfCarRedRemarkedBytes_Type()
)
hwXQoSIfCarRedRemarkedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedRemarkedBytes.setStatus("current")
_HwXQoSIfCarRedDiscardedPackets_Type = Counter64
_HwXQoSIfCarRedDiscardedPackets_Object = MibTableColumn
hwXQoSIfCarRedDiscardedPackets = _HwXQoSIfCarRedDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 19),
    _HwXQoSIfCarRedDiscardedPackets_Type()
)
hwXQoSIfCarRedDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedDiscardedPackets.setStatus("current")
_HwXQoSIfCarRedDiscardedBytes_Type = Counter64
_HwXQoSIfCarRedDiscardedBytes_Object = MibTableColumn
hwXQoSIfCarRedDiscardedBytes = _HwXQoSIfCarRedDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 20),
    _HwXQoSIfCarRedDiscardedBytes_Type()
)
hwXQoSIfCarRedDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarRedDiscardedBytes.setStatus("current")
_HwXQoSIfCarTotalDiscardPackets_Type = Counter64
_HwXQoSIfCarTotalDiscardPackets_Object = MibTableColumn
hwXQoSIfCarTotalDiscardPackets = _HwXQoSIfCarTotalDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 21),
    _HwXQoSIfCarTotalDiscardPackets_Type()
)
hwXQoSIfCarTotalDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarTotalDiscardPackets.setStatus("current")
_HwXQoSIfCarInBoundDiscardPackets_Type = Counter64
_HwXQoSIfCarInBoundDiscardPackets_Object = MibTableColumn
hwXQoSIfCarInBoundDiscardPackets = _HwXQoSIfCarInBoundDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 22),
    _HwXQoSIfCarInBoundDiscardPackets_Type()
)
hwXQoSIfCarInBoundDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarInBoundDiscardPackets.setStatus("current")
_HwXQoSIfCarOutBoundDiscardPackets_Type = Counter64
_HwXQoSIfCarOutBoundDiscardPackets_Object = MibTableColumn
hwXQoSIfCarOutBoundDiscardPackets = _HwXQoSIfCarOutBoundDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 1, 1, 23),
    _HwXQoSIfCarOutBoundDiscardPackets_Type()
)
hwXQoSIfCarOutBoundDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarOutBoundDiscardPackets.setStatus("current")
_HwXQoSIfQueueRunInfoTable_Object = MibTable
hwXQoSIfQueueRunInfoTable = _HwXQoSIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hwXQoSIfQueueRunInfoTable.setStatus("current")
_HwXQoSIfQueueRunInfoEntry_Object = MibTableRow
hwXQoSIfQueueRunInfoEntry = _HwXQoSIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1)
)
hwXQoSIfQueueRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueVlanID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueueCosType"),
)
if mibBuilder.loadTexts:
    hwXQoSIfQueueRunInfoEntry.setStatus("current")
_HwXQoSIfQueueIfIndex_Type = Integer32
_HwXQoSIfQueueIfIndex_Object = MibTableColumn
hwXQoSIfQueueIfIndex = _HwXQoSIfQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 1),
    _HwXQoSIfQueueIfIndex_Type()
)
hwXQoSIfQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueIfIndex.setStatus("current")


class _HwXQoSIfQueueVlanID_Type(Integer32):
    """Custom type hwXQoSIfQueueVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfQueueVlanID_Type.__name__ = "Integer32"
_HwXQoSIfQueueVlanID_Object = MibTableColumn
hwXQoSIfQueueVlanID = _HwXQoSIfQueueVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 2),
    _HwXQoSIfQueueVlanID_Type()
)
hwXQoSIfQueueVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueVlanID.setStatus("current")
_HwXQoSIfQueueCosType_Type = CosType
_HwXQoSIfQueueCosType_Object = MibTableColumn
hwXQoSIfQueueCosType = _HwXQoSIfQueueCosType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 3),
    _HwXQoSIfQueueCosType_Type()
)
hwXQoSIfQueueCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueCosType.setStatus("current")
_HwXQoSIfQueuePassedPackets_Type = Counter64
_HwXQoSIfQueuePassedPackets_Object = MibTableColumn
hwXQoSIfQueuePassedPackets = _HwXQoSIfQueuePassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 4),
    _HwXQoSIfQueuePassedPackets_Type()
)
hwXQoSIfQueuePassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueuePassedPackets.setStatus("current")
_HwXQoSIfQueuePassededBytes_Type = Counter64
_HwXQoSIfQueuePassededBytes_Object = MibTableColumn
hwXQoSIfQueuePassededBytes = _HwXQoSIfQueuePassededBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 5),
    _HwXQoSIfQueuePassededBytes_Type()
)
hwXQoSIfQueuePassededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueuePassededBytes.setStatus("current")
_HwXQoSIfQueueTotalPackets_Type = Counter64
_HwXQoSIfQueueTotalPackets_Object = MibTableColumn
hwXQoSIfQueueTotalPackets = _HwXQoSIfQueueTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 6),
    _HwXQoSIfQueueTotalPackets_Type()
)
hwXQoSIfQueueTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueTotalPackets.setStatus("current")
_HwXQoSIfQueueTotalBytes_Type = Counter64
_HwXQoSIfQueueTotalBytes_Object = MibTableColumn
hwXQoSIfQueueTotalBytes = _HwXQoSIfQueueTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 7),
    _HwXQoSIfQueueTotalBytes_Type()
)
hwXQoSIfQueueTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueTotalBytes.setStatus("current")
_HwXQoSIfQueueDiscardedPackets_Type = Counter64
_HwXQoSIfQueueDiscardedPackets_Object = MibTableColumn
hwXQoSIfQueueDiscardedPackets = _HwXQoSIfQueueDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 8),
    _HwXQoSIfQueueDiscardedPackets_Type()
)
hwXQoSIfQueueDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueDiscardedPackets.setStatus("current")
_HwXQoSIfQueueDiscardedBytes_Type = Counter64
_HwXQoSIfQueueDiscardedBytes_Object = MibTableColumn
hwXQoSIfQueueDiscardedBytes = _HwXQoSIfQueueDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 9),
    _HwXQoSIfQueueDiscardedBytes_Type()
)
hwXQoSIfQueueDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueDiscardedBytes.setStatus("current")
_HwXQoSIfQueuePassedPacketRate_Type = Counter64
_HwXQoSIfQueuePassedPacketRate_Object = MibTableColumn
hwXQoSIfQueuePassedPacketRate = _HwXQoSIfQueuePassedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 10),
    _HwXQoSIfQueuePassedPacketRate_Type()
)
hwXQoSIfQueuePassedPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueuePassedPacketRate.setStatus("current")
_HwXQoSIfQueuePassedByteRate_Type = Counter64
_HwXQoSIfQueuePassedByteRate_Object = MibTableColumn
hwXQoSIfQueuePassedByteRate = _HwXQoSIfQueuePassedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 11),
    _HwXQoSIfQueuePassedByteRate_Type()
)
hwXQoSIfQueuePassedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueuePassedByteRate.setStatus("current")
_HwXQoSIfQueueDiscardedPacketRate_Type = Counter64
_HwXQoSIfQueueDiscardedPacketRate_Object = MibTableColumn
hwXQoSIfQueueDiscardedPacketRate = _HwXQoSIfQueueDiscardedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 12),
    _HwXQoSIfQueueDiscardedPacketRate_Type()
)
hwXQoSIfQueueDiscardedPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueDiscardedPacketRate.setStatus("current")
_HwXQoSIfQueueDiscardedByteRate_Type = Counter64
_HwXQoSIfQueueDiscardedByteRate_Object = MibTableColumn
hwXQoSIfQueueDiscardedByteRate = _HwXQoSIfQueueDiscardedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 13),
    _HwXQoSIfQueueDiscardedByteRate_Type()
)
hwXQoSIfQueueDiscardedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueDiscardedByteRate.setStatus("current")
_HwXQoSIfQueueResetFlag_Type = ResetFlag
_HwXQoSIfQueueResetFlag_Object = MibTableColumn
hwXQoSIfQueueResetFlag = _HwXQoSIfQueueResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 14),
    _HwXQoSIfQueueResetFlag_Type()
)
hwXQoSIfQueueResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSIfQueueResetFlag.setStatus("current")
_HwXQoSIfQueueUsagePercentage_Type = Integer32
_HwXQoSIfQueueUsagePercentage_Object = MibTableColumn
hwXQoSIfQueueUsagePercentage = _HwXQoSIfQueueUsagePercentage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 3, 1, 15),
    _HwXQoSIfQueueUsagePercentage_Type()
)
hwXQoSIfQueueUsagePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueueUsagePercentage.setStatus("current")
_HwXQoSIfWredRunInfoTable_Object = MibTable
hwXQoSIfWredRunInfoTable = _HwXQoSIfWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hwXQoSIfWredRunInfoTable.setStatus("current")
_HwXQoSIfWredRunInfoEntry_Object = MibTableRow
hwXQoSIfWredRunInfoEntry = _HwXQoSIfWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4, 1)
)
hwXQoSIfWredRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfWredIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfWredVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfWredRunInfoEntry.setStatus("current")
_HwXQoSIfWredIfIndex_Type = Integer32
_HwXQoSIfWredIfIndex_Object = MibTableColumn
hwXQoSIfWredIfIndex = _HwXQoSIfWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4, 1, 1),
    _HwXQoSIfWredIfIndex_Type()
)
hwXQoSIfWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredIfIndex.setStatus("current")


class _HwXQoSIfWredVlanID_Type(Integer32):
    """Custom type hwXQoSIfWredVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfWredVlanID_Type.__name__ = "Integer32"
_HwXQoSIfWredVlanID_Object = MibTableColumn
hwXQoSIfWredVlanID = _HwXQoSIfWredVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4, 1, 2),
    _HwXQoSIfWredVlanID_Type()
)
hwXQoSIfWredVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredVlanID.setStatus("current")
_HwXQoSIfWredRandomDiscardedPackets_Type = Counter64
_HwXQoSIfWredRandomDiscardedPackets_Object = MibTableColumn
hwXQoSIfWredRandomDiscardedPackets = _HwXQoSIfWredRandomDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4, 1, 3),
    _HwXQoSIfWredRandomDiscardedPackets_Type()
)
hwXQoSIfWredRandomDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredRandomDiscardedPackets.setStatus("current")
_HwXQoSIfWredTailDiscardedPackets_Type = Counter64
_HwXQoSIfWredTailDiscardedPackets_Object = MibTableColumn
hwXQoSIfWredTailDiscardedPackets = _HwXQoSIfWredTailDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4, 1, 4),
    _HwXQoSIfWredTailDiscardedPackets_Type()
)
hwXQoSIfWredTailDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredTailDiscardedPackets.setStatus("current")
_HwXQoSIfWredDiscardedPackets_Type = Counter64
_HwXQoSIfWredDiscardedPackets_Object = MibTableColumn
hwXQoSIfWredDiscardedPackets = _HwXQoSIfWredDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 4, 1, 5),
    _HwXQoSIfWredDiscardedPackets_Type()
)
hwXQoSIfWredDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfWredDiscardedPackets.setStatus("current")
_HwXQoSIfLrRunInfoTable_Object = MibTable
hwXQoSIfLrRunInfoTable = _HwXQoSIfLrRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    hwXQoSIfLrRunInfoTable.setStatus("current")
_HwXQoSIfLrRunInfoEntry_Object = MibTableRow
hwXQoSIfLrRunInfoEntry = _HwXQoSIfLrRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1)
)
hwXQoSIfLrRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfLrIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfLrVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfLrRunInfoEntry.setStatus("current")
_HwXQoSIfLrIfIndex_Type = Integer32
_HwXQoSIfLrIfIndex_Object = MibTableColumn
hwXQoSIfLrIfIndex = _HwXQoSIfLrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 1),
    _HwXQoSIfLrIfIndex_Type()
)
hwXQoSIfLrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrIfIndex.setStatus("current")


class _HwXQoSIfLrVlanID_Type(Integer32):
    """Custom type hwXQoSIfLrVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfLrVlanID_Type.__name__ = "Integer32"
_HwXQoSIfLrVlanID_Object = MibTableColumn
hwXQoSIfLrVlanID = _HwXQoSIfLrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 2),
    _HwXQoSIfLrVlanID_Type()
)
hwXQoSIfLrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrVlanID.setStatus("current")
_HwXQoSIfLrPassedPackets_Type = Counter64
_HwXQoSIfLrPassedPackets_Object = MibTableColumn
hwXQoSIfLrPassedPackets = _HwXQoSIfLrPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 3),
    _HwXQoSIfLrPassedPackets_Type()
)
hwXQoSIfLrPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrPassedPackets.setStatus("current")
_HwXQoSIfLrPassedBytes_Type = Counter64
_HwXQoSIfLrPassedBytes_Object = MibTableColumn
hwXQoSIfLrPassedBytes = _HwXQoSIfLrPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 4),
    _HwXQoSIfLrPassedBytes_Type()
)
hwXQoSIfLrPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrPassedBytes.setStatus("current")
_HwXQoSIfLrDiscardedPackets_Type = Counter64
_HwXQoSIfLrDiscardedPackets_Object = MibTableColumn
hwXQoSIfLrDiscardedPackets = _HwXQoSIfLrDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 5),
    _HwXQoSIfLrDiscardedPackets_Type()
)
hwXQoSIfLrDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrDiscardedPackets.setStatus("current")
_HwXQoSIfLrDiscardedBytes_Type = Counter64
_HwXQoSIfLrDiscardedBytes_Object = MibTableColumn
hwXQoSIfLrDiscardedBytes = _HwXQoSIfLrDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 6),
    _HwXQoSIfLrDiscardedBytes_Type()
)
hwXQoSIfLrDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrDiscardedBytes.setStatus("current")
_HwXQoSIfLrDelayedPackets_Type = Counter64
_HwXQoSIfLrDelayedPackets_Object = MibTableColumn
hwXQoSIfLrDelayedPackets = _HwXQoSIfLrDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 7),
    _HwXQoSIfLrDelayedPackets_Type()
)
hwXQoSIfLrDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrDelayedPackets.setStatus("current")
_HwXQoSIfLrDelayedBytes_Type = Counter64
_HwXQoSIfLrDelayedBytes_Object = MibTableColumn
hwXQoSIfLrDelayedBytes = _HwXQoSIfLrDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 5, 1, 8),
    _HwXQoSIfLrDelayedBytes_Type()
)
hwXQoSIfLrDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfLrDelayedBytes.setStatus("current")
_HwXQoSIfMirrorRunInfoTable_Object = MibTable
hwXQoSIfMirrorRunInfoTable = _HwXQoSIfMirrorRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    hwXQoSIfMirrorRunInfoTable.setStatus("current")
_HwXQoSIfMirrorRunInfoEntry_Object = MibTableRow
hwXQoSIfMirrorRunInfoEntry = _HwXQoSIfMirrorRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 6, 1)
)
hwXQoSIfMirrorRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMirrorIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfMirrorVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfMirrorRunInfoEntry.setStatus("current")
_HwXQoSIfMirrorIfIndex_Type = Integer32
_HwXQoSIfMirrorIfIndex_Object = MibTableColumn
hwXQoSIfMirrorIfIndex = _HwXQoSIfMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 6, 1, 1),
    _HwXQoSIfMirrorIfIndex_Type()
)
hwXQoSIfMirrorIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorIfIndex.setStatus("current")


class _HwXQoSIfMirrorVlanID_Type(Integer32):
    """Custom type hwXQoSIfMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfMirrorVlanID_Type.__name__ = "Integer32"
_HwXQoSIfMirrorVlanID_Object = MibTableColumn
hwXQoSIfMirrorVlanID = _HwXQoSIfMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 6, 1, 2),
    _HwXQoSIfMirrorVlanID_Type()
)
hwXQoSIfMirrorVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMirrorVlanID.setStatus("current")
_HwXQoSIfMirroredPackets_Type = Counter64
_HwXQoSIfMirroredPackets_Object = MibTableColumn
hwXQoSIfMirroredPackets = _HwXQoSIfMirroredPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 6, 1, 3),
    _HwXQoSIfMirroredPackets_Type()
)
hwXQoSIfMirroredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfMirroredPackets.setStatus("current")
_HwXQoSIfUrpfRunInfoTable_Object = MibTable
hwXQoSIfUrpfRunInfoTable = _HwXQoSIfUrpfRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 7)
)
if mibBuilder.loadTexts:
    hwXQoSIfUrpfRunInfoTable.setStatus("current")
_HwXQoSIfUrpfRunInfoEntry_Object = MibTableRow
hwXQoSIfUrpfRunInfoEntry = _HwXQoSIfUrpfRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 7, 1)
)
hwXQoSIfUrpfRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfUrpfIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfUrpfVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfUrpfRunInfoEntry.setStatus("current")
_HwXQoSIfUrpfIfIndex_Type = Integer32
_HwXQoSIfUrpfIfIndex_Object = MibTableColumn
hwXQoSIfUrpfIfIndex = _HwXQoSIfUrpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 7, 1, 1),
    _HwXQoSIfUrpfIfIndex_Type()
)
hwXQoSIfUrpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfIfIndex.setStatus("current")


class _HwXQoSIfUrpfVlanID_Type(Integer32):
    """Custom type hwXQoSIfUrpfVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfUrpfVlanID_Type.__name__ = "Integer32"
_HwXQoSIfUrpfVlanID_Object = MibTableColumn
hwXQoSIfUrpfVlanID = _HwXQoSIfUrpfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 7, 1, 2),
    _HwXQoSIfUrpfVlanID_Type()
)
hwXQoSIfUrpfVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfVlanID.setStatus("current")
_HwXQoSIfUrpfPassedPackets_Type = Counter64
_HwXQoSIfUrpfPassedPackets_Object = MibTableColumn
hwXQoSIfUrpfPassedPackets = _HwXQoSIfUrpfPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 7, 1, 3),
    _HwXQoSIfUrpfPassedPackets_Type()
)
hwXQoSIfUrpfPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfPassedPackets.setStatus("current")
_HwXQoSIfUrpfDroppdPackets_Type = Counter64
_HwXQoSIfUrpfDroppdPackets_Object = MibTableColumn
hwXQoSIfUrpfDroppdPackets = _HwXQoSIfUrpfDroppdPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 7, 1, 4),
    _HwXQoSIfUrpfDroppdPackets_Type()
)
hwXQoSIfUrpfDroppdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfUrpfDroppdPackets.setStatus("current")
_HwXQoSIfSampleRunInfoTable_Object = MibTable
hwXQoSIfSampleRunInfoTable = _HwXQoSIfSampleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 8)
)
if mibBuilder.loadTexts:
    hwXQoSIfSampleRunInfoTable.setStatus("current")
_HwXQoSIfSampleRunInfoEntry_Object = MibTableRow
hwXQoSIfSampleRunInfoEntry = _HwXQoSIfSampleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 8, 1)
)
hwXQoSIfSampleRunInfoEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSampleIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfSampleVlanID"),
)
if mibBuilder.loadTexts:
    hwXQoSIfSampleRunInfoEntry.setStatus("current")
_HwXQoSIfSampleIfIndex_Type = Integer32
_HwXQoSIfSampleIfIndex_Object = MibTableColumn
hwXQoSIfSampleIfIndex = _HwXQoSIfSampleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 8, 1, 1),
    _HwXQoSIfSampleIfIndex_Type()
)
hwXQoSIfSampleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfSampleIfIndex.setStatus("current")


class _HwXQoSIfSampleVlanID_Type(Integer32):
    """Custom type hwXQoSIfSampleVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )


_HwXQoSIfSampleVlanID_Type.__name__ = "Integer32"
_HwXQoSIfSampleVlanID_Object = MibTableColumn
hwXQoSIfSampleVlanID = _HwXQoSIfSampleVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 8, 1, 2),
    _HwXQoSIfSampleVlanID_Type()
)
hwXQoSIfSampleVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfSampleVlanID.setStatus("current")
_HwXQoSIfSampledPackets_Type = Counter64
_HwXQoSIfSampledPackets_Object = MibTableColumn
hwXQoSIfSampledPackets = _HwXQoSIfSampledPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 8, 1, 3),
    _HwXQoSIfSampledPackets_Type()
)
hwXQoSIfSampledPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfSampledPackets.setStatus("current")
_HwXQoSIfCarStatisticsTable_Object = MibTable
hwXQoSIfCarStatisticsTable = _HwXQoSIfCarStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9)
)
if mibBuilder.loadTexts:
    hwXQoSIfCarStatisticsTable.setStatus("current")
_HwXQoSIfCarStatisticsEntry_Object = MibTableRow
hwXQoSIfCarStatisticsEntry = _HwXQoSIfCarStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1)
)
hwXQoSIfCarStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarCfgIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarVlanID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfCarDirection"),
)
if mibBuilder.loadTexts:
    hwXQoSIfCarStatisticsEntry.setStatus("current")
_HwXQoSIfCarConformedPackets_Type = Counter64
_HwXQoSIfCarConformedPackets_Object = MibTableColumn
hwXQoSIfCarConformedPackets = _HwXQoSIfCarConformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 11),
    _HwXQoSIfCarConformedPackets_Type()
)
hwXQoSIfCarConformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarConformedPackets.setStatus("current")
_HwXQoSIfCarConformedBytes_Type = Counter64
_HwXQoSIfCarConformedBytes_Object = MibTableColumn
hwXQoSIfCarConformedBytes = _HwXQoSIfCarConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 12),
    _HwXQoSIfCarConformedBytes_Type()
)
hwXQoSIfCarConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarConformedBytes.setStatus("current")
_HwXQoSIfCarConformedPacketRate_Type = Counter64
_HwXQoSIfCarConformedPacketRate_Object = MibTableColumn
hwXQoSIfCarConformedPacketRate = _HwXQoSIfCarConformedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 13),
    _HwXQoSIfCarConformedPacketRate_Type()
)
hwXQoSIfCarConformedPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarConformedPacketRate.setStatus("current")
_HwXQoSIfCarConformedByteRate_Type = Counter64
_HwXQoSIfCarConformedByteRate_Object = MibTableColumn
hwXQoSIfCarConformedByteRate = _HwXQoSIfCarConformedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 14),
    _HwXQoSIfCarConformedByteRate_Type()
)
hwXQoSIfCarConformedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarConformedByteRate.setStatus("current")
_HwXQoSIfCarExceededPackets_Type = Counter64
_HwXQoSIfCarExceededPackets_Object = MibTableColumn
hwXQoSIfCarExceededPackets = _HwXQoSIfCarExceededPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 15),
    _HwXQoSIfCarExceededPackets_Type()
)
hwXQoSIfCarExceededPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarExceededPackets.setStatus("current")
_HwXQoSIfCarExceededBytes_Type = Counter64
_HwXQoSIfCarExceededBytes_Object = MibTableColumn
hwXQoSIfCarExceededBytes = _HwXQoSIfCarExceededBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 16),
    _HwXQoSIfCarExceededBytes_Type()
)
hwXQoSIfCarExceededBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarExceededBytes.setStatus("current")
_HwXQoSIfCarExceededPacketRate_Type = Counter64
_HwXQoSIfCarExceededPacketRate_Object = MibTableColumn
hwXQoSIfCarExceededPacketRate = _HwXQoSIfCarExceededPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 17),
    _HwXQoSIfCarExceededPacketRate_Type()
)
hwXQoSIfCarExceededPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarExceededPacketRate.setStatus("current")
_HwXQoSIfCarExceededByteRate_Type = Counter64
_HwXQoSIfCarExceededByteRate_Object = MibTableColumn
hwXQoSIfCarExceededByteRate = _HwXQoSIfCarExceededByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 18),
    _HwXQoSIfCarExceededByteRate_Type()
)
hwXQoSIfCarExceededByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarExceededByteRate.setStatus("current")
_HwXQoSIfCarOverflowPackets_Type = Counter64
_HwXQoSIfCarOverflowPackets_Object = MibTableColumn
hwXQoSIfCarOverflowPackets = _HwXQoSIfCarOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 19),
    _HwXQoSIfCarOverflowPackets_Type()
)
hwXQoSIfCarOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarOverflowPackets.setStatus("current")
_HwXQoSIfCarOverflowBytes_Type = Counter64
_HwXQoSIfCarOverflowBytes_Object = MibTableColumn
hwXQoSIfCarOverflowBytes = _HwXQoSIfCarOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 20),
    _HwXQoSIfCarOverflowBytes_Type()
)
hwXQoSIfCarOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarOverflowBytes.setStatus("current")
_HwXQoSIfCarOverflowPacketRate_Type = Counter64
_HwXQoSIfCarOverflowPacketRate_Object = MibTableColumn
hwXQoSIfCarOverflowPacketRate = _HwXQoSIfCarOverflowPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 21),
    _HwXQoSIfCarOverflowPacketRate_Type()
)
hwXQoSIfCarOverflowPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarOverflowPacketRate.setStatus("current")
_HwXQoSIfCarOverflowByteRate_Type = Counter64
_HwXQoSIfCarOverflowByteRate_Object = MibTableColumn
hwXQoSIfCarOverflowByteRate = _HwXQoSIfCarOverflowByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 22),
    _HwXQoSIfCarOverflowByteRate_Type()
)
hwXQoSIfCarOverflowByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarOverflowByteRate.setStatus("current")
_HwXQoSIfCarPassedPackets_Type = Counter64
_HwXQoSIfCarPassedPackets_Object = MibTableColumn
hwXQoSIfCarPassedPackets = _HwXQoSIfCarPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 23),
    _HwXQoSIfCarPassedPackets_Type()
)
hwXQoSIfCarPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarPassedPackets.setStatus("current")
_HwXQoSIfCarPassedBytes_Type = Counter64
_HwXQoSIfCarPassedBytes_Object = MibTableColumn
hwXQoSIfCarPassedBytes = _HwXQoSIfCarPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 24),
    _HwXQoSIfCarPassedBytes_Type()
)
hwXQoSIfCarPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarPassedBytes.setStatus("current")
_HwXQoSIfCarDiscardedPackets_Type = Counter64
_HwXQoSIfCarDiscardedPackets_Object = MibTableColumn
hwXQoSIfCarDiscardedPackets = _HwXQoSIfCarDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 25),
    _HwXQoSIfCarDiscardedPackets_Type()
)
hwXQoSIfCarDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarDiscardedPackets.setStatus("current")
_HwXQoSIfCarDiscardedBytes_Type = Counter64
_HwXQoSIfCarDiscardedBytes_Object = MibTableColumn
hwXQoSIfCarDiscardedBytes = _HwXQoSIfCarDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 9, 1, 26),
    _HwXQoSIfCarDiscardedBytes_Type()
)
hwXQoSIfCarDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfCarDiscardedBytes.setStatus("current")
_HwXQoSIfOutboundQueueStatisticTable_Object = MibTable
hwXQoSIfOutboundQueueStatisticTable = _HwXQoSIfOutboundQueueStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 10)
)
if mibBuilder.loadTexts:
    hwXQoSIfOutboundQueueStatisticTable.setStatus("current")
_HwXQoSIfOutboundQueueStatisticEntry_Object = MibTableRow
hwXQoSIfOutboundQueueStatisticEntry = _HwXQoSIfOutboundQueueStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 10, 1)
)
hwXQoSIfOutboundQueueStatisticEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfExtIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIfQueIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSIfOutboundQueueStatisticEntry.setStatus("current")
_HwXQoSIfExtIndex_Type = Unsigned32
_HwXQoSIfExtIndex_Object = MibTableColumn
hwXQoSIfExtIndex = _HwXQoSIfExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 10, 1, 1),
    _HwXQoSIfExtIndex_Type()
)
hwXQoSIfExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfExtIndex.setStatus("current")
_HwXQoSIfQueIndex_Type = OctetString
_HwXQoSIfQueIndex_Object = MibTableColumn
hwXQoSIfQueIndex = _HwXQoSIfQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 10, 1, 2),
    _HwXQoSIfQueIndex_Type()
)
hwXQoSIfQueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSIfQueIndex.setStatus("current")
_HwXQoSIfQueDiscardPackets_Type = Integer32
_HwXQoSIfQueDiscardPackets_Object = MibTableColumn
hwXQoSIfQueDiscardPackets = _HwXQoSIfQueDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 3, 10, 1, 3),
    _HwXQoSIfQueDiscardPackets_Type()
)
hwXQoSIfQueDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIfQueDiscardPackets.setStatus("current")
_HwXQoSVlanStatisticsObjects_ObjectIdentity = ObjectIdentity
hwXQoSVlanStatisticsObjects = _HwXQoSVlanStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4)
)
_HwXQosVlanStatTable_Object = MibTable
hwXQosVlanStatTable = _HwXQosVlanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hwXQosVlanStatTable.setStatus("current")
_HwXQosVlanStatEntry_Object = MibTableRow
hwXQosVlanStatEntry = _HwXQosVlanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1)
)
hwXQosVlanStatEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQosVlanStatVlanId"),
)
if mibBuilder.loadTexts:
    hwXQosVlanStatEntry.setStatus("current")


class _HwXQosVlanStatVlanId_Type(Integer32):
    """Custom type hwXQosVlanStatVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwXQosVlanStatVlanId_Type.__name__ = "Integer32"
_HwXQosVlanStatVlanId_Object = MibTableColumn
hwXQosVlanStatVlanId = _HwXQosVlanStatVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 1),
    _HwXQosVlanStatVlanId_Type()
)
hwXQosVlanStatVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQosVlanStatVlanId.setStatus("current")
_HwXQosVlanStatInTotalPkts_Type = Counter64
_HwXQosVlanStatInTotalPkts_Object = MibTableColumn
hwXQosVlanStatInTotalPkts = _HwXQosVlanStatInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 2),
    _HwXQosVlanStatInTotalPkts_Type()
)
hwXQosVlanStatInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInTotalPkts.setStatus("current")
_HwXQosVlanStatInTotalBytes_Type = Counter64
_HwXQosVlanStatInTotalBytes_Object = MibTableColumn
hwXQosVlanStatInTotalBytes = _HwXQosVlanStatInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 3),
    _HwXQosVlanStatInTotalBytes_Type()
)
hwXQosVlanStatInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInTotalBytes.setStatus("current")
_HwXQosVlanStatOutTotalPkts_Type = Counter64
_HwXQosVlanStatOutTotalPkts_Object = MibTableColumn
hwXQosVlanStatOutTotalPkts = _HwXQosVlanStatOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 4),
    _HwXQosVlanStatOutTotalPkts_Type()
)
hwXQosVlanStatOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutTotalPkts.setStatus("current")
_HwXQosVlanStatOutTotalBytes_Type = Counter64
_HwXQosVlanStatOutTotalBytes_Object = MibTableColumn
hwXQosVlanStatOutTotalBytes = _HwXQosVlanStatOutTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 5),
    _HwXQosVlanStatOutTotalBytes_Type()
)
hwXQosVlanStatOutTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutTotalBytes.setStatus("current")
_HwXQosVlanStatInUcastPkts_Type = Counter64
_HwXQosVlanStatInUcastPkts_Object = MibTableColumn
hwXQosVlanStatInUcastPkts = _HwXQosVlanStatInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 6),
    _HwXQosVlanStatInUcastPkts_Type()
)
hwXQosVlanStatInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInUcastPkts.setStatus("current")
_HwXQosVlanStatInUcastBytes_Type = Counter64
_HwXQosVlanStatInUcastBytes_Object = MibTableColumn
hwXQosVlanStatInUcastBytes = _HwXQosVlanStatInUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 7),
    _HwXQosVlanStatInUcastBytes_Type()
)
hwXQosVlanStatInUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInUcastBytes.setStatus("current")
_HwXQosVlanStatOutUcastPkts_Type = Counter64
_HwXQosVlanStatOutUcastPkts_Object = MibTableColumn
hwXQosVlanStatOutUcastPkts = _HwXQosVlanStatOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 8),
    _HwXQosVlanStatOutUcastPkts_Type()
)
hwXQosVlanStatOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutUcastPkts.setStatus("current")
_HwXQosVlanStatOutUcastBytes_Type = Counter64
_HwXQosVlanStatOutUcastBytes_Object = MibTableColumn
hwXQosVlanStatOutUcastBytes = _HwXQosVlanStatOutUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 9),
    _HwXQosVlanStatOutUcastBytes_Type()
)
hwXQosVlanStatOutUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutUcastBytes.setStatus("current")
_HwXQosVlanStatInMcastPkts_Type = Counter64
_HwXQosVlanStatInMcastPkts_Object = MibTableColumn
hwXQosVlanStatInMcastPkts = _HwXQosVlanStatInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 10),
    _HwXQosVlanStatInMcastPkts_Type()
)
hwXQosVlanStatInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInMcastPkts.setStatus("current")
_HwXQosVlanStatInMcastBytes_Type = Counter64
_HwXQosVlanStatInMcastBytes_Object = MibTableColumn
hwXQosVlanStatInMcastBytes = _HwXQosVlanStatInMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 11),
    _HwXQosVlanStatInMcastBytes_Type()
)
hwXQosVlanStatInMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInMcastBytes.setStatus("current")
_HwXQosVlanStatOutMcastPkts_Type = Counter64
_HwXQosVlanStatOutMcastPkts_Object = MibTableColumn
hwXQosVlanStatOutMcastPkts = _HwXQosVlanStatOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 12),
    _HwXQosVlanStatOutMcastPkts_Type()
)
hwXQosVlanStatOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutMcastPkts.setStatus("current")
_HwXQosVlanStatOutMcastBytes_Type = Counter64
_HwXQosVlanStatOutMcastBytes_Object = MibTableColumn
hwXQosVlanStatOutMcastBytes = _HwXQosVlanStatOutMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 13),
    _HwXQosVlanStatOutMcastBytes_Type()
)
hwXQosVlanStatOutMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutMcastBytes.setStatus("current")
_HwXQosVlanStatInBcastPkts_Type = Counter64
_HwXQosVlanStatInBcastPkts_Object = MibTableColumn
hwXQosVlanStatInBcastPkts = _HwXQosVlanStatInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 14),
    _HwXQosVlanStatInBcastPkts_Type()
)
hwXQosVlanStatInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInBcastPkts.setStatus("current")
_HwXQosVlanStatInBcastBytes_Type = Counter64
_HwXQosVlanStatInBcastBytes_Object = MibTableColumn
hwXQosVlanStatInBcastBytes = _HwXQosVlanStatInBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 15),
    _HwXQosVlanStatInBcastBytes_Type()
)
hwXQosVlanStatInBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInBcastBytes.setStatus("current")
_HwXQosVlanStatOutBcastPkts_Type = Counter64
_HwXQosVlanStatOutBcastPkts_Object = MibTableColumn
hwXQosVlanStatOutBcastPkts = _HwXQosVlanStatOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 16),
    _HwXQosVlanStatOutBcastPkts_Type()
)
hwXQosVlanStatOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutBcastPkts.setStatus("current")
_HwXQosVlanStatOutBcastBytes_Type = Counter64
_HwXQosVlanStatOutBcastBytes_Object = MibTableColumn
hwXQosVlanStatOutBcastBytes = _HwXQosVlanStatOutBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 17),
    _HwXQosVlanStatOutBcastBytes_Type()
)
hwXQosVlanStatOutBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatOutBcastBytes.setStatus("current")
_HwXQosVlanStatInUnknownUcastPkts_Type = Counter64
_HwXQosVlanStatInUnknownUcastPkts_Object = MibTableColumn
hwXQosVlanStatInUnknownUcastPkts = _HwXQosVlanStatInUnknownUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 18),
    _HwXQosVlanStatInUnknownUcastPkts_Type()
)
hwXQosVlanStatInUnknownUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInUnknownUcastPkts.setStatus("current")
_HwXQosVlanStatInUnknownUcastBytes_Type = Counter64
_HwXQosVlanStatInUnknownUcastBytes_Object = MibTableColumn
hwXQosVlanStatInUnknownUcastBytes = _HwXQosVlanStatInUnknownUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 19),
    _HwXQosVlanStatInUnknownUcastBytes_Type()
)
hwXQosVlanStatInUnknownUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosVlanStatInUnknownUcastBytes.setStatus("current")
_HwXQosVlanStatResetFlag_Type = EnabledStatus
_HwXQosVlanStatResetFlag_Object = MibTableColumn
hwXQosVlanStatResetFlag = _HwXQosVlanStatResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 4, 4, 1, 1, 20),
    _HwXQosVlanStatResetFlag_Type()
)
hwXQosVlanStatResetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQosVlanStatResetFlag.setStatus("current")
_HwXQoSGlobalObjects_ObjectIdentity = ObjectIdentity
hwXQoSGlobalObjects = _HwXQoSGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5)
)
_HwXQoSSoftCarCfgTable_Object = MibTable
hwXQoSSoftCarCfgTable = _HwXQoSSoftCarCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwXQoSSoftCarCfgTable.setStatus("current")
_HwXQoSSoftCarCfgEntry_Object = MibTableRow
hwXQoSSoftCarCfgEntry = _HwXQoSSoftCarCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1, 1)
)
hwXQoSSoftCarCfgEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSSoftCarIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSSoftCarCfgEntry.setStatus("current")


class _HwXQoSSoftCarIndex_Type(Integer32):
    """Custom type hwXQoSSoftCarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwXQoSSoftCarIndex_Type.__name__ = "Integer32"
_HwXQoSSoftCarIndex_Object = MibTableColumn
hwXQoSSoftCarIndex = _HwXQoSSoftCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1, 1, 1),
    _HwXQoSSoftCarIndex_Type()
)
hwXQoSSoftCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSSoftCarIndex.setStatus("current")


class _HwXQoSSoftCarName_Type(OctetString):
    """Custom type hwXQoSSoftCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSSoftCarName_Type.__name__ = "OctetString"
_HwXQoSSoftCarName_Object = MibTableColumn
hwXQoSSoftCarName = _HwXQoSSoftCarName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1, 1, 2),
    _HwXQoSSoftCarName_Type()
)
hwXQoSSoftCarName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSSoftCarName.setStatus("current")
_HwXQoSSoftCarCir_Type = Integer32
_HwXQoSSoftCarCir_Object = MibTableColumn
hwXQoSSoftCarCir = _HwXQoSSoftCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1, 1, 3),
    _HwXQoSSoftCarCir_Type()
)
hwXQoSSoftCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSSoftCarCir.setStatus("current")
_HwXQoSSoftCarCbs_Type = Integer32
_HwXQoSSoftCarCbs_Object = MibTableColumn
hwXQoSSoftCarCbs = _HwXQoSSoftCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1, 1, 4),
    _HwXQoSSoftCarCbs_Type()
)
hwXQoSSoftCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSSoftCarCbs.setStatus("current")
_HwXQoSSoftCarRowStatus_Type = RowStatus
_HwXQoSSoftCarRowStatus_Object = MibTableColumn
hwXQoSSoftCarRowStatus = _HwXQoSSoftCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 1, 1, 5),
    _HwXQoSSoftCarRowStatus_Type()
)
hwXQoSSoftCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSSoftCarRowStatus.setStatus("current")
_HwXQoSGlobalWredClassCfgTable_Object = MibTable
hwXQoSGlobalWredClassCfgTable = _HwXQoSGlobalWredClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassCfgTable.setStatus("current")
_HwXQoSGlobalWredClassCfgEntry_Object = MibTableRow
hwXQoSGlobalWredClassCfgEntry = _HwXQoSGlobalWredClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2, 1)
)
hwXQoSGlobalWredClassCfgEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSGlobalWredClassIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassCfgEntry.setStatus("current")


class _HwXQoSGlobalWredClassIndex_Type(Integer32):
    """Custom type hwXQoSGlobalWredClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwXQoSGlobalWredClassIndex_Type.__name__ = "Integer32"
_HwXQoSGlobalWredClassIndex_Object = MibTableColumn
hwXQoSGlobalWredClassIndex = _HwXQoSGlobalWredClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2, 1, 1),
    _HwXQoSGlobalWredClassIndex_Type()
)
hwXQoSGlobalWredClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassIndex.setStatus("current")
_HwXQoSGlobalWredClassLowlimit_Type = Integer32
_HwXQoSGlobalWredClassLowlimit_Object = MibTableColumn
hwXQoSGlobalWredClassLowlimit = _HwXQoSGlobalWredClassLowlimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2, 1, 2),
    _HwXQoSGlobalWredClassLowlimit_Type()
)
hwXQoSGlobalWredClassLowlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassLowlimit.setStatus("current")
_HwXQoSGlobalWredClassHighlimit_Type = Integer32
_HwXQoSGlobalWredClassHighlimit_Object = MibTableColumn
hwXQoSGlobalWredClassHighlimit = _HwXQoSGlobalWredClassHighlimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2, 1, 3),
    _HwXQoSGlobalWredClassHighlimit_Type()
)
hwXQoSGlobalWredClassHighlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassHighlimit.setStatus("current")
_HwXQoSGlobalWredClassDiscardProbability_Type = Integer32
_HwXQoSGlobalWredClassDiscardProbability_Object = MibTableColumn
hwXQoSGlobalWredClassDiscardProbability = _HwXQoSGlobalWredClassDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2, 1, 4),
    _HwXQoSGlobalWredClassDiscardProbability_Type()
)
hwXQoSGlobalWredClassDiscardProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassDiscardProbability.setStatus("current")


class _HwXQoSGlobalWredClassSetDefault_Type(Integer32):
    """Custom type hwXQoSGlobalWredClassSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwXQoSGlobalWredClassSetDefault_Type.__name__ = "Integer32"
_HwXQoSGlobalWredClassSetDefault_Object = MibTableColumn
hwXQoSGlobalWredClassSetDefault = _HwXQoSGlobalWredClassSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 2, 1, 5),
    _HwXQoSGlobalWredClassSetDefault_Type()
)
hwXQoSGlobalWredClassSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredClassSetDefault.setStatus("current")
_HwXQoSGlobalWredTypeCfgTable_Object = MibTable
hwXQoSGlobalWredTypeCfgTable = _HwXQoSGlobalWredTypeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeCfgTable.setStatus("current")
_HwXQoSGlobalWredTypeCfgEntry_Object = MibTableRow
hwXQoSGlobalWredTypeCfgEntry = _HwXQoSGlobalWredTypeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1)
)
hwXQoSGlobalWredTypeCfgEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSGlobalWredTypeIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeCfgEntry.setStatus("current")


class _HwXQoSGlobalWredTypeIndex_Type(Integer32):
    """Custom type hwXQoSGlobalWredTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwXQoSGlobalWredTypeIndex_Type.__name__ = "Integer32"
_HwXQoSGlobalWredTypeIndex_Object = MibTableColumn
hwXQoSGlobalWredTypeIndex = _HwXQoSGlobalWredTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1, 1),
    _HwXQoSGlobalWredTypeIndex_Type()
)
hwXQoSGlobalWredTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeIndex.setStatus("current")


class _HwXQoSGlobalWredTypeName_Type(OctetString):
    """Custom type hwXQoSGlobalWredTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSGlobalWredTypeName_Type.__name__ = "OctetString"
_HwXQoSGlobalWredTypeName_Object = MibTableColumn
hwXQoSGlobalWredTypeName = _HwXQoSGlobalWredTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1, 2),
    _HwXQoSGlobalWredTypeName_Type()
)
hwXQoSGlobalWredTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeName.setStatus("current")
_HwXQoSGlobalWredTypeLowlimit_Type = Integer32
_HwXQoSGlobalWredTypeLowlimit_Object = MibTableColumn
hwXQoSGlobalWredTypeLowlimit = _HwXQoSGlobalWredTypeLowlimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1, 3),
    _HwXQoSGlobalWredTypeLowlimit_Type()
)
hwXQoSGlobalWredTypeLowlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeLowlimit.setStatus("current")
_HwXQoSGlobalWredTypeHighlimit_Type = Integer32
_HwXQoSGlobalWredTypeHighlimit_Object = MibTableColumn
hwXQoSGlobalWredTypeHighlimit = _HwXQoSGlobalWredTypeHighlimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1, 4),
    _HwXQoSGlobalWredTypeHighlimit_Type()
)
hwXQoSGlobalWredTypeHighlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeHighlimit.setStatus("current")
_HwXQoSGlobalWredTypeDiscardProbability_Type = Integer32
_HwXQoSGlobalWredTypeDiscardProbability_Object = MibTableColumn
hwXQoSGlobalWredTypeDiscardProbability = _HwXQoSGlobalWredTypeDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1, 5),
    _HwXQoSGlobalWredTypeDiscardProbability_Type()
)
hwXQoSGlobalWredTypeDiscardProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeDiscardProbability.setStatus("current")


class _HwXQoSGlobalWredTypeSetDefault_Type(Integer32):
    """Custom type hwXQoSGlobalWredTypeSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwXQoSGlobalWredTypeSetDefault_Type.__name__ = "Integer32"
_HwXQoSGlobalWredTypeSetDefault_Object = MibTableColumn
hwXQoSGlobalWredTypeSetDefault = _HwXQoSGlobalWredTypeSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 3, 1, 6),
    _HwXQoSGlobalWredTypeSetDefault_Type()
)
hwXQoSGlobalWredTypeSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSGlobalWredTypeSetDefault.setStatus("current")
_HwXQoSVlanBcastSuppressTable_Object = MibTable
hwXQoSVlanBcastSuppressTable = _HwXQoSVlanBcastSuppressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 4)
)
if mibBuilder.loadTexts:
    hwXQoSVlanBcastSuppressTable.setStatus("current")
_HwXQoSVlanBcastSuppressEntry_Object = MibTableRow
hwXQoSVlanBcastSuppressEntry = _HwXQoSVlanBcastSuppressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 4, 1)
)
hwXQoSVlanBcastSuppressEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSVlanBcastSuppressVlanId"),
)
if mibBuilder.loadTexts:
    hwXQoSVlanBcastSuppressEntry.setStatus("current")


class _HwXQoSVlanBcastSuppressVlanId_Type(Integer32):
    """Custom type hwXQoSVlanBcastSuppressVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwXQoSVlanBcastSuppressVlanId_Type.__name__ = "Integer32"
_HwXQoSVlanBcastSuppressVlanId_Object = MibTableColumn
hwXQoSVlanBcastSuppressVlanId = _HwXQoSVlanBcastSuppressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 4, 1, 1),
    _HwXQoSVlanBcastSuppressVlanId_Type()
)
hwXQoSVlanBcastSuppressVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSVlanBcastSuppressVlanId.setStatus("current")


class _HwXQoSVlanBcastSuppressValue_Type(Integer32):
    """Custom type hwXQoSVlanBcastSuppressValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1000000),
    )


_HwXQoSVlanBcastSuppressValue_Type.__name__ = "Integer32"
_HwXQoSVlanBcastSuppressValue_Object = MibTableColumn
hwXQoSVlanBcastSuppressValue = _HwXQoSVlanBcastSuppressValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 4, 1, 2),
    _HwXQoSVlanBcastSuppressValue_Type()
)
hwXQoSVlanBcastSuppressValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSVlanBcastSuppressValue.setStatus("current")
_HwXQoSVlanBcastSuppressRowStatus_Type = RowStatus
_HwXQoSVlanBcastSuppressRowStatus_Object = MibTableColumn
hwXQoSVlanBcastSuppressRowStatus = _HwXQoSVlanBcastSuppressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 4, 1, 3),
    _HwXQoSVlanBcastSuppressRowStatus_Type()
)
hwXQoSVlanBcastSuppressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSVlanBcastSuppressRowStatus.setStatus("current")
_HwXQoSScheduleProfileTable_Object = MibTable
hwXQoSScheduleProfileTable = _HwXQoSScheduleProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5)
)
if mibBuilder.loadTexts:
    hwXQoSScheduleProfileTable.setStatus("current")
_HwXQoSScheduleProfileEntry_Object = MibTableRow
hwXQoSScheduleProfileEntry = _HwXQoSScheduleProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1)
)
hwXQoSScheduleProfileEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSScheduleProfileName"),
)
if mibBuilder.loadTexts:
    hwXQoSScheduleProfileEntry.setStatus("current")


class _HwXQoSScheduleProfileName_Type(OctetString):
    """Custom type hwXQoSScheduleProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSScheduleProfileName_Type.__name__ = "OctetString"
_HwXQoSScheduleProfileName_Object = MibTableColumn
hwXQoSScheduleProfileName = _HwXQoSScheduleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 1),
    _HwXQoSScheduleProfileName_Type()
)
hwXQoSScheduleProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSScheduleProfileName.setStatus("current")


class _HwXQoSScheduleQueueMode_Type(Integer32):
    """Custom type hwXQoSScheduleQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("drr", 6),
          ("pq", 1),
          ("wfq", 4),
          ("wrr", 3))
    )


_HwXQoSScheduleQueueMode_Type.__name__ = "Integer32"
_HwXQoSScheduleQueueMode_Object = MibTableColumn
hwXQoSScheduleQueueMode = _HwXQoSScheduleQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 2),
    _HwXQoSScheduleQueueMode_Type()
)
hwXQoSScheduleQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueMode.setStatus("current")
_HwXQoSScheduleQueueBeWeight_Type = Integer32
_HwXQoSScheduleQueueBeWeight_Object = MibTableColumn
hwXQoSScheduleQueueBeWeight = _HwXQoSScheduleQueueBeWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 3),
    _HwXQoSScheduleQueueBeWeight_Type()
)
hwXQoSScheduleQueueBeWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueBeWeight.setStatus("current")
_HwXQoSScheduleQueueAf1Weight_Type = Integer32
_HwXQoSScheduleQueueAf1Weight_Object = MibTableColumn
hwXQoSScheduleQueueAf1Weight = _HwXQoSScheduleQueueAf1Weight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 4),
    _HwXQoSScheduleQueueAf1Weight_Type()
)
hwXQoSScheduleQueueAf1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueAf1Weight.setStatus("current")
_HwXQoSScheduleQueueAf2Weight_Type = Integer32
_HwXQoSScheduleQueueAf2Weight_Object = MibTableColumn
hwXQoSScheduleQueueAf2Weight = _HwXQoSScheduleQueueAf2Weight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 5),
    _HwXQoSScheduleQueueAf2Weight_Type()
)
hwXQoSScheduleQueueAf2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueAf2Weight.setStatus("current")
_HwXQoSScheduleQueueAf3Weight_Type = Integer32
_HwXQoSScheduleQueueAf3Weight_Object = MibTableColumn
hwXQoSScheduleQueueAf3Weight = _HwXQoSScheduleQueueAf3Weight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 6),
    _HwXQoSScheduleQueueAf3Weight_Type()
)
hwXQoSScheduleQueueAf3Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueAf3Weight.setStatus("current")
_HwXQoSScheduleQueueAf4Weight_Type = Integer32
_HwXQoSScheduleQueueAf4Weight_Object = MibTableColumn
hwXQoSScheduleQueueAf4Weight = _HwXQoSScheduleQueueAf4Weight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 7),
    _HwXQoSScheduleQueueAf4Weight_Type()
)
hwXQoSScheduleQueueAf4Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueAf4Weight.setStatus("current")
_HwXQoSScheduleQueueCs6Weight_Type = Integer32
_HwXQoSScheduleQueueCs6Weight_Object = MibTableColumn
hwXQoSScheduleQueueCs6Weight = _HwXQoSScheduleQueueCs6Weight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 8),
    _HwXQoSScheduleQueueCs6Weight_Type()
)
hwXQoSScheduleQueueCs6Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueCs6Weight.setStatus("current")
_HwXQoSScheduleQueueCs7Weight_Type = Integer32
_HwXQoSScheduleQueueCs7Weight_Object = MibTableColumn
hwXQoSScheduleQueueCs7Weight = _HwXQoSScheduleQueueCs7Weight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 9),
    _HwXQoSScheduleQueueCs7Weight_Type()
)
hwXQoSScheduleQueueCs7Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueCs7Weight.setStatus("current")
_HwXQoSScheduleQueueEfWeight_Type = Integer32
_HwXQoSScheduleQueueEfWeight_Object = MibTableColumn
hwXQoSScheduleQueueEfWeight = _HwXQoSScheduleQueueEfWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 10),
    _HwXQoSScheduleQueueEfWeight_Type()
)
hwXQoSScheduleQueueEfWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSScheduleQueueEfWeight.setStatus("current")
_HwXQoSScheduleProfileRowStatus_Type = RowStatus
_HwXQoSScheduleProfileRowStatus_Object = MibTableColumn
hwXQoSScheduleProfileRowStatus = _HwXQoSScheduleProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 5, 5, 1, 51),
    _HwXQoSScheduleProfileRowStatus_Type()
)
hwXQoSScheduleProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSScheduleProfileRowStatus.setStatus("current")
_HwXQoSCpDefendObjects_ObjectIdentity = ObjectIdentity
hwXQoSCpDefendObjects = _HwXQoSCpDefendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6)
)
_HwXQoSCpDefendStatisticsTable_Object = MibTable
hwXQoSCpDefendStatisticsTable = _HwXQoSCpDefendStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwXQoSCpDefendStatisticsTable.setStatus("current")
_HwXQoSCpDefendStatisticsEntry_Object = MibTableRow
hwXQoSCpDefendStatisticsEntry = _HwXQoSCpDefendStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1)
)
hwXQoSCpDefendStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpDefendChassisID"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpDefendSlotId"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCpDefendObjectIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSCpDefendStatisticsEntry.setStatus("current")


class _HwXQoSCpDefendSlotId_Type(Integer32):
    """Custom type hwXQoSCpDefendSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwXQoSCpDefendSlotId_Type.__name__ = "Integer32"
_HwXQoSCpDefendSlotId_Object = MibTableColumn
hwXQoSCpDefendSlotId = _HwXQoSCpDefendSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 1),
    _HwXQoSCpDefendSlotId_Type()
)
hwXQoSCpDefendSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpDefendSlotId.setStatus("current")


class _HwXQoSCpDefendObjectIndex_Type(Integer32):
    """Custom type hwXQoSCpDefendObjectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_HwXQoSCpDefendObjectIndex_Type.__name__ = "Integer32"
_HwXQoSCpDefendObjectIndex_Object = MibTableColumn
hwXQoSCpDefendObjectIndex = _HwXQoSCpDefendObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 2),
    _HwXQoSCpDefendObjectIndex_Type()
)
hwXQoSCpDefendObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpDefendObjectIndex.setStatus("current")
_HwXQoSCpDefendPassedPackets_Type = Counter64
_HwXQoSCpDefendPassedPackets_Object = MibTableColumn
hwXQoSCpDefendPassedPackets = _HwXQoSCpDefendPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 11),
    _HwXQoSCpDefendPassedPackets_Type()
)
hwXQoSCpDefendPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendPassedPackets.setStatus("current")
_HwXQoSCpDefendPassedBytes_Type = Counter64
_HwXQoSCpDefendPassedBytes_Object = MibTableColumn
hwXQoSCpDefendPassedBytes = _HwXQoSCpDefendPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 12),
    _HwXQoSCpDefendPassedBytes_Type()
)
hwXQoSCpDefendPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendPassedBytes.setStatus("current")
_HwXQoSCpDefendPassedPacketRate_Type = Counter64
_HwXQoSCpDefendPassedPacketRate_Object = MibTableColumn
hwXQoSCpDefendPassedPacketRate = _HwXQoSCpDefendPassedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 13),
    _HwXQoSCpDefendPassedPacketRate_Type()
)
hwXQoSCpDefendPassedPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendPassedPacketRate.setStatus("current")
_HwXQoSCpDefendPassedByteRate_Type = Counter64
_HwXQoSCpDefendPassedByteRate_Object = MibTableColumn
hwXQoSCpDefendPassedByteRate = _HwXQoSCpDefendPassedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 14),
    _HwXQoSCpDefendPassedByteRate_Type()
)
hwXQoSCpDefendPassedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendPassedByteRate.setStatus("current")
_HwXQoSCpDefendDiscardedPackets_Type = Counter64
_HwXQoSCpDefendDiscardedPackets_Object = MibTableColumn
hwXQoSCpDefendDiscardedPackets = _HwXQoSCpDefendDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 15),
    _HwXQoSCpDefendDiscardedPackets_Type()
)
hwXQoSCpDefendDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedPackets.setStatus("current")
_HwXQoSCpDefendDiscardedBytes_Type = Counter64
_HwXQoSCpDefendDiscardedBytes_Object = MibTableColumn
hwXQoSCpDefendDiscardedBytes = _HwXQoSCpDefendDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 16),
    _HwXQoSCpDefendDiscardedBytes_Type()
)
hwXQoSCpDefendDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedBytes.setStatus("current")
_HwXQoSCpDefendDiscardedPacketRate_Type = Counter64
_HwXQoSCpDefendDiscardedPacketRate_Object = MibTableColumn
hwXQoSCpDefendDiscardedPacketRate = _HwXQoSCpDefendDiscardedPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 17),
    _HwXQoSCpDefendDiscardedPacketRate_Type()
)
hwXQoSCpDefendDiscardedPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedPacketRate.setStatus("current")
_HwXQoSCpDefendDiscardedByteRate_Type = Counter64
_HwXQoSCpDefendDiscardedByteRate_Object = MibTableColumn
hwXQoSCpDefendDiscardedByteRate = _HwXQoSCpDefendDiscardedByteRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 18),
    _HwXQoSCpDefendDiscardedByteRate_Type()
)
hwXQoSCpDefendDiscardedByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedByteRate.setStatus("current")
_HwXQoSCpDefendDiscardedThreshold_Type = Counter32
_HwXQoSCpDefendDiscardedThreshold_Object = MibTableColumn
hwXQoSCpDefendDiscardedThreshold = _HwXQoSCpDefendDiscardedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 19),
    _HwXQoSCpDefendDiscardedThreshold_Type()
)
hwXQoSCpDefendDiscardedThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedThreshold.setStatus("current")


class _HwXQoSCpDefendChassisID_Type(Integer32):
    """Custom type hwXQoSCpDefendChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwXQoSCpDefendChassisID_Type.__name__ = "Integer32"
_HwXQoSCpDefendChassisID_Object = MibTableColumn
hwXQoSCpDefendChassisID = _HwXQoSCpDefendChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 6, 1, 1, 20),
    _HwXQoSCpDefendChassisID_Type()
)
hwXQoSCpDefendChassisID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCpDefendChassisID.setStatus("current")
_HwXQoSUrpfObjects_ObjectIdentity = ObjectIdentity
hwXQoSUrpfObjects = _HwXQoSUrpfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 7)
)
_HwXQoSUrpfDiscardStatisticsTable_Object = MibTable
hwXQoSUrpfDiscardStatisticsTable = _HwXQoSUrpfDiscardStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwXQoSUrpfDiscardStatisticsTable.setStatus("current")
_HwXQoSUrpfDiscardStatisticsEntry_Object = MibTableRow
hwXQoSUrpfDiscardStatisticsEntry = _HwXQoSUrpfDiscardStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 7, 1, 1)
)
hwXQoSUrpfDiscardStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSUrpfSlotPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSUrpfDiscardStatisticsEntry.setStatus("current")
_HwXQoSUrpfSlotPhysicalIndex_Type = Integer32
_HwXQoSUrpfSlotPhysicalIndex_Object = MibTableColumn
hwXQoSUrpfSlotPhysicalIndex = _HwXQoSUrpfSlotPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 7, 1, 1, 1),
    _HwXQoSUrpfSlotPhysicalIndex_Type()
)
hwXQoSUrpfSlotPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSUrpfSlotPhysicalIndex.setStatus("current")
_HwXQoSUrpfDiscardedPackets_Type = Counter64
_HwXQoSUrpfDiscardedPackets_Object = MibTableColumn
hwXQoSUrpfDiscardedPackets = _HwXQoSUrpfDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 7, 1, 1, 2),
    _HwXQoSUrpfDiscardedPackets_Type()
)
hwXQoSUrpfDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSUrpfDiscardedPackets.setStatus("current")
_HwXQoSVlanCfgObjects_ObjectIdentity = ObjectIdentity
hwXQoSVlanCfgObjects = _HwXQoSVlanCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 8)
)
_HwXQoSVlanCfgTable_Object = MibTable
hwXQoSVlanCfgTable = _HwXQoSVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hwXQoSVlanCfgTable.setStatus("current")
_HwXQoSVlanCfgEntry_Object = MibTableRow
hwXQoSVlanCfgEntry = _HwXQoSVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 8, 1, 1)
)
hwXQoSVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQosVlanStatVlanId"),
)
if mibBuilder.loadTexts:
    hwXQoSVlanCfgEntry.setStatus("current")
_HwXQoSVlanStatEnable_Type = EnabledStatus
_HwXQoSVlanStatEnable_Object = MibTableColumn
hwXQoSVlanStatEnable = _HwXQoSVlanStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 8, 1, 1, 1),
    _HwXQoSVlanStatEnable_Type()
)
hwXQoSVlanStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSVlanStatEnable.setStatus("current")
_HwXQoSRedirectNextHopObjects_ObjectIdentity = ObjectIdentity
hwXQoSRedirectNextHopObjects = _HwXQoSRedirectNextHopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 9)
)
_HwXQoSRedirectNextHopTable_Object = MibTable
hwXQoSRedirectNextHopTable = _HwXQoSRedirectNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopTable.setStatus("current")
_HwXQoSRedirectNextHopEntry_Object = MibTableRow
hwXQoSRedirectNextHopEntry = _HwXQoSRedirectNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 9, 1, 1)
)
hwXQoSRedirectNextHopEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopBehaviorName"),
)
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopEntry.setStatus("current")


class _HwXQoSRedirectNextHopBehaviorName_Type(OctetString):
    """Custom type hwXQoSRedirectNextHopBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwXQoSRedirectNextHopBehaviorName_Type.__name__ = "OctetString"
_HwXQoSRedirectNextHopBehaviorName_Object = MibTableColumn
hwXQoSRedirectNextHopBehaviorName = _HwXQoSRedirectNextHopBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 9, 1, 1, 1),
    _HwXQoSRedirectNextHopBehaviorName_Type()
)
hwXQoSRedirectNextHopBehaviorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopBehaviorName.setStatus("current")
_HwXQoSRedirectNextHopOldIp_Type = IpAddress
_HwXQoSRedirectNextHopOldIp_Object = MibTableColumn
hwXQoSRedirectNextHopOldIp = _HwXQoSRedirectNextHopOldIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 9, 1, 1, 2),
    _HwXQoSRedirectNextHopOldIp_Type()
)
hwXQoSRedirectNextHopOldIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopOldIp.setStatus("current")
_HwXQoSRedirectNextHopNewIp_Type = IpAddress
_HwXQoSRedirectNextHopNewIp_Object = MibTableColumn
hwXQoSRedirectNextHopNewIp = _HwXQoSRedirectNextHopNewIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 9, 1, 1, 3),
    _HwXQoSRedirectNextHopNewIp_Type()
)
hwXQoSRedirectNextHopNewIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopNewIp.setStatus("current")
_HwXQoSIrsmDefendObjects_ObjectIdentity = ObjectIdentity
hwXQoSIrsmDefendObjects = _HwXQoSIrsmDefendObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10)
)
_HwXQoSIrsmTable_Object = MibTable
hwXQoSIrsmTable = _HwXQoSIrsmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hwXQoSIrsmTable.setStatus("current")
_HwXQoSIrsmEntry_Object = MibTableRow
hwXQoSIrsmEntry = _HwXQoSIrsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1)
)
hwXQoSIrsmEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSIrsmSourceAddress"),
)
if mibBuilder.loadTexts:
    hwXQoSIrsmEntry.setStatus("current")
_HwXQoSIrsmSourceAddress_Type = IpAddress
_HwXQoSIrsmSourceAddress_Object = MibTableColumn
hwXQoSIrsmSourceAddress = _HwXQoSIrsmSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 1),
    _HwXQoSIrsmSourceAddress_Type()
)
hwXQoSIrsmSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmSourceAddress.setStatus("current")
_HwXQoSIrsmGroupAddress_Type = IpAddress
_HwXQoSIrsmGroupAddress_Object = MibTableColumn
hwXQoSIrsmGroupAddress = _HwXQoSIrsmGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 2),
    _HwXQoSIrsmGroupAddress_Type()
)
hwXQoSIrsmGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmGroupAddress.setStatus("current")
_HwXQoSIrsmTime_Type = TimeTicks
_HwXQoSIrsmTime_Object = MibTableColumn
hwXQoSIrsmTime = _HwXQoSIrsmTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 3),
    _HwXQoSIrsmTime_Type()
)
hwXQoSIrsmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmTime.setStatus("current")
_HwXQoSIrsmDelay_Type = Integer32
_HwXQoSIrsmDelay_Object = MibTableColumn
hwXQoSIrsmDelay = _HwXQoSIrsmDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 4),
    _HwXQoSIrsmDelay_Type()
)
hwXQoSIrsmDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmDelay.setStatus("current")
_HwXQoSIrsmThreshold_Type = Integer32
_HwXQoSIrsmThreshold_Object = MibTableColumn
hwXQoSIrsmThreshold = _HwXQoSIrsmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 5),
    _HwXQoSIrsmThreshold_Type()
)
hwXQoSIrsmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmThreshold.setStatus("current")
_HwXQoSIrsmUpstream_Type = IpAddress
_HwXQoSIrsmUpstream_Object = MibTableColumn
hwXQoSIrsmUpstream = _HwXQoSIrsmUpstream_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 6),
    _HwXQoSIrsmUpstream_Type()
)
hwXQoSIrsmUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmUpstream.setStatus("current")
_HwXQoSIrsmLocal_Type = IpAddress
_HwXQoSIrsmLocal_Object = MibTableColumn
hwXQoSIrsmLocal = _HwXQoSIrsmLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 7),
    _HwXQoSIrsmLocal_Type()
)
hwXQoSIrsmLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmLocal.setStatus("current")
_HwXQoSIrsmTotalPacket_Type = Integer32
_HwXQoSIrsmTotalPacket_Object = MibTableColumn
hwXQoSIrsmTotalPacket = _HwXQoSIrsmTotalPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 8),
    _HwXQoSIrsmTotalPacket_Type()
)
hwXQoSIrsmTotalPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmTotalPacket.setStatus("current")
_HwXQoSIrsmDropPacket_Type = Integer32
_HwXQoSIrsmDropPacket_Object = MibTableColumn
hwXQoSIrsmDropPacket = _HwXQoSIrsmDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 10, 1, 1, 9),
    _HwXQoSIrsmDropPacket_Type()
)
hwXQoSIrsmDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSIrsmDropPacket.setStatus("current")
_HwXQoSNotifications_ObjectIdentity = ObjectIdentity
hwXQoSNotifications = _HwXQoSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11)
)
_HwXQoSGeneral_ObjectIdentity = ObjectIdentity
hwXQoSGeneral = _HwXQoSGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12)
)
_HwXQoSFrameId_Type = Integer32
_HwXQoSFrameId_Object = MibScalar
hwXQoSFrameId = _HwXQoSFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12, 1),
    _HwXQoSFrameId_Type()
)
hwXQoSFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSFrameId.setStatus("current")
_HwXQoSSlotId_Type = Integer32
_HwXQoSSlotId_Object = MibScalar
hwXQoSSlotId = _HwXQoSSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12, 2),
    _HwXQoSSlotId_Type()
)
hwXQoSSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSSlotId.setStatus("current")
_HwXQoSPortId_Type = Integer32
_HwXQoSPortId_Object = MibScalar
hwXQoSPortId = _HwXQoSPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12, 3),
    _HwXQoSPortId_Type()
)
hwXQoSPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortId.setStatus("current")


class _HwXQoSTrapIfName_Type(OctetString):
    """Custom type hwXQoSTrapIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSTrapIfName_Type.__name__ = "OctetString"
_HwXQoSTrapIfName_Object = MibScalar
hwXQoSTrapIfName = _HwXQoSTrapIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12, 4),
    _HwXQoSTrapIfName_Type()
)
hwXQoSTrapIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSTrapIfName.setStatus("current")
_HwXQoSTrapQueueId_Type = Integer32
_HwXQoSTrapQueueId_Object = MibScalar
hwXQoSTrapQueueId = _HwXQoSTrapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12, 5),
    _HwXQoSTrapQueueId_Type()
)
hwXQoSTrapQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSTrapQueueId.setStatus("current")
_HwXQoSTrapDiscardPackets_Type = Counter64
_HwXQoSTrapDiscardPackets_Object = MibScalar
hwXQoSTrapDiscardPackets = _HwXQoSTrapDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 12, 6),
    _HwXQoSTrapDiscardPackets_Type()
)
hwXQoSTrapDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSTrapDiscardPackets.setStatus("current")
_HwXQoSStormControlObjects_ObjectIdentity = ObjectIdentity
hwXQoSStormControlObjects = _HwXQoSStormControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13)
)
_HwXQoSStormControlTable_Object = MibTable
hwXQoSStormControlTable = _HwXQoSStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwXQoSStormControlTable.setStatus("current")
_HwXQoSStormControlEntry_Object = MibTableRow
hwXQoSStormControlEntry = _HwXQoSStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1)
)
hwXQoSStormControlEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSStormControlIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSStormControlEntry.setStatus("current")
_HwXQoSStormControlIfIndex_Type = InterfaceIndex
_HwXQoSStormControlIfIndex_Object = MibTableColumn
hwXQoSStormControlIfIndex = _HwXQoSStormControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 1),
    _HwXQoSStormControlIfIndex_Type()
)
hwXQoSStormControlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSStormControlIfIndex.setStatus("current")


class _HwXQoSStormControlBroadcastMinRate_Type(Integer32):
    """Custom type hwXQoSStormControlBroadcastMinRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwXQoSStormControlBroadcastMinRate_Type.__name__ = "Integer32"
_HwXQoSStormControlBroadcastMinRate_Object = MibTableColumn
hwXQoSStormControlBroadcastMinRate = _HwXQoSStormControlBroadcastMinRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 2),
    _HwXQoSStormControlBroadcastMinRate_Type()
)
hwXQoSStormControlBroadcastMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlBroadcastMinRate.setStatus("current")


class _HwXQoSStormControlBroadcastMaxRate_Type(Integer32):
    """Custom type hwXQoSStormControlBroadcastMaxRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwXQoSStormControlBroadcastMaxRate_Type.__name__ = "Integer32"
_HwXQoSStormControlBroadcastMaxRate_Object = MibTableColumn
hwXQoSStormControlBroadcastMaxRate = _HwXQoSStormControlBroadcastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 3),
    _HwXQoSStormControlBroadcastMaxRate_Type()
)
hwXQoSStormControlBroadcastMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlBroadcastMaxRate.setStatus("current")


class _HwXQoSStormControlMulticastMinRate_Type(Integer32):
    """Custom type hwXQoSStormControlMulticastMinRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwXQoSStormControlMulticastMinRate_Type.__name__ = "Integer32"
_HwXQoSStormControlMulticastMinRate_Object = MibTableColumn
hwXQoSStormControlMulticastMinRate = _HwXQoSStormControlMulticastMinRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 4),
    _HwXQoSStormControlMulticastMinRate_Type()
)
hwXQoSStormControlMulticastMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlMulticastMinRate.setStatus("current")


class _HwXQoSStormControlMulticastMaxRate_Type(Integer32):
    """Custom type hwXQoSStormControlMulticastMaxRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwXQoSStormControlMulticastMaxRate_Type.__name__ = "Integer32"
_HwXQoSStormControlMulticastMaxRate_Object = MibTableColumn
hwXQoSStormControlMulticastMaxRate = _HwXQoSStormControlMulticastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 5),
    _HwXQoSStormControlMulticastMaxRate_Type()
)
hwXQoSStormControlMulticastMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlMulticastMaxRate.setStatus("current")


class _HwXQoSStormControlAction_Type(Integer32):
    """Custom type hwXQoSStormControlAction based on Integer32"""
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
        *(("block", 2),
          ("none", 1),
          ("shutdown", 3))
    )


_HwXQoSStormControlAction_Type.__name__ = "Integer32"
_HwXQoSStormControlAction_Object = MibTableColumn
hwXQoSStormControlAction = _HwXQoSStormControlAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 6),
    _HwXQoSStormControlAction_Type()
)
hwXQoSStormControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlAction.setStatus("current")


class _HwXQoSStormControlInterval_Type(Integer32):
    """Custom type hwXQoSStormControlInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_HwXQoSStormControlInterval_Type.__name__ = "Integer32"
_HwXQoSStormControlInterval_Object = MibTableColumn
hwXQoSStormControlInterval = _HwXQoSStormControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 7),
    _HwXQoSStormControlInterval_Type()
)
hwXQoSStormControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlInterval.setStatus("current")


class _HwXQoSStormControlTrapEnable_Type(EnabledStatus):
    """Custom type hwXQoSStormControlTrapEnable based on EnabledStatus"""
    defaultValue = 2


_HwXQoSStormControlTrapEnable_Object = MibTableColumn
hwXQoSStormControlTrapEnable = _HwXQoSStormControlTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 8),
    _HwXQoSStormControlTrapEnable_Type()
)
hwXQoSStormControlTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlTrapEnable.setStatus("current")


class _HwXQoSStormControlLogEnable_Type(EnabledStatus):
    """Custom type hwXQoSStormControlLogEnable based on EnabledStatus"""
    defaultValue = 2


_HwXQoSStormControlLogEnable_Object = MibTableColumn
hwXQoSStormControlLogEnable = _HwXQoSStormControlLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 9),
    _HwXQoSStormControlLogEnable_Type()
)
hwXQoSStormControlLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlLogEnable.setStatus("current")


class _HwXQoSStormControlStatus_Type(Integer32):
    """Custom type hwXQoSStormControlStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("allBlocked", 7),
          ("bcmcBlocked", 8),
          ("bcucBlocked", 9),
          ("bothBlocked", 4),
          ("broadcastBlocked", 2),
          ("multicastBlocked", 3),
          ("normal", 1),
          ("shutdown", 5),
          ("ucmcBlocked", 10),
          ("unicastBlocked", 6))
    )


_HwXQoSStormControlStatus_Type.__name__ = "Integer32"
_HwXQoSStormControlStatus_Object = MibTableColumn
hwXQoSStormControlStatus = _HwXQoSStormControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 10),
    _HwXQoSStormControlStatus_Type()
)
hwXQoSStormControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSStormControlStatus.setStatus("current")


class _HwXQoSStormControlUnicastMinRate_Type(Integer32):
    """Custom type hwXQoSStormControlUnicastMinRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwXQoSStormControlUnicastMinRate_Type.__name__ = "Integer32"
_HwXQoSStormControlUnicastMinRate_Object = MibTableColumn
hwXQoSStormControlUnicastMinRate = _HwXQoSStormControlUnicastMinRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 11),
    _HwXQoSStormControlUnicastMinRate_Type()
)
hwXQoSStormControlUnicastMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlUnicastMinRate.setStatus("current")


class _HwXQoSStormControlUnicastMaxRate_Type(Integer32):
    """Custom type hwXQoSStormControlUnicastMaxRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwXQoSStormControlUnicastMaxRate_Type.__name__ = "Integer32"
_HwXQoSStormControlUnicastMaxRate_Object = MibTableColumn
hwXQoSStormControlUnicastMaxRate = _HwXQoSStormControlUnicastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 12),
    _HwXQoSStormControlUnicastMaxRate_Type()
)
hwXQoSStormControlUnicastMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlUnicastMaxRate.setStatus("current")


class _HwXQoSStormControlBcMode_Type(Integer32):
    """Custom type hwXQoSStormControlBcMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("none", 3),
          ("percent", 2),
          ("pps", 0))
    )


_HwXQoSStormControlBcMode_Type.__name__ = "Integer32"
_HwXQoSStormControlBcMode_Object = MibTableColumn
hwXQoSStormControlBcMode = _HwXQoSStormControlBcMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 13),
    _HwXQoSStormControlBcMode_Type()
)
hwXQoSStormControlBcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlBcMode.setStatus("current")


class _HwXQoSStormControlMcMode_Type(Integer32):
    """Custom type hwXQoSStormControlMcMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("none", 3),
          ("percent", 2),
          ("pps", 0))
    )


_HwXQoSStormControlMcMode_Type.__name__ = "Integer32"
_HwXQoSStormControlMcMode_Object = MibTableColumn
hwXQoSStormControlMcMode = _HwXQoSStormControlMcMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 14),
    _HwXQoSStormControlMcMode_Type()
)
hwXQoSStormControlMcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlMcMode.setStatus("current")


class _HwXQoSStormControlUcMode_Type(Integer32):
    """Custom type hwXQoSStormControlUcMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 1),
          ("none", 3),
          ("percent", 2),
          ("pps", 0))
    )


_HwXQoSStormControlUcMode_Type.__name__ = "Integer32"
_HwXQoSStormControlUcMode_Object = MibTableColumn
hwXQoSStormControlUcMode = _HwXQoSStormControlUcMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 13, 1, 1, 15),
    _HwXQoSStormControlUcMode_Type()
)
hwXQoSStormControlUcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSStormControlUcMode.setStatus("current")
_HwXQoSStormControlNotification_ObjectIdentity = ObjectIdentity
hwXQoSStormControlNotification = _HwXQoSStormControlNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 14)
)
_HwXQoSQueueStatisticsObjects_ObjectIdentity = ObjectIdentity
hwXQoSQueueStatisticsObjects = _HwXQoSQueueStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15)
)
_HwXQoSQueueStatisticsTable_Object = MibTable
hwXQoSQueueStatisticsTable = _HwXQoSQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsTable.setStatus("current")
_HwXQoSQueueStatisticsEntry_Object = MibTableRow
hwXQoSQueueStatisticsEntry = _HwXQoSQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1)
)
hwXQoSQueueStatisticsEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsIngressIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsEgressIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsQueueIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsEntry.setStatus("current")
_HwXQoSQueueStatisticsIngressIfIndex_Type = InterfaceIndex
_HwXQoSQueueStatisticsIngressIfIndex_Object = MibTableColumn
hwXQoSQueueStatisticsIngressIfIndex = _HwXQoSQueueStatisticsIngressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1, 1),
    _HwXQoSQueueStatisticsIngressIfIndex_Type()
)
hwXQoSQueueStatisticsIngressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsIngressIfIndex.setStatus("current")
_HwXQoSQueueStatisticsEgressIfIndex_Type = InterfaceIndex
_HwXQoSQueueStatisticsEgressIfIndex_Object = MibTableColumn
hwXQoSQueueStatisticsEgressIfIndex = _HwXQoSQueueStatisticsEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1, 2),
    _HwXQoSQueueStatisticsEgressIfIndex_Type()
)
hwXQoSQueueStatisticsEgressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsEgressIfIndex.setStatus("current")


class _HwXQoSQueueStatisticsQueueIndex_Type(Integer32):
    """Custom type hwXQoSQueueStatisticsQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSQueueStatisticsQueueIndex_Type.__name__ = "Integer32"
_HwXQoSQueueStatisticsQueueIndex_Object = MibTableColumn
hwXQoSQueueStatisticsQueueIndex = _HwXQoSQueueStatisticsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1, 3),
    _HwXQoSQueueStatisticsQueueIndex_Type()
)
hwXQoSQueueStatisticsQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsQueueIndex.setStatus("current")
_HwXQoSQueueStatisticsPassedPacketsCount_Type = Counter64
_HwXQoSQueueStatisticsPassedPacketsCount_Object = MibTableColumn
hwXQoSQueueStatisticsPassedPacketsCount = _HwXQoSQueueStatisticsPassedPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1, 4),
    _HwXQoSQueueStatisticsPassedPacketsCount_Type()
)
hwXQoSQueueStatisticsPassedPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsPassedPacketsCount.setStatus("current")


class _HwXQosQueueStatisticsReset_Type(Integer32):
    """Custom type hwXQosQueueStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwXQosQueueStatisticsReset_Type.__name__ = "Integer32"
_HwXQosQueueStatisticsReset_Object = MibTableColumn
hwXQosQueueStatisticsReset = _HwXQosQueueStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1, 5),
    _HwXQosQueueStatisticsReset_Type()
)
hwXQosQueueStatisticsReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQosQueueStatisticsReset.setStatus("current")
_HwXQoSQueueStatisticsRowStatus_Type = RowStatus
_HwXQoSQueueStatisticsRowStatus_Object = MibTableColumn
hwXQoSQueueStatisticsRowStatus = _HwXQoSQueueStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 15, 1, 1, 6),
    _HwXQoSQueueStatisticsRowStatus_Type()
)
hwXQoSQueueStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsRowStatus.setStatus("current")
_HwXQoSPortStatisticsDropObjects_ObjectIdentity = ObjectIdentity
hwXQoSPortStatisticsDropObjects = _HwXQoSPortStatisticsDropObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16)
)
_HwXQoSPortStatisticsDropTable_Object = MibTable
hwXQoSPortStatisticsDropTable = _HwXQoSPortStatisticsDropTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    hwXQoSPortStatisticsDropTable.setStatus("current")
_HwXQoSPortStatisticsDropEntry_Object = MibTableRow
hwXQoSPortStatisticsDropEntry = _HwXQoSPortStatisticsDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16, 1, 1)
)
hwXQoSPortStatisticsDropEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPortStatisticsDropIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSPortStatisticsDropEntry.setStatus("current")
_HwXQoSPortStatisticsDropIfIndex_Type = InterfaceIndex
_HwXQoSPortStatisticsDropIfIndex_Object = MibTableColumn
hwXQoSPortStatisticsDropIfIndex = _HwXQoSPortStatisticsDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16, 1, 1, 1),
    _HwXQoSPortStatisticsDropIfIndex_Type()
)
hwXQoSPortStatisticsDropIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSPortStatisticsDropIfIndex.setStatus("current")
_HwXQoSPortStatisticsDropPacketsCount_Type = Counter64
_HwXQoSPortStatisticsDropPacketsCount_Object = MibTableColumn
hwXQoSPortStatisticsDropPacketsCount = _HwXQoSPortStatisticsDropPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16, 1, 1, 2),
    _HwXQoSPortStatisticsDropPacketsCount_Type()
)
hwXQoSPortStatisticsDropPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSPortStatisticsDropPacketsCount.setStatus("current")


class _HwXQosPortStatisticsDropReset_Type(Integer32):
    """Custom type hwXQosPortStatisticsDropReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwXQosPortStatisticsDropReset_Type.__name__ = "Integer32"
_HwXQosPortStatisticsDropReset_Object = MibTableColumn
hwXQosPortStatisticsDropReset = _HwXQosPortStatisticsDropReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16, 1, 1, 3),
    _HwXQosPortStatisticsDropReset_Type()
)
hwXQosPortStatisticsDropReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQosPortStatisticsDropReset.setStatus("current")
_HwXQosPortStatisticsDropResetTime_Type = TimeTicks
_HwXQosPortStatisticsDropResetTime_Object = MibTableColumn
hwXQosPortStatisticsDropResetTime = _HwXQosPortStatisticsDropResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 16, 1, 1, 4),
    _HwXQosPortStatisticsDropResetTime_Type()
)
hwXQosPortStatisticsDropResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosPortStatisticsDropResetTime.setStatus("current")
_HwXQoSQueueStatisticsDropObjects_ObjectIdentity = ObjectIdentity
hwXQoSQueueStatisticsDropObjects = _HwXQoSQueueStatisticsDropObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17)
)
_HwXQoSQueueStatisticsDropTable_Object = MibTable
hwXQoSQueueStatisticsDropTable = _HwXQoSQueueStatisticsDropTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1)
)
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsDropTable.setStatus("current")
_HwXQoSQueueStatisticsDropEntry_Object = MibTableRow
hwXQoSQueueStatisticsDropEntry = _HwXQoSQueueStatisticsDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1, 1)
)
hwXQoSQueueStatisticsDropEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsDropIfIndex"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsDropQueueIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsDropEntry.setStatus("current")
_HwXQoSQueueStatisticsDropIfIndex_Type = InterfaceIndex
_HwXQoSQueueStatisticsDropIfIndex_Object = MibTableColumn
hwXQoSQueueStatisticsDropIfIndex = _HwXQoSQueueStatisticsDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1, 1, 1),
    _HwXQoSQueueStatisticsDropIfIndex_Type()
)
hwXQoSQueueStatisticsDropIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsDropIfIndex.setStatus("current")


class _HwXQoSQueueStatisticsDropQueueIndex_Type(Integer32):
    """Custom type hwXQoSQueueStatisticsDropQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("af1", 2),
          ("af2", 3),
          ("af3", 4),
          ("af4", 5),
          ("be", 1),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 6))
    )


_HwXQoSQueueStatisticsDropQueueIndex_Type.__name__ = "Integer32"
_HwXQoSQueueStatisticsDropQueueIndex_Object = MibTableColumn
hwXQoSQueueStatisticsDropQueueIndex = _HwXQoSQueueStatisticsDropQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1, 1, 2),
    _HwXQoSQueueStatisticsDropQueueIndex_Type()
)
hwXQoSQueueStatisticsDropQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsDropQueueIndex.setStatus("current")
_HwXQoSQueueStatisticsDropPacketsCount_Type = Counter64
_HwXQoSQueueStatisticsDropPacketsCount_Object = MibTableColumn
hwXQoSQueueStatisticsDropPacketsCount = _HwXQoSQueueStatisticsDropPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1, 1, 3),
    _HwXQoSQueueStatisticsDropPacketsCount_Type()
)
hwXQoSQueueStatisticsDropPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsDropPacketsCount.setStatus("current")


class _HwXQosQueueStatisticsDropReset_Type(Integer32):
    """Custom type hwXQosQueueStatisticsDropReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwXQosQueueStatisticsDropReset_Type.__name__ = "Integer32"
_HwXQosQueueStatisticsDropReset_Object = MibTableColumn
hwXQosQueueStatisticsDropReset = _HwXQosQueueStatisticsDropReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1, 1, 4),
    _HwXQosQueueStatisticsDropReset_Type()
)
hwXQosQueueStatisticsDropReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQosQueueStatisticsDropReset.setStatus("current")
_HwXQosQueueStatisticsDropResetTime_Type = TimeTicks
_HwXQosQueueStatisticsDropResetTime_Object = MibTableColumn
hwXQosQueueStatisticsDropResetTime = _HwXQosQueueStatisticsDropResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 17, 1, 1, 5),
    _HwXQosQueueStatisticsDropResetTime_Type()
)
hwXQosQueueStatisticsDropResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQosQueueStatisticsDropResetTime.setStatus("current")
_HwXQoSRuleFailObjects_ObjectIdentity = ObjectIdentity
hwXQoSRuleFailObjects = _HwXQoSRuleFailObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 18)
)
_HwXQoSRuleFailTable_Object = MibTable
hwXQoSRuleFailTable = _HwXQoSRuleFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 18, 1)
)
if mibBuilder.loadTexts:
    hwXQoSRuleFailTable.setStatus("current")
_HwXQoSRuleFailEntry_Object = MibTableRow
hwXQoSRuleFailEntry = _HwXQoSRuleFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 18, 1, 1)
)
hwXQoSRuleFailEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSRuleFailInfo"),
)
if mibBuilder.loadTexts:
    hwXQoSRuleFailEntry.setStatus("current")


class _HwXQoSRuleFailInfo_Type(OctetString):
    """Custom type hwXQoSRuleFailInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwXQoSRuleFailInfo_Type.__name__ = "OctetString"
_HwXQoSRuleFailInfo_Object = MibTableColumn
hwXQoSRuleFailInfo = _HwXQoSRuleFailInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 18, 1, 1, 1),
    _HwXQoSRuleFailInfo_Type()
)
hwXQoSRuleFailInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSRuleFailInfo.setStatus("current")
_HwXQoSProfileObjects_ObjectIdentity = ObjectIdentity
hwXQoSProfileObjects = _HwXQoSProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 19)
)
_HwXQoSProfileTable_Object = MibTable
hwXQoSProfileTable = _HwXQoSProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 19, 1)
)
if mibBuilder.loadTexts:
    hwXQoSProfileTable.setStatus("current")
_HwXQoSProfileEntry_Object = MibTableRow
hwXQoSProfileEntry = _HwXQoSProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 19, 1, 1)
)
hwXQoSProfileEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSProfileName"),
)
if mibBuilder.loadTexts:
    hwXQoSProfileEntry.setStatus("current")


class _HwXQoSProfileName_Type(OctetString):
    """Custom type hwXQoSProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwXQoSProfileName_Type.__name__ = "OctetString"
_HwXQoSProfileName_Object = MibTableColumn
hwXQoSProfileName = _HwXQoSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 19, 1, 1, 1),
    _HwXQoSProfileName_Type()
)
hwXQoSProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSProfileName.setStatus("current")
_HwXQoSPortQueueAlarmObjects_ObjectIdentity = ObjectIdentity
hwXQoSPortQueueAlarmObjects = _HwXQoSPortQueueAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 20)
)
_HwXQoSPortQueueAlarmTable_Object = MibTable
hwXQoSPortQueueAlarmTable = _HwXQoSPortQueueAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 20, 1)
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarmTable.setStatus("current")
_HwXQoSPortQueueAlarmEntry_Object = MibTableRow
hwXQoSPortQueueAlarmEntry = _HwXQoSPortQueueAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 20, 1, 1)
)
hwXQoSPortQueueAlarmEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmIfIndex"),
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarmEntry.setStatus("current")
_HwXQoSPortQueueAlarmIfIndex_Type = InterfaceIndex
_HwXQoSPortQueueAlarmIfIndex_Object = MibTableColumn
hwXQoSPortQueueAlarmIfIndex = _HwXQoSPortQueueAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 20, 1, 1, 1),
    _HwXQoSPortQueueAlarmIfIndex_Type()
)
hwXQoSPortQueueAlarmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarmIfIndex.setStatus("current")


class _HwXQoSPortQueueAlarmQueue_Type(OctetString):
    """Custom type hwXQoSPortQueueAlarmQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_HwXQoSPortQueueAlarmQueue_Type.__name__ = "OctetString"
_HwXQoSPortQueueAlarmQueue_Object = MibTableColumn
hwXQoSPortQueueAlarmQueue = _HwXQoSPortQueueAlarmQueue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 20, 1, 1, 2),
    _HwXQoSPortQueueAlarmQueue_Type()
)
hwXQoSPortQueueAlarmQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarmQueue.setStatus("current")
_HwXQoSPortQueueAlarmTrunkIndex_Type = InterfaceIndex
_HwXQoSPortQueueAlarmTrunkIndex_Object = MibTableColumn
hwXQoSPortQueueAlarmTrunkIndex = _HwXQoSPortQueueAlarmTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 20, 1, 1, 3),
    _HwXQoSPortQueueAlarmTrunkIndex_Type()
)
hwXQoSPortQueueAlarmTrunkIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarmTrunkIndex.setStatus("current")
_HwXQoSSecurityStormControlInterfaceObjects_ObjectIdentity = ObjectIdentity
hwXQoSSecurityStormControlInterfaceObjects = _HwXQoSSecurityStormControlInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21)
)
_HwXQoSSecurityStormControlInterfaceTable_Object = MibTable
hwXQoSSecurityStormControlInterfaceTable = _HwXQoSSecurityStormControlInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21, 1)
)
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceTable.setStatus("current")
_HwXQoSSecurityStormControlInterfaceEntry_Object = MibTableRow
hwXQoSSecurityStormControlInterfaceEntry = _HwXQoSSecurityStormControlInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21, 1, 1)
)
hwXQoSSecurityStormControlInterfaceEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSSecurityStormControlInterfaceChassisId"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSSecurityStormControlInterfaceSlotId"),
)
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceEntry.setStatus("current")


class _HwXQoSSecurityStormControlInterfaceChassisId_Type(Integer32):
    """Custom type hwXQoSSecurityStormControlInterfaceChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwXQoSSecurityStormControlInterfaceChassisId_Type.__name__ = "Integer32"
_HwXQoSSecurityStormControlInterfaceChassisId_Object = MibTableColumn
hwXQoSSecurityStormControlInterfaceChassisId = _HwXQoSSecurityStormControlInterfaceChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21, 1, 1, 1),
    _HwXQoSSecurityStormControlInterfaceChassisId_Type()
)
hwXQoSSecurityStormControlInterfaceChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceChassisId.setStatus("current")


class _HwXQoSSecurityStormControlInterfaceSlotId_Type(Integer32):
    """Custom type hwXQoSSecurityStormControlInterfaceSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwXQoSSecurityStormControlInterfaceSlotId_Type.__name__ = "Integer32"
_HwXQoSSecurityStormControlInterfaceSlotId_Object = MibTableColumn
hwXQoSSecurityStormControlInterfaceSlotId = _HwXQoSSecurityStormControlInterfaceSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21, 1, 1, 2),
    _HwXQoSSecurityStormControlInterfaceSlotId_Type()
)
hwXQoSSecurityStormControlInterfaceSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceSlotId.setStatus("current")


class _HwXQoSSecurityStormControlInterfaceName_Type(OctetString):
    """Custom type hwXQoSSecurityStormControlInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwXQoSSecurityStormControlInterfaceName_Type.__name__ = "OctetString"
_HwXQoSSecurityStormControlInterfaceName_Object = MibTableColumn
hwXQoSSecurityStormControlInterfaceName = _HwXQoSSecurityStormControlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21, 1, 1, 3),
    _HwXQoSSecurityStormControlInterfaceName_Type()
)
hwXQoSSecurityStormControlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceName.setStatus("current")


class _HwXQoSSecurityStormControlInterfaceVlan_Type(Integer32):
    """Custom type hwXQoSSecurityStormControlInterfaceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwXQoSSecurityStormControlInterfaceVlan_Type.__name__ = "Integer32"
_HwXQoSSecurityStormControlInterfaceVlan_Object = MibTableColumn
hwXQoSSecurityStormControlInterfaceVlan = _HwXQoSSecurityStormControlInterfaceVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 21, 1, 1, 4),
    _HwXQoSSecurityStormControlInterfaceVlan_Type()
)
hwXQoSSecurityStormControlInterfaceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceVlan.setStatus("current")
_HwXQoSResouceNotEnoughAlarmObjects_ObjectIdentity = ObjectIdentity
hwXQoSResouceNotEnoughAlarmObjects = _HwXQoSResouceNotEnoughAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22)
)
_HwXQoSStatResouceNotEnoughAlarmTable_Object = MibTable
hwXQoSStatResouceNotEnoughAlarmTable = _HwXQoSStatResouceNotEnoughAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 1)
)
if mibBuilder.loadTexts:
    hwXQoSStatResouceNotEnoughAlarmTable.setStatus("current")
_HwXQoSStatResouceNotEnoughAlarmEntry_Object = MibTableRow
hwXQoSStatResouceNotEnoughAlarmEntry = _HwXQoSStatResouceNotEnoughAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 1, 1)
)
hwXQoSStatResouceNotEnoughAlarmEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSStatResouceNotEnoughSlotId"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSStatResouceNotEnoughStatType"),
)
if mibBuilder.loadTexts:
    hwXQoSStatResouceNotEnoughAlarmEntry.setStatus("current")


class _HwXQoSStatResouceNotEnoughSlotId_Type(Integer32):
    """Custom type hwXQoSStatResouceNotEnoughSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwXQoSStatResouceNotEnoughSlotId_Type.__name__ = "Integer32"
_HwXQoSStatResouceNotEnoughSlotId_Object = MibTableColumn
hwXQoSStatResouceNotEnoughSlotId = _HwXQoSStatResouceNotEnoughSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 1, 1, 1),
    _HwXQoSStatResouceNotEnoughSlotId_Type()
)
hwXQoSStatResouceNotEnoughSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSStatResouceNotEnoughSlotId.setStatus("current")


class _HwXQoSStatResouceNotEnoughStatType_Type(OctetString):
    """Custom type hwXQoSStatResouceNotEnoughStatType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwXQoSStatResouceNotEnoughStatType_Type.__name__ = "OctetString"
_HwXQoSStatResouceNotEnoughStatType_Object = MibTableColumn
hwXQoSStatResouceNotEnoughStatType = _HwXQoSStatResouceNotEnoughStatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 1, 1, 2),
    _HwXQoSStatResouceNotEnoughStatType_Type()
)
hwXQoSStatResouceNotEnoughStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSStatResouceNotEnoughStatType.setStatus("current")
_HwXQoSCARResouceNotEnoughAlarmTable_Object = MibTable
hwXQoSCARResouceNotEnoughAlarmTable = _HwXQoSCARResouceNotEnoughAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 2)
)
if mibBuilder.loadTexts:
    hwXQoSCARResouceNotEnoughAlarmTable.setStatus("current")
_HwXQoSCARResouceNotEnoughAlarmEntry_Object = MibTableRow
hwXQoSCARResouceNotEnoughAlarmEntry = _HwXQoSCARResouceNotEnoughAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 2, 1)
)
hwXQoSCARResouceNotEnoughAlarmEntry.setIndexNames(
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCARResouceNotEnoughSlotId"),
    (0, "HUAWEI-XQoS-MIB", "hwXQoSCARResouceNotEnoughCARType"),
)
if mibBuilder.loadTexts:
    hwXQoSCARResouceNotEnoughAlarmEntry.setStatus("current")


class _HwXQoSCARResouceNotEnoughSlotId_Type(Integer32):
    """Custom type hwXQoSCARResouceNotEnoughSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwXQoSCARResouceNotEnoughSlotId_Type.__name__ = "Integer32"
_HwXQoSCARResouceNotEnoughSlotId_Object = MibTableColumn
hwXQoSCARResouceNotEnoughSlotId = _HwXQoSCARResouceNotEnoughSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 2, 1, 1),
    _HwXQoSCARResouceNotEnoughSlotId_Type()
)
hwXQoSCARResouceNotEnoughSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCARResouceNotEnoughSlotId.setStatus("current")


class _HwXQoSCARResouceNotEnoughCARType_Type(OctetString):
    """Custom type hwXQoSCARResouceNotEnoughCARType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 511),
    )


_HwXQoSCARResouceNotEnoughCARType_Type.__name__ = "OctetString"
_HwXQoSCARResouceNotEnoughCARType_Object = MibTableColumn
hwXQoSCARResouceNotEnoughCARType = _HwXQoSCARResouceNotEnoughCARType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 22, 2, 1, 2),
    _HwXQoSCARResouceNotEnoughCARType_Type()
)
hwXQoSCARResouceNotEnoughCARType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwXQoSCARResouceNotEnoughCARType.setStatus("current")
_HwXQoSConformance_ObjectIdentity = ObjectIdentity
hwXQoSConformance = _HwXQoSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2)
)
_HwXQoSCompliances_ObjectIdentity = ObjectIdentity
hwXQoSCompliances = _HwXQoSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 1)
)
_HwXQoSGroups_ObjectIdentity = ObjectIdentity
hwXQoSGroups = _HwXQoSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2)
)

# Managed Objects groups

hwXQoSIfQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 1)
)
hwXQoSIfQueueGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfQueueIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueVlanID"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueCosType"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueuePassedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueuePassededBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueTotalPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueTotalBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueDiscardedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueDiscardedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueuePassedPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueuePassedByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueDiscardedPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueDiscardedByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueResetFlag"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfQueueUsagePercentage"))
)
if mibBuilder.loadTexts:
    hwXQoSIfQueueGroup.setStatus("current")

hwXQoSIfCarStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 2)
)
hwXQoSIfCarStatisticsGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfCarConformedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarConformedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarConformedPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarConformedByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarExceededPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarExceededBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarExceededPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarExceededByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarOverflowPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarOverflowBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarOverflowPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarOverflowByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarPassedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarPassedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarDiscardedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfCarDiscardedBytes"))
)
if mibBuilder.loadTexts:
    hwXQoSIfCarStatisticsGroup.setStatus("current")

hwXQoSCpDefendStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 3)
)
hwXQoSCpDefendStatisticsGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpDefendSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendObjectIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendPassedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendPassedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendPassedPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendPassedByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedPacketRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedByteRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedThreshold"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendChassisID"))
)
if mibBuilder.loadTexts:
    hwXQoSCpDefendStatisticsGroup.setStatus("current")

hwXQoSGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 5)
)
hwXQoSGeneralGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSFrameId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSTrapIfName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSTrapQueueId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSTrapDiscardPackets"))
)
if mibBuilder.loadTexts:
    hwXQoSGeneralGroup.setStatus("current")

hwXQoSSredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 6)
)
hwXQoSSredGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfSredQueueIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfSredRedStartDiscardPoint"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfSredRedDiscardProbability"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfSredYellowStartDiscardPoint"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfSredYellowDiscardProbability"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfSredRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSSredGroup.setStatus("current")

hwXQosAtmTrafficQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 7)
)
hwXQosAtmTrafficQueueGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSAtmTrafficQueueServiceClass"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmTrafficQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQosAtmTrafficQueueGroup.setStatus("current")

hwXQosAtmPvcServiceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 8)
)
hwXQosAtmPvcServiceTypeGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcNameServiceTypeIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcServiceType"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcPcr"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcCdvt"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcVbrScr"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcVbrMbs"),
        ("HUAWEI-XQoS-MIB", "hwXQoSAtmPvcRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQosAtmPvcServiceTypeGroup.setStatus("current")

hwXQosIfOutboundQueueStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 9)
)
hwXQosIfOutboundQueueStatisticGroup.setObjects(
    ("HUAWEI-XQoS-MIB", "hwXQoSIfQueDiscardPackets")
)
if mibBuilder.loadTexts:
    hwXQosIfOutboundQueueStatisticGroup.setStatus("current")

hwXQoSShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 10)
)
hwXQoSShapingGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfShapingIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfShapingQueueIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfShapingQueueCir"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfShapingQueuePir"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfShapingRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSShapingGroup.setStatus("current")

hwXQoSUrpfDiscardStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 11)
)
hwXQoSUrpfDiscardStatisticsGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSUrpfSlotPhysicalIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSUrpfDiscardedPackets"))
)
if mibBuilder.loadTexts:
    hwXQoSUrpfDiscardStatisticsGroup.setStatus("current")

hwXQoSBaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 12)
)
hwXQoSBaGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaGroup.setStatus("current")

hwXQoSBa8021pPhbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 13)
)
hwXQoSBa8021pPhbGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBa8021pPhbIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pPhbPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pPhbCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pPhbColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pPhbRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBa8021pPhbGroup.setStatus("current")

hwXQoSBa8021pMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 14)
)
hwXQoSBa8021pMapGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBa8021pMapIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pMapCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pMapColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pMapPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBa8021pMapRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBa8021pMapGroup.setStatus("current")

hwXQoSBaDscpPhbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 15)
)
hwXQoSBaDscpPhbGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaDscpPhbIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpPhbPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpPhbCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpPhbColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpPhbRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaDscpPhbGroup.setStatus("current")

hwXQoSBaDscpMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 16)
)
hwXQoSBaDscpMapGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaDscpMapIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpMapCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpMapColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpMapPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaDscpMapRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaDscpMapGroup.setStatus("current")

hwXQoSBaExpPhbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 17)
)
hwXQoSBaExpPhbGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaExpPhbIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpPhbPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpPhbCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpPhbColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpPhbRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaExpPhbGroup.setStatus("current")

hwXQoSBaExpMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 18)
)
hwXQoSBaExpMapGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaExpMapIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpMapCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpMapColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpMapPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaExpMapRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaExpMapGroup.setStatus("current")

hwXQoSIfDiffDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 19)
)
hwXQoSIfDiffDomainGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainVlanId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainRowStatus"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfDiffDomainVlanId2"))
)
if mibBuilder.loadTexts:
    hwXQoSIfDiffDomainGroup.setStatus("current")

hwXQoSBaPhbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 20)
)
hwXQoSBaPhbGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaPhbType"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaPhbPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaPhbCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaPhbColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaPhbRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaPhbGroup.setStatus("current")

hwXQoSBaMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 21)
)
hwXQoSBaMapGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSBaMapType"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaMapCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaMapColour"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaMapPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaMapRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSBaMapGroup.setStatus("current")

hwXQoSIfTrustGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 22)
)
hwXQoSIfTrustGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfTrustIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrustVlanID1"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrustVlanID2"),
        ("HUAWEI-XQoS-MIB", "hwXQoSBaType"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrustAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrustRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSIfTrustGroup.setStatus("current")

hwXQosVlanStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 23)
)
hwXQosVlanStatGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQosVlanStatInTotalPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInTotalBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutTotalPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutTotalBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInUcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInUcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutUcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutUcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInMcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInMcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutMcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutMcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInBcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInBcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutBcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatOutBcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInUnknownUcastPkts"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatInUnknownUcastBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQosVlanStatResetFlag"))
)
if mibBuilder.loadTexts:
    hwXQosVlanStatGroup.setStatus("current")

hwXQoSVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 24)
)
hwXQoSVlanCfgGroup.setObjects(
    ("HUAWEI-XQoS-MIB", "hwXQoSVlanStatEnable")
)
if mibBuilder.loadTexts:
    hwXQoSVlanCfgGroup.setStatus("current")

hwXQoSStormControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 25)
)
hwXQoSStormControlGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSStormControlBroadcastMinRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlBroadcastMaxRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlMulticastMinRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlMulticastMaxRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlInterval"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlTrapEnable"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlLogEnable"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlStatus"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlUnicastMinRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlUnicastMaxRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlBcMode"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlMcMode"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlUcMode"))
)
if mibBuilder.loadTexts:
    hwXQoSStormControlGroup.setStatus("current")

hwXQoSQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 26)
)
hwXQoSQueueStatisticsGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsPassedPacketsCount"),
        ("HUAWEI-XQoS-MIB", "hwXQosQueueStatisticsReset"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsGroup.setStatus("current")

hwXQoSIfPppoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 27)
)
hwXQoSIfPppoeGroup.setObjects(
    ("HUAWEI-XQoS-MIB", "hwXQoSIfPppoeRowStatus")
)
if mibBuilder.loadTexts:
    hwXQoSIfPppoeGroup.setStatus("current")

hwXQoSVlanBcastSuppressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 28)
)
hwXQoSVlanBcastSuppressGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSVlanBcastSuppressValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSVlanBcastSuppressRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSVlanBcastSuppressGroup.setStatus("current")

hwXQoSRedirectNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 29)
)
hwXQoSRedirectNextHopGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopBehaviorName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopOldIp"),
        ("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopNewIp"))
)
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopGroup.setStatus("current")

hwXQoSIfTrust8021pGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 30)
)
hwXQoSIfTrust8021pGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfTrust8021pIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrust8021pVlanID"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrust8021pAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfTrust8021pRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSIfTrust8021pGroup.setStatus("current")

hwXQoSCommonInboundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 31)
)
hwXQoSCommonInboundGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCommonInboundPhbIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCommonInboundPhbCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCommonInboundPhbColor"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCommonInboundPhbPri"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCommonInboundRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSCommonInboundGroup.setStatus("current")

hwXQoSPppInboundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 32)
)
hwXQoSPppInboundGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPppInboundCos"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPppInboundColor"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPppInboundRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSPppInboundGroup.setStatus("current")

hwXQoSServiceclassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 33)
)
hwXQoSServiceclassGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSServiceclassPort"),
        ("HUAWEI-XQoS-MIB", "hwXQoSServiceclass"),
        ("HUAWEI-XQoS-MIB", "hwXQoSServiceclassRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSServiceclassGroup.setStatus("current")

hwXQoSPhbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 34)
)
hwXQoSPhbGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPhbPort"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPhbEnable"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPhbRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSPhbGroup.setStatus("current")

hwXQoSFieldDeiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 35)
)
hwXQoSFieldDeiGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSFieldDeiInterface"),
        ("HUAWEI-XQoS-MIB", "hwXQoSFieldDeiVlanId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSFieldDeiEnabled"),
        ("HUAWEI-XQoS-MIB", "hwXQoSFieldDeiRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSFieldDeiGroup.setStatus("current")

hwXQoSPicForwardingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 36)
)
hwXQoSPicForwardingGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPicForwardingInterface"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPicForwarding8021pValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPicForwardingPriority"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPicForwardingRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSPicForwardingGroup.setStatus("current")

hwXQoSCarTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 37)
)
hwXQoSCarTableGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCarInterfaceIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarDirection"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarVlanID"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarCirValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarPirValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarCbsValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarPbsValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarGreenAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarGreenServiceClass"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarGreenColor"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarYellowAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarYellowServiceClass"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarYellowColor"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarRedAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarRedServiceClass"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarRedColor"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSCarTableGroup.setStatus("current")

hwXQoSPortShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 38)
)
hwXQoSPortShapingGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPortShapingInterface"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortShapingValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortShapingPbsValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortShapingRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSPortShapingGroup.setStatus("current")

hwXQoSQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 39)
)
hwXQoSQueueGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSQueueInterfaceIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueServiceClass"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueCirValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueCirPercentage"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueDirection"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSQueueGroup.setStatus("current")

hwXQoSCarStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 40)
)
hwXQoSCarStatisticsGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsInterfaceIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsDirection"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsVlanid"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsSlotNumber"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsReset"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsPassPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsPassBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsDropPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsDropBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsPassPacketsRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsPassBytesRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsDropPacketsRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCarStatisticsDropBytesRate"))
)
if mibBuilder.loadTexts:
    hwXQoSCarStatisticsGroup.setStatus("current")

hwXQoSCpRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 41)
)
hwXQoSCpRateLimitGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitPeVidValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitCeVidBegin"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitCeVidEnd"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitType"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitIgmpCir"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitIgmpCbs"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSCpRateLimitGroup.setStatus("current")

hwXQoSPortQueueStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 42)
)
hwXQoSPortQueueStatisticsGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsInterfaceIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDirection"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsQueueIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsReset"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsTotalPassPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsTotalPassBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsTotalDiscardPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsTotalDiscardBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDropTailDiscardPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDropTailDiscardBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsWredDiscardPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsWredDiscardBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsPassPacketsRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsPassBytesRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDiscardPacketsRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDiscardBytesRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDropTailDiscardPacketsRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsDropTailDiscardBytesRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsWredDiscardPacketsRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueStatisticsWredDiscardBytesRate"))
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueStatisticsGroup.setStatus("current")

hwXQoSPortStatisticsDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 43)
)
hwXQoSPortStatisticsDropGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPortStatisticsDropPacketsCount"),
        ("HUAWEI-XQoS-MIB", "hwXQosPortStatisticsDropReset"),
        ("HUAWEI-XQoS-MIB", "hwXQosPortStatisticsDropResetTime"))
)
if mibBuilder.loadTexts:
    hwXQoSPortStatisticsDropGroup.setStatus("current")

hwXQoSQueueStatisticsDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 44)
)
hwXQoSQueueStatisticsDropGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSQueueStatisticsDropPacketsCount"),
        ("HUAWEI-XQoS-MIB", "hwXQosQueueStatisticsDropReset"),
        ("HUAWEI-XQoS-MIB", "hwXQosQueueStatisticsDropResetTime"))
)
if mibBuilder.loadTexts:
    hwXQoSQueueStatisticsDropGroup.setStatus("current")

hwXQoSIfScheduleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 45)
)
hwXQoSIfScheduleGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIfScheduleProfile"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIfScheduleRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSIfScheduleGroup.setStatus("current")

hwXQoSScheduleProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 46)
)
hwXQoSScheduleProfileGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueMode"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueBeWeight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueAf1Weight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueAf2Weight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueAf3Weight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueAf4Weight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueCs6Weight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueCs7Weight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleQueueEfWeight"),
        ("HUAWEI-XQoS-MIB", "hwXQoSScheduleProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwXQoSScheduleProfileGroup.setStatus("current")

hwXQoSQppbPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 47)
)
hwXQoSQppbPolicyGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyStatisticsInterfaceIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyDirection"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyLocalID"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyStatisticsReset"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyMatchedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyMatchedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyPassedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyPassedBytes"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyDropedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQppbPolicyDropedBytes"))
)
if mibBuilder.loadTexts:
    hwXQoSQppbPolicyGroup.setStatus("current")

hwXQoSStatResouceNotEnoughAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 48)
)
hwXQoSStatResouceNotEnoughAlarmGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSStatResouceNotEnoughSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStatResouceNotEnoughStatType"))
)
if mibBuilder.loadTexts:
    hwXQoSStatResouceNotEnoughAlarmGroup.setStatus("current")

hwXQoSCARResouceNotEnoughAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 49)
)
hwXQoSCARResouceNotEnoughAlarmGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCARResouceNotEnoughSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCARResouceNotEnoughCARType"))
)
if mibBuilder.loadTexts:
    hwXQoSCARResouceNotEnoughAlarmGroup.setStatus("current")


# Notification objects

hwXQoSCpDefendDiscardedRateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 1)
)
hwXQoSCpDefendDiscardedRateAlarm.setObjects(
    ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedPacketRate")
)
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedRateAlarm.setStatus(
        "current"
    )

hwXQoSQueueDiscardThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 2)
)
hwXQoSQueueDiscardThresholdTrap.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSFrameId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSTrapIfName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSTrapQueueId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSTrapDiscardPackets"))
)
if mibBuilder.loadTexts:
    hwXQoSQueueDiscardThresholdTrap.setStatus(
        "current"
    )

hwXQoSCpDefendDiscardedPacketAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 3)
)
hwXQoSCpDefendDiscardedPacketAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpDefendSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendObjectIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedThreshold"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendChassisID"))
)
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedPacketAlarm.setStatus(
        "current"
    )

hwXQoSCpDefendDiscardedPacketAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 4)
)
hwXQoSCpDefendDiscardedPacketAlarmClear.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpDefendSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendObjectIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedPackets"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedThreshold"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendChassisID"))
)
if mibBuilder.loadTexts:
    hwXQoSCpDefendDiscardedPacketAlarmClear.setStatus(
        "current"
    )

hwXQoSCprlDiscardedPacketAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 5)
)
hwXQoSCprlDiscardedPacketAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitPeVidValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitCeVidBegin"))
)
if mibBuilder.loadTexts:
    hwXQoSCprlDiscardedPacketAlarm.setStatus(
        "current"
    )

hwXQoSCprlDiscardedPacketAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 6)
)
hwXQoSCprlDiscardedPacketAlarmClear.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitPeVidValue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpRateLimitCeVidBegin"))
)
if mibBuilder.loadTexts:
    hwXQoSCprlDiscardedPacketAlarmClear.setStatus(
        "current"
    )

hwXQoSRedirectNextHopChangedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 7)
)
hwXQoSRedirectNextHopChangedAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopBehaviorName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopOldIp"),
        ("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopNewIp"))
)
if mibBuilder.loadTexts:
    hwXQoSRedirectNextHopChangedAlarm.setStatus(
        "current"
    )

hwXQoSIrsmDelayAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 8)
)
hwXQoSIrsmDelayAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIrsmSourceAddress"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmGroupAddress"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmTime"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmDelay"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmThreshold"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmUpstream"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmLocal"))
)
if mibBuilder.loadTexts:
    hwXQoSIrsmDelayAlarm.setStatus(
        "current"
    )

hwXQoSIrsmDropPacketAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 9)
)
hwXQoSIrsmDropPacketAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIrsmSourceAddress"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmGroupAddress"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmTime"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmTotalPacket"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmDropPacket"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmUpstream"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmLocal"))
)
if mibBuilder.loadTexts:
    hwXQoSIrsmDropPacketAlarm.setStatus(
        "current"
    )

hwXQoSIrsmSynFrameDropAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 10)
)
hwXQoSIrsmSynFrameDropAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSIrsmSourceAddress"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmGroupAddress"),
        ("HUAWEI-XQoS-MIB", "hwXQoSIrsmTime"))
)
if mibBuilder.loadTexts:
    hwXQoSIrsmSynFrameDropAlarm.setStatus(
        "current"
    )

hwXQoSRuleFaileAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 11)
)
hwXQoSRuleFaileAlarm.setObjects(
    ("HUAWEI-XQoS-MIB", "hwXQoSRuleFailInfo")
)
if mibBuilder.loadTexts:
    hwXQoSRuleFaileAlarm.setStatus(
        "current"
    )

hwXQoSProfileUsedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 12)
)
hwXQoSProfileUsedAlarm.setObjects(
    ("HUAWEI-XQoS-MIB", "hwXQoSProfileName")
)
if mibBuilder.loadTexts:
    hwXQoSProfileUsedAlarm.setStatus(
        "current"
    )

hwXQoSPortQueueAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 13)
)
hwXQoSPortQueueAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmQueue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmTrunkIndex"))
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarm.setStatus(
        "current"
    )

hwXQoSPortQueueAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 14)
)
hwXQoSPortQueueAlarmClear.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmIfIndex"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmQueue"),
        ("HUAWEI-XQoS-MIB", "hwXQoSPortQueueAlarmTrunkIndex"))
)
if mibBuilder.loadTexts:
    hwXQoSPortQueueAlarmClear.setStatus(
        "current"
    )

hwXQoSSecurityStormControlInterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 15)
)
hwXQoSSecurityStormControlInterfaceTrap.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSSecurityStormControlInterfaceChassisId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSSecurityStormControlInterfaceSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSSecurityStormControlInterfaceName"),
        ("HUAWEI-XQoS-MIB", "hwXQoSSecurityStormControlInterfaceVlan"))
)
if mibBuilder.loadTexts:
    hwXQoSSecurityStormControlInterfaceTrap.setStatus(
        "current"
    )

hwXQoSStatResouceNotEnoughAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 16)
)
hwXQoSStatResouceNotEnoughAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSStatResouceNotEnoughSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStatResouceNotEnoughStatType"))
)
if mibBuilder.loadTexts:
    hwXQoSStatResouceNotEnoughAlarm.setStatus(
        "current"
    )

hwXQoSCARResouceNotEnoughAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 11, 17)
)
hwXQoSCARResouceNotEnoughAlarm.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCARResouceNotEnoughSlotId"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCARResouceNotEnoughCARType"))
)
if mibBuilder.loadTexts:
    hwXQoSCARResouceNotEnoughAlarm.setStatus(
        "current"
    )

hwXQoSStormControlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 1, 14, 1)
)
hwXQoSStormControlTrap.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSStormControlBroadcastMinRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlBroadcastMaxRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlMulticastMinRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlMulticastMaxRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlAction"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlInterval"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlStatus"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlUnicastMinRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlUnicastMaxRate"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlBcMode"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlMcMode"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlUcMode"))
)
if mibBuilder.loadTexts:
    hwXQoSStormControlTrap.setStatus(
        "current"
    )


# Notifications groups

hwNotificationExtGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 2, 4)
)
hwNotificationExtGroup.setObjects(
      *(("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedRateAlarm"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCpDefendDiscardedPacketAlarm"),
        ("HUAWEI-XQoS-MIB", "hwXQoSQueueDiscardThresholdTrap"),
        ("HUAWEI-XQoS-MIB", "hwXQoSStormControlTrap"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCprlDiscardedPacketAlarm"),
        ("HUAWEI-XQoS-MIB", "hwXQoSCprlDiscardedPacketAlarmClear"),
        ("HUAWEI-XQoS-MIB", "hwXQoSRedirectNextHopChangedAlarm"))
)
if mibBuilder.loadTexts:
    hwNotificationExtGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwXQoSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwXQoSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-XQoS-MIB",
    **{"BaType": BaType,
       "XQosQueueType": XQosQueueType,
       "ResetFlag": ResetFlag,
       "CosType": CosType,
       "CarAction": CarAction,
       "DirectionType": DirectionType,
       "UrpfCtrlType": UrpfCtrlType,
       "SampleType": SampleType,
       "IPCARRuleType": IPCARRuleType,
       "hwQoS": hwQoS,
       "hwXQoSMIB": hwXQoSMIB,
       "hwXQoSObjects": hwXQoSObjects,
       "hwXQoSBaObjects": hwXQoSBaObjects,
       "hwXQoSBaCfgInfoTable": hwXQoSBaCfgInfoTable,
       "hwXQoSBaCfgInfoEntry": hwXQoSBaCfgInfoEntry,
       "hwXQoSBaIndex": hwXQoSBaIndex,
       "hwXQoSBaName": hwXQoSBaName,
       "hwXQoSBaRowStatus": hwXQoSBaRowStatus,
       "hwXQoSBa8021pPhbCfgInfoTable": hwXQoSBa8021pPhbCfgInfoTable,
       "hwXQoSBa8021pPhbCfgInfoEntry": hwXQoSBa8021pPhbCfgInfoEntry,
       "hwXQoSBa8021pPhbIndex": hwXQoSBa8021pPhbIndex,
       "hwXQoSBa8021pPhbPri": hwXQoSBa8021pPhbPri,
       "hwXQoSBa8021pPhbCos": hwXQoSBa8021pPhbCos,
       "hwXQoSBa8021pPhbColour": hwXQoSBa8021pPhbColour,
       "hwXQoSBa8021pPhbRowStatus": hwXQoSBa8021pPhbRowStatus,
       "hwXQoSBa8021pMapCfgInfoTable": hwXQoSBa8021pMapCfgInfoTable,
       "hwXQoSBa8021pMapCfgInfoEntry": hwXQoSBa8021pMapCfgInfoEntry,
       "hwXQoSBa8021pMapIndex": hwXQoSBa8021pMapIndex,
       "hwXQoSBa8021pMapCos": hwXQoSBa8021pMapCos,
       "hwXQoSBa8021pMapColour": hwXQoSBa8021pMapColour,
       "hwXQoSBa8021pMapPri": hwXQoSBa8021pMapPri,
       "hwXQoSBa8021pMapRowStatus": hwXQoSBa8021pMapRowStatus,
       "hwXQoSBaDscpPhbCfgInfoTable": hwXQoSBaDscpPhbCfgInfoTable,
       "hwXQoSBaDscpPhbCfgInfoEntry": hwXQoSBaDscpPhbCfgInfoEntry,
       "hwXQoSBaDscpPhbIndex": hwXQoSBaDscpPhbIndex,
       "hwXQoSBaDscpPhbPri": hwXQoSBaDscpPhbPri,
       "hwXQoSBaDscpPhbCos": hwXQoSBaDscpPhbCos,
       "hwXQoSBaDscpPhbColour": hwXQoSBaDscpPhbColour,
       "hwXQoSBaDscpPhbRowStatus": hwXQoSBaDscpPhbRowStatus,
       "hwXQoSBaDscpMapCfgInfoTable": hwXQoSBaDscpMapCfgInfoTable,
       "hwXQoSBaDscpMapCfgInfoEntry": hwXQoSBaDscpMapCfgInfoEntry,
       "hwXQoSBaDscpMapIndex": hwXQoSBaDscpMapIndex,
       "hwXQoSBaDscpMapCos": hwXQoSBaDscpMapCos,
       "hwXQoSBaDscpMapColour": hwXQoSBaDscpMapColour,
       "hwXQoSBaDscpMapPri": hwXQoSBaDscpMapPri,
       "hwXQoSBaDscpMapRowStatus": hwXQoSBaDscpMapRowStatus,
       "hwXQoSBaExpPhbCfgInfoTable": hwXQoSBaExpPhbCfgInfoTable,
       "hwXQoSBaExpPhbCfgInfoEntry": hwXQoSBaExpPhbCfgInfoEntry,
       "hwXQoSBaExpPhbIndex": hwXQoSBaExpPhbIndex,
       "hwXQoSBaExpPhbPri": hwXQoSBaExpPhbPri,
       "hwXQoSBaExpPhbCos": hwXQoSBaExpPhbCos,
       "hwXQoSBaExpPhbColour": hwXQoSBaExpPhbColour,
       "hwXQoSBaExpPhbRowStatus": hwXQoSBaExpPhbRowStatus,
       "hwXQoSBaExpMapCfgInfoTable": hwXQoSBaExpMapCfgInfoTable,
       "hwXQoSBaExpMapCfgInfoEntry": hwXQoSBaExpMapCfgInfoEntry,
       "hwXQoSBaExpMapIndex": hwXQoSBaExpMapIndex,
       "hwXQoSBaExpMapCos": hwXQoSBaExpMapCos,
       "hwXQoSBaExpMapColour": hwXQoSBaExpMapColour,
       "hwXQoSBaExpMapPri": hwXQoSBaExpMapPri,
       "hwXQoSBaExpMapRowStatus": hwXQoSBaExpMapRowStatus,
       "hwXQoSIfDiffDomainTable": hwXQoSIfDiffDomainTable,
       "hwXQoSIfDiffDomainEntry": hwXQoSIfDiffDomainEntry,
       "hwXQoSIfDiffDomainIfIndex": hwXQoSIfDiffDomainIfIndex,
       "hwXQoSIfDiffDomainVlanId": hwXQoSIfDiffDomainVlanId,
       "hwXQoSIfDiffDomainName": hwXQoSIfDiffDomainName,
       "hwXQoSIfDiffDomainRowStatus": hwXQoSIfDiffDomainRowStatus,
       "hwXQoSIfDiffDomainVlanId2": hwXQoSIfDiffDomainVlanId2,
       "hwXQoSIfTrust8021pTable": hwXQoSIfTrust8021pTable,
       "hwXQoSIfTrust8021pEntry": hwXQoSIfTrust8021pEntry,
       "hwXQoSIfTrust8021pIfIndex": hwXQoSIfTrust8021pIfIndex,
       "hwXQoSIfTrust8021pVlanID": hwXQoSIfTrust8021pVlanID,
       "hwXQoSIfTrust8021pAction": hwXQoSIfTrust8021pAction,
       "hwXQoSIfTrust8021pRowStatus": hwXQoSIfTrust8021pRowStatus,
       "hwXQoSBaAtmQosPhbCfgInfoTable": hwXQoSBaAtmQosPhbCfgInfoTable,
       "hwXQoSBaAtmQosPhbCfgInfoEntry": hwXQoSBaAtmQosPhbCfgInfoEntry,
       "hwXQoSBaAtmQosPhbServType": hwXQoSBaAtmQosPhbServType,
       "hwXQoSBaAtmQosPhbClp": hwXQoSBaAtmQosPhbClp,
       "hwXQoSBaAtmQosPhbCos": hwXQoSBaAtmQosPhbCos,
       "hwXQoSBaAtmQosPhbColour": hwXQoSBaAtmQosPhbColour,
       "hwXQoSBaAtmQosPhbRowStatus": hwXQoSBaAtmQosPhbRowStatus,
       "hwXQoSBaAtmQosMapCfgInfoTable": hwXQoSBaAtmQosMapCfgInfoTable,
       "hwXQoSBaAtmQosMapCfgInfoEntry": hwXQoSBaAtmQosMapCfgInfoEntry,
       "hwXQoSBaAtmQosMapIndex": hwXQoSBaAtmQosMapIndex,
       "hwXQoSBaAtmQosMapCos": hwXQoSBaAtmQosMapCos,
       "hwXQoSBaAtmQosMapColour": hwXQoSBaAtmQosMapColour,
       "hwXQoSBaAtmQosMapClp": hwXQoSBaAtmQosMapClp,
       "hwXQoSBaAtmQosMapRowStatus": hwXQoSBaAtmQosMapRowStatus,
       "hwXQoSAtmPvcDiffDomainTable": hwXQoSAtmPvcDiffDomainTable,
       "hwXQoSAtmPvcDiffDomainEntry": hwXQoSAtmPvcDiffDomainEntry,
       "hwXQoSAtmPvcDiffDomainIfIndex": hwXQoSAtmPvcDiffDomainIfIndex,
       "hwXQoSAtmPvcVpi": hwXQoSAtmPvcVpi,
       "hwXQoSAtmPvcVci": hwXQoSAtmPvcVci,
       "hwXQoSAtmPvcDiffDomainName": hwXQoSAtmPvcDiffDomainName,
       "hwXQoSAtmPvcDiffDomainRowStatus": hwXQoSAtmPvcDiffDomainRowStatus,
       "hwXQoSAtmPvpDiffDomainTable": hwXQoSAtmPvpDiffDomainTable,
       "hwXQoSAtmPvpDiffDomainEntry": hwXQoSAtmPvpDiffDomainEntry,
       "hwXQoSAtmPvpDiffDomainIfIndex": hwXQoSAtmPvpDiffDomainIfIndex,
       "hwXQoSAtmPvpVpi": hwXQoSAtmPvpVpi,
       "hwXQoSAtmPvpDiffDomainName": hwXQoSAtmPvpDiffDomainName,
       "hwXQoSAtmPvpDiffDomainRowStatus": hwXQoSAtmPvpDiffDomainRowStatus,
       "hwXQoSBaPhbCfgInfoTable": hwXQoSBaPhbCfgInfoTable,
       "hwXQoSBaPhbCfgInfoEntry": hwXQoSBaPhbCfgInfoEntry,
       "hwXQoSBaPhbType": hwXQoSBaPhbType,
       "hwXQoSBaPhbPri": hwXQoSBaPhbPri,
       "hwXQoSBaPhbCos": hwXQoSBaPhbCos,
       "hwXQoSBaPhbColour": hwXQoSBaPhbColour,
       "hwXQoSBaPhbRowStatus": hwXQoSBaPhbRowStatus,
       "hwXQoSBaMapCfgInfoTable": hwXQoSBaMapCfgInfoTable,
       "hwXQoSBaMapCfgInfoEntry": hwXQoSBaMapCfgInfoEntry,
       "hwXQoSBaMapType": hwXQoSBaMapType,
       "hwXQoSBaMapCos": hwXQoSBaMapCos,
       "hwXQoSBaMapColour": hwXQoSBaMapColour,
       "hwXQoSBaMapPri": hwXQoSBaMapPri,
       "hwXQoSBaMapRowStatus": hwXQoSBaMapRowStatus,
       "hwXQoSIfTrustTable": hwXQoSIfTrustTable,
       "hwXQoSIfTrustEntry": hwXQoSIfTrustEntry,
       "hwXQoSIfTrustIfIndex": hwXQoSIfTrustIfIndex,
       "hwXQoSIfTrustVlanID1": hwXQoSIfTrustVlanID1,
       "hwXQoSIfTrustVlanID2": hwXQoSIfTrustVlanID2,
       "hwXQoSBaType": hwXQoSBaType,
       "hwXQoSIfTrustAction": hwXQoSIfTrustAction,
       "hwXQoSIfTrustRowStatus": hwXQoSIfTrustRowStatus,
       "hwXQoSDeiTable": hwXQoSDeiTable,
       "hwXQoSDeiEntry": hwXQoSDeiEntry,
       "hwXQoSDeiIfIndex": hwXQoSDeiIfIndex,
       "hwXQoSDeiVlanID1": hwXQoSDeiVlanID1,
       "hwXQoSDeiVlanID2": hwXQoSDeiVlanID2,
       "hwXQoSIfEnableDeiAction": hwXQoSIfEnableDeiAction,
       "hwXQoSDeiRowStatus": hwXQoSDeiRowStatus,
       "hwXQoSRemarkTable": hwXQoSRemarkTable,
       "hwXQoSRemarkEntry": hwXQoSRemarkEntry,
       "hwXQoSRemarkIfIndex": hwXQoSRemarkIfIndex,
       "hwXQoSRemarkVlanID1": hwXQoSRemarkVlanID1,
       "hwXQoSRemarkVlanID2": hwXQoSRemarkVlanID2,
       "hwXQoSIfEnableRemarkAction": hwXQoSIfEnableRemarkAction,
       "hwXQoSRemarkRowStatus": hwXQoSRemarkRowStatus,
       "hwXQoSPhbEnableTable": hwXQoSPhbEnableTable,
       "hwXQoSPhbEnableEntry": hwXQoSPhbEnableEntry,
       "hwXQoSPhbEnableIfIndex": hwXQoSPhbEnableIfIndex,
       "hwXQoSPhbEnableVlanID1": hwXQoSPhbEnableVlanID1,
       "hwXQoSPhbEnableVlanID2": hwXQoSPhbEnableVlanID2,
       "hwXQoSPhbEnableRowStatus": hwXQoSPhbEnableRowStatus,
       "hwXQoSCommonInboundTable": hwXQoSCommonInboundTable,
       "hwXQoSCommonInboundEntry": hwXQoSCommonInboundEntry,
       "hwXQoSCommonInboundPhbIndex": hwXQoSCommonInboundPhbIndex,
       "hwXQoSCommonInboundPhbCos": hwXQoSCommonInboundPhbCos,
       "hwXQoSCommonInboundPhbColor": hwXQoSCommonInboundPhbColor,
       "hwXQoSCommonInboundPhbPri": hwXQoSCommonInboundPhbPri,
       "hwXQoSCommonInboundRowStatus": hwXQoSCommonInboundRowStatus,
       "hwXQoSPppInboundTable": hwXQoSPppInboundTable,
       "hwXQoSPppInboundEntry": hwXQoSPppInboundEntry,
       "hwXQoSPppInboundCos": hwXQoSPppInboundCos,
       "hwXQoSPppInboundColor": hwXQoSPppInboundColor,
       "hwXQoSPppInboundRowStatus": hwXQoSPppInboundRowStatus,
       "hwXQoSServiceclassTable": hwXQoSServiceclassTable,
       "hwXQoSServiceclassEntry": hwXQoSServiceclassEntry,
       "hwXQoSServiceclassPort": hwXQoSServiceclassPort,
       "hwXQoSServiceclass": hwXQoSServiceclass,
       "hwXQoSServiceclassRowStatus": hwXQoSServiceclassRowStatus,
       "hwXQoSPhbTable": hwXQoSPhbTable,
       "hwXQoSPhbEntry": hwXQoSPhbEntry,
       "hwXQoSPhbPort": hwXQoSPhbPort,
       "hwXQoSPhbEnable": hwXQoSPhbEnable,
       "hwXQoSPhbRowStatus": hwXQoSPhbRowStatus,
       "hwXQoSFieldDeiTable": hwXQoSFieldDeiTable,
       "hwXQoSFieldDeiEntry": hwXQoSFieldDeiEntry,
       "hwXQoSFieldDeiInterface": hwXQoSFieldDeiInterface,
       "hwXQoSFieldDeiVlanId": hwXQoSFieldDeiVlanId,
       "hwXQoSFieldDeiEnabled": hwXQoSFieldDeiEnabled,
       "hwXQoSFieldDeiRowStatus": hwXQoSFieldDeiRowStatus,
       "hwXQoSPicForwardingTable": hwXQoSPicForwardingTable,
       "hwXQoSPicForwardingEntry": hwXQoSPicForwardingEntry,
       "hwXQoSPicForwardingInterface": hwXQoSPicForwardingInterface,
       "hwXQoSPicForwarding8021pValue": hwXQoSPicForwarding8021pValue,
       "hwXQoSPicForwardingPriority": hwXQoSPicForwardingPriority,
       "hwXQoSPicForwardingRowStatus": hwXQoSPicForwardingRowStatus,
       "hwXQoSCarTable": hwXQoSCarTable,
       "hwXQoSCarEntry": hwXQoSCarEntry,
       "hwXQoSCarInterfaceIndex": hwXQoSCarInterfaceIndex,
       "hwXQoSCarDirection": hwXQoSCarDirection,
       "hwXQoSCarVlanID": hwXQoSCarVlanID,
       "hwXQoSCarCirValue": hwXQoSCarCirValue,
       "hwXQoSCarPirValue": hwXQoSCarPirValue,
       "hwXQoSCarCbsValue": hwXQoSCarCbsValue,
       "hwXQoSCarPbsValue": hwXQoSCarPbsValue,
       "hwXQoSCarGreenAction": hwXQoSCarGreenAction,
       "hwXQoSCarGreenServiceClass": hwXQoSCarGreenServiceClass,
       "hwXQoSCarGreenColor": hwXQoSCarGreenColor,
       "hwXQoSCarYellowAction": hwXQoSCarYellowAction,
       "hwXQoSCarYellowServiceClass": hwXQoSCarYellowServiceClass,
       "hwXQoSCarYellowColor": hwXQoSCarYellowColor,
       "hwXQoSCarRedAction": hwXQoSCarRedAction,
       "hwXQoSCarRedServiceClass": hwXQoSCarRedServiceClass,
       "hwXQoSCarRedColor": hwXQoSCarRedColor,
       "hwXQoSCarRowStatus": hwXQoSCarRowStatus,
       "hwXQoSPortShapingTable": hwXQoSPortShapingTable,
       "hwXQoSPortShapingEntry": hwXQoSPortShapingEntry,
       "hwXQoSPortShapingInterface": hwXQoSPortShapingInterface,
       "hwXQoSPortShapingValue": hwXQoSPortShapingValue,
       "hwXQoSPortShapingPbsValue": hwXQoSPortShapingPbsValue,
       "hwXQoSPortShapingRowStatus": hwXQoSPortShapingRowStatus,
       "hwXQoSQueueTable": hwXQoSQueueTable,
       "hwXQoSQueueEntry": hwXQoSQueueEntry,
       "hwXQoSQueueInterfaceIndex": hwXQoSQueueInterfaceIndex,
       "hwXQoSQueueServiceClass": hwXQoSQueueServiceClass,
       "hwXQoSQueueCirValue": hwXQoSQueueCirValue,
       "hwXQoSQueueCirPercentage": hwXQoSQueueCirPercentage,
       "hwXQoSQueueDirection": hwXQoSQueueDirection,
       "hwXQoSQueueRowStatus": hwXQoSQueueRowStatus,
       "hwXQoSCarStatisticsTable": hwXQoSCarStatisticsTable,
       "hwXQoSCarStatisticsEntry": hwXQoSCarStatisticsEntry,
       "hwXQoSCarStatisticsInterfaceIndex": hwXQoSCarStatisticsInterfaceIndex,
       "hwXQoSCarStatisticsDirection": hwXQoSCarStatisticsDirection,
       "hwXQoSCarStatisticsVlanid": hwXQoSCarStatisticsVlanid,
       "hwXQoSCarStatisticsSlotNumber": hwXQoSCarStatisticsSlotNumber,
       "hwXQoSCarStatisticsReset": hwXQoSCarStatisticsReset,
       "hwXQoSCarStatisticsPassPackets": hwXQoSCarStatisticsPassPackets,
       "hwXQoSCarStatisticsPassBytes": hwXQoSCarStatisticsPassBytes,
       "hwXQoSCarStatisticsDropPackets": hwXQoSCarStatisticsDropPackets,
       "hwXQoSCarStatisticsDropBytes": hwXQoSCarStatisticsDropBytes,
       "hwXQoSCarStatisticsPassPacketsRate": hwXQoSCarStatisticsPassPacketsRate,
       "hwXQoSCarStatisticsPassBytesRate": hwXQoSCarStatisticsPassBytesRate,
       "hwXQoSCarStatisticsDropPacketsRate": hwXQoSCarStatisticsDropPacketsRate,
       "hwXQoSCarStatisticsDropBytesRate": hwXQoSCarStatisticsDropBytesRate,
       "hwXQoSCpRateLimitTable": hwXQoSCpRateLimitTable,
       "hwXQoSCpRateLimitEntry": hwXQoSCpRateLimitEntry,
       "hwXQoSCpRateLimitIfIndex": hwXQoSCpRateLimitIfIndex,
       "hwXQoSCpRateLimitPeVidValue": hwXQoSCpRateLimitPeVidValue,
       "hwXQoSCpRateLimitCeVidBegin": hwXQoSCpRateLimitCeVidBegin,
       "hwXQoSCpRateLimitCeVidEnd": hwXQoSCpRateLimitCeVidEnd,
       "hwXQoSCpRateLimitType": hwXQoSCpRateLimitType,
       "hwXQoSCpRateLimitIgmpCir": hwXQoSCpRateLimitIgmpCir,
       "hwXQoSCpRateLimitIgmpCbs": hwXQoSCpRateLimitIgmpCbs,
       "hwXQoSCpRateLimitRowStatus": hwXQoSCpRateLimitRowStatus,
       "hwXQoSPortQueueStatisticsTable": hwXQoSPortQueueStatisticsTable,
       "hwXQoSPortQueueStatisticsEntry": hwXQoSPortQueueStatisticsEntry,
       "hwXQoSPortQueueStatisticsInterfaceIndex": hwXQoSPortQueueStatisticsInterfaceIndex,
       "hwXQoSPortQueueStatisticsDirection": hwXQoSPortQueueStatisticsDirection,
       "hwXQoSPortQueueStatisticsQueueIndex": hwXQoSPortQueueStatisticsQueueIndex,
       "hwXQoSPortQueueStatisticsReset": hwXQoSPortQueueStatisticsReset,
       "hwXQoSPortQueueStatisticsTotalPassPackets": hwXQoSPortQueueStatisticsTotalPassPackets,
       "hwXQoSPortQueueStatisticsTotalPassBytes": hwXQoSPortQueueStatisticsTotalPassBytes,
       "hwXQoSPortQueueStatisticsTotalDiscardPackets": hwXQoSPortQueueStatisticsTotalDiscardPackets,
       "hwXQoSPortQueueStatisticsTotalDiscardBytes": hwXQoSPortQueueStatisticsTotalDiscardBytes,
       "hwXQoSPortQueueStatisticsDropTailDiscardPackets": hwXQoSPortQueueStatisticsDropTailDiscardPackets,
       "hwXQoSPortQueueStatisticsDropTailDiscardBytes": hwXQoSPortQueueStatisticsDropTailDiscardBytes,
       "hwXQoSPortQueueStatisticsWredDiscardPackets": hwXQoSPortQueueStatisticsWredDiscardPackets,
       "hwXQoSPortQueueStatisticsWredDiscardBytes": hwXQoSPortQueueStatisticsWredDiscardBytes,
       "hwXQoSPortQueueStatisticsPassPacketsRate": hwXQoSPortQueueStatisticsPassPacketsRate,
       "hwXQoSPortQueueStatisticsPassBytesRate": hwXQoSPortQueueStatisticsPassBytesRate,
       "hwXQoSPortQueueStatisticsDiscardPacketsRate": hwXQoSPortQueueStatisticsDiscardPacketsRate,
       "hwXQoSPortQueueStatisticsDiscardBytesRate": hwXQoSPortQueueStatisticsDiscardBytesRate,
       "hwXQoSPortQueueStatisticsDropTailDiscardPacketsRate": hwXQoSPortQueueStatisticsDropTailDiscardPacketsRate,
       "hwXQoSPortQueueStatisticsDropTailDiscardBytesRate": hwXQoSPortQueueStatisticsDropTailDiscardBytesRate,
       "hwXQoSPortQueueStatisticsWredDiscardPacketsRate": hwXQoSPortQueueStatisticsWredDiscardPacketsRate,
       "hwXQoSPortQueueStatisticsWredDiscardBytesRate": hwXQoSPortQueueStatisticsWredDiscardBytesRate,
       "hwXQoSMulBa8021pPhbCfgInfoTable": hwXQoSMulBa8021pPhbCfgInfoTable,
       "hwXQoSMulBa8021pPhbCfgInfoEntry": hwXQoSMulBa8021pPhbCfgInfoEntry,
       "hwXQoSMulBa8021pPhbIndex": hwXQoSMulBa8021pPhbIndex,
       "hwXQoSMulBa8021pPri": hwXQoSMulBa8021pPri,
       "hwXQoSMulBa8021pPhbCos": hwXQoSMulBa8021pPhbCos,
       "hwXQoSMulBa8021pPhbRowStatus": hwXQoSMulBa8021pPhbRowStatus,
       "hwXQoSMulDscpPhbCfgInfoTable": hwXQoSMulDscpPhbCfgInfoTable,
       "hwXQoSMulDscpPhbCfgInfoEntry": hwXQoSMulDscpPhbCfgInfoEntry,
       "hwXQoSMulBaDscpPhbIndex": hwXQoSMulBaDscpPhbIndex,
       "hwXQoSMulBaDscpPri": hwXQoSMulBaDscpPri,
       "hwXQoSMulBaDscpPhbCos": hwXQoSMulBaDscpPhbCos,
       "hwXQoSMulBaDscpPhbRowStatus": hwXQoSMulBaDscpPhbRowStatus,
       "hwXQoSBaUserPriPhbCfgInfoTable": hwXQoSBaUserPriPhbCfgInfoTable,
       "hwXQoSBaUserPriPhbCfgInfoEntry": hwXQoSBaUserPriPhbCfgInfoEntry,
       "hwXQoSDSUserPriIndex": hwXQoSDSUserPriIndex,
       "hwXQoSUserPriPhbPri": hwXQoSUserPriPhbPri,
       "hwXQoSUserPriPhbCos": hwXQoSUserPriPhbCos,
       "hwXQoSUserPriPhbColour": hwXQoSUserPriPhbColour,
       "hwXQoSUserPriPhbRowStatus": hwXQoSUserPriPhbRowStatus,
       "hwXQoSAAATrustCfgInfoTable": hwXQoSAAATrustCfgInfoTable,
       "hwXQoSAAATrustCfgInfoEntry": hwXQoSAAATrustCfgInfoEntry,
       "hwXQoSAaaDomainName": hwXQoSAaaDomainName,
       "hwXQoSAAADsDomainName": hwXQoSAAADsDomainName,
       "hwXQoSAAADsRowStatus": hwXQoSAAADsRowStatus,
       "hwXQoSAAATrust8021pInfoTable": hwXQoSAAATrust8021pInfoTable,
       "hwXQoSAAATrust8021pInfoEntry": hwXQoSAAATrust8021pInfoEntry,
       "hwXQoSAAADs8021P": hwXQoSAAADs8021P,
       "hwXQoSAAADs8021pRowStatus": hwXQoSAAADs8021pRowStatus,
       "hwXQoSQppbPolicyStatisticsTable": hwXQoSQppbPolicyStatisticsTable,
       "hwXQoSQppbPolicyStatisticsEntry": hwXQoSQppbPolicyStatisticsEntry,
       "hwXQoSQppbPolicyLocalID": hwXQoSQppbPolicyLocalID,
       "hwXQoSQppbPolicyDirection": hwXQoSQppbPolicyDirection,
       "hwXQoSQppbPolicyStatisticsInterfaceIndex": hwXQoSQppbPolicyStatisticsInterfaceIndex,
       "hwXQoSQppbPolicyStatisticsReset": hwXQoSQppbPolicyStatisticsReset,
       "hwXQoSQppbPolicyMatchedPackets": hwXQoSQppbPolicyMatchedPackets,
       "hwXQoSQppbPolicyMatchedBytes": hwXQoSQppbPolicyMatchedBytes,
       "hwXQoSQppbPolicyPassedPackets": hwXQoSQppbPolicyPassedPackets,
       "hwXQoSQppbPolicyPassedBytes": hwXQoSQppbPolicyPassedBytes,
       "hwXQoSQppbPolicyDropedPackets": hwXQoSQppbPolicyDropedPackets,
       "hwXQoSQppbPolicyDropedBytes": hwXQoSQppbPolicyDropedBytes,
       "hwXQoSQppbPolicyMatchPacketsRate": hwXQoSQppbPolicyMatchPacketsRate,
       "hwXQoSQppbPolicyMatchBytesRate": hwXQoSQppbPolicyMatchBytesRate,
       "hwXQoSIfPhbEnableTable": hwXQoSIfPhbEnableTable,
       "hwXQoSIfPhbEnableEntry": hwXQoSIfPhbEnableEntry,
       "hwXQoSIfPhbEnableIfIndex": hwXQoSIfPhbEnableIfIndex,
       "hwXQoSIfPhbEnableVlanId": hwXQoSIfPhbEnableVlanId,
       "hwXQoSIfPhbEnableDomainName": hwXQoSIfPhbEnableDomainName,
       "hwXQoSIfPhbEnableRowStatus": hwXQoSIfPhbEnableRowStatus,
       "hwXQoSIfRemarkDscpTable": hwXQoSIfRemarkDscpTable,
       "hwXQoSIfRemarkDscpEntry": hwXQoSIfRemarkDscpEntry,
       "hwXQoSIfRemarkDscpIfIndex": hwXQoSIfRemarkDscpIfIndex,
       "hwXQoSIfRemarkDscpRowStatus": hwXQoSIfRemarkDscpRowStatus,
       "hwXQoSIfActionObjects": hwXQoSIfActionObjects,
       "hwXQoSIfCarCfgInfoTable": hwXQoSIfCarCfgInfoTable,
       "hwXQoSIfCarCfgInfoEntry": hwXQoSIfCarCfgInfoEntry,
       "hwXQoSIfCarCfgIfIndex": hwXQoSIfCarCfgIfIndex,
       "hwXQoSIfCarVlanID": hwXQoSIfCarVlanID,
       "hwXQoSIfCarDirection": hwXQoSIfCarDirection,
       "hwXQoSIfCarCir": hwXQoSIfCarCir,
       "hwXQoSIfCarCbs": hwXQoSIfCarCbs,
       "hwXQoSIfCarEbs": hwXQoSIfCarEbs,
       "hwXQoSIfCarPir": hwXQoSIfCarPir,
       "hwXQoSIfCarPbs": hwXQoSIfCarPbs,
       "hwXQoSIfCarGreenAction": hwXQoSIfCarGreenAction,
       "hwXQoSIfCarGreenRemarkValue": hwXQoSIfCarGreenRemarkValue,
       "hwXQoSIfCarYellowAction": hwXQoSIfCarYellowAction,
       "hwXQoSIfCarYellowRemarkValue": hwXQoSIfCarYellowRemarkValue,
       "hwXQoSIfCarRedAction": hwXQoSIfCarRedAction,
       "hwXQoSIfCarRedRemarkValue": hwXQoSIfCarRedRemarkValue,
       "hwXQoSIfCarRowStatus": hwXQoSIfCarRowStatus,
       "hwXQoSIfMirrorCfgInfoTable": hwXQoSIfMirrorCfgInfoTable,
       "hwXQoSIfMirrorCfgInfoEntry": hwXQoSIfMirrorCfgInfoEntry,
       "hwXQoSIfMirrorCfgIfIndex": hwXQoSIfMirrorCfgIfIndex,
       "hwXQoSIfMirrorCfgVlanID": hwXQoSIfMirrorCfgVlanID,
       "hwXQoSIfMirrorDirection": hwXQoSIfMirrorDirection,
       "hwXQoSIfMirrorObserveIndex": hwXQoSIfMirrorObserveIndex,
       "hwXQoSIfMirrorRowStatus": hwXQoSIfMirrorRowStatus,
       "hwXQoSIfUrpfCfgInfoTable": hwXQoSIfUrpfCfgInfoTable,
       "hwXQoSIfUrpfCfgInfoEntry": hwXQoSIfUrpfCfgInfoEntry,
       "hwXQoSIfUrpfCfgIfIndex": hwXQoSIfUrpfCfgIfIndex,
       "hwXQoSIfUrpfCfgVlanID": hwXQoSIfUrpfCfgVlanID,
       "hwXQoSIfUrpfCtrlType": hwXQoSIfUrpfCtrlType,
       "hwXQoSIfUrpfAllowDefault": hwXQoSIfUrpfAllowDefault,
       "hwXQoSIfUrpfRowStatus": hwXQoSIfUrpfRowStatus,
       "hwXQoSIfSamplingCfgInfoTable": hwXQoSIfSamplingCfgInfoTable,
       "hwXQoSIfSamplingCfgInfoEntry": hwXQoSIfSamplingCfgInfoEntry,
       "hwXQoSIfSamplingIfIndex": hwXQoSIfSamplingIfIndex,
       "hwXQoSIfSamplingVlanID": hwXQoSIfSamplingVlanID,
       "hwXQoSIfSamplingDirection": hwXQoSIfSamplingDirection,
       "hwXQoSIfSamplingType": hwXQoSIfSamplingType,
       "hwXQoSIfSamplingNum": hwXQoSIfSamplingNum,
       "hwXQoSIfSamplingRowStatus": hwXQoSIfSamplingRowStatus,
       "hwXQoSIfLrCfgInfoTable": hwXQoSIfLrCfgInfoTable,
       "hwXQoSIfLrCfgInfoEntry": hwXQoSIfLrCfgInfoEntry,
       "hwXQoSIfLrCfgIfIndex": hwXQoSIfLrCfgIfIndex,
       "hwXQoSIfLrCfgVlanID": hwXQoSIfLrCfgVlanID,
       "hwXQoSIfLrCir": hwXQoSIfLrCir,
       "hwXQoSIfLrRowStatus": hwXQoSIfLrRowStatus,
       "hwXQoSIfLrCbs": hwXQoSIfLrCbs,
       "hwXQoSIfInPhyBandwidth": hwXQoSIfInPhyBandwidth,
       "hwXQoSIfOutPhyBandwidth": hwXQoSIfOutPhyBandwidth,
       "hwXQoSIfInActualBandwidth": hwXQoSIfInActualBandwidth,
       "hwXQoSIfOutActualBandwidth": hwXQoSIfOutActualBandwidth,
       "hwXQoSIfQueueCfgInfoTable": hwXQoSIfQueueCfgInfoTable,
       "hwXQoSIfQueueCfgInfoEntry": hwXQoSIfQueueCfgInfoEntry,
       "hwXQoSIfQueueCfgIfIndex": hwXQoSIfQueueCfgIfIndex,
       "hwXQoSIfQueueCfgVlanID": hwXQoSIfQueueCfgVlanID,
       "hwXQoSIfQueueDirection": hwXQoSIfQueueDirection,
       "hwXQoSIfQueueCfgCosType": hwXQoSIfQueueCfgCosType,
       "hwXQoSIfQueuePriority": hwXQoSIfQueuePriority,
       "hwXQoSIfQueueCir": hwXQoSIfQueueCir,
       "hwXQoSIfQueuePir": hwXQoSIfQueuePir,
       "hwXQoSIfQueueWeight": hwXQoSIfQueueWeight,
       "hwXQoSIfQueueMode": hwXQoSIfQueueMode,
       "hwXQoSIfQueueRowStatus": hwXQoSIfQueueRowStatus,
       "hwXQoSIfObserveCfgInfoTable": hwXQoSIfObserveCfgInfoTable,
       "hwXQoSIfObserveCfgInfoEntry": hwXQoSIfObserveCfgInfoEntry,
       "hwXQoSIfObserveIndex": hwXQoSIfObserveIndex,
       "hwXQoSIfObserveIfIndex": hwXQoSIfObserveIfIndex,
       "hwXQoSIfObserveRowStatus": hwXQoSIfObserveRowStatus,
       "hwXQoSIfWredCfgInfoTable": hwXQoSIfWredCfgInfoTable,
       "hwXQoSIfWredCfgInfoEntry": hwXQoSIfWredCfgInfoEntry,
       "hwXQoSIfWredQueueIndex": hwXQoSIfWredQueueIndex,
       "hwXQoSIfWredDirection": hwXQoSIfWredDirection,
       "hwXQoSIfWredType": hwXQoSIfWredType,
       "hwXQoSIfWredLowlimit": hwXQoSIfWredLowlimit,
       "hwXQoSIfWredHighlimit": hwXQoSIfWredHighlimit,
       "hwXQoSIfWredDiscardProbability": hwXQoSIfWredDiscardProbability,
       "hwXQoSIfWredHighDiscardProbability": hwXQoSIfWredHighDiscardProbability,
       "hwXQoSIfWredRowStatus": hwXQoSIfWredRowStatus,
       "hwXQoSIf8021PMapCfgInfoTable": hwXQoSIf8021PMapCfgInfoTable,
       "hwXQoSIf8021PMapCfgInfoEntry": hwXQoSIf8021PMapCfgInfoEntry,
       "hwXQoSIf8021PMap8021PValue": hwXQoSIf8021PMap8021PValue,
       "hwXQoSIf8021PMapLocalPrecedence": hwXQoSIf8021PMapLocalPrecedence,
       "hwXQoSIf8021PMapRowStatus": hwXQoSIf8021PMapRowStatus,
       "hwXQoSIfMplsExpMapCfgInfoTable": hwXQoSIfMplsExpMapCfgInfoTable,
       "hwXQoSIfMplsExpMapCfgInfoEntry": hwXQoSIfMplsExpMapCfgInfoEntry,
       "hwXQoSIfMplsExpMapIfIndex": hwXQoSIfMplsExpMapIfIndex,
       "hwXQoSIfMplsExpMapInbound": hwXQoSIfMplsExpMapInbound,
       "hwXQoSIfMplsExpMapOutbound": hwXQoSIfMplsExpMapOutbound,
       "hwXQoSIfMplsExpMapRowStatus": hwXQoSIfMplsExpMapRowStatus,
       "hwXQoSIfDefaultPriorityCfgInfoTable": hwXQoSIfDefaultPriorityCfgInfoTable,
       "hwXQoSIfDefaultPriorityCfgInfoEntry": hwXQoSIfDefaultPriorityCfgInfoEntry,
       "hwXQoSIfDefaultPriorityIfIndex": hwXQoSIfDefaultPriorityIfIndex,
       "hwXQoSIfDefaultPriorityVlanID": hwXQoSIfDefaultPriorityVlanID,
       "hwXQoSIfDefaultPriorityValue": hwXQoSIfDefaultPriorityValue,
       "hwXQoSIfDefaultPriorityRowStatus": hwXQoSIfDefaultPriorityRowStatus,
       "hwXQoSIfSoftCarTable": hwXQoSIfSoftCarTable,
       "hwXQoSIfSoftCarEntry": hwXQoSIfSoftCarEntry,
       "hwXQoSIfSoftCarIfIndex": hwXQoSIfSoftCarIfIndex,
       "hwXQoSIfSoftCarDirection": hwXQoSIfSoftCarDirection,
       "hwXQoSIfSoftCarCarIndex": hwXQoSIfSoftCarCarIndex,
       "hwXQoSIfSoftCarRowStatus": hwXQoSIfSoftCarRowStatus,
       "hwXQoSIfLocalPrecedenceQueueMapTable": hwXQoSIfLocalPrecedenceQueueMapTable,
       "hwXQoSIfLocalPrecedenceQueueMapEntry": hwXQoSIfLocalPrecedenceQueueMapEntry,
       "hwXQoSIfLocPreQueMapIfIndex": hwXQoSIfLocPreQueMapIfIndex,
       "hwXQoSIfLocPreQueMapPreValue": hwXQoSIfLocPreQueMapPreValue,
       "hwXQoSIfLocPreQueMapCosType": hwXQoSIfLocPreQueMapCosType,
       "hwXQoSIfLocPreQueMapRowStatus": hwXQoSIfLocPreQueMapRowStatus,
       "hwXQoSIfScheduleModeCfgInfoTable": hwXQoSIfScheduleModeCfgInfoTable,
       "hwXQoSIfScheduleModeCfgInfoEntry": hwXQoSIfScheduleModeCfgInfoEntry,
       "hwXQoSIfScheduleModeIfIndex": hwXQoSIfScheduleModeIfIndex,
       "hwXQoSIfModeType": hwXQoSIfModeType,
       "hwXQoSIfScheduleModeRowStatus": hwXQoSIfScheduleModeRowStatus,
       "hwXQoSIfHQOSPriCfgInfoTable": hwXQoSIfHQOSPriCfgInfoTable,
       "hwXQoSIfHQOSPriCfgInfoEntry": hwXQoSIfHQOSPriCfgInfoEntry,
       "hwXQoSIfHqosPriIfIndex": hwXQoSIfHqosPriIfIndex,
       "hwXQoSIfHqosPriority": hwXQoSIfHqosPriority,
       "hwXQoSIfHqosPriRowStatus": hwXQoSIfHqosPriRowStatus,
       "hwXQoSIfOutboundMulticastCfgInfoTable": hwXQoSIfOutboundMulticastCfgInfoTable,
       "hwXQoSIfOutboundMulticastCfgInfoEntry": hwXQoSIfOutboundMulticastCfgInfoEntry,
       "hwXQoSIfOutMulticastIfIndex": hwXQoSIfOutMulticastIfIndex,
       "hwXQoSIfUnicastWeightValue": hwXQoSIfUnicastWeightValue,
       "hwXQoSIfMulticastWeightValue": hwXQoSIfMulticastWeightValue,
       "hwXQoSIfOutMulticastRowStatus": hwXQoSIfOutMulticastRowStatus,
       "hwXQoSIfSredCfgInfoTable": hwXQoSIfSredCfgInfoTable,
       "hwXQoSIfSredCfgInfoEntry": hwXQoSIfSredCfgInfoEntry,
       "hwXQoSIfSredQueueIndex": hwXQoSIfSredQueueIndex,
       "hwXQoSIfSredRedStartDiscardPoint": hwXQoSIfSredRedStartDiscardPoint,
       "hwXQoSIfSredRedDiscardProbability": hwXQoSIfSredRedDiscardProbability,
       "hwXQoSIfSredYellowStartDiscardPoint": hwXQoSIfSredYellowStartDiscardPoint,
       "hwXQoSIfSredYellowDiscardProbability": hwXQoSIfSredYellowDiscardProbability,
       "hwXQoSIfSredRowStatus": hwXQoSIfSredRowStatus,
       "hwXQosAtmTrafficQueueTable": hwXQosAtmTrafficQueueTable,
       "hwXQosAtmTrafficQueueEntry": hwXQosAtmTrafficQueueEntry,
       "hwXQoSAtmTrafficQueueIfIndex": hwXQoSAtmTrafficQueueIfIndex,
       "hwXQoSAtmTrafficQueueServiceClass": hwXQoSAtmTrafficQueueServiceClass,
       "hwXQoSAtmTrafficQueueRowStatus": hwXQoSAtmTrafficQueueRowStatus,
       "hwXQoSAtmPvcServiceTypeTable": hwXQoSAtmPvcServiceTypeTable,
       "hwXQoSAtmPvcServiceTypeEntry": hwXQoSAtmPvcServiceTypeEntry,
       "hwXQoSAtmPvcServiceTypeIfIndex": hwXQoSAtmPvcServiceTypeIfIndex,
       "hwXQoSAtmPvcServiceTypeVpiIndex": hwXQoSAtmPvcServiceTypeVpiIndex,
       "hwXQoSAtmPvcServiceTypeVciIndex": hwXQoSAtmPvcServiceTypeVciIndex,
       "hwXQoSAtmPvcNameServiceTypeIndex": hwXQoSAtmPvcNameServiceTypeIndex,
       "hwXQoSAtmPvcServiceType": hwXQoSAtmPvcServiceType,
       "hwXQoSAtmPvcPcr": hwXQoSAtmPvcPcr,
       "hwXQoSAtmPvcCdvt": hwXQoSAtmPvcCdvt,
       "hwXQoSAtmPvcVbrScr": hwXQoSAtmPvcVbrScr,
       "hwXQoSAtmPvcVbrMbs": hwXQoSAtmPvcVbrMbs,
       "hwXQoSAtmPvcRowStatus": hwXQoSAtmPvcRowStatus,
       "hwXQoSIfShapingCfgInfoTable": hwXQoSIfShapingCfgInfoTable,
       "hwXQoSIfShapingCfgInfoEntry": hwXQoSIfShapingCfgInfoEntry,
       "hwXQoSIfShapingIfIndex": hwXQoSIfShapingIfIndex,
       "hwXQoSIfShapingQueueIndex": hwXQoSIfShapingQueueIndex,
       "hwXQoSIfShapingQueueCir": hwXQoSIfShapingQueueCir,
       "hwXQoSIfShapingQueuePir": hwXQoSIfShapingQueuePir,
       "hwXQoSIfShapingRowStatus": hwXQoSIfShapingRowStatus,
       "hwXQoSIfPppoeCfgInfoTable": hwXQoSIfPppoeCfgInfoTable,
       "hwXQoSIfPppoeCfgInfoEntry": hwXQoSIfPppoeCfgInfoEntry,
       "hwXQoSIfPppoeIfIndex": hwXQoSIfPppoeIfIndex,
       "hwXQoSIfPppoeMatchType": hwXQoSIfPppoeMatchType,
       "hwXQoSIfPppoeSourceMac": hwXQoSIfPppoeSourceMac,
       "hwXQoSIfPppoeDestMac": hwXQoSIfPppoeDestMac,
       "hwXQoSIfPppoeRowStatus": hwXQoSIfPppoeRowStatus,
       "hwXQoSIfScheduleCfgInfoTable": hwXQoSIfScheduleCfgInfoTable,
       "hwXQoSIfScheduleCfgInfoEntry": hwXQoSIfScheduleCfgInfoEntry,
       "hwXQoSIfScheduleIfIndex": hwXQoSIfScheduleIfIndex,
       "hwXQoSIfScheduleProfile": hwXQoSIfScheduleProfile,
       "hwXQoSIfScheduleRowStatus": hwXQoSIfScheduleRowStatus,
       "hwXQoSIfIPCarCfgInfoTable": hwXQoSIfIPCarCfgInfoTable,
       "hwXQoSIfIPCarCfgInfoEntry": hwXQoSIfIPCarCfgInfoEntry,
       "hwXQoSIfIPCarCfgIfIndex": hwXQoSIfIPCarCfgIfIndex,
       "hwXQoSIfIPCarDirection": hwXQoSIfIPCarDirection,
       "hwXQoSIPCarRuleIndex": hwXQoSIPCarRuleIndex,
       "hwXQoSIPCarRuleType": hwXQoSIPCarRuleType,
       "hwXBQoSIPCarIntValue": hwXBQoSIPCarIntValue,
       "hwXQoSIfIPCarStartIp": hwXQoSIfIPCarStartIp,
       "hwXQoSIfIPCarEndIp": hwXQoSIfIPCarEndIp,
       "hwXQoSIfIPCarCir": hwXQoSIfIPCarCir,
       "hwXQoSIfIPCarCbs": hwXQoSIfIPCarCbs,
       "hwXQoSIfIPCarEbs": hwXQoSIfIPCarEbs,
       "hwXQoSIfIPCarPir": hwXQoSIfIPCarPir,
       "hwXQoSIfIPCarPbs": hwXQoSIfIPCarPbs,
       "hwXQoSIfIPCarGreenAction": hwXQoSIfIPCarGreenAction,
       "hwXQoSIfIPCarGreenRemarkValue": hwXQoSIfIPCarGreenRemarkValue,
       "hwXQoSIfIPCarYellowAction": hwXQoSIfIPCarYellowAction,
       "hwXQoSIfIPCarYellowRemarkValue": hwXQoSIfIPCarYellowRemarkValue,
       "hwXQoSIfIPCarRedAction": hwXQoSIfIPCarRedAction,
       "hwXQoSIfIPCarRedRemarkValue": hwXQoSIfIPCarRedRemarkValue,
       "hwXQoSIfIPCarAggregation": hwXQoSIfIPCarAggregation,
       "hwXQoSIfIPCarRowStatus": hwXQoSIfIPCarRowStatus,
       "hwXQoSCpcarObjects": hwXQoSCpcarObjects,
       "hwXQoSCpcarCfgInfoTable": hwXQoSCpcarCfgInfoTable,
       "hwXQoSCpcarCfgInfoEntry": hwXQoSCpcarCfgInfoEntry,
       "hwXQoSCpcarIndex": hwXQoSCpcarIndex,
       "hwXQoSCpcarName": hwXQoSCpcarName,
       "hwXQoSCpcarRowStatus": hwXQoSCpcarRowStatus,
       "hwXQoSCpCarFilterCfgInfoTable": hwXQoSCpCarFilterCfgInfoTable,
       "hwXQoSCpCarFilterCfgInfoEntry": hwXQoSCpCarFilterCfgInfoEntry,
       "hwXQoSCpCarFilterAction": hwXQoSCpCarFilterAction,
       "hwXQoSCpCarFilterRowStatus": hwXQoSCpCarFilterRowStatus,
       "hwXQoSCpCarCfgInfoTable": hwXQoSCpCarCfgInfoTable,
       "hwXQoSCpCarCfgInfoEntry": hwXQoSCpCarCfgInfoEntry,
       "hwXQoSCpCarSlotId": hwXQoSCpCarSlotId,
       "hwXQoSCpCarCir": hwXQoSCpCarCir,
       "hwXQoSCpCarCbs": hwXQoSCpCarCbs,
       "hwXQoSCpCarEbs": hwXQoSCpCarEbs,
       "hwXQoSCpCarPir": hwXQoSCpCarPir,
       "hwXQoSCpCarPbs": hwXQoSCpCarPbs,
       "hwXQoSCpCarGreenAction": hwXQoSCpCarGreenAction,
       "hwXQoSCpCarGreenRemarkValue": hwXQoSCpCarGreenRemarkValue,
       "hwXQoSCpCarYellowAction": hwXQoSCpCarYellowAction,
       "hwXQoSCpCarYellowRemarkValue": hwXQoSCpCarYellowRemarkValue,
       "hwXQoSCpCarRedAction": hwXQoSCpCarRedAction,
       "hwXQoSCpCarRedRemarkValue": hwXQoSCpCarRedRemarkValue,
       "hwXQoSCpCarRowStatus": hwXQoSCpCarRowStatus,
       "hwXQoSCpApplyPolicyTable": hwXQoSCpApplyPolicyTable,
       "hwXQoSCpApplyPolicyEntry": hwXQoSCpApplyPolicyEntry,
       "hwXQoSCpApplyPolicyName": hwXQoSCpApplyPolicyName,
       "hwXQoSCpApplyPolicyRowStatus": hwXQoSCpApplyPolicyRowStatus,
       "hwXQoSCpCarActionTable": hwXQoSCpCarActionTable,
       "hwXQoSCpCarActionEntry": hwXQoSCpCarActionEntry,
       "hwXQoSCpCarActionSlotIndex": hwXQoSCpCarActionSlotIndex,
       "hwXQoSCpCarActionPacketType": hwXQoSCpCarActionPacketType,
       "hwXQoSCpCarActionPacketTypeName": hwXQoSCpCarActionPacketTypeName,
       "hwXQoSCpCarActionType": hwXQoSCpCarActionType,
       "hwXQoSCpCarActionPolicyName": hwXQoSCpCarActionPolicyName,
       "hwXQoSCpCarActionCarCir": hwXQoSCpCarActionCarCir,
       "hwXQoSCpCarActionCarCbs": hwXQoSCpCarActionCarCbs,
       "hwXQoSCpCarActionCarEbs": hwXQoSCpCarActionCarEbs,
       "hwXQoSCpCarActionCarPir": hwXQoSCpCarActionCarPir,
       "hwXQoSCpCarActionCarPbs": hwXQoSCpCarActionCarPbs,
       "hwXQoSCpCarActionGreenAction": hwXQoSCpCarActionGreenAction,
       "hwXQoSCpCarActionGreenRemarkValue": hwXQoSCpCarActionGreenRemarkValue,
       "hwXQoSCpCarActionYellowAction": hwXQoSCpCarActionYellowAction,
       "hwXQoSCpCarActionYellowRemarkValue": hwXQoSCpCarActionYellowRemarkValue,
       "hwXQoSCpCarActionRedAction": hwXQoSCpCarActionRedAction,
       "hwXQoSCpCarActionRedRemarkValue": hwXQoSCpCarActionRedRemarkValue,
       "hwXQoSCpCarActionSetDefault": hwXQoSCpCarActionSetDefault,
       "hwXQoSStatisticsObjects": hwXQoSStatisticsObjects,
       "hwXQoSCpcarStaticsObjects": hwXQoSCpcarStaticsObjects,
       "hwXQoSCpcarRunInfoTable": hwXQoSCpcarRunInfoTable,
       "hwXQoSCpcarRunInfoEntry": hwXQoSCpcarRunInfoEntry,
       "hwXQoSCpcarPassedPackets": hwXQoSCpcarPassedPackets,
       "hwXQoSCpcarPassededBytes": hwXQoSCpcarPassededBytes,
       "hwXQoSCpcarTotalPackets": hwXQoSCpcarTotalPackets,
       "hwXQoSCpcarTotalBytes": hwXQoSCpcarTotalBytes,
       "hwXQoSCpcarDiscardedPackets": hwXQoSCpcarDiscardedPackets,
       "hwXQoSCpcarDiscardedBytes": hwXQoSCpcarDiscardedBytes,
       "hwXQoSCpCarSlotStatTable": hwXQoSCpCarSlotStatTable,
       "hwXQoSCpCarSlotStatEntry": hwXQoSCpCarSlotStatEntry,
       "hwXQoSCpCarSlotStatSlotIndex": hwXQoSCpCarSlotStatSlotIndex,
       "hwXQoSCpCarSlotStatPacketType": hwXQoSCpCarSlotStatPacketType,
       "hwXQoSCpCarSlotStatDiscardedPackets": hwXQoSCpCarSlotStatDiscardedPackets,
       "hwXQoSCpCarSlotStatDiscardedBytes": hwXQoSCpCarSlotStatDiscardedBytes,
       "hwXQoSCpCarSlotStatPassedPackets": hwXQoSCpCarSlotStatPassedPackets,
       "hwXQoSCpCarSlotStatPassededBytes": hwXQoSCpCarSlotStatPassededBytes,
       "hwXQoSCpCarSlotStatTotalPackets": hwXQoSCpCarSlotStatTotalPackets,
       "hwXQoSCpCarSlotStatTotalBytes": hwXQoSCpCarSlotStatTotalBytes,
       "hwXQoSIfStatisticsObjects": hwXQoSIfStatisticsObjects,
       "hwXQoSIfCarRunInfoTable": hwXQoSIfCarRunInfoTable,
       "hwXQoSIfCarRunInfoEntry": hwXQoSIfCarRunInfoEntry,
       "hwXQoSIfCarIndex": hwXQoSIfCarIndex,
       "hwXQoSIfVlanID": hwXQoSIfVlanID,
       "hwXQoSIfCarGreenPassedPackets": hwXQoSIfCarGreenPassedPackets,
       "hwXQoSIfCarGreenPassedBytes": hwXQoSIfCarGreenPassedBytes,
       "hwXQoSIfCarGreenRemarkedPackets": hwXQoSIfCarGreenRemarkedPackets,
       "hwXQoSIfCarGreenRemarkedBytes": hwXQoSIfCarGreenRemarkedBytes,
       "hwXQoSIfCarGreenDiscardedPackets": hwXQoSIfCarGreenDiscardedPackets,
       "hwXQoSIfCarGreenDiscardedBytes": hwXQoSIfCarGreenDiscardedBytes,
       "hwXQoSIfCarYellowPassedPackets": hwXQoSIfCarYellowPassedPackets,
       "hwXQoSIfCarYellowPassedBytes": hwXQoSIfCarYellowPassedBytes,
       "hwXQoSIfCarYellowRemarkedPackets": hwXQoSIfCarYellowRemarkedPackets,
       "hwXQoSIfCarYellowRemarkedBytes": hwXQoSIfCarYellowRemarkedBytes,
       "hwXQoSIfCarYellowDiscardedPackets": hwXQoSIfCarYellowDiscardedPackets,
       "hwXQoSIfCarYellowDiscardedBytes": hwXQoSIfCarYellowDiscardedBytes,
       "hwXQoSIfCarRedPassedPackets": hwXQoSIfCarRedPassedPackets,
       "hwXQoSIfCarRedPassedBytes": hwXQoSIfCarRedPassedBytes,
       "hwXQoSIfCarRedRemarkedPackets": hwXQoSIfCarRedRemarkedPackets,
       "hwXQoSIfCarRedRemarkedBytes": hwXQoSIfCarRedRemarkedBytes,
       "hwXQoSIfCarRedDiscardedPackets": hwXQoSIfCarRedDiscardedPackets,
       "hwXQoSIfCarRedDiscardedBytes": hwXQoSIfCarRedDiscardedBytes,
       "hwXQoSIfCarTotalDiscardPackets": hwXQoSIfCarTotalDiscardPackets,
       "hwXQoSIfCarInBoundDiscardPackets": hwXQoSIfCarInBoundDiscardPackets,
       "hwXQoSIfCarOutBoundDiscardPackets": hwXQoSIfCarOutBoundDiscardPackets,
       "hwXQoSIfQueueRunInfoTable": hwXQoSIfQueueRunInfoTable,
       "hwXQoSIfQueueRunInfoEntry": hwXQoSIfQueueRunInfoEntry,
       "hwXQoSIfQueueIfIndex": hwXQoSIfQueueIfIndex,
       "hwXQoSIfQueueVlanID": hwXQoSIfQueueVlanID,
       "hwXQoSIfQueueCosType": hwXQoSIfQueueCosType,
       "hwXQoSIfQueuePassedPackets": hwXQoSIfQueuePassedPackets,
       "hwXQoSIfQueuePassededBytes": hwXQoSIfQueuePassededBytes,
       "hwXQoSIfQueueTotalPackets": hwXQoSIfQueueTotalPackets,
       "hwXQoSIfQueueTotalBytes": hwXQoSIfQueueTotalBytes,
       "hwXQoSIfQueueDiscardedPackets": hwXQoSIfQueueDiscardedPackets,
       "hwXQoSIfQueueDiscardedBytes": hwXQoSIfQueueDiscardedBytes,
       "hwXQoSIfQueuePassedPacketRate": hwXQoSIfQueuePassedPacketRate,
       "hwXQoSIfQueuePassedByteRate": hwXQoSIfQueuePassedByteRate,
       "hwXQoSIfQueueDiscardedPacketRate": hwXQoSIfQueueDiscardedPacketRate,
       "hwXQoSIfQueueDiscardedByteRate": hwXQoSIfQueueDiscardedByteRate,
       "hwXQoSIfQueueResetFlag": hwXQoSIfQueueResetFlag,
       "hwXQoSIfQueueUsagePercentage": hwXQoSIfQueueUsagePercentage,
       "hwXQoSIfWredRunInfoTable": hwXQoSIfWredRunInfoTable,
       "hwXQoSIfWredRunInfoEntry": hwXQoSIfWredRunInfoEntry,
       "hwXQoSIfWredIfIndex": hwXQoSIfWredIfIndex,
       "hwXQoSIfWredVlanID": hwXQoSIfWredVlanID,
       "hwXQoSIfWredRandomDiscardedPackets": hwXQoSIfWredRandomDiscardedPackets,
       "hwXQoSIfWredTailDiscardedPackets": hwXQoSIfWredTailDiscardedPackets,
       "hwXQoSIfWredDiscardedPackets": hwXQoSIfWredDiscardedPackets,
       "hwXQoSIfLrRunInfoTable": hwXQoSIfLrRunInfoTable,
       "hwXQoSIfLrRunInfoEntry": hwXQoSIfLrRunInfoEntry,
       "hwXQoSIfLrIfIndex": hwXQoSIfLrIfIndex,
       "hwXQoSIfLrVlanID": hwXQoSIfLrVlanID,
       "hwXQoSIfLrPassedPackets": hwXQoSIfLrPassedPackets,
       "hwXQoSIfLrPassedBytes": hwXQoSIfLrPassedBytes,
       "hwXQoSIfLrDiscardedPackets": hwXQoSIfLrDiscardedPackets,
       "hwXQoSIfLrDiscardedBytes": hwXQoSIfLrDiscardedBytes,
       "hwXQoSIfLrDelayedPackets": hwXQoSIfLrDelayedPackets,
       "hwXQoSIfLrDelayedBytes": hwXQoSIfLrDelayedBytes,
       "hwXQoSIfMirrorRunInfoTable": hwXQoSIfMirrorRunInfoTable,
       "hwXQoSIfMirrorRunInfoEntry": hwXQoSIfMirrorRunInfoEntry,
       "hwXQoSIfMirrorIfIndex": hwXQoSIfMirrorIfIndex,
       "hwXQoSIfMirrorVlanID": hwXQoSIfMirrorVlanID,
       "hwXQoSIfMirroredPackets": hwXQoSIfMirroredPackets,
       "hwXQoSIfUrpfRunInfoTable": hwXQoSIfUrpfRunInfoTable,
       "hwXQoSIfUrpfRunInfoEntry": hwXQoSIfUrpfRunInfoEntry,
       "hwXQoSIfUrpfIfIndex": hwXQoSIfUrpfIfIndex,
       "hwXQoSIfUrpfVlanID": hwXQoSIfUrpfVlanID,
       "hwXQoSIfUrpfPassedPackets": hwXQoSIfUrpfPassedPackets,
       "hwXQoSIfUrpfDroppdPackets": hwXQoSIfUrpfDroppdPackets,
       "hwXQoSIfSampleRunInfoTable": hwXQoSIfSampleRunInfoTable,
       "hwXQoSIfSampleRunInfoEntry": hwXQoSIfSampleRunInfoEntry,
       "hwXQoSIfSampleIfIndex": hwXQoSIfSampleIfIndex,
       "hwXQoSIfSampleVlanID": hwXQoSIfSampleVlanID,
       "hwXQoSIfSampledPackets": hwXQoSIfSampledPackets,
       "hwXQoSIfCarStatisticsTable": hwXQoSIfCarStatisticsTable,
       "hwXQoSIfCarStatisticsEntry": hwXQoSIfCarStatisticsEntry,
       "hwXQoSIfCarConformedPackets": hwXQoSIfCarConformedPackets,
       "hwXQoSIfCarConformedBytes": hwXQoSIfCarConformedBytes,
       "hwXQoSIfCarConformedPacketRate": hwXQoSIfCarConformedPacketRate,
       "hwXQoSIfCarConformedByteRate": hwXQoSIfCarConformedByteRate,
       "hwXQoSIfCarExceededPackets": hwXQoSIfCarExceededPackets,
       "hwXQoSIfCarExceededBytes": hwXQoSIfCarExceededBytes,
       "hwXQoSIfCarExceededPacketRate": hwXQoSIfCarExceededPacketRate,
       "hwXQoSIfCarExceededByteRate": hwXQoSIfCarExceededByteRate,
       "hwXQoSIfCarOverflowPackets": hwXQoSIfCarOverflowPackets,
       "hwXQoSIfCarOverflowBytes": hwXQoSIfCarOverflowBytes,
       "hwXQoSIfCarOverflowPacketRate": hwXQoSIfCarOverflowPacketRate,
       "hwXQoSIfCarOverflowByteRate": hwXQoSIfCarOverflowByteRate,
       "hwXQoSIfCarPassedPackets": hwXQoSIfCarPassedPackets,
       "hwXQoSIfCarPassedBytes": hwXQoSIfCarPassedBytes,
       "hwXQoSIfCarDiscardedPackets": hwXQoSIfCarDiscardedPackets,
       "hwXQoSIfCarDiscardedBytes": hwXQoSIfCarDiscardedBytes,
       "hwXQoSIfOutboundQueueStatisticTable": hwXQoSIfOutboundQueueStatisticTable,
       "hwXQoSIfOutboundQueueStatisticEntry": hwXQoSIfOutboundQueueStatisticEntry,
       "hwXQoSIfExtIndex": hwXQoSIfExtIndex,
       "hwXQoSIfQueIndex": hwXQoSIfQueIndex,
       "hwXQoSIfQueDiscardPackets": hwXQoSIfQueDiscardPackets,
       "hwXQoSVlanStatisticsObjects": hwXQoSVlanStatisticsObjects,
       "hwXQosVlanStatTable": hwXQosVlanStatTable,
       "hwXQosVlanStatEntry": hwXQosVlanStatEntry,
       "hwXQosVlanStatVlanId": hwXQosVlanStatVlanId,
       "hwXQosVlanStatInTotalPkts": hwXQosVlanStatInTotalPkts,
       "hwXQosVlanStatInTotalBytes": hwXQosVlanStatInTotalBytes,
       "hwXQosVlanStatOutTotalPkts": hwXQosVlanStatOutTotalPkts,
       "hwXQosVlanStatOutTotalBytes": hwXQosVlanStatOutTotalBytes,
       "hwXQosVlanStatInUcastPkts": hwXQosVlanStatInUcastPkts,
       "hwXQosVlanStatInUcastBytes": hwXQosVlanStatInUcastBytes,
       "hwXQosVlanStatOutUcastPkts": hwXQosVlanStatOutUcastPkts,
       "hwXQosVlanStatOutUcastBytes": hwXQosVlanStatOutUcastBytes,
       "hwXQosVlanStatInMcastPkts": hwXQosVlanStatInMcastPkts,
       "hwXQosVlanStatInMcastBytes": hwXQosVlanStatInMcastBytes,
       "hwXQosVlanStatOutMcastPkts": hwXQosVlanStatOutMcastPkts,
       "hwXQosVlanStatOutMcastBytes": hwXQosVlanStatOutMcastBytes,
       "hwXQosVlanStatInBcastPkts": hwXQosVlanStatInBcastPkts,
       "hwXQosVlanStatInBcastBytes": hwXQosVlanStatInBcastBytes,
       "hwXQosVlanStatOutBcastPkts": hwXQosVlanStatOutBcastPkts,
       "hwXQosVlanStatOutBcastBytes": hwXQosVlanStatOutBcastBytes,
       "hwXQosVlanStatInUnknownUcastPkts": hwXQosVlanStatInUnknownUcastPkts,
       "hwXQosVlanStatInUnknownUcastBytes": hwXQosVlanStatInUnknownUcastBytes,
       "hwXQosVlanStatResetFlag": hwXQosVlanStatResetFlag,
       "hwXQoSGlobalObjects": hwXQoSGlobalObjects,
       "hwXQoSSoftCarCfgTable": hwXQoSSoftCarCfgTable,
       "hwXQoSSoftCarCfgEntry": hwXQoSSoftCarCfgEntry,
       "hwXQoSSoftCarIndex": hwXQoSSoftCarIndex,
       "hwXQoSSoftCarName": hwXQoSSoftCarName,
       "hwXQoSSoftCarCir": hwXQoSSoftCarCir,
       "hwXQoSSoftCarCbs": hwXQoSSoftCarCbs,
       "hwXQoSSoftCarRowStatus": hwXQoSSoftCarRowStatus,
       "hwXQoSGlobalWredClassCfgTable": hwXQoSGlobalWredClassCfgTable,
       "hwXQoSGlobalWredClassCfgEntry": hwXQoSGlobalWredClassCfgEntry,
       "hwXQoSGlobalWredClassIndex": hwXQoSGlobalWredClassIndex,
       "hwXQoSGlobalWredClassLowlimit": hwXQoSGlobalWredClassLowlimit,
       "hwXQoSGlobalWredClassHighlimit": hwXQoSGlobalWredClassHighlimit,
       "hwXQoSGlobalWredClassDiscardProbability": hwXQoSGlobalWredClassDiscardProbability,
       "hwXQoSGlobalWredClassSetDefault": hwXQoSGlobalWredClassSetDefault,
       "hwXQoSGlobalWredTypeCfgTable": hwXQoSGlobalWredTypeCfgTable,
       "hwXQoSGlobalWredTypeCfgEntry": hwXQoSGlobalWredTypeCfgEntry,
       "hwXQoSGlobalWredTypeIndex": hwXQoSGlobalWredTypeIndex,
       "hwXQoSGlobalWredTypeName": hwXQoSGlobalWredTypeName,
       "hwXQoSGlobalWredTypeLowlimit": hwXQoSGlobalWredTypeLowlimit,
       "hwXQoSGlobalWredTypeHighlimit": hwXQoSGlobalWredTypeHighlimit,
       "hwXQoSGlobalWredTypeDiscardProbability": hwXQoSGlobalWredTypeDiscardProbability,
       "hwXQoSGlobalWredTypeSetDefault": hwXQoSGlobalWredTypeSetDefault,
       "hwXQoSVlanBcastSuppressTable": hwXQoSVlanBcastSuppressTable,
       "hwXQoSVlanBcastSuppressEntry": hwXQoSVlanBcastSuppressEntry,
       "hwXQoSVlanBcastSuppressVlanId": hwXQoSVlanBcastSuppressVlanId,
       "hwXQoSVlanBcastSuppressValue": hwXQoSVlanBcastSuppressValue,
       "hwXQoSVlanBcastSuppressRowStatus": hwXQoSVlanBcastSuppressRowStatus,
       "hwXQoSScheduleProfileTable": hwXQoSScheduleProfileTable,
       "hwXQoSScheduleProfileEntry": hwXQoSScheduleProfileEntry,
       "hwXQoSScheduleProfileName": hwXQoSScheduleProfileName,
       "hwXQoSScheduleQueueMode": hwXQoSScheduleQueueMode,
       "hwXQoSScheduleQueueBeWeight": hwXQoSScheduleQueueBeWeight,
       "hwXQoSScheduleQueueAf1Weight": hwXQoSScheduleQueueAf1Weight,
       "hwXQoSScheduleQueueAf2Weight": hwXQoSScheduleQueueAf2Weight,
       "hwXQoSScheduleQueueAf3Weight": hwXQoSScheduleQueueAf3Weight,
       "hwXQoSScheduleQueueAf4Weight": hwXQoSScheduleQueueAf4Weight,
       "hwXQoSScheduleQueueCs6Weight": hwXQoSScheduleQueueCs6Weight,
       "hwXQoSScheduleQueueCs7Weight": hwXQoSScheduleQueueCs7Weight,
       "hwXQoSScheduleQueueEfWeight": hwXQoSScheduleQueueEfWeight,
       "hwXQoSScheduleProfileRowStatus": hwXQoSScheduleProfileRowStatus,
       "hwXQoSCpDefendObjects": hwXQoSCpDefendObjects,
       "hwXQoSCpDefendStatisticsTable": hwXQoSCpDefendStatisticsTable,
       "hwXQoSCpDefendStatisticsEntry": hwXQoSCpDefendStatisticsEntry,
       "hwXQoSCpDefendSlotId": hwXQoSCpDefendSlotId,
       "hwXQoSCpDefendObjectIndex": hwXQoSCpDefendObjectIndex,
       "hwXQoSCpDefendPassedPackets": hwXQoSCpDefendPassedPackets,
       "hwXQoSCpDefendPassedBytes": hwXQoSCpDefendPassedBytes,
       "hwXQoSCpDefendPassedPacketRate": hwXQoSCpDefendPassedPacketRate,
       "hwXQoSCpDefendPassedByteRate": hwXQoSCpDefendPassedByteRate,
       "hwXQoSCpDefendDiscardedPackets": hwXQoSCpDefendDiscardedPackets,
       "hwXQoSCpDefendDiscardedBytes": hwXQoSCpDefendDiscardedBytes,
       "hwXQoSCpDefendDiscardedPacketRate": hwXQoSCpDefendDiscardedPacketRate,
       "hwXQoSCpDefendDiscardedByteRate": hwXQoSCpDefendDiscardedByteRate,
       "hwXQoSCpDefendDiscardedThreshold": hwXQoSCpDefendDiscardedThreshold,
       "hwXQoSCpDefendChassisID": hwXQoSCpDefendChassisID,
       "hwXQoSUrpfObjects": hwXQoSUrpfObjects,
       "hwXQoSUrpfDiscardStatisticsTable": hwXQoSUrpfDiscardStatisticsTable,
       "hwXQoSUrpfDiscardStatisticsEntry": hwXQoSUrpfDiscardStatisticsEntry,
       "hwXQoSUrpfSlotPhysicalIndex": hwXQoSUrpfSlotPhysicalIndex,
       "hwXQoSUrpfDiscardedPackets": hwXQoSUrpfDiscardedPackets,
       "hwXQoSVlanCfgObjects": hwXQoSVlanCfgObjects,
       "hwXQoSVlanCfgTable": hwXQoSVlanCfgTable,
       "hwXQoSVlanCfgEntry": hwXQoSVlanCfgEntry,
       "hwXQoSVlanStatEnable": hwXQoSVlanStatEnable,
       "hwXQoSRedirectNextHopObjects": hwXQoSRedirectNextHopObjects,
       "hwXQoSRedirectNextHopTable": hwXQoSRedirectNextHopTable,
       "hwXQoSRedirectNextHopEntry": hwXQoSRedirectNextHopEntry,
       "hwXQoSRedirectNextHopBehaviorName": hwXQoSRedirectNextHopBehaviorName,
       "hwXQoSRedirectNextHopOldIp": hwXQoSRedirectNextHopOldIp,
       "hwXQoSRedirectNextHopNewIp": hwXQoSRedirectNextHopNewIp,
       "hwXQoSIrsmDefendObjects": hwXQoSIrsmDefendObjects,
       "hwXQoSIrsmTable": hwXQoSIrsmTable,
       "hwXQoSIrsmEntry": hwXQoSIrsmEntry,
       "hwXQoSIrsmSourceAddress": hwXQoSIrsmSourceAddress,
       "hwXQoSIrsmGroupAddress": hwXQoSIrsmGroupAddress,
       "hwXQoSIrsmTime": hwXQoSIrsmTime,
       "hwXQoSIrsmDelay": hwXQoSIrsmDelay,
       "hwXQoSIrsmThreshold": hwXQoSIrsmThreshold,
       "hwXQoSIrsmUpstream": hwXQoSIrsmUpstream,
       "hwXQoSIrsmLocal": hwXQoSIrsmLocal,
       "hwXQoSIrsmTotalPacket": hwXQoSIrsmTotalPacket,
       "hwXQoSIrsmDropPacket": hwXQoSIrsmDropPacket,
       "hwXQoSNotifications": hwXQoSNotifications,
       "hwXQoSCpDefendDiscardedRateAlarm": hwXQoSCpDefendDiscardedRateAlarm,
       "hwXQoSQueueDiscardThresholdTrap": hwXQoSQueueDiscardThresholdTrap,
       "hwXQoSCpDefendDiscardedPacketAlarm": hwXQoSCpDefendDiscardedPacketAlarm,
       "hwXQoSCpDefendDiscardedPacketAlarmClear": hwXQoSCpDefendDiscardedPacketAlarmClear,
       "hwXQoSCprlDiscardedPacketAlarm": hwXQoSCprlDiscardedPacketAlarm,
       "hwXQoSCprlDiscardedPacketAlarmClear": hwXQoSCprlDiscardedPacketAlarmClear,
       "hwXQoSRedirectNextHopChangedAlarm": hwXQoSRedirectNextHopChangedAlarm,
       "hwXQoSIrsmDelayAlarm": hwXQoSIrsmDelayAlarm,
       "hwXQoSIrsmDropPacketAlarm": hwXQoSIrsmDropPacketAlarm,
       "hwXQoSIrsmSynFrameDropAlarm": hwXQoSIrsmSynFrameDropAlarm,
       "hwXQoSRuleFaileAlarm": hwXQoSRuleFaileAlarm,
       "hwXQoSProfileUsedAlarm": hwXQoSProfileUsedAlarm,
       "hwXQoSPortQueueAlarm": hwXQoSPortQueueAlarm,
       "hwXQoSPortQueueAlarmClear": hwXQoSPortQueueAlarmClear,
       "hwXQoSSecurityStormControlInterfaceTrap": hwXQoSSecurityStormControlInterfaceTrap,
       "hwXQoSStatResouceNotEnoughAlarm": hwXQoSStatResouceNotEnoughAlarm,
       "hwXQoSCARResouceNotEnoughAlarm": hwXQoSCARResouceNotEnoughAlarm,
       "hwXQoSGeneral": hwXQoSGeneral,
       "hwXQoSFrameId": hwXQoSFrameId,
       "hwXQoSSlotId": hwXQoSSlotId,
       "hwXQoSPortId": hwXQoSPortId,
       "hwXQoSTrapIfName": hwXQoSTrapIfName,
       "hwXQoSTrapQueueId": hwXQoSTrapQueueId,
       "hwXQoSTrapDiscardPackets": hwXQoSTrapDiscardPackets,
       "hwXQoSStormControlObjects": hwXQoSStormControlObjects,
       "hwXQoSStormControlTable": hwXQoSStormControlTable,
       "hwXQoSStormControlEntry": hwXQoSStormControlEntry,
       "hwXQoSStormControlIfIndex": hwXQoSStormControlIfIndex,
       "hwXQoSStormControlBroadcastMinRate": hwXQoSStormControlBroadcastMinRate,
       "hwXQoSStormControlBroadcastMaxRate": hwXQoSStormControlBroadcastMaxRate,
       "hwXQoSStormControlMulticastMinRate": hwXQoSStormControlMulticastMinRate,
       "hwXQoSStormControlMulticastMaxRate": hwXQoSStormControlMulticastMaxRate,
       "hwXQoSStormControlAction": hwXQoSStormControlAction,
       "hwXQoSStormControlInterval": hwXQoSStormControlInterval,
       "hwXQoSStormControlTrapEnable": hwXQoSStormControlTrapEnable,
       "hwXQoSStormControlLogEnable": hwXQoSStormControlLogEnable,
       "hwXQoSStormControlStatus": hwXQoSStormControlStatus,
       "hwXQoSStormControlUnicastMinRate": hwXQoSStormControlUnicastMinRate,
       "hwXQoSStormControlUnicastMaxRate": hwXQoSStormControlUnicastMaxRate,
       "hwXQoSStormControlBcMode": hwXQoSStormControlBcMode,
       "hwXQoSStormControlMcMode": hwXQoSStormControlMcMode,
       "hwXQoSStormControlUcMode": hwXQoSStormControlUcMode,
       "hwXQoSStormControlNotification": hwXQoSStormControlNotification,
       "hwXQoSStormControlTrap": hwXQoSStormControlTrap,
       "hwXQoSQueueStatisticsObjects": hwXQoSQueueStatisticsObjects,
       "hwXQoSQueueStatisticsTable": hwXQoSQueueStatisticsTable,
       "hwXQoSQueueStatisticsEntry": hwXQoSQueueStatisticsEntry,
       "hwXQoSQueueStatisticsIngressIfIndex": hwXQoSQueueStatisticsIngressIfIndex,
       "hwXQoSQueueStatisticsEgressIfIndex": hwXQoSQueueStatisticsEgressIfIndex,
       "hwXQoSQueueStatisticsQueueIndex": hwXQoSQueueStatisticsQueueIndex,
       "hwXQoSQueueStatisticsPassedPacketsCount": hwXQoSQueueStatisticsPassedPacketsCount,
       "hwXQosQueueStatisticsReset": hwXQosQueueStatisticsReset,
       "hwXQoSQueueStatisticsRowStatus": hwXQoSQueueStatisticsRowStatus,
       "hwXQoSPortStatisticsDropObjects": hwXQoSPortStatisticsDropObjects,
       "hwXQoSPortStatisticsDropTable": hwXQoSPortStatisticsDropTable,
       "hwXQoSPortStatisticsDropEntry": hwXQoSPortStatisticsDropEntry,
       "hwXQoSPortStatisticsDropIfIndex": hwXQoSPortStatisticsDropIfIndex,
       "hwXQoSPortStatisticsDropPacketsCount": hwXQoSPortStatisticsDropPacketsCount,
       "hwXQosPortStatisticsDropReset": hwXQosPortStatisticsDropReset,
       "hwXQosPortStatisticsDropResetTime": hwXQosPortStatisticsDropResetTime,
       "hwXQoSQueueStatisticsDropObjects": hwXQoSQueueStatisticsDropObjects,
       "hwXQoSQueueStatisticsDropTable": hwXQoSQueueStatisticsDropTable,
       "hwXQoSQueueStatisticsDropEntry": hwXQoSQueueStatisticsDropEntry,
       "hwXQoSQueueStatisticsDropIfIndex": hwXQoSQueueStatisticsDropIfIndex,
       "hwXQoSQueueStatisticsDropQueueIndex": hwXQoSQueueStatisticsDropQueueIndex,
       "hwXQoSQueueStatisticsDropPacketsCount": hwXQoSQueueStatisticsDropPacketsCount,
       "hwXQosQueueStatisticsDropReset": hwXQosQueueStatisticsDropReset,
       "hwXQosQueueStatisticsDropResetTime": hwXQosQueueStatisticsDropResetTime,
       "hwXQoSRuleFailObjects": hwXQoSRuleFailObjects,
       "hwXQoSRuleFailTable": hwXQoSRuleFailTable,
       "hwXQoSRuleFailEntry": hwXQoSRuleFailEntry,
       "hwXQoSRuleFailInfo": hwXQoSRuleFailInfo,
       "hwXQoSProfileObjects": hwXQoSProfileObjects,
       "hwXQoSProfileTable": hwXQoSProfileTable,
       "hwXQoSProfileEntry": hwXQoSProfileEntry,
       "hwXQoSProfileName": hwXQoSProfileName,
       "hwXQoSPortQueueAlarmObjects": hwXQoSPortQueueAlarmObjects,
       "hwXQoSPortQueueAlarmTable": hwXQoSPortQueueAlarmTable,
       "hwXQoSPortQueueAlarmEntry": hwXQoSPortQueueAlarmEntry,
       "hwXQoSPortQueueAlarmIfIndex": hwXQoSPortQueueAlarmIfIndex,
       "hwXQoSPortQueueAlarmQueue": hwXQoSPortQueueAlarmQueue,
       "hwXQoSPortQueueAlarmTrunkIndex": hwXQoSPortQueueAlarmTrunkIndex,
       "hwXQoSSecurityStormControlInterfaceObjects": hwXQoSSecurityStormControlInterfaceObjects,
       "hwXQoSSecurityStormControlInterfaceTable": hwXQoSSecurityStormControlInterfaceTable,
       "hwXQoSSecurityStormControlInterfaceEntry": hwXQoSSecurityStormControlInterfaceEntry,
       "hwXQoSSecurityStormControlInterfaceChassisId": hwXQoSSecurityStormControlInterfaceChassisId,
       "hwXQoSSecurityStormControlInterfaceSlotId": hwXQoSSecurityStormControlInterfaceSlotId,
       "hwXQoSSecurityStormControlInterfaceName": hwXQoSSecurityStormControlInterfaceName,
       "hwXQoSSecurityStormControlInterfaceVlan": hwXQoSSecurityStormControlInterfaceVlan,
       "hwXQoSResouceNotEnoughAlarmObjects": hwXQoSResouceNotEnoughAlarmObjects,
       "hwXQoSStatResouceNotEnoughAlarmTable": hwXQoSStatResouceNotEnoughAlarmTable,
       "hwXQoSStatResouceNotEnoughAlarmEntry": hwXQoSStatResouceNotEnoughAlarmEntry,
       "hwXQoSStatResouceNotEnoughSlotId": hwXQoSStatResouceNotEnoughSlotId,
       "hwXQoSStatResouceNotEnoughStatType": hwXQoSStatResouceNotEnoughStatType,
       "hwXQoSCARResouceNotEnoughAlarmTable": hwXQoSCARResouceNotEnoughAlarmTable,
       "hwXQoSCARResouceNotEnoughAlarmEntry": hwXQoSCARResouceNotEnoughAlarmEntry,
       "hwXQoSCARResouceNotEnoughSlotId": hwXQoSCARResouceNotEnoughSlotId,
       "hwXQoSCARResouceNotEnoughCARType": hwXQoSCARResouceNotEnoughCARType,
       "hwXQoSConformance": hwXQoSConformance,
       "hwXQoSCompliances": hwXQoSCompliances,
       "hwXQoSCompliance": hwXQoSCompliance,
       "hwXQoSGroups": hwXQoSGroups,
       "hwXQoSIfQueueGroup": hwXQoSIfQueueGroup,
       "hwXQoSIfCarStatisticsGroup": hwXQoSIfCarStatisticsGroup,
       "hwXQoSCpDefendStatisticsGroup": hwXQoSCpDefendStatisticsGroup,
       "hwNotificationExtGroup": hwNotificationExtGroup,
       "hwXQoSGeneralGroup": hwXQoSGeneralGroup,
       "hwXQoSSredGroup": hwXQoSSredGroup,
       "hwXQosAtmTrafficQueueGroup": hwXQosAtmTrafficQueueGroup,
       "hwXQosAtmPvcServiceTypeGroup": hwXQosAtmPvcServiceTypeGroup,
       "hwXQosIfOutboundQueueStatisticGroup": hwXQosIfOutboundQueueStatisticGroup,
       "hwXQoSShapingGroup": hwXQoSShapingGroup,
       "hwXQoSUrpfDiscardStatisticsGroup": hwXQoSUrpfDiscardStatisticsGroup,
       "hwXQoSBaGroup": hwXQoSBaGroup,
       "hwXQoSBa8021pPhbGroup": hwXQoSBa8021pPhbGroup,
       "hwXQoSBa8021pMapGroup": hwXQoSBa8021pMapGroup,
       "hwXQoSBaDscpPhbGroup": hwXQoSBaDscpPhbGroup,
       "hwXQoSBaDscpMapGroup": hwXQoSBaDscpMapGroup,
       "hwXQoSBaExpPhbGroup": hwXQoSBaExpPhbGroup,
       "hwXQoSBaExpMapGroup": hwXQoSBaExpMapGroup,
       "hwXQoSIfDiffDomainGroup": hwXQoSIfDiffDomainGroup,
       "hwXQoSBaPhbGroup": hwXQoSBaPhbGroup,
       "hwXQoSBaMapGroup": hwXQoSBaMapGroup,
       "hwXQoSIfTrustGroup": hwXQoSIfTrustGroup,
       "hwXQosVlanStatGroup": hwXQosVlanStatGroup,
       "hwXQoSVlanCfgGroup": hwXQoSVlanCfgGroup,
       "hwXQoSStormControlGroup": hwXQoSStormControlGroup,
       "hwXQoSQueueStatisticsGroup": hwXQoSQueueStatisticsGroup,
       "hwXQoSIfPppoeGroup": hwXQoSIfPppoeGroup,
       "hwXQoSVlanBcastSuppressGroup": hwXQoSVlanBcastSuppressGroup,
       "hwXQoSRedirectNextHopGroup": hwXQoSRedirectNextHopGroup,
       "hwXQoSIfTrust8021pGroup": hwXQoSIfTrust8021pGroup,
       "hwXQoSCommonInboundGroup": hwXQoSCommonInboundGroup,
       "hwXQoSPppInboundGroup": hwXQoSPppInboundGroup,
       "hwXQoSServiceclassGroup": hwXQoSServiceclassGroup,
       "hwXQoSPhbGroup": hwXQoSPhbGroup,
       "hwXQoSFieldDeiGroup": hwXQoSFieldDeiGroup,
       "hwXQoSPicForwardingGroup": hwXQoSPicForwardingGroup,
       "hwXQoSCarTableGroup": hwXQoSCarTableGroup,
       "hwXQoSPortShapingGroup": hwXQoSPortShapingGroup,
       "hwXQoSQueueGroup": hwXQoSQueueGroup,
       "hwXQoSCarStatisticsGroup": hwXQoSCarStatisticsGroup,
       "hwXQoSCpRateLimitGroup": hwXQoSCpRateLimitGroup,
       "hwXQoSPortQueueStatisticsGroup": hwXQoSPortQueueStatisticsGroup,
       "hwXQoSPortStatisticsDropGroup": hwXQoSPortStatisticsDropGroup,
       "hwXQoSQueueStatisticsDropGroup": hwXQoSQueueStatisticsDropGroup,
       "hwXQoSIfScheduleGroup": hwXQoSIfScheduleGroup,
       "hwXQoSScheduleProfileGroup": hwXQoSScheduleProfileGroup,
       "hwXQoSQppbPolicyGroup": hwXQoSQppbPolicyGroup,
       "hwXQoSStatResouceNotEnoughAlarmGroup": hwXQoSStatResouceNotEnoughAlarmGroup,
       "hwXQoSCARResouceNotEnoughAlarmGroup": hwXQoSCARResouceNotEnoughAlarmGroup}
)
