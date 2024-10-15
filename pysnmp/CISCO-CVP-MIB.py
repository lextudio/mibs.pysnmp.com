# SNMP MIB module (CISCO-CVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CVP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:52 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(InetAddressDNS,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressDNS")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCvpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590)
)
ciscoCvpMIB.setRevisions(
        ("2011-09-22 00:00",
         "2007-10-31 00:00",
         "2006-10-06 00:00",
         "2006-05-19 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcvpIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CcvpServiceType(Integer32, TextualConvention):
    status = "current"
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
        *(("h323", 2),
          ("icm", 4),
          ("ivr", 3),
          ("reporting", 5),
          ("sip", 1),
          ("vxml", 6))
    )



class CcvpServiceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("inService", 2),
          ("inServiceCritical", 4),
          ("inServiceWarning", 3),
          ("partialService", 5),
          ("starting", 1),
          ("stopped", 7),
          ("stopping", 6),
          ("unknown", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCvpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCvpMIBNotifs = _CiscoCvpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 0)
)
_CiscoCvpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCvpMIBObjects = _CiscoCvpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1)
)
_CcvpGeneralInfo_ObjectIdentity = ObjectIdentity
ccvpGeneralInfo = _CcvpGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1)
)
_CcvpServerName_Type = InetAddressDNS
_CcvpServerName_Object = MibScalar
ccvpServerName = _CcvpServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 1),
    _CcvpServerName_Type()
)
ccvpServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpServerName.setStatus("current")
_CcvpDescription_Type = SnmpAdminString
_CcvpDescription_Object = MibScalar
ccvpDescription = _CcvpDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 2),
    _CcvpDescription_Type()
)
ccvpDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpDescription.setStatus("current")
_CcvpVersion_Type = SnmpAdminString
_CcvpVersion_Object = MibScalar
ccvpVersion = _CcvpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 3),
    _CcvpVersion_Type()
)
ccvpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVersion.setStatus("current")
_CcvpStartTime_Type = DateAndTime
_CcvpStartTime_Object = MibScalar
ccvpStartTime = _CcvpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 4),
    _CcvpStartTime_Type()
)
ccvpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpStartTime.setStatus("current")
_CcvpTimeZoneName_Type = SnmpAdminString
_CcvpTimeZoneName_Object = MibScalar
ccvpTimeZoneName = _CcvpTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 5),
    _CcvpTimeZoneName_Type()
)
ccvpTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTimeZoneName.setStatus("current")


class _CcvpTimeZoneOffsetHours_Type(Integer32):
    """Custom type ccvpTimeZoneOffsetHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_CcvpTimeZoneOffsetHours_Type.__name__ = "Integer32"
_CcvpTimeZoneOffsetHours_Object = MibScalar
ccvpTimeZoneOffsetHours = _CcvpTimeZoneOffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 6),
    _CcvpTimeZoneOffsetHours_Type()
)
ccvpTimeZoneOffsetHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTimeZoneOffsetHours.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTimeZoneOffsetHours.setUnits("hours")


class _CcvpTimeZoneOffsetMinutes_Type(Integer32):
    """Custom type ccvpTimeZoneOffsetMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-59, 59),
    )


_CcvpTimeZoneOffsetMinutes_Type.__name__ = "Integer32"
_CcvpTimeZoneOffsetMinutes_Object = MibScalar
ccvpTimeZoneOffsetMinutes = _CcvpTimeZoneOffsetMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 7),
    _CcvpTimeZoneOffsetMinutes_Type()
)
ccvpTimeZoneOffsetMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTimeZoneOffsetMinutes.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTimeZoneOffsetMinutes.setUnits("minutes")
_CcvpOpsConsoleURL_Type = CiscoURLString
_CcvpOpsConsoleURL_Object = MibScalar
ccvpOpsConsoleURL = _CcvpOpsConsoleURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 8),
    _CcvpOpsConsoleURL_Type()
)
ccvpOpsConsoleURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpOpsConsoleURL.setStatus("current")
_CcvpSupportToolsURL_Type = CiscoURLString
_CcvpSupportToolsURL_Object = MibScalar
ccvpSupportToolsURL = _CcvpSupportToolsURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 9),
    _CcvpSupportToolsURL_Type()
)
ccvpSupportToolsURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSupportToolsURL.setStatus("current")
_CcvpEnableNotifications_Type = TruthValue
_CcvpEnableNotifications_Object = MibScalar
ccvpEnableNotifications = _CcvpEnableNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 1, 10),
    _CcvpEnableNotifications_Type()
)
ccvpEnableNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpEnableNotifications.setStatus("current")
_CcvpLicensingInfo_ObjectIdentity = ObjectIdentity
ccvpLicensingInfo = _CcvpLicensingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2)
)
_CcvpLicRtPortsAvail_Type = Gauge32
_CcvpLicRtPortsAvail_Object = MibScalar
ccvpLicRtPortsAvail = _CcvpLicRtPortsAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 1),
    _CcvpLicRtPortsAvail_Type()
)
ccvpLicRtPortsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicRtPortsAvail.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicRtPortsAvail.setUnits("ports")
_CcvpLicRtPortsInUse_Type = Gauge32
_CcvpLicRtPortsInUse_Object = MibScalar
ccvpLicRtPortsInUse = _CcvpLicRtPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 2),
    _CcvpLicRtPortsInUse_Type()
)
ccvpLicRtPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicRtPortsInUse.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicRtPortsInUse.setUnits("ports")


class _CcvpLicRtPortState_Type(Integer32):
    """Custom type ccvpLicRtPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("failure", 4),
          ("safe", 0),
          ("unknown", 1),
          ("warning", 2))
    )


_CcvpLicRtPortState_Type.__name__ = "Integer32"
_CcvpLicRtPortState_Object = MibScalar
ccvpLicRtPortState = _CcvpLicRtPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 3),
    _CcvpLicRtPortState_Type()
)
ccvpLicRtPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicRtPortState.setStatus("current")
_CcvpLicIntLastUpdate_Type = DateAndTime
_CcvpLicIntLastUpdate_Object = MibScalar
ccvpLicIntLastUpdate = _CcvpLicIntLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 4),
    _CcvpLicIntLastUpdate_Type()
)
ccvpLicIntLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicIntLastUpdate.setStatus("current")


class _CcvpLicIntPeriod_Type(Gauge32):
    """Custom type ccvpLicIntPeriod based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_CcvpLicIntPeriod_Type.__name__ = "Gauge32"
_CcvpLicIntPeriod_Object = MibScalar
ccvpLicIntPeriod = _CcvpLicIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 5),
    _CcvpLicIntPeriod_Type()
)
ccvpLicIntPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicIntPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicIntPeriod.setUnits("minutes")
_CcvpLicIntPortReqs_Type = Gauge32
_CcvpLicIntPortReqs_Object = MibScalar
ccvpLicIntPortReqs = _CcvpLicIntPortReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 6),
    _CcvpLicIntPortReqs_Type()
)
ccvpLicIntPortReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicIntPortReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicIntPortReqs.setUnits("requests")
_CcvpLicIntAvgPortReqs_Type = Gauge32
_CcvpLicIntAvgPortReqs_Object = MibScalar
ccvpLicIntAvgPortReqs = _CcvpLicIntAvgPortReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 7),
    _CcvpLicIntAvgPortReqs_Type()
)
ccvpLicIntAvgPortReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicIntAvgPortReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicIntAvgPortReqs.setUnits("requests")
_CcvpLicIntMaxPortsInUse_Type = Gauge32
_CcvpLicIntMaxPortsInUse_Object = MibScalar
ccvpLicIntMaxPortsInUse = _CcvpLicIntMaxPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 8),
    _CcvpLicIntMaxPortsInUse_Type()
)
ccvpLicIntMaxPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicIntMaxPortsInUse.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicIntMaxPortsInUse.setUnits("ports")
_CcvpLicIntPortReqsDenied_Type = Gauge32
_CcvpLicIntPortReqsDenied_Object = MibScalar
ccvpLicIntPortReqsDenied = _CcvpLicIntPortReqsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 9),
    _CcvpLicIntPortReqsDenied_Type()
)
ccvpLicIntPortReqsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicIntPortReqsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicIntPortReqsDenied.setUnits("requests")
_CcvpLicAggPortReqs_Type = Counter64
_CcvpLicAggPortReqs_Object = MibScalar
ccvpLicAggPortReqs = _CcvpLicAggPortReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 10),
    _CcvpLicAggPortReqs_Type()
)
ccvpLicAggPortReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicAggPortReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicAggPortReqs.setUnits("requests")
_CcvpLicAggAvgPortReqs_Type = Counter64
_CcvpLicAggAvgPortReqs_Object = MibScalar
ccvpLicAggAvgPortReqs = _CcvpLicAggAvgPortReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 11),
    _CcvpLicAggAvgPortReqs_Type()
)
ccvpLicAggAvgPortReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicAggAvgPortReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicAggAvgPortReqs.setUnits("requests")
_CcvpLicAggMaxPortsInUse_Type = Counter64
_CcvpLicAggMaxPortsInUse_Object = MibScalar
ccvpLicAggMaxPortsInUse = _CcvpLicAggMaxPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 12),
    _CcvpLicAggMaxPortsInUse_Type()
)
ccvpLicAggMaxPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicAggMaxPortsInUse.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicAggMaxPortsInUse.setUnits("ports")
_CcvpLicAggPortReqsDenied_Type = Counter64
_CcvpLicAggPortReqsDenied_Object = MibScalar
ccvpLicAggPortReqsDenied = _CcvpLicAggPortReqsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 13),
    _CcvpLicAggPortReqsDenied_Type()
)
ccvpLicAggPortReqsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicAggPortReqsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicAggPortReqsDenied.setUnits("requests")


class _CcvpLicPortUsageWarning_Type(Gauge32):
    """Custom type ccvpLicPortUsageWarning based on Gauge32"""
    defaultValue = 94


_CcvpLicPortUsageWarning_Object = MibScalar
ccvpLicPortUsageWarning = _CcvpLicPortUsageWarning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 14),
    _CcvpLicPortUsageWarning_Type()
)
ccvpLicPortUsageWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicPortUsageWarning.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicPortUsageWarning.setUnits("percent")


class _CcvpLicPortUsageCritical_Type(Gauge32):
    """Custom type ccvpLicPortUsageCritical based on Gauge32"""
    defaultValue = 97


_CcvpLicPortUsageCritical_Object = MibScalar
ccvpLicPortUsageCritical = _CcvpLicPortUsageCritical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 2, 15),
    _CcvpLicPortUsageCritical_Type()
)
ccvpLicPortUsageCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpLicPortUsageCritical.setStatus("current")
if mibBuilder.loadTexts:
    ccvpLicPortUsageCritical.setUnits("percent")
_CcvpThreadPoolInfo_ObjectIdentity = ObjectIdentity
ccvpThreadPoolInfo = _CcvpThreadPoolInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 3)
)
_CcvpTPoolRtIdleThreads_Type = Gauge32
_CcvpTPoolRtIdleThreads_Object = MibScalar
ccvpTPoolRtIdleThreads = _CcvpTPoolRtIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 3, 1),
    _CcvpTPoolRtIdleThreads_Type()
)
ccvpTPoolRtIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTPoolRtIdleThreads.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTPoolRtIdleThreads.setUnits("threads")
_CcvpTPoolRtRunningThreads_Type = Gauge32
_CcvpTPoolRtRunningThreads_Object = MibScalar
ccvpTPoolRtRunningThreads = _CcvpTPoolRtRunningThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 3, 2),
    _CcvpTPoolRtRunningThreads_Type()
)
ccvpTPoolRtRunningThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTPoolRtRunningThreads.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTPoolRtRunningThreads.setUnits("threads")
_CcvpTPoolRtCoreThreads_Type = Gauge32
_CcvpTPoolRtCoreThreads_Object = MibScalar
ccvpTPoolRtCoreThreads = _CcvpTPoolRtCoreThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 3, 3),
    _CcvpTPoolRtCoreThreads_Type()
)
ccvpTPoolRtCoreThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTPoolRtCoreThreads.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTPoolRtCoreThreads.setUnits("threads")
_CcvpTPoolRtMaxThreadsAvail_Type = Gauge32
_CcvpTPoolRtMaxThreadsAvail_Object = MibScalar
ccvpTPoolRtMaxThreadsAvail = _CcvpTPoolRtMaxThreadsAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 3, 4),
    _CcvpTPoolRtMaxThreadsAvail_Type()
)
ccvpTPoolRtMaxThreadsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTPoolRtMaxThreadsAvail.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTPoolRtMaxThreadsAvail.setUnits("threads")
_CcvpTPoolRtMaxThreadsUsed_Type = Gauge32
_CcvpTPoolRtMaxThreadsUsed_Object = MibScalar
ccvpTPoolRtMaxThreadsUsed = _CcvpTPoolRtMaxThreadsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 3, 5),
    _CcvpTPoolRtMaxThreadsUsed_Type()
)
ccvpTPoolRtMaxThreadsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpTPoolRtMaxThreadsUsed.setStatus("current")
if mibBuilder.loadTexts:
    ccvpTPoolRtMaxThreadsUsed.setUnits("threads")
_CcvpJvmInfo_ObjectIdentity = ObjectIdentity
ccvpJvmInfo = _CcvpJvmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4)
)
_CcvpJvmRtMaxMemUsed_Type = Gauge32
_CcvpJvmRtMaxMemUsed_Object = MibScalar
ccvpJvmRtMaxMemUsed = _CcvpJvmRtMaxMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 1),
    _CcvpJvmRtMaxMemUsed_Type()
)
ccvpJvmRtMaxMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtMaxMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtMaxMemUsed.setUnits("bytes")
_CcvpJvmRtCurrMemUsed_Type = Gauge32
_CcvpJvmRtCurrMemUsed_Object = MibScalar
ccvpJvmRtCurrMemUsed = _CcvpJvmRtCurrMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 2),
    _CcvpJvmRtCurrMemUsed_Type()
)
ccvpJvmRtCurrMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtCurrMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtCurrMemUsed.setUnits("bytes")
_CcvpJvmRtMaxMemAvail_Type = Gauge32
_CcvpJvmRtMaxMemAvail_Object = MibScalar
ccvpJvmRtMaxMemAvail = _CcvpJvmRtMaxMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 3),
    _CcvpJvmRtMaxMemAvail_Type()
)
ccvpJvmRtMaxMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtMaxMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtMaxMemAvail.setUnits("bytes")
_CcvpJvmRtCurrMemAvail_Type = Gauge32
_CcvpJvmRtCurrMemAvail_Object = MibScalar
ccvpJvmRtCurrMemAvail = _CcvpJvmRtCurrMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 4),
    _CcvpJvmRtCurrMemAvail_Type()
)
ccvpJvmRtCurrMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtCurrMemAvail.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtCurrMemAvail.setUnits("bytes")
_CcvpJvmRtCurrThreadsInUse_Type = Gauge32
_CcvpJvmRtCurrThreadsInUse_Object = MibScalar
ccvpJvmRtCurrThreadsInUse = _CcvpJvmRtCurrThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 5),
    _CcvpJvmRtCurrThreadsInUse_Type()
)
ccvpJvmRtCurrThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtCurrThreadsInUse.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtCurrThreadsInUse.setUnits("threads")
_CcvpJvmRtMaxThreadsUsed_Type = Gauge32
_CcvpJvmRtMaxThreadsUsed_Object = MibScalar
ccvpJvmRtMaxThreadsUsed = _CcvpJvmRtMaxThreadsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 6),
    _CcvpJvmRtMaxThreadsUsed_Type()
)
ccvpJvmRtMaxThreadsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtMaxThreadsUsed.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtMaxThreadsUsed.setUnits("threads")
_CcvpJvmRtUpTime_Type = Counter64
_CcvpJvmRtUpTime_Object = MibScalar
ccvpJvmRtUpTime = _CcvpJvmRtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 4, 7),
    _CcvpJvmRtUpTime_Type()
)
ccvpJvmRtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpJvmRtUpTime.setStatus("current")
if mibBuilder.loadTexts:
    ccvpJvmRtUpTime.setUnits("milliseconds")
_CcvpServices_ObjectIdentity = ObjectIdentity
ccvpServices = _CcvpServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5)
)
_CcvpServiceTable_Object = MibTable
ccvpServiceTable = _CcvpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ccvpServiceTable.setStatus("current")
_CcvpServiceEntry_Object = MibTableRow
ccvpServiceEntry = _CcvpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1)
)
ccvpServiceEntry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpServiceEntry.setStatus("current")
_CcvpServiceIndex_Type = CcvpIndex
_CcvpServiceIndex_Object = MibTableColumn
ccvpServiceIndex = _CcvpServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1, 1),
    _CcvpServiceIndex_Type()
)
ccvpServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccvpServiceIndex.setStatus("current")
_CcvpServiceType_Type = CcvpServiceType
_CcvpServiceType_Object = MibTableColumn
ccvpServiceType = _CcvpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1, 2),
    _CcvpServiceType_Type()
)
ccvpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpServiceType.setStatus("current")
_CcvpServiceName_Type = SnmpAdminString
_CcvpServiceName_Object = MibTableColumn
ccvpServiceName = _CcvpServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1, 3),
    _CcvpServiceName_Type()
)
ccvpServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpServiceName.setStatus("current")
_CcvpServiceStatus_Type = CcvpServiceStatus
_CcvpServiceStatus_Object = MibTableColumn
ccvpServiceStatus = _CcvpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1, 4),
    _CcvpServiceStatus_Type()
)
ccvpServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpServiceStatus.setStatus("current")
_CcvpServiceIntLastUpdate_Type = DateAndTime
_CcvpServiceIntLastUpdate_Object = MibTableColumn
ccvpServiceIntLastUpdate = _CcvpServiceIntLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1, 5),
    _CcvpServiceIntLastUpdate_Type()
)
ccvpServiceIntLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpServiceIntLastUpdate.setStatus("current")
_CcvpServiceIntPeriod_Type = Gauge32
_CcvpServiceIntPeriod_Object = MibTableColumn
ccvpServiceIntPeriod = _CcvpServiceIntPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 5, 1, 1, 6),
    _CcvpServiceIntPeriod_Type()
)
ccvpServiceIntPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpServiceIntPeriod.setStatus("current")
_CcvpServiceInfo_ObjectIdentity = ObjectIdentity
ccvpServiceInfo = _CcvpServiceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6)
)
_CcvpSipTable_Object = MibTable
ccvpSipTable = _CcvpSipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ccvpSipTable.setStatus("current")
_CcvpSipEntry_Object = MibTableRow
ccvpSipEntry = _CcvpSipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1)
)
ccvpSipEntry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpSipEntry.setStatus("current")
_CcvpSipRtActiveCalls_Type = Gauge32
_CcvpSipRtActiveCalls_Object = MibTableColumn
ccvpSipRtActiveCalls = _CcvpSipRtActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 1),
    _CcvpSipRtActiveCalls_Type()
)
ccvpSipRtActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipRtActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipRtActiveCalls.setUnits("calls")
_CcvpSipRtTotalCallLegs_Type = Gauge32
_CcvpSipRtTotalCallLegs_Object = MibTableColumn
ccvpSipRtTotalCallLegs = _CcvpSipRtTotalCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 2),
    _CcvpSipRtTotalCallLegs_Type()
)
ccvpSipRtTotalCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipRtTotalCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipRtTotalCallLegs.setUnits("call legs")
_CcvpSipIntNewCalls_Type = Gauge32
_CcvpSipIntNewCalls_Object = MibTableColumn
ccvpSipIntNewCalls = _CcvpSipIntNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 3),
    _CcvpSipIntNewCalls_Type()
)
ccvpSipIntNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntNewCalls.setUnits("calls")
_CcvpSipIntConnectsRcv_Type = Gauge32
_CcvpSipIntConnectsRcv_Object = MibTableColumn
ccvpSipIntConnectsRcv = _CcvpSipIntConnectsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 4),
    _CcvpSipIntConnectsRcv_Type()
)
ccvpSipIntConnectsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntConnectsRcv.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntConnectsRcv.setUnits("connects")
_CcvpSipIntAvgLatency1_Type = Gauge32
_CcvpSipIntAvgLatency1_Object = MibTableColumn
ccvpSipIntAvgLatency1 = _CcvpSipIntAvgLatency1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 5),
    _CcvpSipIntAvgLatency1_Type()
)
ccvpSipIntAvgLatency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntAvgLatency1.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntAvgLatency1.setUnits("milliseconds")
_CcvpSipIntAvgLatency2_Type = Gauge32
_CcvpSipIntAvgLatency2_Object = MibTableColumn
ccvpSipIntAvgLatency2 = _CcvpSipIntAvgLatency2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 6),
    _CcvpSipIntAvgLatency2_Type()
)
ccvpSipIntAvgLatency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntAvgLatency2.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntAvgLatency2.setUnits("milliseconds")
_CcvpSipIntFailedXferPre_Type = Gauge32
_CcvpSipIntFailedXferPre_Object = MibTableColumn
ccvpSipIntFailedXferPre = _CcvpSipIntFailedXferPre_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 7),
    _CcvpSipIntFailedXferPre_Type()
)
ccvpSipIntFailedXferPre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntFailedXferPre.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntFailedXferPre.setUnits("transfers")
_CcvpSipIntFailedXferPost_Type = Gauge32
_CcvpSipIntFailedXferPost_Object = MibTableColumn
ccvpSipIntFailedXferPost = _CcvpSipIntFailedXferPost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 8),
    _CcvpSipIntFailedXferPost_Type()
)
ccvpSipIntFailedXferPost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntFailedXferPost.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntFailedXferPost.setUnits("transfers")
_CcvpSipAggNewCalls_Type = Counter64
_CcvpSipAggNewCalls_Object = MibTableColumn
ccvpSipAggNewCalls = _CcvpSipAggNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 9),
    _CcvpSipAggNewCalls_Type()
)
ccvpSipAggNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggNewCalls.setUnits("calls")
_CcvpSipAggConnectsRcv_Type = Counter64
_CcvpSipAggConnectsRcv_Object = MibTableColumn
ccvpSipAggConnectsRcv = _CcvpSipAggConnectsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 10),
    _CcvpSipAggConnectsRcv_Type()
)
ccvpSipAggConnectsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggConnectsRcv.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggConnectsRcv.setUnits("connects")
_CcvpSipAggAvgLatency1_Type = Gauge32
_CcvpSipAggAvgLatency1_Object = MibTableColumn
ccvpSipAggAvgLatency1 = _CcvpSipAggAvgLatency1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 11),
    _CcvpSipAggAvgLatency1_Type()
)
ccvpSipAggAvgLatency1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggAvgLatency1.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggAvgLatency1.setUnits("milliseconds")
_CcvpSipAggAvgLatency2_Type = Gauge32
_CcvpSipAggAvgLatency2_Object = MibTableColumn
ccvpSipAggAvgLatency2 = _CcvpSipAggAvgLatency2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 12),
    _CcvpSipAggAvgLatency2_Type()
)
ccvpSipAggAvgLatency2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggAvgLatency2.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggAvgLatency2.setUnits("milliseconds")
_CcvpSipAggFailedXferPre_Type = Counter64
_CcvpSipAggFailedXferPre_Object = MibTableColumn
ccvpSipAggFailedXferPre = _CcvpSipAggFailedXferPre_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 13),
    _CcvpSipAggFailedXferPre_Type()
)
ccvpSipAggFailedXferPre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggFailedXferPre.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggFailedXferPre.setUnits("transfers")
_CcvpSipAggFailedXferPost_Type = Counter64
_CcvpSipAggFailedXferPost_Object = MibTableColumn
ccvpSipAggFailedXferPost = _CcvpSipAggFailedXferPost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 14),
    _CcvpSipAggFailedXferPost_Type()
)
ccvpSipAggFailedXferPost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggFailedXferPost.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggFailedXferPost.setUnits("transfers")
_CcvpSipRtBasicVideoOffered_Type = Gauge32
_CcvpSipRtBasicVideoOffered_Object = MibTableColumn
ccvpSipRtBasicVideoOffered = _CcvpSipRtBasicVideoOffered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 15),
    _CcvpSipRtBasicVideoOffered_Type()
)
ccvpSipRtBasicVideoOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipRtBasicVideoOffered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipRtBasicVideoOffered.setUnits("calls")
_CcvpSipRtBasicVideoAnswered_Type = Gauge32
_CcvpSipRtBasicVideoAnswered_Object = MibTableColumn
ccvpSipRtBasicVideoAnswered = _CcvpSipRtBasicVideoAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 16),
    _CcvpSipRtBasicVideoAnswered_Type()
)
ccvpSipRtBasicVideoAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipRtBasicVideoAnswered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipRtBasicVideoAnswered.setUnits("calls")
_CcvpSipIntBasicVideoOffered_Type = Gauge32
_CcvpSipIntBasicVideoOffered_Object = MibTableColumn
ccvpSipIntBasicVideoOffered = _CcvpSipIntBasicVideoOffered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 17),
    _CcvpSipIntBasicVideoOffered_Type()
)
ccvpSipIntBasicVideoOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntBasicVideoOffered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntBasicVideoOffered.setUnits("calls")
_CcvpSipIntBasicVideoAnswered_Type = Gauge32
_CcvpSipIntBasicVideoAnswered_Object = MibTableColumn
ccvpSipIntBasicVideoAnswered = _CcvpSipIntBasicVideoAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 18),
    _CcvpSipIntBasicVideoAnswered_Type()
)
ccvpSipIntBasicVideoAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntBasicVideoAnswered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntBasicVideoAnswered.setUnits("calls")
_CcvpSipAggBasicVideoOffered_Type = Counter64
_CcvpSipAggBasicVideoOffered_Object = MibTableColumn
ccvpSipAggBasicVideoOffered = _CcvpSipAggBasicVideoOffered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 19),
    _CcvpSipAggBasicVideoOffered_Type()
)
ccvpSipAggBasicVideoOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggBasicVideoOffered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggBasicVideoOffered.setUnits("calls")
_CcvpSipAggBasicVideoAnswered_Type = Counter64
_CcvpSipAggBasicVideoAnswered_Object = MibTableColumn
ccvpSipAggBasicVideoAnswered = _CcvpSipAggBasicVideoAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 20),
    _CcvpSipAggBasicVideoAnswered_Type()
)
ccvpSipAggBasicVideoAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipAggBasicVideoAnswered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipAggBasicVideoAnswered.setUnits("calls")
_CcvpSipIntPostCallAnswered_Type = Gauge32
_CcvpSipIntPostCallAnswered_Object = MibTableColumn
ccvpSipIntPostCallAnswered = _CcvpSipIntPostCallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 21),
    _CcvpSipIntPostCallAnswered_Type()
)
ccvpSipIntPostCallAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntPostCallAnswered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntPostCallAnswered.setUnits("calls")
_CcvpSipIntWhisperAnswered_Type = Gauge32
_CcvpSipIntWhisperAnswered_Object = MibTableColumn
ccvpSipIntWhisperAnswered = _CcvpSipIntWhisperAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 22),
    _CcvpSipIntWhisperAnswered_Type()
)
ccvpSipIntWhisperAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntWhisperAnswered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntWhisperAnswered.setUnits("calls")
_CcvpSipIntWhisperFailed_Type = Gauge32
_CcvpSipIntWhisperFailed_Object = MibTableColumn
ccvpSipIntWhisperFailed = _CcvpSipIntWhisperFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 23),
    _CcvpSipIntWhisperFailed_Type()
)
ccvpSipIntWhisperFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntWhisperFailed.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntWhisperFailed.setUnits("calls")
_CcvpSipIntGreetingAnswered_Type = Gauge32
_CcvpSipIntGreetingAnswered_Object = MibTableColumn
ccvpSipIntGreetingAnswered = _CcvpSipIntGreetingAnswered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 24),
    _CcvpSipIntGreetingAnswered_Type()
)
ccvpSipIntGreetingAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntGreetingAnswered.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntGreetingAnswered.setUnits("calls")
_CcvpSipIntGreetingFailed_Type = Gauge32
_CcvpSipIntGreetingFailed_Object = MibTableColumn
ccvpSipIntGreetingFailed = _CcvpSipIntGreetingFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 1, 1, 25),
    _CcvpSipIntGreetingFailed_Type()
)
ccvpSipIntGreetingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpSipIntGreetingFailed.setStatus("current")
if mibBuilder.loadTexts:
    ccvpSipIntGreetingFailed.setUnits("calls")
_CcvpH323Table_Object = MibTable
ccvpH323Table = _CcvpH323Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ccvpH323Table.setStatus("current")
_CcvpH323Entry_Object = MibTableRow
ccvpH323Entry = _CcvpH323Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1)
)
ccvpH323Entry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpH323Entry.setStatus("current")
_CcvpH323RtCallsInProgress_Type = Gauge32
_CcvpH323RtCallsInProgress_Object = MibTableColumn
ccvpH323RtCallsInProgress = _CcvpH323RtCallsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 1),
    _CcvpH323RtCallsInProgress_Type()
)
ccvpH323RtCallsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323RtCallsInProgress.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323RtCallsInProgress.setUnits("calls")


class _CcvpH323RtMemoryInUse_Type(Gauge32):
    """Custom type ccvpH323RtMemoryInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcvpH323RtMemoryInUse_Type.__name__ = "Gauge32"
_CcvpH323RtMemoryInUse_Object = MibTableColumn
ccvpH323RtMemoryInUse = _CcvpH323RtMemoryInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 2),
    _CcvpH323RtMemoryInUse_Type()
)
ccvpH323RtMemoryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323RtMemoryInUse.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323RtMemoryInUse.setUnits("percent")
_CcvpH323IntArrivalRate_Type = Gauge32
_CcvpH323IntArrivalRate_Object = MibTableColumn
ccvpH323IntArrivalRate = _CcvpH323IntArrivalRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 3),
    _CcvpH323IntArrivalRate_Type()
)
ccvpH323IntArrivalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntArrivalRate.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntArrivalRate.setUnits("calls per minute")
_CcvpH323IntTransferRate_Type = Gauge32
_CcvpH323IntTransferRate_Object = MibTableColumn
ccvpH323IntTransferRate = _CcvpH323IntTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 4),
    _CcvpH323IntTransferRate_Type()
)
ccvpH323IntTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntTransferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntTransferRate.setUnits("calls per minute")
_CcvpH323IntMaxNewCallLatency_Type = Gauge32
_CcvpH323IntMaxNewCallLatency_Object = MibTableColumn
ccvpH323IntMaxNewCallLatency = _CcvpH323IntMaxNewCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 5),
    _CcvpH323IntMaxNewCallLatency_Type()
)
ccvpH323IntMaxNewCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntMaxNewCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntMaxNewCallLatency.setUnits("milliseconds")
_CcvpH323IntAvgNewCallLatency_Type = Gauge32
_CcvpH323IntAvgNewCallLatency_Object = MibTableColumn
ccvpH323IntAvgNewCallLatency = _CcvpH323IntAvgNewCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 6),
    _CcvpH323IntAvgNewCallLatency_Type()
)
ccvpH323IntAvgNewCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntAvgNewCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntAvgNewCallLatency.setUnits("milliseconds")
_CcvpH323IntMaxXferToAlert_Type = Gauge32
_CcvpH323IntMaxXferToAlert_Object = MibTableColumn
ccvpH323IntMaxXferToAlert = _CcvpH323IntMaxXferToAlert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 7),
    _CcvpH323IntMaxXferToAlert_Type()
)
ccvpH323IntMaxXferToAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntMaxXferToAlert.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntMaxXferToAlert.setUnits("milliseconds")
_CcvpH323IntAvgXferToAlert_Type = Gauge32
_CcvpH323IntAvgXferToAlert_Object = MibTableColumn
ccvpH323IntAvgXferToAlert = _CcvpH323IntAvgXferToAlert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 8),
    _CcvpH323IntAvgXferToAlert_Type()
)
ccvpH323IntAvgXferToAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntAvgXferToAlert.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntAvgXferToAlert.setUnits("milliseconds")
_CcvpH323IntMaxXferToAnswer_Type = Gauge32
_CcvpH323IntMaxXferToAnswer_Object = MibTableColumn
ccvpH323IntMaxXferToAnswer = _CcvpH323IntMaxXferToAnswer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 9),
    _CcvpH323IntMaxXferToAnswer_Type()
)
ccvpH323IntMaxXferToAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntMaxXferToAnswer.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntMaxXferToAnswer.setUnits("milliseconds")
_CcvpH323IntAvgXferToAnswer_Type = Gauge32
_CcvpH323IntAvgXferToAnswer_Object = MibTableColumn
ccvpH323IntAvgXferToAnswer = _CcvpH323IntAvgXferToAnswer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 10),
    _CcvpH323IntAvgXferToAnswer_Type()
)
ccvpH323IntAvgXferToAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntAvgXferToAnswer.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntAvgXferToAnswer.setUnits("milliseconds")
_CcvpH323IntNewCalls_Type = Gauge32
_CcvpH323IntNewCalls_Object = MibTableColumn
ccvpH323IntNewCalls = _CcvpH323IntNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 11),
    _CcvpH323IntNewCalls_Type()
)
ccvpH323IntNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntNewCalls.setUnits("calls")
_CcvpH323IntTransferred_Type = Gauge32
_CcvpH323IntTransferred_Object = MibTableColumn
ccvpH323IntTransferred = _CcvpH323IntTransferred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 12),
    _CcvpH323IntTransferred_Type()
)
ccvpH323IntTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntTransferred.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntTransferred.setUnits("calls")
_CcvpH323IntRedirected_Type = Gauge32
_CcvpH323IntRedirected_Object = MibTableColumn
ccvpH323IntRedirected = _CcvpH323IntRedirected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 13),
    _CcvpH323IntRedirected_Type()
)
ccvpH323IntRedirected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntRedirected.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntRedirected.setUnits("calls")
_CcvpH323IntNotTransferred_Type = Gauge32
_CcvpH323IntNotTransferred_Object = MibTableColumn
ccvpH323IntNotTransferred = _CcvpH323IntNotTransferred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 14),
    _CcvpH323IntNotTransferred_Type()
)
ccvpH323IntNotTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntNotTransferred.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntNotTransferred.setUnits("calls")
_CcvpH323IntPromptsNotFound_Type = Gauge32
_CcvpH323IntPromptsNotFound_Object = MibTableColumn
ccvpH323IntPromptsNotFound = _CcvpH323IntPromptsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 15),
    _CcvpH323IntPromptsNotFound_Type()
)
ccvpH323IntPromptsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntPromptsNotFound.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntPromptsNotFound.setUnits("calls")
_CcvpH323IntCriticalMedia_Type = Gauge32
_CcvpH323IntCriticalMedia_Object = MibTableColumn
ccvpH323IntCriticalMedia = _CcvpH323IntCriticalMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 16),
    _CcvpH323IntCriticalMedia_Type()
)
ccvpH323IntCriticalMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntCriticalMedia.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntCriticalMedia.setUnits("calls")
_CcvpH323IntCallsFinished_Type = Gauge32
_CcvpH323IntCallsFinished_Object = MibTableColumn
ccvpH323IntCallsFinished = _CcvpH323IntCallsFinished_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 17),
    _CcvpH323IntCallsFinished_Type()
)
ccvpH323IntCallsFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntCallsFinished.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntCallsFinished.setUnits("calls")


class _CcvpH323IntMaxCpuUsage_Type(Gauge32):
    """Custom type ccvpH323IntMaxCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcvpH323IntMaxCpuUsage_Type.__name__ = "Gauge32"
_CcvpH323IntMaxCpuUsage_Object = MibTableColumn
ccvpH323IntMaxCpuUsage = _CcvpH323IntMaxCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 18),
    _CcvpH323IntMaxCpuUsage_Type()
)
ccvpH323IntMaxCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntMaxCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntMaxCpuUsage.setUnits("percent")


class _CcvpH323IntAvgCpuUsage_Type(Gauge32):
    """Custom type ccvpH323IntAvgCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcvpH323IntAvgCpuUsage_Type.__name__ = "Gauge32"
_CcvpH323IntAvgCpuUsage_Object = MibTableColumn
ccvpH323IntAvgCpuUsage = _CcvpH323IntAvgCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 2, 1, 19),
    _CcvpH323IntAvgCpuUsage_Type()
)
ccvpH323IntAvgCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpH323IntAvgCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    ccvpH323IntAvgCpuUsage.setUnits("percent")
_CcvpIvrTable_Object = MibTable
ccvpIvrTable = _CcvpIvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ccvpIvrTable.setStatus("current")
_CcvpIvrEntry_Object = MibTableRow
ccvpIvrEntry = _CcvpIvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1)
)
ccvpIvrEntry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpIvrEntry.setStatus("current")
_CcvpIvrRtActiveCalls_Type = Gauge32
_CcvpIvrRtActiveCalls_Object = MibTableColumn
ccvpIvrRtActiveCalls = _CcvpIvrRtActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 1),
    _CcvpIvrRtActiveCalls_Type()
)
ccvpIvrRtActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrRtActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrRtActiveCalls.setUnits("calls")
_CcvpIvrRtActiveHttpReqs_Type = Gauge32
_CcvpIvrRtActiveHttpReqs_Object = MibTableColumn
ccvpIvrRtActiveHttpReqs = _CcvpIvrRtActiveHttpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 2),
    _CcvpIvrRtActiveHttpReqs_Type()
)
ccvpIvrRtActiveHttpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrRtActiveHttpReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrRtActiveHttpReqs.setUnits("requests")
_CcvpIvrIntNewCalls_Type = Gauge32
_CcvpIvrIntNewCalls_Object = MibTableColumn
ccvpIvrIntNewCalls = _CcvpIvrIntNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 3),
    _CcvpIvrIntNewCalls_Type()
)
ccvpIvrIntNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntNewCalls.setUnits("calls")
_CcvpIvrIntMaxActiveCalls_Type = Gauge32
_CcvpIvrIntMaxActiveCalls_Object = MibTableColumn
ccvpIvrIntMaxActiveCalls = _CcvpIvrIntMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 4),
    _CcvpIvrIntMaxActiveCalls_Type()
)
ccvpIvrIntMaxActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxActiveCalls.setUnits("calls")
_CcvpIvrIntCallsFinished_Type = Gauge32
_CcvpIvrIntCallsFinished_Object = MibTableColumn
ccvpIvrIntCallsFinished = _CcvpIvrIntCallsFinished_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 5),
    _CcvpIvrIntCallsFinished_Type()
)
ccvpIvrIntCallsFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntCallsFinished.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntCallsFinished.setUnits("calls")
_CcvpIvrIntAvgCallLatency_Type = Gauge32
_CcvpIvrIntAvgCallLatency_Object = MibTableColumn
ccvpIvrIntAvgCallLatency = _CcvpIvrIntAvgCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 6),
    _CcvpIvrIntAvgCallLatency_Type()
)
ccvpIvrIntAvgCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntAvgCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntAvgCallLatency.setUnits("milliseconds")
_CcvpIvrIntMaxCallLatency_Type = Gauge32
_CcvpIvrIntMaxCallLatency_Object = MibTableColumn
ccvpIvrIntMaxCallLatency = _CcvpIvrIntMaxCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 7),
    _CcvpIvrIntMaxCallLatency_Type()
)
ccvpIvrIntMaxCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxCallLatency.setUnits("milliseconds")
_CcvpIvrIntMinCallLatency_Type = Gauge32
_CcvpIvrIntMinCallLatency_Object = MibTableColumn
ccvpIvrIntMinCallLatency = _CcvpIvrIntMinCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 8),
    _CcvpIvrIntMinCallLatency_Type()
)
ccvpIvrIntMinCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntMinCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntMinCallLatency.setUnits("milliseconds")
_CcvpIvrIntHttpReqs_Type = Gauge32
_CcvpIvrIntHttpReqs_Object = MibTableColumn
ccvpIvrIntHttpReqs = _CcvpIvrIntHttpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 9),
    _CcvpIvrIntHttpReqs_Type()
)
ccvpIvrIntHttpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntHttpReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntHttpReqs.setUnits("requests")
_CcvpIvrIntMaxActiveHttpReqs_Type = Gauge32
_CcvpIvrIntMaxActiveHttpReqs_Object = MibTableColumn
ccvpIvrIntMaxActiveHttpReqs = _CcvpIvrIntMaxActiveHttpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 10),
    _CcvpIvrIntMaxActiveHttpReqs_Type()
)
ccvpIvrIntMaxActiveHttpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxActiveHttpReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxActiveHttpReqs.setUnits("requests")
_CcvpIvrIntMaxHttpReqRate_Type = Gauge32
_CcvpIvrIntMaxHttpReqRate_Object = MibTableColumn
ccvpIvrIntMaxHttpReqRate = _CcvpIvrIntMaxHttpReqRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 11),
    _CcvpIvrIntMaxHttpReqRate_Type()
)
ccvpIvrIntMaxHttpReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxHttpReqRate.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxHttpReqRate.setUnits("requests per second")
_CcvpIvrIntAvgHttpReqRate_Type = Gauge32
_CcvpIvrIntAvgHttpReqRate_Object = MibTableColumn
ccvpIvrIntAvgHttpReqRate = _CcvpIvrIntAvgHttpReqRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 12),
    _CcvpIvrIntAvgHttpReqRate_Type()
)
ccvpIvrIntAvgHttpReqRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntAvgHttpReqRate.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntAvgHttpReqRate.setUnits("requests per second")
_CcvpIvrAggNewCalls_Type = Counter64
_CcvpIvrAggNewCalls_Object = MibTableColumn
ccvpIvrAggNewCalls = _CcvpIvrAggNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 13),
    _CcvpIvrAggNewCalls_Type()
)
ccvpIvrAggNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggNewCalls.setUnits("calls")
_CcvpIvrAggMaxActiveCalls_Type = Counter32
_CcvpIvrAggMaxActiveCalls_Object = MibTableColumn
ccvpIvrAggMaxActiveCalls = _CcvpIvrAggMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 14),
    _CcvpIvrAggMaxActiveCalls_Type()
)
ccvpIvrAggMaxActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggMaxActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggMaxActiveCalls.setUnits("calls")
_CcvpIvrAggHttpReqs_Type = Counter64
_CcvpIvrAggHttpReqs_Object = MibTableColumn
ccvpIvrAggHttpReqs = _CcvpIvrAggHttpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 15),
    _CcvpIvrAggHttpReqs_Type()
)
ccvpIvrAggHttpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggHttpReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggHttpReqs.setUnits("requests")
_CcvpIvrAggMaxHttpReqs_Type = Counter32
_CcvpIvrAggMaxHttpReqs_Object = MibTableColumn
ccvpIvrAggMaxHttpReqs = _CcvpIvrAggMaxHttpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 16),
    _CcvpIvrAggMaxHttpReqs_Type()
)
ccvpIvrAggMaxHttpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggMaxHttpReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggMaxHttpReqs.setUnits("requests")
_CcvpIvrRtFullVideoCalls_Type = Gauge32
_CcvpIvrRtFullVideoCalls_Object = MibTableColumn
ccvpIvrRtFullVideoCalls = _CcvpIvrRtFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 17),
    _CcvpIvrRtFullVideoCalls_Type()
)
ccvpIvrRtFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrRtFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrRtFullVideoCalls.setUnits("calls")
_CcvpIvrIntFullVideoCalls_Type = Gauge32
_CcvpIvrIntFullVideoCalls_Object = MibTableColumn
ccvpIvrIntFullVideoCalls = _CcvpIvrIntFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 18),
    _CcvpIvrIntFullVideoCalls_Type()
)
ccvpIvrIntFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntFullVideoCalls.setUnits("calls")
_CcvpIvrAggFullVideoCalls_Type = Gauge32
_CcvpIvrAggFullVideoCalls_Object = MibTableColumn
ccvpIvrAggFullVideoCalls = _CcvpIvrAggFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 19),
    _CcvpIvrAggFullVideoCalls_Type()
)
ccvpIvrAggFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggFullVideoCalls.setUnits("calls")
_CcvpIvrIntMaxFullVideoCalls_Type = Gauge32
_CcvpIvrIntMaxFullVideoCalls_Object = MibTableColumn
ccvpIvrIntMaxFullVideoCalls = _CcvpIvrIntMaxFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 20),
    _CcvpIvrIntMaxFullVideoCalls_Type()
)
ccvpIvrIntMaxFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrIntMaxFullVideoCalls.setUnits("calls")
_CcvpIvrAggMaxFullVideoCalls_Type = Counter64
_CcvpIvrAggMaxFullVideoCalls_Object = MibTableColumn
ccvpIvrAggMaxFullVideoCalls = _CcvpIvrAggMaxFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 21),
    _CcvpIvrAggMaxFullVideoCalls_Type()
)
ccvpIvrAggMaxFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggMaxFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggMaxFullVideoCalls.setUnits("calls")
_CcvpIvrAggAgentPushedVideo_Type = Counter64
_CcvpIvrAggAgentPushedVideo_Object = MibTableColumn
ccvpIvrAggAgentPushedVideo = _CcvpIvrAggAgentPushedVideo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 22),
    _CcvpIvrAggAgentPushedVideo_Type()
)
ccvpIvrAggAgentPushedVideo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggAgentPushedVideo.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggAgentPushedVideo.setUnits("requests")
_CcvpIvrAggAgentInitiatedRecordings_Type = Counter64
_CcvpIvrAggAgentInitiatedRecordings_Object = MibTableColumn
ccvpIvrAggAgentInitiatedRecordings = _CcvpIvrAggAgentInitiatedRecordings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 23),
    _CcvpIvrAggAgentInitiatedRecordings_Type()
)
ccvpIvrAggAgentInitiatedRecordings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggAgentInitiatedRecordings.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggAgentInitiatedRecordings.setUnits("requests")
_CcvpIvrAggAgentVCRControlInvocations_Type = Counter64
_CcvpIvrAggAgentVCRControlInvocations_Object = MibTableColumn
ccvpIvrAggAgentVCRControlInvocations = _CcvpIvrAggAgentVCRControlInvocations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 3, 1, 24),
    _CcvpIvrAggAgentVCRControlInvocations_Type()
)
ccvpIvrAggAgentVCRControlInvocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIvrAggAgentVCRControlInvocations.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIvrAggAgentVCRControlInvocations.setUnits("requests")
_CcvpIcmTable_Object = MibTable
ccvpIcmTable = _CcvpIcmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4)
)
if mibBuilder.loadTexts:
    ccvpIcmTable.setStatus("current")
_CcvpIcmEntry_Object = MibTableRow
ccvpIcmEntry = _CcvpIcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1)
)
ccvpIcmEntry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpIcmEntry.setStatus("current")
_CcvpIcmRtActiveCalls_Type = Gauge32
_CcvpIcmRtActiveCalls_Object = MibTableColumn
ccvpIcmRtActiveCalls = _CcvpIcmRtActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 1),
    _CcvpIcmRtActiveCalls_Type()
)
ccvpIcmRtActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveCalls.setUnits("calls")
_CcvpIcmRtActiveSIPCallLegs_Type = Gauge32
_CcvpIcmRtActiveSIPCallLegs_Object = MibTableColumn
ccvpIcmRtActiveSIPCallLegs = _CcvpIcmRtActiveSIPCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 2),
    _CcvpIcmRtActiveSIPCallLegs_Type()
)
ccvpIcmRtActiveSIPCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveSIPCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveSIPCallLegs.setUnits("call legs")
_CcvpIcmRtActiveH323CallLegs_Type = Gauge32
_CcvpIcmRtActiveH323CallLegs_Object = MibTableColumn
ccvpIcmRtActiveH323CallLegs = _CcvpIcmRtActiveH323CallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 3),
    _CcvpIcmRtActiveH323CallLegs_Type()
)
ccvpIcmRtActiveH323CallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveH323CallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveH323CallLegs.setUnits("call legs")
_CcvpIcmRtActiveVRUCallLegs_Type = Gauge32
_CcvpIcmRtActiveVRUCallLegs_Object = MibTableColumn
ccvpIcmRtActiveVRUCallLegs = _CcvpIcmRtActiveVRUCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 4),
    _CcvpIcmRtActiveVRUCallLegs_Type()
)
ccvpIcmRtActiveVRUCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveVRUCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveVRUCallLegs.setUnits("call legs")
_CcvpIcmRtActiveICMLookupReqs_Type = Gauge32
_CcvpIcmRtActiveICMLookupReqs_Object = MibTableColumn
ccvpIcmRtActiveICMLookupReqs = _CcvpIcmRtActiveICMLookupReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 5),
    _CcvpIcmRtActiveICMLookupReqs_Type()
)
ccvpIcmRtActiveICMLookupReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveICMLookupReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtActiveICMLookupReqs.setUnits("requests")
_CcvpIcmIntNewCalls_Type = Gauge32
_CcvpIcmIntNewCalls_Object = MibTableColumn
ccvpIcmIntNewCalls = _CcvpIcmIntNewCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 6),
    _CcvpIcmIntNewCalls_Type()
)
ccvpIcmIntNewCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntNewCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntNewCalls.setUnits("calls")
_CcvpIcmIntSipCallLegs_Type = Gauge32
_CcvpIcmIntSipCallLegs_Object = MibTableColumn
ccvpIcmIntSipCallLegs = _CcvpIcmIntSipCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 7),
    _CcvpIcmIntSipCallLegs_Type()
)
ccvpIcmIntSipCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntSipCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntSipCallLegs.setUnits("call legs")
_CcvpIcmIntH323CallLegs_Type = Gauge32
_CcvpIcmIntH323CallLegs_Object = MibTableColumn
ccvpIcmIntH323CallLegs = _CcvpIcmIntH323CallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 8),
    _CcvpIcmIntH323CallLegs_Type()
)
ccvpIcmIntH323CallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntH323CallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntH323CallLegs.setUnits("call legs")
_CcvpIcmIntVruCallLegs_Type = Gauge32
_CcvpIcmIntVruCallLegs_Object = MibTableColumn
ccvpIcmIntVruCallLegs = _CcvpIcmIntVruCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 9),
    _CcvpIcmIntVruCallLegs_Type()
)
ccvpIcmIntVruCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntVruCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntVruCallLegs.setUnits("call legs")
_CcvpIcmIntIcmLookupReqs_Type = Gauge32
_CcvpIcmIntIcmLookupReqs_Object = MibTableColumn
ccvpIcmIntIcmLookupReqs = _CcvpIcmIntIcmLookupReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 10),
    _CcvpIcmIntIcmLookupReqs_Type()
)
ccvpIcmIntIcmLookupReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntIcmLookupReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntIcmLookupReqs.setUnits("requests")
_CcvpIcmAggCalls_Type = Counter64
_CcvpIcmAggCalls_Object = MibTableColumn
ccvpIcmAggCalls = _CcvpIcmAggCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 11),
    _CcvpIcmAggCalls_Type()
)
ccvpIcmAggCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggCalls.setUnits("calls")
_CcvpIcmAggSipCallLegs_Type = Counter64
_CcvpIcmAggSipCallLegs_Object = MibTableColumn
ccvpIcmAggSipCallLegs = _CcvpIcmAggSipCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 12),
    _CcvpIcmAggSipCallLegs_Type()
)
ccvpIcmAggSipCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggSipCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggSipCallLegs.setUnits("call legs")
_CcvpIcmAggH323CallLegs_Type = Counter64
_CcvpIcmAggH323CallLegs_Object = MibTableColumn
ccvpIcmAggH323CallLegs = _CcvpIcmAggH323CallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 13),
    _CcvpIcmAggH323CallLegs_Type()
)
ccvpIcmAggH323CallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggH323CallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggH323CallLegs.setUnits("call legs")
_CcvpIcmAggVruCallLegs_Type = Counter64
_CcvpIcmAggVruCallLegs_Object = MibTableColumn
ccvpIcmAggVruCallLegs = _CcvpIcmAggVruCallLegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 14),
    _CcvpIcmAggVruCallLegs_Type()
)
ccvpIcmAggVruCallLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggVruCallLegs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggVruCallLegs.setUnits("call legs")
_CcvpIcmAggIcmLookupReqs_Type = Counter64
_CcvpIcmAggIcmLookupReqs_Object = MibTableColumn
ccvpIcmAggIcmLookupReqs = _CcvpIcmAggIcmLookupReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 15),
    _CcvpIcmAggIcmLookupReqs_Type()
)
ccvpIcmAggIcmLookupReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggIcmLookupReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggIcmLookupReqs.setUnits("requests")
_CcvpIcmRtFullVideoCalls_Type = Gauge32
_CcvpIcmRtFullVideoCalls_Object = MibTableColumn
ccvpIcmRtFullVideoCalls = _CcvpIcmRtFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 16),
    _CcvpIcmRtFullVideoCalls_Type()
)
ccvpIcmRtFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtFullVideoCalls.setUnits("calls")
_CcvpIcmRtOfferedBasicVideoCalls_Type = Gauge32
_CcvpIcmRtOfferedBasicVideoCalls_Object = MibTableColumn
ccvpIcmRtOfferedBasicVideoCalls = _CcvpIcmRtOfferedBasicVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 17),
    _CcvpIcmRtOfferedBasicVideoCalls_Type()
)
ccvpIcmRtOfferedBasicVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtOfferedBasicVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtOfferedBasicVideoCalls.setUnits("calls")
_CcvpIcmRtAcceptedBasicVideoCalls_Type = Gauge32
_CcvpIcmRtAcceptedBasicVideoCalls_Object = MibTableColumn
ccvpIcmRtAcceptedBasicVideoCalls = _CcvpIcmRtAcceptedBasicVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 18),
    _CcvpIcmRtAcceptedBasicVideoCalls_Type()
)
ccvpIcmRtAcceptedBasicVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmRtAcceptedBasicVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmRtAcceptedBasicVideoCalls.setUnits("calls")
_CcvpIcmIntFullVideoCalls_Type = Gauge32
_CcvpIcmIntFullVideoCalls_Object = MibTableColumn
ccvpIcmIntFullVideoCalls = _CcvpIcmIntFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 19),
    _CcvpIcmIntFullVideoCalls_Type()
)
ccvpIcmIntFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntFullVideoCalls.setUnits("calls")
_CcvpIcmIntOfferedBasicVideoCalls_Type = Gauge32
_CcvpIcmIntOfferedBasicVideoCalls_Object = MibTableColumn
ccvpIcmIntOfferedBasicVideoCalls = _CcvpIcmIntOfferedBasicVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 20),
    _CcvpIcmIntOfferedBasicVideoCalls_Type()
)
ccvpIcmIntOfferedBasicVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntOfferedBasicVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntOfferedBasicVideoCalls.setUnits("calls")
_CcvpIcmIntAcceptedBasicVideoCalls_Type = Gauge32
_CcvpIcmIntAcceptedBasicVideoCalls_Object = MibTableColumn
ccvpIcmIntAcceptedBasicVideoCalls = _CcvpIcmIntAcceptedBasicVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 21),
    _CcvpIcmIntAcceptedBasicVideoCalls_Type()
)
ccvpIcmIntAcceptedBasicVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmIntAcceptedBasicVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmIntAcceptedBasicVideoCalls.setUnits("calls")
_CcvpIcmAggFullVideoCalls_Type = Counter64
_CcvpIcmAggFullVideoCalls_Object = MibTableColumn
ccvpIcmAggFullVideoCalls = _CcvpIcmAggFullVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 22),
    _CcvpIcmAggFullVideoCalls_Type()
)
ccvpIcmAggFullVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggFullVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggFullVideoCalls.setUnits("calls")
_CcvpIcmAggOfferedBasicVideoCalls_Type = Counter64
_CcvpIcmAggOfferedBasicVideoCalls_Object = MibTableColumn
ccvpIcmAggOfferedBasicVideoCalls = _CcvpIcmAggOfferedBasicVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 23),
    _CcvpIcmAggOfferedBasicVideoCalls_Type()
)
ccvpIcmAggOfferedBasicVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggOfferedBasicVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggOfferedBasicVideoCalls.setUnits("calls")
_CcvpIcmAggAcceptedBasicVideoCalls_Type = Counter64
_CcvpIcmAggAcceptedBasicVideoCalls_Object = MibTableColumn
ccvpIcmAggAcceptedBasicVideoCalls = _CcvpIcmAggAcceptedBasicVideoCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 4, 1, 24),
    _CcvpIcmAggAcceptedBasicVideoCalls_Type()
)
ccvpIcmAggAcceptedBasicVideoCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpIcmAggAcceptedBasicVideoCalls.setStatus("current")
if mibBuilder.loadTexts:
    ccvpIcmAggAcceptedBasicVideoCalls.setUnits("calls")
_CcvpReptTable_Object = MibTable
ccvpReptTable = _CcvpReptTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5)
)
if mibBuilder.loadTexts:
    ccvpReptTable.setStatus("current")
_CcvpReptEntry_Object = MibTableRow
ccvpReptEntry = _CcvpReptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1)
)
ccvpReptEntry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpReptEntry.setStatus("current")
_CcvpReptIntVxmlEvents_Type = Gauge32
_CcvpReptIntVxmlEvents_Object = MibTableColumn
ccvpReptIntVxmlEvents = _CcvpReptIntVxmlEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 1),
    _CcvpReptIntVxmlEvents_Type()
)
ccvpReptIntVxmlEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptIntVxmlEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptIntVxmlEvents.setUnits("events")
_CcvpReptIntSipEvents_Type = Gauge32
_CcvpReptIntSipEvents_Object = MibTableColumn
ccvpReptIntSipEvents = _CcvpReptIntSipEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 2),
    _CcvpReptIntSipEvents_Type()
)
ccvpReptIntSipEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptIntSipEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptIntSipEvents.setUnits("events")
_CcvpReptIntIvrEvents_Type = Gauge32
_CcvpReptIntIvrEvents_Object = MibTableColumn
ccvpReptIntIvrEvents = _CcvpReptIntIvrEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 3),
    _CcvpReptIntIvrEvents_Type()
)
ccvpReptIntIvrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptIntIvrEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptIntIvrEvents.setUnits("events")
_CcvpReptIntDatabaseWrites_Type = Gauge32
_CcvpReptIntDatabaseWrites_Object = MibTableColumn
ccvpReptIntDatabaseWrites = _CcvpReptIntDatabaseWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 4),
    _CcvpReptIntDatabaseWrites_Type()
)
ccvpReptIntDatabaseWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptIntDatabaseWrites.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptIntDatabaseWrites.setUnits("writes")
_CcvpReptAggVxmlEvents_Type = Counter64
_CcvpReptAggVxmlEvents_Object = MibTableColumn
ccvpReptAggVxmlEvents = _CcvpReptAggVxmlEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 5),
    _CcvpReptAggVxmlEvents_Type()
)
ccvpReptAggVxmlEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptAggVxmlEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptAggVxmlEvents.setUnits("events")
_CcvpReptAggSipEvents_Type = Counter64
_CcvpReptAggSipEvents_Object = MibTableColumn
ccvpReptAggSipEvents = _CcvpReptAggSipEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 6),
    _CcvpReptAggSipEvents_Type()
)
ccvpReptAggSipEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptAggSipEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptAggSipEvents.setUnits("events")
_CcvpReptAggIvrEvents_Type = Counter64
_CcvpReptAggIvrEvents_Object = MibTableColumn
ccvpReptAggIvrEvents = _CcvpReptAggIvrEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 7),
    _CcvpReptAggIvrEvents_Type()
)
ccvpReptAggIvrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptAggIvrEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptAggIvrEvents.setUnits("events")
_CcvpReptAggDatabaseWrites_Type = Counter64
_CcvpReptAggDatabaseWrites_Object = MibTableColumn
ccvpReptAggDatabaseWrites = _CcvpReptAggDatabaseWrites_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 5, 1, 8),
    _CcvpReptAggDatabaseWrites_Type()
)
ccvpReptAggDatabaseWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpReptAggDatabaseWrites.setStatus("current")
if mibBuilder.loadTexts:
    ccvpReptAggDatabaseWrites.setUnits("writes")
_CcvpVxmlTable_Object = MibTable
ccvpVxmlTable = _CcvpVxmlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6)
)
if mibBuilder.loadTexts:
    ccvpVxmlTable.setStatus("current")
_CcvpVxmlEntry_Object = MibTableRow
ccvpVxmlEntry = _CcvpVxmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1)
)
ccvpVxmlEntry.setIndexNames(
    (0, "CISCO-CVP-MIB", "ccvpServiceIndex"),
)
if mibBuilder.loadTexts:
    ccvpVxmlEntry.setStatus("current")
_CcvpVxmlRtActiveSessions_Type = Gauge32
_CcvpVxmlRtActiveSessions_Object = MibTableColumn
ccvpVxmlRtActiveSessions = _CcvpVxmlRtActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 1),
    _CcvpVxmlRtActiveSessions_Type()
)
ccvpVxmlRtActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlRtActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlRtActiveSessions.setUnits("sessions")
_CcvpVxmlRtActiveIcmLookups_Type = Gauge32
_CcvpVxmlRtActiveIcmLookups_Object = MibTableColumn
ccvpVxmlRtActiveIcmLookups = _CcvpVxmlRtActiveIcmLookups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 2),
    _CcvpVxmlRtActiveIcmLookups_Type()
)
ccvpVxmlRtActiveIcmLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlRtActiveIcmLookups.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlRtActiveIcmLookups.setUnits("requests")
_CcvpVxmlIntSessions_Type = Gauge32
_CcvpVxmlIntSessions_Object = MibTableColumn
ccvpVxmlIntSessions = _CcvpVxmlIntSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 3),
    _CcvpVxmlIntSessions_Type()
)
ccvpVxmlIntSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlIntSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlIntSessions.setUnits("sessions")
_CcvpVxmlIntReptEvents_Type = Gauge32
_CcvpVxmlIntReptEvents_Object = MibTableColumn
ccvpVxmlIntReptEvents = _CcvpVxmlIntReptEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 4),
    _CcvpVxmlIntReptEvents_Type()
)
ccvpVxmlIntReptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlIntReptEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlIntReptEvents.setUnits("events")
_CcvpVxmlIntIcmLookupReqs_Type = Gauge32
_CcvpVxmlIntIcmLookupReqs_Object = MibTableColumn
ccvpVxmlIntIcmLookupReqs = _CcvpVxmlIntIcmLookupReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 5),
    _CcvpVxmlIntIcmLookupReqs_Type()
)
ccvpVxmlIntIcmLookupReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupReqs.setUnits("requests")
_CcvpVxmlIntIcmLookupResp_Type = Gauge32
_CcvpVxmlIntIcmLookupResp_Object = MibTableColumn
ccvpVxmlIntIcmLookupResp = _CcvpVxmlIntIcmLookupResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 6),
    _CcvpVxmlIntIcmLookupResp_Type()
)
ccvpVxmlIntIcmLookupResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupResp.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupResp.setUnits("responses")
_CcvpVxmlIntIcmLookupSuccess_Type = Gauge32
_CcvpVxmlIntIcmLookupSuccess_Object = MibTableColumn
ccvpVxmlIntIcmLookupSuccess = _CcvpVxmlIntIcmLookupSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 7),
    _CcvpVxmlIntIcmLookupSuccess_Type()
)
ccvpVxmlIntIcmLookupSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupSuccess.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupSuccess.setUnits("requests")
_CcvpVxmlIntIcmLookupFails_Type = Gauge32
_CcvpVxmlIntIcmLookupFails_Object = MibTableColumn
ccvpVxmlIntIcmLookupFails = _CcvpVxmlIntIcmLookupFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 8),
    _CcvpVxmlIntIcmLookupFails_Type()
)
ccvpVxmlIntIcmLookupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupFails.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlIntIcmLookupFails.setUnits("requests")
_CcvpVxmlAggSessions_Type = Counter64
_CcvpVxmlAggSessions_Object = MibTableColumn
ccvpVxmlAggSessions = _CcvpVxmlAggSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 9),
    _CcvpVxmlAggSessions_Type()
)
ccvpVxmlAggSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlAggSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlAggSessions.setUnits("sessions")
_CcvpVxmlAggReptEvents_Type = Counter64
_CcvpVxmlAggReptEvents_Object = MibTableColumn
ccvpVxmlAggReptEvents = _CcvpVxmlAggReptEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 10),
    _CcvpVxmlAggReptEvents_Type()
)
ccvpVxmlAggReptEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlAggReptEvents.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlAggReptEvents.setUnits("events")
_CcvpVxmlAggIcmLookupReqs_Type = Counter64
_CcvpVxmlAggIcmLookupReqs_Object = MibTableColumn
ccvpVxmlAggIcmLookupReqs = _CcvpVxmlAggIcmLookupReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 11),
    _CcvpVxmlAggIcmLookupReqs_Type()
)
ccvpVxmlAggIcmLookupReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupReqs.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupReqs.setUnits("requests")
_CcvpVxmlAggIcmLookupResp_Type = Counter64
_CcvpVxmlAggIcmLookupResp_Object = MibTableColumn
ccvpVxmlAggIcmLookupResp = _CcvpVxmlAggIcmLookupResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 12),
    _CcvpVxmlAggIcmLookupResp_Type()
)
ccvpVxmlAggIcmLookupResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupResp.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupResp.setUnits("responses")
_CcvpVxmlAggIcmLookupSuccess_Type = Counter64
_CcvpVxmlAggIcmLookupSuccess_Object = MibTableColumn
ccvpVxmlAggIcmLookupSuccess = _CcvpVxmlAggIcmLookupSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 13),
    _CcvpVxmlAggIcmLookupSuccess_Type()
)
ccvpVxmlAggIcmLookupSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupSuccess.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupSuccess.setUnits("requests")
_CcvpVxmlAggIcmLookupFails_Type = Counter64
_CcvpVxmlAggIcmLookupFails_Object = MibTableColumn
ccvpVxmlAggIcmLookupFails = _CcvpVxmlAggIcmLookupFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 6, 6, 1, 14),
    _CcvpVxmlAggIcmLookupFails_Type()
)
ccvpVxmlAggIcmLookupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupFails.setStatus("current")
if mibBuilder.loadTexts:
    ccvpVxmlAggIcmLookupFails.setUnits("requests")
_CcvpNotificationInfo_ObjectIdentity = ObjectIdentity
ccvpNotificationInfo = _CcvpNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7)
)
_CcvpEventMessageId_Type = Unsigned32
_CcvpEventMessageId_Object = MibScalar
ccvpEventMessageId = _CcvpEventMessageId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 1),
    _CcvpEventMessageId_Type()
)
ccvpEventMessageId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventMessageId.setStatus("current")
_CcvpEventHostName_Type = SnmpAdminString
_CcvpEventHostName_Object = MibScalar
ccvpEventHostName = _CcvpEventHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 2),
    _CcvpEventHostName_Type()
)
ccvpEventHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventHostName.setStatus("current")
_CcvpEventAppName_Type = SnmpAdminString
_CcvpEventAppName_Object = MibScalar
ccvpEventAppName = _CcvpEventAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 3),
    _CcvpEventAppName_Type()
)
ccvpEventAppName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventAppName.setStatus("current")
_CcvpEventMessageName_Type = SnmpAdminString
_CcvpEventMessageName_Object = MibScalar
ccvpEventMessageName = _CcvpEventMessageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 4),
    _CcvpEventMessageName_Type()
)
ccvpEventMessageName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventMessageName.setStatus("current")


class _CcvpEventState_Type(Integer32):
    """Custom type ccvpEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("raise", 1))
    )


_CcvpEventState_Type.__name__ = "Integer32"
_CcvpEventState_Object = MibScalar
ccvpEventState = _CcvpEventState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 5),
    _CcvpEventState_Type()
)
ccvpEventState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventState.setStatus("current")


class _CcvpEventSeverity_Type(Integer32):
    """Custom type ccvpEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("informational", 6),
          ("notice", 5),
          ("warning", 4))
    )


_CcvpEventSeverity_Type.__name__ = "Integer32"
_CcvpEventSeverity_Object = MibScalar
ccvpEventSeverity = _CcvpEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 6),
    _CcvpEventSeverity_Type()
)
ccvpEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventSeverity.setStatus("current")
_CcvpEventTimestamp_Type = DateAndTime
_CcvpEventTimestamp_Object = MibScalar
ccvpEventTimestamp = _CcvpEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 7),
    _CcvpEventTimestamp_Type()
)
ccvpEventTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventTimestamp.setStatus("current")
_CcvpEventText_Type = SnmpAdminString
_CcvpEventText_Object = MibScalar
ccvpEventText = _CcvpEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 1, 7, 8),
    _CcvpEventText_Type()
)
ccvpEventText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccvpEventText.setStatus("current")
_CiscoCvpMIBConform_ObjectIdentity = ObjectIdentity
ciscoCvpMIBConform = _CiscoCvpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2)
)
_CiscoCvpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCvpMIBCompliances = _CiscoCvpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 1)
)
_CiscoCvpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCvpMIBGroups = _CiscoCvpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2)
)

# Managed Objects groups

ccvpGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 1)
)
ccvpGeneralInfoGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpServerName"),
        ("CISCO-CVP-MIB", "ccvpDescription"),
        ("CISCO-CVP-MIB", "ccvpVersion"),
        ("CISCO-CVP-MIB", "ccvpStartTime"),
        ("CISCO-CVP-MIB", "ccvpTimeZoneName"),
        ("CISCO-CVP-MIB", "ccvpTimeZoneOffsetHours"),
        ("CISCO-CVP-MIB", "ccvpTimeZoneOffsetMinutes"),
        ("CISCO-CVP-MIB", "ccvpOpsConsoleURL"),
        ("CISCO-CVP-MIB", "ccvpSupportToolsURL"),
        ("CISCO-CVP-MIB", "ccvpEnableNotifications"))
)
if mibBuilder.loadTexts:
    ccvpGeneralInfoGroup.setStatus("current")

ccvpLicensingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 2)
)
ccvpLicensingInfoGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpLicRtPortsAvail"),
        ("CISCO-CVP-MIB", "ccvpLicRtPortsInUse"),
        ("CISCO-CVP-MIB", "ccvpLicRtPortState"),
        ("CISCO-CVP-MIB", "ccvpLicIntLastUpdate"),
        ("CISCO-CVP-MIB", "ccvpLicIntPeriod"),
        ("CISCO-CVP-MIB", "ccvpLicIntPortReqs"),
        ("CISCO-CVP-MIB", "ccvpLicIntAvgPortReqs"),
        ("CISCO-CVP-MIB", "ccvpLicIntMaxPortsInUse"),
        ("CISCO-CVP-MIB", "ccvpLicIntPortReqsDenied"),
        ("CISCO-CVP-MIB", "ccvpLicAggPortReqs"),
        ("CISCO-CVP-MIB", "ccvpLicAggAvgPortReqs"),
        ("CISCO-CVP-MIB", "ccvpLicAggMaxPortsInUse"),
        ("CISCO-CVP-MIB", "ccvpLicAggPortReqsDenied"),
        ("CISCO-CVP-MIB", "ccvpLicPortUsageWarning"),
        ("CISCO-CVP-MIB", "ccvpLicPortUsageCritical"))
)
if mibBuilder.loadTexts:
    ccvpLicensingInfoGroup.setStatus("current")

ccvpThreadPoolInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 3)
)
ccvpThreadPoolInfoGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpTPoolRtIdleThreads"),
        ("CISCO-CVP-MIB", "ccvpTPoolRtRunningThreads"),
        ("CISCO-CVP-MIB", "ccvpTPoolRtCoreThreads"),
        ("CISCO-CVP-MIB", "ccvpTPoolRtMaxThreadsAvail"),
        ("CISCO-CVP-MIB", "ccvpTPoolRtMaxThreadsUsed"))
)
if mibBuilder.loadTexts:
    ccvpThreadPoolInfoGroup.setStatus("current")

ccvpJvmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 4)
)
ccvpJvmInfoGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpJvmRtMaxMemUsed"),
        ("CISCO-CVP-MIB", "ccvpJvmRtCurrMemUsed"),
        ("CISCO-CVP-MIB", "ccvpJvmRtMaxMemAvail"),
        ("CISCO-CVP-MIB", "ccvpJvmRtCurrMemAvail"),
        ("CISCO-CVP-MIB", "ccvpJvmRtCurrThreadsInUse"),
        ("CISCO-CVP-MIB", "ccvpJvmRtMaxThreadsUsed"),
        ("CISCO-CVP-MIB", "ccvpJvmRtUpTime"))
)
if mibBuilder.loadTexts:
    ccvpJvmInfoGroup.setStatus("current")

ccvpServiceTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 5)
)
ccvpServiceTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpServiceType"),
        ("CISCO-CVP-MIB", "ccvpServiceName"),
        ("CISCO-CVP-MIB", "ccvpServiceStatus"),
        ("CISCO-CVP-MIB", "ccvpServiceIntLastUpdate"),
        ("CISCO-CVP-MIB", "ccvpServiceIntPeriod"))
)
if mibBuilder.loadTexts:
    ccvpServiceTableGroup.setStatus("current")

ccvpSipTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 6)
)
ccvpSipTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpSipRtActiveCalls"),
        ("CISCO-CVP-MIB", "ccvpSipRtTotalCallLegs"),
        ("CISCO-CVP-MIB", "ccvpSipIntNewCalls"),
        ("CISCO-CVP-MIB", "ccvpSipIntConnectsRcv"),
        ("CISCO-CVP-MIB", "ccvpSipIntAvgLatency1"),
        ("CISCO-CVP-MIB", "ccvpSipIntAvgLatency2"),
        ("CISCO-CVP-MIB", "ccvpSipIntFailedXferPre"),
        ("CISCO-CVP-MIB", "ccvpSipIntFailedXferPost"),
        ("CISCO-CVP-MIB", "ccvpSipAggNewCalls"),
        ("CISCO-CVP-MIB", "ccvpSipAggConnectsRcv"),
        ("CISCO-CVP-MIB", "ccvpSipAggAvgLatency1"),
        ("CISCO-CVP-MIB", "ccvpSipAggAvgLatency2"),
        ("CISCO-CVP-MIB", "ccvpSipAggFailedXferPre"),
        ("CISCO-CVP-MIB", "ccvpSipAggFailedXferPost"),
        ("CISCO-CVP-MIB", "ccvpSipIntPostCallAnswered"),
        ("CISCO-CVP-MIB", "ccvpSipIntWhisperAnswered"),
        ("CISCO-CVP-MIB", "ccvpSipIntWhisperFailed"),
        ("CISCO-CVP-MIB", "ccvpSipIntGreetingAnswered"),
        ("CISCO-CVP-MIB", "ccvpSipIntGreetingFailed"))
)
if mibBuilder.loadTexts:
    ccvpSipTableGroup.setStatus("current")

ccvpH323TableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 7)
)
ccvpH323TableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpH323RtCallsInProgress"),
        ("CISCO-CVP-MIB", "ccvpH323RtMemoryInUse"),
        ("CISCO-CVP-MIB", "ccvpH323IntArrivalRate"),
        ("CISCO-CVP-MIB", "ccvpH323IntTransferRate"),
        ("CISCO-CVP-MIB", "ccvpH323IntMaxNewCallLatency"),
        ("CISCO-CVP-MIB", "ccvpH323IntAvgNewCallLatency"),
        ("CISCO-CVP-MIB", "ccvpH323IntMaxXferToAlert"),
        ("CISCO-CVP-MIB", "ccvpH323IntAvgXferToAlert"),
        ("CISCO-CVP-MIB", "ccvpH323IntMaxXferToAnswer"),
        ("CISCO-CVP-MIB", "ccvpH323IntAvgXferToAnswer"),
        ("CISCO-CVP-MIB", "ccvpH323IntNewCalls"),
        ("CISCO-CVP-MIB", "ccvpH323IntTransferred"),
        ("CISCO-CVP-MIB", "ccvpH323IntRedirected"),
        ("CISCO-CVP-MIB", "ccvpH323IntNotTransferred"),
        ("CISCO-CVP-MIB", "ccvpH323IntPromptsNotFound"),
        ("CISCO-CVP-MIB", "ccvpH323IntCriticalMedia"),
        ("CISCO-CVP-MIB", "ccvpH323IntCallsFinished"),
        ("CISCO-CVP-MIB", "ccvpH323IntMaxCpuUsage"),
        ("CISCO-CVP-MIB", "ccvpH323IntAvgCpuUsage"))
)
if mibBuilder.loadTexts:
    ccvpH323TableGroup.setStatus("current")

ccvpIvrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 8)
)
ccvpIvrTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpIvrRtActiveCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrRtActiveHttpReqs"),
        ("CISCO-CVP-MIB", "ccvpIvrIntNewCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrIntMaxActiveCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrIntCallsFinished"),
        ("CISCO-CVP-MIB", "ccvpIvrIntAvgCallLatency"),
        ("CISCO-CVP-MIB", "ccvpIvrIntMaxCallLatency"),
        ("CISCO-CVP-MIB", "ccvpIvrIntMinCallLatency"),
        ("CISCO-CVP-MIB", "ccvpIvrIntHttpReqs"),
        ("CISCO-CVP-MIB", "ccvpIvrIntMaxActiveHttpReqs"),
        ("CISCO-CVP-MIB", "ccvpIvrIntMaxHttpReqRate"),
        ("CISCO-CVP-MIB", "ccvpIvrIntAvgHttpReqRate"),
        ("CISCO-CVP-MIB", "ccvpIvrAggNewCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrAggMaxActiveCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrAggHttpReqs"),
        ("CISCO-CVP-MIB", "ccvpIvrAggMaxHttpReqs"))
)
if mibBuilder.loadTexts:
    ccvpIvrTableGroup.setStatus("current")

ccvpIcmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 9)
)
ccvpIcmTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpIcmRtActiveCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmRtActiveSIPCallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmRtActiveH323CallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmRtActiveVRUCallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmRtActiveICMLookupReqs"),
        ("CISCO-CVP-MIB", "ccvpIcmIntNewCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmIntSipCallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmIntH323CallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmIntVruCallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmIntIcmLookupReqs"),
        ("CISCO-CVP-MIB", "ccvpIcmAggCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmAggSipCallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmAggH323CallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmAggVruCallLegs"),
        ("CISCO-CVP-MIB", "ccvpIcmAggIcmLookupReqs"))
)
if mibBuilder.loadTexts:
    ccvpIcmTableGroup.setStatus("current")

ccvpReptTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 10)
)
ccvpReptTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpReptIntVxmlEvents"),
        ("CISCO-CVP-MIB", "ccvpReptIntSipEvents"),
        ("CISCO-CVP-MIB", "ccvpReptIntIvrEvents"),
        ("CISCO-CVP-MIB", "ccvpReptIntDatabaseWrites"),
        ("CISCO-CVP-MIB", "ccvpReptAggVxmlEvents"),
        ("CISCO-CVP-MIB", "ccvpReptAggSipEvents"),
        ("CISCO-CVP-MIB", "ccvpReptAggIvrEvents"),
        ("CISCO-CVP-MIB", "ccvpReptAggDatabaseWrites"))
)
if mibBuilder.loadTexts:
    ccvpReptTableGroup.setStatus("current")

ccvpVxmlTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 11)
)
ccvpVxmlTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpVxmlRtActiveSessions"),
        ("CISCO-CVP-MIB", "ccvpVxmlRtActiveIcmLookups"),
        ("CISCO-CVP-MIB", "ccvpVxmlIntSessions"),
        ("CISCO-CVP-MIB", "ccvpVxmlIntReptEvents"),
        ("CISCO-CVP-MIB", "ccvpVxmlIntIcmLookupReqs"),
        ("CISCO-CVP-MIB", "ccvpVxmlIntIcmLookupResp"),
        ("CISCO-CVP-MIB", "ccvpVxmlIntIcmLookupSuccess"),
        ("CISCO-CVP-MIB", "ccvpVxmlIntIcmLookupFails"),
        ("CISCO-CVP-MIB", "ccvpVxmlAggSessions"),
        ("CISCO-CVP-MIB", "ccvpVxmlAggReptEvents"),
        ("CISCO-CVP-MIB", "ccvpVxmlAggIcmLookupReqs"),
        ("CISCO-CVP-MIB", "ccvpVxmlAggIcmLookupResp"),
        ("CISCO-CVP-MIB", "ccvpVxmlAggIcmLookupSuccess"),
        ("CISCO-CVP-MIB", "ccvpVxmlAggIcmLookupFails"))
)
if mibBuilder.loadTexts:
    ccvpVxmlTableGroup.setStatus("current")

ccvpCvpNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 12)
)
ccvpCvpNotificationInfoGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpEventMessageId"),
        ("CISCO-CVP-MIB", "ccvpEventHostName"),
        ("CISCO-CVP-MIB", "ccvpEventAppName"),
        ("CISCO-CVP-MIB", "ccvpEventMessageName"),
        ("CISCO-CVP-MIB", "ccvpEventState"),
        ("CISCO-CVP-MIB", "ccvpEventSeverity"),
        ("CISCO-CVP-MIB", "ccvpEventTimestamp"),
        ("CISCO-CVP-MIB", "ccvpEventText"))
)
if mibBuilder.loadTexts:
    ccvpCvpNotificationInfoGroup.setStatus("current")

ccvpSipVideoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 14)
)
ccvpSipVideoTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpSipRtBasicVideoOffered"),
        ("CISCO-CVP-MIB", "ccvpSipRtBasicVideoAnswered"),
        ("CISCO-CVP-MIB", "ccvpSipIntBasicVideoOffered"),
        ("CISCO-CVP-MIB", "ccvpSipIntBasicVideoAnswered"),
        ("CISCO-CVP-MIB", "ccvpSipAggBasicVideoOffered"),
        ("CISCO-CVP-MIB", "ccvpSipAggBasicVideoAnswered"))
)
if mibBuilder.loadTexts:
    ccvpSipVideoTableGroup.setStatus("current")

ccvpIvrVideoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 15)
)
ccvpIvrVideoTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpIvrRtFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrIntFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrAggFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrIntMaxFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrAggMaxFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIvrAggAgentPushedVideo"),
        ("CISCO-CVP-MIB", "ccvpIvrAggAgentInitiatedRecordings"),
        ("CISCO-CVP-MIB", "ccvpIvrAggAgentVCRControlInvocations"))
)
if mibBuilder.loadTexts:
    ccvpIvrVideoTableGroup.setStatus("current")

ccvpIcmVideoTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 16)
)
ccvpIcmVideoTableGroup.setObjects(
      *(("CISCO-CVP-MIB", "ccvpIcmRtFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmRtOfferedBasicVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmRtAcceptedBasicVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmIntFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmIntOfferedBasicVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmIntAcceptedBasicVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmAggFullVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmAggOfferedBasicVideoCalls"),
        ("CISCO-CVP-MIB", "ccvpIcmAggAcceptedBasicVideoCalls"))
)
if mibBuilder.loadTexts:
    ccvpIcmVideoTableGroup.setStatus("current")


# Notification objects

ccvpCvpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 0, 1)
)
ccvpCvpEvent.setObjects(
      *(("CISCO-CVP-MIB", "ccvpEventMessageId"),
        ("CISCO-CVP-MIB", "ccvpEventHostName"),
        ("CISCO-CVP-MIB", "ccvpEventAppName"),
        ("CISCO-CVP-MIB", "ccvpEventMessageName"),
        ("CISCO-CVP-MIB", "ccvpEventState"),
        ("CISCO-CVP-MIB", "ccvpEventSeverity"),
        ("CISCO-CVP-MIB", "ccvpEventTimestamp"),
        ("CISCO-CVP-MIB", "ccvpEventText"))
)
if mibBuilder.loadTexts:
    ccvpCvpEvent.setStatus(
        "current"
    )


# Notifications groups

ccvpCvpEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 2, 13)
)
ccvpCvpEventsGroup.setObjects(
    ("CISCO-CVP-MIB", "ccvpCvpEvent")
)
if mibBuilder.loadTexts:
    ccvpCvpEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCcvpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCcvpMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCcvpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 590, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCcvpMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CVP-MIB",
    **{"CcvpIndex": CcvpIndex,
       "CcvpServiceType": CcvpServiceType,
       "CcvpServiceStatus": CcvpServiceStatus,
       "ciscoCvpMIB": ciscoCvpMIB,
       "ciscoCvpMIBNotifs": ciscoCvpMIBNotifs,
       "ccvpCvpEvent": ccvpCvpEvent,
       "ciscoCvpMIBObjects": ciscoCvpMIBObjects,
       "ccvpGeneralInfo": ccvpGeneralInfo,
       "ccvpServerName": ccvpServerName,
       "ccvpDescription": ccvpDescription,
       "ccvpVersion": ccvpVersion,
       "ccvpStartTime": ccvpStartTime,
       "ccvpTimeZoneName": ccvpTimeZoneName,
       "ccvpTimeZoneOffsetHours": ccvpTimeZoneOffsetHours,
       "ccvpTimeZoneOffsetMinutes": ccvpTimeZoneOffsetMinutes,
       "ccvpOpsConsoleURL": ccvpOpsConsoleURL,
       "ccvpSupportToolsURL": ccvpSupportToolsURL,
       "ccvpEnableNotifications": ccvpEnableNotifications,
       "ccvpLicensingInfo": ccvpLicensingInfo,
       "ccvpLicRtPortsAvail": ccvpLicRtPortsAvail,
       "ccvpLicRtPortsInUse": ccvpLicRtPortsInUse,
       "ccvpLicRtPortState": ccvpLicRtPortState,
       "ccvpLicIntLastUpdate": ccvpLicIntLastUpdate,
       "ccvpLicIntPeriod": ccvpLicIntPeriod,
       "ccvpLicIntPortReqs": ccvpLicIntPortReqs,
       "ccvpLicIntAvgPortReqs": ccvpLicIntAvgPortReqs,
       "ccvpLicIntMaxPortsInUse": ccvpLicIntMaxPortsInUse,
       "ccvpLicIntPortReqsDenied": ccvpLicIntPortReqsDenied,
       "ccvpLicAggPortReqs": ccvpLicAggPortReqs,
       "ccvpLicAggAvgPortReqs": ccvpLicAggAvgPortReqs,
       "ccvpLicAggMaxPortsInUse": ccvpLicAggMaxPortsInUse,
       "ccvpLicAggPortReqsDenied": ccvpLicAggPortReqsDenied,
       "ccvpLicPortUsageWarning": ccvpLicPortUsageWarning,
       "ccvpLicPortUsageCritical": ccvpLicPortUsageCritical,
       "ccvpThreadPoolInfo": ccvpThreadPoolInfo,
       "ccvpTPoolRtIdleThreads": ccvpTPoolRtIdleThreads,
       "ccvpTPoolRtRunningThreads": ccvpTPoolRtRunningThreads,
       "ccvpTPoolRtCoreThreads": ccvpTPoolRtCoreThreads,
       "ccvpTPoolRtMaxThreadsAvail": ccvpTPoolRtMaxThreadsAvail,
       "ccvpTPoolRtMaxThreadsUsed": ccvpTPoolRtMaxThreadsUsed,
       "ccvpJvmInfo": ccvpJvmInfo,
       "ccvpJvmRtMaxMemUsed": ccvpJvmRtMaxMemUsed,
       "ccvpJvmRtCurrMemUsed": ccvpJvmRtCurrMemUsed,
       "ccvpJvmRtMaxMemAvail": ccvpJvmRtMaxMemAvail,
       "ccvpJvmRtCurrMemAvail": ccvpJvmRtCurrMemAvail,
       "ccvpJvmRtCurrThreadsInUse": ccvpJvmRtCurrThreadsInUse,
       "ccvpJvmRtMaxThreadsUsed": ccvpJvmRtMaxThreadsUsed,
       "ccvpJvmRtUpTime": ccvpJvmRtUpTime,
       "ccvpServices": ccvpServices,
       "ccvpServiceTable": ccvpServiceTable,
       "ccvpServiceEntry": ccvpServiceEntry,
       "ccvpServiceIndex": ccvpServiceIndex,
       "ccvpServiceType": ccvpServiceType,
       "ccvpServiceName": ccvpServiceName,
       "ccvpServiceStatus": ccvpServiceStatus,
       "ccvpServiceIntLastUpdate": ccvpServiceIntLastUpdate,
       "ccvpServiceIntPeriod": ccvpServiceIntPeriod,
       "ccvpServiceInfo": ccvpServiceInfo,
       "ccvpSipTable": ccvpSipTable,
       "ccvpSipEntry": ccvpSipEntry,
       "ccvpSipRtActiveCalls": ccvpSipRtActiveCalls,
       "ccvpSipRtTotalCallLegs": ccvpSipRtTotalCallLegs,
       "ccvpSipIntNewCalls": ccvpSipIntNewCalls,
       "ccvpSipIntConnectsRcv": ccvpSipIntConnectsRcv,
       "ccvpSipIntAvgLatency1": ccvpSipIntAvgLatency1,
       "ccvpSipIntAvgLatency2": ccvpSipIntAvgLatency2,
       "ccvpSipIntFailedXferPre": ccvpSipIntFailedXferPre,
       "ccvpSipIntFailedXferPost": ccvpSipIntFailedXferPost,
       "ccvpSipAggNewCalls": ccvpSipAggNewCalls,
       "ccvpSipAggConnectsRcv": ccvpSipAggConnectsRcv,
       "ccvpSipAggAvgLatency1": ccvpSipAggAvgLatency1,
       "ccvpSipAggAvgLatency2": ccvpSipAggAvgLatency2,
       "ccvpSipAggFailedXferPre": ccvpSipAggFailedXferPre,
       "ccvpSipAggFailedXferPost": ccvpSipAggFailedXferPost,
       "ccvpSipRtBasicVideoOffered": ccvpSipRtBasicVideoOffered,
       "ccvpSipRtBasicVideoAnswered": ccvpSipRtBasicVideoAnswered,
       "ccvpSipIntBasicVideoOffered": ccvpSipIntBasicVideoOffered,
       "ccvpSipIntBasicVideoAnswered": ccvpSipIntBasicVideoAnswered,
       "ccvpSipAggBasicVideoOffered": ccvpSipAggBasicVideoOffered,
       "ccvpSipAggBasicVideoAnswered": ccvpSipAggBasicVideoAnswered,
       "ccvpSipIntPostCallAnswered": ccvpSipIntPostCallAnswered,
       "ccvpSipIntWhisperAnswered": ccvpSipIntWhisperAnswered,
       "ccvpSipIntWhisperFailed": ccvpSipIntWhisperFailed,
       "ccvpSipIntGreetingAnswered": ccvpSipIntGreetingAnswered,
       "ccvpSipIntGreetingFailed": ccvpSipIntGreetingFailed,
       "ccvpH323Table": ccvpH323Table,
       "ccvpH323Entry": ccvpH323Entry,
       "ccvpH323RtCallsInProgress": ccvpH323RtCallsInProgress,
       "ccvpH323RtMemoryInUse": ccvpH323RtMemoryInUse,
       "ccvpH323IntArrivalRate": ccvpH323IntArrivalRate,
       "ccvpH323IntTransferRate": ccvpH323IntTransferRate,
       "ccvpH323IntMaxNewCallLatency": ccvpH323IntMaxNewCallLatency,
       "ccvpH323IntAvgNewCallLatency": ccvpH323IntAvgNewCallLatency,
       "ccvpH323IntMaxXferToAlert": ccvpH323IntMaxXferToAlert,
       "ccvpH323IntAvgXferToAlert": ccvpH323IntAvgXferToAlert,
       "ccvpH323IntMaxXferToAnswer": ccvpH323IntMaxXferToAnswer,
       "ccvpH323IntAvgXferToAnswer": ccvpH323IntAvgXferToAnswer,
       "ccvpH323IntNewCalls": ccvpH323IntNewCalls,
       "ccvpH323IntTransferred": ccvpH323IntTransferred,
       "ccvpH323IntRedirected": ccvpH323IntRedirected,
       "ccvpH323IntNotTransferred": ccvpH323IntNotTransferred,
       "ccvpH323IntPromptsNotFound": ccvpH323IntPromptsNotFound,
       "ccvpH323IntCriticalMedia": ccvpH323IntCriticalMedia,
       "ccvpH323IntCallsFinished": ccvpH323IntCallsFinished,
       "ccvpH323IntMaxCpuUsage": ccvpH323IntMaxCpuUsage,
       "ccvpH323IntAvgCpuUsage": ccvpH323IntAvgCpuUsage,
       "ccvpIvrTable": ccvpIvrTable,
       "ccvpIvrEntry": ccvpIvrEntry,
       "ccvpIvrRtActiveCalls": ccvpIvrRtActiveCalls,
       "ccvpIvrRtActiveHttpReqs": ccvpIvrRtActiveHttpReqs,
       "ccvpIvrIntNewCalls": ccvpIvrIntNewCalls,
       "ccvpIvrIntMaxActiveCalls": ccvpIvrIntMaxActiveCalls,
       "ccvpIvrIntCallsFinished": ccvpIvrIntCallsFinished,
       "ccvpIvrIntAvgCallLatency": ccvpIvrIntAvgCallLatency,
       "ccvpIvrIntMaxCallLatency": ccvpIvrIntMaxCallLatency,
       "ccvpIvrIntMinCallLatency": ccvpIvrIntMinCallLatency,
       "ccvpIvrIntHttpReqs": ccvpIvrIntHttpReqs,
       "ccvpIvrIntMaxActiveHttpReqs": ccvpIvrIntMaxActiveHttpReqs,
       "ccvpIvrIntMaxHttpReqRate": ccvpIvrIntMaxHttpReqRate,
       "ccvpIvrIntAvgHttpReqRate": ccvpIvrIntAvgHttpReqRate,
       "ccvpIvrAggNewCalls": ccvpIvrAggNewCalls,
       "ccvpIvrAggMaxActiveCalls": ccvpIvrAggMaxActiveCalls,
       "ccvpIvrAggHttpReqs": ccvpIvrAggHttpReqs,
       "ccvpIvrAggMaxHttpReqs": ccvpIvrAggMaxHttpReqs,
       "ccvpIvrRtFullVideoCalls": ccvpIvrRtFullVideoCalls,
       "ccvpIvrIntFullVideoCalls": ccvpIvrIntFullVideoCalls,
       "ccvpIvrAggFullVideoCalls": ccvpIvrAggFullVideoCalls,
       "ccvpIvrIntMaxFullVideoCalls": ccvpIvrIntMaxFullVideoCalls,
       "ccvpIvrAggMaxFullVideoCalls": ccvpIvrAggMaxFullVideoCalls,
       "ccvpIvrAggAgentPushedVideo": ccvpIvrAggAgentPushedVideo,
       "ccvpIvrAggAgentInitiatedRecordings": ccvpIvrAggAgentInitiatedRecordings,
       "ccvpIvrAggAgentVCRControlInvocations": ccvpIvrAggAgentVCRControlInvocations,
       "ccvpIcmTable": ccvpIcmTable,
       "ccvpIcmEntry": ccvpIcmEntry,
       "ccvpIcmRtActiveCalls": ccvpIcmRtActiveCalls,
       "ccvpIcmRtActiveSIPCallLegs": ccvpIcmRtActiveSIPCallLegs,
       "ccvpIcmRtActiveH323CallLegs": ccvpIcmRtActiveH323CallLegs,
       "ccvpIcmRtActiveVRUCallLegs": ccvpIcmRtActiveVRUCallLegs,
       "ccvpIcmRtActiveICMLookupReqs": ccvpIcmRtActiveICMLookupReqs,
       "ccvpIcmIntNewCalls": ccvpIcmIntNewCalls,
       "ccvpIcmIntSipCallLegs": ccvpIcmIntSipCallLegs,
       "ccvpIcmIntH323CallLegs": ccvpIcmIntH323CallLegs,
       "ccvpIcmIntVruCallLegs": ccvpIcmIntVruCallLegs,
       "ccvpIcmIntIcmLookupReqs": ccvpIcmIntIcmLookupReqs,
       "ccvpIcmAggCalls": ccvpIcmAggCalls,
       "ccvpIcmAggSipCallLegs": ccvpIcmAggSipCallLegs,
       "ccvpIcmAggH323CallLegs": ccvpIcmAggH323CallLegs,
       "ccvpIcmAggVruCallLegs": ccvpIcmAggVruCallLegs,
       "ccvpIcmAggIcmLookupReqs": ccvpIcmAggIcmLookupReqs,
       "ccvpIcmRtFullVideoCalls": ccvpIcmRtFullVideoCalls,
       "ccvpIcmRtOfferedBasicVideoCalls": ccvpIcmRtOfferedBasicVideoCalls,
       "ccvpIcmRtAcceptedBasicVideoCalls": ccvpIcmRtAcceptedBasicVideoCalls,
       "ccvpIcmIntFullVideoCalls": ccvpIcmIntFullVideoCalls,
       "ccvpIcmIntOfferedBasicVideoCalls": ccvpIcmIntOfferedBasicVideoCalls,
       "ccvpIcmIntAcceptedBasicVideoCalls": ccvpIcmIntAcceptedBasicVideoCalls,
       "ccvpIcmAggFullVideoCalls": ccvpIcmAggFullVideoCalls,
       "ccvpIcmAggOfferedBasicVideoCalls": ccvpIcmAggOfferedBasicVideoCalls,
       "ccvpIcmAggAcceptedBasicVideoCalls": ccvpIcmAggAcceptedBasicVideoCalls,
       "ccvpReptTable": ccvpReptTable,
       "ccvpReptEntry": ccvpReptEntry,
       "ccvpReptIntVxmlEvents": ccvpReptIntVxmlEvents,
       "ccvpReptIntSipEvents": ccvpReptIntSipEvents,
       "ccvpReptIntIvrEvents": ccvpReptIntIvrEvents,
       "ccvpReptIntDatabaseWrites": ccvpReptIntDatabaseWrites,
       "ccvpReptAggVxmlEvents": ccvpReptAggVxmlEvents,
       "ccvpReptAggSipEvents": ccvpReptAggSipEvents,
       "ccvpReptAggIvrEvents": ccvpReptAggIvrEvents,
       "ccvpReptAggDatabaseWrites": ccvpReptAggDatabaseWrites,
       "ccvpVxmlTable": ccvpVxmlTable,
       "ccvpVxmlEntry": ccvpVxmlEntry,
       "ccvpVxmlRtActiveSessions": ccvpVxmlRtActiveSessions,
       "ccvpVxmlRtActiveIcmLookups": ccvpVxmlRtActiveIcmLookups,
       "ccvpVxmlIntSessions": ccvpVxmlIntSessions,
       "ccvpVxmlIntReptEvents": ccvpVxmlIntReptEvents,
       "ccvpVxmlIntIcmLookupReqs": ccvpVxmlIntIcmLookupReqs,
       "ccvpVxmlIntIcmLookupResp": ccvpVxmlIntIcmLookupResp,
       "ccvpVxmlIntIcmLookupSuccess": ccvpVxmlIntIcmLookupSuccess,
       "ccvpVxmlIntIcmLookupFails": ccvpVxmlIntIcmLookupFails,
       "ccvpVxmlAggSessions": ccvpVxmlAggSessions,
       "ccvpVxmlAggReptEvents": ccvpVxmlAggReptEvents,
       "ccvpVxmlAggIcmLookupReqs": ccvpVxmlAggIcmLookupReqs,
       "ccvpVxmlAggIcmLookupResp": ccvpVxmlAggIcmLookupResp,
       "ccvpVxmlAggIcmLookupSuccess": ccvpVxmlAggIcmLookupSuccess,
       "ccvpVxmlAggIcmLookupFails": ccvpVxmlAggIcmLookupFails,
       "ccvpNotificationInfo": ccvpNotificationInfo,
       "ccvpEventMessageId": ccvpEventMessageId,
       "ccvpEventHostName": ccvpEventHostName,
       "ccvpEventAppName": ccvpEventAppName,
       "ccvpEventMessageName": ccvpEventMessageName,
       "ccvpEventState": ccvpEventState,
       "ccvpEventSeverity": ccvpEventSeverity,
       "ccvpEventTimestamp": ccvpEventTimestamp,
       "ccvpEventText": ccvpEventText,
       "ciscoCvpMIBConform": ciscoCvpMIBConform,
       "ciscoCvpMIBCompliances": ciscoCvpMIBCompliances,
       "ciscoCcvpMIBComplianceRev1": ciscoCcvpMIBComplianceRev1,
       "ciscoCcvpMIBComplianceRev2": ciscoCcvpMIBComplianceRev2,
       "ciscoCvpMIBGroups": ciscoCvpMIBGroups,
       "ccvpGeneralInfoGroup": ccvpGeneralInfoGroup,
       "ccvpLicensingInfoGroup": ccvpLicensingInfoGroup,
       "ccvpThreadPoolInfoGroup": ccvpThreadPoolInfoGroup,
       "ccvpJvmInfoGroup": ccvpJvmInfoGroup,
       "ccvpServiceTableGroup": ccvpServiceTableGroup,
       "ccvpSipTableGroup": ccvpSipTableGroup,
       "ccvpH323TableGroup": ccvpH323TableGroup,
       "ccvpIvrTableGroup": ccvpIvrTableGroup,
       "ccvpIcmTableGroup": ccvpIcmTableGroup,
       "ccvpReptTableGroup": ccvpReptTableGroup,
       "ccvpVxmlTableGroup": ccvpVxmlTableGroup,
       "ccvpCvpNotificationInfoGroup": ccvpCvpNotificationInfoGroup,
       "ccvpCvpEventsGroup": ccvpCvpEventsGroup,
       "ccvpSipVideoTableGroup": ccvpSipVideoTableGroup,
       "ccvpIvrVideoTableGroup": ccvpIvrVideoTableGroup,
       "ccvpIcmVideoTableGroup": ccvpIcmVideoTableGroup}
)
