# SNMP MIB module (ALCATEL-IND1-PARTITIONED-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PARTITIONED-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:42 2024
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

(softentIND1Partmgr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Partmgr")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1PartitionedMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EndUserPortList(Bits, TextualConvention):
    status = "current"


class EndUserProfileArea(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PartitionedMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PartitionedMgrMIBObjects = _AlcatelIND1PartitionedMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PartitionedMgrMIBObjects.setStatus("current")
_EndUserProfileMgrMIB_ObjectIdentity = ObjectIdentity
endUserProfileMgrMIB = _EndUserProfileMgrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1)
)
_EndUserProfileTable_Object = MibTable
endUserProfileTable = _EndUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    endUserProfileTable.setStatus("current")
_EndUserProfileEntry_Object = MibTableRow
endUserProfileEntry = _EndUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1)
)
endUserProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileName"),
)
if mibBuilder.loadTexts:
    endUserProfileEntry.setStatus("current")


class _EndUserProfileName_Type(SnmpAdminString):
    """Custom type endUserProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EndUserProfileName_Type.__name__ = "SnmpAdminString"
_EndUserProfileName_Object = MibTableColumn
endUserProfileName = _EndUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 1),
    _EndUserProfileName_Type()
)
endUserProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endUserProfileName.setStatus("current")


class _EndUserProfileAreaPhysical_Type(EndUserProfileArea):
    """Custom type endUserProfileAreaPhysical based on EndUserProfileArea"""


_EndUserProfileAreaPhysical_Object = MibTableColumn
endUserProfileAreaPhysical = _EndUserProfileAreaPhysical_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 2),
    _EndUserProfileAreaPhysical_Type()
)
endUserProfileAreaPhysical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileAreaPhysical.setStatus("current")


class _EndUserProfileAreaVlanTable_Type(EndUserProfileArea):
    """Custom type endUserProfileAreaVlanTable based on EndUserProfileArea"""


_EndUserProfileAreaVlanTable_Object = MibTableColumn
endUserProfileAreaVlanTable = _EndUserProfileAreaVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 3),
    _EndUserProfileAreaVlanTable_Type()
)
endUserProfileAreaVlanTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileAreaVlanTable.setStatus("current")


class _EndUserProfileAreaBasicIpRouting_Type(EndUserProfileArea):
    """Custom type endUserProfileAreaBasicIpRouting based on EndUserProfileArea"""


_EndUserProfileAreaBasicIpRouting_Object = MibTableColumn
endUserProfileAreaBasicIpRouting = _EndUserProfileAreaBasicIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 4),
    _EndUserProfileAreaBasicIpRouting_Type()
)
endUserProfileAreaBasicIpRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileAreaBasicIpRouting.setStatus("current")


class _EndUserProfileAreaIpRoutesTable_Type(EndUserProfileArea):
    """Custom type endUserProfileAreaIpRoutesTable based on EndUserProfileArea"""


_EndUserProfileAreaIpRoutesTable_Object = MibTableColumn
endUserProfileAreaIpRoutesTable = _EndUserProfileAreaIpRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 5),
    _EndUserProfileAreaIpRoutesTable_Type()
)
endUserProfileAreaIpRoutesTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileAreaIpRoutesTable.setStatus("current")


class _EndUserProfileAreaMacFilteringTable_Type(EndUserProfileArea):
    """Custom type endUserProfileAreaMacFilteringTable based on EndUserProfileArea"""


_EndUserProfileAreaMacFilteringTable_Object = MibTableColumn
endUserProfileAreaMacFilteringTable = _EndUserProfileAreaMacFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 6),
    _EndUserProfileAreaMacFilteringTable_Type()
)
endUserProfileAreaMacFilteringTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileAreaMacFilteringTable.setStatus("current")


class _EndUserProfileAreaSpantree_Type(EndUserProfileArea):
    """Custom type endUserProfileAreaSpantree based on EndUserProfileArea"""


_EndUserProfileAreaSpantree_Object = MibTableColumn
endUserProfileAreaSpantree = _EndUserProfileAreaSpantree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 7),
    _EndUserProfileAreaSpantree_Type()
)
endUserProfileAreaSpantree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileAreaSpantree.setStatus("current")
_EndUserProfileRowStatus_Type = RowStatus
_EndUserProfileRowStatus_Object = MibTableColumn
endUserProfileRowStatus = _EndUserProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 1, 1, 8),
    _EndUserProfileRowStatus_Type()
)
endUserProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileRowStatus.setStatus("current")
_EndUserProfileSlotPortTable_Object = MibTable
endUserProfileSlotPortTable = _EndUserProfileSlotPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    endUserProfileSlotPortTable.setStatus("current")
_EndUserProfileSlotPortEntry_Object = MibTableRow
endUserProfileSlotPortEntry = _EndUserProfileSlotPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 2, 1)
)
endUserProfileSlotPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileSlotNumber"),
    (1, "ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileName"),
)
if mibBuilder.loadTexts:
    endUserProfileSlotPortEntry.setStatus("current")


class _EndUserProfileSlotNumber_Type(Integer32):
    """Custom type endUserProfileSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EndUserProfileSlotNumber_Type.__name__ = "Integer32"
_EndUserProfileSlotNumber_Object = MibTableColumn
endUserProfileSlotNumber = _EndUserProfileSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 2, 1, 1),
    _EndUserProfileSlotNumber_Type()
)
endUserProfileSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endUserProfileSlotNumber.setStatus("current")
_EndUserProfilePortList_Type = EndUserPortList
_EndUserProfilePortList_Object = MibTableColumn
endUserProfilePortList = _EndUserProfilePortList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 2, 1, 2),
    _EndUserProfilePortList_Type()
)
endUserProfilePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfilePortList.setStatus("current")
_EndUserProfileSlotPortRowStatus_Type = RowStatus
_EndUserProfileSlotPortRowStatus_Object = MibTableColumn
endUserProfileSlotPortRowStatus = _EndUserProfileSlotPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 2, 1, 3),
    _EndUserProfileSlotPortRowStatus_Type()
)
endUserProfileSlotPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileSlotPortRowStatus.setStatus("current")
_EndUserProfileVlanIdTable_Object = MibTable
endUserProfileVlanIdTable = _EndUserProfileVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    endUserProfileVlanIdTable.setStatus("current")
_EndUserProfileVlanIdEntry_Object = MibTableRow
endUserProfileVlanIdEntry = _EndUserProfileVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 3, 1)
)
endUserProfileVlanIdEntry.setIndexNames(
    (0, "ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileVlanIdStart"),
    (1, "ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileName"),
)
if mibBuilder.loadTexts:
    endUserProfileVlanIdEntry.setStatus("current")
_EndUserProfileVlanIdStart_Type = VlanId
_EndUserProfileVlanIdStart_Object = MibTableColumn
endUserProfileVlanIdStart = _EndUserProfileVlanIdStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 3, 1, 1),
    _EndUserProfileVlanIdStart_Type()
)
endUserProfileVlanIdStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endUserProfileVlanIdStart.setStatus("current")
_EndUserProfileVlanIdEnd_Type = VlanId
_EndUserProfileVlanIdEnd_Object = MibTableColumn
endUserProfileVlanIdEnd = _EndUserProfileVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 3, 1, 2),
    _EndUserProfileVlanIdEnd_Type()
)
endUserProfileVlanIdEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileVlanIdEnd.setStatus("current")
_EndUserProfileVlanIdRowStatus_Type = RowStatus
_EndUserProfileVlanIdRowStatus_Object = MibTableColumn
endUserProfileVlanIdRowStatus = _EndUserProfileVlanIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 1, 1, 3, 1, 3),
    _EndUserProfileVlanIdRowStatus_Type()
)
endUserProfileVlanIdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endUserProfileVlanIdRowStatus.setStatus("current")
_AlcatelIND1PartitionedMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PartitionedMgrMIBConformance = _AlcatelIND1PartitionedMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PartitionedMgrMIBConformance.setStatus("current")
_AlcatelIND1PartitionedMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PartitionedMgrMIBGroups = _AlcatelIND1PartitionedMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PartitionedMgrMIBGroups.setStatus("current")
_AlcatelIND1PartitionedMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PartitionedMgrMIBCompliances = _AlcatelIND1PartitionedMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PartitionedMgrMIBCompliances.setStatus("current")

# Managed Objects groups

endUserProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2, 1, 1)
)
endUserProfileGroup.setObjects(
      *(("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileName"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileAreaPhysical"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileAreaVlanTable"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileAreaBasicIpRouting"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileAreaIpRoutesTable"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileAreaMacFilteringTable"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileAreaSpantree"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileRowStatus"))
)
if mibBuilder.loadTexts:
    endUserProfileGroup.setStatus("current")

endUserProfileSlotPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2, 1, 2)
)
endUserProfileSlotPortGroup.setObjects(
      *(("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileSlotNumber"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfilePortList"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileSlotPortRowStatus"))
)
if mibBuilder.loadTexts:
    endUserProfileSlotPortGroup.setStatus("current")

endUserProfileVlanIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2, 1, 3)
)
endUserProfileVlanIdGroup.setObjects(
      *(("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileVlanIdStart"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileVlanIdEnd"),
        ("ALCATEL-IND1-PARTITIONED-MGR-MIB", "endUserProfileVlanIdRowStatus"))
)
if mibBuilder.loadTexts:
    endUserProfileVlanIdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1PartitionedMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 25, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PartitionedMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PARTITIONED-MGR-MIB",
    **{"EndUserPortList": EndUserPortList,
       "EndUserProfileArea": EndUserProfileArea,
       "alcatelIND1PartitionedMgrMIB": alcatelIND1PartitionedMgrMIB,
       "alcatelIND1PartitionedMgrMIBObjects": alcatelIND1PartitionedMgrMIBObjects,
       "endUserProfileMgrMIB": endUserProfileMgrMIB,
       "endUserProfileTable": endUserProfileTable,
       "endUserProfileEntry": endUserProfileEntry,
       "endUserProfileName": endUserProfileName,
       "endUserProfileAreaPhysical": endUserProfileAreaPhysical,
       "endUserProfileAreaVlanTable": endUserProfileAreaVlanTable,
       "endUserProfileAreaBasicIpRouting": endUserProfileAreaBasicIpRouting,
       "endUserProfileAreaIpRoutesTable": endUserProfileAreaIpRoutesTable,
       "endUserProfileAreaMacFilteringTable": endUserProfileAreaMacFilteringTable,
       "endUserProfileAreaSpantree": endUserProfileAreaSpantree,
       "endUserProfileRowStatus": endUserProfileRowStatus,
       "endUserProfileSlotPortTable": endUserProfileSlotPortTable,
       "endUserProfileSlotPortEntry": endUserProfileSlotPortEntry,
       "endUserProfileSlotNumber": endUserProfileSlotNumber,
       "endUserProfilePortList": endUserProfilePortList,
       "endUserProfileSlotPortRowStatus": endUserProfileSlotPortRowStatus,
       "endUserProfileVlanIdTable": endUserProfileVlanIdTable,
       "endUserProfileVlanIdEntry": endUserProfileVlanIdEntry,
       "endUserProfileVlanIdStart": endUserProfileVlanIdStart,
       "endUserProfileVlanIdEnd": endUserProfileVlanIdEnd,
       "endUserProfileVlanIdRowStatus": endUserProfileVlanIdRowStatus,
       "alcatelIND1PartitionedMgrMIBConformance": alcatelIND1PartitionedMgrMIBConformance,
       "alcatelIND1PartitionedMgrMIBGroups": alcatelIND1PartitionedMgrMIBGroups,
       "endUserProfileGroup": endUserProfileGroup,
       "endUserProfileSlotPortGroup": endUserProfileSlotPortGroup,
       "endUserProfileVlanIdGroup": endUserProfileVlanIdGroup,
       "alcatelIND1PartitionedMgrMIBCompliances": alcatelIND1PartitionedMgrMIBCompliances,
       "alcatelIND1PartitionedMgrMIBCompliance": alcatelIND1PartitionedMgrMIBCompliance}
)
