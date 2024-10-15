# SNMP MIB module (ADTRAN-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:31 2024
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
_AdDS1mg_ObjectIdentity = ObjectIdentity
adDS1mg = _AdDS1mg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 3)
)
_AdDS1AlarmTable_Object = MibTable
adDS1AlarmTable = _AdDS1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 1)
)
if mibBuilder.loadTexts:
    adDS1AlarmTable.setStatus("mandatory")
_AdDS1AlarmEntry_Object = MibTableRow
adDS1AlarmEntry = _AdDS1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 1, 1)
)
adDS1AlarmEntry.setIndexNames(
    (0, "ADTRAN-DS1-MIB", "adDS1AlarmIndex"),
)
if mibBuilder.loadTexts:
    adDS1AlarmEntry.setStatus("mandatory")


class _AdDS1AlarmIndex_Type(Integer32):
    """Custom type adDS1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdDS1AlarmIndex_Type.__name__ = "Integer32"
_AdDS1AlarmIndex_Object = MibTableColumn
adDS1AlarmIndex = _AdDS1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 1, 1, 1),
    _AdDS1AlarmIndex_Type()
)
adDS1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1AlarmIndex.setStatus("mandatory")


class _AdDS1AlarmEnable_Type(Integer32):
    """Custom type adDS1AlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1AlarmOFF", 1),
          ("ds1AlarmON", 2))
    )


_AdDS1AlarmEnable_Type.__name__ = "Integer32"
_AdDS1AlarmEnable_Object = MibTableColumn
adDS1AlarmEnable = _AdDS1AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 1, 1, 2),
    _AdDS1AlarmEnable_Type()
)
adDS1AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1AlarmEnable.setStatus("mandatory")


class _AdDS1LineEvent_Type(Integer32):
    """Custom type adDS1LineEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdDS1LineEvent_Type.__name__ = "Integer32"
_AdDS1LineEvent_Object = MibTableColumn
adDS1LineEvent = _AdDS1LineEvent_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 1, 1, 3),
    _AdDS1LineEvent_Type()
)
adDS1LineEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1LineEvent.setStatus("mandatory")


class _AdDS1LineArm_Type(Integer32):
    """Custom type adDS1LineArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdDS1LineArm_Type.__name__ = "Integer32"
_AdDS1LineArm_Object = MibTableColumn
adDS1LineArm = _AdDS1LineArm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 1, 1, 4),
    _AdDS1LineArm_Type()
)
adDS1LineArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1LineArm.setStatus("mandatory")
_AdDS1AlertTable_Object = MibTable
adDS1AlertTable = _AdDS1AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2)
)
if mibBuilder.loadTexts:
    adDS1AlertTable.setStatus("mandatory")
_AdDS1AlertEntry_Object = MibTableRow
adDS1AlertEntry = _AdDS1AlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1)
)
adDS1AlertEntry.setIndexNames(
    (0, "ADTRAN-DS1-MIB", "adDS1AlertIndex"),
)
if mibBuilder.loadTexts:
    adDS1AlertEntry.setStatus("mandatory")


class _AdDS1AlertIndex_Type(Integer32):
    """Custom type adDS1AlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdDS1AlertIndex_Type.__name__ = "Integer32"
_AdDS1AlertIndex_Object = MibTableColumn
adDS1AlertIndex = _AdDS1AlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 1),
    _AdDS1AlertIndex_Type()
)
adDS1AlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1AlertIndex.setStatus("mandatory")


class _AdDS1AlertEnable_Type(Integer32):
    """Custom type adDS1AlertEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1AlertOFF", 1),
          ("ds1AlertON", 2))
    )


_AdDS1AlertEnable_Type.__name__ = "Integer32"
_AdDS1AlertEnable_Object = MibTableColumn
adDS1AlertEnable = _AdDS1AlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 2),
    _AdDS1AlertEnable_Type()
)
adDS1AlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1AlertEnable.setStatus("mandatory")


class _AdDS1CurrentAlert_Type(Integer32):
    """Custom type adDS1CurrentAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AdDS1CurrentAlert_Type.__name__ = "Integer32"
_AdDS1CurrentAlert_Object = MibTableColumn
adDS1CurrentAlert = _AdDS1CurrentAlert_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 3),
    _AdDS1CurrentAlert_Type()
)
adDS1CurrentAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1CurrentAlert.setStatus("mandatory")


class _AdDS1TotalAlert_Type(Integer32):
    """Custom type adDS1TotalAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AdDS1TotalAlert_Type.__name__ = "Integer32"
_AdDS1TotalAlert_Object = MibTableColumn
adDS1TotalAlert = _AdDS1TotalAlert_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 4),
    _AdDS1TotalAlert_Type()
)
adDS1TotalAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1TotalAlert.setStatus("mandatory")


class _AdDS1FarCurrentAlert_Type(Integer32):
    """Custom type adDS1FarCurrentAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_AdDS1FarCurrentAlert_Type.__name__ = "Integer32"
_AdDS1FarCurrentAlert_Object = MibTableColumn
adDS1FarCurrentAlert = _AdDS1FarCurrentAlert_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 5),
    _AdDS1FarCurrentAlert_Type()
)
adDS1FarCurrentAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1FarCurrentAlert.setStatus("mandatory")


class _AdDS1FarTotalAlert_Type(Integer32):
    """Custom type adDS1FarTotalAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_AdDS1FarTotalAlert_Type.__name__ = "Integer32"
_AdDS1FarTotalAlert_Object = MibTableColumn
adDS1FarTotalAlert = _AdDS1FarTotalAlert_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 6),
    _AdDS1FarTotalAlert_Type()
)
adDS1FarTotalAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDS1FarTotalAlert.setStatus("mandatory")


class _AdDS1CurrentArm_Type(Integer32):
    """Custom type adDS1CurrentArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AdDS1CurrentArm_Type.__name__ = "Integer32"
_AdDS1CurrentArm_Object = MibTableColumn
adDS1CurrentArm = _AdDS1CurrentArm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 7),
    _AdDS1CurrentArm_Type()
)
adDS1CurrentArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentArm.setStatus("mandatory")


class _AdDS1TotalArm_Type(Integer32):
    """Custom type adDS1TotalArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AdDS1TotalArm_Type.__name__ = "Integer32"
_AdDS1TotalArm_Object = MibTableColumn
adDS1TotalArm = _AdDS1TotalArm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 8),
    _AdDS1TotalArm_Type()
)
adDS1TotalArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalArm.setStatus("mandatory")


class _AdDS1FarCurrentArm_Type(Integer32):
    """Custom type adDS1FarCurrentArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_AdDS1FarCurrentArm_Type.__name__ = "Integer32"
_AdDS1FarCurrentArm_Object = MibTableColumn
adDS1FarCurrentArm = _AdDS1FarCurrentArm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 9),
    _AdDS1FarCurrentArm_Type()
)
adDS1FarCurrentArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1FarCurrentArm.setStatus("mandatory")


class _AdDS1FarTotalArm_Type(Integer32):
    """Custom type adDS1FarTotalArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_AdDS1FarTotalArm_Type.__name__ = "Integer32"
_AdDS1FarTotalArm_Object = MibTableColumn
adDS1FarTotalArm = _AdDS1FarTotalArm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 2, 1, 10),
    _AdDS1FarTotalArm_Type()
)
adDS1FarTotalArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1FarTotalArm.setStatus("mandatory")
_AdDS1CurrentThreshold_ObjectIdentity = ObjectIdentity
adDS1CurrentThreshold = _AdDS1CurrentThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3)
)
_AdDS1CurrentThrsES_Type = Integer32
_AdDS1CurrentThrsES_Object = MibScalar
adDS1CurrentThrsES = _AdDS1CurrentThrsES_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 1),
    _AdDS1CurrentThrsES_Type()
)
adDS1CurrentThrsES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsES.setStatus("mandatory")
_AdDS1CurrentThrsSES_Type = Integer32
_AdDS1CurrentThrsSES_Object = MibScalar
adDS1CurrentThrsSES = _AdDS1CurrentThrsSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 2),
    _AdDS1CurrentThrsSES_Type()
)
adDS1CurrentThrsSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsSES.setStatus("mandatory")
_AdDS1CurrentThrsSEFS_Type = Integer32
_AdDS1CurrentThrsSEFS_Object = MibScalar
adDS1CurrentThrsSEFS = _AdDS1CurrentThrsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 3),
    _AdDS1CurrentThrsSEFS_Type()
)
adDS1CurrentThrsSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsSEFS.setStatus("mandatory")
_AdDS1CurrentThrsUAS_Type = Integer32
_AdDS1CurrentThrsUAS_Object = MibScalar
adDS1CurrentThrsUAS = _AdDS1CurrentThrsUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 4),
    _AdDS1CurrentThrsUAS_Type()
)
adDS1CurrentThrsUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsUAS.setStatus("mandatory")
_AdDS1CurrentThrsCSS_Type = Integer32
_AdDS1CurrentThrsCSS_Object = MibScalar
adDS1CurrentThrsCSS = _AdDS1CurrentThrsCSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 5),
    _AdDS1CurrentThrsCSS_Type()
)
adDS1CurrentThrsCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsCSS.setStatus("mandatory")
_AdDS1CurrentThrsPCVsf_Type = Integer32
_AdDS1CurrentThrsPCVsf_Object = MibScalar
adDS1CurrentThrsPCVsf = _AdDS1CurrentThrsPCVsf_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 6),
    _AdDS1CurrentThrsPCVsf_Type()
)
adDS1CurrentThrsPCVsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsPCVsf.setStatus("mandatory")
_AdDS1CurrentThrsPCVesf_Type = Integer32
_AdDS1CurrentThrsPCVesf_Object = MibScalar
adDS1CurrentThrsPCVesf = _AdDS1CurrentThrsPCVesf_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 7),
    _AdDS1CurrentThrsPCVesf_Type()
)
adDS1CurrentThrsPCVesf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsPCVesf.setStatus("mandatory")
_AdDS1CurrentThrsLES_Type = Integer32
_AdDS1CurrentThrsLES_Object = MibScalar
adDS1CurrentThrsLES = _AdDS1CurrentThrsLES_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 8),
    _AdDS1CurrentThrsLES_Type()
)
adDS1CurrentThrsLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsLES.setStatus("mandatory")
_AdDS1CurrentThrsLCV_Type = Integer32
_AdDS1CurrentThrsLCV_Object = MibScalar
adDS1CurrentThrsLCV = _AdDS1CurrentThrsLCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 3, 9),
    _AdDS1CurrentThrsLCV_Type()
)
adDS1CurrentThrsLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1CurrentThrsLCV.setStatus("mandatory")
_AdDS1TotalThreshold_ObjectIdentity = ObjectIdentity
adDS1TotalThreshold = _AdDS1TotalThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4)
)
_AdDS1TotalThrsES_Type = Integer32
_AdDS1TotalThrsES_Object = MibScalar
adDS1TotalThrsES = _AdDS1TotalThrsES_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 1),
    _AdDS1TotalThrsES_Type()
)
adDS1TotalThrsES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsES.setStatus("mandatory")
_AdDS1TotalThrsSES_Type = Integer32
_AdDS1TotalThrsSES_Object = MibScalar
adDS1TotalThrsSES = _AdDS1TotalThrsSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 2),
    _AdDS1TotalThrsSES_Type()
)
adDS1TotalThrsSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsSES.setStatus("mandatory")
_AdDS1TotalThrsSEFS_Type = Integer32
_AdDS1TotalThrsSEFS_Object = MibScalar
adDS1TotalThrsSEFS = _AdDS1TotalThrsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 3),
    _AdDS1TotalThrsSEFS_Type()
)
adDS1TotalThrsSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsSEFS.setStatus("mandatory")
_AdDS1TotalThrsUAS_Type = Integer32
_AdDS1TotalThrsUAS_Object = MibScalar
adDS1TotalThrsUAS = _AdDS1TotalThrsUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 4),
    _AdDS1TotalThrsUAS_Type()
)
adDS1TotalThrsUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsUAS.setStatus("mandatory")
_AdDS1TotalThrsCSS_Type = Integer32
_AdDS1TotalThrsCSS_Object = MibScalar
adDS1TotalThrsCSS = _AdDS1TotalThrsCSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 5),
    _AdDS1TotalThrsCSS_Type()
)
adDS1TotalThrsCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsCSS.setStatus("mandatory")
_AdDS1TotalThrsPCVsf_Type = Integer32
_AdDS1TotalThrsPCVsf_Object = MibScalar
adDS1TotalThrsPCVsf = _AdDS1TotalThrsPCVsf_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 6),
    _AdDS1TotalThrsPCVsf_Type()
)
adDS1TotalThrsPCVsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsPCVsf.setStatus("mandatory")
_AdDS1TotalThrsPCVesf_Type = Integer32
_AdDS1TotalThrsPCVesf_Object = MibScalar
adDS1TotalThrsPCVesf = _AdDS1TotalThrsPCVesf_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 7),
    _AdDS1TotalThrsPCVesf_Type()
)
adDS1TotalThrsPCVesf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsPCVesf.setStatus("mandatory")
_AdDS1TotalThrsLES_Type = Integer32
_AdDS1TotalThrsLES_Object = MibScalar
adDS1TotalThrsLES = _AdDS1TotalThrsLES_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 8),
    _AdDS1TotalThrsLES_Type()
)
adDS1TotalThrsLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsLES.setStatus("mandatory")
_AdDS1TotalThrsLCV_Type = Integer32
_AdDS1TotalThrsLCV_Object = MibScalar
adDS1TotalThrsLCV = _AdDS1TotalThrsLCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 3, 4, 9),
    _AdDS1TotalThrsLCV_Type()
)
adDS1TotalThrsLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDS1TotalThrsLCV.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-DS1-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adDS1mg": adDS1mg,
       "adDS1AlarmTable": adDS1AlarmTable,
       "adDS1AlarmEntry": adDS1AlarmEntry,
       "adDS1AlarmIndex": adDS1AlarmIndex,
       "adDS1AlarmEnable": adDS1AlarmEnable,
       "adDS1LineEvent": adDS1LineEvent,
       "adDS1LineArm": adDS1LineArm,
       "adDS1AlertTable": adDS1AlertTable,
       "adDS1AlertEntry": adDS1AlertEntry,
       "adDS1AlertIndex": adDS1AlertIndex,
       "adDS1AlertEnable": adDS1AlertEnable,
       "adDS1CurrentAlert": adDS1CurrentAlert,
       "adDS1TotalAlert": adDS1TotalAlert,
       "adDS1FarCurrentAlert": adDS1FarCurrentAlert,
       "adDS1FarTotalAlert": adDS1FarTotalAlert,
       "adDS1CurrentArm": adDS1CurrentArm,
       "adDS1TotalArm": adDS1TotalArm,
       "adDS1FarCurrentArm": adDS1FarCurrentArm,
       "adDS1FarTotalArm": adDS1FarTotalArm,
       "adDS1CurrentThreshold": adDS1CurrentThreshold,
       "adDS1CurrentThrsES": adDS1CurrentThrsES,
       "adDS1CurrentThrsSES": adDS1CurrentThrsSES,
       "adDS1CurrentThrsSEFS": adDS1CurrentThrsSEFS,
       "adDS1CurrentThrsUAS": adDS1CurrentThrsUAS,
       "adDS1CurrentThrsCSS": adDS1CurrentThrsCSS,
       "adDS1CurrentThrsPCVsf": adDS1CurrentThrsPCVsf,
       "adDS1CurrentThrsPCVesf": adDS1CurrentThrsPCVesf,
       "adDS1CurrentThrsLES": adDS1CurrentThrsLES,
       "adDS1CurrentThrsLCV": adDS1CurrentThrsLCV,
       "adDS1TotalThreshold": adDS1TotalThreshold,
       "adDS1TotalThrsES": adDS1TotalThrsES,
       "adDS1TotalThrsSES": adDS1TotalThrsSES,
       "adDS1TotalThrsSEFS": adDS1TotalThrsSEFS,
       "adDS1TotalThrsUAS": adDS1TotalThrsUAS,
       "adDS1TotalThrsCSS": adDS1TotalThrsCSS,
       "adDS1TotalThrsPCVsf": adDS1TotalThrsPCVsf,
       "adDS1TotalThrsPCVesf": adDS1TotalThrsPCVesf,
       "adDS1TotalThrsLES": adDS1TotalThrsLES,
       "adDS1TotalThrsLCV": adDS1TotalThrsLCV}
)
