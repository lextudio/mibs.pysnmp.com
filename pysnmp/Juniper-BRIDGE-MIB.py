# SNMP MIB module (Juniper-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:47 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63)
)
juniBridgeMIB.setRevisions(
        ("2003-11-04 20:39",
         "2002-09-16 21:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniBridgeIfLayer_ObjectIdentity = ObjectIdentity
juniBridgeIfLayer = _JuniBridgeIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1)
)
_JuniBridgeIfNextIfIndex_Type = JuniNextIfIndex
_JuniBridgeIfNextIfIndex_Object = MibScalar
juniBridgeIfNextIfIndex = _JuniBridgeIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 1),
    _JuniBridgeIfNextIfIndex_Type()
)
juniBridgeIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgeIfNextIfIndex.setStatus("current")
_JuniBridgeIfTable_Object = MibTable
juniBridgeIfTable = _JuniBridgeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2)
)
if mibBuilder.loadTexts:
    juniBridgeIfTable.setStatus("current")
_JuniBridgeIfEntry_Object = MibTableRow
juniBridgeIfEntry = _JuniBridgeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1)
)
juniBridgeIfEntry.setIndexNames(
    (0, "Juniper-BRIDGE-MIB", "juniBridgeIfIndex"),
)
if mibBuilder.loadTexts:
    juniBridgeIfEntry.setStatus("current")
_JuniBridgeIfIndex_Type = InterfaceIndex
_JuniBridgeIfIndex_Object = MibTableColumn
juniBridgeIfIndex = _JuniBridgeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 1),
    _JuniBridgeIfIndex_Type()
)
juniBridgeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBridgeIfIndex.setStatus("current")
_JuniBridgeIfRowStatus_Type = RowStatus
_JuniBridgeIfRowStatus_Object = MibTableColumn
juniBridgeIfRowStatus = _JuniBridgeIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 2),
    _JuniBridgeIfRowStatus_Type()
)
juniBridgeIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgeIfRowStatus.setStatus("current")
_JuniBridgeIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniBridgeIfLowerIfIndex_Object = MibTableColumn
juniBridgeIfLowerIfIndex = _JuniBridgeIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 3),
    _JuniBridgeIfLowerIfIndex_Type()
)
juniBridgeIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgeIfLowerIfIndex.setStatus("current")
_JuniBridgeSPolicyIndex_Type = Unsigned32
_JuniBridgeSPolicyIndex_Object = MibTableColumn
juniBridgeSPolicyIndex = _JuniBridgeSPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 4),
    _JuniBridgeSPolicyIndex_Type()
)
juniBridgeSPolicyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgeSPolicyIndex.setStatus("current")
_JuniBridgeIfMaxLearnCount_Type = Unsigned32
_JuniBridgeIfMaxLearnCount_Object = MibTableColumn
juniBridgeIfMaxLearnCount = _JuniBridgeIfMaxLearnCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 1, 2, 1, 5),
    _JuniBridgeIfMaxLearnCount_Type()
)
juniBridgeIfMaxLearnCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBridgeIfMaxLearnCount.setStatus("current")
_JuniBridgeAgeLayer_ObjectIdentity = ObjectIdentity
juniBridgeAgeLayer = _JuniBridgeAgeLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2)
)
_JuniBridgeAgeTable_Object = MibTable
juniBridgeAgeTable = _JuniBridgeAgeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1)
)
if mibBuilder.loadTexts:
    juniBridgeAgeTable.setStatus("current")
_JuniBridgeAgeEntry_Object = MibTableRow
juniBridgeAgeEntry = _JuniBridgeAgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1, 1)
)
juniBridgeAgeEntry.setIndexNames(
    (0, "Juniper-BRIDGE-MIB", "juniBridgeMacAddress"),
)
if mibBuilder.loadTexts:
    juniBridgeAgeEntry.setStatus("current")
_JuniBridgeMacAddress_Type = MacAddress
_JuniBridgeMacAddress_Object = MibTableColumn
juniBridgeMacAddress = _JuniBridgeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1, 1, 1),
    _JuniBridgeMacAddress_Type()
)
juniBridgeMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBridgeMacAddress.setStatus("current")
_JuniBridgeAge_Type = Unsigned32
_JuniBridgeAge_Object = MibTableColumn
juniBridgeAge = _JuniBridgeAge_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 2, 1, 1, 2),
    _JuniBridgeAge_Type()
)
juniBridgeAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgeAge.setStatus("current")
_JuniBridgeMiscCounters_ObjectIdentity = ObjectIdentity
juniBridgeMiscCounters = _JuniBridgeMiscCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 3)
)
_JuniBridgeDupMacCounter_Type = Counter32
_JuniBridgeDupMacCounter_Object = MibScalar
juniBridgeDupMacCounter = _JuniBridgeDupMacCounter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 3, 1),
    _JuniBridgeDupMacCounter_Type()
)
juniBridgeDupMacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBridgeDupMacCounter.setStatus("current")
_JuniBridgeConformance_ObjectIdentity = ObjectIdentity
juniBridgeConformance = _JuniBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4)
)
_JuniBridgeCompliances_ObjectIdentity = ObjectIdentity
juniBridgeCompliances = _JuniBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 1)
)
_JuniBridgeGroups_ObjectIdentity = ObjectIdentity
juniBridgeGroups = _JuniBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 2)
)

# Managed Objects groups

juniBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 2, 1)
)
juniBridgeGroup.setObjects(
      *(("Juniper-BRIDGE-MIB", "juniBridgeIfNextIfIndex"),
        ("Juniper-BRIDGE-MIB", "juniBridgeIfRowStatus"),
        ("Juniper-BRIDGE-MIB", "juniBridgeIfLowerIfIndex"),
        ("Juniper-BRIDGE-MIB", "juniBridgeSPolicyIndex"),
        ("Juniper-BRIDGE-MIB", "juniBridgeIfMaxLearnCount"),
        ("Juniper-BRIDGE-MIB", "juniBridgeAge"),
        ("Juniper-BRIDGE-MIB", "juniBridgeDupMacCounter"))
)
if mibBuilder.loadTexts:
    juniBridgeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 63, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-BRIDGE-MIB",
    **{"juniBridgeMIB": juniBridgeMIB,
       "juniBridgeIfLayer": juniBridgeIfLayer,
       "juniBridgeIfNextIfIndex": juniBridgeIfNextIfIndex,
       "juniBridgeIfTable": juniBridgeIfTable,
       "juniBridgeIfEntry": juniBridgeIfEntry,
       "juniBridgeIfIndex": juniBridgeIfIndex,
       "juniBridgeIfRowStatus": juniBridgeIfRowStatus,
       "juniBridgeIfLowerIfIndex": juniBridgeIfLowerIfIndex,
       "juniBridgeSPolicyIndex": juniBridgeSPolicyIndex,
       "juniBridgeIfMaxLearnCount": juniBridgeIfMaxLearnCount,
       "juniBridgeAgeLayer": juniBridgeAgeLayer,
       "juniBridgeAgeTable": juniBridgeAgeTable,
       "juniBridgeAgeEntry": juniBridgeAgeEntry,
       "juniBridgeMacAddress": juniBridgeMacAddress,
       "juniBridgeAge": juniBridgeAge,
       "juniBridgeMiscCounters": juniBridgeMiscCounters,
       "juniBridgeDupMacCounter": juniBridgeDupMacCounter,
       "juniBridgeConformance": juniBridgeConformance,
       "juniBridgeCompliances": juniBridgeCompliances,
       "juniBridgeCompliance": juniBridgeCompliance,
       "juniBridgeGroups": juniBridgeGroups,
       "juniBridgeGroup": juniBridgeGroup}
)
