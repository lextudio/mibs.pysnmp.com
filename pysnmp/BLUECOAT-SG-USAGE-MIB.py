# SNMP MIB module (BLUECOAT-SG-USAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-USAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:23 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

deviceUsageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4)
)
deviceUsageMIB.setRevisions(
        ("2013-07-11 03:00",
         "2008-01-16 03:00",
         "2007-12-07 03:00",
         "2002-11-06 03:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(Integer32, TextualConvention):
    status = "current"
    displayHint = "d%"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class UsageStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("ok", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceUsageMIBObjects_ObjectIdentity = ObjectIdentity
deviceUsageMIBObjects = _DeviceUsageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1)
)
_DeviceUsageTable_Object = MibTable
deviceUsageTable = _DeviceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    deviceUsageTable.setStatus("current")
_DeviceUsageEntry_Object = MibTableRow
deviceUsageEntry = _DeviceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1)
)
deviceUsageEntry.setIndexNames(
    (0, "BLUECOAT-SG-USAGE-MIB", "deviceUsageIndex"),
)
if mibBuilder.loadTexts:
    deviceUsageEntry.setStatus("current")


class _DeviceUsageIndex_Type(Integer32):
    """Custom type deviceUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceUsageIndex_Type.__name__ = "Integer32"
_DeviceUsageIndex_Object = MibTableColumn
deviceUsageIndex = _DeviceUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 1),
    _DeviceUsageIndex_Type()
)
deviceUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceUsageIndex.setStatus("current")
_DeviceUsageTrapEnabled_Type = TruthValue
_DeviceUsageTrapEnabled_Object = MibTableColumn
deviceUsageTrapEnabled = _DeviceUsageTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 2),
    _DeviceUsageTrapEnabled_Type()
)
deviceUsageTrapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUsageTrapEnabled.setStatus("current")
_DeviceUsageName_Type = DisplayString
_DeviceUsageName_Object = MibTableColumn
deviceUsageName = _DeviceUsageName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 3),
    _DeviceUsageName_Type()
)
deviceUsageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUsageName.setStatus("current")
_DeviceUsagePercent_Type = Percent
_DeviceUsagePercent_Object = MibTableColumn
deviceUsagePercent = _DeviceUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 4),
    _DeviceUsagePercent_Type()
)
deviceUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUsagePercent.setStatus("current")
_DeviceUsageHigh_Type = Percent
_DeviceUsageHigh_Object = MibTableColumn
deviceUsageHigh = _DeviceUsageHigh_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 5),
    _DeviceUsageHigh_Type()
)
deviceUsageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUsageHigh.setStatus("current")
_DeviceUsageStatus_Type = UsageStatus
_DeviceUsageStatus_Object = MibTableColumn
deviceUsageStatus = _DeviceUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 6),
    _DeviceUsageStatus_Type()
)
deviceUsageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUsageStatus.setStatus("current")
_DeviceUsageTime_Type = TimeStamp
_DeviceUsageTime_Object = MibTableColumn
deviceUsageTime = _DeviceUsageTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 1, 1, 1, 7),
    _DeviceUsageTime_Type()
)
deviceUsageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUsageTime.setStatus("current")
if mibBuilder.loadTexts:
    deviceUsageTime.setUnits("Hundredths of seconds")
_DeviceUsageMIBNotifications_ObjectIdentity = ObjectIdentity
deviceUsageMIBNotifications = _DeviceUsageMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 2)
)
_DeviceUsageMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
deviceUsageMIBNotificationsPrefix = _DeviceUsageMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0)
)

# Managed Objects groups


# Notification objects

deviceUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 4, 2, 0, 1)
)
deviceUsageTrap.setObjects(
      *(("BLUECOAT-SG-USAGE-MIB", "deviceUsageName"),
        ("BLUECOAT-SG-USAGE-MIB", "deviceUsagePercent"),
        ("BLUECOAT-SG-USAGE-MIB", "deviceUsageStatus"))
)
if mibBuilder.loadTexts:
    deviceUsageTrap.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-USAGE-MIB",
    **{"Percent": Percent,
       "UsageStatus": UsageStatus,
       "deviceUsageMIB": deviceUsageMIB,
       "deviceUsageMIBObjects": deviceUsageMIBObjects,
       "deviceUsageTable": deviceUsageTable,
       "deviceUsageEntry": deviceUsageEntry,
       "deviceUsageIndex": deviceUsageIndex,
       "deviceUsageTrapEnabled": deviceUsageTrapEnabled,
       "deviceUsageName": deviceUsageName,
       "deviceUsagePercent": deviceUsagePercent,
       "deviceUsageHigh": deviceUsageHigh,
       "deviceUsageStatus": deviceUsageStatus,
       "deviceUsageTime": deviceUsageTime,
       "deviceUsageMIBNotifications": deviceUsageMIBNotifications,
       "deviceUsageMIBNotificationsPrefix": deviceUsageMIBNotificationsPrefix,
       "deviceUsageTrap": deviceUsageTrap}
)
