# SNMP MIB module (ASCEND-SDSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-SDSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:41 2024
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

(wanTypeSdsl,) = mibBuilder.importSymbols(
    "ASCEND-WAN-MIB",
    "wanTypeSdsl")

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

_SdslLineStatusTable_Object = MibTable
sdslLineStatusTable = _SdslLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1)
)
if mibBuilder.loadTexts:
    sdslLineStatusTable.setStatus("mandatory")
_SdslLineStatusEntry_Object = MibTableRow
sdslLineStatusEntry = _SdslLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1)
)
sdslLineStatusEntry.setIndexNames(
    (0, "ASCEND-SDSL-MIB", "sdslStatusIfEntryIndex"),
)
if mibBuilder.loadTexts:
    sdslLineStatusEntry.setStatus("mandatory")
_SdslStatusIfEntryIndex_Type = Integer32
_SdslStatusIfEntryIndex_Object = MibTableColumn
sdslStatusIfEntryIndex = _SdslStatusIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 1),
    _SdslStatusIfEntryIndex_Type()
)
sdslStatusIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusIfEntryIndex.setStatus("mandatory")
_SdslStatusShelfIndex_Type = Integer32
_SdslStatusShelfIndex_Object = MibTableColumn
sdslStatusShelfIndex = _SdslStatusShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 2),
    _SdslStatusShelfIndex_Type()
)
sdslStatusShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusShelfIndex.setStatus("mandatory")
_SdslStatusSlotIndex_Type = Integer32
_SdslStatusSlotIndex_Object = MibTableColumn
sdslStatusSlotIndex = _SdslStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 3),
    _SdslStatusSlotIndex_Type()
)
sdslStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusSlotIndex.setStatus("mandatory")
_SdslStatusLineIndex_Type = Integer32
_SdslStatusLineIndex_Object = MibTableColumn
sdslStatusLineIndex = _SdslStatusLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 4),
    _SdslStatusLineIndex_Type()
)
sdslStatusLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusLineIndex.setStatus("mandatory")


class _SdslStatusUnitType_Type(Integer32):
    """Custom type sdslStatusUnitType based on Integer32"""
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


_SdslStatusUnitType_Type.__name__ = "Integer32"
_SdslStatusUnitType_Object = MibTableColumn
sdslStatusUnitType = _SdslStatusUnitType_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 5),
    _SdslStatusUnitType_Type()
)
sdslStatusUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusUnitType.setStatus("mandatory")


class _SdslStatusLineState_Type(Integer32):
    """Custom type sdslStatusLineState based on Integer32"""
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
        *(("configure", 2),
          ("deactivate", 3),
          ("deactive-lost", 4),
          ("other", 1),
          ("out-of-service", 9),
          ("pend-deactivate", 8),
          ("pend-port-up", 6),
          ("start-up", 5),
          ("up", 7))
    )


_SdslStatusLineState_Type.__name__ = "Integer32"
_SdslStatusLineState_Object = MibTableColumn
sdslStatusLineState = _SdslStatusLineState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 6),
    _SdslStatusLineState_Type()
)
sdslStatusLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusLineState.setStatus("mandatory")


class _SdslStatusUpRate_Type(Integer32):
    """Custom type sdslStatusUpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(144000,
              160000,
              192000,
              208000,
              272000,
              384000,
              400000,
              416000,
              528000,
              768000,
              784000,
              1040000,
              1152000,
              1168000,
              1536000,
              1552000,
              1568000,
              2320000)
        )
    )
    namedValues = NamedValues(
        *(("k144000", 144000),
          ("k160000", 160000),
          ("k192000", 192000),
          ("k208000", 208000),
          ("k272000", 272000),
          ("k384000", 384000),
          ("k400000", 400000),
          ("k416000", 416000),
          ("k528000", 528000),
          ("k768000", 768000),
          ("k784000", 784000),
          ("m1040000", 1040000),
          ("m1152000", 1152000),
          ("m1168000", 1168000),
          ("m1536000", 1536000),
          ("m1552000", 1552000),
          ("m1568000", 1568000),
          ("m2320000", 2320000))
    )


_SdslStatusUpRate_Type.__name__ = "Integer32"
_SdslStatusUpRate_Object = MibTableColumn
sdslStatusUpRate = _SdslStatusUpRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 7),
    _SdslStatusUpRate_Type()
)
sdslStatusUpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslStatusUpRate.setStatus("deprecated")


class _SdslStatusDownRate_Type(Integer32):
    """Custom type sdslStatusDownRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(144000,
              160000,
              192000,
              208000,
              272000,
              384000,
              400000,
              416000,
              528000,
              768000,
              784000,
              1040000,
              1152000,
              1168000,
              1536000,
              1552000,
              1568000,
              2320000)
        )
    )
    namedValues = NamedValues(
        *(("k144000", 144000),
          ("k160000", 160000),
          ("k192000", 192000),
          ("k208000", 208000),
          ("k272000", 272000),
          ("k384000", 384000),
          ("k400000", 400000),
          ("k416000", 416000),
          ("k528000", 528000),
          ("k768000", 768000),
          ("k784000", 784000),
          ("m1040000", 1040000),
          ("m1152000", 1152000),
          ("m1168000", 1168000),
          ("m1536000", 1536000),
          ("m1552000", 1552000),
          ("m1568000", 1568000),
          ("m2320000", 2320000))
    )


_SdslStatusDownRate_Type.__name__ = "Integer32"
_SdslStatusDownRate_Object = MibTableColumn
sdslStatusDownRate = _SdslStatusDownRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 8),
    _SdslStatusDownRate_Type()
)
sdslStatusDownRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslStatusDownRate.setStatus("deprecated")
_SdslStatusVendorId_Type = Integer32
_SdslStatusVendorId_Object = MibTableColumn
sdslStatusVendorId = _SdslStatusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 9),
    _SdslStatusVendorId_Type()
)
sdslStatusVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusVendorId.setStatus("mandatory")
_SdslStatusMajorFirmWareVer_Type = Integer32
_SdslStatusMajorFirmWareVer_Object = MibTableColumn
sdslStatusMajorFirmWareVer = _SdslStatusMajorFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 10),
    _SdslStatusMajorFirmWareVer_Type()
)
sdslStatusMajorFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusMajorFirmWareVer.setStatus("mandatory")
_SdslStatusMinorFirmWareVer_Type = Integer32
_SdslStatusMinorFirmWareVer_Object = MibTableColumn
sdslStatusMinorFirmWareVer = _SdslStatusMinorFirmWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 11),
    _SdslStatusMinorFirmWareVer_Type()
)
sdslStatusMinorFirmWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusMinorFirmWareVer.setStatus("mandatory")
_SdslStatusHardWareVer_Type = Integer32
_SdslStatusHardWareVer_Object = MibTableColumn
sdslStatusHardWareVer = _SdslStatusHardWareVer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 12),
    _SdslStatusHardWareVer_Type()
)
sdslStatusHardWareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusHardWareVer.setStatus("mandatory")


class _SdslStatusLineRate_Type(Integer32):
    """Custom type sdslStatusLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              144000,
              160000,
              192000,
              208000,
              272000,
              384000,
              400000,
              416000,
              528000,
              768000,
              784000,
              1040000,
              1152000,
              1168000,
              1536000,
              1552000,
              1568000,
              2320000)
        )
    )
    namedValues = NamedValues(
        *(("k144000", 144000),
          ("k160000", 160000),
          ("k192000", 192000),
          ("k208000", 208000),
          ("k272000", 272000),
          ("k384000", 384000),
          ("k400000", 400000),
          ("k416000", 416000),
          ("k528000", 528000),
          ("k768000", 768000),
          ("k784000", 784000),
          ("m1040000", 1040000),
          ("m1152000", 1152000),
          ("m1168000", 1168000),
          ("m1536000", 1536000),
          ("m1552000", 1552000),
          ("m1568000", 1568000),
          ("m2320000", 2320000),
          ("unknown", 1))
    )


_SdslStatusLineRate_Type.__name__ = "Integer32"
_SdslStatusLineRate_Object = MibTableColumn
sdslStatusLineRate = _SdslStatusLineRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 1, 1, 13),
    _SdslStatusLineRate_Type()
)
sdslStatusLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatusLineRate.setStatus("mandatory")
_SdslLineStatisticTable_Object = MibTable
sdslLineStatisticTable = _SdslLineStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2)
)
if mibBuilder.loadTexts:
    sdslLineStatisticTable.setStatus("mandatory")
_SdslLineStatisticEntry_Object = MibTableRow
sdslLineStatisticEntry = _SdslLineStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1)
)
sdslLineStatisticEntry.setIndexNames(
    (0, "ASCEND-SDSL-MIB", "sdslStatIfEntryIndex"),
)
if mibBuilder.loadTexts:
    sdslLineStatisticEntry.setStatus("mandatory")
_SdslStatIfEntryIndex_Type = Integer32
_SdslStatIfEntryIndex_Object = MibTableColumn
sdslStatIfEntryIndex = _SdslStatIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 1),
    _SdslStatIfEntryIndex_Type()
)
sdslStatIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatIfEntryIndex.setStatus("mandatory")
_SdslStatShelfIndex_Type = Integer32
_SdslStatShelfIndex_Object = MibTableColumn
sdslStatShelfIndex = _SdslStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 2),
    _SdslStatShelfIndex_Type()
)
sdslStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatShelfIndex.setStatus("mandatory")
_SdslStatSlotIndex_Type = Integer32
_SdslStatSlotIndex_Object = MibTableColumn
sdslStatSlotIndex = _SdslStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 3),
    _SdslStatSlotIndex_Type()
)
sdslStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatSlotIndex.setStatus("mandatory")
_SdslStatLineIndex_Type = Integer32
_SdslStatLineIndex_Object = MibTableColumn
sdslStatLineIndex = _SdslStatLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 4),
    _SdslStatLineIndex_Type()
)
sdslStatLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatLineIndex.setStatus("mandatory")
_SdslStatConnUpDays_Type = Integer32
_SdslStatConnUpDays_Object = MibTableColumn
sdslStatConnUpDays = _SdslStatConnUpDays_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 5),
    _SdslStatConnUpDays_Type()
)
sdslStatConnUpDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatConnUpDays.setStatus("mandatory")
_SdslStatConnUpHours_Type = Integer32
_SdslStatConnUpHours_Object = MibTableColumn
sdslStatConnUpHours = _SdslStatConnUpHours_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 6),
    _SdslStatConnUpHours_Type()
)
sdslStatConnUpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatConnUpHours.setStatus("mandatory")
_SdslStatConnUpMinutes_Type = Integer32
_SdslStatConnUpMinutes_Object = MibTableColumn
sdslStatConnUpMinutes = _SdslStatConnUpMinutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 7),
    _SdslStatConnUpMinutes_Type()
)
sdslStatConnUpMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatConnUpMinutes.setStatus("mandatory")


class _SdslStatRxSignalPresent_Type(Integer32):
    """Custom type sdslStatRxSignalPresent based on Integer32"""
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


_SdslStatRxSignalPresent_Type.__name__ = "Integer32"
_SdslStatRxSignalPresent_Object = MibTableColumn
sdslStatRxSignalPresent = _SdslStatRxSignalPresent_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 8),
    _SdslStatRxSignalPresent_Type()
)
sdslStatRxSignalPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatRxSignalPresent.setStatus("mandatory")
_SdslStatLineQualityDb_Type = Integer32
_SdslStatLineQualityDb_Object = MibTableColumn
sdslStatLineQualityDb = _SdslStatLineQualityDb_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 9),
    _SdslStatLineQualityDb_Type()
)
sdslStatLineQualityDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatLineQualityDb.setStatus("mandatory")
_SdslStatUpDwnCntr_Type = Integer32
_SdslStatUpDwnCntr_Object = MibTableColumn
sdslStatUpDwnCntr = _SdslStatUpDwnCntr_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 10),
    _SdslStatUpDwnCntr_Type()
)
sdslStatUpDwnCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatUpDwnCntr.setStatus("mandatory")


class _SdslStatLineSelfTest_Type(Integer32):
    """Custom type sdslStatLineSelfTest based on Integer32"""
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


_SdslStatLineSelfTest_Type.__name__ = "Integer32"
_SdslStatLineSelfTest_Object = MibTableColumn
sdslStatLineSelfTest = _SdslStatLineSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 11),
    _SdslStatLineSelfTest_Type()
)
sdslStatLineSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatLineSelfTest.setStatus("mandatory")


class _SdslStatBertTimer_Type(Integer32):
    """Custom type sdslStatBertTimer based on Integer32"""
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


_SdslStatBertTimer_Type.__name__ = "Integer32"
_SdslStatBertTimer_Object = MibTableColumn
sdslStatBertTimer = _SdslStatBertTimer_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 12),
    _SdslStatBertTimer_Type()
)
sdslStatBertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslStatBertTimer.setStatus("mandatory")


class _SdslStatBertEna_Type(Integer32):
    """Custom type sdslStatBertEna based on Integer32"""
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


_SdslStatBertEna_Type.__name__ = "Integer32"
_SdslStatBertEna_Object = MibTableColumn
sdslStatBertEna = _SdslStatBertEna_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 13),
    _SdslStatBertEna_Type()
)
sdslStatBertEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslStatBertEna.setStatus("mandatory")


class _SdslStatBertState_Type(Integer32):
    """Custom type sdslStatBertState based on Integer32"""
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


_SdslStatBertState_Type.__name__ = "Integer32"
_SdslStatBertState_Object = MibTableColumn
sdslStatBertState = _SdslStatBertState_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 14),
    _SdslStatBertState_Type()
)
sdslStatBertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatBertState.setStatus("mandatory")
_SdslStatBertErrorCounter_Type = Integer32
_SdslStatBertErrorCounter_Object = MibTableColumn
sdslStatBertErrorCounter = _SdslStatBertErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 2, 1, 15),
    _SdslStatBertErrorCounter_Type()
)
sdslStatBertErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslStatBertErrorCounter.setStatus("mandatory")
_SdslLineConfigTable_Object = MibTable
sdslLineConfigTable = _SdslLineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3)
)
if mibBuilder.loadTexts:
    sdslLineConfigTable.setStatus("mandatory")
_SdslLineConfigEntry_Object = MibTableRow
sdslLineConfigEntry = _SdslLineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3, 1)
)
sdslLineConfigEntry.setIndexNames(
    (0, "ASCEND-SDSL-MIB", "sdslConfigIfEntryIndex"),
)
if mibBuilder.loadTexts:
    sdslLineConfigEntry.setStatus("mandatory")
_SdslConfigIfEntryIndex_Type = Integer32
_SdslConfigIfEntryIndex_Object = MibTableColumn
sdslConfigIfEntryIndex = _SdslConfigIfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3, 1, 1),
    _SdslConfigIfEntryIndex_Type()
)
sdslConfigIfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslConfigIfEntryIndex.setStatus("mandatory")
_SdslConfigShelfIndex_Type = Integer32
_SdslConfigShelfIndex_Object = MibTableColumn
sdslConfigShelfIndex = _SdslConfigShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3, 1, 2),
    _SdslConfigShelfIndex_Type()
)
sdslConfigShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslConfigShelfIndex.setStatus("mandatory")
_SdslConfigSlotIndex_Type = Integer32
_SdslConfigSlotIndex_Object = MibTableColumn
sdslConfigSlotIndex = _SdslConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3, 1, 3),
    _SdslConfigSlotIndex_Type()
)
sdslConfigSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslConfigSlotIndex.setStatus("mandatory")
_SdslConfigLineIndex_Type = Integer32
_SdslConfigLineIndex_Object = MibTableColumn
sdslConfigLineIndex = _SdslConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3, 1, 4),
    _SdslConfigLineIndex_Type()
)
sdslConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdslConfigLineIndex.setStatus("mandatory")


class _SdslConfigLineRate_Type(Integer32):
    """Custom type sdslConfigLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              144000,
              160000,
              192000,
              208000,
              272000,
              384000,
              400000,
              416000,
              528000,
              768000,
              784000,
              1040000,
              1152000,
              1168000,
              1536000,
              1552000,
              1568000,
              2320000)
        )
    )
    namedValues = NamedValues(
        *(("k144000", 144000),
          ("k160000", 160000),
          ("k192000", 192000),
          ("k208000", 208000),
          ("k272000", 272000),
          ("k384000", 384000),
          ("k400000", 400000),
          ("k416000", 416000),
          ("k528000", 528000),
          ("k768000", 768000),
          ("k784000", 784000),
          ("m1040000", 1040000),
          ("m1152000", 1152000),
          ("m1168000", 1168000),
          ("m1536000", 1536000),
          ("m1552000", 1552000),
          ("m1568000", 1568000),
          ("m2320000", 2320000),
          ("unknown", 1))
    )


_SdslConfigLineRate_Type.__name__ = "Integer32"
_SdslConfigLineRate_Object = MibTableColumn
sdslConfigLineRate = _SdslConfigLineRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 4, 8, 3, 1, 5),
    _SdslConfigLineRate_Type()
)
sdslConfigLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdslConfigLineRate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-SDSL-MIB",
    **{"sdslLineStatusTable": sdslLineStatusTable,
       "sdslLineStatusEntry": sdslLineStatusEntry,
       "sdslStatusIfEntryIndex": sdslStatusIfEntryIndex,
       "sdslStatusShelfIndex": sdslStatusShelfIndex,
       "sdslStatusSlotIndex": sdslStatusSlotIndex,
       "sdslStatusLineIndex": sdslStatusLineIndex,
       "sdslStatusUnitType": sdslStatusUnitType,
       "sdslStatusLineState": sdslStatusLineState,
       "sdslStatusUpRate": sdslStatusUpRate,
       "sdslStatusDownRate": sdslStatusDownRate,
       "sdslStatusVendorId": sdslStatusVendorId,
       "sdslStatusMajorFirmWareVer": sdslStatusMajorFirmWareVer,
       "sdslStatusMinorFirmWareVer": sdslStatusMinorFirmWareVer,
       "sdslStatusHardWareVer": sdslStatusHardWareVer,
       "sdslStatusLineRate": sdslStatusLineRate,
       "sdslLineStatisticTable": sdslLineStatisticTable,
       "sdslLineStatisticEntry": sdslLineStatisticEntry,
       "sdslStatIfEntryIndex": sdslStatIfEntryIndex,
       "sdslStatShelfIndex": sdslStatShelfIndex,
       "sdslStatSlotIndex": sdslStatSlotIndex,
       "sdslStatLineIndex": sdslStatLineIndex,
       "sdslStatConnUpDays": sdslStatConnUpDays,
       "sdslStatConnUpHours": sdslStatConnUpHours,
       "sdslStatConnUpMinutes": sdslStatConnUpMinutes,
       "sdslStatRxSignalPresent": sdslStatRxSignalPresent,
       "sdslStatLineQualityDb": sdslStatLineQualityDb,
       "sdslStatUpDwnCntr": sdslStatUpDwnCntr,
       "sdslStatLineSelfTest": sdslStatLineSelfTest,
       "sdslStatBertTimer": sdslStatBertTimer,
       "sdslStatBertEna": sdslStatBertEna,
       "sdslStatBertState": sdslStatBertState,
       "sdslStatBertErrorCounter": sdslStatBertErrorCounter,
       "sdslLineConfigTable": sdslLineConfigTable,
       "sdslLineConfigEntry": sdslLineConfigEntry,
       "sdslConfigIfEntryIndex": sdslConfigIfEntryIndex,
       "sdslConfigShelfIndex": sdslConfigShelfIndex,
       "sdslConfigSlotIndex": sdslConfigSlotIndex,
       "sdslConfigLineIndex": sdslConfigLineIndex,
       "sdslConfigLineRate": sdslConfigLineRate}
)
