# SNMP MIB module (CISCO-WAN-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:17 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfIntervalCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfIntervalCount")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWANSonetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3)
)
ciscoWANSonetMIB.setRevisions(
        ("2002-05-20 00:00",
         "2000-03-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWANSonetMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWANSonetMIBObjects = _CiscoWANSonetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1)
)
_CwsSection_ObjectIdentity = ObjectIdentity
cwsSection = _CwsSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1)
)
_CwsSectionAlarmTable_Object = MibTable
cwsSectionAlarmTable = _CwsSectionAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwsSectionAlarmTable.setStatus("current")
_CwsSectionAlarmEntry_Object = MibTableRow
cwsSectionAlarmEntry = _CwsSectionAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1)
)
cwsSectionAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsSectionAlarmEntry.setStatus("current")


class _CwsSectionStatisticalAlarmSeverity_Type(Integer32):
    """Custom type cwsSectionStatisticalAlarmSeverity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1),
          ("none", 3))
    )


_CwsSectionStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_CwsSectionStatisticalAlarmSeverity_Object = MibTableColumn
cwsSectionStatisticalAlarmSeverity = _CwsSectionStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 1),
    _CwsSectionStatisticalAlarmSeverity_Type()
)
cwsSectionStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionStatisticalAlarmSeverity.setStatus("current")


class _CwsSectionCurrentESsThreshold_Type(Unsigned32):
    """Custom type cwsSectionCurrentESsThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionCurrentESsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionCurrentESsThreshold_Object = MibTableColumn
cwsSectionCurrentESsThreshold = _CwsSectionCurrentESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 2),
    _CwsSectionCurrentESsThreshold_Type()
)
cwsSectionCurrentESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionCurrentESsThreshold.setStatus("current")


class _CwsSectionTotalESsThreshold_Type(Unsigned32):
    """Custom type cwsSectionTotalESsThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionTotalESsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionTotalESsThreshold_Object = MibTableColumn
cwsSectionTotalESsThreshold = _CwsSectionTotalESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 3),
    _CwsSectionTotalESsThreshold_Type()
)
cwsSectionTotalESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionTotalESsThreshold.setStatus("current")


class _CwsSectionCurrentSESsThreshold_Type(Unsigned32):
    """Custom type cwsSectionCurrentSESsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionCurrentSESsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionCurrentSESsThreshold_Object = MibTableColumn
cwsSectionCurrentSESsThreshold = _CwsSectionCurrentSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 4),
    _CwsSectionCurrentSESsThreshold_Type()
)
cwsSectionCurrentSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionCurrentSESsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionCurrentSESsThreshold.setUnits("severely errored seconds")


class _CwsSectionTotalSESsThreshold_Type(Unsigned32):
    """Custom type cwsSectionTotalSESsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionTotalSESsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionTotalSESsThreshold_Object = MibTableColumn
cwsSectionTotalSESsThreshold = _CwsSectionTotalSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 5),
    _CwsSectionTotalSESsThreshold_Type()
)
cwsSectionTotalSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionTotalSESsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionTotalSESsThreshold.setUnits("severely errored seconds")


class _CwsSectionCurrentSEFSsThreshold_Type(Unsigned32):
    """Custom type cwsSectionCurrentSEFSsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionCurrentSEFSsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionCurrentSEFSsThreshold_Object = MibTableColumn
cwsSectionCurrentSEFSsThreshold = _CwsSectionCurrentSEFSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 6),
    _CwsSectionCurrentSEFSsThreshold_Type()
)
cwsSectionCurrentSEFSsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionCurrentSEFSsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionCurrentSEFSsThreshold.setUnits("severely errored framing seconds")


class _CwsSectionTotalSEFSsThreshold_Type(Unsigned32):
    """Custom type cwsSectionTotalSEFSsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionTotalSEFSsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionTotalSEFSsThreshold_Object = MibTableColumn
cwsSectionTotalSEFSsThreshold = _CwsSectionTotalSEFSsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 7),
    _CwsSectionTotalSEFSsThreshold_Type()
)
cwsSectionTotalSEFSsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionTotalSEFSsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionTotalSEFSsThreshold.setUnits("severely errored framing seconds")


class _CwsSectionCurrentCVsThreshold_Type(Unsigned32):
    """Custom type cwsSectionCurrentCVsThreshold based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionCurrentCVsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionCurrentCVsThreshold_Object = MibTableColumn
cwsSectionCurrentCVsThreshold = _CwsSectionCurrentCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 8),
    _CwsSectionCurrentCVsThreshold_Type()
)
cwsSectionCurrentCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionCurrentCVsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionCurrentCVsThreshold.setUnits("coding violations")


class _CwsSectionTotalCVsThreshold_Type(Unsigned32):
    """Custom type cwsSectionTotalCVsThreshold based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSectionTotalCVsThreshold_Type.__name__ = "Unsigned32"
_CwsSectionTotalCVsThreshold_Object = MibTableColumn
cwsSectionTotalCVsThreshold = _CwsSectionTotalCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 9),
    _CwsSectionTotalCVsThreshold_Type()
)
cwsSectionTotalCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionTotalCVsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionTotalCVsThreshold.setUnits("coding violations")


class _CwsSectionStatAlarmStatus_Type(Unsigned32):
    """Custom type cwsSectionStatAlarmStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_CwsSectionStatAlarmStatus_Type.__name__ = "Unsigned32"
_CwsSectionStatAlarmStatus_Object = MibTableColumn
cwsSectionStatAlarmStatus = _CwsSectionStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 1, 1, 10),
    _CwsSectionStatAlarmStatus_Type()
)
cwsSectionStatAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsSectionStatAlarmStatus.setStatus("current")
_CwsSectionCurrent24HrTable_Object = MibTable
cwsSectionCurrent24HrTable = _CwsSectionCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrTable.setStatus("current")
_CwsSectionCurrent24HrEntry_Object = MibTableRow
cwsSectionCurrent24HrEntry = _CwsSectionCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1)
)
cwsSectionCurrent24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrEntry.setStatus("current")
_CwsSectionCurrent24HrESs_Type = PerfIntervalCount
_CwsSectionCurrent24HrESs_Object = MibTableColumn
cwsSectionCurrent24HrESs = _CwsSectionCurrent24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 1),
    _CwsSectionCurrent24HrESs_Type()
)
cwsSectionCurrent24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrESs.setStatus("current")
_CwsSectionCurrent24HrSESs_Type = PerfIntervalCount
_CwsSectionCurrent24HrSESs_Object = MibTableColumn
cwsSectionCurrent24HrSESs = _CwsSectionCurrent24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 2),
    _CwsSectionCurrent24HrSESs_Type()
)
cwsSectionCurrent24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrSESs.setUnits("severely errored seconds")
_CwsSectionCurrent24HrSEFSs_Type = PerfIntervalCount
_CwsSectionCurrent24HrSEFSs_Object = MibTableColumn
cwsSectionCurrent24HrSEFSs = _CwsSectionCurrent24HrSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 3),
    _CwsSectionCurrent24HrSEFSs_Type()
)
cwsSectionCurrent24HrSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrSEFSs.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrSEFSs.setUnits("severely errored framing seconds")
_CwsSectionCurrent24HrCVs_Type = PerfIntervalCount
_CwsSectionCurrent24HrCVs_Object = MibTableColumn
cwsSectionCurrent24HrCVs = _CwsSectionCurrent24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 2, 1, 4),
    _CwsSectionCurrent24HrCVs_Type()
)
cwsSectionCurrent24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionCurrent24HrCVs.setUnits("coding violations")
_CwsSectionPrevious24HrTable_Object = MibTable
cwsSectionPrevious24HrTable = _CwsSectionPrevious24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrTable.setStatus("current")
_CwsSectionPrevious24HrEntry_Object = MibTableRow
cwsSectionPrevious24HrEntry = _CwsSectionPrevious24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1)
)
cwsSectionPrevious24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrEntry.setStatus("current")
_CwsSectionPrevious24HrESs_Type = PerfIntervalCount
_CwsSectionPrevious24HrESs_Object = MibTableColumn
cwsSectionPrevious24HrESs = _CwsSectionPrevious24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 1),
    _CwsSectionPrevious24HrESs_Type()
)
cwsSectionPrevious24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrESs.setStatus("current")
_CwsSectionPrevious24HrSESs_Type = PerfIntervalCount
_CwsSectionPrevious24HrSESs_Object = MibTableColumn
cwsSectionPrevious24HrSESs = _CwsSectionPrevious24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 2),
    _CwsSectionPrevious24HrSESs_Type()
)
cwsSectionPrevious24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrSESs.setUnits("severely errored seconds")
_CwsSectionPrevious24HrSEFSs_Type = PerfIntervalCount
_CwsSectionPrevious24HrSEFSs_Object = MibTableColumn
cwsSectionPrevious24HrSEFSs = _CwsSectionPrevious24HrSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 3),
    _CwsSectionPrevious24HrSEFSs_Type()
)
cwsSectionPrevious24HrSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrSEFSs.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrSEFSs.setUnits("severely errored framing seconds")
_CwsSectionPrevious24HrCVs_Type = PerfIntervalCount
_CwsSectionPrevious24HrCVs_Object = MibTableColumn
cwsSectionPrevious24HrCVs = _CwsSectionPrevious24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 1, 3, 1, 4),
    _CwsSectionPrevious24HrCVs_Type()
)
cwsSectionPrevious24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsSectionPrevious24HrCVs.setUnits("coding violations")
_CwsLine_ObjectIdentity = ObjectIdentity
cwsLine = _CwsLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2)
)
_CwsLineAlarmTable_Object = MibTable
cwsLineAlarmTable = _CwsLineAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwsLineAlarmTable.setStatus("current")
_CwsLineAlarmEntry_Object = MibTableRow
cwsLineAlarmEntry = _CwsLineAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1)
)
cwsLineAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsLineAlarmEntry.setStatus("current")


class _CwsLineStatisticalAlarmSeverity_Type(Integer32):
    """Custom type cwsLineStatisticalAlarmSeverity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1),
          ("none", 3))
    )


_CwsLineStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_CwsLineStatisticalAlarmSeverity_Object = MibTableColumn
cwsLineStatisticalAlarmSeverity = _CwsLineStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 1),
    _CwsLineStatisticalAlarmSeverity_Type()
)
cwsLineStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineStatisticalAlarmSeverity.setStatus("current")


class _CwsLineCurrentESsThreshold_Type(Unsigned32):
    """Custom type cwsLineCurrentESsThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineCurrentESsThreshold_Type.__name__ = "Unsigned32"
_CwsLineCurrentESsThreshold_Object = MibTableColumn
cwsLineCurrentESsThreshold = _CwsLineCurrentESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 2),
    _CwsLineCurrentESsThreshold_Type()
)
cwsLineCurrentESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineCurrentESsThreshold.setStatus("current")


class _CwsLineTotalESsThreshold_Type(Unsigned32):
    """Custom type cwsLineTotalESsThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineTotalESsThreshold_Type.__name__ = "Unsigned32"
_CwsLineTotalESsThreshold_Object = MibTableColumn
cwsLineTotalESsThreshold = _CwsLineTotalESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 3),
    _CwsLineTotalESsThreshold_Type()
)
cwsLineTotalESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineTotalESsThreshold.setStatus("current")


class _CwsLineCurrentSESsThreshold_Type(Unsigned32):
    """Custom type cwsLineCurrentSESsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineCurrentSESsThreshold_Type.__name__ = "Unsigned32"
_CwsLineCurrentSESsThreshold_Object = MibTableColumn
cwsLineCurrentSESsThreshold = _CwsLineCurrentSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 4),
    _CwsLineCurrentSESsThreshold_Type()
)
cwsLineCurrentSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineCurrentSESsThreshold.setStatus("current")


class _CwsLineTotalSESsThreshold_Type(Unsigned32):
    """Custom type cwsLineTotalSESsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineTotalSESsThreshold_Type.__name__ = "Unsigned32"
_CwsLineTotalSESsThreshold_Object = MibTableColumn
cwsLineTotalSESsThreshold = _CwsLineTotalSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 5),
    _CwsLineTotalSESsThreshold_Type()
)
cwsLineTotalSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineTotalSESsThreshold.setStatus("current")


class _CwsLineCurrentCVsThreshold_Type(Unsigned32):
    """Custom type cwsLineCurrentCVsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineCurrentCVsThreshold_Type.__name__ = "Unsigned32"
_CwsLineCurrentCVsThreshold_Object = MibTableColumn
cwsLineCurrentCVsThreshold = _CwsLineCurrentCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 6),
    _CwsLineCurrentCVsThreshold_Type()
)
cwsLineCurrentCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineCurrentCVsThreshold.setStatus("current")


class _CwsLineTotalCVsThreshold_Type(Unsigned32):
    """Custom type cwsLineTotalCVsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineTotalCVsThreshold_Type.__name__ = "Unsigned32"
_CwsLineTotalCVsThreshold_Object = MibTableColumn
cwsLineTotalCVsThreshold = _CwsLineTotalCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 7),
    _CwsLineTotalCVsThreshold_Type()
)
cwsLineTotalCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineTotalCVsThreshold.setStatus("current")


class _CwsLineCurrentUASsThreshold_Type(Unsigned32):
    """Custom type cwsLineCurrentUASsThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineCurrentUASsThreshold_Type.__name__ = "Unsigned32"
_CwsLineCurrentUASsThreshold_Object = MibTableColumn
cwsLineCurrentUASsThreshold = _CwsLineCurrentUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 8),
    _CwsLineCurrentUASsThreshold_Type()
)
cwsLineCurrentUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineCurrentUASsThreshold.setStatus("current")


class _CwsLineTotalUASsThreshold_Type(Unsigned32):
    """Custom type cwsLineTotalUASsThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLineTotalUASsThreshold_Type.__name__ = "Unsigned32"
_CwsLineTotalUASsThreshold_Object = MibTableColumn
cwsLineTotalUASsThreshold = _CwsLineTotalUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 9),
    _CwsLineTotalUASsThreshold_Type()
)
cwsLineTotalUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLineTotalUASsThreshold.setStatus("current")
_CwsLineStatAlarmStatus_Type = Unsigned32
_CwsLineStatAlarmStatus_Object = MibTableColumn
cwsLineStatAlarmStatus = _CwsLineStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 1, 1, 10),
    _CwsLineStatAlarmStatus_Type()
)
cwsLineStatAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLineStatAlarmStatus.setStatus("current")
_CwsLineCurrent24HrTable_Object = MibTable
cwsLineCurrent24HrTable = _CwsLineCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwsLineCurrent24HrTable.setStatus("current")
_CwsLineCurrent24HrEntry_Object = MibTableRow
cwsLineCurrent24HrEntry = _CwsLineCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1)
)
cwsLineCurrent24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsLineCurrent24HrEntry.setStatus("current")
_CwsLineCurrent24HrESs_Type = PerfIntervalCount
_CwsLineCurrent24HrESs_Object = MibTableColumn
cwsLineCurrent24HrESs = _CwsLineCurrent24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 1),
    _CwsLineCurrent24HrESs_Type()
)
cwsLineCurrent24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrESs.setStatus("current")
_CwsLineCurrent24HrSESs_Type = PerfIntervalCount
_CwsLineCurrent24HrSESs_Object = MibTableColumn
cwsLineCurrent24HrSESs = _CwsLineCurrent24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 2),
    _CwsLineCurrent24HrSESs_Type()
)
cwsLineCurrent24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrSESs.setUnits("severely errored seconds")
_CwsLineCurrent24HrCVs_Type = PerfIntervalCount
_CwsLineCurrent24HrCVs_Object = MibTableColumn
cwsLineCurrent24HrCVs = _CwsLineCurrent24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 3),
    _CwsLineCurrent24HrCVs_Type()
)
cwsLineCurrent24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrCVs.setUnits("coding violations")
_CwsLineCurrent24HrUASs_Type = PerfIntervalCount
_CwsLineCurrent24HrUASs_Object = MibTableColumn
cwsLineCurrent24HrUASs = _CwsLineCurrent24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 4),
    _CwsLineCurrent24HrUASs_Type()
)
cwsLineCurrent24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsLineCurrent24HrUASs.setUnits("Unavailable seconds")
_CwsFELineCurrent24HrESs_Type = PerfIntervalCount
_CwsFELineCurrent24HrESs_Object = MibTableColumn
cwsFELineCurrent24HrESs = _CwsFELineCurrent24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 5),
    _CwsFELineCurrent24HrESs_Type()
)
cwsFELineCurrent24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrESs.setStatus("current")
_CwsFELineCurrent24HrSESs_Type = PerfIntervalCount
_CwsFELineCurrent24HrSESs_Object = MibTableColumn
cwsFELineCurrent24HrSESs = _CwsFELineCurrent24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 6),
    _CwsFELineCurrent24HrSESs_Type()
)
cwsFELineCurrent24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrSESs.setUnits("severely errored seconds")
_CwsFELineCurrent24HrCVs_Type = PerfIntervalCount
_CwsFELineCurrent24HrCVs_Object = MibTableColumn
cwsFELineCurrent24HrCVs = _CwsFELineCurrent24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 7),
    _CwsFELineCurrent24HrCVs_Type()
)
cwsFELineCurrent24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrCVs.setUnits("coding violations")
_CwsFELineCurrent24HrUASs_Type = PerfIntervalCount
_CwsFELineCurrent24HrUASs_Object = MibTableColumn
cwsFELineCurrent24HrUASs = _CwsFELineCurrent24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 2, 1, 8),
    _CwsFELineCurrent24HrUASs_Type()
)
cwsFELineCurrent24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFELineCurrent24HrUASs.setUnits("Unavailable seconds")
_CwsLinePrevious24HrTable_Object = MibTable
cwsLinePrevious24HrTable = _CwsLinePrevious24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cwsLinePrevious24HrTable.setStatus("current")
_CwsLinePrevious24HrEntry_Object = MibTableRow
cwsLinePrevious24HrEntry = _CwsLinePrevious24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1)
)
cwsLinePrevious24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsLinePrevious24HrEntry.setStatus("current")
_CwsLinePrevious24HrESs_Type = PerfIntervalCount
_CwsLinePrevious24HrESs_Object = MibTableColumn
cwsLinePrevious24HrESs = _CwsLinePrevious24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 1),
    _CwsLinePrevious24HrESs_Type()
)
cwsLinePrevious24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrESs.setStatus("current")
_CwsLinePrevious24HrSESs_Type = PerfIntervalCount
_CwsLinePrevious24HrSESs_Object = MibTableColumn
cwsLinePrevious24HrSESs = _CwsLinePrevious24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 2),
    _CwsLinePrevious24HrSESs_Type()
)
cwsLinePrevious24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrSESs.setUnits("severely errored seconds")
_CwsLinePrevious24HrCVs_Type = PerfIntervalCount
_CwsLinePrevious24HrCVs_Object = MibTableColumn
cwsLinePrevious24HrCVs = _CwsLinePrevious24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 3),
    _CwsLinePrevious24HrCVs_Type()
)
cwsLinePrevious24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrCVs.setUnits("coding violations")
_CwsLinePrevious24HrUASs_Type = PerfIntervalCount
_CwsLinePrevious24HrUASs_Object = MibTableColumn
cwsLinePrevious24HrUASs = _CwsLinePrevious24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 4),
    _CwsLinePrevious24HrUASs_Type()
)
cwsLinePrevious24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsLinePrevious24HrUASs.setUnits("Unavailable seconds")
_CwsFELinePrevious24HrESs_Type = PerfIntervalCount
_CwsFELinePrevious24HrESs_Object = MibTableColumn
cwsFELinePrevious24HrESs = _CwsFELinePrevious24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 5),
    _CwsFELinePrevious24HrESs_Type()
)
cwsFELinePrevious24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrESs.setStatus("current")
_CwsFELinePrevious24HrSESs_Type = PerfIntervalCount
_CwsFELinePrevious24HrSESs_Object = MibTableColumn
cwsFELinePrevious24HrSESs = _CwsFELinePrevious24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 6),
    _CwsFELinePrevious24HrSESs_Type()
)
cwsFELinePrevious24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrSESs.setUnits("severely errored seconds")
_CwsFELinePrevious24HrCVs_Type = PerfIntervalCount
_CwsFELinePrevious24HrCVs_Object = MibTableColumn
cwsFELinePrevious24HrCVs = _CwsFELinePrevious24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 7),
    _CwsFELinePrevious24HrCVs_Type()
)
cwsFELinePrevious24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrCVs.setUnits("coding violations")
_CwsFELinePrevious24HrUASs_Type = PerfIntervalCount
_CwsFELinePrevious24HrUASs_Object = MibTableColumn
cwsFELinePrevious24HrUASs = _CwsFELinePrevious24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 2, 3, 1, 8),
    _CwsFELinePrevious24HrUASs_Type()
)
cwsFELinePrevious24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFELinePrevious24HrUASs.setUnits("Unavailable seconds")
_CwsPath_ObjectIdentity = ObjectIdentity
cwsPath = _CwsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3)
)
_CwsPathAlarmTable_Object = MibTable
cwsPathAlarmTable = _CwsPathAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwsPathAlarmTable.setStatus("current")
_CwsPathAlarmEntry_Object = MibTableRow
cwsPathAlarmEntry = _CwsPathAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1)
)
cwsPathAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsPathAlarmEntry.setStatus("current")


class _CwsPathStatisticalAlarmSeverity_Type(Integer32):
    """Custom type cwsPathStatisticalAlarmSeverity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1),
          ("none", 3))
    )


_CwsPathStatisticalAlarmSeverity_Type.__name__ = "Integer32"
_CwsPathStatisticalAlarmSeverity_Object = MibTableColumn
cwsPathStatisticalAlarmSeverity = _CwsPathStatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 1),
    _CwsPathStatisticalAlarmSeverity_Type()
)
cwsPathStatisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathStatisticalAlarmSeverity.setStatus("current")


class _CwsPathCurrentESsThreshold_Type(Unsigned32):
    """Custom type cwsPathCurrentESsThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathCurrentESsThreshold_Type.__name__ = "Unsigned32"
_CwsPathCurrentESsThreshold_Object = MibTableColumn
cwsPathCurrentESsThreshold = _CwsPathCurrentESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 2),
    _CwsPathCurrentESsThreshold_Type()
)
cwsPathCurrentESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathCurrentESsThreshold.setStatus("current")


class _CwsPathTotalESsThreshold_Type(Unsigned32):
    """Custom type cwsPathTotalESsThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathTotalESsThreshold_Type.__name__ = "Unsigned32"
_CwsPathTotalESsThreshold_Object = MibTableColumn
cwsPathTotalESsThreshold = _CwsPathTotalESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 3),
    _CwsPathTotalESsThreshold_Type()
)
cwsPathTotalESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathTotalESsThreshold.setStatus("current")


class _CwsPathCurrentSESsThreshold_Type(Unsigned32):
    """Custom type cwsPathCurrentSESsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathCurrentSESsThreshold_Type.__name__ = "Unsigned32"
_CwsPathCurrentSESsThreshold_Object = MibTableColumn
cwsPathCurrentSESsThreshold = _CwsPathCurrentSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 4),
    _CwsPathCurrentSESsThreshold_Type()
)
cwsPathCurrentSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathCurrentSESsThreshold.setStatus("current")


class _CwsPathTotalSESsThreshold_Type(Unsigned32):
    """Custom type cwsPathTotalSESsThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathTotalSESsThreshold_Type.__name__ = "Unsigned32"
_CwsPathTotalSESsThreshold_Object = MibTableColumn
cwsPathTotalSESsThreshold = _CwsPathTotalSESsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 5),
    _CwsPathTotalSESsThreshold_Type()
)
cwsPathTotalSESsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathTotalSESsThreshold.setStatus("current")


class _CwsPathCurrentCVsThreshold_Type(Unsigned32):
    """Custom type cwsPathCurrentCVsThreshold based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathCurrentCVsThreshold_Type.__name__ = "Unsigned32"
_CwsPathCurrentCVsThreshold_Object = MibTableColumn
cwsPathCurrentCVsThreshold = _CwsPathCurrentCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 6),
    _CwsPathCurrentCVsThreshold_Type()
)
cwsPathCurrentCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathCurrentCVsThreshold.setStatus("current")


class _CwsPathTotalCVsThreshold_Type(Unsigned32):
    """Custom type cwsPathTotalCVsThreshold based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathTotalCVsThreshold_Type.__name__ = "Unsigned32"
_CwsPathTotalCVsThreshold_Object = MibTableColumn
cwsPathTotalCVsThreshold = _CwsPathTotalCVsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 7),
    _CwsPathTotalCVsThreshold_Type()
)
cwsPathTotalCVsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathTotalCVsThreshold.setStatus("current")


class _CwsPathCurrentUASsThreshold_Type(Unsigned32):
    """Custom type cwsPathCurrentUASsThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathCurrentUASsThreshold_Type.__name__ = "Unsigned32"
_CwsPathCurrentUASsThreshold_Object = MibTableColumn
cwsPathCurrentUASsThreshold = _CwsPathCurrentUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 8),
    _CwsPathCurrentUASsThreshold_Type()
)
cwsPathCurrentUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathCurrentUASsThreshold.setStatus("current")


class _CwsPathTotalUASsThreshold_Type(Unsigned32):
    """Custom type cwsPathTotalUASsThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsPathTotalUASsThreshold_Type.__name__ = "Unsigned32"
_CwsPathTotalUASsThreshold_Object = MibTableColumn
cwsPathTotalUASsThreshold = _CwsPathTotalUASsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 9),
    _CwsPathTotalUASsThreshold_Type()
)
cwsPathTotalUASsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsPathTotalUASsThreshold.setStatus("current")
_CwsPathStatAlarmStatus_Type = Unsigned32
_CwsPathStatAlarmStatus_Object = MibTableColumn
cwsPathStatAlarmStatus = _CwsPathStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 1, 1, 10),
    _CwsPathStatAlarmStatus_Type()
)
cwsPathStatAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathStatAlarmStatus.setStatus("current")
_CwsPathCurrent24HrTable_Object = MibTable
cwsPathCurrent24HrTable = _CwsPathCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cwsPathCurrent24HrTable.setStatus("current")
_CwsPathCurrent24HrEntry_Object = MibTableRow
cwsPathCurrent24HrEntry = _CwsPathCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1)
)
cwsPathCurrent24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsPathCurrent24HrEntry.setStatus("current")
_CwsPathCurrent24HrESs_Type = PerfIntervalCount
_CwsPathCurrent24HrESs_Object = MibTableColumn
cwsPathCurrent24HrESs = _CwsPathCurrent24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 1),
    _CwsPathCurrent24HrESs_Type()
)
cwsPathCurrent24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrESs.setStatus("current")
_CwsPathCurrent24HrSESs_Type = PerfIntervalCount
_CwsPathCurrent24HrSESs_Object = MibTableColumn
cwsPathCurrent24HrSESs = _CwsPathCurrent24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 2),
    _CwsPathCurrent24HrSESs_Type()
)
cwsPathCurrent24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrSESs.setUnits("severely errored seconds")
_CwsPathCurrent24HrCVs_Type = PerfIntervalCount
_CwsPathCurrent24HrCVs_Object = MibTableColumn
cwsPathCurrent24HrCVs = _CwsPathCurrent24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 3),
    _CwsPathCurrent24HrCVs_Type()
)
cwsPathCurrent24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrCVs.setUnits("coding violations")
_CwsPathCurrent24HrUASs_Type = PerfIntervalCount
_CwsPathCurrent24HrUASs_Object = MibTableColumn
cwsPathCurrent24HrUASs = _CwsPathCurrent24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 4),
    _CwsPathCurrent24HrUASs_Type()
)
cwsPathCurrent24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsPathCurrent24HrUASs.setUnits("Unavailable seconds")
_CwsFEPathCurrent24HrESs_Type = PerfIntervalCount
_CwsFEPathCurrent24HrESs_Object = MibTableColumn
cwsFEPathCurrent24HrESs = _CwsFEPathCurrent24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 5),
    _CwsFEPathCurrent24HrESs_Type()
)
cwsFEPathCurrent24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrESs.setStatus("current")
_CwsFEPathCurrent24HrSESs_Type = PerfIntervalCount
_CwsFEPathCurrent24HrSESs_Object = MibTableColumn
cwsFEPathCurrent24HrSESs = _CwsFEPathCurrent24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 6),
    _CwsFEPathCurrent24HrSESs_Type()
)
cwsFEPathCurrent24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrSESs.setUnits("severely errored seconds")
_CwsFEPathCurrent24HrCVs_Type = PerfIntervalCount
_CwsFEPathCurrent24HrCVs_Object = MibTableColumn
cwsFEPathCurrent24HrCVs = _CwsFEPathCurrent24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 7),
    _CwsFEPathCurrent24HrCVs_Type()
)
cwsFEPathCurrent24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrCVs.setUnits("coding violations")
_CwsFEPathCurrent24HrUASs_Type = PerfIntervalCount
_CwsFEPathCurrent24HrUASs_Object = MibTableColumn
cwsFEPathCurrent24HrUASs = _CwsFEPathCurrent24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 2, 1, 8),
    _CwsFEPathCurrent24HrUASs_Type()
)
cwsFEPathCurrent24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFEPathCurrent24HrUASs.setUnits("Unavailable seconds")
_CwsPathPrevious24HrTable_Object = MibTable
cwsPathPrevious24HrTable = _CwsPathPrevious24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cwsPathPrevious24HrTable.setStatus("current")
_CwsPathPrevious24HrEntry_Object = MibTableRow
cwsPathPrevious24HrEntry = _CwsPathPrevious24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1)
)
cwsPathPrevious24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwsPathPrevious24HrEntry.setStatus("current")
_CwsPathPrevious24HrESs_Type = PerfIntervalCount
_CwsPathPrevious24HrESs_Object = MibTableColumn
cwsPathPrevious24HrESs = _CwsPathPrevious24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 1),
    _CwsPathPrevious24HrESs_Type()
)
cwsPathPrevious24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrESs.setStatus("current")
_CwsPathPrevious24HrSESs_Type = PerfIntervalCount
_CwsPathPrevious24HrSESs_Object = MibTableColumn
cwsPathPrevious24HrSESs = _CwsPathPrevious24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 2),
    _CwsPathPrevious24HrSESs_Type()
)
cwsPathPrevious24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrSESs.setUnits("severely errored seconds")
_CwsPathPrevious24HrCVs_Type = PerfIntervalCount
_CwsPathPrevious24HrCVs_Object = MibTableColumn
cwsPathPrevious24HrCVs = _CwsPathPrevious24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 3),
    _CwsPathPrevious24HrCVs_Type()
)
cwsPathPrevious24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrCVs.setUnits("coding violations")
_CwsPathPrevious24HrUASs_Type = PerfIntervalCount
_CwsPathPrevious24HrUASs_Object = MibTableColumn
cwsPathPrevious24HrUASs = _CwsPathPrevious24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 4),
    _CwsPathPrevious24HrUASs_Type()
)
cwsPathPrevious24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsPathPrevious24HrUASs.setUnits("Unavailable seconds")
_CwsFEPathPrevious24HrESs_Type = PerfIntervalCount
_CwsFEPathPrevious24HrESs_Object = MibTableColumn
cwsFEPathPrevious24HrESs = _CwsFEPathPrevious24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 5),
    _CwsFEPathPrevious24HrESs_Type()
)
cwsFEPathPrevious24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrESs.setStatus("current")
_CwsFEPathPrevious24HrSESs_Type = PerfIntervalCount
_CwsFEPathPrevious24HrSESs_Object = MibTableColumn
cwsFEPathPrevious24HrSESs = _CwsFEPathPrevious24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 6),
    _CwsFEPathPrevious24HrSESs_Type()
)
cwsFEPathPrevious24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrSESs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrSESs.setUnits("severely errored seconds")
_CwsFEPathPrevious24HrCVs_Type = PerfIntervalCount
_CwsFEPathPrevious24HrCVs_Object = MibTableColumn
cwsFEPathPrevious24HrCVs = _CwsFEPathPrevious24HrCVs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 7),
    _CwsFEPathPrevious24HrCVs_Type()
)
cwsFEPathPrevious24HrCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrCVs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrCVs.setUnits("coding violations")
_CwsFEPathPrevious24HrUASs_Type = PerfIntervalCount
_CwsFEPathPrevious24HrUASs_Object = MibTableColumn
cwsFEPathPrevious24HrUASs = _CwsFEPathPrevious24HrUASs_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 1, 3, 3, 1, 8),
    _CwsFEPathPrevious24HrUASs_Type()
)
cwsFEPathPrevious24HrUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrUASs.setStatus("current")
if mibBuilder.loadTexts:
    cwsFEPathPrevious24HrUASs.setUnits("Unavailable seconds")
_CiscoWANSonetMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWANSonetMIBConformance = _CiscoWANSonetMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2)
)
_CiscoWANSonetMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWANSonetMIBCompliances = _CiscoWANSonetMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 1)
)
_CiscoWANSonetMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWANSonetMIBGroups = _CiscoWANSonetMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2)
)

# Managed Objects groups

ciscoWANSonetSectAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 1)
)
ciscoWANSonetSectAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsSectionStatisticalAlarmSeverity"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionTotalESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentSESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionTotalSESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentSEFSsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionTotalSEFSsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrentCVsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionTotalCVsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionStatAlarmStatus"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrSEFSs"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionCurrent24HrCVs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetSectAlarmMIBGroup.setStatus("current")

ciscoWANSonetSectPrev24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 2)
)
ciscoWANSonetSectPrev24HrMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrSEFSs"),
        ("CISCO-WAN-SONET-MIB", "cwsSectionPrevious24HrCVs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetSectPrev24HrMIBGroup.setStatus("current")

ciscoWANSonetLineAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 3)
)
ciscoWANSonetLineAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsLineStatisticalAlarmSeverity"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrentESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineTotalESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrentSESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineTotalSESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrentCVsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineTotalCVsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrentUASsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineTotalUASsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsLineStatAlarmStatus"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsLineCurrent24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetLineAlarmMIBGroup.setStatus("current")

ciscoWANSonetFELineAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 4)
)
ciscoWANSonetFELineAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsFELineCurrent24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetFELineAlarmMIBGroup.setStatus("current")

ciscoWANSonetLinePrev24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 5)
)
ciscoWANSonetLinePrev24HrMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsLinePrevious24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetLinePrev24HrMIBGroup.setStatus("current")

ciscoWANSonetFELinePrev24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 6)
)
ciscoWANSonetFELinePrev24HrMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsFELinePrevious24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetFELinePrev24HrMIBGroup.setStatus("current")

ciscoWANSonetPathAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 7)
)
ciscoWANSonetPathAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsPathStatisticalAlarmSeverity"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrentESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathTotalESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrentSESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathTotalSESsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrentCVsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathTotalCVsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrentUASsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathTotalUASsThreshold"),
        ("CISCO-WAN-SONET-MIB", "cwsPathStatAlarmStatus"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsPathCurrent24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetPathAlarmMIBGroup.setStatus("current")

ciscoWANSonetFEPathAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 8)
)
ciscoWANSonetFEPathAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsFEPathCurrent24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetFEPathAlarmMIBGroup.setStatus("current")

ciscoWANSonetPathPrev24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 9)
)
ciscoWANSonetPathPrev24HrMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsPathPrevious24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetPathPrev24HrMIBGroup.setStatus("current")

ciscoWANSonetFEPathPrev24HrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 2, 10)
)
ciscoWANSonetFEPathPrev24HrMIBGroup.setObjects(
      *(("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrSESs"),
        ("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrCVs"),
        ("CISCO-WAN-SONET-MIB", "cwsFEPathPrevious24HrUASs"))
)
if mibBuilder.loadTexts:
    ciscoWANSonetFEPathPrev24HrMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWANSonetMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWANSonetMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-SONET-MIB",
    **{"ciscoWANSonetMIB": ciscoWANSonetMIB,
       "ciscoWANSonetMIBObjects": ciscoWANSonetMIBObjects,
       "cwsSection": cwsSection,
       "cwsSectionAlarmTable": cwsSectionAlarmTable,
       "cwsSectionAlarmEntry": cwsSectionAlarmEntry,
       "cwsSectionStatisticalAlarmSeverity": cwsSectionStatisticalAlarmSeverity,
       "cwsSectionCurrentESsThreshold": cwsSectionCurrentESsThreshold,
       "cwsSectionTotalESsThreshold": cwsSectionTotalESsThreshold,
       "cwsSectionCurrentSESsThreshold": cwsSectionCurrentSESsThreshold,
       "cwsSectionTotalSESsThreshold": cwsSectionTotalSESsThreshold,
       "cwsSectionCurrentSEFSsThreshold": cwsSectionCurrentSEFSsThreshold,
       "cwsSectionTotalSEFSsThreshold": cwsSectionTotalSEFSsThreshold,
       "cwsSectionCurrentCVsThreshold": cwsSectionCurrentCVsThreshold,
       "cwsSectionTotalCVsThreshold": cwsSectionTotalCVsThreshold,
       "cwsSectionStatAlarmStatus": cwsSectionStatAlarmStatus,
       "cwsSectionCurrent24HrTable": cwsSectionCurrent24HrTable,
       "cwsSectionCurrent24HrEntry": cwsSectionCurrent24HrEntry,
       "cwsSectionCurrent24HrESs": cwsSectionCurrent24HrESs,
       "cwsSectionCurrent24HrSESs": cwsSectionCurrent24HrSESs,
       "cwsSectionCurrent24HrSEFSs": cwsSectionCurrent24HrSEFSs,
       "cwsSectionCurrent24HrCVs": cwsSectionCurrent24HrCVs,
       "cwsSectionPrevious24HrTable": cwsSectionPrevious24HrTable,
       "cwsSectionPrevious24HrEntry": cwsSectionPrevious24HrEntry,
       "cwsSectionPrevious24HrESs": cwsSectionPrevious24HrESs,
       "cwsSectionPrevious24HrSESs": cwsSectionPrevious24HrSESs,
       "cwsSectionPrevious24HrSEFSs": cwsSectionPrevious24HrSEFSs,
       "cwsSectionPrevious24HrCVs": cwsSectionPrevious24HrCVs,
       "cwsLine": cwsLine,
       "cwsLineAlarmTable": cwsLineAlarmTable,
       "cwsLineAlarmEntry": cwsLineAlarmEntry,
       "cwsLineStatisticalAlarmSeverity": cwsLineStatisticalAlarmSeverity,
       "cwsLineCurrentESsThreshold": cwsLineCurrentESsThreshold,
       "cwsLineTotalESsThreshold": cwsLineTotalESsThreshold,
       "cwsLineCurrentSESsThreshold": cwsLineCurrentSESsThreshold,
       "cwsLineTotalSESsThreshold": cwsLineTotalSESsThreshold,
       "cwsLineCurrentCVsThreshold": cwsLineCurrentCVsThreshold,
       "cwsLineTotalCVsThreshold": cwsLineTotalCVsThreshold,
       "cwsLineCurrentUASsThreshold": cwsLineCurrentUASsThreshold,
       "cwsLineTotalUASsThreshold": cwsLineTotalUASsThreshold,
       "cwsLineStatAlarmStatus": cwsLineStatAlarmStatus,
       "cwsLineCurrent24HrTable": cwsLineCurrent24HrTable,
       "cwsLineCurrent24HrEntry": cwsLineCurrent24HrEntry,
       "cwsLineCurrent24HrESs": cwsLineCurrent24HrESs,
       "cwsLineCurrent24HrSESs": cwsLineCurrent24HrSESs,
       "cwsLineCurrent24HrCVs": cwsLineCurrent24HrCVs,
       "cwsLineCurrent24HrUASs": cwsLineCurrent24HrUASs,
       "cwsFELineCurrent24HrESs": cwsFELineCurrent24HrESs,
       "cwsFELineCurrent24HrSESs": cwsFELineCurrent24HrSESs,
       "cwsFELineCurrent24HrCVs": cwsFELineCurrent24HrCVs,
       "cwsFELineCurrent24HrUASs": cwsFELineCurrent24HrUASs,
       "cwsLinePrevious24HrTable": cwsLinePrevious24HrTable,
       "cwsLinePrevious24HrEntry": cwsLinePrevious24HrEntry,
       "cwsLinePrevious24HrESs": cwsLinePrevious24HrESs,
       "cwsLinePrevious24HrSESs": cwsLinePrevious24HrSESs,
       "cwsLinePrevious24HrCVs": cwsLinePrevious24HrCVs,
       "cwsLinePrevious24HrUASs": cwsLinePrevious24HrUASs,
       "cwsFELinePrevious24HrESs": cwsFELinePrevious24HrESs,
       "cwsFELinePrevious24HrSESs": cwsFELinePrevious24HrSESs,
       "cwsFELinePrevious24HrCVs": cwsFELinePrevious24HrCVs,
       "cwsFELinePrevious24HrUASs": cwsFELinePrevious24HrUASs,
       "cwsPath": cwsPath,
       "cwsPathAlarmTable": cwsPathAlarmTable,
       "cwsPathAlarmEntry": cwsPathAlarmEntry,
       "cwsPathStatisticalAlarmSeverity": cwsPathStatisticalAlarmSeverity,
       "cwsPathCurrentESsThreshold": cwsPathCurrentESsThreshold,
       "cwsPathTotalESsThreshold": cwsPathTotalESsThreshold,
       "cwsPathCurrentSESsThreshold": cwsPathCurrentSESsThreshold,
       "cwsPathTotalSESsThreshold": cwsPathTotalSESsThreshold,
       "cwsPathCurrentCVsThreshold": cwsPathCurrentCVsThreshold,
       "cwsPathTotalCVsThreshold": cwsPathTotalCVsThreshold,
       "cwsPathCurrentUASsThreshold": cwsPathCurrentUASsThreshold,
       "cwsPathTotalUASsThreshold": cwsPathTotalUASsThreshold,
       "cwsPathStatAlarmStatus": cwsPathStatAlarmStatus,
       "cwsPathCurrent24HrTable": cwsPathCurrent24HrTable,
       "cwsPathCurrent24HrEntry": cwsPathCurrent24HrEntry,
       "cwsPathCurrent24HrESs": cwsPathCurrent24HrESs,
       "cwsPathCurrent24HrSESs": cwsPathCurrent24HrSESs,
       "cwsPathCurrent24HrCVs": cwsPathCurrent24HrCVs,
       "cwsPathCurrent24HrUASs": cwsPathCurrent24HrUASs,
       "cwsFEPathCurrent24HrESs": cwsFEPathCurrent24HrESs,
       "cwsFEPathCurrent24HrSESs": cwsFEPathCurrent24HrSESs,
       "cwsFEPathCurrent24HrCVs": cwsFEPathCurrent24HrCVs,
       "cwsFEPathCurrent24HrUASs": cwsFEPathCurrent24HrUASs,
       "cwsPathPrevious24HrTable": cwsPathPrevious24HrTable,
       "cwsPathPrevious24HrEntry": cwsPathPrevious24HrEntry,
       "cwsPathPrevious24HrESs": cwsPathPrevious24HrESs,
       "cwsPathPrevious24HrSESs": cwsPathPrevious24HrSESs,
       "cwsPathPrevious24HrCVs": cwsPathPrevious24HrCVs,
       "cwsPathPrevious24HrUASs": cwsPathPrevious24HrUASs,
       "cwsFEPathPrevious24HrESs": cwsFEPathPrevious24HrESs,
       "cwsFEPathPrevious24HrSESs": cwsFEPathPrevious24HrSESs,
       "cwsFEPathPrevious24HrCVs": cwsFEPathPrevious24HrCVs,
       "cwsFEPathPrevious24HrUASs": cwsFEPathPrevious24HrUASs,
       "ciscoWANSonetMIBConformance": ciscoWANSonetMIBConformance,
       "ciscoWANSonetMIBCompliances": ciscoWANSonetMIBCompliances,
       "ciscoWANSonetMIBCompliance": ciscoWANSonetMIBCompliance,
       "ciscoWANSonetMIBGroups": ciscoWANSonetMIBGroups,
       "ciscoWANSonetSectAlarmMIBGroup": ciscoWANSonetSectAlarmMIBGroup,
       "ciscoWANSonetSectPrev24HrMIBGroup": ciscoWANSonetSectPrev24HrMIBGroup,
       "ciscoWANSonetLineAlarmMIBGroup": ciscoWANSonetLineAlarmMIBGroup,
       "ciscoWANSonetFELineAlarmMIBGroup": ciscoWANSonetFELineAlarmMIBGroup,
       "ciscoWANSonetLinePrev24HrMIBGroup": ciscoWANSonetLinePrev24HrMIBGroup,
       "ciscoWANSonetFELinePrev24HrMIBGroup": ciscoWANSonetFELinePrev24HrMIBGroup,
       "ciscoWANSonetPathAlarmMIBGroup": ciscoWANSonetPathAlarmMIBGroup,
       "ciscoWANSonetFEPathAlarmMIBGroup": ciscoWANSonetFEPathAlarmMIBGroup,
       "ciscoWANSonetPathPrev24HrMIBGroup": ciscoWANSonetPathPrev24HrMIBGroup,
       "ciscoWANSonetFEPathPrev24HrMIBGroup": ciscoWANSonetFEPathPrev24HrMIBGroup}
)
