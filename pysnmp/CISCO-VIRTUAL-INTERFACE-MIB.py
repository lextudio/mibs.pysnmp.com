# SNMP MIB module (CISCO-VIRTUAL-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VIRTUAL-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:41 2024
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

(PortMemberList,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "PortMemberList")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVirtualInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648)
)
ciscoVirtualInterfaceMIB.setRevisions(
        ("2008-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVirtualInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVirtualInterfaceMIBObjects = _CiscoVirtualInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1)
)
_CvifGlobals_ObjectIdentity = ObjectIdentity
cvifGlobals = _CvifGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 1)
)
_CvifGroupsSupported_Type = TruthValue
_CvifGroupsSupported_Object = MibScalar
cvifGroupsSupported = _CvifGroupsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 1, 1),
    _CvifGroupsSupported_Type()
)
cvifGroupsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvifGroupsSupported.setStatus("current")
_CvifConfig_ObjectIdentity = ObjectIdentity
cvifConfig = _CvifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2)
)
_CvifGroupTable_Object = MibTable
cvifGroupTable = _CvifGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvifGroupTable.setStatus("current")
_CvifGroupEntry_Object = MibTableRow
cvifGroupEntry = _CvifGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1)
)
cvifGroupEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupIndex"),
)
if mibBuilder.loadTexts:
    cvifGroupEntry.setStatus("current")


class _CvifGroupIndex_Type(Unsigned32):
    """Custom type cvifGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CvifGroupIndex_Type.__name__ = "Unsigned32"
_CvifGroupIndex_Object = MibTableColumn
cvifGroupIndex = _CvifGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 1),
    _CvifGroupIndex_Type()
)
cvifGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvifGroupIndex.setStatus("current")
_CvifGroupIfIndex_Type = InterfaceIndex
_CvifGroupIfIndex_Object = MibTableColumn
cvifGroupIfIndex = _CvifGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 2),
    _CvifGroupIfIndex_Type()
)
cvifGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifGroupIfIndex.setStatus("current")
_CvifGroupBindingIfIndex_Type = InterfaceIndexOrZero
_CvifGroupBindingIfIndex_Object = MibTableColumn
cvifGroupBindingIfIndex = _CvifGroupBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 3),
    _CvifGroupBindingIfIndex_Type()
)
cvifGroupBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvifGroupBindingIfIndex.setStatus("current")


class _CvifGroupMemberList_Type(PortMemberList):
    """Custom type cvifGroupMemberList based on PortMemberList"""
    defaultHexValue = ""


_CvifGroupMemberList_Object = MibTableColumn
cvifGroupMemberList = _CvifGroupMemberList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 4),
    _CvifGroupMemberList_Type()
)
cvifGroupMemberList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifGroupMemberList.setStatus("current")
_CvifGroupCreationTime_Type = TimeStamp
_CvifGroupCreationTime_Object = MibTableColumn
cvifGroupCreationTime = _CvifGroupCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 5),
    _CvifGroupCreationTime_Type()
)
cvifGroupCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifGroupCreationTime.setStatus("current")
_CvifGroupFailureCause_Type = SnmpAdminString
_CvifGroupFailureCause_Object = MibTableColumn
cvifGroupFailureCause = _CvifGroupFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 6),
    _CvifGroupFailureCause_Type()
)
cvifGroupFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifGroupFailureCause.setStatus("current")


class _CvifGroupOperState_Type(Integer32):
    """Custom type cvifGroupOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CvifGroupOperState_Type.__name__ = "Integer32"
_CvifGroupOperState_Object = MibTableColumn
cvifGroupOperState = _CvifGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 7),
    _CvifGroupOperState_Type()
)
cvifGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifGroupOperState.setStatus("current")
_CvifGroupRowStatus_Type = RowStatus
_CvifGroupRowStatus_Object = MibTableColumn
cvifGroupRowStatus = _CvifGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 1, 1, 8),
    _CvifGroupRowStatus_Type()
)
cvifGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvifGroupRowStatus.setStatus("current")
_CvifTable_Object = MibTable
cvifTable = _CvifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvifTable.setStatus("current")
_CvifEntry_Object = MibTableRow
cvifEntry = _CvifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1)
)
cvifEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-INTERFACE-MIB", "cvifIndex"),
    (0, "CISCO-VIRTUAL-INTERFACE-MIB", "cvifType"),
)
if mibBuilder.loadTexts:
    cvifEntry.setStatus("current")


class _CvifIndex_Type(Unsigned32):
    """Custom type cvifIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CvifIndex_Type.__name__ = "Unsigned32"
_CvifIndex_Object = MibTableColumn
cvifIndex = _CvifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 1),
    _CvifIndex_Type()
)
cvifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvifIndex.setStatus("current")
_CvifType_Type = IANAifType
_CvifType_Object = MibTableColumn
cvifType = _CvifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 2),
    _CvifType_Type()
)
cvifType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvifType.setStatus("current")
_CvifIfIndex_Type = InterfaceIndex
_CvifIfIndex_Object = MibTableColumn
cvifIfIndex = _CvifIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 3),
    _CvifIfIndex_Type()
)
cvifIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifIfIndex.setStatus("current")
_CvifCreationTime_Type = TimeStamp
_CvifCreationTime_Object = MibTableColumn
cvifCreationTime = _CvifCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 4),
    _CvifCreationTime_Type()
)
cvifCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifCreationTime.setStatus("current")
_CvifBindingIfIndex_Type = InterfaceIndexOrZero
_CvifBindingIfIndex_Object = MibTableColumn
cvifBindingIfIndex = _CvifBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 5),
    _CvifBindingIfIndex_Type()
)
cvifBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvifBindingIfIndex.setStatus("current")
_CvifFailureCause_Type = SnmpAdminString
_CvifFailureCause_Object = MibTableColumn
cvifFailureCause = _CvifFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 6),
    _CvifFailureCause_Type()
)
cvifFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvifFailureCause.setStatus("current")
_CvifRowStatus_Type = RowStatus
_CvifRowStatus_Object = MibTableColumn
cvifRowStatus = _CvifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 1, 2, 2, 1, 7),
    _CvifRowStatus_Type()
)
cvifRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvifRowStatus.setStatus("current")
_CiscoVirtualInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVirtualInterfaceMIBConformance = _CiscoVirtualInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2)
)
_CvifMIBCompliances_ObjectIdentity = ObjectIdentity
cvifMIBCompliances = _CvifMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 1)
)
_CvifMIBGroups_ObjectIdentity = ObjectIdentity
cvifMIBGroups = _CvifMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 2)
)

# Managed Objects groups

cvifGroupConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 2, 1)
)
cvifGroupConformanceObjects.setObjects(
      *(("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupIfIndex"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupBindingIfIndex"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupMemberList"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupCreationTime"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupFailureCause"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupOperState"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupRowStatus"))
)
if mibBuilder.loadTexts:
    cvifGroupConformanceObjects.setStatus("current")

cvifCommonConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 2, 2)
)
cvifCommonConformanceObjects.setObjects(
      *(("CISCO-VIRTUAL-INTERFACE-MIB", "cvifGroupsSupported"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifIfIndex"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifCreationTime"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifRowStatus"))
)
if mibBuilder.loadTexts:
    cvifCommonConformanceObjects.setStatus("current")

cvifPhysicalConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 2, 3)
)
cvifPhysicalConformanceObjects.setObjects(
      *(("CISCO-VIRTUAL-INTERFACE-MIB", "cvifBindingIfIndex"),
        ("CISCO-VIRTUAL-INTERFACE-MIB", "cvifFailureCause"))
)
if mibBuilder.loadTexts:
    cvifPhysicalConformanceObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvifGroupMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvifGroupMIBCompliance.setStatus(
        "current"
    )

cvifMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 648, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cvifMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIRTUAL-INTERFACE-MIB",
    **{"ciscoVirtualInterfaceMIB": ciscoVirtualInterfaceMIB,
       "ciscoVirtualInterfaceMIBObjects": ciscoVirtualInterfaceMIBObjects,
       "cvifGlobals": cvifGlobals,
       "cvifGroupsSupported": cvifGroupsSupported,
       "cvifConfig": cvifConfig,
       "cvifGroupTable": cvifGroupTable,
       "cvifGroupEntry": cvifGroupEntry,
       "cvifGroupIndex": cvifGroupIndex,
       "cvifGroupIfIndex": cvifGroupIfIndex,
       "cvifGroupBindingIfIndex": cvifGroupBindingIfIndex,
       "cvifGroupMemberList": cvifGroupMemberList,
       "cvifGroupCreationTime": cvifGroupCreationTime,
       "cvifGroupFailureCause": cvifGroupFailureCause,
       "cvifGroupOperState": cvifGroupOperState,
       "cvifGroupRowStatus": cvifGroupRowStatus,
       "cvifTable": cvifTable,
       "cvifEntry": cvifEntry,
       "cvifIndex": cvifIndex,
       "cvifType": cvifType,
       "cvifIfIndex": cvifIfIndex,
       "cvifCreationTime": cvifCreationTime,
       "cvifBindingIfIndex": cvifBindingIfIndex,
       "cvifFailureCause": cvifFailureCause,
       "cvifRowStatus": cvifRowStatus,
       "ciscoVirtualInterfaceMIBConformance": ciscoVirtualInterfaceMIBConformance,
       "cvifMIBCompliances": cvifMIBCompliances,
       "cvifGroupMIBCompliance": cvifGroupMIBCompliance,
       "cvifMIBCompliance": cvifMIBCompliance,
       "cvifMIBGroups": cvifMIBGroups,
       "cvifGroupConformanceObjects": cvifGroupConformanceObjects,
       "cvifCommonConformanceObjects": cvifCommonConformanceObjects,
       "cvifPhysicalConformanceObjects": cvifPhysicalConformanceObjects}
)
