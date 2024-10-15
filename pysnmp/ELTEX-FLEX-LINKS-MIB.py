# SNMP MIB module (ELTEX-FLEX-LINKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-FLEX-LINKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:09 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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

eltexFlexLinksMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexFlexLinksMIBNotifs_ObjectIdentity = ObjectIdentity
eltexFlexLinksMIBNotifs = _EltexFlexLinksMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 0)
)
_EltexFlexLinksMIBObjects_ObjectIdentity = ObjectIdentity
eltexFlexLinksMIBObjects = _EltexFlexLinksMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1)
)
_EltexFlConfig_ObjectIdentity = ObjectIdentity
eltexFlConfig = _EltexFlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1)
)
_EltexFlIfConfigTable_Object = MibTable
eltexFlIfConfigTable = _EltexFlIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltexFlIfConfigTable.setStatus("current")
_EltexFlIfConfigEntry_Object = MibTableRow
eltexFlIfConfigEntry = _EltexFlIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 1, 1)
)
eltexFlIfConfigEntry.setIndexNames(
    (0, "ELTEX-FLEX-LINKS-MIB", "eltexFlIfConfigPrimary"),
)
if mibBuilder.loadTexts:
    eltexFlIfConfigEntry.setStatus("current")
_EltexFlIfConfigPrimary_Type = InterfaceIndex
_EltexFlIfConfigPrimary_Object = MibTableColumn
eltexFlIfConfigPrimary = _EltexFlIfConfigPrimary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 1, 1, 1),
    _EltexFlIfConfigPrimary_Type()
)
eltexFlIfConfigPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexFlIfConfigPrimary.setStatus("current")
_EltexFlIfConfigBackUp_Type = InterfaceIndexOrZero
_EltexFlIfConfigBackUp_Object = MibTableColumn
eltexFlIfConfigBackUp = _EltexFlIfConfigBackUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 1, 1, 2),
    _EltexFlIfConfigBackUp_Type()
)
eltexFlIfConfigBackUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexFlIfConfigBackUp.setStatus("current")
_EltexFlEnableStatusChangeNotif_Type = TruthValue
_EltexFlEnableStatusChangeNotif_Object = MibScalar
eltexFlEnableStatusChangeNotif = _EltexFlEnableStatusChangeNotif_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 2),
    _EltexFlEnableStatusChangeNotif_Type()
)
eltexFlEnableStatusChangeNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexFlEnableStatusChangeNotif.setStatus("current")
_EltexFlIfConfigExtTable_Object = MibTable
eltexFlIfConfigExtTable = _EltexFlIfConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltexFlIfConfigExtTable.setStatus("current")
_EltexFlIfConfigExtEntry_Object = MibTableRow
eltexFlIfConfigExtEntry = _EltexFlIfConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 3, 1)
)
eltexFlIfConfigExtEntry.setIndexNames(
    (0, "ELTEX-FLEX-LINKS-MIB", "eltexFlIfConfigPrimary"),
)
if mibBuilder.loadTexts:
    eltexFlIfConfigExtEntry.setStatus("current")


class _EltexFlIfConfigPreemptionMode_Type(Integer32):
    """Custom type eltexFlIfConfigPreemptionMode based on Integer32"""
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


_EltexFlIfConfigPreemptionMode_Type.__name__ = "Integer32"
_EltexFlIfConfigPreemptionMode_Object = MibTableColumn
eltexFlIfConfigPreemptionMode = _EltexFlIfConfigPreemptionMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 3, 1, 1),
    _EltexFlIfConfigPreemptionMode_Type()
)
eltexFlIfConfigPreemptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexFlIfConfigPreemptionMode.setStatus("current")
_EltexFlIfConfigPreemptionDelay_Type = Unsigned32
_EltexFlIfConfigPreemptionDelay_Object = MibTableColumn
eltexFlIfConfigPreemptionDelay = _EltexFlIfConfigPreemptionDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 1, 3, 1, 2),
    _EltexFlIfConfigPreemptionDelay_Type()
)
eltexFlIfConfigPreemptionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexFlIfConfigPreemptionDelay.setStatus("current")
if mibBuilder.loadTexts:
    eltexFlIfConfigPreemptionDelay.setUnits("seconds")
_EltexFlStatus_ObjectIdentity = ObjectIdentity
eltexFlStatus = _EltexFlStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 2)
)
_EltexFlIfStatusTable_Object = MibTable
eltexFlIfStatusTable = _EltexFlIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexFlIfStatusTable.setStatus("current")
_EltexFlIfStatusEntry_Object = MibTableRow
eltexFlIfStatusEntry = _EltexFlIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 2, 1, 1)
)
eltexFlIfStatusEntry.setIndexNames(
    (0, "ELTEX-FLEX-LINKS-MIB", "eltexFlIfIndex"),
)
if mibBuilder.loadTexts:
    eltexFlIfStatusEntry.setStatus("current")
_EltexFlIfIndex_Type = InterfaceIndex
_EltexFlIfIndex_Object = MibTableColumn
eltexFlIfIndex = _EltexFlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 2, 1, 1, 1),
    _EltexFlIfIndex_Type()
)
eltexFlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexFlIfIndex.setStatus("current")


class _EltexFlIfStatus_Type(Integer32):
    """Custom type eltexFlIfStatus based on Integer32"""
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


_EltexFlIfStatus_Type.__name__ = "Integer32"
_EltexFlIfStatus_Object = MibTableColumn
eltexFlIfStatus = _EltexFlIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 31, 1, 2, 1, 1, 2),
    _EltexFlIfStatus_Type()
)
eltexFlIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexFlIfStatus.setStatus("current")
_EltexFlexLinksMIBConformance_ObjectIdentity = ObjectIdentity
eltexFlexLinksMIBConformance = _EltexFlexLinksMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2)
)
_EltexFlexLinksMIBCompliances_ObjectIdentity = ObjectIdentity
eltexFlexLinksMIBCompliances = _EltexFlexLinksMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 1)
)
_EltexFlexLinksMIBGroups_ObjectIdentity = ObjectIdentity
eltexFlexLinksMIBGroups = _EltexFlexLinksMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 2)
)

# Managed Objects groups

eltexFlexLinksIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 2, 1)
)
eltexFlexLinksIfConfigGroup.setObjects(
    ("ELTEX-FLEX-LINKS-MIB", "eltexFlIfConfigBackUp")
)
if mibBuilder.loadTexts:
    eltexFlexLinksIfConfigGroup.setStatus("current")

eltexFlexLinksIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 2, 2)
)
eltexFlexLinksIfStatusGroup.setObjects(
    ("ELTEX-FLEX-LINKS-MIB", "eltexFlIfStatus")
)
if mibBuilder.loadTexts:
    eltexFlexLinksIfStatusGroup.setStatus("current")

eltexFlexLinksEnableNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 2, 3)
)
eltexFlexLinksEnableNotifGroup.setObjects(
    ("ELTEX-FLEX-LINKS-MIB", "eltexFlEnableStatusChangeNotif")
)
if mibBuilder.loadTexts:
    eltexFlexLinksEnableNotifGroup.setStatus("current")

eltexFlexLinksPreemptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 2, 5)
)
eltexFlexLinksPreemptionGroup.setObjects(
      *(("ELTEX-FLEX-LINKS-MIB", "eltexFlIfConfigPreemptionMode"),
        ("ELTEX-FLEX-LINKS-MIB", "eltexFlIfConfigPreemptionDelay"))
)
if mibBuilder.loadTexts:
    eltexFlexLinksPreemptionGroup.setStatus("current")


# Notification objects

eltexFlIfStatusChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 31, 0, 1)
)
eltexFlIfStatusChangeNotif.setObjects(
      *(("ELTEX-FLEX-LINKS-MIB", "eltexFlIfIndex"),
        ("ELTEX-FLEX-LINKS-MIB", "eltexFlIfStatus"))
)
if mibBuilder.loadTexts:
    eltexFlIfStatusChangeNotif.setStatus(
        "current"
    )


# Notifications groups

eltexFlexLinksNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 2, 4)
)
eltexFlexLinksNotifGroup.setObjects(
    ("ELTEX-FLEX-LINKS-MIB", "eltexFlIfStatusChangeNotif")
)
if mibBuilder.loadTexts:
    eltexFlexLinksNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

eltexFlexLinksMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35265, 31, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltexFlexLinksMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FLEX-LINKS-MIB",
    **{"eltexFlexLinksMIB": eltexFlexLinksMIB,
       "eltexFlexLinksMIBNotifs": eltexFlexLinksMIBNotifs,
       "eltexFlIfStatusChangeNotif": eltexFlIfStatusChangeNotif,
       "eltexFlexLinksMIBObjects": eltexFlexLinksMIBObjects,
       "eltexFlConfig": eltexFlConfig,
       "eltexFlIfConfigTable": eltexFlIfConfigTable,
       "eltexFlIfConfigEntry": eltexFlIfConfigEntry,
       "eltexFlIfConfigPrimary": eltexFlIfConfigPrimary,
       "eltexFlIfConfigBackUp": eltexFlIfConfigBackUp,
       "eltexFlEnableStatusChangeNotif": eltexFlEnableStatusChangeNotif,
       "eltexFlIfConfigExtTable": eltexFlIfConfigExtTable,
       "eltexFlIfConfigExtEntry": eltexFlIfConfigExtEntry,
       "eltexFlIfConfigPreemptionMode": eltexFlIfConfigPreemptionMode,
       "eltexFlIfConfigPreemptionDelay": eltexFlIfConfigPreemptionDelay,
       "eltexFlStatus": eltexFlStatus,
       "eltexFlIfStatusTable": eltexFlIfStatusTable,
       "eltexFlIfStatusEntry": eltexFlIfStatusEntry,
       "eltexFlIfIndex": eltexFlIfIndex,
       "eltexFlIfStatus": eltexFlIfStatus,
       "eltexFlexLinksMIBConformance": eltexFlexLinksMIBConformance,
       "eltexFlexLinksMIBCompliances": eltexFlexLinksMIBCompliances,
       "eltexFlexLinksMIBCompliance": eltexFlexLinksMIBCompliance,
       "eltexFlexLinksMIBGroups": eltexFlexLinksMIBGroups,
       "eltexFlexLinksIfConfigGroup": eltexFlexLinksIfConfigGroup,
       "eltexFlexLinksIfStatusGroup": eltexFlexLinksIfStatusGroup,
       "eltexFlexLinksEnableNotifGroup": eltexFlexLinksEnableNotifGroup,
       "eltexFlexLinksNotifGroup": eltexFlexLinksNotifGroup,
       "eltexFlexLinksPreemptionGroup": eltexFlexLinksPreemptionGroup}
)
