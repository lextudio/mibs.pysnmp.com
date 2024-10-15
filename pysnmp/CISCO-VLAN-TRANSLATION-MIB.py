# SNMP MIB module (CISCO-VLAN-TRANSLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VLAN-TRANSLATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:09 2024
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

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

ciscoVlanTranslationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411)
)
ciscoVlanTranslationMIB.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVlanTranslationMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVlanTranslationMIBNotifs = _CiscoVlanTranslationMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 0)
)
_CiscoVlanTranslationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVlanTranslationMIBObjects = _CiscoVlanTranslationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1)
)
_CvtGlobalTranslation_ObjectIdentity = ObjectIdentity
cvtGlobalTranslation = _CvtGlobalTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1)
)
_CvtGlobalTranslationMax_Type = Unsigned32
_CvtGlobalTranslationMax_Object = MibScalar
cvtGlobalTranslationMax = _CvtGlobalTranslationMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 1),
    _CvtGlobalTranslationMax_Type()
)
cvtGlobalTranslationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtGlobalTranslationMax.setStatus("current")
_CvtGlobalTranslationTable_Object = MibTable
cvtGlobalTranslationTable = _CvtGlobalTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvtGlobalTranslationTable.setStatus("current")
_CvtGlobalTranslationEntry_Object = MibTableRow
cvtGlobalTranslationEntry = _CvtGlobalTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1)
)
cvtGlobalTranslationEntry.setIndexNames(
    (0, "CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalOriginalVlan"),
)
if mibBuilder.loadTexts:
    cvtGlobalTranslationEntry.setStatus("current")
_CvtGlobalOriginalVlan_Type = VlanIndex
_CvtGlobalOriginalVlan_Object = MibTableColumn
cvtGlobalOriginalVlan = _CvtGlobalOriginalVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 1),
    _CvtGlobalOriginalVlan_Type()
)
cvtGlobalOriginalVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtGlobalOriginalVlan.setStatus("current")
_CvtGlobalTranslatedVlan_Type = VlanIndex
_CvtGlobalTranslatedVlan_Object = MibTableColumn
cvtGlobalTranslatedVlan = _CvtGlobalTranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 2),
    _CvtGlobalTranslatedVlan_Type()
)
cvtGlobalTranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtGlobalTranslatedVlan.setStatus("current")
_CvtGlobalTranslationEffective_Type = TruthValue
_CvtGlobalTranslationEffective_Object = MibTableColumn
cvtGlobalTranslationEffective = _CvtGlobalTranslationEffective_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 3),
    _CvtGlobalTranslationEffective_Type()
)
cvtGlobalTranslationEffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtGlobalTranslationEffective.setStatus("current")
_CvtGlobalTranslationStatus_Type = RowStatus
_CvtGlobalTranslationStatus_Object = MibTableColumn
cvtGlobalTranslationStatus = _CvtGlobalTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 4),
    _CvtGlobalTranslationStatus_Type()
)
cvtGlobalTranslationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtGlobalTranslationStatus.setStatus("current")
_CvtPortBasedTranslation_ObjectIdentity = ObjectIdentity
cvtPortBasedTranslation = _CvtPortBasedTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2)
)
_CvtPortConfigTable_Object = MibTable
cvtPortConfigTable = _CvtPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvtPortConfigTable.setStatus("current")
_CvtPortConfigEntry_Object = MibTableRow
cvtPortConfigEntry = _CvtPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1)
)
cvtPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvtPortConfigEntry.setStatus("current")
_CvtPortTranslationEnabled_Type = TruthValue
_CvtPortTranslationEnabled_Object = MibTableColumn
cvtPortTranslationEnabled = _CvtPortTranslationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1, 1),
    _CvtPortTranslationEnabled_Type()
)
cvtPortTranslationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortTranslationEnabled.setStatus("current")
_CvtPortTranslationMax_Type = Unsigned32
_CvtPortTranslationMax_Object = MibTableColumn
cvtPortTranslationMax = _CvtPortTranslationMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1, 2),
    _CvtPortTranslationMax_Type()
)
cvtPortTranslationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortTranslationMax.setStatus("current")
_CvtPortTranslationTable_Object = MibTable
cvtPortTranslationTable = _CvtPortTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvtPortTranslationTable.setStatus("current")
_CvtPortTranslationEntry_Object = MibTableRow
cvtPortTranslationEntry = _CvtPortTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1)
)
cvtPortTranslationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VLAN-TRANSLATION-MIB", "cvtPortOriginalVlan"),
)
if mibBuilder.loadTexts:
    cvtPortTranslationEntry.setStatus("current")
_CvtPortOriginalVlan_Type = VlanIndex
_CvtPortOriginalVlan_Object = MibTableColumn
cvtPortOriginalVlan = _CvtPortOriginalVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 1),
    _CvtPortOriginalVlan_Type()
)
cvtPortOriginalVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtPortOriginalVlan.setStatus("current")
_CvtPortTranslatedVlan_Type = VlanIndex
_CvtPortTranslatedVlan_Object = MibTableColumn
cvtPortTranslatedVlan = _CvtPortTranslatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 2),
    _CvtPortTranslatedVlan_Type()
)
cvtPortTranslatedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtPortTranslatedVlan.setStatus("current")
_CvtPortTranslationStatus_Type = RowStatus
_CvtPortTranslationStatus_Object = MibTableColumn
cvtPortTranslationStatus = _CvtPortTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 3),
    _CvtPortTranslationStatus_Type()
)
cvtPortTranslationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtPortTranslationStatus.setStatus("current")
_CiscoVlanTranslationMIBConform_ObjectIdentity = ObjectIdentity
ciscoVlanTranslationMIBConform = _CiscoVlanTranslationMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 2)
)
_CvtMIBCompliances_ObjectIdentity = ObjectIdentity
cvtMIBCompliances = _CvtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 1)
)
_CvtMIBGroups_ObjectIdentity = ObjectIdentity
cvtMIBGroups = _CvtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2)
)

# Managed Objects groups

cvtGlobalTranslationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2, 1)
)
cvtGlobalTranslationGroup.setObjects(
      *(("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationMax"),
        ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslatedVlan"),
        ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationEffective"),
        ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationStatus"))
)
if mibBuilder.loadTexts:
    cvtGlobalTranslationGroup.setStatus("current")

cvtPortTranslationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2, 2)
)
cvtPortTranslationGroup.setObjects(
      *(("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationEnabled"),
        ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationMax"),
        ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslatedVlan"),
        ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationStatus"))
)
if mibBuilder.loadTexts:
    cvtPortTranslationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-TRANSLATION-MIB",
    **{"ciscoVlanTranslationMIB": ciscoVlanTranslationMIB,
       "ciscoVlanTranslationMIBNotifs": ciscoVlanTranslationMIBNotifs,
       "ciscoVlanTranslationMIBObjects": ciscoVlanTranslationMIBObjects,
       "cvtGlobalTranslation": cvtGlobalTranslation,
       "cvtGlobalTranslationMax": cvtGlobalTranslationMax,
       "cvtGlobalTranslationTable": cvtGlobalTranslationTable,
       "cvtGlobalTranslationEntry": cvtGlobalTranslationEntry,
       "cvtGlobalOriginalVlan": cvtGlobalOriginalVlan,
       "cvtGlobalTranslatedVlan": cvtGlobalTranslatedVlan,
       "cvtGlobalTranslationEffective": cvtGlobalTranslationEffective,
       "cvtGlobalTranslationStatus": cvtGlobalTranslationStatus,
       "cvtPortBasedTranslation": cvtPortBasedTranslation,
       "cvtPortConfigTable": cvtPortConfigTable,
       "cvtPortConfigEntry": cvtPortConfigEntry,
       "cvtPortTranslationEnabled": cvtPortTranslationEnabled,
       "cvtPortTranslationMax": cvtPortTranslationMax,
       "cvtPortTranslationTable": cvtPortTranslationTable,
       "cvtPortTranslationEntry": cvtPortTranslationEntry,
       "cvtPortOriginalVlan": cvtPortOriginalVlan,
       "cvtPortTranslatedVlan": cvtPortTranslatedVlan,
       "cvtPortTranslationStatus": cvtPortTranslationStatus,
       "ciscoVlanTranslationMIBConform": ciscoVlanTranslationMIBConform,
       "cvtMIBCompliances": cvtMIBCompliances,
       "cvtMIBCompliance": cvtMIBCompliance,
       "cvtMIBGroups": cvtMIBGroups,
       "cvtGlobalTranslationGroup": cvtGlobalTranslationGroup,
       "cvtPortTranslationGroup": cvtPortTranslationGroup}
)
