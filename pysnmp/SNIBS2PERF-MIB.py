# SNMP MIB module (SNIBS2PERF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNIBS2PERF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:51 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniSar_ObjectIdentity = ObjectIdentity
sniSar = _SniSar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13)
)
_SniSarParms_ObjectIdentity = ObjectIdentity
sniSarParms = _SniSarParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 1)
)
_SniSarMpoints_ObjectIdentity = ObjectIdentity
sniSarMpoints = _SniSarMpoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 2)
)
_SniSarHist_ObjectIdentity = ObjectIdentity
sniSarHist = _SniSarHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 3)
)
_SniSM2Parms_ObjectIdentity = ObjectIdentity
sniSM2Parms = _SniSM2Parms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 10)
)


class _Sm2Status_Type(Integer32):
    """Custom type sm2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-running", 2),
          ("running", 1),
          ("unkown", 3))
    )


_Sm2Status_Type.__name__ = "Integer32"
_Sm2Status_Object = MibScalar
sm2Status = _Sm2Status_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 10, 1),
    _Sm2Status_Type()
)
sm2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2Status.setStatus("mandatory")


class _Sm2Version_Type(DisplayString):
    """Custom type sm2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sm2Version_Type.__name__ = "DisplayString"
_Sm2Version_Object = MibScalar
sm2Version = _Sm2Version_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 10, 2),
    _Sm2Version_Type()
)
sm2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2Version.setStatus("mandatory")


class _Sm2Interval_Type(Integer32):
    """Custom type sm2Interval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_Sm2Interval_Type.__name__ = "Integer32"
_Sm2Interval_Object = MibScalar
sm2Interval = _Sm2Interval_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 10, 3),
    _Sm2Interval_Type()
)
sm2Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm2Interval.setStatus("mandatory")


class _Sm2SamplingCycle_Type(Integer32):
    """Custom type sm2SamplingCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_Sm2SamplingCycle_Type.__name__ = "Integer32"
_Sm2SamplingCycle_Object = MibScalar
sm2SamplingCycle = _Sm2SamplingCycle_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 10, 4),
    _Sm2SamplingCycle_Type()
)
sm2SamplingCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sm2SamplingCycle.setStatus("mandatory")
_SniSM2Mpoints_ObjectIdentity = ObjectIdentity
sniSM2Mpoints = _SniSM2Mpoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11)
)
_Sm2MpBasic_ObjectIdentity = ObjectIdentity
sm2MpBasic = _Sm2MpBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1)
)


class _Sm2BasicStatus_Type(Integer32):
    """Custom type sm2BasicStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2BasicStatus_Type.__name__ = "Integer32"
_Sm2BasicStatus_Object = MibScalar
sm2BasicStatus = _Sm2BasicStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1, 1),
    _Sm2BasicStatus_Type()
)
sm2BasicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2BasicStatus.setStatus("mandatory")
_Sm2BasicTime_Type = DateAndTime
_Sm2BasicTime_Object = MibScalar
sm2BasicTime = _Sm2BasicTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1, 2),
    _Sm2BasicTime_Type()
)
sm2BasicTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2BasicTime.setStatus("mandatory")


class _Sm2BasicTimeString_Type(DisplayString):
    """Custom type sm2BasicTimeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
        ValueSizeConstraint(28, 28),
    )


_Sm2BasicTimeString_Type.__name__ = "DisplayString"
_Sm2BasicTimeString_Object = MibScalar
sm2BasicTimeString = _Sm2BasicTimeString_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1, 3),
    _Sm2BasicTimeString_Type()
)
sm2BasicTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2BasicTimeString.setStatus("mandatory")


class _Sm2BasicSamples_Type(Integer32):
    """Custom type sm2BasicSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2BasicSamples_Type.__name__ = "Integer32"
_Sm2BasicSamples_Object = MibScalar
sm2BasicSamples = _Sm2BasicSamples_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1, 4),
    _Sm2BasicSamples_Type()
)
sm2BasicSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2BasicSamples.setStatus("mandatory")


class _Sm2BasicMaxLogMach_Type(Integer32):
    """Custom type sm2BasicMaxLogMach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2BasicMaxLogMach_Type.__name__ = "Integer32"
_Sm2BasicMaxLogMach_Object = MibScalar
sm2BasicMaxLogMach = _Sm2BasicMaxLogMach_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1, 5),
    _Sm2BasicMaxLogMach_Type()
)
sm2BasicMaxLogMach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2BasicMaxLogMach.setStatus("mandatory")


class _Sm2BasicVM2000_Type(Integer32):
    """Custom type sm2BasicVM2000 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("no-data", -1))
    )


_Sm2BasicVM2000_Type.__name__ = "Integer32"
_Sm2BasicVM2000_Object = MibScalar
sm2BasicVM2000 = _Sm2BasicVM2000_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 1, 6),
    _Sm2BasicVM2000_Type()
)
sm2BasicVM2000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2BasicVM2000.setStatus("mandatory")
_Sm2MpTimeIO_ObjectIdentity = ObjectIdentity
sm2MpTimeIO = _Sm2MpTimeIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2)
)


class _Sm2TimeIOStatus_Type(Integer32):
    """Custom type sm2TimeIOStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2TimeIOStatus_Type.__name__ = "Integer32"
_Sm2TimeIOStatus_Object = MibScalar
sm2TimeIOStatus = _Sm2TimeIOStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 1),
    _Sm2TimeIOStatus_Type()
)
sm2TimeIOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOStatus.setStatus("mandatory")


class _Sm2TimeIOActMach_Type(Integer32):
    """Custom type sm2TimeIOActMach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOActMach_Type.__name__ = "Integer32"
_Sm2TimeIOActMach_Object = MibScalar
sm2TimeIOActMach = _Sm2TimeIOActMach_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 2),
    _Sm2TimeIOActMach_Type()
)
sm2TimeIOActMach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOActMach.setStatus("mandatory")


class _Sm2TimeIOMachTabNumber_Type(Integer32):
    """Custom type sm2TimeIOMachTabNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabNumber_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabNumber_Object = MibScalar
sm2TimeIOMachTabNumber = _Sm2TimeIOMachTabNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 3),
    _Sm2TimeIOMachTabNumber_Type()
)
sm2TimeIOMachTabNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabNumber.setStatus("mandatory")
_Sm2TimeIOMachTab_Object = MibTable
sm2TimeIOMachTab = _Sm2TimeIOMachTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4)
)
if mibBuilder.loadTexts:
    sm2TimeIOMachTab.setStatus("mandatory")
_Sm2TimeIOMachTabEntry_Object = MibTableRow
sm2TimeIOMachTabEntry = _Sm2TimeIOMachTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1)
)
sm2TimeIOMachTabEntry.setIndexNames(
    (0, "SNIBS2PERF-MIB", "sm2TimeIOMachTabIndex"),
)
if mibBuilder.loadTexts:
    sm2TimeIOMachTabEntry.setStatus("mandatory")


class _Sm2TimeIOMachTabIndex_Type(Integer32):
    """Custom type sm2TimeIOMachTabIndex based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("average", 100),
          ("mach1", 1),
          ("mach10", 10),
          ("mach11", 11),
          ("mach12", 12),
          ("mach13", 13),
          ("mach14", 14),
          ("mach15", 15),
          ("mach16", 16),
          ("mach2", 2),
          ("mach3", 3),
          ("mach4", 4),
          ("mach5", 5),
          ("mach6", 6),
          ("mach7", 7),
          ("mach8", 8),
          ("mach9", 9))
    )


_Sm2TimeIOMachTabIndex_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabIndex_Object = MibTableColumn
sm2TimeIOMachTabIndex = _Sm2TimeIOMachTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 1),
    _Sm2TimeIOMachTabIndex_Type()
)
sm2TimeIOMachTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabIndex.setStatus("mandatory")


class _Sm2TimeIOMachTabIdleTime_Type(Integer32):
    """Custom type sm2TimeIOMachTabIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabIdleTime_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabIdleTime_Object = MibTableColumn
sm2TimeIOMachTabIdleTime = _Sm2TimeIOMachTabIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 2),
    _Sm2TimeIOMachTabIdleTime_Type()
)
sm2TimeIOMachTabIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabIdleTime.setStatus("mandatory")


class _Sm2TimeIOMachTabTUTime_Type(Integer32):
    """Custom type sm2TimeIOMachTabTUTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabTUTime_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabTUTime_Object = MibTableColumn
sm2TimeIOMachTabTUTime = _Sm2TimeIOMachTabTUTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 3),
    _Sm2TimeIOMachTabTUTime_Type()
)
sm2TimeIOMachTabTUTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabTUTime.setStatus("mandatory")


class _Sm2TimeIOMachTabTPRTime_Type(Integer32):
    """Custom type sm2TimeIOMachTabTPRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabTPRTime_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabTPRTime_Object = MibTableColumn
sm2TimeIOMachTabTPRTime = _Sm2TimeIOMachTabTPRTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 4),
    _Sm2TimeIOMachTabTPRTime_Type()
)
sm2TimeIOMachTabTPRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabTPRTime.setStatus("mandatory")


class _Sm2TimeIOMachTabSIHTime_Type(Integer32):
    """Custom type sm2TimeIOMachTabSIHTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabSIHTime_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabSIHTime_Object = MibTableColumn
sm2TimeIOMachTabSIHTime = _Sm2TimeIOMachTabSIHTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 5),
    _Sm2TimeIOMachTabSIHTime_Type()
)
sm2TimeIOMachTabSIHTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabSIHTime.setStatus("mandatory")


class _Sm2TimeIOMachTabStopTime_Type(Integer32):
    """Custom type sm2TimeIOMachTabStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabStopTime_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabStopTime_Object = MibTableColumn
sm2TimeIOMachTabStopTime = _Sm2TimeIOMachTabStopTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 6),
    _Sm2TimeIOMachTabStopTime_Type()
)
sm2TimeIOMachTabStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabStopTime.setStatus("mandatory")


class _Sm2TimeIOMachTabPagingIO_Type(Integer32):
    """Custom type sm2TimeIOMachTabPagingIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabPagingIO_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabPagingIO_Object = MibTableColumn
sm2TimeIOMachTabPagingIO = _Sm2TimeIOMachTabPagingIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 7),
    _Sm2TimeIOMachTabPagingIO_Type()
)
sm2TimeIOMachTabPagingIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabPagingIO.setStatus("mandatory")


class _Sm2TimeIOMachTabDiskIO_Type(Integer32):
    """Custom type sm2TimeIOMachTabDiskIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabDiskIO_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabDiskIO_Object = MibTableColumn
sm2TimeIOMachTabDiskIO = _Sm2TimeIOMachTabDiskIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 8),
    _Sm2TimeIOMachTabDiskIO_Type()
)
sm2TimeIOMachTabDiskIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabDiskIO.setStatus("mandatory")


class _Sm2TimeIOMachTabTapeIO_Type(Integer32):
    """Custom type sm2TimeIOMachTabTapeIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabTapeIO_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabTapeIO_Object = MibTableColumn
sm2TimeIOMachTabTapeIO = _Sm2TimeIOMachTabTapeIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 9),
    _Sm2TimeIOMachTabTapeIO_Type()
)
sm2TimeIOMachTabTapeIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabTapeIO.setStatus("mandatory")


class _Sm2TimeIOMachTabPrinterIO_Type(Integer32):
    """Custom type sm2TimeIOMachTabPrinterIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabPrinterIO_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabPrinterIO_Object = MibTableColumn
sm2TimeIOMachTabPrinterIO = _Sm2TimeIOMachTabPrinterIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 10),
    _Sm2TimeIOMachTabPrinterIO_Type()
)
sm2TimeIOMachTabPrinterIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabPrinterIO.setStatus("mandatory")


class _Sm2TimeIOMachTabOtherIO_Type(Integer32):
    """Custom type sm2TimeIOMachTabOtherIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2TimeIOMachTabOtherIO_Type.__name__ = "Integer32"
_Sm2TimeIOMachTabOtherIO_Object = MibTableColumn
sm2TimeIOMachTabOtherIO = _Sm2TimeIOMachTabOtherIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 2, 4, 1, 11),
    _Sm2TimeIOMachTabOtherIO_Type()
)
sm2TimeIOMachTabOtherIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2TimeIOMachTabOtherIO.setStatus("mandatory")
_Sm2MpMemory_ObjectIdentity = ObjectIdentity
sm2MpMemory = _Sm2MpMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3)
)


class _Sm2MemoryStatus_Type(Integer32):
    """Custom type sm2MemoryStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2MemoryStatus_Type.__name__ = "Integer32"
_Sm2MemoryStatus_Object = MibScalar
sm2MemoryStatus = _Sm2MemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 1),
    _Sm2MemoryStatus_Type()
)
sm2MemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryStatus.setStatus("mandatory")


class _Sm2MemorySize_Type(Integer32):
    """Custom type sm2MemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemorySize_Type.__name__ = "Integer32"
_Sm2MemorySize_Object = MibScalar
sm2MemorySize = _Sm2MemorySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 2),
    _Sm2MemorySize_Type()
)
sm2MemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemorySize.setStatus("mandatory")


class _Sm2MemoryPageableSize_Type(Integer32):
    """Custom type sm2MemoryPageableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageableSize_Type.__name__ = "Integer32"
_Sm2MemoryPageableSize_Object = MibScalar
sm2MemoryPageableSize = _Sm2MemoryPageableSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 3),
    _Sm2MemoryPageableSize_Type()
)
sm2MemoryPageableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageableSize.setStatus("mandatory")


class _Sm2MemoryFreeReadSize_Type(Integer32):
    """Custom type sm2MemoryFreeReadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryFreeReadSize_Type.__name__ = "Integer32"
_Sm2MemoryFreeReadSize_Object = MibScalar
sm2MemoryFreeReadSize = _Sm2MemoryFreeReadSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 4),
    _Sm2MemoryFreeReadSize_Type()
)
sm2MemoryFreeReadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryFreeReadSize.setStatus("mandatory")


class _Sm2MemoryFreeReadWriteSize_Type(Integer32):
    """Custom type sm2MemoryFreeReadWriteSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryFreeReadWriteSize_Type.__name__ = "Integer32"
_Sm2MemoryFreeReadWriteSize_Object = MibScalar
sm2MemoryFreeReadWriteSize = _Sm2MemoryFreeReadWriteSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 5),
    _Sm2MemoryFreeReadWriteSize_Type()
)
sm2MemoryFreeReadWriteSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryFreeReadWriteSize.setStatus("mandatory")


class _Sm2MemoryPagingAreaTotal_Type(Integer32):
    """Custom type sm2MemoryPagingAreaTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPagingAreaTotal_Type.__name__ = "Integer32"
_Sm2MemoryPagingAreaTotal_Object = MibScalar
sm2MemoryPagingAreaTotal = _Sm2MemoryPagingAreaTotal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 6),
    _Sm2MemoryPagingAreaTotal_Type()
)
sm2MemoryPagingAreaTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPagingAreaTotal.setStatus("mandatory")


class _Sm2MemoryPagingAreaESGS_Type(Integer32):
    """Custom type sm2MemoryPagingAreaESGS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPagingAreaESGS_Type.__name__ = "Integer32"
_Sm2MemoryPagingAreaESGS_Object = MibScalar
sm2MemoryPagingAreaESGS = _Sm2MemoryPagingAreaESGS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 7),
    _Sm2MemoryPagingAreaESGS_Type()
)
sm2MemoryPagingAreaESGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPagingAreaESGS.setStatus("mandatory")


class _Sm2MemoryPagingAreaFree_Type(Integer32):
    """Custom type sm2MemoryPagingAreaFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPagingAreaFree_Type.__name__ = "Integer32"
_Sm2MemoryPagingAreaFree_Object = MibScalar
sm2MemoryPagingAreaFree = _Sm2MemoryPagingAreaFree_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 8),
    _Sm2MemoryPagingAreaFree_Type()
)
sm2MemoryPagingAreaFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPagingAreaFree.setStatus("mandatory")


class _Sm2MemoryPageFaults_Type(Integer32):
    """Custom type sm2MemoryPageFaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageFaults_Type.__name__ = "Integer32"
_Sm2MemoryPageFaults_Object = MibScalar
sm2MemoryPageFaults = _Sm2MemoryPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 9),
    _Sm2MemoryPageFaults_Type()
)
sm2MemoryPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageFaults.setStatus("mandatory")


class _Sm2MemoryPage1stFaults_Type(Integer32):
    """Custom type sm2MemoryPage1stFaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPage1stFaults_Type.__name__ = "Integer32"
_Sm2MemoryPage1stFaults_Object = MibScalar
sm2MemoryPage1stFaults = _Sm2MemoryPage1stFaults_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 10),
    _Sm2MemoryPage1stFaults_Type()
)
sm2MemoryPage1stFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPage1stFaults.setStatus("mandatory")


class _Sm2MemoryPageReclaims_Type(Integer32):
    """Custom type sm2MemoryPageReclaims based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageReclaims_Type.__name__ = "Integer32"
_Sm2MemoryPageReclaims_Object = MibScalar
sm2MemoryPageReclaims = _Sm2MemoryPageReclaims_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 11),
    _Sm2MemoryPageReclaims_Type()
)
sm2MemoryPageReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageReclaims.setStatus("mandatory")


class _Sm2MemoryPageReads_Type(Integer32):
    """Custom type sm2MemoryPageReads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageReads_Type.__name__ = "Integer32"
_Sm2MemoryPageReads_Object = MibScalar
sm2MemoryPageReads = _Sm2MemoryPageReads_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 12),
    _Sm2MemoryPageReads_Type()
)
sm2MemoryPageReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageReads.setStatus("mandatory")


class _Sm2MemoryPageWrites_Type(Integer32):
    """Custom type sm2MemoryPageWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageWrites_Type.__name__ = "Integer32"
_Sm2MemoryPageWrites_Object = MibScalar
sm2MemoryPageWrites = _Sm2MemoryPageWrites_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 13),
    _Sm2MemoryPageWrites_Type()
)
sm2MemoryPageWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageWrites.setStatus("mandatory")


class _Sm2MemoryPageReadESGS_Type(Integer32):
    """Custom type sm2MemoryPageReadESGS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageReadESGS_Type.__name__ = "Integer32"
_Sm2MemoryPageReadESGS_Object = MibScalar
sm2MemoryPageReadESGS = _Sm2MemoryPageReadESGS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 14),
    _Sm2MemoryPageReadESGS_Type()
)
sm2MemoryPageReadESGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageReadESGS.setStatus("mandatory")


class _Sm2MemoryPageWriteESGS_Type(Integer32):
    """Custom type sm2MemoryPageWriteESGS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2MemoryPageWriteESGS_Type.__name__ = "Integer32"
_Sm2MemoryPageWriteESGS_Object = MibScalar
sm2MemoryPageWriteESGS = _Sm2MemoryPageWriteESGS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 3, 15),
    _Sm2MemoryPageWriteESGS_Type()
)
sm2MemoryPageWriteESGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2MemoryPageWriteESGS.setStatus("mandatory")
_Sm2MpCategory_ObjectIdentity = ObjectIdentity
sm2MpCategory = _Sm2MpCategory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 5)
)


class _Sm2CategoryStatus_Type(Integer32):
    """Custom type sm2CategoryStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2CategoryStatus_Type.__name__ = "Integer32"
_Sm2CategoryStatus_Object = MibScalar
sm2CategoryStatus = _Sm2CategoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 5, 1),
    _Sm2CategoryStatus_Type()
)
sm2CategoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2CategoryStatus.setStatus("mandatory")


class _Sm2CategorySystemTasks_Type(Integer32):
    """Custom type sm2CategorySystemTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2CategorySystemTasks_Type.__name__ = "Integer32"
_Sm2CategorySystemTasks_Object = MibScalar
sm2CategorySystemTasks = _Sm2CategorySystemTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 5, 2),
    _Sm2CategorySystemTasks_Type()
)
sm2CategorySystemTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2CategorySystemTasks.setStatus("mandatory")


class _Sm2CategoryDialogTasks_Type(Integer32):
    """Custom type sm2CategoryDialogTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2CategoryDialogTasks_Type.__name__ = "Integer32"
_Sm2CategoryDialogTasks_Object = MibScalar
sm2CategoryDialogTasks = _Sm2CategoryDialogTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 5, 3),
    _Sm2CategoryDialogTasks_Type()
)
sm2CategoryDialogTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2CategoryDialogTasks.setStatus("mandatory")


class _Sm2CategoryBatchTasks_Type(Integer32):
    """Custom type sm2CategoryBatchTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2CategoryBatchTasks_Type.__name__ = "Integer32"
_Sm2CategoryBatchTasks_Object = MibScalar
sm2CategoryBatchTasks = _Sm2CategoryBatchTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 5, 4),
    _Sm2CategoryBatchTasks_Type()
)
sm2CategoryBatchTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2CategoryBatchTasks.setStatus("mandatory")


class _Sm2CategoryTPTasks_Type(Integer32):
    """Custom type sm2CategoryTPTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2CategoryTPTasks_Type.__name__ = "Integer32"
_Sm2CategoryTPTasks_Object = MibScalar
sm2CategoryTPTasks = _Sm2CategoryTPTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 5, 5),
    _Sm2CategoryTPTasks_Type()
)
sm2CategoryTPTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2CategoryTPTasks.setStatus("mandatory")
_Sm2MpSDevice_ObjectIdentity = ObjectIdentity
sm2MpSDevice = _Sm2MpSDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7)
)


class _Sm2SDeviceStatus_Type(Integer32):
    """Custom type sm2SDeviceStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2SDeviceStatus_Type.__name__ = "Integer32"
_Sm2SDeviceStatus_Object = MibScalar
sm2SDeviceStatus = _Sm2SDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 1),
    _Sm2SDeviceStatus_Type()
)
sm2SDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceStatus.setStatus("mandatory")


class _Sm2SDeviceRealNumber_Type(Integer32):
    """Custom type sm2SDeviceRealNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2SDeviceRealNumber_Type.__name__ = "Integer32"
_Sm2SDeviceRealNumber_Object = MibScalar
sm2SDeviceRealNumber = _Sm2SDeviceRealNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 2),
    _Sm2SDeviceRealNumber_Type()
)
sm2SDeviceRealNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceRealNumber.setStatus("mandatory")


class _Sm2SDeviceTabNumber_Type(Integer32):
    """Custom type sm2SDeviceTabNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2SDeviceTabNumber_Type.__name__ = "Integer32"
_Sm2SDeviceTabNumber_Object = MibScalar
sm2SDeviceTabNumber = _Sm2SDeviceTabNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 3),
    _Sm2SDeviceTabNumber_Type()
)
sm2SDeviceTabNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabNumber.setStatus("mandatory")
_Sm2SDeviceTab_Object = MibTable
sm2SDeviceTab = _Sm2SDeviceTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4)
)
if mibBuilder.loadTexts:
    sm2SDeviceTab.setStatus("mandatory")
_Sm2SDeviceTabEntry_Object = MibTableRow
sm2SDeviceTabEntry = _Sm2SDeviceTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1)
)
sm2SDeviceTabEntry.setIndexNames(
    (0, "SNIBS2PERF-MIB", "sm2SDeviceTabIndex"),
)
if mibBuilder.loadTexts:
    sm2SDeviceTabEntry.setStatus("mandatory")
_Sm2SDeviceTabIndex_Type = Integer32
_Sm2SDeviceTabIndex_Object = MibTableColumn
sm2SDeviceTabIndex = _Sm2SDeviceTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 1),
    _Sm2SDeviceTabIndex_Type()
)
sm2SDeviceTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabIndex.setStatus("mandatory")


class _Sm2SDeviceTabVSN_Type(DisplayString):
    """Custom type sm2SDeviceTabVSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Sm2SDeviceTabVSN_Type.__name__ = "DisplayString"
_Sm2SDeviceTabVSN_Object = MibTableColumn
sm2SDeviceTabVSN = _Sm2SDeviceTabVSN_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 2),
    _Sm2SDeviceTabVSN_Type()
)
sm2SDeviceTabVSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabVSN.setStatus("mandatory")


class _Sm2SDeviceTabMnemonic_Type(DisplayString):
    """Custom type sm2SDeviceTabMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sm2SDeviceTabMnemonic_Type.__name__ = "DisplayString"
_Sm2SDeviceTabMnemonic_Object = MibTableColumn
sm2SDeviceTabMnemonic = _Sm2SDeviceTabMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 3),
    _Sm2SDeviceTabMnemonic_Type()
)
sm2SDeviceTabMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabMnemonic.setStatus("mandatory")
_Sm2SDeviceTabType_Type = DisplayString
_Sm2SDeviceTabType_Object = MibTableColumn
sm2SDeviceTabType = _Sm2SDeviceTabType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 4),
    _Sm2SDeviceTabType_Type()
)
sm2SDeviceTabType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabType.setStatus("mandatory")


class _Sm2SDeviceTabIO_Type(Integer32):
    """Custom type sm2SDeviceTabIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2SDeviceTabIO_Type.__name__ = "Integer32"
_Sm2SDeviceTabIO_Object = MibTableColumn
sm2SDeviceTabIO = _Sm2SDeviceTabIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 5),
    _Sm2SDeviceTabIO_Type()
)
sm2SDeviceTabIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabIO.setStatus("mandatory")


class _Sm2SDeviceTabBusyDms_Type(Integer32):
    """Custom type sm2SDeviceTabBusyDms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2SDeviceTabBusyDms_Type.__name__ = "Integer32"
_Sm2SDeviceTabBusyDms_Object = MibTableColumn
sm2SDeviceTabBusyDms = _Sm2SDeviceTabBusyDms_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 6),
    _Sm2SDeviceTabBusyDms_Type()
)
sm2SDeviceTabBusyDms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabBusyDms.setStatus("mandatory")


class _Sm2SDeviceTabBusyPaging_Type(Integer32):
    """Custom type sm2SDeviceTabBusyPaging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2SDeviceTabBusyPaging_Type.__name__ = "Integer32"
_Sm2SDeviceTabBusyPaging_Object = MibTableColumn
sm2SDeviceTabBusyPaging = _Sm2SDeviceTabBusyPaging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 7, 4, 1, 7),
    _Sm2SDeviceTabBusyPaging_Type()
)
sm2SDeviceTabBusyPaging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2SDeviceTabBusyPaging.setStatus("mandatory")
_Sm2MpUTM_ObjectIdentity = ObjectIdentity
sm2MpUTM = _Sm2MpUTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15)
)


class _Sm2UTMStatus_Type(Integer32):
    """Custom type sm2UTMStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2UTMStatus_Type.__name__ = "Integer32"
_Sm2UTMStatus_Object = MibScalar
sm2UTMStatus = _Sm2UTMStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 1),
    _Sm2UTMStatus_Type()
)
sm2UTMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMStatus.setStatus("mandatory")


class _Sm2UTMTabNumber_Type(Integer32):
    """Custom type sm2UTMTabNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabNumber_Type.__name__ = "Integer32"
_Sm2UTMTabNumber_Object = MibScalar
sm2UTMTabNumber = _Sm2UTMTabNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 2),
    _Sm2UTMTabNumber_Type()
)
sm2UTMTabNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabNumber.setStatus("mandatory")
_Sm2UTMTab_Object = MibTable
sm2UTMTab = _Sm2UTMTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3)
)
if mibBuilder.loadTexts:
    sm2UTMTab.setStatus("mandatory")
_Sm2UTMTabEntry_Object = MibTableRow
sm2UTMTabEntry = _Sm2UTMTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1)
)
sm2UTMTabEntry.setIndexNames(
    (0, "SNIBS2PERF-MIB", "sm2UTMTabIndex"),
)
if mibBuilder.loadTexts:
    sm2UTMTabEntry.setStatus("mandatory")
_Sm2UTMTabIndex_Type = Integer32
_Sm2UTMTabIndex_Object = MibTableColumn
sm2UTMTabIndex = _Sm2UTMTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 1),
    _Sm2UTMTabIndex_Type()
)
sm2UTMTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabIndex.setStatus("mandatory")


class _Sm2UTMTabApplName_Type(DisplayString):
    """Custom type sm2UTMTabApplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sm2UTMTabApplName_Type.__name__ = "DisplayString"
_Sm2UTMTabApplName_Object = MibTableColumn
sm2UTMTabApplName = _Sm2UTMTabApplName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 2),
    _Sm2UTMTabApplName_Type()
)
sm2UTMTabApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabApplName.setStatus("mandatory")


class _Sm2UTMTabUTMVersion_Type(DisplayString):
    """Custom type sm2UTMTabUTMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sm2UTMTabUTMVersion_Type.__name__ = "DisplayString"
_Sm2UTMTabUTMVersion_Object = MibTableColumn
sm2UTMTabUTMVersion = _Sm2UTMTabUTMVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 3),
    _Sm2UTMTabUTMVersion_Type()
)
sm2UTMTabUTMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabUTMVersion.setStatus("mandatory")


class _Sm2UTMTabApplMode_Type(Integer32):
    """Custom type sm2UTMTabApplMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-data", -1),
          ("utm-f-application", 2),
          ("utm-s-application", 1))
    )


_Sm2UTMTabApplMode_Type.__name__ = "Integer32"
_Sm2UTMTabApplMode_Object = MibTableColumn
sm2UTMTabApplMode = _Sm2UTMTabApplMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 4),
    _Sm2UTMTabApplMode_Type()
)
sm2UTMTabApplMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabApplMode.setStatus("mandatory")


class _Sm2UTMTabTasksRunning_Type(Integer32):
    """Custom type sm2UTMTabTasksRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabTasksRunning_Type.__name__ = "Integer32"
_Sm2UTMTabTasksRunning_Object = MibTableColumn
sm2UTMTabTasksRunning = _Sm2UTMTabTasksRunning_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 5),
    _Sm2UTMTabTasksRunning_Type()
)
sm2UTMTabTasksRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabTasksRunning.setStatus("mandatory")


class _Sm2UTMTabMaxAsyncTasks_Type(Integer32):
    """Custom type sm2UTMTabMaxAsyncTasks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabMaxAsyncTasks_Type.__name__ = "Integer32"
_Sm2UTMTabMaxAsyncTasks_Object = MibTableColumn
sm2UTMTabMaxAsyncTasks = _Sm2UTMTabMaxAsyncTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 6),
    _Sm2UTMTabMaxAsyncTasks_Type()
)
sm2UTMTabMaxAsyncTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabMaxAsyncTasks.setStatus("mandatory")


class _Sm2UTMTabConnectedUsers_Type(Integer32):
    """Custom type sm2UTMTabConnectedUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabConnectedUsers_Type.__name__ = "Integer32"
_Sm2UTMTabConnectedUsers_Object = MibTableColumn
sm2UTMTabConnectedUsers = _Sm2UTMTabConnectedUsers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 7),
    _Sm2UTMTabConnectedUsers_Type()
)
sm2UTMTabConnectedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabConnectedUsers.setStatus("mandatory")


class _Sm2UTMTabCurrConvDial_Type(Integer32):
    """Custom type sm2UTMTabCurrConvDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabCurrConvDial_Type.__name__ = "Integer32"
_Sm2UTMTabCurrConvDial_Object = MibTableColumn
sm2UTMTabCurrConvDial = _Sm2UTMTabCurrConvDial_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 8),
    _Sm2UTMTabCurrConvDial_Type()
)
sm2UTMTabCurrConvDial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabCurrConvDial.setStatus("mandatory")


class _Sm2UTMTabCurrConvAsync_Type(Integer32):
    """Custom type sm2UTMTabCurrConvAsync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabCurrConvAsync_Type.__name__ = "Integer32"
_Sm2UTMTabCurrConvAsync_Object = MibTableColumn
sm2UTMTabCurrConvAsync = _Sm2UTMTabCurrConvAsync_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 9),
    _Sm2UTMTabCurrConvAsync_Type()
)
sm2UTMTabCurrConvAsync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabCurrConvAsync.setStatus("mandatory")


class _Sm2UTMTabWaitingATACS_Type(Integer32):
    """Custom type sm2UTMTabWaitingATACS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabWaitingATACS_Type.__name__ = "Integer32"
_Sm2UTMTabWaitingATACS_Object = MibTableColumn
sm2UTMTabWaitingATACS = _Sm2UTMTabWaitingATACS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 10),
    _Sm2UTMTabWaitingATACS_Type()
)
sm2UTMTabWaitingATACS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabWaitingATACS.setStatus("mandatory")


class _Sm2UTMTabCacheHitRate_Type(Integer32):
    """Custom type sm2UTMTabCacheHitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabCacheHitRate_Type.__name__ = "Integer32"
_Sm2UTMTabCacheHitRate_Object = MibTableColumn
sm2UTMTabCacheHitRate = _Sm2UTMTabCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 11),
    _Sm2UTMTabCacheHitRate_Type()
)
sm2UTMTabCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabCacheHitRate.setStatus("mandatory")


class _Sm2UTMTabFreePagePool_Type(Integer32):
    """Custom type sm2UTMTabFreePagePool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabFreePagePool_Type.__name__ = "Integer32"
_Sm2UTMTabFreePagePool_Object = MibTableColumn
sm2UTMTabFreePagePool = _Sm2UTMTabFreePagePool_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 12),
    _Sm2UTMTabFreePagePool_Type()
)
sm2UTMTabFreePagePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabFreePagePool.setStatus("mandatory")


class _Sm2UTMTabDialTACS_Type(Integer32):
    """Custom type sm2UTMTabDialTACS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialTACS_Type.__name__ = "Integer32"
_Sm2UTMTabDialTACS_Object = MibTableColumn
sm2UTMTabDialTACS = _Sm2UTMTabDialTACS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 13),
    _Sm2UTMTabDialTACS_Type()
)
sm2UTMTabDialTACS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialTACS.setStatus("mandatory")


class _Sm2UTMTabAsyncTACS_Type(Integer32):
    """Custom type sm2UTMTabAsyncTACS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncTACS_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncTACS_Object = MibTableColumn
sm2UTMTabAsyncTACS = _Sm2UTMTabAsyncTACS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 14),
    _Sm2UTMTabAsyncTACS_Type()
)
sm2UTMTabAsyncTACS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncTACS.setStatus("mandatory")


class _Sm2UTMTabDialTotalTime_Type(Integer32):
    """Custom type sm2UTMTabDialTotalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialTotalTime_Type.__name__ = "Integer32"
_Sm2UTMTabDialTotalTime_Object = MibTableColumn
sm2UTMTabDialTotalTime = _Sm2UTMTabDialTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 15),
    _Sm2UTMTabDialTotalTime_Type()
)
sm2UTMTabDialTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialTotalTime.setStatus("mandatory")


class _Sm2UTMTabDialTotalTimeDB_Type(Integer32):
    """Custom type sm2UTMTabDialTotalTimeDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialTotalTimeDB_Type.__name__ = "Integer32"
_Sm2UTMTabDialTotalTimeDB_Object = MibTableColumn
sm2UTMTabDialTotalTimeDB = _Sm2UTMTabDialTotalTimeDB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 16),
    _Sm2UTMTabDialTotalTimeDB_Type()
)
sm2UTMTabDialTotalTimeDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialTotalTimeDB.setStatus("mandatory")


class _Sm2UTMTabDialDBTime_Type(Integer32):
    """Custom type sm2UTMTabDialDBTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialDBTime_Type.__name__ = "Integer32"
_Sm2UTMTabDialDBTime_Object = MibTableColumn
sm2UTMTabDialDBTime = _Sm2UTMTabDialDBTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 17),
    _Sm2UTMTabDialDBTime_Type()
)
sm2UTMTabDialDBTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialDBTime.setStatus("mandatory")


class _Sm2UTMTabDialDBCall_Type(Integer32):
    """Custom type sm2UTMTabDialDBCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialDBCall_Type.__name__ = "Integer32"
_Sm2UTMTabDialDBCall_Object = MibTableColumn
sm2UTMTabDialDBCall = _Sm2UTMTabDialDBCall_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 18),
    _Sm2UTMTabDialDBCall_Type()
)
sm2UTMTabDialDBCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialDBCall.setStatus("mandatory")


class _Sm2UTMTabDialDBCpuTime_Type(Integer32):
    """Custom type sm2UTMTabDialDBCpuTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialDBCpuTime_Type.__name__ = "Integer32"
_Sm2UTMTabDialDBCpuTime_Object = MibTableColumn
sm2UTMTabDialDBCpuTime = _Sm2UTMTabDialDBCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 19),
    _Sm2UTMTabDialDBCpuTime_Type()
)
sm2UTMTabDialDBCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialDBCpuTime.setStatus("mandatory")


class _Sm2UTMTabDialDBIO_Type(Integer32):
    """Custom type sm2UTMTabDialDBIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialDBIO_Type.__name__ = "Integer32"
_Sm2UTMTabDialDBIO_Object = MibTableColumn
sm2UTMTabDialDBIO = _Sm2UTMTabDialDBIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 20),
    _Sm2UTMTabDialDBIO_Type()
)
sm2UTMTabDialDBIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialDBIO.setStatus("mandatory")


class _Sm2UTMTabDialUTMCpuTime_Type(Integer32):
    """Custom type sm2UTMTabDialUTMCpuTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialUTMCpuTime_Type.__name__ = "Integer32"
_Sm2UTMTabDialUTMCpuTime_Object = MibTableColumn
sm2UTMTabDialUTMCpuTime = _Sm2UTMTabDialUTMCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 21),
    _Sm2UTMTabDialUTMCpuTime_Type()
)
sm2UTMTabDialUTMCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialUTMCpuTime.setStatus("mandatory")


class _Sm2UTMTabDialUTMIO_Type(Integer32):
    """Custom type sm2UTMTabDialUTMIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabDialUTMIO_Type.__name__ = "Integer32"
_Sm2UTMTabDialUTMIO_Object = MibTableColumn
sm2UTMTabDialUTMIO = _Sm2UTMTabDialUTMIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 22),
    _Sm2UTMTabDialUTMIO_Type()
)
sm2UTMTabDialUTMIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabDialUTMIO.setStatus("mandatory")


class _Sm2UTMTabAsyncTotalTime_Type(Integer32):
    """Custom type sm2UTMTabAsyncTotalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncTotalTime_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncTotalTime_Object = MibTableColumn
sm2UTMTabAsyncTotalTime = _Sm2UTMTabAsyncTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 23),
    _Sm2UTMTabAsyncTotalTime_Type()
)
sm2UTMTabAsyncTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncTotalTime.setStatus("mandatory")


class _Sm2UTMTabAsyncTotalTimeDB_Type(Integer32):
    """Custom type sm2UTMTabAsyncTotalTimeDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncTotalTimeDB_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncTotalTimeDB_Object = MibTableColumn
sm2UTMTabAsyncTotalTimeDB = _Sm2UTMTabAsyncTotalTimeDB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 24),
    _Sm2UTMTabAsyncTotalTimeDB_Type()
)
sm2UTMTabAsyncTotalTimeDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncTotalTimeDB.setStatus("mandatory")


class _Sm2UTMTabAsyncDBTime_Type(Integer32):
    """Custom type sm2UTMTabAsyncDBTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncDBTime_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncDBTime_Object = MibTableColumn
sm2UTMTabAsyncDBTime = _Sm2UTMTabAsyncDBTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 25),
    _Sm2UTMTabAsyncDBTime_Type()
)
sm2UTMTabAsyncDBTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncDBTime.setStatus("mandatory")


class _Sm2UTMTabAsyncDBCall_Type(Integer32):
    """Custom type sm2UTMTabAsyncDBCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncDBCall_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncDBCall_Object = MibTableColumn
sm2UTMTabAsyncDBCall = _Sm2UTMTabAsyncDBCall_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 26),
    _Sm2UTMTabAsyncDBCall_Type()
)
sm2UTMTabAsyncDBCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncDBCall.setStatus("mandatory")


class _Sm2UTMTabAsyncDBCpuTime_Type(Integer32):
    """Custom type sm2UTMTabAsyncDBCpuTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncDBCpuTime_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncDBCpuTime_Object = MibTableColumn
sm2UTMTabAsyncDBCpuTime = _Sm2UTMTabAsyncDBCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 27),
    _Sm2UTMTabAsyncDBCpuTime_Type()
)
sm2UTMTabAsyncDBCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncDBCpuTime.setStatus("mandatory")


class _Sm2UTMTabAsyncDBIO_Type(Integer32):
    """Custom type sm2UTMTabAsyncDBIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncDBIO_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncDBIO_Object = MibTableColumn
sm2UTMTabAsyncDBIO = _Sm2UTMTabAsyncDBIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 28),
    _Sm2UTMTabAsyncDBIO_Type()
)
sm2UTMTabAsyncDBIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncDBIO.setStatus("mandatory")


class _Sm2UTMTabAsyncUTMCpuTime_Type(Integer32):
    """Custom type sm2UTMTabAsyncUTMCpuTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncUTMCpuTime_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncUTMCpuTime_Object = MibTableColumn
sm2UTMTabAsyncUTMCpuTime = _Sm2UTMTabAsyncUTMCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 29),
    _Sm2UTMTabAsyncUTMCpuTime_Type()
)
sm2UTMTabAsyncUTMCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncUTMCpuTime.setStatus("mandatory")


class _Sm2UTMTabAsyncUTMIO_Type(Integer32):
    """Custom type sm2UTMTabAsyncUTMIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2UTMTabAsyncUTMIO_Type.__name__ = "Integer32"
_Sm2UTMTabAsyncUTMIO_Object = MibTableColumn
sm2UTMTabAsyncUTMIO = _Sm2UTMTabAsyncUTMIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 15, 3, 1, 30),
    _Sm2UTMTabAsyncUTMIO_Type()
)
sm2UTMTabAsyncUTMIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2UTMTabAsyncUTMIO.setStatus("mandatory")
_Sm2MpPerTask_ObjectIdentity = ObjectIdentity
sm2MpPerTask = _Sm2MpPerTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16)
)


class _Sm2PerTaskStatus_Type(Integer32):
    """Custom type sm2PerTaskStatus based on Integer32"""
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
        *(("data-invalid", 2),
          ("data-supported", 1),
          ("no-subsystem", 4),
          ("prg-inactive", 3),
          ("sm2-not-running", 5),
          ("unkown", 6))
    )


_Sm2PerTaskStatus_Type.__name__ = "Integer32"
_Sm2PerTaskStatus_Object = MibScalar
sm2PerTaskStatus = _Sm2PerTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 1),
    _Sm2PerTaskStatus_Type()
)
sm2PerTaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskStatus.setStatus("mandatory")


class _Sm2PerTaskRealNumber_Type(Integer32):
    """Custom type sm2PerTaskRealNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskRealNumber_Type.__name__ = "Integer32"
_Sm2PerTaskRealNumber_Object = MibScalar
sm2PerTaskRealNumber = _Sm2PerTaskRealNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 2),
    _Sm2PerTaskRealNumber_Type()
)
sm2PerTaskRealNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskRealNumber.setStatus("mandatory")


class _Sm2PerTaskTabNumber_Type(Integer32):
    """Custom type sm2PerTaskTabNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskTabNumber_Type.__name__ = "Integer32"
_Sm2PerTaskTabNumber_Object = MibScalar
sm2PerTaskTabNumber = _Sm2PerTaskTabNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 3),
    _Sm2PerTaskTabNumber_Type()
)
sm2PerTaskTabNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabNumber.setStatus("mandatory")
_Sm2PerTaskTab_Object = MibTable
sm2PerTaskTab = _Sm2PerTaskTab_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4)
)
if mibBuilder.loadTexts:
    sm2PerTaskTab.setStatus("mandatory")
_Sm2PerTaskTabEntry_Object = MibTableRow
sm2PerTaskTabEntry = _Sm2PerTaskTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1)
)
sm2PerTaskTabEntry.setIndexNames(
    (0, "SNIBS2PERF-MIB", "sm2PerTaskTabIndex"),
)
if mibBuilder.loadTexts:
    sm2PerTaskTabEntry.setStatus("mandatory")
_Sm2PerTaskTabIndex_Type = Integer32
_Sm2PerTaskTabIndex_Object = MibTableColumn
sm2PerTaskTabIndex = _Sm2PerTaskTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 1),
    _Sm2PerTaskTabIndex_Type()
)
sm2PerTaskTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabIndex.setStatus("mandatory")


class _Sm2PerTaskTabTSN_Type(DisplayString):
    """Custom type sm2PerTaskTabTSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sm2PerTaskTabTSN_Type.__name__ = "DisplayString"
_Sm2PerTaskTabTSN_Object = MibTableColumn
sm2PerTaskTabTSN = _Sm2PerTaskTabTSN_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 2),
    _Sm2PerTaskTabTSN_Type()
)
sm2PerTaskTabTSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabTSN.setStatus("mandatory")


class _Sm2PerTaskTabUserID_Type(DisplayString):
    """Custom type sm2PerTaskTabUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sm2PerTaskTabUserID_Type.__name__ = "DisplayString"
_Sm2PerTaskTabUserID_Object = MibTableColumn
sm2PerTaskTabUserID = _Sm2PerTaskTabUserID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 3),
    _Sm2PerTaskTabUserID_Type()
)
sm2PerTaskTabUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabUserID.setStatus("mandatory")


class _Sm2PerTaskTabJobName_Type(DisplayString):
    """Custom type sm2PerTaskTabJobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sm2PerTaskTabJobName_Type.__name__ = "DisplayString"
_Sm2PerTaskTabJobName_Object = MibTableColumn
sm2PerTaskTabJobName = _Sm2PerTaskTabJobName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 4),
    _Sm2PerTaskTabJobName_Type()
)
sm2PerTaskTabJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabJobName.setStatus("mandatory")


class _Sm2PerTaskTabType_Type(Integer32):
    """Custom type sm2PerTaskTabType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("batch", 3),
          ("dialog", 2),
          ("no-data", -1),
          ("system", 1),
          ("tp", 4))
    )


_Sm2PerTaskTabType_Type.__name__ = "Integer32"
_Sm2PerTaskTabType_Object = MibTableColumn
sm2PerTaskTabType = _Sm2PerTaskTabType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 5),
    _Sm2PerTaskTabType_Type()
)
sm2PerTaskTabType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabType.setStatus("mandatory")


class _Sm2PerTaskTabCPU_Type(Integer32):
    """Custom type sm2PerTaskTabCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskTabCPU_Type.__name__ = "Integer32"
_Sm2PerTaskTabCPU_Object = MibTableColumn
sm2PerTaskTabCPU = _Sm2PerTaskTabCPU_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 6),
    _Sm2PerTaskTabCPU_Type()
)
sm2PerTaskTabCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabCPU.setStatus("mandatory")


class _Sm2PerTaskTabIO_Type(Integer32):
    """Custom type sm2PerTaskTabIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskTabIO_Type.__name__ = "Integer32"
_Sm2PerTaskTabIO_Object = MibTableColumn
sm2PerTaskTabIO = _Sm2PerTaskTabIO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 7),
    _Sm2PerTaskTabIO_Type()
)
sm2PerTaskTabIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabIO.setStatus("mandatory")


class _Sm2PerTaskTabUPG_Type(Integer32):
    """Custom type sm2PerTaskTabUPG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskTabUPG_Type.__name__ = "Integer32"
_Sm2PerTaskTabUPG_Object = MibTableColumn
sm2PerTaskTabUPG = _Sm2PerTaskTabUPG_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 8),
    _Sm2PerTaskTabUPG_Type()
)
sm2PerTaskTabUPG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabUPG.setStatus("mandatory")


class _Sm2PerTaskTabServiceUnits_Type(Integer32):
    """Custom type sm2PerTaskTabServiceUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskTabServiceUnits_Type.__name__ = "Integer32"
_Sm2PerTaskTabServiceUnits_Object = MibTableColumn
sm2PerTaskTabServiceUnits = _Sm2PerTaskTabServiceUnits_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 9),
    _Sm2PerTaskTabServiceUnits_Type()
)
sm2PerTaskTabServiceUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabServiceUnits.setStatus("mandatory")


class _Sm2PerTaskTabPageRead_Type(Integer32):
    """Custom type sm2PerTaskTabPageRead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("no-data", -1)
    )


_Sm2PerTaskTabPageRead_Type.__name__ = "Integer32"
_Sm2PerTaskTabPageRead_Object = MibTableColumn
sm2PerTaskTabPageRead = _Sm2PerTaskTabPageRead_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 13, 11, 16, 4, 1, 10),
    _Sm2PerTaskTabPageRead_Type()
)
sm2PerTaskTabPageRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sm2PerTaskTabPageRead.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNIBS2PERF-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniSar": sniSar,
       "sniSarParms": sniSarParms,
       "sniSarMpoints": sniSarMpoints,
       "sniSarHist": sniSarHist,
       "sniSM2Parms": sniSM2Parms,
       "sm2Status": sm2Status,
       "sm2Version": sm2Version,
       "sm2Interval": sm2Interval,
       "sm2SamplingCycle": sm2SamplingCycle,
       "sniSM2Mpoints": sniSM2Mpoints,
       "sm2MpBasic": sm2MpBasic,
       "sm2BasicStatus": sm2BasicStatus,
       "sm2BasicTime": sm2BasicTime,
       "sm2BasicTimeString": sm2BasicTimeString,
       "sm2BasicSamples": sm2BasicSamples,
       "sm2BasicMaxLogMach": sm2BasicMaxLogMach,
       "sm2BasicVM2000": sm2BasicVM2000,
       "sm2MpTimeIO": sm2MpTimeIO,
       "sm2TimeIOStatus": sm2TimeIOStatus,
       "sm2TimeIOActMach": sm2TimeIOActMach,
       "sm2TimeIOMachTabNumber": sm2TimeIOMachTabNumber,
       "sm2TimeIOMachTab": sm2TimeIOMachTab,
       "sm2TimeIOMachTabEntry": sm2TimeIOMachTabEntry,
       "sm2TimeIOMachTabIndex": sm2TimeIOMachTabIndex,
       "sm2TimeIOMachTabIdleTime": sm2TimeIOMachTabIdleTime,
       "sm2TimeIOMachTabTUTime": sm2TimeIOMachTabTUTime,
       "sm2TimeIOMachTabTPRTime": sm2TimeIOMachTabTPRTime,
       "sm2TimeIOMachTabSIHTime": sm2TimeIOMachTabSIHTime,
       "sm2TimeIOMachTabStopTime": sm2TimeIOMachTabStopTime,
       "sm2TimeIOMachTabPagingIO": sm2TimeIOMachTabPagingIO,
       "sm2TimeIOMachTabDiskIO": sm2TimeIOMachTabDiskIO,
       "sm2TimeIOMachTabTapeIO": sm2TimeIOMachTabTapeIO,
       "sm2TimeIOMachTabPrinterIO": sm2TimeIOMachTabPrinterIO,
       "sm2TimeIOMachTabOtherIO": sm2TimeIOMachTabOtherIO,
       "sm2MpMemory": sm2MpMemory,
       "sm2MemoryStatus": sm2MemoryStatus,
       "sm2MemorySize": sm2MemorySize,
       "sm2MemoryPageableSize": sm2MemoryPageableSize,
       "sm2MemoryFreeReadSize": sm2MemoryFreeReadSize,
       "sm2MemoryFreeReadWriteSize": sm2MemoryFreeReadWriteSize,
       "sm2MemoryPagingAreaTotal": sm2MemoryPagingAreaTotal,
       "sm2MemoryPagingAreaESGS": sm2MemoryPagingAreaESGS,
       "sm2MemoryPagingAreaFree": sm2MemoryPagingAreaFree,
       "sm2MemoryPageFaults": sm2MemoryPageFaults,
       "sm2MemoryPage1stFaults": sm2MemoryPage1stFaults,
       "sm2MemoryPageReclaims": sm2MemoryPageReclaims,
       "sm2MemoryPageReads": sm2MemoryPageReads,
       "sm2MemoryPageWrites": sm2MemoryPageWrites,
       "sm2MemoryPageReadESGS": sm2MemoryPageReadESGS,
       "sm2MemoryPageWriteESGS": sm2MemoryPageWriteESGS,
       "sm2MpCategory": sm2MpCategory,
       "sm2CategoryStatus": sm2CategoryStatus,
       "sm2CategorySystemTasks": sm2CategorySystemTasks,
       "sm2CategoryDialogTasks": sm2CategoryDialogTasks,
       "sm2CategoryBatchTasks": sm2CategoryBatchTasks,
       "sm2CategoryTPTasks": sm2CategoryTPTasks,
       "sm2MpSDevice": sm2MpSDevice,
       "sm2SDeviceStatus": sm2SDeviceStatus,
       "sm2SDeviceRealNumber": sm2SDeviceRealNumber,
       "sm2SDeviceTabNumber": sm2SDeviceTabNumber,
       "sm2SDeviceTab": sm2SDeviceTab,
       "sm2SDeviceTabEntry": sm2SDeviceTabEntry,
       "sm2SDeviceTabIndex": sm2SDeviceTabIndex,
       "sm2SDeviceTabVSN": sm2SDeviceTabVSN,
       "sm2SDeviceTabMnemonic": sm2SDeviceTabMnemonic,
       "sm2SDeviceTabType": sm2SDeviceTabType,
       "sm2SDeviceTabIO": sm2SDeviceTabIO,
       "sm2SDeviceTabBusyDms": sm2SDeviceTabBusyDms,
       "sm2SDeviceTabBusyPaging": sm2SDeviceTabBusyPaging,
       "sm2MpUTM": sm2MpUTM,
       "sm2UTMStatus": sm2UTMStatus,
       "sm2UTMTabNumber": sm2UTMTabNumber,
       "sm2UTMTab": sm2UTMTab,
       "sm2UTMTabEntry": sm2UTMTabEntry,
       "sm2UTMTabIndex": sm2UTMTabIndex,
       "sm2UTMTabApplName": sm2UTMTabApplName,
       "sm2UTMTabUTMVersion": sm2UTMTabUTMVersion,
       "sm2UTMTabApplMode": sm2UTMTabApplMode,
       "sm2UTMTabTasksRunning": sm2UTMTabTasksRunning,
       "sm2UTMTabMaxAsyncTasks": sm2UTMTabMaxAsyncTasks,
       "sm2UTMTabConnectedUsers": sm2UTMTabConnectedUsers,
       "sm2UTMTabCurrConvDial": sm2UTMTabCurrConvDial,
       "sm2UTMTabCurrConvAsync": sm2UTMTabCurrConvAsync,
       "sm2UTMTabWaitingATACS": sm2UTMTabWaitingATACS,
       "sm2UTMTabCacheHitRate": sm2UTMTabCacheHitRate,
       "sm2UTMTabFreePagePool": sm2UTMTabFreePagePool,
       "sm2UTMTabDialTACS": sm2UTMTabDialTACS,
       "sm2UTMTabAsyncTACS": sm2UTMTabAsyncTACS,
       "sm2UTMTabDialTotalTime": sm2UTMTabDialTotalTime,
       "sm2UTMTabDialTotalTimeDB": sm2UTMTabDialTotalTimeDB,
       "sm2UTMTabDialDBTime": sm2UTMTabDialDBTime,
       "sm2UTMTabDialDBCall": sm2UTMTabDialDBCall,
       "sm2UTMTabDialDBCpuTime": sm2UTMTabDialDBCpuTime,
       "sm2UTMTabDialDBIO": sm2UTMTabDialDBIO,
       "sm2UTMTabDialUTMCpuTime": sm2UTMTabDialUTMCpuTime,
       "sm2UTMTabDialUTMIO": sm2UTMTabDialUTMIO,
       "sm2UTMTabAsyncTotalTime": sm2UTMTabAsyncTotalTime,
       "sm2UTMTabAsyncTotalTimeDB": sm2UTMTabAsyncTotalTimeDB,
       "sm2UTMTabAsyncDBTime": sm2UTMTabAsyncDBTime,
       "sm2UTMTabAsyncDBCall": sm2UTMTabAsyncDBCall,
       "sm2UTMTabAsyncDBCpuTime": sm2UTMTabAsyncDBCpuTime,
       "sm2UTMTabAsyncDBIO": sm2UTMTabAsyncDBIO,
       "sm2UTMTabAsyncUTMCpuTime": sm2UTMTabAsyncUTMCpuTime,
       "sm2UTMTabAsyncUTMIO": sm2UTMTabAsyncUTMIO,
       "sm2MpPerTask": sm2MpPerTask,
       "sm2PerTaskStatus": sm2PerTaskStatus,
       "sm2PerTaskRealNumber": sm2PerTaskRealNumber,
       "sm2PerTaskTabNumber": sm2PerTaskTabNumber,
       "sm2PerTaskTab": sm2PerTaskTab,
       "sm2PerTaskTabEntry": sm2PerTaskTabEntry,
       "sm2PerTaskTabIndex": sm2PerTaskTabIndex,
       "sm2PerTaskTabTSN": sm2PerTaskTabTSN,
       "sm2PerTaskTabUserID": sm2PerTaskTabUserID,
       "sm2PerTaskTabJobName": sm2PerTaskTabJobName,
       "sm2PerTaskTabType": sm2PerTaskTabType,
       "sm2PerTaskTabCPU": sm2PerTaskTabCPU,
       "sm2PerTaskTabIO": sm2PerTaskTabIO,
       "sm2PerTaskTabUPG": sm2PerTaskTabUPG,
       "sm2PerTaskTabServiceUnits": sm2PerTaskTabServiceUnits,
       "sm2PerTaskTabPageRead": sm2PerTaskTabPageRead}
)
