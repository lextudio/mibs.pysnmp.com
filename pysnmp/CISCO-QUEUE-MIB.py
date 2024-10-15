# SNMP MIB module (CISCO-QUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-QUEUE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:24 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoQueueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 37)
)
ciscoQueueMIB.setRevisions(
        ("1995-08-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CQAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("custom", 3),
          ("fifo", 1),
          ("priority", 2),
          ("weightedFair", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoQueueObjects_ObjectIdentity = ObjectIdentity
ciscoQueueObjects = _CiscoQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1)
)
_CQIfTable_Object = MibTable
cQIfTable = _CQIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1)
)
if mibBuilder.loadTexts:
    cQIfTable.setStatus("current")
_CQIfEntry_Object = MibTableRow
cQIfEntry = _CQIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1)
)
cQIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cQIfEntry.setStatus("current")
_CQIfQType_Type = CQAlgorithm
_CQIfQType_Object = MibTableColumn
cQIfQType = _CQIfQType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 1),
    _CQIfQType_Type()
)
cQIfQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQIfQType.setStatus("current")
_CQIfTxLimit_Type = Integer32
_CQIfTxLimit_Object = MibTableColumn
cQIfTxLimit = _CQIfTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 2),
    _CQIfTxLimit_Type()
)
cQIfTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQIfTxLimit.setStatus("current")
_CQIfSubqueues_Type = Integer32
_CQIfSubqueues_Object = MibTableColumn
cQIfSubqueues = _CQIfSubqueues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 3),
    _CQIfSubqueues_Type()
)
cQIfSubqueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQIfSubqueues.setStatus("current")
_CQStatsTable_Object = MibTable
cQStatsTable = _CQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2)
)
if mibBuilder.loadTexts:
    cQStatsTable.setStatus("current")
_CQStatsEntry_Object = MibTableRow
cQStatsEntry = _CQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1)
)
cQStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"),
)
if mibBuilder.loadTexts:
    cQStatsEntry.setStatus("current")


class _CQStatsQNumber_Type(Integer32):
    """Custom type cQStatsQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CQStatsQNumber_Type.__name__ = "Integer32"
_CQStatsQNumber_Object = MibTableColumn
cQStatsQNumber = _CQStatsQNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 1),
    _CQStatsQNumber_Type()
)
cQStatsQNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cQStatsQNumber.setStatus("current")
_CQStatsDepth_Type = Gauge32
_CQStatsDepth_Object = MibTableColumn
cQStatsDepth = _CQStatsDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 2),
    _CQStatsDepth_Type()
)
cQStatsDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQStatsDepth.setStatus("current")
_CQStatsMaxDepth_Type = Integer32
_CQStatsMaxDepth_Object = MibTableColumn
cQStatsMaxDepth = _CQStatsMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 3),
    _CQStatsMaxDepth_Type()
)
cQStatsMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQStatsMaxDepth.setStatus("current")
_CQStatsDiscards_Type = Counter32
_CQStatsDiscards_Object = MibTableColumn
cQStatsDiscards = _CQStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 4),
    _CQStatsDiscards_Type()
)
cQStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQStatsDiscards.setStatus("current")
_CQRotationTable_Object = MibTable
cQRotationTable = _CQRotationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3)
)
if mibBuilder.loadTexts:
    cQRotationTable.setStatus("current")
_CQRotationEntry_Object = MibTableRow
cQRotationEntry = _CQRotationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1)
)
cQRotationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"),
)
if mibBuilder.loadTexts:
    cQRotationEntry.setStatus("current")
_CQRotationOctets_Type = Integer32
_CQRotationOctets_Object = MibTableColumn
cQRotationOctets = _CQRotationOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1, 1),
    _CQRotationOctets_Type()
)
cQRotationOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cQRotationOctets.setStatus("current")
_CiscoQueueTraps_ObjectIdentity = ObjectIdentity
ciscoQueueTraps = _CiscoQueueTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 2)
)
_CiscoQueueConformance_ObjectIdentity = ObjectIdentity
ciscoQueueConformance = _CiscoQueueConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3)
)
_CQCompliances_ObjectIdentity = ObjectIdentity
cQCompliances = _CQCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1)
)
_CQGroups_ObjectIdentity = ObjectIdentity
cQGroups = _CQGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2)
)

# Managed Objects groups

cQIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 1)
)
cQIfGroup.setObjects(
      *(("CISCO-QUEUE-MIB", "cQIfQType"),
        ("CISCO-QUEUE-MIB", "cQIfTxLimit"),
        ("CISCO-QUEUE-MIB", "cQIfSubqueues"))
)
if mibBuilder.loadTexts:
    cQIfGroup.setStatus("current")

cQStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 2)
)
cQStatsGroup.setObjects(
      *(("CISCO-QUEUE-MIB", "cQStatsDepth"),
        ("CISCO-QUEUE-MIB", "cQStatsMaxDepth"),
        ("CISCO-QUEUE-MIB", "cQStatsDiscards"))
)
if mibBuilder.loadTexts:
    cQStatsGroup.setStatus("current")

cQRotationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 3)
)
cQRotationGroup.setObjects(
    ("CISCO-QUEUE-MIB", "cQRotationOctets")
)
if mibBuilder.loadTexts:
    cQRotationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cQCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cQCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QUEUE-MIB",
    **{"CQAlgorithm": CQAlgorithm,
       "ciscoQueueMIB": ciscoQueueMIB,
       "ciscoQueueObjects": ciscoQueueObjects,
       "cQIfTable": cQIfTable,
       "cQIfEntry": cQIfEntry,
       "cQIfQType": cQIfQType,
       "cQIfTxLimit": cQIfTxLimit,
       "cQIfSubqueues": cQIfSubqueues,
       "cQStatsTable": cQStatsTable,
       "cQStatsEntry": cQStatsEntry,
       "cQStatsQNumber": cQStatsQNumber,
       "cQStatsDepth": cQStatsDepth,
       "cQStatsMaxDepth": cQStatsMaxDepth,
       "cQStatsDiscards": cQStatsDiscards,
       "cQRotationTable": cQRotationTable,
       "cQRotationEntry": cQRotationEntry,
       "cQRotationOctets": cQRotationOctets,
       "ciscoQueueTraps": ciscoQueueTraps,
       "ciscoQueueConformance": ciscoQueueConformance,
       "cQCompliances": cQCompliances,
       "cQCompliance": cQCompliance,
       "cQGroups": cQGroups,
       "cQIfGroup": cQIfGroup,
       "cQStatsGroup": cQStatsGroup,
       "cQRotationGroup": cQRotationGroup}
)
