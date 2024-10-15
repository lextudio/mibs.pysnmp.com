# SNMP MIB module (ADTRAN-AOS-DS1-EXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-DS1-EXT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:06 2024
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

(adGenAOSConformance,
 adGenAOSWan) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSWan")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

adGenAOSDs1ThresholdsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSDs1Threshold_ObjectIdentity = ObjectIdentity
adGenAOSDs1Threshold = _AdGenAOSDs1Threshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1)
)
_AdGenAOSDs1ThresholdTraps_ObjectIdentity = ObjectIdentity
adGenAOSDs1ThresholdTraps = _AdGenAOSDs1ThresholdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 0)
)
if mibBuilder.loadTexts:
    adGenAOSDs1ThresholdTraps.setStatus("current")
_AdGenAOSDs1ThresholdsReachedTable_Object = MibTable
adGenAOSDs1ThresholdsReachedTable = _AdGenAOSDs1ThresholdsReachedTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAOSDs1ThresholdsReachedTable.setStatus("current")
_AdGenAOSDs1ThresholdsReachedEntry_Object = MibTableRow
adGenAOSDs1ThresholdsReachedEntry = _AdGenAOSDs1ThresholdsReachedEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1)
)
adGenAOSDs1ThresholdsReachedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSDs1ThresholdsReachedEntry.setStatus("current")
_AdGenAOSDs1Index_Type = InterfaceIndex
_AdGenAOSDs1Index_Object = MibTableColumn
adGenAOSDs1Index = _AdGenAOSDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 1),
    _AdGenAOSDs1Index_Type()
)
adGenAOSDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSDs1Index.setStatus("current")


class _AdGenAOSDs1ThresholdAlarms_Type(Bits):
    """Custom type adGenAOSDs1ThresholdAlarms based on Bits"""
    namedValues = NamedValues(
        *(("ds1ThresholdReached15MinBES", 0),
          ("ds1ThresholdReached15MinCSS", 1),
          ("ds1ThresholdReached15MinDM", 2),
          ("ds1ThresholdReached15MinES", 3),
          ("ds1ThresholdReached15MinLCV", 4),
          ("ds1ThresholdReached15MinLES", 5),
          ("ds1ThresholdReached15MinPCV", 6),
          ("ds1ThresholdReached15MinSEFS", 8),
          ("ds1ThresholdReached15MinSES", 7),
          ("ds1ThresholdReached15MinUAS", 9),
          ("ds1ThresholdReached24HrBES", 10),
          ("ds1ThresholdReached24HrCSS", 11),
          ("ds1ThresholdReached24HrDM", 12),
          ("ds1ThresholdReached24HrES", 13),
          ("ds1ThresholdReached24HrLCV", 14),
          ("ds1ThresholdReached24HrLES", 15),
          ("ds1ThresholdReached24HrPCV", 16),
          ("ds1ThresholdReached24HrSEFS", 18),
          ("ds1ThresholdReached24HrSES", 17),
          ("ds1ThresholdReached24HrUAS", 19))
    )

_AdGenAOSDs1ThresholdAlarms_Type.__name__ = "Bits"
_AdGenAOSDs1ThresholdAlarms_Object = MibTableColumn
adGenAOSDs1ThresholdAlarms = _AdGenAOSDs1ThresholdAlarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 2),
    _AdGenAOSDs1ThresholdAlarms_Type()
)
adGenAOSDs1ThresholdAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSDs1ThresholdAlarms.setStatus("current")


class _AdGenAOSDs1PreviousThresholdAlarms_Type(Bits):
    """Custom type adGenAOSDs1PreviousThresholdAlarms based on Bits"""
    namedValues = NamedValues(
        *(("ds1ThresholdReached15MinBES", 0),
          ("ds1ThresholdReached15MinCSS", 1),
          ("ds1ThresholdReached15MinDM", 2),
          ("ds1ThresholdReached15MinES", 3),
          ("ds1ThresholdReached15MinLCV", 4),
          ("ds1ThresholdReached15MinLES", 5),
          ("ds1ThresholdReached15MinPCV", 6),
          ("ds1ThresholdReached15MinSEFS", 8),
          ("ds1ThresholdReached15MinSES", 7),
          ("ds1ThresholdReached15MinUAS", 9),
          ("ds1ThresholdReached24HrBES", 10),
          ("ds1ThresholdReached24HrCSS", 11),
          ("ds1ThresholdReached24HrDM", 12),
          ("ds1ThresholdReached24HrES", 13),
          ("ds1ThresholdReached24HrLCV", 14),
          ("ds1ThresholdReached24HrLES", 15),
          ("ds1ThresholdReached24HrPCV", 16),
          ("ds1ThresholdReached24HrSEFS", 18),
          ("ds1ThresholdReached24HrSES", 17),
          ("ds1ThresholdReached24HrUAS", 19))
    )

_AdGenAOSDs1PreviousThresholdAlarms_Type.__name__ = "Bits"
_AdGenAOSDs1PreviousThresholdAlarms_Object = MibTableColumn
adGenAOSDs1PreviousThresholdAlarms = _AdGenAOSDs1PreviousThresholdAlarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 3),
    _AdGenAOSDs1PreviousThresholdAlarms_Type()
)
adGenAOSDs1PreviousThresholdAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSDs1PreviousThresholdAlarms.setStatus("current")
_AdGenAOSDs1LastThresholdChange_Type = TimeStamp
_AdGenAOSDs1LastThresholdChange_Object = MibTableColumn
adGenAOSDs1LastThresholdChange = _AdGenAOSDs1LastThresholdChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 4),
    _AdGenAOSDs1LastThresholdChange_Type()
)
adGenAOSDs1LastThresholdChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSDs1LastThresholdChange.setStatus("current")


class _AdGenAOSDs1Threshold15MinBES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinBES based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinBES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinBES_Object = MibScalar
adGenAOSDs1Threshold15MinBES = _AdGenAOSDs1Threshold15MinBES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 2),
    _AdGenAOSDs1Threshold15MinBES_Type()
)
adGenAOSDs1Threshold15MinBES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinBES.setStatus("current")


class _AdGenAOSDs1Threshold15MinCSS_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinCSS based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinCSS_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinCSS_Object = MibScalar
adGenAOSDs1Threshold15MinCSS = _AdGenAOSDs1Threshold15MinCSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 3),
    _AdGenAOSDs1Threshold15MinCSS_Type()
)
adGenAOSDs1Threshold15MinCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinCSS.setStatus("current")


class _AdGenAOSDs1Threshold15MinDM_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinDM based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinDM_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinDM_Object = MibScalar
adGenAOSDs1Threshold15MinDM = _AdGenAOSDs1Threshold15MinDM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 4),
    _AdGenAOSDs1Threshold15MinDM_Type()
)
adGenAOSDs1Threshold15MinDM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinDM.setStatus("current")


class _AdGenAOSDs1Threshold15MinES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinES based on Unsigned32"""
    defaultValue = 65

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinES_Object = MibScalar
adGenAOSDs1Threshold15MinES = _AdGenAOSDs1Threshold15MinES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 5),
    _AdGenAOSDs1Threshold15MinES_Type()
)
adGenAOSDs1Threshold15MinES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinES.setStatus("current")


class _AdGenAOSDs1Threshold15MinLCV_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinLCV based on Unsigned32"""
    defaultValue = 13340

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinLCV_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinLCV_Object = MibScalar
adGenAOSDs1Threshold15MinLCV = _AdGenAOSDs1Threshold15MinLCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 6),
    _AdGenAOSDs1Threshold15MinLCV_Type()
)
adGenAOSDs1Threshold15MinLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinLCV.setStatus("current")


class _AdGenAOSDs1Threshold15MinLES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinLES based on Unsigned32"""
    defaultValue = 65

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinLES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinLES_Object = MibScalar
adGenAOSDs1Threshold15MinLES = _AdGenAOSDs1Threshold15MinLES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 7),
    _AdGenAOSDs1Threshold15MinLES_Type()
)
adGenAOSDs1Threshold15MinLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinLES.setStatus("current")


class _AdGenAOSDs1Threshold15MinPCV_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinPCV based on Unsigned32"""
    defaultValue = 72

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinPCV_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinPCV_Object = MibScalar
adGenAOSDs1Threshold15MinPCV = _AdGenAOSDs1Threshold15MinPCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 8),
    _AdGenAOSDs1Threshold15MinPCV_Type()
)
adGenAOSDs1Threshold15MinPCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinPCV.setStatus("current")


class _AdGenAOSDs1Threshold15MinSES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinSES based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinSES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinSES_Object = MibScalar
adGenAOSDs1Threshold15MinSES = _AdGenAOSDs1Threshold15MinSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 9),
    _AdGenAOSDs1Threshold15MinSES_Type()
)
adGenAOSDs1Threshold15MinSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinSES.setStatus("current")


class _AdGenAOSDs1Threshold15MinSEFS_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinSEFS based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinSEFS_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinSEFS_Object = MibScalar
adGenAOSDs1Threshold15MinSEFS = _AdGenAOSDs1Threshold15MinSEFS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 10),
    _AdGenAOSDs1Threshold15MinSEFS_Type()
)
adGenAOSDs1Threshold15MinSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinSEFS.setStatus("current")


class _AdGenAOSDs1Threshold15MinUAS_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold15MinUAS based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold15MinUAS_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold15MinUAS_Object = MibScalar
adGenAOSDs1Threshold15MinUAS = _AdGenAOSDs1Threshold15MinUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 11),
    _AdGenAOSDs1Threshold15MinUAS_Type()
)
adGenAOSDs1Threshold15MinUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold15MinUAS.setStatus("current")


class _AdGenAOSDs1Threshold24HrBES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrBES based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrBES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrBES_Object = MibScalar
adGenAOSDs1Threshold24HrBES = _AdGenAOSDs1Threshold24HrBES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 12),
    _AdGenAOSDs1Threshold24HrBES_Type()
)
adGenAOSDs1Threshold24HrBES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrBES.setStatus("current")


class _AdGenAOSDs1Threshold24HrCSS_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrCSS based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrCSS_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrCSS_Object = MibScalar
adGenAOSDs1Threshold24HrCSS = _AdGenAOSDs1Threshold24HrCSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 13),
    _AdGenAOSDs1Threshold24HrCSS_Type()
)
adGenAOSDs1Threshold24HrCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrCSS.setStatus("current")


class _AdGenAOSDs1Threshold24HrDM_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrDM based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrDM_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrDM_Object = MibScalar
adGenAOSDs1Threshold24HrDM = _AdGenAOSDs1Threshold24HrDM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 14),
    _AdGenAOSDs1Threshold24HrDM_Type()
)
adGenAOSDs1Threshold24HrDM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrDM.setStatus("current")


class _AdGenAOSDs1Threshold24HrES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrES based on Unsigned32"""
    defaultValue = 648

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrES_Object = MibScalar
adGenAOSDs1Threshold24HrES = _AdGenAOSDs1Threshold24HrES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 15),
    _AdGenAOSDs1Threshold24HrES_Type()
)
adGenAOSDs1Threshold24HrES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrES.setStatus("current")


class _AdGenAOSDs1Threshold24HrLCV_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrLCV based on Unsigned32"""
    defaultValue = 133400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrLCV_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrLCV_Object = MibScalar
adGenAOSDs1Threshold24HrLCV = _AdGenAOSDs1Threshold24HrLCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 16),
    _AdGenAOSDs1Threshold24HrLCV_Type()
)
adGenAOSDs1Threshold24HrLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrLCV.setStatus("current")


class _AdGenAOSDs1Threshold24HrLES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrLES based on Unsigned32"""
    defaultValue = 648

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrLES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrLES_Object = MibScalar
adGenAOSDs1Threshold24HrLES = _AdGenAOSDs1Threshold24HrLES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 17),
    _AdGenAOSDs1Threshold24HrLES_Type()
)
adGenAOSDs1Threshold24HrLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrLES.setStatus("current")


class _AdGenAOSDs1Threshold24HrPCV_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrPCV based on Unsigned32"""
    defaultValue = 691

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrPCV_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrPCV_Object = MibScalar
adGenAOSDs1Threshold24HrPCV = _AdGenAOSDs1Threshold24HrPCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 18),
    _AdGenAOSDs1Threshold24HrPCV_Type()
)
adGenAOSDs1Threshold24HrPCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrPCV.setStatus("current")


class _AdGenAOSDs1Threshold24HrSES_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrSES based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrSES_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrSES_Object = MibScalar
adGenAOSDs1Threshold24HrSES = _AdGenAOSDs1Threshold24HrSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 19),
    _AdGenAOSDs1Threshold24HrSES_Type()
)
adGenAOSDs1Threshold24HrSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrSES.setStatus("current")


class _AdGenAOSDs1Threshold24HrSEFS_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrSEFS based on Unsigned32"""
    defaultValue = 17

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrSEFS_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrSEFS_Object = MibScalar
adGenAOSDs1Threshold24HrSEFS = _AdGenAOSDs1Threshold24HrSEFS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 20),
    _AdGenAOSDs1Threshold24HrSEFS_Type()
)
adGenAOSDs1Threshold24HrSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrSEFS.setStatus("current")


class _AdGenAOSDs1Threshold24HrUAS_Type(Unsigned32):
    """Custom type adGenAOSDs1Threshold24HrUAS based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenAOSDs1Threshold24HrUAS_Type.__name__ = "Unsigned32"
_AdGenAOSDs1Threshold24HrUAS_Object = MibScalar
adGenAOSDs1Threshold24HrUAS = _AdGenAOSDs1Threshold24HrUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 21),
    _AdGenAOSDs1Threshold24HrUAS_Type()
)
adGenAOSDs1Threshold24HrUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSDs1Threshold24HrUAS.setStatus("current")
_AdGenAOSDs1ThresholdConformance_ObjectIdentity = ObjectIdentity
adGenAOSDs1ThresholdConformance = _AdGenAOSDs1ThresholdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6)
)
_AdAOSDs1ThresholdCompliances_ObjectIdentity = ObjectIdentity
adAOSDs1ThresholdCompliances = _AdAOSDs1ThresholdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 1)
)
_AdAOSDs1ThresholdGroups_ObjectIdentity = ObjectIdentity
adAOSDs1ThresholdGroups = _AdAOSDs1ThresholdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 2)
)

# Managed Objects groups

adGenAOSDs1ThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 2, 1)
)
adGenAOSDs1ThresholdGroup.setObjects(
      *(("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Index"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1PreviousThresholdAlarms"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1LastThresholdChange"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1ThresholdAlarms"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinBES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinCSS"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinDM"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinLCV"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinLES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinPCV"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinSES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinSEFS"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinUAS"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrBES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrCSS"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrDM"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrLCV"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrLES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrPCV"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrSES"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrSEFS"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrUAS"))
)
if mibBuilder.loadTexts:
    adGenAOSDs1ThresholdGroup.setStatus("current")


# Notification objects

adGenAOSDs1ThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 0, 1)
)
adGenAOSDs1ThresholdReached.setObjects(
      *(("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1ThresholdAlarms"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1PreviousThresholdAlarms"),
        ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1LastThresholdChange"))
)
if mibBuilder.loadTexts:
    adGenAOSDs1ThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

adAOSDs1ThresholdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 1, 1)
)
if mibBuilder.loadTexts:
    adAOSDs1ThresholdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-DS1-EXT",
    **{"adGenAOSDs1Threshold": adGenAOSDs1Threshold,
       "adGenAOSDs1ThresholdTraps": adGenAOSDs1ThresholdTraps,
       "adGenAOSDs1ThresholdReached": adGenAOSDs1ThresholdReached,
       "adGenAOSDs1ThresholdsReachedTable": adGenAOSDs1ThresholdsReachedTable,
       "adGenAOSDs1ThresholdsReachedEntry": adGenAOSDs1ThresholdsReachedEntry,
       "adGenAOSDs1Index": adGenAOSDs1Index,
       "adGenAOSDs1ThresholdAlarms": adGenAOSDs1ThresholdAlarms,
       "adGenAOSDs1PreviousThresholdAlarms": adGenAOSDs1PreviousThresholdAlarms,
       "adGenAOSDs1LastThresholdChange": adGenAOSDs1LastThresholdChange,
       "adGenAOSDs1Threshold15MinBES": adGenAOSDs1Threshold15MinBES,
       "adGenAOSDs1Threshold15MinCSS": adGenAOSDs1Threshold15MinCSS,
       "adGenAOSDs1Threshold15MinDM": adGenAOSDs1Threshold15MinDM,
       "adGenAOSDs1Threshold15MinES": adGenAOSDs1Threshold15MinES,
       "adGenAOSDs1Threshold15MinLCV": adGenAOSDs1Threshold15MinLCV,
       "adGenAOSDs1Threshold15MinLES": adGenAOSDs1Threshold15MinLES,
       "adGenAOSDs1Threshold15MinPCV": adGenAOSDs1Threshold15MinPCV,
       "adGenAOSDs1Threshold15MinSES": adGenAOSDs1Threshold15MinSES,
       "adGenAOSDs1Threshold15MinSEFS": adGenAOSDs1Threshold15MinSEFS,
       "adGenAOSDs1Threshold15MinUAS": adGenAOSDs1Threshold15MinUAS,
       "adGenAOSDs1Threshold24HrBES": adGenAOSDs1Threshold24HrBES,
       "adGenAOSDs1Threshold24HrCSS": adGenAOSDs1Threshold24HrCSS,
       "adGenAOSDs1Threshold24HrDM": adGenAOSDs1Threshold24HrDM,
       "adGenAOSDs1Threshold24HrES": adGenAOSDs1Threshold24HrES,
       "adGenAOSDs1Threshold24HrLCV": adGenAOSDs1Threshold24HrLCV,
       "adGenAOSDs1Threshold24HrLES": adGenAOSDs1Threshold24HrLES,
       "adGenAOSDs1Threshold24HrPCV": adGenAOSDs1Threshold24HrPCV,
       "adGenAOSDs1Threshold24HrSES": adGenAOSDs1Threshold24HrSES,
       "adGenAOSDs1Threshold24HrSEFS": adGenAOSDs1Threshold24HrSEFS,
       "adGenAOSDs1Threshold24HrUAS": adGenAOSDs1Threshold24HrUAS,
       "adGenAOSDs1ThresholdConformance": adGenAOSDs1ThresholdConformance,
       "adAOSDs1ThresholdCompliances": adAOSDs1ThresholdCompliances,
       "adAOSDs1ThresholdCompliance": adAOSDs1ThresholdCompliance,
       "adAOSDs1ThresholdGroups": adAOSDs1ThresholdGroups,
       "adGenAOSDs1ThresholdGroup": adGenAOSDs1ThresholdGroup,
       "adGenAOSDs1ThresholdsMib": adGenAOSDs1ThresholdsMib}
)
