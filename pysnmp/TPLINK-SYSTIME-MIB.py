# SNMP MIB module (TPLINK-SYSTIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SYSTIME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:47 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSysTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2)
)
tplinkSysTimeMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSysTimeMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSysTimeMIBObjects = _TplinkSysTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1)
)


class _TpSysTimeCurrentTime_Type(OctetString):
    """Custom type tpSysTimeCurrentTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpSysTimeCurrentTime_Type.__name__ = "OctetString"
_TpSysTimeCurrentTime_Object = MibScalar
tpSysTimeCurrentTime = _TpSysTimeCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 1),
    _TpSysTimeCurrentTime_Type()
)
tpSysTimeCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysTimeCurrentTime.setStatus("current")


class _TpSysTimeSource_Type(OctetString):
    """Custom type tpSysTimeSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpSysTimeSource_Type.__name__ = "OctetString"
_TpSysTimeSource_Object = MibScalar
tpSysTimeSource = _TpSysTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 2),
    _TpSysTimeSource_Type()
)
tpSysTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysTimeSource.setStatus("current")


class _TpSysTimeMode_Type(OctetString):
    """Custom type tpSysTimeMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpSysTimeMode_Type.__name__ = "OctetString"
_TpSysTimeMode_Object = MibScalar
tpSysTimeMode = _TpSysTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 3),
    _TpSysTimeMode_Type()
)
tpSysTimeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSysTimeMode.setStatus("current")
_TpSysTimeManualTimeConfig_ObjectIdentity = ObjectIdentity
tpSysTimeManualTimeConfig = _TpSysTimeManualTimeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 4)
)


class _TpSysTimeManualTimeStatus_Type(Integer32):
    """Custom type tpSysTimeManualTimeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSysTimeManualTimeStatus_Type.__name__ = "Integer32"
_TpSysTimeManualTimeStatus_Object = MibScalar
tpSysTimeManualTimeStatus = _TpSysTimeManualTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 4, 1),
    _TpSysTimeManualTimeStatus_Type()
)
tpSysTimeManualTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeManualTimeStatus.setStatus("current")


class _TpSysTimeTimeToSet_Type(OctetString):
    """Custom type tpSysTimeTimeToSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_TpSysTimeTimeToSet_Type.__name__ = "OctetString"
_TpSysTimeTimeToSet_Object = MibScalar
tpSysTimeTimeToSet = _TpSysTimeTimeToSet_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 4, 2),
    _TpSysTimeTimeToSet_Type()
)
tpSysTimeTimeToSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeTimeToSet.setStatus("current")
_TpSysTimeNTPClientConfig_ObjectIdentity = ObjectIdentity
tpSysTimeNTPClientConfig = _TpSysTimeNTPClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 5)
)


class _TpSysTimeNTPClientStatus_Type(Integer32):
    """Custom type tpSysTimeNTPClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpSysTimeNTPClientStatus_Type.__name__ = "Integer32"
_TpSysTimeNTPClientStatus_Object = MibScalar
tpSysTimeNTPClientStatus = _TpSysTimeNTPClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 5, 1),
    _TpSysTimeNTPClientStatus_Type()
)
tpSysTimeNTPClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeNTPClientStatus.setStatus("current")


class _TpSysTimeNTPTimezone_Type(Integer32):
    """Custom type tpSysTimeNTPTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1200,
              -1100,
              -1000,
              -900,
              -800,
              -700,
              -600,
              -500,
              -450,
              -400,
              -350,
              -300,
              -200,
              -100,
              0,
              100,
              200,
              300,
              350,
              400,
              450,
              500,
              550,
              575,
              600,
              650,
              700,
              800,
              900,
              950,
              1000,
              1100,
              1200,
              1300)
        )
    )
    namedValues = NamedValues(
        *(("utc", 0),
          ("utc-0100", -100),
          ("utc-0200", -200),
          ("utc-0300", -300),
          ("utc-0330", -350),
          ("utc-0400", -400),
          ("utc-0430", -450),
          ("utc-0500", -500),
          ("utc-0600", -600),
          ("utc-0700", -700),
          ("utc-0800", -800),
          ("utc-0900", -900),
          ("utc-1000", -1000),
          ("utc-1100", -1100),
          ("utc-1200", -1200),
          ("utc0100", 100),
          ("utc0200", 200),
          ("utc0300", 300),
          ("utc0330", 350),
          ("utc0400", 400),
          ("utc0430", 450),
          ("utc0500", 500),
          ("utc0530", 550),
          ("utc0545", 575),
          ("utc0600", 600),
          ("utc0630", 650),
          ("utc0700", 700),
          ("utc0800", 800),
          ("utc0900", 900),
          ("utc0930", 950),
          ("utc1000", 1000),
          ("utc1100", 1100),
          ("utc1200", 1200),
          ("utc1300", 1300))
    )


_TpSysTimeNTPTimezone_Type.__name__ = "Integer32"
_TpSysTimeNTPTimezone_Object = MibScalar
tpSysTimeNTPTimezone = _TpSysTimeNTPTimezone_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 5, 2),
    _TpSysTimeNTPTimezone_Type()
)
tpSysTimeNTPTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeNTPTimezone.setStatus("current")
_TpSysTimeNTPServerAddr_Type = IpAddress
_TpSysTimeNTPServerAddr_Object = MibScalar
tpSysTimeNTPServerAddr = _TpSysTimeNTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 5, 3),
    _TpSysTimeNTPServerAddr_Type()
)
tpSysTimeNTPServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeNTPServerAddr.setStatus("current")
_TpSysTimeNTPBackupServerAddr_Type = IpAddress
_TpSysTimeNTPBackupServerAddr_Object = MibScalar
tpSysTimeNTPBackupServerAddr = _TpSysTimeNTPBackupServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 5, 4),
    _TpSysTimeNTPBackupServerAddr_Type()
)
tpSysTimeNTPBackupServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeNTPBackupServerAddr.setStatus("current")


class _TpSysTimeNTPUpdateRate_Type(Integer32):
    """Custom type tpSysTimeNTPUpdateRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TpSysTimeNTPUpdateRate_Type.__name__ = "Integer32"
_TpSysTimeNTPUpdateRate_Object = MibScalar
tpSysTimeNTPUpdateRate = _TpSysTimeNTPUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 5, 5),
    _TpSysTimeNTPUpdateRate_Type()
)
tpSysTimeNTPUpdateRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeNTPUpdateRate.setStatus("current")
_TpSysTimeDstConfig_ObjectIdentity = ObjectIdentity
tpSysTimeDstConfig = _TpSysTimeDstConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6)
)


class _TpSysTimeDstStatus_Type(Integer32):
    """Custom type tpSysTimeDstStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("date", 3),
          ("disabled", 0),
          ("predefined", 1),
          ("recurring", 2))
    )


_TpSysTimeDstStatus_Type.__name__ = "Integer32"
_TpSysTimeDstStatus_Object = MibScalar
tpSysTimeDstStatus = _TpSysTimeDstStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 1),
    _TpSysTimeDstStatus_Type()
)
tpSysTimeDstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstStatus.setStatus("current")


class _TpSysTimeDstOffset_Type(Integer32):
    """Custom type tpSysTimeDstOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_TpSysTimeDstOffset_Type.__name__ = "Integer32"
_TpSysTimeDstOffset_Object = MibScalar
tpSysTimeDstOffset = _TpSysTimeDstOffset_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 2),
    _TpSysTimeDstOffset_Type()
)
tpSysTimeDstOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstOffset.setStatus("current")
if mibBuilder.loadTexts:
    tpSysTimeDstOffset.setUnits("Minutes")
_TpSysTimeDstDateMode_ObjectIdentity = ObjectIdentity
tpSysTimeDstDateMode = _TpSysTimeDstDateMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 3)
)


class _TpSysTimeDstDateTimeToStart_Type(OctetString):
    """Custom type tpSysTimeDstDateTimeToStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_TpSysTimeDstDateTimeToStart_Type.__name__ = "OctetString"
_TpSysTimeDstDateTimeToStart_Object = MibScalar
tpSysTimeDstDateTimeToStart = _TpSysTimeDstDateTimeToStart_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 3, 1),
    _TpSysTimeDstDateTimeToStart_Type()
)
tpSysTimeDstDateTimeToStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstDateTimeToStart.setStatus("current")


class _TpSysTimeDstDateTimeToEnd_Type(OctetString):
    """Custom type tpSysTimeDstDateTimeToEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_TpSysTimeDstDateTimeToEnd_Type.__name__ = "OctetString"
_TpSysTimeDstDateTimeToEnd_Object = MibScalar
tpSysTimeDstDateTimeToEnd = _TpSysTimeDstDateTimeToEnd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 3, 2),
    _TpSysTimeDstDateTimeToEnd_Type()
)
tpSysTimeDstDateTimeToEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstDateTimeToEnd.setStatus("current")
_TpSysTimeDstPredefinedMode_ObjectIdentity = ObjectIdentity
tpSysTimeDstPredefinedMode = _TpSysTimeDstPredefinedMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 4)
)


class _TpSysTimeDstRegionSelected_Type(Integer32):
    """Custom type tpSysTimeDstRegionSelected based on Integer32"""
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
        *(("australia", 2),
          ("europe", 3),
          ("new-Zealand", 4),
          ("none", 0),
          ("usa", 1))
    )


_TpSysTimeDstRegionSelected_Type.__name__ = "Integer32"
_TpSysTimeDstRegionSelected_Object = MibScalar
tpSysTimeDstRegionSelected = _TpSysTimeDstRegionSelected_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 4, 1),
    _TpSysTimeDstRegionSelected_Type()
)
tpSysTimeDstRegionSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstRegionSelected.setStatus("current")
_TpSysTimeDstRecurringMode_ObjectIdentity = ObjectIdentity
tpSysTimeDstRecurringMode = _TpSysTimeDstRecurringMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 5)
)


class _TpSysTimeDstRecurringToStart_Type(OctetString):
    """Custom type tpSysTimeDstRecurringToStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_TpSysTimeDstRecurringToStart_Type.__name__ = "OctetString"
_TpSysTimeDstRecurringToStart_Object = MibScalar
tpSysTimeDstRecurringToStart = _TpSysTimeDstRecurringToStart_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 5, 1),
    _TpSysTimeDstRecurringToStart_Type()
)
tpSysTimeDstRecurringToStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstRecurringToStart.setStatus("current")


class _TpSysTimeDstRecurringToEnd_Type(OctetString):
    """Custom type tpSysTimeDstRecurringToEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_TpSysTimeDstRecurringToEnd_Type.__name__ = "OctetString"
_TpSysTimeDstRecurringToEnd_Object = MibScalar
tpSysTimeDstRecurringToEnd = _TpSysTimeDstRecurringToEnd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 1, 6, 5, 2),
    _TpSysTimeDstRecurringToEnd_Type()
)
tpSysTimeDstRecurringToEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSysTimeDstRecurringToEnd.setStatus("current")
_TplinkSysTimeNotifications_ObjectIdentity = ObjectIdentity
tplinkSysTimeNotifications = _TplinkSysTimeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SYSTIME-MIB",
    **{"tplinkSysTimeMIB": tplinkSysTimeMIB,
       "tplinkSysTimeMIBObjects": tplinkSysTimeMIBObjects,
       "tpSysTimeCurrentTime": tpSysTimeCurrentTime,
       "tpSysTimeSource": tpSysTimeSource,
       "tpSysTimeMode": tpSysTimeMode,
       "tpSysTimeManualTimeConfig": tpSysTimeManualTimeConfig,
       "tpSysTimeManualTimeStatus": tpSysTimeManualTimeStatus,
       "tpSysTimeTimeToSet": tpSysTimeTimeToSet,
       "tpSysTimeNTPClientConfig": tpSysTimeNTPClientConfig,
       "tpSysTimeNTPClientStatus": tpSysTimeNTPClientStatus,
       "tpSysTimeNTPTimezone": tpSysTimeNTPTimezone,
       "tpSysTimeNTPServerAddr": tpSysTimeNTPServerAddr,
       "tpSysTimeNTPBackupServerAddr": tpSysTimeNTPBackupServerAddr,
       "tpSysTimeNTPUpdateRate": tpSysTimeNTPUpdateRate,
       "tpSysTimeDstConfig": tpSysTimeDstConfig,
       "tpSysTimeDstStatus": tpSysTimeDstStatus,
       "tpSysTimeDstOffset": tpSysTimeDstOffset,
       "tpSysTimeDstDateMode": tpSysTimeDstDateMode,
       "tpSysTimeDstDateTimeToStart": tpSysTimeDstDateTimeToStart,
       "tpSysTimeDstDateTimeToEnd": tpSysTimeDstDateTimeToEnd,
       "tpSysTimeDstPredefinedMode": tpSysTimeDstPredefinedMode,
       "tpSysTimeDstRegionSelected": tpSysTimeDstRegionSelected,
       "tpSysTimeDstRecurringMode": tpSysTimeDstRecurringMode,
       "tpSysTimeDstRecurringToStart": tpSysTimeDstRecurringToStart,
       "tpSysTimeDstRecurringToEnd": tpSysTimeDstRecurringToEnd,
       "tplinkSysTimeNotifications": tplinkSysTimeNotifications}
)
