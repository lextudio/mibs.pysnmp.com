# SNMP MIB module (FD-ONU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FD-ONU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:28 2024
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

(DeviceOperation,
 DeviceStatus,
 DeviceType,
 OperSwitch,
 epon) = mibBuilder.importSymbols(
    "EPON-EOC-MIB",
    "DeviceOperation",
    "DeviceStatus",
    "DeviceType",
    "OperSwitch",
    "epon")

(linkId,
 oltId) = mibBuilder.importSymbols(
    "FD-OLT-MIB",
    "linkId",
    "oltId")

(ponCardSlotId,) = mibBuilder.importSymbols(
    "FD-SYSTEM-MIB",
    "ponCardSlotId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

fdOnu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OnuBaseManageTable_Object = MibTable
onuBaseManageTable = _OnuBaseManageTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    onuBaseManageTable.setStatus("current")
_OnuBaseManageEntry_Object = MibTableRow
onuBaseManageEntry = _OnuBaseManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1)
)
onuBaseManageEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuBaseManageEntry.setStatus("current")


class _OnuId_Type(Integer32):
    """Custom type onuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OnuId_Type.__name__ = "Integer32"
_OnuId_Object = MibTableColumn
onuId = _OnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 1),
    _OnuId_Type()
)
onuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuId.setStatus("current")
_OnuDeviceType_Type = DeviceType
_OnuDeviceType_Object = MibTableColumn
onuDeviceType = _OnuDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 2),
    _OnuDeviceType_Type()
)
onuDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuDeviceType.setStatus("current")


class _OnuFactorySerial_Type(OctetString):
    """Custom type onuFactorySerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OnuFactorySerial_Type.__name__ = "OctetString"
_OnuFactorySerial_Object = MibTableColumn
onuFactorySerial = _OnuFactorySerial_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 3),
    _OnuFactorySerial_Type()
)
onuFactorySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuFactorySerial.setStatus("current")
_OnuUserInfo_Type = DisplayString
_OnuUserInfo_Object = MibTableColumn
onuUserInfo = _OnuUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 4),
    _OnuUserInfo_Type()
)
onuUserInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUserInfo.setStatus("current")
_OnuHwRev_Type = DisplayString
_OnuHwRev_Object = MibTableColumn
onuHwRev = _OnuHwRev_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 5),
    _OnuHwRev_Type()
)
onuHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuHwRev.setStatus("current")
_OnuFwRev_Type = DisplayString
_OnuFwRev_Object = MibTableColumn
onuFwRev = _OnuFwRev_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 6),
    _OnuFwRev_Type()
)
onuFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuFwRev.setStatus("current")
_OnuBaseMac_Type = MacAddress
_OnuBaseMac_Object = MibTableColumn
onuBaseMac = _OnuBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 7),
    _OnuBaseMac_Type()
)
onuBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuBaseMac.setStatus("current")


class _MaxAllowedLLIDs_Type(Integer32):
    """Custom type maxAllowedLLIDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MaxAllowedLLIDs_Type.__name__ = "Integer32"
_MaxAllowedLLIDs_Object = MibTableColumn
maxAllowedLLIDs = _MaxAllowedLLIDs_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 9),
    _MaxAllowedLLIDs_Type()
)
maxAllowedLLIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAllowedLLIDs.setStatus("current")


class _RegisteredLLIDNum_Type(Integer32):
    """Custom type registeredLLIDNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RegisteredLLIDNum_Type.__name__ = "Integer32"
_RegisteredLLIDNum_Object = MibTableColumn
registeredLLIDNum = _RegisteredLLIDNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 10),
    _RegisteredLLIDNum_Type()
)
registeredLLIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registeredLLIDNum.setStatus("current")
_OnuOnLineStatus_Type = DeviceStatus
_OnuOnLineStatus_Object = MibTableColumn
onuOnLineStatus = _OnuOnLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 11),
    _OnuOnLineStatus_Type()
)
onuOnLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuOnLineStatus.setStatus("current")
_OnuUserTrafficEnable_Type = OperSwitch
_OnuUserTrafficEnable_Object = MibTableColumn
onuUserTrafficEnable = _OnuUserTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 12),
    _OnuUserTrafficEnable_Type()
)
onuUserTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUserTrafficEnable.setStatus("current")
_OnuRangeValue_Type = Integer32
_OnuRangeValue_Object = MibTableColumn
onuRangeValue = _OnuRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 13),
    _OnuRangeValue_Type()
)
onuRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuRangeValue.setStatus("current")


class _SupportUniPorts_Type(Integer32):
    """Custom type supportUniPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SupportUniPorts_Type.__name__ = "Integer32"
_SupportUniPorts_Object = MibTableColumn
supportUniPorts = _SupportUniPorts_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 14),
    _SupportUniPorts_Type()
)
supportUniPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supportUniPorts.setStatus("current")
_OnuOperation_Type = DeviceOperation
_OnuOperation_Object = MibTableColumn
onuOperation = _OnuOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 32),
    _OnuOperation_Type()
)
onuOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuOperation.setStatus("current")


class _OnuUpgradeStat_Type(Integer32):
    """Custom type onuUpgradeStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("booting", 1),
          ("normalRun", 2),
          ("upgradeErr", 8),
          ("upgradeOk", 7),
          ("upgrading", 6))
    )


_OnuUpgradeStat_Type.__name__ = "Integer32"
_OnuUpgradeStat_Object = MibTableColumn
onuUpgradeStat = _OnuUpgradeStat_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 33),
    _OnuUpgradeStat_Type()
)
onuUpgradeStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuUpgradeStat.setStatus("current")


class _OnuLinkIdMap_Type(OctetString):
    """Custom type onuLinkIdMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_OnuLinkIdMap_Type.__name__ = "OctetString"
_OnuLinkIdMap_Object = MibTableColumn
onuLinkIdMap = _OnuLinkIdMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 34),
    _OnuLinkIdMap_Type()
)
onuLinkIdMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLinkIdMap.setStatus("current")


class _OnuMgmtType_Type(Integer32):
    """Custom type onuMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 2),
          ("tk", 1))
    )


_OnuMgmtType_Type.__name__ = "Integer32"
_OnuMgmtType_Object = MibTableColumn
onuMgmtType = _OnuMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 35),
    _OnuMgmtType_Type()
)
onuMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMgmtType.setStatus("current")
_OnuLaserRxPower_Type = Integer32
_OnuLaserRxPower_Object = MibTableColumn
onuLaserRxPower = _OnuLaserRxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 36),
    _OnuLaserRxPower_Type()
)
onuLaserRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLaserRxPower.setStatus("current")
_OnuLaserTxPower_Type = Integer32
_OnuLaserTxPower_Object = MibTableColumn
onuLaserTxPower = _OnuLaserTxPower_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 1, 1, 37),
    _OnuLaserTxPower_Type()
)
onuLaserTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLaserTxPower.setStatus("current")
_OnuAdvancedManage_ObjectIdentity = ObjectIdentity
onuAdvancedManage = _OnuAdvancedManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2)
)
_OnuChipInfoTable_Object = MibTable
onuChipInfoTable = _OnuChipInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    onuChipInfoTable.setStatus("current")
_OnuChipInfoEntry_Object = MibTableRow
onuChipInfoEntry = _OnuChipInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1)
)
onuChipInfoEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuChipInfoEntry.setStatus("current")
_OnuChipProCode_Type = Integer32
_OnuChipProCode_Object = MibTableColumn
onuChipProCode = _OnuChipProCode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 1),
    _OnuChipProCode_Type()
)
onuChipProCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipProCode.setStatus("current")
_OnuChipProVer_Type = Integer32
_OnuChipProVer_Object = MibTableColumn
onuChipProVer = _OnuChipProVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 2),
    _OnuChipProVer_Type()
)
onuChipProVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipProVer.setStatus("current")
_OnuChipId_Type = Integer32
_OnuChipId_Object = MibTableColumn
onuChipId = _OnuChipId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 3),
    _OnuChipId_Type()
)
onuChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipId.setStatus("current")
_OnuChipVer_Type = Integer32
_OnuChipVer_Object = MibTableColumn
onuChipVer = _OnuChipVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 4),
    _OnuChipVer_Type()
)
onuChipVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipVer.setStatus("current")
_OnuBootVer_Type = Integer32
_OnuBootVer_Object = MibTableColumn
onuBootVer = _OnuBootVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 5),
    _OnuBootVer_Type()
)
onuBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuBootVer.setStatus("current")
_OnuPersVer_Type = Integer32
_OnuPersVer_Object = MibTableColumn
onuPersVer = _OnuPersVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 6),
    _OnuPersVer_Type()
)
onuPersVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuPersVer.setStatus("current")
_OnuChipApp0Ver_Type = Integer32
_OnuChipApp0Ver_Object = MibTableColumn
onuChipApp0Ver = _OnuChipApp0Ver_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 7),
    _OnuChipApp0Ver_Type()
)
onuChipApp0Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipApp0Ver.setStatus("current")
_OnuChipApp1Ver_Type = Integer32
_OnuChipApp1Ver_Object = MibTableColumn
onuChipApp1Ver = _OnuChipApp1Ver_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 8),
    _OnuChipApp1Ver_Type()
)
onuChipApp1Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipApp1Ver.setStatus("current")
_OnuChipDiagVer_Type = Integer32
_OnuChipDiagVer_Object = MibTableColumn
onuChipDiagVer = _OnuChipDiagVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 1, 1, 9),
    _OnuChipDiagVer_Type()
)
onuChipDiagVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipDiagVer.setStatus("current")
_OnuAdvancedConfigTable_Object = MibTable
onuAdvancedConfigTable = _OnuAdvancedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    onuAdvancedConfigTable.setStatus("current")
_OnuAdvancedConfigEntry_Object = MibTableRow
onuAdvancedConfigEntry = _OnuAdvancedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 2, 1)
)
onuAdvancedConfigEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuAdvancedConfigEntry.setStatus("current")


class _OnuAddiVlanEthType_Type(OctetString):
    """Custom type onuAddiVlanEthType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OnuAddiVlanEthType_Type.__name__ = "OctetString"
_OnuAddiVlanEthType_Object = MibTableColumn
onuAddiVlanEthType = _OnuAddiVlanEthType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 2, 1, 1),
    _OnuAddiVlanEthType_Type()
)
onuAddiVlanEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAddiVlanEthType.setStatus("current")
_OnuRstpEnable_Type = OperSwitch
_OnuRstpEnable_Object = MibTableColumn
onuRstpEnable = _OnuRstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 2, 1, 2),
    _OnuRstpEnable_Type()
)
onuRstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuRstpEnable.setStatus("current")
_OnuLocalSwitch_Type = OperSwitch
_OnuLocalSwitch_Object = MibTableColumn
onuLocalSwitch = _OnuLocalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 2, 1, 3),
    _OnuLocalSwitch_Type()
)
onuLocalSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuLocalSwitch.setStatus("current")
_OnuCatv_Type = OperSwitch
_OnuCatv_Object = MibTableColumn
onuCatv = _OnuCatv_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 2, 2, 1, 4),
    _OnuCatv_Type()
)
onuCatv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatv.setStatus("current")
_OnuUniPortTable_Object = MibTable
onuUniPortTable = _OnuUniPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    onuUniPortTable.setStatus("current")
_OnuUniPortEntry_Object = MibTableRow
onuUniPortEntry = _OnuUniPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1)
)
onuUniPortEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
)
if mibBuilder.loadTexts:
    onuUniPortEntry.setStatus("current")


class _UniPortId_Type(Integer32):
    """Custom type uniPortId based on Integer32"""
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
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("uniPort1", 1),
          ("uniPort10", 10),
          ("uniPort11", 11),
          ("uniPort12", 12),
          ("uniPort13", 13),
          ("uniPort14", 14),
          ("uniPort15", 15),
          ("uniPort16", 16),
          ("uniPort17", 17),
          ("uniPort18", 18),
          ("uniPort19", 19),
          ("uniPort2", 2),
          ("uniPort20", 20),
          ("uniPort21", 21),
          ("uniPort22", 22),
          ("uniPort23", 23),
          ("uniPort24", 24),
          ("uniPort25", 25),
          ("uniPort26", 26),
          ("uniPort27", 27),
          ("uniPort28", 28),
          ("uniPort29", 29),
          ("uniPort3", 3),
          ("uniPort30", 30),
          ("uniPort31", 31),
          ("uniPort32", 32),
          ("uniPort33", 33),
          ("uniPort34", 34),
          ("uniPort35", 35),
          ("uniPort36", 36),
          ("uniPort37", 37),
          ("uniPort38", 38),
          ("uniPort39", 39),
          ("uniPort4", 4),
          ("uniPort40", 40),
          ("uniPort41", 41),
          ("uniPort42", 42),
          ("uniPort43", 43),
          ("uniPort44", 44),
          ("uniPort45", 45),
          ("uniPort46", 46),
          ("uniPort47", 47),
          ("uniPort48", 48),
          ("uniPort5", 5),
          ("uniPort6", 6),
          ("uniPort7", 7),
          ("uniPort8", 8),
          ("uniPort9", 9))
    )


_UniPortId_Type.__name__ = "Integer32"
_UniPortId_Object = MibTableColumn
uniPortId = _UniPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 1),
    _UniPortId_Type()
)
uniPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortId.setStatus("current")
_UniPortUserInfo_Type = DisplayString
_UniPortUserInfo_Object = MibTableColumn
uniPortUserInfo = _UniPortUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 2),
    _UniPortUserInfo_Type()
)
uniPortUserInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortUserInfo.setStatus("current")


class _UniPortLink_Type(Integer32):
    """Custom type uniPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 2),
          ("linkup", 1))
    )


_UniPortLink_Type.__name__ = "Integer32"
_UniPortLink_Object = MibTableColumn
uniPortLink = _UniPortLink_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 3),
    _UniPortLink_Type()
)
uniPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniPortLink.setStatus("current")
_UniPortAutoNego_Type = OperSwitch
_UniPortAutoNego_Object = MibTableColumn
uniPortAutoNego = _UniPortAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 4),
    _UniPortAutoNego_Type()
)
uniPortAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortAutoNego.setStatus("current")


class _UniPortSpeed_Type(Integer32):
    """Custom type uniPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mbps10", 1),
          ("mbps100", 2),
          ("mbps1000", 3))
    )


_UniPortSpeed_Type.__name__ = "Integer32"
_UniPortSpeed_Object = MibTableColumn
uniPortSpeed = _UniPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 5),
    _UniPortSpeed_Type()
)
uniPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortSpeed.setStatus("current")


class _UniPortDuplex_Type(Integer32):
    """Custom type uniPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_UniPortDuplex_Type.__name__ = "Integer32"
_UniPortDuplex_Object = MibTableColumn
uniPortDuplex = _UniPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 6),
    _UniPortDuplex_Type()
)
uniPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortDuplex.setStatus("current")
_UniPortFlowCtrl_Type = OperSwitch
_UniPortFlowCtrl_Object = MibTableColumn
uniPortFlowCtrl = _UniPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 7),
    _UniPortFlowCtrl_Type()
)
uniPortFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortFlowCtrl.setStatus("current")


class _UniPortMacEntryLimit_Type(Integer32):
    """Custom type uniPortMacEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_UniPortMacEntryLimit_Type.__name__ = "Integer32"
_UniPortMacEntryLimit_Object = MibTableColumn
uniPortMacEntryLimit = _UniPortMacEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 8),
    _UniPortMacEntryLimit_Type()
)
uniPortMacEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortMacEntryLimit.setStatus("current")


class _UniPortMacAgeTime_Type(Integer32):
    """Custom type uniPortMacAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 286),
    )


_UniPortMacAgeTime_Type.__name__ = "Integer32"
_UniPortMacAgeTime_Object = MibTableColumn
uniPortMacAgeTime = _UniPortMacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 9),
    _UniPortMacAgeTime_Type()
)
uniPortMacAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortMacAgeTime.setStatus("current")


class _UniPortFowardMode_Type(Integer32):
    """Custom type uniPortFowardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d8021mode", 1),
          ("dropUntilLearned", 2))
    )


_UniPortFowardMode_Type.__name__ = "Integer32"
_UniPortFowardMode_Object = MibTableColumn
uniPortFowardMode = _UniPortFowardMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 10),
    _UniPortFowardMode_Type()
)
uniPortFowardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortFowardMode.setStatus("current")
_UniPortEnable_Type = OperSwitch
_UniPortEnable_Object = MibTableColumn
uniPortEnable = _UniPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 11),
    _UniPortEnable_Type()
)
uniPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortEnable.setStatus("current")


class _UniPortRstpState_Type(Integer32):
    """Custom type uniPortRstpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("normal", 1))
    )


_UniPortRstpState_Type.__name__ = "Integer32"
_UniPortRstpState_Object = MibTableColumn
uniPortRstpState = _UniPortRstpState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 3, 1, 12),
    _UniPortRstpState_Type()
)
uniPortRstpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniPortRstpState.setStatus("current")
_OnuQueueCfgTable_Object = MibTable
onuQueueCfgTable = _OnuQueueCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    onuQueueCfgTable.setStatus("current")
_OnuQueueCfgEntry_Object = MibTableRow
onuQueueCfgEntry = _OnuQueueCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 4, 1)
)
onuQueueCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuQueueCfgEntry.setStatus("current")
_OnuQueueCfgData_Type = OctetString
_OnuQueueCfgData_Object = MibTableColumn
onuQueueCfgData = _OnuQueueCfgData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 4, 1, 1),
    _OnuQueueCfgData_Type()
)
onuQueueCfgData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuQueueCfgData.setStatus("current")
_OnuAclRuleTable_Object = MibTable
onuAclRuleTable = _OnuAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    onuAclRuleTable.setStatus("current")
_OnuAclRuleEntry_Object = MibTableRow
onuAclRuleEntry = _OnuAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 5, 1)
)
onuAclRuleEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "onuIntPortId"),
)
if mibBuilder.loadTexts:
    onuAclRuleEntry.setStatus("current")


class _OnuIntPortId_Type(Integer32):
    """Custom type onuIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onuIntUniPort", 2),
          ("onuPonPort", 1))
    )


_OnuIntPortId_Type.__name__ = "Integer32"
_OnuIntPortId_Object = MibTableColumn
onuIntPortId = _OnuIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 5, 1, 1),
    _OnuIntPortId_Type()
)
onuIntPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuIntPortId.setStatus("current")
_OnuAclRuleCfgData_Type = OctetString
_OnuAclRuleCfgData_Object = MibTableColumn
onuAclRuleCfgData = _OnuAclRuleCfgData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 5, 1, 2),
    _OnuAclRuleCfgData_Type()
)
onuAclRuleCfgData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAclRuleCfgData.setStatus("current")
_OnuPortVlanTable_Object = MibTable
onuPortVlanTable = _OnuPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    onuPortVlanTable.setStatus("current")
_OnuPortVlanEntry_Object = MibTableRow
onuPortVlanEntry = _OnuPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 6, 1)
)
onuPortVlanEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "onuPortId"),
)
if mibBuilder.loadTexts:
    onuPortVlanEntry.setStatus("current")


class _OnuPortId_Type(Integer32):
    """Custom type onuPortId based on Integer32"""
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
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("ponPort", 1),
          ("uniPort1", 2),
          ("uniPort10", 11),
          ("uniPort11", 12),
          ("uniPort12", 13),
          ("uniPort13", 14),
          ("uniPort14", 15),
          ("uniPort15", 16),
          ("uniPort16", 17),
          ("uniPort17", 18),
          ("uniPort18", 19),
          ("uniPort19", 20),
          ("uniPort2", 3),
          ("uniPort20", 21),
          ("uniPort21", 22),
          ("uniPort22", 23),
          ("uniPort23", 24),
          ("uniPort24", 25),
          ("uniPort25", 26),
          ("uniPort26", 27),
          ("uniPort27", 28),
          ("uniPort28", 29),
          ("uniPort29", 30),
          ("uniPort3", 4),
          ("uniPort30", 31),
          ("uniPort31", 32),
          ("uniPort32", 33),
          ("uniPort33", 34),
          ("uniPort34", 35),
          ("uniPort35", 36),
          ("uniPort36", 37),
          ("uniPort37", 38),
          ("uniPort38", 39),
          ("uniPort39", 40),
          ("uniPort4", 5),
          ("uniPort40", 41),
          ("uniPort41", 42),
          ("uniPort42", 43),
          ("uniPort43", 44),
          ("uniPort44", 45),
          ("uniPort45", 46),
          ("uniPort46", 47),
          ("uniPort47", 48),
          ("uniPort5", 6),
          ("uniPort6", 7),
          ("uniPort7", 8),
          ("uniPort8", 9),
          ("uniPort9", 10))
    )


_OnuPortId_Type.__name__ = "Integer32"
_OnuPortId_Object = MibTableColumn
onuPortId = _OnuPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 6, 1, 1),
    _OnuPortId_Type()
)
onuPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPortId.setStatus("current")
_OnuPortVlanData_Type = OctetString
_OnuPortVlanData_Object = MibTableColumn
onuPortVlanData = _OnuPortVlanData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 6, 1, 2),
    _OnuPortVlanData_Type()
)
onuPortVlanData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuPortVlanData.setStatus("current")
_OnuPortQos_ObjectIdentity = ObjectIdentity
onuPortQos = _OnuPortQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7)
)
_PortEgressShappingTable_Object = MibTable
portEgressShappingTable = _PortEgressShappingTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    portEgressShappingTable.setStatus("current")
_PortEgressShappingEntry_Object = MibTableRow
portEgressShappingEntry = _PortEgressShappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 1, 1)
)
portEgressShappingEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
)
if mibBuilder.loadTexts:
    portEgressShappingEntry.setStatus("current")


class _ScheduleAlgorithm_Type(Integer32):
    """Custom type scheduleAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 2),
          ("weightedFair", 1))
    )


_ScheduleAlgorithm_Type.__name__ = "Integer32"
_ScheduleAlgorithm_Object = MibTableColumn
scheduleAlgorithm = _ScheduleAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 1, 1, 1),
    _ScheduleAlgorithm_Type()
)
scheduleAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleAlgorithm.setStatus("current")


class _MaxTrafficOutputRate_Type(Integer32):
    """Custom type maxTrafficOutputRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_MaxTrafficOutputRate_Type.__name__ = "Integer32"
_MaxTrafficOutputRate_Object = MibTableColumn
maxTrafficOutputRate = _MaxTrafficOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 1, 1, 2),
    _MaxTrafficOutputRate_Type()
)
maxTrafficOutputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxTrafficOutputRate.setStatus("current")


class _OutputModule_Type(Integer32):
    """Custom type outputModule based on Integer32"""
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


_OutputModule_Type.__name__ = "Integer32"
_OutputModule_Object = MibTableColumn
outputModule = _OutputModule_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 1, 1, 3),
    _OutputModule_Type()
)
outputModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputModule.setStatus("current")
_PortIngressPolicingTable_Object = MibTable
portIngressPolicingTable = _PortIngressPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 2)
)
if mibBuilder.loadTexts:
    portIngressPolicingTable.setStatus("current")
_PortIngressPolicingEntry_Object = MibTableRow
portIngressPolicingEntry = _PortIngressPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 2, 1)
)
portIngressPolicingEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
)
if mibBuilder.loadTexts:
    portIngressPolicingEntry.setStatus("current")


class _PolicingTrafficType_Type(Integer32):
    """Custom type policingTrafficType based on Integer32"""
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
        *(("allFrameTypes", 4),
          ("broadCast", 1),
          ("broadcastMulticastAndFloodedUnicast", 3),
          ("multiCast", 2))
    )


_PolicingTrafficType_Type.__name__ = "Integer32"
_PolicingTrafficType_Object = MibTableColumn
policingTrafficType = _PolicingTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 2, 1, 1),
    _PolicingTrafficType_Type()
)
policingTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policingTrafficType.setStatus("current")


class _MaxTrafficInputRate_Type(Integer32):
    """Custom type maxTrafficInputRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_MaxTrafficInputRate_Type.__name__ = "Integer32"
_MaxTrafficInputRate_Object = MibTableColumn
maxTrafficInputRate = _MaxTrafficInputRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 2, 1, 2),
    _MaxTrafficInputRate_Type()
)
maxTrafficInputRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxTrafficInputRate.setStatus("current")


class _InputModule_Type(Integer32):
    """Custom type inputModule based on Integer32"""
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


_InputModule_Type.__name__ = "Integer32"
_InputModule_Object = MibTableColumn
inputModule = _InputModule_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 7, 2, 1, 3),
    _InputModule_Type()
)
inputModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputModule.setStatus("current")
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8)
)
_IgmpSnoopParaTable_Object = MibTable
igmpSnoopParaTable = _IgmpSnoopParaTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    igmpSnoopParaTable.setStatus("current")
_IgmpSnoopParaEntry_Object = MibTableRow
igmpSnoopParaEntry = _IgmpSnoopParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8, 1, 1)
)
igmpSnoopParaEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    igmpSnoopParaEntry.setStatus("current")
_IgmpSnoopParaData_Type = OctetString
_IgmpSnoopParaData_Object = MibTableColumn
igmpSnoopParaData = _IgmpSnoopParaData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8, 1, 1, 1),
    _IgmpSnoopParaData_Type()
)
igmpSnoopParaData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopParaData.setStatus("current")
_IgmpSnoopGroupTable_Object = MibTable
igmpSnoopGroupTable = _IgmpSnoopGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8, 2)
)
if mibBuilder.loadTexts:
    igmpSnoopGroupTable.setStatus("current")
_IgmpSnoopGroupEntry_Object = MibTableRow
igmpSnoopGroupEntry = _IgmpSnoopGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8, 2, 1)
)
igmpSnoopGroupEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
)
if mibBuilder.loadTexts:
    igmpSnoopGroupEntry.setStatus("current")
_IgmpSnoopGroupData_Type = OctetString
_IgmpSnoopGroupData_Object = MibTableColumn
igmpSnoopGroupData = _IgmpSnoopGroupData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 8, 2, 1, 1),
    _IgmpSnoopGroupData_Type()
)
igmpSnoopGroupData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopGroupData.setStatus("current")
_OnuLoopTestTable_Object = MibTable
onuLoopTestTable = _OnuLoopTestTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 9)
)
if mibBuilder.loadTexts:
    onuLoopTestTable.setStatus("current")
_OnuLoopTestEntry_Object = MibTableRow
onuLoopTestEntry = _OnuLoopTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 9, 1)
)
onuLoopTestEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuLoopTestEntry.setStatus("current")
_OnuLoopTestData_Type = OctetString
_OnuLoopTestData_Object = MibTableColumn
onuLoopTestData = _OnuLoopTestData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 9, 1, 1),
    _OnuLoopTestData_Type()
)
onuLoopTestData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuLoopTestData.setStatus("current")
_OnuLoopTestResult_Type = OctetString
_OnuLoopTestResult_Object = MibTableColumn
onuLoopTestResult = _OnuLoopTestResult_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 9, 1, 2),
    _OnuLoopTestResult_Type()
)
onuLoopTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLoopTestResult.setStatus("current")
_OnuDynMac_ObjectIdentity = ObjectIdentity
onuDynMac = _OnuDynMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10)
)
_OnuDynMacOperTable_Object = MibTable
onuDynMacOperTable = _OnuDynMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 1)
)
if mibBuilder.loadTexts:
    onuDynMacOperTable.setStatus("current")
_OnuDynMacOperEntry_Object = MibTableRow
onuDynMacOperEntry = _OnuDynMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 1, 1)
)
onuDynMacOperEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
)
if mibBuilder.loadTexts:
    onuDynMacOperEntry.setStatus("current")


class _OnuDynMacOperation_Type(Integer32):
    """Custom type onuDynMacOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("refresh", 2))
    )


_OnuDynMacOperation_Type.__name__ = "Integer32"
_OnuDynMacOperation_Object = MibTableColumn
onuDynMacOperation = _OnuDynMacOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 1, 1, 1),
    _OnuDynMacOperation_Type()
)
onuDynMacOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuDynMacOperation.setStatus("current")
_OnuDynMacTable_Object = MibTable
onuDynMacTable = _OnuDynMacTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 2)
)
if mibBuilder.loadTexts:
    onuDynMacTable.setStatus("current")
_OnuDynMacEntry_Object = MibTableRow
onuDynMacEntry = _OnuDynMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 2, 1)
)
onuDynMacEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "uniPortId"),
    (0, "FD-ONU-MIB", "onuDynMacIndex"),
)
if mibBuilder.loadTexts:
    onuDynMacEntry.setStatus("current")


class _OnuDynMacIndex_Type(Integer32):
    """Custom type onuDynMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_OnuDynMacIndex_Type.__name__ = "Integer32"
_OnuDynMacIndex_Object = MibTableColumn
onuDynMacIndex = _OnuDynMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 2, 1, 1),
    _OnuDynMacIndex_Type()
)
onuDynMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuDynMacIndex.setStatus("current")
_OnuDynMacAddr_Type = MacAddress
_OnuDynMacAddr_Object = MibTableColumn
onuDynMacAddr = _OnuDynMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 10, 2, 1, 2),
    _OnuDynMacAddr_Type()
)
onuDynMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuDynMacAddr.setStatus("current")
_OnuVoiceService_ObjectIdentity = ObjectIdentity
onuVoiceService = _OnuVoiceService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11)
)
_OnuIADInfoTable_Object = MibTable
onuIADInfoTable = _OnuIADInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1)
)
if mibBuilder.loadTexts:
    onuIADInfoTable.setStatus("current")
_OnuIADInfoEntry_Object = MibTableRow
onuIADInfoEntry = _OnuIADInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1, 1)
)
onuIADInfoEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuIADInfoEntry.setStatus("current")
_OnuIADMac_Type = MacAddress
_OnuIADMac_Object = MibTableColumn
onuIADMac = _OnuIADMac_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1, 1, 1),
    _OnuIADMac_Type()
)
onuIADMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADMac.setStatus("current")


class _OnuIADProtocol_Type(Integer32):
    """Custom type onuIADProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("h248", 0),
          ("sip", 1))
    )


_OnuIADProtocol_Type.__name__ = "Integer32"
_OnuIADProtocol_Object = MibTableColumn
onuIADProtocol = _OnuIADProtocol_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1, 1, 2),
    _OnuIADProtocol_Type()
)
onuIADProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADProtocol.setStatus("current")


class _OnuIADSwVersion_Type(DisplayString):
    """Custom type onuIADSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OnuIADSwVersion_Type.__name__ = "DisplayString"
_OnuIADSwVersion_Object = MibTableColumn
onuIADSwVersion = _OnuIADSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1, 1, 3),
    _OnuIADSwVersion_Type()
)
onuIADSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADSwVersion.setStatus("current")


class _OnuIADSwTime_Type(DisplayString):
    """Custom type onuIADSwTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OnuIADSwTime_Type.__name__ = "DisplayString"
_OnuIADSwTime_Object = MibTableColumn
onuIADSwTime = _OnuIADSwTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1, 1, 4),
    _OnuIADSwTime_Type()
)
onuIADSwTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADSwTime.setStatus("current")
_OnuIADVoipNum_Type = Integer32
_OnuIADVoipNum_Object = MibTableColumn
onuIADVoipNum = _OnuIADVoipNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 1, 1, 5),
    _OnuIADVoipNum_Type()
)
onuIADVoipNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADVoipNum.setStatus("current")
_OnuIADParamCfgTable_Object = MibTable
onuIADParamCfgTable = _OnuIADParamCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2)
)
if mibBuilder.loadTexts:
    onuIADParamCfgTable.setStatus("current")
_OnuIADParamCfgEntry_Object = MibTableRow
onuIADParamCfgEntry = _OnuIADParamCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1)
)
onuIADParamCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuIADParamCfgEntry.setStatus("current")


class _OnuIADMode_Type(Integer32):
    """Custom type onuIADMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("pppoe", 2),
          ("static", 0))
    )


_OnuIADMode_Type.__name__ = "Integer32"
_OnuIADMode_Object = MibTableColumn
onuIADMode = _OnuIADMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 1),
    _OnuIADMode_Type()
)
onuIADMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADMode.setStatus("current")
_OnuIADIpAddr_Type = IpAddress
_OnuIADIpAddr_Object = MibTableColumn
onuIADIpAddr = _OnuIADIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 2),
    _OnuIADIpAddr_Type()
)
onuIADIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADIpAddr.setStatus("current")
_OnuIADNetMask_Type = IpAddress
_OnuIADNetMask_Object = MibTableColumn
onuIADNetMask = _OnuIADNetMask_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 3),
    _OnuIADNetMask_Type()
)
onuIADNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADNetMask.setStatus("current")
_OnuIADDefaultGw_Type = IpAddress
_OnuIADDefaultGw_Object = MibTableColumn
onuIADDefaultGw = _OnuIADDefaultGw_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 4),
    _OnuIADDefaultGw_Type()
)
onuIADDefaultGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADDefaultGw.setStatus("current")


class _OnuIADPppoeMode_Type(Integer32):
    """Custom type onuIADPppoeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("chap", 1),
          ("pap", 2))
    )


_OnuIADPppoeMode_Type.__name__ = "Integer32"
_OnuIADPppoeMode_Object = MibTableColumn
onuIADPppoeMode = _OnuIADPppoeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 5),
    _OnuIADPppoeMode_Type()
)
onuIADPppoeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADPppoeMode.setStatus("current")


class _OnuIADPppoeUsrnm_Type(DisplayString):
    """Custom type onuIADPppoeUsrnm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OnuIADPppoeUsrnm_Type.__name__ = "DisplayString"
_OnuIADPppoeUsrnm_Object = MibTableColumn
onuIADPppoeUsrnm = _OnuIADPppoeUsrnm_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 6),
    _OnuIADPppoeUsrnm_Type()
)
onuIADPppoeUsrnm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADPppoeUsrnm.setStatus("current")


class _OnuIADPppoePw_Type(DisplayString):
    """Custom type onuIADPppoePw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OnuIADPppoePw_Type.__name__ = "DisplayString"
_OnuIADPppoePw_Object = MibTableColumn
onuIADPppoePw = _OnuIADPppoePw_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 7),
    _OnuIADPppoePw_Type()
)
onuIADPppoePw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADPppoePw.setStatus("current")


class _OnuIADTagMode_Type(Integer32):
    """Custom type onuIADTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passThrough", 0),
          ("tag", 1),
          ("vlanStack", 2))
    )


_OnuIADTagMode_Type.__name__ = "Integer32"
_OnuIADTagMode_Object = MibTableColumn
onuIADTagMode = _OnuIADTagMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 8),
    _OnuIADTagMode_Type()
)
onuIADTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADTagMode.setStatus("current")


class _OnuIADVoiceCVlan_Type(Integer32):
    """Custom type onuIADVoiceCVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_OnuIADVoiceCVlan_Type.__name__ = "Integer32"
_OnuIADVoiceCVlan_Object = MibTableColumn
onuIADVoiceCVlan = _OnuIADVoiceCVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 9),
    _OnuIADVoiceCVlan_Type()
)
onuIADVoiceCVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADVoiceCVlan.setStatus("current")


class _OnuIADVoiceSVlan_Type(Integer32):
    """Custom type onuIADVoiceSVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_OnuIADVoiceSVlan_Type.__name__ = "Integer32"
_OnuIADVoiceSVlan_Object = MibTableColumn
onuIADVoiceSVlan = _OnuIADVoiceSVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 10),
    _OnuIADVoiceSVlan_Type()
)
onuIADVoiceSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADVoiceSVlan.setStatus("current")


class _OnuIADVoicePriority_Type(Integer32):
    """Custom type onuIADVoicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OnuIADVoicePriority_Type.__name__ = "Integer32"
_OnuIADVoicePriority_Object = MibTableColumn
onuIADVoicePriority = _OnuIADVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 2, 1, 11),
    _OnuIADVoicePriority_Type()
)
onuIADVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADVoicePriority.setStatus("current")
_OnuIADH248Param_ObjectIdentity = ObjectIdentity
onuIADH248Param = _OnuIADH248Param_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3)
)
_H248ParamCfgTable_Object = MibTable
h248ParamCfgTable = _H248ParamCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1)
)
if mibBuilder.loadTexts:
    h248ParamCfgTable.setStatus("current")
_H248ParamCfgEntry_Object = MibTableRow
h248ParamCfgEntry = _H248ParamCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1)
)
h248ParamCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    h248ParamCfgEntry.setStatus("current")


class _H248MgPort_Type(Integer32):
    """Custom type h248MgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H248MgPort_Type.__name__ = "Integer32"
_H248MgPort_Object = MibTableColumn
h248MgPort = _H248MgPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 1),
    _H248MgPort_Type()
)
h248MgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgPort.setStatus("current")
_H248MgcIp_Type = IpAddress
_H248MgcIp_Object = MibTableColumn
h248MgcIp = _H248MgcIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 2),
    _H248MgcIp_Type()
)
h248MgcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgcIp.setStatus("current")


class _H248MgcPort_Type(Integer32):
    """Custom type h248MgcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H248MgcPort_Type.__name__ = "Integer32"
_H248MgcPort_Object = MibTableColumn
h248MgcPort = _H248MgcPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 3),
    _H248MgcPort_Type()
)
h248MgcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MgcPort.setStatus("current")
_H248BakMacIp_Type = IpAddress
_H248BakMacIp_Object = MibTableColumn
h248BakMacIp = _H248BakMacIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 4),
    _H248BakMacIp_Type()
)
h248BakMacIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248BakMacIp.setStatus("current")


class _H248BakMgcPort_Type(Integer32):
    """Custom type h248BakMgcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H248BakMgcPort_Type.__name__ = "Integer32"
_H248BakMgcPort_Object = MibTableColumn
h248BakMgcPort = _H248BakMgcPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 5),
    _H248BakMgcPort_Type()
)
h248BakMgcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248BakMgcPort.setStatus("current")


class _H248ActiveMgc_Type(Integer32):
    """Custom type h248ActiveMgc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 0))
    )


_H248ActiveMgc_Type.__name__ = "Integer32"
_H248ActiveMgc_Object = MibTableColumn
h248ActiveMgc = _H248ActiveMgc_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 6),
    _H248ActiveMgc_Type()
)
h248ActiveMgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248ActiveMgc.setStatus("current")


class _H248RegMode_Type(Integer32):
    """Custom type h248RegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deviceName", 2),
          ("domainName", 1),
          ("ipAddress", 0))
    )


_H248RegMode_Type.__name__ = "Integer32"
_H248RegMode_Object = MibTableColumn
h248RegMode = _H248RegMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 7),
    _H248RegMode_Type()
)
h248RegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RegMode.setStatus("current")


class _H248MID_Type(DisplayString):
    """Custom type h248MID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H248MID_Type.__name__ = "DisplayString"
_H248MID_Object = MibTableColumn
h248MID = _H248MID_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 8),
    _H248MID_Type()
)
h248MID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248MID.setStatus("current")


class _H248HbMode_Type(Integer32):
    """Custom type h248HbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("h248ctc", 1))
    )


_H248HbMode_Type.__name__ = "Integer32"
_H248HbMode_Object = MibTableColumn
h248HbMode = _H248HbMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 9),
    _H248HbMode_Type()
)
h248HbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248HbMode.setStatus("current")


class _H248HbCycle_Type(Integer32):
    """Custom type h248HbCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H248HbCycle_Type.__name__ = "Integer32"
_H248HbCycle_Object = MibTableColumn
h248HbCycle = _H248HbCycle_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 10),
    _H248HbCycle_Type()
)
h248HbCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248HbCycle.setStatus("current")


class _H248HbCount_Type(Integer32):
    """Custom type h248HbCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H248HbCount_Type.__name__ = "Integer32"
_H248HbCount_Object = MibTableColumn
h248HbCount = _H248HbCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 1, 1, 11),
    _H248HbCount_Type()
)
h248HbCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248HbCount.setStatus("current")
_H248UserTIDTable_Object = MibTable
h248UserTIDTable = _H248UserTIDTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 2)
)
if mibBuilder.loadTexts:
    h248UserTIDTable.setStatus("current")
_H248UserTIDEntry_Object = MibTableRow
h248UserTIDEntry = _H248UserTIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 2, 1)
)
h248UserTIDEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "onuIADPotsId"),
)
if mibBuilder.loadTexts:
    h248UserTIDEntry.setStatus("current")


class _OnuVoipPortId_Type(Integer32):
    """Custom type onuVoipPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_OnuVoipPortId_Type.__name__ = "Integer32"
_OnuVoipPortId_Object = MibTableColumn
onuVoipPortId = _OnuVoipPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 2, 1, 1),
    _OnuVoipPortId_Type()
)
onuVoipPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuVoipPortId.setStatus("current")


class _H248UserTIDName_Type(DisplayString):
    """Custom type h248UserTIDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H248UserTIDName_Type.__name__ = "DisplayString"
_H248UserTIDName_Object = MibTableColumn
h248UserTIDName = _H248UserTIDName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 2, 1, 2),
    _H248UserTIDName_Type()
)
h248UserTIDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248UserTIDName.setStatus("current")
_H248RtpTIDCfgTable_Object = MibTable
h248RtpTIDCfgTable = _H248RtpTIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3)
)
if mibBuilder.loadTexts:
    h248RtpTIDCfgTable.setStatus("current")
_H248RtpTIDCfgEntry_Object = MibTableRow
h248RtpTIDCfgEntry = _H248RtpTIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3, 1)
)
h248RtpTIDCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    h248RtpTIDCfgEntry.setStatus("current")


class _H248RtpTIDNum_Type(Integer32):
    """Custom type h248RtpTIDNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H248RtpTIDNum_Type.__name__ = "Integer32"
_H248RtpTIDNum_Object = MibTableColumn
h248RtpTIDNum = _H248RtpTIDNum_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3, 1, 1),
    _H248RtpTIDNum_Type()
)
h248RtpTIDNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTIDNum.setStatus("current")


class _H248RtpTIDPrefix_Type(DisplayString):
    """Custom type h248RtpTIDPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_H248RtpTIDPrefix_Type.__name__ = "DisplayString"
_H248RtpTIDPrefix_Object = MibTableColumn
h248RtpTIDPrefix = _H248RtpTIDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3, 1, 2),
    _H248RtpTIDPrefix_Type()
)
h248RtpTIDPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTIDPrefix.setStatus("current")
_H248RtpTIDDigitBegin_Type = Integer32
_H248RtpTIDDigitBegin_Object = MibTableColumn
h248RtpTIDDigitBegin = _H248RtpTIDDigitBegin_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3, 1, 3),
    _H248RtpTIDDigitBegin_Type()
)
h248RtpTIDDigitBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTIDDigitBegin.setStatus("current")


class _H248RtpTIDMode_Type(Integer32):
    """Custom type h248RtpTIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("align", 0),
          ("nonAlign", 1))
    )


_H248RtpTIDMode_Type.__name__ = "Integer32"
_H248RtpTIDMode_Object = MibTableColumn
h248RtpTIDMode = _H248RtpTIDMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3, 1, 4),
    _H248RtpTIDMode_Type()
)
h248RtpTIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTIDMode.setStatus("current")


class _H248RtpTIDDigitLen_Type(Integer32):
    """Custom type h248RtpTIDDigitLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H248RtpTIDDigitLen_Type.__name__ = "Integer32"
_H248RtpTIDDigitLen_Object = MibTableColumn
h248RtpTIDDigitLen = _H248RtpTIDDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 3, 1, 5),
    _H248RtpTIDDigitLen_Type()
)
h248RtpTIDDigitLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h248RtpTIDDigitLen.setStatus("current")
_H248RtpTIDInfoTable_Object = MibTable
h248RtpTIDInfoTable = _H248RtpTIDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 4)
)
if mibBuilder.loadTexts:
    h248RtpTIDInfoTable.setStatus("current")
_H248RtpTIDInfoEntry_Object = MibTableRow
h248RtpTIDInfoEntry = _H248RtpTIDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 4, 1)
)
h248RtpTIDInfoEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    h248RtpTIDInfoEntry.setStatus("current")


class _H248RtpTIDCount_Type(Integer32):
    """Custom type h248RtpTIDCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H248RtpTIDCount_Type.__name__ = "Integer32"
_H248RtpTIDCount_Object = MibTableColumn
h248RtpTIDCount = _H248RtpTIDCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 4, 1, 1),
    _H248RtpTIDCount_Type()
)
h248RtpTIDCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h248RtpTIDCount.setStatus("current")


class _H248FstRtpTIDName_Type(DisplayString):
    """Custom type h248FstRtpTIDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H248FstRtpTIDName_Type.__name__ = "DisplayString"
_H248FstRtpTIDName_Object = MibTableColumn
h248FstRtpTIDName = _H248FstRtpTIDName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 3, 4, 1, 2),
    _H248FstRtpTIDName_Type()
)
h248FstRtpTIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h248FstRtpTIDName.setStatus("current")
_OnuIADSipParam_ObjectIdentity = ObjectIdentity
onuIADSipParam = _OnuIADSipParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4)
)
_SipParamCfgTable_Object = MibTable
sipParamCfgTable = _SipParamCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1)
)
if mibBuilder.loadTexts:
    sipParamCfgTable.setStatus("current")
_SipParamCfgEntry_Object = MibTableRow
sipParamCfgEntry = _SipParamCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1)
)
sipParamCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    sipParamCfgEntry.setStatus("current")


class _SipMgPort_Type(Integer32):
    """Custom type sipMgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipMgPort_Type.__name__ = "Integer32"
_SipMgPort_Object = MibTableColumn
sipMgPort = _SipMgPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 1),
    _SipMgPort_Type()
)
sipMgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMgPort.setStatus("current")
_SipProxySvrIp_Type = IpAddress
_SipProxySvrIp_Object = MibTableColumn
sipProxySvrIp = _SipProxySvrIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 2),
    _SipProxySvrIp_Type()
)
sipProxySvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxySvrIp.setStatus("current")


class _SipProxySvrPort_Type(Integer32):
    """Custom type sipProxySvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipProxySvrPort_Type.__name__ = "Integer32"
_SipProxySvrPort_Object = MibTableColumn
sipProxySvrPort = _SipProxySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 3),
    _SipProxySvrPort_Type()
)
sipProxySvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxySvrPort.setStatus("current")
_SipBakProxySvrIp_Type = IpAddress
_SipBakProxySvrIp_Object = MibTableColumn
sipBakProxySvrIp = _SipBakProxySvrIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 4),
    _SipBakProxySvrIp_Type()
)
sipBakProxySvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipBakProxySvrIp.setStatus("current")


class _SipBakProxySvrPort_Type(Integer32):
    """Custom type sipBakProxySvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipBakProxySvrPort_Type.__name__ = "Integer32"
_SipBakProxySvrPort_Object = MibTableColumn
sipBakProxySvrPort = _SipBakProxySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 5),
    _SipBakProxySvrPort_Type()
)
sipBakProxySvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipBakProxySvrPort.setStatus("current")
_SipActiveProxySvr_Type = IpAddress
_SipActiveProxySvr_Object = MibTableColumn
sipActiveProxySvr = _SipActiveProxySvr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 6),
    _SipActiveProxySvr_Type()
)
sipActiveProxySvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipActiveProxySvr.setStatus("current")
_SipRegSvrIp_Type = IpAddress
_SipRegSvrIp_Object = MibTableColumn
sipRegSvrIp = _SipRegSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 7),
    _SipRegSvrIp_Type()
)
sipRegSvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegSvrIp.setStatus("current")
_SipRegSvrPort_Type = Integer32
_SipRegSvrPort_Object = MibTableColumn
sipRegSvrPort = _SipRegSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 8),
    _SipRegSvrPort_Type()
)
sipRegSvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegSvrPort.setStatus("current")
_SipBakRegSvrIp_Type = IpAddress
_SipBakRegSvrIp_Object = MibTableColumn
sipBakRegSvrIp = _SipBakRegSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 9),
    _SipBakRegSvrIp_Type()
)
sipBakRegSvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipBakRegSvrIp.setStatus("current")


class _SipBakRegSvrPort_Type(Integer32):
    """Custom type sipBakRegSvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipBakRegSvrPort_Type.__name__ = "Integer32"
_SipBakRegSvrPort_Object = MibTableColumn
sipBakRegSvrPort = _SipBakRegSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 10),
    _SipBakRegSvrPort_Type()
)
sipBakRegSvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipBakRegSvrPort.setStatus("current")
_SipOutBoundSvrIp_Type = IpAddress
_SipOutBoundSvrIp_Object = MibTableColumn
sipOutBoundSvrIp = _SipOutBoundSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 11),
    _SipOutBoundSvrIp_Type()
)
sipOutBoundSvrIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOutBoundSvrIp.setStatus("current")


class _SipOutBoundSvrPort_Type(Integer32):
    """Custom type sipOutBoundSvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipOutBoundSvrPort_Type.__name__ = "Integer32"
_SipOutBoundSvrPort_Object = MibTableColumn
sipOutBoundSvrPort = _SipOutBoundSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 12),
    _SipOutBoundSvrPort_Type()
)
sipOutBoundSvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOutBoundSvrPort.setStatus("current")
_SipRegInterval_Type = Integer32
_SipRegInterval_Object = MibTableColumn
sipRegInterval = _SipRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 13),
    _SipRegInterval_Type()
)
sipRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegInterval.setStatus("current")


class _SipHbSwitch_Type(Integer32):
    """Custom type sipHbSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_SipHbSwitch_Type.__name__ = "Integer32"
_SipHbSwitch_Object = MibTableColumn
sipHbSwitch = _SipHbSwitch_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 14),
    _SipHbSwitch_Type()
)
sipHbSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHbSwitch.setStatus("current")


class _SipHbCycle_Type(Integer32):
    """Custom type sipHbCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipHbCycle_Type.__name__ = "Integer32"
_SipHbCycle_Object = MibTableColumn
sipHbCycle = _SipHbCycle_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 15),
    _SipHbCycle_Type()
)
sipHbCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHbCycle.setStatus("current")


class _SipHbCount_Type(Integer32):
    """Custom type sipHbCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipHbCount_Type.__name__ = "Integer32"
_SipHbCount_Object = MibTableColumn
sipHbCount = _SipHbCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 1, 1, 16),
    _SipHbCount_Type()
)
sipHbCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHbCount.setStatus("current")
_SipUserCfgTable_Object = MibTable
sipUserCfgTable = _SipUserCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 2)
)
if mibBuilder.loadTexts:
    sipUserCfgTable.setStatus("current")
_SipUserCfgEntry_Object = MibTableRow
sipUserCfgEntry = _SipUserCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 2, 1)
)
sipUserCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "onuIADPotsId"),
)
if mibBuilder.loadTexts:
    sipUserCfgEntry.setStatus("current")


class _SipUserAccount_Type(DisplayString):
    """Custom type sipUserAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SipUserAccount_Type.__name__ = "DisplayString"
_SipUserAccount_Object = MibTableColumn
sipUserAccount = _SipUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 2, 1, 1),
    _SipUserAccount_Type()
)
sipUserAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUserAccount.setStatus("current")


class _SipUserName_Type(DisplayString):
    """Custom type sipUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SipUserName_Type.__name__ = "DisplayString"
_SipUserName_Object = MibTableColumn
sipUserName = _SipUserName_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 2, 1, 2),
    _SipUserName_Type()
)
sipUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUserName.setStatus("current")


class _SipUserPasswd_Type(DisplayString):
    """Custom type sipUserPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SipUserPasswd_Type.__name__ = "DisplayString"
_SipUserPasswd_Object = MibTableColumn
sipUserPasswd = _SipUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 2, 1, 3),
    _SipUserPasswd_Type()
)
sipUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUserPasswd.setStatus("current")
_SipDigitMapTable_Object = MibTable
sipDigitMapTable = _SipDigitMapTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 3)
)
if mibBuilder.loadTexts:
    sipDigitMapTable.setStatus("current")
_SipDigitMapEntry_Object = MibTableRow
sipDigitMapEntry = _SipDigitMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 3, 1)
)
sipDigitMapEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    sipDigitMapEntry.setStatus("current")


class _SipDigitMapLen_Type(Integer32):
    """Custom type sipDigitMapLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SipDigitMapLen_Type.__name__ = "Integer32"
_SipDigitMapLen_Object = MibTableColumn
sipDigitMapLen = _SipDigitMapLen_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 3, 1, 1),
    _SipDigitMapLen_Type()
)
sipDigitMapLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDigitMapLen.setStatus("current")
_SipDigitMap_Type = DisplayString
_SipDigitMap_Object = MibTableColumn
sipDigitMap = _SipDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 4, 3, 1, 2),
    _SipDigitMap_Type()
)
sipDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDigitMap.setStatus("current")
_OnuIADFaxCfgTable_Object = MibTable
onuIADFaxCfgTable = _OnuIADFaxCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 5)
)
if mibBuilder.loadTexts:
    onuIADFaxCfgTable.setStatus("current")
_OnuIADFaxCfgEntry_Object = MibTableRow
onuIADFaxCfgEntry = _OnuIADFaxCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 5, 1)
)
onuIADFaxCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuIADFaxCfgEntry.setStatus("current")


class _OnuIADVoiceFaxMode_Type(Integer32):
    """Custom type onuIADVoiceFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 0),
          ("t38", 1))
    )


_OnuIADVoiceFaxMode_Type.__name__ = "Integer32"
_OnuIADVoiceFaxMode_Object = MibTableColumn
onuIADVoiceFaxMode = _OnuIADVoiceFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 5, 1, 1),
    _OnuIADVoiceFaxMode_Type()
)
onuIADVoiceFaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADVoiceFaxMode.setStatus("current")


class _OnuIADVoiceFaxControl_Type(Integer32):
    """Custom type onuIADVoiceFaxControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("autoVBD", 1),
          ("negotiation", 0))
    )


_OnuIADVoiceFaxControl_Type.__name__ = "Integer32"
_OnuIADVoiceFaxControl_Object = MibTableColumn
onuIADVoiceFaxControl = _OnuIADVoiceFaxControl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 5, 1, 2),
    _OnuIADVoiceFaxControl_Type()
)
onuIADVoiceFaxControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADVoiceFaxControl.setStatus("current")
_OnuIADOperTable_Object = MibTable
onuIADOperTable = _OnuIADOperTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 6)
)
if mibBuilder.loadTexts:
    onuIADOperTable.setStatus("current")
_OnuIADOperEntry_Object = MibTableRow
onuIADOperEntry = _OnuIADOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 6, 1)
)
onuIADOperEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
)
if mibBuilder.loadTexts:
    onuIADOperEntry.setStatus("current")


class _OnuIADOperStatusSet_Type(Integer32):
    """Custom type onuIADOperStatusSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logout", 1),
          ("reregister", 0),
          ("reset", 2))
    )


_OnuIADOperStatusSet_Type.__name__ = "Integer32"
_OnuIADOperStatusSet_Object = MibTableColumn
onuIADOperStatusSet = _OnuIADOperStatusSet_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 6, 1, 1),
    _OnuIADOperStatusSet_Type()
)
onuIADOperStatusSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADOperStatusSet.setStatus("current")


class _OnuIADOperStatus_Type(Integer32):
    """Custom type onuIADOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("iadFault", 2),
          ("iadRestarting", 4),
          ("logout", 3),
          ("regSuccess", 1),
          ("registering", 0))
    )


_OnuIADOperStatus_Type.__name__ = "Integer32"
_OnuIADOperStatus_Object = MibTableColumn
onuIADOperStatus = _OnuIADOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 6, 1, 2),
    _OnuIADOperStatus_Type()
)
onuIADOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADOperStatus.setStatus("current")
_OnuIADPOTSStatusTable_Object = MibTable
onuIADPOTSStatusTable = _OnuIADPOTSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 7)
)
if mibBuilder.loadTexts:
    onuIADPOTSStatusTable.setStatus("current")
_OnuIADPOTSStatusEntry_Object = MibTableRow
onuIADPOTSStatusEntry = _OnuIADPOTSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 7, 1)
)
onuIADPOTSStatusEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "onuIADPotsId"),
)
if mibBuilder.loadTexts:
    onuIADPOTSStatusEntry.setStatus("current")


class _OnuIADPotsStatus_Type(Integer32):
    """Custom type onuIADPotsStatus based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("connected", 7),
          ("connecting", 6),
          ("dialing", 3),
          ("idle", 1),
          ("notActivated", 10),
          ("pickUp", 2),
          ("regFailure", 9),
          ("registering", 0),
          ("releasing", 8),
          ("ringBack", 5),
          ("ringing", 4))
    )


_OnuIADPotsStatus_Type.__name__ = "Integer32"
_OnuIADPotsStatus_Object = MibTableColumn
onuIADPotsStatus = _OnuIADPotsStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 7, 1, 1),
    _OnuIADPotsStatus_Type()
)
onuIADPotsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADPotsStatus.setStatus("current")


class _OnuIADPotsServiceState_Type(Integer32):
    """Custom type onuIADPotsServiceState based on Integer32"""
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
        *(("endAuto", 2),
          ("endLocal", 0),
          ("endRemote", 1),
          ("normal", 3))
    )


_OnuIADPotsServiceState_Type.__name__ = "Integer32"
_OnuIADPotsServiceState_Object = MibTableColumn
onuIADPotsServiceState = _OnuIADPotsServiceState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 7, 1, 2),
    _OnuIADPotsServiceState_Type()
)
onuIADPotsServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADPotsServiceState.setStatus("current")


class _OnuIADPotsCodeMode_Type(Integer32):
    """Custom type onuIADPotsCodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 0),
          ("g711u", 2),
          ("g723", 3),
          ("g726", 4),
          ("g729", 1),
          ("t38", 5))
    )


_OnuIADPotsCodeMode_Type.__name__ = "Integer32"
_OnuIADPotsCodeMode_Object = MibTableColumn
onuIADPotsCodeMode = _OnuIADPotsCodeMode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 7, 1, 3),
    _OnuIADPotsCodeMode_Type()
)
onuIADPotsCodeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIADPotsCodeMode.setStatus("current")


class _OnuIADPotsId_Type(Integer32):
    """Custom type onuIADPotsId based on Integer32"""
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
        *(("iadPots1", 1),
          ("iadPots2", 2),
          ("iadPots3", 3),
          ("iadPots4", 4),
          ("iadPots5", 5),
          ("iadPots6", 6),
          ("iadPots7", 7),
          ("iadPots8", 8))
    )


_OnuIADPotsId_Type.__name__ = "Integer32"
_OnuIADPotsId_Object = MibTableColumn
onuIADPotsId = _OnuIADPotsId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 7, 1, 4),
    _OnuIADPotsId_Type()
)
onuIADPotsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuIADPotsId.setStatus("current")
_OnuIADPOTSEnableTable_Object = MibTable
onuIADPOTSEnableTable = _OnuIADPOTSEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 8)
)
if mibBuilder.loadTexts:
    onuIADPOTSEnableTable.setStatus("current")
_OnuIADPOTSEnableEntry_Object = MibTableRow
onuIADPOTSEnableEntry = _OnuIADPOTSEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 8, 1)
)
onuIADPOTSEnableEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-ONU-MIB", "onuId"),
    (0, "FD-ONU-MIB", "onuIADPotsId"),
)
if mibBuilder.loadTexts:
    onuIADPOTSEnableEntry.setStatus("current")


class _PotsId_Type(Integer32):
    """Custom type potsId based on Integer32"""
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
        *(("iadPots1", 1),
          ("iadPots2", 2),
          ("iadPots3", 3),
          ("iadPots4", 4),
          ("iadPots5", 5),
          ("iadPots6", 6),
          ("iadPots7", 7),
          ("iadPots8", 8))
    )


_PotsId_Type.__name__ = "Integer32"
_PotsId_Object = MibTableColumn
potsId = _PotsId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 8, 1, 1),
    _PotsId_Type()
)
potsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsId.setStatus("current")


class _OnuIADPotsEnable_Type(Integer32):
    """Custom type onuIADPotsEnable based on Integer32"""
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


_OnuIADPotsEnable_Type.__name__ = "Integer32"
_OnuIADPotsEnable_Object = MibTableColumn
onuIADPotsEnable = _OnuIADPotsEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 11, 8, 1, 2),
    _OnuIADPotsEnable_Type()
)
onuIADPotsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIADPotsEnable.setStatus("current")
_FdOnuConformance_ObjectIdentity = ObjectIdentity
fdOnuConformance = _FdOnuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15)
)
_FdOnuGroups_ObjectIdentity = ObjectIdentity
fdOnuGroups = _FdOnuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1)
)
_FdOnuCompliances_ObjectIdentity = ObjectIdentity
fdOnuCompliances = _FdOnuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 2)
)

# Managed Objects groups

fdOnuBaseManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1, 1)
)
fdOnuBaseManageGroup.setObjects(
      *(("FD-ONU-MIB", "onuDeviceType"),
        ("FD-ONU-MIB", "onuFactorySerial"),
        ("FD-ONU-MIB", "onuUserInfo"),
        ("FD-ONU-MIB", "onuHwRev"),
        ("FD-ONU-MIB", "onuFwRev"),
        ("FD-ONU-MIB", "onuBaseMac"),
        ("FD-ONU-MIB", "maxAllowedLLIDs"),
        ("FD-ONU-MIB", "registeredLLIDNum"),
        ("FD-ONU-MIB", "onuOnLineStatus"),
        ("FD-ONU-MIB", "onuUserTrafficEnable"),
        ("FD-ONU-MIB", "onuRangeValue"),
        ("FD-ONU-MIB", "onuMgmtType"),
        ("FD-ONU-MIB", "onuLaserRxPower"),
        ("FD-ONU-MIB", "onuLaserTxPower"),
        ("FD-ONU-MIB", "onuOperation"),
        ("FD-ONU-MIB", "onuRstpEnable"),
        ("FD-ONU-MIB", "onuQueueCfgData"),
        ("FD-ONU-MIB", "onuAclRuleCfgData"),
        ("FD-ONU-MIB", "onuPortVlanData"),
        ("FD-ONU-MIB", "maxTrafficOutputRate"),
        ("FD-ONU-MIB", "outputModule"),
        ("FD-ONU-MIB", "scheduleAlgorithm"),
        ("FD-ONU-MIB", "policingTrafficType"),
        ("FD-ONU-MIB", "maxTrafficInputRate"),
        ("FD-ONU-MIB", "inputModule"),
        ("FD-ONU-MIB", "onuDynMacOperation"),
        ("FD-ONU-MIB", "supportUniPorts"),
        ("FD-ONU-MIB", "onuLinkIdMap"),
        ("FD-ONU-MIB", "onuDynMacAddr"),
        ("FD-ONU-MIB", "onuUpgradeStat"))
)
if mibBuilder.loadTexts:
    fdOnuBaseManageGroup.setStatus("current")

fdOnuAdvanceManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1, 2)
)
fdOnuAdvanceManageGroup.setObjects(
      *(("FD-ONU-MIB", "onuChipProCode"),
        ("FD-ONU-MIB", "onuChipProVer"),
        ("FD-ONU-MIB", "onuChipId"),
        ("FD-ONU-MIB", "onuChipVer"),
        ("FD-ONU-MIB", "onuBootVer"),
        ("FD-ONU-MIB", "onuPersVer"),
        ("FD-ONU-MIB", "onuChipApp0Ver"),
        ("FD-ONU-MIB", "onuChipApp1Ver"),
        ("FD-ONU-MIB", "onuChipDiagVer"),
        ("FD-ONU-MIB", "onuAddiVlanEthType"),
        ("FD-ONU-MIB", "onuRstpEnable"),
        ("FD-ONU-MIB", "onuLocalSwitch"),
        ("FD-ONU-MIB", "onuCatv"))
)
if mibBuilder.loadTexts:
    fdOnuAdvanceManageGroup.setStatus("current")

fdOnuPortParaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1, 3)
)
fdOnuPortParaGroup.setObjects(
      *(("FD-ONU-MIB", "uniPortUserInfo"),
        ("FD-ONU-MIB", "uniPortLink"),
        ("FD-ONU-MIB", "uniPortAutoNego"),
        ("FD-ONU-MIB", "uniPortSpeed"),
        ("FD-ONU-MIB", "uniPortDuplex"),
        ("FD-ONU-MIB", "uniPortFlowCtrl"),
        ("FD-ONU-MIB", "uniPortMacEntryLimit"),
        ("FD-ONU-MIB", "uniPortMacAgeTime"),
        ("FD-ONU-MIB", "uniPortFowardMode"),
        ("FD-ONU-MIB", "uniPortEnable"),
        ("FD-ONU-MIB", "uniPortRstpState"))
)
if mibBuilder.loadTexts:
    fdOnuPortParaGroup.setStatus("current")

onuIgmpSnoopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1, 4)
)
onuIgmpSnoopGroup.setObjects(
      *(("FD-ONU-MIB", "igmpSnoopParaData"),
        ("FD-ONU-MIB", "igmpSnoopGroupData"))
)
if mibBuilder.loadTexts:
    onuIgmpSnoopGroup.setStatus("current")

fdOnuLpTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1, 5)
)
fdOnuLpTestGroup.setObjects(
      *(("FD-ONU-MIB", "onuLoopTestData"),
        ("FD-ONU-MIB", "onuLoopTestResult"))
)
if mibBuilder.loadTexts:
    fdOnuLpTestGroup.setStatus("current")

fdOnuVoiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 1, 6)
)
fdOnuVoiceGroup.setObjects(
      *(("FD-ONU-MIB", "onuIADMac"),
        ("FD-ONU-MIB", "onuIADProtocol"),
        ("FD-ONU-MIB", "onuIADSwVersion"),
        ("FD-ONU-MIB", "onuIADSwTime"),
        ("FD-ONU-MIB", "onuIADVoipNum"),
        ("FD-ONU-MIB", "onuIADMode"),
        ("FD-ONU-MIB", "onuIADIpAddr"),
        ("FD-ONU-MIB", "onuIADNetMask"),
        ("FD-ONU-MIB", "onuIADDefaultGw"),
        ("FD-ONU-MIB", "onuIADPppoeMode"),
        ("FD-ONU-MIB", "onuIADPppoeUsrnm"),
        ("FD-ONU-MIB", "onuIADPppoePw"),
        ("FD-ONU-MIB", "onuIADTagMode"),
        ("FD-ONU-MIB", "onuIADVoiceCVlan"),
        ("FD-ONU-MIB", "onuIADVoiceSVlan"),
        ("FD-ONU-MIB", "onuIADVoicePriority"),
        ("FD-ONU-MIB", "h248MgPort"),
        ("FD-ONU-MIB", "h248MgcIp"),
        ("FD-ONU-MIB", "h248MgcPort"),
        ("FD-ONU-MIB", "h248BakMacIp"),
        ("FD-ONU-MIB", "h248BakMgcPort"),
        ("FD-ONU-MIB", "h248ActiveMgc"),
        ("FD-ONU-MIB", "h248RegMode"),
        ("FD-ONU-MIB", "h248MID"),
        ("FD-ONU-MIB", "h248HbMode"),
        ("FD-ONU-MIB", "h248HbCycle"),
        ("FD-ONU-MIB", "h248HbCount"),
        ("FD-ONU-MIB", "onuVoipPortId"),
        ("FD-ONU-MIB", "h248UserTIDName"),
        ("FD-ONU-MIB", "h248RtpTIDNum"),
        ("FD-ONU-MIB", "h248RtpTIDPrefix"),
        ("FD-ONU-MIB", "h248RtpTIDDigitBegin"),
        ("FD-ONU-MIB", "h248RtpTIDMode"),
        ("FD-ONU-MIB", "h248RtpTIDDigitLen"),
        ("FD-ONU-MIB", "h248RtpTIDCount"),
        ("FD-ONU-MIB", "h248FstRtpTIDName"),
        ("FD-ONU-MIB", "sipMgPort"),
        ("FD-ONU-MIB", "sipProxySvrIp"),
        ("FD-ONU-MIB", "sipProxySvrPort"),
        ("FD-ONU-MIB", "sipBakProxySvrIp"),
        ("FD-ONU-MIB", "sipBakProxySvrPort"),
        ("FD-ONU-MIB", "sipActiveProxySvr"),
        ("FD-ONU-MIB", "sipRegSvrIp"),
        ("FD-ONU-MIB", "sipRegSvrPort"),
        ("FD-ONU-MIB", "sipBakRegSvrIp"),
        ("FD-ONU-MIB", "sipBakRegSvrPort"),
        ("FD-ONU-MIB", "sipOutBoundSvrIp"),
        ("FD-ONU-MIB", "sipOutBoundSvrPort"),
        ("FD-ONU-MIB", "sipRegInterval"),
        ("FD-ONU-MIB", "sipHbSwitch"),
        ("FD-ONU-MIB", "sipHbCycle"),
        ("FD-ONU-MIB", "sipHbCount"),
        ("FD-ONU-MIB", "sipUserAccount"),
        ("FD-ONU-MIB", "sipUserName"),
        ("FD-ONU-MIB", "sipUserPasswd"),
        ("FD-ONU-MIB", "sipDigitMapLen"),
        ("FD-ONU-MIB", "sipDigitMap"),
        ("FD-ONU-MIB", "onuIADVoiceFaxMode"),
        ("FD-ONU-MIB", "onuIADVoiceFaxControl"),
        ("FD-ONU-MIB", "onuIADOperStatusSet"),
        ("FD-ONU-MIB", "onuIADOperStatus"),
        ("FD-ONU-MIB", "onuIADPotsStatus"),
        ("FD-ONU-MIB", "onuIADPotsServiceState"),
        ("FD-ONU-MIB", "onuIADPotsCodeMode"),
        ("FD-ONU-MIB", "onuIADPotsEnable"))
)
if mibBuilder.loadTexts:
    fdOnuVoiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fdOnuCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 4, 15, 2, 1)
)
if mibBuilder.loadTexts:
    fdOnuCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FD-ONU-MIB",
    **{"fdOnu": fdOnu,
       "onuBaseManageTable": onuBaseManageTable,
       "onuBaseManageEntry": onuBaseManageEntry,
       "onuId": onuId,
       "onuDeviceType": onuDeviceType,
       "onuFactorySerial": onuFactorySerial,
       "onuUserInfo": onuUserInfo,
       "onuHwRev": onuHwRev,
       "onuFwRev": onuFwRev,
       "onuBaseMac": onuBaseMac,
       "maxAllowedLLIDs": maxAllowedLLIDs,
       "registeredLLIDNum": registeredLLIDNum,
       "onuOnLineStatus": onuOnLineStatus,
       "onuUserTrafficEnable": onuUserTrafficEnable,
       "onuRangeValue": onuRangeValue,
       "supportUniPorts": supportUniPorts,
       "onuOperation": onuOperation,
       "onuUpgradeStat": onuUpgradeStat,
       "onuLinkIdMap": onuLinkIdMap,
       "onuMgmtType": onuMgmtType,
       "onuLaserRxPower": onuLaserRxPower,
       "onuLaserTxPower": onuLaserTxPower,
       "onuAdvancedManage": onuAdvancedManage,
       "onuChipInfoTable": onuChipInfoTable,
       "onuChipInfoEntry": onuChipInfoEntry,
       "onuChipProCode": onuChipProCode,
       "onuChipProVer": onuChipProVer,
       "onuChipId": onuChipId,
       "onuChipVer": onuChipVer,
       "onuBootVer": onuBootVer,
       "onuPersVer": onuPersVer,
       "onuChipApp0Ver": onuChipApp0Ver,
       "onuChipApp1Ver": onuChipApp1Ver,
       "onuChipDiagVer": onuChipDiagVer,
       "onuAdvancedConfigTable": onuAdvancedConfigTable,
       "onuAdvancedConfigEntry": onuAdvancedConfigEntry,
       "onuAddiVlanEthType": onuAddiVlanEthType,
       "onuRstpEnable": onuRstpEnable,
       "onuLocalSwitch": onuLocalSwitch,
       "onuCatv": onuCatv,
       "onuUniPortTable": onuUniPortTable,
       "onuUniPortEntry": onuUniPortEntry,
       "uniPortId": uniPortId,
       "uniPortUserInfo": uniPortUserInfo,
       "uniPortLink": uniPortLink,
       "uniPortAutoNego": uniPortAutoNego,
       "uniPortSpeed": uniPortSpeed,
       "uniPortDuplex": uniPortDuplex,
       "uniPortFlowCtrl": uniPortFlowCtrl,
       "uniPortMacEntryLimit": uniPortMacEntryLimit,
       "uniPortMacAgeTime": uniPortMacAgeTime,
       "uniPortFowardMode": uniPortFowardMode,
       "uniPortEnable": uniPortEnable,
       "uniPortRstpState": uniPortRstpState,
       "onuQueueCfgTable": onuQueueCfgTable,
       "onuQueueCfgEntry": onuQueueCfgEntry,
       "onuQueueCfgData": onuQueueCfgData,
       "onuAclRuleTable": onuAclRuleTable,
       "onuAclRuleEntry": onuAclRuleEntry,
       "onuIntPortId": onuIntPortId,
       "onuAclRuleCfgData": onuAclRuleCfgData,
       "onuPortVlanTable": onuPortVlanTable,
       "onuPortVlanEntry": onuPortVlanEntry,
       "onuPortId": onuPortId,
       "onuPortVlanData": onuPortVlanData,
       "onuPortQos": onuPortQos,
       "portEgressShappingTable": portEgressShappingTable,
       "portEgressShappingEntry": portEgressShappingEntry,
       "scheduleAlgorithm": scheduleAlgorithm,
       "maxTrafficOutputRate": maxTrafficOutputRate,
       "outputModule": outputModule,
       "portIngressPolicingTable": portIngressPolicingTable,
       "portIngressPolicingEntry": portIngressPolicingEntry,
       "policingTrafficType": policingTrafficType,
       "maxTrafficInputRate": maxTrafficInputRate,
       "inputModule": inputModule,
       "igmpSnooping": igmpSnooping,
       "igmpSnoopParaTable": igmpSnoopParaTable,
       "igmpSnoopParaEntry": igmpSnoopParaEntry,
       "igmpSnoopParaData": igmpSnoopParaData,
       "igmpSnoopGroupTable": igmpSnoopGroupTable,
       "igmpSnoopGroupEntry": igmpSnoopGroupEntry,
       "igmpSnoopGroupData": igmpSnoopGroupData,
       "onuLoopTestTable": onuLoopTestTable,
       "onuLoopTestEntry": onuLoopTestEntry,
       "onuLoopTestData": onuLoopTestData,
       "onuLoopTestResult": onuLoopTestResult,
       "onuDynMac": onuDynMac,
       "onuDynMacOperTable": onuDynMacOperTable,
       "onuDynMacOperEntry": onuDynMacOperEntry,
       "onuDynMacOperation": onuDynMacOperation,
       "onuDynMacTable": onuDynMacTable,
       "onuDynMacEntry": onuDynMacEntry,
       "onuDynMacIndex": onuDynMacIndex,
       "onuDynMacAddr": onuDynMacAddr,
       "onuVoiceService": onuVoiceService,
       "onuIADInfoTable": onuIADInfoTable,
       "onuIADInfoEntry": onuIADInfoEntry,
       "onuIADMac": onuIADMac,
       "onuIADProtocol": onuIADProtocol,
       "onuIADSwVersion": onuIADSwVersion,
       "onuIADSwTime": onuIADSwTime,
       "onuIADVoipNum": onuIADVoipNum,
       "onuIADParamCfgTable": onuIADParamCfgTable,
       "onuIADParamCfgEntry": onuIADParamCfgEntry,
       "onuIADMode": onuIADMode,
       "onuIADIpAddr": onuIADIpAddr,
       "onuIADNetMask": onuIADNetMask,
       "onuIADDefaultGw": onuIADDefaultGw,
       "onuIADPppoeMode": onuIADPppoeMode,
       "onuIADPppoeUsrnm": onuIADPppoeUsrnm,
       "onuIADPppoePw": onuIADPppoePw,
       "onuIADTagMode": onuIADTagMode,
       "onuIADVoiceCVlan": onuIADVoiceCVlan,
       "onuIADVoiceSVlan": onuIADVoiceSVlan,
       "onuIADVoicePriority": onuIADVoicePriority,
       "onuIADH248Param": onuIADH248Param,
       "h248ParamCfgTable": h248ParamCfgTable,
       "h248ParamCfgEntry": h248ParamCfgEntry,
       "h248MgPort": h248MgPort,
       "h248MgcIp": h248MgcIp,
       "h248MgcPort": h248MgcPort,
       "h248BakMacIp": h248BakMacIp,
       "h248BakMgcPort": h248BakMgcPort,
       "h248ActiveMgc": h248ActiveMgc,
       "h248RegMode": h248RegMode,
       "h248MID": h248MID,
       "h248HbMode": h248HbMode,
       "h248HbCycle": h248HbCycle,
       "h248HbCount": h248HbCount,
       "h248UserTIDTable": h248UserTIDTable,
       "h248UserTIDEntry": h248UserTIDEntry,
       "onuVoipPortId": onuVoipPortId,
       "h248UserTIDName": h248UserTIDName,
       "h248RtpTIDCfgTable": h248RtpTIDCfgTable,
       "h248RtpTIDCfgEntry": h248RtpTIDCfgEntry,
       "h248RtpTIDNum": h248RtpTIDNum,
       "h248RtpTIDPrefix": h248RtpTIDPrefix,
       "h248RtpTIDDigitBegin": h248RtpTIDDigitBegin,
       "h248RtpTIDMode": h248RtpTIDMode,
       "h248RtpTIDDigitLen": h248RtpTIDDigitLen,
       "h248RtpTIDInfoTable": h248RtpTIDInfoTable,
       "h248RtpTIDInfoEntry": h248RtpTIDInfoEntry,
       "h248RtpTIDCount": h248RtpTIDCount,
       "h248FstRtpTIDName": h248FstRtpTIDName,
       "onuIADSipParam": onuIADSipParam,
       "sipParamCfgTable": sipParamCfgTable,
       "sipParamCfgEntry": sipParamCfgEntry,
       "sipMgPort": sipMgPort,
       "sipProxySvrIp": sipProxySvrIp,
       "sipProxySvrPort": sipProxySvrPort,
       "sipBakProxySvrIp": sipBakProxySvrIp,
       "sipBakProxySvrPort": sipBakProxySvrPort,
       "sipActiveProxySvr": sipActiveProxySvr,
       "sipRegSvrIp": sipRegSvrIp,
       "sipRegSvrPort": sipRegSvrPort,
       "sipBakRegSvrIp": sipBakRegSvrIp,
       "sipBakRegSvrPort": sipBakRegSvrPort,
       "sipOutBoundSvrIp": sipOutBoundSvrIp,
       "sipOutBoundSvrPort": sipOutBoundSvrPort,
       "sipRegInterval": sipRegInterval,
       "sipHbSwitch": sipHbSwitch,
       "sipHbCycle": sipHbCycle,
       "sipHbCount": sipHbCount,
       "sipUserCfgTable": sipUserCfgTable,
       "sipUserCfgEntry": sipUserCfgEntry,
       "sipUserAccount": sipUserAccount,
       "sipUserName": sipUserName,
       "sipUserPasswd": sipUserPasswd,
       "sipDigitMapTable": sipDigitMapTable,
       "sipDigitMapEntry": sipDigitMapEntry,
       "sipDigitMapLen": sipDigitMapLen,
       "sipDigitMap": sipDigitMap,
       "onuIADFaxCfgTable": onuIADFaxCfgTable,
       "onuIADFaxCfgEntry": onuIADFaxCfgEntry,
       "onuIADVoiceFaxMode": onuIADVoiceFaxMode,
       "onuIADVoiceFaxControl": onuIADVoiceFaxControl,
       "onuIADOperTable": onuIADOperTable,
       "onuIADOperEntry": onuIADOperEntry,
       "onuIADOperStatusSet": onuIADOperStatusSet,
       "onuIADOperStatus": onuIADOperStatus,
       "onuIADPOTSStatusTable": onuIADPOTSStatusTable,
       "onuIADPOTSStatusEntry": onuIADPOTSStatusEntry,
       "onuIADPotsStatus": onuIADPotsStatus,
       "onuIADPotsServiceState": onuIADPotsServiceState,
       "onuIADPotsCodeMode": onuIADPotsCodeMode,
       "onuIADPotsId": onuIADPotsId,
       "onuIADPOTSEnableTable": onuIADPOTSEnableTable,
       "onuIADPOTSEnableEntry": onuIADPOTSEnableEntry,
       "potsId": potsId,
       "onuIADPotsEnable": onuIADPotsEnable,
       "fdOnuConformance": fdOnuConformance,
       "fdOnuGroups": fdOnuGroups,
       "fdOnuBaseManageGroup": fdOnuBaseManageGroup,
       "fdOnuAdvanceManageGroup": fdOnuAdvanceManageGroup,
       "fdOnuPortParaGroup": fdOnuPortParaGroup,
       "onuIgmpSnoopGroup": onuIgmpSnoopGroup,
       "fdOnuLpTestGroup": fdOnuLpTestGroup,
       "fdOnuVoiceGroup": fdOnuVoiceGroup,
       "fdOnuCompliances": fdOnuCompliances,
       "fdOnuCompliance": fdOnuCompliance}
)
