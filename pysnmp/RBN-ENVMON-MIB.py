# SNMP MIB module (RBN-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-ENVMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:06 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnEnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBNotifications = _RbnEnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0)
)
_RbnEnvMonMIBObjects_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBObjects = _RbnEnvMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1)
)
_RbnFanStatusTable_Object = MibTable
rbnFanStatusTable = _RbnFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rbnFanStatusTable.setStatus("current")
_RbnFanStatusEntry_Object = MibTableRow
rbnFanStatusEntry = _RbnFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1)
)
rbnFanStatusEntry.setIndexNames(
    (0, "RBN-ENVMON-MIB", "rbnFanIndex"),
)
if mibBuilder.loadTexts:
    rbnFanStatusEntry.setStatus("current")
_RbnFanIndex_Type = Integer32
_RbnFanIndex_Object = MibTableColumn
rbnFanIndex = _RbnFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 1),
    _RbnFanIndex_Type()
)
rbnFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFanIndex.setStatus("current")
_RbnFanDescr_Type = DisplayString
_RbnFanDescr_Object = MibTableColumn
rbnFanDescr = _RbnFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 2),
    _RbnFanDescr_Type()
)
rbnFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanDescr.setStatus("current")
_RbnFanFail_Type = TruthValue
_RbnFanFail_Object = MibTableColumn
rbnFanFail = _RbnFanFail_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 3),
    _RbnFanFail_Type()
)
rbnFanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFanFail.setStatus("current")
_RbnPowerStatusTable_Object = MibTable
rbnPowerStatusTable = _RbnPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rbnPowerStatusTable.setStatus("current")
_RbnPowerStatusEntry_Object = MibTableRow
rbnPowerStatusEntry = _RbnPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1)
)
rbnPowerStatusEntry.setIndexNames(
    (0, "RBN-ENVMON-MIB", "rbnPowerIndex"),
)
if mibBuilder.loadTexts:
    rbnPowerStatusEntry.setStatus("current")
_RbnPowerIndex_Type = Integer32
_RbnPowerIndex_Object = MibTableColumn
rbnPowerIndex = _RbnPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 1),
    _RbnPowerIndex_Type()
)
rbnPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnPowerIndex.setStatus("current")
_RbnPowerDescr_Type = DisplayString
_RbnPowerDescr_Object = MibTableColumn
rbnPowerDescr = _RbnPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 2),
    _RbnPowerDescr_Type()
)
rbnPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPowerDescr.setStatus("current")
_RbnPowerFail_Type = TruthValue
_RbnPowerFail_Object = MibTableColumn
rbnPowerFail = _RbnPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 3),
    _RbnPowerFail_Type()
)
rbnPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnPowerFail.setStatus("current")
_RbnEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBConformance = _RbnEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2)
)
_RbnEnvMonMIBGroups_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBGroups = _RbnEnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1)
)
_RbnEnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
rbnEnvMonMIBCompliances = _RbnEnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2)
)

# Managed Objects groups

rbnEnvMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 1)
)
rbnEnvMonMIBObjectGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanDescr"),
        ("RBN-ENVMON-MIB", "rbnFanFail"),
        ("RBN-ENVMON-MIB", "rbnPowerDescr"),
        ("RBN-ENVMON-MIB", "rbnPowerFail"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBObjectGroup.setStatus("current")


# Notification objects

rbnFanFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 1)
)
rbnFanFailChange.setObjects(
    ("RBN-ENVMON-MIB", "rbnFanFail")
)
if mibBuilder.loadTexts:
    rbnFanFailChange.setStatus(
        "current"
    )

rbnPowerFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 2)
)
rbnPowerFailChange.setObjects(
    ("RBN-ENVMON-MIB", "rbnPowerFail")
)
if mibBuilder.loadTexts:
    rbnPowerFailChange.setStatus(
        "current"
    )


# Notifications groups

rbnEnvMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 2)
)
rbnEnvMonMIBNotificationGroup.setObjects(
      *(("RBN-ENVMON-MIB", "rbnFanFailChange"),
        ("RBN-ENVMON-MIB", "rbnPowerFailChange"))
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnEnvMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnEnvMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ENVMON-MIB",
    **{"rbnEnvMonMIB": rbnEnvMonMIB,
       "rbnEnvMonMIBNotifications": rbnEnvMonMIBNotifications,
       "rbnFanFailChange": rbnFanFailChange,
       "rbnPowerFailChange": rbnPowerFailChange,
       "rbnEnvMonMIBObjects": rbnEnvMonMIBObjects,
       "rbnFanStatusTable": rbnFanStatusTable,
       "rbnFanStatusEntry": rbnFanStatusEntry,
       "rbnFanIndex": rbnFanIndex,
       "rbnFanDescr": rbnFanDescr,
       "rbnFanFail": rbnFanFail,
       "rbnPowerStatusTable": rbnPowerStatusTable,
       "rbnPowerStatusEntry": rbnPowerStatusEntry,
       "rbnPowerIndex": rbnPowerIndex,
       "rbnPowerDescr": rbnPowerDescr,
       "rbnPowerFail": rbnPowerFail,
       "rbnEnvMonMIBConformance": rbnEnvMonMIBConformance,
       "rbnEnvMonMIBGroups": rbnEnvMonMIBGroups,
       "rbnEnvMonMIBObjectGroup": rbnEnvMonMIBObjectGroup,
       "rbnEnvMonMIBNotificationGroup": rbnEnvMonMIBNotificationGroup,
       "rbnEnvMonMIBCompliances": rbnEnvMonMIBCompliances,
       "rbnEnvMonMIBCompliance": rbnEnvMonMIBCompliance}
)
