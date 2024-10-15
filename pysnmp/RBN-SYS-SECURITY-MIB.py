# SNMP MIB module (RBN-SYS-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-SYS-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:26 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(rbnModules,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnModules")

(RbnUnsigned64,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnUnsigned64")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnSysSecurityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54)
)
rbnSysSecurityMib.setRevisions(
        ("2009-11-09 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSysSecNotifications_ObjectIdentity = ObjectIdentity
rbnSysSecNotifications = _RbnSysSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 0)
)
_RbnSysSecObjects_ObjectIdentity = ObjectIdentity
rbnSysSecObjects = _RbnSysSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1)
)
_RbnSysSecThresholdObjects_ObjectIdentity = ObjectIdentity
rbnSysSecThresholdObjects = _RbnSysSecThresholdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1)
)


class _RbnSysSecNotifyEnable_Type(Bits):
    """Custom type rbnSysSecNotifyEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("maliciousPkt", 0)
    )

_RbnSysSecNotifyEnable_Type.__name__ = "Bits"
_RbnSysSecNotifyEnable_Object = MibScalar
rbnSysSecNotifyEnable = _RbnSysSecNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 1),
    _RbnSysSecNotifyEnable_Type()
)
rbnSysSecNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSysSecNotifyEnable.setStatus("current")


class _RbnMeasurementInterval_Type(Gauge32):
    """Custom type rbnMeasurementInterval based on Gauge32"""
    defaultValue = 60

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RbnMeasurementInterval_Type.__name__ = "Gauge32"
_RbnMeasurementInterval_Object = MibScalar
rbnMeasurementInterval = _RbnMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 2),
    _RbnMeasurementInterval_Type()
)
rbnMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    rbnMeasurementInterval.setUnits("seconds")
_RbnMaliciousPktsThresholdHi_Type = RbnUnsigned64
_RbnMaliciousPktsThresholdHi_Object = MibScalar
rbnMaliciousPktsThresholdHi = _RbnMaliciousPktsThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 3),
    _RbnMaliciousPktsThresholdHi_Type()
)
rbnMaliciousPktsThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnMaliciousPktsThresholdHi.setStatus("current")
if mibBuilder.loadTexts:
    rbnMaliciousPktsThresholdHi.setUnits("Packets")
_RbnMaliciousPktsThresholdLow_Type = RbnUnsigned64
_RbnMaliciousPktsThresholdLow_Object = MibScalar
rbnMaliciousPktsThresholdLow = _RbnMaliciousPktsThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 1, 4),
    _RbnMaliciousPktsThresholdLow_Type()
)
rbnMaliciousPktsThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnMaliciousPktsThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    rbnMaliciousPktsThresholdLow.setUnits("Packets")
_RbnSysSecStatsObjects_ObjectIdentity = ObjectIdentity
rbnSysSecStatsObjects = _RbnSysSecStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 2)
)
_RbnMaliciousPktsCounter_Type = Counter64
_RbnMaliciousPktsCounter_Object = MibScalar
rbnMaliciousPktsCounter = _RbnMaliciousPktsCounter_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 2, 1),
    _RbnMaliciousPktsCounter_Type()
)
rbnMaliciousPktsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMaliciousPktsCounter.setStatus("current")
if mibBuilder.loadTexts:
    rbnMaliciousPktsCounter.setUnits("Packets")
_RbnMaliciousPktsDelta_Type = CounterBasedGauge64
_RbnMaliciousPktsDelta_Object = MibScalar
rbnMaliciousPktsDelta = _RbnMaliciousPktsDelta_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 2, 2),
    _RbnMaliciousPktsDelta_Type()
)
rbnMaliciousPktsDelta.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnMaliciousPktsDelta.setStatus("current")
if mibBuilder.loadTexts:
    rbnMaliciousPktsDelta.setUnits("packets")
_RbnSysSecNotifyObjects_ObjectIdentity = ObjectIdentity
rbnSysSecNotifyObjects = _RbnSysSecNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 4)
)
_RbnThresholdNotifyTime_Type = DateAndTime
_RbnThresholdNotifyTime_Object = MibScalar
rbnThresholdNotifyTime = _RbnThresholdNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 1, 4, 1),
    _RbnThresholdNotifyTime_Type()
)
rbnThresholdNotifyTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnThresholdNotifyTime.setStatus("current")
_RbnSysSecConformance_ObjectIdentity = ObjectIdentity
rbnSysSecConformance = _RbnSysSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2)
)
_RbnSysSecCompliances_ObjectIdentity = ObjectIdentity
rbnSysSecCompliances = _RbnSysSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 1)
)
_RbnSysSecGroups_ObjectIdentity = ObjectIdentity
rbnSysSecGroups = _RbnSysSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2)
)

# Managed Objects groups

rbnMaliciousPktGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2, 1)
)
rbnMaliciousPktGroup.setObjects(
      *(("RBN-SYS-SECURITY-MIB", "rbnSysSecNotifyEnable"),
        ("RBN-SYS-SECURITY-MIB", "rbnMeasurementInterval"),
        ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsThresholdHi"),
        ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsThresholdLow"),
        ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsCounter"))
)
if mibBuilder.loadTexts:
    rbnMaliciousPktGroup.setStatus("current")

rbnSysSecNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2, 4)
)
rbnSysSecNotifyObjectsGroup.setObjects(
      *(("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktsDelta"),
        ("RBN-SYS-SECURITY-MIB", "rbnThresholdNotifyTime"))
)
if mibBuilder.loadTexts:
    rbnSysSecNotifyObjectsGroup.setStatus("current")


# Notification objects

rbnMaliciousPktThresholdHiExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 0, 1)
)
if mibBuilder.loadTexts:
    rbnMaliciousPktThresholdHiExceeded.setStatus(
        "current"
    )

rbnMaliciousPktThresholdLowExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 0, 2)
)
rbnMaliciousPktThresholdLowExceeded.setObjects(
    ("RBN-SYS-SECURITY-MIB", "rbnThresholdNotifyTime")
)
if mibBuilder.loadTexts:
    rbnMaliciousPktThresholdLowExceeded.setStatus(
        "current"
    )


# Notifications groups

rbnSysSecNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 2, 5)
)
rbnSysSecNotificationGroup.setObjects(
      *(("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktThresholdHiExceeded"),
        ("RBN-SYS-SECURITY-MIB", "rbnMaliciousPktThresholdLowExceeded"))
)
if mibBuilder.loadTexts:
    rbnSysSecNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnSysSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 5, 54, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSysSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SYS-SECURITY-MIB",
    **{"rbnSysSecurityMib": rbnSysSecurityMib,
       "rbnSysSecNotifications": rbnSysSecNotifications,
       "rbnMaliciousPktThresholdHiExceeded": rbnMaliciousPktThresholdHiExceeded,
       "rbnMaliciousPktThresholdLowExceeded": rbnMaliciousPktThresholdLowExceeded,
       "rbnSysSecObjects": rbnSysSecObjects,
       "rbnSysSecThresholdObjects": rbnSysSecThresholdObjects,
       "rbnSysSecNotifyEnable": rbnSysSecNotifyEnable,
       "rbnMeasurementInterval": rbnMeasurementInterval,
       "rbnMaliciousPktsThresholdHi": rbnMaliciousPktsThresholdHi,
       "rbnMaliciousPktsThresholdLow": rbnMaliciousPktsThresholdLow,
       "rbnSysSecStatsObjects": rbnSysSecStatsObjects,
       "rbnMaliciousPktsCounter": rbnMaliciousPktsCounter,
       "rbnMaliciousPktsDelta": rbnMaliciousPktsDelta,
       "rbnSysSecNotifyObjects": rbnSysSecNotifyObjects,
       "rbnThresholdNotifyTime": rbnThresholdNotifyTime,
       "rbnSysSecConformance": rbnSysSecConformance,
       "rbnSysSecCompliances": rbnSysSecCompliances,
       "rbnSysSecCompliance": rbnSysSecCompliance,
       "rbnSysSecGroups": rbnSysSecGroups,
       "rbnMaliciousPktGroup": rbnMaliciousPktGroup,
       "rbnSysSecNotifyObjectsGroup": rbnSysSecNotifyObjectsGroup,
       "rbnSysSecNotificationGroup": rbnSysSecNotificationGroup}
)
