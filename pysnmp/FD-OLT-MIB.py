# SNMP MIB module (FD-OLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FD-OLT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:27 2024
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

(DataDirection,
 DeviceOperation,
 DeviceStatus,
 OperSwitch,
 epon) = mibBuilder.importSymbols(
    "EPON-EOC-MIB",
    "DataDirection",
    "DeviceOperation",
    "DeviceStatus",
    "OperSwitch",
    "epon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fdOlt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OltBaseManageTable_Object = MibTable
oltBaseManageTable = _OltBaseManageTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    oltBaseManageTable.setStatus("current")
_OltBaseManageEntry_Object = MibTableRow
oltBaseManageEntry = _OltBaseManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1)
)
oltBaseManageEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    oltBaseManageEntry.setStatus("current")


class _OltId_Type(Integer32):
    """Custom type oltId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_OltId_Type.__name__ = "Integer32"
_OltId_Object = MibTableColumn
oltId = _OltId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 1),
    _OltId_Type()
)
oltId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltId.setStatus("current")
_OltMacAddr_Type = MacAddress
_OltMacAddr_Object = MibTableColumn
oltMacAddr = _OltMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 2),
    _OltMacAddr_Type()
)
oltMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMacAddr.setStatus("current")
_OltWorkState_Type = DeviceStatus
_OltWorkState_Object = MibTableColumn
oltWorkState = _OltWorkState_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 3),
    _OltWorkState_Type()
)
oltWorkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltWorkState.setStatus("current")
_OltEnable_Type = OperSwitch
_OltEnable_Object = MibTableColumn
oltEnable = _OltEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 4),
    _OltEnable_Type()
)
oltEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltEnable.setStatus("current")


class _MaxPermitLLIDNumber_Type(Unsigned32):
    """Custom type maxPermitLLIDNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MaxPermitLLIDNumber_Type.__name__ = "Unsigned32"
_MaxPermitLLIDNumber_Object = MibTableColumn
maxPermitLLIDNumber = _MaxPermitLLIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 5),
    _MaxPermitLLIDNumber_Type()
)
maxPermitLLIDNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxPermitLLIDNumber.setStatus("current")


class _RegisteredLLIDNumber_Type(Unsigned32):
    """Custom type registeredLLIDNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RegisteredLLIDNumber_Type.__name__ = "Unsigned32"
_RegisteredLLIDNumber_Object = MibTableColumn
registeredLLIDNumber = _RegisteredLLIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 6),
    _RegisteredLLIDNumber_Type()
)
registeredLLIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registeredLLIDNumber.setStatus("current")


class _AccessedOnuNumber_Type(Unsigned32):
    """Custom type accessedOnuNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AccessedOnuNumber_Type.__name__ = "Unsigned32"
_AccessedOnuNumber_Object = MibTableColumn
accessedOnuNumber = _AccessedOnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 7),
    _AccessedOnuNumber_Type()
)
accessedOnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessedOnuNumber.setStatus("current")
_LinkIdExhaust_Type = TruthValue
_LinkIdExhaust_Object = MibTableColumn
linkIdExhaust = _LinkIdExhaust_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 8),
    _LinkIdExhaust_Type()
)
linkIdExhaust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIdExhaust.setStatus("current")
_OnuIdExhaust_Type = TruthValue
_OnuIdExhaust_Object = MibTableColumn
onuIdExhaust = _OnuIdExhaust_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 9),
    _OnuIdExhaust_Type()
)
onuIdExhaust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuIdExhaust.setStatus("current")
_LinkIdOverWrite_Type = TruthValue
_LinkIdOverWrite_Object = MibTableColumn
linkIdOverWrite = _LinkIdOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 10),
    _LinkIdOverWrite_Type()
)
linkIdOverWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkIdOverWrite.setStatus("current")
_OnuIdOverWrite_Type = TruthValue
_OnuIdOverWrite_Object = MibTableColumn
onuIdOverWrite = _OnuIdOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 11),
    _OnuIdOverWrite_Type()
)
onuIdOverWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIdOverWrite.setStatus("current")
_OltOperate_Type = DeviceOperation
_OltOperate_Object = MibTableColumn
oltOperate = _OltOperate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 20),
    _OltOperate_Type()
)
oltOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltOperate.setStatus("current")


class _OltUpgradeStat_Type(Integer32):
    """Custom type oltUpgradeStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("booting", 1),
          ("normalRun", 2),
          ("upgradeErr", 8),
          ("upgradeOk", 7),
          ("upgradeOnu", 10),
          ("upgrading", 6))
    )


_OltUpgradeStat_Type.__name__ = "Integer32"
_OltUpgradeStat_Object = MibTableColumn
oltUpgradeStat = _OltUpgradeStat_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 21),
    _OltUpgradeStat_Type()
)
oltUpgradeStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltUpgradeStat.setStatus("current")


class _OnuMgmtDefType_Type(Integer32):
    """Custom type onuMgmtDefType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onuMgmtCtc", 2),
          ("onuMgmtTk", 1))
    )


_OnuMgmtDefType_Type.__name__ = "Integer32"
_OnuMgmtDefType_Object = MibTableColumn
onuMgmtDefType = _OnuMgmtDefType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 1, 1, 22),
    _OnuMgmtDefType_Type()
)
onuMgmtDefType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtDefType.setStatus("current")
_OltAdvancedManage_ObjectIdentity = ObjectIdentity
oltAdvancedManage = _OltAdvancedManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4)
)
_OltChipInfoTable_Object = MibTable
oltChipInfoTable = _OltChipInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    oltChipInfoTable.setStatus("current")
_OltChipInfoEntry_Object = MibTableRow
oltChipInfoEntry = _OltChipInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1)
)
oltChipInfoEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    oltChipInfoEntry.setStatus("current")
_OltChipProCode_Type = Unsigned32
_OltChipProCode_Object = MibTableColumn
oltChipProCode = _OltChipProCode_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 1),
    _OltChipProCode_Type()
)
oltChipProCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipProCode.setStatus("current")
_OltChipVer_Type = Unsigned32
_OltChipVer_Object = MibTableColumn
oltChipVer = _OltChipVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 2),
    _OltChipVer_Type()
)
oltChipVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipVer.setStatus("current")
_OltChipFirmVer_Type = Unsigned32
_OltChipFirmVer_Object = MibTableColumn
oltChipFirmVer = _OltChipFirmVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 3),
    _OltChipFirmVer_Type()
)
oltChipFirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipFirmVer.setStatus("current")
_OltChipBootVer_Type = Unsigned32
_OltChipBootVer_Object = MibTableColumn
oltChipBootVer = _OltChipBootVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 4),
    _OltChipBootVer_Type()
)
oltChipBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipBootVer.setStatus("current")
_OltChipPersVer_Type = Unsigned32
_OltChipPersVer_Object = MibTableColumn
oltChipPersVer = _OltChipPersVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 5),
    _OltChipPersVer_Type()
)
oltChipPersVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipPersVer.setStatus("current")
_OltChipApp0Ver_Type = Unsigned32
_OltChipApp0Ver_Object = MibTableColumn
oltChipApp0Ver = _OltChipApp0Ver_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 6),
    _OltChipApp0Ver_Type()
)
oltChipApp0Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipApp0Ver.setStatus("current")
_OltChipApp1Ver_Type = Unsigned32
_OltChipApp1Ver_Object = MibTableColumn
oltChipApp1Ver = _OltChipApp1Ver_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 7),
    _OltChipApp1Ver_Type()
)
oltChipApp1Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipApp1Ver.setStatus("current")
_OltChipDiagVer_Type = Unsigned32
_OltChipDiagVer_Object = MibTableColumn
oltChipDiagVer = _OltChipDiagVer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 1, 1, 8),
    _OltChipDiagVer_Type()
)
oltChipDiagVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltChipDiagVer.setStatus("current")
_OltOamRateTable_Object = MibTable
oltOamRateTable = _OltOamRateTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    oltOamRateTable.setStatus("current")
_OltOamRateEntry_Object = MibTableRow
oltOamRateEntry = _OltOamRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 2, 1)
)
oltOamRateEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    oltOamRateEntry.setStatus("current")


class _MinOamRate_Type(Integer32):
    """Custom type minOamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MinOamRate_Type.__name__ = "Integer32"
_MinOamRate_Object = MibTableColumn
minOamRate = _MinOamRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 2, 1, 1),
    _MinOamRate_Type()
)
minOamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minOamRate.setStatus("current")
if mibBuilder.loadTexts:
    minOamRate.setUnits("sec/PDU")


class _MaxOamRate_Type(Integer32):
    """Custom type maxOamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxOamRate_Type.__name__ = "Integer32"
_MaxOamRate_Object = MibTableColumn
maxOamRate = _MaxOamRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 2, 1, 2),
    _MaxOamRate_Type()
)
maxOamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxOamRate.setStatus("current")
if mibBuilder.loadTexts:
    maxOamRate.setUnits("PDUs/sec")


class _OamRspTimeout_Type(Integer32):
    """Custom type oamRspTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OamRspTimeout_Type.__name__ = "Integer32"
_OamRspTimeout_Object = MibTableColumn
oamRspTimeout = _OamRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 2, 1, 3),
    _OamRspTimeout_Type()
)
oamRspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamRspTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oamRspTimeout.setUnits("sec")
_DiscoveryParaTable_Object = MibTable
discoveryParaTable = _DiscoveryParaTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 3)
)
if mibBuilder.loadTexts:
    discoveryParaTable.setStatus("current")
_DiscoveryParaEntry_Object = MibTableRow
discoveryParaEntry = _DiscoveryParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 3, 1)
)
discoveryParaEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    discoveryParaEntry.setStatus("current")


class _DiscoverPeriod_Type(Integer32):
    """Custom type discoverPeriod based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_DiscoverPeriod_Type.__name__ = "Integer32"
_DiscoverPeriod_Object = MibTableColumn
discoverPeriod = _DiscoverPeriod_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 3, 1, 1),
    _DiscoverPeriod_Type()
)
discoverPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoverPeriod.setStatus("current")
if mibBuilder.loadTexts:
    discoverPeriod.setUnits("ms")


class _DiscoverWindow_Type(Integer32):
    """Custom type discoverWindow based on Integer32"""
    defaultValue = 16319

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(84, 131070),
    )


_DiscoverWindow_Type.__name__ = "Integer32"
_DiscoverWindow_Object = MibTableColumn
discoverWindow = _DiscoverWindow_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 3, 1, 2),
    _DiscoverWindow_Type()
)
discoverWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoverWindow.setStatus("current")
if mibBuilder.loadTexts:
    discoverWindow.setUnits("bytes")


class _DiscoverTimeoutVal_Type(Integer32):
    """Custom type discoverTimeoutVal based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DiscoverTimeoutVal_Type.__name__ = "Integer32"
_DiscoverTimeoutVal_Object = MibTableColumn
discoverTimeoutVal = _DiscoverTimeoutVal_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 3, 1, 3),
    _DiscoverTimeoutVal_Type()
)
discoverTimeoutVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discoverTimeoutVal.setStatus("current")
if mibBuilder.loadTexts:
    discoverTimeoutVal.setUnits("100ms")
_OltAdvancedConfigTable_Object = MibTable
oltAdvancedConfigTable = _OltAdvancedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    oltAdvancedConfigTable.setStatus("current")
_OltAdvancedConfigEntry_Object = MibTableRow
oltAdvancedConfigEntry = _OltAdvancedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1)
)
oltAdvancedConfigEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    oltAdvancedConfigEntry.setStatus("current")


class _OltAddiVlanEthType_Type(OctetString):
    """Custom type oltAddiVlanEthType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OltAddiVlanEthType_Type.__name__ = "OctetString"
_OltAddiVlanEthType_Object = MibTableColumn
oltAddiVlanEthType = _OltAddiVlanEthType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1, 1),
    _OltAddiVlanEthType_Type()
)
oltAddiVlanEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltAddiVlanEthType.setStatus("current")
_OnuUltraLongDistanceTrans_Type = OperSwitch
_OnuUltraLongDistanceTrans_Object = MibTableColumn
onuUltraLongDistanceTrans = _OnuUltraLongDistanceTrans_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1, 2),
    _OnuUltraLongDistanceTrans_Type()
)
onuUltraLongDistanceTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuUltraLongDistanceTrans.setStatus("current")
_OltBroadCastRateCtl_Type = OperSwitch
_OltBroadCastRateCtl_Object = MibTableColumn
oltBroadCastRateCtl = _OltBroadCastRateCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1, 3),
    _OltBroadCastRateCtl_Type()
)
oltBroadCastRateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltBroadCastRateCtl.setStatus("current")
_OltMultiCastRateCtl_Type = OperSwitch
_OltMultiCastRateCtl_Object = MibTableColumn
oltMultiCastRateCtl = _OltMultiCastRateCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1, 4),
    _OltMultiCastRateCtl_Type()
)
oltMultiCastRateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltMultiCastRateCtl.setStatus("current")
_OltUnkUcCastRateCtl_Type = OperSwitch
_OltUnkUcCastRateCtl_Object = MibTableColumn
oltUnkUcCastRateCtl = _OltUnkUcCastRateCtl_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1, 5),
    _OltUnkUcCastRateCtl_Type()
)
oltUnkUcCastRateCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltUnkUcCastRateCtl.setStatus("current")


class _OltBroadCastRate_Type(Integer32):
    """Custom type oltBroadCastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_OltBroadCastRate_Type.__name__ = "Integer32"
_OltBroadCastRate_Object = MibTableColumn
oltBroadCastRate = _OltBroadCastRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 4, 4, 1, 6),
    _OltBroadCastRate_Type()
)
oltBroadCastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltBroadCastRate.setStatus("current")
_OltBridgeConfigTable_Object = MibTable
oltBridgeConfigTable = _OltBridgeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    oltBridgeConfigTable.setStatus("current")
_OltBridgeConfigEntry_Object = MibTableRow
oltBridgeConfigEntry = _OltBridgeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1)
)
oltBridgeConfigEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    oltBridgeConfigEntry.setStatus("current")


class _DynMacAgeTime_Type(Integer32):
    """Custom type dynMacAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2419200),
    )


_DynMacAgeTime_Type.__name__ = "Integer32"
_DynMacAgeTime_Object = MibTableColumn
dynMacAgeTime = _DynMacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1, 1),
    _DynMacAgeTime_Type()
)
dynMacAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynMacAgeTime.setStatus("current")
_DownStreamResetAgeTimer_Type = OperSwitch
_DownStreamResetAgeTimer_Object = MibTableColumn
downStreamResetAgeTimer = _DownStreamResetAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1, 2),
    _DownStreamResetAgeTimer_Type()
)
downStreamResetAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downStreamResetAgeTimer.setStatus("current")


class _BridgedVlanNumber_Type(Integer32):
    """Custom type bridgedVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_BridgedVlanNumber_Type.__name__ = "Integer32"
_BridgedVlanNumber_Object = MibTableColumn
bridgedVlanNumber = _BridgedVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1, 3),
    _BridgedVlanNumber_Type()
)
bridgedVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgedVlanNumber.setStatus("current")
_MacOverWrite_Type = OperSwitch
_MacOverWrite_Object = MibTableColumn
macOverWrite = _MacOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1, 4),
    _MacOverWrite_Type()
)
macOverWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macOverWrite.setStatus("current")
_DiscardUnknownMac_Type = OperSwitch
_DiscardUnknownMac_Object = MibTableColumn
discardUnknownMac = _DiscardUnknownMac_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1, 5),
    _DiscardUnknownMac_Type()
)
discardUnknownMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discardUnknownMac.setStatus("current")
_ForwardTagOnSimpleBridge_Type = OperSwitch
_ForwardTagOnSimpleBridge_Object = MibTableColumn
forwardTagOnSimpleBridge = _ForwardTagOnSimpleBridge_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 5, 1, 6),
    _ForwardTagOnSimpleBridge_Type()
)
forwardTagOnSimpleBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardTagOnSimpleBridge.setStatus("current")
_Dba_ObjectIdentity = ObjectIdentity
dba = _Dba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6)
)
_LinkLevelSizeTable_Object = MibTable
linkLevelSizeTable = _LinkLevelSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    linkLevelSizeTable.setStatus("current")
_LinkLevelSizeEntry_Object = MibTableRow
linkLevelSizeEntry = _LinkLevelSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 1, 1)
)
linkLevelSizeEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    linkLevelSizeEntry.setStatus("current")


class _Level0Links_Type(Integer32):
    """Custom type level0Links based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Level0Links_Type.__name__ = "Integer32"
_Level0Links_Object = MibTableColumn
level0Links = _Level0Links_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 1, 1, 1),
    _Level0Links_Type()
)
level0Links.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    level0Links.setStatus("current")


class _Level1Links_Type(Integer32):
    """Custom type level1Links based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Level1Links_Type.__name__ = "Integer32"
_Level1Links_Object = MibTableColumn
level1Links = _Level1Links_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 1, 1, 2),
    _Level1Links_Type()
)
level1Links.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    level1Links.setStatus("current")


class _Level2Links_Type(Integer32):
    """Custom type level2Links based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Level2Links_Type.__name__ = "Integer32"
_Level2Links_Object = MibTableColumn
level2Links = _Level2Links_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 1, 1, 3),
    _Level2Links_Type()
)
level2Links.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    level2Links.setStatus("current")


class _NonDbaLinks_Type(Integer32):
    """Custom type nonDbaLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_NonDbaLinks_Type.__name__ = "Integer32"
_NonDbaLinks_Object = MibTableColumn
nonDbaLinks = _NonDbaLinks_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 1, 1, 4),
    _NonDbaLinks_Type()
)
nonDbaLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nonDbaLinks.setStatus("current")
_DbaDropDownWeightTable_Object = MibTable
dbaDropDownWeightTable = _DbaDropDownWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 2)
)
if mibBuilder.loadTexts:
    dbaDropDownWeightTable.setStatus("current")
_DbaDropDownWeightEntry_Object = MibTableRow
dbaDropDownWeightEntry = _DbaDropDownWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 2, 1)
)
dbaDropDownWeightEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    dbaDropDownWeightEntry.setStatus("current")


class _L0DropDownWeight_Type(Integer32):
    """Custom type l0DropDownWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_L0DropDownWeight_Type.__name__ = "Integer32"
_L0DropDownWeight_Object = MibTableColumn
l0DropDownWeight = _L0DropDownWeight_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 2, 1, 1),
    _L0DropDownWeight_Type()
)
l0DropDownWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l0DropDownWeight.setStatus("current")


class _L1DropDownWeight_Type(Integer32):
    """Custom type l1DropDownWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_L1DropDownWeight_Type.__name__ = "Integer32"
_L1DropDownWeight_Object = MibTableColumn
l1DropDownWeight = _L1DropDownWeight_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 2, 1, 2),
    _L1DropDownWeight_Type()
)
l1DropDownWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l1DropDownWeight.setStatus("current")


class _L2DropDownWeight_Type(Integer32):
    """Custom type l2DropDownWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_L2DropDownWeight_Type.__name__ = "Integer32"
_L2DropDownWeight_Object = MibTableColumn
l2DropDownWeight = _L2DropDownWeight_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 2, 1, 3),
    _L2DropDownWeight_Type()
)
l2DropDownWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2DropDownWeight.setStatus("current")
_DbaPollRateTable_Object = MibTable
dbaPollRateTable = _DbaPollRateTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 3)
)
if mibBuilder.loadTexts:
    dbaPollRateTable.setStatus("current")
_DbaPollRateEntry_Object = MibTableRow
dbaPollRateEntry = _DbaPollRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 3, 1)
)
dbaPollRateEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    dbaPollRateEntry.setStatus("current")


class _L0PollingRate_Type(Integer32):
    """Custom type l0PollingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L0PollingRate_Type.__name__ = "Integer32"
_L0PollingRate_Object = MibTableColumn
l0PollingRate = _L0PollingRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 3, 1, 1),
    _L0PollingRate_Type()
)
l0PollingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l0PollingRate.setStatus("current")


class _L1PollingRate_Type(Integer32):
    """Custom type l1PollingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L1PollingRate_Type.__name__ = "Integer32"
_L1PollingRate_Object = MibTableColumn
l1PollingRate = _L1PollingRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 3, 1, 2),
    _L1PollingRate_Type()
)
l1PollingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l1PollingRate.setStatus("current")


class _L2PollingRate_Type(Integer32):
    """Custom type l2PollingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2PollingRate_Type.__name__ = "Integer32"
_L2PollingRate_Object = MibTableColumn
l2PollingRate = _L2PollingRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 6, 3, 1, 3),
    _L2PollingRate_Type()
)
l2PollingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2PollingRate.setStatus("current")
_AggreBandWidthTable_Object = MibTable
aggreBandWidthTable = _AggreBandWidthTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    aggreBandWidthTable.setStatus("current")
_AggreBandWidthEntry_Object = MibTableRow
aggreBandWidthEntry = _AggreBandWidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 7, 1)
)
aggreBandWidthEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    aggreBandWidthEntry.setStatus("current")
_DirectionId_Type = DataDirection
_DirectionId_Object = MibTableColumn
directionId = _DirectionId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 7, 1, 1),
    _DirectionId_Type()
)
directionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    directionId.setStatus("current")


class _AggreBandWidth_Type(Integer32):
    """Custom type aggreBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AggreBandWidth_Type.__name__ = "Integer32"
_AggreBandWidth_Object = MibTableColumn
aggreBandWidth = _AggreBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 7, 1, 2),
    _AggreBandWidth_Type()
)
aggreBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggreBandWidth.setStatus("current")


class _AggreMaxBurstSize_Type(Integer32):
    """Custom type aggreMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AggreMaxBurstSize_Type.__name__ = "Integer32"
_AggreMaxBurstSize_Object = MibTableColumn
aggreMaxBurstSize = _AggreMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 7, 1, 3),
    _AggreMaxBurstSize_Type()
)
aggreMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggreMaxBurstSize.setStatus("current")
_OltAclRuleTable_Object = MibTable
oltAclRuleTable = _OltAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 8)
)
if mibBuilder.loadTexts:
    oltAclRuleTable.setStatus("current")
_OltAclRuleEntry_Object = MibTableRow
oltAclRuleEntry = _OltAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 8, 1)
)
oltAclRuleEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "oltPortId"),
)
if mibBuilder.loadTexts:
    oltAclRuleEntry.setStatus("current")


class _OltPortId_Type(Integer32):
    """Custom type oltPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oltPonPort", 1),
          ("oltSniPort", 2))
    )


_OltPortId_Type.__name__ = "Integer32"
_OltPortId_Object = MibTableColumn
oltPortId = _OltPortId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 8, 1, 1),
    _OltPortId_Type()
)
oltPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltPortId.setStatus("current")
_OltAclRuleData_Type = OctetString
_OltAclRuleData_Object = MibTableColumn
oltAclRuleData = _OltAclRuleData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 8, 1, 2),
    _OltAclRuleData_Type()
)
oltAclRuleData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltAclRuleData.setStatus("current")
_PriCopyMapTable_Object = MibTable
priCopyMapTable = _PriCopyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 9)
)
if mibBuilder.loadTexts:
    priCopyMapTable.setStatus("current")
_PriCopyMapEntry_Object = MibTableRow
priCopyMapEntry = _PriCopyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 9, 1)
)
priCopyMapEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    priCopyMapEntry.setStatus("current")
_PriCopyMapData_Type = OctetString
_PriCopyMapData_Object = MibTableColumn
priCopyMapData = _PriCopyMapData_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 9, 1, 1),
    _PriCopyMapData_Type()
)
priCopyMapData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priCopyMapData.setStatus("current")
_OltIgmpProxy_ObjectIdentity = ObjectIdentity
oltIgmpProxy = _OltIgmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10)
)
_IgmpProxyConfigTable_Object = MibTable
igmpProxyConfigTable = _IgmpProxyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1)
)
if mibBuilder.loadTexts:
    igmpProxyConfigTable.setStatus("current")
_IgmpProxyConfigEntry_Object = MibTableRow
igmpProxyConfigEntry = _IgmpProxyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1)
)
igmpProxyConfigEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    igmpProxyConfigEntry.setStatus("current")


class _MaxIgmpGroups_Type(Integer32):
    """Custom type maxIgmpGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MaxIgmpGroups_Type.__name__ = "Integer32"
_MaxIgmpGroups_Object = MibTableColumn
maxIgmpGroups = _MaxIgmpGroups_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 1),
    _MaxIgmpGroups_Type()
)
maxIgmpGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxIgmpGroups.setStatus("current")


class _RobustCount_Type(Integer32):
    """Custom type robustCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RobustCount_Type.__name__ = "Integer32"
_RobustCount_Object = MibTableColumn
robustCount = _RobustCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 2),
    _RobustCount_Type()
)
robustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    robustCount.setStatus("current")


class _QueryInterval_Type(Integer32):
    """Custom type queryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 65535),
    )


_QueryInterval_Type.__name__ = "Integer32"
_QueryInterval_Object = MibTableColumn
queryInterval = _QueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 3),
    _QueryInterval_Type()
)
queryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryInterval.setStatus("current")


class _QueryRspTimeout_Type(Integer32):
    """Custom type queryRspTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(11, 65534),
    )


_QueryRspTimeout_Type.__name__ = "Integer32"
_QueryRspTimeout_Object = MibTableColumn
queryRspTimeout = _QueryRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 4),
    _QueryRspTimeout_Type()
)
queryRspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryRspTimeout.setStatus("current")


class _QueryMaxResTime_Type(Integer32):
    """Custom type queryMaxResTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QueryMaxResTime_Type.__name__ = "Integer32"
_QueryMaxResTime_Object = MibTableColumn
queryMaxResTime = _QueryMaxResTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 5),
    _QueryMaxResTime_Type()
)
queryMaxResTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryMaxResTime.setStatus("current")


class _StartQueryCount_Type(Integer32):
    """Custom type startQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_StartQueryCount_Type.__name__ = "Integer32"
_StartQueryCount_Object = MibTableColumn
startQueryCount = _StartQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 6),
    _StartQueryCount_Type()
)
startQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startQueryCount.setStatus("current")


class _StartupQueryInterval_Type(Integer32):
    """Custom type startupQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 65535),
    )


_StartupQueryInterval_Type.__name__ = "Integer32"
_StartupQueryInterval_Object = MibTableColumn
startupQueryInterval = _StartupQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 7),
    _StartupQueryInterval_Type()
)
startupQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startupQueryInterval.setStatus("current")


class _LastMemberQueryCount_Type(Integer32):
    """Custom type lastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LastMemberQueryCount_Type.__name__ = "Integer32"
_LastMemberQueryCount_Object = MibTableColumn
lastMemberQueryCount = _LastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 8),
    _LastMemberQueryCount_Type()
)
lastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryCount.setStatus("current")


class _LastMemberQueryInterval_Type(Integer32):
    """Custom type lastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(11, 65535),
    )


_LastMemberQueryInterval_Type.__name__ = "Integer32"
_LastMemberQueryInterval_Object = MibTableColumn
lastMemberQueryInterval = _LastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 9),
    _LastMemberQueryInterval_Type()
)
lastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryInterval.setStatus("current")


class _LastMemberQueryResTime_Type(Integer32):
    """Custom type lastMemberQueryResTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LastMemberQueryResTime_Type.__name__ = "Integer32"
_LastMemberQueryResTime_Object = MibTableColumn
lastMemberQueryResTime = _LastMemberQueryResTime_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 10),
    _LastMemberQueryResTime_Type()
)
lastMemberQueryResTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryResTime.setStatus("current")


class _UpstreamRetransCount_Type(Integer32):
    """Custom type upstreamRetransCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UpstreamRetransCount_Type.__name__ = "Integer32"
_UpstreamRetransCount_Object = MibTableColumn
upstreamRetransCount = _UpstreamRetransCount_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 11),
    _UpstreamRetransCount_Type()
)
upstreamRetransCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreamRetransCount.setStatus("current")


class _UpstreamRetransInterval_Type(Integer32):
    """Custom type upstreamRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UpstreamRetransInterval_Type.__name__ = "Integer32"
_UpstreamRetransInterval_Object = MibTableColumn
upstreamRetransInterval = _UpstreamRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 12),
    _UpstreamRetransInterval_Type()
)
upstreamRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upstreamRetransInterval.setStatus("current")


class _IgmpQueues_Type(Integer32):
    """Custom type igmpQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IgmpQueues_Type.__name__ = "Integer32"
_IgmpQueues_Object = MibTableColumn
igmpQueues = _IgmpQueues_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 13),
    _IgmpQueues_Type()
)
igmpQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQueues.setStatus("current")


class _IgmpSlaMinGuaranteedBW_Type(Integer32):
    """Custom type igmpSlaMinGuaranteedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_IgmpSlaMinGuaranteedBW_Type.__name__ = "Integer32"
_IgmpSlaMinGuaranteedBW_Object = MibTableColumn
igmpSlaMinGuaranteedBW = _IgmpSlaMinGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 14),
    _IgmpSlaMinGuaranteedBW_Type()
)
igmpSlaMinGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSlaMinGuaranteedBW.setStatus("current")


class _IgmpSlaMaxAllowedBW_Type(Integer32):
    """Custom type igmpSlaMaxAllowedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_IgmpSlaMaxAllowedBW_Type.__name__ = "Integer32"
_IgmpSlaMaxAllowedBW_Object = MibTableColumn
igmpSlaMaxAllowedBW = _IgmpSlaMaxAllowedBW_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 15),
    _IgmpSlaMaxAllowedBW_Type()
)
igmpSlaMaxAllowedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSlaMaxAllowedBW.setStatus("current")


class _IgmpSlaDelaySensitive_Type(Integer32):
    """Custom type igmpSlaDelaySensitive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sensitive", 1),
          ("tolerant", 2))
    )


_IgmpSlaDelaySensitive_Type.__name__ = "Integer32"
_IgmpSlaDelaySensitive_Object = MibTableColumn
igmpSlaDelaySensitive = _IgmpSlaDelaySensitive_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 16),
    _IgmpSlaDelaySensitive_Type()
)
igmpSlaDelaySensitive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSlaDelaySensitive.setStatus("current")


class _IgmpSlaMaxBurstSize_Type(Integer32):
    """Custom type igmpSlaMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IgmpSlaMaxBurstSize_Type.__name__ = "Integer32"
_IgmpSlaMaxBurstSize_Object = MibTableColumn
igmpSlaMaxBurstSize = _IgmpSlaMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 17),
    _IgmpSlaMaxBurstSize_Type()
)
igmpSlaMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSlaMaxBurstSize.setStatus("current")


class _IgmpProxyOper_Type(Integer32):
    """Custom type igmpProxyOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("refreshGroups", 3),
          ("restorePara", 2))
    )


_IgmpProxyOper_Type.__name__ = "Integer32"
_IgmpProxyOper_Object = MibTableColumn
igmpProxyOper = _IgmpProxyOper_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 1, 1, 19),
    _IgmpProxyOper_Type()
)
igmpProxyOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProxyOper.setStatus("current")
_IgmpGroupTable_Object = MibTable
igmpGroupTable = _IgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 2)
)
if mibBuilder.loadTexts:
    igmpGroupTable.setStatus("current")
_IgmpGroupEntry_Object = MibTableRow
igmpGroupEntry = _IgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 2, 1)
)
igmpGroupEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "igmpGroupIndex"),
)
if mibBuilder.loadTexts:
    igmpGroupEntry.setStatus("current")


class _IgmpGroupIndex_Type(Integer32):
    """Custom type igmpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpGroupIndex_Type.__name__ = "Integer32"
_IgmpGroupIndex_Object = MibTableColumn
igmpGroupIndex = _IgmpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 2, 1, 1),
    _IgmpGroupIndex_Type()
)
igmpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpGroupIndex.setStatus("current")


class _IgmpGroupVlan_Type(Integer32):
    """Custom type igmpGroupVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgmpGroupVlan_Type.__name__ = "Integer32"
_IgmpGroupVlan_Object = MibTableColumn
igmpGroupVlan = _IgmpGroupVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 2, 1, 2),
    _IgmpGroupVlan_Type()
)
igmpGroupVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupVlan.setStatus("current")
_IgmpGroupIpAddr_Type = IpAddress
_IgmpGroupIpAddr_Object = MibTableColumn
igmpGroupIpAddr = _IgmpGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 10, 2, 1, 3),
    _IgmpGroupIpAddr_Type()
)
igmpGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupIpAddr.setStatus("current")
_AccessUserIdentifer_ObjectIdentity = ObjectIdentity
accessUserIdentifer = _AccessUserIdentifer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 11)
)
_AccessUserIdentiferConfigTable_Object = MibTable
accessUserIdentiferConfigTable = _AccessUserIdentiferConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 11, 1)
)
if mibBuilder.loadTexts:
    accessUserIdentiferConfigTable.setStatus("current")
_AccessUserIdentiferConfigEntry_Object = MibTableRow
accessUserIdentiferConfigEntry = _AccessUserIdentiferConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 11, 1, 1)
)
accessUserIdentiferConfigEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
)
if mibBuilder.loadTexts:
    accessUserIdentiferConfigEntry.setStatus("current")
_PppoePlusEnable_Type = OperSwitch
_PppoePlusEnable_Object = MibTableColumn
pppoePlusEnable = _PppoePlusEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 11, 1, 1, 1),
    _PppoePlusEnable_Type()
)
pppoePlusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePlusEnable.setStatus("current")
_DhcpOption82_Type = OperSwitch
_DhcpOption82_Object = MibTableColumn
dhcpOption82 = _DhcpOption82_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 11, 1, 1, 2),
    _DhcpOption82_Type()
)
dhcpOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82.setStatus("current")
_Llid_ObjectIdentity = ObjectIdentity
llid = _Llid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12)
)
_LlidConfigTable_Object = MibTable
llidConfigTable = _LlidConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1)
)
if mibBuilder.loadTexts:
    llidConfigTable.setStatus("current")
_LlidConfigEntry_Object = MibTableRow
llidConfigEntry = _LlidConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1)
)
llidConfigEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
)
if mibBuilder.loadTexts:
    llidConfigEntry.setStatus("current")
_LinkId_Type = Unsigned32
_LinkId_Object = MibTableColumn
linkId = _LinkId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 1),
    _LinkId_Type()
)
linkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkId.setStatus("current")
_LlidAssigned_Type = Unsigned32
_LlidAssigned_Object = MibTableColumn
llidAssigned = _LlidAssigned_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 2),
    _LlidAssigned_Type()
)
llidAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidAssigned.setStatus("current")
_AssociatedOnuId_Type = Unsigned32
_AssociatedOnuId_Object = MibTableColumn
associatedOnuId = _AssociatedOnuId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 3),
    _AssociatedOnuId_Type()
)
associatedOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associatedOnuId.setStatus("current")
_LlidMac_Type = MacAddress
_LlidMac_Object = MibTableColumn
llidMac = _LlidMac_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 4),
    _LlidMac_Type()
)
llidMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidMac.setStatus("current")
_LinkOnLineStatus_Type = DeviceStatus
_LinkOnLineStatus_Object = MibTableColumn
linkOnLineStatus = _LinkOnLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 5),
    _LinkOnLineStatus_Type()
)
linkOnLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOnLineStatus.setStatus("current")


class _KeyChangeTimer_Type(Integer32):
    """Custom type keyChangeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_KeyChangeTimer_Type.__name__ = "Integer32"
_KeyChangeTimer_Object = MibTableColumn
keyChangeTimer = _KeyChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 6),
    _KeyChangeTimer_Type()
)
keyChangeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyChangeTimer.setStatus("current")


class _LlidBridgeType_Type(Integer32):
    """Custom type llidBridgeType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("dedicatedDoubleVlan", 3),
          ("dedicatedSingleVlan", 2),
          ("doubleTaggedSharedVlan", 16),
          ("linkCrossConnect", 7),
          ("prioritiedVlan", 8),
          ("priorityCopyDoubleVlan", 10),
          ("priorityCopySharedVlan", 11),
          ("priorityCopySingleVlan", 9),
          ("prioritySharedVlan", 12),
          ("prioritySimpleBridged", 13),
          ("sharedVlan", 4),
          ("simpleBridged", 1),
          ("translatedVlan", 6),
          ("transparentPrioritySharedVlan", 14),
          ("transparentSharedVlanWithBroadcast", 15),
          ("transparentVlan", 5))
    )


_LlidBridgeType_Type.__name__ = "Integer32"
_LlidBridgeType_Object = MibTableColumn
llidBridgeType = _LlidBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 7),
    _LlidBridgeType_Type()
)
llidBridgeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidBridgeType.setStatus("current")


class _LlidMacEntryLimit_Type(Integer32):
    """Custom type llidMacEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LlidMacEntryLimit_Type.__name__ = "Integer32"
_LlidMacEntryLimit_Object = MibTableColumn
llidMacEntryLimit = _LlidMacEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 8),
    _LlidMacEntryLimit_Type()
)
llidMacEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidMacEntryLimit.setStatus("current")
_CrossConnectLinkId_Type = Unsigned32
_CrossConnectLinkId_Object = MibTableColumn
crossConnectLinkId = _CrossConnectLinkId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 9),
    _CrossConnectLinkId_Type()
)
crossConnectLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectLinkId.setStatus("current")


class _LlidOperation_Type(Integer32):
    """Custom type llidOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("breakCrossLink", 4),
          ("deleteLinkEntry", 6),
          ("reRegist", 3),
          ("restoreConfig", 5))
    )


_LlidOperation_Type.__name__ = "Integer32"
_LlidOperation_Object = MibTableColumn
llidOperation = _LlidOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 1, 1, 10),
    _LlidOperation_Type()
)
llidOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llidOperation.setStatus("current")
_LlidAdvancedManage_ObjectIdentity = ObjectIdentity
llidAdvancedManage = _LlidAdvancedManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 2)
)
_LinkOamRateTable_Object = MibTable
linkOamRateTable = _LinkOamRateTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 2, 1)
)
if mibBuilder.loadTexts:
    linkOamRateTable.setStatus("current")
_LinkOamRateEntry_Object = MibTableRow
linkOamRateEntry = _LinkOamRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 2, 1, 1)
)
linkOamRateEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
)
if mibBuilder.loadTexts:
    linkOamRateEntry.setStatus("current")


class _MaxLinkOamRate_Type(Integer32):
    """Custom type maxLinkOamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_MaxLinkOamRate_Type.__name__ = "Integer32"
_MaxLinkOamRate_Object = MibTableColumn
maxLinkOamRate = _MaxLinkOamRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 2, 1, 1, 1),
    _MaxLinkOamRate_Type()
)
maxLinkOamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLinkOamRate.setStatus("current")


class _MinLinkOamRate_Type(Integer32):
    """Custom type minLinkOamRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MinLinkOamRate_Type.__name__ = "Integer32"
_MinLinkOamRate_Object = MibTableColumn
minLinkOamRate = _MinLinkOamRate_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 2, 1, 1, 2),
    _MinLinkOamRate_Type()
)
minLinkOamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minLinkOamRate.setStatus("current")
_Sla_ObjectIdentity = ObjectIdentity
sla = _Sla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3)
)
_LlidSlaTable_Object = MibTable
llidSlaTable = _LlidSlaTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1)
)
if mibBuilder.loadTexts:
    llidSlaTable.setStatus("current")
_LlidSlaEntry_Object = MibTableRow
llidSlaEntry = _LlidSlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1, 1)
)
llidSlaEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    llidSlaEntry.setStatus("current")


class _MinGuaranteedBW_Type(Integer32):
    """Custom type minGuaranteedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MinGuaranteedBW_Type.__name__ = "Integer32"
_MinGuaranteedBW_Object = MibTableColumn
minGuaranteedBW = _MinGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1, 1, 1),
    _MinGuaranteedBW_Type()
)
minGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minGuaranteedBW.setStatus("current")
if mibBuilder.loadTexts:
    minGuaranteedBW.setUnits("kbps")


class _MaxAllowedBW_Type(Integer32):
    """Custom type maxAllowedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MaxAllowedBW_Type.__name__ = "Integer32"
_MaxAllowedBW_Object = MibTableColumn
maxAllowedBW = _MaxAllowedBW_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1, 1, 2),
    _MaxAllowedBW_Type()
)
maxAllowedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxAllowedBW.setStatus("current")
if mibBuilder.loadTexts:
    maxAllowedBW.setUnits("kbps")


class _DelaySensitive_Type(Integer32):
    """Custom type delaySensitive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sensitive", 2),
          ("tolerant", 1))
    )


_DelaySensitive_Type.__name__ = "Integer32"
_DelaySensitive_Object = MibTableColumn
delaySensitive = _DelaySensitive_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1, 1, 3),
    _DelaySensitive_Type()
)
delaySensitive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    delaySensitive.setStatus("current")


class _MaxBurstSize_Type(Integer32):
    """Custom type maxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MaxBurstSize_Type.__name__ = "Integer32"
_MaxBurstSize_Object = MibTableColumn
maxBurstSize = _MaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1, 1, 4),
    _MaxBurstSize_Type()
)
maxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    maxBurstSize.setUnits("kbytes")
_SlaEnable_Type = OperSwitch
_SlaEnable_Object = MibTableColumn
slaEnable = _SlaEnable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 1, 1, 5),
    _SlaEnable_Type()
)
slaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaEnable.setStatus("current")
_SlaWeightTable_Object = MibTable
slaWeightTable = _SlaWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 2)
)
if mibBuilder.loadTexts:
    slaWeightTable.setStatus("current")
_SlaWeightEntry_Object = MibTableRow
slaWeightEntry = _SlaWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 2, 1)
)
slaWeightEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
    (0, "FD-OLT-MIB", "directionId"),
)
if mibBuilder.loadTexts:
    slaWeightEntry.setStatus("current")


class _DbaTokens_Type(Integer32):
    """Custom type dbaTokens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DbaTokens_Type.__name__ = "Integer32"
_DbaTokens_Object = MibTableColumn
dbaTokens = _DbaTokens_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 2, 1, 1),
    _DbaTokens_Type()
)
dbaTokens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbaTokens.setStatus("current")


class _SchedulerMinTokens_Type(Integer32):
    """Custom type schedulerMinTokens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_SchedulerMinTokens_Type.__name__ = "Integer32"
_SchedulerMinTokens_Object = MibTableColumn
schedulerMinTokens = _SchedulerMinTokens_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 2, 1, 2),
    _SchedulerMinTokens_Type()
)
schedulerMinTokens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulerMinTokens.setStatus("current")


class _SchedulerMaxTokens_Type(Integer32):
    """Custom type schedulerMaxTokens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_SchedulerMaxTokens_Type.__name__ = "Integer32"
_SchedulerMaxTokens_Object = MibTableColumn
schedulerMaxTokens = _SchedulerMaxTokens_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 2, 1, 3),
    _SchedulerMaxTokens_Type()
)
schedulerMaxTokens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulerMaxTokens.setStatus("current")
_ForceReport_Type = TruthValue
_ForceReport_Object = MibTableColumn
forceReport = _ForceReport_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 2, 1, 4),
    _ForceReport_Type()
)
forceReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forceReport.setStatus("current")
_MulticastSlaTable_Object = MibTable
multicastSlaTable = _MulticastSlaTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 3)
)
if mibBuilder.loadTexts:
    multicastSlaTable.setStatus("current")
_MulticastSlaEntry_Object = MibTableRow
multicastSlaEntry = _MulticastSlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 3, 1)
)
multicastSlaEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
)
if mibBuilder.loadTexts:
    multicastSlaEntry.setStatus("current")


class _MultiMinGuanBW_Type(Integer32):
    """Custom type multiMinGuanBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_MultiMinGuanBW_Type.__name__ = "Integer32"
_MultiMinGuanBW_Object = MibTableColumn
multiMinGuanBW = _MultiMinGuanBW_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 3, 1, 1),
    _MultiMinGuanBW_Type()
)
multiMinGuanBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiMinGuanBW.setStatus("current")


class _MultiMaxAllowedBW_Type(Integer32):
    """Custom type multiMaxAllowedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1000000),
    )


_MultiMaxAllowedBW_Type.__name__ = "Integer32"
_MultiMaxAllowedBW_Object = MibTableColumn
multiMaxAllowedBW = _MultiMaxAllowedBW_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 3, 1, 2),
    _MultiMaxAllowedBW_Type()
)
multiMaxAllowedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiMaxAllowedBW.setStatus("current")


class _MultiDelaySensitive_Type(Integer32):
    """Custom type multiDelaySensitive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sensitive", 1),
          ("tolerant", 2))
    )


_MultiDelaySensitive_Type.__name__ = "Integer32"
_MultiDelaySensitive_Object = MibTableColumn
multiDelaySensitive = _MultiDelaySensitive_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 3, 1, 3),
    _MultiDelaySensitive_Type()
)
multiDelaySensitive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiDelaySensitive.setStatus("current")


class _MultiMaxBurstSize_Type(Integer32):
    """Custom type multiMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MultiMaxBurstSize_Type.__name__ = "Integer32"
_MultiMaxBurstSize_Object = MibTableColumn
multiMaxBurstSize = _MultiMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 3, 3, 1, 4),
    _MultiMaxBurstSize_Type()
)
multiMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multiMaxBurstSize.setStatus("current")
_LlidVlan_ObjectIdentity = ObjectIdentity
llidVlan = _LlidVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4)
)
_LlidVlanCfgTable_Object = MibTable
llidVlanCfgTable = _LlidVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 1)
)
if mibBuilder.loadTexts:
    llidVlanCfgTable.setStatus("current")
_LlidVlanCfgEntry_Object = MibTableRow
llidVlanCfgEntry = _LlidVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 1, 1)
)
llidVlanCfgEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
    (0, "FD-OLT-MIB", "llidVlanTag"),
)
if mibBuilder.loadTexts:
    llidVlanCfgEntry.setStatus("current")


class _LlidVlanTag_Type(Integer32):
    """Custom type llidVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_LlidVlanTag_Type.__name__ = "Integer32"
_LlidVlanTag_Object = MibTableColumn
llidVlanTag = _LlidVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 1, 1, 1),
    _LlidVlanTag_Type()
)
llidVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    llidVlanTag.setStatus("current")
_LlidVlanRowStatus_Type = RowStatus
_LlidVlanRowStatus_Object = MibTableColumn
llidVlanRowStatus = _LlidVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 1, 1, 2),
    _LlidVlanRowStatus_Type()
)
llidVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llidVlanRowStatus.setStatus("current")
_VlanLlidTable_Object = MibTable
vlanLlidTable = _VlanLlidTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 2)
)
if mibBuilder.loadTexts:
    vlanLlidTable.setStatus("current")
_VlanLlidEntry_Object = MibTableRow
vlanLlidEntry = _VlanLlidEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 2, 1)
)
vlanLlidEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanLlidEntry.setStatus("current")
_VlanId_Type = Unsigned32
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 2, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_LinkIDsInVlan_Type = OctetString
_LinkIDsInVlan_Object = MibTableColumn
linkIDsInVlan = _LinkIDsInVlan_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 2, 1, 2),
    _LinkIDsInVlan_Type()
)
linkIDsInVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIDsInVlan.setStatus("current")
_PriVlanTable_Object = MibTable
priVlanTable = _PriVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3)
)
if mibBuilder.loadTexts:
    priVlanTable.setStatus("current")
_PriVlanEntry_Object = MibTableRow
priVlanEntry = _PriVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1)
)
priVlanEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
)
if mibBuilder.loadTexts:
    priVlanEntry.setStatus("current")


class _NetVlanId_Type(Integer32):
    """Custom type netVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_NetVlanId_Type.__name__ = "Integer32"
_NetVlanId_Object = MibTableColumn
netVlanId = _NetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 1),
    _NetVlanId_Type()
)
netVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netVlanId.setStatus("current")


class _UpstreamCos_Type(Integer32):
    """Custom type upstreamCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UpstreamCos_Type.__name__ = "Integer32"
_UpstreamCos_Object = MibTableColumn
upstreamCos = _UpstreamCos_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 2),
    _UpstreamCos_Type()
)
upstreamCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    upstreamCos.setStatus("current")


class _PriSelector_Type(Integer32):
    """Custom type priSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("tos", 2))
    )


_PriSelector_Type.__name__ = "Integer32"
_PriSelector_Object = MibTableColumn
priSelector = _PriSelector_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 3),
    _PriSelector_Type()
)
priSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priSelector.setStatus("current")


class _MinPriValue_Type(Integer32):
    """Custom type minPriValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MinPriValue_Type.__name__ = "Integer32"
_MinPriValue_Object = MibTableColumn
minPriValue = _MinPriValue_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 4),
    _MinPriValue_Type()
)
minPriValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    minPriValue.setStatus("current")


class _MaxPriValue_Type(Integer32):
    """Custom type maxPriValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MaxPriValue_Type.__name__ = "Integer32"
_MaxPriValue_Object = MibTableColumn
maxPriValue = _MaxPriValue_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 5),
    _MaxPriValue_Type()
)
maxPriValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maxPriValue.setStatus("current")
_TransNonTosFrame_Type = TruthValue
_TransNonTosFrame_Object = MibTableColumn
transNonTosFrame = _TransNonTosFrame_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 6),
    _TransNonTosFrame_Type()
)
transNonTosFrame.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    transNonTosFrame.setStatus("current")
_PriVlanRowStatus_Type = RowStatus
_PriVlanRowStatus_Object = MibTableColumn
priVlanRowStatus = _PriVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 4, 3, 1, 7),
    _PriVlanRowStatus_Type()
)
priVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priVlanRowStatus.setStatus("current")
_BlockedLinkTable_Object = MibTable
blockedLinkTable = _BlockedLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 5)
)
if mibBuilder.loadTexts:
    blockedLinkTable.setStatus("current")
_BlockedLinkEntry_Object = MibTableRow
blockedLinkEntry = _BlockedLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 5, 1)
)
blockedLinkEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
)
if mibBuilder.loadTexts:
    blockedLinkEntry.setStatus("current")
_BlockedLinkMac_Type = MacAddress
_BlockedLinkMac_Object = MibTableColumn
blockedLinkMac = _BlockedLinkMac_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 5, 1, 1),
    _BlockedLinkMac_Type()
)
blockedLinkMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockedLinkMac.setStatus("current")


class _BlockedMacOper_Type(Integer32):
    """Custom type blockedMacOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("unblock", 2)
    )


_BlockedMacOper_Type.__name__ = "Integer32"
_BlockedMacOper_Object = MibTableColumn
blockedMacOper = _BlockedMacOper_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 5, 1, 2),
    _BlockedMacOper_Type()
)
blockedMacOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockedMacOper.setStatus("current")
_MacAddr_ObjectIdentity = ObjectIdentity
macAddr = _MacAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6)
)
_DynamicMac_ObjectIdentity = ObjectIdentity
dynamicMac = _DynamicMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1)
)
_DynMacOperTable_Object = MibTable
dynMacOperTable = _DynMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dynMacOperTable.setStatus("current")
_DynMacOperEntry_Object = MibTableRow
dynMacOperEntry = _DynMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 1, 1)
)
dynMacOperEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
)
if mibBuilder.loadTexts:
    dynMacOperEntry.setStatus("current")


class _DynMacOperation_Type(Integer32):
    """Custom type dynMacOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("refresh", 3))
    )


_DynMacOperation_Type.__name__ = "Integer32"
_DynMacOperation_Object = MibTableColumn
dynMacOperation = _DynMacOperation_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 1, 1, 1),
    _DynMacOperation_Type()
)
dynMacOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynMacOperation.setStatus("current")
_DynMacTable_Object = MibTable
dynMacTable = _DynMacTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 2)
)
if mibBuilder.loadTexts:
    dynMacTable.setStatus("current")
_DynMacEntry_Object = MibTableRow
dynMacEntry = _DynMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 2, 1)
)
dynMacEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
    (0, "FD-OLT-MIB", "dynMacIndex"),
)
if mibBuilder.loadTexts:
    dynMacEntry.setStatus("current")


class _DynMacIndex_Type(Integer32):
    """Custom type dynMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DynMacIndex_Type.__name__ = "Integer32"
_DynMacIndex_Object = MibTableColumn
dynMacIndex = _DynMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 2, 1, 1),
    _DynMacIndex_Type()
)
dynMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dynMacIndex.setStatus("current")
_DynMacAddr_Type = MacAddress
_DynMacAddr_Object = MibTableColumn
dynMacAddr = _DynMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 1, 2, 1, 2),
    _DynMacAddr_Type()
)
dynMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynMacAddr.setStatus("current")
_StaticMac_ObjectIdentity = ObjectIdentity
staticMac = _StaticMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 2)
)
_StaticMacTable_Object = MibTable
staticMacTable = _StaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 2, 1)
)
if mibBuilder.loadTexts:
    staticMacTable.setStatus("current")
_StaticMacEntry_Object = MibTableRow
staticMacEntry = _StaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 2, 1, 1)
)
staticMacEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
    (0, "FD-OLT-MIB", "oltId"),
    (0, "FD-OLT-MIB", "linkId"),
    (0, "FD-OLT-MIB", "staticMacIndex"),
)
if mibBuilder.loadTexts:
    staticMacEntry.setStatus("current")


class _StaticMacIndex_Type(Integer32):
    """Custom type staticMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_StaticMacIndex_Type.__name__ = "Integer32"
_StaticMacIndex_Object = MibTableColumn
staticMacIndex = _StaticMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 2, 1, 1, 1),
    _StaticMacIndex_Type()
)
staticMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticMacIndex.setStatus("current")
_StaticMacAddr_Type = MacAddress
_StaticMacAddr_Object = MibTableColumn
staticMacAddr = _StaticMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 2, 1, 1, 2),
    _StaticMacAddr_Type()
)
staticMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacAddr.setStatus("current")
_StaticMacRowStatus_Type = RowStatus
_StaticMacRowStatus_Object = MibTableColumn
staticMacRowStatus = _StaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 12, 6, 2, 1, 1, 3),
    _StaticMacRowStatus_Type()
)
staticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMacRowStatus.setStatus("current")
_OnuP2pTable_Object = MibTable
onuP2pTable = _OnuP2pTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 13)
)
if mibBuilder.loadTexts:
    onuP2pTable.setStatus("current")
_OnuP2pEntry_Object = MibTableRow
onuP2pEntry = _OnuP2pEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 13, 1)
)
onuP2pEntry.setIndexNames(
    (0, "FD-SYSTEM-MIB", "ponCardSlotId"),
)
if mibBuilder.loadTexts:
    onuP2pEntry.setStatus("current")


class _OnuP2pEnDis_Type(Integer32):
    """Custom type onuP2pEnDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuP2pEnDis_Type.__name__ = "Integer32"
_OnuP2pEnDis_Object = MibTableColumn
onuP2pEnDis = _OnuP2pEnDis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 13, 1, 1),
    _OnuP2pEnDis_Type()
)
onuP2pEnDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuP2pEnDis.setStatus("current")


class _OnuP2pPonEnDis_Type(Integer32):
    """Custom type onuP2pPonEnDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              65536,
              65537)
        )
    )
    namedValues = NamedValues(
        *(("disdis", 0),
          ("disen", 1),
          ("endis", 65536),
          ("enen", 65537))
    )


_OnuP2pPonEnDis_Type.__name__ = "Integer32"
_OnuP2pPonEnDis_Object = MibTableColumn
onuP2pPonEnDis = _OnuP2pPonEnDis_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 13, 1, 2),
    _OnuP2pPonEnDis_Type()
)
onuP2pPonEnDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuP2pPonEnDis.setStatus("current")
_FdOltConformance_ObjectIdentity = ObjectIdentity
fdOltConformance = _FdOltConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20)
)
_FdOltGroups_ObjectIdentity = ObjectIdentity
fdOltGroups = _FdOltGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1)
)
_FdOltCompliances_ObjectIdentity = ObjectIdentity
fdOltCompliances = _FdOltCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 2)
)

# Managed Objects groups

oltBaseManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 1)
)
oltBaseManageGroup.setObjects(
      *(("FD-OLT-MIB", "oltMacAddr"),
        ("FD-OLT-MIB", "oltWorkState"),
        ("FD-OLT-MIB", "oltEnable"),
        ("FD-OLT-MIB", "maxPermitLLIDNumber"),
        ("FD-OLT-MIB", "registeredLLIDNumber"),
        ("FD-OLT-MIB", "accessedOnuNumber"),
        ("FD-OLT-MIB", "oltUpgradeStat"),
        ("FD-OLT-MIB", "onuMgmtDefType"),
        ("FD-OLT-MIB", "oltOperate"),
        ("FD-OLT-MIB", "linkIdExhaust"),
        ("FD-OLT-MIB", "onuIdExhaust"),
        ("FD-OLT-MIB", "linkIdOverWrite"),
        ("FD-OLT-MIB", "onuIdOverWrite"),
        ("FD-OLT-MIB", "dynMacAgeTime"),
        ("FD-OLT-MIB", "downStreamResetAgeTimer"),
        ("FD-OLT-MIB", "bridgedVlanNumber"),
        ("FD-OLT-MIB", "macOverWrite"),
        ("FD-OLT-MIB", "discardUnknownMac"),
        ("FD-OLT-MIB", "forwardTagOnSimpleBridge"),
        ("FD-OLT-MIB", "level0Links"),
        ("FD-OLT-MIB", "level1Links"),
        ("FD-OLT-MIB", "level2Links"),
        ("FD-OLT-MIB", "nonDbaLinks"),
        ("FD-OLT-MIB", "l0DropDownWeight"),
        ("FD-OLT-MIB", "l1DropDownWeight"),
        ("FD-OLT-MIB", "l2DropDownWeight"),
        ("FD-OLT-MIB", "l0PollingRate"),
        ("FD-OLT-MIB", "l1PollingRate"),
        ("FD-OLT-MIB", "l2PollingRate"),
        ("FD-OLT-MIB", "aggreBandWidth"),
        ("FD-OLT-MIB", "aggreMaxBurstSize"),
        ("FD-OLT-MIB", "oltAclRuleData"),
        ("FD-OLT-MIB", "priCopyMapData"))
)
if mibBuilder.loadTexts:
    oltBaseManageGroup.setStatus("current")

oltAdvanceManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 2)
)
oltAdvanceManageGroup.setObjects(
      *(("FD-OLT-MIB", "oltChipProCode"),
        ("FD-OLT-MIB", "oltChipVer"),
        ("FD-OLT-MIB", "oltChipFirmVer"),
        ("FD-OLT-MIB", "oltChipBootVer"),
        ("FD-OLT-MIB", "oltChipPersVer"),
        ("FD-OLT-MIB", "oltChipApp0Ver"),
        ("FD-OLT-MIB", "oltChipApp1Ver"),
        ("FD-OLT-MIB", "oltChipDiagVer"),
        ("FD-OLT-MIB", "minOamRate"),
        ("FD-OLT-MIB", "maxOamRate"),
        ("FD-OLT-MIB", "oamRspTimeout"),
        ("FD-OLT-MIB", "discoverPeriod"),
        ("FD-OLT-MIB", "discoverWindow"),
        ("FD-OLT-MIB", "discoverTimeoutVal"),
        ("FD-OLT-MIB", "oltAddiVlanEthType"),
        ("FD-OLT-MIB", "onuUltraLongDistanceTrans"),
        ("FD-OLT-MIB", "oltBroadCastRateCtl"),
        ("FD-OLT-MIB", "oltMultiCastRateCtl"),
        ("FD-OLT-MIB", "oltUnkUcCastRateCtl"),
        ("FD-OLT-MIB", "oltBroadCastRate"))
)
if mibBuilder.loadTexts:
    oltAdvanceManageGroup.setStatus("current")

oltIgmpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 3)
)
oltIgmpProxyGroup.setObjects(
      *(("FD-OLT-MIB", "maxIgmpGroups"),
        ("FD-OLT-MIB", "robustCount"),
        ("FD-OLT-MIB", "queryInterval"),
        ("FD-OLT-MIB", "queryRspTimeout"),
        ("FD-OLT-MIB", "queryMaxResTime"),
        ("FD-OLT-MIB", "startQueryCount"),
        ("FD-OLT-MIB", "startupQueryInterval"),
        ("FD-OLT-MIB", "lastMemberQueryCount"),
        ("FD-OLT-MIB", "lastMemberQueryInterval"),
        ("FD-OLT-MIB", "lastMemberQueryResTime"),
        ("FD-OLT-MIB", "upstreamRetransCount"),
        ("FD-OLT-MIB", "upstreamRetransInterval"),
        ("FD-OLT-MIB", "igmpQueues"),
        ("FD-OLT-MIB", "igmpSlaMinGuaranteedBW"),
        ("FD-OLT-MIB", "igmpSlaMaxAllowedBW"),
        ("FD-OLT-MIB", "igmpSlaDelaySensitive"),
        ("FD-OLT-MIB", "igmpSlaMaxBurstSize"),
        ("FD-OLT-MIB", "igmpProxyOper"),
        ("FD-OLT-MIB", "igmpGroupVlan"),
        ("FD-OLT-MIB", "igmpGroupIpAddr"))
)
if mibBuilder.loadTexts:
    oltIgmpProxyGroup.setStatus("current")

oltPPPoEPlusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 4)
)
oltPPPoEPlusGroup.setObjects(
      *(("FD-OLT-MIB", "pppoePlusEnable"),
        ("FD-OLT-MIB", "dhcpOption82"))
)
if mibBuilder.loadTexts:
    oltPPPoEPlusGroup.setStatus("current")

oltLlidBaseManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 5)
)
oltLlidBaseManageGroup.setObjects(
      *(("FD-OLT-MIB", "llidAssigned"),
        ("FD-OLT-MIB", "associatedOnuId"),
        ("FD-OLT-MIB", "llidMac"),
        ("FD-OLT-MIB", "linkOnLineStatus"),
        ("FD-OLT-MIB", "keyChangeTimer"),
        ("FD-OLT-MIB", "llidBridgeType"),
        ("FD-OLT-MIB", "llidMacEntryLimit"),
        ("FD-OLT-MIB", "crossConnectLinkId"),
        ("FD-OLT-MIB", "llidOperation"),
        ("FD-OLT-MIB", "minGuaranteedBW"),
        ("FD-OLT-MIB", "maxAllowedBW"),
        ("FD-OLT-MIB", "delaySensitive"),
        ("FD-OLT-MIB", "maxBurstSize"),
        ("FD-OLT-MIB", "slaEnable"),
        ("FD-OLT-MIB", "dbaTokens"),
        ("FD-OLT-MIB", "schedulerMinTokens"),
        ("FD-OLT-MIB", "schedulerMaxTokens"),
        ("FD-OLT-MIB", "forceReport"),
        ("FD-OLT-MIB", "llidVlanRowStatus"),
        ("FD-OLT-MIB", "linkIDsInVlan"),
        ("FD-OLT-MIB", "netVlanId"),
        ("FD-OLT-MIB", "upstreamCos"),
        ("FD-OLT-MIB", "priSelector"),
        ("FD-OLT-MIB", "minPriValue"),
        ("FD-OLT-MIB", "maxPriValue"),
        ("FD-OLT-MIB", "transNonTosFrame"),
        ("FD-OLT-MIB", "priVlanRowStatus"),
        ("FD-OLT-MIB", "blockedLinkMac"),
        ("FD-OLT-MIB", "blockedMacOper"),
        ("FD-OLT-MIB", "dynMacOperation"),
        ("FD-OLT-MIB", "dynMacAddr"),
        ("FD-OLT-MIB", "staticMacAddr"),
        ("FD-OLT-MIB", "staticMacRowStatus"),
        ("FD-OLT-MIB", "multiMinGuanBW"),
        ("FD-OLT-MIB", "multiMaxAllowedBW"),
        ("FD-OLT-MIB", "multiDelaySensitive"),
        ("FD-OLT-MIB", "multiMaxBurstSize"))
)
if mibBuilder.loadTexts:
    oltLlidBaseManageGroup.setStatus("current")

oltLlidAdvanceManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 6)
)
oltLlidAdvanceManageGroup.setObjects(
      *(("FD-OLT-MIB", "maxLinkOamRate"),
        ("FD-OLT-MIB", "minLinkOamRate"))
)
if mibBuilder.loadTexts:
    oltLlidAdvanceManageGroup.setStatus("current")

onuP2pManageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 1, 7)
)
onuP2pManageGroup.setObjects(
      *(("FD-OLT-MIB", "onuP2pEnDis"),
        ("FD-OLT-MIB", "onuP2pPonEnDis"))
)
if mibBuilder.loadTexts:
    onuP2pManageGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fdOltCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3, 3, 20, 2, 1)
)
if mibBuilder.loadTexts:
    fdOltCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FD-OLT-MIB",
    **{"fdOlt": fdOlt,
       "oltBaseManageTable": oltBaseManageTable,
       "oltBaseManageEntry": oltBaseManageEntry,
       "oltId": oltId,
       "oltMacAddr": oltMacAddr,
       "oltWorkState": oltWorkState,
       "oltEnable": oltEnable,
       "maxPermitLLIDNumber": maxPermitLLIDNumber,
       "registeredLLIDNumber": registeredLLIDNumber,
       "accessedOnuNumber": accessedOnuNumber,
       "linkIdExhaust": linkIdExhaust,
       "onuIdExhaust": onuIdExhaust,
       "linkIdOverWrite": linkIdOverWrite,
       "onuIdOverWrite": onuIdOverWrite,
       "oltOperate": oltOperate,
       "oltUpgradeStat": oltUpgradeStat,
       "onuMgmtDefType": onuMgmtDefType,
       "oltAdvancedManage": oltAdvancedManage,
       "oltChipInfoTable": oltChipInfoTable,
       "oltChipInfoEntry": oltChipInfoEntry,
       "oltChipProCode": oltChipProCode,
       "oltChipVer": oltChipVer,
       "oltChipFirmVer": oltChipFirmVer,
       "oltChipBootVer": oltChipBootVer,
       "oltChipPersVer": oltChipPersVer,
       "oltChipApp0Ver": oltChipApp0Ver,
       "oltChipApp1Ver": oltChipApp1Ver,
       "oltChipDiagVer": oltChipDiagVer,
       "oltOamRateTable": oltOamRateTable,
       "oltOamRateEntry": oltOamRateEntry,
       "minOamRate": minOamRate,
       "maxOamRate": maxOamRate,
       "oamRspTimeout": oamRspTimeout,
       "discoveryParaTable": discoveryParaTable,
       "discoveryParaEntry": discoveryParaEntry,
       "discoverPeriod": discoverPeriod,
       "discoverWindow": discoverWindow,
       "discoverTimeoutVal": discoverTimeoutVal,
       "oltAdvancedConfigTable": oltAdvancedConfigTable,
       "oltAdvancedConfigEntry": oltAdvancedConfigEntry,
       "oltAddiVlanEthType": oltAddiVlanEthType,
       "onuUltraLongDistanceTrans": onuUltraLongDistanceTrans,
       "oltBroadCastRateCtl": oltBroadCastRateCtl,
       "oltMultiCastRateCtl": oltMultiCastRateCtl,
       "oltUnkUcCastRateCtl": oltUnkUcCastRateCtl,
       "oltBroadCastRate": oltBroadCastRate,
       "oltBridgeConfigTable": oltBridgeConfigTable,
       "oltBridgeConfigEntry": oltBridgeConfigEntry,
       "dynMacAgeTime": dynMacAgeTime,
       "downStreamResetAgeTimer": downStreamResetAgeTimer,
       "bridgedVlanNumber": bridgedVlanNumber,
       "macOverWrite": macOverWrite,
       "discardUnknownMac": discardUnknownMac,
       "forwardTagOnSimpleBridge": forwardTagOnSimpleBridge,
       "dba": dba,
       "linkLevelSizeTable": linkLevelSizeTable,
       "linkLevelSizeEntry": linkLevelSizeEntry,
       "level0Links": level0Links,
       "level1Links": level1Links,
       "level2Links": level2Links,
       "nonDbaLinks": nonDbaLinks,
       "dbaDropDownWeightTable": dbaDropDownWeightTable,
       "dbaDropDownWeightEntry": dbaDropDownWeightEntry,
       "l0DropDownWeight": l0DropDownWeight,
       "l1DropDownWeight": l1DropDownWeight,
       "l2DropDownWeight": l2DropDownWeight,
       "dbaPollRateTable": dbaPollRateTable,
       "dbaPollRateEntry": dbaPollRateEntry,
       "l0PollingRate": l0PollingRate,
       "l1PollingRate": l1PollingRate,
       "l2PollingRate": l2PollingRate,
       "aggreBandWidthTable": aggreBandWidthTable,
       "aggreBandWidthEntry": aggreBandWidthEntry,
       "directionId": directionId,
       "aggreBandWidth": aggreBandWidth,
       "aggreMaxBurstSize": aggreMaxBurstSize,
       "oltAclRuleTable": oltAclRuleTable,
       "oltAclRuleEntry": oltAclRuleEntry,
       "oltPortId": oltPortId,
       "oltAclRuleData": oltAclRuleData,
       "priCopyMapTable": priCopyMapTable,
       "priCopyMapEntry": priCopyMapEntry,
       "priCopyMapData": priCopyMapData,
       "oltIgmpProxy": oltIgmpProxy,
       "igmpProxyConfigTable": igmpProxyConfigTable,
       "igmpProxyConfigEntry": igmpProxyConfigEntry,
       "maxIgmpGroups": maxIgmpGroups,
       "robustCount": robustCount,
       "queryInterval": queryInterval,
       "queryRspTimeout": queryRspTimeout,
       "queryMaxResTime": queryMaxResTime,
       "startQueryCount": startQueryCount,
       "startupQueryInterval": startupQueryInterval,
       "lastMemberQueryCount": lastMemberQueryCount,
       "lastMemberQueryInterval": lastMemberQueryInterval,
       "lastMemberQueryResTime": lastMemberQueryResTime,
       "upstreamRetransCount": upstreamRetransCount,
       "upstreamRetransInterval": upstreamRetransInterval,
       "igmpQueues": igmpQueues,
       "igmpSlaMinGuaranteedBW": igmpSlaMinGuaranteedBW,
       "igmpSlaMaxAllowedBW": igmpSlaMaxAllowedBW,
       "igmpSlaDelaySensitive": igmpSlaDelaySensitive,
       "igmpSlaMaxBurstSize": igmpSlaMaxBurstSize,
       "igmpProxyOper": igmpProxyOper,
       "igmpGroupTable": igmpGroupTable,
       "igmpGroupEntry": igmpGroupEntry,
       "igmpGroupIndex": igmpGroupIndex,
       "igmpGroupVlan": igmpGroupVlan,
       "igmpGroupIpAddr": igmpGroupIpAddr,
       "accessUserIdentifer": accessUserIdentifer,
       "accessUserIdentiferConfigTable": accessUserIdentiferConfigTable,
       "accessUserIdentiferConfigEntry": accessUserIdentiferConfigEntry,
       "pppoePlusEnable": pppoePlusEnable,
       "dhcpOption82": dhcpOption82,
       "llid": llid,
       "llidConfigTable": llidConfigTable,
       "llidConfigEntry": llidConfigEntry,
       "linkId": linkId,
       "llidAssigned": llidAssigned,
       "associatedOnuId": associatedOnuId,
       "llidMac": llidMac,
       "linkOnLineStatus": linkOnLineStatus,
       "keyChangeTimer": keyChangeTimer,
       "llidBridgeType": llidBridgeType,
       "llidMacEntryLimit": llidMacEntryLimit,
       "crossConnectLinkId": crossConnectLinkId,
       "llidOperation": llidOperation,
       "llidAdvancedManage": llidAdvancedManage,
       "linkOamRateTable": linkOamRateTable,
       "linkOamRateEntry": linkOamRateEntry,
       "maxLinkOamRate": maxLinkOamRate,
       "minLinkOamRate": minLinkOamRate,
       "sla": sla,
       "llidSlaTable": llidSlaTable,
       "llidSlaEntry": llidSlaEntry,
       "minGuaranteedBW": minGuaranteedBW,
       "maxAllowedBW": maxAllowedBW,
       "delaySensitive": delaySensitive,
       "maxBurstSize": maxBurstSize,
       "slaEnable": slaEnable,
       "slaWeightTable": slaWeightTable,
       "slaWeightEntry": slaWeightEntry,
       "dbaTokens": dbaTokens,
       "schedulerMinTokens": schedulerMinTokens,
       "schedulerMaxTokens": schedulerMaxTokens,
       "forceReport": forceReport,
       "multicastSlaTable": multicastSlaTable,
       "multicastSlaEntry": multicastSlaEntry,
       "multiMinGuanBW": multiMinGuanBW,
       "multiMaxAllowedBW": multiMaxAllowedBW,
       "multiDelaySensitive": multiDelaySensitive,
       "multiMaxBurstSize": multiMaxBurstSize,
       "llidVlan": llidVlan,
       "llidVlanCfgTable": llidVlanCfgTable,
       "llidVlanCfgEntry": llidVlanCfgEntry,
       "llidVlanTag": llidVlanTag,
       "llidVlanRowStatus": llidVlanRowStatus,
       "vlanLlidTable": vlanLlidTable,
       "vlanLlidEntry": vlanLlidEntry,
       "vlanId": vlanId,
       "linkIDsInVlan": linkIDsInVlan,
       "priVlanTable": priVlanTable,
       "priVlanEntry": priVlanEntry,
       "netVlanId": netVlanId,
       "upstreamCos": upstreamCos,
       "priSelector": priSelector,
       "minPriValue": minPriValue,
       "maxPriValue": maxPriValue,
       "transNonTosFrame": transNonTosFrame,
       "priVlanRowStatus": priVlanRowStatus,
       "blockedLinkTable": blockedLinkTable,
       "blockedLinkEntry": blockedLinkEntry,
       "blockedLinkMac": blockedLinkMac,
       "blockedMacOper": blockedMacOper,
       "macAddr": macAddr,
       "dynamicMac": dynamicMac,
       "dynMacOperTable": dynMacOperTable,
       "dynMacOperEntry": dynMacOperEntry,
       "dynMacOperation": dynMacOperation,
       "dynMacTable": dynMacTable,
       "dynMacEntry": dynMacEntry,
       "dynMacIndex": dynMacIndex,
       "dynMacAddr": dynMacAddr,
       "staticMac": staticMac,
       "staticMacTable": staticMacTable,
       "staticMacEntry": staticMacEntry,
       "staticMacIndex": staticMacIndex,
       "staticMacAddr": staticMacAddr,
       "staticMacRowStatus": staticMacRowStatus,
       "onuP2pTable": onuP2pTable,
       "onuP2pEntry": onuP2pEntry,
       "onuP2pEnDis": onuP2pEnDis,
       "onuP2pPonEnDis": onuP2pPonEnDis,
       "fdOltConformance": fdOltConformance,
       "fdOltGroups": fdOltGroups,
       "oltBaseManageGroup": oltBaseManageGroup,
       "oltAdvanceManageGroup": oltAdvanceManageGroup,
       "oltIgmpProxyGroup": oltIgmpProxyGroup,
       "oltPPPoEPlusGroup": oltPPPoEPlusGroup,
       "oltLlidBaseManageGroup": oltLlidBaseManageGroup,
       "oltLlidAdvanceManageGroup": oltLlidAdvanceManageGroup,
       "onuP2pManageGroup": onuP2pManageGroup,
       "fdOltCompliances": fdOltCompliances,
       "fdOltCompliance": fdOltCompliance}
)
