# SNMP MIB module (ADTRAN-ATLAS-T1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-T1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:25 2024
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

(adATLASModuleInfoFPStatus,) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-MODULE-MIB",
    "adATLASModuleInfoFPStatus")

(adATLASUnitFPStatus,
 adATLASUnitPortAddress,
 adATLASUnitSlotAddress) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-UNIT-MIB",
    "adATLASUnitFPStatus",
    "adATLASUnitPortAddress",
    "adATLASUnitSlotAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dsx1LineStatus,) = mibBuilder.importSymbols(
    "RFC1406-MIB",
    "dsx1LineStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLAST1mg_ObjectIdentity = ObjectIdentity
adATLAST1mg = _AdATLAST1mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9)
)
_AdATLAST1IfNumber_Type = Integer32
_AdATLAST1IfNumber_Object = MibScalar
adATLAST1IfNumber = _AdATLAST1IfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 1),
    _AdATLAST1IfNumber_Type()
)
adATLAST1IfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfNumber.setStatus("mandatory")
_AdATLAST1IfTable_Object = MibTable
adATLAST1IfTable = _AdATLAST1IfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2)
)
if mibBuilder.loadTexts:
    adATLAST1IfTable.setStatus("mandatory")
_AdATLAST1IfEntry_Object = MibTableRow
adATLAST1IfEntry = _AdATLAST1IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1)
)
adATLAST1IfEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfIndex"),
)
if mibBuilder.loadTexts:
    adATLAST1IfEntry.setStatus("mandatory")
_AdATLAST1IfIndex_Type = Integer32
_AdATLAST1IfIndex_Object = MibTableColumn
adATLAST1IfIndex = _AdATLAST1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 1),
    _AdATLAST1IfIndex_Type()
)
adATLAST1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfIndex.setStatus("mandatory")
_AdATLAST1IfSlotNum_Type = Integer32
_AdATLAST1IfSlotNum_Object = MibTableColumn
adATLAST1IfSlotNum = _AdATLAST1IfSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 2),
    _AdATLAST1IfSlotNum_Type()
)
adATLAST1IfSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfSlotNum.setStatus("mandatory")
_AdATLAST1IfPortNum_Type = Integer32
_AdATLAST1IfPortNum_Object = MibTableColumn
adATLAST1IfPortNum = _AdATLAST1IfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 3),
    _AdATLAST1IfPortNum_Type()
)
adATLAST1IfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfPortNum.setStatus("mandatory")
_AdATLAST1IfAlarmStatus_Type = Integer32
_AdATLAST1IfAlarmStatus_Object = MibTableColumn
adATLAST1IfAlarmStatus = _AdATLAST1IfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 4),
    _AdATLAST1IfAlarmStatus_Type()
)
adATLAST1IfAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfAlarmStatus.setStatus("mandatory")


class _AdATLAST1IfRxLevel_Type(Integer32):
    """Custom type adATLAST1IfRxLevel based on Integer32"""
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
        *(("neg15db", 3),
          ("neg22pt5db", 4),
          ("neg7pt5db", 2),
          ("zerodb", 1))
    )


_AdATLAST1IfRxLevel_Type.__name__ = "Integer32"
_AdATLAST1IfRxLevel_Object = MibTableColumn
adATLAST1IfRxLevel = _AdATLAST1IfRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 5),
    _AdATLAST1IfRxLevel_Type()
)
adATLAST1IfRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfRxLevel.setStatus("mandatory")
_AdATLAST1IfCurrentLOFC_Type = Counter32
_AdATLAST1IfCurrentLOFC_Object = MibTableColumn
adATLAST1IfCurrentLOFC = _AdATLAST1IfCurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 6),
    _AdATLAST1IfCurrentLOFC_Type()
)
adATLAST1IfCurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfCurrentLOFC.setStatus("mandatory")
_AdATLAST1IfTotalLOFC_Type = Counter32
_AdATLAST1IfTotalLOFC_Object = MibTableColumn
adATLAST1IfTotalLOFC = _AdATLAST1IfTotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 7),
    _AdATLAST1IfTotalLOFC_Type()
)
adATLAST1IfTotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfTotalLOFC.setStatus("mandatory")


class _AdATLAST1IfResetPRMStats_Type(Integer32):
    """Custom type adATLAST1IfResetPRMStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdATLAST1IfResetPRMStats_Type.__name__ = "Integer32"
_AdATLAST1IfResetPRMStats_Object = MibTableColumn
adATLAST1IfResetPRMStats = _AdATLAST1IfResetPRMStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 2, 1, 8),
    _AdATLAST1IfResetPRMStats_Type()
)
adATLAST1IfResetPRMStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAST1IfResetPRMStats.setStatus("mandatory")
_AdATLAST1IfIntervalTable_Object = MibTable
adATLAST1IfIntervalTable = _AdATLAST1IfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3)
)
if mibBuilder.loadTexts:
    adATLAST1IfIntervalTable.setStatus("mandatory")
_AdATLAST1IfIntervalEntry_Object = MibTableRow
adATLAST1IfIntervalEntry = _AdATLAST1IfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1)
)
adATLAST1IfIntervalEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfIntervalIndex"),
    (0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfIntervalNumber"),
)
if mibBuilder.loadTexts:
    adATLAST1IfIntervalEntry.setStatus("mandatory")
_AdATLAST1IfIntervalIndex_Type = Integer32
_AdATLAST1IfIntervalIndex_Object = MibTableColumn
adATLAST1IfIntervalIndex = _AdATLAST1IfIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1, 1),
    _AdATLAST1IfIntervalIndex_Type()
)
adATLAST1IfIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfIntervalIndex.setStatus("mandatory")
_AdATLAST1IfIntervalNumber_Type = Integer32
_AdATLAST1IfIntervalNumber_Object = MibTableColumn
adATLAST1IfIntervalNumber = _AdATLAST1IfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1, 2),
    _AdATLAST1IfIntervalNumber_Type()
)
adATLAST1IfIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfIntervalNumber.setStatus("mandatory")
_AdATLAST1IfIntervalLOFC_Type = Counter32
_AdATLAST1IfIntervalLOFC_Object = MibTableColumn
adATLAST1IfIntervalLOFC = _AdATLAST1IfIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 3, 1, 3),
    _AdATLAST1IfIntervalLOFC_Type()
)
adATLAST1IfIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfIntervalLOFC.setStatus("mandatory")
_AdATLAST1IfDS0Table_Object = MibTable
adATLAST1IfDS0Table = _AdATLAST1IfDS0Table_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4)
)
if mibBuilder.loadTexts:
    adATLAST1IfDS0Table.setStatus("mandatory")
_AdATLAST1IfDS0Entry_Object = MibTableRow
adATLAST1IfDS0Entry = _AdATLAST1IfDS0Entry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1)
)
adATLAST1IfDS0Entry.setIndexNames(
    (0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1IfDS0Index"),
)
if mibBuilder.loadTexts:
    adATLAST1IfDS0Entry.setStatus("mandatory")
_AdATLAST1IfDS0Index_Type = Integer32
_AdATLAST1IfDS0Index_Object = MibTableColumn
adATLAST1IfDS0Index = _AdATLAST1IfDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 1),
    _AdATLAST1IfDS0Index_Type()
)
adATLAST1IfDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0Index.setStatus("mandatory")


class _AdATLAST1IfDS0Status_Type(OctetString):
    """Custom type adATLAST1IfDS0Status based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AdATLAST1IfDS0Status_Type.__name__ = "OctetString"
_AdATLAST1IfDS0Status_Object = MibTableColumn
adATLAST1IfDS0Status = _AdATLAST1IfDS0Status_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 2),
    _AdATLAST1IfDS0Status_Type()
)
adATLAST1IfDS0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0Status.setStatus("mandatory")


class _AdATLAST1IfDS0Alarm_Type(OctetString):
    """Custom type adATLAST1IfDS0Alarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AdATLAST1IfDS0Alarm_Type.__name__ = "OctetString"
_AdATLAST1IfDS0Alarm_Object = MibTableColumn
adATLAST1IfDS0Alarm = _AdATLAST1IfDS0Alarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 3),
    _AdATLAST1IfDS0Alarm_Type()
)
adATLAST1IfDS0Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0Alarm.setStatus("mandatory")


class _AdATLAST1IfDS0RxSignalStatusA_Type(OctetString):
    """Custom type adATLAST1IfDS0RxSignalStatusA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AdATLAST1IfDS0RxSignalStatusA_Type.__name__ = "OctetString"
_AdATLAST1IfDS0RxSignalStatusA_Object = MibTableColumn
adATLAST1IfDS0RxSignalStatusA = _AdATLAST1IfDS0RxSignalStatusA_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 4),
    _AdATLAST1IfDS0RxSignalStatusA_Type()
)
adATLAST1IfDS0RxSignalStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0RxSignalStatusA.setStatus("mandatory")


class _AdATLAST1IfDS0RxSignalStatusB_Type(OctetString):
    """Custom type adATLAST1IfDS0RxSignalStatusB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AdATLAST1IfDS0RxSignalStatusB_Type.__name__ = "OctetString"
_AdATLAST1IfDS0RxSignalStatusB_Object = MibTableColumn
adATLAST1IfDS0RxSignalStatusB = _AdATLAST1IfDS0RxSignalStatusB_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 5),
    _AdATLAST1IfDS0RxSignalStatusB_Type()
)
adATLAST1IfDS0RxSignalStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0RxSignalStatusB.setStatus("mandatory")


class _AdATLAST1IfDS0TxSignalStatusA_Type(OctetString):
    """Custom type adATLAST1IfDS0TxSignalStatusA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AdATLAST1IfDS0TxSignalStatusA_Type.__name__ = "OctetString"
_AdATLAST1IfDS0TxSignalStatusA_Object = MibTableColumn
adATLAST1IfDS0TxSignalStatusA = _AdATLAST1IfDS0TxSignalStatusA_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 6),
    _AdATLAST1IfDS0TxSignalStatusA_Type()
)
adATLAST1IfDS0TxSignalStatusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0TxSignalStatusA.setStatus("mandatory")


class _AdATLAST1IfDS0TxSignalStatusB_Type(OctetString):
    """Custom type adATLAST1IfDS0TxSignalStatusB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AdATLAST1IfDS0TxSignalStatusB_Type.__name__ = "OctetString"
_AdATLAST1IfDS0TxSignalStatusB_Object = MibTableColumn
adATLAST1IfDS0TxSignalStatusB = _AdATLAST1IfDS0TxSignalStatusB_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 4, 1, 7),
    _AdATLAST1IfDS0TxSignalStatusB_Type()
)
adATLAST1IfDS0TxSignalStatusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1IfDS0TxSignalStatusB.setStatus("mandatory")
_AdATLAST1TstTable_Object = MibTable
adATLAST1TstTable = _AdATLAST1TstTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5)
)
if mibBuilder.loadTexts:
    adATLAST1TstTable.setStatus("mandatory")
_AdATLAST1TstEntry_Object = MibTableRow
adATLAST1TstEntry = _AdATLAST1TstEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1)
)
adATLAST1TstEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-T1-MIB", "adATLAST1TstIndex"),
)
if mibBuilder.loadTexts:
    adATLAST1TstEntry.setStatus("mandatory")
_AdATLAST1TstIndex_Type = Integer32
_AdATLAST1TstIndex_Object = MibTableColumn
adATLAST1TstIndex = _AdATLAST1TstIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 1),
    _AdATLAST1TstIndex_Type()
)
adATLAST1TstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstIndex.setStatus("mandatory")


class _AdATLAST1TstLocalLpBk_Type(Integer32):
    """Custom type adATLAST1TstLocalLpBk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("line", 3),
          ("none", 1),
          ("payload", 2))
    )


_AdATLAST1TstLocalLpBk_Type.__name__ = "Integer32"
_AdATLAST1TstLocalLpBk_Object = MibTableColumn
adATLAST1TstLocalLpBk = _AdATLAST1TstLocalLpBk_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 2),
    _AdATLAST1TstLocalLpBk_Type()
)
adATLAST1TstLocalLpBk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAST1TstLocalLpBk.setStatus("mandatory")


class _AdATLAST1TstRemoteLpBk_Type(Integer32):
    """Custom type adATLAST1TstRemoteLpBk based on Integer32"""
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
        *(("ansiFDLLine", 3),
          ("ansiFDLPayload", 4),
          ("attInbandLine", 2),
          ("inbandNIU", 5),
          ("none", 1))
    )


_AdATLAST1TstRemoteLpBk_Type.__name__ = "Integer32"
_AdATLAST1TstRemoteLpBk_Object = MibTableColumn
adATLAST1TstRemoteLpBk = _AdATLAST1TstRemoteLpBk_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 3),
    _AdATLAST1TstRemoteLpBk_Type()
)
adATLAST1TstRemoteLpBk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAST1TstRemoteLpBk.setStatus("mandatory")


class _AdATLAST1TstRemoteLpBkStatus_Type(Integer32):
    """Custom type adATLAST1TstRemoteLpBkStatus based on Integer32"""
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
        *(("noRemoteLoops", 1),
          ("remLpDwnDone", 8),
          ("remLpDwnInProgress", 7),
          ("remLpDwnStarted", 6),
          ("remLpUpDone", 5),
          ("remLpUpInProgress", 3),
          ("remLpUpStarted", 2),
          ("remLpUpTimeout", 4))
    )


_AdATLAST1TstRemoteLpBkStatus_Type.__name__ = "Integer32"
_AdATLAST1TstRemoteLpBkStatus_Object = MibTableColumn
adATLAST1TstRemoteLpBkStatus = _AdATLAST1TstRemoteLpBkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 4),
    _AdATLAST1TstRemoteLpBkStatus_Type()
)
adATLAST1TstRemoteLpBkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstRemoteLpBkStatus.setStatus("mandatory")


class _AdATLAST1TstPattern_Type(Integer32):
    """Custom type adATLAST1TstPattern based on Integer32"""
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
        *(("allOnes", 2),
          ("allZeros", 3),
          ("none", 1),
          ("qRSS", 4))
    )


_AdATLAST1TstPattern_Type.__name__ = "Integer32"
_AdATLAST1TstPattern_Object = MibTableColumn
adATLAST1TstPattern = _AdATLAST1TstPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 5),
    _AdATLAST1TstPattern_Type()
)
adATLAST1TstPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAST1TstPattern.setStatus("mandatory")


class _AdATLAST1TstPatternSync_Type(Integer32):
    """Custom type adATLAST1TstPatternSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 2),
          ("synced", 1))
    )


_AdATLAST1TstPatternSync_Type.__name__ = "Integer32"
_AdATLAST1TstPatternSync_Object = MibTableColumn
adATLAST1TstPatternSync = _AdATLAST1TstPatternSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 6),
    _AdATLAST1TstPatternSync_Type()
)
adATLAST1TstPatternSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstPatternSync.setStatus("mandatory")


class _AdATLAST1TstPatternSyncLost_Type(Integer32):
    """Custom type adATLAST1TstPatternSyncLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncLost", 1),
          ("syncNotLost", 2))
    )


_AdATLAST1TstPatternSyncLost_Type.__name__ = "Integer32"
_AdATLAST1TstPatternSyncLost_Object = MibTableColumn
adATLAST1TstPatternSyncLost = _AdATLAST1TstPatternSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 7),
    _AdATLAST1TstPatternSyncLost_Type()
)
adATLAST1TstPatternSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstPatternSyncLost.setStatus("mandatory")
_AdATLAST1TstPatternESs_Type = Counter32
_AdATLAST1TstPatternESs_Object = MibTableColumn
adATLAST1TstPatternESs = _AdATLAST1TstPatternESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 8),
    _AdATLAST1TstPatternESs_Type()
)
adATLAST1TstPatternESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstPatternESs.setStatus("mandatory")
_AdATLAST1TstPatternBESs_Type = Counter32
_AdATLAST1TstPatternBESs_Object = MibTableColumn
adATLAST1TstPatternBESs = _AdATLAST1TstPatternBESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 9),
    _AdATLAST1TstPatternBESs_Type()
)
adATLAST1TstPatternBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstPatternBESs.setStatus("mandatory")
_AdATLAST1TstPatternSESs_Type = Counter32
_AdATLAST1TstPatternSESs_Object = MibTableColumn
adATLAST1TstPatternSESs = _AdATLAST1TstPatternSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 10),
    _AdATLAST1TstPatternSESs_Type()
)
adATLAST1TstPatternSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLAST1TstPatternSESs.setStatus("mandatory")


class _AdATLAST1TstClearResults_Type(Integer32):
    """Custom type adATLAST1TstClearResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdATLAST1TstClearResults_Type.__name__ = "Integer32"
_AdATLAST1TstClearResults_Object = MibTableColumn
adATLAST1TstClearResults = _AdATLAST1TstClearResults_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 11),
    _AdATLAST1TstClearResults_Type()
)
adATLAST1TstClearResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAST1TstClearResults.setStatus("mandatory")


class _AdATLAST1TstInjectError_Type(Integer32):
    """Custom type adATLAST1TstInjectError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("inject", 1)
    )


_AdATLAST1TstInjectError_Type.__name__ = "Integer32"
_AdATLAST1TstInjectError_Object = MibTableColumn
adATLAST1TstInjectError = _AdATLAST1TstInjectError_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 9, 5, 1, 12),
    _AdATLAST1TstInjectError_Type()
)
adATLAST1TstInjectError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLAST1TstInjectError.setStatus("mandatory")

# Managed Objects groups


# Notification objects

adATLAST1RxYellowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400900)
)
adATLAST1RxYellowActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1RxYellowActive.setStatus(
        ""
    )

adATLAST1RxYellowInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400901)
)
adATLAST1RxYellowInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1RxYellowInActive.setStatus(
        ""
    )

adATLAST1RxAISActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400902)
)
adATLAST1RxAISActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1RxAISActive.setStatus(
        ""
    )

adATLAST1RxAISInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400903)
)
adATLAST1RxAISInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1RxAISInActive.setStatus(
        ""
    )

adATLAST1RedAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400904)
)
adATLAST1RedAlarmActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1RedAlarmActive.setStatus(
        ""
    )

adATLAST1RedAlarmInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400905)
)
adATLAST1RedAlarmInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1RedAlarmInActive.setStatus(
        ""
    )

adATLAST1LOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400906)
)
adATLAST1LOSActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1LOSActive.setStatus(
        ""
    )

adATLAST1LOSInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400907)
)
adATLAST1LOSInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1LOSInActive.setStatus(
        ""
    )

adATLAST1TxAISActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400908)
)
adATLAST1TxAISActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TxAISActive.setStatus(
        ""
    )

adATLAST1TxAISInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400909)
)
adATLAST1TxAISInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TxAISInActive.setStatus(
        ""
    )

adATLAST1TxYellowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400910)
)
adATLAST1TxYellowActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TxYellowActive.setStatus(
        ""
    )

adATLAST1TxYellowInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400911)
)
adATLAST1TxYellowInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TxYellowInActive.setStatus(
        ""
    )

adATLAST1CurrentES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400912)
)
adATLAST1CurrentES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentES.setStatus(
        ""
    )

adATLAST1CurrentSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400913)
)
adATLAST1CurrentSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentSES.setStatus(
        ""
    )

adATLAST1CurrentSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400914)
)
adATLAST1CurrentSEFS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentSEFS.setStatus(
        ""
    )

adATLAST1CurrentUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400915)
)
adATLAST1CurrentUAS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentUAS.setStatus(
        ""
    )

adATLAST1CurrentCSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400916)
)
adATLAST1CurrentCSS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentCSS.setStatus(
        ""
    )

adATLAST1CurrentPCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400917)
)
adATLAST1CurrentPCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentPCV.setStatus(
        ""
    )

adATLAST1CurrentLES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400918)
)
adATLAST1CurrentLES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentLES.setStatus(
        ""
    )

adATLAST1CurrentLCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400919)
)
adATLAST1CurrentLCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1CurrentLCV.setStatus(
        ""
    )

adATLAST1TotalES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400920)
)
adATLAST1TotalES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalES.setStatus(
        ""
    )

adATLAST1TotalSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400921)
)
adATLAST1TotalSES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalSES.setStatus(
        ""
    )

adATLAST1TotalSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400922)
)
adATLAST1TotalSEFS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalSEFS.setStatus(
        ""
    )

adATLAST1TotalUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400923)
)
adATLAST1TotalUAS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalUAS.setStatus(
        ""
    )

adATLAST1TotalCSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400924)
)
adATLAST1TotalCSS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalCSS.setStatus(
        ""
    )

adATLAST1TotalPCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400925)
)
adATLAST1TotalPCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalPCV.setStatus(
        ""
    )

adATLAST1TotalLES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400926)
)
adATLAST1TotalLES.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalLES.setStatus(
        ""
    )

adATLAST1TotalLCV = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400927)
)
adATLAST1TotalLCV.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("RFC1406-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    adATLAST1TotalLCV.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-T1-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adATLAST1RxYellowActive": adATLAST1RxYellowActive,
       "adATLAST1RxYellowInActive": adATLAST1RxYellowInActive,
       "adATLAST1RxAISActive": adATLAST1RxAISActive,
       "adATLAST1RxAISInActive": adATLAST1RxAISInActive,
       "adATLAST1RedAlarmActive": adATLAST1RedAlarmActive,
       "adATLAST1RedAlarmInActive": adATLAST1RedAlarmInActive,
       "adATLAST1LOSActive": adATLAST1LOSActive,
       "adATLAST1LOSInActive": adATLAST1LOSInActive,
       "adATLAST1TxAISActive": adATLAST1TxAISActive,
       "adATLAST1TxAISInActive": adATLAST1TxAISInActive,
       "adATLAST1TxYellowActive": adATLAST1TxYellowActive,
       "adATLAST1TxYellowInActive": adATLAST1TxYellowInActive,
       "adATLAST1CurrentES": adATLAST1CurrentES,
       "adATLAST1CurrentSES": adATLAST1CurrentSES,
       "adATLAST1CurrentSEFS": adATLAST1CurrentSEFS,
       "adATLAST1CurrentUAS": adATLAST1CurrentUAS,
       "adATLAST1CurrentCSS": adATLAST1CurrentCSS,
       "adATLAST1CurrentPCV": adATLAST1CurrentPCV,
       "adATLAST1CurrentLES": adATLAST1CurrentLES,
       "adATLAST1CurrentLCV": adATLAST1CurrentLCV,
       "adATLAST1TotalES": adATLAST1TotalES,
       "adATLAST1TotalSES": adATLAST1TotalSES,
       "adATLAST1TotalSEFS": adATLAST1TotalSEFS,
       "adATLAST1TotalUAS": adATLAST1TotalUAS,
       "adATLAST1TotalCSS": adATLAST1TotalCSS,
       "adATLAST1TotalPCV": adATLAST1TotalPCV,
       "adATLAST1TotalLES": adATLAST1TotalLES,
       "adATLAST1TotalLCV": adATLAST1TotalLCV,
       "adGenATLASmg": adGenATLASmg,
       "adATLAST1mg": adATLAST1mg,
       "adATLAST1IfNumber": adATLAST1IfNumber,
       "adATLAST1IfTable": adATLAST1IfTable,
       "adATLAST1IfEntry": adATLAST1IfEntry,
       "adATLAST1IfIndex": adATLAST1IfIndex,
       "adATLAST1IfSlotNum": adATLAST1IfSlotNum,
       "adATLAST1IfPortNum": adATLAST1IfPortNum,
       "adATLAST1IfAlarmStatus": adATLAST1IfAlarmStatus,
       "adATLAST1IfRxLevel": adATLAST1IfRxLevel,
       "adATLAST1IfCurrentLOFC": adATLAST1IfCurrentLOFC,
       "adATLAST1IfTotalLOFC": adATLAST1IfTotalLOFC,
       "adATLAST1IfResetPRMStats": adATLAST1IfResetPRMStats,
       "adATLAST1IfIntervalTable": adATLAST1IfIntervalTable,
       "adATLAST1IfIntervalEntry": adATLAST1IfIntervalEntry,
       "adATLAST1IfIntervalIndex": adATLAST1IfIntervalIndex,
       "adATLAST1IfIntervalNumber": adATLAST1IfIntervalNumber,
       "adATLAST1IfIntervalLOFC": adATLAST1IfIntervalLOFC,
       "adATLAST1IfDS0Table": adATLAST1IfDS0Table,
       "adATLAST1IfDS0Entry": adATLAST1IfDS0Entry,
       "adATLAST1IfDS0Index": adATLAST1IfDS0Index,
       "adATLAST1IfDS0Status": adATLAST1IfDS0Status,
       "adATLAST1IfDS0Alarm": adATLAST1IfDS0Alarm,
       "adATLAST1IfDS0RxSignalStatusA": adATLAST1IfDS0RxSignalStatusA,
       "adATLAST1IfDS0RxSignalStatusB": adATLAST1IfDS0RxSignalStatusB,
       "adATLAST1IfDS0TxSignalStatusA": adATLAST1IfDS0TxSignalStatusA,
       "adATLAST1IfDS0TxSignalStatusB": adATLAST1IfDS0TxSignalStatusB,
       "adATLAST1TstTable": adATLAST1TstTable,
       "adATLAST1TstEntry": adATLAST1TstEntry,
       "adATLAST1TstIndex": adATLAST1TstIndex,
       "adATLAST1TstLocalLpBk": adATLAST1TstLocalLpBk,
       "adATLAST1TstRemoteLpBk": adATLAST1TstRemoteLpBk,
       "adATLAST1TstRemoteLpBkStatus": adATLAST1TstRemoteLpBkStatus,
       "adATLAST1TstPattern": adATLAST1TstPattern,
       "adATLAST1TstPatternSync": adATLAST1TstPatternSync,
       "adATLAST1TstPatternSyncLost": adATLAST1TstPatternSyncLost,
       "adATLAST1TstPatternESs": adATLAST1TstPatternESs,
       "adATLAST1TstPatternBESs": adATLAST1TstPatternBESs,
       "adATLAST1TstPatternSESs": adATLAST1TstPatternSESs,
       "adATLAST1TstClearResults": adATLAST1TstClearResults,
       "adATLAST1TstInjectError": adATLAST1TstInjectError}
)
