# SNMP MIB module (CISCO-POLICY-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-POLICY-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:01 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

ciscoPolicyGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507)
)
ciscoPolicyGroupMIB.setRevisions(
        ("2006-01-13 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpgPolicyName(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class CpgPolicyNameOrEmpty(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class CpgGroupName(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPolicyGroupMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPolicyGroupMIBNotifs = _CiscoPolicyGroupMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 0)
)
_CiscoPolicyGroupMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPolicyGroupMIBObjects = _CiscoPolicyGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1)
)
_CpgGroup_ObjectIdentity = ObjectIdentity
cpgGroup = _CpgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1)
)
_CpgGroupTable_Object = MibTable
cpgGroupTable = _CpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpgGroupTable.setStatus("current")
_CpgGroupEntry_Object = MibTableRow
cpgGroupEntry = _CpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1)
)
cpgGroupEntry.setIndexNames(
    (1, "CISCO-POLICY-GROUP-MIB", "cpgGroupName"),
)
if mibBuilder.loadTexts:
    cpgGroupEntry.setStatus("current")
_CpgGroupName_Type = CpgGroupName
_CpgGroupName_Object = MibTableColumn
cpgGroupName = _CpgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 1),
    _CpgGroupName_Type()
)
cpgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgGroupName.setStatus("current")


class _CpgGroupSourceType_Type(Integer32):
    """Custom type cpgGroupSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessList", 2),
          ("configured", 3),
          ("unknown", 1))
    )


_CpgGroupSourceType_Type.__name__ = "Integer32"
_CpgGroupSourceType_Object = MibTableColumn
cpgGroupSourceType = _CpgGroupSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 2),
    _CpgGroupSourceType_Type()
)
cpgGroupSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpgGroupSourceType.setStatus("current")
_CpgGroupIpAddrCount_Type = Unsigned32
_CpgGroupIpAddrCount_Object = MibTableColumn
cpgGroupIpAddrCount = _CpgGroupIpAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 3),
    _CpgGroupIpAddrCount_Type()
)
cpgGroupIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpgGroupIpAddrCount.setStatus("current")
_CpgGroupRowStatus_Type = RowStatus
_CpgGroupRowStatus_Object = MibTableColumn
cpgGroupRowStatus = _CpgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 4),
    _CpgGroupRowStatus_Type()
)
cpgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpgGroupRowStatus.setStatus("current")
_CpgGroupIpTable_Object = MibTable
cpgGroupIpTable = _CpgGroupIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpgGroupIpTable.setStatus("current")
_CpgGroupIpEntry_Object = MibTableRow
cpgGroupIpEntry = _CpgGroupIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1)
)
cpgGroupIpEntry.setIndexNames(
    (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpGroupName"),
    (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrType"),
    (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddress"),
)
if mibBuilder.loadTexts:
    cpgGroupIpEntry.setStatus("current")
_CpgGroupIpGroupName_Type = CpgGroupName
_CpgGroupIpGroupName_Object = MibTableColumn
cpgGroupIpGroupName = _CpgGroupIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 1),
    _CpgGroupIpGroupName_Type()
)
cpgGroupIpGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgGroupIpGroupName.setStatus("current")
_CpgGroupIpAddrType_Type = InetAddressType
_CpgGroupIpAddrType_Object = MibTableColumn
cpgGroupIpAddrType = _CpgGroupIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 2),
    _CpgGroupIpAddrType_Type()
)
cpgGroupIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgGroupIpAddrType.setStatus("current")


class _CpgGroupIpAddress_Type(InetAddress):
    """Custom type cpgGroupIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpgGroupIpAddress_Type.__name__ = "InetAddress"
_CpgGroupIpAddress_Object = MibTableColumn
cpgGroupIpAddress = _CpgGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 3),
    _CpgGroupIpAddress_Type()
)
cpgGroupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgGroupIpAddress.setStatus("current")


class _CpgGroupIpMask_Type(InetAddress):
    """Custom type cpgGroupIpMask based on InetAddress"""
    defaultHexValue = "FFFFFFFF"


_CpgGroupIpMask_Object = MibTableColumn
cpgGroupIpMask = _CpgGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 4),
    _CpgGroupIpMask_Type()
)
cpgGroupIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpgGroupIpMask.setStatus("current")


class _CpgGroupIpSourceType_Type(Integer32):
    """Custom type cpgGroupIpSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("dot1x", 3),
          ("macAuth", 6),
          ("nac", 4),
          ("other", 1),
          ("webAuth", 5))
    )


_CpgGroupIpSourceType_Type.__name__ = "Integer32"
_CpgGroupIpSourceType_Object = MibTableColumn
cpgGroupIpSourceType = _CpgGroupIpSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 5),
    _CpgGroupIpSourceType_Type()
)
cpgGroupIpSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpgGroupIpSourceType.setStatus("current")
_CpgGroupIpRowStatus_Type = RowStatus
_CpgGroupIpRowStatus_Object = MibTableColumn
cpgGroupIpRowStatus = _CpgGroupIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 6),
    _CpgGroupIpRowStatus_Type()
)
cpgGroupIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpgGroupIpRowStatus.setStatus("current")
_CpgPolicy_ObjectIdentity = ObjectIdentity
cpgPolicy = _CpgPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2)
)
_CpgPolicyTable_Object = MibTable
cpgPolicyTable = _CpgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpgPolicyTable.setStatus("current")
_CpgPolicyEntry_Object = MibTableRow
cpgPolicyEntry = _CpgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1)
)
cpgPolicyEntry.setIndexNames(
    (1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyName"),
)
if mibBuilder.loadTexts:
    cpgPolicyEntry.setStatus("current")
_CpgPolicyName_Type = CpgPolicyName
_CpgPolicyName_Object = MibTableColumn
cpgPolicyName = _CpgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 1),
    _CpgPolicyName_Type()
)
cpgPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgPolicyName.setStatus("current")
_CpgPolicyGroupCount_Type = Unsigned32
_CpgPolicyGroupCount_Object = MibTableColumn
cpgPolicyGroupCount = _CpgPolicyGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 2),
    _CpgPolicyGroupCount_Type()
)
cpgPolicyGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpgPolicyGroupCount.setStatus("current")
_CpgPolicyGroupTable_Object = MibTable
cpgPolicyGroupTable = _CpgPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpgPolicyGroupTable.setStatus("current")
_CpgPolicyGroupEntry_Object = MibTableRow
cpgPolicyGroupEntry = _CpgPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1)
)
cpgPolicyGroupEntry.setIndexNames(
    (0, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupPolicyName"),
    (1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupGroupName"),
)
if mibBuilder.loadTexts:
    cpgPolicyGroupEntry.setStatus("current")
_CpgPolicyGroupPolicyName_Type = CpgPolicyName
_CpgPolicyGroupPolicyName_Object = MibTableColumn
cpgPolicyGroupPolicyName = _CpgPolicyGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 1),
    _CpgPolicyGroupPolicyName_Type()
)
cpgPolicyGroupPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgPolicyGroupPolicyName.setStatus("current")
_CpgPolicyGroupGroupName_Type = CpgGroupName
_CpgPolicyGroupGroupName_Object = MibTableColumn
cpgPolicyGroupGroupName = _CpgPolicyGroupGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 2),
    _CpgPolicyGroupGroupName_Type()
)
cpgPolicyGroupGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpgPolicyGroupGroupName.setStatus("current")
_CpgPolicyGroupRowStatus_Type = RowStatus
_CpgPolicyGroupRowStatus_Object = MibTableColumn
cpgPolicyGroupRowStatus = _CpgPolicyGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 3),
    _CpgPolicyGroupRowStatus_Type()
)
cpgPolicyGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpgPolicyGroupRowStatus.setStatus("current")
_CiscoPolicyGroupMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPolicyGroupMIBConformance = _CiscoPolicyGroupMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2)
)
_CiscoPolicyGroupMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPolicyGroupMIBCompliances = _CiscoPolicyGroupMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1)
)
_CiscoPolicyGroupMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPolicyGroupMIBGroups = _CiscoPolicyGroupMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2)
)

# Managed Objects groups

ciscoCpgGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 1)
)
ciscoCpgGroupInfoGroup.setObjects(
      *(("CISCO-POLICY-GROUP-MIB", "cpgGroupSourceType"),
        ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrCount"),
        ("CISCO-POLICY-GROUP-MIB", "cpgGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoCpgGroupInfoGroup.setStatus("current")

ciscoCpgGroupIpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 2)
)
ciscoCpgGroupIpInfoGroup.setObjects(
      *(("CISCO-POLICY-GROUP-MIB", "cpgGroupIpMask"),
        ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpSourceType"),
        ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoCpgGroupIpInfoGroup.setStatus("current")

ciscoCpgPolicyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 3)
)
ciscoCpgPolicyInfoGroup.setObjects(
    ("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupCount")
)
if mibBuilder.loadTexts:
    ciscoCpgPolicyInfoGroup.setStatus("current")

ciscoCpgPolicyGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 4)
)
ciscoCpgPolicyGroupInfoGroup.setObjects(
    ("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupRowStatus")
)
if mibBuilder.loadTexts:
    ciscoCpgPolicyGroupInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPolicyGroupMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPolicyGroupMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-POLICY-GROUP-MIB",
    **{"CpgPolicyName": CpgPolicyName,
       "CpgPolicyNameOrEmpty": CpgPolicyNameOrEmpty,
       "CpgGroupName": CpgGroupName,
       "ciscoPolicyGroupMIB": ciscoPolicyGroupMIB,
       "ciscoPolicyGroupMIBNotifs": ciscoPolicyGroupMIBNotifs,
       "ciscoPolicyGroupMIBObjects": ciscoPolicyGroupMIBObjects,
       "cpgGroup": cpgGroup,
       "cpgGroupTable": cpgGroupTable,
       "cpgGroupEntry": cpgGroupEntry,
       "cpgGroupName": cpgGroupName,
       "cpgGroupSourceType": cpgGroupSourceType,
       "cpgGroupIpAddrCount": cpgGroupIpAddrCount,
       "cpgGroupRowStatus": cpgGroupRowStatus,
       "cpgGroupIpTable": cpgGroupIpTable,
       "cpgGroupIpEntry": cpgGroupIpEntry,
       "cpgGroupIpGroupName": cpgGroupIpGroupName,
       "cpgGroupIpAddrType": cpgGroupIpAddrType,
       "cpgGroupIpAddress": cpgGroupIpAddress,
       "cpgGroupIpMask": cpgGroupIpMask,
       "cpgGroupIpSourceType": cpgGroupIpSourceType,
       "cpgGroupIpRowStatus": cpgGroupIpRowStatus,
       "cpgPolicy": cpgPolicy,
       "cpgPolicyTable": cpgPolicyTable,
       "cpgPolicyEntry": cpgPolicyEntry,
       "cpgPolicyName": cpgPolicyName,
       "cpgPolicyGroupCount": cpgPolicyGroupCount,
       "cpgPolicyGroupTable": cpgPolicyGroupTable,
       "cpgPolicyGroupEntry": cpgPolicyGroupEntry,
       "cpgPolicyGroupPolicyName": cpgPolicyGroupPolicyName,
       "cpgPolicyGroupGroupName": cpgPolicyGroupGroupName,
       "cpgPolicyGroupRowStatus": cpgPolicyGroupRowStatus,
       "ciscoPolicyGroupMIBConformance": ciscoPolicyGroupMIBConformance,
       "ciscoPolicyGroupMIBCompliances": ciscoPolicyGroupMIBCompliances,
       "ciscoPolicyGroupMIBCompliance": ciscoPolicyGroupMIBCompliance,
       "ciscoPolicyGroupMIBGroups": ciscoPolicyGroupMIBGroups,
       "ciscoCpgGroupInfoGroup": ciscoCpgGroupInfoGroup,
       "ciscoCpgGroupIpInfoGroup": ciscoCpgGroupIpInfoGroup,
       "ciscoCpgPolicyInfoGroup": ciscoCpgPolicyInfoGroup,
       "ciscoCpgPolicyGroupInfoGroup": ciscoCpgPolicyGroupInfoGroup}
)
