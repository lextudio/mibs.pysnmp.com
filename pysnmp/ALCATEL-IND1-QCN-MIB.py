# SNMP MIB module (ALCATEL-IND1-QCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-QCN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:53 2024
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

(softentIND1QcnMib,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1QcnMib")

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

alcatelIND1QcnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1)
)
alcatelIND1QcnMIB.setRevisions(
        ("2011-09-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1QcnMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1QcnMIBObjects = _AlcatelIND1QcnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1QcnMIBObjects.setStatus("current")
_AlaQcnConfig_ObjectIdentity = ObjectIdentity
alaQcnConfig = _AlaQcnConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1)
)
_AlaQcnGlobalTable_Object = MibTable
alaQcnGlobalTable = _AlaQcnGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaQcnGlobalTable.setStatus("current")
_AlaQcnGlobalEntry_Object = MibTableRow
alaQcnGlobalEntry = _AlaQcnGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 1, 1)
)
alaQcnGlobalEntry.setIndexNames(
    (0, "ALCATEL-IND1-QCN-MIB", "alaQcnGlobalCompId"),
)
if mibBuilder.loadTexts:
    alaQcnGlobalEntry.setStatus("current")


class _AlaQcnGlobalCompId_Type(Integer32):
    """Custom type alaQcnGlobalCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaQcnGlobalCompId_Type.__name__ = "Integer32"
_AlaQcnGlobalCompId_Object = MibTableColumn
alaQcnGlobalCompId = _AlaQcnGlobalCompId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 1, 1, 1),
    _AlaQcnGlobalCompId_Type()
)
alaQcnGlobalCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQcnGlobalCompId.setStatus("current")


class _AlaQcnGlobalCNMVlanTag_Type(Integer32):
    """Custom type alaQcnGlobalCNMVlanTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaQcnGlobalCNMVlanTag_Type.__name__ = "Integer32"
_AlaQcnGlobalCNMVlanTag_Object = MibTableColumn
alaQcnGlobalCNMVlanTag = _AlaQcnGlobalCNMVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 1, 1, 2),
    _AlaQcnGlobalCNMVlanTag_Type()
)
alaQcnGlobalCNMVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQcnGlobalCNMVlanTag.setStatus("current")


class _AlaQcnGlobalCID_Type(Integer32):
    """Custom type alaQcnGlobalCID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AlaQcnGlobalCID_Type.__name__ = "Integer32"
_AlaQcnGlobalCID_Object = MibTableColumn
alaQcnGlobalCID = _AlaQcnGlobalCID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 1, 1, 3),
    _AlaQcnGlobalCID_Type()
)
alaQcnGlobalCID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQcnGlobalCID.setStatus("current")
_AlaQcnPortInstanceTable_Object = MibTable
alaQcnPortInstanceTable = _AlaQcnPortInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaQcnPortInstanceTable.setStatus("current")
_AlaQcnPortInstanceEntry_Object = MibTableRow
alaQcnPortInstanceEntry = _AlaQcnPortInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2, 1)
)
alaQcnPortInstanceEntry.setIndexNames(
    (0, "ALCATEL-IND1-QCN-MIB", "alaQcnPIIfIndex"),
    (0, "ALCATEL-IND1-QCN-MIB", "alaQcnPIPriority"),
)
if mibBuilder.loadTexts:
    alaQcnPortInstanceEntry.setStatus("current")
_AlaQcnPIIfIndex_Type = Unsigned32
_AlaQcnPIIfIndex_Object = MibTableColumn
alaQcnPIIfIndex = _AlaQcnPIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2, 1, 1),
    _AlaQcnPIIfIndex_Type()
)
alaQcnPIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQcnPIIfIndex.setStatus("current")
_AlaQcnPIPriority_Type = Unsigned32
_AlaQcnPIPriority_Object = MibTableColumn
alaQcnPIPriority = _AlaQcnPIPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2, 1, 2),
    _AlaQcnPIPriority_Type()
)
alaQcnPIPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaQcnPIPriority.setStatus("current")


class _AlaQcnPIPriorityReset_Type(TruthValue):
    """Custom type alaQcnPIPriorityReset based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_AlaQcnPIPriorityReset_Type.__name__ = "TruthValue"
_AlaQcnPIPriorityReset_Object = MibTableColumn
alaQcnPIPriorityReset = _AlaQcnPIPriorityReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2, 1, 3),
    _AlaQcnPIPriorityReset_Type()
)
alaQcnPIPriorityReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQcnPIPriorityReset.setStatus("current")


class _AlaQcnPICncpStatsClear_Type(TruthValue):
    """Custom type alaQcnPICncpStatsClear based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_AlaQcnPICncpStatsClear_Type.__name__ = "TruthValue"
_AlaQcnPICncpStatsClear_Object = MibTableColumn
alaQcnPICncpStatsClear = _AlaQcnPICncpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2, 1, 4),
    _AlaQcnPICncpStatsClear_Type()
)
alaQcnPICncpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQcnPICncpStatsClear.setStatus("current")


class _AlaQcnPICncpReset_Type(TruthValue):
    """Custom type alaQcnPICncpReset based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_AlaQcnPICncpReset_Type.__name__ = "TruthValue"
_AlaQcnPICncpReset_Object = MibTableColumn
alaQcnPICncpReset = _AlaQcnPICncpReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 1, 2, 1, 5),
    _AlaQcnPICncpReset_Type()
)
alaQcnPICncpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaQcnPICncpReset.setStatus("current")
_AlaQcnConformance_ObjectIdentity = ObjectIdentity
alaQcnConformance = _AlaQcnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 1, 2)
)
_AlcatelIND1QcnMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1QcnMIBConformance = _AlcatelIND1QcnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1QcnMIBConformance.setStatus("current")
_AlcatelIND1QcnMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1QcnMIBGroups = _AlcatelIND1QcnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1QcnMIBGroups.setStatus("current")
_AlcatelIND1QcnMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1QcnMIBCompliances = _AlcatelIND1QcnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1QcnMIBCompliances.setStatus("current")

# Managed Objects groups

alaQcnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 2, 1, 1)
)
alaQcnGlobalGroup.setObjects(
      *(("ALCATEL-IND1-QCN-MIB", "alaQcnGlobalCNMVlanTag"),
        ("ALCATEL-IND1-QCN-MIB", "alaQcnGlobalCID"))
)
if mibBuilder.loadTexts:
    alaQcnGlobalGroup.setStatus("current")

alaQcnPortInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 2, 1, 2)
)
alaQcnPortInstanceGroup.setObjects(
      *(("ALCATEL-IND1-QCN-MIB", "alaQcnPIPriorityReset"),
        ("ALCATEL-IND1-QCN-MIB", "alaQcnPICncpStatsClear"),
        ("ALCATEL-IND1-QCN-MIB", "alaQcnPICncpReset"))
)
if mibBuilder.loadTexts:
    alaQcnPortInstanceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1QcnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 71, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1QcnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-QCN-MIB",
    **{"alcatelIND1QcnMIB": alcatelIND1QcnMIB,
       "alcatelIND1QcnMIBObjects": alcatelIND1QcnMIBObjects,
       "alaQcnConfig": alaQcnConfig,
       "alaQcnGlobalTable": alaQcnGlobalTable,
       "alaQcnGlobalEntry": alaQcnGlobalEntry,
       "alaQcnGlobalCompId": alaQcnGlobalCompId,
       "alaQcnGlobalCNMVlanTag": alaQcnGlobalCNMVlanTag,
       "alaQcnGlobalCID": alaQcnGlobalCID,
       "alaQcnPortInstanceTable": alaQcnPortInstanceTable,
       "alaQcnPortInstanceEntry": alaQcnPortInstanceEntry,
       "alaQcnPIIfIndex": alaQcnPIIfIndex,
       "alaQcnPIPriority": alaQcnPIPriority,
       "alaQcnPIPriorityReset": alaQcnPIPriorityReset,
       "alaQcnPICncpStatsClear": alaQcnPICncpStatsClear,
       "alaQcnPICncpReset": alaQcnPICncpReset,
       "alaQcnConformance": alaQcnConformance,
       "alcatelIND1QcnMIBConformance": alcatelIND1QcnMIBConformance,
       "alcatelIND1QcnMIBGroups": alcatelIND1QcnMIBGroups,
       "alaQcnGlobalGroup": alaQcnGlobalGroup,
       "alaQcnPortInstanceGroup": alaQcnPortInstanceGroup,
       "alcatelIND1QcnMIBCompliances": alcatelIND1QcnMIBCompliances,
       "alcatelIND1QcnMIBCompliance": alcatelIND1QcnMIBCompliance}
)
