# SNMP MIB module (HUAWEI-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:24 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

(HWFrameType,
 HWPCBType,
 HWPortType,
 HWSubPCBType) = mibBuilder.importSymbols(
    "HUAWEI-TC-MIB",
    "HWFrameType",
    "HWPCBType",
    "HWPortType",
    "HWSubPCBType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwDev = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSystemPara_ObjectIdentity = ObjectIdentity
hwSystemPara = _HwSystemPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 1)
)
_HwSysIpAddr_Type = IpAddress
_HwSysIpAddr_Object = MibScalar
hwSysIpAddr = _HwSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 1, 1),
    _HwSysIpAddr_Type()
)
hwSysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysIpAddr.setStatus("current")
_HwSysIpMask_Type = IpAddress
_HwSysIpMask_Object = MibScalar
hwSysIpMask = _HwSysIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 1, 2),
    _HwSysIpMask_Type()
)
hwSysIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysIpMask.setStatus("current")
_HwSysVersion_Type = DisplayString
_HwSysVersion_Object = MibScalar
hwSysVersion = _HwSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 1, 3),
    _HwSysVersion_Type()
)
hwSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysVersion.setStatus("current")
_HwSysTime_Type = DateAndTime
_HwSysTime_Object = MibScalar
hwSysTime = _HwSysTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 1, 4),
    _HwSysTime_Type()
)
hwSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysTime.setStatus("current")
_HwNmsParaTable_Object = MibTable
hwNmsParaTable = _HwNmsParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2)
)
if mibBuilder.loadTexts:
    hwNmsParaTable.setStatus("current")
_HwNmsParaEntry_Object = MibTableRow
hwNmsParaEntry = _HwNmsParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1)
)
hwNmsParaEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwNmsIndex"),
)
if mibBuilder.loadTexts:
    hwNmsParaEntry.setStatus("current")


class _HwNmsIndex_Type(Integer32):
    """Custom type hwNmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwNmsIndex_Type.__name__ = "Integer32"
_HwNmsIndex_Object = MibTableColumn
hwNmsIndex = _HwNmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 1),
    _HwNmsIndex_Type()
)
hwNmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNmsIndex.setStatus("current")


class _HwNmsName_Type(OctetString):
    """Custom type hwNmsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwNmsName_Type.__name__ = "OctetString"
_HwNmsName_Object = MibTableColumn
hwNmsName = _HwNmsName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 2),
    _HwNmsName_Type()
)
hwNmsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsName.setStatus("current")
_HwNmsIp_Type = IpAddress
_HwNmsIp_Object = MibTableColumn
hwNmsIp = _HwNmsIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 3),
    _HwNmsIp_Type()
)
hwNmsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsIp.setStatus("current")
_HwNmsMask_Type = IpAddress
_HwNmsMask_Object = MibTableColumn
hwNmsMask = _HwNmsMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 4),
    _HwNmsMask_Type()
)
hwNmsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsMask.setStatus("deprecated")


class _HwNmsMaintainMode_Type(Integer32):
    """Custom type hwNmsMaintainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inBandwidth", 1),
          ("outBandwidth", 2))
    )


_HwNmsMaintainMode_Type.__name__ = "Integer32"
_HwNmsMaintainMode_Object = MibTableColumn
hwNmsMaintainMode = _HwNmsMaintainMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 5),
    _HwNmsMaintainMode_Type()
)
hwNmsMaintainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsMaintainMode.setStatus("deprecated")


class _HwNmsGetCommunity_Type(OctetString):
    """Custom type hwNmsGetCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwNmsGetCommunity_Type.__name__ = "OctetString"
_HwNmsGetCommunity_Object = MibTableColumn
hwNmsGetCommunity = _HwNmsGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 6),
    _HwNmsGetCommunity_Type()
)
hwNmsGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsGetCommunity.setStatus("current")


class _HwNmsSetCommunity_Type(OctetString):
    """Custom type hwNmsSetCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwNmsSetCommunity_Type.__name__ = "OctetString"
_HwNmsSetCommunity_Object = MibTableColumn
hwNmsSetCommunity = _HwNmsSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 7),
    _HwNmsSetCommunity_Type()
)
hwNmsSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsSetCommunity.setStatus("current")
_HwNmsSnmpPort_Type = Integer32
_HwNmsSnmpPort_Object = MibTableColumn
hwNmsSnmpPort = _HwNmsSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 8),
    _HwNmsSnmpPort_Type()
)
hwNmsSnmpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsSnmpPort.setStatus("deprecated")
_HwNmsTrapPort_Type = Integer32
_HwNmsTrapPort_Object = MibTableColumn
hwNmsTrapPort = _HwNmsTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 9),
    _HwNmsTrapPort_Type()
)
hwNmsTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsTrapPort.setStatus("deprecated")


class _HwNmsClass_Type(Integer32):
    """Custom type hwNmsClass based on Integer32"""
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
        *(("ro", 1),
          ("rw", 2),
          ("rwWithTrap", 3),
          ("trapOnly", 4))
    )


_HwNmsClass_Type.__name__ = "Integer32"
_HwNmsClass_Object = MibTableColumn
hwNmsClass = _HwNmsClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 10),
    _HwNmsClass_Type()
)
hwNmsClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsClass.setStatus("deprecated")
_HwNmsStatus_Type = RowStatus
_HwNmsStatus_Object = MibTableColumn
hwNmsStatus = _HwNmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 2, 1, 11),
    _HwNmsStatus_Type()
)
hwNmsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNmsStatus.setStatus("current")
_HwSlotConf_ObjectIdentity = ObjectIdentity
hwSlotConf = _HwSlotConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3)
)
_HwFrameTable_Object = MibTable
hwFrameTable = _HwFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hwFrameTable.setStatus("current")
_HwFrameEntry_Object = MibTableRow
hwFrameEntry = _HwFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1)
)
hwFrameEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
)
if mibBuilder.loadTexts:
    hwFrameEntry.setStatus("current")


class _HwFrameIndex_Type(Integer32):
    """Custom type hwFrameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwFrameIndex_Type.__name__ = "Integer32"
_HwFrameIndex_Object = MibTableColumn
hwFrameIndex = _HwFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 1),
    _HwFrameIndex_Type()
)
hwFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrameIndex.setStatus("current")
_HwFrameType_Type = HWFrameType
_HwFrameType_Object = MibTableColumn
hwFrameType = _HwFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 2),
    _HwFrameType_Type()
)
hwFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFrameType.setStatus("current")


class _HwFrameDesc_Type(OctetString):
    """Custom type hwFrameDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwFrameDesc_Type.__name__ = "OctetString"
_HwFrameDesc_Object = MibTableColumn
hwFrameDesc = _HwFrameDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 3),
    _HwFrameDesc_Type()
)
hwFrameDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFrameDesc.setStatus("current")
_HwSlots_Type = Integer32
_HwSlots_Object = MibTableColumn
hwSlots = _HwSlots_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 4),
    _HwSlots_Type()
)
hwSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlots.setStatus("current")


class _HwFrameOperStatus_Type(Integer32):
    """Custom type hwFrameOperStatus based on Integer32"""
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
        *(("discovery", 4),
          ("fault", 2),
          ("normal", 1),
          ("other", 3))
    )


_HwFrameOperStatus_Type.__name__ = "Integer32"
_HwFrameOperStatus_Object = MibTableColumn
hwFrameOperStatus = _HwFrameOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 5),
    _HwFrameOperStatus_Type()
)
hwFrameOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrameOperStatus.setStatus("current")


class _HwFrameAdminStatus_Type(Integer32):
    """Custom type hwFrameAdminStatus based on Integer32"""
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
        *(("confirm", 5),
          ("delete", 6),
          ("disable", 1),
          ("enable", 2),
          ("reset", 3),
          ("test", 4))
    )


_HwFrameAdminStatus_Type.__name__ = "Integer32"
_HwFrameAdminStatus_Object = MibTableColumn
hwFrameAdminStatus = _HwFrameAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 6),
    _HwFrameAdminStatus_Type()
)
hwFrameAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFrameAdminStatus.setStatus("current")
_HwFrameRowStatus_Type = RowStatus
_HwFrameRowStatus_Object = MibTableColumn
hwFrameRowStatus = _HwFrameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 1, 1, 7),
    _HwFrameRowStatus_Type()
)
hwFrameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFrameRowStatus.setStatus("current")
_HwSlotTable_Object = MibTable
hwSlotTable = _HwSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hwSlotTable.setStatus("current")
_HwSlotEntry_Object = MibTableRow
hwSlotEntry = _HwSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1)
)
hwSlotEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwSlotEntry.setStatus("current")


class _HwSlotIndex_Type(Integer32):
    """Custom type hwSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwSlotIndex_Type.__name__ = "Integer32"
_HwSlotIndex_Object = MibTableColumn
hwSlotIndex = _HwSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 1),
    _HwSlotIndex_Type()
)
hwSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotIndex.setStatus("current")
_HwSlotType_Type = HWPCBType
_HwSlotType_Object = MibTableColumn
hwSlotType = _HwSlotType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 2),
    _HwSlotType_Type()
)
hwSlotType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotType.setStatus("current")


class _HwSlotDesc_Type(OctetString):
    """Custom type hwSlotDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSlotDesc_Type.__name__ = "OctetString"
_HwSlotDesc_Object = MibTableColumn
hwSlotDesc = _HwSlotDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 3),
    _HwSlotDesc_Type()
)
hwSlotDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotDesc.setStatus("current")


class _HwSlotPcbVersion_Type(OctetString):
    """Custom type hwSlotPcbVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSlotPcbVersion_Type.__name__ = "OctetString"
_HwSlotPcbVersion_Object = MibTableColumn
hwSlotPcbVersion = _HwSlotPcbVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 4),
    _HwSlotPcbVersion_Type()
)
hwSlotPcbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotPcbVersion.setStatus("deprecated")


class _HwSlotVersion_Type(OctetString):
    """Custom type hwSlotVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 640),
    )


_HwSlotVersion_Type.__name__ = "OctetString"
_HwSlotVersion_Object = MibTableColumn
hwSlotVersion = _HwSlotVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 5),
    _HwSlotVersion_Type()
)
hwSlotVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotVersion.setStatus("current")


class _HwSlotWorkMode_Type(Integer32):
    """Custom type hwSlotWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("other", 255),
          ("standby", 2))
    )


_HwSlotWorkMode_Type.__name__ = "Integer32"
_HwSlotWorkMode_Object = MibTableColumn
hwSlotWorkMode = _HwSlotWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 6),
    _HwSlotWorkMode_Type()
)
hwSlotWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotWorkMode.setStatus("current")
_HwSubSlots_Type = Integer32
_HwSubSlots_Object = MibTableColumn
hwSubSlots = _HwSubSlots_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 7),
    _HwSubSlots_Type()
)
hwSubSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubSlots.setStatus("current")


class _HwSlotOperStatus_Type(Integer32):
    """Custom type hwSlotOperStatus based on Integer32"""
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
        *(("abnormal", 8),
          ("config", 6),
          ("discovery", 5),
          ("fault", 3),
          ("forbidden", 4),
          ("normal", 2),
          ("offline", 7),
          ("uninstall", 1))
    )


_HwSlotOperStatus_Type.__name__ = "Integer32"
_HwSlotOperStatus_Object = MibTableColumn
hwSlotOperStatus = _HwSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 8),
    _HwSlotOperStatus_Type()
)
hwSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotOperStatus.setStatus("current")


class _HwSlotAdminStatus_Type(Integer32):
    """Custom type hwSlotAdminStatus based on Integer32"""
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
        *(("confirm", 5),
          ("delete", 7),
          ("disable", 1),
          ("enable", 2),
          ("forbidden", 8),
          ("reset", 3),
          ("switch", 6),
          ("test", 4),
          ("unforbidden", 9))
    )


_HwSlotAdminStatus_Type.__name__ = "Integer32"
_HwSlotAdminStatus_Object = MibTableColumn
hwSlotAdminStatus = _HwSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 9),
    _HwSlotAdminStatus_Type()
)
hwSlotAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotAdminStatus.setStatus("current")
_HwSlotRowStatus_Type = RowStatus
_HwSlotRowStatus_Object = MibTableColumn
hwSlotRowStatus = _HwSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 10),
    _HwSlotRowStatus_Type()
)
hwSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotRowStatus.setStatus("current")


class _HwSlotPhySerialNum_Type(DisplayString):
    """Custom type hwSlotPhySerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwSlotPhySerialNum_Type.__name__ = "DisplayString"
_HwSlotPhySerialNum_Object = MibTableColumn
hwSlotPhySerialNum = _HwSlotPhySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 2, 1, 11),
    _HwSlotPhySerialNum_Type()
)
hwSlotPhySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotPhySerialNum.setStatus("current")
_HwSubslotTable_Object = MibTable
hwSubslotTable = _HwSubslotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hwSubslotTable.setStatus("current")
_HwSubslotEntry_Object = MibTableRow
hwSubslotEntry = _HwSubslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1)
)
hwSubslotEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSubslotIndex"),
)
if mibBuilder.loadTexts:
    hwSubslotEntry.setStatus("current")


class _HwSubslotIndex_Type(Integer32):
    """Custom type hwSubslotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwSubslotIndex_Type.__name__ = "Integer32"
_HwSubslotIndex_Object = MibTableColumn
hwSubslotIndex = _HwSubslotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 1),
    _HwSubslotIndex_Type()
)
hwSubslotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubslotIndex.setStatus("current")
_HwSubslotType_Type = HWSubPCBType
_HwSubslotType_Object = MibTableColumn
hwSubslotType = _HwSubslotType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 2),
    _HwSubslotType_Type()
)
hwSubslotType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubslotType.setStatus("current")
_HwSubslotPorts_Type = Integer32
_HwSubslotPorts_Object = MibTableColumn
hwSubslotPorts = _HwSubslotPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 3),
    _HwSubslotPorts_Type()
)
hwSubslotPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubslotPorts.setStatus("current")


class _HwSubslotOperStatus_Type(Integer32):
    """Custom type hwSubslotOperStatus based on Integer32"""
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
        *(("fault", 3),
          ("forbidden", 4),
          ("normal", 2),
          ("uninstall", 1))
    )


_HwSubslotOperStatus_Type.__name__ = "Integer32"
_HwSubslotOperStatus_Object = MibTableColumn
hwSubslotOperStatus = _HwSubslotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 5),
    _HwSubslotOperStatus_Type()
)
hwSubslotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSubslotOperStatus.setStatus("current")


class _HwSubslotAdminStatus_Type(Integer32):
    """Custom type hwSubslotAdminStatus based on Integer32"""
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
        *(("confirm", 5),
          ("delete", 6),
          ("disable", 1),
          ("enable", 2),
          ("reset", 3),
          ("test", 4))
    )


_HwSubslotAdminStatus_Type.__name__ = "Integer32"
_HwSubslotAdminStatus_Object = MibTableColumn
hwSubslotAdminStatus = _HwSubslotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 7),
    _HwSubslotAdminStatus_Type()
)
hwSubslotAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubslotAdminStatus.setStatus("current")


class _HwSubslotVersion_Type(OctetString):
    """Custom type hwSubslotVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwSubslotVersion_Type.__name__ = "OctetString"
_HwSubslotVersion_Object = MibTableColumn
hwSubslotVersion = _HwSubslotVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 8),
    _HwSubslotVersion_Type()
)
hwSubslotVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubslotVersion.setStatus("current")


class _HwSubSlotDesc_Type(OctetString):
    """Custom type hwSubSlotDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSubSlotDesc_Type.__name__ = "OctetString"
_HwSubSlotDesc_Object = MibTableColumn
hwSubSlotDesc = _HwSubSlotDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 9),
    _HwSubSlotDesc_Type()
)
hwSubSlotDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubSlotDesc.setStatus("current")
_HwSubslotRowStatus_Type = RowStatus
_HwSubslotRowStatus_Object = MibTableColumn
hwSubslotRowStatus = _HwSubslotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 3, 1, 10),
    _HwSubslotRowStatus_Type()
)
hwSubslotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubslotRowStatus.setStatus("current")
_HwPortTable_Object = MibTable
hwPortTable = _HwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hwPortTable.setStatus("current")
_HwPortEntry_Object = MibTableRow
hwPortEntry = _HwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1)
)
hwPortEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSubslotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwPortIndex"),
)
if mibBuilder.loadTexts:
    hwPortEntry.setStatus("current")


class _HwPortIndex_Type(Integer32):
    """Custom type hwPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPortIndex_Type.__name__ = "Integer32"
_HwPortIndex_Object = MibTableColumn
hwPortIndex = _HwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1, 1),
    _HwPortIndex_Type()
)
hwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortIndex.setStatus("current")
_HwPortType_Type = HWPortType
_HwPortType_Object = MibTableColumn
hwPortType = _HwPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1, 2),
    _HwPortType_Type()
)
hwPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortType.setStatus("current")


class _HwPortDesc_Type(OctetString):
    """Custom type hwPortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwPortDesc_Type.__name__ = "OctetString"
_HwPortDesc_Object = MibTableColumn
hwPortDesc = _HwPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1, 3),
    _HwPortDesc_Type()
)
hwPortDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortDesc.setStatus("current")
_HwPortSpeed_Type = Integer32
_HwPortSpeed_Object = MibTableColumn
hwPortSpeed = _HwPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1, 4),
    _HwPortSpeed_Type()
)
hwPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortSpeed.setStatus("deprecated")


class _HwPortOperStatus_Type(Integer32):
    """Custom type hwPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("activing", 10),
          ("block", 12),
          ("deactive", 11),
          ("fault", 2),
          ("forbidden", 4),
          ("innerLocalLoopback", 14),
          ("innerRemoteLoopback", 15),
          ("localLoopback", 3),
          ("nolight", 13),
          ("normal", 1),
          ("remoteLoopback", 6),
          ("test", 5))
    )


_HwPortOperStatus_Type.__name__ = "Integer32"
_HwPortOperStatus_Object = MibTableColumn
hwPortOperStatus = _HwPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1, 5),
    _HwPortOperStatus_Type()
)
hwPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortOperStatus.setStatus("current")


class _HwPortAdminStatus_Type(Integer32):
    """Custom type hwPortAdminStatus based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 3),
          ("confirm", 5),
          ("deactive", 2),
          ("delete", 6),
          ("innerLocalLoopback", 12),
          ("innerRemoteLoopback", 13),
          ("localLoopback", 8),
          ("remoteLoopback", 9),
          ("reset", 7),
          ("rtuLocalLoopback", 14),
          ("rtuRemoteLoopback", 15),
          ("stopLoopback", 11),
          ("unblock", 4))
    )


_HwPortAdminStatus_Type.__name__ = "Integer32"
_HwPortAdminStatus_Object = MibTableColumn
hwPortAdminStatus = _HwPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 4, 1, 6),
    _HwPortAdminStatus_Type()
)
hwPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortAdminStatus.setStatus("current")
_HwFrameLinks_ObjectIdentity = ObjectIdentity
hwFrameLinks = _HwFrameLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5)
)
_HwFrameLinkNumber_Type = Integer32
_HwFrameLinkNumber_Object = MibScalar
hwFrameLinkNumber = _HwFrameLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 1),
    _HwFrameLinkNumber_Type()
)
hwFrameLinkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkNumber.setStatus("current")
_HwFrameLinkTable_Object = MibTable
hwFrameLinkTable = _HwFrameLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    hwFrameLinkTable.setStatus("current")
_HwFrameLinkEntry_Object = MibTableRow
hwFrameLinkEntry = _HwFrameLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1)
)
hwFrameLinkEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameLinkIndex"),
)
if mibBuilder.loadTexts:
    hwFrameLinkEntry.setStatus("current")


class _HwFrameLinkIndex_Type(Integer32):
    """Custom type hwFrameLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwFrameLinkIndex_Type.__name__ = "Integer32"
_HwFrameLinkIndex_Object = MibTableColumn
hwFrameLinkIndex = _HwFrameLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 1),
    _HwFrameLinkIndex_Type()
)
hwFrameLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrameLinkIndex.setStatus("current")
_HwFrameLinkLeftFrame_Type = Integer32
_HwFrameLinkLeftFrame_Object = MibTableColumn
hwFrameLinkLeftFrame = _HwFrameLinkLeftFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 2),
    _HwFrameLinkLeftFrame_Type()
)
hwFrameLinkLeftFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkLeftFrame.setStatus("current")
_HwFrameLinkLeftSlot_Type = Integer32
_HwFrameLinkLeftSlot_Object = MibTableColumn
hwFrameLinkLeftSlot = _HwFrameLinkLeftSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 3),
    _HwFrameLinkLeftSlot_Type()
)
hwFrameLinkLeftSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkLeftSlot.setStatus("current")
_HwFrameLinkLeftSubSlot_Type = Integer32
_HwFrameLinkLeftSubSlot_Object = MibTableColumn
hwFrameLinkLeftSubSlot = _HwFrameLinkLeftSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 4),
    _HwFrameLinkLeftSubSlot_Type()
)
hwFrameLinkLeftSubSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkLeftSubSlot.setStatus("current")
_HwFrameLinkLeftPort_Type = Integer32
_HwFrameLinkLeftPort_Object = MibTableColumn
hwFrameLinkLeftPort = _HwFrameLinkLeftPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 5),
    _HwFrameLinkLeftPort_Type()
)
hwFrameLinkLeftPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkLeftPort.setStatus("current")
_HwFrameLinkRightFrame_Type = Integer32
_HwFrameLinkRightFrame_Object = MibTableColumn
hwFrameLinkRightFrame = _HwFrameLinkRightFrame_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 6),
    _HwFrameLinkRightFrame_Type()
)
hwFrameLinkRightFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkRightFrame.setStatus("current")
_HwFrameLinkRightSlot_Type = Integer32
_HwFrameLinkRightSlot_Object = MibTableColumn
hwFrameLinkRightSlot = _HwFrameLinkRightSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 7),
    _HwFrameLinkRightSlot_Type()
)
hwFrameLinkRightSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkRightSlot.setStatus("current")
_HwFrameLinkRightSubSlot_Type = Integer32
_HwFrameLinkRightSubSlot_Object = MibTableColumn
hwFrameLinkRightSubSlot = _HwFrameLinkRightSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 8),
    _HwFrameLinkRightSubSlot_Type()
)
hwFrameLinkRightSubSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkRightSubSlot.setStatus("current")
_HwFrameLinkRightPort_Type = Integer32
_HwFrameLinkRightPort_Object = MibTableColumn
hwFrameLinkRightPort = _HwFrameLinkRightPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 9),
    _HwFrameLinkRightPort_Type()
)
hwFrameLinkRightPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkRightPort.setStatus("current")


class _HwFrameLinkOperStatus_Type(Integer32):
    """Custom type hwFrameLinkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("normal", 1),
          ("unknown", 3))
    )


_HwFrameLinkOperStatus_Type.__name__ = "Integer32"
_HwFrameLinkOperStatus_Object = MibTableColumn
hwFrameLinkOperStatus = _HwFrameLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 10),
    _HwFrameLinkOperStatus_Type()
)
hwFrameLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrameLinkOperStatus.setStatus("current")
_HwFrameLinkRowStatus_Type = RowStatus
_HwFrameLinkRowStatus_Object = MibTableColumn
hwFrameLinkRowStatus = _HwFrameLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 2, 1, 11),
    _HwFrameLinkRowStatus_Type()
)
hwFrameLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFrameLinkRowStatus.setStatus("current")


class _HwFrameLinkNextIndex_Type(Integer32):
    """Custom type hwFrameLinkNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwFrameLinkNextIndex_Type.__name__ = "Integer32"
_HwFrameLinkNextIndex_Object = MibScalar
hwFrameLinkNextIndex = _HwFrameLinkNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 5, 3),
    _HwFrameLinkNextIndex_Type()
)
hwFrameLinkNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFrameLinkNextIndex.setStatus("current")
_HwNarrowBoard_ObjectIdentity = ObjectIdentity
hwNarrowBoard = _HwNarrowBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 6)
)
_HwBoardAttrTable_Object = MibTable
hwBoardAttrTable = _HwBoardAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    hwBoardAttrTable.setStatus("current")
_HwBoardAttrEntry_Object = MibTableRow
hwBoardAttrEntry = _HwBoardAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 6, 1, 1)
)
hwBoardAttrEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwBoardAttrEntry.setStatus("current")


class _HwBoardAulaw_Type(Integer32):
    """Custom type hwBoardAulaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwBoardAulaw_Type.__name__ = "Integer32"
_HwBoardAulaw_Object = MibTableColumn
hwBoardAulaw = _HwBoardAulaw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 6, 1, 1, 1),
    _HwBoardAulaw_Type()
)
hwBoardAulaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBoardAulaw.setStatus("current")


class _HwBoardCurrent_Type(Integer32):
    """Custom type hwBoardCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwBoardCurrent_Type.__name__ = "Integer32"
_HwBoardCurrent_Object = MibTableColumn
hwBoardCurrent = _HwBoardCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 6, 1, 1, 2),
    _HwBoardCurrent_Type()
)
hwBoardCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBoardCurrent.setStatus("current")


class _HwBoardImpedance_Type(Integer32):
    """Custom type hwBoardImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
        ValueRangeConstraint(255, 255),
    )


_HwBoardImpedance_Type.__name__ = "Integer32"
_HwBoardImpedance_Object = MibTableColumn
hwBoardImpedance = _HwBoardImpedance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 3, 6, 1, 1, 3),
    _HwBoardImpedance_Type()
)
hwBoardImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBoardImpedance.setStatus("current")
_HwCpuDevTable_Object = MibTable
hwCpuDevTable = _HwCpuDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4)
)
if mibBuilder.loadTexts:
    hwCpuDevTable.setStatus("current")
_HwCpuDevEntry_Object = MibTableRow
hwCpuDevEntry = _HwCpuDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1)
)
hwCpuDevEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwCpuDevIndex"),
)
if mibBuilder.loadTexts:
    hwCpuDevEntry.setStatus("current")


class _HwCpuDevIndex_Type(Integer32):
    """Custom type hwCpuDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCpuDevIndex_Type.__name__ = "Integer32"
_HwCpuDevIndex_Object = MibTableColumn
hwCpuDevIndex = _HwCpuDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 1),
    _HwCpuDevIndex_Type()
)
hwCpuDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCpuDevIndex.setStatus("current")


class _HwCpuDevDuty_Type(Integer32):
    """Custom type hwCpuDevDuty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCpuDevDuty_Type.__name__ = "Integer32"
_HwCpuDevDuty_Object = MibTableColumn
hwCpuDevDuty = _HwCpuDevDuty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 2),
    _HwCpuDevDuty_Type()
)
hwCpuDevDuty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuDevDuty.setStatus("current")


class _HwAvgDuty1min_Type(Integer32):
    """Custom type hwAvgDuty1min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAvgDuty1min_Type.__name__ = "Integer32"
_HwAvgDuty1min_Object = MibTableColumn
hwAvgDuty1min = _HwAvgDuty1min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 3),
    _HwAvgDuty1min_Type()
)
hwAvgDuty1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAvgDuty1min.setStatus("current")


class _HwAvgDuty5min_Type(Integer32):
    """Custom type hwAvgDuty5min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwAvgDuty5min_Type.__name__ = "Integer32"
_HwAvgDuty5min_Object = MibTableColumn
hwAvgDuty5min = _HwAvgDuty5min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 4),
    _HwAvgDuty5min_Type()
)
hwAvgDuty5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAvgDuty5min.setStatus("current")
_HwMemoryDev_ObjectIdentity = ObjectIdentity
hwMemoryDev = _HwMemoryDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5)
)
_HwMemoryDevTable_Object = MibTable
hwMemoryDevTable = _HwMemoryDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1)
)
if mibBuilder.loadTexts:
    hwMemoryDevTable.setStatus("current")
_HwMemoryDevEntry_Object = MibTableRow
hwMemoryDevEntry = _HwMemoryDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1)
)
hwMemoryDevEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwMemoryDevModuleIndex"),
)
if mibBuilder.loadTexts:
    hwMemoryDevEntry.setStatus("current")


class _HwMemoryDevModuleIndex_Type(Integer32):
    """Custom type hwMemoryDevModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMemoryDevModuleIndex_Type.__name__ = "Integer32"
_HwMemoryDevModuleIndex_Object = MibTableColumn
hwMemoryDevModuleIndex = _HwMemoryDevModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 1),
    _HwMemoryDevModuleIndex_Type()
)
hwMemoryDevModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMemoryDevModuleIndex.setStatus("current")
_HwMemoryDevSize_Type = Integer32
_HwMemoryDevSize_Object = MibTableColumn
hwMemoryDevSize = _HwMemoryDevSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 2),
    _HwMemoryDevSize_Type()
)
hwMemoryDevSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevSize.setStatus("current")
_HwMemoryDevFree_Type = Integer32
_HwMemoryDevFree_Object = MibTableColumn
hwMemoryDevFree = _HwMemoryDevFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 3),
    _HwMemoryDevFree_Type()
)
hwMemoryDevFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevFree.setStatus("current")
_HwMemoryDevRawSliceUsed_Type = Integer32
_HwMemoryDevRawSliceUsed_Object = MibTableColumn
hwMemoryDevRawSliceUsed = _HwMemoryDevRawSliceUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 4),
    _HwMemoryDevRawSliceUsed_Type()
)
hwMemoryDevRawSliceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevRawSliceUsed.setStatus("current")
_HwMemoryDevLargestFree_Type = Integer32
_HwMemoryDevLargestFree_Object = MibTableColumn
hwMemoryDevLargestFree = _HwMemoryDevLargestFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 5),
    _HwMemoryDevLargestFree_Type()
)
hwMemoryDevLargestFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevLargestFree.setStatus("current")
_HwMemoryDevFail_Type = Integer32
_HwMemoryDevFail_Object = MibTableColumn
hwMemoryDevFail = _HwMemoryDevFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 6),
    _HwMemoryDevFail_Type()
)
hwMemoryDevFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevFail.setStatus("current")
_HwMemoryDevFailNoMem_Type = Integer32
_HwMemoryDevFailNoMem_Object = MibTableColumn
hwMemoryDevFailNoMem = _HwMemoryDevFailNoMem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 1, 1, 7),
    _HwMemoryDevFailNoMem_Type()
)
hwMemoryDevFailNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemoryDevFailNoMem.setStatus("current")
_HwBufferTable_Object = MibTable
hwBufferTable = _HwBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2)
)
if mibBuilder.loadTexts:
    hwBufferTable.setStatus("current")
_HwBufferEntry_Object = MibTableRow
hwBufferEntry = _HwBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1)
)
hwBufferEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwBufferModuleIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwBufferSize"),
)
if mibBuilder.loadTexts:
    hwBufferEntry.setStatus("current")


class _HwBufferModuleIndex_Type(Integer32):
    """Custom type hwBufferModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwBufferModuleIndex_Type.__name__ = "Integer32"
_HwBufferModuleIndex_Object = MibTableColumn
hwBufferModuleIndex = _HwBufferModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 1),
    _HwBufferModuleIndex_Type()
)
hwBufferModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBufferModuleIndex.setStatus("current")


class _HwBufferSize_Type(Integer32):
    """Custom type hwBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwBufferSize_Type.__name__ = "Integer32"
_HwBufferSize_Object = MibTableColumn
hwBufferSize = _HwBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 2),
    _HwBufferSize_Type()
)
hwBufferSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBufferSize.setStatus("current")
_HwBufferCurrentTotal_Type = Integer32
_HwBufferCurrentTotal_Object = MibTableColumn
hwBufferCurrentTotal = _HwBufferCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 3),
    _HwBufferCurrentTotal_Type()
)
hwBufferCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBufferCurrentTotal.setStatus("current")
_HwBufferCurrentUsed_Type = Integer32
_HwBufferCurrentUsed_Object = MibTableColumn
hwBufferCurrentUsed = _HwBufferCurrentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 5, 2, 1, 4),
    _HwBufferCurrentUsed_Type()
)
hwBufferCurrentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBufferCurrentUsed.setStatus("current")
_HwFlashDev_ObjectIdentity = ObjectIdentity
hwFlashDev = _HwFlashDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6)
)
_HwFlashDevTable_Object = MibTable
hwFlashDevTable = _HwFlashDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1)
)
if mibBuilder.loadTexts:
    hwFlashDevTable.setStatus("current")
_HwFlashDevEntry_Object = MibTableRow
hwFlashDevEntry = _HwFlashDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1)
)
hwFlashDevEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwFlashDevIndex"),
)
if mibBuilder.loadTexts:
    hwFlashDevEntry.setStatus("current")


class _HwFlashDevIndex_Type(Integer32):
    """Custom type hwFlashDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwFlashDevIndex_Type.__name__ = "Integer32"
_HwFlashDevIndex_Object = MibTableColumn
hwFlashDevIndex = _HwFlashDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1, 1),
    _HwFlashDevIndex_Type()
)
hwFlashDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFlashDevIndex.setStatus("current")
_HwFlashDevSize_Type = Integer32
_HwFlashDevSize_Object = MibTableColumn
hwFlashDevSize = _HwFlashDevSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1, 2),
    _HwFlashDevSize_Type()
)
hwFlashDevSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlashDevSize.setStatus("current")
_HwFlashDevFree_Type = Integer32
_HwFlashDevFree_Object = MibTableColumn
hwFlashDevFree = _HwFlashDevFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1, 3),
    _HwFlashDevFree_Type()
)
hwFlashDevFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlashDevFree.setStatus("current")
_HwFlashDevEraseTime_Type = TimeTicks
_HwFlashDevEraseTime_Object = MibTableColumn
hwFlashDevEraseTime = _HwFlashDevEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1, 4),
    _HwFlashDevEraseTime_Type()
)
hwFlashDevEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlashDevEraseTime.setStatus("current")


class _HwFlashDevEraseStatus_Type(Integer32):
    """Custom type hwFlashDevEraseStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashErasedFail", 3),
          ("flashErasedSuccessful", 2),
          ("flashErasing", 1),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4),
          ("noEraseAfterPowerOn", 7))
    )


_HwFlashDevEraseStatus_Type.__name__ = "Integer32"
_HwFlashDevEraseStatus_Object = MibTableColumn
hwFlashDevEraseStatus = _HwFlashDevEraseStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1, 5),
    _HwFlashDevEraseStatus_Type()
)
hwFlashDevEraseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlashDevEraseStatus.setStatus("current")


class _HwFlashDevStatus_Type(Integer32):
    """Custom type hwFlashDevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("busy", 1))
    )


_HwFlashDevStatus_Type.__name__ = "Integer32"
_HwFlashDevStatus_Object = MibTableColumn
hwFlashDevStatus = _HwFlashDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 6, 1, 1, 6),
    _HwFlashDevStatus_Type()
)
hwFlashDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlashDevStatus.setStatus("current")
_HwAlarmInfo_ObjectIdentity = ObjectIdentity
hwAlarmInfo = _HwAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7)
)
_HwAlarmTable_Object = MibTable
hwAlarmTable = _HwAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7, 1)
)
if mibBuilder.loadTexts:
    hwAlarmTable.setStatus("obsolete")
_HwAlarmEntry_Object = MibTableRow
hwAlarmEntry = _HwAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7, 1, 1)
)
hwAlarmEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwAlarmSerialIndex"),
)
if mibBuilder.loadTexts:
    hwAlarmEntry.setStatus("obsolete")


class _HwAlarmSerialIndex_Type(Integer32):
    """Custom type hwAlarmSerialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwAlarmSerialIndex_Type.__name__ = "Integer32"
_HwAlarmSerialIndex_Object = MibTableColumn
hwAlarmSerialIndex = _HwAlarmSerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7, 1, 1, 1),
    _HwAlarmSerialIndex_Type()
)
hwAlarmSerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmSerialIndex.setStatus("obsolete")


class _HwAlarmType_Type(Integer32):
    """Custom type hwAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("event", 3),
          ("restore", 2))
    )


_HwAlarmType_Type.__name__ = "Integer32"
_HwAlarmType_Object = MibTableColumn
hwAlarmType = _HwAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7, 1, 1, 2),
    _HwAlarmType_Type()
)
hwAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmType.setStatus("obsolete")
_HwAlarmOcurTime_Type = DateAndTime
_HwAlarmOcurTime_Object = MibTableColumn
hwAlarmOcurTime = _HwAlarmOcurTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7, 1, 1, 3),
    _HwAlarmOcurTime_Type()
)
hwAlarmOcurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAlarmOcurTime.setStatus("obsolete")
_TrapObjectIdValue_Type = OctetString
_TrapObjectIdValue_Object = MibTableColumn
trapObjectIdValue = _TrapObjectIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 7, 1, 1, 4),
    _TrapObjectIdValue_Type()
)
trapObjectIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapObjectIdValue.setStatus("obsolete")
_HwDevTraps_ObjectIdentity = ObjectIdentity
hwDevTraps = _HwDevTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8)
)
_HwDevTrapVbOids_ObjectIdentity = ObjectIdentity
hwDevTrapVbOids = _HwDevTrapVbOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 1)
)


class _HwFrameAdminResult_Type(Integer32):
    """Custom type hwFrameAdminResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_HwFrameAdminResult_Type.__name__ = "Integer32"
_HwFrameAdminResult_Object = MibScalar
hwFrameAdminResult = _HwFrameAdminResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 1, 1),
    _HwFrameAdminResult_Type()
)
hwFrameAdminResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFrameAdminResult.setStatus("current")


class _HwSlotAdminResult_Type(Integer32):
    """Custom type hwSlotAdminResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_HwSlotAdminResult_Type.__name__ = "Integer32"
_HwSlotAdminResult_Object = MibScalar
hwSlotAdminResult = _HwSlotAdminResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 1, 2),
    _HwSlotAdminResult_Type()
)
hwSlotAdminResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSlotAdminResult.setStatus("current")


class _HwSubslotAdminResult_Type(Integer32):
    """Custom type hwSubslotAdminResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_HwSubslotAdminResult_Type.__name__ = "Integer32"
_HwSubslotAdminResult_Object = MibScalar
hwSubslotAdminResult = _HwSubslotAdminResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 1, 3),
    _HwSubslotAdminResult_Type()
)
hwSubslotAdminResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSubslotAdminResult.setStatus("current")


class _HwPortAdminResult_Type(Integer32):
    """Custom type hwPortAdminResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("success", 1))
    )


_HwPortAdminResult_Type.__name__ = "Integer32"
_HwPortAdminResult_Object = MibScalar
hwPortAdminResult = _HwPortAdminResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 1, 4),
    _HwPortAdminResult_Type()
)
hwPortAdminResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPortAdminResult.setStatus("current")
_HwDevGeneralTraps_ObjectIdentity = ObjectIdentity
hwDevGeneralTraps = _HwDevGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 5, 0)
)
_HwCliUserMgmt_ObjectIdentity = ObjectIdentity
hwCliUserMgmt = _HwCliUserMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10)
)
_HwCliUserParaTable_Object = MibTable
hwCliUserParaTable = _HwCliUserParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1)
)
if mibBuilder.loadTexts:
    hwCliUserParaTable.setStatus("current")
_HwCliUserParaEntry_Object = MibTableRow
hwCliUserParaEntry = _HwCliUserParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1)
)
hwCliUserParaEntry.setIndexNames(
    (1, "HUAWEI-DEVICE-MIB", "hwCliUserName"),
)
if mibBuilder.loadTexts:
    hwCliUserParaEntry.setStatus("current")


class _HwCliUserName_Type(OctetString):
    """Custom type hwCliUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HwCliUserName_Type.__name__ = "OctetString"
_HwCliUserName_Object = MibTableColumn
hwCliUserName = _HwCliUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1, 1),
    _HwCliUserName_Type()
)
hwCliUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCliUserName.setStatus("current")


class _HwCliUserPassword_Type(OctetString):
    """Custom type hwCliUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HwCliUserPassword_Type.__name__ = "OctetString"
_HwCliUserPassword_Object = MibTableColumn
hwCliUserPassword = _HwCliUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1, 2),
    _HwCliUserPassword_Type()
)
hwCliUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCliUserPassword.setStatus("current")


class _HwCliUserLevel_Type(Integer32):
    """Custom type hwCliUserLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 3),
          ("common", 1),
          ("operator", 2))
    )


_HwCliUserLevel_Type.__name__ = "Integer32"
_HwCliUserLevel_Object = MibTableColumn
hwCliUserLevel = _HwCliUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1, 3),
    _HwCliUserLevel_Type()
)
hwCliUserLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCliUserLevel.setStatus("current")


class _HwCliUserLogins_Type(Integer32):
    """Custom type hwCliUserLogins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwCliUserLogins_Type.__name__ = "Integer32"
_HwCliUserLogins_Object = MibTableColumn
hwCliUserLogins = _HwCliUserLogins_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1, 4),
    _HwCliUserLogins_Type()
)
hwCliUserLogins.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCliUserLogins.setStatus("current")


class _HwCliUserDecr_Type(OctetString):
    """Custom type hwCliUserDecr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HwCliUserDecr_Type.__name__ = "OctetString"
_HwCliUserDecr_Object = MibTableColumn
hwCliUserDecr = _HwCliUserDecr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1, 5),
    _HwCliUserDecr_Type()
)
hwCliUserDecr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCliUserDecr.setStatus("current")
_HwCliUserRowStatus_Type = RowStatus
_HwCliUserRowStatus_Object = MibTableColumn
hwCliUserRowStatus = _HwCliUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 1, 1, 6),
    _HwCliUserRowStatus_Type()
)
hwCliUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCliUserRowStatus.setStatus("current")
_HwCliClientTable_Object = MibTable
hwCliClientTable = _HwCliClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2)
)
if mibBuilder.loadTexts:
    hwCliClientTable.setStatus("current")
_HwCliClientEntry_Object = MibTableRow
hwCliClientEntry = _HwCliClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1)
)
hwCliClientEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwCliClientID"),
)
if mibBuilder.loadTexts:
    hwCliClientEntry.setStatus("current")


class _HwCliClientID_Type(Integer32):
    """Custom type hwCliClientID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwCliClientID_Type.__name__ = "Integer32"
_HwCliClientID_Object = MibTableColumn
hwCliClientID = _HwCliClientID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1, 1),
    _HwCliClientID_Type()
)
hwCliClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCliClientID.setStatus("current")


class _HwCliClientUserName_Type(OctetString):
    """Custom type hwCliClientUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HwCliClientUserName_Type.__name__ = "OctetString"
_HwCliClientUserName_Object = MibTableColumn
hwCliClientUserName = _HwCliClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1, 2),
    _HwCliClientUserName_Type()
)
hwCliClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCliClientUserName.setStatus("current")


class _HwCliClientType_Type(Integer32):
    """Custom type hwCliClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serial", 1),
          ("telnet", 2))
    )


_HwCliClientType_Type.__name__ = "Integer32"
_HwCliClientType_Object = MibTableColumn
hwCliClientType = _HwCliClientType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1, 3),
    _HwCliClientType_Type()
)
hwCliClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCliClientType.setStatus("current")
_HwCliClientIp_Type = IpAddress
_HwCliClientIp_Object = MibTableColumn
hwCliClientIp = _HwCliClientIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1, 4),
    _HwCliClientIp_Type()
)
hwCliClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCliClientIp.setStatus("current")
_HwCliClientLoginTime_Type = DateAndTime
_HwCliClientLoginTime_Object = MibTableColumn
hwCliClientLoginTime = _HwCliClientLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1, 5),
    _HwCliClientLoginTime_Type()
)
hwCliClientLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCliClientLoginTime.setStatus("current")


class _HwCliClientAdminStatus_Type(Integer32):
    """Custom type hwCliClientAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("disconnect", 1)
    )


_HwCliClientAdminStatus_Type.__name__ = "Integer32"
_HwCliClientAdminStatus_Object = MibTableColumn
hwCliClientAdminStatus = _HwCliClientAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 10, 2, 1, 6),
    _HwCliClientAdminStatus_Type()
)
hwCliClientAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCliClientAdminStatus.setStatus("current")
_HwDevCompatibleTable_ObjectIdentity = ObjectIdentity
hwDevCompatibleTable = _HwDevCompatibleTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 11)
)
_HwCompatibleSysOid_Type = ObjectIdentifier
_HwCompatibleSysOid_Object = MibScalar
hwCompatibleSysOid = _HwCompatibleSysOid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 11, 1),
    _HwCompatibleSysOid_Type()
)
hwCompatibleSysOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCompatibleSysOid.setStatus("current")


class _HwCompatibleVersion_Type(OctetString):
    """Custom type hwCompatibleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwCompatibleVersion_Type.__name__ = "OctetString"
_HwCompatibleVersion_Object = MibScalar
hwCompatibleVersion = _HwCompatibleVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 11, 2),
    _HwCompatibleVersion_Type()
)
hwCompatibleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCompatibleVersion.setStatus("current")


class _HwCompatibleVRCB_Type(OctetString):
    """Custom type hwCompatibleVRCB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwCompatibleVRCB_Type.__name__ = "OctetString"
_HwCompatibleVRCB_Object = MibScalar
hwCompatibleVRCB = _HwCompatibleVRCB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 11, 3),
    _HwCompatibleVRCB_Type()
)
hwCompatibleVRCB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCompatibleVRCB.setStatus("current")


class _HwCompatibleProductName_Type(OctetString):
    """Custom type hwCompatibleProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwCompatibleProductName_Type.__name__ = "OctetString"
_HwCompatibleProductName_Object = MibScalar
hwCompatibleProductName = _HwCompatibleProductName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 11, 4),
    _HwCompatibleProductName_Type()
)
hwCompatibleProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCompatibleProductName.setStatus("current")

# Managed Objects groups


# Notification objects

hwFrameAdminResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 5, 0, 1)
)
hwFrameAdminResultTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwFrameAdminStatus"),
        ("HUAWEI-DEVICE-MIB", "hwFrameAdminResult"))
)
if mibBuilder.loadTexts:
    hwFrameAdminResultTrap.setStatus(
        "current"
    )

hwSlotAdminResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 5, 0, 2)
)
hwSlotAdminResultTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotAdminStatus"),
        ("HUAWEI-DEVICE-MIB", "hwSlotAdminResult"))
)
if mibBuilder.loadTexts:
    hwSlotAdminResultTrap.setStatus(
        "current"
    )

hwSubSlotAdminResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 5, 0, 3)
)
hwSubSlotAdminResultTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSubslotIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSubslotAdminStatus"),
        ("HUAWEI-DEVICE-MIB", "hwSubslotAdminResult"))
)
if mibBuilder.loadTexts:
    hwSubSlotAdminResultTrap.setStatus(
        "current"
    )

hwPortAdminResultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 3, 8, 5, 0, 4)
)
hwPortAdminResultTrap.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSubslotIndex"),
        ("HUAWEI-DEVICE-MIB", "hwPortIndex"),
        ("HUAWEI-DEVICE-MIB", "hwPortAdminStatus"),
        ("HUAWEI-DEVICE-MIB", "hwPortAdminResult"))
)
if mibBuilder.loadTexts:
    hwPortAdminResultTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DEVICE-MIB",
    **{"hwDev": hwDev,
       "hwSystemPara": hwSystemPara,
       "hwSysIpAddr": hwSysIpAddr,
       "hwSysIpMask": hwSysIpMask,
       "hwSysVersion": hwSysVersion,
       "hwSysTime": hwSysTime,
       "hwNmsParaTable": hwNmsParaTable,
       "hwNmsParaEntry": hwNmsParaEntry,
       "hwNmsIndex": hwNmsIndex,
       "hwNmsName": hwNmsName,
       "hwNmsIp": hwNmsIp,
       "hwNmsMask": hwNmsMask,
       "hwNmsMaintainMode": hwNmsMaintainMode,
       "hwNmsGetCommunity": hwNmsGetCommunity,
       "hwNmsSetCommunity": hwNmsSetCommunity,
       "hwNmsSnmpPort": hwNmsSnmpPort,
       "hwNmsTrapPort": hwNmsTrapPort,
       "hwNmsClass": hwNmsClass,
       "hwNmsStatus": hwNmsStatus,
       "hwSlotConf": hwSlotConf,
       "hwFrameTable": hwFrameTable,
       "hwFrameEntry": hwFrameEntry,
       "hwFrameIndex": hwFrameIndex,
       "hwFrameType": hwFrameType,
       "hwFrameDesc": hwFrameDesc,
       "hwSlots": hwSlots,
       "hwFrameOperStatus": hwFrameOperStatus,
       "hwFrameAdminStatus": hwFrameAdminStatus,
       "hwFrameRowStatus": hwFrameRowStatus,
       "hwSlotTable": hwSlotTable,
       "hwSlotEntry": hwSlotEntry,
       "hwSlotIndex": hwSlotIndex,
       "hwSlotType": hwSlotType,
       "hwSlotDesc": hwSlotDesc,
       "hwSlotPcbVersion": hwSlotPcbVersion,
       "hwSlotVersion": hwSlotVersion,
       "hwSlotWorkMode": hwSlotWorkMode,
       "hwSubSlots": hwSubSlots,
       "hwSlotOperStatus": hwSlotOperStatus,
       "hwSlotAdminStatus": hwSlotAdminStatus,
       "hwSlotRowStatus": hwSlotRowStatus,
       "hwSlotPhySerialNum": hwSlotPhySerialNum,
       "hwSubslotTable": hwSubslotTable,
       "hwSubslotEntry": hwSubslotEntry,
       "hwSubslotIndex": hwSubslotIndex,
       "hwSubslotType": hwSubslotType,
       "hwSubslotPorts": hwSubslotPorts,
       "hwSubslotOperStatus": hwSubslotOperStatus,
       "hwSubslotAdminStatus": hwSubslotAdminStatus,
       "hwSubslotVersion": hwSubslotVersion,
       "hwSubSlotDesc": hwSubSlotDesc,
       "hwSubslotRowStatus": hwSubslotRowStatus,
       "hwPortTable": hwPortTable,
       "hwPortEntry": hwPortEntry,
       "hwPortIndex": hwPortIndex,
       "hwPortType": hwPortType,
       "hwPortDesc": hwPortDesc,
       "hwPortSpeed": hwPortSpeed,
       "hwPortOperStatus": hwPortOperStatus,
       "hwPortAdminStatus": hwPortAdminStatus,
       "hwFrameLinks": hwFrameLinks,
       "hwFrameLinkNumber": hwFrameLinkNumber,
       "hwFrameLinkTable": hwFrameLinkTable,
       "hwFrameLinkEntry": hwFrameLinkEntry,
       "hwFrameLinkIndex": hwFrameLinkIndex,
       "hwFrameLinkLeftFrame": hwFrameLinkLeftFrame,
       "hwFrameLinkLeftSlot": hwFrameLinkLeftSlot,
       "hwFrameLinkLeftSubSlot": hwFrameLinkLeftSubSlot,
       "hwFrameLinkLeftPort": hwFrameLinkLeftPort,
       "hwFrameLinkRightFrame": hwFrameLinkRightFrame,
       "hwFrameLinkRightSlot": hwFrameLinkRightSlot,
       "hwFrameLinkRightSubSlot": hwFrameLinkRightSubSlot,
       "hwFrameLinkRightPort": hwFrameLinkRightPort,
       "hwFrameLinkOperStatus": hwFrameLinkOperStatus,
       "hwFrameLinkRowStatus": hwFrameLinkRowStatus,
       "hwFrameLinkNextIndex": hwFrameLinkNextIndex,
       "hwNarrowBoard": hwNarrowBoard,
       "hwBoardAttrTable": hwBoardAttrTable,
       "hwBoardAttrEntry": hwBoardAttrEntry,
       "hwBoardAulaw": hwBoardAulaw,
       "hwBoardCurrent": hwBoardCurrent,
       "hwBoardImpedance": hwBoardImpedance,
       "hwCpuDevTable": hwCpuDevTable,
       "hwCpuDevEntry": hwCpuDevEntry,
       "hwCpuDevIndex": hwCpuDevIndex,
       "hwCpuDevDuty": hwCpuDevDuty,
       "hwAvgDuty1min": hwAvgDuty1min,
       "hwAvgDuty5min": hwAvgDuty5min,
       "hwMemoryDev": hwMemoryDev,
       "hwMemoryDevTable": hwMemoryDevTable,
       "hwMemoryDevEntry": hwMemoryDevEntry,
       "hwMemoryDevModuleIndex": hwMemoryDevModuleIndex,
       "hwMemoryDevSize": hwMemoryDevSize,
       "hwMemoryDevFree": hwMemoryDevFree,
       "hwMemoryDevRawSliceUsed": hwMemoryDevRawSliceUsed,
       "hwMemoryDevLargestFree": hwMemoryDevLargestFree,
       "hwMemoryDevFail": hwMemoryDevFail,
       "hwMemoryDevFailNoMem": hwMemoryDevFailNoMem,
       "hwBufferTable": hwBufferTable,
       "hwBufferEntry": hwBufferEntry,
       "hwBufferModuleIndex": hwBufferModuleIndex,
       "hwBufferSize": hwBufferSize,
       "hwBufferCurrentTotal": hwBufferCurrentTotal,
       "hwBufferCurrentUsed": hwBufferCurrentUsed,
       "hwFlashDev": hwFlashDev,
       "hwFlashDevTable": hwFlashDevTable,
       "hwFlashDevEntry": hwFlashDevEntry,
       "hwFlashDevIndex": hwFlashDevIndex,
       "hwFlashDevSize": hwFlashDevSize,
       "hwFlashDevFree": hwFlashDevFree,
       "hwFlashDevEraseTime": hwFlashDevEraseTime,
       "hwFlashDevEraseStatus": hwFlashDevEraseStatus,
       "hwFlashDevStatus": hwFlashDevStatus,
       "hwAlarmInfo": hwAlarmInfo,
       "hwAlarmTable": hwAlarmTable,
       "hwAlarmEntry": hwAlarmEntry,
       "hwAlarmSerialIndex": hwAlarmSerialIndex,
       "hwAlarmType": hwAlarmType,
       "hwAlarmOcurTime": hwAlarmOcurTime,
       "trapObjectIdValue": trapObjectIdValue,
       "hwDevTraps": hwDevTraps,
       "hwDevTrapVbOids": hwDevTrapVbOids,
       "hwFrameAdminResult": hwFrameAdminResult,
       "hwSlotAdminResult": hwSlotAdminResult,
       "hwSubslotAdminResult": hwSubslotAdminResult,
       "hwPortAdminResult": hwPortAdminResult,
       "hwDevGeneralTraps": hwDevGeneralTraps,
       "hwFrameAdminResultTrap": hwFrameAdminResultTrap,
       "hwSlotAdminResultTrap": hwSlotAdminResultTrap,
       "hwSubSlotAdminResultTrap": hwSubSlotAdminResultTrap,
       "hwPortAdminResultTrap": hwPortAdminResultTrap,
       "hwCliUserMgmt": hwCliUserMgmt,
       "hwCliUserParaTable": hwCliUserParaTable,
       "hwCliUserParaEntry": hwCliUserParaEntry,
       "hwCliUserName": hwCliUserName,
       "hwCliUserPassword": hwCliUserPassword,
       "hwCliUserLevel": hwCliUserLevel,
       "hwCliUserLogins": hwCliUserLogins,
       "hwCliUserDecr": hwCliUserDecr,
       "hwCliUserRowStatus": hwCliUserRowStatus,
       "hwCliClientTable": hwCliClientTable,
       "hwCliClientEntry": hwCliClientEntry,
       "hwCliClientID": hwCliClientID,
       "hwCliClientUserName": hwCliClientUserName,
       "hwCliClientType": hwCliClientType,
       "hwCliClientIp": hwCliClientIp,
       "hwCliClientLoginTime": hwCliClientLoginTime,
       "hwCliClientAdminStatus": hwCliClientAdminStatus,
       "hwDevCompatibleTable": hwDevCompatibleTable,
       "hwCompatibleSysOid": hwCompatibleSysOid,
       "hwCompatibleVersion": hwCompatibleVersion,
       "hwCompatibleVRCB": hwCompatibleVRCB,
       "hwCompatibleProductName": hwCompatibleProductName}
)
