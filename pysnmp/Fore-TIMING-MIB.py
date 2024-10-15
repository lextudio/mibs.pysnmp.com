# SNMP MIB module (Fore-TIMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-TIMING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:19 2024
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

(hardware,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "hardware")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

tcmGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11)
)


# Types definitions



class TcmTimingMode(Integer32):
    """Custom type TcmTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modeExternal", 2),
          ("modeFreeRun", 1),
          ("modeLine", 3))
    )





class TcmReferenceSource(Integer32):
    """Custom type TcmReferenceSource based on Integer32"""
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
        *(("bits1", 2),
          ("bits2", 3),
          ("freerun", 1),
          ("switchPrimary", 4),
          ("switchSecondary", 5))
    )





class DerivedReferenceSource(Integer32):
    """Custom type DerivedReferenceSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("switchPrimary", 4),
          ("switchSecondary", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TcmTable_Object = MibTable
tcmTable = _TcmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tcmTable.setStatus("current")
_TcmEntry_Object = MibTableRow
tcmEntry = _TcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1)
)
tcmEntry.setIndexNames(
    (0, "Fore-TIMING-MIB", "tcmIndex"),
)
if mibBuilder.loadTexts:
    tcmEntry.setStatus("current")
_TcmIndex_Type = Integer32
_TcmIndex_Object = MibTableColumn
tcmIndex = _TcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 1),
    _TcmIndex_Type()
)
tcmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcmIndex.setStatus("current")


class _TcmHwType_Type(Integer32):
    """Custom type tcmHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcmDs1Stratum3E", 1),
          ("tcmE1Stratum3E", 2))
    )


_TcmHwType_Type.__name__ = "Integer32"
_TcmHwType_Object = MibTableColumn
tcmHwType = _TcmHwType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 2),
    _TcmHwType_Type()
)
tcmHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmHwType.setStatus("current")
_TcmHwVersion_Type = Integer32
_TcmHwVersion_Object = MibTableColumn
tcmHwVersion = _TcmHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 3),
    _TcmHwVersion_Type()
)
tcmHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmHwVersion.setStatus("current")


class _TcmPllStatus_Type(Integer32):
    """Custom type tcmPllStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("pllAcquire", 4),
          ("pllFreeRun", 1),
          ("pllHoldover", 5),
          ("pllInitRefQual", 2),
          ("pllLocked", 3),
          ("pllQualifyingRef", 7),
          ("pllRefQualFail", 6))
    )


_TcmPllStatus_Type.__name__ = "Integer32"
_TcmPllStatus_Object = MibTableColumn
tcmPllStatus = _TcmPllStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 4),
    _TcmPllStatus_Type()
)
tcmPllStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmPllStatus.setStatus("current")


class _TcmOperationStatus_Type(Integer32):
    """Custom type tcmOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TcmOperationStatus_Type.__name__ = "Integer32"
_TcmOperationStatus_Object = MibTableColumn
tcmOperationStatus = _TcmOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 5),
    _TcmOperationStatus_Type()
)
tcmOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmOperationStatus.setStatus("current")


class _TcmCurrentTimingRef_Type(Integer32):
    """Custom type tcmCurrentTimingRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("refLocal", 1),
          ("refPrimary", 2),
          ("refSecondary", 3))
    )


_TcmCurrentTimingRef_Type.__name__ = "Integer32"
_TcmCurrentTimingRef_Object = MibTableColumn
tcmCurrentTimingRef = _TcmCurrentTimingRef_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 6),
    _TcmCurrentTimingRef_Type()
)
tcmCurrentTimingRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmCurrentTimingRef.setStatus("current")
_TcmRequestedTimingMode_Type = TcmTimingMode
_TcmRequestedTimingMode_Object = MibTableColumn
tcmRequestedTimingMode = _TcmRequestedTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 7),
    _TcmRequestedTimingMode_Type()
)
tcmRequestedTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmRequestedTimingMode.setStatus("current")
_TcmOperatingTimingMode_Type = TcmTimingMode
_TcmOperatingTimingMode_Object = MibTableColumn
tcmOperatingTimingMode = _TcmOperatingTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 8),
    _TcmOperatingTimingMode_Type()
)
tcmOperatingTimingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmOperatingTimingMode.setStatus("current")


class _TcmModeFailover_Type(Integer32):
    """Custom type tcmModeFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TcmModeFailover_Type.__name__ = "Integer32"
_TcmModeFailover_Object = MibTableColumn
tcmModeFailover = _TcmModeFailover_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 9),
    _TcmModeFailover_Type()
)
tcmModeFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmModeFailover.setStatus("current")
_TcmPrimaryRefSource_Type = TcmReferenceSource
_TcmPrimaryRefSource_Object = MibTableColumn
tcmPrimaryRefSource = _TcmPrimaryRefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 10),
    _TcmPrimaryRefSource_Type()
)
tcmPrimaryRefSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmPrimaryRefSource.setStatus("current")
_TcmSecondaryRefSource_Type = TcmReferenceSource
_TcmSecondaryRefSource_Object = MibTableColumn
tcmSecondaryRefSource = _TcmSecondaryRefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 11),
    _TcmSecondaryRefSource_Type()
)
tcmSecondaryRefSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmSecondaryRefSource.setStatus("current")


class _TcmBitsFramingFormat_Type(Integer32):
    """Custom type tcmBitsFramingFormat based on Integer32"""
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
        *(("d4", 1),
          ("esf", 2),
          ("fas", 5),
          ("fascrc4", 6),
          ("mfas", 3),
          ("mfascrc4", 4))
    )


_TcmBitsFramingFormat_Type.__name__ = "Integer32"
_TcmBitsFramingFormat_Object = MibTableColumn
tcmBitsFramingFormat = _TcmBitsFramingFormat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 12),
    _TcmBitsFramingFormat_Type()
)
tcmBitsFramingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmBitsFramingFormat.setStatus("current")


class _TcmBitsCodingFormat_Type(Integer32):
    """Custom type tcmBitsCodingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_TcmBitsCodingFormat_Type.__name__ = "Integer32"
_TcmBitsCodingFormat_Object = MibTableColumn
tcmBitsCodingFormat = _TcmBitsCodingFormat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 13),
    _TcmBitsCodingFormat_Type()
)
tcmBitsCodingFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmBitsCodingFormat.setStatus("current")


class _TcmBitsOutputLevel_Type(Integer32):
    """Custom type tcmBitsOutputLevel based on Integer32"""
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
        *(("tcmDs1Level0-6", 1),
          ("tcmDs1Level1-2", 2),
          ("tcmDs1Level1-8", 3),
          ("tcmDs1Level2-4", 4),
          ("tcmDs1Level3-0", 5))
    )


_TcmBitsOutputLevel_Type.__name__ = "Integer32"
_TcmBitsOutputLevel_Object = MibTableColumn
tcmBitsOutputLevel = _TcmBitsOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 14),
    _TcmBitsOutputLevel_Type()
)
tcmBitsOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmBitsOutputLevel.setStatus("current")


class _TcmRevertiveSwitching_Type(Integer32):
    """Custom type tcmRevertiveSwitching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_TcmRevertiveSwitching_Type.__name__ = "Integer32"
_TcmRevertiveSwitching_Object = MibTableColumn
tcmRevertiveSwitching = _TcmRevertiveSwitching_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 15),
    _TcmRevertiveSwitching_Type()
)
tcmRevertiveSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmRevertiveSwitching.setStatus("current")
_TcmRevertiveDelay_Type = TimeInterval
_TcmRevertiveDelay_Object = MibTableColumn
tcmRevertiveDelay = _TcmRevertiveDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 16),
    _TcmRevertiveDelay_Type()
)
tcmRevertiveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmRevertiveDelay.setStatus("current")
_TcmFailoverDelay_Type = TimeInterval
_TcmFailoverDelay_Object = MibTableColumn
tcmFailoverDelay = _TcmFailoverDelay_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 1, 1, 17),
    _TcmFailoverDelay_Type()
)
tcmFailoverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmFailoverDelay.setStatus("current")
_TcmReferenceTable_Object = MibTable
tcmReferenceTable = _TcmReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    tcmReferenceTable.setStatus("current")
_TcmReferenceEntry_Object = MibTableRow
tcmReferenceEntry = _TcmReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2, 1)
)
tcmReferenceEntry.setIndexNames(
    (0, "Fore-TIMING-MIB", "tcmIndex"),
    (0, "Fore-TIMING-MIB", "tcmRefSource"),
)
if mibBuilder.loadTexts:
    tcmReferenceEntry.setStatus("current")
_TcmRefSource_Type = TcmReferenceSource
_TcmRefSource_Object = MibTableColumn
tcmRefSource = _TcmRefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2, 1, 1),
    _TcmRefSource_Type()
)
tcmRefSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tcmRefSource.setStatus("current")
_TcmRefSourceText_Type = DisplayString
_TcmRefSourceText_Object = MibTableColumn
tcmRefSourceText = _TcmRefSourceText_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2, 1, 2),
    _TcmRefSourceText_Type()
)
tcmRefSourceText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmRefSourceText.setStatus("current")


class _TcmRefSourceStatus_Type(Integer32):
    """Custom type tcmRefSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_TcmRefSourceStatus_Type.__name__ = "Integer32"
_TcmRefSourceStatus_Object = MibTableColumn
tcmRefSourceStatus = _TcmRefSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2, 1, 3),
    _TcmRefSourceStatus_Type()
)
tcmRefSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmRefSourceStatus.setStatus("current")


class _TcmRefSourceAdminStatus_Type(Integer32):
    """Custom type tcmRefSourceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TcmRefSourceAdminStatus_Type.__name__ = "Integer32"
_TcmRefSourceAdminStatus_Object = MibTableColumn
tcmRefSourceAdminStatus = _TcmRefSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2, 1, 4),
    _TcmRefSourceAdminStatus_Type()
)
tcmRefSourceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmRefSourceAdminStatus.setStatus("current")


class _TcmRefSourceQualStatus_Type(Integer32):
    """Custom type tcmRefSourceQualStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_TcmRefSourceQualStatus_Type.__name__ = "Integer32"
_TcmRefSourceQualStatus_Object = MibTableColumn
tcmRefSourceQualStatus = _TcmRefSourceQualStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 2, 1, 5),
    _TcmRefSourceQualStatus_Type()
)
tcmRefSourceQualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcmRefSourceQualStatus.setStatus("current")
_TcmTxBits1RefSource_Type = DerivedReferenceSource
_TcmTxBits1RefSource_Object = MibScalar
tcmTxBits1RefSource = _TcmTxBits1RefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 3),
    _TcmTxBits1RefSource_Type()
)
tcmTxBits1RefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmTxBits1RefSource.setStatus("current")
_TcmTxBits2RefSource_Type = DerivedReferenceSource
_TcmTxBits2RefSource_Object = MibScalar
tcmTxBits2RefSource = _TcmTxBits2RefSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 4),
    _TcmTxBits2RefSource_Type()
)
tcmTxBits2RefSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmTxBits2RefSource.setStatus("current")


class _TcmTxBitsOperMode_Type(Integer32):
    """Custom type tcmTxBitsOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("thresholdAIS", 2))
    )


_TcmTxBitsOperMode_Type.__name__ = "Integer32"
_TcmTxBitsOperMode_Object = MibScalar
tcmTxBitsOperMode = _TcmTxBitsOperMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 5),
    _TcmTxBitsOperMode_Type()
)
tcmTxBitsOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcmTxBitsOperMode.setStatus("current")

# Managed Objects groups


# Notification objects

tcmTimingSourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 0, 1)
)
tcmTimingSourceChange.setObjects(
      *(("Fore-TIMING-MIB", "tcmIndex"),
        ("Fore-TIMING-MIB", "tcmCurrentTimingRef"),
        ("Fore-TIMING-MIB", "tcmRefSource"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    tcmTimingSourceChange.setStatus(
        "current"
    )

tcmTimingSourceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 11, 0, 2)
)
tcmTimingSourceFailed.setObjects(
      *(("Fore-TIMING-MIB", "tcmIndex"),
        ("Fore-TIMING-MIB", "tcmCurrentTimingRef"),
        ("Fore-TIMING-MIB", "tcmRefSource"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    tcmTimingSourceFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-TIMING-MIB",
    **{"TcmTimingMode": TcmTimingMode,
       "TcmReferenceSource": TcmReferenceSource,
       "DerivedReferenceSource": DerivedReferenceSource,
       "tcmGroup": tcmGroup,
       "tcmTimingSourceChange": tcmTimingSourceChange,
       "tcmTimingSourceFailed": tcmTimingSourceFailed,
       "tcmTable": tcmTable,
       "tcmEntry": tcmEntry,
       "tcmIndex": tcmIndex,
       "tcmHwType": tcmHwType,
       "tcmHwVersion": tcmHwVersion,
       "tcmPllStatus": tcmPllStatus,
       "tcmOperationStatus": tcmOperationStatus,
       "tcmCurrentTimingRef": tcmCurrentTimingRef,
       "tcmRequestedTimingMode": tcmRequestedTimingMode,
       "tcmOperatingTimingMode": tcmOperatingTimingMode,
       "tcmModeFailover": tcmModeFailover,
       "tcmPrimaryRefSource": tcmPrimaryRefSource,
       "tcmSecondaryRefSource": tcmSecondaryRefSource,
       "tcmBitsFramingFormat": tcmBitsFramingFormat,
       "tcmBitsCodingFormat": tcmBitsCodingFormat,
       "tcmBitsOutputLevel": tcmBitsOutputLevel,
       "tcmRevertiveSwitching": tcmRevertiveSwitching,
       "tcmRevertiveDelay": tcmRevertiveDelay,
       "tcmFailoverDelay": tcmFailoverDelay,
       "tcmReferenceTable": tcmReferenceTable,
       "tcmReferenceEntry": tcmReferenceEntry,
       "tcmRefSource": tcmRefSource,
       "tcmRefSourceText": tcmRefSourceText,
       "tcmRefSourceStatus": tcmRefSourceStatus,
       "tcmRefSourceAdminStatus": tcmRefSourceAdminStatus,
       "tcmRefSourceQualStatus": tcmRefSourceQualStatus,
       "tcmTxBits1RefSource": tcmTxBits1RefSource,
       "tcmTxBits2RefSource": tcmTxBits2RefSource,
       "tcmTxBitsOperMode": tcmTxBitsOperMode}
)
