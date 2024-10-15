# SNMP MIB module (ARISTA-DAEMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-DAEMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:19 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

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

aristaDaemonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17)
)
aristaDaemonMIB.setRevisions(
        ("2015-04-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class AgentAttributeKey(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class AgentAttributeValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "10240a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10240),
    )



# MIB Managed Objects in the order of their OIDs

_AristaDaemonConfig_ObjectIdentity = ObjectIdentity
aristaDaemonConfig = _AristaDaemonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1)
)
_AristaDaemonEnabledTable_Object = MibTable
aristaDaemonEnabledTable = _AristaDaemonEnabledTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    aristaDaemonEnabledTable.setStatus("current")
_AristaDaemonEnabledEntry_Object = MibTableRow
aristaDaemonEnabledEntry = _AristaDaemonEnabledEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1)
)
aristaDaemonEnabledEntry.setIndexNames(
    (0, "ARISTA-DAEMON-MIB", "aristaDaemonEnabledAgentName"),
)
if mibBuilder.loadTexts:
    aristaDaemonEnabledEntry.setStatus("current")
_AristaDaemonEnabledAgentName_Type = AgentName
_AristaDaemonEnabledAgentName_Object = MibTableColumn
aristaDaemonEnabledAgentName = _AristaDaemonEnabledAgentName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1, 1),
    _AristaDaemonEnabledAgentName_Type()
)
aristaDaemonEnabledAgentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDaemonEnabledAgentName.setStatus("current")
_AristaDaemonEnabled_Type = TruthValue
_AristaDaemonEnabled_Object = MibTableColumn
aristaDaemonEnabled = _AristaDaemonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1, 2),
    _AristaDaemonEnabled_Type()
)
aristaDaemonEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDaemonEnabled.setStatus("current")
_AristaDaemonOptionTable_Object = MibTable
aristaDaemonOptionTable = _AristaDaemonOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2)
)
if mibBuilder.loadTexts:
    aristaDaemonOptionTable.setStatus("current")
_AristaDaemonOptionEntry_Object = MibTableRow
aristaDaemonOptionEntry = _AristaDaemonOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1)
)
aristaDaemonOptionEntry.setIndexNames(
    (0, "ARISTA-DAEMON-MIB", "aristaDaemonOptionAgentName"),
    (0, "ARISTA-DAEMON-MIB", "aristaDaemonOptionKey"),
)
if mibBuilder.loadTexts:
    aristaDaemonOptionEntry.setStatus("current")
_AristaDaemonOptionAgentName_Type = AgentName
_AristaDaemonOptionAgentName_Object = MibTableColumn
aristaDaemonOptionAgentName = _AristaDaemonOptionAgentName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 1),
    _AristaDaemonOptionAgentName_Type()
)
aristaDaemonOptionAgentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDaemonOptionAgentName.setStatus("current")
_AristaDaemonOptionKey_Type = AgentAttributeKey
_AristaDaemonOptionKey_Object = MibTableColumn
aristaDaemonOptionKey = _AristaDaemonOptionKey_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 2),
    _AristaDaemonOptionKey_Type()
)
aristaDaemonOptionKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDaemonOptionKey.setStatus("current")
_AristaDaemonOptionValue_Type = AgentAttributeValue
_AristaDaemonOptionValue_Object = MibTableColumn
aristaDaemonOptionValue = _AristaDaemonOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 3),
    _AristaDaemonOptionValue_Type()
)
aristaDaemonOptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDaemonOptionValue.setStatus("current")
_AristaDaemonStatus_ObjectIdentity = ObjectIdentity
aristaDaemonStatus = _AristaDaemonStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2)
)
_AristaDaemonRunningTable_Object = MibTable
aristaDaemonRunningTable = _AristaDaemonRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1)
)
if mibBuilder.loadTexts:
    aristaDaemonRunningTable.setStatus("current")
_AristaDaemonRunningEntry_Object = MibTableRow
aristaDaemonRunningEntry = _AristaDaemonRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1)
)
aristaDaemonRunningEntry.setIndexNames(
    (0, "ARISTA-DAEMON-MIB", "aristaDaemonRunningAgentName"),
)
if mibBuilder.loadTexts:
    aristaDaemonRunningEntry.setStatus("current")
_AristaDaemonRunningAgentName_Type = AgentName
_AristaDaemonRunningAgentName_Object = MibTableColumn
aristaDaemonRunningAgentName = _AristaDaemonRunningAgentName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1, 1),
    _AristaDaemonRunningAgentName_Type()
)
aristaDaemonRunningAgentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDaemonRunningAgentName.setStatus("current")
_AristaDaemonRunning_Type = TruthValue
_AristaDaemonRunning_Object = MibTableColumn
aristaDaemonRunning = _AristaDaemonRunning_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1, 2),
    _AristaDaemonRunning_Type()
)
aristaDaemonRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDaemonRunning.setStatus("current")
_AristaDaemonDataTable_Object = MibTable
aristaDaemonDataTable = _AristaDaemonDataTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2)
)
if mibBuilder.loadTexts:
    aristaDaemonDataTable.setStatus("current")
_AristaDaemonDataEntry_Object = MibTableRow
aristaDaemonDataEntry = _AristaDaemonDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1)
)
aristaDaemonDataEntry.setIndexNames(
    (0, "ARISTA-DAEMON-MIB", "aristaDaemonDataAgentName"),
    (0, "ARISTA-DAEMON-MIB", "aristaDaemonDataKey"),
)
if mibBuilder.loadTexts:
    aristaDaemonDataEntry.setStatus("current")
_AristaDaemonDataAgentName_Type = AgentName
_AristaDaemonDataAgentName_Object = MibTableColumn
aristaDaemonDataAgentName = _AristaDaemonDataAgentName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 1),
    _AristaDaemonDataAgentName_Type()
)
aristaDaemonDataAgentName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDaemonDataAgentName.setStatus("current")
_AristaDaemonDataKey_Type = AgentAttributeKey
_AristaDaemonDataKey_Object = MibTableColumn
aristaDaemonDataKey = _AristaDaemonDataKey_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 2),
    _AristaDaemonDataKey_Type()
)
aristaDaemonDataKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaDaemonDataKey.setStatus("current")
_AristaDaemonDataValue_Type = AgentAttributeValue
_AristaDaemonDataValue_Object = MibTableColumn
aristaDaemonDataValue = _AristaDaemonDataValue_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 3),
    _AristaDaemonDataValue_Type()
)
aristaDaemonDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaDaemonDataValue.setStatus("current")
_AristaDaemonConformance_ObjectIdentity = ObjectIdentity
aristaDaemonConformance = _AristaDaemonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 3)
)
_AristaDaemonGroups_ObjectIdentity = ObjectIdentity
aristaDaemonGroups = _AristaDaemonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 1)
)
_AristaDaemonCompliances_ObjectIdentity = ObjectIdentity
aristaDaemonCompliances = _AristaDaemonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 2)
)

# Managed Objects groups

aristaDaemonBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 1, 1)
)
aristaDaemonBaseGroup.setObjects(
      *(("ARISTA-DAEMON-MIB", "aristaDaemonEnabled"),
        ("ARISTA-DAEMON-MIB", "aristaDaemonOptionValue"),
        ("ARISTA-DAEMON-MIB", "aristaDaemonRunning"),
        ("ARISTA-DAEMON-MIB", "aristaDaemonDataValue"))
)
if mibBuilder.loadTexts:
    aristaDaemonBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaDaemonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aristaDaemonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-DAEMON-MIB",
    **{"AgentName": AgentName,
       "AgentAttributeKey": AgentAttributeKey,
       "AgentAttributeValue": AgentAttributeValue,
       "aristaDaemonMIB": aristaDaemonMIB,
       "aristaDaemonConfig": aristaDaemonConfig,
       "aristaDaemonEnabledTable": aristaDaemonEnabledTable,
       "aristaDaemonEnabledEntry": aristaDaemonEnabledEntry,
       "aristaDaemonEnabledAgentName": aristaDaemonEnabledAgentName,
       "aristaDaemonEnabled": aristaDaemonEnabled,
       "aristaDaemonOptionTable": aristaDaemonOptionTable,
       "aristaDaemonOptionEntry": aristaDaemonOptionEntry,
       "aristaDaemonOptionAgentName": aristaDaemonOptionAgentName,
       "aristaDaemonOptionKey": aristaDaemonOptionKey,
       "aristaDaemonOptionValue": aristaDaemonOptionValue,
       "aristaDaemonStatus": aristaDaemonStatus,
       "aristaDaemonRunningTable": aristaDaemonRunningTable,
       "aristaDaemonRunningEntry": aristaDaemonRunningEntry,
       "aristaDaemonRunningAgentName": aristaDaemonRunningAgentName,
       "aristaDaemonRunning": aristaDaemonRunning,
       "aristaDaemonDataTable": aristaDaemonDataTable,
       "aristaDaemonDataEntry": aristaDaemonDataEntry,
       "aristaDaemonDataAgentName": aristaDaemonDataAgentName,
       "aristaDaemonDataKey": aristaDaemonDataKey,
       "aristaDaemonDataValue": aristaDaemonDataValue,
       "aristaDaemonConformance": aristaDaemonConformance,
       "aristaDaemonGroups": aristaDaemonGroups,
       "aristaDaemonBaseGroup": aristaDaemonBaseGroup,
       "aristaDaemonCompliances": aristaDaemonCompliances,
       "aristaDaemonCompliance": aristaDaemonCompliance}
)
