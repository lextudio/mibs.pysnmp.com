# SNMP MIB module (RBN-CPU-METER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-CPU-METER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:03 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPercentage,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPercentage")

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

rbnCpuMeterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6)
)
rbnCpuMeterMIB.setRevisions(
        ("2011-12-13 18:00",
         "2011-01-19 18:00",
         "2002-12-16 00:00",
         "2002-06-26 00:00",
         "2002-05-29 00:00",
         "1999-06-16 23:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Percentage(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_RbnCpuMeterMIBObjects_ObjectIdentity = ObjectIdentity
rbnCpuMeterMIBObjects = _RbnCpuMeterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1)
)
_RbnCpuMeterFiveSecondAvg_Type = RbnPercentage
_RbnCpuMeterFiveSecondAvg_Object = MibScalar
rbnCpuMeterFiveSecondAvg = _RbnCpuMeterFiveSecondAvg_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 1),
    _RbnCpuMeterFiveSecondAvg_Type()
)
rbnCpuMeterFiveSecondAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuMeterFiveSecondAvg.setStatus("current")
_RbnCpuMeterOneMinuteAvg_Type = RbnPercentage
_RbnCpuMeterOneMinuteAvg_Object = MibScalar
rbnCpuMeterOneMinuteAvg = _RbnCpuMeterOneMinuteAvg_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 2),
    _RbnCpuMeterOneMinuteAvg_Type()
)
rbnCpuMeterOneMinuteAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuMeterOneMinuteAvg.setStatus("current")
_RbnCpuMeterFiveMinuteAvg_Type = RbnPercentage
_RbnCpuMeterFiveMinuteAvg_Object = MibScalar
rbnCpuMeterFiveMinuteAvg = _RbnCpuMeterFiveMinuteAvg_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 3),
    _RbnCpuMeterFiveMinuteAvg_Type()
)
rbnCpuMeterFiveMinuteAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuMeterFiveMinuteAvg.setStatus("current")
_RbnCpuMeterFiveSecondPeak_Type = RbnPercentage
_RbnCpuMeterFiveSecondPeak_Object = MibScalar
rbnCpuMeterFiveSecondPeak = _RbnCpuMeterFiveSecondPeak_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 4),
    _RbnCpuMeterFiveSecondPeak_Type()
)
rbnCpuMeterFiveSecondPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuMeterFiveSecondPeak.setStatus("current")
_RbnCpuMeterOneMinutePeak_Type = RbnPercentage
_RbnCpuMeterOneMinutePeak_Object = MibScalar
rbnCpuMeterOneMinutePeak = _RbnCpuMeterOneMinutePeak_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 5),
    _RbnCpuMeterOneMinutePeak_Type()
)
rbnCpuMeterOneMinutePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuMeterOneMinutePeak.setStatus("current")
_RbnCpuMeterFiveMinutePeak_Type = RbnPercentage
_RbnCpuMeterFiveMinutePeak_Object = MibScalar
rbnCpuMeterFiveMinutePeak = _RbnCpuMeterFiveMinutePeak_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 1, 6),
    _RbnCpuMeterFiveMinutePeak_Type()
)
rbnCpuMeterFiveMinutePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuMeterFiveMinutePeak.setStatus("current")
_RbnCpuMeterMIBConformance_ObjectIdentity = ObjectIdentity
rbnCpuMeterMIBConformance = _RbnCpuMeterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2)
)
_RbnCpuMeterMIBGroups_ObjectIdentity = ObjectIdentity
rbnCpuMeterMIBGroups = _RbnCpuMeterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1)
)
_RbnCpuMeterMIBCompliances_ObjectIdentity = ObjectIdentity
rbnCpuMeterMIBCompliances = _RbnCpuMeterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2)
)
_RbnCpuProcGroups_ObjectIdentity = ObjectIdentity
rbnCpuProcGroups = _RbnCpuProcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 3)
)
_RbnCpuProcMIBObjects_ObjectIdentity = ObjectIdentity
rbnCpuProcMIBObjects = _RbnCpuProcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3)
)
_RbnCpuProcTable_Object = MibTable
rbnCpuProcTable = _RbnCpuProcTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    rbnCpuProcTable.setStatus("current")
_RbnCpuProcEntry_Object = MibTableRow
rbnCpuProcEntry = _RbnCpuProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1)
)
rbnCpuProcEntry.setIndexNames(
    (1, "RBN-CPU-METER-MIB", "rbnCpuProcName"),
)
if mibBuilder.loadTexts:
    rbnCpuProcEntry.setStatus("current")


class _RbnCpuProcName_Type(DisplayString):
    """Custom type rbnCpuProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 114),
    )


_RbnCpuProcName_Type.__name__ = "DisplayString"
_RbnCpuProcName_Object = MibTableColumn
rbnCpuProcName = _RbnCpuProcName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 1),
    _RbnCpuProcName_Type()
)
rbnCpuProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProcName.setStatus("current")


class _RbnCpuProcPriority_Type(Unsigned32):
    """Custom type rbnCpuProcPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnCpuProcPriority_Type.__name__ = "Unsigned32"
_RbnCpuProcPriority_Object = MibTableColumn
rbnCpuProcPriority = _RbnCpuProcPriority_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 2),
    _RbnCpuProcPriority_Type()
)
rbnCpuProcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProcPriority.setStatus("current")
_RbnCpuProcTime_Type = Counter32
_RbnCpuProcTime_Object = MibTableColumn
rbnCpuProcTime = _RbnCpuProcTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 3),
    _RbnCpuProcTime_Type()
)
rbnCpuProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProcTime.setStatus("current")
_RbnCpuProcCalls_Type = Counter32
_RbnCpuProcCalls_Object = MibTableColumn
rbnCpuProcCalls = _RbnCpuProcCalls_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 4),
    _RbnCpuProcCalls_Type()
)
rbnCpuProcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProcCalls.setStatus("current")
_RbnCpuProc5Sec_Type = RbnPercentage
_RbnCpuProc5Sec_Object = MibTableColumn
rbnCpuProc5Sec = _RbnCpuProc5Sec_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 5),
    _RbnCpuProc5Sec_Type()
)
rbnCpuProc5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProc5Sec.setStatus("current")
_RbnCpuProc1Min_Type = RbnPercentage
_RbnCpuProc1Min_Object = MibTableColumn
rbnCpuProc1Min = _RbnCpuProc1Min_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 6),
    _RbnCpuProc1Min_Type()
)
rbnCpuProc1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProc1Min.setStatus("current")
_RbnCpuProc5Min_Type = RbnPercentage
_RbnCpuProc5Min_Object = MibTableColumn
rbnCpuProc5Min = _RbnCpuProc5Min_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 7),
    _RbnCpuProc5Min_Type()
)
rbnCpuProc5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProc5Min.setStatus("current")
_RbnCpuProcLongest_Type = Gauge32
_RbnCpuProcLongest_Object = MibTableColumn
rbnCpuProcLongest = _RbnCpuProcLongest_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 3, 1, 1, 8),
    _RbnCpuProcLongest_Type()
)
rbnCpuProcLongest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCpuProcLongest.setStatus("current")

# Managed Objects groups

rbnCpuMeterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1, 1)
)
rbnCpuMeterStatsGroup.setObjects(
      *(("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondAvg"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinuteAvg"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinuteAvg"))
)
if mibBuilder.loadTexts:
    rbnCpuMeterStatsGroup.setStatus("deprecated")

rbnCpuMeterStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 1, 2)
)
rbnCpuMeterStatsGroup2.setObjects(
      *(("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondAvg"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinuteAvg"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinuteAvg"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveSecondPeak"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterOneMinutePeak"),
        ("RBN-CPU-METER-MIB", "rbnCpuMeterFiveMinutePeak"))
)
if mibBuilder.loadTexts:
    rbnCpuMeterStatsGroup2.setStatus("current")

rbnCpuProcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 3, 1)
)
rbnCpuProcGroup.setObjects(
      *(("RBN-CPU-METER-MIB", "rbnCpuProcName"),
        ("RBN-CPU-METER-MIB", "rbnCpuProcPriority"),
        ("RBN-CPU-METER-MIB", "rbnCpuProcTime"),
        ("RBN-CPU-METER-MIB", "rbnCpuProcCalls"),
        ("RBN-CPU-METER-MIB", "rbnCpuProc5Sec"),
        ("RBN-CPU-METER-MIB", "rbnCpuProc1Min"),
        ("RBN-CPU-METER-MIB", "rbnCpuProc5Min"),
        ("RBN-CPU-METER-MIB", "rbnCpuProcLongest"))
)
if mibBuilder.loadTexts:
    rbnCpuProcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnCpuMeterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnCpuMeterMIBCompliance.setStatus(
        "deprecated"
    )

rbnCpuMeterMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rbnCpuMeterMIBCompliance1.setStatus(
        "deprecated"
    )

rbnCpuMeterMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 6, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rbnCpuMeterMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-CPU-METER-MIB",
    **{"Percentage": Percentage,
       "rbnCpuMeterMIB": rbnCpuMeterMIB,
       "rbnCpuMeterMIBObjects": rbnCpuMeterMIBObjects,
       "rbnCpuMeterFiveSecondAvg": rbnCpuMeterFiveSecondAvg,
       "rbnCpuMeterOneMinuteAvg": rbnCpuMeterOneMinuteAvg,
       "rbnCpuMeterFiveMinuteAvg": rbnCpuMeterFiveMinuteAvg,
       "rbnCpuMeterFiveSecondPeak": rbnCpuMeterFiveSecondPeak,
       "rbnCpuMeterOneMinutePeak": rbnCpuMeterOneMinutePeak,
       "rbnCpuMeterFiveMinutePeak": rbnCpuMeterFiveMinutePeak,
       "rbnCpuMeterMIBConformance": rbnCpuMeterMIBConformance,
       "rbnCpuMeterMIBGroups": rbnCpuMeterMIBGroups,
       "rbnCpuMeterStatsGroup": rbnCpuMeterStatsGroup,
       "rbnCpuMeterStatsGroup2": rbnCpuMeterStatsGroup2,
       "rbnCpuMeterMIBCompliances": rbnCpuMeterMIBCompliances,
       "rbnCpuMeterMIBCompliance": rbnCpuMeterMIBCompliance,
       "rbnCpuMeterMIBCompliance1": rbnCpuMeterMIBCompliance1,
       "rbnCpuMeterMIBCompliance2": rbnCpuMeterMIBCompliance2,
       "rbnCpuProcGroups": rbnCpuProcGroups,
       "rbnCpuProcGroup": rbnCpuProcGroup,
       "rbnCpuProcMIBObjects": rbnCpuProcMIBObjects,
       "rbnCpuProcTable": rbnCpuProcTable,
       "rbnCpuProcEntry": rbnCpuProcEntry,
       "rbnCpuProcName": rbnCpuProcName,
       "rbnCpuProcPriority": rbnCpuProcPriority,
       "rbnCpuProcTime": rbnCpuProcTime,
       "rbnCpuProcCalls": rbnCpuProcCalls,
       "rbnCpuProc5Sec": rbnCpuProc5Sec,
       "rbnCpuProc1Min": rbnCpuProc1Min,
       "rbnCpuProc5Min": rbnCpuProc5Min,
       "rbnCpuProcLongest": rbnCpuProcLongest}
)
