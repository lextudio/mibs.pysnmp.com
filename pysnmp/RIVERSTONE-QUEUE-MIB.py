# SNMP MIB module (RIVERSTONE-QUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-QUEUE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:50 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

(RsDiscardPolicy,) = mibBuilder.importSymbols(
    "RIVERSTONE-TC-MIB",
    "RsDiscardPolicy")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rsQueueMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70)
)
rsQueueMIB.setRevisions(
        ("2002-06-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IndexInteger(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_RsQueueMIBObjects_ObjectIdentity = ObjectIdentity
rsQueueMIBObjects = _RsQueueMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1)
)
_RsQueuePropertiesTable_Object = MibTable
rsQueuePropertiesTable = _RsQueuePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1)
)
if mibBuilder.loadTexts:
    rsQueuePropertiesTable.setStatus("current")
_RsQueuePropertiesEntry_Object = MibTableRow
rsQueuePropertiesEntry = _RsQueuePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1)
)
rsQueuePropertiesEntry.setIndexNames(
    (0, "RIVERSTONE-QUEUE-MIB", "rsQueueId"),
)
if mibBuilder.loadTexts:
    rsQueuePropertiesEntry.setStatus("current")
_RsQueueId_Type = IndexInteger
_RsQueueId_Object = MibTableColumn
rsQueueId = _RsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 1),
    _RsQueueId_Type()
)
rsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsQueueId.setStatus("current")
_RsQueueName_Type = SnmpAdminString
_RsQueueName_Object = MibTableColumn
rsQueueName = _RsQueueName_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 2),
    _RsQueueName_Type()
)
rsQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueName.setStatus("current")
_RsQueueDescr_Type = SnmpAdminString
_RsQueueDescr_Object = MibTableColumn
rsQueueDescr = _RsQueueDescr_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 3),
    _RsQueueDescr_Type()
)
rsQueueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueDescr.setStatus("current")
_RsQueueDiscardPolicy_Type = RsDiscardPolicy
_RsQueueDiscardPolicy_Object = MibTableColumn
rsQueueDiscardPolicy = _RsQueueDiscardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 4),
    _RsQueueDiscardPolicy_Type()
)
rsQueueDiscardPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueDiscardPolicy.setStatus("current")
_RsQueueMaxCapacity_Type = Gauge32
_RsQueueMaxCapacity_Object = MibTableColumn
rsQueueMaxCapacity = _RsQueueMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 1, 1, 6),
    _RsQueueMaxCapacity_Type()
)
rsQueueMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueMaxCapacity.setStatus("current")
_RsQueueStatsTable_Object = MibTable
rsQueueStatsTable = _RsQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2)
)
if mibBuilder.loadTexts:
    rsQueueStatsTable.setStatus("current")
_RsQueueStatsEntry_Object = MibTableRow
rsQueueStatsEntry = _RsQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1)
)
rsQueueStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RIVERSTONE-QUEUE-MIB", "rsQueueId"),
)
if mibBuilder.loadTexts:
    rsQueueStatsEntry.setStatus("current")
_RsQueueStatsLastCapChange_Type = TimeStamp
_RsQueueStatsLastCapChange_Object = MibTableColumn
rsQueueStatsLastCapChange = _RsQueueStatsLastCapChange_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 1),
    _RsQueueStatsLastCapChange_Type()
)
rsQueueStatsLastCapChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueStatsLastCapChange.setStatus("current")


class _RsQueueStatsValid_Type(Bits):
    """Custom type rsQueueStatsValid based on Bits"""
    namedValues = NamedValues(
        *(("validBytes", 0),
          ("validDiscards", 2),
          ("validFrames", 1),
          ("validHCBytes", 3),
          ("validHCFrames", 4))
    )

_RsQueueStatsValid_Type.__name__ = "Bits"
_RsQueueStatsValid_Object = MibTableColumn
rsQueueStatsValid = _RsQueueStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 2),
    _RsQueueStatsValid_Type()
)
rsQueueStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueStatsValid.setStatus("current")
_RsQueueBytes_Type = Counter32
_RsQueueBytes_Object = MibTableColumn
rsQueueBytes = _RsQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 101),
    _RsQueueBytes_Type()
)
rsQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueBytes.setStatus("current")
_RsQueueFrames_Type = Counter32
_RsQueueFrames_Object = MibTableColumn
rsQueueFrames = _RsQueueFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 102),
    _RsQueueFrames_Type()
)
rsQueueFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueFrames.setStatus("current")
_RsQueueDiscards_Type = Counter32
_RsQueueDiscards_Object = MibTableColumn
rsQueueDiscards = _RsQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 103),
    _RsQueueDiscards_Type()
)
rsQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueDiscards.setStatus("current")
_RsQueueHCBytes_Type = Counter64
_RsQueueHCBytes_Object = MibTableColumn
rsQueueHCBytes = _RsQueueHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 201),
    _RsQueueHCBytes_Type()
)
rsQueueHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueHCBytes.setStatus("current")
_RsQueueHCFrames_Type = Counter64
_RsQueueHCFrames_Object = MibTableColumn
rsQueueHCFrames = _RsQueueHCFrames_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 1, 2, 1, 202),
    _RsQueueHCFrames_Type()
)
rsQueueHCFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsQueueHCFrames.setStatus("current")
_RsQueueConformance_ObjectIdentity = ObjectIdentity
rsQueueConformance = _RsQueueConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 2)
)
_RsQueueCompliances_ObjectIdentity = ObjectIdentity
rsQueueCompliances = _RsQueueCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 1)
)
_RsQueueGroups_ObjectIdentity = ObjectIdentity
rsQueueGroups = _RsQueueGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 2)
)

# Managed Objects groups

rsQueuePropertiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 2, 1)
)
rsQueuePropertiesGroup.setObjects(
      *(("RIVERSTONE-QUEUE-MIB", "rsQueueName"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueDescr"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueDiscardPolicy"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueMaxCapacity"))
)
if mibBuilder.loadTexts:
    rsQueuePropertiesGroup.setStatus("current")

rsQueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 2, 2)
)
rsQueueStatsGroup.setObjects(
      *(("RIVERSTONE-QUEUE-MIB", "rsQueueStatsLastCapChange"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueStatsValid"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueBytes"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueFrames"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueDiscards"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueHCBytes"),
        ("RIVERSTONE-QUEUE-MIB", "rsQueueHCFrames"))
)
if mibBuilder.loadTexts:
    rsQueueStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsQueueCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 70, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsQueueCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-QUEUE-MIB",
    **{"IndexInteger": IndexInteger,
       "rsQueueMIB": rsQueueMIB,
       "rsQueueMIBObjects": rsQueueMIBObjects,
       "rsQueuePropertiesTable": rsQueuePropertiesTable,
       "rsQueuePropertiesEntry": rsQueuePropertiesEntry,
       "rsQueueId": rsQueueId,
       "rsQueueName": rsQueueName,
       "rsQueueDescr": rsQueueDescr,
       "rsQueueDiscardPolicy": rsQueueDiscardPolicy,
       "rsQueueMaxCapacity": rsQueueMaxCapacity,
       "rsQueueStatsTable": rsQueueStatsTable,
       "rsQueueStatsEntry": rsQueueStatsEntry,
       "rsQueueStatsLastCapChange": rsQueueStatsLastCapChange,
       "rsQueueStatsValid": rsQueueStatsValid,
       "rsQueueBytes": rsQueueBytes,
       "rsQueueFrames": rsQueueFrames,
       "rsQueueDiscards": rsQueueDiscards,
       "rsQueueHCBytes": rsQueueHCBytes,
       "rsQueueHCFrames": rsQueueHCFrames,
       "rsQueueConformance": rsQueueConformance,
       "rsQueueCompliances": rsQueueCompliances,
       "rsQueueCompliance": rsQueueCompliance,
       "rsQueueGroups": rsQueueGroups,
       "rsQueuePropertiesGroup": rsQueuePropertiesGroup,
       "rsQueueStatsGroup": rsQueueStatsGroup}
)
