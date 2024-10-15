# SNMP MIB module (HUAWEI-FR-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-FR-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:50 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hwFrQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



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



# MIB Managed Objects in the order of their OIDs

_HwQoS_ObjectIdentity = ObjectIdentity
hwQoS = _HwQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32)
)
_HwFrQoSObjects_ObjectIdentity = ObjectIdentity
hwFrQoSObjects = _HwFrQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1)
)
_HwFrClassObjects_ObjectIdentity = ObjectIdentity
hwFrClassObjects = _HwFrClassObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1)
)
_HwFrClassIndexNext_Type = Integer32
_HwFrClassIndexNext_Object = MibScalar
hwFrClassIndexNext = _HwFrClassIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 1),
    _HwFrClassIndexNext_Type()
)
hwFrClassIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrClassIndexNext.setStatus("current")
_HwFrClassCfgInfoTable_Object = MibTable
hwFrClassCfgInfoTable = _HwFrClassCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwFrClassCfgInfoTable.setStatus("current")
_HwFrClassCfgInfoEntry_Object = MibTableRow
hwFrClassCfgInfoEntry = _HwFrClassCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 2, 1)
)
hwFrClassCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwFrClassIndex"),
)
if mibBuilder.loadTexts:
    hwFrClassCfgInfoEntry.setStatus("current")
_HwFrClassIndex_Type = Integer32
_HwFrClassIndex_Object = MibTableColumn
hwFrClassIndex = _HwFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 2, 1, 1),
    _HwFrClassIndex_Type()
)
hwFrClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrClassIndex.setStatus("current")


class _HwFrClassName_Type(OctetString):
    """Custom type hwFrClassName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwFrClassName_Type.__name__ = "OctetString"
_HwFrClassName_Object = MibTableColumn
hwFrClassName = _HwFrClassName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 2, 1, 2),
    _HwFrClassName_Type()
)
hwFrClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFrClassName.setStatus("current")
_HwFrClassRowStatus_Type = RowStatus
_HwFrClassRowStatus_Object = MibTableColumn
hwFrClassRowStatus = _HwFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 2, 1, 3),
    _HwFrClassRowStatus_Type()
)
hwFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFrClassRowStatus.setStatus("current")
_HwCirAllowCfgInfoTable_Object = MibTable
hwCirAllowCfgInfoTable = _HwCirAllowCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwCirAllowCfgInfoTable.setStatus("current")
_HwCirAllowCfgInfoEntry_Object = MibTableRow
hwCirAllowCfgInfoEntry = _HwCirAllowCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 3, 1)
)
hwCirAllowCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwCirAllowFrClassIndex"),
    (0, "HUAWEI-FR-QOS-MIB", "hwCirAllowDirection"),
)
if mibBuilder.loadTexts:
    hwCirAllowCfgInfoEntry.setStatus("current")
_HwCirAllowFrClassIndex_Type = Integer32
_HwCirAllowFrClassIndex_Object = MibTableColumn
hwCirAllowFrClassIndex = _HwCirAllowFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 3, 1, 1),
    _HwCirAllowFrClassIndex_Type()
)
hwCirAllowFrClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCirAllowFrClassIndex.setStatus("current")
_HwCirAllowDirection_Type = Integer32
_HwCirAllowDirection_Object = MibTableColumn
hwCirAllowDirection = _HwCirAllowDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 3, 1, 2),
    _HwCirAllowDirection_Type()
)
hwCirAllowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCirAllowDirection.setStatus("current")


class _HwCirAllowValue_Type(Integer32):
    """Custom type hwCirAllowValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_HwCirAllowValue_Type.__name__ = "Integer32"
_HwCirAllowValue_Object = MibTableColumn
hwCirAllowValue = _HwCirAllowValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 3, 1, 3),
    _HwCirAllowValue_Type()
)
hwCirAllowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCirAllowValue.setStatus("current")
_HwCirAllowRowStatus_Type = RowStatus
_HwCirAllowRowStatus_Object = MibTableColumn
hwCirAllowRowStatus = _HwCirAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 3, 1, 4),
    _HwCirAllowRowStatus_Type()
)
hwCirAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCirAllowRowStatus.setStatus("current")
_HwCirCfgInfoTable_Object = MibTable
hwCirCfgInfoTable = _HwCirCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwCirCfgInfoTable.setStatus("current")
_HwCirCfgInfoEntry_Object = MibTableRow
hwCirCfgInfoEntry = _HwCirCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 4, 1)
)
hwCirCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwCirFrClassIndex"),
)
if mibBuilder.loadTexts:
    hwCirCfgInfoEntry.setStatus("current")
_HwCirFrClassIndex_Type = Integer32
_HwCirFrClassIndex_Object = MibTableColumn
hwCirFrClassIndex = _HwCirFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 4, 1, 1),
    _HwCirFrClassIndex_Type()
)
hwCirFrClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCirFrClassIndex.setStatus("current")


class _HwCirValue_Type(Integer32):
    """Custom type hwCirValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 45000000),
    )


_HwCirValue_Type.__name__ = "Integer32"
_HwCirValue_Object = MibTableColumn
hwCirValue = _HwCirValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 4, 1, 2),
    _HwCirValue_Type()
)
hwCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCirValue.setStatus("current")
_HwCirRowStatus_Type = RowStatus
_HwCirRowStatus_Object = MibTableColumn
hwCirRowStatus = _HwCirRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 4, 1, 3),
    _HwCirRowStatus_Type()
)
hwCirRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCirRowStatus.setStatus("current")
_HwIfApplyFrClassTable_Object = MibTable
hwIfApplyFrClassTable = _HwIfApplyFrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwIfApplyFrClassTable.setStatus("current")
_HwIfApplyFrClassEntry_Object = MibTableRow
hwIfApplyFrClassEntry = _HwIfApplyFrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 5, 1)
)
hwIfApplyFrClassEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwIfApplyFrClassIfIndex"),
)
if mibBuilder.loadTexts:
    hwIfApplyFrClassEntry.setStatus("current")
_HwIfApplyFrClassIfIndex_Type = Integer32
_HwIfApplyFrClassIfIndex_Object = MibTableColumn
hwIfApplyFrClassIfIndex = _HwIfApplyFrClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 5, 1, 1),
    _HwIfApplyFrClassIfIndex_Type()
)
hwIfApplyFrClassIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIfApplyFrClassIfIndex.setStatus("current")
_HwIfApplyFrClassIndex_Type = Integer32
_HwIfApplyFrClassIndex_Object = MibTableColumn
hwIfApplyFrClassIndex = _HwIfApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 5, 1, 2),
    _HwIfApplyFrClassIndex_Type()
)
hwIfApplyFrClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfApplyFrClassIndex.setStatus("current")
_HwIfApplyFrClassRowStatus_Type = RowStatus
_HwIfApplyFrClassRowStatus_Object = MibTableColumn
hwIfApplyFrClassRowStatus = _HwIfApplyFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 5, 1, 3),
    _HwIfApplyFrClassRowStatus_Type()
)
hwIfApplyFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIfApplyFrClassRowStatus.setStatus("current")
_HwPvcApplyFrClassTable_Object = MibTable
hwPvcApplyFrClassTable = _HwPvcApplyFrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwPvcApplyFrClassTable.setStatus("current")
_HwPvcApplyFrClassEntry_Object = MibTableRow
hwPvcApplyFrClassEntry = _HwPvcApplyFrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 6, 1)
)
hwPvcApplyFrClassEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwPvcApplyFrClassIfIndex"),
    (0, "HUAWEI-FR-QOS-MIB", "hwPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hwPvcApplyFrClassEntry.setStatus("current")
_HwPvcApplyFrClassIfIndex_Type = Integer32
_HwPvcApplyFrClassIfIndex_Object = MibTableColumn
hwPvcApplyFrClassIfIndex = _HwPvcApplyFrClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 6, 1, 1),
    _HwPvcApplyFrClassIfIndex_Type()
)
hwPvcApplyFrClassIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPvcApplyFrClassIfIndex.setStatus("current")


class _HwPvcApplyFrClassDlciNum_Type(Integer32):
    """Custom type hwPvcApplyFrClassDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_HwPvcApplyFrClassDlciNum_Type.__name__ = "Integer32"
_HwPvcApplyFrClassDlciNum_Object = MibTableColumn
hwPvcApplyFrClassDlciNum = _HwPvcApplyFrClassDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 6, 1, 2),
    _HwPvcApplyFrClassDlciNum_Type()
)
hwPvcApplyFrClassDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPvcApplyFrClassDlciNum.setStatus("current")
_HwPvcApplyFrClassIndex_Type = Integer32
_HwPvcApplyFrClassIndex_Object = MibTableColumn
hwPvcApplyFrClassIndex = _HwPvcApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 6, 1, 3),
    _HwPvcApplyFrClassIndex_Type()
)
hwPvcApplyFrClassIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPvcApplyFrClassIndex.setStatus("current")
_HwPvcApplyFrClassRowStatus_Type = RowStatus
_HwPvcApplyFrClassRowStatus_Object = MibTableColumn
hwPvcApplyFrClassRowStatus = _HwPvcApplyFrClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 6, 1, 4),
    _HwPvcApplyFrClassRowStatus_Type()
)
hwPvcApplyFrClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPvcApplyFrClassRowStatus.setStatus("current")
_HwFrPvcBandwidthTable_Object = MibTable
hwFrPvcBandwidthTable = _HwFrPvcBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwFrPvcBandwidthTable.setStatus("current")
_HwFrPvcBandwidthEntry_Object = MibTableRow
hwFrPvcBandwidthEntry = _HwFrPvcBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 7, 1)
)
hwFrPvcBandwidthEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwPvcApplyFrClassIfIndex"),
    (0, "HUAWEI-FR-QOS-MIB", "hwPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hwFrPvcBandwidthEntry.setStatus("current")
_HwFrPvcBandwidthMaxReservedBW_Type = Integer32
_HwFrPvcBandwidthMaxReservedBW_Object = MibTableColumn
hwFrPvcBandwidthMaxReservedBW = _HwFrPvcBandwidthMaxReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 7, 1, 1),
    _HwFrPvcBandwidthMaxReservedBW_Type()
)
hwFrPvcBandwidthMaxReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcBandwidthMaxReservedBW.setStatus("current")
_HwFrPvcBandwidthAvailable_Type = Integer32
_HwFrPvcBandwidthAvailable_Object = MibTableColumn
hwFrPvcBandwidthAvailable = _HwFrPvcBandwidthAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 1, 7, 1, 2),
    _HwFrPvcBandwidthAvailable_Type()
)
hwFrPvcBandwidthAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrPvcBandwidthAvailable.setStatus("current")
_HwRTPQoSObjects_ObjectIdentity = ObjectIdentity
hwRTPQoSObjects = _HwRTPQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2)
)
_HwRTPFrClassApplyTable_Object = MibTable
hwRTPFrClassApplyTable = _HwRTPFrClassApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwRTPFrClassApplyTable.setStatus("current")
_HwRTPFrClassApplyEntry_Object = MibTableRow
hwRTPFrClassApplyEntry = _HwRTPFrClassApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1)
)
hwRTPFrClassApplyEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwRTPFrClassApplyFrClassIndex"),
)
if mibBuilder.loadTexts:
    hwRTPFrClassApplyEntry.setStatus("current")
_HwRTPFrClassApplyFrClassIndex_Type = Integer32
_HwRTPFrClassApplyFrClassIndex_Object = MibTableColumn
hwRTPFrClassApplyFrClassIndex = _HwRTPFrClassApplyFrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1, 1),
    _HwRTPFrClassApplyFrClassIndex_Type()
)
hwRTPFrClassApplyFrClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRTPFrClassApplyFrClassIndex.setStatus("current")


class _HwRTPFrClassApplyStartPort_Type(Integer32):
    """Custom type hwRTPFrClassApplyStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_HwRTPFrClassApplyStartPort_Type.__name__ = "Integer32"
_HwRTPFrClassApplyStartPort_Object = MibTableColumn
hwRTPFrClassApplyStartPort = _HwRTPFrClassApplyStartPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1, 2),
    _HwRTPFrClassApplyStartPort_Type()
)
hwRTPFrClassApplyStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRTPFrClassApplyStartPort.setStatus("current")


class _HwRTPFrClassApplyEndPort_Type(Integer32):
    """Custom type hwRTPFrClassApplyEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_HwRTPFrClassApplyEndPort_Type.__name__ = "Integer32"
_HwRTPFrClassApplyEndPort_Object = MibTableColumn
hwRTPFrClassApplyEndPort = _HwRTPFrClassApplyEndPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1, 3),
    _HwRTPFrClassApplyEndPort_Type()
)
hwRTPFrClassApplyEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRTPFrClassApplyEndPort.setStatus("current")


class _HwRTPFrClassApplyBandWidth_Type(Integer32):
    """Custom type hwRTPFrClassApplyBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_HwRTPFrClassApplyBandWidth_Type.__name__ = "Integer32"
_HwRTPFrClassApplyBandWidth_Object = MibTableColumn
hwRTPFrClassApplyBandWidth = _HwRTPFrClassApplyBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1, 4),
    _HwRTPFrClassApplyBandWidth_Type()
)
hwRTPFrClassApplyBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRTPFrClassApplyBandWidth.setStatus("current")


class _HwRTPFrClassApplyCbs_Type(Integer32):
    """Custom type hwRTPFrClassApplyCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 2000000),
    )


_HwRTPFrClassApplyCbs_Type.__name__ = "Integer32"
_HwRTPFrClassApplyCbs_Object = MibTableColumn
hwRTPFrClassApplyCbs = _HwRTPFrClassApplyCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1, 5),
    _HwRTPFrClassApplyCbs_Type()
)
hwRTPFrClassApplyCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRTPFrClassApplyCbs.setStatus("current")
_HwRTPFrClassApplyRowStatus_Type = RowStatus
_HwRTPFrClassApplyRowStatus_Object = MibTableColumn
hwRTPFrClassApplyRowStatus = _HwRTPFrClassApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 1, 1, 6),
    _HwRTPFrClassApplyRowStatus_Type()
)
hwRTPFrClassApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRTPFrClassApplyRowStatus.setStatus("current")
_HwRTPFrPvcQueueRunInfoTable_Object = MibTable
hwRTPFrPvcQueueRunInfoTable = _HwRTPFrPvcQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwRTPFrPvcQueueRunInfoTable.setStatus("current")
_HwRTPFrPvcQueueRunInfoEntry_Object = MibTableRow
hwRTPFrPvcQueueRunInfoEntry = _HwRTPFrPvcQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 2, 1)
)
hwRTPFrPvcQueueRunInfoEntry.setIndexNames(
    (0, "HUAWEI-FR-QOS-MIB", "hwPvcApplyFrClassIfIndex"),
    (0, "HUAWEI-FR-QOS-MIB", "hwPvcApplyFrClassDlciNum"),
)
if mibBuilder.loadTexts:
    hwRTPFrPvcQueueRunInfoEntry.setStatus("current")
_HwRTPFrPvcQueueSize_Type = Integer32
_HwRTPFrPvcQueueSize_Object = MibTableColumn
hwRTPFrPvcQueueSize = _HwRTPFrPvcQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 2, 1, 1),
    _HwRTPFrPvcQueueSize_Type()
)
hwRTPFrPvcQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRTPFrPvcQueueSize.setStatus("current")
_HwRTPFrPvcQueueMaxSize_Type = Integer32
_HwRTPFrPvcQueueMaxSize_Object = MibTableColumn
hwRTPFrPvcQueueMaxSize = _HwRTPFrPvcQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 2, 1, 2),
    _HwRTPFrPvcQueueMaxSize_Type()
)
hwRTPFrPvcQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRTPFrPvcQueueMaxSize.setStatus("current")
_HwRTPFrPvcQueueOutputs_Type = Counter32
_HwRTPFrPvcQueueOutputs_Object = MibTableColumn
hwRTPFrPvcQueueOutputs = _HwRTPFrPvcQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 2, 1, 3),
    _HwRTPFrPvcQueueOutputs_Type()
)
hwRTPFrPvcQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRTPFrPvcQueueOutputs.setStatus("current")
_HwRTPFrPvcQueueDiscards_Type = Counter32
_HwRTPFrPvcQueueDiscards_Object = MibTableColumn
hwRTPFrPvcQueueDiscards = _HwRTPFrPvcQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 3, 1, 2, 2, 1, 4),
    _HwRTPFrPvcQueueDiscards_Type()
)
hwRTPFrPvcQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRTPFrPvcQueueDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-FR-QOS-MIB",
    **{"DirectionType": DirectionType,
       "hwQoS": hwQoS,
       "hwFrQoSMib": hwFrQoSMib,
       "hwFrQoSObjects": hwFrQoSObjects,
       "hwFrClassObjects": hwFrClassObjects,
       "hwFrClassIndexNext": hwFrClassIndexNext,
       "hwFrClassCfgInfoTable": hwFrClassCfgInfoTable,
       "hwFrClassCfgInfoEntry": hwFrClassCfgInfoEntry,
       "hwFrClassIndex": hwFrClassIndex,
       "hwFrClassName": hwFrClassName,
       "hwFrClassRowStatus": hwFrClassRowStatus,
       "hwCirAllowCfgInfoTable": hwCirAllowCfgInfoTable,
       "hwCirAllowCfgInfoEntry": hwCirAllowCfgInfoEntry,
       "hwCirAllowFrClassIndex": hwCirAllowFrClassIndex,
       "hwCirAllowDirection": hwCirAllowDirection,
       "hwCirAllowValue": hwCirAllowValue,
       "hwCirAllowRowStatus": hwCirAllowRowStatus,
       "hwCirCfgInfoTable": hwCirCfgInfoTable,
       "hwCirCfgInfoEntry": hwCirCfgInfoEntry,
       "hwCirFrClassIndex": hwCirFrClassIndex,
       "hwCirValue": hwCirValue,
       "hwCirRowStatus": hwCirRowStatus,
       "hwIfApplyFrClassTable": hwIfApplyFrClassTable,
       "hwIfApplyFrClassEntry": hwIfApplyFrClassEntry,
       "hwIfApplyFrClassIfIndex": hwIfApplyFrClassIfIndex,
       "hwIfApplyFrClassIndex": hwIfApplyFrClassIndex,
       "hwIfApplyFrClassRowStatus": hwIfApplyFrClassRowStatus,
       "hwPvcApplyFrClassTable": hwPvcApplyFrClassTable,
       "hwPvcApplyFrClassEntry": hwPvcApplyFrClassEntry,
       "hwPvcApplyFrClassIfIndex": hwPvcApplyFrClassIfIndex,
       "hwPvcApplyFrClassDlciNum": hwPvcApplyFrClassDlciNum,
       "hwPvcApplyFrClassIndex": hwPvcApplyFrClassIndex,
       "hwPvcApplyFrClassRowStatus": hwPvcApplyFrClassRowStatus,
       "hwFrPvcBandwidthTable": hwFrPvcBandwidthTable,
       "hwFrPvcBandwidthEntry": hwFrPvcBandwidthEntry,
       "hwFrPvcBandwidthMaxReservedBW": hwFrPvcBandwidthMaxReservedBW,
       "hwFrPvcBandwidthAvailable": hwFrPvcBandwidthAvailable,
       "hwRTPQoSObjects": hwRTPQoSObjects,
       "hwRTPFrClassApplyTable": hwRTPFrClassApplyTable,
       "hwRTPFrClassApplyEntry": hwRTPFrClassApplyEntry,
       "hwRTPFrClassApplyFrClassIndex": hwRTPFrClassApplyFrClassIndex,
       "hwRTPFrClassApplyStartPort": hwRTPFrClassApplyStartPort,
       "hwRTPFrClassApplyEndPort": hwRTPFrClassApplyEndPort,
       "hwRTPFrClassApplyBandWidth": hwRTPFrClassApplyBandWidth,
       "hwRTPFrClassApplyCbs": hwRTPFrClassApplyCbs,
       "hwRTPFrClassApplyRowStatus": hwRTPFrClassApplyRowStatus,
       "hwRTPFrPvcQueueRunInfoTable": hwRTPFrPvcQueueRunInfoTable,
       "hwRTPFrPvcQueueRunInfoEntry": hwRTPFrPvcQueueRunInfoEntry,
       "hwRTPFrPvcQueueSize": hwRTPFrPvcQueueSize,
       "hwRTPFrPvcQueueMaxSize": hwRTPFrPvcQueueMaxSize,
       "hwRTPFrPvcQueueOutputs": hwRTPFrPvcQueueOutputs,
       "hwRTPFrPvcQueueDiscards": hwRTPFrPvcQueueDiscards}
)
