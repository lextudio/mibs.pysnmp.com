# SNMP MIB module (CISCO-PORT-TRACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PORT-TRACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:00 2024
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

(VsanIndex,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "VsanIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPortTrackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 437)
)
ciscoPortTrackMIB.setRevisions(
        ("2005-04-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPortTrackObjects_ObjectIdentity = ObjectIdentity
ciscoPortTrackObjects = _CiscoPortTrackObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1)
)
_CptConfig_ObjectIdentity = ObjectIdentity
cptConfig = _CptConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1)
)
_CptPortTrackTable_Object = MibTable
cptPortTrackTable = _CptPortTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cptPortTrackTable.setStatus("current")
_CptPortTrackEntry_Object = MibTableRow
cptPortTrackEntry = _CptPortTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1, 1)
)
cptPortTrackEntry.setIndexNames(
    (0, "CISCO-PORT-TRACK-MIB", "cptPortTrackLinkedPort"),
    (0, "CISCO-PORT-TRACK-MIB", "cptPortTrackTrackedPort"),
)
if mibBuilder.loadTexts:
    cptPortTrackEntry.setStatus("current")
_CptPortTrackLinkedPort_Type = InterfaceIndex
_CptPortTrackLinkedPort_Object = MibTableColumn
cptPortTrackLinkedPort = _CptPortTrackLinkedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1, 1, 1),
    _CptPortTrackLinkedPort_Type()
)
cptPortTrackLinkedPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cptPortTrackLinkedPort.setStatus("current")
_CptPortTrackTrackedPort_Type = InterfaceIndex
_CptPortTrackTrackedPort_Object = MibTableColumn
cptPortTrackTrackedPort = _CptPortTrackTrackedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1, 1, 2),
    _CptPortTrackTrackedPort_Type()
)
cptPortTrackTrackedPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cptPortTrackTrackedPort.setStatus("current")


class _CptPortTrackVsanType_Type(Integer32):
    """Custom type cptPortTrackVsanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allVsans", 2),
          ("singleVsan", 1))
    )


_CptPortTrackVsanType_Type.__name__ = "Integer32"
_CptPortTrackVsanType_Object = MibTableColumn
cptPortTrackVsanType = _CptPortTrackVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1, 1, 3),
    _CptPortTrackVsanType_Type()
)
cptPortTrackVsanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cptPortTrackVsanType.setStatus("current")
_CptPortTrackVsanIndex_Type = VsanIndex
_CptPortTrackVsanIndex_Object = MibTableColumn
cptPortTrackVsanIndex = _CptPortTrackVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1, 1, 4),
    _CptPortTrackVsanIndex_Type()
)
cptPortTrackVsanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cptPortTrackVsanIndex.setStatus("current")
_CptPortTrackRowStatus_Type = RowStatus
_CptPortTrackRowStatus_Object = MibTableColumn
cptPortTrackRowStatus = _CptPortTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 1, 1, 5),
    _CptPortTrackRowStatus_Type()
)
cptPortTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cptPortTrackRowStatus.setStatus("current")
_CptPortForceShutTable_Object = MibTable
cptPortForceShutTable = _CptPortForceShutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cptPortForceShutTable.setStatus("current")
_CptPortForceShutEntry_Object = MibTableRow
cptPortForceShutEntry = _CptPortForceShutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 2, 1)
)
cptPortForceShutEntry.setIndexNames(
    (0, "CISCO-PORT-TRACK-MIB", "cptPortTrackLinkedPort"),
)
if mibBuilder.loadTexts:
    cptPortForceShutEntry.setStatus("current")


class _CptPortForceState_Type(TruthValue):
    """Custom type cptPortForceState based on TruthValue"""


_CptPortForceState_Object = MibTableColumn
cptPortForceState = _CptPortForceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 1, 1, 2, 1, 1),
    _CptPortForceState_Type()
)
cptPortForceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cptPortForceState.setStatus("current")
_CptMIBConformance_ObjectIdentity = ObjectIdentity
cptMIBConformance = _CptMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 2)
)
_CptMIBCompliances_ObjectIdentity = ObjectIdentity
cptMIBCompliances = _CptMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 2, 1)
)
_CptMIBGroups_ObjectIdentity = ObjectIdentity
cptMIBGroups = _CptMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 2, 2)
)

# Managed Objects groups

cptTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 2, 2, 1)
)
cptTrackGroup.setObjects(
      *(("CISCO-PORT-TRACK-MIB", "cptPortTrackVsanType"),
        ("CISCO-PORT-TRACK-MIB", "cptPortTrackVsanIndex"),
        ("CISCO-PORT-TRACK-MIB", "cptPortTrackRowStatus"))
)
if mibBuilder.loadTexts:
    cptTrackGroup.setStatus("current")

cptShutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 2, 2, 2)
)
cptShutGroup.setObjects(
    ("CISCO-PORT-TRACK-MIB", "cptPortForceState")
)
if mibBuilder.loadTexts:
    cptShutGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cptMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 437, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cptMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PORT-TRACK-MIB",
    **{"ciscoPortTrackMIB": ciscoPortTrackMIB,
       "ciscoPortTrackObjects": ciscoPortTrackObjects,
       "cptConfig": cptConfig,
       "cptPortTrackTable": cptPortTrackTable,
       "cptPortTrackEntry": cptPortTrackEntry,
       "cptPortTrackLinkedPort": cptPortTrackLinkedPort,
       "cptPortTrackTrackedPort": cptPortTrackTrackedPort,
       "cptPortTrackVsanType": cptPortTrackVsanType,
       "cptPortTrackVsanIndex": cptPortTrackVsanIndex,
       "cptPortTrackRowStatus": cptPortTrackRowStatus,
       "cptPortForceShutTable": cptPortForceShutTable,
       "cptPortForceShutEntry": cptPortForceShutEntry,
       "cptPortForceState": cptPortForceState,
       "cptMIBConformance": cptMIBConformance,
       "cptMIBCompliances": cptMIBCompliances,
       "cptMIBCompliance": cptMIBCompliance,
       "cptMIBGroups": cptMIBGroups,
       "cptTrackGroup": cptTrackGroup,
       "cptShutGroup": cptShutGroup}
)
