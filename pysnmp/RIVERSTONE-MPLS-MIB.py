# SNMP MIB module (RIVERSTONE-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-MPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:48 2024
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

(mplsXCEntry,
 mplsXCOperStatus) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "mplsXCEntry",
    "mplsXCOperStatus")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

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
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsMPLSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsMPLSObjects_ObjectIdentity = ObjectIdentity
rsMPLSObjects = _RsMPLSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1)
)
_RsMPLSXCExtTable_Object = MibTable
rsMPLSXCExtTable = _RsMPLSXCExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1, 1)
)
if mibBuilder.loadTexts:
    rsMPLSXCExtTable.setStatus("current")
_RsMPLSXCExtEntry_Object = MibTableRow
rsMPLSXCExtEntry = _RsMPLSXCExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsMPLSXCExtEntry.setStatus("current")


class _RsMPLSXCType_Type(Integer32):
    """Custom type rsMPLSXCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("detour", 7),
          ("nonIngress", 3),
          ("other", 2),
          ("primary", 5),
          ("primaryNoSecondary", 4),
          ("secondary", 6),
          ("unknown", 1))
    )


_RsMPLSXCType_Type.__name__ = "Integer32"
_RsMPLSXCType_Object = MibTableColumn
rsMPLSXCType = _RsMPLSXCType_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1, 1, 1, 1),
    _RsMPLSXCType_Type()
)
rsMPLSXCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMPLSXCType.setStatus("current")


class _RsMPLSXCExtendedOperStatus_Type(Integer32):
    """Custom type rsMPLSXCExtendedOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("rerouted", 8),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_RsMPLSXCExtendedOperStatus_Type.__name__ = "Integer32"
_RsMPLSXCExtendedOperStatus_Object = MibTableColumn
rsMPLSXCExtendedOperStatus = _RsMPLSXCExtendedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1, 1, 1, 2),
    _RsMPLSXCExtendedOperStatus_Type()
)
rsMPLSXCExtendedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMPLSXCExtendedOperStatus.setStatus("current")
_RsMPLSXCDetourXC_Type = RowPointer
_RsMPLSXCDetourXC_Object = MibTableColumn
rsMPLSXCDetourXC = _RsMPLSXCDetourXC_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1, 1, 1, 3),
    _RsMPLSXCDetourXC_Type()
)
rsMPLSXCDetourXC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMPLSXCDetourXC.setStatus("current")
_RsMPLSXCSecondaryXC_Type = RowPointer
_RsMPLSXCSecondaryXC_Object = MibTableColumn
rsMPLSXCSecondaryXC = _RsMPLSXCSecondaryXC_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 1, 1, 1, 4),
    _RsMPLSXCSecondaryXC_Type()
)
rsMPLSXCSecondaryXC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsMPLSXCSecondaryXC.setStatus("current")
_RsMPLSNotification_ObjectIdentity = ObjectIdentity
rsMPLSNotification = _RsMPLSNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2)
)
_RsMPLSNotificationControl_ObjectIdentity = ObjectIdentity
rsMPLSNotificationControl = _RsMPLSNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 1)
)


class _RsMPLSEnableNotifications_Type(TruthValue):
    """Custom type rsMPLSEnableNotifications based on TruthValue"""


_RsMPLSEnableNotifications_Object = MibScalar
rsMPLSEnableNotifications = _RsMPLSEnableNotifications_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 1, 1),
    _RsMPLSEnableNotifications_Type()
)
rsMPLSEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsMPLSEnableNotifications.setStatus("current")
_RsMPLSNotifications_ObjectIdentity = ObjectIdentity
rsMPLSNotifications = _RsMPLSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2)
)
_RsMPLSNotifyPrefix_ObjectIdentity = ObjectIdentity
rsMPLSNotifyPrefix = _RsMPLSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2, 0)
)
_RsMPLSConformance_ObjectIdentity = ObjectIdentity
rsMPLSConformance = _RsMPLSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3)
)
_RsMPLSCompliances_ObjectIdentity = ObjectIdentity
rsMPLSCompliances = _RsMPLSCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3, 1)
)
_RsMPLSGroups_ObjectIdentity = ObjectIdentity
rsMPLSGroups = _RsMPLSGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3, 2)
)
mplsXCEntry.registerAugmentions(
    ("RIVERSTONE-MPLS-MIB",
     "rsMPLSXCExtEntry")
)
rsMPLSXCExtEntry.setIndexNames(*mplsXCEntry.getIndexNames())

# Managed Objects groups

rsMPLSLSRExtensionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3, 2, 1)
)
rsMPLSLSRExtensionGroup.setObjects(
      *(("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSXCDetourXC"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSXCSecondaryXC"))
)
if mibBuilder.loadTexts:
    rsMPLSLSRExtensionGroup.setStatus("current")

rsMPLSNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3, 2, 3)
)
rsMPLSNotificationControlGroup.setObjects(
    ("RIVERSTONE-MPLS-MIB", "rsMPLSEnableNotifications")
)
if mibBuilder.loadTexts:
    rsMPLSNotificationControlGroup.setStatus("current")


# Notification objects

rsMPLSPrimaryPathFailOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2, 0, 1)
)
rsMPLSPrimaryPathFailOver.setObjects(
      *(("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"))
)
if mibBuilder.loadTexts:
    rsMPLSPrimaryPathFailOver.setStatus(
        "current"
    )

rsMPLSPrimaryPathTakeOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2, 0, 2)
)
rsMPLSPrimaryPathTakeOver.setObjects(
    ("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus")
)
if mibBuilder.loadTexts:
    rsMPLSPrimaryPathTakeOver.setStatus(
        "current"
    )

rsMPLSStartedDetourUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2, 0, 3)
)
rsMPLSStartedDetourUse.setObjects(
      *(("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"))
)
if mibBuilder.loadTexts:
    rsMPLSStartedDetourUse.setStatus(
        "current"
    )

rsMPLSEndedDetourUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2, 0, 4)
)
rsMPLSEndedDetourUse.setObjects(
    ("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus")
)
if mibBuilder.loadTexts:
    rsMPLSEndedDetourUse.setStatus(
        "current"
    )

rsMPLSLSPPreempted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 2, 2, 0, 5)
)
rsMPLSLSPPreempted.setObjects(
      *(("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSXCExtendedOperStatus"))
)
if mibBuilder.loadTexts:
    rsMPLSLSPPreempted.setStatus(
        "current"
    )


# Notifications groups

rsMPLSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3, 2, 2)
)
rsMPLSNotificationGroup.setObjects(
      *(("RIVERSTONE-MPLS-MIB", "rsMPLSPrimaryPathFailOver"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSPrimaryPathTakeOver"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSStartedDetourUse"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSEndedDetourUse"),
        ("RIVERSTONE-MPLS-MIB", "rsMPLSLSPPreempted"))
)
if mibBuilder.loadTexts:
    rsMPLSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rsMPLSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 39, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rsMPLSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-MPLS-MIB",
    **{"rsMPLSMIB": rsMPLSMIB,
       "rsMPLSObjects": rsMPLSObjects,
       "rsMPLSXCExtTable": rsMPLSXCExtTable,
       "rsMPLSXCExtEntry": rsMPLSXCExtEntry,
       "rsMPLSXCType": rsMPLSXCType,
       "rsMPLSXCExtendedOperStatus": rsMPLSXCExtendedOperStatus,
       "rsMPLSXCDetourXC": rsMPLSXCDetourXC,
       "rsMPLSXCSecondaryXC": rsMPLSXCSecondaryXC,
       "rsMPLSNotification": rsMPLSNotification,
       "rsMPLSNotificationControl": rsMPLSNotificationControl,
       "rsMPLSEnableNotifications": rsMPLSEnableNotifications,
       "rsMPLSNotifications": rsMPLSNotifications,
       "rsMPLSNotifyPrefix": rsMPLSNotifyPrefix,
       "rsMPLSPrimaryPathFailOver": rsMPLSPrimaryPathFailOver,
       "rsMPLSPrimaryPathTakeOver": rsMPLSPrimaryPathTakeOver,
       "rsMPLSStartedDetourUse": rsMPLSStartedDetourUse,
       "rsMPLSEndedDetourUse": rsMPLSEndedDetourUse,
       "rsMPLSLSPPreempted": rsMPLSLSPPreempted,
       "rsMPLSConformance": rsMPLSConformance,
       "rsMPLSCompliances": rsMPLSCompliances,
       "rsMPLSCompliance": rsMPLSCompliance,
       "rsMPLSGroups": rsMPLSGroups,
       "rsMPLSLSRExtensionGroup": rsMPLSLSRExtensionGroup,
       "rsMPLSNotificationGroup": rsMPLSNotificationGroup,
       "rsMPLSNotificationControlGroup": rsMPLSNotificationControlGroup}
)
