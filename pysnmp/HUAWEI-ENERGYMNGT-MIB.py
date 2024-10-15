# SNMP MIB module (HUAWEI-ENERGYMNGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ENERGYMNGT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:39 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwEnergyMngt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157)
)
hwEnergyMngt.setRevisions(
        ("2015-05-30 00:00",
         "2014-01-23 00:00",
         "2011-07-01 00:00",
         "2011-03-14 15:30",
         "2011-03-14 00:00",
         "2011-03-10 00:00",
         "2011-02-10 00:00",
         "2010-08-06 00:00",
         "2010-08-05 00:00",
         "2010-08-03 00:00",
         "2010-07-12 00:00",
         "2010-07-07 00:00",
         "2010-06-29 00:00",
         "2010-06-23 00:00",
         "2010-06-18 00:00",
         "2010-06-17 00:00",
         "2010-06-08 00:00",
         "2010-05-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSysPowerMgnt_ObjectIdentity = ObjectIdentity
hwSysPowerMgnt = _HwSysPowerMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1)
)
_HwPowerConsumption_Type = Counter64
_HwPowerConsumption_Object = MibScalar
hwPowerConsumption = _HwPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 1),
    _HwPowerConsumption_Type()
)
hwPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPowerConsumption.setStatus("current")


class _HwPowerStatPeriod_Type(Integer32):
    """Custom type hwPowerStatPeriod based on Integer32"""
    defaultValue = 3

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
        *(("fifteenMinutes", 1),
          ("oneDay", 4),
          ("oneHour", 3),
          ("oneMonth", 6),
          ("oneWeek", 5),
          ("thirtyMinutes", 2))
    )


_HwPowerStatPeriod_Type.__name__ = "Integer32"
_HwPowerStatPeriod_Object = MibScalar
hwPowerStatPeriod = _HwPowerStatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 2),
    _HwPowerStatPeriod_Type()
)
hwPowerStatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPowerStatPeriod.setStatus("current")
_HwAveragePower_Type = Integer32
_HwAveragePower_Object = MibScalar
hwAveragePower = _HwAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 3),
    _HwAveragePower_Type()
)
hwAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAveragePower.setStatus("current")
_HwRatedPower_Type = Integer32
_HwRatedPower_Object = MibScalar
hwRatedPower = _HwRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 4),
    _HwRatedPower_Type()
)
hwRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRatedPower.setStatus("current")
_HwThresholdOfPower_Type = Integer32
_HwThresholdOfPower_Object = MibScalar
hwThresholdOfPower = _HwThresholdOfPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 5),
    _HwThresholdOfPower_Type()
)
hwThresholdOfPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwThresholdOfPower.setStatus("current")
_HwCurrentPower_Type = Integer32
_HwCurrentPower_Object = MibScalar
hwCurrentPower = _HwCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 6),
    _HwCurrentPower_Type()
)
hwCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCurrentPower.setStatus("current")


class _HwPoEType_Type(Integer32):
    """Custom type hwPoEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noPoe", 255),
          ("pd", 2),
          ("pse", 1))
    )


_HwPoEType_Type.__name__ = "Integer32"
_HwPoEType_Object = MibScalar
hwPoEType = _HwPoEType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 7),
    _HwPoEType_Type()
)
hwPoEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPoEType.setStatus("current")
_HwPSEPower_Type = Integer32
_HwPSEPower_Object = MibScalar
hwPSEPower = _HwPSEPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 1, 8),
    _HwPSEPower_Type()
)
hwPSEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPSEPower.setStatus("current")
_HwBoardPowerMngt_ObjectIdentity = ObjectIdentity
hwBoardPowerMngt = _HwBoardPowerMngt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2)
)
_HwBoardPowerMngtTable_Object = MibTable
hwBoardPowerMngtTable = _HwBoardPowerMngtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1)
)
if mibBuilder.loadTexts:
    hwBoardPowerMngtTable.setStatus("current")
_HwBoardPowerMngtEntry_Object = MibTableRow
hwBoardPowerMngtEntry = _HwBoardPowerMngtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1)
)
hwBoardPowerMngtEntry.setIndexNames(
    (0, "HUAWEI-ENERGYMNGT-MIB", "hwBoardIndex"),
)
if mibBuilder.loadTexts:
    hwBoardPowerMngtEntry.setStatus("current")
_HwBoardIndex_Type = Integer32
_HwBoardIndex_Object = MibTableColumn
hwBoardIndex = _HwBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 1),
    _HwBoardIndex_Type()
)
hwBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBoardIndex.setStatus("current")
_HwBoardType_Type = DisplayString
_HwBoardType_Object = MibTableColumn
hwBoardType = _HwBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 2),
    _HwBoardType_Type()
)
hwBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBoardType.setStatus("current")
_HwBoardName_Type = DisplayString
_HwBoardName_Object = MibTableColumn
hwBoardName = _HwBoardName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 3),
    _HwBoardName_Type()
)
hwBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBoardName.setStatus("current")
_HwBoardCurrentPower_Type = Integer32
_HwBoardCurrentPower_Object = MibTableColumn
hwBoardCurrentPower = _HwBoardCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 4),
    _HwBoardCurrentPower_Type()
)
hwBoardCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBoardCurrentPower.setStatus("current")
_HwBoardRatedPower_Type = Integer32
_HwBoardRatedPower_Object = MibTableColumn
hwBoardRatedPower = _HwBoardRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 5),
    _HwBoardRatedPower_Type()
)
hwBoardRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBoardRatedPower.setStatus("current")
_HwBoardThresholdOfPower_Type = Integer32
_HwBoardThresholdOfPower_Object = MibTableColumn
hwBoardThresholdOfPower = _HwBoardThresholdOfPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 2, 1, 1, 6),
    _HwBoardThresholdOfPower_Type()
)
hwBoardThresholdOfPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBoardThresholdOfPower.setStatus("current")
_HwEnergySavingMngt_ObjectIdentity = ObjectIdentity
hwEnergySavingMngt = _HwEnergySavingMngt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3)
)


class _HwEnergySavingMode_Type(Integer32):
    """Custom type hwEnergySavingMode based on Integer32"""
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
        *(("basic", 3),
          ("deep", 4),
          ("optimal", 5),
          ("standard", 2),
          ("userDefined", 1))
    )


_HwEnergySavingMode_Type.__name__ = "Integer32"
_HwEnergySavingMode_Object = MibScalar
hwEnergySavingMode = _HwEnergySavingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 1),
    _HwEnergySavingMode_Type()
)
hwEnergySavingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnergySavingMode.setStatus("current")
_HwEnergySavingMethodTable_Object = MibTable
hwEnergySavingMethodTable = _HwEnergySavingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2)
)
if mibBuilder.loadTexts:
    hwEnergySavingMethodTable.setStatus("current")
_HwEnergySavingMethodEntry_Object = MibTableRow
hwEnergySavingMethodEntry = _HwEnergySavingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2, 1)
)
hwEnergySavingMethodEntry.setIndexNames(
    (0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMethodIndex"),
)
if mibBuilder.loadTexts:
    hwEnergySavingMethodEntry.setStatus("current")
_HwEnergySavingMethodIndex_Type = Integer32
_HwEnergySavingMethodIndex_Object = MibTableColumn
hwEnergySavingMethodIndex = _HwEnergySavingMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2, 1, 1),
    _HwEnergySavingMethodIndex_Type()
)
hwEnergySavingMethodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergySavingMethodIndex.setStatus("current")


class _HwEnergySavingMethodEnable_Type(Integer32):
    """Custom type hwEnergySavingMethodEnable based on Integer32"""
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


_HwEnergySavingMethodEnable_Type.__name__ = "Integer32"
_HwEnergySavingMethodEnable_Object = MibTableColumn
hwEnergySavingMethodEnable = _HwEnergySavingMethodEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 2, 1, 2),
    _HwEnergySavingMethodEnable_Type()
)
hwEnergySavingMethodEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnergySavingMethodEnable.setStatus("current")
_HwEnergySavingParameterTable_Object = MibTable
hwEnergySavingParameterTable = _HwEnergySavingParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3)
)
if mibBuilder.loadTexts:
    hwEnergySavingParameterTable.setStatus("current")
_HwEnergySavingParameterEntry_Object = MibTableRow
hwEnergySavingParameterEntry = _HwEnergySavingParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3, 1)
)
hwEnergySavingParameterEntry.setIndexNames(
    (0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMethodIndex"),
    (0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingParameterIndex"),
)
if mibBuilder.loadTexts:
    hwEnergySavingParameterEntry.setStatus("current")
_HwEnergySavingParameterIndex_Type = Integer32
_HwEnergySavingParameterIndex_Object = MibTableColumn
hwEnergySavingParameterIndex = _HwEnergySavingParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3, 1, 1),
    _HwEnergySavingParameterIndex_Type()
)
hwEnergySavingParameterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergySavingParameterIndex.setStatus("current")
_HwEnergySavingParameterValue_Type = DisplayString
_HwEnergySavingParameterValue_Object = MibTableColumn
hwEnergySavingParameterValue = _HwEnergySavingParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 3, 1, 2),
    _HwEnergySavingParameterValue_Type()
)
hwEnergySavingParameterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnergySavingParameterValue.setStatus("current")
_HwEnergySavingCapabilityMngtTable_Object = MibTable
hwEnergySavingCapabilityMngtTable = _HwEnergySavingCapabilityMngtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4)
)
if mibBuilder.loadTexts:
    hwEnergySavingCapabilityMngtTable.setStatus("current")
_HwEnergySavingCapabilityMngtEntry_Object = MibTableRow
hwEnergySavingCapabilityMngtEntry = _HwEnergySavingCapabilityMngtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1)
)
hwEnergySavingCapabilityMngtEntry.setIndexNames(
    (0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingCapabilityDescIndex"),
)
if mibBuilder.loadTexts:
    hwEnergySavingCapabilityMngtEntry.setStatus("current")
_HwEnergySavingCapabilityDescIndex_Type = Integer32
_HwEnergySavingCapabilityDescIndex_Object = MibTableColumn
hwEnergySavingCapabilityDescIndex = _HwEnergySavingCapabilityDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1, 1),
    _HwEnergySavingCapabilityDescIndex_Type()
)
hwEnergySavingCapabilityDescIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergySavingCapabilityDescIndex.setStatus("current")
_HwEnergySavingCapabilityDescLanguage_Type = DisplayString
_HwEnergySavingCapabilityDescLanguage_Object = MibTableColumn
hwEnergySavingCapabilityDescLanguage = _HwEnergySavingCapabilityDescLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1, 2),
    _HwEnergySavingCapabilityDescLanguage_Type()
)
hwEnergySavingCapabilityDescLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergySavingCapabilityDescLanguage.setStatus("current")


class _HwEnergySavingCapabilityDesc_Type(OctetString):
    """Custom type hwEnergySavingCapabilityDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10240),
    )


_HwEnergySavingCapabilityDesc_Type.__name__ = "OctetString"
_HwEnergySavingCapabilityDesc_Object = MibTableColumn
hwEnergySavingCapabilityDesc = _HwEnergySavingCapabilityDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 4, 1, 3),
    _HwEnergySavingCapabilityDesc_Type()
)
hwEnergySavingCapabilityDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergySavingCapabilityDesc.setStatus("current")


class _HwEnergySavingDescReqMode_Type(Integer32):
    """Custom type hwEnergySavingDescReqMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("snmp", 1))
    )


_HwEnergySavingDescReqMode_Type.__name__ = "Integer32"
_HwEnergySavingDescReqMode_Object = MibScalar
hwEnergySavingDescReqMode = _HwEnergySavingDescReqMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 3, 5),
    _HwEnergySavingDescReqMode_Type()
)
hwEnergySavingDescReqMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergySavingDescReqMode.setStatus("current")
_HwEnergyFtpcObjects_ObjectIdentity = ObjectIdentity
hwEnergyFtpcObjects = _HwEnergyFtpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4)
)
_HwEnergyFtpcTransFileTable_Object = MibTable
hwEnergyFtpcTransFileTable = _HwEnergyFtpcTransFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1)
)
if mibBuilder.loadTexts:
    hwEnergyFtpcTransFileTable.setStatus("current")
_HwEnergyFtpcTransFileEntry_Object = MibTableRow
hwEnergyFtpcTransFileEntry = _HwEnergyFtpcTransFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1)
)
hwEnergyFtpcTransFileEntry.setIndexNames(
    (0, "HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSetName"),
)
if mibBuilder.loadTexts:
    hwEnergyFtpcTransFileEntry.setStatus("current")


class _HwEnergyFtpcSetName_Type(OctetString):
    """Custom type hwEnergyFtpcSetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwEnergyFtpcSetName_Type.__name__ = "OctetString"
_HwEnergyFtpcSetName_Object = MibTableColumn
hwEnergyFtpcSetName = _HwEnergyFtpcSetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 1),
    _HwEnergyFtpcSetName_Type()
)
hwEnergyFtpcSetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwEnergyFtpcSetName.setStatus("current")
_HwEnergyFtpcSrcAddrType_Type = InetAddressType
_HwEnergyFtpcSrcAddrType_Object = MibTableColumn
hwEnergyFtpcSrcAddrType = _HwEnergyFtpcSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 2),
    _HwEnergyFtpcSrcAddrType_Type()
)
hwEnergyFtpcSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcSrcAddrType.setStatus("current")
_HwEnergyFtpcSrcAddr_Type = InetAddress
_HwEnergyFtpcSrcAddr_Object = MibTableColumn
hwEnergyFtpcSrcAddr = _HwEnergyFtpcSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 3),
    _HwEnergyFtpcSrcAddr_Type()
)
hwEnergyFtpcSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcSrcAddr.setStatus("current")


class _HwEnergyFtpcVpnName_Type(OctetString):
    """Custom type hwEnergyFtpcVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwEnergyFtpcVpnName_Type.__name__ = "OctetString"
_HwEnergyFtpcVpnName_Object = MibTableColumn
hwEnergyFtpcVpnName = _HwEnergyFtpcVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 4),
    _HwEnergyFtpcVpnName_Type()
)
hwEnergyFtpcVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcVpnName.setStatus("current")
_HwEnergyFtpcHostAddrType_Type = InetAddressType
_HwEnergyFtpcHostAddrType_Object = MibTableColumn
hwEnergyFtpcHostAddrType = _HwEnergyFtpcHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 5),
    _HwEnergyFtpcHostAddrType_Type()
)
hwEnergyFtpcHostAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcHostAddrType.setStatus("current")
_HwEnergyFtpcHostAddr_Type = InetAddress
_HwEnergyFtpcHostAddr_Object = MibTableColumn
hwEnergyFtpcHostAddr = _HwEnergyFtpcHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 6),
    _HwEnergyFtpcHostAddr_Type()
)
hwEnergyFtpcHostAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcHostAddr.setStatus("current")


class _HwEnergyFtpcServerPort_Type(Integer32):
    """Custom type hwEnergyFtpcServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(1025, 55535),
    )


_HwEnergyFtpcServerPort_Type.__name__ = "Integer32"
_HwEnergyFtpcServerPort_Object = MibTableColumn
hwEnergyFtpcServerPort = _HwEnergyFtpcServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 7),
    _HwEnergyFtpcServerPort_Type()
)
hwEnergyFtpcServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcServerPort.setStatus("current")


class _HwEnergyFtpcUserName_Type(OctetString):
    """Custom type hwEnergyFtpcUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 85),
    )


_HwEnergyFtpcUserName_Type.__name__ = "OctetString"
_HwEnergyFtpcUserName_Object = MibTableColumn
hwEnergyFtpcUserName = _HwEnergyFtpcUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 8),
    _HwEnergyFtpcUserName_Type()
)
hwEnergyFtpcUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcUserName.setStatus("current")


class _HwEnergyFtpcPassword_Type(OctetString):
    """Custom type hwEnergyFtpcPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_HwEnergyFtpcPassword_Type.__name__ = "OctetString"
_HwEnergyFtpcPassword_Object = MibTableColumn
hwEnergyFtpcPassword = _HwEnergyFtpcPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 9),
    _HwEnergyFtpcPassword_Type()
)
hwEnergyFtpcPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcPassword.setStatus("current")


class _HwEnergyFtpcDirectory_Type(OctetString):
    """Custom type hwEnergyFtpcDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwEnergyFtpcDirectory_Type.__name__ = "OctetString"
_HwEnergyFtpcDirectory_Object = MibTableColumn
hwEnergyFtpcDirectory = _HwEnergyFtpcDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 10),
    _HwEnergyFtpcDirectory_Type()
)
hwEnergyFtpcDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcDirectory.setStatus("current")


class _HwEnergyFtpcSrcIfName_Type(OctetString):
    """Custom type hwEnergyFtpcSrcIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwEnergyFtpcSrcIfName_Type.__name__ = "OctetString"
_HwEnergyFtpcSrcIfName_Object = MibTableColumn
hwEnergyFtpcSrcIfName = _HwEnergyFtpcSrcIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 11),
    _HwEnergyFtpcSrcIfName_Type()
)
hwEnergyFtpcSrcIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcSrcIfName.setStatus("current")
_HwEnergyFtpcTransCfgRowStatus_Type = RowStatus
_HwEnergyFtpcTransCfgRowStatus_Object = MibTableColumn
hwEnergyFtpcTransCfgRowStatus = _HwEnergyFtpcTransCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 12),
    _HwEnergyFtpcTransCfgRowStatus_Type()
)
hwEnergyFtpcTransCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwEnergyFtpcTransCfgRowStatus.setStatus("current")


class _HwEnergyFtpcAction_Type(Integer32):
    """Custom type hwEnergyFtpcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_HwEnergyFtpcAction_Type.__name__ = "Integer32"
_HwEnergyFtpcAction_Object = MibTableColumn
hwEnergyFtpcAction = _HwEnergyFtpcAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 13),
    _HwEnergyFtpcAction_Type()
)
hwEnergyFtpcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnergyFtpcAction.setStatus("current")


class _HwEnergyFtpcTransMode_Type(Integer32):
    """Custom type hwEnergyFtpcTransMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )


_HwEnergyFtpcTransMode_Type.__name__ = "Integer32"
_HwEnergyFtpcTransMode_Object = MibTableColumn
hwEnergyFtpcTransMode = _HwEnergyFtpcTransMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 14),
    _HwEnergyFtpcTransMode_Type()
)
hwEnergyFtpcTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnergyFtpcTransMode.setStatus("current")


class _HwEnergyFtpOperStatus_Type(Integer32):
    """Custom type hwEnergyFtpOperStatus based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("opAbort", 15),
          ("opAuthFail", 13),
          ("opDeviceBusy", 8),
          ("opDeviceError", 9),
          ("opFileChecksumError", 12),
          ("opFileOpenError", 10),
          ("opFileTransferError", 11),
          ("opInProgress", 1),
          ("opInvalid", 3),
          ("opInvalidDestName", 6),
          ("opInvalidProtocol", 4),
          ("opInvalidServerAddress", 7),
          ("opInvalidSourceAddress", 16),
          ("opInvalidSourceInterface", 17),
          ("opInvalidSourceName", 5),
          ("opSuccess", 2),
          ("opUnknownFailure", 14))
    )


_HwEnergyFtpOperStatus_Type.__name__ = "Integer32"
_HwEnergyFtpOperStatus_Object = MibTableColumn
hwEnergyFtpOperStatus = _HwEnergyFtpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 4, 1, 1, 15),
    _HwEnergyFtpOperStatus_Type()
)
hwEnergyFtpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnergyFtpOperStatus.setStatus("current")
_HwEnergyConformance_ObjectIdentity = ObjectIdentity
hwEnergyConformance = _HwEnergyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6)
)
_HwEnergyCompliances_ObjectIdentity = ObjectIdentity
hwEnergyCompliances = _HwEnergyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 1)
)
_HwEnergyGroups_ObjectIdentity = ObjectIdentity
hwEnergyGroups = _HwEnergyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2)
)
_HwEnergyTrapObjects_ObjectIdentity = ObjectIdentity
hwEnergyTrapObjects = _HwEnergyTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 10)
)
_HwEnergyDevId_Type = Integer32
_HwEnergyDevId_Object = MibScalar
hwEnergyDevId = _HwEnergyDevId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 10, 1),
    _HwEnergyDevId_Type()
)
hwEnergyDevId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEnergyDevId.setStatus("current")
_HwEnergyNotification_ObjectIdentity = ObjectIdentity
hwEnergyNotification = _HwEnergyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 11)
)

# Managed Objects groups

hwEnergyFtpcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 1)
)
hwEnergyFtpcGroup.setObjects(
      *(("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSrcAddrType"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSrcAddr"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcVpnName"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcHostAddrType"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcHostAddr"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcServerPort"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcUserName"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcPassword"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcDirectory"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcSrcIfName"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyFtpcTransCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwEnergyFtpcGroup.setStatus("current")

hwSysPowerMgntGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 2)
)
hwSysPowerMgntGroup.setObjects(
      *(("HUAWEI-ENERGYMNGT-MIB", "hwThresholdOfPower"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwPowerConsumption"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwPowerStatPeriod"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwAveragePower"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwRatedPower"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwCurrentPower"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwPSEPower"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwPoEType"))
)
if mibBuilder.loadTexts:
    hwSysPowerMgntGroup.setStatus("current")

hwEnergySavingMngtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 3)
)
hwEnergySavingMngtGroup.setObjects(
      *(("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMode"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingMethodIndex"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingParameterIndex"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingCapabilityDescIndex"),
        ("HUAWEI-ENERGYMNGT-MIB", "hwEnergySavingDescReqMode"))
)
if mibBuilder.loadTexts:
    hwEnergySavingMngtGroup.setStatus("current")


# Notification objects

hwEnergyDevChangeToSleep = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 11, 1)
)
hwEnergyDevChangeToSleep.setObjects(
    ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyDevId")
)
if mibBuilder.loadTexts:
    hwEnergyDevChangeToSleep.setStatus(
        "current"
    )


# Notifications groups

hwEnergyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 2, 4)
)
hwEnergyNotificationGroup.setObjects(
    ("HUAWEI-ENERGYMNGT-MIB", "hwEnergyDevChangeToSleep")
)
if mibBuilder.loadTexts:
    hwEnergyNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEnergyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 157, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwEnergyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ENERGYMNGT-MIB",
    **{"hwEnergyMngt": hwEnergyMngt,
       "hwSysPowerMgnt": hwSysPowerMgnt,
       "hwPowerConsumption": hwPowerConsumption,
       "hwPowerStatPeriod": hwPowerStatPeriod,
       "hwAveragePower": hwAveragePower,
       "hwRatedPower": hwRatedPower,
       "hwThresholdOfPower": hwThresholdOfPower,
       "hwCurrentPower": hwCurrentPower,
       "hwPoEType": hwPoEType,
       "hwPSEPower": hwPSEPower,
       "hwBoardPowerMngt": hwBoardPowerMngt,
       "hwBoardPowerMngtTable": hwBoardPowerMngtTable,
       "hwBoardPowerMngtEntry": hwBoardPowerMngtEntry,
       "hwBoardIndex": hwBoardIndex,
       "hwBoardType": hwBoardType,
       "hwBoardName": hwBoardName,
       "hwBoardCurrentPower": hwBoardCurrentPower,
       "hwBoardRatedPower": hwBoardRatedPower,
       "hwBoardThresholdOfPower": hwBoardThresholdOfPower,
       "hwEnergySavingMngt": hwEnergySavingMngt,
       "hwEnergySavingMode": hwEnergySavingMode,
       "hwEnergySavingMethodTable": hwEnergySavingMethodTable,
       "hwEnergySavingMethodEntry": hwEnergySavingMethodEntry,
       "hwEnergySavingMethodIndex": hwEnergySavingMethodIndex,
       "hwEnergySavingMethodEnable": hwEnergySavingMethodEnable,
       "hwEnergySavingParameterTable": hwEnergySavingParameterTable,
       "hwEnergySavingParameterEntry": hwEnergySavingParameterEntry,
       "hwEnergySavingParameterIndex": hwEnergySavingParameterIndex,
       "hwEnergySavingParameterValue": hwEnergySavingParameterValue,
       "hwEnergySavingCapabilityMngtTable": hwEnergySavingCapabilityMngtTable,
       "hwEnergySavingCapabilityMngtEntry": hwEnergySavingCapabilityMngtEntry,
       "hwEnergySavingCapabilityDescIndex": hwEnergySavingCapabilityDescIndex,
       "hwEnergySavingCapabilityDescLanguage": hwEnergySavingCapabilityDescLanguage,
       "hwEnergySavingCapabilityDesc": hwEnergySavingCapabilityDesc,
       "hwEnergySavingDescReqMode": hwEnergySavingDescReqMode,
       "hwEnergyFtpcObjects": hwEnergyFtpcObjects,
       "hwEnergyFtpcTransFileTable": hwEnergyFtpcTransFileTable,
       "hwEnergyFtpcTransFileEntry": hwEnergyFtpcTransFileEntry,
       "hwEnergyFtpcSetName": hwEnergyFtpcSetName,
       "hwEnergyFtpcSrcAddrType": hwEnergyFtpcSrcAddrType,
       "hwEnergyFtpcSrcAddr": hwEnergyFtpcSrcAddr,
       "hwEnergyFtpcVpnName": hwEnergyFtpcVpnName,
       "hwEnergyFtpcHostAddrType": hwEnergyFtpcHostAddrType,
       "hwEnergyFtpcHostAddr": hwEnergyFtpcHostAddr,
       "hwEnergyFtpcServerPort": hwEnergyFtpcServerPort,
       "hwEnergyFtpcUserName": hwEnergyFtpcUserName,
       "hwEnergyFtpcPassword": hwEnergyFtpcPassword,
       "hwEnergyFtpcDirectory": hwEnergyFtpcDirectory,
       "hwEnergyFtpcSrcIfName": hwEnergyFtpcSrcIfName,
       "hwEnergyFtpcTransCfgRowStatus": hwEnergyFtpcTransCfgRowStatus,
       "hwEnergyFtpcAction": hwEnergyFtpcAction,
       "hwEnergyFtpcTransMode": hwEnergyFtpcTransMode,
       "hwEnergyFtpOperStatus": hwEnergyFtpOperStatus,
       "hwEnergyConformance": hwEnergyConformance,
       "hwEnergyCompliances": hwEnergyCompliances,
       "hwEnergyCompliance": hwEnergyCompliance,
       "hwEnergyGroups": hwEnergyGroups,
       "hwEnergyFtpcGroup": hwEnergyFtpcGroup,
       "hwSysPowerMgntGroup": hwSysPowerMgntGroup,
       "hwEnergySavingMngtGroup": hwEnergySavingMngtGroup,
       "hwEnergyNotificationGroup": hwEnergyNotificationGroup,
       "hwEnergyTrapObjects": hwEnergyTrapObjects,
       "hwEnergyDevId": hwEnergyDevId,
       "hwEnergyNotification": hwEnergyNotification,
       "hwEnergyDevChangeToSleep": hwEnergyDevChangeToSleep}
)
