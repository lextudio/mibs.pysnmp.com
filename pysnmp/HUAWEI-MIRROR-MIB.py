# SNMP MIB module (HUAWEI-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MIRROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:02 2024
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

(huaweiMgmt,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwMirrorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMirrorMIBObjects_ObjectIdentity = ObjectIdentity
hwMirrorMIBObjects = _HwMirrorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1)
)
_HwLocalMirror_ObjectIdentity = ObjectIdentity
hwLocalMirror = _HwLocalMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1)
)
_HwLocalObserveTable_Object = MibTable
hwLocalObserveTable = _HwLocalObserveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwLocalObserveTable.setStatus("current")
_HwLocalObserveEntry_Object = MibTableRow
hwLocalObserveEntry = _HwLocalObserveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1)
)
hwLocalObserveEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwLocalObservePort"),
)
if mibBuilder.loadTexts:
    hwLocalObserveEntry.setStatus("current")
_HwLocalObservePort_Type = InterfaceIndex
_HwLocalObservePort_Object = MibTableColumn
hwLocalObservePort = _HwLocalObservePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 1),
    _HwLocalObservePort_Type()
)
hwLocalObservePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLocalObservePort.setStatus("current")


class _HwLocalObserveIndex_Type(Integer32):
    """Custom type hwLocalObserveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwLocalObserveIndex_Type.__name__ = "Integer32"
_HwLocalObserveIndex_Object = MibTableColumn
hwLocalObserveIndex = _HwLocalObserveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 2),
    _HwLocalObserveIndex_Type()
)
hwLocalObserveIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalObserveIndex.setStatus("current")


class _HwLocalObserveWithLinkLayerHeader_Type(Integer32):
    """Custom type hwLocalObserveWithLinkLayerHeader based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwLocalObserveWithLinkLayerHeader_Type.__name__ = "Integer32"
_HwLocalObserveWithLinkLayerHeader_Object = MibTableColumn
hwLocalObserveWithLinkLayerHeader = _HwLocalObserveWithLinkLayerHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 3),
    _HwLocalObserveWithLinkLayerHeader_Type()
)
hwLocalObserveWithLinkLayerHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalObserveWithLinkLayerHeader.setStatus("current")
_HwLocalObserveRowStatus_Type = RowStatus
_HwLocalObserveRowStatus_Object = MibTableColumn
hwLocalObserveRowStatus = _HwLocalObserveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 1, 1, 4),
    _HwLocalObserveRowStatus_Type()
)
hwLocalObserveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalObserveRowStatus.setStatus("current")
_HwLocalPortMirrorTable_Object = MibTable
hwLocalPortMirrorTable = _HwLocalPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwLocalPortMirrorTable.setStatus("current")
_HwLocalPortMirrorEntry_Object = MibTableRow
hwLocalPortMirrorEntry = _HwLocalPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1)
)
hwLocalPortMirrorEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwLocalMirrorPort"),
)
if mibBuilder.loadTexts:
    hwLocalPortMirrorEntry.setStatus("current")
_HwLocalMirrorPort_Type = InterfaceIndex
_HwLocalMirrorPort_Object = MibTableColumn
hwLocalMirrorPort = _HwLocalMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 1),
    _HwLocalMirrorPort_Type()
)
hwLocalMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLocalMirrorPort.setStatus("current")


class _HwLocalMirrorBearing_Type(Integer32):
    """Custom type hwLocalMirrorBearing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwLocalMirrorBearing_Type.__name__ = "Integer32"
_HwLocalMirrorBearing_Object = MibTableColumn
hwLocalMirrorBearing = _HwLocalMirrorBearing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 2),
    _HwLocalMirrorBearing_Type()
)
hwLocalMirrorBearing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalMirrorBearing.setStatus("current")


class _HwLocalCpuPacketFlag_Type(TruthValue):
    """Custom type hwLocalCpuPacketFlag based on TruthValue"""


_HwLocalCpuPacketFlag_Object = MibTableColumn
hwLocalCpuPacketFlag = _HwLocalCpuPacketFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 3),
    _HwLocalCpuPacketFlag_Type()
)
hwLocalCpuPacketFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalCpuPacketFlag.setStatus("current")


class _HwLocalPortMirrorCar_Type(Integer32):
    """Custom type hwLocalPortMirrorCar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 2500000),
    )


_HwLocalPortMirrorCar_Type.__name__ = "Integer32"
_HwLocalPortMirrorCar_Object = MibTableColumn
hwLocalPortMirrorCar = _HwLocalPortMirrorCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 4),
    _HwLocalPortMirrorCar_Type()
)
hwLocalPortMirrorCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalPortMirrorCar.setStatus("current")
if mibBuilder.loadTexts:
    hwLocalPortMirrorCar.setUnits("Kbps")
_HwLocalPortMirrorRowStatus_Type = RowStatus
_HwLocalPortMirrorRowStatus_Object = MibTableColumn
hwLocalPortMirrorRowStatus = _HwLocalPortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 2, 1, 5),
    _HwLocalPortMirrorRowStatus_Type()
)
hwLocalPortMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalPortMirrorRowStatus.setStatus("current")
_HwLocalFlowMirrorTable_Object = MibTable
hwLocalFlowMirrorTable = _HwLocalFlowMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwLocalFlowMirrorTable.setStatus("current")
_HwLocalFlowMirrorEntry_Object = MibTableRow
hwLocalFlowMirrorEntry = _HwLocalFlowMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1)
)
hwLocalFlowMirrorEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwLocalBehaviorName"),
)
if mibBuilder.loadTexts:
    hwLocalFlowMirrorEntry.setStatus("current")


class _HwLocalBehaviorName_Type(OctetString):
    """Custom type hwLocalBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwLocalBehaviorName_Type.__name__ = "OctetString"
_HwLocalBehaviorName_Object = MibTableColumn
hwLocalBehaviorName = _HwLocalBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 1),
    _HwLocalBehaviorName_Type()
)
hwLocalBehaviorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLocalBehaviorName.setStatus("current")


class _HwLocalFlowMirrorEnable_Type(EnabledStatus):
    """Custom type hwLocalFlowMirrorEnable based on EnabledStatus"""
    defaultValue = 2


_HwLocalFlowMirrorEnable_Object = MibTableColumn
hwLocalFlowMirrorEnable = _HwLocalFlowMirrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 2),
    _HwLocalFlowMirrorEnable_Type()
)
hwLocalFlowMirrorEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalFlowMirrorEnable.setStatus("current")


class _HwLocalFlowMirrorCar_Type(Integer32):
    """Custom type hwLocalFlowMirrorCar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 2500000),
    )


_HwLocalFlowMirrorCar_Type.__name__ = "Integer32"
_HwLocalFlowMirrorCar_Object = MibTableColumn
hwLocalFlowMirrorCar = _HwLocalFlowMirrorCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 3),
    _HwLocalFlowMirrorCar_Type()
)
hwLocalFlowMirrorCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalFlowMirrorCar.setStatus("current")
if mibBuilder.loadTexts:
    hwLocalFlowMirrorCar.setUnits("Kbps")
_HwLocalFlowMirrorRowStatus_Type = RowStatus
_HwLocalFlowMirrorRowStatus_Object = MibTableColumn
hwLocalFlowMirrorRowStatus = _HwLocalFlowMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 3, 1, 4),
    _HwLocalFlowMirrorRowStatus_Type()
)
hwLocalFlowMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalFlowMirrorRowStatus.setStatus("current")
_HwLocalSlotMirrorTable_Object = MibTable
hwLocalSlotMirrorTable = _HwLocalSlotMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwLocalSlotMirrorTable.setStatus("current")
_HwLocalSlotMirrorEntry_Object = MibTableRow
hwLocalSlotMirrorEntry = _HwLocalSlotMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1)
)
hwLocalSlotMirrorEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwLocalSlotNo"),
)
if mibBuilder.loadTexts:
    hwLocalSlotMirrorEntry.setStatus("current")


class _HwLocalSlotNo_Type(Integer32):
    """Custom type hwLocalSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwLocalSlotNo_Type.__name__ = "Integer32"
_HwLocalSlotNo_Object = MibTableColumn
hwLocalSlotNo = _HwLocalSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1, 1),
    _HwLocalSlotNo_Type()
)
hwLocalSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLocalSlotNo.setStatus("current")


class _HwSlotObserveIndex_Type(Integer32):
    """Custom type hwSlotObserveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwSlotObserveIndex_Type.__name__ = "Integer32"
_HwSlotObserveIndex_Object = MibTableColumn
hwSlotObserveIndex = _HwSlotObserveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1, 2),
    _HwSlotObserveIndex_Type()
)
hwSlotObserveIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotObserveIndex.setStatus("current")
_HwLocalSlotMirrorRowStatus_Type = RowStatus
_HwLocalSlotMirrorRowStatus_Object = MibTableColumn
hwLocalSlotMirrorRowStatus = _HwLocalSlotMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 4, 1, 3),
    _HwLocalSlotMirrorRowStatus_Type()
)
hwLocalSlotMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLocalSlotMirrorRowStatus.setStatus("current")
_HwPortMirrorInfoTable_Object = MibTable
hwPortMirrorInfoTable = _HwPortMirrorInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwPortMirrorInfoTable.setStatus("current")
_HwPortMirrorInfoEntry_Object = MibTableRow
hwPortMirrorInfoEntry = _HwPortMirrorInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1)
)
hwPortMirrorInfoEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwMirrorPortIndex"),
)
if mibBuilder.loadTexts:
    hwPortMirrorInfoEntry.setStatus("current")
_HwMirrorPortIndex_Type = InterfaceIndex
_HwMirrorPortIndex_Object = MibTableColumn
hwMirrorPortIndex = _HwMirrorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 1),
    _HwMirrorPortIndex_Type()
)
hwMirrorPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMirrorPortIndex.setStatus("current")


class _HwMirrorType_Type(Integer32):
    """Custom type hwMirrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_HwMirrorType_Type.__name__ = "Integer32"
_HwMirrorType_Object = MibTableColumn
hwMirrorType = _HwMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 2),
    _HwMirrorType_Type()
)
hwMirrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorType.setStatus("current")


class _HwMirrorCar_Type(Integer32):
    """Custom type hwMirrorCar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 2500000),
    )


_HwMirrorCar_Type.__name__ = "Integer32"
_HwMirrorCar_Object = MibTableColumn
hwMirrorCar = _HwMirrorCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 3),
    _HwMirrorCar_Type()
)
hwMirrorCar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorCar.setStatus("current")
if mibBuilder.loadTexts:
    hwMirrorCar.setUnits("Kbps")


class _HwMirrorClass_Type(Integer32):
    """Custom type hwMirrorClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("policy", 2),
          ("port", 1))
    )


_HwMirrorClass_Type.__name__ = "Integer32"
_HwMirrorClass_Object = MibTableColumn
hwMirrorClass = _HwMirrorClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 4),
    _HwMirrorClass_Type()
)
hwMirrorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorClass.setStatus("current")


class _HwMirrorBearing_Type(Integer32):
    """Custom type hwMirrorBearing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwMirrorBearing_Type.__name__ = "Integer32"
_HwMirrorBearing_Object = MibTableColumn
hwMirrorBearing = _HwMirrorBearing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 5),
    _HwMirrorBearing_Type()
)
hwMirrorBearing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorBearing.setStatus("current")


class _HwMirrorCpuPacketFlag_Type(TruthValue):
    """Custom type hwMirrorCpuPacketFlag based on TruthValue"""


_HwMirrorCpuPacketFlag_Object = MibTableColumn
hwMirrorCpuPacketFlag = _HwMirrorCpuPacketFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 6),
    _HwMirrorCpuPacketFlag_Type()
)
hwMirrorCpuPacketFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorCpuPacketFlag.setStatus("current")


class _HwMirrorWithLinkLayerHeader_Type(Integer32):
    """Custom type hwMirrorWithLinkLayerHeader based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMirrorWithLinkLayerHeader_Type.__name__ = "Integer32"
_HwMirrorWithLinkLayerHeader_Object = MibTableColumn
hwMirrorWithLinkLayerHeader = _HwMirrorWithLinkLayerHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 7),
    _HwMirrorWithLinkLayerHeader_Type()
)
hwMirrorWithLinkLayerHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorWithLinkLayerHeader.setStatus("current")


class _HwRemoteMirrorInstanceName_Type(OctetString):
    """Custom type hwRemoteMirrorInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRemoteMirrorInstanceName_Type.__name__ = "OctetString"
_HwRemoteMirrorInstanceName_Object = MibTableColumn
hwRemoteMirrorInstanceName = _HwRemoteMirrorInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 1, 5, 1, 8),
    _HwRemoteMirrorInstanceName_Type()
)
hwRemoteMirrorInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRemoteMirrorInstanceName.setStatus("current")
_HwRemoteMirror_ObjectIdentity = ObjectIdentity
hwRemoteMirror = _HwRemoteMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2)
)
_HwRemoteObserveTable_Object = MibTable
hwRemoteObserveTable = _HwRemoteObserveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwRemoteObserveTable.setStatus("current")
_HwRemoteObserveEntry_Object = MibTableRow
hwRemoteObserveEntry = _HwRemoteObserveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1)
)
hwRemoteObserveEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwRemoteObservePort"),
)
if mibBuilder.loadTexts:
    hwRemoteObserveEntry.setStatus("current")
_HwRemoteObservePort_Type = InterfaceIndex
_HwRemoteObservePort_Object = MibTableColumn
hwRemoteObservePort = _HwRemoteObservePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 1),
    _HwRemoteObservePort_Type()
)
hwRemoteObservePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemoteObservePort.setStatus("current")


class _HwRemoteIdentifier_Type(Integer32):
    """Custom type hwRemoteIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwRemoteIdentifier_Type.__name__ = "Integer32"
_HwRemoteIdentifier_Object = MibTableColumn
hwRemoteIdentifier = _HwRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 2),
    _HwRemoteIdentifier_Type()
)
hwRemoteIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteIdentifier.setStatus("current")


class _HwRemoteDescription_Type(OctetString):
    """Custom type hwRemoteDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRemoteDescription_Type.__name__ = "OctetString"
_HwRemoteDescription_Object = MibTableColumn
hwRemoteDescription = _HwRemoteDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 3),
    _HwRemoteDescription_Type()
)
hwRemoteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteDescription.setStatus("current")


class _HwRemoteObserveWithLinkLayerHeader_Type(Integer32):
    """Custom type hwRemoteObserveWithLinkLayerHeader based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRemoteObserveWithLinkLayerHeader_Type.__name__ = "Integer32"
_HwRemoteObserveWithLinkLayerHeader_Object = MibTableColumn
hwRemoteObserveWithLinkLayerHeader = _HwRemoteObserveWithLinkLayerHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 4),
    _HwRemoteObserveWithLinkLayerHeader_Type()
)
hwRemoteObserveWithLinkLayerHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteObserveWithLinkLayerHeader.setStatus("current")
_HwRemoteObserveRowStatus_Type = RowStatus
_HwRemoteObserveRowStatus_Object = MibTableColumn
hwRemoteObserveRowStatus = _HwRemoteObserveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 1, 1, 5),
    _HwRemoteObserveRowStatus_Type()
)
hwRemoteObserveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteObserveRowStatus.setStatus("current")
_HwRemotePortMirrorTable_Object = MibTable
hwRemotePortMirrorTable = _HwRemotePortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwRemotePortMirrorTable.setStatus("current")
_HwRemotePortMirrorEntry_Object = MibTableRow
hwRemotePortMirrorEntry = _HwRemotePortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1)
)
hwRemotePortMirrorEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwRemoteMirrorPort"),
)
if mibBuilder.loadTexts:
    hwRemotePortMirrorEntry.setStatus("current")
_HwRemoteMirrorPort_Type = InterfaceIndex
_HwRemoteMirrorPort_Object = MibTableColumn
hwRemoteMirrorPort = _HwRemoteMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 1),
    _HwRemoteMirrorPort_Type()
)
hwRemoteMirrorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemoteMirrorPort.setStatus("current")


class _HwRemoteMirrorBearing_Type(Integer32):
    """Custom type hwRemoteMirrorBearing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("inout", 3),
          ("outbound", 2))
    )


_HwRemoteMirrorBearing_Type.__name__ = "Integer32"
_HwRemoteMirrorBearing_Object = MibTableColumn
hwRemoteMirrorBearing = _HwRemoteMirrorBearing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 2),
    _HwRemoteMirrorBearing_Type()
)
hwRemoteMirrorBearing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteMirrorBearing.setStatus("current")


class _HwRemoteCpuPacketFlag_Type(TruthValue):
    """Custom type hwRemoteCpuPacketFlag based on TruthValue"""


_HwRemoteCpuPacketFlag_Object = MibTableColumn
hwRemoteCpuPacketFlag = _HwRemoteCpuPacketFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 3),
    _HwRemoteCpuPacketFlag_Type()
)
hwRemoteCpuPacketFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteCpuPacketFlag.setStatus("current")


class _HwPortMirrorInstanceName_Type(OctetString):
    """Custom type hwPortMirrorInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwPortMirrorInstanceName_Type.__name__ = "OctetString"
_HwPortMirrorInstanceName_Object = MibTableColumn
hwPortMirrorInstanceName = _HwPortMirrorInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 4),
    _HwPortMirrorInstanceName_Type()
)
hwPortMirrorInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortMirrorInstanceName.setStatus("current")


class _HwRemotePortMirrorCar_Type(Integer32):
    """Custom type hwRemotePortMirrorCar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 2500000),
    )


_HwRemotePortMirrorCar_Type.__name__ = "Integer32"
_HwRemotePortMirrorCar_Object = MibTableColumn
hwRemotePortMirrorCar = _HwRemotePortMirrorCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 5),
    _HwRemotePortMirrorCar_Type()
)
hwRemotePortMirrorCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemotePortMirrorCar.setStatus("current")
if mibBuilder.loadTexts:
    hwRemotePortMirrorCar.setUnits("Kbps")
_HwRemotePortMirrorRowStatus_Type = RowStatus
_HwRemotePortMirrorRowStatus_Object = MibTableColumn
hwRemotePortMirrorRowStatus = _HwRemotePortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 2, 1, 6),
    _HwRemotePortMirrorRowStatus_Type()
)
hwRemotePortMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemotePortMirrorRowStatus.setStatus("current")
_HwRemoteFlowMirrorTable_Object = MibTable
hwRemoteFlowMirrorTable = _HwRemoteFlowMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwRemoteFlowMirrorTable.setStatus("current")
_HwRemoteFlowMirrorEntry_Object = MibTableRow
hwRemoteFlowMirrorEntry = _HwRemoteFlowMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1)
)
hwRemoteFlowMirrorEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwRemoteBehaviorName"),
)
if mibBuilder.loadTexts:
    hwRemoteFlowMirrorEntry.setStatus("current")


class _HwRemoteBehaviorName_Type(OctetString):
    """Custom type hwRemoteBehaviorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRemoteBehaviorName_Type.__name__ = "OctetString"
_HwRemoteBehaviorName_Object = MibTableColumn
hwRemoteBehaviorName = _HwRemoteBehaviorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 1),
    _HwRemoteBehaviorName_Type()
)
hwRemoteBehaviorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemoteBehaviorName.setStatus("current")


class _HwFlowMirrorInstanceName_Type(OctetString):
    """Custom type hwFlowMirrorInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwFlowMirrorInstanceName_Type.__name__ = "OctetString"
_HwFlowMirrorInstanceName_Object = MibTableColumn
hwFlowMirrorInstanceName = _HwFlowMirrorInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 2),
    _HwFlowMirrorInstanceName_Type()
)
hwFlowMirrorInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowMirrorInstanceName.setStatus("current")


class _HwRemoteFlowMirrorCar_Type(Integer32):
    """Custom type hwRemoteFlowMirrorCar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 2500000),
    )


_HwRemoteFlowMirrorCar_Type.__name__ = "Integer32"
_HwRemoteFlowMirrorCar_Object = MibTableColumn
hwRemoteFlowMirrorCar = _HwRemoteFlowMirrorCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 3),
    _HwRemoteFlowMirrorCar_Type()
)
hwRemoteFlowMirrorCar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteFlowMirrorCar.setStatus("current")
if mibBuilder.loadTexts:
    hwRemoteFlowMirrorCar.setUnits("Kbps")
_HwRemoteFlowMirrorRowStatus_Type = RowStatus
_HwRemoteFlowMirrorRowStatus_Object = MibTableColumn
hwRemoteFlowMirrorRowStatus = _HwRemoteFlowMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 3, 1, 4),
    _HwRemoteFlowMirrorRowStatus_Type()
)
hwRemoteFlowMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteFlowMirrorRowStatus.setStatus("current")
_HwRemoteMirrorInstanceTable_Object = MibTable
hwRemoteMirrorInstanceTable = _HwRemoteMirrorInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwRemoteMirrorInstanceTable.setStatus("current")
_HwRemoteMirrorInstanceEntry_Object = MibTableRow
hwRemoteMirrorInstanceEntry = _HwRemoteMirrorInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1)
)
hwRemoteMirrorInstanceEntry.setIndexNames(
    (0, "HUAWEI-MIRROR-MIB", "hwMirrorInstanceName"),
)
if mibBuilder.loadTexts:
    hwRemoteMirrorInstanceEntry.setStatus("current")


class _HwMirrorInstanceName_Type(OctetString):
    """Custom type hwMirrorInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMirrorInstanceName_Type.__name__ = "OctetString"
_HwMirrorInstanceName_Object = MibTableColumn
hwMirrorInstanceName = _HwMirrorInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 1),
    _HwMirrorInstanceName_Type()
)
hwMirrorInstanceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMirrorInstanceName.setStatus("current")
_HwRemoteObservePortIp_Type = IpAddress
_HwRemoteObservePortIp_Object = MibTableColumn
hwRemoteObservePortIp = _HwRemoteObservePortIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 2),
    _HwRemoteObservePortIp_Type()
)
hwRemoteObservePortIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteObservePortIp.setStatus("current")


class _HwRemoteMirrorIdentifier_Type(Integer32):
    """Custom type hwRemoteMirrorIdentifier based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 64),
    )


_HwRemoteMirrorIdentifier_Type.__name__ = "Integer32"
_HwRemoteMirrorIdentifier_Object = MibTableColumn
hwRemoteMirrorIdentifier = _HwRemoteMirrorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 3),
    _HwRemoteMirrorIdentifier_Type()
)
hwRemoteMirrorIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteMirrorIdentifier.setStatus("current")


class _HwRemoteMirrorWithLinkLayerHeader_Type(Integer32):
    """Custom type hwRemoteMirrorWithLinkLayerHeader based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwRemoteMirrorWithLinkLayerHeader_Type.__name__ = "Integer32"
_HwRemoteMirrorWithLinkLayerHeader_Object = MibTableColumn
hwRemoteMirrorWithLinkLayerHeader = _HwRemoteMirrorWithLinkLayerHeader_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 4),
    _HwRemoteMirrorWithLinkLayerHeader_Type()
)
hwRemoteMirrorWithLinkLayerHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemoteMirrorWithLinkLayerHeader.setStatus("current")


class _HwMirrorFlowClass_Type(Integer32):
    """Custom type hwMirrorFlowClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("af1", 1),
          ("af2", 2),
          ("af3", 3),
          ("af4", 4),
          ("be", 0),
          ("cs6", 6),
          ("cs7", 7),
          ("ef", 5))
    )


_HwMirrorFlowClass_Type.__name__ = "Integer32"
_HwMirrorFlowClass_Object = MibTableColumn
hwMirrorFlowClass = _HwMirrorFlowClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 5),
    _HwMirrorFlowClass_Type()
)
hwMirrorFlowClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorFlowClass.setStatus("current")


class _HwMirrorSliceSize_Type(Integer32):
    """Custom type hwMirrorSliceSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 9600),
    )


_HwMirrorSliceSize_Type.__name__ = "Integer32"
_HwMirrorSliceSize_Object = MibTableColumn
hwMirrorSliceSize = _HwMirrorSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 6),
    _HwMirrorSliceSize_Type()
)
hwMirrorSliceSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorSliceSize.setStatus("current")
if mibBuilder.loadTexts:
    hwMirrorSliceSize.setUnits("Byte")
_HwMirrorTunnelIndex_Type = Integer32
_HwMirrorTunnelIndex_Object = MibTableColumn
hwMirrorTunnelIndex = _HwMirrorTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 7),
    _HwMirrorTunnelIndex_Type()
)
hwMirrorTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorTunnelIndex.setStatus("current")


class _HwMirrorTunnelType_Type(Integer32):
    """Custom type hwMirrorTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greTunnel", 3),
          ("lspTunnel", 1),
          ("teTunnel", 2))
    )


_HwMirrorTunnelType_Type.__name__ = "Integer32"
_HwMirrorTunnelType_Object = MibTableColumn
hwMirrorTunnelType = _HwMirrorTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 8),
    _HwMirrorTunnelType_Type()
)
hwMirrorTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorTunnelType.setStatus("current")


class _HwMirrorTunnelStatus_Type(Integer32):
    """Custom type hwMirrorTunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMirrorTunnelStatus_Type.__name__ = "Integer32"
_HwMirrorTunnelStatus_Object = MibTableColumn
hwMirrorTunnelStatus = _HwMirrorTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 9),
    _HwMirrorTunnelStatus_Type()
)
hwMirrorTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorTunnelStatus.setStatus("current")


class _HwMirrorTunnelPolicy_Type(OctetString):
    """Custom type hwMirrorTunnelPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HwMirrorTunnelPolicy_Type.__name__ = "OctetString"
_HwMirrorTunnelPolicy_Object = MibTableColumn
hwMirrorTunnelPolicy = _HwMirrorTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 10),
    _HwMirrorTunnelPolicy_Type()
)
hwMirrorTunnelPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorTunnelPolicy.setStatus("current")
_HwMirrorInstanceRowStatus_Type = RowStatus
_HwMirrorInstanceRowStatus_Object = MibTableColumn
hwMirrorInstanceRowStatus = _HwMirrorInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 1, 2, 4, 1, 11),
    _HwMirrorInstanceRowStatus_Type()
)
hwMirrorInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorInstanceRowStatus.setStatus("current")
_HwMirrorConformance_ObjectIdentity = ObjectIdentity
hwMirrorConformance = _HwMirrorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11)
)
_HwMirrorCompliances_ObjectIdentity = ObjectIdentity
hwMirrorCompliances = _HwMirrorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 1)
)
_HwBaseMirrorGroup_ObjectIdentity = ObjectIdentity
hwBaseMirrorGroup = _HwBaseMirrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2)
)

# Managed Objects groups

hwLocalObserveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 1)
)
hwLocalObserveGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwLocalObserveIndex"),
        ("HUAWEI-MIRROR-MIB", "hwLocalObserveWithLinkLayerHeader"),
        ("HUAWEI-MIRROR-MIB", "hwLocalObserveRowStatus"))
)
if mibBuilder.loadTexts:
    hwLocalObserveGroup.setStatus("current")

hwLocalPortMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 2)
)
hwLocalPortMirrorGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwLocalMirrorBearing"),
        ("HUAWEI-MIRROR-MIB", "hwLocalCpuPacketFlag"),
        ("HUAWEI-MIRROR-MIB", "hwLocalPortMirrorCar"),
        ("HUAWEI-MIRROR-MIB", "hwLocalPortMirrorRowStatus"))
)
if mibBuilder.loadTexts:
    hwLocalPortMirrorGroup.setStatus("current")

hwLocalFlowMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 3)
)
hwLocalFlowMirrorGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorEnable"),
        ("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorCar"),
        ("HUAWEI-MIRROR-MIB", "hwLocalFlowMirrorRowStatus"))
)
if mibBuilder.loadTexts:
    hwLocalFlowMirrorGroup.setStatus("current")

hwLocalSlotMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 4)
)
hwLocalSlotMirrorGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwSlotObserveIndex"),
        ("HUAWEI-MIRROR-MIB", "hwLocalSlotMirrorRowStatus"))
)
if mibBuilder.loadTexts:
    hwLocalSlotMirrorGroup.setStatus("current")

hwLocalPortMirrorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 5)
)
hwLocalPortMirrorInfoGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwMirrorType"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorCar"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorClass"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorBearing"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorCpuPacketFlag"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorWithLinkLayerHeader"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorInstanceName"))
)
if mibBuilder.loadTexts:
    hwLocalPortMirrorInfoGroup.setStatus("current")

hwRemoteObserveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 6)
)
hwRemoteObserveGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwRemoteIdentifier"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteDescription"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteObserveWithLinkLayerHeader"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteObserveRowStatus"))
)
if mibBuilder.loadTexts:
    hwRemoteObserveGroup.setStatus("current")

hwRemotePortMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 7)
)
hwRemotePortMirrorGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwRemoteMirrorBearing"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteCpuPacketFlag"),
        ("HUAWEI-MIRROR-MIB", "hwPortMirrorInstanceName"),
        ("HUAWEI-MIRROR-MIB", "hwRemotePortMirrorCar"),
        ("HUAWEI-MIRROR-MIB", "hwRemotePortMirrorRowStatus"))
)
if mibBuilder.loadTexts:
    hwRemotePortMirrorGroup.setStatus("current")

hwRemoteFlowMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 8)
)
hwRemoteFlowMirrorGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwFlowMirrorInstanceName"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteFlowMirrorCar"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteFlowMirrorRowStatus"))
)
if mibBuilder.loadTexts:
    hwRemoteFlowMirrorGroup.setStatus("current")

hwRemoteMirrorInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 2, 9)
)
hwRemoteMirrorInstanceGroup.setObjects(
      *(("HUAWEI-MIRROR-MIB", "hwRemoteObservePortIp"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorIdentifier"),
        ("HUAWEI-MIRROR-MIB", "hwRemoteMirrorWithLinkLayerHeader"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorFlowClass"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorSliceSize"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorTunnelIndex"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorTunnelType"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorTunnelStatus"),
        ("HUAWEI-MIRROR-MIB", "hwMirrorInstanceRowStatus"))
)
if mibBuilder.loadTexts:
    hwRemoteMirrorInstanceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwMirrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 162, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwMirrorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MIRROR-MIB",
    **{"hwMirrorMIB": hwMirrorMIB,
       "hwMirrorMIBObjects": hwMirrorMIBObjects,
       "hwLocalMirror": hwLocalMirror,
       "hwLocalObserveTable": hwLocalObserveTable,
       "hwLocalObserveEntry": hwLocalObserveEntry,
       "hwLocalObservePort": hwLocalObservePort,
       "hwLocalObserveIndex": hwLocalObserveIndex,
       "hwLocalObserveWithLinkLayerHeader": hwLocalObserveWithLinkLayerHeader,
       "hwLocalObserveRowStatus": hwLocalObserveRowStatus,
       "hwLocalPortMirrorTable": hwLocalPortMirrorTable,
       "hwLocalPortMirrorEntry": hwLocalPortMirrorEntry,
       "hwLocalMirrorPort": hwLocalMirrorPort,
       "hwLocalMirrorBearing": hwLocalMirrorBearing,
       "hwLocalCpuPacketFlag": hwLocalCpuPacketFlag,
       "hwLocalPortMirrorCar": hwLocalPortMirrorCar,
       "hwLocalPortMirrorRowStatus": hwLocalPortMirrorRowStatus,
       "hwLocalFlowMirrorTable": hwLocalFlowMirrorTable,
       "hwLocalFlowMirrorEntry": hwLocalFlowMirrorEntry,
       "hwLocalBehaviorName": hwLocalBehaviorName,
       "hwLocalFlowMirrorEnable": hwLocalFlowMirrorEnable,
       "hwLocalFlowMirrorCar": hwLocalFlowMirrorCar,
       "hwLocalFlowMirrorRowStatus": hwLocalFlowMirrorRowStatus,
       "hwLocalSlotMirrorTable": hwLocalSlotMirrorTable,
       "hwLocalSlotMirrorEntry": hwLocalSlotMirrorEntry,
       "hwLocalSlotNo": hwLocalSlotNo,
       "hwSlotObserveIndex": hwSlotObserveIndex,
       "hwLocalSlotMirrorRowStatus": hwLocalSlotMirrorRowStatus,
       "hwPortMirrorInfoTable": hwPortMirrorInfoTable,
       "hwPortMirrorInfoEntry": hwPortMirrorInfoEntry,
       "hwMirrorPortIndex": hwMirrorPortIndex,
       "hwMirrorType": hwMirrorType,
       "hwMirrorCar": hwMirrorCar,
       "hwMirrorClass": hwMirrorClass,
       "hwMirrorBearing": hwMirrorBearing,
       "hwMirrorCpuPacketFlag": hwMirrorCpuPacketFlag,
       "hwMirrorWithLinkLayerHeader": hwMirrorWithLinkLayerHeader,
       "hwRemoteMirrorInstanceName": hwRemoteMirrorInstanceName,
       "hwRemoteMirror": hwRemoteMirror,
       "hwRemoteObserveTable": hwRemoteObserveTable,
       "hwRemoteObserveEntry": hwRemoteObserveEntry,
       "hwRemoteObservePort": hwRemoteObservePort,
       "hwRemoteIdentifier": hwRemoteIdentifier,
       "hwRemoteDescription": hwRemoteDescription,
       "hwRemoteObserveWithLinkLayerHeader": hwRemoteObserveWithLinkLayerHeader,
       "hwRemoteObserveRowStatus": hwRemoteObserveRowStatus,
       "hwRemotePortMirrorTable": hwRemotePortMirrorTable,
       "hwRemotePortMirrorEntry": hwRemotePortMirrorEntry,
       "hwRemoteMirrorPort": hwRemoteMirrorPort,
       "hwRemoteMirrorBearing": hwRemoteMirrorBearing,
       "hwRemoteCpuPacketFlag": hwRemoteCpuPacketFlag,
       "hwPortMirrorInstanceName": hwPortMirrorInstanceName,
       "hwRemotePortMirrorCar": hwRemotePortMirrorCar,
       "hwRemotePortMirrorRowStatus": hwRemotePortMirrorRowStatus,
       "hwRemoteFlowMirrorTable": hwRemoteFlowMirrorTable,
       "hwRemoteFlowMirrorEntry": hwRemoteFlowMirrorEntry,
       "hwRemoteBehaviorName": hwRemoteBehaviorName,
       "hwFlowMirrorInstanceName": hwFlowMirrorInstanceName,
       "hwRemoteFlowMirrorCar": hwRemoteFlowMirrorCar,
       "hwRemoteFlowMirrorRowStatus": hwRemoteFlowMirrorRowStatus,
       "hwRemoteMirrorInstanceTable": hwRemoteMirrorInstanceTable,
       "hwRemoteMirrorInstanceEntry": hwRemoteMirrorInstanceEntry,
       "hwMirrorInstanceName": hwMirrorInstanceName,
       "hwRemoteObservePortIp": hwRemoteObservePortIp,
       "hwRemoteMirrorIdentifier": hwRemoteMirrorIdentifier,
       "hwRemoteMirrorWithLinkLayerHeader": hwRemoteMirrorWithLinkLayerHeader,
       "hwMirrorFlowClass": hwMirrorFlowClass,
       "hwMirrorSliceSize": hwMirrorSliceSize,
       "hwMirrorTunnelIndex": hwMirrorTunnelIndex,
       "hwMirrorTunnelType": hwMirrorTunnelType,
       "hwMirrorTunnelStatus": hwMirrorTunnelStatus,
       "hwMirrorTunnelPolicy": hwMirrorTunnelPolicy,
       "hwMirrorInstanceRowStatus": hwMirrorInstanceRowStatus,
       "hwMirrorConformance": hwMirrorConformance,
       "hwMirrorCompliances": hwMirrorCompliances,
       "hwMirrorCompliance": hwMirrorCompliance,
       "hwBaseMirrorGroup": hwBaseMirrorGroup,
       "hwLocalObserveGroup": hwLocalObserveGroup,
       "hwLocalPortMirrorGroup": hwLocalPortMirrorGroup,
       "hwLocalFlowMirrorGroup": hwLocalFlowMirrorGroup,
       "hwLocalSlotMirrorGroup": hwLocalSlotMirrorGroup,
       "hwLocalPortMirrorInfoGroup": hwLocalPortMirrorInfoGroup,
       "hwRemoteObserveGroup": hwRemoteObserveGroup,
       "hwRemotePortMirrorGroup": hwRemotePortMirrorGroup,
       "hwRemoteFlowMirrorGroup": hwRemoteFlowMirrorGroup,
       "hwRemoteMirrorInstanceGroup": hwRemoteMirrorInstanceGroup}
)
