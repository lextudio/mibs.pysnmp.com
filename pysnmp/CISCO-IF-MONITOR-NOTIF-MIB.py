# SNMP MIB module (CISCO-IF-MONITOR-NOTIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-MONITOR-NOTIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:13 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

ciscoIfMonitorNotifMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999)
)
ciscoIfMonitorNotifMIB.setRevisions(
        ("2002-10-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CIfMonNotifMIBNotifications_ObjectIdentity = ObjectIdentity
cIfMonNotifMIBNotifications = _CIfMonNotifMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0)
)
_CIfMonNotifMIBObjects_ObjectIdentity = ObjectIdentity
cIfMonNotifMIBObjects = _CIfMonNotifMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1)
)


class _CIfMonNotifCount_Type(Unsigned32):
    """Custom type cIfMonNotifCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIfMonNotifCount_Type.__name__ = "Unsigned32"
_CIfMonNotifCount_Object = MibScalar
cIfMonNotifCount = _CIfMonNotifCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1),
    _CIfMonNotifCount_Type()
)
cIfMonNotifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifCount.setStatus("current")
_CIfMonNotifTable_Object = MibTable
cIfMonNotifTable = _CIfMonNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2)
)
if mibBuilder.loadTexts:
    cIfMonNotifTable.setStatus("current")
_CIfMonNotifEntry_Object = MibTableRow
cIfMonNotifEntry = _CIfMonNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1)
)
cIfMonNotifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIfMonNotifEntry.setStatus("current")
_CIfMonNotifLastChange_Type = TimeStamp
_CIfMonNotifLastChange_Object = MibTableColumn
cIfMonNotifLastChange = _CIfMonNotifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 1),
    _CIfMonNotifLastChange_Type()
)
cIfMonNotifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifLastChange.setStatus("current")


class _CIfMonNotifSeverity_Type(Integer32):
    """Custom type cIfMonNotifSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("red", 1),
          ("yellow", 2))
    )


_CIfMonNotifSeverity_Type.__name__ = "Integer32"
_CIfMonNotifSeverity_Object = MibTableColumn
cIfMonNotifSeverity = _CIfMonNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 2),
    _CIfMonNotifSeverity_Type()
)
cIfMonNotifSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifSeverity.setStatus("current")


class _CIfMonNotifCause_Type(Integer32):
    """Custom type cIfMonNotifCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborts", 1),
          ("crc", 2),
          ("disc", 9),
          ("drops", 3),
          ("flaps", 4),
          ("frame-reject", 5),
          ("frmr", 8),
          ("runts", 6),
          ("sabm", 7))
    )


_CIfMonNotifCause_Type.__name__ = "Integer32"
_CIfMonNotifCause_Object = MibTableColumn
cIfMonNotifCause = _CIfMonNotifCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 3),
    _CIfMonNotifCause_Type()
)
cIfMonNotifCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifCause.setStatus("current")


class _CIfMonNotifValue_Type(Unsigned32):
    """Custom type cIfMonNotifValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIfMonNotifValue_Type.__name__ = "Unsigned32"
_CIfMonNotifValue_Object = MibTableColumn
cIfMonNotifValue = _CIfMonNotifValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 4),
    _CIfMonNotifValue_Type()
)
cIfMonNotifValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifValue.setStatus("current")


class _CIfMonNotifThreshold_Type(Unsigned32):
    """Custom type cIfMonNotifThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_CIfMonNotifThreshold_Type.__name__ = "Unsigned32"
_CIfMonNotifThreshold_Object = MibTableColumn
cIfMonNotifThreshold = _CIfMonNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 5),
    _CIfMonNotifThreshold_Type()
)
cIfMonNotifThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifThreshold.setStatus("current")


class _CIfMonNotifInterval_Type(Unsigned32):
    """Custom type cIfMonNotifInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_CIfMonNotifInterval_Type.__name__ = "Unsigned32"
_CIfMonNotifInterval_Object = MibTableColumn
cIfMonNotifInterval = _CIfMonNotifInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 6),
    _CIfMonNotifInterval_Type()
)
cIfMonNotifInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIfMonNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    cIfMonNotifInterval.setUnits("seconds")
_CIfMonNotifMIBConformance_ObjectIdentity = ObjectIdentity
cIfMonNotifMIBConformance = _CIfMonNotifMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2)
)
_CIfMonNotifMIBCompliances_ObjectIdentity = ObjectIdentity
cIfMonNotifMIBCompliances = _CIfMonNotifMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1)
)
_CIfMonNotifMIBGroups_ObjectIdentity = ObjectIdentity
cIfMonNotifMIBGroups = _CIfMonNotifMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2)
)

# Managed Objects groups

cIfMonNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)
)
cIfMonNotifObjectGroup.setObjects(
      *(("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCount"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifLastChange"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifSeverity"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCause"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifValue"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifThreshold"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifInterval"))
)
if mibBuilder.loadTexts:
    cIfMonNotifObjectGroup.setStatus("current")


# Notification objects

cIfMonNotifEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)
)
cIfMonNotifEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCount"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifSeverity"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCause"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifValue"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifThreshold"),
        ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifInterval"))
)
if mibBuilder.loadTexts:
    cIfMonNotifEvent.setStatus(
        "current"
    )


# Notifications groups

cIfMonNotifEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 2)
)
cIfMonNotifEventGroup.setObjects(
    ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifEvent")
)
if mibBuilder.loadTexts:
    cIfMonNotifEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cIfMonNotifMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cIfMonNotifMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-MONITOR-NOTIF-MIB",
    **{"ciscoIfMonitorNotifMIB": ciscoIfMonitorNotifMIB,
       "cIfMonNotifMIBNotifications": cIfMonNotifMIBNotifications,
       "cIfMonNotifEvent": cIfMonNotifEvent,
       "cIfMonNotifMIBObjects": cIfMonNotifMIBObjects,
       "cIfMonNotifCount": cIfMonNotifCount,
       "cIfMonNotifTable": cIfMonNotifTable,
       "cIfMonNotifEntry": cIfMonNotifEntry,
       "cIfMonNotifLastChange": cIfMonNotifLastChange,
       "cIfMonNotifSeverity": cIfMonNotifSeverity,
       "cIfMonNotifCause": cIfMonNotifCause,
       "cIfMonNotifValue": cIfMonNotifValue,
       "cIfMonNotifThreshold": cIfMonNotifThreshold,
       "cIfMonNotifInterval": cIfMonNotifInterval,
       "cIfMonNotifMIBConformance": cIfMonNotifMIBConformance,
       "cIfMonNotifMIBCompliances": cIfMonNotifMIBCompliances,
       "cIfMonNotifMIBCompliance": cIfMonNotifMIBCompliance,
       "cIfMonNotifMIBGroups": cIfMonNotifMIBGroups,
       "cIfMonNotifObjectGroup": cIfMonNotifObjectGroup,
       "cIfMonNotifEventGroup": cIfMonNotifEventGroup}
)
