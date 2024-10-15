# SNMP MIB module (TERADICI-PCOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERADICI-PCOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:09 2024
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

teraMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25071)
)
teraMibModule.setRevisions(
        ("2008-01-28 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeraProducts_ObjectIdentity = ObjectIdentity
teraProducts = _TeraProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1)
)
_TeraPcoip_ObjectIdentity = ObjectIdentity
teraPcoip = _TeraPcoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1)
)
_TeraPcoipStatistics_ObjectIdentity = ObjectIdentity
teraPcoipStatistics = _TeraPcoipStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1)
)
_PcoipStatisticsTable_Object = MibTable
pcoipStatisticsTable = _PcoipStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pcoipStatisticsTable.setStatus("current")
_PcoipStatisticsEntry_Object = MibTableRow
pcoipStatisticsEntry = _PcoipStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1)
)
pcoipStatisticsEntry.setIndexNames(
    (0, "TERADICI-PCOIP-MIB", "pcoipStatisticsIndex"),
)
if mibBuilder.loadTexts:
    pcoipStatisticsEntry.setStatus("current")


class _PcoipStatisticsIndex_Type(Integer32):
    """Custom type pcoipStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipStatisticsIndex_Type.__name__ = "Integer32"
_PcoipStatisticsIndex_Object = MibTableColumn
pcoipStatisticsIndex = _PcoipStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 1),
    _PcoipStatisticsIndex_Type()
)
pcoipStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsIndex.setStatus("current")


class _PcoipStatisticsSessionNumber_Type(Integer32):
    """Custom type pcoipStatisticsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipStatisticsSessionNumber_Type.__name__ = "Integer32"
_PcoipStatisticsSessionNumber_Object = MibTableColumn
pcoipStatisticsSessionNumber = _PcoipStatisticsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 2),
    _PcoipStatisticsSessionNumber_Type()
)
pcoipStatisticsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsSessionNumber.setStatus("current")
_PcoipStatisticsPcoipPacketsTransmitted_Type = Counter64
_PcoipStatisticsPcoipPacketsTransmitted_Object = MibTableColumn
pcoipStatisticsPcoipPacketsTransmitted = _PcoipStatisticsPcoipPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 3),
    _PcoipStatisticsPcoipPacketsTransmitted_Type()
)
pcoipStatisticsPcoipPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsPcoipPacketsTransmitted.setStatus("current")
_PcoipStatisticsPcoipBytesTransmitted_Type = Counter64
_PcoipStatisticsPcoipBytesTransmitted_Object = MibTableColumn
pcoipStatisticsPcoipBytesTransmitted = _PcoipStatisticsPcoipBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 4),
    _PcoipStatisticsPcoipBytesTransmitted_Type()
)
pcoipStatisticsPcoipBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsPcoipBytesTransmitted.setStatus("current")
_PcoipStatisticsPcoipPacketsReceived_Type = Counter64
_PcoipStatisticsPcoipPacketsReceived_Object = MibTableColumn
pcoipStatisticsPcoipPacketsReceived = _PcoipStatisticsPcoipPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 5),
    _PcoipStatisticsPcoipPacketsReceived_Type()
)
pcoipStatisticsPcoipPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsPcoipPacketsReceived.setStatus("current")
_PcoipStatisticsPcoipBytesReceived_Type = Counter64
_PcoipStatisticsPcoipBytesReceived_Object = MibTableColumn
pcoipStatisticsPcoipBytesReceived = _PcoipStatisticsPcoipBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 6),
    _PcoipStatisticsPcoipBytesReceived_Type()
)
pcoipStatisticsPcoipBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsPcoipBytesReceived.setStatus("current")
_PcoipStatisticsPcoipLostPackets_Type = Counter64
_PcoipStatisticsPcoipLostPackets_Object = MibTableColumn
pcoipStatisticsPcoipLostPackets = _PcoipStatisticsPcoipLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 7),
    _PcoipStatisticsPcoipLostPackets_Type()
)
pcoipStatisticsPcoipLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsPcoipLostPackets.setStatus("current")


class _PcoipStatisticsPcoipLatency_Type(Integer32):
    """Custom type pcoipStatisticsPcoipLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PcoipStatisticsPcoipLatency_Type.__name__ = "Integer32"
_PcoipStatisticsPcoipLatency_Object = MibTableColumn
pcoipStatisticsPcoipLatency = _PcoipStatisticsPcoipLatency_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 1, 1, 1, 8),
    _PcoipStatisticsPcoipLatency_Type()
)
pcoipStatisticsPcoipLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipStatisticsPcoipLatency.setStatus("current")
_TeraImagingStatistics_ObjectIdentity = ObjectIdentity
teraImagingStatistics = _TeraImagingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2)
)
_ImagingStatisticsTable_Object = MibTable
imagingStatisticsTable = _ImagingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    imagingStatisticsTable.setStatus("current")
_ImagingStatisticsEntry_Object = MibTableRow
imagingStatisticsEntry = _ImagingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1)
)
imagingStatisticsEntry.setIndexNames(
    (0, "TERADICI-PCOIP-MIB", "imagingStatisticsIndex"),
)
if mibBuilder.loadTexts:
    imagingStatisticsEntry.setStatus("current")


class _ImagingStatisticsIndex_Type(Integer32):
    """Custom type imagingStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ImagingStatisticsIndex_Type.__name__ = "Integer32"
_ImagingStatisticsIndex_Object = MibTableColumn
imagingStatisticsIndex = _ImagingStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 1),
    _ImagingStatisticsIndex_Type()
)
imagingStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsIndex.setStatus("current")


class _ImagingStatisticsSessionNumber_Type(Integer32):
    """Custom type imagingStatisticsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ImagingStatisticsSessionNumber_Type.__name__ = "Integer32"
_ImagingStatisticsSessionNumber_Object = MibTableColumn
imagingStatisticsSessionNumber = _ImagingStatisticsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 2),
    _ImagingStatisticsSessionNumber_Type()
)
imagingStatisticsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsSessionNumber.setStatus("current")


class _ImagingStatisticsSessionActive_Type(Integer32):
    """Custom type imagingStatisticsSessionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 0))
    )


_ImagingStatisticsSessionActive_Type.__name__ = "Integer32"
_ImagingStatisticsSessionActive_Object = MibTableColumn
imagingStatisticsSessionActive = _ImagingStatisticsSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 3),
    _ImagingStatisticsSessionActive_Type()
)
imagingStatisticsSessionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsSessionActive.setStatus("current")


class _ImagingStatisticsDisplayActive_Type(Integer32):
    """Custom type imagingStatisticsDisplayActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 0))
    )


_ImagingStatisticsDisplayActive_Type.__name__ = "Integer32"
_ImagingStatisticsDisplayActive_Object = MibTableColumn
imagingStatisticsDisplayActive = _ImagingStatisticsDisplayActive_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 4),
    _ImagingStatisticsDisplayActive_Type()
)
imagingStatisticsDisplayActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsDisplayActive.setStatus("current")


class _ImagingStatisticsDisplayWidth_Type(Integer32):
    """Custom type imagingStatisticsDisplayWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1600),
    )


_ImagingStatisticsDisplayWidth_Type.__name__ = "Integer32"
_ImagingStatisticsDisplayWidth_Object = MibTableColumn
imagingStatisticsDisplayWidth = _ImagingStatisticsDisplayWidth_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 5),
    _ImagingStatisticsDisplayWidth_Type()
)
imagingStatisticsDisplayWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsDisplayWidth.setStatus("current")


class _ImagingStatisticsDisplayHeight_Type(Integer32):
    """Custom type imagingStatisticsDisplayHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1600),
    )


_ImagingStatisticsDisplayHeight_Type.__name__ = "Integer32"
_ImagingStatisticsDisplayHeight_Object = MibTableColumn
imagingStatisticsDisplayHeight = _ImagingStatisticsDisplayHeight_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 6),
    _ImagingStatisticsDisplayHeight_Type()
)
imagingStatisticsDisplayHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsDisplayHeight.setStatus("current")


class _ImagingStatisticsDisplayRefreshRate_Type(Integer32):
    """Custom type imagingStatisticsDisplayRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ImagingStatisticsDisplayRefreshRate_Type.__name__ = "Integer32"
_ImagingStatisticsDisplayRefreshRate_Object = MibTableColumn
imagingStatisticsDisplayRefreshRate = _ImagingStatisticsDisplayRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 7),
    _ImagingStatisticsDisplayRefreshRate_Type()
)
imagingStatisticsDisplayRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsDisplayRefreshRate.setStatus("current")
_ImagingStatisticsFrameCount_Type = Counter64
_ImagingStatisticsFrameCount_Object = MibTableColumn
imagingStatisticsFrameCount = _ImagingStatisticsFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 1, 2, 1, 1, 8),
    _ImagingStatisticsFrameCount_Type()
)
imagingStatisticsFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagingStatisticsFrameCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERADICI-PCOIP-MIB",
    **{"teraMibModule": teraMibModule,
       "teraProducts": teraProducts,
       "teraPcoip": teraPcoip,
       "teraPcoipStatistics": teraPcoipStatistics,
       "pcoipStatisticsTable": pcoipStatisticsTable,
       "pcoipStatisticsEntry": pcoipStatisticsEntry,
       "pcoipStatisticsIndex": pcoipStatisticsIndex,
       "pcoipStatisticsSessionNumber": pcoipStatisticsSessionNumber,
       "pcoipStatisticsPcoipPacketsTransmitted": pcoipStatisticsPcoipPacketsTransmitted,
       "pcoipStatisticsPcoipBytesTransmitted": pcoipStatisticsPcoipBytesTransmitted,
       "pcoipStatisticsPcoipPacketsReceived": pcoipStatisticsPcoipPacketsReceived,
       "pcoipStatisticsPcoipBytesReceived": pcoipStatisticsPcoipBytesReceived,
       "pcoipStatisticsPcoipLostPackets": pcoipStatisticsPcoipLostPackets,
       "pcoipStatisticsPcoipLatency": pcoipStatisticsPcoipLatency,
       "teraImagingStatistics": teraImagingStatistics,
       "imagingStatisticsTable": imagingStatisticsTable,
       "imagingStatisticsEntry": imagingStatisticsEntry,
       "imagingStatisticsIndex": imagingStatisticsIndex,
       "imagingStatisticsSessionNumber": imagingStatisticsSessionNumber,
       "imagingStatisticsSessionActive": imagingStatisticsSessionActive,
       "imagingStatisticsDisplayActive": imagingStatisticsDisplayActive,
       "imagingStatisticsDisplayWidth": imagingStatisticsDisplayWidth,
       "imagingStatisticsDisplayHeight": imagingStatisticsDisplayHeight,
       "imagingStatisticsDisplayRefreshRate": imagingStatisticsDisplayRefreshRate,
       "imagingStatisticsFrameCount": imagingStatisticsFrameCount}
)
