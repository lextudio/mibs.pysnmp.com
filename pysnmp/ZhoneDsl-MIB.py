# SNMP MIB module (ZhoneDsl-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZhoneDsl-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:19 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "VariablePointer")

(zhoneDsl,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneDsl",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneDsl_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 3)
)
zhoneDsl_MIB.setRevisions(
        ("2000-04-26 17:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneDslLineTable_Object = MibTable
zhoneDslLineTable = _ZhoneDslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneDslLineTable.setStatus("current")
_ZhoneDslLineEntry_Object = MibTableRow
zhoneDslLineEntry = _ZhoneDslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1)
)
zhoneDslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneDslLineEntry.setStatus("current")


class _ZhoneDslLineType_Type(Integer32):
    """Custom type zhoneDslLineType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              96)
        )
    )
    namedValues = NamedValues(
        *(("hdsl", 1),
          ("hdsl2", 2),
          ("sdsl", 96),
          ("shdsl", 3))
    )


_ZhoneDslLineType_Type.__name__ = "Integer32"
_ZhoneDslLineType_Object = MibTableColumn
zhoneDslLineType = _ZhoneDslLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 1),
    _ZhoneDslLineType_Type()
)
zhoneDslLineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslLineType.setStatus("current")


class _ZhoneDslLineCapabilities_Type(Bits):
    """Custom type zhoneDslLineCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hdsl", 1),
          ("hdsl2", 2),
          ("sdsl", 8),
          ("shdsl", 4))
    )

_ZhoneDslLineCapabilities_Type.__name__ = "Bits"
_ZhoneDslLineCapabilities_Object = MibTableColumn
zhoneDslLineCapabilities = _ZhoneDslLineCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 2),
    _ZhoneDslLineCapabilities_Type()
)
zhoneDslLineCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineCapabilities.setStatus("current")


class _ZhoneDslLineStatus_Type(Integer32):
    """Custom type zhoneDslLineStatus based on Integer32"""
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
        *(("activated", 3),
          ("down", 1),
          ("downloading", 2),
          ("training", 4),
          ("up", 5))
    )


_ZhoneDslLineStatus_Type.__name__ = "Integer32"
_ZhoneDslLineStatus_Object = MibTableColumn
zhoneDslLineStatus = _ZhoneDslLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 3),
    _ZhoneDslLineStatus_Type()
)
zhoneDslLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslLineStatus.setStatus("current")
_ZhoneDslUpLineRate_Type = Gauge32
_ZhoneDslUpLineRate_Object = MibTableColumn
zhoneDslUpLineRate = _ZhoneDslUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 4),
    _ZhoneDslUpLineRate_Type()
)
zhoneDslUpLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslUpLineRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslUpLineRate.setUnits("bps")
_ZhoneDslDownLineRate_Type = Gauge32
_ZhoneDslDownLineRate_Object = MibTableColumn
zhoneDslDownLineRate = _ZhoneDslDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 5),
    _ZhoneDslDownLineRate_Type()
)
zhoneDslDownLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslDownLineRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslDownLineRate.setUnits("bps")
_ZhoneDslLineConfigProfile_Type = ZhoneAdminString
_ZhoneDslLineConfigProfile_Object = MibTableColumn
zhoneDslLineConfigProfile = _ZhoneDslLineConfigProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 6),
    _ZhoneDslLineConfigProfile_Type()
)
zhoneDslLineConfigProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslLineConfigProfile.setStatus("current")
_ZhoneDslLineAlarmProfile_Type = ZhoneAdminString
_ZhoneDslLineAlarmProfile_Object = MibTableColumn
zhoneDslLineAlarmProfile = _ZhoneDslLineAlarmProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 7),
    _ZhoneDslLineAlarmProfile_Type()
)
zhoneDslLineAlarmProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslLineAlarmProfile.setStatus("current")
_ZhoneDslLineRowStatus_Type = ZhoneRowStatus
_ZhoneDslLineRowStatus_Object = MibTableColumn
zhoneDslLineRowStatus = _ZhoneDslLineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 1, 1, 8),
    _ZhoneDslLineRowStatus_Type()
)
zhoneDslLineRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslLineRowStatus.setStatus("current")
_ZhoneHdsl2ConfigProfileTable_Object = MibTable
zhoneHdsl2ConfigProfileTable = _ZhoneHdsl2ConfigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3)
)
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigProfileTable.setStatus("current")
_ZhoneHdsl2ConfigProfileEntry_Object = MibTableRow
zhoneHdsl2ConfigProfileEntry = _ZhoneHdsl2ConfigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1)
)
zhoneHdsl2ConfigProfileEntry.setIndexNames(
    (1, "ZhoneDsl-MIB", "zhoneHdsl2ConfigProfileName"),
)
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigProfileEntry.setStatus("current")
_ZhoneHdsl2ConfigProfileName_Type = ZhoneAdminString
_ZhoneHdsl2ConfigProfileName_Object = MibTableColumn
zhoneHdsl2ConfigProfileName = _ZhoneHdsl2ConfigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 1),
    _ZhoneHdsl2ConfigProfileName_Type()
)
zhoneHdsl2ConfigProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigProfileName.setStatus("current")


class _ZhoneHdsl2ConfigUnitMode_Type(Integer32):
    """Custom type zhoneHdsl2ConfigUnitMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("co", 1),
          ("cpe", 2))
    )


_ZhoneHdsl2ConfigUnitMode_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigUnitMode_Object = MibTableColumn
zhoneHdsl2ConfigUnitMode = _ZhoneHdsl2ConfigUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 2),
    _ZhoneHdsl2ConfigUnitMode_Type()
)
zhoneHdsl2ConfigUnitMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigUnitMode.setStatus("current")


class _ZhoneHdsl2ConfigTransmitPowerbackoffMode_Type(Integer32):
    """Custom type zhoneHdsl2ConfigTransmitPowerbackoffMode based on Integer32"""
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
        *(("backoff-disable", 1),
          ("backoff-enable", 2),
          ("no-change-backoff", 3))
    )


_ZhoneHdsl2ConfigTransmitPowerbackoffMode_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigTransmitPowerbackoffMode_Object = MibTableColumn
zhoneHdsl2ConfigTransmitPowerbackoffMode = _ZhoneHdsl2ConfigTransmitPowerbackoffMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 3),
    _ZhoneHdsl2ConfigTransmitPowerbackoffMode_Type()
)
zhoneHdsl2ConfigTransmitPowerbackoffMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigTransmitPowerbackoffMode.setStatus("current")


class _ZhoneHdsl2ConfigDecoderCoeffA_Type(Integer32):
    """Custom type zhoneHdsl2ConfigDecoderCoeffA based on Integer32"""
    defaultBinValue = 970752


_ZhoneHdsl2ConfigDecoderCoeffA_Object = MibTableColumn
zhoneHdsl2ConfigDecoderCoeffA = _ZhoneHdsl2ConfigDecoderCoeffA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 4),
    _ZhoneHdsl2ConfigDecoderCoeffA_Type()
)
zhoneHdsl2ConfigDecoderCoeffA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigDecoderCoeffA.setStatus("current")


class _ZhoneHdsl2ConfigDecoderCoeffB_Type(Integer32):
    """Custom type zhoneHdsl2ConfigDecoderCoeffB based on Integer32"""
    defaultBinValue = 970752


_ZhoneHdsl2ConfigDecoderCoeffB_Object = MibTableColumn
zhoneHdsl2ConfigDecoderCoeffB = _ZhoneHdsl2ConfigDecoderCoeffB_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 5),
    _ZhoneHdsl2ConfigDecoderCoeffB_Type()
)
zhoneHdsl2ConfigDecoderCoeffB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigDecoderCoeffB.setStatus("current")


class _ZhoneHdsl2ConfigFrameSyncWord_Type(Integer32):
    """Custom type zhoneHdsl2ConfigFrameSyncWord based on Integer32"""
    defaultBinValue = 45


_ZhoneHdsl2ConfigFrameSyncWord_Object = MibTableColumn
zhoneHdsl2ConfigFrameSyncWord = _ZhoneHdsl2ConfigFrameSyncWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 6),
    _ZhoneHdsl2ConfigFrameSyncWord_Type()
)
zhoneHdsl2ConfigFrameSyncWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigFrameSyncWord.setStatus("current")


class _ZhoneHdsl2ConfigStuffBits_Type(Integer32):
    """Custom type zhoneHdsl2ConfigStuffBits based on Integer32"""
    defaultBinValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZhoneHdsl2ConfigStuffBits_Type.__name__ = "Integer32"
_ZhoneHdsl2ConfigStuffBits_Object = MibTableColumn
zhoneHdsl2ConfigStuffBits = _ZhoneHdsl2ConfigStuffBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 7),
    _ZhoneHdsl2ConfigStuffBits_Type()
)
zhoneHdsl2ConfigStuffBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigStuffBits.setStatus("current")
_ZhoneHdsl2ConfigRowStatus_Type = ZhoneRowStatus
_ZhoneHdsl2ConfigRowStatus_Object = MibTableColumn
zhoneHdsl2ConfigRowStatus = _ZhoneHdsl2ConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 3, 1, 8),
    _ZhoneHdsl2ConfigRowStatus_Type()
)
zhoneHdsl2ConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneHdsl2ConfigRowStatus.setStatus("current")
_ZhoneHdsl2StatusTable_Object = MibTable
zhoneHdsl2StatusTable = _ZhoneHdsl2StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4)
)
if mibBuilder.loadTexts:
    zhoneHdsl2StatusTable.setStatus("current")
_ZhoneHdsl2StatusEntry_Object = MibTableRow
zhoneHdsl2StatusEntry = _ZhoneHdsl2StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    zhoneHdsl2StatusEntry.setStatus("current")


class _ZhoneHdsl2DriftAlarm_Type(Integer32):
    """Custom type zhoneHdsl2DriftAlarm based on Integer32"""
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
        *(("no-drift-alarm", 4),
          ("not-applicable", 5),
          ("rx-clk-alarm", 1),
          ("tx-clk-alarm", 2),
          ("tx-rx-clk-alarm", 3))
    )


_ZhoneHdsl2DriftAlarm_Type.__name__ = "Integer32"
_ZhoneHdsl2DriftAlarm_Object = MibTableColumn
zhoneHdsl2DriftAlarm = _ZhoneHdsl2DriftAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 1),
    _ZhoneHdsl2DriftAlarm_Type()
)
zhoneHdsl2DriftAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2DriftAlarm.setStatus("current")


class _ZhoneHdsl2FramerIBStatus_Type(OctetString):
    """Custom type zhoneHdsl2FramerIBStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ZhoneHdsl2FramerIBStatus_Type.__name__ = "OctetString"
_ZhoneHdsl2FramerIBStatus_Object = MibTableColumn
zhoneHdsl2FramerIBStatus = _ZhoneHdsl2FramerIBStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 2),
    _ZhoneHdsl2FramerIBStatus_Type()
)
zhoneHdsl2FramerIBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2FramerIBStatus.setStatus("current")
_ZhoneHdsl2LocalPSDMaskStatus_Type = Integer32
_ZhoneHdsl2LocalPSDMaskStatus_Object = MibTableColumn
zhoneHdsl2LocalPSDMaskStatus = _ZhoneHdsl2LocalPSDMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 3),
    _ZhoneHdsl2LocalPSDMaskStatus_Type()
)
zhoneHdsl2LocalPSDMaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2LocalPSDMaskStatus.setStatus("current")
_ZhoneHdsl2LoopAttenuation_Type = Integer32
_ZhoneHdsl2LoopAttenuation_Object = MibTableColumn
zhoneHdsl2LoopAttenuation = _ZhoneHdsl2LoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 4),
    _ZhoneHdsl2LoopAttenuation_Type()
)
zhoneHdsl2LoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2LoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    zhoneHdsl2LoopAttenuation.setUnits("tenth DB")


class _ZhoneHdsl2LossWordStatus_Type(Integer32):
    """Custom type zhoneHdsl2LossWordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lossw-defect", 2),
          ("no-lossw-defect", 1))
    )


_ZhoneHdsl2LossWordStatus_Type.__name__ = "Integer32"
_ZhoneHdsl2LossWordStatus_Object = MibTableColumn
zhoneHdsl2LossWordStatus = _ZhoneHdsl2LossWordStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 5),
    _ZhoneHdsl2LossWordStatus_Type()
)
zhoneHdsl2LossWordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2LossWordStatus.setStatus("current")
_ZhoneHdsl2RmtPSDMaskStatus_Type = Integer32
_ZhoneHdsl2RmtPSDMaskStatus_Object = MibTableColumn
zhoneHdsl2RmtPSDMaskStatus = _ZhoneHdsl2RmtPSDMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 6),
    _ZhoneHdsl2RmtPSDMaskStatus_Type()
)
zhoneHdsl2RmtPSDMaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtPSDMaskStatus.setStatus("current")
_ZhoneHdsl2RmtCountryCode_Type = Integer32
_ZhoneHdsl2RmtCountryCode_Object = MibTableColumn
zhoneHdsl2RmtCountryCode = _ZhoneHdsl2RmtCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 7),
    _ZhoneHdsl2RmtCountryCode_Type()
)
zhoneHdsl2RmtCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtCountryCode.setStatus("current")
_ZhoneHdsl2RmtVersion_Type = Integer32
_ZhoneHdsl2RmtVersion_Object = MibTableColumn
zhoneHdsl2RmtVersion = _ZhoneHdsl2RmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 8),
    _ZhoneHdsl2RmtVersion_Type()
)
zhoneHdsl2RmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtVersion.setStatus("current")
_ZhoneHdsl2RmtProviderCode_Type = Integer32
_ZhoneHdsl2RmtProviderCode_Object = MibTableColumn
zhoneHdsl2RmtProviderCode = _ZhoneHdsl2RmtProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 9),
    _ZhoneHdsl2RmtProviderCode_Type()
)
zhoneHdsl2RmtProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtProviderCode.setStatus("current")


class _ZhoneHdsl2RmtVendorData_Type(OctetString):
    """Custom type zhoneHdsl2RmtVendorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ZhoneHdsl2RmtVendorData_Type.__name__ = "OctetString"
_ZhoneHdsl2RmtVendorData_Object = MibTableColumn
zhoneHdsl2RmtVendorData = _ZhoneHdsl2RmtVendorData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 10),
    _ZhoneHdsl2RmtVendorData_Type()
)
zhoneHdsl2RmtVendorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtVendorData.setStatus("current")
_ZhoneHdsl2RmtTxEncoderA_Type = Integer32
_ZhoneHdsl2RmtTxEncoderA_Object = MibTableColumn
zhoneHdsl2RmtTxEncoderA = _ZhoneHdsl2RmtTxEncoderA_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 11),
    _ZhoneHdsl2RmtTxEncoderA_Type()
)
zhoneHdsl2RmtTxEncoderA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtTxEncoderA.setStatus("current")
_ZhoneHdsl2RmtTxEncoderB_Type = Integer32
_ZhoneHdsl2RmtTxEncoderB_Object = MibTableColumn
zhoneHdsl2RmtTxEncoderB = _ZhoneHdsl2RmtTxEncoderB_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 12),
    _ZhoneHdsl2RmtTxEncoderB_Type()
)
zhoneHdsl2RmtTxEncoderB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2RmtTxEncoderB.setStatus("current")


class _ZhoneHdsl2TipRingStatus_Type(Integer32):
    """Custom type zhoneHdsl2TipRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reverse", 2))
    )


_ZhoneHdsl2TipRingStatus_Type.__name__ = "Integer32"
_ZhoneHdsl2TipRingStatus_Object = MibTableColumn
zhoneHdsl2TipRingStatus = _ZhoneHdsl2TipRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 13),
    _ZhoneHdsl2TipRingStatus_Type()
)
zhoneHdsl2TipRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2TipRingStatus.setStatus("current")
_ZhoneHdsl2FrameSyncWord_Type = Integer32
_ZhoneHdsl2FrameSyncWord_Object = MibTableColumn
zhoneHdsl2FrameSyncWord = _ZhoneHdsl2FrameSyncWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 14),
    _ZhoneHdsl2FrameSyncWord_Type()
)
zhoneHdsl2FrameSyncWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2FrameSyncWord.setStatus("current")
_ZhoneHdsl2StuffBits_Type = Integer32
_ZhoneHdsl2StuffBits_Object = MibTableColumn
zhoneHdsl2StuffBits = _ZhoneHdsl2StuffBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 4, 1, 15),
    _ZhoneHdsl2StuffBits_Type()
)
zhoneHdsl2StuffBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneHdsl2StuffBits.setStatus("current")
_ZhoneDslPerfDataTable_Object = MibTable
zhoneDslPerfDataTable = _ZhoneDslPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5)
)
if mibBuilder.loadTexts:
    zhoneDslPerfDataTable.setStatus("current")
_ZhoneDslPerfDataEntry_Object = MibTableRow
zhoneDslPerfDataEntry = _ZhoneDslPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1)
)
if mibBuilder.loadTexts:
    zhoneDslPerfDataEntry.setStatus("current")
_ZhoneDslPerfLofs_Type = Counter32
_ZhoneDslPerfLofs_Object = MibTableColumn
zhoneDslPerfLofs = _ZhoneDslPerfLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 1),
    _ZhoneDslPerfLofs_Type()
)
zhoneDslPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLofs.setStatus("current")
_ZhoneDslPerfLoss_Type = Counter32
_ZhoneDslPerfLoss_Object = MibTableColumn
zhoneDslPerfLoss = _ZhoneDslPerfLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 2),
    _ZhoneDslPerfLoss_Type()
)
zhoneDslPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLoss.setStatus("current")
_ZhoneDslPerfLols_Type = Counter32
_ZhoneDslPerfLols_Object = MibTableColumn
zhoneDslPerfLols = _ZhoneDslPerfLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 3),
    _ZhoneDslPerfLols_Type()
)
zhoneDslPerfLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfLols.setStatus("current")
_ZhoneDslPerfInits_Type = Counter32
_ZhoneDslPerfInits_Object = MibTableColumn
zhoneDslPerfInits = _ZhoneDslPerfInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 4),
    _ZhoneDslPerfInits_Type()
)
zhoneDslPerfInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfInits.setStatus("current")
_ZhoneDslPerfCur15MinTimeElapsed_Type = Gauge32
_ZhoneDslPerfCur15MinTimeElapsed_Object = MibTableColumn
zhoneDslPerfCur15MinTimeElapsed = _ZhoneDslPerfCur15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 5),
    _ZhoneDslPerfCur15MinTimeElapsed_Type()
)
zhoneDslPerfCur15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinTimeElapsed.setUnits("seconds")
_ZhoneDslPerfCur15MinLofs_Type = Gauge32
_ZhoneDslPerfCur15MinLofs_Object = MibTableColumn
zhoneDslPerfCur15MinLofs = _ZhoneDslPerfCur15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 6),
    _ZhoneDslPerfCur15MinLofs_Type()
)
zhoneDslPerfCur15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinLofs.setUnits("seconds")
_ZhoneDslPerfCur15MinLoss_Type = Gauge32
_ZhoneDslPerfCur15MinLoss_Object = MibTableColumn
zhoneDslPerfCur15MinLoss = _ZhoneDslPerfCur15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 7),
    _ZhoneDslPerfCur15MinLoss_Type()
)
zhoneDslPerfCur15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinLoss.setUnits("seconds")
_ZhoneDslPerfCur15MinLols_Type = Gauge32
_ZhoneDslPerfCur15MinLols_Object = MibTableColumn
zhoneDslPerfCur15MinLols = _ZhoneDslPerfCur15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 8),
    _ZhoneDslPerfCur15MinLols_Type()
)
zhoneDslPerfCur15MinLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinLols.setUnits("seconds")
_ZhoneDslPerfCur15MinInits_Type = Counter32
_ZhoneDslPerfCur15MinInits_Object = MibTableColumn
zhoneDslPerfCur15MinInits = _ZhoneDslPerfCur15MinInits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 5, 1, 9),
    _ZhoneDslPerfCur15MinInits_Type()
)
zhoneDslPerfCur15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDslPerfCur15MinInits.setStatus("current")
_ZhoneDslAlarmProfileTable_Object = MibTable
zhoneDslAlarmProfileTable = _ZhoneDslAlarmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6)
)
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileTable.setStatus("current")
_ZhoneDslAlarmProfileEntry_Object = MibTableRow
zhoneDslAlarmProfileEntry = _ZhoneDslAlarmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1)
)
zhoneDslAlarmProfileEntry.setIndexNames(
    (1, "ZhoneDsl-MIB", "zhoneDslAlarmProfileName"),
)
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileEntry.setStatus("current")
_ZhoneDslAlarmProfileName_Type = ZhoneAdminString
_ZhoneDslAlarmProfileName_Object = MibTableColumn
zhoneDslAlarmProfileName = _ZhoneDslAlarmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 1),
    _ZhoneDslAlarmProfileName_Type()
)
zhoneDslAlarmProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileName.setStatus("current")


class _ZhoneDslThreshold15MinLoss_Type(Integer32):
    """Custom type zhoneDslThreshold15MinLoss based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslThreshold15MinLoss_Type.__name__ = "Integer32"
_ZhoneDslThreshold15MinLoss_Object = MibTableColumn
zhoneDslThreshold15MinLoss = _ZhoneDslThreshold15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 2),
    _ZhoneDslThreshold15MinLoss_Type()
)
zhoneDslThreshold15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLoss.setUnits("seconds")


class _ZhoneDslThreshold15MinLols_Type(Integer32):
    """Custom type zhoneDslThreshold15MinLols based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslThreshold15MinLols_Type.__name__ = "Integer32"
_ZhoneDslThreshold15MinLols_Object = MibTableColumn
zhoneDslThreshold15MinLols = _ZhoneDslThreshold15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 3),
    _ZhoneDslThreshold15MinLols_Type()
)
zhoneDslThreshold15MinLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLols.setUnits("seconds")


class _ZhoneDslThreshold15MinLofs_Type(Integer32):
    """Custom type zhoneDslThreshold15MinLofs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZhoneDslThreshold15MinLofs_Type.__name__ = "Integer32"
_ZhoneDslThreshold15MinLofs_Object = MibTableColumn
zhoneDslThreshold15MinLofs = _ZhoneDslThreshold15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 4),
    _ZhoneDslThreshold15MinLofs_Type()
)
zhoneDslThreshold15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDslThreshold15MinLofs.setUnits("seconds")
_ZhoneDslAlarmProfileRowStatus_Type = ZhoneAdminString
_ZhoneDslAlarmProfileRowStatus_Object = MibTableColumn
zhoneDslAlarmProfileRowStatus = _ZhoneDslAlarmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 4, 6, 1, 5),
    _ZhoneDslAlarmProfileRowStatus_Type()
)
zhoneDslAlarmProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDslAlarmProfileRowStatus.setStatus("current")
ifIndex.registerAugmentions(
    ("ZhoneDsl-MIB",
     "zhoneHdsl2StatusEntry")
)
zhoneHdsl2StatusEntry.setIndexNames(*ifIndex.getIndexNames())
zhoneDslLineEntry.registerAugmentions(
    ("ZhoneDsl-MIB",
     "zhoneDslPerfDataEntry")
)
zhoneDslPerfDataEntry.setIndexNames(*zhoneDslLineEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZhoneDsl-MIB",
    **{"zhoneDslLineTable": zhoneDslLineTable,
       "zhoneDslLineEntry": zhoneDslLineEntry,
       "zhoneDslLineType": zhoneDslLineType,
       "zhoneDslLineCapabilities": zhoneDslLineCapabilities,
       "zhoneDslLineStatus": zhoneDslLineStatus,
       "zhoneDslUpLineRate": zhoneDslUpLineRate,
       "zhoneDslDownLineRate": zhoneDslDownLineRate,
       "zhoneDslLineConfigProfile": zhoneDslLineConfigProfile,
       "zhoneDslLineAlarmProfile": zhoneDslLineAlarmProfile,
       "zhoneDslLineRowStatus": zhoneDslLineRowStatus,
       "zhoneHdsl2ConfigProfileTable": zhoneHdsl2ConfigProfileTable,
       "zhoneHdsl2ConfigProfileEntry": zhoneHdsl2ConfigProfileEntry,
       "zhoneHdsl2ConfigProfileName": zhoneHdsl2ConfigProfileName,
       "zhoneHdsl2ConfigUnitMode": zhoneHdsl2ConfigUnitMode,
       "zhoneHdsl2ConfigTransmitPowerbackoffMode": zhoneHdsl2ConfigTransmitPowerbackoffMode,
       "zhoneHdsl2ConfigDecoderCoeffA": zhoneHdsl2ConfigDecoderCoeffA,
       "zhoneHdsl2ConfigDecoderCoeffB": zhoneHdsl2ConfigDecoderCoeffB,
       "zhoneHdsl2ConfigFrameSyncWord": zhoneHdsl2ConfigFrameSyncWord,
       "zhoneHdsl2ConfigStuffBits": zhoneHdsl2ConfigStuffBits,
       "zhoneHdsl2ConfigRowStatus": zhoneHdsl2ConfigRowStatus,
       "zhoneHdsl2StatusTable": zhoneHdsl2StatusTable,
       "zhoneHdsl2StatusEntry": zhoneHdsl2StatusEntry,
       "zhoneHdsl2DriftAlarm": zhoneHdsl2DriftAlarm,
       "zhoneHdsl2FramerIBStatus": zhoneHdsl2FramerIBStatus,
       "zhoneHdsl2LocalPSDMaskStatus": zhoneHdsl2LocalPSDMaskStatus,
       "zhoneHdsl2LoopAttenuation": zhoneHdsl2LoopAttenuation,
       "zhoneHdsl2LossWordStatus": zhoneHdsl2LossWordStatus,
       "zhoneHdsl2RmtPSDMaskStatus": zhoneHdsl2RmtPSDMaskStatus,
       "zhoneHdsl2RmtCountryCode": zhoneHdsl2RmtCountryCode,
       "zhoneHdsl2RmtVersion": zhoneHdsl2RmtVersion,
       "zhoneHdsl2RmtProviderCode": zhoneHdsl2RmtProviderCode,
       "zhoneHdsl2RmtVendorData": zhoneHdsl2RmtVendorData,
       "zhoneHdsl2RmtTxEncoderA": zhoneHdsl2RmtTxEncoderA,
       "zhoneHdsl2RmtTxEncoderB": zhoneHdsl2RmtTxEncoderB,
       "zhoneHdsl2TipRingStatus": zhoneHdsl2TipRingStatus,
       "zhoneHdsl2FrameSyncWord": zhoneHdsl2FrameSyncWord,
       "zhoneHdsl2StuffBits": zhoneHdsl2StuffBits,
       "zhoneDslPerfDataTable": zhoneDslPerfDataTable,
       "zhoneDslPerfDataEntry": zhoneDslPerfDataEntry,
       "zhoneDslPerfLofs": zhoneDslPerfLofs,
       "zhoneDslPerfLoss": zhoneDslPerfLoss,
       "zhoneDslPerfLols": zhoneDslPerfLols,
       "zhoneDslPerfInits": zhoneDslPerfInits,
       "zhoneDslPerfCur15MinTimeElapsed": zhoneDslPerfCur15MinTimeElapsed,
       "zhoneDslPerfCur15MinLofs": zhoneDslPerfCur15MinLofs,
       "zhoneDslPerfCur15MinLoss": zhoneDslPerfCur15MinLoss,
       "zhoneDslPerfCur15MinLols": zhoneDslPerfCur15MinLols,
       "zhoneDslPerfCur15MinInits": zhoneDslPerfCur15MinInits,
       "zhoneDslAlarmProfileTable": zhoneDslAlarmProfileTable,
       "zhoneDslAlarmProfileEntry": zhoneDslAlarmProfileEntry,
       "zhoneDslAlarmProfileName": zhoneDslAlarmProfileName,
       "zhoneDslThreshold15MinLoss": zhoneDslThreshold15MinLoss,
       "zhoneDslThreshold15MinLols": zhoneDslThreshold15MinLols,
       "zhoneDslThreshold15MinLofs": zhoneDslThreshold15MinLofs,
       "zhoneDslAlarmProfileRowStatus": zhoneDslAlarmProfileRowStatus,
       "zhoneDsl-MIB": zhoneDsl_MIB}
)
