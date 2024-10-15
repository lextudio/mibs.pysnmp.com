# SNMP MIB module (ASCEND-ADSL-CAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-ADSL-CAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:50 2024
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

(wanTypeAdslCap,) = mibBuilder.importSymbols(
    "ASCEND-WAN-MIB",
    "wanTypeAdslCap")

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

_AdslCapLineStatusTable_Object = MibTable
adslCapLineStatusTable = _AdslCapLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1)
)
if mibBuilder.loadTexts:
    adslCapLineStatusTable.setStatus("mandatory")
_AdslCapLineStatusEntry_Object = MibTableRow
adslCapLineStatusEntry = _AdslCapLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1)
)
adslCapLineStatusEntry.setIndexNames(
    (0, "ASCEND-ADSL-CAP-MIB", "adslCapStatusIfEntryIndex"),
)
if mibBuilder.loadTexts:
    adslCapLineStatusEntry.setStatus("mandatory")


class _AdslCapStatusIfEntryIndex_Type(Integer32):
    """Custom type adslCapStatusIfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdslCapStatusIfEntryIndex_Type.__name__ = "Integer32"
_AdslCapStatusIfEntryIndex_Object = MibTableColumn
adslCapStatusIfEntryIndex = _AdslCapStatusIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 1),
    _AdslCapStatusIfEntryIndex_Type()
)
adslCapStatusIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusIfEntryIndex.setStatus("mandatory")
_AdslCapStatusShelfIndex_Type = Integer32
_AdslCapStatusShelfIndex_Object = MibTableColumn
adslCapStatusShelfIndex = _AdslCapStatusShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 2),
    _AdslCapStatusShelfIndex_Type()
)
adslCapStatusShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusShelfIndex.setStatus("mandatory")
_AdslCapStatusSlotIndex_Type = Integer32
_AdslCapStatusSlotIndex_Object = MibTableColumn
adslCapStatusSlotIndex = _AdslCapStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 3),
    _AdslCapStatusSlotIndex_Type()
)
adslCapStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusSlotIndex.setStatus("mandatory")
_AdslCapStatusLineIndex_Type = Integer32
_AdslCapStatusLineIndex_Object = MibTableColumn
adslCapStatusLineIndex = _AdslCapStatusLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 4),
    _AdslCapStatusLineIndex_Type()
)
adslCapStatusLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusLineIndex.setStatus("mandatory")


class _AdslCapStatusUnitType_Type(Integer32):
    """Custom type adslCapStatusUnitType based on Integer32"""
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


_AdslCapStatusUnitType_Type.__name__ = "Integer32"
_AdslCapStatusUnitType_Object = MibTableColumn
adslCapStatusUnitType = _AdslCapStatusUnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 5),
    _AdslCapStatusUnitType_Type()
)
adslCapStatusUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusUnitType.setStatus("mandatory")


class _AdslCapStatusLineState_Type(Integer32):
    """Custom type adslCapStatusLineState based on Integer32"""
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


_AdslCapStatusLineState_Type.__name__ = "Integer32"
_AdslCapStatusLineState_Object = MibTableColumn
adslCapStatusLineState = _AdslCapStatusLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 6),
    _AdslCapStatusLineState_Type()
)
adslCapStatusLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusLineState.setStatus("mandatory")


class _AdslCapStatusUpRate_Type(Integer32):
    """Custom type adslCapStatusUpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(272000,
              408000,
              544000,
              680000,
              816000,
              952000,
              1088000)
        )
    )
    namedValues = NamedValues(
        *(("k272000", 272000),
          ("k408000", 408000),
          ("k544000", 544000),
          ("k680000", 680000),
          ("k816000", 816000),
          ("k952000", 952000),
          ("m1088000", 1088000))
    )


_AdslCapStatusUpRate_Type.__name__ = "Integer32"
_AdslCapStatusUpRate_Object = MibTableColumn
adslCapStatusUpRate = _AdslCapStatusUpRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 7),
    _AdslCapStatusUpRate_Type()
)
adslCapStatusUpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslCapStatusUpRate.setStatus("mandatory")


class _AdslCapStatusDownRate_Type(Integer32):
    """Custom type adslCapStatusDownRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(640000,
              960000,
              1280000,
              1600000,
              1920000,
              2240000,
              2560000,
              2688000,
              3200000,
              4480000,
              5120000,
              6272000,
              7168000)
        )
    )
    namedValues = NamedValues(
        *(("k640000", 640000),
          ("k960000", 960000),
          ("m1280000", 1280000),
          ("m1600000", 1600000),
          ("m1920000", 1920000),
          ("m2240000", 2240000),
          ("m2560000", 2560000),
          ("m2688000", 2688000),
          ("m3200000", 3200000),
          ("m4480000", 4480000),
          ("m5120000", 5120000),
          ("m6272000", 6272000),
          ("m7168000", 7168000))
    )


_AdslCapStatusDownRate_Type.__name__ = "Integer32"
_AdslCapStatusDownRate_Object = MibTableColumn
adslCapStatusDownRate = _AdslCapStatusDownRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 8),
    _AdslCapStatusDownRate_Type()
)
adslCapStatusDownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslCapStatusDownRate.setStatus("mandatory")
_AdslCapStatusVendorId_Type = Integer32
_AdslCapStatusVendorId_Object = MibTableColumn
adslCapStatusVendorId = _AdslCapStatusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 9),
    _AdslCapStatusVendorId_Type()
)
adslCapStatusVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusVendorId.setStatus("mandatory")
_AdslCapStatusMajorFirmWareVer_Type = Integer32
_AdslCapStatusMajorFirmWareVer_Object = MibTableColumn
adslCapStatusMajorFirmWareVer = _AdslCapStatusMajorFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 10),
    _AdslCapStatusMajorFirmWareVer_Type()
)
adslCapStatusMajorFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusMajorFirmWareVer.setStatus("mandatory")
_AdslCapStatusMinorFirmWareVer_Type = Integer32
_AdslCapStatusMinorFirmWareVer_Object = MibTableColumn
adslCapStatusMinorFirmWareVer = _AdslCapStatusMinorFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 11),
    _AdslCapStatusMinorFirmWareVer_Type()
)
adslCapStatusMinorFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusMinorFirmWareVer.setStatus("mandatory")
_AdslCapStatusHardWareVer_Type = Integer32
_AdslCapStatusHardWareVer_Object = MibTableColumn
adslCapStatusHardWareVer = _AdslCapStatusHardWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 1, 1, 12),
    _AdslCapStatusHardWareVer_Type()
)
adslCapStatusHardWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatusHardWareVer.setStatus("mandatory")
_AdslCapLineStatisticTable_Object = MibTable
adslCapLineStatisticTable = _AdslCapLineStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2)
)
if mibBuilder.loadTexts:
    adslCapLineStatisticTable.setStatus("mandatory")
_AdslCapLineStatisticEntry_Object = MibTableRow
adslCapLineStatisticEntry = _AdslCapLineStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1)
)
adslCapLineStatisticEntry.setIndexNames(
    (0, "ASCEND-ADSL-CAP-MIB", "adslCapStatIfEntryIndex"),
)
if mibBuilder.loadTexts:
    adslCapLineStatisticEntry.setStatus("mandatory")


class _AdslCapStatIfEntryIndex_Type(Integer32):
    """Custom type adslCapStatIfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdslCapStatIfEntryIndex_Type.__name__ = "Integer32"
_AdslCapStatIfEntryIndex_Object = MibTableColumn
adslCapStatIfEntryIndex = _AdslCapStatIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 1),
    _AdslCapStatIfEntryIndex_Type()
)
adslCapStatIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatIfEntryIndex.setStatus("mandatory")
_AdslCapStatShelfIndex_Type = Integer32
_AdslCapStatShelfIndex_Object = MibTableColumn
adslCapStatShelfIndex = _AdslCapStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 2),
    _AdslCapStatShelfIndex_Type()
)
adslCapStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatShelfIndex.setStatus("mandatory")
_AdslCapStatSlotIndex_Type = Integer32
_AdslCapStatSlotIndex_Object = MibTableColumn
adslCapStatSlotIndex = _AdslCapStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 3),
    _AdslCapStatSlotIndex_Type()
)
adslCapStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatSlotIndex.setStatus("mandatory")
_AdslCapStatLineIndex_Type = Integer32
_AdslCapStatLineIndex_Object = MibTableColumn
adslCapStatLineIndex = _AdslCapStatLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 4),
    _AdslCapStatLineIndex_Type()
)
adslCapStatLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatLineIndex.setStatus("mandatory")
_AdslCapStatConnUpDays_Type = Integer32
_AdslCapStatConnUpDays_Object = MibTableColumn
adslCapStatConnUpDays = _AdslCapStatConnUpDays_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 5),
    _AdslCapStatConnUpDays_Type()
)
adslCapStatConnUpDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatConnUpDays.setStatus("mandatory")
_AdslCapStatConnUpHours_Type = Integer32
_AdslCapStatConnUpHours_Object = MibTableColumn
adslCapStatConnUpHours = _AdslCapStatConnUpHours_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 6),
    _AdslCapStatConnUpHours_Type()
)
adslCapStatConnUpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatConnUpHours.setStatus("mandatory")
_AdslCapStatConnUpMinutes_Type = Integer32
_AdslCapStatConnUpMinutes_Object = MibTableColumn
adslCapStatConnUpMinutes = _AdslCapStatConnUpMinutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 7),
    _AdslCapStatConnUpMinutes_Type()
)
adslCapStatConnUpMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatConnUpMinutes.setStatus("mandatory")


class _AdslCapStatRxSignalPresent_Type(Integer32):
    """Custom type adslCapStatRxSignalPresent based on Integer32"""
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


_AdslCapStatRxSignalPresent_Type.__name__ = "Integer32"
_AdslCapStatRxSignalPresent_Object = MibTableColumn
adslCapStatRxSignalPresent = _AdslCapStatRxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 8),
    _AdslCapStatRxSignalPresent_Type()
)
adslCapStatRxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatRxSignalPresent.setStatus("mandatory")
_AdslCapStatLineQualityDb_Type = Integer32
_AdslCapStatLineQualityDb_Object = MibTableColumn
adslCapStatLineQualityDb = _AdslCapStatLineQualityDb_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 9),
    _AdslCapStatLineQualityDb_Type()
)
adslCapStatLineQualityDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatLineQualityDb.setStatus("mandatory")
_AdslCapStatUpDwnCntr_Type = Integer32
_AdslCapStatUpDwnCntr_Object = MibTableColumn
adslCapStatUpDwnCntr = _AdslCapStatUpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 10),
    _AdslCapStatUpDwnCntr_Type()
)
adslCapStatUpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatUpDwnCntr.setStatus("mandatory")


class _AdslCapStatLineSelfTest_Type(Integer32):
    """Custom type adslCapStatLineSelfTest based on Integer32"""
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


_AdslCapStatLineSelfTest_Type.__name__ = "Integer32"
_AdslCapStatLineSelfTest_Object = MibTableColumn
adslCapStatLineSelfTest = _AdslCapStatLineSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 11),
    _AdslCapStatLineSelfTest_Type()
)
adslCapStatLineSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatLineSelfTest.setStatus("mandatory")


class _AdslCapStatBertTimer_Type(Integer32):
    """Custom type adslCapStatBertTimer based on Integer32"""
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


_AdslCapStatBertTimer_Type.__name__ = "Integer32"
_AdslCapStatBertTimer_Object = MibTableColumn
adslCapStatBertTimer = _AdslCapStatBertTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 12),
    _AdslCapStatBertTimer_Type()
)
adslCapStatBertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslCapStatBertTimer.setStatus("mandatory")


class _AdslCapStatBertEna_Type(Integer32):
    """Custom type adslCapStatBertEna based on Integer32"""
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


_AdslCapStatBertEna_Type.__name__ = "Integer32"
_AdslCapStatBertEna_Object = MibTableColumn
adslCapStatBertEna = _AdslCapStatBertEna_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 13),
    _AdslCapStatBertEna_Type()
)
adslCapStatBertEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adslCapStatBertEna.setStatus("mandatory")


class _AdslCapStatBertState_Type(Integer32):
    """Custom type adslCapStatBertState based on Integer32"""
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
        *(("active", 3),
          ("ber-sync-loss", 8),
          ("data-overflow", 7),
          ("local-loop-active", 2),
          ("loop-back-setup", 5),
          ("start-up", 6),
          ("stopped", 4),
          ("waiting-for-511-sync", 1))
    )


_AdslCapStatBertState_Type.__name__ = "Integer32"
_AdslCapStatBertState_Object = MibTableColumn
adslCapStatBertState = _AdslCapStatBertState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 14),
    _AdslCapStatBertState_Type()
)
adslCapStatBertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatBertState.setStatus("mandatory")
_AdslCapStatBertErrorCounter_Type = Integer32
_AdslCapStatBertErrorCounter_Object = MibTableColumn
adslCapStatBertErrorCounter = _AdslCapStatBertErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 9, 2, 1, 15),
    _AdslCapStatBertErrorCounter_Type()
)
adslCapStatBertErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslCapStatBertErrorCounter.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-ADSL-CAP-MIB",
    **{"adslCapLineStatusTable": adslCapLineStatusTable,
       "adslCapLineStatusEntry": adslCapLineStatusEntry,
       "adslCapStatusIfEntryIndex": adslCapStatusIfEntryIndex,
       "adslCapStatusShelfIndex": adslCapStatusShelfIndex,
       "adslCapStatusSlotIndex": adslCapStatusSlotIndex,
       "adslCapStatusLineIndex": adslCapStatusLineIndex,
       "adslCapStatusUnitType": adslCapStatusUnitType,
       "adslCapStatusLineState": adslCapStatusLineState,
       "adslCapStatusUpRate": adslCapStatusUpRate,
       "adslCapStatusDownRate": adslCapStatusDownRate,
       "adslCapStatusVendorId": adslCapStatusVendorId,
       "adslCapStatusMajorFirmWareVer": adslCapStatusMajorFirmWareVer,
       "adslCapStatusMinorFirmWareVer": adslCapStatusMinorFirmWareVer,
       "adslCapStatusHardWareVer": adslCapStatusHardWareVer,
       "adslCapLineStatisticTable": adslCapLineStatisticTable,
       "adslCapLineStatisticEntry": adslCapLineStatisticEntry,
       "adslCapStatIfEntryIndex": adslCapStatIfEntryIndex,
       "adslCapStatShelfIndex": adslCapStatShelfIndex,
       "adslCapStatSlotIndex": adslCapStatSlotIndex,
       "adslCapStatLineIndex": adslCapStatLineIndex,
       "adslCapStatConnUpDays": adslCapStatConnUpDays,
       "adslCapStatConnUpHours": adslCapStatConnUpHours,
       "adslCapStatConnUpMinutes": adslCapStatConnUpMinutes,
       "adslCapStatRxSignalPresent": adslCapStatRxSignalPresent,
       "adslCapStatLineQualityDb": adslCapStatLineQualityDb,
       "adslCapStatUpDwnCntr": adslCapStatUpDwnCntr,
       "adslCapStatLineSelfTest": adslCapStatLineSelfTest,
       "adslCapStatBertTimer": adslCapStatBertTimer,
       "adslCapStatBertEna": adslCapStatBertEna,
       "adslCapStatBertState": adslCapStatBertState,
       "adslCapStatBertErrorCounter": adslCapStatBertErrorCounter}
)
