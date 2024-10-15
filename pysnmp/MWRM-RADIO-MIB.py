# SNMP MIB module (MWRM-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MWRM-RADIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:10 2024
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

(AllowedNotAllowed,
 BerLevel,
 ClockSrc,
 DownUp,
 EnableDisable,
 EnableDisableSMI2,
 GreenYellow,
 HalfFull,
 InputSeverity,
 Integrity,
 LoopbackType,
 MetricImperial,
 NoYes,
 OffOn,
 PmTableType,
 ProgressStatus,
 QueueName,
 RadioId,
 RateMbps,
 RfuId,
 Severity,
 SignalLevel,
 SlotId,
 SupportedNotsupported,
 SwCommand,
 SwCommandTimer,
 TrailIfType,
 TrailProtectedType) = mibBuilder.importSymbols(
    "MWRM-UNIT-MIB",
    "AllowedNotAllowed",
    "BerLevel",
    "ClockSrc",
    "DownUp",
    "EnableDisable",
    "EnableDisableSMI2",
    "GreenYellow",
    "HalfFull",
    "InputSeverity",
    "Integrity",
    "LoopbackType",
    "MetricImperial",
    "NoYes",
    "OffOn",
    "PmTableType",
    "ProgressStatus",
    "QueueName",
    "RadioId",
    "RateMbps",
    "RfuId",
    "Severity",
    "SignalLevel",
    "SlotId",
    "SupportedNotsupported",
    "SwCommand",
    "SwCommandTimer",
    "TrailIfType",
    "TrailProtectedType")

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
 enterprises,
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
    "enterprises",
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


# Types definitions



class MuteOnOff(Integer32):
    """Custom type MuteOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )





class RfuGrade(Integer32):
    """Custom type RfuGrade based on Integer32"""
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
        *(("grade-1", 1),
          ("grade-2", 2),
          ("grade-3", 3),
          ("unknown", 0))
    )





class MrmcBitRate(Integer32):
    """Custom type MrmcBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )





class MrmcScriptId(Integer32):
    """Custom type MrmcScriptId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )





class QamOrder(Integer32):
    """Custom type QamOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )





class MrmcProfile(Integer32):
    """Custom type MrmcProfile based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("profile-0", 0),
          ("profile-1", 1),
          ("profile-10", 10),
          ("profile-11", 11),
          ("profile-12", 12),
          ("profile-13", 13),
          ("profile-14", 14),
          ("profile-15", 15),
          ("profile-2", 2),
          ("profile-3", 3),
          ("profile-4", 4),
          ("profile-5", 5),
          ("profile-6", 6),
          ("profile-7", 7),
          ("profile-8", 8),
          ("profile-9", 9))
    )





class ThresholdExponent(Integer32):
    """Custom type ThresholdExponent based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("n1e-0", 18),
          ("n1e-1", 0),
          ("n1e-11", 10),
          ("n1e-12", 11),
          ("n1e-13", 12),
          ("n1e-14", 13),
          ("n1e-15", 14),
          ("n1e-16", 15),
          ("n1e-17", 16),
          ("n1e-18", 17),
          ("n1e-2", 1),
          ("n1e-3", 2),
          ("n1e-4", 3),
          ("n1e-5", 4),
          ("n1e-6", 5),
          ("n1e-7", 6),
          ("n1e-8", 7),
          ("n1e-9", 8))
    )





class RFUSoftwareInstallStat(Integer32):
    """Custom type RFUSoftwareInstallStat based on Integer32"""
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
        *(("installation-failure", 5),
          ("installation-in-progress", 3),
          ("installation-success", 4),
          ("ready", 0),
          ("transferring-files", 2),
          ("verifying-files", 1))
    )





class RadioProtectionCmd(Integer32):
    """Custom type RadioProtectionCmd based on Integer32"""
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
        *(("clear", 0),
          ("force-switch", 2),
          ("lockout", 3),
          ("manual-switch", 1))
    )





class RfuMajorType(Integer32):
    """Custom type RfuMajorType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("rfu-A", 7),
          ("rfu-C", 4),
          ("rfu-D", 8),
          ("rfu-H", 5),
          ("rfu-HC", 1),
          ("rfu-HP", 2),
          ("rfu-HP-2", 6),
          ("rfu-SP", 3),
          ("unknown", 0))
    )





class Copy2mate(Integer32):
    """Custom type Copy2mate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("copyToMate", 1),
          ("noAction", 0))
    )





class XpicState(Integer32):
    """Custom type XpicState based on Integer32"""
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
        *(("init", 0),
          ("singleChannel", 2),
          ("xpicDisabled", 1),
          ("xpicIdle", 5),
          ("xrsmDisabled", 3),
          ("xrsmRecovery", 4))
    )





class HcModeType(Integer32):
    """Custom type HcModeType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("layer2", 2),
          ("layer3", 4),
          ("layer4", 5),
          ("legacy", 0),
          ("mpls", 3),
          ("tunnel", 6),
          ("tunnel-layer3", 7),
          ("tunnel-layer4", 8))
    )





class EnhancedHCExclRuleType(Integer32):
    """Custom type EnhancedHCExclRuleType based on Integer32"""
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
        *(("ethertype", 3),
          ("flow-type", 4),
          ("mac-da", 1),
          ("mac-sa", 2),
          ("vlan", 0))
    )





class HcType(Integer32):
    """Custom type HcType based on Integer32"""
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
        *(("deep-header-compression", 3),
          ("legacy", 0),
          ("multi-layer-header-compression", 2),
          ("no-compression", 1))
    )





class CommunicationChannel(Integer32):
    """Custom type CommunicationChannel based on Integer32"""
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
        *(("ftp", 0),
          ("http", 2),
          ("https", 3),
          ("sftp", 1))
    )





class FalseTrue(Integer32):
    """Custom type FalseTrue based on Integer32"""
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





class WaysideBandwidth(Integer32):
    """Custom type WaysideBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              64,
              128,
              192,
              256,
              320,
              384,
              448,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1024", 1024),
          ("n128", 128),
          ("n192", 192),
          ("n2048", 2048),
          ("n256", 256),
          ("n320", 320),
          ("n384", 384),
          ("n448", 448),
          ("n512", 512),
          ("n64", 64))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microwave_radio_ObjectIdentity = ObjectIdentity
microwave_radio = _Microwave_radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281)
)
_GenEquip_ObjectIdentity = ObjectIdentity
genEquip = _GenEquip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10)
)
_GenEquipUnit_ObjectIdentity = ObjectIdentity
genEquipUnit = _GenEquipUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 1)
)
_GenEquipRFU_ObjectIdentity = ObjectIdentity
genEquipRFU = _GenEquipRFU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5)
)
_GenEquipRfuStatusTable_Object = MibTable
genEquipRfuStatusTable = _GenEquipRfuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1)
)
if mibBuilder.loadTexts:
    genEquipRfuStatusTable.setStatus("mandatory")
_GenEquipRfuStatusEntry_Object = MibTableRow
genEquipRfuStatusEntry = _GenEquipRfuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1)
)
genEquipRfuStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuStatusId"),
)
if mibBuilder.loadTexts:
    genEquipRfuStatusEntry.setStatus("mandatory")
_GenEquipRfuStatusId_Type = RfuId
_GenEquipRfuStatusId_Object = MibTableColumn
genEquipRfuStatusId = _GenEquipRfuStatusId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 1),
    _GenEquipRfuStatusId_Type()
)
genEquipRfuStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusId.setStatus("mandatory")


class _GenEquipRfuStatusRxLevel_Type(Integer32):
    """Custom type genEquipRfuStatusRxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 0),
    )


_GenEquipRfuStatusRxLevel_Type.__name__ = "Integer32"
_GenEquipRfuStatusRxLevel_Object = MibTableColumn
genEquipRfuStatusRxLevel = _GenEquipRfuStatusRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 2),
    _GenEquipRfuStatusRxLevel_Type()
)
genEquipRfuStatusRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRxLevel.setStatus("mandatory")


class _GenEquipRfuStatusTxLevel_Type(Integer32):
    """Custom type genEquipRfuStatusTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 34),
    )


_GenEquipRfuStatusTxLevel_Type.__name__ = "Integer32"
_GenEquipRfuStatusTxLevel_Object = MibTableColumn
genEquipRfuStatusTxLevel = _GenEquipRfuStatusTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 3),
    _GenEquipRfuStatusTxLevel_Type()
)
genEquipRfuStatusTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusTxLevel.setStatus("mandatory")
_GenEquipRfuStatusTemperature_Type = Integer32
_GenEquipRfuStatusTemperature_Object = MibTableColumn
genEquipRfuStatusTemperature = _GenEquipRfuStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 4),
    _GenEquipRfuStatusTemperature_Type()
)
genEquipRfuStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusTemperature.setStatus("mandatory")
_GenEquipRfuStatusRunningVersion_Type = DisplayString
_GenEquipRfuStatusRunningVersion_Object = MibTableColumn
genEquipRfuStatusRunningVersion = _GenEquipRfuStatusRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 5),
    _GenEquipRfuStatusRunningVersion_Type()
)
genEquipRfuStatusRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRunningVersion.setStatus("mandatory")


class _GenEquipRfuStatusRFUType_Type(Integer32):
    """Custom type genEquipRfuStatusRFUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              32,
              34,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("rfu-1500hp", 34),
          ("rfu-1500p", 32),
          ("rfu-1500sp", 40),
          ("rfu-a", 42),
          ("rfu-c", 38),
          ("rfu-d", 43),
          ("rfu-h", 39),
          ("rfu-hp", 41),
          ("unknown", 2))
    )


_GenEquipRfuStatusRFUType_Type.__name__ = "Integer32"
_GenEquipRfuStatusRFUType_Object = MibTableColumn
genEquipRfuStatusRFUType = _GenEquipRfuStatusRFUType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 6),
    _GenEquipRfuStatusRFUType_Type()
)
genEquipRfuStatusRFUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUType.setStatus("mandatory")
_GenEquipRfuStatusRFUGrade_Type = RfuGrade
_GenEquipRfuStatusRFUGrade_Object = MibTableColumn
genEquipRfuStatusRFUGrade = _GenEquipRfuStatusRFUGrade_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 7),
    _GenEquipRfuStatusRFUGrade_Type()
)
genEquipRfuStatusRFUGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUGrade.setStatus("mandatory")
_GenEquipRfuStatusTxRxFreqSeparation_Type = Integer32
_GenEquipRfuStatusTxRxFreqSeparation_Object = MibTableColumn
genEquipRfuStatusTxRxFreqSeparation = _GenEquipRfuStatusTxRxFreqSeparation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 8),
    _GenEquipRfuStatusTxRxFreqSeparation_Type()
)
genEquipRfuStatusTxRxFreqSeparation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusTxRxFreqSeparation.setStatus("mandatory")


class _GenEquipRfuStatusRFUMode_Type(Integer32):
    """Custom type genEquipRfuStatusRFUMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("combined", 4),
          ("diversity", 3),
          ("main", 2))
    )


_GenEquipRfuStatusRFUMode_Type.__name__ = "Integer32"
_GenEquipRfuStatusRFUMode_Object = MibTableColumn
genEquipRfuStatusRFUMode = _GenEquipRfuStatusRFUMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 9),
    _GenEquipRfuStatusRFUMode_Type()
)
genEquipRfuStatusRFUMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUMode.setStatus("mandatory")


class _GenEquipRfuStatusRxLevelDiversity_Type(Integer32):
    """Custom type genEquipRfuStatusRxLevelDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 0),
    )


_GenEquipRfuStatusRxLevelDiversity_Type.__name__ = "Integer32"
_GenEquipRfuStatusRxLevelDiversity_Object = MibTableColumn
genEquipRfuStatusRxLevelDiversity = _GenEquipRfuStatusRxLevelDiversity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 10),
    _GenEquipRfuStatusRxLevelDiversity_Type()
)
genEquipRfuStatusRxLevelDiversity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRxLevelDiversity.setStatus("mandatory")


class _GenEquipRfuStatusRxLevelCombined_Type(Integer32):
    """Custom type genEquipRfuStatusRxLevelCombined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 0),
    )


_GenEquipRfuStatusRxLevelCombined_Type.__name__ = "Integer32"
_GenEquipRfuStatusRxLevelCombined_Object = MibTableColumn
genEquipRfuStatusRxLevelCombined = _GenEquipRfuStatusRxLevelCombined_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 11),
    _GenEquipRfuStatusRxLevelCombined_Type()
)
genEquipRfuStatusRxLevelCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRxLevelCombined.setStatus("mandatory")


class _GenEquipRfuStatusAutoDelayCalStatus_Type(Integer32):
    """Custom type genEquipRfuStatusAutoDelayCalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("error", 4),
          ("no-action", 2),
          ("pass", 3))
    )


_GenEquipRfuStatusAutoDelayCalStatus_Type.__name__ = "Integer32"
_GenEquipRfuStatusAutoDelayCalStatus_Object = MibTableColumn
genEquipRfuStatusAutoDelayCalStatus = _GenEquipRfuStatusAutoDelayCalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 12),
    _GenEquipRfuStatusAutoDelayCalStatus_Type()
)
genEquipRfuStatusAutoDelayCalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusAutoDelayCalStatus.setStatus("mandatory")
_GenEquipRfuStatusRFUSerialNumber_Type = DisplayString
_GenEquipRfuStatusRFUSerialNumber_Object = MibTableColumn
genEquipRfuStatusRFUSerialNumber = _GenEquipRfuStatusRFUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 13),
    _GenEquipRfuStatusRFUSerialNumber_Type()
)
genEquipRfuStatusRFUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUSerialNumber.setStatus("mandatory")
_GenEquipRfuStatusRFUPartNumber_Type = DisplayString
_GenEquipRfuStatusRFUPartNumber_Object = MibTableColumn
genEquipRfuStatusRFUPartNumber = _GenEquipRfuStatusRFUPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 14),
    _GenEquipRfuStatusRFUPartNumber_Type()
)
genEquipRfuStatusRFUPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUPartNumber.setStatus("mandatory")
_GenEquipRfuStatusRFUmateCarrier_Type = Integer32
_GenEquipRfuStatusRFUmateCarrier_Object = MibTableColumn
genEquipRfuStatusRFUmateCarrier = _GenEquipRfuStatusRFUmateCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 15),
    _GenEquipRfuStatusRFUmateCarrier_Type()
)
genEquipRfuStatusRFUmateCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUmateCarrier.setStatus("mandatory")
_GenEquipRfuStatusRFUMaxTxFreq_Type = Integer32
_GenEquipRfuStatusRFUMaxTxFreq_Object = MibTableColumn
genEquipRfuStatusRFUMaxTxFreq = _GenEquipRfuStatusRFUMaxTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 16),
    _GenEquipRfuStatusRFUMaxTxFreq_Type()
)
genEquipRfuStatusRFUMaxTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUMaxTxFreq.setStatus("mandatory")
_GenEquipRfuStatusRFUMinTxFreq_Type = Integer32
_GenEquipRfuStatusRFUMinTxFreq_Object = MibTableColumn
genEquipRfuStatusRFUMinTxFreq = _GenEquipRfuStatusRFUMinTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 17),
    _GenEquipRfuStatusRFUMinTxFreq_Type()
)
genEquipRfuStatusRFUMinTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUMinTxFreq.setStatus("mandatory")
_GenEquipRfuStatusRFUMaxRxFreq_Type = Integer32
_GenEquipRfuStatusRFUMaxRxFreq_Object = MibTableColumn
genEquipRfuStatusRFUMaxRxFreq = _GenEquipRfuStatusRFUMaxRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 18),
    _GenEquipRfuStatusRFUMaxRxFreq_Type()
)
genEquipRfuStatusRFUMaxRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUMaxRxFreq.setStatus("mandatory")
_GenEquipRfuStatusRFUMinRxFreq_Type = Integer32
_GenEquipRfuStatusRFUMinRxFreq_Object = MibTableColumn
genEquipRfuStatusRFUMinRxFreq = _GenEquipRfuStatusRFUMinRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 19),
    _GenEquipRfuStatusRFUMinRxFreq_Type()
)
genEquipRfuStatusRFUMinRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusRFUMinRxFreq.setStatus("mandatory")


class _GenEquipRfuStatusInstallation_Type(Integer32):
    """Custom type genEquipRfuStatusInstallation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all-indoor", 1),
          ("split-mount", 0))
    )


_GenEquipRfuStatusInstallation_Type.__name__ = "Integer32"
_GenEquipRfuStatusInstallation_Object = MibTableColumn
genEquipRfuStatusInstallation = _GenEquipRfuStatusInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 20),
    _GenEquipRfuStatusInstallation_Type()
)
genEquipRfuStatusInstallation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusInstallation.setStatus("mandatory")
_GenEquipRfuStatusDataSciErrors_Type = Integer32
_GenEquipRfuStatusDataSciErrors_Object = MibTableColumn
genEquipRfuStatusDataSciErrors = _GenEquipRfuStatusDataSciErrors_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 21),
    _GenEquipRfuStatusDataSciErrors_Type()
)
genEquipRfuStatusDataSciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusDataSciErrors.setStatus("mandatory")
_GenEquipRfuStatusDeviceError_Type = Integer32
_GenEquipRfuStatusDeviceError_Object = MibTableColumn
genEquipRfuStatusDeviceError = _GenEquipRfuStatusDeviceError_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 22),
    _GenEquipRfuStatusDeviceError_Type()
)
genEquipRfuStatusDeviceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusDeviceError.setStatus("mandatory")


class _GenEquipRfuStatusBand_Type(Integer32):
    """Custom type genEquipRfuStatusBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("band-10dot5-11", 11),
          ("band-13", 10),
          ("band-15", 9),
          ("band-18", 2),
          ("band-23", 3),
          ("band-26", 4),
          ("band-28", 5),
          ("band-29", 7),
          ("band-31", 8),
          ("band-32", 14),
          ("band-38", 6),
          ("band-6L-6H", 13),
          ("band-7-8", 12),
          ("unknown", 0))
    )


_GenEquipRfuStatusBand_Type.__name__ = "Integer32"
_GenEquipRfuStatusBand_Object = MibTableColumn
genEquipRfuStatusBand = _GenEquipRfuStatusBand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 23),
    _GenEquipRfuStatusBand_Type()
)
genEquipRfuStatusBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusBand.setStatus("mandatory")
_GenEquipRfuStatusPATemp_Type = Integer32
_GenEquipRfuStatusPATemp_Object = MibTableColumn
genEquipRfuStatusPATemp = _GenEquipRfuStatusPATemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 24),
    _GenEquipRfuStatusPATemp_Type()
)
genEquipRfuStatusPATemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusPATemp.setStatus("mandatory")
_GenEquipRfuStatusTxMute_Type = OffOn
_GenEquipRfuStatusTxMute_Object = MibTableColumn
genEquipRfuStatusTxMute = _GenEquipRfuStatusTxMute_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 25),
    _GenEquipRfuStatusTxMute_Type()
)
genEquipRfuStatusTxMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusTxMute.setStatus("mandatory")
_GenEquipRfuStatusMinTxLevel_Type = Integer32
_GenEquipRfuStatusMinTxLevel_Object = MibTableColumn
genEquipRfuStatusMinTxLevel = _GenEquipRfuStatusMinTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 26),
    _GenEquipRfuStatusMinTxLevel_Type()
)
genEquipRfuStatusMinTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusMinTxLevel.setStatus("mandatory")
_GenEquipRfuStatusMaxTxLevel_Type = Integer32
_GenEquipRfuStatusMaxTxLevel_Object = MibTableColumn
genEquipRfuStatusMaxTxLevel = _GenEquipRfuStatusMaxTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 27),
    _GenEquipRfuStatusMaxTxLevel_Type()
)
genEquipRfuStatusMaxTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusMaxTxLevel.setStatus("mandatory")
_GenEquipRfuStatusMinBW_Type = Integer32
_GenEquipRfuStatusMinBW_Object = MibTableColumn
genEquipRfuStatusMinBW = _GenEquipRfuStatusMinBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 28),
    _GenEquipRfuStatusMinBW_Type()
)
genEquipRfuStatusMinBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusMinBW.setStatus("mandatory")
_GenEquipRfuStatusMaxBW_Type = Integer32
_GenEquipRfuStatusMaxBW_Object = MibTableColumn
genEquipRfuStatusMaxBW = _GenEquipRfuStatusMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 29),
    _GenEquipRfuStatusMaxBW_Type()
)
genEquipRfuStatusMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusMaxBW.setStatus("mandatory")
_GenEquipRfuStatusCommunication_Type = DownUp
_GenEquipRfuStatusCommunication_Object = MibTableColumn
genEquipRfuStatusCommunication = _GenEquipRfuStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 30),
    _GenEquipRfuStatusCommunication_Type()
)
genEquipRfuStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusCommunication.setStatus("mandatory")


class _GenEquipRfuCfgATPCOverrideTimerState_Type(Integer32):
    """Custom type genEquipRfuCfgATPCOverrideTimerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expired", 1),
          ("normal", 0))
    )


_GenEquipRfuCfgATPCOverrideTimerState_Type.__name__ = "Integer32"
_GenEquipRfuCfgATPCOverrideTimerState_Object = MibTableColumn
genEquipRfuCfgATPCOverrideTimerState = _GenEquipRfuCfgATPCOverrideTimerState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 31),
    _GenEquipRfuCfgATPCOverrideTimerState_Type()
)
genEquipRfuCfgATPCOverrideTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCOverrideTimerState.setStatus("mandatory")
_GenEquipRfuStatusIfCombSupport_Type = SupportedNotsupported
_GenEquipRfuStatusIfCombSupport_Object = MibTableColumn
genEquipRfuStatusIfCombSupport = _GenEquipRfuStatusIfCombSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 32),
    _GenEquipRfuStatusIfCombSupport_Type()
)
genEquipRfuStatusIfCombSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusIfCombSupport.setStatus("mandatory")
_GenEquipRfuStatusMinRxLevel_Type = Integer32
_GenEquipRfuStatusMinRxLevel_Object = MibTableColumn
genEquipRfuStatusMinRxLevel = _GenEquipRfuStatusMinRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 33),
    _GenEquipRfuStatusMinRxLevel_Type()
)
genEquipRfuStatusMinRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusMinRxLevel.setStatus("mandatory")
_GenEquipRfuStatusMaxRxLevel_Type = Integer32
_GenEquipRfuStatusMaxRxLevel_Object = MibTableColumn
genEquipRfuStatusMaxRxLevel = _GenEquipRfuStatusMaxRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 1, 1, 34),
    _GenEquipRfuStatusMaxRxLevel_Type()
)
genEquipRfuStatusMaxRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuStatusMaxRxLevel.setStatus("mandatory")
_GenEquipRfuCfgTable_Object = MibTable
genEquipRfuCfgTable = _GenEquipRfuCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2)
)
if mibBuilder.loadTexts:
    genEquipRfuCfgTable.setStatus("mandatory")
_GenEquipRfuCfgEntry_Object = MibTableRow
genEquipRfuCfgEntry = _GenEquipRfuCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1)
)
genEquipRfuCfgEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuCfgId"),
)
if mibBuilder.loadTexts:
    genEquipRfuCfgEntry.setStatus("mandatory")
_GenEquipRfuCfgId_Type = RfuId
_GenEquipRfuCfgId_Object = MibTableColumn
genEquipRfuCfgId = _GenEquipRfuCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 1),
    _GenEquipRfuCfgId_Type()
)
genEquipRfuCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuCfgId.setStatus("mandatory")


class _GenEquipRfuCfgMaxTxLevel_Type(Integer32):
    """Custom type genEquipRfuCfgMaxTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 34),
    )


_GenEquipRfuCfgMaxTxLevel_Type.__name__ = "Integer32"
_GenEquipRfuCfgMaxTxLevel_Object = MibTableColumn
genEquipRfuCfgMaxTxLevel = _GenEquipRfuCfgMaxTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 2),
    _GenEquipRfuCfgMaxTxLevel_Type()
)
genEquipRfuCfgMaxTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgMaxTxLevel.setStatus("mandatory")
_GenEquipRfuCfgTxFreq_Type = Integer32
_GenEquipRfuCfgTxFreq_Object = MibTableColumn
genEquipRfuCfgTxFreq = _GenEquipRfuCfgTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 3),
    _GenEquipRfuCfgTxFreq_Type()
)
genEquipRfuCfgTxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgTxFreq.setStatus("mandatory")
_GenEquipRfuCfgRxFreq_Type = Integer32
_GenEquipRfuCfgRxFreq_Object = MibTableColumn
genEquipRfuCfgRxFreq = _GenEquipRfuCfgRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 4),
    _GenEquipRfuCfgRxFreq_Type()
)
genEquipRfuCfgRxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgRxFreq.setStatus("mandatory")
_GenEquipRfuCfgATPCAdmin_Type = EnableDisable
_GenEquipRfuCfgATPCAdmin_Object = MibTableColumn
genEquipRfuCfgATPCAdmin = _GenEquipRfuCfgATPCAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 5),
    _GenEquipRfuCfgATPCAdmin_Type()
)
genEquipRfuCfgATPCAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCAdmin.setStatus("mandatory")


class _GenEquipRfuCfgATPCRefRSL_Type(Integer32):
    """Custom type genEquipRfuCfgATPCRefRSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_GenEquipRfuCfgATPCRefRSL_Type.__name__ = "Integer32"
_GenEquipRfuCfgATPCRefRSL_Object = MibTableColumn
genEquipRfuCfgATPCRefRSL = _GenEquipRfuCfgATPCRefRSL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 6),
    _GenEquipRfuCfgATPCRefRSL_Type()
)
genEquipRfuCfgATPCRefRSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCRefRSL.setStatus("mandatory")
_GenEquipRfuCfgMuteTx_Type = MuteOnOff
_GenEquipRfuCfgMuteTx_Object = MibTableColumn
genEquipRfuCfgMuteTx = _GenEquipRfuCfgMuteTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 7),
    _GenEquipRfuCfgMuteTx_Type()
)
genEquipRfuCfgMuteTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgMuteTx.setStatus("mandatory")


class _GenEquipRfuCfgRSLConnSrc_Type(Integer32):
    """Custom type genEquipRfuCfgRSLConnSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 3),
          ("main", 2))
    )


_GenEquipRfuCfgRSLConnSrc_Type.__name__ = "Integer32"
_GenEquipRfuCfgRSLConnSrc_Object = MibTableColumn
genEquipRfuCfgRSLConnSrc = _GenEquipRfuCfgRSLConnSrc_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 8),
    _GenEquipRfuCfgRSLConnSrc_Type()
)
genEquipRfuCfgRSLConnSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgRSLConnSrc.setStatus("mandatory")


class _GenEquipRfuCfgDelayCal_Type(Integer32):
    """Custom type genEquipRfuCfgDelayCal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 130),
    )


_GenEquipRfuCfgDelayCal_Type.__name__ = "Integer32"
_GenEquipRfuCfgDelayCal_Object = MibTableColumn
genEquipRfuCfgDelayCal = _GenEquipRfuCfgDelayCal_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 9),
    _GenEquipRfuCfgDelayCal_Type()
)
genEquipRfuCfgDelayCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgDelayCal.setStatus("mandatory")


class _GenEquipRfuCfgLoopback_Type(Integer32):
    """Custom type genEquipRfuCfgLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("towardsSystem", 1))
    )


_GenEquipRfuCfgLoopback_Type.__name__ = "Integer32"
_GenEquipRfuCfgLoopback_Object = MibTableColumn
genEquipRfuCfgLoopback = _GenEquipRfuCfgLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 10),
    _GenEquipRfuCfgLoopback_Type()
)
genEquipRfuCfgLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgLoopback.setStatus("mandatory")
_GenEquipRfuCfgLogAdmin_Type = EnableDisable
_GenEquipRfuCfgLogAdmin_Object = MibTableColumn
genEquipRfuCfgLogAdmin = _GenEquipRfuCfgLogAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 11),
    _GenEquipRfuCfgLogAdmin_Type()
)
genEquipRfuCfgLogAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgLogAdmin.setStatus("mandatory")
_GenEquipRfuCfgClearComDeviceError_Type = OffOn
_GenEquipRfuCfgClearComDeviceError_Object = MibTableColumn
genEquipRfuCfgClearComDeviceError = _GenEquipRfuCfgClearComDeviceError_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 12),
    _GenEquipRfuCfgClearComDeviceError_Type()
)
genEquipRfuCfgClearComDeviceError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgClearComDeviceError.setStatus("mandatory")
_GenEquipRfuCfgGreenModeAdmin_Type = EnableDisable
_GenEquipRfuCfgGreenModeAdmin_Object = MibTableColumn
genEquipRfuCfgGreenModeAdmin = _GenEquipRfuCfgGreenModeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 13),
    _GenEquipRfuCfgGreenModeAdmin_Type()
)
genEquipRfuCfgGreenModeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgGreenModeAdmin.setStatus("mandatory")


class _GenEquipRfuCfgGreenModeReferenceLevel_Type(Integer32):
    """Custom type genEquipRfuCfgGreenModeReferenceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_GenEquipRfuCfgGreenModeReferenceLevel_Type.__name__ = "Integer32"
_GenEquipRfuCfgGreenModeReferenceLevel_Object = MibTableColumn
genEquipRfuCfgGreenModeReferenceLevel = _GenEquipRfuCfgGreenModeReferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 14),
    _GenEquipRfuCfgGreenModeReferenceLevel_Type()
)
genEquipRfuCfgGreenModeReferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgGreenModeReferenceLevel.setStatus("mandatory")


class _GenEquipRfuCfgATPCOverrideTxLevel_Type(Integer32):
    """Custom type genEquipRfuCfgATPCOverrideTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 34),
    )


_GenEquipRfuCfgATPCOverrideTxLevel_Type.__name__ = "Integer32"
_GenEquipRfuCfgATPCOverrideTxLevel_Object = MibTableColumn
genEquipRfuCfgATPCOverrideTxLevel = _GenEquipRfuCfgATPCOverrideTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 15),
    _GenEquipRfuCfgATPCOverrideTxLevel_Type()
)
genEquipRfuCfgATPCOverrideTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCOverrideTxLevel.setStatus("mandatory")


class _GenEquipRfuCfgATPCOverrideTimeout_Type(Integer32):
    """Custom type genEquipRfuCfgATPCOverrideTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_GenEquipRfuCfgATPCOverrideTimeout_Type.__name__ = "Integer32"
_GenEquipRfuCfgATPCOverrideTimeout_Object = MibTableColumn
genEquipRfuCfgATPCOverrideTimeout = _GenEquipRfuCfgATPCOverrideTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 16),
    _GenEquipRfuCfgATPCOverrideTimeout_Type()
)
genEquipRfuCfgATPCOverrideTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCOverrideTimeout.setStatus("mandatory")


class _GenEquipRfuCfgATPCOverrideTimerCounter_Type(Integer32):
    """Custom type genEquipRfuCfgATPCOverrideTimerCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_GenEquipRfuCfgATPCOverrideTimerCounter_Type.__name__ = "Integer32"
_GenEquipRfuCfgATPCOverrideTimerCounter_Object = MibTableColumn
genEquipRfuCfgATPCOverrideTimerCounter = _GenEquipRfuCfgATPCOverrideTimerCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 17),
    _GenEquipRfuCfgATPCOverrideTimerCounter_Type()
)
genEquipRfuCfgATPCOverrideTimerCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCOverrideTimerCounter.setStatus("mandatory")
_GenEquipRfuCfgATPCOverrideTimerCancel_Type = OffOn
_GenEquipRfuCfgATPCOverrideTimerCancel_Object = MibTableColumn
genEquipRfuCfgATPCOverrideTimerCancel = _GenEquipRfuCfgATPCOverrideTimerCancel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 2, 1, 18),
    _GenEquipRfuCfgATPCOverrideTimerCancel_Type()
)
genEquipRfuCfgATPCOverrideTimerCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuCfgATPCOverrideTimerCancel.setStatus("mandatory")
_GenEquipRfuUploadTable_Object = MibTable
genEquipRfuUploadTable = _GenEquipRfuUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 3)
)
if mibBuilder.loadTexts:
    genEquipRfuUploadTable.setStatus("mandatory")
_GenEquipRfuUploadEntry_Object = MibTableRow
genEquipRfuUploadEntry = _GenEquipRfuUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 3, 1)
)
genEquipRfuUploadEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuUploadId"),
)
if mibBuilder.loadTexts:
    genEquipRfuUploadEntry.setStatus("mandatory")
_GenEquipRfuUploadId_Type = RadioId
_GenEquipRfuUploadId_Object = MibTableColumn
genEquipRfuUploadId = _GenEquipRfuUploadId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 3, 1, 1),
    _GenEquipRfuUploadId_Type()
)
genEquipRfuUploadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuUploadId.setStatus("mandatory")


class _GenEquipRfuUploadSwCommand_Type(Integer32):
    """Custom type genEquipRfuUploadSwCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 2),
          ("uploadSW", 1))
    )


_GenEquipRfuUploadSwCommand_Type.__name__ = "Integer32"
_GenEquipRfuUploadSwCommand_Object = MibTableColumn
genEquipRfuUploadSwCommand = _GenEquipRfuUploadSwCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 3, 1, 2),
    _GenEquipRfuUploadSwCommand_Type()
)
genEquipRfuUploadSwCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuUploadSwCommand.setStatus("mandatory")


class _GenEquipRfuUploadSwStatus_Type(Integer32):
    """Custom type genEquipRfuUploadSwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("loadDone", 5),
          ("loadError", 1),
          ("loadSendBlock", 3),
          ("loadStart", 2),
          ("noLoad", 0))
    )


_GenEquipRfuUploadSwStatus_Type.__name__ = "Integer32"
_GenEquipRfuUploadSwStatus_Object = MibTableColumn
genEquipRfuUploadSwStatus = _GenEquipRfuUploadSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 3, 1, 3),
    _GenEquipRfuUploadSwStatus_Type()
)
genEquipRfuUploadSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuUploadSwStatus.setStatus("mandatory")
_GenEquipRfuUploadCounter_Type = Integer32
_GenEquipRfuUploadCounter_Object = MibTableColumn
genEquipRfuUploadCounter = _GenEquipRfuUploadCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 3, 1, 4),
    _GenEquipRfuUploadCounter_Type()
)
genEquipRfuUploadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuUploadCounter.setStatus("mandatory")
_GenEquipRFUNG_ObjectIdentity = ObjectIdentity
genEquipRFUNG = _GenEquipRFUNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4)
)
_GenEquipRfuSwInstallTable_Object = MibTable
genEquipRfuSwInstallTable = _GenEquipRfuSwInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 2)
)
if mibBuilder.loadTexts:
    genEquipRfuSwInstallTable.setStatus("mandatory")
_GenEquipRfuSwInstallEntry_Object = MibTableRow
genEquipRfuSwInstallEntry = _GenEquipRfuSwInstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 2, 1)
)
genEquipRfuSwInstallEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuSwInstallIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRfuSwInstallEntry.setStatus("mandatory")
_GenEquipRfuSwInstallIfIndex_Type = Integer32
_GenEquipRfuSwInstallIfIndex_Object = MibTableColumn
genEquipRfuSwInstallIfIndex = _GenEquipRfuSwInstallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 2, 1, 1),
    _GenEquipRfuSwInstallIfIndex_Type()
)
genEquipRfuSwInstallIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuSwInstallIfIndex.setStatus("mandatory")


class _GenEquipRfuSwInstallOperation_Type(Integer32):
    """Custom type genEquipRfuSwInstallOperation based on Integer32"""
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
        *(("abort-timer", 3),
          ("install-existing-version", 2),
          ("no-operation", 0),
          ("update-version-from-bundle", 1))
    )


_GenEquipRfuSwInstallOperation_Type.__name__ = "Integer32"
_GenEquipRfuSwInstallOperation_Object = MibTableColumn
genEquipRfuSwInstallOperation = _GenEquipRfuSwInstallOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 2, 1, 2),
    _GenEquipRfuSwInstallOperation_Type()
)
genEquipRfuSwInstallOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuSwInstallOperation.setStatus("mandatory")
_GenEquipRfuSwInstallTimedInstallation_Type = NoYes
_GenEquipRfuSwInstallTimedInstallation_Object = MibTableColumn
genEquipRfuSwInstallTimedInstallation = _GenEquipRfuSwInstallTimedInstallation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 2, 1, 3),
    _GenEquipRfuSwInstallTimedInstallation_Type()
)
genEquipRfuSwInstallTimedInstallation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuSwInstallTimedInstallation.setStatus("mandatory")
_GenEquipRfuSwInstallTimer_Type = Integer32
_GenEquipRfuSwInstallTimer_Object = MibTableColumn
genEquipRfuSwInstallTimer = _GenEquipRfuSwInstallTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 2, 1, 4),
    _GenEquipRfuSwInstallTimer_Type()
)
genEquipRfuSwInstallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRfuSwInstallTimer.setStatus("mandatory")
_GenEquipRfuInstalledVersionsTable_Object = MibTable
genEquipRfuInstalledVersionsTable = _GenEquipRfuInstalledVersionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3)
)
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsTable.setStatus("mandatory")
_GenEquipRfuInstalledVersionsEntry_Object = MibTableRow
genEquipRfuInstalledVersionsEntry = _GenEquipRfuInstalledVersionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1)
)
genEquipRfuInstalledVersionsEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuInstalledVersionsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsEntry.setStatus("mandatory")
_GenEquipRfuInstalledVersionsIfIndex_Type = Integer32
_GenEquipRfuInstalledVersionsIfIndex_Object = MibTableColumn
genEquipRfuInstalledVersionsIfIndex = _GenEquipRfuInstalledVersionsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1, 1),
    _GenEquipRfuInstalledVersionsIfIndex_Type()
)
genEquipRfuInstalledVersionsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsIfIndex.setStatus("mandatory")
_GenEquipRfuInstalledVersionsDSP_Type = DisplayString
_GenEquipRfuInstalledVersionsDSP_Object = MibTableColumn
genEquipRfuInstalledVersionsDSP = _GenEquipRfuInstalledVersionsDSP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1, 2),
    _GenEquipRfuInstalledVersionsDSP_Type()
)
genEquipRfuInstalledVersionsDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsDSP.setStatus("mandatory")
_GenEquipRfuInstalledVersionsConfigurations_Type = DisplayString
_GenEquipRfuInstalledVersionsConfigurations_Object = MibTableColumn
genEquipRfuInstalledVersionsConfigurations = _GenEquipRfuInstalledVersionsConfigurations_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1, 3),
    _GenEquipRfuInstalledVersionsConfigurations_Type()
)
genEquipRfuInstalledVersionsConfigurations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsConfigurations.setStatus("mandatory")
_GenEquipRfuInstalledVersionsConstants_Type = DisplayString
_GenEquipRfuInstalledVersionsConstants_Object = MibTableColumn
genEquipRfuInstalledVersionsConstants = _GenEquipRfuInstalledVersionsConstants_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1, 4),
    _GenEquipRfuInstalledVersionsConstants_Type()
)
genEquipRfuInstalledVersionsConstants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsConstants.setStatus("mandatory")
_GenEquipRfuInstalledVersionsScripts_Type = DisplayString
_GenEquipRfuInstalledVersionsScripts_Object = MibTableColumn
genEquipRfuInstalledVersionsScripts = _GenEquipRfuInstalledVersionsScripts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1, 5),
    _GenEquipRfuInstalledVersionsScripts_Type()
)
genEquipRfuInstalledVersionsScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsScripts.setStatus("mandatory")
_GenEquipRfuInstalledVersionsFirmware_Type = DisplayString
_GenEquipRfuInstalledVersionsFirmware_Object = MibTableColumn
genEquipRfuInstalledVersionsFirmware = _GenEquipRfuInstalledVersionsFirmware_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 3, 1, 6),
    _GenEquipRfuInstalledVersionsFirmware_Type()
)
genEquipRfuInstalledVersionsFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuInstalledVersionsFirmware.setStatus("mandatory")
_GenEquipRfuSwStatusTable_Object = MibTable
genEquipRfuSwStatusTable = _GenEquipRfuSwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 4)
)
if mibBuilder.loadTexts:
    genEquipRfuSwStatusTable.setStatus("mandatory")
_GenEquipRfuSwStatusEntry_Object = MibTableRow
genEquipRfuSwStatusEntry = _GenEquipRfuSwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 4, 1)
)
genEquipRfuSwStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuSwStatusIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRfuSwStatusEntry.setStatus("mandatory")
_GenEquipRfuSwStatusIfIndex_Type = Integer32
_GenEquipRfuSwStatusIfIndex_Object = MibTableColumn
genEquipRfuSwStatusIfIndex = _GenEquipRfuSwStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 4, 1, 1),
    _GenEquipRfuSwStatusIfIndex_Type()
)
genEquipRfuSwStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuSwStatusIfIndex.setStatus("mandatory")
_GenEquipRfuSwStatusCurrentState_Type = RFUSoftwareInstallStat
_GenEquipRfuSwStatusCurrentState_Object = MibTableColumn
genEquipRfuSwStatusCurrentState = _GenEquipRfuSwStatusCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 4, 1, 2),
    _GenEquipRfuSwStatusCurrentState_Type()
)
genEquipRfuSwStatusCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuSwStatusCurrentState.setStatus("mandatory")
_GenEquipRfuSwStatusProgress_Type = Integer32
_GenEquipRfuSwStatusProgress_Object = MibTableColumn
genEquipRfuSwStatusProgress = _GenEquipRfuSwStatusProgress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 4, 1, 3),
    _GenEquipRfuSwStatusProgress_Type()
)
genEquipRfuSwStatusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuSwStatusProgress.setStatus("mandatory")
_GenEquipRfuRunningVersionsTable_Object = MibTable
genEquipRfuRunningVersionsTable = _GenEquipRfuRunningVersionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5)
)
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsTable.setStatus("mandatory")
_GenEquipRfuRunningVersionsEntry_Object = MibTableRow
genEquipRfuRunningVersionsEntry = _GenEquipRfuRunningVersionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1)
)
genEquipRfuRunningVersionsEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuRunningVersionsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsEntry.setStatus("mandatory")
_GenEquipRfuRunningVersionsIfIndex_Type = Integer32
_GenEquipRfuRunningVersionsIfIndex_Object = MibTableColumn
genEquipRfuRunningVersionsIfIndex = _GenEquipRfuRunningVersionsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1, 1),
    _GenEquipRfuRunningVersionsIfIndex_Type()
)
genEquipRfuRunningVersionsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsIfIndex.setStatus("mandatory")
_GenEquipRfuRunningVersionsDSP_Type = DisplayString
_GenEquipRfuRunningVersionsDSP_Object = MibTableColumn
genEquipRfuRunningVersionsDSP = _GenEquipRfuRunningVersionsDSP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1, 2),
    _GenEquipRfuRunningVersionsDSP_Type()
)
genEquipRfuRunningVersionsDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsDSP.setStatus("mandatory")
_GenEquipRfuRunningVersionsConfigurations_Type = DisplayString
_GenEquipRfuRunningVersionsConfigurations_Object = MibTableColumn
genEquipRfuRunningVersionsConfigurations = _GenEquipRfuRunningVersionsConfigurations_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1, 3),
    _GenEquipRfuRunningVersionsConfigurations_Type()
)
genEquipRfuRunningVersionsConfigurations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsConfigurations.setStatus("mandatory")
_GenEquipRfuRunningVersionsConstants_Type = DisplayString
_GenEquipRfuRunningVersionsConstants_Object = MibTableColumn
genEquipRfuRunningVersionsConstants = _GenEquipRfuRunningVersionsConstants_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1, 4),
    _GenEquipRfuRunningVersionsConstants_Type()
)
genEquipRfuRunningVersionsConstants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsConstants.setStatus("mandatory")
_GenEquipRfuRunningVersionsScripts_Type = DisplayString
_GenEquipRfuRunningVersionsScripts_Object = MibTableColumn
genEquipRfuRunningVersionsScripts = _GenEquipRfuRunningVersionsScripts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1, 5),
    _GenEquipRfuRunningVersionsScripts_Type()
)
genEquipRfuRunningVersionsScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsScripts.setStatus("mandatory")
_GenEquipRfuRunningVersionsFirmware_Type = DisplayString
_GenEquipRfuRunningVersionsFirmware_Object = MibTableColumn
genEquipRfuRunningVersionsFirmware = _GenEquipRfuRunningVersionsFirmware_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 5, 1, 6),
    _GenEquipRfuRunningVersionsFirmware_Type()
)
genEquipRfuRunningVersionsFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuRunningVersionsFirmware.setStatus("mandatory")
_GenEquipRfuAvailableVersionsTable_Object = MibTable
genEquipRfuAvailableVersionsTable = _GenEquipRfuAvailableVersionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6)
)
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsTable.setStatus("mandatory")
_GenEquipRfuAvailableVersionsEntry_Object = MibTableRow
genEquipRfuAvailableVersionsEntry = _GenEquipRfuAvailableVersionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1)
)
genEquipRfuAvailableVersionsEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRfuAvailableVersionsRfuType"),
)
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsEntry.setStatus("mandatory")
_GenEquipRfuAvailableVersionsRfuType_Type = RfuMajorType
_GenEquipRfuAvailableVersionsRfuType_Object = MibTableColumn
genEquipRfuAvailableVersionsRfuType = _GenEquipRfuAvailableVersionsRfuType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1, 1),
    _GenEquipRfuAvailableVersionsRfuType_Type()
)
genEquipRfuAvailableVersionsRfuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsRfuType.setStatus("mandatory")
_GenEquipRfuAvailableVersionsDSP_Type = DisplayString
_GenEquipRfuAvailableVersionsDSP_Object = MibTableColumn
genEquipRfuAvailableVersionsDSP = _GenEquipRfuAvailableVersionsDSP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1, 2),
    _GenEquipRfuAvailableVersionsDSP_Type()
)
genEquipRfuAvailableVersionsDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsDSP.setStatus("mandatory")
_GenEquipRfuAvailableVersionsConfigurations_Type = DisplayString
_GenEquipRfuAvailableVersionsConfigurations_Object = MibTableColumn
genEquipRfuAvailableVersionsConfigurations = _GenEquipRfuAvailableVersionsConfigurations_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1, 3),
    _GenEquipRfuAvailableVersionsConfigurations_Type()
)
genEquipRfuAvailableVersionsConfigurations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsConfigurations.setStatus("mandatory")
_GenEquipRfuAvailableVersionsConstants_Type = DisplayString
_GenEquipRfuAvailableVersionsConstants_Object = MibTableColumn
genEquipRfuAvailableVersionsConstants = _GenEquipRfuAvailableVersionsConstants_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1, 4),
    _GenEquipRfuAvailableVersionsConstants_Type()
)
genEquipRfuAvailableVersionsConstants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsConstants.setStatus("mandatory")
_GenEquipRfuAvailableVersionsScripts_Type = DisplayString
_GenEquipRfuAvailableVersionsScripts_Object = MibTableColumn
genEquipRfuAvailableVersionsScripts = _GenEquipRfuAvailableVersionsScripts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1, 5),
    _GenEquipRfuAvailableVersionsScripts_Type()
)
genEquipRfuAvailableVersionsScripts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsScripts.setStatus("mandatory")
_GenEquipRfuAvailableVersionsFirmware_Type = DisplayString
_GenEquipRfuAvailableVersionsFirmware_Object = MibTableColumn
genEquipRfuAvailableVersionsFirmware = _GenEquipRfuAvailableVersionsFirmware_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 5, 4, 6, 1, 6),
    _GenEquipRfuAvailableVersionsFirmware_Type()
)
genEquipRfuAvailableVersionsFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRfuAvailableVersionsFirmware.setStatus("mandatory")
_GenEquipRadio_ObjectIdentity = ObjectIdentity
genEquipRadio = _GenEquipRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7)
)
_GenEquipRadioStatusTable_Object = MibTable
genEquipRadioStatusTable = _GenEquipRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioStatusTable.setStatus("mandatory")
_GenEquipRadioStatusEntry_Object = MibTableRow
genEquipRadioStatusEntry = _GenEquipRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1)
)
genEquipRadioStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioStatusRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioStatusEntry.setStatus("mandatory")
_GenEquipRadioStatusRadioId_Type = RadioId
_GenEquipRadioStatusRadioId_Object = MibTableColumn
genEquipRadioStatusRadioId = _GenEquipRadioStatusRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1, 1),
    _GenEquipRadioStatusRadioId_Type()
)
genEquipRadioStatusRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioStatusRadioId.setStatus("mandatory")
_GenEquipRadioStatusMSE_Type = Integer32
_GenEquipRadioStatusMSE_Object = MibTableColumn
genEquipRadioStatusMSE = _GenEquipRadioStatusMSE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1, 2),
    _GenEquipRadioStatusMSE_Type()
)
genEquipRadioStatusMSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioStatusMSE.setStatus("mandatory")
_GenEquipRadioStatusDefectedBlocks_Type = Integer32
_GenEquipRadioStatusDefectedBlocks_Object = MibTableColumn
genEquipRadioStatusDefectedBlocks = _GenEquipRadioStatusDefectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1, 3),
    _GenEquipRadioStatusDefectedBlocks_Type()
)
genEquipRadioStatusDefectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioStatusDefectedBlocks.setStatus("mandatory")
_GenEquipRadioStatusBER_Type = ThresholdExponent
_GenEquipRadioStatusBER_Object = MibTableColumn
genEquipRadioStatusBER = _GenEquipRadioStatusBER_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1, 4),
    _GenEquipRadioStatusBER_Type()
)
genEquipRadioStatusBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioStatusBER.setStatus("mandatory")
_GenEquipRadioStatusXPI_Type = Integer32
_GenEquipRadioStatusXPI_Object = MibTableColumn
genEquipRadioStatusXPI = _GenEquipRadioStatusXPI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1, 5),
    _GenEquipRadioStatusXPI_Type()
)
genEquipRadioStatusXPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioStatusXPI.setStatus("mandatory")
_GenEquipRadioStatusXPICEnabled_Type = EnableDisableSMI2
_GenEquipRadioStatusXPICEnabled_Object = MibTableColumn
genEquipRadioStatusXPICEnabled = _GenEquipRadioStatusXPICEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 1, 1, 6),
    _GenEquipRadioStatusXPICEnabled_Type()
)
genEquipRadioStatusXPICEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioStatusXPICEnabled.setStatus("mandatory")
_GenEquipRadioCfgTable_Object = MibTable
genEquipRadioCfgTable = _GenEquipRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioCfgTable.setStatus("mandatory")
_GenEquipRadioCfgEntry_Object = MibTableRow
genEquipRadioCfgEntry = _GenEquipRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1)
)
genEquipRadioCfgEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCfgEntry.setStatus("mandatory")
_GenEquipRadioCfgRadioId_Type = RadioId
_GenEquipRadioCfgRadioId_Object = MibTableColumn
genEquipRadioCfgRadioId = _GenEquipRadioCfgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 1),
    _GenEquipRadioCfgRadioId_Type()
)
genEquipRadioCfgRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioId.setStatus("mandatory")


class _GenEquipRadioCfgLinkId_Type(Integer32):
    """Custom type genEquipRadioCfgLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GenEquipRadioCfgLinkId_Type.__name__ = "Integer32"
_GenEquipRadioCfgLinkId_Object = MibTableColumn
genEquipRadioCfgLinkId = _GenEquipRadioCfgLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 2),
    _GenEquipRadioCfgLinkId_Type()
)
genEquipRadioCfgLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgLinkId.setStatus("mandatory")
_GenEquipRadioCfgMACHeaderCompression_Type = EnableDisable
_GenEquipRadioCfgMACHeaderCompression_Object = MibTableColumn
genEquipRadioCfgMACHeaderCompression = _GenEquipRadioCfgMACHeaderCompression_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 3),
    _GenEquipRadioCfgMACHeaderCompression_Type()
)
genEquipRadioCfgMACHeaderCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgMACHeaderCompression.setStatus("mandatory")
_GenEquipRadioCfgClearCounters_Type = OffOn
_GenEquipRadioCfgClearCounters_Object = MibTableColumn
genEquipRadioCfgClearCounters = _GenEquipRadioCfgClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 4),
    _GenEquipRadioCfgClearCounters_Type()
)
genEquipRadioCfgClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgClearCounters.setStatus("mandatory")


class _GenEquipRadioCfgIfLoopback_Type(Integer32):
    """Custom type genEquipRadioCfgIfLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("towardsSystem", 1))
    )


_GenEquipRadioCfgIfLoopback_Type.__name__ = "Integer32"
_GenEquipRadioCfgIfLoopback_Object = MibTableColumn
genEquipRadioCfgIfLoopback = _GenEquipRadioCfgIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 5),
    _GenEquipRadioCfgIfLoopback_Type()
)
genEquipRadioCfgIfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgIfLoopback.setStatus("mandatory")
_GenEquipRadioCfgExcessiveBERThreshold_Type = ThresholdExponent
_GenEquipRadioCfgExcessiveBERThreshold_Object = MibTableColumn
genEquipRadioCfgExcessiveBERThreshold = _GenEquipRadioCfgExcessiveBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 6),
    _GenEquipRadioCfgExcessiveBERThreshold_Type()
)
genEquipRadioCfgExcessiveBERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgExcessiveBERThreshold.setStatus("mandatory")
_GenEquipRadioCfgSignalDegradeThreshold_Type = ThresholdExponent
_GenEquipRadioCfgSignalDegradeThreshold_Object = MibTableColumn
genEquipRadioCfgSignalDegradeThreshold = _GenEquipRadioCfgSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 7),
    _GenEquipRadioCfgSignalDegradeThreshold_Type()
)
genEquipRadioCfgSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgSignalDegradeThreshold.setStatus("mandatory")
_GenEquipRadioCfgRadioAdmin_Type = EnableDisable
_GenEquipRadioCfgRadioAdmin_Object = MibTableColumn
genEquipRadioCfgRadioAdmin = _GenEquipRadioCfgRadioAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 8),
    _GenEquipRadioCfgRadioAdmin_Type()
)
genEquipRadioCfgRadioAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioAdmin.setStatus("obsolete")
_GenEquipRadioCfgRadioOperationalStatus_Type = DownUp
_GenEquipRadioCfgRadioOperationalStatus_Object = MibTableColumn
genEquipRadioCfgRadioOperationalStatus = _GenEquipRadioCfgRadioOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 9),
    _GenEquipRadioCfgRadioOperationalStatus_Type()
)
genEquipRadioCfgRadioOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioOperationalStatus.setStatus("mandatory")


class _GenEquipRadioCfgRadioTrafficPriorityScheme_Type(Integer32):
    """Custom type genEquipRadioCfgRadioTrafficPriorityScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-ethernet-over-tdm", 1),
          ("high-tdm-over-ethernet", 0),
          ("high-tdm-over-high-ethernet", 2))
    )


_GenEquipRadioCfgRadioTrafficPriorityScheme_Type.__name__ = "Integer32"
_GenEquipRadioCfgRadioTrafficPriorityScheme_Object = MibTableColumn
genEquipRadioCfgRadioTrafficPriorityScheme = _GenEquipRadioCfgRadioTrafficPriorityScheme_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 10),
    _GenEquipRadioCfgRadioTrafficPriorityScheme_Type()
)
genEquipRadioCfgRadioTrafficPriorityScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioTrafficPriorityScheme.setStatus("mandatory")


class _GenEquipRadioCfgRadioHiPriorityEthernetBW_Type(Integer32):
    """Custom type genEquipRadioCfgRadioHiPriorityEthernetBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_GenEquipRadioCfgRadioHiPriorityEthernetBW_Type.__name__ = "Integer32"
_GenEquipRadioCfgRadioHiPriorityEthernetBW_Object = MibTableColumn
genEquipRadioCfgRadioHiPriorityEthernetBW = _GenEquipRadioCfgRadioHiPriorityEthernetBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 11),
    _GenEquipRadioCfgRadioHiPriorityEthernetBW_Type()
)
genEquipRadioCfgRadioHiPriorityEthernetBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioHiPriorityEthernetBW.setStatus("mandatory")
_GenEquipRadioCfgRadioMultiRadioEnable_Type = EnableDisable
_GenEquipRadioCfgRadioMultiRadioEnable_Object = MibTableColumn
genEquipRadioCfgRadioMultiRadioEnable = _GenEquipRadioCfgRadioMultiRadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 12),
    _GenEquipRadioCfgRadioMultiRadioEnable_Type()
)
genEquipRadioCfgRadioMultiRadioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioMultiRadioEnable.setStatus("mandatory")


class _GenEquipRadioCfgRadioMultiRadioBlockLocalTraffic_Type(Integer32):
    """Custom type genEquipRadioCfgRadioMultiRadioBlockLocalTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block-this-radio", 1),
          ("dont-block", 0))
    )


_GenEquipRadioCfgRadioMultiRadioBlockLocalTraffic_Type.__name__ = "Integer32"
_GenEquipRadioCfgRadioMultiRadioBlockLocalTraffic_Object = MibTableColumn
genEquipRadioCfgRadioMultiRadioBlockLocalTraffic = _GenEquipRadioCfgRadioMultiRadioBlockLocalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 13),
    _GenEquipRadioCfgRadioMultiRadioBlockLocalTraffic_Type()
)
genEquipRadioCfgRadioMultiRadioBlockLocalTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioMultiRadioBlockLocalTraffic.setStatus("mandatory")


class _GenEquipRadioCfgRadioMultiRadioBlockMateTraffic_Type(Integer32):
    """Custom type genEquipRadioCfgRadioMultiRadioBlockMateTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block-this-radio", 1),
          ("dont-block", 0))
    )


_GenEquipRadioCfgRadioMultiRadioBlockMateTraffic_Type.__name__ = "Integer32"
_GenEquipRadioCfgRadioMultiRadioBlockMateTraffic_Object = MibTableColumn
genEquipRadioCfgRadioMultiRadioBlockMateTraffic = _GenEquipRadioCfgRadioMultiRadioBlockMateTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 14),
    _GenEquipRadioCfgRadioMultiRadioBlockMateTraffic_Type()
)
genEquipRadioCfgRadioMultiRadioBlockMateTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioMultiRadioBlockMateTraffic.setStatus("mandatory")
_GenEquipRadioCfgRadioCurrentAvailableCapacity_Type = Integer32
_GenEquipRadioCfgRadioCurrentAvailableCapacity_Object = MibTableColumn
genEquipRadioCfgRadioCurrentAvailableCapacity = _GenEquipRadioCfgRadioCurrentAvailableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 15),
    _GenEquipRadioCfgRadioCurrentAvailableCapacity_Type()
)
genEquipRadioCfgRadioCurrentAvailableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioCurrentAvailableCapacity.setStatus("mandatory")
_GenEquipRadioCfgRadioMultiRadioExcessiveBERAdmin_Type = EnableDisable
_GenEquipRadioCfgRadioMultiRadioExcessiveBERAdmin_Object = MibTableColumn
genEquipRadioCfgRadioMultiRadioExcessiveBERAdmin = _GenEquipRadioCfgRadioMultiRadioExcessiveBERAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 16),
    _GenEquipRadioCfgRadioMultiRadioExcessiveBERAdmin_Type()
)
genEquipRadioCfgRadioMultiRadioExcessiveBERAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioMultiRadioExcessiveBERAdmin.setStatus("mandatory")
_GenEquipRadioCfgRadioMultiRadioSignalDegradeAdmin_Type = EnableDisable
_GenEquipRadioCfgRadioMultiRadioSignalDegradeAdmin_Object = MibTableColumn
genEquipRadioCfgRadioMultiRadioSignalDegradeAdmin = _GenEquipRadioCfgRadioMultiRadioSignalDegradeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 17),
    _GenEquipRadioCfgRadioMultiRadioSignalDegradeAdmin_Type()
)
genEquipRadioCfgRadioMultiRadioSignalDegradeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgRadioMultiRadioSignalDegradeAdmin.setStatus("mandatory")
_GenEquipRadioCfgEnAlarmGenOnRslDegrade_Type = EnableDisable
_GenEquipRadioCfgEnAlarmGenOnRslDegrade_Object = MibTableColumn
genEquipRadioCfgEnAlarmGenOnRslDegrade = _GenEquipRadioCfgEnAlarmGenOnRslDegrade_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 18),
    _GenEquipRadioCfgEnAlarmGenOnRslDegrade_Type()
)
genEquipRadioCfgEnAlarmGenOnRslDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgEnAlarmGenOnRslDegrade.setStatus("mandatory")


class _GenEquipRadioCfgAlarmGenRslNominalLevel_Type(Integer32):
    """Custom type genEquipRadioCfgAlarmGenRslNominalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_GenEquipRadioCfgAlarmGenRslNominalLevel_Type.__name__ = "Integer32"
_GenEquipRadioCfgAlarmGenRslNominalLevel_Object = MibTableColumn
genEquipRadioCfgAlarmGenRslNominalLevel = _GenEquipRadioCfgAlarmGenRslNominalLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 19),
    _GenEquipRadioCfgAlarmGenRslNominalLevel_Type()
)
genEquipRadioCfgAlarmGenRslNominalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgAlarmGenRslNominalLevel.setStatus("mandatory")


class _GenEquipRadioCfgAlarmGenRslDegradationMargin_Type(Integer32):
    """Custom type genEquipRadioCfgAlarmGenRslDegradationMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_GenEquipRadioCfgAlarmGenRslDegradationMargin_Type.__name__ = "Integer32"
_GenEquipRadioCfgAlarmGenRslDegradationMargin_Object = MibTableColumn
genEquipRadioCfgAlarmGenRslDegradationMargin = _GenEquipRadioCfgAlarmGenRslDegradationMargin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 20),
    _GenEquipRadioCfgAlarmGenRslDegradationMargin_Type()
)
genEquipRadioCfgAlarmGenRslDegradationMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgAlarmGenRslDegradationMargin.setStatus("mandatory")
_GenEquipRadioCfgLinkShutDownOnRadioFailure_Type = EnableDisable
_GenEquipRadioCfgLinkShutDownOnRadioFailure_Object = MibTableColumn
genEquipRadioCfgLinkShutDownOnRadioFailure = _GenEquipRadioCfgLinkShutDownOnRadioFailure_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 21),
    _GenEquipRadioCfgLinkShutDownOnRadioFailure_Type()
)
genEquipRadioCfgLinkShutDownOnRadioFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgLinkShutDownOnRadioFailure.setStatus("mandatory")


class _GenEquipRadioCfgLoopbackTimeout_Type(Integer32):
    """Custom type genEquipRadioCfgLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GenEquipRadioCfgLoopbackTimeout_Type.__name__ = "Integer32"
_GenEquipRadioCfgLoopbackTimeout_Object = MibTableColumn
genEquipRadioCfgLoopbackTimeout = _GenEquipRadioCfgLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 22),
    _GenEquipRadioCfgLoopbackTimeout_Type()
)
genEquipRadioCfgLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgLoopbackTimeout.setStatus("mandatory")


class _GenEquipRadioCfgAbcMode_Type(Integer32):
    """Custom type genEquipRadioCfgAbcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multi-carrier-abc", 2),
          ("multi-directional", 3))
    )


_GenEquipRadioCfgAbcMode_Type.__name__ = "Integer32"
_GenEquipRadioCfgAbcMode_Object = MibTableColumn
genEquipRadioCfgAbcMode = _GenEquipRadioCfgAbcMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 2, 1, 23),
    _GenEquipRadioCfgAbcMode_Type()
)
genEquipRadioCfgAbcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCfgAbcMode.setStatus("mandatory")
_GenEquipRemoteRadio_ObjectIdentity = ObjectIdentity
genEquipRemoteRadio = _GenEquipRemoteRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3)
)
_GenEquipRemoteRadioTable_Object = MibTable
genEquipRemoteRadioTable = _GenEquipRemoteRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1)
)
if mibBuilder.loadTexts:
    genEquipRemoteRadioTable.setStatus("mandatory")
_GenEquipRemoteRadioEntry_Object = MibTableRow
genEquipRemoteRadioEntry = _GenEquipRemoteRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1)
)
genEquipRemoteRadioEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRemoteRadioRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRemoteRadioEntry.setStatus("mandatory")
_GenEquipRemoteRadioRadioId_Type = RadioId
_GenEquipRemoteRadioRadioId_Object = MibTableColumn
genEquipRemoteRadioRadioId = _GenEquipRemoteRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 1),
    _GenEquipRemoteRadioRadioId_Type()
)
genEquipRemoteRadioRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRadioId.setStatus("mandatory")
_GenEquipRemoteRadioRemoteCommunication_Type = DownUp
_GenEquipRemoteRadioRemoteCommunication_Object = MibTableColumn
genEquipRemoteRadioRemoteCommunication = _GenEquipRemoteRadioRemoteCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 2),
    _GenEquipRemoteRadioRemoteCommunication_Type()
)
genEquipRemoteRadioRemoteCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteCommunication.setStatus("mandatory")
_GenEquipRemoteRadioRemoteIPAddr_Type = IpAddress
_GenEquipRemoteRadioRemoteIPAddr_Object = MibTableColumn
genEquipRemoteRadioRemoteIPAddr = _GenEquipRemoteRadioRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 3),
    _GenEquipRemoteRadioRemoteIPAddr_Type()
)
genEquipRemoteRadioRemoteIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteIPAddr.setStatus("mandatory")


class _GenEquipRemoteRadioRemoteRxLevel_Type(Integer32):
    """Custom type genEquipRemoteRadioRemoteRxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-199, 0),
    )


_GenEquipRemoteRadioRemoteRxLevel_Type.__name__ = "Integer32"
_GenEquipRemoteRadioRemoteRxLevel_Object = MibTableColumn
genEquipRemoteRadioRemoteRxLevel = _GenEquipRemoteRadioRemoteRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 4),
    _GenEquipRemoteRadioRemoteRxLevel_Type()
)
genEquipRemoteRadioRemoteRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteRxLevel.setStatus("mandatory")


class _GenEquipRemoteRadioRemoteForceMaxTxLevel_Type(Integer32):
    """Custom type genEquipRemoteRadioRemoteForceMaxTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 34),
    )


_GenEquipRemoteRadioRemoteForceMaxTxLevel_Type.__name__ = "Integer32"
_GenEquipRemoteRadioRemoteForceMaxTxLevel_Object = MibTableColumn
genEquipRemoteRadioRemoteForceMaxTxLevel = _GenEquipRemoteRadioRemoteForceMaxTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 5),
    _GenEquipRemoteRadioRemoteForceMaxTxLevel_Type()
)
genEquipRemoteRadioRemoteForceMaxTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteForceMaxTxLevel.setStatus("mandatory")
_GenEquipRemoteRadioRemoteTxFreq_Type = Integer32
_GenEquipRemoteRadioRemoteTxFreq_Object = MibTableColumn
genEquipRemoteRadioRemoteTxFreq = _GenEquipRemoteRadioRemoteTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 6),
    _GenEquipRemoteRadioRemoteTxFreq_Type()
)
genEquipRemoteRadioRemoteTxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteTxFreq.setStatus("mandatory")
_GenEquipRemoteRadioRemoteRxFreq_Type = Integer32
_GenEquipRemoteRadioRemoteRxFreq_Object = MibTableColumn
genEquipRemoteRadioRemoteRxFreq = _GenEquipRemoteRadioRemoteRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 7),
    _GenEquipRemoteRadioRemoteRxFreq_Type()
)
genEquipRemoteRadioRemoteRxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteRxFreq.setStatus("mandatory")


class _GenEquipRemoteRadioRemoteATPCReferenceRxLevel_Type(Integer32):
    """Custom type genEquipRemoteRadioRemoteATPCReferenceRxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_GenEquipRemoteRadioRemoteATPCReferenceRxLevel_Type.__name__ = "Integer32"
_GenEquipRemoteRadioRemoteATPCReferenceRxLevel_Object = MibTableColumn
genEquipRemoteRadioRemoteATPCReferenceRxLevel = _GenEquipRemoteRadioRemoteATPCReferenceRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 8),
    _GenEquipRemoteRadioRemoteATPCReferenceRxLevel_Type()
)
genEquipRemoteRadioRemoteATPCReferenceRxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteATPCReferenceRxLevel.setStatus("mandatory")
_GenEquipRemoteRadioRemoteFloatingIPAddr_Type = IpAddress
_GenEquipRemoteRadioRemoteFloatingIPAddr_Object = MibTableColumn
genEquipRemoteRadioRemoteFloatingIPAddr = _GenEquipRemoteRadioRemoteFloatingIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 9),
    _GenEquipRemoteRadioRemoteFloatingIPAddr_Type()
)
genEquipRemoteRadioRemoteFloatingIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteFloatingIPAddr.setStatus("mandatory")
_GenEquipRemoteRadioRemoteDefaultGateway_Type = IpAddress
_GenEquipRemoteRadioRemoteDefaultGateway_Object = MibTableColumn
genEquipRemoteRadioRemoteDefaultGateway = _GenEquipRemoteRadioRemoteDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 10),
    _GenEquipRemoteRadioRemoteDefaultGateway_Type()
)
genEquipRemoteRadioRemoteDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteDefaultGateway.setStatus("mandatory")
_GenEquipRemoteRadioRemoteMostSevereAlarm_Type = Severity
_GenEquipRemoteRadioRemoteMostSevereAlarm_Object = MibTableColumn
genEquipRemoteRadioRemoteMostSevereAlarm = _GenEquipRemoteRadioRemoteMostSevereAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 11),
    _GenEquipRemoteRadioRemoteMostSevereAlarm_Type()
)
genEquipRemoteRadioRemoteMostSevereAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteMostSevereAlarm.setStatus("mandatory")
_GenEquipRemoteRadioRemoteSubnetMask_Type = IpAddress
_GenEquipRemoteRadioRemoteSubnetMask_Object = MibTableColumn
genEquipRemoteRadioRemoteSubnetMask = _GenEquipRemoteRadioRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 12),
    _GenEquipRemoteRadioRemoteSubnetMask_Type()
)
genEquipRemoteRadioRemoteSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteSubnetMask.setStatus("mandatory")


class _GenEquipRemoteRadioRemoteSlotID_Type(Integer32):
    """Custom type genEquipRemoteRadioRemoteSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_GenEquipRemoteRadioRemoteSlotID_Type.__name__ = "Integer32"
_GenEquipRemoteRadioRemoteSlotID_Object = MibTableColumn
genEquipRemoteRadioRemoteSlotID = _GenEquipRemoteRadioRemoteSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 13),
    _GenEquipRemoteRadioRemoteSlotID_Type()
)
genEquipRemoteRadioRemoteSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteSlotID.setStatus("mandatory")
_GenEquipRemoteRadioRemoteForceTxMute_Type = OffOn
_GenEquipRemoteRadioRemoteForceTxMute_Object = MibTableColumn
genEquipRemoteRadioRemoteForceTxMute = _GenEquipRemoteRadioRemoteForceTxMute_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 14),
    _GenEquipRemoteRadioRemoteForceTxMute_Type()
)
genEquipRemoteRadioRemoteForceTxMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteForceTxMute.setStatus("mandatory")
_GenEquipRemoteRadioRemoteLinkId_Type = Integer32
_GenEquipRemoteRadioRemoteLinkId_Object = MibTableColumn
genEquipRemoteRadioRemoteLinkId = _GenEquipRemoteRadioRemoteLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 15),
    _GenEquipRemoteRadioRemoteLinkId_Type()
)
genEquipRemoteRadioRemoteLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteLinkId.setStatus("mandatory")
_GenEquipRemoteRadioRemoteATPCoverrideState_Type = NoYes
_GenEquipRemoteRadioRemoteATPCoverrideState_Object = MibTableColumn
genEquipRemoteRadioRemoteATPCoverrideState = _GenEquipRemoteRadioRemoteATPCoverrideState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 16),
    _GenEquipRemoteRadioRemoteATPCoverrideState_Type()
)
genEquipRemoteRadioRemoteATPCoverrideState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteATPCoverrideState.setStatus("mandatory")
_GenEquipRemoteRadioRemoteATPCoverrideStateCancel_Type = NoYes
_GenEquipRemoteRadioRemoteATPCoverrideStateCancel_Object = MibTableColumn
genEquipRemoteRadioRemoteATPCoverrideStateCancel = _GenEquipRemoteRadioRemoteATPCoverrideStateCancel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 17),
    _GenEquipRemoteRadioRemoteATPCoverrideStateCancel_Type()
)
genEquipRemoteRadioRemoteATPCoverrideStateCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteATPCoverrideStateCancel.setStatus("mandatory")
_GenEquipRemoteRadioRemoteDataLoopBackAdmin_Type = EnableDisable
_GenEquipRemoteRadioRemoteDataLoopBackAdmin_Object = MibTableColumn
genEquipRemoteRadioRemoteDataLoopBackAdmin = _GenEquipRemoteRadioRemoteDataLoopBackAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 18),
    _GenEquipRemoteRadioRemoteDataLoopBackAdmin_Type()
)
genEquipRemoteRadioRemoteDataLoopBackAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteDataLoopBackAdmin.setStatus("mandatory")
_GenEquipRemoteRadioRemoteDataLoopBackDuration_Type = Integer32
_GenEquipRemoteRadioRemoteDataLoopBackDuration_Object = MibTableColumn
genEquipRemoteRadioRemoteDataLoopBackDuration = _GenEquipRemoteRadioRemoteDataLoopBackDuration_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 19),
    _GenEquipRemoteRadioRemoteDataLoopBackDuration_Type()
)
genEquipRemoteRadioRemoteDataLoopBackDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteDataLoopBackDuration.setStatus("mandatory")
_GenEquipRemoteRadioRemoteDataLoopBackSwitchAddress_Type = EnableDisable
_GenEquipRemoteRadioRemoteDataLoopBackSwitchAddress_Object = MibTableColumn
genEquipRemoteRadioRemoteDataLoopBackSwitchAddress = _GenEquipRemoteRadioRemoteDataLoopBackSwitchAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 20),
    _GenEquipRemoteRadioRemoteDataLoopBackSwitchAddress_Type()
)
genEquipRemoteRadioRemoteDataLoopBackSwitchAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteDataLoopBackSwitchAddress.setStatus("mandatory")
_GenEquipRemoteRadioRemoteGreenReferenceRxLevel_Type = Integer32
_GenEquipRemoteRadioRemoteGreenReferenceRxLevel_Object = MibTableColumn
genEquipRemoteRadioRemoteGreenReferenceRxLevel = _GenEquipRemoteRadioRemoteGreenReferenceRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 21),
    _GenEquipRemoteRadioRemoteGreenReferenceRxLevel_Type()
)
genEquipRemoteRadioRemoteGreenReferenceRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteGreenReferenceRxLevel.setStatus("mandatory")
_GenEquipRemoteRadioRemoteMNGvlan_Type = Integer32
_GenEquipRemoteRadioRemoteMNGvlan_Object = MibTableColumn
genEquipRemoteRadioRemoteMNGvlan = _GenEquipRemoteRadioRemoteMNGvlan_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 22),
    _GenEquipRemoteRadioRemoteMNGvlan_Type()
)
genEquipRemoteRadioRemoteMNGvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteMNGvlan.setStatus("mandatory")
_GenEquipRemoteRadioRemoteReset_Type = FalseTrue
_GenEquipRemoteRadioRemoteReset_Object = MibTableColumn
genEquipRemoteRadioRemoteReset = _GenEquipRemoteRadioRemoteReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 23),
    _GenEquipRemoteRadioRemoteReset_Type()
)
genEquipRemoteRadioRemoteReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteReset.setStatus("mandatory")
_GenEquipRemoteRadioRemoteGreenModeAdmin_Type = EnableDisable
_GenEquipRemoteRadioRemoteGreenModeAdmin_Object = MibTableColumn
genEquipRemoteRadioRemoteGreenModeAdmin = _GenEquipRemoteRadioRemoteGreenModeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 24),
    _GenEquipRemoteRadioRemoteGreenModeAdmin_Type()
)
genEquipRemoteRadioRemoteGreenModeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteGreenModeAdmin.setStatus("mandatory")
_GenEquipRemoteRadioRemoteWebProtocol_Type = CommunicationChannel
_GenEquipRemoteRadioRemoteWebProtocol_Object = MibTableColumn
genEquipRemoteRadioRemoteWebProtocol = _GenEquipRemoteRadioRemoteWebProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 25),
    _GenEquipRemoteRadioRemoteWebProtocol_Type()
)
genEquipRemoteRadioRemoteWebProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteWebProtocol.setStatus("mandatory")


class _GenEquipRemoteRadioRemoteIPv6Addr_Type(OctetString):
    """Custom type genEquipRemoteRadioRemoteIPv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipRemoteRadioRemoteIPv6Addr_Type.__name__ = "OctetString"
_GenEquipRemoteRadioRemoteIPv6Addr_Object = MibTableColumn
genEquipRemoteRadioRemoteIPv6Addr = _GenEquipRemoteRadioRemoteIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 26),
    _GenEquipRemoteRadioRemoteIPv6Addr_Type()
)
genEquipRemoteRadioRemoteIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteIPv6Addr.setStatus("mandatory")
_GenEquipRemoteRadioRemotePrefixLength_Type = Integer32
_GenEquipRemoteRadioRemotePrefixLength_Object = MibTableColumn
genEquipRemoteRadioRemotePrefixLength = _GenEquipRemoteRadioRemotePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 27),
    _GenEquipRemoteRadioRemotePrefixLength_Type()
)
genEquipRemoteRadioRemotePrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemotePrefixLength.setStatus("mandatory")


class _GenEquipRemoteRadioRemoteDefaultGatewayIpv6_Type(OctetString):
    """Custom type genEquipRemoteRadioRemoteDefaultGatewayIpv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GenEquipRemoteRadioRemoteDefaultGatewayIpv6_Type.__name__ = "OctetString"
_GenEquipRemoteRadioRemoteDefaultGatewayIpv6_Object = MibTableColumn
genEquipRemoteRadioRemoteDefaultGatewayIpv6 = _GenEquipRemoteRadioRemoteDefaultGatewayIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 28),
    _GenEquipRemoteRadioRemoteDefaultGatewayIpv6_Type()
)
genEquipRemoteRadioRemoteDefaultGatewayIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteDefaultGatewayIpv6.setStatus("mandatory")
_GenEquipRemoteRadioRemoteResetSlot_Type = FalseTrue
_GenEquipRemoteRadioRemoteResetSlot_Object = MibTableColumn
genEquipRemoteRadioRemoteResetSlot = _GenEquipRemoteRadioRemoteResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 3, 1, 1, 29),
    _GenEquipRemoteRadioRemoteResetSlot_Type()
)
genEquipRemoteRadioRemoteResetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRemoteRadioRemoteResetSlot.setStatus("mandatory")
_GenEquipRadioMRMC_ObjectIdentity = ObjectIdentity
genEquipRadioMRMC = _GenEquipRadioMRMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4)
)
_GenEquipRadioMRMCTable_Object = MibTable
genEquipRadioMRMCTable = _GenEquipRadioMRMCTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCTable.setStatus("mandatory")
_GenEquipRadioMRMCEntry_Object = MibTableRow
genEquipRadioMRMCEntry = _GenEquipRadioMRMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1)
)
genEquipRadioMRMCEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCEntry.setStatus("mandatory")
_GenEquipRadioMRMCRadioId_Type = RadioId
_GenEquipRadioMRMCRadioId_Object = MibTableColumn
genEquipRadioMRMCRadioId = _GenEquipRadioMRMCRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 1),
    _GenEquipRadioMRMCRadioId_Type()
)
genEquipRadioMRMCRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCRadioId.setStatus("mandatory")
_GenEquipRadioMRMCSelectedScriptIndex_Type = Integer32
_GenEquipRadioMRMCSelectedScriptIndex_Object = MibTableColumn
genEquipRadioMRMCSelectedScriptIndex = _GenEquipRadioMRMCSelectedScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 2),
    _GenEquipRadioMRMCSelectedScriptIndex_Type()
)
genEquipRadioMRMCSelectedScriptIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCSelectedScriptIndex.setStatus("mandatory")
_GenEquipRadioMRMCOccupidBandwidth_Type = Integer32
_GenEquipRadioMRMCOccupidBandwidth_Object = MibTableColumn
genEquipRadioMRMCOccupidBandwidth = _GenEquipRadioMRMCOccupidBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 3),
    _GenEquipRadioMRMCOccupidBandwidth_Type()
)
genEquipRadioMRMCOccupidBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCOccupidBandwidth.setStatus("mandatory")


class _GenEquipRadioMRMCOperMode_Type(Integer32):
    """Custom type genEquipRadioMRMCOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acm-adaptive-mode", 2),
          ("acm-fixed-mode", 1),
          ("regular-mode", 0))
    )


_GenEquipRadioMRMCOperMode_Type.__name__ = "Integer32"
_GenEquipRadioMRMCOperMode_Object = MibTableColumn
genEquipRadioMRMCOperMode = _GenEquipRadioMRMCOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 4),
    _GenEquipRadioMRMCOperMode_Type()
)
genEquipRadioMRMCOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCOperMode.setStatus("mandatory")
_GenEquipRadioMRMCCurrTxProfile_Type = MrmcProfile
_GenEquipRadioMRMCCurrTxProfile_Object = MibTableColumn
genEquipRadioMRMCCurrTxProfile = _GenEquipRadioMRMCCurrTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 5),
    _GenEquipRadioMRMCCurrTxProfile_Type()
)
genEquipRadioMRMCCurrTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrTxProfile.setStatus("mandatory")


class _GenEquipRadioMRMCCurrTxQAM_Type(Integer32):
    """Custom type genEquipRadioMRMCCurrTxQAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 2048),
    )


_GenEquipRadioMRMCCurrTxQAM_Type.__name__ = "Integer32"
_GenEquipRadioMRMCCurrTxQAM_Object = MibTableColumn
genEquipRadioMRMCCurrTxQAM = _GenEquipRadioMRMCCurrTxQAM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 6),
    _GenEquipRadioMRMCCurrTxQAM_Type()
)
genEquipRadioMRMCCurrTxQAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrTxQAM.setStatus("mandatory")
_GenEquipRadioMRMCCurrTxBitrate_Type = MrmcBitRate
_GenEquipRadioMRMCCurrTxBitrate_Object = MibTableColumn
genEquipRadioMRMCCurrTxBitrate = _GenEquipRadioMRMCCurrTxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 7),
    _GenEquipRadioMRMCCurrTxBitrate_Type()
)
genEquipRadioMRMCCurrTxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrTxBitrate.setStatus("mandatory")


class _GenEquipRadioMRMCCurrTxVc_Type(Integer32):
    """Custom type genEquipRadioMRMCCurrTxVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GenEquipRadioMRMCCurrTxVc_Type.__name__ = "Integer32"
_GenEquipRadioMRMCCurrTxVc_Object = MibTableColumn
genEquipRadioMRMCCurrTxVc = _GenEquipRadioMRMCCurrTxVc_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 8),
    _GenEquipRadioMRMCCurrTxVc_Type()
)
genEquipRadioMRMCCurrTxVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrTxVc.setStatus("mandatory")
_GenEquipRadioMRMCCurrRxProfile_Type = MrmcProfile
_GenEquipRadioMRMCCurrRxProfile_Object = MibTableColumn
genEquipRadioMRMCCurrRxProfile = _GenEquipRadioMRMCCurrRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 9),
    _GenEquipRadioMRMCCurrRxProfile_Type()
)
genEquipRadioMRMCCurrRxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrRxProfile.setStatus("mandatory")


class _GenEquipRadioMRMCCurrRxQAM_Type(Integer32):
    """Custom type genEquipRadioMRMCCurrRxQAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 2048),
    )


_GenEquipRadioMRMCCurrRxQAM_Type.__name__ = "Integer32"
_GenEquipRadioMRMCCurrRxQAM_Object = MibTableColumn
genEquipRadioMRMCCurrRxQAM = _GenEquipRadioMRMCCurrRxQAM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 10),
    _GenEquipRadioMRMCCurrRxQAM_Type()
)
genEquipRadioMRMCCurrRxQAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrRxQAM.setStatus("mandatory")
_GenEquipRadioMRMCCurrRxBitrate_Type = MrmcBitRate
_GenEquipRadioMRMCCurrRxBitrate_Object = MibTableColumn
genEquipRadioMRMCCurrRxBitrate = _GenEquipRadioMRMCCurrRxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 11),
    _GenEquipRadioMRMCCurrRxBitrate_Type()
)
genEquipRadioMRMCCurrRxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrRxBitrate.setStatus("mandatory")


class _GenEquipRadioMRMCCurrRxVc_Type(Integer32):
    """Custom type genEquipRadioMRMCCurrRxVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GenEquipRadioMRMCCurrRxVc_Type.__name__ = "Integer32"
_GenEquipRadioMRMCCurrRxVc_Object = MibTableColumn
genEquipRadioMRMCCurrRxVc = _GenEquipRadioMRMCCurrRxVc_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 12),
    _GenEquipRadioMRMCCurrRxVc_Type()
)
genEquipRadioMRMCCurrRxVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrRxVc.setStatus("mandatory")
_GenEquipRadioMRMCCurrGrade_Type = RfuGrade
_GenEquipRadioMRMCCurrGrade_Object = MibTableColumn
genEquipRadioMRMCCurrGrade = _GenEquipRadioMRMCCurrGrade_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 13),
    _GenEquipRadioMRMCCurrGrade_Type()
)
genEquipRadioMRMCCurrGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCCurrGrade.setStatus("mandatory")
_GenEquipRadioMRMCEnAlarmOnAcmProfileDegrade_Type = EnableDisable
_GenEquipRadioMRMCEnAlarmOnAcmProfileDegrade_Object = MibTableColumn
genEquipRadioMRMCEnAlarmOnAcmProfileDegrade = _GenEquipRadioMRMCEnAlarmOnAcmProfileDegrade_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 14),
    _GenEquipRadioMRMCEnAlarmOnAcmProfileDegrade_Type()
)
genEquipRadioMRMCEnAlarmOnAcmProfileDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCEnAlarmOnAcmProfileDegrade.setStatus("mandatory")


class _GenEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold_Type(Integer32):
    """Custom type genEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_GenEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold_Type.__name__ = "Integer32"
_GenEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold_Object = MibTableColumn
genEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold = _GenEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 1, 1, 15),
    _GenEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold_Type()
)
genEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold.setStatus("mandatory")
_GenEquipRadioMRMCScriptTable_Object = MibTable
genEquipRadioMRMCScriptTable = _GenEquipRadioMRMCScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptTable.setStatus("mandatory")
_GenEquipRadioMRMCScriptEntry_Object = MibTableRow
genEquipRadioMRMCScriptEntry = _GenEquipRadioMRMCScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1)
)
genEquipRadioMRMCScriptEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCScriptRadioId"),
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCScriptIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptEntry.setStatus("mandatory")
_GenEquipRadioMRMCScriptRadioId_Type = RadioId
_GenEquipRadioMRMCScriptRadioId_Object = MibTableColumn
genEquipRadioMRMCScriptRadioId = _GenEquipRadioMRMCScriptRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 1),
    _GenEquipRadioMRMCScriptRadioId_Type()
)
genEquipRadioMRMCScriptRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptRadioId.setStatus("mandatory")
_GenEquipRadioMRMCScriptIndex_Type = Integer32
_GenEquipRadioMRMCScriptIndex_Object = MibTableColumn
genEquipRadioMRMCScriptIndex = _GenEquipRadioMRMCScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 2),
    _GenEquipRadioMRMCScriptIndex_Type()
)
genEquipRadioMRMCScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptIndex.setStatus("mandatory")
_GenEquipRadioMRMCScriptName_Type = DisplayString
_GenEquipRadioMRMCScriptName_Object = MibTableColumn
genEquipRadioMRMCScriptName = _GenEquipRadioMRMCScriptName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 3),
    _GenEquipRadioMRMCScriptName_Type()
)
genEquipRadioMRMCScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptName.setStatus("mandatory")


class _GenEquipRadioMRMCScriptOperMode_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acm-adaptive-mode", 2),
          ("acm-fixed-mode", 1),
          ("regular-mode", 0))
    )


_GenEquipRadioMRMCScriptOperMode_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptOperMode_Object = MibTableColumn
genEquipRadioMRMCScriptOperMode = _GenEquipRadioMRMCScriptOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 4),
    _GenEquipRadioMRMCScriptOperMode_Type()
)
genEquipRadioMRMCScriptOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptOperMode.setStatus("mandatory")
_GenEquipRadioMRMCScriptProfile_Type = MrmcProfile
_GenEquipRadioMRMCScriptProfile_Object = MibTableColumn
genEquipRadioMRMCScriptProfile = _GenEquipRadioMRMCScriptProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 5),
    _GenEquipRadioMRMCScriptProfile_Type()
)
genEquipRadioMRMCScriptProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptProfile.setStatus("mandatory")
_GenEquipRadioMRMCScriptProfileBitrate_Type = MrmcBitRate
_GenEquipRadioMRMCScriptProfileBitrate_Object = MibTableColumn
genEquipRadioMRMCScriptProfileBitrate = _GenEquipRadioMRMCScriptProfileBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 6),
    _GenEquipRadioMRMCScriptProfileBitrate_Type()
)
genEquipRadioMRMCScriptProfileBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptProfileBitrate.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAdaptivePower_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAdaptivePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable-adaptive-power", 1),
          ("enable-adaptive-power", 0))
    )


_GenEquipRadioMRMCScriptAdaptivePower_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAdaptivePower_Object = MibTableColumn
genEquipRadioMRMCScriptAdaptivePower = _GenEquipRadioMRMCScriptAdaptivePower_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 7),
    _GenEquipRadioMRMCScriptAdaptivePower_Type()
)
genEquipRadioMRMCScriptAdaptivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAdaptivePower.setStatus("mandatory")


class _GenEquipRadioMRMCScriptReference_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptReference based on Integer32"""
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
        *(("calss-2", 0),
          ("class-4", 1),
          ("class-5b", 2),
          ("class-6a", 3),
          ("fcc", 4))
    )


_GenEquipRadioMRMCScriptReference_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptReference_Object = MibTableColumn
genEquipRadioMRMCScriptReference = _GenEquipRadioMRMCScriptReference_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 8),
    _GenEquipRadioMRMCScriptReference_Type()
)
genEquipRadioMRMCScriptReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptReference.setStatus("mandatory")
_GenEquipRadioMRMCScriptMinProfile_Type = MrmcProfile
_GenEquipRadioMRMCScriptMinProfile_Object = MibTableColumn
genEquipRadioMRMCScriptMinProfile = _GenEquipRadioMRMCScriptMinProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 2, 1, 9),
    _GenEquipRadioMRMCScriptMinProfile_Type()
)
genEquipRadioMRMCScriptMinProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptMinProfile.setStatus("mandatory")
_GenEquipRadioMRMCFilteredTable_Object = MibTable
genEquipRadioMRMCFilteredTable = _GenEquipRadioMRMCFilteredTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCFilteredTable.setStatus("mandatory")
_GenEquipRadioMRMCFilteredEntry_Object = MibTableRow
genEquipRadioMRMCFilteredEntry = _GenEquipRadioMRMCFilteredEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 3, 1)
)
genEquipRadioMRMCFilteredEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCFilteredRadioId"),
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCFilteredScriptId"),
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCFilteredEntry.setStatus("mandatory")
_GenEquipRadioMRMCFilteredRadioId_Type = RadioId
_GenEquipRadioMRMCFilteredRadioId_Object = MibTableColumn
genEquipRadioMRMCFilteredRadioId = _GenEquipRadioMRMCFilteredRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 3, 1, 1),
    _GenEquipRadioMRMCFilteredRadioId_Type()
)
genEquipRadioMRMCFilteredRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCFilteredRadioId.setStatus("mandatory")
_GenEquipRadioMRMCFilteredScriptId_Type = MrmcScriptId
_GenEquipRadioMRMCFilteredScriptId_Object = MibTableColumn
genEquipRadioMRMCFilteredScriptId = _GenEquipRadioMRMCFilteredScriptId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 3, 1, 2),
    _GenEquipRadioMRMCFilteredScriptId_Type()
)
genEquipRadioMRMCFilteredScriptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCFilteredScriptId.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrTable_Object = MibTable
genEquipRadioMRMCProfileAttrTable = _GenEquipRadioMRMCProfileAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4)
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrTable.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrEntry_Object = MibTableRow
genEquipRadioMRMCProfileAttrEntry = _GenEquipRadioMRMCProfileAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1)
)
genEquipRadioMRMCProfileAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCProfileAttrScriptId"),
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCProfileAttrTxProfile"),
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCProfileAttrRxProfile"),
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrEntry.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrScriptId_Type = MrmcScriptId
_GenEquipRadioMRMCProfileAttrScriptId_Object = MibTableColumn
genEquipRadioMRMCProfileAttrScriptId = _GenEquipRadioMRMCProfileAttrScriptId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 1),
    _GenEquipRadioMRMCProfileAttrScriptId_Type()
)
genEquipRadioMRMCProfileAttrScriptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrScriptId.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrTxProfile_Type = MrmcProfile
_GenEquipRadioMRMCProfileAttrTxProfile_Object = MibTableColumn
genEquipRadioMRMCProfileAttrTxProfile = _GenEquipRadioMRMCProfileAttrTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 2),
    _GenEquipRadioMRMCProfileAttrTxProfile_Type()
)
genEquipRadioMRMCProfileAttrTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrTxProfile.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrRxProfile_Type = MrmcProfile
_GenEquipRadioMRMCProfileAttrRxProfile_Object = MibTableColumn
genEquipRadioMRMCProfileAttrRxProfile = _GenEquipRadioMRMCProfileAttrRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 3),
    _GenEquipRadioMRMCProfileAttrRxProfile_Type()
)
genEquipRadioMRMCProfileAttrRxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrRxProfile.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrTxQAM_Type = QamOrder
_GenEquipRadioMRMCProfileAttrTxQAM_Object = MibTableColumn
genEquipRadioMRMCProfileAttrTxQAM = _GenEquipRadioMRMCProfileAttrTxQAM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 4),
    _GenEquipRadioMRMCProfileAttrTxQAM_Type()
)
genEquipRadioMRMCProfileAttrTxQAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrTxQAM.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrTxBitRate_Type = MrmcBitRate
_GenEquipRadioMRMCProfileAttrTxBitRate_Object = MibTableColumn
genEquipRadioMRMCProfileAttrTxBitRate = _GenEquipRadioMRMCProfileAttrTxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 5),
    _GenEquipRadioMRMCProfileAttrTxBitRate_Type()
)
genEquipRadioMRMCProfileAttrTxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrTxBitRate.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrRxQAM_Type = QamOrder
_GenEquipRadioMRMCProfileAttrRxQAM_Object = MibTableColumn
genEquipRadioMRMCProfileAttrRxQAM = _GenEquipRadioMRMCProfileAttrRxQAM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 6),
    _GenEquipRadioMRMCProfileAttrRxQAM_Type()
)
genEquipRadioMRMCProfileAttrRxQAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrRxQAM.setStatus("mandatory")
_GenEquipRadioMRMCProfileAttrRxBitRate_Type = MrmcBitRate
_GenEquipRadioMRMCProfileAttrRxBitRate_Object = MibTableColumn
genEquipRadioMRMCProfileAttrRxBitRate = _GenEquipRadioMRMCProfileAttrRxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 4, 1, 7),
    _GenEquipRadioMRMCProfileAttrRxBitRate_Type()
)
genEquipRadioMRMCProfileAttrRxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCProfileAttrRxBitRate.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrTable_Object = MibTable
genEquipRadioMRMCScriptAttrTable = _GenEquipRadioMRMCScriptAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5)
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrTable.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrEntry_Object = MibTableRow
genEquipRadioMRMCScriptAttrEntry = _GenEquipRadioMRMCScriptAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1)
)
genEquipRadioMRMCScriptAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCScriptAttrScriptId"),
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrEntry.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrScriptId_Type = MrmcScriptId
_GenEquipRadioMRMCScriptAttrScriptId_Object = MibTableColumn
genEquipRadioMRMCScriptAttrScriptId = _GenEquipRadioMRMCScriptAttrScriptId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 1),
    _GenEquipRadioMRMCScriptAttrScriptId_Type()
)
genEquipRadioMRMCScriptAttrScriptId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrScriptId.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrScriptName_Type(DisplayString):
    """Custom type genEquipRadioMRMCScriptAttrScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GenEquipRadioMRMCScriptAttrScriptName_Type.__name__ = "DisplayString"
_GenEquipRadioMRMCScriptAttrScriptName_Object = MibTableColumn
genEquipRadioMRMCScriptAttrScriptName = _GenEquipRadioMRMCScriptAttrScriptName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 2),
    _GenEquipRadioMRMCScriptAttrScriptName_Type()
)
genEquipRadioMRMCScriptAttrScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrScriptName.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrSupportACM_Type = NoYes
_GenEquipRadioMRMCScriptAttrSupportACM_Object = MibTableColumn
genEquipRadioMRMCScriptAttrSupportACM = _GenEquipRadioMRMCScriptAttrSupportACM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 3),
    _GenEquipRadioMRMCScriptAttrSupportACM_Type()
)
genEquipRadioMRMCScriptAttrSupportACM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrSupportACM.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrStandard_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrStandard based on Integer32"""
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
        *(("etsi", 1),
          ("etsi-fcc", 3),
          ("fcc", 2),
          ("unknown", 0))
    )


_GenEquipRadioMRMCScriptAttrStandard_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrStandard_Object = MibTableColumn
genEquipRadioMRMCScriptAttrStandard = _GenEquipRadioMRMCScriptAttrStandard_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 4),
    _GenEquipRadioMRMCScriptAttrStandard_Type()
)
genEquipRadioMRMCScriptAttrStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrStandard.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrMultiCarrier_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrMultiCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mimo", 2),
          ("single-carrier", 0),
          ("xpic", 1))
    )


_GenEquipRadioMRMCScriptAttrMultiCarrier_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrMultiCarrier_Object = MibTableColumn
genEquipRadioMRMCScriptAttrMultiCarrier = _GenEquipRadioMRMCScriptAttrMultiCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 5),
    _GenEquipRadioMRMCScriptAttrMultiCarrier_Type()
)
genEquipRadioMRMCScriptAttrMultiCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrMultiCarrier.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrAdjChannel_Type = NoYes
_GenEquipRadioMRMCScriptAttrAdjChannel_Object = MibTableColumn
genEquipRadioMRMCScriptAttrAdjChannel = _GenEquipRadioMRMCScriptAttrAdjChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 6),
    _GenEquipRadioMRMCScriptAttrAdjChannel_Type()
)
genEquipRadioMRMCScriptAttrAdjChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrAdjChannel.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrModScheme_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrModScheme based on Integer32"""
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
        *(("adaptive", 4),
          ("fixed", 3),
          ("fixed-adaptive", 5),
          ("manual", 6),
          ("regular", 2))
    )


_GenEquipRadioMRMCScriptAttrModScheme_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrModScheme_Object = MibTableColumn
genEquipRadioMRMCScriptAttrModScheme = _GenEquipRadioMRMCScriptAttrModScheme_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 7),
    _GenEquipRadioMRMCScriptAttrModScheme_Type()
)
genEquipRadioMRMCScriptAttrModScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrModScheme.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrSymmetry_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrSymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asymmetry", 1),
          ("normal", 0))
    )


_GenEquipRadioMRMCScriptAttrSymmetry_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrSymmetry_Object = MibTableColumn
genEquipRadioMRMCScriptAttrSymmetry = _GenEquipRadioMRMCScriptAttrSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 8),
    _GenEquipRadioMRMCScriptAttrSymmetry_Type()
)
genEquipRadioMRMCScriptAttrSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrSymmetry.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrLatency_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("normal", 0))
    )


_GenEquipRadioMRMCScriptAttrLatency_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrLatency_Object = MibTableColumn
genEquipRadioMRMCScriptAttrLatency = _GenEquipRadioMRMCScriptAttrLatency_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 9),
    _GenEquipRadioMRMCScriptAttrLatency_Type()
)
genEquipRadioMRMCScriptAttrLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrLatency.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrTxBW_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrTxBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512000),
    )


_GenEquipRadioMRMCScriptAttrTxBW_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrTxBW_Object = MibTableColumn
genEquipRadioMRMCScriptAttrTxBW = _GenEquipRadioMRMCScriptAttrTxBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 10),
    _GenEquipRadioMRMCScriptAttrTxBW_Type()
)
genEquipRadioMRMCScriptAttrTxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrTxBW.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrRxBW_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrRxBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512000),
    )


_GenEquipRadioMRMCScriptAttrRxBW_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrRxBW_Object = MibTableColumn
genEquipRadioMRMCScriptAttrRxBW = _GenEquipRadioMRMCScriptAttrRxBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 11),
    _GenEquipRadioMRMCScriptAttrRxBW_Type()
)
genEquipRadioMRMCScriptAttrRxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrRxBW.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrTxOccupiedBW_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrTxOccupiedBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512000),
    )


_GenEquipRadioMRMCScriptAttrTxOccupiedBW_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrTxOccupiedBW_Object = MibTableColumn
genEquipRadioMRMCScriptAttrTxOccupiedBW = _GenEquipRadioMRMCScriptAttrTxOccupiedBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 12),
    _GenEquipRadioMRMCScriptAttrTxOccupiedBW_Type()
)
genEquipRadioMRMCScriptAttrTxOccupiedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrTxOccupiedBW.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrRxOccupiedBW_Type = Integer32
_GenEquipRadioMRMCScriptAttrRxOccupiedBW_Object = MibTableColumn
genEquipRadioMRMCScriptAttrRxOccupiedBW = _GenEquipRadioMRMCScriptAttrRxOccupiedBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 13),
    _GenEquipRadioMRMCScriptAttrRxOccupiedBW_Type()
)
genEquipRadioMRMCScriptAttrRxOccupiedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrRxOccupiedBW.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrLinkGrade_Type = RfuGrade
_GenEquipRadioMRMCScriptAttrLinkGrade_Object = MibTableColumn
genEquipRadioMRMCScriptAttrLinkGrade = _GenEquipRadioMRMCScriptAttrLinkGrade_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 14),
    _GenEquipRadioMRMCScriptAttrLinkGrade_Type()
)
genEquipRadioMRMCScriptAttrLinkGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrLinkGrade.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrDiffGrade_Type = RfuGrade
_GenEquipRadioMRMCScriptAttrDiffGrade_Object = MibTableColumn
genEquipRadioMRMCScriptAttrDiffGrade = _GenEquipRadioMRMCScriptAttrDiffGrade_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 15),
    _GenEquipRadioMRMCScriptAttrDiffGrade_Type()
)
genEquipRadioMRMCScriptAttrDiffGrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrDiffGrade.setStatus("mandatory")


class _GenEquipRadioMRMCScriptAttrChannelBW_Type(Integer32):
    """Custom type genEquipRadioMRMCScriptAttrChannelBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512000),
    )


_GenEquipRadioMRMCScriptAttrChannelBW_Type.__name__ = "Integer32"
_GenEquipRadioMRMCScriptAttrChannelBW_Object = MibTableColumn
genEquipRadioMRMCScriptAttrChannelBW = _GenEquipRadioMRMCScriptAttrChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 16),
    _GenEquipRadioMRMCScriptAttrChannelBW_Type()
)
genEquipRadioMRMCScriptAttrChannelBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrChannelBW.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrTxMaxProfile_Type = MrmcProfile
_GenEquipRadioMRMCScriptAttrTxMaxProfile_Object = MibTableColumn
genEquipRadioMRMCScriptAttrTxMaxProfile = _GenEquipRadioMRMCScriptAttrTxMaxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 17),
    _GenEquipRadioMRMCScriptAttrTxMaxProfile_Type()
)
genEquipRadioMRMCScriptAttrTxMaxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrTxMaxProfile.setStatus("mandatory")
_GenEquipRadioMRMCScriptAttrRxMaxProfile_Type = MrmcProfile
_GenEquipRadioMRMCScriptAttrRxMaxProfile_Object = MibTableColumn
genEquipRadioMRMCScriptAttrRxMaxProfile = _GenEquipRadioMRMCScriptAttrRxMaxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 5, 1, 18),
    _GenEquipRadioMRMCScriptAttrRxMaxProfile_Type()
)
genEquipRadioMRMCScriptAttrRxMaxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCScriptAttrRxMaxProfile.setStatus("mandatory")
_GenEquipRadioMRMCConfigTable_Object = MibTable
genEquipRadioMRMCConfigTable = _GenEquipRadioMRMCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6)
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigTable.setStatus("mandatory")
_GenEquipRadioMRMCConfigEntry_Object = MibTableRow
genEquipRadioMRMCConfigEntry = _GenEquipRadioMRMCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1)
)
genEquipRadioMRMCConfigEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioMRMCConfigRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigEntry.setStatus("mandatory")
_GenEquipRadioMRMCConfigRadioId_Type = RadioId
_GenEquipRadioMRMCConfigRadioId_Object = MibTableColumn
genEquipRadioMRMCConfigRadioId = _GenEquipRadioMRMCConfigRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 1),
    _GenEquipRadioMRMCConfigRadioId_Type()
)
genEquipRadioMRMCConfigRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigRadioId.setStatus("mandatory")
_GenEquipRadioMRMCConfigActiveScriptId_Type = MrmcScriptId
_GenEquipRadioMRMCConfigActiveScriptId_Object = MibTableColumn
genEquipRadioMRMCConfigActiveScriptId = _GenEquipRadioMRMCConfigActiveScriptId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 2),
    _GenEquipRadioMRMCConfigActiveScriptId_Type()
)
genEquipRadioMRMCConfigActiveScriptId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigActiveScriptId.setStatus("mandatory")
_GenEquipRadioMRMCConfigStandbyScriptId_Type = MrmcScriptId
_GenEquipRadioMRMCConfigStandbyScriptId_Object = MibTableColumn
genEquipRadioMRMCConfigStandbyScriptId = _GenEquipRadioMRMCConfigStandbyScriptId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 3),
    _GenEquipRadioMRMCConfigStandbyScriptId_Type()
)
genEquipRadioMRMCConfigStandbyScriptId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigStandbyScriptId.setStatus("mandatory")


class _GenEquipRadioMRMCConfigOperMode_Type(Integer32):
    """Custom type genEquipRadioMRMCConfigOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("fixed", 2),
          ("manual", 4))
    )


_GenEquipRadioMRMCConfigOperMode_Type.__name__ = "Integer32"
_GenEquipRadioMRMCConfigOperMode_Object = MibTableColumn
genEquipRadioMRMCConfigOperMode = _GenEquipRadioMRMCConfigOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 4),
    _GenEquipRadioMRMCConfigOperMode_Type()
)
genEquipRadioMRMCConfigOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigOperMode.setStatus("mandatory")
_GenEquipRadioMRMCConfigMaxProfile_Type = MrmcProfile
_GenEquipRadioMRMCConfigMaxProfile_Object = MibTableColumn
genEquipRadioMRMCConfigMaxProfile = _GenEquipRadioMRMCConfigMaxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 5),
    _GenEquipRadioMRMCConfigMaxProfile_Type()
)
genEquipRadioMRMCConfigMaxProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigMaxProfile.setStatus("mandatory")
_GenEquipRadioMRMCConfigMinProfile_Type = MrmcProfile
_GenEquipRadioMRMCConfigMinProfile_Object = MibTableColumn
genEquipRadioMRMCConfigMinProfile = _GenEquipRadioMRMCConfigMinProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 6),
    _GenEquipRadioMRMCConfigMinProfile_Type()
)
genEquipRadioMRMCConfigMinProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigMinProfile.setStatus("mandatory")
_GenEquipRadioMRMCConfigAdaptivePowerAdmin_Type = EnableDisable
_GenEquipRadioMRMCConfigAdaptivePowerAdmin_Object = MibTableColumn
genEquipRadioMRMCConfigAdaptivePowerAdmin = _GenEquipRadioMRMCConfigAdaptivePowerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 7),
    _GenEquipRadioMRMCConfigAdaptivePowerAdmin_Type()
)
genEquipRadioMRMCConfigAdaptivePowerAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigAdaptivePowerAdmin.setStatus("mandatory")


class _GenEquipRadioMRMCConfigAdaptivePowerRefClass_Type(Integer32):
    """Custom type genEquipRadioMRMCConfigAdaptivePowerRefClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("class-2", 0),
          ("class-4", 1),
          ("class-5b", 2),
          ("class-6a", 3),
          ("class-7a", 5),
          ("class-7b", 6),
          ("fcc", 4))
    )


_GenEquipRadioMRMCConfigAdaptivePowerRefClass_Type.__name__ = "Integer32"
_GenEquipRadioMRMCConfigAdaptivePowerRefClass_Object = MibTableColumn
genEquipRadioMRMCConfigAdaptivePowerRefClass = _GenEquipRadioMRMCConfigAdaptivePowerRefClass_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 4, 6, 1, 8),
    _GenEquipRadioMRMCConfigAdaptivePowerRefClass_Type()
)
genEquipRadioMRMCConfigAdaptivePowerRefClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioMRMCConfigAdaptivePowerRefClass.setStatus("mandatory")
_GenEquipRadioComp_ObjectIdentity = ObjectIdentity
genEquipRadioComp = _GenEquipRadioComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5)
)
_GenEquipRadioCompCfgTable_Object = MibTable
genEquipRadioCompCfgTable = _GenEquipRadioCompCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioCompCfgTable.setStatus("mandatory")
_GenEquipRadioCompCfgEntry_Object = MibTableRow
genEquipRadioCompCfgEntry = _GenEquipRadioCompCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 1, 1)
)
genEquipRadioCompCfgEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompCfgEntry.setStatus("mandatory")


class _GenEquipRadioCompMode_Type(Integer32):
    """Custom type genEquipRadioCompMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 1),
          ("legacy", 0))
    )


_GenEquipRadioCompMode_Type.__name__ = "Integer32"
_GenEquipRadioCompMode_Object = MibTableColumn
genEquipRadioCompMode = _GenEquipRadioCompMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 1, 1, 1),
    _GenEquipRadioCompMode_Type()
)
genEquipRadioCompMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCompMode.setStatus("mandatory")
_GenEquipRadioEnhHeaderCompAdmin_Type = AllowedNotAllowed
_GenEquipRadioEnhHeaderCompAdmin_Object = MibTableColumn
genEquipRadioEnhHeaderCompAdmin = _GenEquipRadioEnhHeaderCompAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 1, 1, 2),
    _GenEquipRadioEnhHeaderCompAdmin_Type()
)
genEquipRadioEnhHeaderCompAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioEnhHeaderCompAdmin.setStatus("mandatory")
_GenEquipRadioEnhDataCompAdmin_Type = EnableDisable
_GenEquipRadioEnhDataCompAdmin_Object = MibTableColumn
genEquipRadioEnhDataCompAdmin = _GenEquipRadioEnhDataCompAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 1, 1, 3),
    _GenEquipRadioEnhDataCompAdmin_Type()
)
genEquipRadioEnhDataCompAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioEnhDataCompAdmin.setStatus("mandatory")


class _GenEquipRadioEnhHeaderCompMode_Type(Integer32):
    """Custom type genEquipRadioEnhHeaderCompMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2", 0),
          ("l3", 1),
          ("l4", 2))
    )


_GenEquipRadioEnhHeaderCompMode_Type.__name__ = "Integer32"
_GenEquipRadioEnhHeaderCompMode_Object = MibTableColumn
genEquipRadioEnhHeaderCompMode = _GenEquipRadioEnhHeaderCompMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 1, 1, 4),
    _GenEquipRadioEnhHeaderCompMode_Type()
)
genEquipRadioEnhHeaderCompMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioEnhHeaderCompMode.setStatus("mandatory")
_GenEquipRadioCompStatusTable_Object = MibTable
genEquipRadioCompStatusTable = _GenEquipRadioCompStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioCompStatusTable.setStatus("mandatory")
_GenEquipRadioCompStatusEntry_Object = MibTableRow
genEquipRadioCompStatusEntry = _GenEquipRadioCompStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 2, 1)
)
genEquipRadioCompStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompStatusEntry.setStatus("mandatory")


class _GenEquipRadioCompOperationalState_Type(Integer32):
    """Custom type genEquipRadioCompOperationalState based on Integer32"""
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
        *(("enhanced-DC-active-HC-bypass", 3),
          ("enhanced-HC-DC-active", 4),
          ("enhanced-HC-DC-bypass", 1),
          ("enhanced-HC-active-DC-bypass", 2),
          ("legacy", 0),
          ("undefined", 5))
    )


_GenEquipRadioCompOperationalState_Type.__name__ = "Integer32"
_GenEquipRadioCompOperationalState_Object = MibTableColumn
genEquipRadioCompOperationalState = _GenEquipRadioCompOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 2, 1, 1),
    _GenEquipRadioCompOperationalState_Type()
)
genEquipRadioCompOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompOperationalState.setStatus("mandatory")
_GenEquipRadioCompExclRulesTable_Object = MibTable
genEquipRadioCompExclRulesTable = _GenEquipRadioCompExclRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioCompExclRulesTable.setStatus("mandatory")
_GenEquipRadioCompExclRulesEntry_Object = MibTableRow
genEquipRadioCompExclRulesEntry = _GenEquipRadioCompExclRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3, 1)
)
genEquipRadioCompExclRulesEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
    (0, "MWRM-RADIO-MIB", "genEquipRadioCompExclRuleId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompExclRulesEntry.setStatus("mandatory")


class _GenEquipRadioCompExclRuleId_Type(Integer32):
    """Custom type genEquipRadioCompExclRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GenEquipRadioCompExclRuleId_Type.__name__ = "Integer32"
_GenEquipRadioCompExclRuleId_Object = MibTableColumn
genEquipRadioCompExclRuleId = _GenEquipRadioCompExclRuleId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3, 1, 1),
    _GenEquipRadioCompExclRuleId_Type()
)
genEquipRadioCompExclRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompExclRuleId.setStatus("mandatory")


class _GenEquipRadioCompExclRuleType_Type(Integer32):
    """Custom type genEquipRadioCompExclRuleType based on Integer32"""
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
        *(("ethertype", 4),
          ("flow-Id", 0),
          ("mac-DA", 2),
          ("mac-SA", 3),
          ("none", 5),
          ("vlan", 1))
    )


_GenEquipRadioCompExclRuleType_Type.__name__ = "Integer32"
_GenEquipRadioCompExclRuleType_Object = MibTableColumn
genEquipRadioCompExclRuleType = _GenEquipRadioCompExclRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3, 1, 2),
    _GenEquipRadioCompExclRuleType_Type()
)
genEquipRadioCompExclRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCompExclRuleType.setStatus("mandatory")
_GenEquipRadioCompExclRuleName_Type = DisplayString
_GenEquipRadioCompExclRuleName_Object = MibTableColumn
genEquipRadioCompExclRuleName = _GenEquipRadioCompExclRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3, 1, 3),
    _GenEquipRadioCompExclRuleName_Type()
)
genEquipRadioCompExclRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCompExclRuleName.setStatus("mandatory")
_GenEquipRadioCompExclRuleValue_Type = OctetString
_GenEquipRadioCompExclRuleValue_Object = MibTableColumn
genEquipRadioCompExclRuleValue = _GenEquipRadioCompExclRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3, 1, 4),
    _GenEquipRadioCompExclRuleValue_Type()
)
genEquipRadioCompExclRuleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCompExclRuleValue.setStatus("mandatory")
_GenEquipRadioCompExclRuleRowStatus_Type = RowStatus
_GenEquipRadioCompExclRuleRowStatus_Object = MibTableColumn
genEquipRadioCompExclRuleRowStatus = _GenEquipRadioCompExclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 3, 1, 30),
    _GenEquipRadioCompExclRuleRowStatus_Type()
)
genEquipRadioCompExclRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCompExclRuleRowStatus.setStatus("mandatory")
_GenEquipRadioCompNG_ObjectIdentity = ObjectIdentity
genEquipRadioCompNG = _GenEquipRadioCompNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4)
)
_GenEquipRadioCompNGCfgTable_Object = MibTable
genEquipRadioCompNGCfgTable = _GenEquipRadioCompNGCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGCfgTable.setStatus("mandatory")
_GenEquipRadioCompNGCfgEntry_Object = MibTableRow
genEquipRadioCompNGCfgEntry = _GenEquipRadioCompNGCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1, 1)
)
genEquipRadioCompNGCfgEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCompNGCfgifIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGCfgEntry.setStatus("mandatory")
_GenEquipRadioCompNGCfgifIndex_Type = Integer32
_GenEquipRadioCompNGCfgifIndex_Object = MibTableColumn
genEquipRadioCompNGCfgifIndex = _GenEquipRadioCompNGCfgifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1, 1, 1),
    _GenEquipRadioCompNGCfgifIndex_Type()
)
genEquipRadioCompNGCfgifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCfgifIndex.setStatus("mandatory")
_GenEquipRadioHeaderCompNGCfgClearStats_Type = NoYes
_GenEquipRadioHeaderCompNGCfgClearStats_Object = MibTableColumn
genEquipRadioHeaderCompNGCfgClearStats = _GenEquipRadioHeaderCompNGCfgClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1, 1, 2),
    _GenEquipRadioHeaderCompNGCfgClearStats_Type()
)
genEquipRadioHeaderCompNGCfgClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioHeaderCompNGCfgClearStats.setStatus("mandatory")
_GenEquipRadioHeaderCompNGCfgUserFlowType_Type = Integer32
_GenEquipRadioHeaderCompNGCfgUserFlowType_Object = MibTableColumn
genEquipRadioHeaderCompNGCfgUserFlowType = _GenEquipRadioHeaderCompNGCfgUserFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1, 1, 3),
    _GenEquipRadioHeaderCompNGCfgUserFlowType_Type()
)
genEquipRadioHeaderCompNGCfgUserFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioHeaderCompNGCfgUserFlowType.setStatus("mandatory")
_GenEquipRadioHeaderCompNGCfgMode_Type = HcModeType
_GenEquipRadioHeaderCompNGCfgMode_Object = MibTableColumn
genEquipRadioHeaderCompNGCfgMode = _GenEquipRadioHeaderCompNGCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1, 1, 4),
    _GenEquipRadioHeaderCompNGCfgMode_Type()
)
genEquipRadioHeaderCompNGCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioHeaderCompNGCfgMode.setStatus("mandatory")
_GenEquipRadioCutThroughNGCfgMode_Type = NoYes
_GenEquipRadioCutThroughNGCfgMode_Object = MibTableColumn
genEquipRadioCutThroughNGCfgMode = _GenEquipRadioCutThroughNGCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 1, 1, 5),
    _GenEquipRadioCutThroughNGCfgMode_Type()
)
genEquipRadioCutThroughNGCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCfgMode.setStatus("mandatory")
_GenEquipRadioCompNGExclRulesTable_Object = MibTable
genEquipRadioCompNGExclRulesTable = _GenEquipRadioCompNGExclRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRulesTable.setStatus("mandatory")
_GenEquipRadioCompNGExclRulesEntry_Object = MibTableRow
genEquipRadioCompNGExclRulesEntry = _GenEquipRadioCompNGExclRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2, 1)
)
genEquipRadioCompNGExclRulesEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCompNGExclRulesifIndex"),
    (0, "MWRM-RADIO-MIB", "genEquipRadioCompNGExclRuleId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRulesEntry.setStatus("mandatory")
_GenEquipRadioCompNGExclRulesifIndex_Type = Integer32
_GenEquipRadioCompNGExclRulesifIndex_Object = MibTableColumn
genEquipRadioCompNGExclRulesifIndex = _GenEquipRadioCompNGExclRulesifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2, 1, 1),
    _GenEquipRadioCompNGExclRulesifIndex_Type()
)
genEquipRadioCompNGExclRulesifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRulesifIndex.setStatus("mandatory")
_GenEquipRadioCompNGExclRuleId_Type = Integer32
_GenEquipRadioCompNGExclRuleId_Object = MibTableColumn
genEquipRadioCompNGExclRuleId = _GenEquipRadioCompNGExclRuleId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2, 1, 2),
    _GenEquipRadioCompNGExclRuleId_Type()
)
genEquipRadioCompNGExclRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRuleId.setStatus("mandatory")


class _GenEquipRadioCompNGExclRuleName_Type(DisplayString):
    """Custom type genEquipRadioCompNGExclRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenEquipRadioCompNGExclRuleName_Type.__name__ = "DisplayString"
_GenEquipRadioCompNGExclRuleName_Object = MibTableColumn
genEquipRadioCompNGExclRuleName = _GenEquipRadioCompNGExclRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2, 1, 3),
    _GenEquipRadioCompNGExclRuleName_Type()
)
genEquipRadioCompNGExclRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRuleName.setStatus("mandatory")
_GenEquipRadioCompNGExclRuleType_Type = EnhancedHCExclRuleType
_GenEquipRadioCompNGExclRuleType_Object = MibTableColumn
genEquipRadioCompNGExclRuleType = _GenEquipRadioCompNGExclRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2, 1, 4),
    _GenEquipRadioCompNGExclRuleType_Type()
)
genEquipRadioCompNGExclRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRuleType.setStatus("mandatory")
_GenEquipRadioCompNGExclRuleValue_Type = OctetString
_GenEquipRadioCompNGExclRuleValue_Object = MibTableColumn
genEquipRadioCompNGExclRuleValue = _GenEquipRadioCompNGExclRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 2, 1, 5),
    _GenEquipRadioCompNGExclRuleValue_Type()
)
genEquipRadioCompNGExclRuleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGExclRuleValue.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTable_Object = MibTable
genEquipRadioCutThroughNGCountersTable = _GenEquipRadioCutThroughNGCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTable.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersEntry_Object = MibTableRow
genEquipRadioCutThroughNGCountersEntry = _GenEquipRadioCutThroughNGCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1)
)
genEquipRadioCutThroughNGCountersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCutThroughNGCountersifIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersEntry.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersifIndex_Type = Integer32
_GenEquipRadioCutThroughNGCountersifIndex_Object = MibTableColumn
genEquipRadioCutThroughNGCountersifIndex = _GenEquipRadioCutThroughNGCountersifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 1),
    _GenEquipRadioCutThroughNGCountersifIndex_Type()
)
genEquipRadioCutThroughNGCountersifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersifIndex.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersRxFrames_Type = Counter64
_GenEquipRadioCutThroughNGCountersRxFrames_Object = MibTableColumn
genEquipRadioCutThroughNGCountersRxFrames = _GenEquipRadioCutThroughNGCountersRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 2),
    _GenEquipRadioCutThroughNGCountersRxFrames_Type()
)
genEquipRadioCutThroughNGCountersRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersRxFrames.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersRxBytes_Type = Counter64
_GenEquipRadioCutThroughNGCountersRxBytes_Object = MibTableColumn
genEquipRadioCutThroughNGCountersRxBytes = _GenEquipRadioCutThroughNGCountersRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 3),
    _GenEquipRadioCutThroughNGCountersRxBytes_Type()
)
genEquipRadioCutThroughNGCountersRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersRxBytes.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTxFrames_Type = Counter64
_GenEquipRadioCutThroughNGCountersTxFrames_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTxFrames = _GenEquipRadioCutThroughNGCountersTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 4),
    _GenEquipRadioCutThroughNGCountersTxFrames_Type()
)
genEquipRadioCutThroughNGCountersTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTxFrames.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTxBytes_Type = Counter64
_GenEquipRadioCutThroughNGCountersTxBytes_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTxBytes = _GenEquipRadioCutThroughNGCountersTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 5),
    _GenEquipRadioCutThroughNGCountersTxBytes_Type()
)
genEquipRadioCutThroughNGCountersTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTxBytes.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTotalRxFrames_Type = Counter64
_GenEquipRadioCutThroughNGCountersTotalRxFrames_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTotalRxFrames = _GenEquipRadioCutThroughNGCountersTotalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 6),
    _GenEquipRadioCutThroughNGCountersTotalRxFrames_Type()
)
genEquipRadioCutThroughNGCountersTotalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTotalRxFrames.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTotalRxBytes_Type = Counter64
_GenEquipRadioCutThroughNGCountersTotalRxBytes_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTotalRxBytes = _GenEquipRadioCutThroughNGCountersTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 7),
    _GenEquipRadioCutThroughNGCountersTotalRxBytes_Type()
)
genEquipRadioCutThroughNGCountersTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTotalRxBytes.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTotalTxBytesOut_Type = Counter64
_GenEquipRadioCutThroughNGCountersTotalTxBytesOut_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTotalTxBytesOut = _GenEquipRadioCutThroughNGCountersTotalTxBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 8),
    _GenEquipRadioCutThroughNGCountersTotalTxBytesOut_Type()
)
genEquipRadioCutThroughNGCountersTotalTxBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTotalTxBytesOut.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTotalTxFrames_Type = Counter64
_GenEquipRadioCutThroughNGCountersTotalTxFrames_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTotalTxFrames = _GenEquipRadioCutThroughNGCountersTotalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 9),
    _GenEquipRadioCutThroughNGCountersTotalTxFrames_Type()
)
genEquipRadioCutThroughNGCountersTotalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTotalTxFrames.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTotalTxIdleBytes_Type = Counter64
_GenEquipRadioCutThroughNGCountersTotalTxIdleBytes_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTotalTxIdleBytes = _GenEquipRadioCutThroughNGCountersTotalTxIdleBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 10),
    _GenEquipRadioCutThroughNGCountersTotalTxIdleBytes_Type()
)
genEquipRadioCutThroughNGCountersTotalTxIdleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTotalTxIdleBytes.setStatus("mandatory")
_GenEquipRadioCutThroughNGCountersTotalTxBytesIn_Type = Counter64
_GenEquipRadioCutThroughNGCountersTotalTxBytesIn_Object = MibTableColumn
genEquipRadioCutThroughNGCountersTotalTxBytesIn = _GenEquipRadioCutThroughNGCountersTotalTxBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 3, 1, 11),
    _GenEquipRadioCutThroughNGCountersTotalTxBytesIn_Type()
)
genEquipRadioCutThroughNGCountersTotalTxBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughNGCountersTotalTxBytesIn.setStatus("mandatory")
_GenEquipRadioCompNGStatusTable_Object = MibTable
genEquipRadioCompNGStatusTable = _GenEquipRadioCompNGStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 4)
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGStatusTable.setStatus("mandatory")
_GenEquipRadioCompNGStatusEntry_Object = MibTableRow
genEquipRadioCompNGStatusEntry = _GenEquipRadioCompNGStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 4, 1)
)
genEquipRadioCompNGStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCompNGStatusifindex"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGStatusEntry.setStatus("mandatory")
_GenEquipRadioCompNGStatusifindex_Type = Integer32
_GenEquipRadioCompNGStatusifindex_Object = MibTableColumn
genEquipRadioCompNGStatusifindex = _GenEquipRadioCompNGStatusifindex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 4, 1, 1),
    _GenEquipRadioCompNGStatusifindex_Type()
)
genEquipRadioCompNGStatusifindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGStatusifindex.setStatus("mandatory")
_GenEquipRadioCompNGStatusOperationalState_Type = HcModeType
_GenEquipRadioCompNGStatusOperationalState_Object = MibTableColumn
genEquipRadioCompNGStatusOperationalState = _GenEquipRadioCompNGStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 4, 1, 2),
    _GenEquipRadioCompNGStatusOperationalState_Type()
)
genEquipRadioCompNGStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGStatusOperationalState.setStatus("mandatory")
_GenEquipRadioCompNGStatusType_Type = HcType
_GenEquipRadioCompNGStatusType_Object = MibTableColumn
genEquipRadioCompNGStatusType = _GenEquipRadioCompNGStatusType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 4, 1, 3),
    _GenEquipRadioCompNGStatusType_Type()
)
genEquipRadioCompNGStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGStatusType.setStatus("mandatory")
_GenEquipRadioCompNGCountersTable_Object = MibTable
genEquipRadioCompNGCountersTable = _GenEquipRadioCompNGCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7)
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersTable.setStatus("mandatory")
_GenEquipRadioCompNGCountersEntry_Object = MibTableRow
genEquipRadioCompNGCountersEntry = _GenEquipRadioCompNGCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1)
)
genEquipRadioCompNGCountersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCompNGCountersifIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersEntry.setStatus("mandatory")
_GenEquipRadioCompNGCountersifIndex_Type = Integer32
_GenEquipRadioCompNGCountersifIndex_Object = MibTableColumn
genEquipRadioCompNGCountersifIndex = _GenEquipRadioCompNGCountersifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 1),
    _GenEquipRadioCompNGCountersifIndex_Type()
)
genEquipRadioCompNGCountersifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersifIndex.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCInBytes_Type = Counter64
_GenEquipRadioCompNGCountersHCInBytes_Object = MibTableColumn
genEquipRadioCompNGCountersHCInBytes = _GenEquipRadioCompNGCountersHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 2),
    _GenEquipRadioCompNGCountersHCInBytes_Type()
)
genEquipRadioCompNGCountersHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCInBytes.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCOutBytes_Type = Counter64
_GenEquipRadioCompNGCountersHCOutBytes_Object = MibTableColumn
genEquipRadioCompNGCountersHCOutBytes = _GenEquipRadioCompNGCountersHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 3),
    _GenEquipRadioCompNGCountersHCOutBytes_Type()
)
genEquipRadioCompNGCountersHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCOutBytes.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCCompFrm_Type = Counter64
_GenEquipRadioCompNGCountersHCCompFrm_Object = MibTableColumn
genEquipRadioCompNGCountersHCCompFrm = _GenEquipRadioCompNGCountersHCCompFrm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 4),
    _GenEquipRadioCompNGCountersHCCompFrm_Type()
)
genEquipRadioCompNGCountersHCCompFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCCompFrm.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCFrmUncmpExclRule_Type = Counter64
_GenEquipRadioCompNGCountersHCFrmUncmpExclRule_Object = MibTableColumn
genEquipRadioCompNGCountersHCFrmUncmpExclRule = _GenEquipRadioCompNGCountersHCFrmUncmpExclRule_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 5),
    _GenEquipRadioCompNGCountersHCFrmUncmpExclRule_Type()
)
genEquipRadioCompNGCountersHCFrmUncmpExclRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCFrmUncmpExclRule.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCFrmUcompInternal_Type = Counter64
_GenEquipRadioCompNGCountersHCFrmUcompInternal_Object = MibTableColumn
genEquipRadioCompNGCountersHCFrmUcompInternal = _GenEquipRadioCompNGCountersHCFrmUcompInternal_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 6),
    _GenEquipRadioCompNGCountersHCFrmUcompInternal_Type()
)
genEquipRadioCompNGCountersHCFrmUcompInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCFrmUcompInternal.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCLearningFrm_Type = Counter64
_GenEquipRadioCompNGCountersHCLearningFrm_Object = MibTableColumn
genEquipRadioCompNGCountersHCLearningFrm = _GenEquipRadioCompNGCountersHCLearningFrm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 7),
    _GenEquipRadioCompNGCountersHCLearningFrm_Type()
)
genEquipRadioCompNGCountersHCLearningFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCLearningFrm.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCUserFlowTypeActiveFlows_Type = Counter64
_GenEquipRadioCompNGCountersHCUserFlowTypeActiveFlows_Object = MibTableColumn
genEquipRadioCompNGCountersHCUserFlowTypeActiveFlows = _GenEquipRadioCompNGCountersHCUserFlowTypeActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 8),
    _GenEquipRadioCompNGCountersHCUserFlowTypeActiveFlows_Type()
)
genEquipRadioCompNGCountersHCUserFlowTypeActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCUserFlowTypeActiveFlows.setStatus("mandatory")
_GenEquipRadioCompNGCountersHCTotalActiveFlows_Type = Counter64
_GenEquipRadioCompNGCountersHCTotalActiveFlows_Object = MibTableColumn
genEquipRadioCompNGCountersHCTotalActiveFlows = _GenEquipRadioCompNGCountersHCTotalActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 5, 4, 7, 1, 9),
    _GenEquipRadioCompNGCountersHCTotalActiveFlows_Type()
)
genEquipRadioCompNGCountersHCTotalActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCompNGCountersHCTotalActiveFlows.setStatus("mandatory")
_GenEquipRadioPtpTransport_ObjectIdentity = ObjectIdentity
genEquipRadioPtpTransport = _GenEquipRadioPtpTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6)
)
_GenEquipRadioPtpTransportCfgTable_Object = MibTable
genEquipRadioPtpTransportCfgTable = _GenEquipRadioPtpTransportCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportCfgTable.setStatus("mandatory")
_GenEquipRadioPtpTransportCfgEntry_Object = MibTableRow
genEquipRadioPtpTransportCfgEntry = _GenEquipRadioPtpTransportCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 1, 1)
)
genEquipRadioPtpTransportCfgEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportCfgEntry.setStatus("mandatory")
_GenEquipRadioPtpTransportChannelAdmin_Type = EnableDisable
_GenEquipRadioPtpTransportChannelAdmin_Object = MibTableColumn
genEquipRadioPtpTransportChannelAdmin = _GenEquipRadioPtpTransportChannelAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 1, 1, 1),
    _GenEquipRadioPtpTransportChannelAdmin_Type()
)
genEquipRadioPtpTransportChannelAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportChannelAdmin.setStatus("mandatory")


class _GenEquipRadioPtpTransportChannelMode_Type(Integer32):
    """Custom type genEquipRadioPtpTransportChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("h-cos", 0),
          ("ieee-1588", 1))
    )


_GenEquipRadioPtpTransportChannelMode_Type.__name__ = "Integer32"
_GenEquipRadioPtpTransportChannelMode_Object = MibTableColumn
genEquipRadioPtpTransportChannelMode = _GenEquipRadioPtpTransportChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 1, 1, 2),
    _GenEquipRadioPtpTransportChannelMode_Type()
)
genEquipRadioPtpTransportChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportChannelMode.setStatus("mandatory")
_GenEquipRadioPtpTransportCountersTable_Object = MibTable
genEquipRadioPtpTransportCountersTable = _GenEquipRadioPtpTransportCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportCountersTable.setStatus("mandatory")
_GenEquipRadioPtpTransportCountersEntry_Object = MibTableRow
genEquipRadioPtpTransportCountersEntry = _GenEquipRadioPtpTransportCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1)
)
genEquipRadioPtpTransportCountersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportCountersEntry.setStatus("mandatory")
_GenEquipRadioPtpTransportTxFrames_Type = Integer32
_GenEquipRadioPtpTransportTxFrames_Object = MibTableColumn
genEquipRadioPtpTransportTxFrames = _GenEquipRadioPtpTransportTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1, 1),
    _GenEquipRadioPtpTransportTxFrames_Type()
)
genEquipRadioPtpTransportTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportTxFrames.setStatus("mandatory")
_GenEquipRadioPtpTransportTxDroppedFrames_Type = Integer32
_GenEquipRadioPtpTransportTxDroppedFrames_Object = MibTableColumn
genEquipRadioPtpTransportTxDroppedFrames = _GenEquipRadioPtpTransportTxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1, 2),
    _GenEquipRadioPtpTransportTxDroppedFrames_Type()
)
genEquipRadioPtpTransportTxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportTxDroppedFrames.setStatus("mandatory")
_GenEquipRadioPtpTransportTxBytes_Type = Integer32
_GenEquipRadioPtpTransportTxBytes_Object = MibTableColumn
genEquipRadioPtpTransportTxBytes = _GenEquipRadioPtpTransportTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1, 3),
    _GenEquipRadioPtpTransportTxBytes_Type()
)
genEquipRadioPtpTransportTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportTxBytes.setStatus("mandatory")
_GenEquipRadioPtpTransportTxDroppedBytes_Type = Integer32
_GenEquipRadioPtpTransportTxDroppedBytes_Object = MibTableColumn
genEquipRadioPtpTransportTxDroppedBytes = _GenEquipRadioPtpTransportTxDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1, 4),
    _GenEquipRadioPtpTransportTxDroppedBytes_Type()
)
genEquipRadioPtpTransportTxDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportTxDroppedBytes.setStatus("mandatory")
_GenEquipRadioPtpTransportRxFrames_Type = Integer32
_GenEquipRadioPtpTransportRxFrames_Object = MibTableColumn
genEquipRadioPtpTransportRxFrames = _GenEquipRadioPtpTransportRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1, 5),
    _GenEquipRadioPtpTransportRxFrames_Type()
)
genEquipRadioPtpTransportRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportRxFrames.setStatus("mandatory")
_GenEquipRadioPtpTransportRxBytes_Type = Integer32
_GenEquipRadioPtpTransportRxBytes_Object = MibTableColumn
genEquipRadioPtpTransportRxBytes = _GenEquipRadioPtpTransportRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 6, 2, 1, 6),
    _GenEquipRadioPtpTransportRxBytes_Type()
)
genEquipRadioPtpTransportRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioPtpTransportRxBytes.setStatus("mandatory")
_GenEquipRadioCutThrough_ObjectIdentity = ObjectIdentity
genEquipRadioCutThrough = _GenEquipRadioCutThrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7)
)
_GenEquipRadioCutThroughCfgTable_Object = MibTable
genEquipRadioCutThroughCfgTable = _GenEquipRadioCutThroughCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioCutThroughCfgTable.setStatus("mandatory")
_GenEquipRadioCutThroughCfgEntry_Object = MibTableRow
genEquipRadioCutThroughCfgEntry = _GenEquipRadioCutThroughCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 1, 1)
)
genEquipRadioCutThroughCfgEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCutThroughCfgEntry.setStatus("mandatory")
_GenEquipRadioCutThroughChannelAdmin_Type = EnableDisable
_GenEquipRadioCutThroughChannelAdmin_Object = MibTableColumn
genEquipRadioCutThroughChannelAdmin = _GenEquipRadioCutThroughChannelAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 1, 1, 1),
    _GenEquipRadioCutThroughChannelAdmin_Type()
)
genEquipRadioCutThroughChannelAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughChannelAdmin.setStatus("mandatory")
_GenEquipRadioCutThroughCountersTable_Object = MibTable
genEquipRadioCutThroughCountersTable = _GenEquipRadioCutThroughCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioCutThroughCountersTable.setStatus("mandatory")
_GenEquipRadioCutThroughCountersEntry_Object = MibTableRow
genEquipRadioCutThroughCountersEntry = _GenEquipRadioCutThroughCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 2, 1)
)
genEquipRadioCutThroughCountersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipRadioCutThroughCountersEntry.setStatus("mandatory")
_GenEquipRadioCutThroughTxFrames_Type = Integer32
_GenEquipRadioCutThroughTxFrames_Object = MibTableColumn
genEquipRadioCutThroughTxFrames = _GenEquipRadioCutThroughTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 2, 1, 1),
    _GenEquipRadioCutThroughTxFrames_Type()
)
genEquipRadioCutThroughTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughTxFrames.setStatus("mandatory")
_GenEquipRadioCutThroughTxBytes_Type = Integer32
_GenEquipRadioCutThroughTxBytes_Object = MibTableColumn
genEquipRadioCutThroughTxBytes = _GenEquipRadioCutThroughTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 2, 1, 2),
    _GenEquipRadioCutThroughTxBytes_Type()
)
genEquipRadioCutThroughTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughTxBytes.setStatus("mandatory")
_GenEquipRadioCutThroughRxFrames_Type = Integer32
_GenEquipRadioCutThroughRxFrames_Object = MibTableColumn
genEquipRadioCutThroughRxFrames = _GenEquipRadioCutThroughRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 2, 1, 3),
    _GenEquipRadioCutThroughRxFrames_Type()
)
genEquipRadioCutThroughRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughRxFrames.setStatus("mandatory")
_GenEquipRadioCutThroughRxBytes_Type = Integer32
_GenEquipRadioCutThroughRxBytes_Object = MibTableColumn
genEquipRadioCutThroughRxBytes = _GenEquipRadioCutThroughRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 7, 2, 1, 4),
    _GenEquipRadioCutThroughRxBytes_Type()
)
genEquipRadioCutThroughRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioCutThroughRxBytes.setStatus("mandatory")
_GenEquipRadioGroups_ObjectIdentity = ObjectIdentity
genEquipRadioGroups = _GenEquipRadioGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8)
)
_GenEquipRadioGroupsProtection_ObjectIdentity = ObjectIdentity
genEquipRadioGroupsProtection = _GenEquipRadioGroupsProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1)
)
_GenEquipRadioGroupsProtectionAttrTable_Object = MibTable
genEquipRadioGroupsProtectionAttrTable = _GenEquipRadioGroupsProtectionAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrTable.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrEntry_Object = MibTableRow
genEquipRadioGroupsProtectionAttrEntry = _GenEquipRadioGroupsProtectionAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1)
)
genEquipRadioGroupsProtectionAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsProtectionAttrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrEntry.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionAttrGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrGroupIfIndex = _GenEquipRadioGroupsProtectionAttrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 1),
    _GenEquipRadioGroupsProtectionAttrGroupIfIndex_Type()
)
genEquipRadioGroupsProtectionAttrGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrGroupIfIndex.setStatus("mandatory")


class _GenEquipRadioGroupsProtectionAttrGroupId_Type(Integer32):
    """Custom type genEquipRadioGroupsProtectionAttrGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GenEquipRadioGroupsProtectionAttrGroupId_Type.__name__ = "Integer32"
_GenEquipRadioGroupsProtectionAttrGroupId_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrGroupId = _GenEquipRadioGroupsProtectionAttrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 2),
    _GenEquipRadioGroupsProtectionAttrGroupId_Type()
)
genEquipRadioGroupsProtectionAttrGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrGroupId.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrCommand_Type = RadioProtectionCmd
_GenEquipRadioGroupsProtectionAttrCommand_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrCommand = _GenEquipRadioGroupsProtectionAttrCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 3),
    _GenEquipRadioGroupsProtectionAttrCommand_Type()
)
genEquipRadioGroupsProtectionAttrCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrCommand.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrCopyToMate_Type = OffOn
_GenEquipRadioGroupsProtectionAttrCopyToMate_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrCopyToMate = _GenEquipRadioGroupsProtectionAttrCopyToMate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 4),
    _GenEquipRadioGroupsProtectionAttrCopyToMate_Type()
)
genEquipRadioGroupsProtectionAttrCopyToMate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrCopyToMate.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex = _GenEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 5),
    _GenEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex_Type()
)
genEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrRevertiveAdmin_Type = EnableDisable
_GenEquipRadioGroupsProtectionAttrRevertiveAdmin_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrRevertiveAdmin = _GenEquipRadioGroupsProtectionAttrRevertiveAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 6),
    _GenEquipRadioGroupsProtectionAttrRevertiveAdmin_Type()
)
genEquipRadioGroupsProtectionAttrRevertiveAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrRevertiveAdmin.setStatus("mandatory")
_GenEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex = _GenEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 1, 1, 7),
    _GenEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex_Type()
)
genEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionMembersTable_Object = MibTable
genEquipRadioGroupsProtectionMembersTable = _GenEquipRadioGroupsProtectionMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersTable.setStatus("mandatory")
_GenEquipRadioGroupsProtectionMembersEntry_Object = MibTableRow
genEquipRadioGroupsProtectionMembersEntry = _GenEquipRadioGroupsProtectionMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2, 1)
)
genEquipRadioGroupsProtectionMembersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsProtectionMembersIfIndexGroup"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersEntry.setStatus("mandatory")
_GenEquipRadioGroupsProtectionMembersIfIndexGroup_Type = Integer32
_GenEquipRadioGroupsProtectionMembersIfIndexGroup_Object = MibTableColumn
genEquipRadioGroupsProtectionMembersIfIndexGroup = _GenEquipRadioGroupsProtectionMembersIfIndexGroup_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2, 1, 1),
    _GenEquipRadioGroupsProtectionMembersIfIndexGroup_Type()
)
genEquipRadioGroupsProtectionMembersIfIndexGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersIfIndexGroup.setStatus("mandatory")


class _GenEquipRadioGroupsProtectionMembersGroupId_Type(Integer32):
    """Custom type genEquipRadioGroupsProtectionMembersGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GenEquipRadioGroupsProtectionMembersGroupId_Type.__name__ = "Integer32"
_GenEquipRadioGroupsProtectionMembersGroupId_Object = MibTableColumn
genEquipRadioGroupsProtectionMembersGroupId = _GenEquipRadioGroupsProtectionMembersGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2, 1, 2),
    _GenEquipRadioGroupsProtectionMembersGroupId_Type()
)
genEquipRadioGroupsProtectionMembersGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersGroupId.setStatus("mandatory")
_GenEquipRadioGroupsProtectionMembersMem1IfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionMembersMem1IfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionMembersMem1IfIndex = _GenEquipRadioGroupsProtectionMembersMem1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2, 1, 3),
    _GenEquipRadioGroupsProtectionMembersMem1IfIndex_Type()
)
genEquipRadioGroupsProtectionMembersMem1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersMem1IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionMembersMem2IfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionMembersMem2IfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionMembersMem2IfIndex = _GenEquipRadioGroupsProtectionMembersMem2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2, 1, 4),
    _GenEquipRadioGroupsProtectionMembersMem2IfIndex_Type()
)
genEquipRadioGroupsProtectionMembersMem2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersMem2IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionMembersRowStatus_Type = RowStatus
_GenEquipRadioGroupsProtectionMembersRowStatus_Object = MibTableColumn
genEquipRadioGroupsProtectionMembersRowStatus = _GenEquipRadioGroupsProtectionMembersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 2, 1, 30),
    _GenEquipRadioGroupsProtectionMembersRowStatus_Type()
)
genEquipRadioGroupsProtectionMembersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionMembersRowStatus.setStatus("mandatory")
_GenEquipRadioGroupsProtectionStatusTable_Object = MibTable
genEquipRadioGroupsProtectionStatusTable = _GenEquipRadioGroupsProtectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionStatusTable.setStatus("mandatory")
_GenEquipRadioGroupsProtectionStatusEntry_Object = MibTableRow
genEquipRadioGroupsProtectionStatusEntry = _GenEquipRadioGroupsProtectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 3, 1)
)
genEquipRadioGroupsProtectionStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsProtectionStatusGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionStatusEntry.setStatus("mandatory")
_GenEquipRadioGroupsProtectionStatusGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionStatusGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionStatusGroupIfIndex = _GenEquipRadioGroupsProtectionStatusGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 3, 1, 1),
    _GenEquipRadioGroupsProtectionStatusGroupIfIndex_Type()
)
genEquipRadioGroupsProtectionStatusGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionStatusGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionStatusActiveIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionStatusActiveIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionStatusActiveIfIndex = _GenEquipRadioGroupsProtectionStatusActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 3, 1, 2),
    _GenEquipRadioGroupsProtectionStatusActiveIfIndex_Type()
)
genEquipRadioGroupsProtectionStatusActiveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionStatusActiveIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionStatusStandbyIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionStatusStandbyIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionStatusStandbyIfIndex = _GenEquipRadioGroupsProtectionStatusStandbyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 3, 1, 3),
    _GenEquipRadioGroupsProtectionStatusStandbyIfIndex_Type()
)
genEquipRadioGroupsProtectionStatusStandbyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionStatusStandbyIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionStatusLockout_Type = NoYes
_GenEquipRadioGroupsProtectionStatusLockout_Object = MibTableColumn
genEquipRadioGroupsProtectionStatusLockout = _GenEquipRadioGroupsProtectionStatusLockout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 3, 1, 4),
    _GenEquipRadioGroupsProtectionStatusLockout_Type()
)
genEquipRadioGroupsProtectionStatusLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionStatusLockout.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSD_ObjectIdentity = ObjectIdentity
genEquipRadioGroupsProtectionBBSSD = _GenEquipRadioGroupsProtectionBBSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10)
)
_GenEquipRadioGroupsProtectionBBSSDAttrTable_Object = MibTable
genEquipRadioGroupsProtectionBBSSDAttrTable = _GenEquipRadioGroupsProtectionBBSSDAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDAttrTable.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDAttrEntry_Object = MibTableRow
genEquipRadioGroupsProtectionBBSSDAttrEntry = _GenEquipRadioGroupsProtectionBBSSDAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 1, 1)
)
genEquipRadioGroupsProtectionBBSSDAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDAttrEntry.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex = _GenEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 1, 1, 1),
    _GenEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDAttrRevertive_Type = EnableDisable
_GenEquipRadioGroupsProtectionBBSSDAttrRevertive_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDAttrRevertive = _GenEquipRadioGroupsProtectionBBSSDAttrRevertive_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 1, 1, 2),
    _GenEquipRadioGroupsProtectionBBSSDAttrRevertive_Type()
)
genEquipRadioGroupsProtectionBBSSDAttrRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDAttrRevertive.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDAttrClrSwCnt_Type = OffOn
_GenEquipRadioGroupsProtectionBBSSDAttrClrSwCnt_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDAttrClrSwCnt = _GenEquipRadioGroupsProtectionBBSSDAttrClrSwCnt_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 1, 1, 3),
    _GenEquipRadioGroupsProtectionBBSSDAttrClrSwCnt_Type()
)
genEquipRadioGroupsProtectionBBSSDAttrClrSwCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDAttrClrSwCnt.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDAttrFWAuto_Type = EnableDisable
_GenEquipRadioGroupsProtectionBBSSDAttrFWAuto_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDAttrFWAuto = _GenEquipRadioGroupsProtectionBBSSDAttrFWAuto_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 1, 1, 4),
    _GenEquipRadioGroupsProtectionBBSSDAttrFWAuto_Type()
)
genEquipRadioGroupsProtectionBBSSDAttrFWAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDAttrFWAuto.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusTable_Object = MibTable
genEquipRadioGroupsProtectionBBSSDStatusTable = _GenEquipRadioGroupsProtectionBBSSDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusTable.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusEntry_Object = MibTableRow
genEquipRadioGroupsProtectionBBSSDStatusEntry = _GenEquipRadioGroupsProtectionBBSSDStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1)
)
genEquipRadioGroupsProtectionBBSSDStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusEntry.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex = _GenEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 1),
    _GenEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex = _GenEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 2),
    _GenEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality = _GenEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 3),
    _GenEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex = _GenEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 4),
    _GenEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex = _GenEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 5),
    _GenEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusLockout_Type = NoYes
_GenEquipRadioGroupsProtectionBBSSDStatusLockout_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusLockout = _GenEquipRadioGroupsProtectionBBSSDStatusLockout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 6),
    _GenEquipRadioGroupsProtectionBBSSDStatusLockout_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusLockout.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusRxChId_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusRxChId_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusRxChId = _GenEquipRadioGroupsProtectionBBSSDStatusRxChId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 7),
    _GenEquipRadioGroupsProtectionBBSSDStatusRxChId_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusRxChId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusRxChId.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality = _GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 8),
    _GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex = _GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 9),
    _GenEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex_Type = Integer32
_GenEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex_Object = MibTableColumn
genEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex = _GenEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 1, 10, 2, 1, 10),
    _GenEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex_Type()
)
genEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsXpic_ObjectIdentity = ObjectIdentity
genEquipRadioGroupsXpic = _GenEquipRadioGroupsXpic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2)
)
_GenEquipRadioGroupsXPICAttrTable_Object = MibTable
genEquipRadioGroupsXPICAttrTable = _GenEquipRadioGroupsXPICAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrTable.setStatus("mandatory")
_GenEquipRadioGroupsXPICAttrEntry_Object = MibTableRow
genEquipRadioGroupsXPICAttrEntry = _GenEquipRadioGroupsXPICAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1)
)
genEquipRadioGroupsXPICAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsXPICAttrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrEntry.setStatus("mandatory")
_GenEquipRadioGroupsXPICAttrGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsXPICAttrGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsXPICAttrGroupIfIndex = _GenEquipRadioGroupsXPICAttrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1, 1),
    _GenEquipRadioGroupsXPICAttrGroupIfIndex_Type()
)
genEquipRadioGroupsXPICAttrGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex_Type = Integer32
_GenEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex_Object = MibTableColumn
genEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex = _GenEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1, 2),
    _GenEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex_Type()
)
genEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex.setStatus("mandatory")


class _GenEquipRadioGroupsXPICAttrGroupId_Type(Integer32):
    """Custom type genEquipRadioGroupsXPICAttrGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GenEquipRadioGroupsXPICAttrGroupId_Type.__name__ = "Integer32"
_GenEquipRadioGroupsXPICAttrGroupId_Object = MibTableColumn
genEquipRadioGroupsXPICAttrGroupId = _GenEquipRadioGroupsXPICAttrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1, 3),
    _GenEquipRadioGroupsXPICAttrGroupId_Type()
)
genEquipRadioGroupsXPICAttrGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrGroupId.setStatus("mandatory")
_GenEquipRadioGroupsXPICAttrXRSMAdmin_Type = EnableDisable
_GenEquipRadioGroupsXPICAttrXRSMAdmin_Object = MibTableColumn
genEquipRadioGroupsXPICAttrXRSMAdmin = _GenEquipRadioGroupsXPICAttrXRSMAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1, 4),
    _GenEquipRadioGroupsXPICAttrXRSMAdmin_Type()
)
genEquipRadioGroupsXPICAttrXRSMAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrXRSMAdmin.setStatus("mandatory")
_GenEquipRadioGroupsXPICAttrAdmin_Type = EnableDisable
_GenEquipRadioGroupsXPICAttrAdmin_Object = MibTableColumn
genEquipRadioGroupsXPICAttrAdmin = _GenEquipRadioGroupsXPICAttrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1, 5),
    _GenEquipRadioGroupsXPICAttrAdmin_Type()
)
genEquipRadioGroupsXPICAttrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrAdmin.setStatus("mandatory")
_GenEquipRadioGroupsXPICAttrCopyToMate_Type = Copy2mate
_GenEquipRadioGroupsXPICAttrCopyToMate_Object = MibTableColumn
genEquipRadioGroupsXPICAttrCopyToMate = _GenEquipRadioGroupsXPICAttrCopyToMate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 1, 1, 6),
    _GenEquipRadioGroupsXPICAttrCopyToMate_Type()
)
genEquipRadioGroupsXPICAttrCopyToMate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICAttrCopyToMate.setStatus("mandatory")
_GenEquipRadioGroupsXPICMembersTable_Object = MibTable
genEquipRadioGroupsXPICMembersTable = _GenEquipRadioGroupsXPICMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICMembersTable.setStatus("mandatory")
_GenEquipRadioGroupsXPICMembersEntry_Object = MibTableRow
genEquipRadioGroupsXPICMembersEntry = _GenEquipRadioGroupsXPICMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 2, 1)
)
genEquipRadioGroupsXPICMembersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsXPICMembersIfIndexGroup"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICMembersEntry.setStatus("mandatory")
_GenEquipRadioGroupsXPICMembersIfIndexGroup_Type = Integer32
_GenEquipRadioGroupsXPICMembersIfIndexGroup_Object = MibTableColumn
genEquipRadioGroupsXPICMembersIfIndexGroup = _GenEquipRadioGroupsXPICMembersIfIndexGroup_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 2, 1, 1),
    _GenEquipRadioGroupsXPICMembersIfIndexGroup_Type()
)
genEquipRadioGroupsXPICMembersIfIndexGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICMembersIfIndexGroup.setStatus("mandatory")


class _GenEquipRadioGroupsXPICMembersMem1IfIndex_Type(Integer32):
    """Custom type genEquipRadioGroupsXPICMembersMem1IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GenEquipRadioGroupsXPICMembersMem1IfIndex_Type.__name__ = "Integer32"
_GenEquipRadioGroupsXPICMembersMem1IfIndex_Object = MibTableColumn
genEquipRadioGroupsXPICMembersMem1IfIndex = _GenEquipRadioGroupsXPICMembersMem1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 2, 1, 2),
    _GenEquipRadioGroupsXPICMembersMem1IfIndex_Type()
)
genEquipRadioGroupsXPICMembersMem1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICMembersMem1IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsXPICMembersMem2IfIndex_Type = Integer32
_GenEquipRadioGroupsXPICMembersMem2IfIndex_Object = MibTableColumn
genEquipRadioGroupsXPICMembersMem2IfIndex = _GenEquipRadioGroupsXPICMembersMem2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 2, 1, 3),
    _GenEquipRadioGroupsXPICMembersMem2IfIndex_Type()
)
genEquipRadioGroupsXPICMembersMem2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICMembersMem2IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsXPICMembersRowStatus_Type = RowStatus
_GenEquipRadioGroupsXPICMembersRowStatus_Object = MibTableColumn
genEquipRadioGroupsXPICMembersRowStatus = _GenEquipRadioGroupsXPICMembersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 2, 1, 30),
    _GenEquipRadioGroupsXPICMembersRowStatus_Type()
)
genEquipRadioGroupsXPICMembersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICMembersRowStatus.setStatus("mandatory")
_GenEquipRadioGroupsXPICStatusTable_Object = MibTable
genEquipRadioGroupsXPICStatusTable = _GenEquipRadioGroupsXPICStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICStatusTable.setStatus("mandatory")
_GenEquipRadioGroupsXPICStatusEntry_Object = MibTableRow
genEquipRadioGroupsXPICStatusEntry = _GenEquipRadioGroupsXPICStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 3, 1)
)
genEquipRadioGroupsXPICStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsXPICStatusGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICStatusEntry.setStatus("mandatory")
_GenEquipRadioGroupsXPICStatusGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsXPICStatusGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsXPICStatusGroupIfIndex = _GenEquipRadioGroupsXPICStatusGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 3, 1, 1),
    _GenEquipRadioGroupsXPICStatusGroupIfIndex_Type()
)
genEquipRadioGroupsXPICStatusGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICStatusGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsXPICStatusState_Type = XpicState
_GenEquipRadioGroupsXPICStatusState_Object = MibTableColumn
genEquipRadioGroupsXPICStatusState = _GenEquipRadioGroupsXPICStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 2, 3, 1, 2),
    _GenEquipRadioGroupsXPICStatusState_Type()
)
genEquipRadioGroupsXPICStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsXPICStatusState.setStatus("mandatory")
_GenEquipRadioGroupsMR_ObjectIdentity = ObjectIdentity
genEquipRadioGroupsMR = _GenEquipRadioGroupsMR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3)
)
_GenEquipRadioGroupsMRAttrTable_Object = MibTable
genEquipRadioGroupsMRAttrTable = _GenEquipRadioGroupsMRAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrTable.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrEntry_Object = MibTableRow
genEquipRadioGroupsMRAttrEntry = _GenEquipRadioGroupsMRAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1)
)
genEquipRadioGroupsMRAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsMRAttrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrEntry.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsMRAttrGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsMRAttrGroupIfIndex = _GenEquipRadioGroupsMRAttrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 1),
    _GenEquipRadioGroupsMRAttrGroupIfIndex_Type()
)
genEquipRadioGroupsMRAttrGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrGroupIfIndex.setStatus("mandatory")


class _GenEquipRadioGroupsMRAttrGroupId_Type(Integer32):
    """Custom type genEquipRadioGroupsMRAttrGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GenEquipRadioGroupsMRAttrGroupId_Type.__name__ = "Integer32"
_GenEquipRadioGroupsMRAttrGroupId_Object = MibTableColumn
genEquipRadioGroupsMRAttrGroupId = _GenEquipRadioGroupsMRAttrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 2),
    _GenEquipRadioGroupsMRAttrGroupId_Type()
)
genEquipRadioGroupsMRAttrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrGroupId.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrAdmin_Type = EnableDisable
_GenEquipRadioGroupsMRAttrAdmin_Object = MibTableColumn
genEquipRadioGroupsMRAttrAdmin = _GenEquipRadioGroupsMRAttrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 3),
    _GenEquipRadioGroupsMRAttrAdmin_Type()
)
genEquipRadioGroupsMRAttrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrBlockRadioIfindex_Type = Integer32
_GenEquipRadioGroupsMRAttrBlockRadioIfindex_Object = MibTableColumn
genEquipRadioGroupsMRAttrBlockRadioIfindex = _GenEquipRadioGroupsMRAttrBlockRadioIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 4),
    _GenEquipRadioGroupsMRAttrBlockRadioIfindex_Type()
)
genEquipRadioGroupsMRAttrBlockRadioIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrBlockRadioIfindex.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrBlockRadioAdmin_Type = EnableDisable
_GenEquipRadioGroupsMRAttrBlockRadioAdmin_Object = MibTableColumn
genEquipRadioGroupsMRAttrBlockRadioAdmin = _GenEquipRadioGroupsMRAttrBlockRadioAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 5),
    _GenEquipRadioGroupsMRAttrBlockRadioAdmin_Type()
)
genEquipRadioGroupsMRAttrBlockRadioAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrBlockRadioAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrCopy2MateIfindex_Type = Integer32
_GenEquipRadioGroupsMRAttrCopy2MateIfindex_Object = MibTableColumn
genEquipRadioGroupsMRAttrCopy2MateIfindex = _GenEquipRadioGroupsMRAttrCopy2MateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 6),
    _GenEquipRadioGroupsMRAttrCopy2MateIfindex_Type()
)
genEquipRadioGroupsMRAttrCopy2MateIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrCopy2MateIfindex.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrCopy2MateAdmin_Type = EnableDisable
_GenEquipRadioGroupsMRAttrCopy2MateAdmin_Object = MibTableColumn
genEquipRadioGroupsMRAttrCopy2MateAdmin = _GenEquipRadioGroupsMRAttrCopy2MateAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 7),
    _GenEquipRadioGroupsMRAttrCopy2MateAdmin_Type()
)
genEquipRadioGroupsMRAttrCopy2MateAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrCopy2MateAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrExBerAdmin_Type = EnableDisable
_GenEquipRadioGroupsMRAttrExBerAdmin_Object = MibTableColumn
genEquipRadioGroupsMRAttrExBerAdmin = _GenEquipRadioGroupsMRAttrExBerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 8),
    _GenEquipRadioGroupsMRAttrExBerAdmin_Type()
)
genEquipRadioGroupsMRAttrExBerAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrExBerAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrMinNumRadio_Type = Integer32
_GenEquipRadioGroupsMRAttrMinNumRadio_Object = MibTableColumn
genEquipRadioGroupsMRAttrMinNumRadio = _GenEquipRadioGroupsMRAttrMinNumRadio_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 9),
    _GenEquipRadioGroupsMRAttrMinNumRadio_Type()
)
genEquipRadioGroupsMRAttrMinNumRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrMinNumRadio.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrMinProfileAdmin_Type = EnableDisable
_GenEquipRadioGroupsMRAttrMinProfileAdmin_Object = MibTableColumn
genEquipRadioGroupsMRAttrMinProfileAdmin = _GenEquipRadioGroupsMRAttrMinProfileAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 10),
    _GenEquipRadioGroupsMRAttrMinProfileAdmin_Type()
)
genEquipRadioGroupsMRAttrMinProfileAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrMinProfileAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMRAttrSigDegardeAdmin_Type = EnableDisable
_GenEquipRadioGroupsMRAttrSigDegardeAdmin_Object = MibTableColumn
genEquipRadioGroupsMRAttrSigDegardeAdmin = _GenEquipRadioGroupsMRAttrSigDegardeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 1, 1, 11),
    _GenEquipRadioGroupsMRAttrSigDegardeAdmin_Type()
)
genEquipRadioGroupsMRAttrSigDegardeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRAttrSigDegardeAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMRMembersTable_Object = MibTable
genEquipRadioGroupsMRMembersTable = _GenEquipRadioGroupsMRMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRMembersTable.setStatus("mandatory")
_GenEquipRadioGroupsMRMembersEntry_Object = MibTableRow
genEquipRadioGroupsMRMembersEntry = _GenEquipRadioGroupsMRMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 2, 1)
)
genEquipRadioGroupsMRMembersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsMRMembersIfIndexGroup"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRMembersEntry.setStatus("mandatory")
_GenEquipRadioGroupsMRMembersIfIndexGroup_Type = Integer32
_GenEquipRadioGroupsMRMembersIfIndexGroup_Object = MibTableColumn
genEquipRadioGroupsMRMembersIfIndexGroup = _GenEquipRadioGroupsMRMembersIfIndexGroup_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 2, 1, 1),
    _GenEquipRadioGroupsMRMembersIfIndexGroup_Type()
)
genEquipRadioGroupsMRMembersIfIndexGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRMembersIfIndexGroup.setStatus("mandatory")
_GenEquipRadioGroupsMRMembersMem1IfIndex_Type = Integer32
_GenEquipRadioGroupsMRMembersMem1IfIndex_Object = MibTableColumn
genEquipRadioGroupsMRMembersMem1IfIndex = _GenEquipRadioGroupsMRMembersMem1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 2, 1, 2),
    _GenEquipRadioGroupsMRMembersMem1IfIndex_Type()
)
genEquipRadioGroupsMRMembersMem1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRMembersMem1IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMRMembersMem2IfIndex_Type = Integer32
_GenEquipRadioGroupsMRMembersMem2IfIndex_Object = MibTableColumn
genEquipRadioGroupsMRMembersMem2IfIndex = _GenEquipRadioGroupsMRMembersMem2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 2, 1, 3),
    _GenEquipRadioGroupsMRMembersMem2IfIndex_Type()
)
genEquipRadioGroupsMRMembersMem2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRMembersMem2IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMRMembersRowStatus_Type = RowStatus
_GenEquipRadioGroupsMRMembersRowStatus_Object = MibTableColumn
genEquipRadioGroupsMRMembersRowStatus = _GenEquipRadioGroupsMRMembersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 2, 1, 30),
    _GenEquipRadioGroupsMRMembersRowStatus_Type()
)
genEquipRadioGroupsMRMembersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRMembersRowStatus.setStatus("mandatory")
_GenEquipRadioGroupsMRStatusTable_Object = MibTable
genEquipRadioGroupsMRStatusTable = _GenEquipRadioGroupsMRStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRStatusTable.setStatus("mandatory")
_GenEquipRadioGroupsMRStatusEntry_Object = MibTableRow
genEquipRadioGroupsMRStatusEntry = _GenEquipRadioGroupsMRStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 3, 1)
)
genEquipRadioGroupsMRStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsMRStatusGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRStatusEntry.setStatus("mandatory")
_GenEquipRadioGroupsMRStatusGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsMRStatusGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsMRStatusGroupIfIndex = _GenEquipRadioGroupsMRStatusGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 3, 1, 1),
    _GenEquipRadioGroupsMRStatusGroupIfIndex_Type()
)
genEquipRadioGroupsMRStatusGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRStatusGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMRStatusOpertionalState_Type = Integer32
_GenEquipRadioGroupsMRStatusOpertionalState_Object = MibTableColumn
genEquipRadioGroupsMRStatusOpertionalState = _GenEquipRadioGroupsMRStatusOpertionalState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 3, 1, 2),
    _GenEquipRadioGroupsMRStatusOpertionalState_Type()
)
genEquipRadioGroupsMRStatusOpertionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRStatusOpertionalState.setStatus("mandatory")
_GenEquipRadioGroupsMRStatusRemoteOpertionalState_Type = Integer32
_GenEquipRadioGroupsMRStatusRemoteOpertionalState_Object = MibTableColumn
genEquipRadioGroupsMRStatusRemoteOpertionalState = _GenEquipRadioGroupsMRStatusRemoteOpertionalState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 3, 3, 1, 3),
    _GenEquipRadioGroupsMRStatusRemoteOpertionalState_Type()
)
genEquipRadioGroupsMRStatusRemoteOpertionalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMRStatusRemoteOpertionalState.setStatus("mandatory")
_GenEquipRadioGroupsMIMO_ObjectIdentity = ObjectIdentity
genEquipRadioGroupsMIMO = _GenEquipRadioGroupsMIMO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4)
)
_GenEquipRadioGroupsMIMOAttrTable_Object = MibTable
genEquipRadioGroupsMIMOAttrTable = _GenEquipRadioGroupsMIMOAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOAttrTable.setStatus("mandatory")
_GenEquipRadioGroupsMIMOAttrEntry_Object = MibTableRow
genEquipRadioGroupsMIMOAttrEntry = _GenEquipRadioGroupsMIMOAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 1, 1)
)
genEquipRadioGroupsMIMOAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsMIMOAttrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOAttrEntry.setStatus("mandatory")
_GenEquipRadioGroupsMIMOAttrGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOAttrGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOAttrGroupIfIndex = _GenEquipRadioGroupsMIMOAttrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 1, 1, 1),
    _GenEquipRadioGroupsMIMOAttrGroupIfIndex_Type()
)
genEquipRadioGroupsMIMOAttrGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOAttrGroupIfIndex.setStatus("mandatory")


class _GenEquipRadioGroupsMIMOAttrRole_Type(Integer32):
    """Custom type genEquipRadioGroupsMIMOAttrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("not-relevant", 2),
          ("slave", 0))
    )


_GenEquipRadioGroupsMIMOAttrRole_Type.__name__ = "Integer32"
_GenEquipRadioGroupsMIMOAttrRole_Object = MibTableColumn
genEquipRadioGroupsMIMOAttrRole = _GenEquipRadioGroupsMIMOAttrRole_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 1, 1, 2),
    _GenEquipRadioGroupsMIMOAttrRole_Type()
)
genEquipRadioGroupsMIMOAttrRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOAttrRole.setStatus("mandatory")
_GenEquipRadioGroupsMIMOAttrAdmin_Type = EnableDisable
_GenEquipRadioGroupsMIMOAttrAdmin_Object = MibTableColumn
genEquipRadioGroupsMIMOAttrAdmin = _GenEquipRadioGroupsMIMOAttrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 1, 1, 3),
    _GenEquipRadioGroupsMIMOAttrAdmin_Type()
)
genEquipRadioGroupsMIMOAttrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOAttrAdmin.setStatus("mandatory")
_GenEquipRadioGroupsMIMOAttrResetStateMachine_Type = OffOn
_GenEquipRadioGroupsMIMOAttrResetStateMachine_Object = MibTableColumn
genEquipRadioGroupsMIMOAttrResetStateMachine = _GenEquipRadioGroupsMIMOAttrResetStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 1, 1, 4),
    _GenEquipRadioGroupsMIMOAttrResetStateMachine_Type()
)
genEquipRadioGroupsMIMOAttrResetStateMachine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOAttrResetStateMachine.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersTable_Object = MibTable
genEquipRadioGroupsMIMOMembersTable = _GenEquipRadioGroupsMIMOMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersTable.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersEntry_Object = MibTableRow
genEquipRadioGroupsMIMOMembersEntry = _GenEquipRadioGroupsMIMOMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1)
)
genEquipRadioGroupsMIMOMembersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsMIMOMembersGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersEntry.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOMembersGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersGroupIfIndex = _GenEquipRadioGroupsMIMOMembersGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 1),
    _GenEquipRadioGroupsMIMOMembersGroupIfIndex_Type()
)
genEquipRadioGroupsMIMOMembersGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersGroupIfIndex.setStatus("mandatory")


class _GenEquipRadioGroupsMIMOMembersGroupType_Type(Integer32):
    """Custom type genEquipRadioGroupsMIMOMembersGroupType based on Integer32"""
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
        *(("base-band-combining-2x2", 2),
          ("base-band-combining-4x4", 3),
          ("mimo-2x2", 0),
          ("mimo-4x4", 1))
    )


_GenEquipRadioGroupsMIMOMembersGroupType_Type.__name__ = "Integer32"
_GenEquipRadioGroupsMIMOMembersGroupType_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersGroupType = _GenEquipRadioGroupsMIMOMembersGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 2),
    _GenEquipRadioGroupsMIMOMembersGroupType_Type()
)
genEquipRadioGroupsMIMOMembersGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersGroupType.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersMem1IfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOMembersMem1IfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersMem1IfIndex = _GenEquipRadioGroupsMIMOMembersMem1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 3),
    _GenEquipRadioGroupsMIMOMembersMem1IfIndex_Type()
)
genEquipRadioGroupsMIMOMembersMem1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersMem1IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersMem2IfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOMembersMem2IfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersMem2IfIndex = _GenEquipRadioGroupsMIMOMembersMem2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 4),
    _GenEquipRadioGroupsMIMOMembersMem2IfIndex_Type()
)
genEquipRadioGroupsMIMOMembersMem2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersMem2IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersMem3IfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOMembersMem3IfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersMem3IfIndex = _GenEquipRadioGroupsMIMOMembersMem3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 5),
    _GenEquipRadioGroupsMIMOMembersMem3IfIndex_Type()
)
genEquipRadioGroupsMIMOMembersMem3IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersMem3IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersMem4IfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOMembersMem4IfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersMem4IfIndex = _GenEquipRadioGroupsMIMOMembersMem4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 6),
    _GenEquipRadioGroupsMIMOMembersMem4IfIndex_Type()
)
genEquipRadioGroupsMIMOMembersMem4IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersMem4IfIndex.setStatus("mandatory")
_GenEquipRadioGroupsMIMOMembersRowStatus_Type = RowStatus
_GenEquipRadioGroupsMIMOMembersRowStatus_Object = MibTableColumn
genEquipRadioGroupsMIMOMembersRowStatus = _GenEquipRadioGroupsMIMOMembersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 2, 1, 30),
    _GenEquipRadioGroupsMIMOMembersRowStatus_Type()
)
genEquipRadioGroupsMIMOMembersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOMembersRowStatus.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatusTable_Object = MibTable
genEquipRadioGroupsMIMOStatusTable = _GenEquipRadioGroupsMIMOStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatusTable.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatusEntry_Object = MibTableRow
genEquipRadioGroupsMIMOStatusEntry = _GenEquipRadioGroupsMIMOStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1)
)
genEquipRadioGroupsMIMOStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsMIMOStatusGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatusEntry.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatusGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsMIMOStatusGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsMIMOStatusGroupIfIndex = _GenEquipRadioGroupsMIMOStatusGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 1),
    _GenEquipRadioGroupsMIMOStatusGroupIfIndex_Type()
)
genEquipRadioGroupsMIMOStatusGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatusGroupIfIndex.setStatus("mandatory")


class _GenEquipRadioGroupsMIMOStatusState_Type(Integer32):
    """Custom type genEquipRadioGroupsMIMOStatusState based on Integer32"""
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
        *(("disabled", 2),
          ("half-capacity", 5),
          ("idle", 3),
          ("init", 1),
          ("recovery", 4),
          ("slave", 0))
    )


_GenEquipRadioGroupsMIMOStatusState_Type.__name__ = "Integer32"
_GenEquipRadioGroupsMIMOStatusState_Object = MibTableColumn
genEquipRadioGroupsMIMOStatusState = _GenEquipRadioGroupsMIMOStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 2),
    _GenEquipRadioGroupsMIMOStatusState_Type()
)
genEquipRadioGroupsMIMOStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatusState.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatus1stMMI_Type = Integer32
_GenEquipRadioGroupsMIMOStatus1stMMI_Object = MibTableColumn
genEquipRadioGroupsMIMOStatus1stMMI = _GenEquipRadioGroupsMIMOStatus1stMMI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 3),
    _GenEquipRadioGroupsMIMOStatus1stMMI_Type()
)
genEquipRadioGroupsMIMOStatus1stMMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatus1stMMI.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatus2ndMMI_Type = Integer32
_GenEquipRadioGroupsMIMOStatus2ndMMI_Object = MibTableColumn
genEquipRadioGroupsMIMOStatus2ndMMI = _GenEquipRadioGroupsMIMOStatus2ndMMI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 4),
    _GenEquipRadioGroupsMIMOStatus2ndMMI_Type()
)
genEquipRadioGroupsMIMOStatus2ndMMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatus2ndMMI.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatus3rdMMI_Type = Integer32
_GenEquipRadioGroupsMIMOStatus3rdMMI_Object = MibTableColumn
genEquipRadioGroupsMIMOStatus3rdMMI = _GenEquipRadioGroupsMIMOStatus3rdMMI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 5),
    _GenEquipRadioGroupsMIMOStatus3rdMMI_Type()
)
genEquipRadioGroupsMIMOStatus3rdMMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatus3rdMMI.setStatus("mandatory")
_GenEquipRadioGroupsMIMOStatus4thMMI_Type = Integer32
_GenEquipRadioGroupsMIMOStatus4thMMI_Object = MibTableColumn
genEquipRadioGroupsMIMOStatus4thMMI = _GenEquipRadioGroupsMIMOStatus4thMMI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 6),
    _GenEquipRadioGroupsMIMOStatus4thMMI_Type()
)
genEquipRadioGroupsMIMOStatus4thMMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatus4thMMI.setStatus("mandatory")


class _GenEquipRadioGroupsMIMOStatusAdvancedState_Type(Integer32):
    """Custom type genEquipRadioGroupsMIMOStatusAdvancedState based on Integer32"""
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
        *(("disabled", 0),
          ("half-capacity", 7),
          ("half-capacity-master-failure", 17),
          ("half-capacity-no-master", 16),
          ("idle", 5),
          ("init-retry", 2),
          ("init-retry-bringup", 4),
          ("init-retry-checkup", 3),
          ("initializing", 1),
          ("master-failure", 8),
          ("mute-slave", 11),
          ("remote-has-no-master", 10),
          ("remote-master-failure", 9),
          ("self-mute-comm-fail-to-master", 15),
          ("slave-idle", 13),
          ("slave-init", 12),
          ("slave-mutted", 14),
          ("unsuitable-hw", 6))
    )


_GenEquipRadioGroupsMIMOStatusAdvancedState_Type.__name__ = "Integer32"
_GenEquipRadioGroupsMIMOStatusAdvancedState_Object = MibTableColumn
genEquipRadioGroupsMIMOStatusAdvancedState = _GenEquipRadioGroupsMIMOStatusAdvancedState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 4, 3, 1, 7),
    _GenEquipRadioGroupsMIMOStatusAdvancedState_Type()
)
genEquipRadioGroupsMIMOStatusAdvancedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsMIMOStatusAdvancedState.setStatus("mandatory")
_GenEquipRadioGroupsAbc_ObjectIdentity = ObjectIdentity
genEquipRadioGroupsAbc = _GenEquipRadioGroupsAbc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5)
)
_GenEquipRadioGroupsAbcAttrTable_Object = MibTable
genEquipRadioGroupsAbcAttrTable = _GenEquipRadioGroupsAbcAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrTable.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrEntry_Object = MibTableRow
genEquipRadioGroupsAbcAttrEntry = _GenEquipRadioGroupsAbcAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1)
)
genEquipRadioGroupsAbcAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsAbcAttrIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrEntry.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcAttrIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcAttrIfIndex = _GenEquipRadioGroupsAbcAttrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 1),
    _GenEquipRadioGroupsAbcAttrIfIndex_Type()
)
genEquipRadioGroupsAbcAttrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrGroupName_Type = DisplayString
_GenEquipRadioGroupsAbcAttrGroupName_Object = MibTableColumn
genEquipRadioGroupsAbcAttrGroupName = _GenEquipRadioGroupsAbcAttrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 2),
    _GenEquipRadioGroupsAbcAttrGroupName_Type()
)
genEquipRadioGroupsAbcAttrGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrGroupName.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrAdminState_Type = EnableDisable
_GenEquipRadioGroupsAbcAttrAdminState_Object = MibTableColumn
genEquipRadioGroupsAbcAttrAdminState = _GenEquipRadioGroupsAbcAttrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 3),
    _GenEquipRadioGroupsAbcAttrAdminState_Type()
)
genEquipRadioGroupsAbcAttrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrAdminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrQnumberOfRadioMembers_Type = Integer32
_GenEquipRadioGroupsAbcAttrQnumberOfRadioMembers_Object = MibTableColumn
genEquipRadioGroupsAbcAttrQnumberOfRadioMembers = _GenEquipRadioGroupsAbcAttrQnumberOfRadioMembers_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 4),
    _GenEquipRadioGroupsAbcAttrQnumberOfRadioMembers_Type()
)
genEquipRadioGroupsAbcAttrQnumberOfRadioMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrQnumberOfRadioMembers.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrProtectionEnable_Type = EnableDisable
_GenEquipRadioGroupsAbcAttrProtectionEnable_Object = MibTableColumn
genEquipRadioGroupsAbcAttrProtectionEnable = _GenEquipRadioGroupsAbcAttrProtectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 5),
    _GenEquipRadioGroupsAbcAttrProtectionEnable_Type()
)
genEquipRadioGroupsAbcAttrProtectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrProtectionEnable.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrHighPriEthernetBandwidth_Type = Integer32
_GenEquipRadioGroupsAbcAttrHighPriEthernetBandwidth_Object = MibTableColumn
genEquipRadioGroupsAbcAttrHighPriEthernetBandwidth = _GenEquipRadioGroupsAbcAttrHighPriEthernetBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 6),
    _GenEquipRadioGroupsAbcAttrHighPriEthernetBandwidth_Type()
)
genEquipRadioGroupsAbcAttrHighPriEthernetBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrHighPriEthernetBandwidth.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrQualityThreshold_Type = Integer32
_GenEquipRadioGroupsAbcAttrQualityThreshold_Object = MibTableColumn
genEquipRadioGroupsAbcAttrQualityThreshold = _GenEquipRadioGroupsAbcAttrQualityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 7),
    _GenEquipRadioGroupsAbcAttrQualityThreshold_Type()
)
genEquipRadioGroupsAbcAttrQualityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrQualityThreshold.setStatus("mandatory")
_GenEquipRadioGroupsAbcAttrRowStatus_Type = RowStatus
_GenEquipRadioGroupsAbcAttrRowStatus_Object = MibTableColumn
genEquipRadioGroupsAbcAttrRowStatus = _GenEquipRadioGroupsAbcAttrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 1, 1, 30),
    _GenEquipRadioGroupsAbcAttrRowStatus_Type()
)
genEquipRadioGroupsAbcAttrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcAttrRowStatus.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersTable_Object = MibTable
genEquipRadioGroupsAbcMembersTable = _GenEquipRadioGroupsAbcMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersTable.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersEntry_Object = MibTableRow
genEquipRadioGroupsAbcMembersEntry = _GenEquipRadioGroupsAbcMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1)
)
genEquipRadioGroupsAbcMembersEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsAbcMembersGroupIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersEntry.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersGroupIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersGroupIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersGroupIfIndex = _GenEquipRadioGroupsAbcMembersGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 1),
    _GenEquipRadioGroupsAbcMembersGroupIfIndex_Type()
)
genEquipRadioGroupsAbcMembersGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersGroupIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersGroupId_Type = Integer32
_GenEquipRadioGroupsAbcMembersGroupId_Object = MibTableColumn
genEquipRadioGroupsAbcMembersGroupId = _GenEquipRadioGroupsAbcMembersGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 2),
    _GenEquipRadioGroupsAbcMembersGroupId_Type()
)
genEquipRadioGroupsAbcMembersGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersGroupId.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel1MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel1MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel1MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel1MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 3),
    _GenEquipRadioGroupsAbcMembersChannel1MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel1MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel1MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel1adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel1adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel1adminState = _GenEquipRadioGroupsAbcMembersChannel1adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 4),
    _GenEquipRadioGroupsAbcMembersChannel1adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel1adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel1adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel2MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel2MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel2MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel2MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 5),
    _GenEquipRadioGroupsAbcMembersChannel2MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel2MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel2MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel2adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel2adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel2adminState = _GenEquipRadioGroupsAbcMembersChannel2adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 6),
    _GenEquipRadioGroupsAbcMembersChannel2adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel2adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel2adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel3MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel3MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel3MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel3MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 7),
    _GenEquipRadioGroupsAbcMembersChannel3MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel3MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel3MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel3adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel3adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel3adminState = _GenEquipRadioGroupsAbcMembersChannel3adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 8),
    _GenEquipRadioGroupsAbcMembersChannel3adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel3adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel3adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel4MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel4MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel4MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel4MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 9),
    _GenEquipRadioGroupsAbcMembersChannel4MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel4MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel4MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel4adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel4adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel4adminState = _GenEquipRadioGroupsAbcMembersChannel4adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 10),
    _GenEquipRadioGroupsAbcMembersChannel4adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel4adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel4adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel5MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel5MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel5MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel5MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 11),
    _GenEquipRadioGroupsAbcMembersChannel5MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel5MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel5MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel5adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel5adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel5adminState = _GenEquipRadioGroupsAbcMembersChannel5adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 12),
    _GenEquipRadioGroupsAbcMembersChannel5adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel5adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel5adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel6MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel6MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel6MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel6MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 13),
    _GenEquipRadioGroupsAbcMembersChannel6MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel6MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel6MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel6adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel6adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel6adminState = _GenEquipRadioGroupsAbcMembersChannel6adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 14),
    _GenEquipRadioGroupsAbcMembersChannel6adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel6adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel6adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel7MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel7MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel7MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel7MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 15),
    _GenEquipRadioGroupsAbcMembersChannel7MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel7MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel7MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel7adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel7adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel7adminState = _GenEquipRadioGroupsAbcMembersChannel7adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 16),
    _GenEquipRadioGroupsAbcMembersChannel7adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel7adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel7adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel8MemberIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcMembersChannel8MemberIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel8MemberIfIndex = _GenEquipRadioGroupsAbcMembersChannel8MemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 17),
    _GenEquipRadioGroupsAbcMembersChannel8MemberIfIndex_Type()
)
genEquipRadioGroupsAbcMembersChannel8MemberIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel8MemberIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcMembersChannel8adminState_Type = EnableDisable
_GenEquipRadioGroupsAbcMembersChannel8adminState_Object = MibTableColumn
genEquipRadioGroupsAbcMembersChannel8adminState = _GenEquipRadioGroupsAbcMembersChannel8adminState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 2, 1, 18),
    _GenEquipRadioGroupsAbcMembersChannel8adminState_Type()
)
genEquipRadioGroupsAbcMembersChannel8adminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcMembersChannel8adminState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusTable_Object = MibTable
genEquipRadioGroupsAbcStatusTable = _GenEquipRadioGroupsAbcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3)
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusTable.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusEntry_Object = MibTableRow
genEquipRadioGroupsAbcStatusEntry = _GenEquipRadioGroupsAbcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1)
)
genEquipRadioGroupsAbcStatusEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioGroupsAbcStatusIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusEntry.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusIfIndex_Type = Integer32
_GenEquipRadioGroupsAbcStatusIfIndex_Object = MibTableColumn
genEquipRadioGroupsAbcStatusIfIndex = _GenEquipRadioGroupsAbcStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 1),
    _GenEquipRadioGroupsAbcStatusIfIndex_Type()
)
genEquipRadioGroupsAbcStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusIfIndex.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusOperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusOperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusOperState = _GenEquipRadioGroupsAbcStatusOperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 2),
    _GenEquipRadioGroupsAbcStatusOperState_Type()
)
genEquipRadioGroupsAbcStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusOperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusRemoteOperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusRemoteOperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusRemoteOperState = _GenEquipRadioGroupsAbcStatusRemoteOperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 3),
    _GenEquipRadioGroupsAbcStatusRemoteOperState_Type()
)
genEquipRadioGroupsAbcStatusRemoteOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusRemoteOperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX_Type = Integer32
_GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX_Object = MibTableColumn
genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX = _GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 4),
    _GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX_Type()
)
genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX_Type = Integer32
_GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX_Object = MibTableColumn
genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX = _GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 5),
    _GenEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX_Type()
)
genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel1Operstate_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel1Operstate_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel1Operstate = _GenEquipRadioGroupsAbcStatusChannel1Operstate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 6),
    _GenEquipRadioGroupsAbcStatusChannel1Operstate_Type()
)
genEquipRadioGroupsAbcStatusChannel1Operstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel1Operstate.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel1Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel1Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel1Capacity = _GenEquipRadioGroupsAbcStatusChannel1Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 7),
    _GenEquipRadioGroupsAbcStatusChannel1Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel1Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel1Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel2Operstate_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel2Operstate_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel2Operstate = _GenEquipRadioGroupsAbcStatusChannel2Operstate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 8),
    _GenEquipRadioGroupsAbcStatusChannel2Operstate_Type()
)
genEquipRadioGroupsAbcStatusChannel2Operstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel2Operstate.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel2Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel2Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel2Capacity = _GenEquipRadioGroupsAbcStatusChannel2Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 9),
    _GenEquipRadioGroupsAbcStatusChannel2Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel2Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel2Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel3OperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel3OperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel3OperState = _GenEquipRadioGroupsAbcStatusChannel3OperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 10),
    _GenEquipRadioGroupsAbcStatusChannel3OperState_Type()
)
genEquipRadioGroupsAbcStatusChannel3OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel3OperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel3Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel3Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel3Capacity = _GenEquipRadioGroupsAbcStatusChannel3Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 11),
    _GenEquipRadioGroupsAbcStatusChannel3Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel3Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel3Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel4OperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel4OperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel4OperState = _GenEquipRadioGroupsAbcStatusChannel4OperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 12),
    _GenEquipRadioGroupsAbcStatusChannel4OperState_Type()
)
genEquipRadioGroupsAbcStatusChannel4OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel4OperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel4Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel4Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel4Capacity = _GenEquipRadioGroupsAbcStatusChannel4Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 13),
    _GenEquipRadioGroupsAbcStatusChannel4Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel4Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel4Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel5OperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel5OperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel5OperState = _GenEquipRadioGroupsAbcStatusChannel5OperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 14),
    _GenEquipRadioGroupsAbcStatusChannel5OperState_Type()
)
genEquipRadioGroupsAbcStatusChannel5OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel5OperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel5Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel5Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel5Capacity = _GenEquipRadioGroupsAbcStatusChannel5Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 15),
    _GenEquipRadioGroupsAbcStatusChannel5Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel5Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel5Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel6OperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel6OperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel6OperState = _GenEquipRadioGroupsAbcStatusChannel6OperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 16),
    _GenEquipRadioGroupsAbcStatusChannel6OperState_Type()
)
genEquipRadioGroupsAbcStatusChannel6OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel6OperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel6Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel6Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel6Capacity = _GenEquipRadioGroupsAbcStatusChannel6Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 17),
    _GenEquipRadioGroupsAbcStatusChannel6Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel6Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel6Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel7OperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel7OperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel7OperState = _GenEquipRadioGroupsAbcStatusChannel7OperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 18),
    _GenEquipRadioGroupsAbcStatusChannel7OperState_Type()
)
genEquipRadioGroupsAbcStatusChannel7OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel7OperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel7Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel7Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel7Capacity = _GenEquipRadioGroupsAbcStatusChannel7Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 19),
    _GenEquipRadioGroupsAbcStatusChannel7Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel7Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel7Capacity.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel8OperState_Type = DownUp
_GenEquipRadioGroupsAbcStatusChannel8OperState_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel8OperState = _GenEquipRadioGroupsAbcStatusChannel8OperState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 20),
    _GenEquipRadioGroupsAbcStatusChannel8OperState_Type()
)
genEquipRadioGroupsAbcStatusChannel8OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel8OperState.setStatus("mandatory")
_GenEquipRadioGroupsAbcStatusChannel8Capacity_Type = Integer32
_GenEquipRadioGroupsAbcStatusChannel8Capacity_Object = MibTableColumn
genEquipRadioGroupsAbcStatusChannel8Capacity = _GenEquipRadioGroupsAbcStatusChannel8Capacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 3, 1, 21),
    _GenEquipRadioGroupsAbcStatusChannel8Capacity_Type()
)
genEquipRadioGroupsAbcStatusChannel8Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipRadioGroupsAbcStatusChannel8Capacity.setStatus("mandatory")
_GenEquipStm1AbcAttrTable_Object = MibTable
genEquipStm1AbcAttrTable = _GenEquipStm1AbcAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5)
)
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrTable.setStatus("mandatory")
_GenEquipStm1AbcAttrEntry_Object = MibTableRow
genEquipStm1AbcAttrEntry = _GenEquipStm1AbcAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1)
)
genEquipStm1AbcAttrEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipStm1AbcAttrIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrEntry.setStatus("mandatory")
_GenEquipStm1AbcAttrIfIndex_Type = Integer32
_GenEquipStm1AbcAttrIfIndex_Object = MibTableColumn
genEquipStm1AbcAttrIfIndex = _GenEquipStm1AbcAttrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 1),
    _GenEquipStm1AbcAttrIfIndex_Type()
)
genEquipStm1AbcAttrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrIfIndex.setStatus("mandatory")
_GenEquipStm1AbcAttrGroupId_Type = Integer32
_GenEquipStm1AbcAttrGroupId_Object = MibTableColumn
genEquipStm1AbcAttrGroupId = _GenEquipStm1AbcAttrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 2),
    _GenEquipStm1AbcAttrGroupId_Type()
)
genEquipStm1AbcAttrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrGroupId.setStatus("mandatory")
_GenEquipStm1AbcAttrNumberOfMembers_Type = Integer32
_GenEquipStm1AbcAttrNumberOfMembers_Object = MibTableColumn
genEquipStm1AbcAttrNumberOfMembers = _GenEquipStm1AbcAttrNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 3),
    _GenEquipStm1AbcAttrNumberOfMembers_Type()
)
genEquipStm1AbcAttrNumberOfMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrNumberOfMembers.setStatus("mandatory")
_GenEquipStm1AbcAttrPri1IfIndex_Type = Integer32
_GenEquipStm1AbcAttrPri1IfIndex_Object = MibTableColumn
genEquipStm1AbcAttrPri1IfIndex = _GenEquipStm1AbcAttrPri1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 4),
    _GenEquipStm1AbcAttrPri1IfIndex_Type()
)
genEquipStm1AbcAttrPri1IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrPri1IfIndex.setStatus("mandatory")
_GenEquipStm1AbcAttrPri2IfIndex_Type = Integer32
_GenEquipStm1AbcAttrPri2IfIndex_Object = MibTableColumn
genEquipStm1AbcAttrPri2IfIndex = _GenEquipStm1AbcAttrPri2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 5),
    _GenEquipStm1AbcAttrPri2IfIndex_Type()
)
genEquipStm1AbcAttrPri2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrPri2IfIndex.setStatus("mandatory")
_GenEquipStm1AbcAttrPri3IfIndex_Type = Integer32
_GenEquipStm1AbcAttrPri3IfIndex_Object = MibTableColumn
genEquipStm1AbcAttrPri3IfIndex = _GenEquipStm1AbcAttrPri3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 6),
    _GenEquipStm1AbcAttrPri3IfIndex_Type()
)
genEquipStm1AbcAttrPri3IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrPri3IfIndex.setStatus("mandatory")
_GenEquipStm1AbcAttrPri4IfIndex_Type = Integer32
_GenEquipStm1AbcAttrPri4IfIndex_Object = MibTableColumn
genEquipStm1AbcAttrPri4IfIndex = _GenEquipStm1AbcAttrPri4IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 7, 8, 5, 5, 1, 7),
    _GenEquipStm1AbcAttrPri4IfIndex_Type()
)
genEquipStm1AbcAttrPri4IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipStm1AbcAttrPri4IfIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWRM-RADIO-MIB",
    **{"MuteOnOff": MuteOnOff,
       "RfuGrade": RfuGrade,
       "MrmcBitRate": MrmcBitRate,
       "MrmcScriptId": MrmcScriptId,
       "QamOrder": QamOrder,
       "MrmcProfile": MrmcProfile,
       "ThresholdExponent": ThresholdExponent,
       "RFUSoftwareInstallStat": RFUSoftwareInstallStat,
       "RadioProtectionCmd": RadioProtectionCmd,
       "RfuMajorType": RfuMajorType,
       "Copy2mate": Copy2mate,
       "XpicState": XpicState,
       "HcModeType": HcModeType,
       "EnhancedHCExclRuleType": EnhancedHCExclRuleType,
       "HcType": HcType,
       "CommunicationChannel": CommunicationChannel,
       "FalseTrue": FalseTrue,
       "WaysideBandwidth": WaysideBandwidth,
       "microwave-radio": microwave_radio,
       "genEquip": genEquip,
       "genEquipUnit": genEquipUnit,
       "genEquipRFU": genEquipRFU,
       "genEquipRfuStatusTable": genEquipRfuStatusTable,
       "genEquipRfuStatusEntry": genEquipRfuStatusEntry,
       "genEquipRfuStatusId": genEquipRfuStatusId,
       "genEquipRfuStatusRxLevel": genEquipRfuStatusRxLevel,
       "genEquipRfuStatusTxLevel": genEquipRfuStatusTxLevel,
       "genEquipRfuStatusTemperature": genEquipRfuStatusTemperature,
       "genEquipRfuStatusRunningVersion": genEquipRfuStatusRunningVersion,
       "genEquipRfuStatusRFUType": genEquipRfuStatusRFUType,
       "genEquipRfuStatusRFUGrade": genEquipRfuStatusRFUGrade,
       "genEquipRfuStatusTxRxFreqSeparation": genEquipRfuStatusTxRxFreqSeparation,
       "genEquipRfuStatusRFUMode": genEquipRfuStatusRFUMode,
       "genEquipRfuStatusRxLevelDiversity": genEquipRfuStatusRxLevelDiversity,
       "genEquipRfuStatusRxLevelCombined": genEquipRfuStatusRxLevelCombined,
       "genEquipRfuStatusAutoDelayCalStatus": genEquipRfuStatusAutoDelayCalStatus,
       "genEquipRfuStatusRFUSerialNumber": genEquipRfuStatusRFUSerialNumber,
       "genEquipRfuStatusRFUPartNumber": genEquipRfuStatusRFUPartNumber,
       "genEquipRfuStatusRFUmateCarrier": genEquipRfuStatusRFUmateCarrier,
       "genEquipRfuStatusRFUMaxTxFreq": genEquipRfuStatusRFUMaxTxFreq,
       "genEquipRfuStatusRFUMinTxFreq": genEquipRfuStatusRFUMinTxFreq,
       "genEquipRfuStatusRFUMaxRxFreq": genEquipRfuStatusRFUMaxRxFreq,
       "genEquipRfuStatusRFUMinRxFreq": genEquipRfuStatusRFUMinRxFreq,
       "genEquipRfuStatusInstallation": genEquipRfuStatusInstallation,
       "genEquipRfuStatusDataSciErrors": genEquipRfuStatusDataSciErrors,
       "genEquipRfuStatusDeviceError": genEquipRfuStatusDeviceError,
       "genEquipRfuStatusBand": genEquipRfuStatusBand,
       "genEquipRfuStatusPATemp": genEquipRfuStatusPATemp,
       "genEquipRfuStatusTxMute": genEquipRfuStatusTxMute,
       "genEquipRfuStatusMinTxLevel": genEquipRfuStatusMinTxLevel,
       "genEquipRfuStatusMaxTxLevel": genEquipRfuStatusMaxTxLevel,
       "genEquipRfuStatusMinBW": genEquipRfuStatusMinBW,
       "genEquipRfuStatusMaxBW": genEquipRfuStatusMaxBW,
       "genEquipRfuStatusCommunication": genEquipRfuStatusCommunication,
       "genEquipRfuCfgATPCOverrideTimerState": genEquipRfuCfgATPCOverrideTimerState,
       "genEquipRfuStatusIfCombSupport": genEquipRfuStatusIfCombSupport,
       "genEquipRfuStatusMinRxLevel": genEquipRfuStatusMinRxLevel,
       "genEquipRfuStatusMaxRxLevel": genEquipRfuStatusMaxRxLevel,
       "genEquipRfuCfgTable": genEquipRfuCfgTable,
       "genEquipRfuCfgEntry": genEquipRfuCfgEntry,
       "genEquipRfuCfgId": genEquipRfuCfgId,
       "genEquipRfuCfgMaxTxLevel": genEquipRfuCfgMaxTxLevel,
       "genEquipRfuCfgTxFreq": genEquipRfuCfgTxFreq,
       "genEquipRfuCfgRxFreq": genEquipRfuCfgRxFreq,
       "genEquipRfuCfgATPCAdmin": genEquipRfuCfgATPCAdmin,
       "genEquipRfuCfgATPCRefRSL": genEquipRfuCfgATPCRefRSL,
       "genEquipRfuCfgMuteTx": genEquipRfuCfgMuteTx,
       "genEquipRfuCfgRSLConnSrc": genEquipRfuCfgRSLConnSrc,
       "genEquipRfuCfgDelayCal": genEquipRfuCfgDelayCal,
       "genEquipRfuCfgLoopback": genEquipRfuCfgLoopback,
       "genEquipRfuCfgLogAdmin": genEquipRfuCfgLogAdmin,
       "genEquipRfuCfgClearComDeviceError": genEquipRfuCfgClearComDeviceError,
       "genEquipRfuCfgGreenModeAdmin": genEquipRfuCfgGreenModeAdmin,
       "genEquipRfuCfgGreenModeReferenceLevel": genEquipRfuCfgGreenModeReferenceLevel,
       "genEquipRfuCfgATPCOverrideTxLevel": genEquipRfuCfgATPCOverrideTxLevel,
       "genEquipRfuCfgATPCOverrideTimeout": genEquipRfuCfgATPCOverrideTimeout,
       "genEquipRfuCfgATPCOverrideTimerCounter": genEquipRfuCfgATPCOverrideTimerCounter,
       "genEquipRfuCfgATPCOverrideTimerCancel": genEquipRfuCfgATPCOverrideTimerCancel,
       "genEquipRfuUploadTable": genEquipRfuUploadTable,
       "genEquipRfuUploadEntry": genEquipRfuUploadEntry,
       "genEquipRfuUploadId": genEquipRfuUploadId,
       "genEquipRfuUploadSwCommand": genEquipRfuUploadSwCommand,
       "genEquipRfuUploadSwStatus": genEquipRfuUploadSwStatus,
       "genEquipRfuUploadCounter": genEquipRfuUploadCounter,
       "genEquipRFUNG": genEquipRFUNG,
       "genEquipRfuSwInstallTable": genEquipRfuSwInstallTable,
       "genEquipRfuSwInstallEntry": genEquipRfuSwInstallEntry,
       "genEquipRfuSwInstallIfIndex": genEquipRfuSwInstallIfIndex,
       "genEquipRfuSwInstallOperation": genEquipRfuSwInstallOperation,
       "genEquipRfuSwInstallTimedInstallation": genEquipRfuSwInstallTimedInstallation,
       "genEquipRfuSwInstallTimer": genEquipRfuSwInstallTimer,
       "genEquipRfuInstalledVersionsTable": genEquipRfuInstalledVersionsTable,
       "genEquipRfuInstalledVersionsEntry": genEquipRfuInstalledVersionsEntry,
       "genEquipRfuInstalledVersionsIfIndex": genEquipRfuInstalledVersionsIfIndex,
       "genEquipRfuInstalledVersionsDSP": genEquipRfuInstalledVersionsDSP,
       "genEquipRfuInstalledVersionsConfigurations": genEquipRfuInstalledVersionsConfigurations,
       "genEquipRfuInstalledVersionsConstants": genEquipRfuInstalledVersionsConstants,
       "genEquipRfuInstalledVersionsScripts": genEquipRfuInstalledVersionsScripts,
       "genEquipRfuInstalledVersionsFirmware": genEquipRfuInstalledVersionsFirmware,
       "genEquipRfuSwStatusTable": genEquipRfuSwStatusTable,
       "genEquipRfuSwStatusEntry": genEquipRfuSwStatusEntry,
       "genEquipRfuSwStatusIfIndex": genEquipRfuSwStatusIfIndex,
       "genEquipRfuSwStatusCurrentState": genEquipRfuSwStatusCurrentState,
       "genEquipRfuSwStatusProgress": genEquipRfuSwStatusProgress,
       "genEquipRfuRunningVersionsTable": genEquipRfuRunningVersionsTable,
       "genEquipRfuRunningVersionsEntry": genEquipRfuRunningVersionsEntry,
       "genEquipRfuRunningVersionsIfIndex": genEquipRfuRunningVersionsIfIndex,
       "genEquipRfuRunningVersionsDSP": genEquipRfuRunningVersionsDSP,
       "genEquipRfuRunningVersionsConfigurations": genEquipRfuRunningVersionsConfigurations,
       "genEquipRfuRunningVersionsConstants": genEquipRfuRunningVersionsConstants,
       "genEquipRfuRunningVersionsScripts": genEquipRfuRunningVersionsScripts,
       "genEquipRfuRunningVersionsFirmware": genEquipRfuRunningVersionsFirmware,
       "genEquipRfuAvailableVersionsTable": genEquipRfuAvailableVersionsTable,
       "genEquipRfuAvailableVersionsEntry": genEquipRfuAvailableVersionsEntry,
       "genEquipRfuAvailableVersionsRfuType": genEquipRfuAvailableVersionsRfuType,
       "genEquipRfuAvailableVersionsDSP": genEquipRfuAvailableVersionsDSP,
       "genEquipRfuAvailableVersionsConfigurations": genEquipRfuAvailableVersionsConfigurations,
       "genEquipRfuAvailableVersionsConstants": genEquipRfuAvailableVersionsConstants,
       "genEquipRfuAvailableVersionsScripts": genEquipRfuAvailableVersionsScripts,
       "genEquipRfuAvailableVersionsFirmware": genEquipRfuAvailableVersionsFirmware,
       "genEquipRadio": genEquipRadio,
       "genEquipRadioStatusTable": genEquipRadioStatusTable,
       "genEquipRadioStatusEntry": genEquipRadioStatusEntry,
       "genEquipRadioStatusRadioId": genEquipRadioStatusRadioId,
       "genEquipRadioStatusMSE": genEquipRadioStatusMSE,
       "genEquipRadioStatusDefectedBlocks": genEquipRadioStatusDefectedBlocks,
       "genEquipRadioStatusBER": genEquipRadioStatusBER,
       "genEquipRadioStatusXPI": genEquipRadioStatusXPI,
       "genEquipRadioStatusXPICEnabled": genEquipRadioStatusXPICEnabled,
       "genEquipRadioCfgTable": genEquipRadioCfgTable,
       "genEquipRadioCfgEntry": genEquipRadioCfgEntry,
       "genEquipRadioCfgRadioId": genEquipRadioCfgRadioId,
       "genEquipRadioCfgLinkId": genEquipRadioCfgLinkId,
       "genEquipRadioCfgMACHeaderCompression": genEquipRadioCfgMACHeaderCompression,
       "genEquipRadioCfgClearCounters": genEquipRadioCfgClearCounters,
       "genEquipRadioCfgIfLoopback": genEquipRadioCfgIfLoopback,
       "genEquipRadioCfgExcessiveBERThreshold": genEquipRadioCfgExcessiveBERThreshold,
       "genEquipRadioCfgSignalDegradeThreshold": genEquipRadioCfgSignalDegradeThreshold,
       "genEquipRadioCfgRadioAdmin": genEquipRadioCfgRadioAdmin,
       "genEquipRadioCfgRadioOperationalStatus": genEquipRadioCfgRadioOperationalStatus,
       "genEquipRadioCfgRadioTrafficPriorityScheme": genEquipRadioCfgRadioTrafficPriorityScheme,
       "genEquipRadioCfgRadioHiPriorityEthernetBW": genEquipRadioCfgRadioHiPriorityEthernetBW,
       "genEquipRadioCfgRadioMultiRadioEnable": genEquipRadioCfgRadioMultiRadioEnable,
       "genEquipRadioCfgRadioMultiRadioBlockLocalTraffic": genEquipRadioCfgRadioMultiRadioBlockLocalTraffic,
       "genEquipRadioCfgRadioMultiRadioBlockMateTraffic": genEquipRadioCfgRadioMultiRadioBlockMateTraffic,
       "genEquipRadioCfgRadioCurrentAvailableCapacity": genEquipRadioCfgRadioCurrentAvailableCapacity,
       "genEquipRadioCfgRadioMultiRadioExcessiveBERAdmin": genEquipRadioCfgRadioMultiRadioExcessiveBERAdmin,
       "genEquipRadioCfgRadioMultiRadioSignalDegradeAdmin": genEquipRadioCfgRadioMultiRadioSignalDegradeAdmin,
       "genEquipRadioCfgEnAlarmGenOnRslDegrade": genEquipRadioCfgEnAlarmGenOnRslDegrade,
       "genEquipRadioCfgAlarmGenRslNominalLevel": genEquipRadioCfgAlarmGenRslNominalLevel,
       "genEquipRadioCfgAlarmGenRslDegradationMargin": genEquipRadioCfgAlarmGenRslDegradationMargin,
       "genEquipRadioCfgLinkShutDownOnRadioFailure": genEquipRadioCfgLinkShutDownOnRadioFailure,
       "genEquipRadioCfgLoopbackTimeout": genEquipRadioCfgLoopbackTimeout,
       "genEquipRadioCfgAbcMode": genEquipRadioCfgAbcMode,
       "genEquipRemoteRadio": genEquipRemoteRadio,
       "genEquipRemoteRadioTable": genEquipRemoteRadioTable,
       "genEquipRemoteRadioEntry": genEquipRemoteRadioEntry,
       "genEquipRemoteRadioRadioId": genEquipRemoteRadioRadioId,
       "genEquipRemoteRadioRemoteCommunication": genEquipRemoteRadioRemoteCommunication,
       "genEquipRemoteRadioRemoteIPAddr": genEquipRemoteRadioRemoteIPAddr,
       "genEquipRemoteRadioRemoteRxLevel": genEquipRemoteRadioRemoteRxLevel,
       "genEquipRemoteRadioRemoteForceMaxTxLevel": genEquipRemoteRadioRemoteForceMaxTxLevel,
       "genEquipRemoteRadioRemoteTxFreq": genEquipRemoteRadioRemoteTxFreq,
       "genEquipRemoteRadioRemoteRxFreq": genEquipRemoteRadioRemoteRxFreq,
       "genEquipRemoteRadioRemoteATPCReferenceRxLevel": genEquipRemoteRadioRemoteATPCReferenceRxLevel,
       "genEquipRemoteRadioRemoteFloatingIPAddr": genEquipRemoteRadioRemoteFloatingIPAddr,
       "genEquipRemoteRadioRemoteDefaultGateway": genEquipRemoteRadioRemoteDefaultGateway,
       "genEquipRemoteRadioRemoteMostSevereAlarm": genEquipRemoteRadioRemoteMostSevereAlarm,
       "genEquipRemoteRadioRemoteSubnetMask": genEquipRemoteRadioRemoteSubnetMask,
       "genEquipRemoteRadioRemoteSlotID": genEquipRemoteRadioRemoteSlotID,
       "genEquipRemoteRadioRemoteForceTxMute": genEquipRemoteRadioRemoteForceTxMute,
       "genEquipRemoteRadioRemoteLinkId": genEquipRemoteRadioRemoteLinkId,
       "genEquipRemoteRadioRemoteATPCoverrideState": genEquipRemoteRadioRemoteATPCoverrideState,
       "genEquipRemoteRadioRemoteATPCoverrideStateCancel": genEquipRemoteRadioRemoteATPCoverrideStateCancel,
       "genEquipRemoteRadioRemoteDataLoopBackAdmin": genEquipRemoteRadioRemoteDataLoopBackAdmin,
       "genEquipRemoteRadioRemoteDataLoopBackDuration": genEquipRemoteRadioRemoteDataLoopBackDuration,
       "genEquipRemoteRadioRemoteDataLoopBackSwitchAddress": genEquipRemoteRadioRemoteDataLoopBackSwitchAddress,
       "genEquipRemoteRadioRemoteGreenReferenceRxLevel": genEquipRemoteRadioRemoteGreenReferenceRxLevel,
       "genEquipRemoteRadioRemoteMNGvlan": genEquipRemoteRadioRemoteMNGvlan,
       "genEquipRemoteRadioRemoteReset": genEquipRemoteRadioRemoteReset,
       "genEquipRemoteRadioRemoteGreenModeAdmin": genEquipRemoteRadioRemoteGreenModeAdmin,
       "genEquipRemoteRadioRemoteWebProtocol": genEquipRemoteRadioRemoteWebProtocol,
       "genEquipRemoteRadioRemoteIPv6Addr": genEquipRemoteRadioRemoteIPv6Addr,
       "genEquipRemoteRadioRemotePrefixLength": genEquipRemoteRadioRemotePrefixLength,
       "genEquipRemoteRadioRemoteDefaultGatewayIpv6": genEquipRemoteRadioRemoteDefaultGatewayIpv6,
       "genEquipRemoteRadioRemoteResetSlot": genEquipRemoteRadioRemoteResetSlot,
       "genEquipRadioMRMC": genEquipRadioMRMC,
       "genEquipRadioMRMCTable": genEquipRadioMRMCTable,
       "genEquipRadioMRMCEntry": genEquipRadioMRMCEntry,
       "genEquipRadioMRMCRadioId": genEquipRadioMRMCRadioId,
       "genEquipRadioMRMCSelectedScriptIndex": genEquipRadioMRMCSelectedScriptIndex,
       "genEquipRadioMRMCOccupidBandwidth": genEquipRadioMRMCOccupidBandwidth,
       "genEquipRadioMRMCOperMode": genEquipRadioMRMCOperMode,
       "genEquipRadioMRMCCurrTxProfile": genEquipRadioMRMCCurrTxProfile,
       "genEquipRadioMRMCCurrTxQAM": genEquipRadioMRMCCurrTxQAM,
       "genEquipRadioMRMCCurrTxBitrate": genEquipRadioMRMCCurrTxBitrate,
       "genEquipRadioMRMCCurrTxVc": genEquipRadioMRMCCurrTxVc,
       "genEquipRadioMRMCCurrRxProfile": genEquipRadioMRMCCurrRxProfile,
       "genEquipRadioMRMCCurrRxQAM": genEquipRadioMRMCCurrRxQAM,
       "genEquipRadioMRMCCurrRxBitrate": genEquipRadioMRMCCurrRxBitrate,
       "genEquipRadioMRMCCurrRxVc": genEquipRadioMRMCCurrRxVc,
       "genEquipRadioMRMCCurrGrade": genEquipRadioMRMCCurrGrade,
       "genEquipRadioMRMCEnAlarmOnAcmProfileDegrade": genEquipRadioMRMCEnAlarmOnAcmProfileDegrade,
       "genEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold": genEquipRadioMRMCAlarmOnAcmProfileDegradeThreshold,
       "genEquipRadioMRMCScriptTable": genEquipRadioMRMCScriptTable,
       "genEquipRadioMRMCScriptEntry": genEquipRadioMRMCScriptEntry,
       "genEquipRadioMRMCScriptRadioId": genEquipRadioMRMCScriptRadioId,
       "genEquipRadioMRMCScriptIndex": genEquipRadioMRMCScriptIndex,
       "genEquipRadioMRMCScriptName": genEquipRadioMRMCScriptName,
       "genEquipRadioMRMCScriptOperMode": genEquipRadioMRMCScriptOperMode,
       "genEquipRadioMRMCScriptProfile": genEquipRadioMRMCScriptProfile,
       "genEquipRadioMRMCScriptProfileBitrate": genEquipRadioMRMCScriptProfileBitrate,
       "genEquipRadioMRMCScriptAdaptivePower": genEquipRadioMRMCScriptAdaptivePower,
       "genEquipRadioMRMCScriptReference": genEquipRadioMRMCScriptReference,
       "genEquipRadioMRMCScriptMinProfile": genEquipRadioMRMCScriptMinProfile,
       "genEquipRadioMRMCFilteredTable": genEquipRadioMRMCFilteredTable,
       "genEquipRadioMRMCFilteredEntry": genEquipRadioMRMCFilteredEntry,
       "genEquipRadioMRMCFilteredRadioId": genEquipRadioMRMCFilteredRadioId,
       "genEquipRadioMRMCFilteredScriptId": genEquipRadioMRMCFilteredScriptId,
       "genEquipRadioMRMCProfileAttrTable": genEquipRadioMRMCProfileAttrTable,
       "genEquipRadioMRMCProfileAttrEntry": genEquipRadioMRMCProfileAttrEntry,
       "genEquipRadioMRMCProfileAttrScriptId": genEquipRadioMRMCProfileAttrScriptId,
       "genEquipRadioMRMCProfileAttrTxProfile": genEquipRadioMRMCProfileAttrTxProfile,
       "genEquipRadioMRMCProfileAttrRxProfile": genEquipRadioMRMCProfileAttrRxProfile,
       "genEquipRadioMRMCProfileAttrTxQAM": genEquipRadioMRMCProfileAttrTxQAM,
       "genEquipRadioMRMCProfileAttrTxBitRate": genEquipRadioMRMCProfileAttrTxBitRate,
       "genEquipRadioMRMCProfileAttrRxQAM": genEquipRadioMRMCProfileAttrRxQAM,
       "genEquipRadioMRMCProfileAttrRxBitRate": genEquipRadioMRMCProfileAttrRxBitRate,
       "genEquipRadioMRMCScriptAttrTable": genEquipRadioMRMCScriptAttrTable,
       "genEquipRadioMRMCScriptAttrEntry": genEquipRadioMRMCScriptAttrEntry,
       "genEquipRadioMRMCScriptAttrScriptId": genEquipRadioMRMCScriptAttrScriptId,
       "genEquipRadioMRMCScriptAttrScriptName": genEquipRadioMRMCScriptAttrScriptName,
       "genEquipRadioMRMCScriptAttrSupportACM": genEquipRadioMRMCScriptAttrSupportACM,
       "genEquipRadioMRMCScriptAttrStandard": genEquipRadioMRMCScriptAttrStandard,
       "genEquipRadioMRMCScriptAttrMultiCarrier": genEquipRadioMRMCScriptAttrMultiCarrier,
       "genEquipRadioMRMCScriptAttrAdjChannel": genEquipRadioMRMCScriptAttrAdjChannel,
       "genEquipRadioMRMCScriptAttrModScheme": genEquipRadioMRMCScriptAttrModScheme,
       "genEquipRadioMRMCScriptAttrSymmetry": genEquipRadioMRMCScriptAttrSymmetry,
       "genEquipRadioMRMCScriptAttrLatency": genEquipRadioMRMCScriptAttrLatency,
       "genEquipRadioMRMCScriptAttrTxBW": genEquipRadioMRMCScriptAttrTxBW,
       "genEquipRadioMRMCScriptAttrRxBW": genEquipRadioMRMCScriptAttrRxBW,
       "genEquipRadioMRMCScriptAttrTxOccupiedBW": genEquipRadioMRMCScriptAttrTxOccupiedBW,
       "genEquipRadioMRMCScriptAttrRxOccupiedBW": genEquipRadioMRMCScriptAttrRxOccupiedBW,
       "genEquipRadioMRMCScriptAttrLinkGrade": genEquipRadioMRMCScriptAttrLinkGrade,
       "genEquipRadioMRMCScriptAttrDiffGrade": genEquipRadioMRMCScriptAttrDiffGrade,
       "genEquipRadioMRMCScriptAttrChannelBW": genEquipRadioMRMCScriptAttrChannelBW,
       "genEquipRadioMRMCScriptAttrTxMaxProfile": genEquipRadioMRMCScriptAttrTxMaxProfile,
       "genEquipRadioMRMCScriptAttrRxMaxProfile": genEquipRadioMRMCScriptAttrRxMaxProfile,
       "genEquipRadioMRMCConfigTable": genEquipRadioMRMCConfigTable,
       "genEquipRadioMRMCConfigEntry": genEquipRadioMRMCConfigEntry,
       "genEquipRadioMRMCConfigRadioId": genEquipRadioMRMCConfigRadioId,
       "genEquipRadioMRMCConfigActiveScriptId": genEquipRadioMRMCConfigActiveScriptId,
       "genEquipRadioMRMCConfigStandbyScriptId": genEquipRadioMRMCConfigStandbyScriptId,
       "genEquipRadioMRMCConfigOperMode": genEquipRadioMRMCConfigOperMode,
       "genEquipRadioMRMCConfigMaxProfile": genEquipRadioMRMCConfigMaxProfile,
       "genEquipRadioMRMCConfigMinProfile": genEquipRadioMRMCConfigMinProfile,
       "genEquipRadioMRMCConfigAdaptivePowerAdmin": genEquipRadioMRMCConfigAdaptivePowerAdmin,
       "genEquipRadioMRMCConfigAdaptivePowerRefClass": genEquipRadioMRMCConfigAdaptivePowerRefClass,
       "genEquipRadioComp": genEquipRadioComp,
       "genEquipRadioCompCfgTable": genEquipRadioCompCfgTable,
       "genEquipRadioCompCfgEntry": genEquipRadioCompCfgEntry,
       "genEquipRadioCompMode": genEquipRadioCompMode,
       "genEquipRadioEnhHeaderCompAdmin": genEquipRadioEnhHeaderCompAdmin,
       "genEquipRadioEnhDataCompAdmin": genEquipRadioEnhDataCompAdmin,
       "genEquipRadioEnhHeaderCompMode": genEquipRadioEnhHeaderCompMode,
       "genEquipRadioCompStatusTable": genEquipRadioCompStatusTable,
       "genEquipRadioCompStatusEntry": genEquipRadioCompStatusEntry,
       "genEquipRadioCompOperationalState": genEquipRadioCompOperationalState,
       "genEquipRadioCompExclRulesTable": genEquipRadioCompExclRulesTable,
       "genEquipRadioCompExclRulesEntry": genEquipRadioCompExclRulesEntry,
       "genEquipRadioCompExclRuleId": genEquipRadioCompExclRuleId,
       "genEquipRadioCompExclRuleType": genEquipRadioCompExclRuleType,
       "genEquipRadioCompExclRuleName": genEquipRadioCompExclRuleName,
       "genEquipRadioCompExclRuleValue": genEquipRadioCompExclRuleValue,
       "genEquipRadioCompExclRuleRowStatus": genEquipRadioCompExclRuleRowStatus,
       "genEquipRadioCompNG": genEquipRadioCompNG,
       "genEquipRadioCompNGCfgTable": genEquipRadioCompNGCfgTable,
       "genEquipRadioCompNGCfgEntry": genEquipRadioCompNGCfgEntry,
       "genEquipRadioCompNGCfgifIndex": genEquipRadioCompNGCfgifIndex,
       "genEquipRadioHeaderCompNGCfgClearStats": genEquipRadioHeaderCompNGCfgClearStats,
       "genEquipRadioHeaderCompNGCfgUserFlowType": genEquipRadioHeaderCompNGCfgUserFlowType,
       "genEquipRadioHeaderCompNGCfgMode": genEquipRadioHeaderCompNGCfgMode,
       "genEquipRadioCutThroughNGCfgMode": genEquipRadioCutThroughNGCfgMode,
       "genEquipRadioCompNGExclRulesTable": genEquipRadioCompNGExclRulesTable,
       "genEquipRadioCompNGExclRulesEntry": genEquipRadioCompNGExclRulesEntry,
       "genEquipRadioCompNGExclRulesifIndex": genEquipRadioCompNGExclRulesifIndex,
       "genEquipRadioCompNGExclRuleId": genEquipRadioCompNGExclRuleId,
       "genEquipRadioCompNGExclRuleName": genEquipRadioCompNGExclRuleName,
       "genEquipRadioCompNGExclRuleType": genEquipRadioCompNGExclRuleType,
       "genEquipRadioCompNGExclRuleValue": genEquipRadioCompNGExclRuleValue,
       "genEquipRadioCutThroughNGCountersTable": genEquipRadioCutThroughNGCountersTable,
       "genEquipRadioCutThroughNGCountersEntry": genEquipRadioCutThroughNGCountersEntry,
       "genEquipRadioCutThroughNGCountersifIndex": genEquipRadioCutThroughNGCountersifIndex,
       "genEquipRadioCutThroughNGCountersRxFrames": genEquipRadioCutThroughNGCountersRxFrames,
       "genEquipRadioCutThroughNGCountersRxBytes": genEquipRadioCutThroughNGCountersRxBytes,
       "genEquipRadioCutThroughNGCountersTxFrames": genEquipRadioCutThroughNGCountersTxFrames,
       "genEquipRadioCutThroughNGCountersTxBytes": genEquipRadioCutThroughNGCountersTxBytes,
       "genEquipRadioCutThroughNGCountersTotalRxFrames": genEquipRadioCutThroughNGCountersTotalRxFrames,
       "genEquipRadioCutThroughNGCountersTotalRxBytes": genEquipRadioCutThroughNGCountersTotalRxBytes,
       "genEquipRadioCutThroughNGCountersTotalTxBytesOut": genEquipRadioCutThroughNGCountersTotalTxBytesOut,
       "genEquipRadioCutThroughNGCountersTotalTxFrames": genEquipRadioCutThroughNGCountersTotalTxFrames,
       "genEquipRadioCutThroughNGCountersTotalTxIdleBytes": genEquipRadioCutThroughNGCountersTotalTxIdleBytes,
       "genEquipRadioCutThroughNGCountersTotalTxBytesIn": genEquipRadioCutThroughNGCountersTotalTxBytesIn,
       "genEquipRadioCompNGStatusTable": genEquipRadioCompNGStatusTable,
       "genEquipRadioCompNGStatusEntry": genEquipRadioCompNGStatusEntry,
       "genEquipRadioCompNGStatusifindex": genEquipRadioCompNGStatusifindex,
       "genEquipRadioCompNGStatusOperationalState": genEquipRadioCompNGStatusOperationalState,
       "genEquipRadioCompNGStatusType": genEquipRadioCompNGStatusType,
       "genEquipRadioCompNGCountersTable": genEquipRadioCompNGCountersTable,
       "genEquipRadioCompNGCountersEntry": genEquipRadioCompNGCountersEntry,
       "genEquipRadioCompNGCountersifIndex": genEquipRadioCompNGCountersifIndex,
       "genEquipRadioCompNGCountersHCInBytes": genEquipRadioCompNGCountersHCInBytes,
       "genEquipRadioCompNGCountersHCOutBytes": genEquipRadioCompNGCountersHCOutBytes,
       "genEquipRadioCompNGCountersHCCompFrm": genEquipRadioCompNGCountersHCCompFrm,
       "genEquipRadioCompNGCountersHCFrmUncmpExclRule": genEquipRadioCompNGCountersHCFrmUncmpExclRule,
       "genEquipRadioCompNGCountersHCFrmUcompInternal": genEquipRadioCompNGCountersHCFrmUcompInternal,
       "genEquipRadioCompNGCountersHCLearningFrm": genEquipRadioCompNGCountersHCLearningFrm,
       "genEquipRadioCompNGCountersHCUserFlowTypeActiveFlows": genEquipRadioCompNGCountersHCUserFlowTypeActiveFlows,
       "genEquipRadioCompNGCountersHCTotalActiveFlows": genEquipRadioCompNGCountersHCTotalActiveFlows,
       "genEquipRadioPtpTransport": genEquipRadioPtpTransport,
       "genEquipRadioPtpTransportCfgTable": genEquipRadioPtpTransportCfgTable,
       "genEquipRadioPtpTransportCfgEntry": genEquipRadioPtpTransportCfgEntry,
       "genEquipRadioPtpTransportChannelAdmin": genEquipRadioPtpTransportChannelAdmin,
       "genEquipRadioPtpTransportChannelMode": genEquipRadioPtpTransportChannelMode,
       "genEquipRadioPtpTransportCountersTable": genEquipRadioPtpTransportCountersTable,
       "genEquipRadioPtpTransportCountersEntry": genEquipRadioPtpTransportCountersEntry,
       "genEquipRadioPtpTransportTxFrames": genEquipRadioPtpTransportTxFrames,
       "genEquipRadioPtpTransportTxDroppedFrames": genEquipRadioPtpTransportTxDroppedFrames,
       "genEquipRadioPtpTransportTxBytes": genEquipRadioPtpTransportTxBytes,
       "genEquipRadioPtpTransportTxDroppedBytes": genEquipRadioPtpTransportTxDroppedBytes,
       "genEquipRadioPtpTransportRxFrames": genEquipRadioPtpTransportRxFrames,
       "genEquipRadioPtpTransportRxBytes": genEquipRadioPtpTransportRxBytes,
       "genEquipRadioCutThrough": genEquipRadioCutThrough,
       "genEquipRadioCutThroughCfgTable": genEquipRadioCutThroughCfgTable,
       "genEquipRadioCutThroughCfgEntry": genEquipRadioCutThroughCfgEntry,
       "genEquipRadioCutThroughChannelAdmin": genEquipRadioCutThroughChannelAdmin,
       "genEquipRadioCutThroughCountersTable": genEquipRadioCutThroughCountersTable,
       "genEquipRadioCutThroughCountersEntry": genEquipRadioCutThroughCountersEntry,
       "genEquipRadioCutThroughTxFrames": genEquipRadioCutThroughTxFrames,
       "genEquipRadioCutThroughTxBytes": genEquipRadioCutThroughTxBytes,
       "genEquipRadioCutThroughRxFrames": genEquipRadioCutThroughRxFrames,
       "genEquipRadioCutThroughRxBytes": genEquipRadioCutThroughRxBytes,
       "genEquipRadioGroups": genEquipRadioGroups,
       "genEquipRadioGroupsProtection": genEquipRadioGroupsProtection,
       "genEquipRadioGroupsProtectionAttrTable": genEquipRadioGroupsProtectionAttrTable,
       "genEquipRadioGroupsProtectionAttrEntry": genEquipRadioGroupsProtectionAttrEntry,
       "genEquipRadioGroupsProtectionAttrGroupIfIndex": genEquipRadioGroupsProtectionAttrGroupIfIndex,
       "genEquipRadioGroupsProtectionAttrGroupId": genEquipRadioGroupsProtectionAttrGroupId,
       "genEquipRadioGroupsProtectionAttrCommand": genEquipRadioGroupsProtectionAttrCommand,
       "genEquipRadioGroupsProtectionAttrCopyToMate": genEquipRadioGroupsProtectionAttrCopyToMate,
       "genEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex": genEquipRadioGroupsProtectionAttrCopyToMateSourceIfIndex,
       "genEquipRadioGroupsProtectionAttrRevertiveAdmin": genEquipRadioGroupsProtectionAttrRevertiveAdmin,
       "genEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex": genEquipRadioGroupsProtectionAttrRevertivePrimaryIfIndex,
       "genEquipRadioGroupsProtectionMembersTable": genEquipRadioGroupsProtectionMembersTable,
       "genEquipRadioGroupsProtectionMembersEntry": genEquipRadioGroupsProtectionMembersEntry,
       "genEquipRadioGroupsProtectionMembersIfIndexGroup": genEquipRadioGroupsProtectionMembersIfIndexGroup,
       "genEquipRadioGroupsProtectionMembersGroupId": genEquipRadioGroupsProtectionMembersGroupId,
       "genEquipRadioGroupsProtectionMembersMem1IfIndex": genEquipRadioGroupsProtectionMembersMem1IfIndex,
       "genEquipRadioGroupsProtectionMembersMem2IfIndex": genEquipRadioGroupsProtectionMembersMem2IfIndex,
       "genEquipRadioGroupsProtectionMembersRowStatus": genEquipRadioGroupsProtectionMembersRowStatus,
       "genEquipRadioGroupsProtectionStatusTable": genEquipRadioGroupsProtectionStatusTable,
       "genEquipRadioGroupsProtectionStatusEntry": genEquipRadioGroupsProtectionStatusEntry,
       "genEquipRadioGroupsProtectionStatusGroupIfIndex": genEquipRadioGroupsProtectionStatusGroupIfIndex,
       "genEquipRadioGroupsProtectionStatusActiveIfIndex": genEquipRadioGroupsProtectionStatusActiveIfIndex,
       "genEquipRadioGroupsProtectionStatusStandbyIfIndex": genEquipRadioGroupsProtectionStatusStandbyIfIndex,
       "genEquipRadioGroupsProtectionStatusLockout": genEquipRadioGroupsProtectionStatusLockout,
       "genEquipRadioGroupsProtectionBBSSD": genEquipRadioGroupsProtectionBBSSD,
       "genEquipRadioGroupsProtectionBBSSDAttrTable": genEquipRadioGroupsProtectionBBSSDAttrTable,
       "genEquipRadioGroupsProtectionBBSSDAttrEntry": genEquipRadioGroupsProtectionBBSSDAttrEntry,
       "genEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex": genEquipRadioGroupsProtectionBBSSDAttrGroupIfIndex,
       "genEquipRadioGroupsProtectionBBSSDAttrRevertive": genEquipRadioGroupsProtectionBBSSDAttrRevertive,
       "genEquipRadioGroupsProtectionBBSSDAttrClrSwCnt": genEquipRadioGroupsProtectionBBSSDAttrClrSwCnt,
       "genEquipRadioGroupsProtectionBBSSDAttrFWAuto": genEquipRadioGroupsProtectionBBSSDAttrFWAuto,
       "genEquipRadioGroupsProtectionBBSSDStatusTable": genEquipRadioGroupsProtectionBBSSDStatusTable,
       "genEquipRadioGroupsProtectionBBSSDStatusEntry": genEquipRadioGroupsProtectionBBSSDStatusEntry,
       "genEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex": genEquipRadioGroupsProtectionBBSSDStatusGroupIfIndex,
       "genEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex": genEquipRadioGroupsProtectionBBSSDStatusAbcGroupIfIndex,
       "genEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality": genEquipRadioGroupsProtectionBBSSDStatusActiveRxQuality,
       "genEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex": genEquipRadioGroupsProtectionBBSSDStatusActiveRxRadioIfIndex,
       "genEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex": genEquipRadioGroupsProtectionBBSSDStatusActiveTxRadioIfIndex,
       "genEquipRadioGroupsProtectionBBSSDStatusLockout": genEquipRadioGroupsProtectionBBSSDStatusLockout,
       "genEquipRadioGroupsProtectionBBSSDStatusRxChId": genEquipRadioGroupsProtectionBBSSDStatusRxChId,
       "genEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality": genEquipRadioGroupsProtectionBBSSDStatusStdbyRxQuality,
       "genEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex": genEquipRadioGroupsProtectionBBSSDStatusStdbyRxRadioIfIndex,
       "genEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex": genEquipRadioGroupsProtectionBBSSDStatusStandbyTxRadioIfIndex,
       "genEquipRadioGroupsXpic": genEquipRadioGroupsXpic,
       "genEquipRadioGroupsXPICAttrTable": genEquipRadioGroupsXPICAttrTable,
       "genEquipRadioGroupsXPICAttrEntry": genEquipRadioGroupsXPICAttrEntry,
       "genEquipRadioGroupsXPICAttrGroupIfIndex": genEquipRadioGroupsXPICAttrGroupIfIndex,
       "genEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex": genEquipRadioGroupsXPICAttrCopyToMateSourceIfIndex,
       "genEquipRadioGroupsXPICAttrGroupId": genEquipRadioGroupsXPICAttrGroupId,
       "genEquipRadioGroupsXPICAttrXRSMAdmin": genEquipRadioGroupsXPICAttrXRSMAdmin,
       "genEquipRadioGroupsXPICAttrAdmin": genEquipRadioGroupsXPICAttrAdmin,
       "genEquipRadioGroupsXPICAttrCopyToMate": genEquipRadioGroupsXPICAttrCopyToMate,
       "genEquipRadioGroupsXPICMembersTable": genEquipRadioGroupsXPICMembersTable,
       "genEquipRadioGroupsXPICMembersEntry": genEquipRadioGroupsXPICMembersEntry,
       "genEquipRadioGroupsXPICMembersIfIndexGroup": genEquipRadioGroupsXPICMembersIfIndexGroup,
       "genEquipRadioGroupsXPICMembersMem1IfIndex": genEquipRadioGroupsXPICMembersMem1IfIndex,
       "genEquipRadioGroupsXPICMembersMem2IfIndex": genEquipRadioGroupsXPICMembersMem2IfIndex,
       "genEquipRadioGroupsXPICMembersRowStatus": genEquipRadioGroupsXPICMembersRowStatus,
       "genEquipRadioGroupsXPICStatusTable": genEquipRadioGroupsXPICStatusTable,
       "genEquipRadioGroupsXPICStatusEntry": genEquipRadioGroupsXPICStatusEntry,
       "genEquipRadioGroupsXPICStatusGroupIfIndex": genEquipRadioGroupsXPICStatusGroupIfIndex,
       "genEquipRadioGroupsXPICStatusState": genEquipRadioGroupsXPICStatusState,
       "genEquipRadioGroupsMR": genEquipRadioGroupsMR,
       "genEquipRadioGroupsMRAttrTable": genEquipRadioGroupsMRAttrTable,
       "genEquipRadioGroupsMRAttrEntry": genEquipRadioGroupsMRAttrEntry,
       "genEquipRadioGroupsMRAttrGroupIfIndex": genEquipRadioGroupsMRAttrGroupIfIndex,
       "genEquipRadioGroupsMRAttrGroupId": genEquipRadioGroupsMRAttrGroupId,
       "genEquipRadioGroupsMRAttrAdmin": genEquipRadioGroupsMRAttrAdmin,
       "genEquipRadioGroupsMRAttrBlockRadioIfindex": genEquipRadioGroupsMRAttrBlockRadioIfindex,
       "genEquipRadioGroupsMRAttrBlockRadioAdmin": genEquipRadioGroupsMRAttrBlockRadioAdmin,
       "genEquipRadioGroupsMRAttrCopy2MateIfindex": genEquipRadioGroupsMRAttrCopy2MateIfindex,
       "genEquipRadioGroupsMRAttrCopy2MateAdmin": genEquipRadioGroupsMRAttrCopy2MateAdmin,
       "genEquipRadioGroupsMRAttrExBerAdmin": genEquipRadioGroupsMRAttrExBerAdmin,
       "genEquipRadioGroupsMRAttrMinNumRadio": genEquipRadioGroupsMRAttrMinNumRadio,
       "genEquipRadioGroupsMRAttrMinProfileAdmin": genEquipRadioGroupsMRAttrMinProfileAdmin,
       "genEquipRadioGroupsMRAttrSigDegardeAdmin": genEquipRadioGroupsMRAttrSigDegardeAdmin,
       "genEquipRadioGroupsMRMembersTable": genEquipRadioGroupsMRMembersTable,
       "genEquipRadioGroupsMRMembersEntry": genEquipRadioGroupsMRMembersEntry,
       "genEquipRadioGroupsMRMembersIfIndexGroup": genEquipRadioGroupsMRMembersIfIndexGroup,
       "genEquipRadioGroupsMRMembersMem1IfIndex": genEquipRadioGroupsMRMembersMem1IfIndex,
       "genEquipRadioGroupsMRMembersMem2IfIndex": genEquipRadioGroupsMRMembersMem2IfIndex,
       "genEquipRadioGroupsMRMembersRowStatus": genEquipRadioGroupsMRMembersRowStatus,
       "genEquipRadioGroupsMRStatusTable": genEquipRadioGroupsMRStatusTable,
       "genEquipRadioGroupsMRStatusEntry": genEquipRadioGroupsMRStatusEntry,
       "genEquipRadioGroupsMRStatusGroupIfIndex": genEquipRadioGroupsMRStatusGroupIfIndex,
       "genEquipRadioGroupsMRStatusOpertionalState": genEquipRadioGroupsMRStatusOpertionalState,
       "genEquipRadioGroupsMRStatusRemoteOpertionalState": genEquipRadioGroupsMRStatusRemoteOpertionalState,
       "genEquipRadioGroupsMIMO": genEquipRadioGroupsMIMO,
       "genEquipRadioGroupsMIMOAttrTable": genEquipRadioGroupsMIMOAttrTable,
       "genEquipRadioGroupsMIMOAttrEntry": genEquipRadioGroupsMIMOAttrEntry,
       "genEquipRadioGroupsMIMOAttrGroupIfIndex": genEquipRadioGroupsMIMOAttrGroupIfIndex,
       "genEquipRadioGroupsMIMOAttrRole": genEquipRadioGroupsMIMOAttrRole,
       "genEquipRadioGroupsMIMOAttrAdmin": genEquipRadioGroupsMIMOAttrAdmin,
       "genEquipRadioGroupsMIMOAttrResetStateMachine": genEquipRadioGroupsMIMOAttrResetStateMachine,
       "genEquipRadioGroupsMIMOMembersTable": genEquipRadioGroupsMIMOMembersTable,
       "genEquipRadioGroupsMIMOMembersEntry": genEquipRadioGroupsMIMOMembersEntry,
       "genEquipRadioGroupsMIMOMembersGroupIfIndex": genEquipRadioGroupsMIMOMembersGroupIfIndex,
       "genEquipRadioGroupsMIMOMembersGroupType": genEquipRadioGroupsMIMOMembersGroupType,
       "genEquipRadioGroupsMIMOMembersMem1IfIndex": genEquipRadioGroupsMIMOMembersMem1IfIndex,
       "genEquipRadioGroupsMIMOMembersMem2IfIndex": genEquipRadioGroupsMIMOMembersMem2IfIndex,
       "genEquipRadioGroupsMIMOMembersMem3IfIndex": genEquipRadioGroupsMIMOMembersMem3IfIndex,
       "genEquipRadioGroupsMIMOMembersMem4IfIndex": genEquipRadioGroupsMIMOMembersMem4IfIndex,
       "genEquipRadioGroupsMIMOMembersRowStatus": genEquipRadioGroupsMIMOMembersRowStatus,
       "genEquipRadioGroupsMIMOStatusTable": genEquipRadioGroupsMIMOStatusTable,
       "genEquipRadioGroupsMIMOStatusEntry": genEquipRadioGroupsMIMOStatusEntry,
       "genEquipRadioGroupsMIMOStatusGroupIfIndex": genEquipRadioGroupsMIMOStatusGroupIfIndex,
       "genEquipRadioGroupsMIMOStatusState": genEquipRadioGroupsMIMOStatusState,
       "genEquipRadioGroupsMIMOStatus1stMMI": genEquipRadioGroupsMIMOStatus1stMMI,
       "genEquipRadioGroupsMIMOStatus2ndMMI": genEquipRadioGroupsMIMOStatus2ndMMI,
       "genEquipRadioGroupsMIMOStatus3rdMMI": genEquipRadioGroupsMIMOStatus3rdMMI,
       "genEquipRadioGroupsMIMOStatus4thMMI": genEquipRadioGroupsMIMOStatus4thMMI,
       "genEquipRadioGroupsMIMOStatusAdvancedState": genEquipRadioGroupsMIMOStatusAdvancedState,
       "genEquipRadioGroupsAbc": genEquipRadioGroupsAbc,
       "genEquipRadioGroupsAbcAttrTable": genEquipRadioGroupsAbcAttrTable,
       "genEquipRadioGroupsAbcAttrEntry": genEquipRadioGroupsAbcAttrEntry,
       "genEquipRadioGroupsAbcAttrIfIndex": genEquipRadioGroupsAbcAttrIfIndex,
       "genEquipRadioGroupsAbcAttrGroupName": genEquipRadioGroupsAbcAttrGroupName,
       "genEquipRadioGroupsAbcAttrAdminState": genEquipRadioGroupsAbcAttrAdminState,
       "genEquipRadioGroupsAbcAttrQnumberOfRadioMembers": genEquipRadioGroupsAbcAttrQnumberOfRadioMembers,
       "genEquipRadioGroupsAbcAttrProtectionEnable": genEquipRadioGroupsAbcAttrProtectionEnable,
       "genEquipRadioGroupsAbcAttrHighPriEthernetBandwidth": genEquipRadioGroupsAbcAttrHighPriEthernetBandwidth,
       "genEquipRadioGroupsAbcAttrQualityThreshold": genEquipRadioGroupsAbcAttrQualityThreshold,
       "genEquipRadioGroupsAbcAttrRowStatus": genEquipRadioGroupsAbcAttrRowStatus,
       "genEquipRadioGroupsAbcMembersTable": genEquipRadioGroupsAbcMembersTable,
       "genEquipRadioGroupsAbcMembersEntry": genEquipRadioGroupsAbcMembersEntry,
       "genEquipRadioGroupsAbcMembersGroupIfIndex": genEquipRadioGroupsAbcMembersGroupIfIndex,
       "genEquipRadioGroupsAbcMembersGroupId": genEquipRadioGroupsAbcMembersGroupId,
       "genEquipRadioGroupsAbcMembersChannel1MemberIfIndex": genEquipRadioGroupsAbcMembersChannel1MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel1adminState": genEquipRadioGroupsAbcMembersChannel1adminState,
       "genEquipRadioGroupsAbcMembersChannel2MemberIfIndex": genEquipRadioGroupsAbcMembersChannel2MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel2adminState": genEquipRadioGroupsAbcMembersChannel2adminState,
       "genEquipRadioGroupsAbcMembersChannel3MemberIfIndex": genEquipRadioGroupsAbcMembersChannel3MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel3adminState": genEquipRadioGroupsAbcMembersChannel3adminState,
       "genEquipRadioGroupsAbcMembersChannel4MemberIfIndex": genEquipRadioGroupsAbcMembersChannel4MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel4adminState": genEquipRadioGroupsAbcMembersChannel4adminState,
       "genEquipRadioGroupsAbcMembersChannel5MemberIfIndex": genEquipRadioGroupsAbcMembersChannel5MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel5adminState": genEquipRadioGroupsAbcMembersChannel5adminState,
       "genEquipRadioGroupsAbcMembersChannel6MemberIfIndex": genEquipRadioGroupsAbcMembersChannel6MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel6adminState": genEquipRadioGroupsAbcMembersChannel6adminState,
       "genEquipRadioGroupsAbcMembersChannel7MemberIfIndex": genEquipRadioGroupsAbcMembersChannel7MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel7adminState": genEquipRadioGroupsAbcMembersChannel7adminState,
       "genEquipRadioGroupsAbcMembersChannel8MemberIfIndex": genEquipRadioGroupsAbcMembersChannel8MemberIfIndex,
       "genEquipRadioGroupsAbcMembersChannel8adminState": genEquipRadioGroupsAbcMembersChannel8adminState,
       "genEquipRadioGroupsAbcStatusTable": genEquipRadioGroupsAbcStatusTable,
       "genEquipRadioGroupsAbcStatusEntry": genEquipRadioGroupsAbcStatusEntry,
       "genEquipRadioGroupsAbcStatusIfIndex": genEquipRadioGroupsAbcStatusIfIndex,
       "genEquipRadioGroupsAbcStatusOperState": genEquipRadioGroupsAbcStatusOperState,
       "genEquipRadioGroupsAbcStatusRemoteOperState": genEquipRadioGroupsAbcStatusRemoteOperState,
       "genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX": genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityRX,
       "genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX": genEquipRadioGroupsAbcStatusCurrentAggregatedCapacityTX,
       "genEquipRadioGroupsAbcStatusChannel1Operstate": genEquipRadioGroupsAbcStatusChannel1Operstate,
       "genEquipRadioGroupsAbcStatusChannel1Capacity": genEquipRadioGroupsAbcStatusChannel1Capacity,
       "genEquipRadioGroupsAbcStatusChannel2Operstate": genEquipRadioGroupsAbcStatusChannel2Operstate,
       "genEquipRadioGroupsAbcStatusChannel2Capacity": genEquipRadioGroupsAbcStatusChannel2Capacity,
       "genEquipRadioGroupsAbcStatusChannel3OperState": genEquipRadioGroupsAbcStatusChannel3OperState,
       "genEquipRadioGroupsAbcStatusChannel3Capacity": genEquipRadioGroupsAbcStatusChannel3Capacity,
       "genEquipRadioGroupsAbcStatusChannel4OperState": genEquipRadioGroupsAbcStatusChannel4OperState,
       "genEquipRadioGroupsAbcStatusChannel4Capacity": genEquipRadioGroupsAbcStatusChannel4Capacity,
       "genEquipRadioGroupsAbcStatusChannel5OperState": genEquipRadioGroupsAbcStatusChannel5OperState,
       "genEquipRadioGroupsAbcStatusChannel5Capacity": genEquipRadioGroupsAbcStatusChannel5Capacity,
       "genEquipRadioGroupsAbcStatusChannel6OperState": genEquipRadioGroupsAbcStatusChannel6OperState,
       "genEquipRadioGroupsAbcStatusChannel6Capacity": genEquipRadioGroupsAbcStatusChannel6Capacity,
       "genEquipRadioGroupsAbcStatusChannel7OperState": genEquipRadioGroupsAbcStatusChannel7OperState,
       "genEquipRadioGroupsAbcStatusChannel7Capacity": genEquipRadioGroupsAbcStatusChannel7Capacity,
       "genEquipRadioGroupsAbcStatusChannel8OperState": genEquipRadioGroupsAbcStatusChannel8OperState,
       "genEquipRadioGroupsAbcStatusChannel8Capacity": genEquipRadioGroupsAbcStatusChannel8Capacity,
       "genEquipStm1AbcAttrTable": genEquipStm1AbcAttrTable,
       "genEquipStm1AbcAttrEntry": genEquipStm1AbcAttrEntry,
       "genEquipStm1AbcAttrIfIndex": genEquipStm1AbcAttrIfIndex,
       "genEquipStm1AbcAttrGroupId": genEquipStm1AbcAttrGroupId,
       "genEquipStm1AbcAttrNumberOfMembers": genEquipStm1AbcAttrNumberOfMembers,
       "genEquipStm1AbcAttrPri1IfIndex": genEquipStm1AbcAttrPri1IfIndex,
       "genEquipStm1AbcAttrPri2IfIndex": genEquipStm1AbcAttrPri2IfIndex,
       "genEquipStm1AbcAttrPri3IfIndex": genEquipStm1AbcAttrPri3IfIndex,
       "genEquipStm1AbcAttrPri4IfIndex": genEquipStm1AbcAttrPri4IfIndex}
)
