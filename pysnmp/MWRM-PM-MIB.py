# SNMP MIB module (MWRM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MWRM-PM-MIB
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(genEquipRadioCfgRadioId,) = mibBuilder.importSymbols(
    "MWRM-RADIO-MIB",
    "genEquipRadioCfgRadioId")

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
 NotificationType,
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
    "NotificationType",
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
_GenEquipPM_ObjectIdentity = ObjectIdentity
genEquipPM = _GenEquipPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6)
)
_GenEquipPmRfu_ObjectIdentity = ObjectIdentity
genEquipPmRfu = _GenEquipPmRfu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1)
)
_GenEquipPmRfuCommon_ObjectIdentity = ObjectIdentity
genEquipPmRfuCommon = _GenEquipPmRfuCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1)
)
_GenEquipPmRfuCommonSL15minTable_Object = MibTable
genEquipPmRfuCommonSL15minTable = _GenEquipPmRfuCommonSL15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minTable.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minEntry_Object = MibTableRow
genEquipPmRfuCommonSL15minEntry = _GenEquipPmRfuCommonSL15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1)
)
genEquipPmRfuCommonSL15minEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRfuCommonSL15minId"),
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minEntry.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minId_Type = Integer32
_GenEquipPmRfuCommonSL15minId_Object = MibTableColumn
genEquipPmRfuCommonSL15minId = _GenEquipPmRfuCommonSL15minId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 1),
    _GenEquipPmRfuCommonSL15minId_Type()
)
genEquipPmRfuCommonSL15minId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minId.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minIfIndex_Type = Integer32
_GenEquipPmRfuCommonSL15minIfIndex_Object = MibTableColumn
genEquipPmRfuCommonSL15minIfIndex = _GenEquipPmRfuCommonSL15minIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 2),
    _GenEquipPmRfuCommonSL15minIfIndex_Type()
)
genEquipPmRfuCommonSL15minIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minIfIndex.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minTimeAndDate_Type = DisplayString
_GenEquipPmRfuCommonSL15minTimeAndDate_Object = MibTableColumn
genEquipPmRfuCommonSL15minTimeAndDate = _GenEquipPmRfuCommonSL15minTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 3),
    _GenEquipPmRfuCommonSL15minTimeAndDate_Type()
)
genEquipPmRfuCommonSL15minTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minTimeAndDate.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minMinRsl_Type = Integer32
_GenEquipPmRfuCommonSL15minMinRsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minMinRsl = _GenEquipPmRfuCommonSL15minMinRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 4),
    _GenEquipPmRfuCommonSL15minMinRsl_Type()
)
genEquipPmRfuCommonSL15minMinRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minMinRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minMaxRsl_Type = Integer32
_GenEquipPmRfuCommonSL15minMaxRsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minMaxRsl = _GenEquipPmRfuCommonSL15minMaxRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 5),
    _GenEquipPmRfuCommonSL15minMaxRsl_Type()
)
genEquipPmRfuCommonSL15minMaxRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minMaxRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minRslExceed1_Type = Integer32
_GenEquipPmRfuCommonSL15minRslExceed1_Object = MibTableColumn
genEquipPmRfuCommonSL15minRslExceed1 = _GenEquipPmRfuCommonSL15minRslExceed1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 6),
    _GenEquipPmRfuCommonSL15minRslExceed1_Type()
)
genEquipPmRfuCommonSL15minRslExceed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minRslExceed1.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minRslExceed2_Type = Integer32
_GenEquipPmRfuCommonSL15minRslExceed2_Object = MibTableColumn
genEquipPmRfuCommonSL15minRslExceed2 = _GenEquipPmRfuCommonSL15minRslExceed2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 7),
    _GenEquipPmRfuCommonSL15minRslExceed2_Type()
)
genEquipPmRfuCommonSL15minRslExceed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minRslExceed2.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minMinTsl_Type = Integer32
_GenEquipPmRfuCommonSL15minMinTsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minMinTsl = _GenEquipPmRfuCommonSL15minMinTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 8),
    _GenEquipPmRfuCommonSL15minMinTsl_Type()
)
genEquipPmRfuCommonSL15minMinTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minMinTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minMaxTsl_Type = Integer32
_GenEquipPmRfuCommonSL15minMaxTsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minMaxTsl = _GenEquipPmRfuCommonSL15minMaxTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 9),
    _GenEquipPmRfuCommonSL15minMaxTsl_Type()
)
genEquipPmRfuCommonSL15minMaxTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minMaxTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minTslExceed_Type = Integer32
_GenEquipPmRfuCommonSL15minTslExceed_Object = MibTableColumn
genEquipPmRfuCommonSL15minTslExceed = _GenEquipPmRfuCommonSL15minTslExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 10),
    _GenEquipPmRfuCommonSL15minTslExceed_Type()
)
genEquipPmRfuCommonSL15minTslExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minTslExceed.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minIDF_Type = Integrity
_GenEquipPmRfuCommonSL15minIDF_Object = MibTableColumn
genEquipPmRfuCommonSL15minIDF = _GenEquipPmRfuCommonSL15minIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 1, 1, 11),
    _GenEquipPmRfuCommonSL15minIDF_Type()
)
genEquipPmRfuCommonSL15minIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minIDF.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrTable_Object = MibTable
genEquipPmRfuCommonSL15minCurrTable = _GenEquipPmRfuCommonSL15minCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrTable.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrEntry_Object = MibTableRow
genEquipPmRfuCommonSL15minCurrEntry = _GenEquipPmRfuCommonSL15minCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1)
)
genEquipPmRfuCommonSL15minCurrEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRfuCommonSL15minCurrId"),
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrEntry.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrId_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrId_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrId = _GenEquipPmRfuCommonSL15minCurrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 1),
    _GenEquipPmRfuCommonSL15minCurrId_Type()
)
genEquipPmRfuCommonSL15minCurrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrId.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrIfIndex_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrIfIndex_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrIfIndex = _GenEquipPmRfuCommonSL15minCurrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 2),
    _GenEquipPmRfuCommonSL15minCurrIfIndex_Type()
)
genEquipPmRfuCommonSL15minCurrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrIfIndex.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrTimeAndDate_Type = DisplayString
_GenEquipPmRfuCommonSL15minCurrTimeAndDate_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrTimeAndDate = _GenEquipPmRfuCommonSL15minCurrTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 3),
    _GenEquipPmRfuCommonSL15minCurrTimeAndDate_Type()
)
genEquipPmRfuCommonSL15minCurrTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrTimeAndDate.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrMinRsl_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrMinRsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrMinRsl = _GenEquipPmRfuCommonSL15minCurrMinRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 4),
    _GenEquipPmRfuCommonSL15minCurrMinRsl_Type()
)
genEquipPmRfuCommonSL15minCurrMinRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrMinRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrMaxRsl_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrMaxRsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrMaxRsl = _GenEquipPmRfuCommonSL15minCurrMaxRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 5),
    _GenEquipPmRfuCommonSL15minCurrMaxRsl_Type()
)
genEquipPmRfuCommonSL15minCurrMaxRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrMaxRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrRslExceed1_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrRslExceed1_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrRslExceed1 = _GenEquipPmRfuCommonSL15minCurrRslExceed1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 6),
    _GenEquipPmRfuCommonSL15minCurrRslExceed1_Type()
)
genEquipPmRfuCommonSL15minCurrRslExceed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrRslExceed1.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrRslExceed2_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrRslExceed2_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrRslExceed2 = _GenEquipPmRfuCommonSL15minCurrRslExceed2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 7),
    _GenEquipPmRfuCommonSL15minCurrRslExceed2_Type()
)
genEquipPmRfuCommonSL15minCurrRslExceed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrRslExceed2.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrMinTsl_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrMinTsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrMinTsl = _GenEquipPmRfuCommonSL15minCurrMinTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 8),
    _GenEquipPmRfuCommonSL15minCurrMinTsl_Type()
)
genEquipPmRfuCommonSL15minCurrMinTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrMinTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrMaxTsl_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrMaxTsl_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrMaxTsl = _GenEquipPmRfuCommonSL15minCurrMaxTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 9),
    _GenEquipPmRfuCommonSL15minCurrMaxTsl_Type()
)
genEquipPmRfuCommonSL15minCurrMaxTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrMaxTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrTslExceed_Type = Integer32
_GenEquipPmRfuCommonSL15minCurrTslExceed_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrTslExceed = _GenEquipPmRfuCommonSL15minCurrTslExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 10),
    _GenEquipPmRfuCommonSL15minCurrTslExceed_Type()
)
genEquipPmRfuCommonSL15minCurrTslExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrTslExceed.setStatus("mandatory")
_GenEquipPmRfuCommonSL15minCurrIDF_Type = Integrity
_GenEquipPmRfuCommonSL15minCurrIDF_Object = MibTableColumn
genEquipPmRfuCommonSL15minCurrIDF = _GenEquipPmRfuCommonSL15minCurrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 2, 1, 11),
    _GenEquipPmRfuCommonSL15minCurrIDF_Type()
)
genEquipPmRfuCommonSL15minCurrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL15minCurrIDF.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrTable_Object = MibTable
genEquipPmRfuCommonSL24hrTable = _GenEquipPmRfuCommonSL24hrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrTable.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrEntry_Object = MibTableRow
genEquipPmRfuCommonSL24hrEntry = _GenEquipPmRfuCommonSL24hrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1)
)
genEquipPmRfuCommonSL24hrEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRfuCommonSL24hrId"),
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrEntry.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrId_Type = Integer32
_GenEquipPmRfuCommonSL24hrId_Object = MibTableColumn
genEquipPmRfuCommonSL24hrId = _GenEquipPmRfuCommonSL24hrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 1),
    _GenEquipPmRfuCommonSL24hrId_Type()
)
genEquipPmRfuCommonSL24hrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrId.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrIfIndex_Type = Integer32
_GenEquipPmRfuCommonSL24hrIfIndex_Object = MibTableColumn
genEquipPmRfuCommonSL24hrIfIndex = _GenEquipPmRfuCommonSL24hrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 2),
    _GenEquipPmRfuCommonSL24hrIfIndex_Type()
)
genEquipPmRfuCommonSL24hrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrIfIndex.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrTimeAndDate_Type = DisplayString
_GenEquipPmRfuCommonSL24hrTimeAndDate_Object = MibTableColumn
genEquipPmRfuCommonSL24hrTimeAndDate = _GenEquipPmRfuCommonSL24hrTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 3),
    _GenEquipPmRfuCommonSL24hrTimeAndDate_Type()
)
genEquipPmRfuCommonSL24hrTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrTimeAndDate.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrMinRsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrMinRsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrMinRsl = _GenEquipPmRfuCommonSL24hrMinRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 4),
    _GenEquipPmRfuCommonSL24hrMinRsl_Type()
)
genEquipPmRfuCommonSL24hrMinRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrMinRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrMaxRsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrMaxRsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrMaxRsl = _GenEquipPmRfuCommonSL24hrMaxRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 5),
    _GenEquipPmRfuCommonSL24hrMaxRsl_Type()
)
genEquipPmRfuCommonSL24hrMaxRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrMaxRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrRslExceed1_Type = Integer32
_GenEquipPmRfuCommonSL24hrRslExceed1_Object = MibTableColumn
genEquipPmRfuCommonSL24hrRslExceed1 = _GenEquipPmRfuCommonSL24hrRslExceed1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 6),
    _GenEquipPmRfuCommonSL24hrRslExceed1_Type()
)
genEquipPmRfuCommonSL24hrRslExceed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrRslExceed1.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrRslExceed2_Type = Integer32
_GenEquipPmRfuCommonSL24hrRslExceed2_Object = MibTableColumn
genEquipPmRfuCommonSL24hrRslExceed2 = _GenEquipPmRfuCommonSL24hrRslExceed2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 7),
    _GenEquipPmRfuCommonSL24hrRslExceed2_Type()
)
genEquipPmRfuCommonSL24hrRslExceed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrRslExceed2.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrMinTsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrMinTsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrMinTsl = _GenEquipPmRfuCommonSL24hrMinTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 8),
    _GenEquipPmRfuCommonSL24hrMinTsl_Type()
)
genEquipPmRfuCommonSL24hrMinTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrMinTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrMaxTsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrMaxTsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrMaxTsl = _GenEquipPmRfuCommonSL24hrMaxTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 9),
    _GenEquipPmRfuCommonSL24hrMaxTsl_Type()
)
genEquipPmRfuCommonSL24hrMaxTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrMaxTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrTslExceed_Type = Integer32
_GenEquipPmRfuCommonSL24hrTslExceed_Object = MibTableColumn
genEquipPmRfuCommonSL24hrTslExceed = _GenEquipPmRfuCommonSL24hrTslExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 10),
    _GenEquipPmRfuCommonSL24hrTslExceed_Type()
)
genEquipPmRfuCommonSL24hrTslExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrTslExceed.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrIDF_Type = Integrity
_GenEquipPmRfuCommonSL24hrIDF_Object = MibTableColumn
genEquipPmRfuCommonSL24hrIDF = _GenEquipPmRfuCommonSL24hrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 3, 1, 11),
    _GenEquipPmRfuCommonSL24hrIDF_Type()
)
genEquipPmRfuCommonSL24hrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrIDF.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrTable_Object = MibTable
genEquipPmRfuCommonSL24hrCurrTable = _GenEquipPmRfuCommonSL24hrCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrTable.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrEntry_Object = MibTableRow
genEquipPmRfuCommonSL24hrCurrEntry = _GenEquipPmRfuCommonSL24hrCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1)
)
genEquipPmRfuCommonSL24hrCurrEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRfuCommonSL24hrCurrId"),
)
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrEntry.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrId_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrId_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrId = _GenEquipPmRfuCommonSL24hrCurrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 1),
    _GenEquipPmRfuCommonSL24hrCurrId_Type()
)
genEquipPmRfuCommonSL24hrCurrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrId.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrIfIndex_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrIfIndex_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrIfIndex = _GenEquipPmRfuCommonSL24hrCurrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 2),
    _GenEquipPmRfuCommonSL24hrCurrIfIndex_Type()
)
genEquipPmRfuCommonSL24hrCurrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrIfIndex.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrTimeAndDate_Type = DisplayString
_GenEquipPmRfuCommonSL24hrCurrTimeAndDate_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrTimeAndDate = _GenEquipPmRfuCommonSL24hrCurrTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 3),
    _GenEquipPmRfuCommonSL24hrCurrTimeAndDate_Type()
)
genEquipPmRfuCommonSL24hrCurrTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrTimeAndDate.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrMinRsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrMinRsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrMinRsl = _GenEquipPmRfuCommonSL24hrCurrMinRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 4),
    _GenEquipPmRfuCommonSL24hrCurrMinRsl_Type()
)
genEquipPmRfuCommonSL24hrCurrMinRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrMinRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrMaxRsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrMaxRsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrMaxRsl = _GenEquipPmRfuCommonSL24hrCurrMaxRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 5),
    _GenEquipPmRfuCommonSL24hrCurrMaxRsl_Type()
)
genEquipPmRfuCommonSL24hrCurrMaxRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrMaxRsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrRslExceed1_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrRslExceed1_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrRslExceed1 = _GenEquipPmRfuCommonSL24hrCurrRslExceed1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 6),
    _GenEquipPmRfuCommonSL24hrCurrRslExceed1_Type()
)
genEquipPmRfuCommonSL24hrCurrRslExceed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrRslExceed1.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrRslExceed2_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrRslExceed2_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrRslExceed2 = _GenEquipPmRfuCommonSL24hrCurrRslExceed2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 7),
    _GenEquipPmRfuCommonSL24hrCurrRslExceed2_Type()
)
genEquipPmRfuCommonSL24hrCurrRslExceed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrRslExceed2.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrMinTsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrMinTsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrMinTsl = _GenEquipPmRfuCommonSL24hrCurrMinTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 8),
    _GenEquipPmRfuCommonSL24hrCurrMinTsl_Type()
)
genEquipPmRfuCommonSL24hrCurrMinTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrMinTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrMaxTsl_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrMaxTsl_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrMaxTsl = _GenEquipPmRfuCommonSL24hrCurrMaxTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 9),
    _GenEquipPmRfuCommonSL24hrCurrMaxTsl_Type()
)
genEquipPmRfuCommonSL24hrCurrMaxTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrMaxTsl.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrTslExceed_Type = Integer32
_GenEquipPmRfuCommonSL24hrCurrTslExceed_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrTslExceed = _GenEquipPmRfuCommonSL24hrCurrTslExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 10),
    _GenEquipPmRfuCommonSL24hrCurrTslExceed_Type()
)
genEquipPmRfuCommonSL24hrCurrTslExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrTslExceed.setStatus("mandatory")
_GenEquipPmRfuCommonSL24hrCurrIDF_Type = Integrity
_GenEquipPmRfuCommonSL24hrCurrIDF_Object = MibTableColumn
genEquipPmRfuCommonSL24hrCurrIDF = _GenEquipPmRfuCommonSL24hrCurrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 1, 1, 4, 1, 11),
    _GenEquipPmRfuCommonSL24hrCurrIDF_Type()
)
genEquipPmRfuCommonSL24hrCurrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRfuCommonSL24hrCurrIDF.setStatus("mandatory")
_GenEquipPmTraffic_ObjectIdentity = ObjectIdentity
genEquipPmTraffic = _GenEquipPmTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2)
)
_GenEquipPmTrafficRadioAgg15minTable_Object = MibTable
genEquipPmTrafficRadioAgg15minTable = _GenEquipPmTrafficRadioAgg15minTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minTable.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minEntry_Object = MibTableRow
genEquipPmTrafficRadioAgg15minEntry = _GenEquipPmTrafficRadioAgg15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1)
)
genEquipPmTrafficRadioAgg15minEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrafficRadioAgg15minId"),
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minEntry.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minId_Type = Integer32
_GenEquipPmTrafficRadioAgg15minId_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minId = _GenEquipPmTrafficRadioAgg15minId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 1),
    _GenEquipPmTrafficRadioAgg15minId_Type()
)
genEquipPmTrafficRadioAgg15minId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minId.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minIfIndex_Type = Integer32
_GenEquipPmTrafficRadioAgg15minIfIndex_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minIfIndex = _GenEquipPmTrafficRadioAgg15minIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 2),
    _GenEquipPmTrafficRadioAgg15minIfIndex_Type()
)
genEquipPmTrafficRadioAgg15minIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minIfIndex.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minTimeAndDate_Type = DisplayString
_GenEquipPmTrafficRadioAgg15minTimeAndDate_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minTimeAndDate = _GenEquipPmTrafficRadioAgg15minTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 3),
    _GenEquipPmTrafficRadioAgg15minTimeAndDate_Type()
)
genEquipPmTrafficRadioAgg15minTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minTimeAndDate.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minES_Type = Integer32
_GenEquipPmTrafficRadioAgg15minES_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minES = _GenEquipPmTrafficRadioAgg15minES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 4),
    _GenEquipPmTrafficRadioAgg15minES_Type()
)
genEquipPmTrafficRadioAgg15minES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minSES_Type = Integer32
_GenEquipPmTrafficRadioAgg15minSES_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minSES = _GenEquipPmTrafficRadioAgg15minSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 5),
    _GenEquipPmTrafficRadioAgg15minSES_Type()
)
genEquipPmTrafficRadioAgg15minSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minSES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minUAS_Type = Integer32
_GenEquipPmTrafficRadioAgg15minUAS_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minUAS = _GenEquipPmTrafficRadioAgg15minUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 6),
    _GenEquipPmTrafficRadioAgg15minUAS_Type()
)
genEquipPmTrafficRadioAgg15minUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minUAS.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minBBE_Type = Integer32
_GenEquipPmTrafficRadioAgg15minBBE_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minBBE = _GenEquipPmTrafficRadioAgg15minBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 7),
    _GenEquipPmTrafficRadioAgg15minBBE_Type()
)
genEquipPmTrafficRadioAgg15minBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minBBE.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minIDF_Type = Integrity
_GenEquipPmTrafficRadioAgg15minIDF_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minIDF = _GenEquipPmTrafficRadioAgg15minIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 1, 1, 8),
    _GenEquipPmTrafficRadioAgg15minIDF_Type()
)
genEquipPmTrafficRadioAgg15minIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minIDF.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrTable_Object = MibTable
genEquipPmTrafficRadioAgg15minCurrTable = _GenEquipPmTrafficRadioAgg15minCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2)
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrTable.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrEntry_Object = MibTableRow
genEquipPmTrafficRadioAgg15minCurrEntry = _GenEquipPmTrafficRadioAgg15minCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1)
)
genEquipPmTrafficRadioAgg15minCurrEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrafficRadioAgg15minCurrId"),
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrEntry.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrId_Type = Integer32
_GenEquipPmTrafficRadioAgg15minCurrId_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrId = _GenEquipPmTrafficRadioAgg15minCurrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 1),
    _GenEquipPmTrafficRadioAgg15minCurrId_Type()
)
genEquipPmTrafficRadioAgg15minCurrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrId.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrIfIndex_Type = Integer32
_GenEquipPmTrafficRadioAgg15minCurrIfIndex_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrIfIndex = _GenEquipPmTrafficRadioAgg15minCurrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 2),
    _GenEquipPmTrafficRadioAgg15minCurrIfIndex_Type()
)
genEquipPmTrafficRadioAgg15minCurrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrIfIndex.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrTimeAndDate_Type = DisplayString
_GenEquipPmTrafficRadioAgg15minCurrTimeAndDate_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrTimeAndDate = _GenEquipPmTrafficRadioAgg15minCurrTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 3),
    _GenEquipPmTrafficRadioAgg15minCurrTimeAndDate_Type()
)
genEquipPmTrafficRadioAgg15minCurrTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrTimeAndDate.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrES_Type = Integer32
_GenEquipPmTrafficRadioAgg15minCurrES_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrES = _GenEquipPmTrafficRadioAgg15minCurrES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 4),
    _GenEquipPmTrafficRadioAgg15minCurrES_Type()
)
genEquipPmTrafficRadioAgg15minCurrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrSES_Type = Integer32
_GenEquipPmTrafficRadioAgg15minCurrSES_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrSES = _GenEquipPmTrafficRadioAgg15minCurrSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 5),
    _GenEquipPmTrafficRadioAgg15minCurrSES_Type()
)
genEquipPmTrafficRadioAgg15minCurrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrSES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrUAS_Type = Integer32
_GenEquipPmTrafficRadioAgg15minCurrUAS_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrUAS = _GenEquipPmTrafficRadioAgg15minCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 6),
    _GenEquipPmTrafficRadioAgg15minCurrUAS_Type()
)
genEquipPmTrafficRadioAgg15minCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrUAS.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrBBE_Type = Integer32
_GenEquipPmTrafficRadioAgg15minCurrBBE_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrBBE = _GenEquipPmTrafficRadioAgg15minCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 7),
    _GenEquipPmTrafficRadioAgg15minCurrBBE_Type()
)
genEquipPmTrafficRadioAgg15minCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrBBE.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg15minCurrIDF_Type = Integrity
_GenEquipPmTrafficRadioAgg15minCurrIDF_Object = MibTableColumn
genEquipPmTrafficRadioAgg15minCurrIDF = _GenEquipPmTrafficRadioAgg15minCurrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 2, 1, 8),
    _GenEquipPmTrafficRadioAgg15minCurrIDF_Type()
)
genEquipPmTrafficRadioAgg15minCurrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg15minCurrIDF.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrTable_Object = MibTable
genEquipPmTrafficRadioAgg24hrTable = _GenEquipPmTrafficRadioAgg24hrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3)
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrTable.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrEntry_Object = MibTableRow
genEquipPmTrafficRadioAgg24hrEntry = _GenEquipPmTrafficRadioAgg24hrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1)
)
genEquipPmTrafficRadioAgg24hrEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrafficRadioAgg24hrId"),
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrEntry.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrId_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrId_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrId = _GenEquipPmTrafficRadioAgg24hrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 1),
    _GenEquipPmTrafficRadioAgg24hrId_Type()
)
genEquipPmTrafficRadioAgg24hrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrId.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrIfIndex_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrIfIndex_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrIfIndex = _GenEquipPmTrafficRadioAgg24hrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 2),
    _GenEquipPmTrafficRadioAgg24hrIfIndex_Type()
)
genEquipPmTrafficRadioAgg24hrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrIfIndex.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrTimeAndDate_Type = DisplayString
_GenEquipPmTrafficRadioAgg24hrTimeAndDate_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrTimeAndDate = _GenEquipPmTrafficRadioAgg24hrTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 3),
    _GenEquipPmTrafficRadioAgg24hrTimeAndDate_Type()
)
genEquipPmTrafficRadioAgg24hrTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrTimeAndDate.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrES_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrES_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrES = _GenEquipPmTrafficRadioAgg24hrES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 4),
    _GenEquipPmTrafficRadioAgg24hrES_Type()
)
genEquipPmTrafficRadioAgg24hrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrSES_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrSES_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrSES = _GenEquipPmTrafficRadioAgg24hrSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 5),
    _GenEquipPmTrafficRadioAgg24hrSES_Type()
)
genEquipPmTrafficRadioAgg24hrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrSES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrUAS_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrUAS_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrUAS = _GenEquipPmTrafficRadioAgg24hrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 6),
    _GenEquipPmTrafficRadioAgg24hrUAS_Type()
)
genEquipPmTrafficRadioAgg24hrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrUAS.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrBBE_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrBBE_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrBBE = _GenEquipPmTrafficRadioAgg24hrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 7),
    _GenEquipPmTrafficRadioAgg24hrBBE_Type()
)
genEquipPmTrafficRadioAgg24hrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrBBE.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrIDF_Type = Integrity
_GenEquipPmTrafficRadioAgg24hrIDF_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrIDF = _GenEquipPmTrafficRadioAgg24hrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 3, 1, 8),
    _GenEquipPmTrafficRadioAgg24hrIDF_Type()
)
genEquipPmTrafficRadioAgg24hrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrIDF.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrTable_Object = MibTable
genEquipPmTrafficRadioAgg24hrCurrTable = _GenEquipPmTrafficRadioAgg24hrCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4)
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrTable.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrEntry_Object = MibTableRow
genEquipPmTrafficRadioAgg24hrCurrEntry = _GenEquipPmTrafficRadioAgg24hrCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1)
)
genEquipPmTrafficRadioAgg24hrCurrEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrafficRadioAgg24hrCurrId"),
)
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrEntry.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrId_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrCurrId_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrId = _GenEquipPmTrafficRadioAgg24hrCurrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 1),
    _GenEquipPmTrafficRadioAgg24hrCurrId_Type()
)
genEquipPmTrafficRadioAgg24hrCurrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrId.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrIfIndex_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrCurrIfIndex_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrIfIndex = _GenEquipPmTrafficRadioAgg24hrCurrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 2),
    _GenEquipPmTrafficRadioAgg24hrCurrIfIndex_Type()
)
genEquipPmTrafficRadioAgg24hrCurrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrIfIndex.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrTimeAndDate_Type = DisplayString
_GenEquipPmTrafficRadioAgg24hrCurrTimeAndDate_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrTimeAndDate = _GenEquipPmTrafficRadioAgg24hrCurrTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 3),
    _GenEquipPmTrafficRadioAgg24hrCurrTimeAndDate_Type()
)
genEquipPmTrafficRadioAgg24hrCurrTimeAndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrTimeAndDate.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrES_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrCurrES_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrES = _GenEquipPmTrafficRadioAgg24hrCurrES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 4),
    _GenEquipPmTrafficRadioAgg24hrCurrES_Type()
)
genEquipPmTrafficRadioAgg24hrCurrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrSES_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrCurrSES_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrSES = _GenEquipPmTrafficRadioAgg24hrCurrSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 5),
    _GenEquipPmTrafficRadioAgg24hrCurrSES_Type()
)
genEquipPmTrafficRadioAgg24hrCurrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrSES.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrUAS_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrCurrUAS_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrUAS = _GenEquipPmTrafficRadioAgg24hrCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 6),
    _GenEquipPmTrafficRadioAgg24hrCurrUAS_Type()
)
genEquipPmTrafficRadioAgg24hrCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrUAS.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrBBE_Type = Integer32
_GenEquipPmTrafficRadioAgg24hrCurrBBE_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrBBE = _GenEquipPmTrafficRadioAgg24hrCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 7),
    _GenEquipPmTrafficRadioAgg24hrCurrBBE_Type()
)
genEquipPmTrafficRadioAgg24hrCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrBBE.setStatus("mandatory")
_GenEquipPmTrafficRadioAgg24hrCurrIDF_Type = Integrity
_GenEquipPmTrafficRadioAgg24hrCurrIDF_Object = MibTableColumn
genEquipPmTrafficRadioAgg24hrCurrIDF = _GenEquipPmTrafficRadioAgg24hrCurrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 2, 4, 1, 8),
    _GenEquipPmTrafficRadioAgg24hrCurrIDF_Type()
)
genEquipPmTrafficRadioAgg24hrCurrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficRadioAgg24hrCurrIDF.setStatus("mandatory")
_GenEquipPmAll_ObjectIdentity = ObjectIdentity
genEquipPmAll = _GenEquipPmAll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3)
)
_GenEquipPmClear_Type = OffOn
_GenEquipPmClear_Object = MibScalar
genEquipPmClear = _GenEquipPmClear_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 1),
    _GenEquipPmClear_Type()
)
genEquipPmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmClear.setStatus("mandatory")
_GenEquipPmTrafficSL_ObjectIdentity = ObjectIdentity
genEquipPmTrafficSL = _GenEquipPmTrafficSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2)
)
_GenEquipPmTrafficSLTable_Object = MibTable
genEquipPmTrafficSLTable = _GenEquipPmTrafficSLTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipPmTrafficSLTable.setStatus("mandatory")
_GenEquipPmTrafficSLEntry_Object = MibTableRow
genEquipPmTrafficSLEntry = _GenEquipPmTrafficSLEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1)
)
genEquipPmTrafficSLEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrafficSLPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmTrafficSLId"),
    (0, "MWRM-PM-MIB", "genEquipPmTrafficSLInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmTrafficSLEntry.setStatus("mandatory")
_GenEquipPmTrafficSLPmType_Type = PmTableType
_GenEquipPmTrafficSLPmType_Object = MibTableColumn
genEquipPmTrafficSLPmType = _GenEquipPmTrafficSLPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 1),
    _GenEquipPmTrafficSLPmType_Type()
)
genEquipPmTrafficSLPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLPmType.setStatus("mandatory")
_GenEquipPmTrafficSLId_Type = RfuId
_GenEquipPmTrafficSLId_Object = MibTableColumn
genEquipPmTrafficSLId = _GenEquipPmTrafficSLId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 2),
    _GenEquipPmTrafficSLId_Type()
)
genEquipPmTrafficSLId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLId.setStatus("mandatory")
_GenEquipPmTrafficSLInterval_Type = Integer32
_GenEquipPmTrafficSLInterval_Object = MibTableColumn
genEquipPmTrafficSLInterval = _GenEquipPmTrafficSLInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 3),
    _GenEquipPmTrafficSLInterval_Type()
)
genEquipPmTrafficSLInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLInterval.setStatus("mandatory")
_GenEquipPmTrafficSLMinRsl_Type = Integer32
_GenEquipPmTrafficSLMinRsl_Object = MibTableColumn
genEquipPmTrafficSLMinRsl = _GenEquipPmTrafficSLMinRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 4),
    _GenEquipPmTrafficSLMinRsl_Type()
)
genEquipPmTrafficSLMinRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLMinRsl.setStatus("mandatory")
_GenEquipPmTrafficSLMaxRsl_Type = Integer32
_GenEquipPmTrafficSLMaxRsl_Object = MibTableColumn
genEquipPmTrafficSLMaxRsl = _GenEquipPmTrafficSLMaxRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 5),
    _GenEquipPmTrafficSLMaxRsl_Type()
)
genEquipPmTrafficSLMaxRsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLMaxRsl.setStatus("mandatory")
_GenEquipPmTrafficSLRslExceed1_Type = Integer32
_GenEquipPmTrafficSLRslExceed1_Object = MibTableColumn
genEquipPmTrafficSLRslExceed1 = _GenEquipPmTrafficSLRslExceed1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 6),
    _GenEquipPmTrafficSLRslExceed1_Type()
)
genEquipPmTrafficSLRslExceed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLRslExceed1.setStatus("mandatory")
_GenEquipPmTrafficSLRslExceed2_Type = Integer32
_GenEquipPmTrafficSLRslExceed2_Object = MibTableColumn
genEquipPmTrafficSLRslExceed2 = _GenEquipPmTrafficSLRslExceed2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 7),
    _GenEquipPmTrafficSLRslExceed2_Type()
)
genEquipPmTrafficSLRslExceed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLRslExceed2.setStatus("mandatory")
_GenEquipPmTrafficSLMinTsl_Type = Integer32
_GenEquipPmTrafficSLMinTsl_Object = MibTableColumn
genEquipPmTrafficSLMinTsl = _GenEquipPmTrafficSLMinTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 8),
    _GenEquipPmTrafficSLMinTsl_Type()
)
genEquipPmTrafficSLMinTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLMinTsl.setStatus("mandatory")
_GenEquipPmTrafficSLMaxTsl_Type = Integer32
_GenEquipPmTrafficSLMaxTsl_Object = MibTableColumn
genEquipPmTrafficSLMaxTsl = _GenEquipPmTrafficSLMaxTsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 9),
    _GenEquipPmTrafficSLMaxTsl_Type()
)
genEquipPmTrafficSLMaxTsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLMaxTsl.setStatus("mandatory")
_GenEquipPmTrafficSLTslExceed_Type = Integer32
_GenEquipPmTrafficSLTslExceed_Object = MibTableColumn
genEquipPmTrafficSLTslExceed = _GenEquipPmTrafficSLTslExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 10),
    _GenEquipPmTrafficSLTslExceed_Type()
)
genEquipPmTrafficSLTslExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLTslExceed.setStatus("mandatory")
_GenEquipPmTrafficSLIDF_Type = Integrity
_GenEquipPmTrafficSLIDF_Object = MibTableColumn
genEquipPmTrafficSLIDF = _GenEquipPmTrafficSLIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 2, 1, 1, 11),
    _GenEquipPmTrafficSLIDF_Type()
)
genEquipPmTrafficSLIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficSLIDF.setStatus("mandatory")
_GenEquipPmTrafficAggregate_ObjectIdentity = ObjectIdentity
genEquipPmTrafficAggregate = _GenEquipPmTrafficAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3)
)
_GenEquipPmTrafficAggTable_Object = MibTable
genEquipPmTrafficAggTable = _GenEquipPmTrafficAggTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    genEquipPmTrafficAggTable.setStatus("mandatory")
_GenEquipPmTrafficAggEntry_Object = MibTableRow
genEquipPmTrafficAggEntry = _GenEquipPmTrafficAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1)
)
genEquipPmTrafficAggEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrafficAggPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmTrafficAggInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmTrafficAggEntry.setStatus("mandatory")
_GenEquipPmTrafficAggPmType_Type = PmTableType
_GenEquipPmTrafficAggPmType_Object = MibTableColumn
genEquipPmTrafficAggPmType = _GenEquipPmTrafficAggPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 1),
    _GenEquipPmTrafficAggPmType_Type()
)
genEquipPmTrafficAggPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggPmType.setStatus("mandatory")
_GenEquipPmTrafficAggInterval_Type = Integer32
_GenEquipPmTrafficAggInterval_Object = MibTableColumn
genEquipPmTrafficAggInterval = _GenEquipPmTrafficAggInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 2),
    _GenEquipPmTrafficAggInterval_Type()
)
genEquipPmTrafficAggInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggInterval.setStatus("mandatory")
_GenEquipPmTrafficAggES_Type = Integer32
_GenEquipPmTrafficAggES_Object = MibTableColumn
genEquipPmTrafficAggES = _GenEquipPmTrafficAggES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 3),
    _GenEquipPmTrafficAggES_Type()
)
genEquipPmTrafficAggES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggES.setStatus("mandatory")
_GenEquipPmTrafficAggSES_Type = Integer32
_GenEquipPmTrafficAggSES_Object = MibTableColumn
genEquipPmTrafficAggSES = _GenEquipPmTrafficAggSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 4),
    _GenEquipPmTrafficAggSES_Type()
)
genEquipPmTrafficAggSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggSES.setStatus("mandatory")
_GenEquipPmTrafficAggUAS_Type = Integer32
_GenEquipPmTrafficAggUAS_Object = MibTableColumn
genEquipPmTrafficAggUAS = _GenEquipPmTrafficAggUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 5),
    _GenEquipPmTrafficAggUAS_Type()
)
genEquipPmTrafficAggUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggUAS.setStatus("mandatory")
_GenEquipPmTrafficAggBBE_Type = Integer32
_GenEquipPmTrafficAggBBE_Object = MibTableColumn
genEquipPmTrafficAggBBE = _GenEquipPmTrafficAggBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 6),
    _GenEquipPmTrafficAggBBE_Type()
)
genEquipPmTrafficAggBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggBBE.setStatus("mandatory")
_GenEquipPmTrafficAggIDF_Type = Integrity
_GenEquipPmTrafficAggIDF_Object = MibTableColumn
genEquipPmTrafficAggIDF = _GenEquipPmTrafficAggIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 3, 1, 1, 7),
    _GenEquipPmTrafficAggIDF_Type()
)
genEquipPmTrafficAggIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrafficAggIDF.setStatus("mandatory")
_GenEquipPmRadio_ObjectIdentity = ObjectIdentity
genEquipPmRadio = _GenEquipPmRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4)
)
_GenEquipPmRadioMRMC_ObjectIdentity = ObjectIdentity
genEquipPmRadioMRMC = _GenEquipPmRadioMRMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1)
)
_GenEquipPmRadioMRMCTable_Object = MibTable
genEquipPmRadioMRMCTable = _GenEquipPmRadioMRMCTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCTable.setStatus("mandatory")
_GenEquipPmRadioMRMCEntry_Object = MibTableRow
genEquipPmRadioMRMCEntry = _GenEquipPmRadioMRMCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1)
)
genEquipPmRadioMRMCEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRadioMRMCPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioMRMCId"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioMRMCInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCEntry.setStatus("mandatory")
_GenEquipPmRadioMRMCPmType_Type = PmTableType
_GenEquipPmRadioMRMCPmType_Object = MibTableColumn
genEquipPmRadioMRMCPmType = _GenEquipPmRadioMRMCPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 1),
    _GenEquipPmRadioMRMCPmType_Type()
)
genEquipPmRadioMRMCPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCPmType.setStatus("mandatory")
_GenEquipPmRadioMRMCId_Type = RadioId
_GenEquipPmRadioMRMCId_Object = MibTableColumn
genEquipPmRadioMRMCId = _GenEquipPmRadioMRMCId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 2),
    _GenEquipPmRadioMRMCId_Type()
)
genEquipPmRadioMRMCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCId.setStatus("mandatory")
_GenEquipPmRadioMRMCInterval_Type = Integer32
_GenEquipPmRadioMRMCInterval_Object = MibTableColumn
genEquipPmRadioMRMCInterval = _GenEquipPmRadioMRMCInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 3),
    _GenEquipPmRadioMRMCInterval_Type()
)
genEquipPmRadioMRMCInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCInterval.setStatus("mandatory")
_GenEquipPmRadioMRMCIfIndex_Type = Integer32
_GenEquipPmRadioMRMCIfIndex_Object = MibTableColumn
genEquipPmRadioMRMCIfIndex = _GenEquipPmRadioMRMCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 4),
    _GenEquipPmRadioMRMCIfIndex_Type()
)
genEquipPmRadioMRMCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCIfIndex.setStatus("mandatory")
_GenEquipPmRadioMRMCMinProfile_Type = Integer32
_GenEquipPmRadioMRMCMinProfile_Object = MibTableColumn
genEquipPmRadioMRMCMinProfile = _GenEquipPmRadioMRMCMinProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 5),
    _GenEquipPmRadioMRMCMinProfile_Type()
)
genEquipPmRadioMRMCMinProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCMinProfile.setStatus("mandatory")
_GenEquipPmRadioMRMCMaxProfile_Type = Integer32
_GenEquipPmRadioMRMCMaxProfile_Object = MibTableColumn
genEquipPmRadioMRMCMaxProfile = _GenEquipPmRadioMRMCMaxProfile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 6),
    _GenEquipPmRadioMRMCMaxProfile_Type()
)
genEquipPmRadioMRMCMaxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCMaxProfile.setStatus("mandatory")
_GenEquipPmRadioMRMCMinBitrate_Type = Integer32
_GenEquipPmRadioMRMCMinBitrate_Object = MibTableColumn
genEquipPmRadioMRMCMinBitrate = _GenEquipPmRadioMRMCMinBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 7),
    _GenEquipPmRadioMRMCMinBitrate_Type()
)
genEquipPmRadioMRMCMinBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCMinBitrate.setStatus("mandatory")
_GenEquipPmRadioMRMCMaxBitrate_Type = Integer32
_GenEquipPmRadioMRMCMaxBitrate_Object = MibTableColumn
genEquipPmRadioMRMCMaxBitrate = _GenEquipPmRadioMRMCMaxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 8),
    _GenEquipPmRadioMRMCMaxBitrate_Type()
)
genEquipPmRadioMRMCMaxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCMaxBitrate.setStatus("mandatory")
_GenEquipPmRadioMRMCMinTDMIf_Type = Integer32
_GenEquipPmRadioMRMCMinTDMIf_Object = MibTableColumn
genEquipPmRadioMRMCMinTDMIf = _GenEquipPmRadioMRMCMinTDMIf_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 9),
    _GenEquipPmRadioMRMCMinTDMIf_Type()
)
genEquipPmRadioMRMCMinTDMIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCMinTDMIf.setStatus("mandatory")
_GenEquipPmRadioMRMCMaxTDMIf_Type = Integer32
_GenEquipPmRadioMRMCMaxTDMIf_Object = MibTableColumn
genEquipPmRadioMRMCMaxTDMIf = _GenEquipPmRadioMRMCMaxTDMIf_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 10),
    _GenEquipPmRadioMRMCMaxTDMIf_Type()
)
genEquipPmRadioMRMCMaxTDMIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCMaxTDMIf.setStatus("mandatory")
_GenEquipPmRadioMRMCIDF_Type = Integrity
_GenEquipPmRadioMRMCIDF_Object = MibTableColumn
genEquipPmRadioMRMCIDF = _GenEquipPmRadioMRMCIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 1, 1, 1, 11),
    _GenEquipPmRadioMRMCIDF_Type()
)
genEquipPmRadioMRMCIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMRMCIDF.setStatus("mandatory")
_GenEquipPmRadioTDM_ObjectIdentity = ObjectIdentity
genEquipPmRadioTDM = _GenEquipPmRadioTDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2)
)
_GenEquipPmRadioTDMTable_Object = MibTable
genEquipPmRadioTDMTable = _GenEquipPmRadioTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    genEquipPmRadioTDMTable.setStatus("mandatory")
_GenEquipPmRadioTDMEntry_Object = MibTableRow
genEquipPmRadioTDMEntry = _GenEquipPmRadioTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2, 1, 1)
)
genEquipPmRadioTDMEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRadioTDMPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioTDMInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioTDMEntry.setStatus("mandatory")
_GenEquipPmRadioTDMPmType_Type = PmTableType
_GenEquipPmRadioTDMPmType_Object = MibTableColumn
genEquipPmRadioTDMPmType = _GenEquipPmRadioTDMPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2, 1, 1, 1),
    _GenEquipPmRadioTDMPmType_Type()
)
genEquipPmRadioTDMPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioTDMPmType.setStatus("mandatory")
_GenEquipPmRadioTDMInterval_Type = Integer32
_GenEquipPmRadioTDMInterval_Object = MibTableColumn
genEquipPmRadioTDMInterval = _GenEquipPmRadioTDMInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2, 1, 1, 2),
    _GenEquipPmRadioTDMInterval_Type()
)
genEquipPmRadioTDMInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioTDMInterval.setStatus("mandatory")
_GenEquipPmRadioTDMRadioUAS_Type = Integer32
_GenEquipPmRadioTDMRadioUAS_Object = MibTableColumn
genEquipPmRadioTDMRadioUAS = _GenEquipPmRadioTDMRadioUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2, 1, 1, 3),
    _GenEquipPmRadioTDMRadioUAS_Type()
)
genEquipPmRadioTDMRadioUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioTDMRadioUAS.setStatus("mandatory")
_GenEquipPmRadioTDMIDF_Type = Integrity
_GenEquipPmRadioTDMIDF_Object = MibTableColumn
genEquipPmRadioTDMIDF = _GenEquipPmRadioTDMIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 2, 1, 1, 4),
    _GenEquipPmRadioTDMIDF_Type()
)
genEquipPmRadioTDMIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioTDMIDF.setStatus("mandatory")
_GenEquipPmRadioEthernet_ObjectIdentity = ObjectIdentity
genEquipPmRadioEthernet = _GenEquipPmRadioEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3)
)
_GenEquipPmRadioEthernetTable_Object = MibTable
genEquipPmRadioEthernetTable = _GenEquipPmRadioEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetTable.setStatus("mandatory")
_GenEquipPmRadioEthernetEntry_Object = MibTableRow
genEquipPmRadioEthernetEntry = _GenEquipPmRadioEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1)
)
genEquipPmRadioEthernetEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRadioEthernetPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioEthernetInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEntry.setStatus("mandatory")
_GenEquipPmRadioEthernetPmType_Type = PmTableType
_GenEquipPmRadioEthernetPmType_Object = MibTableColumn
genEquipPmRadioEthernetPmType = _GenEquipPmRadioEthernetPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 1),
    _GenEquipPmRadioEthernetPmType_Type()
)
genEquipPmRadioEthernetPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetPmType.setStatus("mandatory")
_GenEquipPmRadioEthernetInterval_Type = Integer32
_GenEquipPmRadioEthernetInterval_Object = MibTableColumn
genEquipPmRadioEthernetInterval = _GenEquipPmRadioEthernetInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 2),
    _GenEquipPmRadioEthernetInterval_Type()
)
genEquipPmRadioEthernetInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetInterval.setStatus("mandatory")
_GenEquipPmRadioEthernetFrameErrorRate_Type = Integer32
_GenEquipPmRadioEthernetFrameErrorRate_Object = MibTableColumn
genEquipPmRadioEthernetFrameErrorRate = _GenEquipPmRadioEthernetFrameErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 3),
    _GenEquipPmRadioEthernetFrameErrorRate_Type()
)
genEquipPmRadioEthernetFrameErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetFrameErrorRate.setStatus("mandatory")
_GenEquipPmRadioEthernetPeakThroughput_Type = Integer32
_GenEquipPmRadioEthernetPeakThroughput_Object = MibTableColumn
genEquipPmRadioEthernetPeakThroughput = _GenEquipPmRadioEthernetPeakThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 4),
    _GenEquipPmRadioEthernetPeakThroughput_Type()
)
genEquipPmRadioEthernetPeakThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetPeakThroughput.setStatus("mandatory")
_GenEquipPmRadioEthernetAverageThroughput_Type = Integer32
_GenEquipPmRadioEthernetAverageThroughput_Object = MibTableColumn
genEquipPmRadioEthernetAverageThroughput = _GenEquipPmRadioEthernetAverageThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 5),
    _GenEquipPmRadioEthernetAverageThroughput_Type()
)
genEquipPmRadioEthernetAverageThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetAverageThroughput.setStatus("mandatory")
_GenEquipPmRadioEthernetExceedThroughput_Type = Integer32
_GenEquipPmRadioEthernetExceedThroughput_Object = MibTableColumn
genEquipPmRadioEthernetExceedThroughput = _GenEquipPmRadioEthernetExceedThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 6),
    _GenEquipPmRadioEthernetExceedThroughput_Type()
)
genEquipPmRadioEthernetExceedThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetExceedThroughput.setStatus("mandatory")
_GenEquipPmRadioEthernetPeakCapacity_Type = Integer32
_GenEquipPmRadioEthernetPeakCapacity_Object = MibTableColumn
genEquipPmRadioEthernetPeakCapacity = _GenEquipPmRadioEthernetPeakCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 7),
    _GenEquipPmRadioEthernetPeakCapacity_Type()
)
genEquipPmRadioEthernetPeakCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetPeakCapacity.setStatus("mandatory")
_GenEquipPmRadioEthernetAverageCapacity_Type = Integer32
_GenEquipPmRadioEthernetAverageCapacity_Object = MibTableColumn
genEquipPmRadioEthernetAverageCapacity = _GenEquipPmRadioEthernetAverageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 8),
    _GenEquipPmRadioEthernetAverageCapacity_Type()
)
genEquipPmRadioEthernetAverageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetAverageCapacity.setStatus("mandatory")
_GenEquipPmRadioEthernetExceedCapacity_Type = Integer32
_GenEquipPmRadioEthernetExceedCapacity_Object = MibTableColumn
genEquipPmRadioEthernetExceedCapacity = _GenEquipPmRadioEthernetExceedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 9),
    _GenEquipPmRadioEthernetExceedCapacity_Type()
)
genEquipPmRadioEthernetExceedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetExceedCapacity.setStatus("mandatory")
_GenEquipPmRadioEthernetPeakUtilization_Type = Integer32
_GenEquipPmRadioEthernetPeakUtilization_Object = MibTableColumn
genEquipPmRadioEthernetPeakUtilization = _GenEquipPmRadioEthernetPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 10),
    _GenEquipPmRadioEthernetPeakUtilization_Type()
)
genEquipPmRadioEthernetPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetPeakUtilization.setStatus("mandatory")
_GenEquipPmRadioEthernetAverageUtilization_Type = Integer32
_GenEquipPmRadioEthernetAverageUtilization_Object = MibTableColumn
genEquipPmRadioEthernetAverageUtilization = _GenEquipPmRadioEthernetAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 11),
    _GenEquipPmRadioEthernetAverageUtilization_Type()
)
genEquipPmRadioEthernetAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetAverageUtilization.setStatus("mandatory")
_GenEquipPmRadioEthernetExceedUtilization_Type = Integer32
_GenEquipPmRadioEthernetExceedUtilization_Object = MibTableColumn
genEquipPmRadioEthernetExceedUtilization = _GenEquipPmRadioEthernetExceedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 12),
    _GenEquipPmRadioEthernetExceedUtilization_Type()
)
genEquipPmRadioEthernetExceedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetExceedUtilization.setStatus("mandatory")
_GenEquipPmRadioEthernetIDF_Type = Integrity
_GenEquipPmRadioEthernetIDF_Object = MibTableColumn
genEquipPmRadioEthernetIDF = _GenEquipPmRadioEthernetIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 1, 1, 13),
    _GenEquipPmRadioEthernetIDF_Type()
)
genEquipPmRadioEthernetIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetIDF.setStatus("mandatory")
_GenEquipPmRadioEthernetThresholdTable_Object = MibTable
genEquipPmRadioEthernetThresholdTable = _GenEquipPmRadioEthernetThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetThresholdTable.setStatus("mandatory")
_GenEquipPmRadioEthernetThresholdEntry_Object = MibTableRow
genEquipPmRadioEthernetThresholdEntry = _GenEquipPmRadioEthernetThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 2, 1)
)
genEquipPmRadioEthernetThresholdEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetThresholdEntry.setStatus("mandatory")


class _GenEquipPmRadioEthernetThresholdThroughput_Type(Integer32):
    """Custom type genEquipPmRadioEthernetThresholdThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_GenEquipPmRadioEthernetThresholdThroughput_Type.__name__ = "Integer32"
_GenEquipPmRadioEthernetThresholdThroughput_Object = MibTableColumn
genEquipPmRadioEthernetThresholdThroughput = _GenEquipPmRadioEthernetThresholdThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 2, 1, 1),
    _GenEquipPmRadioEthernetThresholdThroughput_Type()
)
genEquipPmRadioEthernetThresholdThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetThresholdThroughput.setStatus("mandatory")


class _GenEquipPmRadioEthernetThresholdCapacity_Type(Integer32):
    """Custom type genEquipPmRadioEthernetThresholdCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_GenEquipPmRadioEthernetThresholdCapacity_Type.__name__ = "Integer32"
_GenEquipPmRadioEthernetThresholdCapacity_Object = MibTableColumn
genEquipPmRadioEthernetThresholdCapacity = _GenEquipPmRadioEthernetThresholdCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 2, 1, 2),
    _GenEquipPmRadioEthernetThresholdCapacity_Type()
)
genEquipPmRadioEthernetThresholdCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetThresholdCapacity.setStatus("mandatory")


class _GenEquipPmRadioEthernetThresholdUtilization_Type(Integer32):
    """Custom type genEquipPmRadioEthernetThresholdUtilization based on Integer32"""
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
        *(("above-0", 0),
          ("above-20", 1),
          ("above-40", 2),
          ("above-60", 3),
          ("above-80", 4),
          ("no-threshold", 5))
    )


_GenEquipPmRadioEthernetThresholdUtilization_Type.__name__ = "Integer32"
_GenEquipPmRadioEthernetThresholdUtilization_Object = MibTableColumn
genEquipPmRadioEthernetThresholdUtilization = _GenEquipPmRadioEthernetThresholdUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 2, 1, 3),
    _GenEquipPmRadioEthernetThresholdUtilization_Type()
)
genEquipPmRadioEthernetThresholdUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetThresholdUtilization.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmTable_Object = MibTable
genEquipPmRadioEthernetEtmTable = _GenEquipPmRadioEthernetEtmTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3)
)
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmTable.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmEntry_Object = MibTableRow
genEquipPmRadioEthernetEtmEntry = _GenEquipPmRadioEthernetEtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1)
)
genEquipPmRadioEthernetEtmEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRadioEthernetEtmPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioEthernetEtmPmQueueIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioEthernetEtmInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmEntry.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmType_Type = PmTableType
_GenEquipPmRadioEthernetEtmPmType_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmType = _GenEquipPmRadioEthernetEtmPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 1),
    _GenEquipPmRadioEthernetEtmPmType_Type()
)
genEquipPmRadioEthernetEtmPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmType.setStatus("mandatory")


class _GenEquipPmRadioEthernetEtmPmQueueIndex_Type(Integer32):
    """Custom type genEquipPmRadioEthernetEtmPmQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GenEquipPmRadioEthernetEtmPmQueueIndex_Type.__name__ = "Integer32"
_GenEquipPmRadioEthernetEtmPmQueueIndex_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmQueueIndex = _GenEquipPmRadioEthernetEtmPmQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 2),
    _GenEquipPmRadioEthernetEtmPmQueueIndex_Type()
)
genEquipPmRadioEthernetEtmPmQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmQueueIndex.setStatus("mandatory")


class _GenEquipPmRadioEthernetEtmInterval_Type(Integer32):
    """Custom type genEquipPmRadioEthernetEtmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_GenEquipPmRadioEthernetEtmInterval_Type.__name__ = "Integer32"
_GenEquipPmRadioEthernetEtmInterval_Object = MibTableColumn
genEquipPmRadioEthernetEtmInterval = _GenEquipPmRadioEthernetEtmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 3),
    _GenEquipPmRadioEthernetEtmInterval_Type()
)
genEquipPmRadioEthernetEtmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmInterval.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxGreenBytesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxGreenBytesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxGreenBytesPassed = _GenEquipPmRadioEthernetEtmPmMaxGreenBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 4),
    _GenEquipPmRadioEthernetEtmPmMaxGreenBytesPassed_Type()
)
genEquipPmRadioEthernetEtmPmMaxGreenBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxGreenBytesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgGreenBytesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgGreenBytesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgGreenBytesPassed = _GenEquipPmRadioEthernetEtmPmAvgGreenBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 5),
    _GenEquipPmRadioEthernetEtmPmAvgGreenBytesPassed_Type()
)
genEquipPmRadioEthernetEtmPmAvgGreenBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgGreenBytesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxGreenFramesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxGreenFramesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxGreenFramesDropped = _GenEquipPmRadioEthernetEtmPmMaxGreenFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 6),
    _GenEquipPmRadioEthernetEtmPmMaxGreenFramesDropped_Type()
)
genEquipPmRadioEthernetEtmPmMaxGreenFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxGreenFramesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgGreenFramesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgGreenFramesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgGreenFramesDropped = _GenEquipPmRadioEthernetEtmPmAvgGreenFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 7),
    _GenEquipPmRadioEthernetEtmPmAvgGreenFramesDropped_Type()
)
genEquipPmRadioEthernetEtmPmAvgGreenFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgGreenFramesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxYellowBytesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxYellowBytesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxYellowBytesPassed = _GenEquipPmRadioEthernetEtmPmMaxYellowBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 8),
    _GenEquipPmRadioEthernetEtmPmMaxYellowBytesPassed_Type()
)
genEquipPmRadioEthernetEtmPmMaxYellowBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxYellowBytesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgYellowBytesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgYellowBytesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgYellowBytesPassed = _GenEquipPmRadioEthernetEtmPmAvgYellowBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 9),
    _GenEquipPmRadioEthernetEtmPmAvgYellowBytesPassed_Type()
)
genEquipPmRadioEthernetEtmPmAvgYellowBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgYellowBytesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxYellowFramesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxYellowFramesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxYellowFramesDropped = _GenEquipPmRadioEthernetEtmPmMaxYellowFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 10),
    _GenEquipPmRadioEthernetEtmPmMaxYellowFramesDropped_Type()
)
genEquipPmRadioEthernetEtmPmMaxYellowFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxYellowFramesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgYellowFramesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgYellowFramesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgYellowFramesDropped = _GenEquipPmRadioEthernetEtmPmAvgYellowFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 11),
    _GenEquipPmRadioEthernetEtmPmAvgYellowFramesDropped_Type()
)
genEquipPmRadioEthernetEtmPmAvgYellowFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgYellowFramesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxRedFramesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxRedFramesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxRedFramesDropped = _GenEquipPmRadioEthernetEtmPmMaxRedFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 12),
    _GenEquipPmRadioEthernetEtmPmMaxRedFramesDropped_Type()
)
genEquipPmRadioEthernetEtmPmMaxRedFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxRedFramesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgRedFramesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgRedFramesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgRedFramesDropped = _GenEquipPmRadioEthernetEtmPmAvgRedFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 13),
    _GenEquipPmRadioEthernetEtmPmAvgRedFramesDropped_Type()
)
genEquipPmRadioEthernetEtmPmAvgRedFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgRedFramesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmIDF_Type = Integrity
_GenEquipPmRadioEthernetEtmPmIDF_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmIDF = _GenEquipPmRadioEthernetEtmPmIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 14),
    _GenEquipPmRadioEthernetEtmPmIDF_Type()
)
genEquipPmRadioEthernetEtmPmIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmIDF.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxGreenFramesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxGreenFramesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxGreenFramesPassed = _GenEquipPmRadioEthernetEtmPmMaxGreenFramesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 17),
    _GenEquipPmRadioEthernetEtmPmMaxGreenFramesPassed_Type()
)
genEquipPmRadioEthernetEtmPmMaxGreenFramesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxGreenFramesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgGreenFramesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgGreenFramesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgGreenFramesPassed = _GenEquipPmRadioEthernetEtmPmAvgGreenFramesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 18),
    _GenEquipPmRadioEthernetEtmPmAvgGreenFramesPassed_Type()
)
genEquipPmRadioEthernetEtmPmAvgGreenFramesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgGreenFramesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxYellowFramesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxYellowFramesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxYellowFramesPassed = _GenEquipPmRadioEthernetEtmPmMaxYellowFramesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 21),
    _GenEquipPmRadioEthernetEtmPmMaxYellowFramesPassed_Type()
)
genEquipPmRadioEthernetEtmPmMaxYellowFramesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxYellowFramesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgYellowFramesPassed_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgYellowFramesPassed_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgYellowFramesPassed = _GenEquipPmRadioEthernetEtmPmAvgYellowFramesPassed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 22),
    _GenEquipPmRadioEthernetEtmPmAvgYellowFramesPassed_Type()
)
genEquipPmRadioEthernetEtmPmAvgYellowFramesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgYellowFramesPassed.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmMaxRedBytesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmMaxRedBytesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmMaxRedBytesDropped = _GenEquipPmRadioEthernetEtmPmMaxRedBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 23),
    _GenEquipPmRadioEthernetEtmPmMaxRedBytesDropped_Type()
)
genEquipPmRadioEthernetEtmPmMaxRedBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmMaxRedBytesDropped.setStatus("mandatory")
_GenEquipPmRadioEthernetEtmPmAvgRedBytesDropped_Type = Integer32
_GenEquipPmRadioEthernetEtmPmAvgRedBytesDropped_Object = MibTableColumn
genEquipPmRadioEthernetEtmPmAvgRedBytesDropped = _GenEquipPmRadioEthernetEtmPmAvgRedBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 3, 3, 1, 24),
    _GenEquipPmRadioEthernetEtmPmAvgRedBytesDropped_Type()
)
genEquipPmRadioEthernetEtmPmAvgRedBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioEthernetEtmPmAvgRedBytesDropped.setStatus("mandatory")
_GenEquipPmRadioMSETable_Object = MibTable
genEquipPmRadioMSETable = _GenEquipPmRadioMSETable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4)
)
if mibBuilder.loadTexts:
    genEquipPmRadioMSETable.setStatus("mandatory")
_GenEquipPmRadioMSEEntry_Object = MibTableRow
genEquipPmRadioMSEEntry = _GenEquipPmRadioMSEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1)
)
genEquipPmRadioMSEEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRadioMSEPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioMSEInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioMSEEntry.setStatus("mandatory")
_GenEquipPmRadioMSEPmType_Type = PmTableType
_GenEquipPmRadioMSEPmType_Object = MibTableColumn
genEquipPmRadioMSEPmType = _GenEquipPmRadioMSEPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1, 1),
    _GenEquipPmRadioMSEPmType_Type()
)
genEquipPmRadioMSEPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMSEPmType.setStatus("mandatory")
_GenEquipPmRadioMSEInterval_Type = Integer32
_GenEquipPmRadioMSEInterval_Object = MibTableColumn
genEquipPmRadioMSEInterval = _GenEquipPmRadioMSEInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1, 2),
    _GenEquipPmRadioMSEInterval_Type()
)
genEquipPmRadioMSEInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMSEInterval.setStatus("mandatory")
_GenEquipPmRadioMSEMinMse_Type = Integer32
_GenEquipPmRadioMSEMinMse_Object = MibTableColumn
genEquipPmRadioMSEMinMse = _GenEquipPmRadioMSEMinMse_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1, 3),
    _GenEquipPmRadioMSEMinMse_Type()
)
genEquipPmRadioMSEMinMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMSEMinMse.setStatus("mandatory")
_GenEquipPmRadioMSEMaxMse_Type = Integer32
_GenEquipPmRadioMSEMaxMse_Object = MibTableColumn
genEquipPmRadioMSEMaxMse = _GenEquipPmRadioMSEMaxMse_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1, 4),
    _GenEquipPmRadioMSEMaxMse_Type()
)
genEquipPmRadioMSEMaxMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMSEMaxMse.setStatus("mandatory")
_GenEquipPmRadioMSEexceeded_Type = Integer32
_GenEquipPmRadioMSEexceeded_Object = MibTableColumn
genEquipPmRadioMSEexceeded = _GenEquipPmRadioMSEexceeded_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1, 5),
    _GenEquipPmRadioMSEexceeded_Type()
)
genEquipPmRadioMSEexceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMSEexceeded.setStatus("mandatory")
_GenEquipPmRadioMSEIDF_Type = Integrity
_GenEquipPmRadioMSEIDF_Object = MibTableColumn
genEquipPmRadioMSEIDF = _GenEquipPmRadioMSEIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 4, 1, 6),
    _GenEquipPmRadioMSEIDF_Type()
)
genEquipPmRadioMSEIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioMSEIDF.setStatus("mandatory")
_GenEquipPmRadioThresholdTable_Object = MibTable
genEquipPmRadioThresholdTable = _GenEquipPmRadioThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5)
)
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdTable.setStatus("mandatory")
_GenEquipPmRadioThresholdEntry_Object = MibTableRow
genEquipPmRadioThresholdEntry = _GenEquipPmRadioThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5, 1)
)
genEquipPmRadioThresholdEntry.setIndexNames(
    (0, "MWRM-RADIO-MIB", "genEquipRadioCfgRadioId"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdEntry.setStatus("mandatory")


class _GenEquipPmRadioThresholdMSE_Type(Integer32):
    """Custom type genEquipPmRadioThresholdMSE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -1),
    )


_GenEquipPmRadioThresholdMSE_Type.__name__ = "Integer32"
_GenEquipPmRadioThresholdMSE_Object = MibTableColumn
genEquipPmRadioThresholdMSE = _GenEquipPmRadioThresholdMSE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5, 1, 1),
    _GenEquipPmRadioThresholdMSE_Type()
)
genEquipPmRadioThresholdMSE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdMSE.setStatus("mandatory")


class _GenEquipPmRadioThresholdRSL1_Type(Integer32):
    """Custom type genEquipPmRadioThresholdRSL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, -15),
    )


_GenEquipPmRadioThresholdRSL1_Type.__name__ = "Integer32"
_GenEquipPmRadioThresholdRSL1_Object = MibTableColumn
genEquipPmRadioThresholdRSL1 = _GenEquipPmRadioThresholdRSL1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5, 1, 2),
    _GenEquipPmRadioThresholdRSL1_Type()
)
genEquipPmRadioThresholdRSL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdRSL1.setStatus("mandatory")


class _GenEquipPmRadioThresholdRSL2_Type(Integer32):
    """Custom type genEquipPmRadioThresholdRSL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, -15),
    )


_GenEquipPmRadioThresholdRSL2_Type.__name__ = "Integer32"
_GenEquipPmRadioThresholdRSL2_Object = MibTableColumn
genEquipPmRadioThresholdRSL2 = _GenEquipPmRadioThresholdRSL2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5, 1, 3),
    _GenEquipPmRadioThresholdRSL2_Type()
)
genEquipPmRadioThresholdRSL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdRSL2.setStatus("mandatory")
_GenEquipPmRadioThresholdTSL_Type = Integer32
_GenEquipPmRadioThresholdTSL_Object = MibTableColumn
genEquipPmRadioThresholdTSL = _GenEquipPmRadioThresholdTSL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5, 1, 4),
    _GenEquipPmRadioThresholdTSL_Type()
)
genEquipPmRadioThresholdTSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdTSL.setStatus("mandatory")


class _GenEquipPmRadioThresholdXPI_Type(Integer32):
    """Custom type genEquipPmRadioThresholdXPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GenEquipPmRadioThresholdXPI_Type.__name__ = "Integer32"
_GenEquipPmRadioThresholdXPI_Object = MibTableColumn
genEquipPmRadioThresholdXPI = _GenEquipPmRadioThresholdXPI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 5, 1, 5),
    _GenEquipPmRadioThresholdXPI_Type()
)
genEquipPmRadioThresholdXPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioThresholdXPI.setStatus("mandatory")
_GenEquipPmRadioXPITable_Object = MibTable
genEquipPmRadioXPITable = _GenEquipPmRadioXPITable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6)
)
if mibBuilder.loadTexts:
    genEquipPmRadioXPITable.setStatus("mandatory")
_GenEquipPmRadioXPIEntry_Object = MibTableRow
genEquipPmRadioXPIEntry = _GenEquipPmRadioXPIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1)
)
genEquipPmRadioXPIEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmRadioXPIPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmRadioXPIPmInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmRadioXPIEntry.setStatus("mandatory")
_GenEquipPmRadioXPIPmType_Type = PmTableType
_GenEquipPmRadioXPIPmType_Object = MibTableColumn
genEquipPmRadioXPIPmType = _GenEquipPmRadioXPIPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1, 1),
    _GenEquipPmRadioXPIPmType_Type()
)
genEquipPmRadioXPIPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioXPIPmType.setStatus("mandatory")
_GenEquipPmRadioXPIPmInterval_Type = Integer32
_GenEquipPmRadioXPIPmInterval_Object = MibTableColumn
genEquipPmRadioXPIPmInterval = _GenEquipPmRadioXPIPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1, 2),
    _GenEquipPmRadioXPIPmInterval_Type()
)
genEquipPmRadioXPIPmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioXPIPmInterval.setStatus("mandatory")
_GenEquipPmRadioXPIPmMinXPI_Type = Integer32
_GenEquipPmRadioXPIPmMinXPI_Object = MibTableColumn
genEquipPmRadioXPIPmMinXPI = _GenEquipPmRadioXPIPmMinXPI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1, 3),
    _GenEquipPmRadioXPIPmMinXPI_Type()
)
genEquipPmRadioXPIPmMinXPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioXPIPmMinXPI.setStatus("mandatory")
_GenEquipPmRadioXPIPmMaxXPI_Type = Integer32
_GenEquipPmRadioXPIPmMaxXPI_Object = MibTableColumn
genEquipPmRadioXPIPmMaxXPI = _GenEquipPmRadioXPIPmMaxXPI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1, 4),
    _GenEquipPmRadioXPIPmMaxXPI_Type()
)
genEquipPmRadioXPIPmMaxXPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioXPIPmMaxXPI.setStatus("mandatory")
_GenEquipPmRadioXPIBelowThreshold_Type = Integer32
_GenEquipPmRadioXPIBelowThreshold_Object = MibTableColumn
genEquipPmRadioXPIBelowThreshold = _GenEquipPmRadioXPIBelowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1, 5),
    _GenEquipPmRadioXPIBelowThreshold_Type()
)
genEquipPmRadioXPIBelowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioXPIBelowThreshold.setStatus("mandatory")
_GenEquipPmRadioXPIIDF_Type = Integrity
_GenEquipPmRadioXPIIDF_Object = MibTableColumn
genEquipPmRadioXPIIDF = _GenEquipPmRadioXPIIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 6, 1, 6),
    _GenEquipPmRadioXPIIDF_Type()
)
genEquipPmRadioXPIIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmRadioXPIIDF.setStatus("mandatory")
_GenEquipPmRadioClear_Type = OffOn
_GenEquipPmRadioClear_Object = MibScalar
genEquipPmRadioClear = _GenEquipPmRadioClear_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 4, 7),
    _GenEquipPmRadioClear_Type()
)
genEquipPmRadioClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmRadioClear.setStatus("mandatory")
_GenEquipPmTDM_ObjectIdentity = ObjectIdentity
genEquipPmTDM = _GenEquipPmTDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5)
)
_GenEquipPmTdmTable_Object = MibTable
genEquipPmTdmTable = _GenEquipPmTdmTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1)
)
if mibBuilder.loadTexts:
    genEquipPmTdmTable.setStatus("mandatory")
_GenEquipPmTdmEntry_Object = MibTableRow
genEquipPmTdmEntry = _GenEquipPmTdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1)
)
genEquipPmTdmEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTdmPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmTdmInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmTdmEntry.setStatus("mandatory")
_GenEquipPmTdmPmType_Type = PmTableType
_GenEquipPmTdmPmType_Object = MibTableColumn
genEquipPmTdmPmType = _GenEquipPmTdmPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 1),
    _GenEquipPmTdmPmType_Type()
)
genEquipPmTdmPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmPmType.setStatus("mandatory")
_GenEquipPmTdmInterval_Type = Integer32
_GenEquipPmTdmInterval_Object = MibTableColumn
genEquipPmTdmInterval = _GenEquipPmTdmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 2),
    _GenEquipPmTdmInterval_Type()
)
genEquipPmTdmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmInterval.setStatus("mandatory")
_GenEquipPmTdmES_Type = Integer32
_GenEquipPmTdmES_Object = MibTableColumn
genEquipPmTdmES = _GenEquipPmTdmES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 3),
    _GenEquipPmTdmES_Type()
)
genEquipPmTdmES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmES.setStatus("mandatory")
_GenEquipPmTdmSES_Type = Integer32
_GenEquipPmTdmSES_Object = MibTableColumn
genEquipPmTdmSES = _GenEquipPmTdmSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 4),
    _GenEquipPmTdmSES_Type()
)
genEquipPmTdmSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmSES.setStatus("mandatory")
_GenEquipPmTdmUAS_Type = Integer32
_GenEquipPmTdmUAS_Object = MibTableColumn
genEquipPmTdmUAS = _GenEquipPmTdmUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 5),
    _GenEquipPmTdmUAS_Type()
)
genEquipPmTdmUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmUAS.setStatus("mandatory")
_GenEquipPmTdmBBE_Type = Integer32
_GenEquipPmTdmBBE_Object = MibTableColumn
genEquipPmTdmBBE = _GenEquipPmTdmBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 6),
    _GenEquipPmTdmBBE_Type()
)
genEquipPmTdmBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmBBE.setStatus("mandatory")
_GenEquipPmTdmIDF_Type = Integrity
_GenEquipPmTdmIDF_Object = MibTableColumn
genEquipPmTdmIDF = _GenEquipPmTdmIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 5, 1, 1, 7),
    _GenEquipPmTdmIDF_Type()
)
genEquipPmTdmIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTdmIDF.setStatus("mandatory")
_GenEquipPmSDH_ObjectIdentity = ObjectIdentity
genEquipPmSDH = _GenEquipPmSDH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6)
)
_GenEquipPmSdhTable_Object = MibTable
genEquipPmSdhTable = _GenEquipPmSdhTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1)
)
if mibBuilder.loadTexts:
    genEquipPmSdhTable.setStatus("mandatory")
_GenEquipPmSdhEntry_Object = MibTableRow
genEquipPmSdhEntry = _GenEquipPmSdhEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1)
)
genEquipPmSdhEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmSdhPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmSdhInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmSdhEntry.setStatus("mandatory")
_GenEquipPmSdhPmType_Type = PmTableType
_GenEquipPmSdhPmType_Object = MibTableColumn
genEquipPmSdhPmType = _GenEquipPmSdhPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 1),
    _GenEquipPmSdhPmType_Type()
)
genEquipPmSdhPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhPmType.setStatus("mandatory")
_GenEquipPmSdhInterval_Type = Integer32
_GenEquipPmSdhInterval_Object = MibTableColumn
genEquipPmSdhInterval = _GenEquipPmSdhInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 2),
    _GenEquipPmSdhInterval_Type()
)
genEquipPmSdhInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhInterval.setStatus("mandatory")
_GenEquipPmSdhES_Type = Integer32
_GenEquipPmSdhES_Object = MibTableColumn
genEquipPmSdhES = _GenEquipPmSdhES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 3),
    _GenEquipPmSdhES_Type()
)
genEquipPmSdhES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhES.setStatus("mandatory")
_GenEquipPmSdhSES_Type = Integer32
_GenEquipPmSdhSES_Object = MibTableColumn
genEquipPmSdhSES = _GenEquipPmSdhSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 4),
    _GenEquipPmSdhSES_Type()
)
genEquipPmSdhSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhSES.setStatus("mandatory")
_GenEquipPmSdhEB_Type = Integer32
_GenEquipPmSdhEB_Object = MibTableColumn
genEquipPmSdhEB = _GenEquipPmSdhEB_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 5),
    _GenEquipPmSdhEB_Type()
)
genEquipPmSdhEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhEB.setStatus("mandatory")
_GenEquipPmSdhBBE_Type = Integer32
_GenEquipPmSdhBBE_Object = MibTableColumn
genEquipPmSdhBBE = _GenEquipPmSdhBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 6),
    _GenEquipPmSdhBBE_Type()
)
genEquipPmSdhBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhBBE.setStatus("mandatory")
_GenEquipPmSdhIDF_Type = Integrity
_GenEquipPmSdhIDF_Object = MibTableColumn
genEquipPmSdhIDF = _GenEquipPmSdhIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 7),
    _GenEquipPmSdhIDF_Type()
)
genEquipPmSdhIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhIDF.setStatus("mandatory")
_GenEquipPmSdhIfIndex_Type = Integer32
_GenEquipPmSdhIfIndex_Object = MibTableColumn
genEquipPmSdhIfIndex = _GenEquipPmSdhIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 8),
    _GenEquipPmSdhIfIndex_Type()
)
genEquipPmSdhIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhIfIndex.setStatus("mandatory")
_GenEquipPmSdhTimeStamp_Type = Integer32
_GenEquipPmSdhTimeStamp_Object = MibTableColumn
genEquipPmSdhTimeStamp = _GenEquipPmSdhTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 9),
    _GenEquipPmSdhTimeStamp_Type()
)
genEquipPmSdhTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhTimeStamp.setStatus("mandatory")
_GenEquipPmSdhUAS_Type = Integer32
_GenEquipPmSdhUAS_Object = MibTableColumn
genEquipPmSdhUAS = _GenEquipPmSdhUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 1, 1, 10),
    _GenEquipPmSdhUAS_Type()
)
genEquipPmSdhUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhUAS.setStatus("mandatory")
_GenEquipPmSdhRstLRTable_Object = MibTable
genEquipPmSdhRstLRTable = _GenEquipPmSdhRstLRTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2)
)
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRTable.setStatus("mandatory")
_GenEquipPmSdhRstLREntry_Object = MibTableRow
genEquipPmSdhRstLREntry = _GenEquipPmSdhRstLREntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1)
)
genEquipPmSdhRstLREntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmSdhRstLRPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmSdhRstLRIfIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmSdhRstLRInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmSdhRstLREntry.setStatus("mandatory")
_GenEquipPmSdhRstLRPmType_Type = PmTableType
_GenEquipPmSdhRstLRPmType_Object = MibTableColumn
genEquipPmSdhRstLRPmType = _GenEquipPmSdhRstLRPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 1),
    _GenEquipPmSdhRstLRPmType_Type()
)
genEquipPmSdhRstLRPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRPmType.setStatus("mandatory")
_GenEquipPmSdhRstLRIfIndex_Type = Integer32
_GenEquipPmSdhRstLRIfIndex_Object = MibTableColumn
genEquipPmSdhRstLRIfIndex = _GenEquipPmSdhRstLRIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 2),
    _GenEquipPmSdhRstLRIfIndex_Type()
)
genEquipPmSdhRstLRIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRIfIndex.setStatus("mandatory")
_GenEquipPmSdhRstLRInterval_Type = Integer32
_GenEquipPmSdhRstLRInterval_Object = MibTableColumn
genEquipPmSdhRstLRInterval = _GenEquipPmSdhRstLRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 3),
    _GenEquipPmSdhRstLRInterval_Type()
)
genEquipPmSdhRstLRInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRInterval.setStatus("mandatory")
_GenEquipPmSdhRstLRTimeStamp_Type = Integer32
_GenEquipPmSdhRstLRTimeStamp_Object = MibTableColumn
genEquipPmSdhRstLRTimeStamp = _GenEquipPmSdhRstLRTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 4),
    _GenEquipPmSdhRstLRTimeStamp_Type()
)
genEquipPmSdhRstLRTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRTimeStamp.setStatus("mandatory")
_GenEquipPmSdhRstLRES_Type = Integer32
_GenEquipPmSdhRstLRES_Object = MibTableColumn
genEquipPmSdhRstLRES = _GenEquipPmSdhRstLRES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 5),
    _GenEquipPmSdhRstLRES_Type()
)
genEquipPmSdhRstLRES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRES.setStatus("mandatory")
_GenEquipPmSdhRstLRSES_Type = Integer32
_GenEquipPmSdhRstLRSES_Object = MibTableColumn
genEquipPmSdhRstLRSES = _GenEquipPmSdhRstLRSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 6),
    _GenEquipPmSdhRstLRSES_Type()
)
genEquipPmSdhRstLRSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRSES.setStatus("mandatory")
_GenEquipPmSdhRstLRUAS_Type = Integer32
_GenEquipPmSdhRstLRUAS_Object = MibTableColumn
genEquipPmSdhRstLRUAS = _GenEquipPmSdhRstLRUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 7),
    _GenEquipPmSdhRstLRUAS_Type()
)
genEquipPmSdhRstLRUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRUAS.setStatus("mandatory")
_GenEquipPmSdhRstLREB_Type = Integer32
_GenEquipPmSdhRstLREB_Object = MibTableColumn
genEquipPmSdhRstLREB = _GenEquipPmSdhRstLREB_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 8),
    _GenEquipPmSdhRstLREB_Type()
)
genEquipPmSdhRstLREB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLREB.setStatus("mandatory")
_GenEquipPmSdhRstLRCV_Type = Integer32
_GenEquipPmSdhRstLRCV_Object = MibTableColumn
genEquipPmSdhRstLRCV = _GenEquipPmSdhRstLRCV_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 9),
    _GenEquipPmSdhRstLRCV_Type()
)
genEquipPmSdhRstLRCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRCV.setStatus("mandatory")
_GenEquipPmSdhRstLRBBE_Type = Integer32
_GenEquipPmSdhRstLRBBE_Object = MibTableColumn
genEquipPmSdhRstLRBBE = _GenEquipPmSdhRstLRBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 10),
    _GenEquipPmSdhRstLRBBE_Type()
)
genEquipPmSdhRstLRBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRBBE.setStatus("mandatory")
_GenEquipPmSdhRstLRIDF_Type = Integrity
_GenEquipPmSdhRstLRIDF_Object = MibTableColumn
genEquipPmSdhRstLRIDF = _GenEquipPmSdhRstLRIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 2, 1, 11),
    _GenEquipPmSdhRstLRIDF_Type()
)
genEquipPmSdhRstLRIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstLRIDF.setStatus("mandatory")
_GenEquipPmSdhRstRLTable_Object = MibTable
genEquipPmSdhRstRLTable = _GenEquipPmSdhRstRLTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3)
)
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLTable.setStatus("mandatory")
_GenEquipPmSdhRstRLEntry_Object = MibTableRow
genEquipPmSdhRstRLEntry = _GenEquipPmSdhRstRLEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1)
)
genEquipPmSdhRstRLEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmSdhRstRLPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmSdhRstRLIfIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmSdhRstRLInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLEntry.setStatus("mandatory")
_GenEquipPmSdhRstRLPmType_Type = PmTableType
_GenEquipPmSdhRstRLPmType_Object = MibTableColumn
genEquipPmSdhRstRLPmType = _GenEquipPmSdhRstRLPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 1),
    _GenEquipPmSdhRstRLPmType_Type()
)
genEquipPmSdhRstRLPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLPmType.setStatus("mandatory")
_GenEquipPmSdhRstRLIfIndex_Type = Integer32
_GenEquipPmSdhRstRLIfIndex_Object = MibTableColumn
genEquipPmSdhRstRLIfIndex = _GenEquipPmSdhRstRLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 2),
    _GenEquipPmSdhRstRLIfIndex_Type()
)
genEquipPmSdhRstRLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLIfIndex.setStatus("mandatory")
_GenEquipPmSdhRstRLInterval_Type = Integer32
_GenEquipPmSdhRstRLInterval_Object = MibTableColumn
genEquipPmSdhRstRLInterval = _GenEquipPmSdhRstRLInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 3),
    _GenEquipPmSdhRstRLInterval_Type()
)
genEquipPmSdhRstRLInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLInterval.setStatus("mandatory")
_GenEquipPmSdhRstRLTimeStamp_Type = Integer32
_GenEquipPmSdhRstRLTimeStamp_Object = MibTableColumn
genEquipPmSdhRstRLTimeStamp = _GenEquipPmSdhRstRLTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 4),
    _GenEquipPmSdhRstRLTimeStamp_Type()
)
genEquipPmSdhRstRLTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLTimeStamp.setStatus("mandatory")
_GenEquipPmSdhRstRLES_Type = Integer32
_GenEquipPmSdhRstRLES_Object = MibTableColumn
genEquipPmSdhRstRLES = _GenEquipPmSdhRstRLES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 5),
    _GenEquipPmSdhRstRLES_Type()
)
genEquipPmSdhRstRLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLES.setStatus("mandatory")
_GenEquipPmSdhRstRLSES_Type = Integer32
_GenEquipPmSdhRstRLSES_Object = MibTableColumn
genEquipPmSdhRstRLSES = _GenEquipPmSdhRstRLSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 6),
    _GenEquipPmSdhRstRLSES_Type()
)
genEquipPmSdhRstRLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLSES.setStatus("mandatory")
_GenEquipPmSdhRstRLUAS_Type = Integer32
_GenEquipPmSdhRstRLUAS_Object = MibTableColumn
genEquipPmSdhRstRLUAS = _GenEquipPmSdhRstRLUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 7),
    _GenEquipPmSdhRstRLUAS_Type()
)
genEquipPmSdhRstRLUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLUAS.setStatus("mandatory")
_GenEquipPmSdhRstRLEB_Type = Integer32
_GenEquipPmSdhRstRLEB_Object = MibTableColumn
genEquipPmSdhRstRLEB = _GenEquipPmSdhRstRLEB_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 8),
    _GenEquipPmSdhRstRLEB_Type()
)
genEquipPmSdhRstRLEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLEB.setStatus("mandatory")
_GenEquipPmSdhRstRLCV_Type = Integer32
_GenEquipPmSdhRstRLCV_Object = MibTableColumn
genEquipPmSdhRstRLCV = _GenEquipPmSdhRstRLCV_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 9),
    _GenEquipPmSdhRstRLCV_Type()
)
genEquipPmSdhRstRLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLCV.setStatus("mandatory")
_GenEquipPmSdhRstRLBBE_Type = Integer32
_GenEquipPmSdhRstRLBBE_Object = MibTableColumn
genEquipPmSdhRstRLBBE = _GenEquipPmSdhRstRLBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 10),
    _GenEquipPmSdhRstRLBBE_Type()
)
genEquipPmSdhRstRLBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLBBE.setStatus("mandatory")
_GenEquipPmSdhRstRLIDF_Type = Integrity
_GenEquipPmSdhRstRLIDF_Object = MibTableColumn
genEquipPmSdhRstRLIDF = _GenEquipPmSdhRstRLIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 6, 3, 1, 11),
    _GenEquipPmSdhRstRLIDF_Type()
)
genEquipPmSdhRstRLIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmSdhRstRLIDF.setStatus("mandatory")
_GenEquipPmTrails_ObjectIdentity = ObjectIdentity
genEquipPmTrails = _GenEquipPmTrails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7)
)
_GenEquipPmTrailsEndPointTable_Object = MibTable
genEquipPmTrailsEndPointTable = _GenEquipPmTrailsEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1)
)
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointTable.setStatus("mandatory")
_GenEquipPmTrailsEndPointEntry_Object = MibTableRow
genEquipPmTrailsEndPointEntry = _GenEquipPmTrailsEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1)
)
genEquipPmTrailsEndPointEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmTrailsEndPointPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmTrailsEndPointId"),
    (0, "MWRM-PM-MIB", "genEquipPmTrailsEndPointEPId"),
    (0, "MWRM-PM-MIB", "genEquipPmTrailsEndPointInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointEntry.setStatus("mandatory")
_GenEquipPmTrailsEndPointPmType_Type = PmTableType
_GenEquipPmTrailsEndPointPmType_Object = MibTableColumn
genEquipPmTrailsEndPointPmType = _GenEquipPmTrailsEndPointPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 1),
    _GenEquipPmTrailsEndPointPmType_Type()
)
genEquipPmTrailsEndPointPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointPmType.setStatus("mandatory")
_GenEquipPmTrailsEndPointId_Type = DisplayString
_GenEquipPmTrailsEndPointId_Object = MibTableColumn
genEquipPmTrailsEndPointId = _GenEquipPmTrailsEndPointId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 2),
    _GenEquipPmTrailsEndPointId_Type()
)
genEquipPmTrailsEndPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointId.setStatus("mandatory")
_GenEquipPmTrailsEndPointEPId_Type = Integer32
_GenEquipPmTrailsEndPointEPId_Object = MibTableColumn
genEquipPmTrailsEndPointEPId = _GenEquipPmTrailsEndPointEPId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 3),
    _GenEquipPmTrailsEndPointEPId_Type()
)
genEquipPmTrailsEndPointEPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointEPId.setStatus("mandatory")
_GenEquipPmTrailsEndPointInterval_Type = Integer32
_GenEquipPmTrailsEndPointInterval_Object = MibTableColumn
genEquipPmTrailsEndPointInterval = _GenEquipPmTrailsEndPointInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 4),
    _GenEquipPmTrailsEndPointInterval_Type()
)
genEquipPmTrailsEndPointInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointInterval.setStatus("mandatory")
_GenEquipPmTrailsEndPointES_Type = Integer32
_GenEquipPmTrailsEndPointES_Object = MibTableColumn
genEquipPmTrailsEndPointES = _GenEquipPmTrailsEndPointES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 5),
    _GenEquipPmTrailsEndPointES_Type()
)
genEquipPmTrailsEndPointES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointES.setStatus("mandatory")
_GenEquipPmTrailsEndPointSES_Type = Integer32
_GenEquipPmTrailsEndPointSES_Object = MibTableColumn
genEquipPmTrailsEndPointSES = _GenEquipPmTrailsEndPointSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 6),
    _GenEquipPmTrailsEndPointSES_Type()
)
genEquipPmTrailsEndPointSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointSES.setStatus("mandatory")
_GenEquipPmTrailsEndPointUAS_Type = Integer32
_GenEquipPmTrailsEndPointUAS_Object = MibTableColumn
genEquipPmTrailsEndPointUAS = _GenEquipPmTrailsEndPointUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 7),
    _GenEquipPmTrailsEndPointUAS_Type()
)
genEquipPmTrailsEndPointUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointUAS.setStatus("mandatory")
_GenEquipPmTrailsEndPointBBE_Type = Integer32
_GenEquipPmTrailsEndPointBBE_Object = MibTableColumn
genEquipPmTrailsEndPointBBE = _GenEquipPmTrailsEndPointBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 8),
    _GenEquipPmTrailsEndPointBBE_Type()
)
genEquipPmTrailsEndPointBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointBBE.setStatus("mandatory")
_GenEquipPmTrailsEndPointNoOfSwitches_Type = Integer32
_GenEquipPmTrailsEndPointNoOfSwitches_Object = MibTableColumn
genEquipPmTrailsEndPointNoOfSwitches = _GenEquipPmTrailsEndPointNoOfSwitches_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 9),
    _GenEquipPmTrailsEndPointNoOfSwitches_Type()
)
genEquipPmTrailsEndPointNoOfSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointNoOfSwitches.setStatus("mandatory")
_GenEquipPmTrailsEndPointActivePathCounts_Type = Integer32
_GenEquipPmTrailsEndPointActivePathCounts_Object = MibTableColumn
genEquipPmTrailsEndPointActivePathCounts = _GenEquipPmTrailsEndPointActivePathCounts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 10),
    _GenEquipPmTrailsEndPointActivePathCounts_Type()
)
genEquipPmTrailsEndPointActivePathCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointActivePathCounts.setStatus("mandatory")
_GenEquipPmTrailsEndPointIDF_Type = Integrity
_GenEquipPmTrailsEndPointIDF_Object = MibTableColumn
genEquipPmTrailsEndPointIDF = _GenEquipPmTrailsEndPointIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 7, 1, 1, 11),
    _GenEquipPmTrailsEndPointIDF_Type()
)
genEquipPmTrailsEndPointIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmTrailsEndPointIDF.setStatus("mandatory")
_GenEquipPmPW_ObjectIdentity = ObjectIdentity
genEquipPmPW = _GenEquipPmPW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8)
)
_GenEquipPmPWTable_Object = MibTable
genEquipPmPWTable = _GenEquipPmPWTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1)
)
if mibBuilder.loadTexts:
    genEquipPmPWTable.setStatus("mandatory")
_GenEquipPmPWEntry_Object = MibTableRow
genEquipPmPWEntry = _GenEquipPmPWEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1)
)
genEquipPmPWEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmPWPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmPWId"),
    (0, "MWRM-PM-MIB", "genEquipPmPWInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmPWEntry.setStatus("mandatory")
_GenEquipPmPWPmType_Type = PmTableType
_GenEquipPmPWPmType_Object = MibTableColumn
genEquipPmPWPmType = _GenEquipPmPWPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 1),
    _GenEquipPmPWPmType_Type()
)
genEquipPmPWPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWPmType.setStatus("mandatory")
_GenEquipPmPWId_Type = Integer32
_GenEquipPmPWId_Object = MibTableColumn
genEquipPmPWId = _GenEquipPmPWId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 2),
    _GenEquipPmPWId_Type()
)
genEquipPmPWId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWId.setStatus("mandatory")
_GenEquipPmPWInterval_Type = Integer32
_GenEquipPmPWInterval_Object = MibTableColumn
genEquipPmPWInterval = _GenEquipPmPWInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 3),
    _GenEquipPmPWInterval_Type()
)
genEquipPmPWInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWInterval.setStatus("mandatory")
_GenEquipPmPWMissingPkts_Type = Integer32
_GenEquipPmPWMissingPkts_Object = MibTableColumn
genEquipPmPWMissingPkts = _GenEquipPmPWMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 4),
    _GenEquipPmPWMissingPkts_Type()
)
genEquipPmPWMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWMissingPkts.setStatus("mandatory")
_GenEquipPmPWPktsReOrder_Type = Integer32
_GenEquipPmPWPktsReOrder_Object = MibTableColumn
genEquipPmPWPktsReOrder = _GenEquipPmPWPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 5),
    _GenEquipPmPWPktsReOrder_Type()
)
genEquipPmPWPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWPktsReOrder.setStatus("mandatory")
_GenEquipPmPWtrBfrUnderruns_Type = Integer32
_GenEquipPmPWtrBfrUnderruns_Object = MibTableColumn
genEquipPmPWtrBfrUnderruns = _GenEquipPmPWtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 6),
    _GenEquipPmPWtrBfrUnderruns_Type()
)
genEquipPmPWtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWtrBfrUnderruns.setStatus("mandatory")
_GenEquipPmPWMisOrderDropped_Type = Integer32
_GenEquipPmPWMisOrderDropped_Object = MibTableColumn
genEquipPmPWMisOrderDropped = _GenEquipPmPWMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 7),
    _GenEquipPmPWMisOrderDropped_Type()
)
genEquipPmPWMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWMisOrderDropped.setStatus("mandatory")
_GenEquipPmPWMalformedPkt_Type = Integer32
_GenEquipPmPWMalformedPkt_Object = MibTableColumn
genEquipPmPWMalformedPkt = _GenEquipPmPWMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 8),
    _GenEquipPmPWMalformedPkt_Type()
)
genEquipPmPWMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWMalformedPkt.setStatus("mandatory")
_GenEquipPmPWES_Type = Integer32
_GenEquipPmPWES_Object = MibTableColumn
genEquipPmPWES = _GenEquipPmPWES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 9),
    _GenEquipPmPWES_Type()
)
genEquipPmPWES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWES.setStatus("mandatory")
_GenEquipPmPWSES_Type = Integer32
_GenEquipPmPWSES_Object = MibTableColumn
genEquipPmPWSES = _GenEquipPmPWSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 10),
    _GenEquipPmPWSES_Type()
)
genEquipPmPWSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWSES.setStatus("mandatory")
_GenEquipPmPWUAS_Type = Integer32
_GenEquipPmPWUAS_Object = MibTableColumn
genEquipPmPWUAS = _GenEquipPmPWUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 11),
    _GenEquipPmPWUAS_Type()
)
genEquipPmPWUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWUAS.setStatus("mandatory")
_GenEquipPmPWFC_Type = Integer32
_GenEquipPmPWFC_Object = MibTableColumn
genEquipPmPWFC = _GenEquipPmPWFC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 12),
    _GenEquipPmPWFC_Type()
)
genEquipPmPWFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWFC.setStatus("mandatory")
_GenEquipPmPWIDF_Type = Integrity
_GenEquipPmPWIDF_Object = MibTableColumn
genEquipPmPWIDF = _GenEquipPmPWIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 1, 1, 13),
    _GenEquipPmPWIDF_Type()
)
genEquipPmPWIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmPWIDF.setStatus("mandatory")
_GenEquipPmNGPWTable_Object = MibTable
genEquipPmNGPWTable = _GenEquipPmNGPWTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2)
)
if mibBuilder.loadTexts:
    genEquipPmNGPWTable.setStatus("mandatory")
_GenEquipPmNGPWEntry_Object = MibTableRow
genEquipPmNGPWEntry = _GenEquipPmNGPWEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1)
)
genEquipPmNGPWEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmNGPWPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmNGPWIfIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmNGPWInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmNGPWEntry.setStatus("mandatory")
_GenEquipPmNGPWPmType_Type = PmTableType
_GenEquipPmNGPWPmType_Object = MibTableColumn
genEquipPmNGPWPmType = _GenEquipPmNGPWPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 1),
    _GenEquipPmNGPWPmType_Type()
)
genEquipPmNGPWPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWPmType.setStatus("mandatory")
_GenEquipPmNGPWIfIndex_Type = Integer32
_GenEquipPmNGPWIfIndex_Object = MibTableColumn
genEquipPmNGPWIfIndex = _GenEquipPmNGPWIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 2),
    _GenEquipPmNGPWIfIndex_Type()
)
genEquipPmNGPWIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWIfIndex.setStatus("mandatory")
_GenEquipPmNGPWInterval_Type = Integer32
_GenEquipPmNGPWInterval_Object = MibTableColumn
genEquipPmNGPWInterval = _GenEquipPmNGPWInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 3),
    _GenEquipPmNGPWInterval_Type()
)
genEquipPmNGPWInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWInterval.setStatus("mandatory")
_GenEquipPmNGPWES_Type = Integer32
_GenEquipPmNGPWES_Object = MibTableColumn
genEquipPmNGPWES = _GenEquipPmNGPWES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 4),
    _GenEquipPmNGPWES_Type()
)
genEquipPmNGPWES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWES.setStatus("mandatory")
_GenEquipPmNGPWSES_Type = Integer32
_GenEquipPmNGPWSES_Object = MibTableColumn
genEquipPmNGPWSES = _GenEquipPmNGPWSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 5),
    _GenEquipPmNGPWSES_Type()
)
genEquipPmNGPWSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWSES.setStatus("mandatory")
_GenEquipPmNGPWUAS_Type = Integer32
_GenEquipPmNGPWUAS_Object = MibTableColumn
genEquipPmNGPWUAS = _GenEquipPmNGPWUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 6),
    _GenEquipPmNGPWUAS_Type()
)
genEquipPmNGPWUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWUAS.setStatus("mandatory")
_GenEquipPmNGPWFC_Type = Integer32
_GenEquipPmNGPWFC_Object = MibTableColumn
genEquipPmNGPWFC = _GenEquipPmNGPWFC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 7),
    _GenEquipPmNGPWFC_Type()
)
genEquipPmNGPWFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWFC.setStatus("mandatory")
_GenEquipPmNGPWFER_Type = Integer32
_GenEquipPmNGPWFER_Object = MibTableColumn
genEquipPmNGPWFER = _GenEquipPmNGPWFER_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 8),
    _GenEquipPmNGPWFER_Type()
)
genEquipPmNGPWFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWFER.setStatus("mandatory")
_GenEquipPmNGPWMissingPkts_Type = Integer32
_GenEquipPmNGPWMissingPkts_Object = MibTableColumn
genEquipPmNGPWMissingPkts = _GenEquipPmNGPWMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 9),
    _GenEquipPmNGPWMissingPkts_Type()
)
genEquipPmNGPWMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWMissingPkts.setStatus("mandatory")
_GenEquipPmNGPWPktsReOrder_Type = Integer32
_GenEquipPmNGPWPktsReOrder_Object = MibTableColumn
genEquipPmNGPWPktsReOrder = _GenEquipPmNGPWPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 10),
    _GenEquipPmNGPWPktsReOrder_Type()
)
genEquipPmNGPWPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWPktsReOrder.setStatus("mandatory")
_GenEquipPmNGPWMisOrderDropped_Type = Integer32
_GenEquipPmNGPWMisOrderDropped_Object = MibTableColumn
genEquipPmNGPWMisOrderDropped = _GenEquipPmNGPWMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 11),
    _GenEquipPmNGPWMisOrderDropped_Type()
)
genEquipPmNGPWMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWMisOrderDropped.setStatus("mandatory")
_GenEquipPmNGPWMalformedPkt_Type = Integer32
_GenEquipPmNGPWMalformedPkt_Object = MibTableColumn
genEquipPmNGPWMalformedPkt = _GenEquipPmNGPWMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 12),
    _GenEquipPmNGPWMalformedPkt_Type()
)
genEquipPmNGPWMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWMalformedPkt.setStatus("mandatory")
_GenEquipPmNGPWIdf_Type = Integrity
_GenEquipPmNGPWIdf_Object = MibTableColumn
genEquipPmNGPWIdf = _GenEquipPmNGPWIdf_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 8, 2, 1, 13),
    _GenEquipPmNGPWIdf_Type()
)
genEquipPmNGPWIdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmNGPWIdf.setStatus("mandatory")
_GenEquipPmEthUtilization_ObjectIdentity = ObjectIdentity
genEquipPmEthUtilization = _GenEquipPmEthUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9)
)
_GenEquipPmEthUtilizationAdmin_Type = EnableDisable
_GenEquipPmEthUtilizationAdmin_Object = MibScalar
genEquipPmEthUtilizationAdmin = _GenEquipPmEthUtilizationAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 1),
    _GenEquipPmEthUtilizationAdmin_Type()
)
genEquipPmEthUtilizationAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationAdmin.setStatus("mandatory")


class _GenEquipPmEthUtilizationThreshold_Type(Integer32):
    """Custom type genEquipPmEthUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipPmEthUtilizationThreshold_Type.__name__ = "Integer32"
_GenEquipPmEthUtilizationThreshold_Object = MibScalar
genEquipPmEthUtilizationThreshold = _GenEquipPmEthUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 2),
    _GenEquipPmEthUtilizationThreshold_Type()
)
genEquipPmEthUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationThreshold.setStatus("mandatory")
_GenEquipPmEthUtilizationTable_Object = MibTable
genEquipPmEthUtilizationTable = _GenEquipPmEthUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3)
)
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationTable.setStatus("mandatory")
_GenEquipPmEthUtilizationEntry_Object = MibTableRow
genEquipPmEthUtilizationEntry = _GenEquipPmEthUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1)
)
genEquipPmEthUtilizationEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthUtilizationPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmEthUtilizationInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationEntry.setStatus("mandatory")
_GenEquipPmEthUtilizationPmType_Type = PmTableType
_GenEquipPmEthUtilizationPmType_Object = MibTableColumn
genEquipPmEthUtilizationPmType = _GenEquipPmEthUtilizationPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1, 1),
    _GenEquipPmEthUtilizationPmType_Type()
)
genEquipPmEthUtilizationPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationPmType.setStatus("mandatory")
_GenEquipPmEthUtilizationInterval_Type = Integer32
_GenEquipPmEthUtilizationInterval_Object = MibTableColumn
genEquipPmEthUtilizationInterval = _GenEquipPmEthUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1, 2),
    _GenEquipPmEthUtilizationInterval_Type()
)
genEquipPmEthUtilizationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationInterval.setStatus("mandatory")
_GenEquipPmEthUtilizationPeakUtilization_Type = Integer32
_GenEquipPmEthUtilizationPeakUtilization_Object = MibTableColumn
genEquipPmEthUtilizationPeakUtilization = _GenEquipPmEthUtilizationPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1, 3),
    _GenEquipPmEthUtilizationPeakUtilization_Type()
)
genEquipPmEthUtilizationPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationPeakUtilization.setStatus("mandatory")
_GenEquipPmEthUtilizationAverageUtilization_Type = Integer32
_GenEquipPmEthUtilizationAverageUtilization_Object = MibTableColumn
genEquipPmEthUtilizationAverageUtilization = _GenEquipPmEthUtilizationAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1, 4),
    _GenEquipPmEthUtilizationAverageUtilization_Type()
)
genEquipPmEthUtilizationAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationAverageUtilization.setStatus("mandatory")
_GenEquipPmEthUtilizationExceedUtilization_Type = Integer32
_GenEquipPmEthUtilizationExceedUtilization_Object = MibTableColumn
genEquipPmEthUtilizationExceedUtilization = _GenEquipPmEthUtilizationExceedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1, 5),
    _GenEquipPmEthUtilizationExceedUtilization_Type()
)
genEquipPmEthUtilizationExceedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationExceedUtilization.setStatus("mandatory")
_GenEquipPmEthUtilizationIDF_Type = Integrity
_GenEquipPmEthUtilizationIDF_Object = MibTableColumn
genEquipPmEthUtilizationIDF = _GenEquipPmEthUtilizationIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 9, 3, 1, 6),
    _GenEquipPmEthUtilizationIDF_Type()
)
genEquipPmEthUtilizationIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthUtilizationIDF.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicer_ObjectIdentity = ObjectIdentity
genEquipPmEthernetIngressPolicer = _GenEquipPmEthernetIngressPolicer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10)
)
_GenEquipPmEthernetIngressPolicerUnicastStatisticsTable_Object = MibTable
genEquipPmEthernetIngressPolicerUnicastStatisticsTable = _GenEquipPmEthernetIngressPolicerUnicastStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsEntry_Object = MibTableRow
genEquipPmEthernetIngressPolicerUnicastStatisticsEntry = _GenEquipPmEthernetIngressPolicerUnicastStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1)
)
genEquipPmEthernetIngressPolicerUnicastStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex = _GenEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 1),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead = _GenEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 2),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket = _GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 3),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes = _GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 4),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket = _GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 5),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes = _GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 6),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket = _GenEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 7),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes = _GenEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 1, 1, 8),
    _GenEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes_Type()
)
genEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsTable_Object = MibTable
genEquipPmEthernetIngressPolicerMulticastStatisticsTable = _GenEquipPmEthernetIngressPolicerMulticastStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsEntry_Object = MibTableRow
genEquipPmEthernetIngressPolicerMulticastStatisticsEntry = _GenEquipPmEthernetIngressPolicerMulticastStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1)
)
genEquipPmEthernetIngressPolicerMulticastStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex = _GenEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 1),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead = _GenEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 2),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket = _GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 3),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes = _GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 4),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket = _GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 5),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes = _GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 6),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket = _GenEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 7),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes = _GenEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 2, 1, 8),
    _GenEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes_Type()
)
genEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsTable_Object = MibTable
genEquipPmEthernetIngressPolicerBroadcastStatisticsTable = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsEntry_Object = MibTableRow
genEquipPmEthernetIngressPolicerBroadcastStatisticsEntry = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1)
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 1),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 2),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 3),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 4),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 5),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 6),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 7),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes = _GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 3, 1, 8),
    _GenEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes_Type()
)
genEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsTable_Object = MibTable
genEquipPmEthernetIngressPolicerEtherType1StatisticsTable = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsEntry_Object = MibTableRow
genEquipPmEthernetIngressPolicerEtherType1StatisticsEntry = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1)
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 1),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 2),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 3),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 4),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 5),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 6),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 7),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes = _GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 4, 1, 8),
    _GenEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsTable_Object = MibTable
genEquipPmEthernetIngressPolicerEtherType2StatisticsTable = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsEntry_Object = MibTableRow
genEquipPmEthernetIngressPolicerEtherType2StatisticsEntry = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1)
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 1),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 2),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 3),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 4),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 5),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 6),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 7),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes = _GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 5, 1, 8),
    _GenEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsTable_Object = MibTable
genEquipPmEthernetIngressPolicerEtherType3StatisticsTable = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsEntry_Object = MibTableRow
genEquipPmEthernetIngressPolicerEtherType3StatisticsEntry = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1)
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 1),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 2),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 3),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 4),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 5),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 6),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 7),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket.setStatus("mandatory")
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes_Type = Counter64
_GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes_Object = MibTableColumn
genEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes = _GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 10, 6, 1, 8),
    _GenEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes_Type()
)
genEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTable_Object = MibTable
genEquipPmEthernetRmonStatisticsTable = _GenEquipPmEthernetRmonStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTable.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsEntry_Object = MibTableRow
genEquipPmEthernetRmonStatisticsEntry = _GenEquipPmEthernetRmonStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1)
)
genEquipPmEthernetRmonStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetRmonStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsEntry.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsIfIndex_Type = Integer32
_GenEquipPmEthernetRmonStatisticsIfIndex_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsIfIndex = _GenEquipPmEthernetRmonStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 1),
    _GenEquipPmEthernetRmonStatisticsIfIndex_Type()
)
genEquipPmEthernetRmonStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsIfIndex.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsClearOnRead_Type = NoYes
_GenEquipPmEthernetRmonStatisticsClearOnRead_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsClearOnRead = _GenEquipPmEthernetRmonStatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 2),
    _GenEquipPmEthernetRmonStatisticsClearOnRead_Type()
)
genEquipPmEthernetRmonStatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsClearOnRead.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxByteCount_Type = Counter64
_GenEquipPmEthernetRmonStatisticsTxByteCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxByteCount = _GenEquipPmEthernetRmonStatisticsTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 3),
    _GenEquipPmEthernetRmonStatisticsTxByteCount_Type()
)
genEquipPmEthernetRmonStatisticsTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxByteCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxFrameCount = _GenEquipPmEthernetRmonStatisticsTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 4),
    _GenEquipPmEthernetRmonStatisticsTxFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxMulticastFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxMulticastFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxMulticastFrameCount = _GenEquipPmEthernetRmonStatisticsTxMulticastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 5),
    _GenEquipPmEthernetRmonStatisticsTxMulticastFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxMulticastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxMulticastFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxBroadcastFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxBroadcastFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxBroadcastFrameCount = _GenEquipPmEthernetRmonStatisticsTxBroadcastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 6),
    _GenEquipPmEthernetRmonStatisticsTxBroadcastFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxBroadcastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxBroadcastFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxControlFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxControlFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxControlFrameCount = _GenEquipPmEthernetRmonStatisticsTxControlFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 7),
    _GenEquipPmEthernetRmonStatisticsTxControlFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxControlFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxControlFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxPauseFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxPauseFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxPauseFrameCount = _GenEquipPmEthernetRmonStatisticsTxPauseFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 8),
    _GenEquipPmEthernetRmonStatisticsTxPauseFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxPauseFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxPauseFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount = _GenEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 9),
    _GenEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount = _GenEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 10),
    _GenEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxOversizeFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxOversizeFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxOversizeFrameCount = _GenEquipPmEthernetRmonStatisticsTxOversizeFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 11),
    _GenEquipPmEthernetRmonStatisticsTxOversizeFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxOversizeFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxOversizeFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxUndersizeFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxUndersizeFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxUndersizeFrameCount = _GenEquipPmEthernetRmonStatisticsTxUndersizeFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 12),
    _GenEquipPmEthernetRmonStatisticsTxUndersizeFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxUndersizeFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxUndersizeFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxFragmentFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxFragmentFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxFragmentFrameCount = _GenEquipPmEthernetRmonStatisticsTxFragmentFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 13),
    _GenEquipPmEthernetRmonStatisticsTxFragmentFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxFragmentFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxFragmentFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTxJabberFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTxJabberFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTxJabberFrameCount = _GenEquipPmEthernetRmonStatisticsTxJabberFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 14),
    _GenEquipPmEthernetRmonStatisticsTxJabberFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTxJabberFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTxJabberFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx64FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx64FrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsTx64FrameCount = _GenEquipPmEthernetRmonStatisticsTx64FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 15),
    _GenEquipPmEthernetRmonStatisticsTx64FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx64FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx64FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx65_127FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx65_127FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsTx65_127FrameCount = _GenEquipPmEthernetRmonStatisticsTx65_127FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 16),
    _GenEquipPmEthernetRmonStatisticsTx65_127FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx65_127FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx65_127FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx128_255FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx128_255FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsTx128_255FrameCount = _GenEquipPmEthernetRmonStatisticsTx128_255FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 17),
    _GenEquipPmEthernetRmonStatisticsTx128_255FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx128_255FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx128_255FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx256_511FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx256_511FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsTx256_511FrameCount = _GenEquipPmEthernetRmonStatisticsTx256_511FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 18),
    _GenEquipPmEthernetRmonStatisticsTx256_511FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx256_511FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx256_511FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx512_1023FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx512_1023FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsTx512_1023FrameCount = _GenEquipPmEthernetRmonStatisticsTx512_1023FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 19),
    _GenEquipPmEthernetRmonStatisticsTx512_1023FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx512_1023FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx512_1023FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx1024_1518FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx1024_1518FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsTx1024_1518FrameCount = _GenEquipPmEthernetRmonStatisticsTx1024_1518FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 20),
    _GenEquipPmEthernetRmonStatisticsTx1024_1518FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx1024_1518FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx1024_1518FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsTx1519_1522FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsTx1519_1522FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsTx1519_1522FrameCount = _GenEquipPmEthernetRmonStatisticsTx1519_1522FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 21),
    _GenEquipPmEthernetRmonStatisticsTx1519_1522FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsTx1519_1522FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsTx1519_1522FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxByteCount_Type = Counter64
_GenEquipPmEthernetRmonStatisticsRxByteCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxByteCount = _GenEquipPmEthernetRmonStatisticsRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 22),
    _GenEquipPmEthernetRmonStatisticsRxByteCount_Type()
)
genEquipPmEthernetRmonStatisticsRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxByteCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxFrameCount = _GenEquipPmEthernetRmonStatisticsRxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 23),
    _GenEquipPmEthernetRmonStatisticsRxFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxMulticastFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxMulticastFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxMulticastFrameCount = _GenEquipPmEthernetRmonStatisticsRxMulticastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 24),
    _GenEquipPmEthernetRmonStatisticsRxMulticastFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxMulticastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxMulticastFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxBroadcastFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxBroadcastFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxBroadcastFrameCount = _GenEquipPmEthernetRmonStatisticsRxBroadcastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 25),
    _GenEquipPmEthernetRmonStatisticsRxBroadcastFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxBroadcastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxBroadcastFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxControlFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxControlFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxControlFrameCount = _GenEquipPmEthernetRmonStatisticsRxControlFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 26),
    _GenEquipPmEthernetRmonStatisticsRxControlFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxControlFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxControlFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxPauseFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxPauseFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxPauseFrameCount = _GenEquipPmEthernetRmonStatisticsRxPauseFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 27),
    _GenEquipPmEthernetRmonStatisticsRxPauseFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxPauseFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxPauseFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount = _GenEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 28),
    _GenEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount = _GenEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 29),
    _GenEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxcode_ErrorCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxcode_ErrorCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRxcode_ErrorCount = _GenEquipPmEthernetRmonStatisticsRxcode_ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 30),
    _GenEquipPmEthernetRmonStatisticsRxcode_ErrorCount_Type()
)
genEquipPmEthernetRmonStatisticsRxcode_ErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxcode_ErrorCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxoversizeFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxoversizeFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxoversizeFrameCount = _GenEquipPmEthernetRmonStatisticsRxoversizeFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 31),
    _GenEquipPmEthernetRmonStatisticsRxoversizeFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxoversizeFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxoversizeFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount = _GenEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 32),
    _GenEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxFragmentFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxFragmentFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxFragmentFrameCount = _GenEquipPmEthernetRmonStatisticsRxFragmentFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 33),
    _GenEquipPmEthernetRmonStatisticsRxFragmentFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxFragmentFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxFragmentFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx64FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx64FrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRx64FrameCount = _GenEquipPmEthernetRmonStatisticsRx64FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 35),
    _GenEquipPmEthernetRmonStatisticsRx64FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx64FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx64FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx65_127FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx65_127FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRx65_127FrameCount = _GenEquipPmEthernetRmonStatisticsRx65_127FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 36),
    _GenEquipPmEthernetRmonStatisticsRx65_127FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx65_127FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx65_127FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx128_255FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx128_255FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRx128_255FrameCount = _GenEquipPmEthernetRmonStatisticsRx128_255FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 37),
    _GenEquipPmEthernetRmonStatisticsRx128_255FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx128_255FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx128_255FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx256_511FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx256_511FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRx256_511FrameCount = _GenEquipPmEthernetRmonStatisticsRx256_511FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 38),
    _GenEquipPmEthernetRmonStatisticsRx256_511FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx256_511FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx256_511FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx512_1023FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx512_1023FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRx512_1023FrameCount = _GenEquipPmEthernetRmonStatisticsRx512_1023FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 39),
    _GenEquipPmEthernetRmonStatisticsRx512_1023FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx512_1023FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx512_1023FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx1024_1518FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx1024_1518FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRx1024_1518FrameCount = _GenEquipPmEthernetRmonStatisticsRx1024_1518FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 40),
    _GenEquipPmEthernetRmonStatisticsRx1024_1518FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx1024_1518FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx1024_1518FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRx1519_1522FrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRx1519_1522FrameCount_Object = MibScalar
genEquipPmEthernetRmonStatisticsRx1519_1522FrameCount = _GenEquipPmEthernetRmonStatisticsRx1519_1522FrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 41),
    _GenEquipPmEthernetRmonStatisticsRx1519_1522FrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRx1519_1522FrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRx1519_1522FrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount = _GenEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 42),
    _GenEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount = _GenEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 43),
    _GenEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount.setStatus("mandatory")
_GenEquipPmEthernetRmonStatisticsRxJabberFrameCount_Type = Counter32
_GenEquipPmEthernetRmonStatisticsRxJabberFrameCount_Object = MibTableColumn
genEquipPmEthernetRmonStatisticsRxJabberFrameCount = _GenEquipPmEthernetRmonStatisticsRxJabberFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 11, 1, 44),
    _GenEquipPmEthernetRmonStatisticsRxJabberFrameCount_Type()
)
genEquipPmEthernetRmonStatisticsRxJabberFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetRmonStatisticsRxJabberFrameCount.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTable_Object = MibTable
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTable = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12)
)
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTable.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry_Object = MibTableRow
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1)
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex"),
    (0, "MWRM-PM-MIB", "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex"),
)
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 1),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 2),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead_Type = NoYes
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 3),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 4),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 5),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 6),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 7),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 8),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 9),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 10),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 11),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 12),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes = _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 12, 1, 13),
    _GenEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatisticsTable_Object = MibTable
genEquipServicesCetSpPmCosIngressPolicerStatisticsTable = _GenEquipServicesCetSpPmCosIngressPolicerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13)
)
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatisticsTable.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatisticsEntry_Object = MibTableRow
genEquipServicesCetSpPmCosIngressPolicerStatisticsEntry = _GenEquipServicesCetSpPmCosIngressPolicerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1)
)
genEquipServicesCetSpPmCosIngressPolicerStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex"),
    (0, "MWRM-PM-MIB", "genEquipServicesCetSpPmCosIngressPolicerStatiSpIndex"),
    (0, "MWRM-PM-MIB", "genEquipServicesCetSpPmCosIngressPolicerStatiCos"),
)
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatisticsEntry.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex_Type = Integer32
_GenEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex = _GenEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 1),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiSpIndex_Type = Integer32
_GenEquipServicesCetSpPmCosIngressPolicerStatiSpIndex_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiSpIndex = _GenEquipServicesCetSpPmCosIngressPolicerStatiSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 2),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiSpIndex_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiSpIndex.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiCos_Type = Integer32
_GenEquipServicesCetSpPmCosIngressPolicerStatiCos_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiCos = _GenEquipServicesCetSpPmCosIngressPolicerStatiCos_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 3),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiCos_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiCos.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead_Type = NoYes
_GenEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead = _GenEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 4),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket_Type = Counter64
_GenEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket = _GenEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 5),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes_Type = Counter64
_GenEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes = _GenEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 6),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket_Type = Counter64
_GenEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket = _GenEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 7),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes_Type = Counter64
_GenEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes = _GenEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 8),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiRedPacket_Type = Counter64
_GenEquipServicesCetSpPmCosIngressPolicerStatiRedPacket_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiRedPacket = _GenEquipServicesCetSpPmCosIngressPolicerStatiRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 9),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiRedPacket_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiRedPacket.setStatus("mandatory")
_GenEquipServicesCetSpPmCosIngressPolicerStatiRedBytes_Type = Counter64
_GenEquipServicesCetSpPmCosIngressPolicerStatiRedBytes_Object = MibTableColumn
genEquipServicesCetSpPmCosIngressPolicerStatiRedBytes = _GenEquipServicesCetSpPmCosIngressPolicerStatiRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 13, 1, 10),
    _GenEquipServicesCetSpPmCosIngressPolicerStatiRedBytes_Type()
)
genEquipServicesCetSpPmCosIngressPolicerStatiRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmCosIngressPolicerStatiRedBytes.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatisticsTable_Object = MibTable
genEquipServicesCetSpPmIngressPolicerStatisticsTable = _GenEquipServicesCetSpPmIngressPolicerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14)
)
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatisticsTable.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatisticsEntry_Object = MibTableRow
genEquipServicesCetSpPmIngressPolicerStatisticsEntry = _GenEquipServicesCetSpPmIngressPolicerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1)
)
genEquipServicesCetSpPmIngressPolicerStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipServicesCetSpPmIngressPolicerStatiServiceIndex"),
    (0, "MWRM-PM-MIB", "genEquipServicesCetSpPmIngressPolicerStatiSpIndex"),
)
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatisticsEntry.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiServiceIndex_Type = Integer32
_GenEquipServicesCetSpPmIngressPolicerStatiServiceIndex_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiServiceIndex = _GenEquipServicesCetSpPmIngressPolicerStatiServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 1),
    _GenEquipServicesCetSpPmIngressPolicerStatiServiceIndex_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiServiceIndex.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiSpIndex_Type = Integer32
_GenEquipServicesCetSpPmIngressPolicerStatiSpIndex_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiSpIndex = _GenEquipServicesCetSpPmIngressPolicerStatiSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 2),
    _GenEquipServicesCetSpPmIngressPolicerStatiSpIndex_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiSpIndex.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiClearOnRead_Type = NoYes
_GenEquipServicesCetSpPmIngressPolicerStatiClearOnRead_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiClearOnRead = _GenEquipServicesCetSpPmIngressPolicerStatiClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 3),
    _GenEquipServicesCetSpPmIngressPolicerStatiClearOnRead_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiClearOnRead.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiGreenPacket_Type = Counter64
_GenEquipServicesCetSpPmIngressPolicerStatiGreenPacket_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiGreenPacket = _GenEquipServicesCetSpPmIngressPolicerStatiGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 4),
    _GenEquipServicesCetSpPmIngressPolicerStatiGreenPacket_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiGreenPacket.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiGreenBytes_Type = Counter64
_GenEquipServicesCetSpPmIngressPolicerStatiGreenBytes_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiGreenBytes = _GenEquipServicesCetSpPmIngressPolicerStatiGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 5),
    _GenEquipServicesCetSpPmIngressPolicerStatiGreenBytes_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiGreenBytes.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiYellowPacket_Type = Counter64
_GenEquipServicesCetSpPmIngressPolicerStatiYellowPacket_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiYellowPacket = _GenEquipServicesCetSpPmIngressPolicerStatiYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 6),
    _GenEquipServicesCetSpPmIngressPolicerStatiYellowPacket_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiYellowPacket.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiYellowBytes_Type = Counter64
_GenEquipServicesCetSpPmIngressPolicerStatiYellowBytes_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiYellowBytes = _GenEquipServicesCetSpPmIngressPolicerStatiYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 7),
    _GenEquipServicesCetSpPmIngressPolicerStatiYellowBytes_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiYellowBytes.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiRedPacket_Type = Counter64
_GenEquipServicesCetSpPmIngressPolicerStatiRedPacket_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiRedPacket = _GenEquipServicesCetSpPmIngressPolicerStatiRedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 8),
    _GenEquipServicesCetSpPmIngressPolicerStatiRedPacket_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiRedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiRedPacket.setStatus("mandatory")
_GenEquipServicesCetSpPmIngressPolicerStatiRedBytes_Type = Counter64
_GenEquipServicesCetSpPmIngressPolicerStatiRedBytes_Object = MibTableColumn
genEquipServicesCetSpPmIngressPolicerStatiRedBytes = _GenEquipServicesCetSpPmIngressPolicerStatiRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 14, 1, 9),
    _GenEquipServicesCetSpPmIngressPolicerStatiRedBytes_Type()
)
genEquipServicesCetSpPmIngressPolicerStatiRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCetSpPmIngressPolicerStatiRedBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTable_Object = MibTable
genEquipServicesCETTmPmSpEgressQueueStatisticsTable = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15)
)
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTable.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsEntry_Object = MibTableRow
genEquipServicesCETTmPmSpEgressQueueStatisticsEntry = _GenEquipServicesCETTmPmSpEgressQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1)
)
genEquipServicesCETTmPmSpEgressQueueStatisticsEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex"),
    (0, "MWRM-PM-MIB", "genEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex"),
    (0, "MWRM-PM-MIB", "genEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex"),
)
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsEntry.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex = _GenEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 1),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex = _GenEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 2),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex = _GenEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 3),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead_Type = NoYes
_GenEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead = _GenEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 4),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 5),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 6),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 7),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket = _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 8),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes = _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 9),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 10),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 11),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond_Type = Integer32
_GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond = _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 12),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket = _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 13),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket.setStatus("mandatory")
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes_Type = Counter64
_GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes_Object = MibTableColumn
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes = _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 15, 1, 14),
    _GenEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes_Type()
)
genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes.setStatus("mandatory")
_GenEquipPmUtilization_ObjectIdentity = ObjectIdentity
genEquipPmUtilization = _GenEquipPmUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16)
)
_GenEquipPmUtilizationCPU_ObjectIdentity = ObjectIdentity
genEquipPmUtilizationCPU = _GenEquipPmUtilizationCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1)
)
_GenEquipPmUtilizationCPUAdmin_Type = EnableDisable
_GenEquipPmUtilizationCPUAdmin_Object = MibScalar
genEquipPmUtilizationCPUAdmin = _GenEquipPmUtilizationCPUAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 1),
    _GenEquipPmUtilizationCPUAdmin_Type()
)
genEquipPmUtilizationCPUAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUAdmin.setStatus("mandatory")


class _GenEquipPmUtilizationCPUThreshold_Type(Integer32):
    """Custom type genEquipPmUtilizationCPUThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipPmUtilizationCPUThreshold_Type.__name__ = "Integer32"
_GenEquipPmUtilizationCPUThreshold_Object = MibScalar
genEquipPmUtilizationCPUThreshold = _GenEquipPmUtilizationCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 2),
    _GenEquipPmUtilizationCPUThreshold_Type()
)
genEquipPmUtilizationCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUThreshold.setStatus("mandatory")
_GenEquipPmUtilizationCPUTable_Object = MibTable
genEquipPmUtilizationCPUTable = _GenEquipPmUtilizationCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3)
)
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUTable.setStatus("mandatory")
_GenEquipPmUtilizationCPUEntry_Object = MibTableRow
genEquipPmUtilizationCPUEntry = _GenEquipPmUtilizationCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1)
)
genEquipPmUtilizationCPUEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmUtilizationCPUPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmUtilizationCPUInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUEntry.setStatus("mandatory")
_GenEquipPmUtilizationCPUPmType_Type = PmTableType
_GenEquipPmUtilizationCPUPmType_Object = MibTableColumn
genEquipPmUtilizationCPUPmType = _GenEquipPmUtilizationCPUPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 1),
    _GenEquipPmUtilizationCPUPmType_Type()
)
genEquipPmUtilizationCPUPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUPmType.setStatus("mandatory")
_GenEquipPmUtilizationCPUInterval_Type = Integer32
_GenEquipPmUtilizationCPUInterval_Object = MibTableColumn
genEquipPmUtilizationCPUInterval = _GenEquipPmUtilizationCPUInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 2),
    _GenEquipPmUtilizationCPUInterval_Type()
)
genEquipPmUtilizationCPUInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUInterval.setStatus("mandatory")
_GenEquipPmUtilizationCPUPeakUtilization_Type = Integer32
_GenEquipPmUtilizationCPUPeakUtilization_Object = MibTableColumn
genEquipPmUtilizationCPUPeakUtilization = _GenEquipPmUtilizationCPUPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 3),
    _GenEquipPmUtilizationCPUPeakUtilization_Type()
)
genEquipPmUtilizationCPUPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUPeakUtilization.setStatus("mandatory")
_GenEquipPmUtilizationCPUAverageUtilization_Type = Integer32
_GenEquipPmUtilizationCPUAverageUtilization_Object = MibTableColumn
genEquipPmUtilizationCPUAverageUtilization = _GenEquipPmUtilizationCPUAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 4),
    _GenEquipPmUtilizationCPUAverageUtilization_Type()
)
genEquipPmUtilizationCPUAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUAverageUtilization.setStatus("mandatory")
_GenEquipPmUtilizationCPUMinimumUtilization_Type = Integer32
_GenEquipPmUtilizationCPUMinimumUtilization_Object = MibTableColumn
genEquipPmUtilizationCPUMinimumUtilization = _GenEquipPmUtilizationCPUMinimumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 5),
    _GenEquipPmUtilizationCPUMinimumUtilization_Type()
)
genEquipPmUtilizationCPUMinimumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUMinimumUtilization.setStatus("mandatory")
_GenEquipPmUtilizationCPUExceedUtilization_Type = Integer32
_GenEquipPmUtilizationCPUExceedUtilization_Object = MibTableColumn
genEquipPmUtilizationCPUExceedUtilization = _GenEquipPmUtilizationCPUExceedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 6),
    _GenEquipPmUtilizationCPUExceedUtilization_Type()
)
genEquipPmUtilizationCPUExceedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUExceedUtilization.setStatus("mandatory")
_GenEquipPmUtilizationCPUIDF_Type = Integrity
_GenEquipPmUtilizationCPUIDF_Object = MibTableColumn
genEquipPmUtilizationCPUIDF = _GenEquipPmUtilizationCPUIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 1, 3, 1, 7),
    _GenEquipPmUtilizationCPUIDF_Type()
)
genEquipPmUtilizationCPUIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationCPUIDF.setStatus("mandatory")
_GenEquipPmUtilizationMem_ObjectIdentity = ObjectIdentity
genEquipPmUtilizationMem = _GenEquipPmUtilizationMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2)
)
_GenEquipPmUtilizationMemAdmin_Type = EnableDisable
_GenEquipPmUtilizationMemAdmin_Object = MibScalar
genEquipPmUtilizationMemAdmin = _GenEquipPmUtilizationMemAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 1),
    _GenEquipPmUtilizationMemAdmin_Type()
)
genEquipPmUtilizationMemAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemAdmin.setStatus("mandatory")


class _GenEquipPmUtilizationMemThreshold_Type(Integer32):
    """Custom type genEquipPmUtilizationMemThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GenEquipPmUtilizationMemThreshold_Type.__name__ = "Integer32"
_GenEquipPmUtilizationMemThreshold_Object = MibScalar
genEquipPmUtilizationMemThreshold = _GenEquipPmUtilizationMemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 2),
    _GenEquipPmUtilizationMemThreshold_Type()
)
genEquipPmUtilizationMemThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemThreshold.setStatus("mandatory")
_GenEquipPmUtilizationMemTable_Object = MibTable
genEquipPmUtilizationMemTable = _GenEquipPmUtilizationMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3)
)
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemTable.setStatus("mandatory")
_GenEquipPmUtilizationMemEntry_Object = MibTableRow
genEquipPmUtilizationMemEntry = _GenEquipPmUtilizationMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1)
)
genEquipPmUtilizationMemEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmUtilizationMemPmType"),
    (0, "MWRM-PM-MIB", "genEquipPmUtilizationMemInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemEntry.setStatus("mandatory")
_GenEquipPmUtilizationMemPmType_Type = PmTableType
_GenEquipPmUtilizationMemPmType_Object = MibTableColumn
genEquipPmUtilizationMemPmType = _GenEquipPmUtilizationMemPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 1),
    _GenEquipPmUtilizationMemPmType_Type()
)
genEquipPmUtilizationMemPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemPmType.setStatus("mandatory")
_GenEquipPmUtilizationMemInterval_Type = Integer32
_GenEquipPmUtilizationMemInterval_Object = MibTableColumn
genEquipPmUtilizationMemInterval = _GenEquipPmUtilizationMemInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 2),
    _GenEquipPmUtilizationMemInterval_Type()
)
genEquipPmUtilizationMemInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemInterval.setStatus("mandatory")
_GenEquipPmUtilizationMemPeakUtilization_Type = Integer32
_GenEquipPmUtilizationMemPeakUtilization_Object = MibTableColumn
genEquipPmUtilizationMemPeakUtilization = _GenEquipPmUtilizationMemPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 3),
    _GenEquipPmUtilizationMemPeakUtilization_Type()
)
genEquipPmUtilizationMemPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemPeakUtilization.setStatus("mandatory")
_GenEquipPmUtilizationMemAverageUtilization_Type = Integer32
_GenEquipPmUtilizationMemAverageUtilization_Object = MibTableColumn
genEquipPmUtilizationMemAverageUtilization = _GenEquipPmUtilizationMemAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 4),
    _GenEquipPmUtilizationMemAverageUtilization_Type()
)
genEquipPmUtilizationMemAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemAverageUtilization.setStatus("mandatory")
_GenEquipPmUtilizationMemMinimumUtilization_Type = Integer32
_GenEquipPmUtilizationMemMinimumUtilization_Object = MibTableColumn
genEquipPmUtilizationMemMinimumUtilization = _GenEquipPmUtilizationMemMinimumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 5),
    _GenEquipPmUtilizationMemMinimumUtilization_Type()
)
genEquipPmUtilizationMemMinimumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemMinimumUtilization.setStatus("mandatory")
_GenEquipPmUtilizationMemExceedUtilization_Type = Integer32
_GenEquipPmUtilizationMemExceedUtilization_Object = MibTableColumn
genEquipPmUtilizationMemExceedUtilization = _GenEquipPmUtilizationMemExceedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 6),
    _GenEquipPmUtilizationMemExceedUtilization_Type()
)
genEquipPmUtilizationMemExceedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemExceedUtilization.setStatus("mandatory")
_GenEquipPmUtilizationMemIDF_Type = Integrity
_GenEquipPmUtilizationMemIDF_Object = MibTableColumn
genEquipPmUtilizationMemIDF = _GenEquipPmUtilizationMemIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 16, 2, 3, 1, 7),
    _GenEquipPmUtilizationMemIDF_Type()
)
genEquipPmUtilizationMemIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmUtilizationMemIDF.setStatus("mandatory")
_GenEquipPmEthernet_ObjectIdentity = ObjectIdentity
genEquipPmEthernet = _GenEquipPmEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17)
)
_GenEquipPmEthernetPortTable_Object = MibTable
genEquipPmEthernetPortTable = _GenEquipPmEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1)
)
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTable.setStatus("mandatory")
_GenEquipPmEthernetPortEntry_Object = MibTableRow
genEquipPmEthernetPortEntry = _GenEquipPmEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1)
)
genEquipPmEthernetPortEntry.setIndexNames(
    (0, "MWRM-PM-MIB", "genEquipPmEthernetPortPmType"),
    (0, "IF-MIB", "ifIndex"),
    (0, "MWRM-PM-MIB", "genEquipPmEthernetPortPmInterval"),
)
if mibBuilder.loadTexts:
    genEquipPmEthernetPortEntry.setStatus("mandatory")
_GenEquipPmEthernetPortPmType_Type = Integer32
_GenEquipPmEthernetPortPmType_Object = MibTableColumn
genEquipPmEthernetPortPmType = _GenEquipPmEthernetPortPmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 1),
    _GenEquipPmEthernetPortPmType_Type()
)
genEquipPmEthernetPortPmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortPmType.setStatus("mandatory")
_GenEquipPmEthernetPortPmInterval_Type = Integer32
_GenEquipPmEthernetPortPmInterval_Object = MibTableColumn
genEquipPmEthernetPortPmInterval = _GenEquipPmEthernetPortPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 2),
    _GenEquipPmEthernetPortPmInterval_Type()
)
genEquipPmEthernetPortPmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortPmInterval.setStatus("mandatory")
_GenEquipPmEthernetPortRxAvgBcastPackets_Type = Integer32
_GenEquipPmEthernetPortRxAvgBcastPackets_Object = MibTableColumn
genEquipPmEthernetPortRxAvgBcastPackets = _GenEquipPmEthernetPortRxAvgBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 3),
    _GenEquipPmEthernetPortRxAvgBcastPackets_Type()
)
genEquipPmEthernetPortRxAvgBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxAvgBcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortRxPeakBcastPackets_Type = Integer32
_GenEquipPmEthernetPortRxPeakBcastPackets_Object = MibTableColumn
genEquipPmEthernetPortRxPeakBcastPackets = _GenEquipPmEthernetPortRxPeakBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 4),
    _GenEquipPmEthernetPortRxPeakBcastPackets_Type()
)
genEquipPmEthernetPortRxPeakBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxPeakBcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt_Type = Integer32
_GenEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt_Object = MibTableColumn
genEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt = _GenEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 5),
    _GenEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt_Type()
)
genEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt.setStatus("mandatory")
_GenEquipPmEthernetPortRxAvgBytesLayer1_Type = Integer32
_GenEquipPmEthernetPortRxAvgBytesLayer1_Object = MibTableColumn
genEquipPmEthernetPortRxAvgBytesLayer1 = _GenEquipPmEthernetPortRxAvgBytesLayer1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 6),
    _GenEquipPmEthernetPortRxAvgBytesLayer1_Type()
)
genEquipPmEthernetPortRxAvgBytesLayer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxAvgBytesLayer1.setStatus("mandatory")
_GenEquipPmEthernetPortRxPeakBytesLayer1_Type = Integer32
_GenEquipPmEthernetPortRxPeakBytesLayer1_Object = MibTableColumn
genEquipPmEthernetPortRxPeakBytesLayer1 = _GenEquipPmEthernetPortRxPeakBytesLayer1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 7),
    _GenEquipPmEthernetPortRxPeakBytesLayer1_Type()
)
genEquipPmEthernetPortRxPeakBytesLayer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxPeakBytesLayer1.setStatus("mandatory")
_GenEquipPmEthernetPortRxAvgBytesLayer2_Type = Integer32
_GenEquipPmEthernetPortRxAvgBytesLayer2_Object = MibTableColumn
genEquipPmEthernetPortRxAvgBytesLayer2 = _GenEquipPmEthernetPortRxAvgBytesLayer2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 8),
    _GenEquipPmEthernetPortRxAvgBytesLayer2_Type()
)
genEquipPmEthernetPortRxAvgBytesLayer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxAvgBytesLayer2.setStatus("mandatory")
_GenEquipPmEthernetPortRxPeakBytesLayer2_Type = Integer32
_GenEquipPmEthernetPortRxPeakBytesLayer2_Object = MibTableColumn
genEquipPmEthernetPortRxPeakBytesLayer2 = _GenEquipPmEthernetPortRxPeakBytesLayer2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 9),
    _GenEquipPmEthernetPortRxPeakBytesLayer2_Type()
)
genEquipPmEthernetPortRxPeakBytesLayer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxPeakBytesLayer2.setStatus("mandatory")
_GenEquipPmEthernetPortRxAvgMcastPackets_Type = Integer32
_GenEquipPmEthernetPortRxAvgMcastPackets_Object = MibTableColumn
genEquipPmEthernetPortRxAvgMcastPackets = _GenEquipPmEthernetPortRxAvgMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 10),
    _GenEquipPmEthernetPortRxAvgMcastPackets_Type()
)
genEquipPmEthernetPortRxAvgMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxAvgMcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortRxPeakMcastPackets_Type = Integer32
_GenEquipPmEthernetPortRxPeakMcastPackets_Object = MibTableColumn
genEquipPmEthernetPortRxPeakMcastPackets = _GenEquipPmEthernetPortRxPeakMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 11),
    _GenEquipPmEthernetPortRxPeakMcastPackets_Type()
)
genEquipPmEthernetPortRxPeakMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxPeakMcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortRxAvgPackets_Type = Integer32
_GenEquipPmEthernetPortRxAvgPackets_Object = MibTableColumn
genEquipPmEthernetPortRxAvgPackets = _GenEquipPmEthernetPortRxAvgPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 12),
    _GenEquipPmEthernetPortRxAvgPackets_Type()
)
genEquipPmEthernetPortRxAvgPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxAvgPackets.setStatus("mandatory")
_GenEquipPmEthernetPortRxPeakPackets_Type = Integer32
_GenEquipPmEthernetPortRxPeakPackets_Object = MibTableColumn
genEquipPmEthernetPortRxPeakPackets = _GenEquipPmEthernetPortRxPeakPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 13),
    _GenEquipPmEthernetPortRxPeakPackets_Type()
)
genEquipPmEthernetPortRxPeakPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortRxPeakPackets.setStatus("mandatory")
_GenEquipPmEthernetPortTxAvgBcastPackets_Type = Integer32
_GenEquipPmEthernetPortTxAvgBcastPackets_Object = MibTableColumn
genEquipPmEthernetPortTxAvgBcastPackets = _GenEquipPmEthernetPortTxAvgBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 14),
    _GenEquipPmEthernetPortTxAvgBcastPackets_Type()
)
genEquipPmEthernetPortTxAvgBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxAvgBcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortTxPeakBcastPackets_Type = Integer32
_GenEquipPmEthernetPortTxPeakBcastPackets_Object = MibTableColumn
genEquipPmEthernetPortTxPeakBcastPackets = _GenEquipPmEthernetPortTxPeakBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 15),
    _GenEquipPmEthernetPortTxPeakBcastPackets_Type()
)
genEquipPmEthernetPortTxPeakBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxPeakBcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt_Type = Integer32
_GenEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt_Object = MibTableColumn
genEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt = _GenEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 16),
    _GenEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt_Type()
)
genEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt.setStatus("mandatory")
_GenEquipPmEthernetPortTxAvgBytesLayer1_Type = Integer32
_GenEquipPmEthernetPortTxAvgBytesLayer1_Object = MibTableColumn
genEquipPmEthernetPortTxAvgBytesLayer1 = _GenEquipPmEthernetPortTxAvgBytesLayer1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 17),
    _GenEquipPmEthernetPortTxAvgBytesLayer1_Type()
)
genEquipPmEthernetPortTxAvgBytesLayer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxAvgBytesLayer1.setStatus("mandatory")
_GenEquipPmEthernetPortTxPeakBytesLayer1_Type = Integer32
_GenEquipPmEthernetPortTxPeakBytesLayer1_Object = MibTableColumn
genEquipPmEthernetPortTxPeakBytesLayer1 = _GenEquipPmEthernetPortTxPeakBytesLayer1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 18),
    _GenEquipPmEthernetPortTxPeakBytesLayer1_Type()
)
genEquipPmEthernetPortTxPeakBytesLayer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxPeakBytesLayer1.setStatus("mandatory")
_GenEquipPmEthernetPortTxAvgBytesLayer2_Type = Integer32
_GenEquipPmEthernetPortTxAvgBytesLayer2_Object = MibTableColumn
genEquipPmEthernetPortTxAvgBytesLayer2 = _GenEquipPmEthernetPortTxAvgBytesLayer2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 19),
    _GenEquipPmEthernetPortTxAvgBytesLayer2_Type()
)
genEquipPmEthernetPortTxAvgBytesLayer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxAvgBytesLayer2.setStatus("mandatory")
_GenEquipPmEthernetPortTxPeakBytesLayer2_Type = Integer32
_GenEquipPmEthernetPortTxPeakBytesLayer2_Object = MibTableColumn
genEquipPmEthernetPortTxPeakBytesLayer2 = _GenEquipPmEthernetPortTxPeakBytesLayer2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 20),
    _GenEquipPmEthernetPortTxPeakBytesLayer2_Type()
)
genEquipPmEthernetPortTxPeakBytesLayer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxPeakBytesLayer2.setStatus("mandatory")
_GenEquipPmEthernetPortTxAvgMcastPackets_Type = Integer32
_GenEquipPmEthernetPortTxAvgMcastPackets_Object = MibTableColumn
genEquipPmEthernetPortTxAvgMcastPackets = _GenEquipPmEthernetPortTxAvgMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 21),
    _GenEquipPmEthernetPortTxAvgMcastPackets_Type()
)
genEquipPmEthernetPortTxAvgMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxAvgMcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortTxPeakMcastPackets_Type = Integer32
_GenEquipPmEthernetPortTxPeakMcastPackets_Object = MibTableColumn
genEquipPmEthernetPortTxPeakMcastPackets = _GenEquipPmEthernetPortTxPeakMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 22),
    _GenEquipPmEthernetPortTxPeakMcastPackets_Type()
)
genEquipPmEthernetPortTxPeakMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxPeakMcastPackets.setStatus("mandatory")
_GenEquipPmEthernetPortTxAvgPackets_Type = Integer32
_GenEquipPmEthernetPortTxAvgPackets_Object = MibTableColumn
genEquipPmEthernetPortTxAvgPackets = _GenEquipPmEthernetPortTxAvgPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 23),
    _GenEquipPmEthernetPortTxAvgPackets_Type()
)
genEquipPmEthernetPortTxAvgPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxAvgPackets.setStatus("mandatory")
_GenEquipPmEthernetPortTxPeakPackets_Type = Integer32
_GenEquipPmEthernetPortTxPeakPackets_Object = MibTableColumn
genEquipPmEthernetPortTxPeakPackets = _GenEquipPmEthernetPortTxPeakPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 24),
    _GenEquipPmEthernetPortTxPeakPackets_Type()
)
genEquipPmEthernetPortTxPeakPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortTxPeakPackets.setStatus("mandatory")
_GenEquipPmEthernetPortPmIDF_Type = Integer32
_GenEquipPmEthernetPortPmIDF_Object = MibTableColumn
genEquipPmEthernetPortPmIDF = _GenEquipPmEthernetPortPmIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 3, 17, 1, 1, 25),
    _GenEquipPmEthernetPortPmIDF_Type()
)
genEquipPmEthernetPortPmIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genEquipPmEthernetPortPmIDF.setStatus("mandatory")
_GenEquipPMStatistics_ObjectIdentity = ObjectIdentity
genEquipPMStatistics = _GenEquipPMStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 4)
)
_GenEquipRMONResetCounters_Type = OffOn
_GenEquipRMONResetCounters_Object = MibScalar
genEquipRMONResetCounters = _GenEquipRMONResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 4, 1),
    _GenEquipRMONResetCounters_Type()
)
genEquipRMONResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipRMONResetCounters.setStatus("mandatory")
_GenEquipPMStatisticsResetAllL2PortPm_Type = OffOn
_GenEquipPMStatisticsResetAllL2PortPm_Object = MibScalar
genEquipPMStatisticsResetAllL2PortPm = _GenEquipPMStatisticsResetAllL2PortPm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 10, 6, 4, 2),
    _GenEquipPMStatisticsResetAllL2PortPm_Type()
)
genEquipPMStatisticsResetAllL2PortPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genEquipPMStatisticsResetAllL2PortPm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWRM-PM-MIB",
    **{"microwave-radio": microwave_radio,
       "genEquip": genEquip,
       "genEquipUnit": genEquipUnit,
       "genEquipPM": genEquipPM,
       "genEquipPmRfu": genEquipPmRfu,
       "genEquipPmRfuCommon": genEquipPmRfuCommon,
       "genEquipPmRfuCommonSL15minTable": genEquipPmRfuCommonSL15minTable,
       "genEquipPmRfuCommonSL15minEntry": genEquipPmRfuCommonSL15minEntry,
       "genEquipPmRfuCommonSL15minId": genEquipPmRfuCommonSL15minId,
       "genEquipPmRfuCommonSL15minIfIndex": genEquipPmRfuCommonSL15minIfIndex,
       "genEquipPmRfuCommonSL15minTimeAndDate": genEquipPmRfuCommonSL15minTimeAndDate,
       "genEquipPmRfuCommonSL15minMinRsl": genEquipPmRfuCommonSL15minMinRsl,
       "genEquipPmRfuCommonSL15minMaxRsl": genEquipPmRfuCommonSL15minMaxRsl,
       "genEquipPmRfuCommonSL15minRslExceed1": genEquipPmRfuCommonSL15minRslExceed1,
       "genEquipPmRfuCommonSL15minRslExceed2": genEquipPmRfuCommonSL15minRslExceed2,
       "genEquipPmRfuCommonSL15minMinTsl": genEquipPmRfuCommonSL15minMinTsl,
       "genEquipPmRfuCommonSL15minMaxTsl": genEquipPmRfuCommonSL15minMaxTsl,
       "genEquipPmRfuCommonSL15minTslExceed": genEquipPmRfuCommonSL15minTslExceed,
       "genEquipPmRfuCommonSL15minIDF": genEquipPmRfuCommonSL15minIDF,
       "genEquipPmRfuCommonSL15minCurrTable": genEquipPmRfuCommonSL15minCurrTable,
       "genEquipPmRfuCommonSL15minCurrEntry": genEquipPmRfuCommonSL15minCurrEntry,
       "genEquipPmRfuCommonSL15minCurrId": genEquipPmRfuCommonSL15minCurrId,
       "genEquipPmRfuCommonSL15minCurrIfIndex": genEquipPmRfuCommonSL15minCurrIfIndex,
       "genEquipPmRfuCommonSL15minCurrTimeAndDate": genEquipPmRfuCommonSL15minCurrTimeAndDate,
       "genEquipPmRfuCommonSL15minCurrMinRsl": genEquipPmRfuCommonSL15minCurrMinRsl,
       "genEquipPmRfuCommonSL15minCurrMaxRsl": genEquipPmRfuCommonSL15minCurrMaxRsl,
       "genEquipPmRfuCommonSL15minCurrRslExceed1": genEquipPmRfuCommonSL15minCurrRslExceed1,
       "genEquipPmRfuCommonSL15minCurrRslExceed2": genEquipPmRfuCommonSL15minCurrRslExceed2,
       "genEquipPmRfuCommonSL15minCurrMinTsl": genEquipPmRfuCommonSL15minCurrMinTsl,
       "genEquipPmRfuCommonSL15minCurrMaxTsl": genEquipPmRfuCommonSL15minCurrMaxTsl,
       "genEquipPmRfuCommonSL15minCurrTslExceed": genEquipPmRfuCommonSL15minCurrTslExceed,
       "genEquipPmRfuCommonSL15minCurrIDF": genEquipPmRfuCommonSL15minCurrIDF,
       "genEquipPmRfuCommonSL24hrTable": genEquipPmRfuCommonSL24hrTable,
       "genEquipPmRfuCommonSL24hrEntry": genEquipPmRfuCommonSL24hrEntry,
       "genEquipPmRfuCommonSL24hrId": genEquipPmRfuCommonSL24hrId,
       "genEquipPmRfuCommonSL24hrIfIndex": genEquipPmRfuCommonSL24hrIfIndex,
       "genEquipPmRfuCommonSL24hrTimeAndDate": genEquipPmRfuCommonSL24hrTimeAndDate,
       "genEquipPmRfuCommonSL24hrMinRsl": genEquipPmRfuCommonSL24hrMinRsl,
       "genEquipPmRfuCommonSL24hrMaxRsl": genEquipPmRfuCommonSL24hrMaxRsl,
       "genEquipPmRfuCommonSL24hrRslExceed1": genEquipPmRfuCommonSL24hrRslExceed1,
       "genEquipPmRfuCommonSL24hrRslExceed2": genEquipPmRfuCommonSL24hrRslExceed2,
       "genEquipPmRfuCommonSL24hrMinTsl": genEquipPmRfuCommonSL24hrMinTsl,
       "genEquipPmRfuCommonSL24hrMaxTsl": genEquipPmRfuCommonSL24hrMaxTsl,
       "genEquipPmRfuCommonSL24hrTslExceed": genEquipPmRfuCommonSL24hrTslExceed,
       "genEquipPmRfuCommonSL24hrIDF": genEquipPmRfuCommonSL24hrIDF,
       "genEquipPmRfuCommonSL24hrCurrTable": genEquipPmRfuCommonSL24hrCurrTable,
       "genEquipPmRfuCommonSL24hrCurrEntry": genEquipPmRfuCommonSL24hrCurrEntry,
       "genEquipPmRfuCommonSL24hrCurrId": genEquipPmRfuCommonSL24hrCurrId,
       "genEquipPmRfuCommonSL24hrCurrIfIndex": genEquipPmRfuCommonSL24hrCurrIfIndex,
       "genEquipPmRfuCommonSL24hrCurrTimeAndDate": genEquipPmRfuCommonSL24hrCurrTimeAndDate,
       "genEquipPmRfuCommonSL24hrCurrMinRsl": genEquipPmRfuCommonSL24hrCurrMinRsl,
       "genEquipPmRfuCommonSL24hrCurrMaxRsl": genEquipPmRfuCommonSL24hrCurrMaxRsl,
       "genEquipPmRfuCommonSL24hrCurrRslExceed1": genEquipPmRfuCommonSL24hrCurrRslExceed1,
       "genEquipPmRfuCommonSL24hrCurrRslExceed2": genEquipPmRfuCommonSL24hrCurrRslExceed2,
       "genEquipPmRfuCommonSL24hrCurrMinTsl": genEquipPmRfuCommonSL24hrCurrMinTsl,
       "genEquipPmRfuCommonSL24hrCurrMaxTsl": genEquipPmRfuCommonSL24hrCurrMaxTsl,
       "genEquipPmRfuCommonSL24hrCurrTslExceed": genEquipPmRfuCommonSL24hrCurrTslExceed,
       "genEquipPmRfuCommonSL24hrCurrIDF": genEquipPmRfuCommonSL24hrCurrIDF,
       "genEquipPmTraffic": genEquipPmTraffic,
       "genEquipPmTrafficRadioAgg15minTable": genEquipPmTrafficRadioAgg15minTable,
       "genEquipPmTrafficRadioAgg15minEntry": genEquipPmTrafficRadioAgg15minEntry,
       "genEquipPmTrafficRadioAgg15minId": genEquipPmTrafficRadioAgg15minId,
       "genEquipPmTrafficRadioAgg15minIfIndex": genEquipPmTrafficRadioAgg15minIfIndex,
       "genEquipPmTrafficRadioAgg15minTimeAndDate": genEquipPmTrafficRadioAgg15minTimeAndDate,
       "genEquipPmTrafficRadioAgg15minES": genEquipPmTrafficRadioAgg15minES,
       "genEquipPmTrafficRadioAgg15minSES": genEquipPmTrafficRadioAgg15minSES,
       "genEquipPmTrafficRadioAgg15minUAS": genEquipPmTrafficRadioAgg15minUAS,
       "genEquipPmTrafficRadioAgg15minBBE": genEquipPmTrafficRadioAgg15minBBE,
       "genEquipPmTrafficRadioAgg15minIDF": genEquipPmTrafficRadioAgg15minIDF,
       "genEquipPmTrafficRadioAgg15minCurrTable": genEquipPmTrafficRadioAgg15minCurrTable,
       "genEquipPmTrafficRadioAgg15minCurrEntry": genEquipPmTrafficRadioAgg15minCurrEntry,
       "genEquipPmTrafficRadioAgg15minCurrId": genEquipPmTrafficRadioAgg15minCurrId,
       "genEquipPmTrafficRadioAgg15minCurrIfIndex": genEquipPmTrafficRadioAgg15minCurrIfIndex,
       "genEquipPmTrafficRadioAgg15minCurrTimeAndDate": genEquipPmTrafficRadioAgg15minCurrTimeAndDate,
       "genEquipPmTrafficRadioAgg15minCurrES": genEquipPmTrafficRadioAgg15minCurrES,
       "genEquipPmTrafficRadioAgg15minCurrSES": genEquipPmTrafficRadioAgg15minCurrSES,
       "genEquipPmTrafficRadioAgg15minCurrUAS": genEquipPmTrafficRadioAgg15minCurrUAS,
       "genEquipPmTrafficRadioAgg15minCurrBBE": genEquipPmTrafficRadioAgg15minCurrBBE,
       "genEquipPmTrafficRadioAgg15minCurrIDF": genEquipPmTrafficRadioAgg15minCurrIDF,
       "genEquipPmTrafficRadioAgg24hrTable": genEquipPmTrafficRadioAgg24hrTable,
       "genEquipPmTrafficRadioAgg24hrEntry": genEquipPmTrafficRadioAgg24hrEntry,
       "genEquipPmTrafficRadioAgg24hrId": genEquipPmTrafficRadioAgg24hrId,
       "genEquipPmTrafficRadioAgg24hrIfIndex": genEquipPmTrafficRadioAgg24hrIfIndex,
       "genEquipPmTrafficRadioAgg24hrTimeAndDate": genEquipPmTrafficRadioAgg24hrTimeAndDate,
       "genEquipPmTrafficRadioAgg24hrES": genEquipPmTrafficRadioAgg24hrES,
       "genEquipPmTrafficRadioAgg24hrSES": genEquipPmTrafficRadioAgg24hrSES,
       "genEquipPmTrafficRadioAgg24hrUAS": genEquipPmTrafficRadioAgg24hrUAS,
       "genEquipPmTrafficRadioAgg24hrBBE": genEquipPmTrafficRadioAgg24hrBBE,
       "genEquipPmTrafficRadioAgg24hrIDF": genEquipPmTrafficRadioAgg24hrIDF,
       "genEquipPmTrafficRadioAgg24hrCurrTable": genEquipPmTrafficRadioAgg24hrCurrTable,
       "genEquipPmTrafficRadioAgg24hrCurrEntry": genEquipPmTrafficRadioAgg24hrCurrEntry,
       "genEquipPmTrafficRadioAgg24hrCurrId": genEquipPmTrafficRadioAgg24hrCurrId,
       "genEquipPmTrafficRadioAgg24hrCurrIfIndex": genEquipPmTrafficRadioAgg24hrCurrIfIndex,
       "genEquipPmTrafficRadioAgg24hrCurrTimeAndDate": genEquipPmTrafficRadioAgg24hrCurrTimeAndDate,
       "genEquipPmTrafficRadioAgg24hrCurrES": genEquipPmTrafficRadioAgg24hrCurrES,
       "genEquipPmTrafficRadioAgg24hrCurrSES": genEquipPmTrafficRadioAgg24hrCurrSES,
       "genEquipPmTrafficRadioAgg24hrCurrUAS": genEquipPmTrafficRadioAgg24hrCurrUAS,
       "genEquipPmTrafficRadioAgg24hrCurrBBE": genEquipPmTrafficRadioAgg24hrCurrBBE,
       "genEquipPmTrafficRadioAgg24hrCurrIDF": genEquipPmTrafficRadioAgg24hrCurrIDF,
       "genEquipPmAll": genEquipPmAll,
       "genEquipPmClear": genEquipPmClear,
       "genEquipPmTrafficSL": genEquipPmTrafficSL,
       "genEquipPmTrafficSLTable": genEquipPmTrafficSLTable,
       "genEquipPmTrafficSLEntry": genEquipPmTrafficSLEntry,
       "genEquipPmTrafficSLPmType": genEquipPmTrafficSLPmType,
       "genEquipPmTrafficSLId": genEquipPmTrafficSLId,
       "genEquipPmTrafficSLInterval": genEquipPmTrafficSLInterval,
       "genEquipPmTrafficSLMinRsl": genEquipPmTrafficSLMinRsl,
       "genEquipPmTrafficSLMaxRsl": genEquipPmTrafficSLMaxRsl,
       "genEquipPmTrafficSLRslExceed1": genEquipPmTrafficSLRslExceed1,
       "genEquipPmTrafficSLRslExceed2": genEquipPmTrafficSLRslExceed2,
       "genEquipPmTrafficSLMinTsl": genEquipPmTrafficSLMinTsl,
       "genEquipPmTrafficSLMaxTsl": genEquipPmTrafficSLMaxTsl,
       "genEquipPmTrafficSLTslExceed": genEquipPmTrafficSLTslExceed,
       "genEquipPmTrafficSLIDF": genEquipPmTrafficSLIDF,
       "genEquipPmTrafficAggregate": genEquipPmTrafficAggregate,
       "genEquipPmTrafficAggTable": genEquipPmTrafficAggTable,
       "genEquipPmTrafficAggEntry": genEquipPmTrafficAggEntry,
       "genEquipPmTrafficAggPmType": genEquipPmTrafficAggPmType,
       "genEquipPmTrafficAggInterval": genEquipPmTrafficAggInterval,
       "genEquipPmTrafficAggES": genEquipPmTrafficAggES,
       "genEquipPmTrafficAggSES": genEquipPmTrafficAggSES,
       "genEquipPmTrafficAggUAS": genEquipPmTrafficAggUAS,
       "genEquipPmTrafficAggBBE": genEquipPmTrafficAggBBE,
       "genEquipPmTrafficAggIDF": genEquipPmTrafficAggIDF,
       "genEquipPmRadio": genEquipPmRadio,
       "genEquipPmRadioMRMC": genEquipPmRadioMRMC,
       "genEquipPmRadioMRMCTable": genEquipPmRadioMRMCTable,
       "genEquipPmRadioMRMCEntry": genEquipPmRadioMRMCEntry,
       "genEquipPmRadioMRMCPmType": genEquipPmRadioMRMCPmType,
       "genEquipPmRadioMRMCId": genEquipPmRadioMRMCId,
       "genEquipPmRadioMRMCInterval": genEquipPmRadioMRMCInterval,
       "genEquipPmRadioMRMCIfIndex": genEquipPmRadioMRMCIfIndex,
       "genEquipPmRadioMRMCMinProfile": genEquipPmRadioMRMCMinProfile,
       "genEquipPmRadioMRMCMaxProfile": genEquipPmRadioMRMCMaxProfile,
       "genEquipPmRadioMRMCMinBitrate": genEquipPmRadioMRMCMinBitrate,
       "genEquipPmRadioMRMCMaxBitrate": genEquipPmRadioMRMCMaxBitrate,
       "genEquipPmRadioMRMCMinTDMIf": genEquipPmRadioMRMCMinTDMIf,
       "genEquipPmRadioMRMCMaxTDMIf": genEquipPmRadioMRMCMaxTDMIf,
       "genEquipPmRadioMRMCIDF": genEquipPmRadioMRMCIDF,
       "genEquipPmRadioTDM": genEquipPmRadioTDM,
       "genEquipPmRadioTDMTable": genEquipPmRadioTDMTable,
       "genEquipPmRadioTDMEntry": genEquipPmRadioTDMEntry,
       "genEquipPmRadioTDMPmType": genEquipPmRadioTDMPmType,
       "genEquipPmRadioTDMInterval": genEquipPmRadioTDMInterval,
       "genEquipPmRadioTDMRadioUAS": genEquipPmRadioTDMRadioUAS,
       "genEquipPmRadioTDMIDF": genEquipPmRadioTDMIDF,
       "genEquipPmRadioEthernet": genEquipPmRadioEthernet,
       "genEquipPmRadioEthernetTable": genEquipPmRadioEthernetTable,
       "genEquipPmRadioEthernetEntry": genEquipPmRadioEthernetEntry,
       "genEquipPmRadioEthernetPmType": genEquipPmRadioEthernetPmType,
       "genEquipPmRadioEthernetInterval": genEquipPmRadioEthernetInterval,
       "genEquipPmRadioEthernetFrameErrorRate": genEquipPmRadioEthernetFrameErrorRate,
       "genEquipPmRadioEthernetPeakThroughput": genEquipPmRadioEthernetPeakThroughput,
       "genEquipPmRadioEthernetAverageThroughput": genEquipPmRadioEthernetAverageThroughput,
       "genEquipPmRadioEthernetExceedThroughput": genEquipPmRadioEthernetExceedThroughput,
       "genEquipPmRadioEthernetPeakCapacity": genEquipPmRadioEthernetPeakCapacity,
       "genEquipPmRadioEthernetAverageCapacity": genEquipPmRadioEthernetAverageCapacity,
       "genEquipPmRadioEthernetExceedCapacity": genEquipPmRadioEthernetExceedCapacity,
       "genEquipPmRadioEthernetPeakUtilization": genEquipPmRadioEthernetPeakUtilization,
       "genEquipPmRadioEthernetAverageUtilization": genEquipPmRadioEthernetAverageUtilization,
       "genEquipPmRadioEthernetExceedUtilization": genEquipPmRadioEthernetExceedUtilization,
       "genEquipPmRadioEthernetIDF": genEquipPmRadioEthernetIDF,
       "genEquipPmRadioEthernetThresholdTable": genEquipPmRadioEthernetThresholdTable,
       "genEquipPmRadioEthernetThresholdEntry": genEquipPmRadioEthernetThresholdEntry,
       "genEquipPmRadioEthernetThresholdThroughput": genEquipPmRadioEthernetThresholdThroughput,
       "genEquipPmRadioEthernetThresholdCapacity": genEquipPmRadioEthernetThresholdCapacity,
       "genEquipPmRadioEthernetThresholdUtilization": genEquipPmRadioEthernetThresholdUtilization,
       "genEquipPmRadioEthernetEtmTable": genEquipPmRadioEthernetEtmTable,
       "genEquipPmRadioEthernetEtmEntry": genEquipPmRadioEthernetEtmEntry,
       "genEquipPmRadioEthernetEtmPmType": genEquipPmRadioEthernetEtmPmType,
       "genEquipPmRadioEthernetEtmPmQueueIndex": genEquipPmRadioEthernetEtmPmQueueIndex,
       "genEquipPmRadioEthernetEtmInterval": genEquipPmRadioEthernetEtmInterval,
       "genEquipPmRadioEthernetEtmPmMaxGreenBytesPassed": genEquipPmRadioEthernetEtmPmMaxGreenBytesPassed,
       "genEquipPmRadioEthernetEtmPmAvgGreenBytesPassed": genEquipPmRadioEthernetEtmPmAvgGreenBytesPassed,
       "genEquipPmRadioEthernetEtmPmMaxGreenFramesDropped": genEquipPmRadioEthernetEtmPmMaxGreenFramesDropped,
       "genEquipPmRadioEthernetEtmPmAvgGreenFramesDropped": genEquipPmRadioEthernetEtmPmAvgGreenFramesDropped,
       "genEquipPmRadioEthernetEtmPmMaxYellowBytesPassed": genEquipPmRadioEthernetEtmPmMaxYellowBytesPassed,
       "genEquipPmRadioEthernetEtmPmAvgYellowBytesPassed": genEquipPmRadioEthernetEtmPmAvgYellowBytesPassed,
       "genEquipPmRadioEthernetEtmPmMaxYellowFramesDropped": genEquipPmRadioEthernetEtmPmMaxYellowFramesDropped,
       "genEquipPmRadioEthernetEtmPmAvgYellowFramesDropped": genEquipPmRadioEthernetEtmPmAvgYellowFramesDropped,
       "genEquipPmRadioEthernetEtmPmMaxRedFramesDropped": genEquipPmRadioEthernetEtmPmMaxRedFramesDropped,
       "genEquipPmRadioEthernetEtmPmAvgRedFramesDropped": genEquipPmRadioEthernetEtmPmAvgRedFramesDropped,
       "genEquipPmRadioEthernetEtmPmIDF": genEquipPmRadioEthernetEtmPmIDF,
       "genEquipPmRadioEthernetEtmPmMaxGreenFramesPassed": genEquipPmRadioEthernetEtmPmMaxGreenFramesPassed,
       "genEquipPmRadioEthernetEtmPmAvgGreenFramesPassed": genEquipPmRadioEthernetEtmPmAvgGreenFramesPassed,
       "genEquipPmRadioEthernetEtmPmMaxYellowFramesPassed": genEquipPmRadioEthernetEtmPmMaxYellowFramesPassed,
       "genEquipPmRadioEthernetEtmPmAvgYellowFramesPassed": genEquipPmRadioEthernetEtmPmAvgYellowFramesPassed,
       "genEquipPmRadioEthernetEtmPmMaxRedBytesDropped": genEquipPmRadioEthernetEtmPmMaxRedBytesDropped,
       "genEquipPmRadioEthernetEtmPmAvgRedBytesDropped": genEquipPmRadioEthernetEtmPmAvgRedBytesDropped,
       "genEquipPmRadioMSETable": genEquipPmRadioMSETable,
       "genEquipPmRadioMSEEntry": genEquipPmRadioMSEEntry,
       "genEquipPmRadioMSEPmType": genEquipPmRadioMSEPmType,
       "genEquipPmRadioMSEInterval": genEquipPmRadioMSEInterval,
       "genEquipPmRadioMSEMinMse": genEquipPmRadioMSEMinMse,
       "genEquipPmRadioMSEMaxMse": genEquipPmRadioMSEMaxMse,
       "genEquipPmRadioMSEexceeded": genEquipPmRadioMSEexceeded,
       "genEquipPmRadioMSEIDF": genEquipPmRadioMSEIDF,
       "genEquipPmRadioThresholdTable": genEquipPmRadioThresholdTable,
       "genEquipPmRadioThresholdEntry": genEquipPmRadioThresholdEntry,
       "genEquipPmRadioThresholdMSE": genEquipPmRadioThresholdMSE,
       "genEquipPmRadioThresholdRSL1": genEquipPmRadioThresholdRSL1,
       "genEquipPmRadioThresholdRSL2": genEquipPmRadioThresholdRSL2,
       "genEquipPmRadioThresholdTSL": genEquipPmRadioThresholdTSL,
       "genEquipPmRadioThresholdXPI": genEquipPmRadioThresholdXPI,
       "genEquipPmRadioXPITable": genEquipPmRadioXPITable,
       "genEquipPmRadioXPIEntry": genEquipPmRadioXPIEntry,
       "genEquipPmRadioXPIPmType": genEquipPmRadioXPIPmType,
       "genEquipPmRadioXPIPmInterval": genEquipPmRadioXPIPmInterval,
       "genEquipPmRadioXPIPmMinXPI": genEquipPmRadioXPIPmMinXPI,
       "genEquipPmRadioXPIPmMaxXPI": genEquipPmRadioXPIPmMaxXPI,
       "genEquipPmRadioXPIBelowThreshold": genEquipPmRadioXPIBelowThreshold,
       "genEquipPmRadioXPIIDF": genEquipPmRadioXPIIDF,
       "genEquipPmRadioClear": genEquipPmRadioClear,
       "genEquipPmTDM": genEquipPmTDM,
       "genEquipPmTdmTable": genEquipPmTdmTable,
       "genEquipPmTdmEntry": genEquipPmTdmEntry,
       "genEquipPmTdmPmType": genEquipPmTdmPmType,
       "genEquipPmTdmInterval": genEquipPmTdmInterval,
       "genEquipPmTdmES": genEquipPmTdmES,
       "genEquipPmTdmSES": genEquipPmTdmSES,
       "genEquipPmTdmUAS": genEquipPmTdmUAS,
       "genEquipPmTdmBBE": genEquipPmTdmBBE,
       "genEquipPmTdmIDF": genEquipPmTdmIDF,
       "genEquipPmSDH": genEquipPmSDH,
       "genEquipPmSdhTable": genEquipPmSdhTable,
       "genEquipPmSdhEntry": genEquipPmSdhEntry,
       "genEquipPmSdhPmType": genEquipPmSdhPmType,
       "genEquipPmSdhInterval": genEquipPmSdhInterval,
       "genEquipPmSdhES": genEquipPmSdhES,
       "genEquipPmSdhSES": genEquipPmSdhSES,
       "genEquipPmSdhEB": genEquipPmSdhEB,
       "genEquipPmSdhBBE": genEquipPmSdhBBE,
       "genEquipPmSdhIDF": genEquipPmSdhIDF,
       "genEquipPmSdhIfIndex": genEquipPmSdhIfIndex,
       "genEquipPmSdhTimeStamp": genEquipPmSdhTimeStamp,
       "genEquipPmSdhUAS": genEquipPmSdhUAS,
       "genEquipPmSdhRstLRTable": genEquipPmSdhRstLRTable,
       "genEquipPmSdhRstLREntry": genEquipPmSdhRstLREntry,
       "genEquipPmSdhRstLRPmType": genEquipPmSdhRstLRPmType,
       "genEquipPmSdhRstLRIfIndex": genEquipPmSdhRstLRIfIndex,
       "genEquipPmSdhRstLRInterval": genEquipPmSdhRstLRInterval,
       "genEquipPmSdhRstLRTimeStamp": genEquipPmSdhRstLRTimeStamp,
       "genEquipPmSdhRstLRES": genEquipPmSdhRstLRES,
       "genEquipPmSdhRstLRSES": genEquipPmSdhRstLRSES,
       "genEquipPmSdhRstLRUAS": genEquipPmSdhRstLRUAS,
       "genEquipPmSdhRstLREB": genEquipPmSdhRstLREB,
       "genEquipPmSdhRstLRCV": genEquipPmSdhRstLRCV,
       "genEquipPmSdhRstLRBBE": genEquipPmSdhRstLRBBE,
       "genEquipPmSdhRstLRIDF": genEquipPmSdhRstLRIDF,
       "genEquipPmSdhRstRLTable": genEquipPmSdhRstRLTable,
       "genEquipPmSdhRstRLEntry": genEquipPmSdhRstRLEntry,
       "genEquipPmSdhRstRLPmType": genEquipPmSdhRstRLPmType,
       "genEquipPmSdhRstRLIfIndex": genEquipPmSdhRstRLIfIndex,
       "genEquipPmSdhRstRLInterval": genEquipPmSdhRstRLInterval,
       "genEquipPmSdhRstRLTimeStamp": genEquipPmSdhRstRLTimeStamp,
       "genEquipPmSdhRstRLES": genEquipPmSdhRstRLES,
       "genEquipPmSdhRstRLSES": genEquipPmSdhRstRLSES,
       "genEquipPmSdhRstRLUAS": genEquipPmSdhRstRLUAS,
       "genEquipPmSdhRstRLEB": genEquipPmSdhRstRLEB,
       "genEquipPmSdhRstRLCV": genEquipPmSdhRstRLCV,
       "genEquipPmSdhRstRLBBE": genEquipPmSdhRstRLBBE,
       "genEquipPmSdhRstRLIDF": genEquipPmSdhRstRLIDF,
       "genEquipPmTrails": genEquipPmTrails,
       "genEquipPmTrailsEndPointTable": genEquipPmTrailsEndPointTable,
       "genEquipPmTrailsEndPointEntry": genEquipPmTrailsEndPointEntry,
       "genEquipPmTrailsEndPointPmType": genEquipPmTrailsEndPointPmType,
       "genEquipPmTrailsEndPointId": genEquipPmTrailsEndPointId,
       "genEquipPmTrailsEndPointEPId": genEquipPmTrailsEndPointEPId,
       "genEquipPmTrailsEndPointInterval": genEquipPmTrailsEndPointInterval,
       "genEquipPmTrailsEndPointES": genEquipPmTrailsEndPointES,
       "genEquipPmTrailsEndPointSES": genEquipPmTrailsEndPointSES,
       "genEquipPmTrailsEndPointUAS": genEquipPmTrailsEndPointUAS,
       "genEquipPmTrailsEndPointBBE": genEquipPmTrailsEndPointBBE,
       "genEquipPmTrailsEndPointNoOfSwitches": genEquipPmTrailsEndPointNoOfSwitches,
       "genEquipPmTrailsEndPointActivePathCounts": genEquipPmTrailsEndPointActivePathCounts,
       "genEquipPmTrailsEndPointIDF": genEquipPmTrailsEndPointIDF,
       "genEquipPmPW": genEquipPmPW,
       "genEquipPmPWTable": genEquipPmPWTable,
       "genEquipPmPWEntry": genEquipPmPWEntry,
       "genEquipPmPWPmType": genEquipPmPWPmType,
       "genEquipPmPWId": genEquipPmPWId,
       "genEquipPmPWInterval": genEquipPmPWInterval,
       "genEquipPmPWMissingPkts": genEquipPmPWMissingPkts,
       "genEquipPmPWPktsReOrder": genEquipPmPWPktsReOrder,
       "genEquipPmPWtrBfrUnderruns": genEquipPmPWtrBfrUnderruns,
       "genEquipPmPWMisOrderDropped": genEquipPmPWMisOrderDropped,
       "genEquipPmPWMalformedPkt": genEquipPmPWMalformedPkt,
       "genEquipPmPWES": genEquipPmPWES,
       "genEquipPmPWSES": genEquipPmPWSES,
       "genEquipPmPWUAS": genEquipPmPWUAS,
       "genEquipPmPWFC": genEquipPmPWFC,
       "genEquipPmPWIDF": genEquipPmPWIDF,
       "genEquipPmNGPWTable": genEquipPmNGPWTable,
       "genEquipPmNGPWEntry": genEquipPmNGPWEntry,
       "genEquipPmNGPWPmType": genEquipPmNGPWPmType,
       "genEquipPmNGPWIfIndex": genEquipPmNGPWIfIndex,
       "genEquipPmNGPWInterval": genEquipPmNGPWInterval,
       "genEquipPmNGPWES": genEquipPmNGPWES,
       "genEquipPmNGPWSES": genEquipPmNGPWSES,
       "genEquipPmNGPWUAS": genEquipPmNGPWUAS,
       "genEquipPmNGPWFC": genEquipPmNGPWFC,
       "genEquipPmNGPWFER": genEquipPmNGPWFER,
       "genEquipPmNGPWMissingPkts": genEquipPmNGPWMissingPkts,
       "genEquipPmNGPWPktsReOrder": genEquipPmNGPWPktsReOrder,
       "genEquipPmNGPWMisOrderDropped": genEquipPmNGPWMisOrderDropped,
       "genEquipPmNGPWMalformedPkt": genEquipPmNGPWMalformedPkt,
       "genEquipPmNGPWIdf": genEquipPmNGPWIdf,
       "genEquipPmEthUtilization": genEquipPmEthUtilization,
       "genEquipPmEthUtilizationAdmin": genEquipPmEthUtilizationAdmin,
       "genEquipPmEthUtilizationThreshold": genEquipPmEthUtilizationThreshold,
       "genEquipPmEthUtilizationTable": genEquipPmEthUtilizationTable,
       "genEquipPmEthUtilizationEntry": genEquipPmEthUtilizationEntry,
       "genEquipPmEthUtilizationPmType": genEquipPmEthUtilizationPmType,
       "genEquipPmEthUtilizationInterval": genEquipPmEthUtilizationInterval,
       "genEquipPmEthUtilizationPeakUtilization": genEquipPmEthUtilizationPeakUtilization,
       "genEquipPmEthUtilizationAverageUtilization": genEquipPmEthUtilizationAverageUtilization,
       "genEquipPmEthUtilizationExceedUtilization": genEquipPmEthUtilizationExceedUtilization,
       "genEquipPmEthUtilizationIDF": genEquipPmEthUtilizationIDF,
       "genEquipPmEthernetIngressPolicer": genEquipPmEthernetIngressPolicer,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsTable": genEquipPmEthernetIngressPolicerUnicastStatisticsTable,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsEntry": genEquipPmEthernetIngressPolicerUnicastStatisticsEntry,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex": genEquipPmEthernetIngressPolicerUnicastStatisticsIfIndex,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead": genEquipPmEthernetIngressPolicerUnicastStatisticsClearOnRead,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket": genEquipPmEthernetIngressPolicerUnicastStatisticsGreenPacket,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes": genEquipPmEthernetIngressPolicerUnicastStatisticsGreenBytes,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket": genEquipPmEthernetIngressPolicerUnicastStatisticsYellowPacket,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes": genEquipPmEthernetIngressPolicerUnicastStatisticsYellowBytes,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket": genEquipPmEthernetIngressPolicerUnicastStatisticsRedPacket,
       "genEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes": genEquipPmEthernetIngressPolicerUnicastStatisticsRedBytes,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsTable": genEquipPmEthernetIngressPolicerMulticastStatisticsTable,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsEntry": genEquipPmEthernetIngressPolicerMulticastStatisticsEntry,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex": genEquipPmEthernetIngressPolicerMulticastStatisticsIfIndex,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead": genEquipPmEthernetIngressPolicerMulticastStatisticsClearOnRead,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket": genEquipPmEthernetIngressPolicerMulticastStatisticsGreenPacket,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes": genEquipPmEthernetIngressPolicerMulticastStatisticsGreenBytes,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket": genEquipPmEthernetIngressPolicerMulticastStatisticsYellowPacket,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes": genEquipPmEthernetIngressPolicerMulticastStatisticsYellowBytes,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket": genEquipPmEthernetIngressPolicerMulticastStatisticsRedPacket,
       "genEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes": genEquipPmEthernetIngressPolicerMulticastStatisticsRedBytes,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsTable": genEquipPmEthernetIngressPolicerBroadcastStatisticsTable,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsEntry": genEquipPmEthernetIngressPolicerBroadcastStatisticsEntry,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex": genEquipPmEthernetIngressPolicerBroadcastStatisticsIfIndex,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead": genEquipPmEthernetIngressPolicerBroadcastStatisticsClearOnRead,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket": genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenPacket,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes": genEquipPmEthernetIngressPolicerBroadcastStatisticsGreenBytes,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket": genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowPacket,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes": genEquipPmEthernetIngressPolicerBroadcastStatisticsYellowBytes,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket": genEquipPmEthernetIngressPolicerBroadcastStatisticsRedPacket,
       "genEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes": genEquipPmEthernetIngressPolicerBroadcastStatisticsRedBytes,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsTable": genEquipPmEthernetIngressPolicerEtherType1StatisticsTable,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsEntry": genEquipPmEthernetIngressPolicerEtherType1StatisticsEntry,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex": genEquipPmEthernetIngressPolicerEtherType1StatisticsIfIndex,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead": genEquipPmEthernetIngressPolicerEtherType1StatisticsClearOnRead,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket": genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenPacket,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes": genEquipPmEthernetIngressPolicerEtherType1StatisticsGreenBytes,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket": genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowPacket,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes": genEquipPmEthernetIngressPolicerEtherType1StatisticsYellowBytes,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket": genEquipPmEthernetIngressPolicerEtherType1StatisticsRedPacket,
       "genEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes": genEquipPmEthernetIngressPolicerEtherType1StatisticsRedBytes,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsTable": genEquipPmEthernetIngressPolicerEtherType2StatisticsTable,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsEntry": genEquipPmEthernetIngressPolicerEtherType2StatisticsEntry,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex": genEquipPmEthernetIngressPolicerEtherType2StatisticsIfIndex,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead": genEquipPmEthernetIngressPolicerEtherType2StatisticsClearOnRead,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket": genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenPacket,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes": genEquipPmEthernetIngressPolicerEtherType2StatisticsGreenBytes,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket": genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowPacket,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes": genEquipPmEthernetIngressPolicerEtherType2StatisticsYellowBytes,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket": genEquipPmEthernetIngressPolicerEtherType2StatisticsRedPacket,
       "genEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes": genEquipPmEthernetIngressPolicerEtherType2StatisticsRedBytes,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsTable": genEquipPmEthernetIngressPolicerEtherType3StatisticsTable,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsEntry": genEquipPmEthernetIngressPolicerEtherType3StatisticsEntry,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex": genEquipPmEthernetIngressPolicerEtherType3StatisticsIfIndex,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead": genEquipPmEthernetIngressPolicerEtherType3StatisticsClearOnRead,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket": genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenPacket,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes": genEquipPmEthernetIngressPolicerEtherType3StatisticsGreenBytes,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket": genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowPacket,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes": genEquipPmEthernetIngressPolicerEtherType3StatisticsYellowBytes,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket": genEquipPmEthernetIngressPolicerEtherType3StatisticsRedPacket,
       "genEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes": genEquipPmEthernetIngressPolicerEtherType3StatisticsRedBytes,
       "genEquipPmEthernetRmonStatisticsTable": genEquipPmEthernetRmonStatisticsTable,
       "genEquipPmEthernetRmonStatisticsEntry": genEquipPmEthernetRmonStatisticsEntry,
       "genEquipPmEthernetRmonStatisticsIfIndex": genEquipPmEthernetRmonStatisticsIfIndex,
       "genEquipPmEthernetRmonStatisticsClearOnRead": genEquipPmEthernetRmonStatisticsClearOnRead,
       "genEquipPmEthernetRmonStatisticsTxByteCount": genEquipPmEthernetRmonStatisticsTxByteCount,
       "genEquipPmEthernetRmonStatisticsTxFrameCount": genEquipPmEthernetRmonStatisticsTxFrameCount,
       "genEquipPmEthernetRmonStatisticsTxMulticastFrameCount": genEquipPmEthernetRmonStatisticsTxMulticastFrameCount,
       "genEquipPmEthernetRmonStatisticsTxBroadcastFrameCount": genEquipPmEthernetRmonStatisticsTxBroadcastFrameCount,
       "genEquipPmEthernetRmonStatisticsTxControlFrameCount": genEquipPmEthernetRmonStatisticsTxControlFrameCount,
       "genEquipPmEthernetRmonStatisticsTxPauseFrameCount": genEquipPmEthernetRmonStatisticsTxPauseFrameCount,
       "genEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount": genEquipPmEthernetRmonStatisticsTxFcsErrorFrameCount,
       "genEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount": genEquipPmEthernetRmonStatisticsTxLengthErrorFrameCount,
       "genEquipPmEthernetRmonStatisticsTxOversizeFrameCount": genEquipPmEthernetRmonStatisticsTxOversizeFrameCount,
       "genEquipPmEthernetRmonStatisticsTxUndersizeFrameCount": genEquipPmEthernetRmonStatisticsTxUndersizeFrameCount,
       "genEquipPmEthernetRmonStatisticsTxFragmentFrameCount": genEquipPmEthernetRmonStatisticsTxFragmentFrameCount,
       "genEquipPmEthernetRmonStatisticsTxJabberFrameCount": genEquipPmEthernetRmonStatisticsTxJabberFrameCount,
       "genEquipPmEthernetRmonStatisticsTx64FrameCount": genEquipPmEthernetRmonStatisticsTx64FrameCount,
       "genEquipPmEthernetRmonStatisticsTx65-127FrameCount": genEquipPmEthernetRmonStatisticsTx65_127FrameCount,
       "genEquipPmEthernetRmonStatisticsTx128-255FrameCount": genEquipPmEthernetRmonStatisticsTx128_255FrameCount,
       "genEquipPmEthernetRmonStatisticsTx256-511FrameCount": genEquipPmEthernetRmonStatisticsTx256_511FrameCount,
       "genEquipPmEthernetRmonStatisticsTx512-1023FrameCount": genEquipPmEthernetRmonStatisticsTx512_1023FrameCount,
       "genEquipPmEthernetRmonStatisticsTx1024-1518FrameCount": genEquipPmEthernetRmonStatisticsTx1024_1518FrameCount,
       "genEquipPmEthernetRmonStatisticsTx1519-1522FrameCount": genEquipPmEthernetRmonStatisticsTx1519_1522FrameCount,
       "genEquipPmEthernetRmonStatisticsRxByteCount": genEquipPmEthernetRmonStatisticsRxByteCount,
       "genEquipPmEthernetRmonStatisticsRxFrameCount": genEquipPmEthernetRmonStatisticsRxFrameCount,
       "genEquipPmEthernetRmonStatisticsRxMulticastFrameCount": genEquipPmEthernetRmonStatisticsRxMulticastFrameCount,
       "genEquipPmEthernetRmonStatisticsRxBroadcastFrameCount": genEquipPmEthernetRmonStatisticsRxBroadcastFrameCount,
       "genEquipPmEthernetRmonStatisticsRxControlFrameCount": genEquipPmEthernetRmonStatisticsRxControlFrameCount,
       "genEquipPmEthernetRmonStatisticsRxPauseFrameCount": genEquipPmEthernetRmonStatisticsRxPauseFrameCount,
       "genEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount": genEquipPmEthernetRmonStatisticsRxFcsErrorFrameCount,
       "genEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount": genEquipPmEthernetRmonStatisticsRxLengthErrorFrameCount,
       "genEquipPmEthernetRmonStatisticsRxcode-ErrorCount": genEquipPmEthernetRmonStatisticsRxcode_ErrorCount,
       "genEquipPmEthernetRmonStatisticsRxoversizeFrameCount": genEquipPmEthernetRmonStatisticsRxoversizeFrameCount,
       "genEquipPmEthernetRmonStatisticsRxundersize-ErrorFrameCount": genEquipPmEthernetRmonStatisticsRxundersize_ErrorFrameCount,
       "genEquipPmEthernetRmonStatisticsRxFragmentFrameCount": genEquipPmEthernetRmonStatisticsRxFragmentFrameCount,
       "genEquipPmEthernetRmonStatisticsRx64FrameCount": genEquipPmEthernetRmonStatisticsRx64FrameCount,
       "genEquipPmEthernetRmonStatisticsRx65-127FrameCount": genEquipPmEthernetRmonStatisticsRx65_127FrameCount,
       "genEquipPmEthernetRmonStatisticsRx128-255FrameCount": genEquipPmEthernetRmonStatisticsRx128_255FrameCount,
       "genEquipPmEthernetRmonStatisticsRx256-511FrameCount": genEquipPmEthernetRmonStatisticsRx256_511FrameCount,
       "genEquipPmEthernetRmonStatisticsRx512-1023FrameCount": genEquipPmEthernetRmonStatisticsRx512_1023FrameCount,
       "genEquipPmEthernetRmonStatisticsRx1024-1518FrameCount": genEquipPmEthernetRmonStatisticsRx1024_1518FrameCount,
       "genEquipPmEthernetRmonStatisticsRx1519-1522FrameCount": genEquipPmEthernetRmonStatisticsRx1519_1522FrameCount,
       "genEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount": genEquipPmEthernetRmonStatisticsRxExceedmaxFrameCount,
       "genEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount": genEquipPmEthernetRmonStatisticsRxExceedMaxWithErrorFrameCount,
       "genEquipPmEthernetRmonStatisticsRxJabberFrameCount": genEquipPmEthernetRmonStatisticsRxJabberFrameCount,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTable": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTable,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsEntry,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsIfIndex,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsServiceIndex,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsClearOnRead,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenPacket,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBytes,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedGreenBitsPerSecond,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenPacket,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedGreenBytes,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowPacket,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBytes,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsTransmittedYellowBitsPerSecond,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowPacket,
       "genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes": genEquipServicesCETTmPmSpEgressQueuesAggragateStatisticsDroppedYellowBytes,
       "genEquipServicesCetSpPmCosIngressPolicerStatisticsTable": genEquipServicesCetSpPmCosIngressPolicerStatisticsTable,
       "genEquipServicesCetSpPmCosIngressPolicerStatisticsEntry": genEquipServicesCetSpPmCosIngressPolicerStatisticsEntry,
       "genEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex": genEquipServicesCetSpPmCosIngressPolicerStatiServiceIndex,
       "genEquipServicesCetSpPmCosIngressPolicerStatiSpIndex": genEquipServicesCetSpPmCosIngressPolicerStatiSpIndex,
       "genEquipServicesCetSpPmCosIngressPolicerStatiCos": genEquipServicesCetSpPmCosIngressPolicerStatiCos,
       "genEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead": genEquipServicesCetSpPmCosIngressPolicerStatiClearOnRead,
       "genEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket": genEquipServicesCetSpPmCosIngressPolicerStatiGreenPacket,
       "genEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes": genEquipServicesCetSpPmCosIngressPolicerStatiGreenBytes,
       "genEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket": genEquipServicesCetSpPmCosIngressPolicerStatiYellowPacket,
       "genEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes": genEquipServicesCetSpPmCosIngressPolicerStatiYellowBytes,
       "genEquipServicesCetSpPmCosIngressPolicerStatiRedPacket": genEquipServicesCetSpPmCosIngressPolicerStatiRedPacket,
       "genEquipServicesCetSpPmCosIngressPolicerStatiRedBytes": genEquipServicesCetSpPmCosIngressPolicerStatiRedBytes,
       "genEquipServicesCetSpPmIngressPolicerStatisticsTable": genEquipServicesCetSpPmIngressPolicerStatisticsTable,
       "genEquipServicesCetSpPmIngressPolicerStatisticsEntry": genEquipServicesCetSpPmIngressPolicerStatisticsEntry,
       "genEquipServicesCetSpPmIngressPolicerStatiServiceIndex": genEquipServicesCetSpPmIngressPolicerStatiServiceIndex,
       "genEquipServicesCetSpPmIngressPolicerStatiSpIndex": genEquipServicesCetSpPmIngressPolicerStatiSpIndex,
       "genEquipServicesCetSpPmIngressPolicerStatiClearOnRead": genEquipServicesCetSpPmIngressPolicerStatiClearOnRead,
       "genEquipServicesCetSpPmIngressPolicerStatiGreenPacket": genEquipServicesCetSpPmIngressPolicerStatiGreenPacket,
       "genEquipServicesCetSpPmIngressPolicerStatiGreenBytes": genEquipServicesCetSpPmIngressPolicerStatiGreenBytes,
       "genEquipServicesCetSpPmIngressPolicerStatiYellowPacket": genEquipServicesCetSpPmIngressPolicerStatiYellowPacket,
       "genEquipServicesCetSpPmIngressPolicerStatiYellowBytes": genEquipServicesCetSpPmIngressPolicerStatiYellowBytes,
       "genEquipServicesCetSpPmIngressPolicerStatiRedPacket": genEquipServicesCetSpPmIngressPolicerStatiRedPacket,
       "genEquipServicesCetSpPmIngressPolicerStatiRedBytes": genEquipServicesCetSpPmIngressPolicerStatiRedBytes,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTable": genEquipServicesCETTmPmSpEgressQueueStatisticsTable,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsEntry": genEquipServicesCETTmPmSpEgressQueueStatisticsEntry,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex": genEquipServicesCETTmPmSpEgressQueueStatisticsIfIndex,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex": genEquipServicesCETTmPmSpEgressQueueStatisticsServiceIndex,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex": genEquipServicesCETTmPmSpEgressQueueStatisticsCosQueueIndex,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead": genEquipServicesCETTmPmSpEgressQueueStatisticsClearOnRead,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket": genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenPacket,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes": genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBytes,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond": genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedGreenBitsPerSecond,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket": genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenPacket,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes": genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedGreenBytes,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket": genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowPacket,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes": genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBytes,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond": genEquipServicesCETTmPmSpEgressQueueStatisticsTransmittedYellowBitsPerSecond,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket": genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowPacket,
       "genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes": genEquipServicesCETTmPmSpEgressQueueStatisticsDroppedYellowBytes,
       "genEquipPmUtilization": genEquipPmUtilization,
       "genEquipPmUtilizationCPU": genEquipPmUtilizationCPU,
       "genEquipPmUtilizationCPUAdmin": genEquipPmUtilizationCPUAdmin,
       "genEquipPmUtilizationCPUThreshold": genEquipPmUtilizationCPUThreshold,
       "genEquipPmUtilizationCPUTable": genEquipPmUtilizationCPUTable,
       "genEquipPmUtilizationCPUEntry": genEquipPmUtilizationCPUEntry,
       "genEquipPmUtilizationCPUPmType": genEquipPmUtilizationCPUPmType,
       "genEquipPmUtilizationCPUInterval": genEquipPmUtilizationCPUInterval,
       "genEquipPmUtilizationCPUPeakUtilization": genEquipPmUtilizationCPUPeakUtilization,
       "genEquipPmUtilizationCPUAverageUtilization": genEquipPmUtilizationCPUAverageUtilization,
       "genEquipPmUtilizationCPUMinimumUtilization": genEquipPmUtilizationCPUMinimumUtilization,
       "genEquipPmUtilizationCPUExceedUtilization": genEquipPmUtilizationCPUExceedUtilization,
       "genEquipPmUtilizationCPUIDF": genEquipPmUtilizationCPUIDF,
       "genEquipPmUtilizationMem": genEquipPmUtilizationMem,
       "genEquipPmUtilizationMemAdmin": genEquipPmUtilizationMemAdmin,
       "genEquipPmUtilizationMemThreshold": genEquipPmUtilizationMemThreshold,
       "genEquipPmUtilizationMemTable": genEquipPmUtilizationMemTable,
       "genEquipPmUtilizationMemEntry": genEquipPmUtilizationMemEntry,
       "genEquipPmUtilizationMemPmType": genEquipPmUtilizationMemPmType,
       "genEquipPmUtilizationMemInterval": genEquipPmUtilizationMemInterval,
       "genEquipPmUtilizationMemPeakUtilization": genEquipPmUtilizationMemPeakUtilization,
       "genEquipPmUtilizationMemAverageUtilization": genEquipPmUtilizationMemAverageUtilization,
       "genEquipPmUtilizationMemMinimumUtilization": genEquipPmUtilizationMemMinimumUtilization,
       "genEquipPmUtilizationMemExceedUtilization": genEquipPmUtilizationMemExceedUtilization,
       "genEquipPmUtilizationMemIDF": genEquipPmUtilizationMemIDF,
       "genEquipPmEthernet": genEquipPmEthernet,
       "genEquipPmEthernetPortTable": genEquipPmEthernetPortTable,
       "genEquipPmEthernetPortEntry": genEquipPmEthernetPortEntry,
       "genEquipPmEthernetPortPmType": genEquipPmEthernetPortPmType,
       "genEquipPmEthernetPortPmInterval": genEquipPmEthernetPortPmInterval,
       "genEquipPmEthernetPortRxAvgBcastPackets": genEquipPmEthernetPortRxAvgBcastPackets,
       "genEquipPmEthernetPortRxPeakBcastPackets": genEquipPmEthernetPortRxPeakBcastPackets,
       "genEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt": genEquipPmEthernetPortRxBytesLayer1ExcedThSecCnt,
       "genEquipPmEthernetPortRxAvgBytesLayer1": genEquipPmEthernetPortRxAvgBytesLayer1,
       "genEquipPmEthernetPortRxPeakBytesLayer1": genEquipPmEthernetPortRxPeakBytesLayer1,
       "genEquipPmEthernetPortRxAvgBytesLayer2": genEquipPmEthernetPortRxAvgBytesLayer2,
       "genEquipPmEthernetPortRxPeakBytesLayer2": genEquipPmEthernetPortRxPeakBytesLayer2,
       "genEquipPmEthernetPortRxAvgMcastPackets": genEquipPmEthernetPortRxAvgMcastPackets,
       "genEquipPmEthernetPortRxPeakMcastPackets": genEquipPmEthernetPortRxPeakMcastPackets,
       "genEquipPmEthernetPortRxAvgPackets": genEquipPmEthernetPortRxAvgPackets,
       "genEquipPmEthernetPortRxPeakPackets": genEquipPmEthernetPortRxPeakPackets,
       "genEquipPmEthernetPortTxAvgBcastPackets": genEquipPmEthernetPortTxAvgBcastPackets,
       "genEquipPmEthernetPortTxPeakBcastPackets": genEquipPmEthernetPortTxPeakBcastPackets,
       "genEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt": genEquipPmEthernetPortTxBytesLayer1ExcedThSecCnt,
       "genEquipPmEthernetPortTxAvgBytesLayer1": genEquipPmEthernetPortTxAvgBytesLayer1,
       "genEquipPmEthernetPortTxPeakBytesLayer1": genEquipPmEthernetPortTxPeakBytesLayer1,
       "genEquipPmEthernetPortTxAvgBytesLayer2": genEquipPmEthernetPortTxAvgBytesLayer2,
       "genEquipPmEthernetPortTxPeakBytesLayer2": genEquipPmEthernetPortTxPeakBytesLayer2,
       "genEquipPmEthernetPortTxAvgMcastPackets": genEquipPmEthernetPortTxAvgMcastPackets,
       "genEquipPmEthernetPortTxPeakMcastPackets": genEquipPmEthernetPortTxPeakMcastPackets,
       "genEquipPmEthernetPortTxAvgPackets": genEquipPmEthernetPortTxAvgPackets,
       "genEquipPmEthernetPortTxPeakPackets": genEquipPmEthernetPortTxPeakPackets,
       "genEquipPmEthernetPortPmIDF": genEquipPmEthernetPortPmIDF,
       "genEquipPMStatistics": genEquipPMStatistics,
       "genEquipRMONResetCounters": genEquipRMONResetCounters,
       "genEquipPMStatisticsResetAllL2PortPm": genEquipPMStatisticsResetAllL2PortPm}
)
