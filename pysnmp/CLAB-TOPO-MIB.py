# SNMP MIB module (CLAB-TOPO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAB-TOPO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:25 2024
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

clabTopoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2)
)
clabTopoMib.setRevisions(
        ("2017-06-15 00:00",
         "2009-01-21 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_ClabTopoMibObjects_ObjectIdentity = ObjectIdentity
clabTopoMibObjects = _ClabTopoMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1)
)
_ClabTopoFiberNodeCfgTable_Object = MibTable
clabTopoFiberNodeCfgTable = _ClabTopoFiberNodeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clabTopoFiberNodeCfgTable.setStatus("current")
_ClabTopoFiberNodeCfgEntry_Object = MibTableRow
clabTopoFiberNodeCfgEntry = _ClabTopoFiberNodeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1)
)
clabTopoFiberNodeCfgEntry.setIndexNames(
    (0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"),
)
if mibBuilder.loadTexts:
    clabTopoFiberNodeCfgEntry.setStatus("current")


class _ClabTopoFiberNodeCfgNodeName_Type(NodeName):
    """Custom type clabTopoFiberNodeCfgNodeName based on NodeName"""
    subtypeSpec = NodeName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ClabTopoFiberNodeCfgNodeName_Type.__name__ = "NodeName"
_ClabTopoFiberNodeCfgNodeName_Object = MibTableColumn
clabTopoFiberNodeCfgNodeName = _ClabTopoFiberNodeCfgNodeName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 1),
    _ClabTopoFiberNodeCfgNodeName_Type()
)
clabTopoFiberNodeCfgNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabTopoFiberNodeCfgNodeName.setStatus("current")


class _ClabTopoFiberNodeCfgNodeDescr_Type(SnmpAdminString):
    """Custom type clabTopoFiberNodeCfgNodeDescr based on SnmpAdminString"""
    defaultHexValue = ""


_ClabTopoFiberNodeCfgNodeDescr_Object = MibTableColumn
clabTopoFiberNodeCfgNodeDescr = _ClabTopoFiberNodeCfgNodeDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 2),
    _ClabTopoFiberNodeCfgNodeDescr_Type()
)
clabTopoFiberNodeCfgNodeDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabTopoFiberNodeCfgNodeDescr.setStatus("current")
_ClabTopoFiberNodeCfgRowStatus_Type = RowStatus
_ClabTopoFiberNodeCfgRowStatus_Object = MibTableColumn
clabTopoFiberNodeCfgRowStatus = _ClabTopoFiberNodeCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 3),
    _ClabTopoFiberNodeCfgRowStatus_Type()
)
clabTopoFiberNodeCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabTopoFiberNodeCfgRowStatus.setStatus("current")
_ClabTopoChFnCfgTable_Object = MibTable
clabTopoChFnCfgTable = _ClabTopoChFnCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    clabTopoChFnCfgTable.setStatus("current")
_ClabTopoChFnCfgEntry_Object = MibTableRow
clabTopoChFnCfgEntry = _ClabTopoChFnCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1)
)
clabTopoChFnCfgEntry.setIndexNames(
    (0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"),
    (0, "CLAB-TOPO-MIB", "clabTopoChFnCfgChIfIndex"),
)
if mibBuilder.loadTexts:
    clabTopoChFnCfgEntry.setStatus("current")
_ClabTopoChFnCfgChIfIndex_Type = InterfaceIndex
_ClabTopoChFnCfgChIfIndex_Object = MibTableColumn
clabTopoChFnCfgChIfIndex = _ClabTopoChFnCfgChIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 1),
    _ClabTopoChFnCfgChIfIndex_Type()
)
clabTopoChFnCfgChIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabTopoChFnCfgChIfIndex.setStatus("current")
_ClabTopoChFnCfgRowStatus_Type = RowStatus
_ClabTopoChFnCfgRowStatus_Object = MibTableColumn
clabTopoChFnCfgRowStatus = _ClabTopoChFnCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 2),
    _ClabTopoChFnCfgRowStatus_Type()
)
clabTopoChFnCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabTopoChFnCfgRowStatus.setStatus("current")
_ClabTopoMibConformance_ObjectIdentity = ObjectIdentity
clabTopoMibConformance = _ClabTopoMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 2)
)
_ClabTopoMibCompliances_ObjectIdentity = ObjectIdentity
clabTopoMibCompliances = _ClabTopoMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1)
)
_ClabTopoMibGroups_ObjectIdentity = ObjectIdentity
clabTopoMibGroups = _ClabTopoMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2)
)

# Managed Objects groups

clabTopoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2, 1)
)
clabTopoGroup.setObjects(
      *(("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeDescr"),
        ("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgRowStatus"),
        ("CLAB-TOPO-MIB", "clabTopoChFnCfgRowStatus"))
)
if mibBuilder.loadTexts:
    clabTopoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabTopoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clabTopoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-TOPO-MIB",
    **{"NodeName": NodeName,
       "clabTopoMib": clabTopoMib,
       "clabTopoMibObjects": clabTopoMibObjects,
       "clabTopoFiberNodeCfgTable": clabTopoFiberNodeCfgTable,
       "clabTopoFiberNodeCfgEntry": clabTopoFiberNodeCfgEntry,
       "clabTopoFiberNodeCfgNodeName": clabTopoFiberNodeCfgNodeName,
       "clabTopoFiberNodeCfgNodeDescr": clabTopoFiberNodeCfgNodeDescr,
       "clabTopoFiberNodeCfgRowStatus": clabTopoFiberNodeCfgRowStatus,
       "clabTopoChFnCfgTable": clabTopoChFnCfgTable,
       "clabTopoChFnCfgEntry": clabTopoChFnCfgEntry,
       "clabTopoChFnCfgChIfIndex": clabTopoChFnCfgChIfIndex,
       "clabTopoChFnCfgRowStatus": clabTopoChFnCfgRowStatus,
       "clabTopoMibConformance": clabTopoMibConformance,
       "clabTopoMibCompliances": clabTopoMibCompliances,
       "clabTopoCompliance": clabTopoCompliance,
       "clabTopoMibGroups": clabTopoMibGroups,
       "clabTopoGroup": clabTopoGroup}
)
