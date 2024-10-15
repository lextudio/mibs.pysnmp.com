# SNMP MIB module (PDN-STACKABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-STACKABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:10 2024
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

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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

pdnStackable = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36)
)
pdnStackable.setRevisions(
        ("2004-09-14 00:00",
         "2003-03-12 00:00",
         "2002-07-31 00:00",
         "2002-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnStackableNotifications_ObjectIdentity = ObjectIdentity
pdnStackableNotifications = _PdnStackableNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 0)
)
_PdnStackableObjects_ObjectIdentity = ObjectIdentity
pdnStackableObjects = _PdnStackableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1)
)


class _WanInterface_Type(Bits):
    """Custom type wanInterface based on Bits"""
    namedValues = NamedValues(
        *(("plugInModule", 2),
          ("stackLink1", 0),
          ("stackLink10", 10),
          ("stackLink11", 11),
          ("stackLink12", 12),
          ("stackLink13", 13),
          ("stackLink14", 14),
          ("stackLink15", 15),
          ("stackLink16", 16),
          ("stackLink17", 17),
          ("stackLink18", 18),
          ("stackLink2", 1),
          ("stackLink3", 3),
          ("stackLink4", 4),
          ("stackLink5", 5),
          ("stackLink6", 6),
          ("stackLink7", 7),
          ("stackLink8", 8),
          ("stackLink9", 9))
    )

_WanInterface_Type.__name__ = "Bits"
_WanInterface_Object = MibScalar
wanInterface = _WanInterface_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 1),
    _WanInterface_Type()
)
wanInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanInterface.setStatus("current")


class _PdnStackMethod_Type(Integer32):
    """Custom type pdnStackMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daisyChain", 1),
          ("star", 2))
    )


_PdnStackMethod_Type.__name__ = "Integer32"
_PdnStackMethod_Object = MibScalar
pdnStackMethod = _PdnStackMethod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 2),
    _PdnStackMethod_Type()
)
pdnStackMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnStackMethod.setStatus("current")
_PdnStackConfigurationTable_Object = MibTable
pdnStackConfigurationTable = _PdnStackConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    pdnStackConfigurationTable.setStatus("current")
_PdnStackConfigurationEntry_Object = MibTableRow
pdnStackConfigurationEntry = _PdnStackConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3, 1)
)
pdnStackConfigurationEntry.setIndexNames(
    (0, "PDN-STACKABLE-MIB", "pdnUnitExternalID"),
)
if mibBuilder.loadTexts:
    pdnStackConfigurationEntry.setStatus("current")
_PdnUnitExternalID_Type = Unsigned32
_PdnUnitExternalID_Object = MibTableColumn
pdnUnitExternalID = _PdnUnitExternalID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3, 1, 1),
    _PdnUnitExternalID_Type()
)
pdnUnitExternalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnUnitExternalID.setStatus("current")


class _PdnUnitEntPhysicalIndex_Type(Integer32):
    """Custom type pdnUnitEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnUnitEntPhysicalIndex_Type.__name__ = "Integer32"
_PdnUnitEntPhysicalIndex_Object = MibTableColumn
pdnUnitEntPhysicalIndex = _PdnUnitEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3, 1, 2),
    _PdnUnitEntPhysicalIndex_Type()
)
pdnUnitEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnUnitEntPhysicalIndex.setStatus("current")
_PdnUnitAssigned_Type = TruthValue
_PdnUnitAssigned_Object = MibTableColumn
pdnUnitAssigned = _PdnUnitAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3, 1, 3),
    _PdnUnitAssigned_Type()
)
pdnUnitAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnUnitAssigned.setStatus("current")
_PdnUnitGUID_Type = DisplayString
_PdnUnitGUID_Object = MibTableColumn
pdnUnitGUID = _PdnUnitGUID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3, 1, 4),
    _PdnUnitGUID_Type()
)
pdnUnitGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnUnitGUID.setStatus("current")
_PdnUnitPresent_Type = TruthValue
_PdnUnitPresent_Object = MibTableColumn
pdnUnitPresent = _PdnUnitPresent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 3, 1, 5),
    _PdnUnitPresent_Type()
)
pdnUnitPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnUnitPresent.setStatus("current")
_PdnMoveUnitCmdTable_Object = MibTable
pdnMoveUnitCmdTable = _PdnMoveUnitCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 4)
)
if mibBuilder.loadTexts:
    pdnMoveUnitCmdTable.setStatus("current")
_PdnMoveUnitCmdEntry_Object = MibTableRow
pdnMoveUnitCmdEntry = _PdnMoveUnitCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 4, 1)
)
pdnMoveUnitCmdEntry.setIndexNames(
    (0, "PDN-STACKABLE-MIB", "pdnMoveUnitSrcNumber"),
    (0, "PDN-STACKABLE-MIB", "pdnMoveUnitDestNumber"),
)
if mibBuilder.loadTexts:
    pdnMoveUnitCmdEntry.setStatus("current")
_PdnMoveUnitSrcNumber_Type = Unsigned32
_PdnMoveUnitSrcNumber_Object = MibTableColumn
pdnMoveUnitSrcNumber = _PdnMoveUnitSrcNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 4, 1, 1),
    _PdnMoveUnitSrcNumber_Type()
)
pdnMoveUnitSrcNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnMoveUnitSrcNumber.setStatus("current")
_PdnMoveUnitDestNumber_Type = Unsigned32
_PdnMoveUnitDestNumber_Object = MibTableColumn
pdnMoveUnitDestNumber = _PdnMoveUnitDestNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 4, 1, 2),
    _PdnMoveUnitDestNumber_Type()
)
pdnMoveUnitDestNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnMoveUnitDestNumber.setStatus("current")


class _PdnMoveUnitCmd_Type(Integer32):
    """Custom type pdnMoveUnitCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("move", 2),
          ("noOp", 1))
    )


_PdnMoveUnitCmd_Type.__name__ = "Integer32"
_PdnMoveUnitCmd_Object = MibTableColumn
pdnMoveUnitCmd = _PdnMoveUnitCmd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 4, 1, 3),
    _PdnMoveUnitCmd_Type()
)
pdnMoveUnitCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMoveUnitCmd.setStatus("current")
_PdnStackUnitAddedTrapEnable_Type = SwitchState
_PdnStackUnitAddedTrapEnable_Object = MibScalar
pdnStackUnitAddedTrapEnable = _PdnStackUnitAddedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 5),
    _PdnStackUnitAddedTrapEnable_Type()
)
pdnStackUnitAddedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnStackUnitAddedTrapEnable.setStatus("current")
_PdnStackUnitComFailureTrapEnable_Type = SwitchState
_PdnStackUnitComFailureTrapEnable_Object = MibScalar
pdnStackUnitComFailureTrapEnable = _PdnStackUnitComFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 6),
    _PdnStackUnitComFailureTrapEnable_Type()
)
pdnStackUnitComFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnStackUnitComFailureTrapEnable.setStatus("current")
_PdnStackUnitComRestoredTrapEnable_Type = SwitchState
_PdnStackUnitComRestoredTrapEnable_Object = MibScalar
pdnStackUnitComRestoredTrapEnable = _PdnStackUnitComRestoredTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 1, 7),
    _PdnStackUnitComRestoredTrapEnable_Type()
)
pdnStackUnitComRestoredTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnStackUnitComRestoredTrapEnable.setStatus("current")
_PdnStackableAFNs_ObjectIdentity = ObjectIdentity
pdnStackableAFNs = _PdnStackableAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 2)
)
_PdnStackableConformance_ObjectIdentity = ObjectIdentity
pdnStackableConformance = _PdnStackableConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3)
)
_PdnStackableCompliances_ObjectIdentity = ObjectIdentity
pdnStackableCompliances = _PdnStackableCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 1)
)
_PdnStackableGroups_ObjectIdentity = ObjectIdentity
pdnStackableGroups = _PdnStackableGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2)
)
_PdnStackableObjGroups_ObjectIdentity = ObjectIdentity
pdnStackableObjGroups = _PdnStackableObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2, 1)
)
_PdnStackableAfnGroups_ObjectIdentity = ObjectIdentity
pdnStackableAfnGroups = _PdnStackableAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2, 2)
)
_PdnStackableNtfyGroups_ObjectIdentity = ObjectIdentity
pdnStackableNtfyGroups = _PdnStackableNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2, 3)
)

# Managed Objects groups

wanInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2, 1, 1)
)
wanInterfaceGroup.setObjects(
    ("PDN-STACKABLE-MIB", "wanInterface")
)
if mibBuilder.loadTexts:
    wanInterfaceGroup.setStatus("current")

singleManagementEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2, 1, 2)
)
singleManagementEntityGroup.setObjects(
      *(("PDN-STACKABLE-MIB", "pdnStackMethod"),
        ("PDN-STACKABLE-MIB", "pdnUnitEntPhysicalIndex"),
        ("PDN-STACKABLE-MIB", "pdnUnitAssigned"),
        ("PDN-STACKABLE-MIB", "pdnUnitGUID"),
        ("PDN-STACKABLE-MIB", "pdnUnitPresent"),
        ("PDN-STACKABLE-MIB", "pdnMoveUnitCmd"),
        ("PDN-STACKABLE-MIB", "pdnStackUnitAddedTrapEnable"),
        ("PDN-STACKABLE-MIB", "pdnStackUnitComFailureTrapEnable"),
        ("PDN-STACKABLE-MIB", "pdnStackUnitComRestoredTrapEnable"))
)
if mibBuilder.loadTexts:
    singleManagementEntityGroup.setStatus("current")


# Notification objects

pdnStackUnitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 0, 1)
)
pdnStackUnitAdded.setObjects(
    ("PDN-STACKABLE-MIB", "pdnUnitGUID")
)
if mibBuilder.loadTexts:
    pdnStackUnitAdded.setStatus(
        "current"
    )

pdnStackUnitComFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 0, 2)
)
pdnStackUnitComFailure.setObjects(
    ("PDN-STACKABLE-MIB", "pdnUnitGUID")
)
if mibBuilder.loadTexts:
    pdnStackUnitComFailure.setStatus(
        "current"
    )

pdnStackUnitComRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 0, 3)
)
pdnStackUnitComRestored.setObjects(
    ("PDN-STACKABLE-MIB", "pdnUnitGUID")
)
if mibBuilder.loadTexts:
    pdnStackUnitComRestored.setStatus(
        "current"
    )


# Notifications groups

singleManagementEntityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 2, 3, 1)
)
singleManagementEntityNotificationGroup.setObjects(
      *(("PDN-STACKABLE-MIB", "pdnStackUnitAdded"),
        ("PDN-STACKABLE-MIB", "pdnStackUnitComFailure"),
        ("PDN-STACKABLE-MIB", "pdnStackUnitComRestored"))
)
if mibBuilder.loadTexts:
    singleManagementEntityNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdnStackableConmpliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 36, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnStackableConmpliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-STACKABLE-MIB",
    **{"pdnStackable": pdnStackable,
       "pdnStackableNotifications": pdnStackableNotifications,
       "pdnStackUnitAdded": pdnStackUnitAdded,
       "pdnStackUnitComFailure": pdnStackUnitComFailure,
       "pdnStackUnitComRestored": pdnStackUnitComRestored,
       "pdnStackableObjects": pdnStackableObjects,
       "wanInterface": wanInterface,
       "pdnStackMethod": pdnStackMethod,
       "pdnStackConfigurationTable": pdnStackConfigurationTable,
       "pdnStackConfigurationEntry": pdnStackConfigurationEntry,
       "pdnUnitExternalID": pdnUnitExternalID,
       "pdnUnitEntPhysicalIndex": pdnUnitEntPhysicalIndex,
       "pdnUnitAssigned": pdnUnitAssigned,
       "pdnUnitGUID": pdnUnitGUID,
       "pdnUnitPresent": pdnUnitPresent,
       "pdnMoveUnitCmdTable": pdnMoveUnitCmdTable,
       "pdnMoveUnitCmdEntry": pdnMoveUnitCmdEntry,
       "pdnMoveUnitSrcNumber": pdnMoveUnitSrcNumber,
       "pdnMoveUnitDestNumber": pdnMoveUnitDestNumber,
       "pdnMoveUnitCmd": pdnMoveUnitCmd,
       "pdnStackUnitAddedTrapEnable": pdnStackUnitAddedTrapEnable,
       "pdnStackUnitComFailureTrapEnable": pdnStackUnitComFailureTrapEnable,
       "pdnStackUnitComRestoredTrapEnable": pdnStackUnitComRestoredTrapEnable,
       "pdnStackableAFNs": pdnStackableAFNs,
       "pdnStackableConformance": pdnStackableConformance,
       "pdnStackableCompliances": pdnStackableCompliances,
       "pdnStackableConmpliance": pdnStackableConmpliance,
       "pdnStackableGroups": pdnStackableGroups,
       "pdnStackableObjGroups": pdnStackableObjGroups,
       "wanInterfaceGroup": wanInterfaceGroup,
       "singleManagementEntityGroup": singleManagementEntityGroup,
       "pdnStackableAfnGroups": pdnStackableAfnGroups,
       "pdnStackableNtfyGroups": pdnStackableNtfyGroups,
       "singleManagementEntityNotificationGroup": singleManagementEntityNotificationGroup}
)
