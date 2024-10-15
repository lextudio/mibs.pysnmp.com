# SNMP MIB module (TPT-TRAFFIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-TRAFFIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:14 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_traffic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8)
)
tpt_traffic.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ThresholdFilterState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RateLimitTable_Object = MibTable
rateLimitTable = _RateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    rateLimitTable.setStatus("current")
_RateLimitEntry_Object = MibTableRow
rateLimitEntry = _RateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1)
)
rateLimitEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "rateLimitGlobalID"),
)
if mibBuilder.loadTexts:
    rateLimitEntry.setStatus("current")


class _RateLimitGlobalID_Type(OctetString):
    """Custom type rateLimitGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RateLimitGlobalID_Type.__name__ = "OctetString"
_RateLimitGlobalID_Object = MibTableColumn
rateLimitGlobalID = _RateLimitGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 1),
    _RateLimitGlobalID_Type()
)
rateLimitGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitGlobalID.setStatus("current")
_RateLimitRequestedRate_Type = Unsigned32
_RateLimitRequestedRate_Object = MibTableColumn
rateLimitRequestedRate = _RateLimitRequestedRate_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 2),
    _RateLimitRequestedRate_Type()
)
rateLimitRequestedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitRequestedRate.setStatus("current")
_RateLimitActualRate_Type = Unsigned32
_RateLimitActualRate_Object = MibTableColumn
rateLimitActualRate = _RateLimitActualRate_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 3),
    _RateLimitActualRate_Type()
)
rateLimitActualRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitActualRate.setStatus("current")
_RateLimitPacketsSent_Type = Counter64
_RateLimitPacketsSent_Object = MibTableColumn
rateLimitPacketsSent = _RateLimitPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 4),
    _RateLimitPacketsSent_Type()
)
rateLimitPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitPacketsSent.setStatus("current")
_RateLimitPacketsDropped_Type = Counter64
_RateLimitPacketsDropped_Object = MibTableColumn
rateLimitPacketsDropped = _RateLimitPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 5),
    _RateLimitPacketsDropped_Type()
)
rateLimitPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitPacketsDropped.setStatus("current")
_RateLimitPacketsQueued_Type = Counter64
_RateLimitPacketsQueued_Object = MibTableColumn
rateLimitPacketsQueued = _RateLimitPacketsQueued_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 6),
    _RateLimitPacketsQueued_Type()
)
rateLimitPacketsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitPacketsQueued.setStatus("current")
_RateLimitHistNumSeconds_Type = Unsigned32
_RateLimitHistNumSeconds_Object = MibTableColumn
rateLimitHistNumSeconds = _RateLimitHistNumSeconds_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 7),
    _RateLimitHistNumSeconds_Type()
)
rateLimitHistNumSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistNumSeconds.setStatus("current")
_RateLimitHistNumMinutes_Type = Unsigned32
_RateLimitHistNumMinutes_Object = MibTableColumn
rateLimitHistNumMinutes = _RateLimitHistNumMinutes_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 8),
    _RateLimitHistNumMinutes_Type()
)
rateLimitHistNumMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistNumMinutes.setStatus("current")
_RateLimitHistNumHours_Type = Unsigned32
_RateLimitHistNumHours_Object = MibTableColumn
rateLimitHistNumHours = _RateLimitHistNumHours_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 1, 1, 9),
    _RateLimitHistNumHours_Type()
)
rateLimitHistNumHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistNumHours.setStatus("current")
_RateLimitHistSecondsTable_Object = MibTable
rateLimitHistSecondsTable = _RateLimitHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 2)
)
if mibBuilder.loadTexts:
    rateLimitHistSecondsTable.setStatus("current")
_RateLimitHistSecondsEntry_Object = MibTableRow
rateLimitHistSecondsEntry = _RateLimitHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 2, 1)
)
rateLimitHistSecondsEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "rateLimitHistSecondsGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "rateLimitHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    rateLimitHistSecondsEntry.setStatus("current")


class _RateLimitHistSecondsGlobalID_Type(OctetString):
    """Custom type rateLimitHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RateLimitHistSecondsGlobalID_Type.__name__ = "OctetString"
_RateLimitHistSecondsGlobalID_Object = MibTableColumn
rateLimitHistSecondsGlobalID = _RateLimitHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 2, 1, 1),
    _RateLimitHistSecondsGlobalID_Type()
)
rateLimitHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitHistSecondsGlobalID.setStatus("current")
_RateLimitHistSecondsIndex_Type = Unsigned32
_RateLimitHistSecondsIndex_Object = MibTableColumn
rateLimitHistSecondsIndex = _RateLimitHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 2, 1, 2),
    _RateLimitHistSecondsIndex_Type()
)
rateLimitHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitHistSecondsIndex.setStatus("current")
_RateLimitHistSecondsBytesSent_Type = Counter64
_RateLimitHistSecondsBytesSent_Object = MibTableColumn
rateLimitHistSecondsBytesSent = _RateLimitHistSecondsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 2, 1, 3),
    _RateLimitHistSecondsBytesSent_Type()
)
rateLimitHistSecondsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistSecondsBytesSent.setStatus("current")
_RateLimitHistSecondsTimestamp_Type = Unsigned32
_RateLimitHistSecondsTimestamp_Object = MibTableColumn
rateLimitHistSecondsTimestamp = _RateLimitHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 2, 1, 4),
    _RateLimitHistSecondsTimestamp_Type()
)
rateLimitHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistSecondsTimestamp.setStatus("current")
_RateLimitHistMinutesTable_Object = MibTable
rateLimitHistMinutesTable = _RateLimitHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 3)
)
if mibBuilder.loadTexts:
    rateLimitHistMinutesTable.setStatus("current")
_RateLimitHistMinutesEntry_Object = MibTableRow
rateLimitHistMinutesEntry = _RateLimitHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 3, 1)
)
rateLimitHistMinutesEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "rateLimitHistMinutesGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "rateLimitHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    rateLimitHistMinutesEntry.setStatus("current")


class _RateLimitHistMinutesGlobalID_Type(OctetString):
    """Custom type rateLimitHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RateLimitHistMinutesGlobalID_Type.__name__ = "OctetString"
_RateLimitHistMinutesGlobalID_Object = MibTableColumn
rateLimitHistMinutesGlobalID = _RateLimitHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 3, 1, 1),
    _RateLimitHistMinutesGlobalID_Type()
)
rateLimitHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitHistMinutesGlobalID.setStatus("current")
_RateLimitHistMinutesIndex_Type = Unsigned32
_RateLimitHistMinutesIndex_Object = MibTableColumn
rateLimitHistMinutesIndex = _RateLimitHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 3, 1, 2),
    _RateLimitHistMinutesIndex_Type()
)
rateLimitHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitHistMinutesIndex.setStatus("current")
_RateLimitHistMinutesBytesSent_Type = Counter64
_RateLimitHistMinutesBytesSent_Object = MibTableColumn
rateLimitHistMinutesBytesSent = _RateLimitHistMinutesBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 3, 1, 3),
    _RateLimitHistMinutesBytesSent_Type()
)
rateLimitHistMinutesBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistMinutesBytesSent.setStatus("current")
_RateLimitHistMinutesTimestamp_Type = Unsigned32
_RateLimitHistMinutesTimestamp_Object = MibTableColumn
rateLimitHistMinutesTimestamp = _RateLimitHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 3, 1, 4),
    _RateLimitHistMinutesTimestamp_Type()
)
rateLimitHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistMinutesTimestamp.setStatus("current")
_RateLimitHistHoursTable_Object = MibTable
rateLimitHistHoursTable = _RateLimitHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 4)
)
if mibBuilder.loadTexts:
    rateLimitHistHoursTable.setStatus("current")
_RateLimitHistHoursEntry_Object = MibTableRow
rateLimitHistHoursEntry = _RateLimitHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 4, 1)
)
rateLimitHistHoursEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "rateLimitHistHoursGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "rateLimitHistHoursIndex"),
)
if mibBuilder.loadTexts:
    rateLimitHistHoursEntry.setStatus("current")


class _RateLimitHistHoursGlobalID_Type(OctetString):
    """Custom type rateLimitHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RateLimitHistHoursGlobalID_Type.__name__ = "OctetString"
_RateLimitHistHoursGlobalID_Object = MibTableColumn
rateLimitHistHoursGlobalID = _RateLimitHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 4, 1, 1),
    _RateLimitHistHoursGlobalID_Type()
)
rateLimitHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitHistHoursGlobalID.setStatus("current")
_RateLimitHistHoursIndex_Type = Unsigned32
_RateLimitHistHoursIndex_Object = MibTableColumn
rateLimitHistHoursIndex = _RateLimitHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 4, 1, 2),
    _RateLimitHistHoursIndex_Type()
)
rateLimitHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rateLimitHistHoursIndex.setStatus("current")
_RateLimitHistHoursBytesSent_Type = Counter64
_RateLimitHistHoursBytesSent_Object = MibTableColumn
rateLimitHistHoursBytesSent = _RateLimitHistHoursBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 4, 1, 3),
    _RateLimitHistHoursBytesSent_Type()
)
rateLimitHistHoursBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistHoursBytesSent.setStatus("current")
_RateLimitHistHoursTimestamp_Type = Unsigned32
_RateLimitHistHoursTimestamp_Object = MibTableColumn
rateLimitHistHoursTimestamp = _RateLimitHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 4, 1, 4),
    _RateLimitHistHoursTimestamp_Type()
)
rateLimitHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitHistHoursTimestamp.setStatus("current")
_ThresholdHistSecondsTable_Object = MibTable
thresholdHistSecondsTable = _ThresholdHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 5)
)
if mibBuilder.loadTexts:
    thresholdHistSecondsTable.setStatus("current")
_ThresholdHistSecondsEntry_Object = MibTableRow
thresholdHistSecondsEntry = _ThresholdHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 5, 1)
)
thresholdHistSecondsEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "thresholdHistSecondsGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "thresholdHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    thresholdHistSecondsEntry.setStatus("current")


class _ThresholdHistSecondsGlobalID_Type(OctetString):
    """Custom type thresholdHistSecondsGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ThresholdHistSecondsGlobalID_Type.__name__ = "OctetString"
_ThresholdHistSecondsGlobalID_Object = MibTableColumn
thresholdHistSecondsGlobalID = _ThresholdHistSecondsGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 5, 1, 1),
    _ThresholdHistSecondsGlobalID_Type()
)
thresholdHistSecondsGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistSecondsGlobalID.setStatus("current")
_ThresholdHistSecondsIndex_Type = Unsigned32
_ThresholdHistSecondsIndex_Object = MibTableColumn
thresholdHistSecondsIndex = _ThresholdHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 5, 1, 2),
    _ThresholdHistSecondsIndex_Type()
)
thresholdHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistSecondsIndex.setStatus("current")
_ThresholdHistSecondsUnitCount_Type = Counter64
_ThresholdHistSecondsUnitCount_Object = MibTableColumn
thresholdHistSecondsUnitCount = _ThresholdHistSecondsUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 5, 1, 3),
    _ThresholdHistSecondsUnitCount_Type()
)
thresholdHistSecondsUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistSecondsUnitCount.setStatus("current")
_ThresholdHistSecondsTimestamp_Type = Unsigned32
_ThresholdHistSecondsTimestamp_Object = MibTableColumn
thresholdHistSecondsTimestamp = _ThresholdHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 5, 1, 4),
    _ThresholdHistSecondsTimestamp_Type()
)
thresholdHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistSecondsTimestamp.setStatus("current")
_ThresholdHistMinutesTable_Object = MibTable
thresholdHistMinutesTable = _ThresholdHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 6)
)
if mibBuilder.loadTexts:
    thresholdHistMinutesTable.setStatus("current")
_ThresholdHistMinutesEntry_Object = MibTableRow
thresholdHistMinutesEntry = _ThresholdHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 6, 1)
)
thresholdHistMinutesEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "thresholdHistMinutesGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "thresholdHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    thresholdHistMinutesEntry.setStatus("current")


class _ThresholdHistMinutesGlobalID_Type(OctetString):
    """Custom type thresholdHistMinutesGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ThresholdHistMinutesGlobalID_Type.__name__ = "OctetString"
_ThresholdHistMinutesGlobalID_Object = MibTableColumn
thresholdHistMinutesGlobalID = _ThresholdHistMinutesGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 6, 1, 1),
    _ThresholdHistMinutesGlobalID_Type()
)
thresholdHistMinutesGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistMinutesGlobalID.setStatus("current")
_ThresholdHistMinutesIndex_Type = Unsigned32
_ThresholdHistMinutesIndex_Object = MibTableColumn
thresholdHistMinutesIndex = _ThresholdHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 6, 1, 2),
    _ThresholdHistMinutesIndex_Type()
)
thresholdHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistMinutesIndex.setStatus("current")
_ThresholdHistMinutesUnitCount_Type = Counter64
_ThresholdHistMinutesUnitCount_Object = MibTableColumn
thresholdHistMinutesUnitCount = _ThresholdHistMinutesUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 6, 1, 3),
    _ThresholdHistMinutesUnitCount_Type()
)
thresholdHistMinutesUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistMinutesUnitCount.setStatus("current")
_ThresholdHistMinutesTimestamp_Type = Unsigned32
_ThresholdHistMinutesTimestamp_Object = MibTableColumn
thresholdHistMinutesTimestamp = _ThresholdHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 6, 1, 4),
    _ThresholdHistMinutesTimestamp_Type()
)
thresholdHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistMinutesTimestamp.setStatus("current")
_ThresholdHistHoursTable_Object = MibTable
thresholdHistHoursTable = _ThresholdHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 7)
)
if mibBuilder.loadTexts:
    thresholdHistHoursTable.setStatus("current")
_ThresholdHistHoursEntry_Object = MibTableRow
thresholdHistHoursEntry = _ThresholdHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 7, 1)
)
thresholdHistHoursEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "thresholdHistHoursGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "thresholdHistHoursIndex"),
)
if mibBuilder.loadTexts:
    thresholdHistHoursEntry.setStatus("current")


class _ThresholdHistHoursGlobalID_Type(OctetString):
    """Custom type thresholdHistHoursGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ThresholdHistHoursGlobalID_Type.__name__ = "OctetString"
_ThresholdHistHoursGlobalID_Object = MibTableColumn
thresholdHistHoursGlobalID = _ThresholdHistHoursGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 7, 1, 1),
    _ThresholdHistHoursGlobalID_Type()
)
thresholdHistHoursGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistHoursGlobalID.setStatus("current")
_ThresholdHistHoursIndex_Type = Unsigned32
_ThresholdHistHoursIndex_Object = MibTableColumn
thresholdHistHoursIndex = _ThresholdHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 7, 1, 2),
    _ThresholdHistHoursIndex_Type()
)
thresholdHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistHoursIndex.setStatus("current")
_ThresholdHistHoursUnitCount_Type = Counter64
_ThresholdHistHoursUnitCount_Object = MibTableColumn
thresholdHistHoursUnitCount = _ThresholdHistHoursUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 7, 1, 3),
    _ThresholdHistHoursUnitCount_Type()
)
thresholdHistHoursUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistHoursUnitCount.setStatus("current")
_ThresholdHistHoursTimestamp_Type = Unsigned32
_ThresholdHistHoursTimestamp_Object = MibTableColumn
thresholdHistHoursTimestamp = _ThresholdHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 7, 1, 4),
    _ThresholdHistHoursTimestamp_Type()
)
thresholdHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistHoursTimestamp.setStatus("current")
_ThresholdHistDaysTable_Object = MibTable
thresholdHistDaysTable = _ThresholdHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 8)
)
if mibBuilder.loadTexts:
    thresholdHistDaysTable.setStatus("current")
_ThresholdHistDaysEntry_Object = MibTableRow
thresholdHistDaysEntry = _ThresholdHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 8, 1)
)
thresholdHistDaysEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "thresholdHistDaysGlobalID"),
    (0, "TPT-TRAFFIC-MIB", "thresholdHistDaysIndex"),
)
if mibBuilder.loadTexts:
    thresholdHistDaysEntry.setStatus("current")


class _ThresholdHistDaysGlobalID_Type(OctetString):
    """Custom type thresholdHistDaysGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ThresholdHistDaysGlobalID_Type.__name__ = "OctetString"
_ThresholdHistDaysGlobalID_Object = MibTableColumn
thresholdHistDaysGlobalID = _ThresholdHistDaysGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 8, 1, 1),
    _ThresholdHistDaysGlobalID_Type()
)
thresholdHistDaysGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistDaysGlobalID.setStatus("current")
_ThresholdHistDaysIndex_Type = Unsigned32
_ThresholdHistDaysIndex_Object = MibTableColumn
thresholdHistDaysIndex = _ThresholdHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 8, 1, 2),
    _ThresholdHistDaysIndex_Type()
)
thresholdHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdHistDaysIndex.setStatus("current")
_ThresholdHistDaysUnitCount_Type = Counter64
_ThresholdHistDaysUnitCount_Object = MibTableColumn
thresholdHistDaysUnitCount = _ThresholdHistDaysUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 8, 1, 3),
    _ThresholdHistDaysUnitCount_Type()
)
thresholdHistDaysUnitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistDaysUnitCount.setStatus("current")
_ThresholdHistDaysTimestamp_Type = Unsigned32
_ThresholdHistDaysTimestamp_Object = MibTableColumn
thresholdHistDaysTimestamp = _ThresholdHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 8, 1, 4),
    _ThresholdHistDaysTimestamp_Type()
)
thresholdHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdHistDaysTimestamp.setStatus("current")
_ThresholdTable_Object = MibTable
thresholdTable = _ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 9)
)
if mibBuilder.loadTexts:
    thresholdTable.setStatus("current")
_ThresholdEntry_Object = MibTableRow
thresholdEntry = _ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 9, 1)
)
thresholdEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "thresholdGlobalID"),
)
if mibBuilder.loadTexts:
    thresholdEntry.setStatus("current")


class _ThresholdGlobalID_Type(OctetString):
    """Custom type thresholdGlobalID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ThresholdGlobalID_Type.__name__ = "OctetString"
_ThresholdGlobalID_Object = MibTableColumn
thresholdGlobalID = _ThresholdGlobalID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 9, 1, 1),
    _ThresholdGlobalID_Type()
)
thresholdGlobalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thresholdGlobalID.setStatus("current")
_ThresholdState_Type = ThresholdFilterState
_ThresholdState_Object = MibTableColumn
thresholdState = _ThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 9, 1, 2),
    _ThresholdState_Type()
)
thresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdState.setStatus("current")


class _ThresholdUnits_Type(OctetString):
    """Custom type thresholdUnits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ThresholdUnits_Type.__name__ = "OctetString"
_ThresholdUnits_Object = MibTableColumn
thresholdUnits = _ThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 9, 1, 3),
    _ThresholdUnits_Type()
)
thresholdUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdUnits.setStatus("current")
_InterfaceHistSecondsTable_Object = MibTable
interfaceHistSecondsTable = _InterfaceHistSecondsTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10)
)
if mibBuilder.loadTexts:
    interfaceHistSecondsTable.setStatus("current")
_InterfaceHistSecondsEntry_Object = MibTableRow
interfaceHistSecondsEntry = _InterfaceHistSecondsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10, 1)
)
interfaceHistSecondsEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "interfaceHistSecondsIfIndex"),
    (0, "TPT-TRAFFIC-MIB", "interfaceHistSecondsIndex"),
)
if mibBuilder.loadTexts:
    interfaceHistSecondsEntry.setStatus("current")
_InterfaceHistSecondsIfIndex_Type = InterfaceIndex
_InterfaceHistSecondsIfIndex_Object = MibTableColumn
interfaceHistSecondsIfIndex = _InterfaceHistSecondsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10, 1, 1),
    _InterfaceHistSecondsIfIndex_Type()
)
interfaceHistSecondsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistSecondsIfIndex.setStatus("current")
_InterfaceHistSecondsIndex_Type = Unsigned32
_InterfaceHistSecondsIndex_Object = MibTableColumn
interfaceHistSecondsIndex = _InterfaceHistSecondsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10, 1, 2),
    _InterfaceHistSecondsIndex_Type()
)
interfaceHistSecondsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistSecondsIndex.setStatus("current")
_InterfaceHistSecondsUnitCountIn_Type = Counter64
_InterfaceHistSecondsUnitCountIn_Object = MibTableColumn
interfaceHistSecondsUnitCountIn = _InterfaceHistSecondsUnitCountIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10, 1, 3),
    _InterfaceHistSecondsUnitCountIn_Type()
)
interfaceHistSecondsUnitCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistSecondsUnitCountIn.setStatus("current")
_InterfaceHistSecondsUnitCountOut_Type = Counter64
_InterfaceHistSecondsUnitCountOut_Object = MibTableColumn
interfaceHistSecondsUnitCountOut = _InterfaceHistSecondsUnitCountOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10, 1, 4),
    _InterfaceHistSecondsUnitCountOut_Type()
)
interfaceHistSecondsUnitCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistSecondsUnitCountOut.setStatus("current")
_InterfaceHistSecondsTimestamp_Type = Unsigned32
_InterfaceHistSecondsTimestamp_Object = MibTableColumn
interfaceHistSecondsTimestamp = _InterfaceHistSecondsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 10, 1, 5),
    _InterfaceHistSecondsTimestamp_Type()
)
interfaceHistSecondsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistSecondsTimestamp.setStatus("current")
_InterfaceHistMinutesTable_Object = MibTable
interfaceHistMinutesTable = _InterfaceHistMinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11)
)
if mibBuilder.loadTexts:
    interfaceHistMinutesTable.setStatus("current")
_InterfaceHistMinutesEntry_Object = MibTableRow
interfaceHistMinutesEntry = _InterfaceHistMinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11, 1)
)
interfaceHistMinutesEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "interfaceHistMinutesIfIndex"),
    (0, "TPT-TRAFFIC-MIB", "interfaceHistMinutesIndex"),
)
if mibBuilder.loadTexts:
    interfaceHistMinutesEntry.setStatus("current")
_InterfaceHistMinutesIfIndex_Type = InterfaceIndex
_InterfaceHistMinutesIfIndex_Object = MibTableColumn
interfaceHistMinutesIfIndex = _InterfaceHistMinutesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11, 1, 1),
    _InterfaceHistMinutesIfIndex_Type()
)
interfaceHistMinutesIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistMinutesIfIndex.setStatus("current")
_InterfaceHistMinutesIndex_Type = Unsigned32
_InterfaceHistMinutesIndex_Object = MibTableColumn
interfaceHistMinutesIndex = _InterfaceHistMinutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11, 1, 2),
    _InterfaceHistMinutesIndex_Type()
)
interfaceHistMinutesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistMinutesIndex.setStatus("current")
_InterfaceHistMinutesUnitCountIn_Type = Counter64
_InterfaceHistMinutesUnitCountIn_Object = MibTableColumn
interfaceHistMinutesUnitCountIn = _InterfaceHistMinutesUnitCountIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11, 1, 3),
    _InterfaceHistMinutesUnitCountIn_Type()
)
interfaceHistMinutesUnitCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistMinutesUnitCountIn.setStatus("current")
_InterfaceHistMinutesUnitCountOut_Type = Counter64
_InterfaceHistMinutesUnitCountOut_Object = MibTableColumn
interfaceHistMinutesUnitCountOut = _InterfaceHistMinutesUnitCountOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11, 1, 4),
    _InterfaceHistMinutesUnitCountOut_Type()
)
interfaceHistMinutesUnitCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistMinutesUnitCountOut.setStatus("current")
_InterfaceHistMinutesTimestamp_Type = Unsigned32
_InterfaceHistMinutesTimestamp_Object = MibTableColumn
interfaceHistMinutesTimestamp = _InterfaceHistMinutesTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 11, 1, 5),
    _InterfaceHistMinutesTimestamp_Type()
)
interfaceHistMinutesTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistMinutesTimestamp.setStatus("current")
_InterfaceHistHoursTable_Object = MibTable
interfaceHistHoursTable = _InterfaceHistHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12)
)
if mibBuilder.loadTexts:
    interfaceHistHoursTable.setStatus("current")
_InterfaceHistHoursEntry_Object = MibTableRow
interfaceHistHoursEntry = _InterfaceHistHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12, 1)
)
interfaceHistHoursEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "interfaceHistHoursIfIndex"),
    (0, "TPT-TRAFFIC-MIB", "interfaceHistHoursIndex"),
)
if mibBuilder.loadTexts:
    interfaceHistHoursEntry.setStatus("current")
_InterfaceHistHoursIfIndex_Type = InterfaceIndex
_InterfaceHistHoursIfIndex_Object = MibTableColumn
interfaceHistHoursIfIndex = _InterfaceHistHoursIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12, 1, 1),
    _InterfaceHistHoursIfIndex_Type()
)
interfaceHistHoursIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistHoursIfIndex.setStatus("current")
_InterfaceHistHoursIndex_Type = Unsigned32
_InterfaceHistHoursIndex_Object = MibTableColumn
interfaceHistHoursIndex = _InterfaceHistHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12, 1, 2),
    _InterfaceHistHoursIndex_Type()
)
interfaceHistHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistHoursIndex.setStatus("current")
_InterfaceHistHoursUnitCountIn_Type = Counter64
_InterfaceHistHoursUnitCountIn_Object = MibTableColumn
interfaceHistHoursUnitCountIn = _InterfaceHistHoursUnitCountIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12, 1, 3),
    _InterfaceHistHoursUnitCountIn_Type()
)
interfaceHistHoursUnitCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistHoursUnitCountIn.setStatus("current")
_InterfaceHistHoursUnitCountOut_Type = Counter64
_InterfaceHistHoursUnitCountOut_Object = MibTableColumn
interfaceHistHoursUnitCountOut = _InterfaceHistHoursUnitCountOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12, 1, 4),
    _InterfaceHistHoursUnitCountOut_Type()
)
interfaceHistHoursUnitCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistHoursUnitCountOut.setStatus("current")
_InterfaceHistHoursTimestamp_Type = Unsigned32
_InterfaceHistHoursTimestamp_Object = MibTableColumn
interfaceHistHoursTimestamp = _InterfaceHistHoursTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 12, 1, 5),
    _InterfaceHistHoursTimestamp_Type()
)
interfaceHistHoursTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistHoursTimestamp.setStatus("current")
_InterfaceHistDaysTable_Object = MibTable
interfaceHistDaysTable = _InterfaceHistDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13)
)
if mibBuilder.loadTexts:
    interfaceHistDaysTable.setStatus("current")
_InterfaceHistDaysEntry_Object = MibTableRow
interfaceHistDaysEntry = _InterfaceHistDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13, 1)
)
interfaceHistDaysEntry.setIndexNames(
    (0, "TPT-TRAFFIC-MIB", "interfaceHistDaysIfIndex"),
    (0, "TPT-TRAFFIC-MIB", "interfaceHistDaysIndex"),
)
if mibBuilder.loadTexts:
    interfaceHistDaysEntry.setStatus("current")
_InterfaceHistDaysIfIndex_Type = InterfaceIndex
_InterfaceHistDaysIfIndex_Object = MibTableColumn
interfaceHistDaysIfIndex = _InterfaceHistDaysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13, 1, 1),
    _InterfaceHistDaysIfIndex_Type()
)
interfaceHistDaysIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistDaysIfIndex.setStatus("current")
_InterfaceHistDaysIndex_Type = Unsigned32
_InterfaceHistDaysIndex_Object = MibTableColumn
interfaceHistDaysIndex = _InterfaceHistDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13, 1, 2),
    _InterfaceHistDaysIndex_Type()
)
interfaceHistDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceHistDaysIndex.setStatus("current")
_InterfaceHistDaysUnitCountIn_Type = Counter64
_InterfaceHistDaysUnitCountIn_Object = MibTableColumn
interfaceHistDaysUnitCountIn = _InterfaceHistDaysUnitCountIn_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13, 1, 3),
    _InterfaceHistDaysUnitCountIn_Type()
)
interfaceHistDaysUnitCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistDaysUnitCountIn.setStatus("current")
_InterfaceHistDaysUnitCountOut_Type = Counter64
_InterfaceHistDaysUnitCountOut_Object = MibTableColumn
interfaceHistDaysUnitCountOut = _InterfaceHistDaysUnitCountOut_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13, 1, 4),
    _InterfaceHistDaysUnitCountOut_Type()
)
interfaceHistDaysUnitCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistDaysUnitCountOut.setStatus("current")
_InterfaceHistDaysTimestamp_Type = Unsigned32
_InterfaceHistDaysTimestamp_Object = MibTableColumn
interfaceHistDaysTimestamp = _InterfaceHistDaysTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 8, 13, 1, 5),
    _InterfaceHistDaysTimestamp_Type()
)
interfaceHistDaysTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHistDaysTimestamp.setStatus("current")


class _TptThresholdNotifyDeviceID_Type(OctetString):
    """Custom type tptThresholdNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptThresholdNotifyDeviceID_Type.__name__ = "OctetString"
_TptThresholdNotifyDeviceID_Object = MibScalar
tptThresholdNotifyDeviceID = _TptThresholdNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 111),
    _TptThresholdNotifyDeviceID_Type()
)
tptThresholdNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptThresholdNotifyDeviceID.setStatus("current")


class _TptThresholdNotifyPolicyID_Type(OctetString):
    """Custom type tptThresholdNotifyPolicyID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptThresholdNotifyPolicyID_Type.__name__ = "OctetString"
_TptThresholdNotifyPolicyID_Object = MibScalar
tptThresholdNotifyPolicyID = _TptThresholdNotifyPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 112),
    _TptThresholdNotifyPolicyID_Type()
)
tptThresholdNotifyPolicyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptThresholdNotifyPolicyID.setStatus("current")


class _TptThresholdNotifySignatureID_Type(OctetString):
    """Custom type tptThresholdNotifySignatureID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptThresholdNotifySignatureID_Type.__name__ = "OctetString"
_TptThresholdNotifySignatureID_Object = MibScalar
tptThresholdNotifySignatureID = _TptThresholdNotifySignatureID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 113),
    _TptThresholdNotifySignatureID_Type()
)
tptThresholdNotifySignatureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptThresholdNotifySignatureID.setStatus("current")


class _TptThresholdNotifySegmentName_Type(OctetString):
    """Custom type tptThresholdNotifySegmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptThresholdNotifySegmentName_Type.__name__ = "OctetString"
_TptThresholdNotifySegmentName_Object = MibScalar
tptThresholdNotifySegmentName = _TptThresholdNotifySegmentName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 114),
    _TptThresholdNotifySegmentName_Type()
)
tptThresholdNotifySegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptThresholdNotifySegmentName.setStatus("obsolete")


class _TptThresholdNotifyZonePair_Type(OctetString):
    """Custom type tptThresholdNotifyZonePair based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptThresholdNotifyZonePair_Type.__name__ = "OctetString"
_TptThresholdNotifyZonePair_Object = MibScalar
tptThresholdNotifyZonePair = _TptThresholdNotifyZonePair_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 115),
    _TptThresholdNotifyZonePair_Type()
)
tptThresholdNotifyZonePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptThresholdNotifyZonePair.setStatus("current")

# Managed Objects groups


# Notification objects

tptThresholdFilterNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 17)
)
tptThresholdFilterNotify.setObjects(
      *(("TPT-TRAFFIC-MIB", "tptThresholdNotifyDeviceID"),
        ("TPT-TRAFFIC-MIB", "tptThresholdNotifyPolicyID"),
        ("TPT-TRAFFIC-MIB", "tptThresholdNotifySignatureID"),
        ("TPT-TRAFFIC-MIB", "tptThresholdNotifyZonePair"))
)
if mibBuilder.loadTexts:
    tptThresholdFilterNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-TRAFFIC-MIB",
    **{"ThresholdFilterState": ThresholdFilterState,
       "tpt-traffic": tpt_traffic,
       "rateLimitTable": rateLimitTable,
       "rateLimitEntry": rateLimitEntry,
       "rateLimitGlobalID": rateLimitGlobalID,
       "rateLimitRequestedRate": rateLimitRequestedRate,
       "rateLimitActualRate": rateLimitActualRate,
       "rateLimitPacketsSent": rateLimitPacketsSent,
       "rateLimitPacketsDropped": rateLimitPacketsDropped,
       "rateLimitPacketsQueued": rateLimitPacketsQueued,
       "rateLimitHistNumSeconds": rateLimitHistNumSeconds,
       "rateLimitHistNumMinutes": rateLimitHistNumMinutes,
       "rateLimitHistNumHours": rateLimitHistNumHours,
       "rateLimitHistSecondsTable": rateLimitHistSecondsTable,
       "rateLimitHistSecondsEntry": rateLimitHistSecondsEntry,
       "rateLimitHistSecondsGlobalID": rateLimitHistSecondsGlobalID,
       "rateLimitHistSecondsIndex": rateLimitHistSecondsIndex,
       "rateLimitHistSecondsBytesSent": rateLimitHistSecondsBytesSent,
       "rateLimitHistSecondsTimestamp": rateLimitHistSecondsTimestamp,
       "rateLimitHistMinutesTable": rateLimitHistMinutesTable,
       "rateLimitHistMinutesEntry": rateLimitHistMinutesEntry,
       "rateLimitHistMinutesGlobalID": rateLimitHistMinutesGlobalID,
       "rateLimitHistMinutesIndex": rateLimitHistMinutesIndex,
       "rateLimitHistMinutesBytesSent": rateLimitHistMinutesBytesSent,
       "rateLimitHistMinutesTimestamp": rateLimitHistMinutesTimestamp,
       "rateLimitHistHoursTable": rateLimitHistHoursTable,
       "rateLimitHistHoursEntry": rateLimitHistHoursEntry,
       "rateLimitHistHoursGlobalID": rateLimitHistHoursGlobalID,
       "rateLimitHistHoursIndex": rateLimitHistHoursIndex,
       "rateLimitHistHoursBytesSent": rateLimitHistHoursBytesSent,
       "rateLimitHistHoursTimestamp": rateLimitHistHoursTimestamp,
       "thresholdHistSecondsTable": thresholdHistSecondsTable,
       "thresholdHistSecondsEntry": thresholdHistSecondsEntry,
       "thresholdHistSecondsGlobalID": thresholdHistSecondsGlobalID,
       "thresholdHistSecondsIndex": thresholdHistSecondsIndex,
       "thresholdHistSecondsUnitCount": thresholdHistSecondsUnitCount,
       "thresholdHistSecondsTimestamp": thresholdHistSecondsTimestamp,
       "thresholdHistMinutesTable": thresholdHistMinutesTable,
       "thresholdHistMinutesEntry": thresholdHistMinutesEntry,
       "thresholdHistMinutesGlobalID": thresholdHistMinutesGlobalID,
       "thresholdHistMinutesIndex": thresholdHistMinutesIndex,
       "thresholdHistMinutesUnitCount": thresholdHistMinutesUnitCount,
       "thresholdHistMinutesTimestamp": thresholdHistMinutesTimestamp,
       "thresholdHistHoursTable": thresholdHistHoursTable,
       "thresholdHistHoursEntry": thresholdHistHoursEntry,
       "thresholdHistHoursGlobalID": thresholdHistHoursGlobalID,
       "thresholdHistHoursIndex": thresholdHistHoursIndex,
       "thresholdHistHoursUnitCount": thresholdHistHoursUnitCount,
       "thresholdHistHoursTimestamp": thresholdHistHoursTimestamp,
       "thresholdHistDaysTable": thresholdHistDaysTable,
       "thresholdHistDaysEntry": thresholdHistDaysEntry,
       "thresholdHistDaysGlobalID": thresholdHistDaysGlobalID,
       "thresholdHistDaysIndex": thresholdHistDaysIndex,
       "thresholdHistDaysUnitCount": thresholdHistDaysUnitCount,
       "thresholdHistDaysTimestamp": thresholdHistDaysTimestamp,
       "thresholdTable": thresholdTable,
       "thresholdEntry": thresholdEntry,
       "thresholdGlobalID": thresholdGlobalID,
       "thresholdState": thresholdState,
       "thresholdUnits": thresholdUnits,
       "interfaceHistSecondsTable": interfaceHistSecondsTable,
       "interfaceHistSecondsEntry": interfaceHistSecondsEntry,
       "interfaceHistSecondsIfIndex": interfaceHistSecondsIfIndex,
       "interfaceHistSecondsIndex": interfaceHistSecondsIndex,
       "interfaceHistSecondsUnitCountIn": interfaceHistSecondsUnitCountIn,
       "interfaceHistSecondsUnitCountOut": interfaceHistSecondsUnitCountOut,
       "interfaceHistSecondsTimestamp": interfaceHistSecondsTimestamp,
       "interfaceHistMinutesTable": interfaceHistMinutesTable,
       "interfaceHistMinutesEntry": interfaceHistMinutesEntry,
       "interfaceHistMinutesIfIndex": interfaceHistMinutesIfIndex,
       "interfaceHistMinutesIndex": interfaceHistMinutesIndex,
       "interfaceHistMinutesUnitCountIn": interfaceHistMinutesUnitCountIn,
       "interfaceHistMinutesUnitCountOut": interfaceHistMinutesUnitCountOut,
       "interfaceHistMinutesTimestamp": interfaceHistMinutesTimestamp,
       "interfaceHistHoursTable": interfaceHistHoursTable,
       "interfaceHistHoursEntry": interfaceHistHoursEntry,
       "interfaceHistHoursIfIndex": interfaceHistHoursIfIndex,
       "interfaceHistHoursIndex": interfaceHistHoursIndex,
       "interfaceHistHoursUnitCountIn": interfaceHistHoursUnitCountIn,
       "interfaceHistHoursUnitCountOut": interfaceHistHoursUnitCountOut,
       "interfaceHistHoursTimestamp": interfaceHistHoursTimestamp,
       "interfaceHistDaysTable": interfaceHistDaysTable,
       "interfaceHistDaysEntry": interfaceHistDaysEntry,
       "interfaceHistDaysIfIndex": interfaceHistDaysIfIndex,
       "interfaceHistDaysIndex": interfaceHistDaysIndex,
       "interfaceHistDaysUnitCountIn": interfaceHistDaysUnitCountIn,
       "interfaceHistDaysUnitCountOut": interfaceHistDaysUnitCountOut,
       "interfaceHistDaysTimestamp": interfaceHistDaysTimestamp,
       "tptThresholdFilterNotify": tptThresholdFilterNotify,
       "tptThresholdNotifyDeviceID": tptThresholdNotifyDeviceID,
       "tptThresholdNotifyPolicyID": tptThresholdNotifyPolicyID,
       "tptThresholdNotifySignatureID": tptThresholdNotifySignatureID,
       "tptThresholdNotifySegmentName": tptThresholdNotifySegmentName,
       "tptThresholdNotifyZonePair": tptThresholdNotifyZonePair}
)
