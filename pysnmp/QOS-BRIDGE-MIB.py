# SNMP MIB module (QOS-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QOS-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:58 2024
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

(dot1qVlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dot1dQosMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 12346)
)
dot1dQosMib.setRevisions(
        ("2000-06-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot1dUserPri(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_Dot1dQosObjects_ObjectIdentity = ObjectIdentity
dot1dQosObjects = _Dot1dQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12346, 1)
)
_Dot1dQosTables_ObjectIdentity = ObjectIdentity
dot1dQosTables = _Dot1dQosTables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12346, 2)
)
_Dot1dQosUserPriTable_Object = MibTable
dot1dQosUserPriTable = _Dot1dQosUserPriTable_Object(
    (1, 3, 6, 1, 2, 1, 12346, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dQosUserPriTable.setStatus("current")
_Dot1dQosUserPriEntry_Object = MibTableRow
dot1dQosUserPriEntry = _Dot1dQosUserPriEntry_Object(
    (1, 3, 6, 1, 2, 1, 12346, 2, 1, 1)
)
dot1dQosUserPriEntry.setIndexNames(
    (0, "QOS-BRIDGE-MIB", "dot1dQosUserPri"),
)
if mibBuilder.loadTexts:
    dot1dQosUserPriEntry.setStatus("current")
_Dot1dQosUserPri_Type = Dot1dUserPri
_Dot1dQosUserPri_Object = MibTableColumn
dot1dQosUserPri = _Dot1dQosUserPri_Object(
    (1, 3, 6, 1, 2, 1, 12346, 2, 1, 1, 1),
    _Dot1dQosUserPri_Type()
)
dot1dQosUserPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dQosUserPri.setStatus("current")
_Dot1dQosVlanClfrTable_Object = MibTable
dot1dQosVlanClfrTable = _Dot1dQosVlanClfrTable_Object(
    (1, 3, 6, 1, 2, 1, 12346, 2, 2)
)
if mibBuilder.loadTexts:
    dot1dQosVlanClfrTable.setStatus("current")
_Dot1dQosVlanClfrEntry_Object = MibTableRow
dot1dQosVlanClfrEntry = _Dot1dQosVlanClfrEntry_Object(
    (1, 3, 6, 1, 2, 1, 12346, 2, 2, 1)
)
dot1dQosVlanClfrEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1dQosVlanClfrEntry.setStatus("current")
_Dot1dQosVlanStatus_Type = RowStatus
_Dot1dQosVlanStatus_Object = MibTableColumn
dot1dQosVlanStatus = _Dot1dQosVlanStatus_Object(
    (1, 3, 6, 1, 2, 1, 12346, 2, 2, 1, 1),
    _Dot1dQosVlanStatus_Type()
)
dot1dQosVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dQosVlanStatus.setStatus("current")
_Dot1dQosMIBConformance_ObjectIdentity = ObjectIdentity
dot1dQosMIBConformance = _Dot1dQosMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12346, 3)
)
_Dot1dQosMIBCompliances_ObjectIdentity = ObjectIdentity
dot1dQosMIBCompliances = _Dot1dQosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12346, 3, 1)
)
_Dot1dQosMIBGroups_ObjectIdentity = ObjectIdentity
dot1dQosMIBGroups = _Dot1dQosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 12346, 3, 2)
)

# Managed Objects groups

dot1dQosMIBUserPriGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12346, 3, 2, 1)
)
dot1dQosMIBUserPriGroup.setObjects(
    ("QOS-BRIDGE-MIB", "dot1dQosUserPri")
)
if mibBuilder.loadTexts:
    dot1dQosMIBUserPriGroup.setStatus("current")

dot1dQosMIBVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 12346, 3, 2, 2)
)
dot1dQosMIBVlanGroup.setObjects(
    ("QOS-BRIDGE-MIB", "dot1dQosVlanStatus")
)
if mibBuilder.loadTexts:
    dot1dQosMIBVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot1dQosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 12346, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dot1dQosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOS-BRIDGE-MIB",
    **{"Dot1dUserPri": Dot1dUserPri,
       "dot1dQosMib": dot1dQosMib,
       "dot1dQosObjects": dot1dQosObjects,
       "dot1dQosTables": dot1dQosTables,
       "dot1dQosUserPriTable": dot1dQosUserPriTable,
       "dot1dQosUserPriEntry": dot1dQosUserPriEntry,
       "dot1dQosUserPri": dot1dQosUserPri,
       "dot1dQosVlanClfrTable": dot1dQosVlanClfrTable,
       "dot1dQosVlanClfrEntry": dot1dQosVlanClfrEntry,
       "dot1dQosVlanStatus": dot1dQosVlanStatus,
       "dot1dQosMIBConformance": dot1dQosMIBConformance,
       "dot1dQosMIBCompliances": dot1dQosMIBCompliances,
       "dot1dQosMIBCompliance": dot1dQosMIBCompliance,
       "dot1dQosMIBGroups": dot1dQosMIBGroups,
       "dot1dQosMIBUserPriGroup": dot1dQosMIBUserPriGroup,
       "dot1dQosMIBVlanGroup": dot1dQosMIBVlanGroup}
)
