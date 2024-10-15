# SNMP MIB module (GSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:54 2024
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

(gsa,) = mibBuilder.importSymbols(
    "GOOGLE-MIB",
    "gsa")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Crawl_ObjectIdentity = ObjectIdentity
crawl = _Crawl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1)
)


class _CrawlRunning_Type(Integer32):
    """Custom type crawlRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("paused", 0),
          ("running", 1))
    )


_CrawlRunning_Type.__name__ = "Integer32"
_CrawlRunning_Object = MibScalar
crawlRunning = _CrawlRunning_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 1),
    _CrawlRunning_Type()
)
crawlRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crawlRunning.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2)
)
_DocsServed_Type = Integer32
_DocsServed_Object = MibScalar
docsServed = _DocsServed_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 1),
    _DocsServed_Type()
)
docsServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsServed.setStatus("current")
_CrawlingRate_Type = Integer32
_CrawlingRate_Object = MibScalar
crawlingRate = _CrawlingRate_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 2),
    _CrawlingRate_Type()
)
crawlingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crawlingRate.setStatus("current")
_DocBytes_Type = Integer32
_DocBytes_Object = MibScalar
docBytes = _DocBytes_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 3),
    _DocBytes_Type()
)
docBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docBytes.setStatus("current")
_TodayDocsCrawled_Type = Integer32
_TodayDocsCrawled_Object = MibScalar
todayDocsCrawled = _TodayDocsCrawled_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 4),
    _TodayDocsCrawled_Type()
)
todayDocsCrawled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    todayDocsCrawled.setStatus("current")
_DocErrors_Type = Integer32
_DocErrors_Object = MibScalar
docErrors = _DocErrors_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 5),
    _DocErrors_Type()
)
docErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docErrors.setStatus("current")
_DocsFound_Type = Integer32
_DocsFound_Object = MibScalar
docsFound = _DocsFound_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 6),
    _DocsFound_Type()
)
docsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsFound.setStatus("current")


class _BatchCrawlRunning_Type(Integer32):
    """Custom type batchCrawlRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_BatchCrawlRunning_Type.__name__ = "Integer32"
_BatchCrawlRunning_Object = MibScalar
batchCrawlRunning = _BatchCrawlRunning_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 7),
    _BatchCrawlRunning_Type()
)
batchCrawlRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchCrawlRunning.setStatus("current")
_BatchCrawlStartTime_Type = Integer32
_BatchCrawlStartTime_Object = MibScalar
batchCrawlStartTime = _BatchCrawlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 8),
    _BatchCrawlStartTime_Type()
)
batchCrawlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchCrawlStartTime.setStatus("current")
_BatchCrawlEndTime_Type = Integer32
_BatchCrawlEndTime_Object = MibScalar
batchCrawlEndTime = _BatchCrawlEndTime_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 9),
    _BatchCrawlEndTime_Type()
)
batchCrawlEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchCrawlEndTime.setStatus("current")


class _BatchCrawlEndReason_Type(Integer32):
    """Custom type batchCrawlEndReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schedulestopped", 1),
          ("urllimit", 0))
    )


_BatchCrawlEndReason_Type.__name__ = "Integer32"
_BatchCrawlEndReason_Object = MibScalar
batchCrawlEndReason = _BatchCrawlEndReason_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 2, 10),
    _BatchCrawlEndReason_Type()
)
batchCrawlEndReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchCrawlEndReason.setStatus("current")
_Diagnostics_ObjectIdentity = ObjectIdentity
diagnostics = _Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 1, 3)
)
_Serving_ObjectIdentity = ObjectIdentity
serving = _Serving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 2)
)
_Qpm_Type = Integer32
_Qpm_Object = MibScalar
qpm = _Qpm_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 2, 1),
    _Qpm_Type()
)
qpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qpm.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3)
)
_GsaDisk_ObjectIdentity = ObjectIdentity
gsaDisk = _GsaDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 1)
)


class _DiskHealth_Type(Integer32):
    """Custom type diskHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("red", 2),
          ("yellow", 1))
    )


_DiskHealth_Type.__name__ = "Integer32"
_DiskHealth_Object = MibScalar
diskHealth = _DiskHealth_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 1, 1),
    _DiskHealth_Type()
)
diskHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskHealth.setStatus("current")
_DiskErrors_Type = DisplayString
_DiskErrors_Object = MibScalar
diskErrors = _DiskErrors_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 1, 2),
    _DiskErrors_Type()
)
diskErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskErrors.setStatus("current")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 2)
)


class _TemperatureHealth_Type(Integer32):
    """Custom type temperatureHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("red", 2),
          ("yellow", 1))
    )


_TemperatureHealth_Type.__name__ = "Integer32"
_TemperatureHealth_Object = MibScalar
temperatureHealth = _TemperatureHealth_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 2, 1),
    _TemperatureHealth_Type()
)
temperatureHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureHealth.setStatus("current")
_TemperatureErrors_Type = DisplayString
_TemperatureErrors_Object = MibScalar
temperatureErrors = _TemperatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 2, 2),
    _TemperatureErrors_Type()
)
temperatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureErrors.setStatus("current")
_Machine_ObjectIdentity = ObjectIdentity
machine = _Machine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 3)
)


class _MachineHealth_Type(Integer32):
    """Custom type machineHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("red", 2),
          ("yellow", 1))
    )


_MachineHealth_Type.__name__ = "Integer32"
_MachineHealth_Object = MibScalar
machineHealth = _MachineHealth_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 3, 1),
    _MachineHealth_Type()
)
machineHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineHealth.setStatus("current")
_MachineErrors_Type = DisplayString
_MachineErrors_Object = MibScalar
machineErrors = _MachineErrors_Object(
    (1, 3, 6, 1, 4, 1, 11129, 1, 3, 3, 2),
    _MachineErrors_Type()
)
machineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineErrors.setStatus("current")
_Search_ObjectIdentity = ObjectIdentity
search = _Search_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 4)
)
_Reports_ObjectIdentity = ObjectIdentity
reports = _Reports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 4, 1)
)
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 4, 2)
)
_EventLogs_ObjectIdentity = ObjectIdentity
eventLogs = _EventLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11129, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GSA-MIB",
    **{"crawl": crawl,
       "crawlRunning": crawlRunning,
       "status": status,
       "docsServed": docsServed,
       "crawlingRate": crawlingRate,
       "docBytes": docBytes,
       "todayDocsCrawled": todayDocsCrawled,
       "docErrors": docErrors,
       "docsFound": docsFound,
       "batchCrawlRunning": batchCrawlRunning,
       "batchCrawlStartTime": batchCrawlStartTime,
       "batchCrawlEndTime": batchCrawlEndTime,
       "batchCrawlEndReason": batchCrawlEndReason,
       "diagnostics": diagnostics,
       "serving": serving,
       "qpm": qpm,
       "system": system,
       "gsaDisk": gsaDisk,
       "diskHealth": diskHealth,
       "diskErrors": diskErrors,
       "temperature": temperature,
       "temperatureHealth": temperatureHealth,
       "temperatureErrors": temperatureErrors,
       "machine": machine,
       "machineHealth": machineHealth,
       "machineErrors": machineErrors,
       "search": search,
       "reports": reports,
       "logs": logs,
       "eventLogs": eventLogs}
)
