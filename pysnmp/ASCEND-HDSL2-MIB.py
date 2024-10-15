# SNMP MIB module (ASCEND-HDSL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-HDSL2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:58 2024
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

(wanTypeHdsl2,) = mibBuilder.importSymbols(
    "ASCEND-WAN-MIB",
    "wanTypeHdsl2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hdsl2LineStatusTable_Object = MibTable
hdsl2LineStatusTable = _Hdsl2LineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1)
)
if mibBuilder.loadTexts:
    hdsl2LineStatusTable.setStatus("mandatory")
_Hdsl2LineStatusEntry_Object = MibTableRow
hdsl2LineStatusEntry = _Hdsl2LineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1)
)
hdsl2LineStatusEntry.setIndexNames(
    (0, "ASCEND-HDSL2-MIB", "hdsl2StatusIfEntryIndex"),
)
if mibBuilder.loadTexts:
    hdsl2LineStatusEntry.setStatus("mandatory")
_Hdsl2StatusIfEntryIndex_Type = Integer32
_Hdsl2StatusIfEntryIndex_Object = MibTableColumn
hdsl2StatusIfEntryIndex = _Hdsl2StatusIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 1),
    _Hdsl2StatusIfEntryIndex_Type()
)
hdsl2StatusIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusIfEntryIndex.setStatus("mandatory")
_Hdsl2StatusShelfIndex_Type = Integer32
_Hdsl2StatusShelfIndex_Object = MibTableColumn
hdsl2StatusShelfIndex = _Hdsl2StatusShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 2),
    _Hdsl2StatusShelfIndex_Type()
)
hdsl2StatusShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusShelfIndex.setStatus("mandatory")
_Hdsl2StatusSlotIndex_Type = Integer32
_Hdsl2StatusSlotIndex_Object = MibTableColumn
hdsl2StatusSlotIndex = _Hdsl2StatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 3),
    _Hdsl2StatusSlotIndex_Type()
)
hdsl2StatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusSlotIndex.setStatus("mandatory")
_Hdsl2StatusLineIndex_Type = Integer32
_Hdsl2StatusLineIndex_Object = MibTableColumn
hdsl2StatusLineIndex = _Hdsl2StatusLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 4),
    _Hdsl2StatusLineIndex_Type()
)
hdsl2StatusLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusLineIndex.setStatus("mandatory")


class _Hdsl2StatusUnitType_Type(Integer32):
    """Custom type hdsl2StatusUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coe", 2),
          ("cpe", 3),
          ("other", 1))
    )


_Hdsl2StatusUnitType_Type.__name__ = "Integer32"
_Hdsl2StatusUnitType_Object = MibTableColumn
hdsl2StatusUnitType = _Hdsl2StatusUnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 5),
    _Hdsl2StatusUnitType_Type()
)
hdsl2StatusUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusUnitType.setStatus("mandatory")


class _Hdsl2StatusLineState_Type(Integer32):
    """Custom type hdsl2StatusLineState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("analog-loopback", 10),
          ("configure", 2),
          ("deactivate", 3),
          ("deactive-lost", 4),
          ("digital-loopback", 11),
          ("other", 1),
          ("out-of-service", 9),
          ("pend-deactivate", 8),
          ("pend-port-up", 6),
          ("start-up", 5),
          ("up", 7))
    )


_Hdsl2StatusLineState_Type.__name__ = "Integer32"
_Hdsl2StatusLineState_Object = MibTableColumn
hdsl2StatusLineState = _Hdsl2StatusLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 6),
    _Hdsl2StatusLineState_Type()
)
hdsl2StatusLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusLineState.setStatus("mandatory")


class _Hdsl2StatusOpRate_Type(Integer32):
    """Custom type hdsl2StatusOpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1552000
        )
    )
    namedValues = NamedValues(
        ("m1552000", 1552000)
    )


_Hdsl2StatusOpRate_Type.__name__ = "Integer32"
_Hdsl2StatusOpRate_Object = MibTableColumn
hdsl2StatusOpRate = _Hdsl2StatusOpRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 7),
    _Hdsl2StatusOpRate_Type()
)
hdsl2StatusOpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2StatusOpRate.setStatus("mandatory")
_Hdsl2StatusVendorId_Type = Integer32
_Hdsl2StatusVendorId_Object = MibTableColumn
hdsl2StatusVendorId = _Hdsl2StatusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 8),
    _Hdsl2StatusVendorId_Type()
)
hdsl2StatusVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusVendorId.setStatus("mandatory")
_Hdsl2StatusMajorFirmWareVer_Type = Integer32
_Hdsl2StatusMajorFirmWareVer_Object = MibTableColumn
hdsl2StatusMajorFirmWareVer = _Hdsl2StatusMajorFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 9),
    _Hdsl2StatusMajorFirmWareVer_Type()
)
hdsl2StatusMajorFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusMajorFirmWareVer.setStatus("mandatory")
_Hdsl2StatusMinorFirmWareVer_Type = Integer32
_Hdsl2StatusMinorFirmWareVer_Object = MibTableColumn
hdsl2StatusMinorFirmWareVer = _Hdsl2StatusMinorFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 10),
    _Hdsl2StatusMinorFirmWareVer_Type()
)
hdsl2StatusMinorFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusMinorFirmWareVer.setStatus("mandatory")
_Hdsl2StatusHardWareVer_Type = Integer32
_Hdsl2StatusHardWareVer_Object = MibTableColumn
hdsl2StatusHardWareVer = _Hdsl2StatusHardWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 11),
    _Hdsl2StatusHardWareVer_Type()
)
hdsl2StatusHardWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatusHardWareVer.setStatus("mandatory")
_Hdsl2LineStatisticTable_Object = MibTable
hdsl2LineStatisticTable = _Hdsl2LineStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2)
)
if mibBuilder.loadTexts:
    hdsl2LineStatisticTable.setStatus("mandatory")
_Hdsl2LineStatisticEntry_Object = MibTableRow
hdsl2LineStatisticEntry = _Hdsl2LineStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1)
)
hdsl2LineStatisticEntry.setIndexNames(
    (0, "ASCEND-HDSL2-MIB", "hdsl2StatIfEntryIndex"),
)
if mibBuilder.loadTexts:
    hdsl2LineStatisticEntry.setStatus("mandatory")
_Hdsl2StatIfEntryIndex_Type = Integer32
_Hdsl2StatIfEntryIndex_Object = MibTableColumn
hdsl2StatIfEntryIndex = _Hdsl2StatIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 1),
    _Hdsl2StatIfEntryIndex_Type()
)
hdsl2StatIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatIfEntryIndex.setStatus("mandatory")
_Hdsl2StatShelfIndex_Type = Integer32
_Hdsl2StatShelfIndex_Object = MibTableColumn
hdsl2StatShelfIndex = _Hdsl2StatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 2),
    _Hdsl2StatShelfIndex_Type()
)
hdsl2StatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatShelfIndex.setStatus("mandatory")
_Hdsl2StatSlotIndex_Type = Integer32
_Hdsl2StatSlotIndex_Object = MibTableColumn
hdsl2StatSlotIndex = _Hdsl2StatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 3),
    _Hdsl2StatSlotIndex_Type()
)
hdsl2StatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatSlotIndex.setStatus("mandatory")
_Hdsl2StatLineIndex_Type = Integer32
_Hdsl2StatLineIndex_Object = MibTableColumn
hdsl2StatLineIndex = _Hdsl2StatLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 4),
    _Hdsl2StatLineIndex_Type()
)
hdsl2StatLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatLineIndex.setStatus("mandatory")
_Hdsl2StatConnUpDays_Type = Integer32
_Hdsl2StatConnUpDays_Object = MibTableColumn
hdsl2StatConnUpDays = _Hdsl2StatConnUpDays_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 5),
    _Hdsl2StatConnUpDays_Type()
)
hdsl2StatConnUpDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatConnUpDays.setStatus("mandatory")
_Hdsl2StatConnUpHours_Type = Integer32
_Hdsl2StatConnUpHours_Object = MibTableColumn
hdsl2StatConnUpHours = _Hdsl2StatConnUpHours_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 6),
    _Hdsl2StatConnUpHours_Type()
)
hdsl2StatConnUpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatConnUpHours.setStatus("mandatory")
_Hdsl2StatConnUpMinutes_Type = Integer32
_Hdsl2StatConnUpMinutes_Object = MibTableColumn
hdsl2StatConnUpMinutes = _Hdsl2StatConnUpMinutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 7),
    _Hdsl2StatConnUpMinutes_Type()
)
hdsl2StatConnUpMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatConnUpMinutes.setStatus("mandatory")


class _Hdsl2StatRxSignalPresent_Type(Integer32):
    """Custom type hdsl2StatRxSignalPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Hdsl2StatRxSignalPresent_Type.__name__ = "Integer32"
_Hdsl2StatRxSignalPresent_Object = MibTableColumn
hdsl2StatRxSignalPresent = _Hdsl2StatRxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 8),
    _Hdsl2StatRxSignalPresent_Type()
)
hdsl2StatRxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatRxSignalPresent.setStatus("mandatory")
_Hdsl2StatLineQualityDb_Type = Integer32
_Hdsl2StatLineQualityDb_Object = MibTableColumn
hdsl2StatLineQualityDb = _Hdsl2StatLineQualityDb_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 9),
    _Hdsl2StatLineQualityDb_Type()
)
hdsl2StatLineQualityDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatLineQualityDb.setStatus("mandatory")
_Hdsl2StatUpDwnCntr_Type = Integer32
_Hdsl2StatUpDwnCntr_Object = MibTableColumn
hdsl2StatUpDwnCntr = _Hdsl2StatUpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 10),
    _Hdsl2StatUpDwnCntr_Type()
)
hdsl2StatUpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatUpDwnCntr.setStatus("mandatory")


class _Hdsl2StatLineSelfTest_Type(Integer32):
    """Custom type hdsl2StatLineSelfTest based on Integer32"""
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
        *(("localLoopBackFailed", 2),
          ("other", 4),
          ("passed", 3),
          ("selfTestFailed", 1))
    )


_Hdsl2StatLineSelfTest_Type.__name__ = "Integer32"
_Hdsl2StatLineSelfTest_Object = MibTableColumn
hdsl2StatLineSelfTest = _Hdsl2StatLineSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 11),
    _Hdsl2StatLineSelfTest_Type()
)
hdsl2StatLineSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatLineSelfTest.setStatus("mandatory")


class _Hdsl2StatTxPower_Type(Integer32):
    """Custom type hdsl2StatTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatTxPower_Type.__name__ = "Integer32"
_Hdsl2StatTxPower_Object = MibTableColumn
hdsl2StatTxPower = _Hdsl2StatTxPower_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 12),
    _Hdsl2StatTxPower_Type()
)
hdsl2StatTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatTxPower.setStatus("mandatory")


class _Hdsl2StatFramerCrcErrors_Type(Integer32):
    """Custom type hdsl2StatFramerCrcErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatFramerCrcErrors_Type.__name__ = "Integer32"
_Hdsl2StatFramerCrcErrors_Object = MibTableColumn
hdsl2StatFramerCrcErrors = _Hdsl2StatFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 13),
    _Hdsl2StatFramerCrcErrors_Type()
)
hdsl2StatFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatFramerCrcErrors.setStatus("mandatory")


class _Hdsl2StatFramerSyncStatus_Type(Integer32):
    """Custom type hdsl2StatFramerSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatFramerSyncStatus_Type.__name__ = "Integer32"
_Hdsl2StatFramerSyncStatus_Object = MibTableColumn
hdsl2StatFramerSyncStatus = _Hdsl2StatFramerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 14),
    _Hdsl2StatFramerSyncStatus_Type()
)
hdsl2StatFramerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatFramerSyncStatus.setStatus("mandatory")


class _Hdsl2StatFramerLosdCnt_Type(Integer32):
    """Custom type hdsl2StatFramerLosdCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatFramerLosdCnt_Type.__name__ = "Integer32"
_Hdsl2StatFramerLosdCnt_Object = MibTableColumn
hdsl2StatFramerLosdCnt = _Hdsl2StatFramerLosdCnt_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 15),
    _Hdsl2StatFramerLosdCnt_Type()
)
hdsl2StatFramerLosdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatFramerLosdCnt.setStatus("mandatory")


class _Hdsl2StatFramerSegaCnt_Type(Integer32):
    """Custom type hdsl2StatFramerSegaCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatFramerSegaCnt_Type.__name__ = "Integer32"
_Hdsl2StatFramerSegaCnt_Object = MibTableColumn
hdsl2StatFramerSegaCnt = _Hdsl2StatFramerSegaCnt_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 16),
    _Hdsl2StatFramerSegaCnt_Type()
)
hdsl2StatFramerSegaCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatFramerSegaCnt.setStatus("mandatory")


class _Hdsl2StatFramerSegdCnt_Type(Integer32):
    """Custom type hdsl2StatFramerSegdCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatFramerSegdCnt_Type.__name__ = "Integer32"
_Hdsl2StatFramerSegdCnt_Object = MibTableColumn
hdsl2StatFramerSegdCnt = _Hdsl2StatFramerSegdCnt_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 17),
    _Hdsl2StatFramerSegdCnt_Type()
)
hdsl2StatFramerSegdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatFramerSegdCnt.setStatus("mandatory")


class _Hdsl2StatFramerRxHecErrors_Type(Integer32):
    """Custom type hdsl2StatFramerRxHecErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hdsl2StatFramerRxHecErrors_Type.__name__ = "Integer32"
_Hdsl2StatFramerRxHecErrors_Object = MibTableColumn
hdsl2StatFramerRxHecErrors = _Hdsl2StatFramerRxHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 18),
    _Hdsl2StatFramerRxHecErrors_Type()
)
hdsl2StatFramerRxHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatFramerRxHecErrors.setStatus("mandatory")


class _Hdsl2StatBertTimer_Type(Integer32):
    """Custom type hdsl2StatBertTimer based on Integer32"""
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
        *(("fifteen-minutes", 7),
          ("five-minutes", 5),
          ("four-minutes", 4),
          ("one-minute", 1),
          ("ten-minutes", 6),
          ("thirty-minutes", 9),
          ("three-minutes", 3),
          ("twenty-minutes", 8),
          ("two-minutes", 2))
    )


_Hdsl2StatBertTimer_Type.__name__ = "Integer32"
_Hdsl2StatBertTimer_Object = MibTableColumn
hdsl2StatBertTimer = _Hdsl2StatBertTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 19),
    _Hdsl2StatBertTimer_Type()
)
hdsl2StatBertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2StatBertTimer.setStatus("mandatory")


class _Hdsl2StatBertEna_Type(Integer32):
    """Custom type hdsl2StatBertEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Hdsl2StatBertEna_Type.__name__ = "Integer32"
_Hdsl2StatBertEna_Object = MibTableColumn
hdsl2StatBertEna = _Hdsl2StatBertEna_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 20),
    _Hdsl2StatBertEna_Type()
)
hdsl2StatBertEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdsl2StatBertEna.setStatus("mandatory")


class _Hdsl2StatBertState_Type(Integer32):
    """Custom type hdsl2StatBertState based on Integer32"""
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
        *(("active", 1),
          ("bert-los", 6),
          ("pend-active", 5),
          ("start-up", 3),
          ("stopped", 2),
          ("waiting", 4))
    )


_Hdsl2StatBertState_Type.__name__ = "Integer32"
_Hdsl2StatBertState_Object = MibTableColumn
hdsl2StatBertState = _Hdsl2StatBertState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 21),
    _Hdsl2StatBertState_Type()
)
hdsl2StatBertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatBertState.setStatus("mandatory")
_Hdsl2StatBertErrorCounter_Type = Integer32
_Hdsl2StatBertErrorCounter_Object = MibTableColumn
hdsl2StatBertErrorCounter = _Hdsl2StatBertErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 22),
    _Hdsl2StatBertErrorCounter_Type()
)
hdsl2StatBertErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsl2StatBertErrorCounter.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-HDSL2-MIB",
    **{"hdsl2LineStatusTable": hdsl2LineStatusTable,
       "hdsl2LineStatusEntry": hdsl2LineStatusEntry,
       "hdsl2StatusIfEntryIndex": hdsl2StatusIfEntryIndex,
       "hdsl2StatusShelfIndex": hdsl2StatusShelfIndex,
       "hdsl2StatusSlotIndex": hdsl2StatusSlotIndex,
       "hdsl2StatusLineIndex": hdsl2StatusLineIndex,
       "hdsl2StatusUnitType": hdsl2StatusUnitType,
       "hdsl2StatusLineState": hdsl2StatusLineState,
       "hdsl2StatusOpRate": hdsl2StatusOpRate,
       "hdsl2StatusVendorId": hdsl2StatusVendorId,
       "hdsl2StatusMajorFirmWareVer": hdsl2StatusMajorFirmWareVer,
       "hdsl2StatusMinorFirmWareVer": hdsl2StatusMinorFirmWareVer,
       "hdsl2StatusHardWareVer": hdsl2StatusHardWareVer,
       "hdsl2LineStatisticTable": hdsl2LineStatisticTable,
       "hdsl2LineStatisticEntry": hdsl2LineStatisticEntry,
       "hdsl2StatIfEntryIndex": hdsl2StatIfEntryIndex,
       "hdsl2StatShelfIndex": hdsl2StatShelfIndex,
       "hdsl2StatSlotIndex": hdsl2StatSlotIndex,
       "hdsl2StatLineIndex": hdsl2StatLineIndex,
       "hdsl2StatConnUpDays": hdsl2StatConnUpDays,
       "hdsl2StatConnUpHours": hdsl2StatConnUpHours,
       "hdsl2StatConnUpMinutes": hdsl2StatConnUpMinutes,
       "hdsl2StatRxSignalPresent": hdsl2StatRxSignalPresent,
       "hdsl2StatLineQualityDb": hdsl2StatLineQualityDb,
       "hdsl2StatUpDwnCntr": hdsl2StatUpDwnCntr,
       "hdsl2StatLineSelfTest": hdsl2StatLineSelfTest,
       "hdsl2StatTxPower": hdsl2StatTxPower,
       "hdsl2StatFramerCrcErrors": hdsl2StatFramerCrcErrors,
       "hdsl2StatFramerSyncStatus": hdsl2StatFramerSyncStatus,
       "hdsl2StatFramerLosdCnt": hdsl2StatFramerLosdCnt,
       "hdsl2StatFramerSegaCnt": hdsl2StatFramerSegaCnt,
       "hdsl2StatFramerSegdCnt": hdsl2StatFramerSegdCnt,
       "hdsl2StatFramerRxHecErrors": hdsl2StatFramerRxHecErrors,
       "hdsl2StatBertTimer": hdsl2StatBertTimer,
       "hdsl2StatBertEna": hdsl2StatBertEna,
       "hdsl2StatBertState": hdsl2StatBertState,
       "hdsl2StatBertErrorCounter": hdsl2StatBertErrorCounter}
)
