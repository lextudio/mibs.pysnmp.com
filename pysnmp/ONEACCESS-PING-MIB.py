# SNMP MIB module (ONEACCESS-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:01 2024
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

(pingCtlOwnerIndex,
 pingCtlTestName) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlOwnerIndex",
    "pingCtlTestName")

(oacExpIMPing,
 oacMIBModules,
 oneAccess) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMPing",
    "oacMIBModules",
    "oneAccess")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

oacPingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 6601)
)
oacPingMIBModule.setRevisions(
        ("2011-06-15 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacPingNotifications_ObjectIdentity = ObjectIdentity
oacPingNotifications = _OacPingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 0)
)
_OacPingObjects_ObjectIdentity = ObjectIdentity
oacPingObjects = _OacPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1)
)
_OacPingResultsTable_Object = MibTable
oacPingResultsTable = _OacPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    oacPingResultsTable.setStatus("current")
_OacPingResultsEntry_Object = MibTableRow
oacPingResultsEntry = _OacPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1)
)
oacPingResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    oacPingResultsEntry.setStatus("current")
_OacPingJitterSamples_Type = Unsigned32
_OacPingJitterSamples_Object = MibTableColumn
oacPingJitterSamples = _OacPingJitterSamples_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 1),
    _OacPingJitterSamples_Type()
)
oacPingJitterSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacPingJitterSamples.setStatus("current")
_OacPingResultsMinJitter_Type = Unsigned32
_OacPingResultsMinJitter_Object = MibTableColumn
oacPingResultsMinJitter = _OacPingResultsMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 2),
    _OacPingResultsMinJitter_Type()
)
oacPingResultsMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacPingResultsMinJitter.setStatus("current")
if mibBuilder.loadTexts:
    oacPingResultsMinJitter.setUnits("microseconds")
_OacPingResultsMaxJitter_Type = Unsigned32
_OacPingResultsMaxJitter_Object = MibTableColumn
oacPingResultsMaxJitter = _OacPingResultsMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 3),
    _OacPingResultsMaxJitter_Type()
)
oacPingResultsMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacPingResultsMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    oacPingResultsMaxJitter.setUnits("microseconds")
_OacPingResultsAverageJitter_Type = Unsigned32
_OacPingResultsAverageJitter_Object = MibTableColumn
oacPingResultsAverageJitter = _OacPingResultsAverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 4),
    _OacPingResultsAverageJitter_Type()
)
oacPingResultsAverageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacPingResultsAverageJitter.setStatus("current")
if mibBuilder.loadTexts:
    oacPingResultsAverageJitter.setUnits("microseconds")
_OacPingConformance_ObjectIdentity = ObjectIdentity
oacPingConformance = _OacPingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2)
)
_OacPingCompliances_ObjectIdentity = ObjectIdentity
oacPingCompliances = _OacPingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 1)
)
_OacPingGroups_ObjectIdentity = ObjectIdentity
oacPingGroups = _OacPingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 2)
)

# Managed Objects groups

oacPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 2, 1)
)
oacPingGroup.setObjects(
      *(("ONEACCESS-PING-MIB", "oacPingJitterSamples"),
        ("ONEACCESS-PING-MIB", "oacPingResultsMinJitter"),
        ("ONEACCESS-PING-MIB", "oacPingResultsMaxJitter"),
        ("ONEACCESS-PING-MIB", "oacPingResultsAverageJitter"))
)
if mibBuilder.loadTexts:
    oacPingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacPingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    oacPingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-PING-MIB",
    **{"oacPingMIBModule": oacPingMIBModule,
       "oacPingNotifications": oacPingNotifications,
       "oacPingObjects": oacPingObjects,
       "oacPingResultsTable": oacPingResultsTable,
       "oacPingResultsEntry": oacPingResultsEntry,
       "oacPingJitterSamples": oacPingJitterSamples,
       "oacPingResultsMinJitter": oacPingResultsMinJitter,
       "oacPingResultsMaxJitter": oacPingResultsMaxJitter,
       "oacPingResultsAverageJitter": oacPingResultsAverageJitter,
       "oacPingConformance": oacPingConformance,
       "oacPingCompliances": oacPingCompliances,
       "oacPingCompliance": oacPingCompliance,
       "oacPingGroups": oacPingGroups,
       "oacPingGroup": oacPingGroup}
)
