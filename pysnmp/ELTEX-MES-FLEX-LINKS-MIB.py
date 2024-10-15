# SNMP MIB module (ELTEX-MES-FLEX-LINKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-FLEX-LINKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:40 2024
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

eltMesFlexLinksMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5)
)
eltMesFlexLinksMIB.setRevisions(
        ("2015-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesFlexLinksMIBNotifs_ObjectIdentity = ObjectIdentity
eltMesFlexLinksMIBNotifs = _EltMesFlexLinksMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 0)
)
_EltMesFlexLinksMIBObjects_ObjectIdentity = ObjectIdentity
eltMesFlexLinksMIBObjects = _EltMesFlexLinksMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1)
)
_EltMesFlConfig_ObjectIdentity = ObjectIdentity
eltMesFlConfig = _EltMesFlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1)
)
_EltFlIfConfigTable_Object = MibTable
eltFlIfConfigTable = _EltFlIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltFlIfConfigTable.setStatus("deprecated")
_EltFlIfConfigEntry_Object = MibTableRow
eltFlIfConfigEntry = _EltFlIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 1, 1)
)
eltFlIfConfigEntry.setIndexNames(
    (0, "ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfConfigPrimary"),
)
if mibBuilder.loadTexts:
    eltFlIfConfigEntry.setStatus("deprecated")
_EltFlIfConfigPrimary_Type = InterfaceIndex
_EltFlIfConfigPrimary_Object = MibTableColumn
eltFlIfConfigPrimary = _EltFlIfConfigPrimary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 1, 1, 1),
    _EltFlIfConfigPrimary_Type()
)
eltFlIfConfigPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltFlIfConfigPrimary.setStatus("deprecated")
_EltFlIfConfigBackUp_Type = InterfaceIndexOrZero
_EltFlIfConfigBackUp_Object = MibTableColumn
eltFlIfConfigBackUp = _EltFlIfConfigBackUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 1, 1, 2),
    _EltFlIfConfigBackUp_Type()
)
eltFlIfConfigBackUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltFlIfConfigBackUp.setStatus("deprecated")
_EltFlEnableStatusChangeNotif_Type = TruthValue
_EltFlEnableStatusChangeNotif_Object = MibScalar
eltFlEnableStatusChangeNotif = _EltFlEnableStatusChangeNotif_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 2),
    _EltFlEnableStatusChangeNotif_Type()
)
eltFlEnableStatusChangeNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltFlEnableStatusChangeNotif.setStatus("deprecated")
_EltFlIfConfigExtTable_Object = MibTable
eltFlIfConfigExtTable = _EltFlIfConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltFlIfConfigExtTable.setStatus("deprecated")
_EltFlIfConfigExtEntry_Object = MibTableRow
eltFlIfConfigExtEntry = _EltFlIfConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 3, 1)
)
eltFlIfConfigExtEntry.setIndexNames(
    (0, "ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfConfigPrimary"),
)
if mibBuilder.loadTexts:
    eltFlIfConfigExtEntry.setStatus("deprecated")


class _EltFlIfConfigPreemptionMode_Type(Integer32):
    """Custom type eltFlIfConfigPreemptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 3),
          ("forced", 2),
          ("off", 1))
    )


_EltFlIfConfigPreemptionMode_Type.__name__ = "Integer32"
_EltFlIfConfigPreemptionMode_Object = MibTableColumn
eltFlIfConfigPreemptionMode = _EltFlIfConfigPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 3, 1, 1),
    _EltFlIfConfigPreemptionMode_Type()
)
eltFlIfConfigPreemptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltFlIfConfigPreemptionMode.setStatus("deprecated")
_EltFlIfConfigPreemptionDelay_Type = Unsigned32
_EltFlIfConfigPreemptionDelay_Object = MibTableColumn
eltFlIfConfigPreemptionDelay = _EltFlIfConfigPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 1, 3, 1, 2),
    _EltFlIfConfigPreemptionDelay_Type()
)
eltFlIfConfigPreemptionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltFlIfConfigPreemptionDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    eltFlIfConfigPreemptionDelay.setUnits("seconds")
_EltMesFlStatus_ObjectIdentity = ObjectIdentity
eltMesFlStatus = _EltMesFlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 2)
)
_EltFlIfStatusTable_Object = MibTable
eltFlIfStatusTable = _EltFlIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltFlIfStatusTable.setStatus("deprecated")
_EltFlIfStatusEntry_Object = MibTableRow
eltFlIfStatusEntry = _EltFlIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 2, 1, 1)
)
eltFlIfStatusEntry.setIndexNames(
    (0, "ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfIndex"),
)
if mibBuilder.loadTexts:
    eltFlIfStatusEntry.setStatus("deprecated")
_EltFlIfIndex_Type = InterfaceIndex
_EltFlIfIndex_Object = MibTableColumn
eltFlIfIndex = _EltFlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 2, 1, 1, 1),
    _EltFlIfIndex_Type()
)
eltFlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltFlIfIndex.setStatus("deprecated")


class _EltFlIfStatus_Type(Integer32):
    """Custom type eltFlIfStatus based on Integer32"""
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
        *(("blocking", 2),
          ("down", 3),
          ("forwarding", 1),
          ("unknown", 4))
    )


_EltFlIfStatus_Type.__name__ = "Integer32"
_EltFlIfStatus_Object = MibTableColumn
eltFlIfStatus = _EltFlIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 1, 2, 1, 1, 2),
    _EltFlIfStatus_Type()
)
eltFlIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltFlIfStatus.setStatus("deprecated")
_EltMesFlexLinksMIBConformance_ObjectIdentity = ObjectIdentity
eltMesFlexLinksMIBConformance = _EltMesFlexLinksMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2)
)
_EltMesFlexLinksMIBCompliances_ObjectIdentity = ObjectIdentity
eltMesFlexLinksMIBCompliances = _EltMesFlexLinksMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 1)
)
_EltMesFlexLinksMIBGroups_ObjectIdentity = ObjectIdentity
eltMesFlexLinksMIBGroups = _EltMesFlexLinksMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 2)
)

# Managed Objects groups

eltFlexLinksIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 2, 1)
)
eltFlexLinksIfConfigGroup.setObjects(
    ("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfConfigBackUp")
)
if mibBuilder.loadTexts:
    eltFlexLinksIfConfigGroup.setStatus("deprecated")

eltFlexLinksIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 2, 2)
)
eltFlexLinksIfStatusGroup.setObjects(
    ("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfStatus")
)
if mibBuilder.loadTexts:
    eltFlexLinksIfStatusGroup.setStatus("deprecated")

eltFlexLinksEnableNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 2, 3)
)
eltFlexLinksEnableNotifGroup.setObjects(
    ("ELTEX-MES-FLEX-LINKS-MIB", "eltFlEnableStatusChangeNotif")
)
if mibBuilder.loadTexts:
    eltFlexLinksEnableNotifGroup.setStatus("deprecated")

eltFlexLinksPreemptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 2, 5)
)
eltFlexLinksPreemptionGroup.setObjects(
      *(("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfConfigPreemptionMode"),
        ("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfConfigPreemptionDelay"))
)
if mibBuilder.loadTexts:
    eltFlexLinksPreemptionGroup.setStatus("deprecated")


# Notification objects

eltFlIfStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 0, 1)
)
eltFlIfStatusChangeNotif.setObjects(
      *(("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfIndex"),
        ("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfStatus"))
)
if mibBuilder.loadTexts:
    eltFlIfStatusChangeNotif.setStatus(
        "deprecated"
    )


# Notifications groups

eltFlexLinksNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 2, 4)
)
eltFlexLinksNotifGroup.setObjects(
    ("ELTEX-MES-FLEX-LINKS-MIB", "eltFlIfStatusChangeNotif")
)
if mibBuilder.loadTexts:
    eltFlexLinksNotifGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

eltFlexLinksMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltFlexLinksMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-FLEX-LINKS-MIB",
    **{"eltMesFlexLinksMIB": eltMesFlexLinksMIB,
       "eltMesFlexLinksMIBNotifs": eltMesFlexLinksMIBNotifs,
       "eltFlIfStatusChangeNotif": eltFlIfStatusChangeNotif,
       "eltMesFlexLinksMIBObjects": eltMesFlexLinksMIBObjects,
       "eltMesFlConfig": eltMesFlConfig,
       "eltFlIfConfigTable": eltFlIfConfigTable,
       "eltFlIfConfigEntry": eltFlIfConfigEntry,
       "eltFlIfConfigPrimary": eltFlIfConfigPrimary,
       "eltFlIfConfigBackUp": eltFlIfConfigBackUp,
       "eltFlEnableStatusChangeNotif": eltFlEnableStatusChangeNotif,
       "eltFlIfConfigExtTable": eltFlIfConfigExtTable,
       "eltFlIfConfigExtEntry": eltFlIfConfigExtEntry,
       "eltFlIfConfigPreemptionMode": eltFlIfConfigPreemptionMode,
       "eltFlIfConfigPreemptionDelay": eltFlIfConfigPreemptionDelay,
       "eltMesFlStatus": eltMesFlStatus,
       "eltFlIfStatusTable": eltFlIfStatusTable,
       "eltFlIfStatusEntry": eltFlIfStatusEntry,
       "eltFlIfIndex": eltFlIfIndex,
       "eltFlIfStatus": eltFlIfStatus,
       "eltMesFlexLinksMIBConformance": eltMesFlexLinksMIBConformance,
       "eltMesFlexLinksMIBCompliances": eltMesFlexLinksMIBCompliances,
       "eltFlexLinksMIBCompliance": eltFlexLinksMIBCompliance,
       "eltMesFlexLinksMIBGroups": eltMesFlexLinksMIBGroups,
       "eltFlexLinksIfConfigGroup": eltFlexLinksIfConfigGroup,
       "eltFlexLinksIfStatusGroup": eltFlexLinksIfStatusGroup,
       "eltFlexLinksEnableNotifGroup": eltFlexLinksEnableNotifGroup,
       "eltFlexLinksNotifGroup": eltFlexLinksNotifGroup,
       "eltFlexLinksPreemptionGroup": eltFlexLinksPreemptionGroup}
)
