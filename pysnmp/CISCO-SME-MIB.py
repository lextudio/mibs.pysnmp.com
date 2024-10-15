# SNMP MIB module (CISCO-SME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:27 2024
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

(FcNameId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId")

(InterfaceIndex,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSmeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632)
)
ciscoSmeMIB.setRevisions(
        ("2008-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoSmeInterfaceStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("initializing", 2),
          ("offline", 3),
          ("online", 4),
          ("unknown", 1))
    )



class CiscoSmeClusterStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("degraded", 3),
          ("inactive", 2),
          ("recovery", 4),
          ("unknown", 1))
    )



class CiscoSmeClusterIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSmeMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSmeMIBNotifs = _CiscoSmeMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 0)
)
_CiscoSmeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSmeMIBObjects = _CiscoSmeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1)
)
_CSmeConfig_ObjectIdentity = ObjectIdentity
cSmeConfig = _CSmeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1)
)
_CSmeClusterTable_Object = MibTable
cSmeClusterTable = _CSmeClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cSmeClusterTable.setStatus("current")
_CSmeClusterEntry_Object = MibTableRow
cSmeClusterEntry = _CSmeClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1)
)
cSmeClusterEntry.setIndexNames(
    (0, "CISCO-SME-MIB", "cSmeClusterId"),
)
if mibBuilder.loadTexts:
    cSmeClusterEntry.setStatus("current")
_CSmeClusterId_Type = CiscoSmeClusterIndex
_CSmeClusterId_Object = MibTableColumn
cSmeClusterId = _CSmeClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 1),
    _CSmeClusterId_Type()
)
cSmeClusterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSmeClusterId.setStatus("current")


class _CSmeClusterName_Type(SnmpAdminString):
    """Custom type cSmeClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSmeClusterName_Type.__name__ = "SnmpAdminString"
_CSmeClusterName_Object = MibTableColumn
cSmeClusterName = _CSmeClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 2),
    _CSmeClusterName_Type()
)
cSmeClusterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeClusterName.setStatus("current")
_CSmeClusterState_Type = CiscoSmeClusterStatus
_CSmeClusterState_Object = MibTableColumn
cSmeClusterState = _CSmeClusterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 3),
    _CSmeClusterState_Type()
)
cSmeClusterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeClusterState.setStatus("current")
_CSmeClusterMasterInetAddrType_Type = InetAddressType
_CSmeClusterMasterInetAddrType_Object = MibTableColumn
cSmeClusterMasterInetAddrType = _CSmeClusterMasterInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 4),
    _CSmeClusterMasterInetAddrType_Type()
)
cSmeClusterMasterInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeClusterMasterInetAddrType.setStatus("current")
_CSmeClusterMasterInetAddr_Type = InetAddress
_CSmeClusterMasterInetAddr_Object = MibTableColumn
cSmeClusterMasterInetAddr = _CSmeClusterMasterInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 5),
    _CSmeClusterMasterInetAddr_Type()
)
cSmeClusterMasterInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeClusterMasterInetAddr.setStatus("current")
_CSmeClusterStorageType_Type = StorageType
_CSmeClusterStorageType_Object = MibTableColumn
cSmeClusterStorageType = _CSmeClusterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 6),
    _CSmeClusterStorageType_Type()
)
cSmeClusterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeClusterStorageType.setStatus("current")
_CSmeClusterRowStatus_Type = RowStatus
_CSmeClusterRowStatus_Object = MibTableColumn
cSmeClusterRowStatus = _CSmeClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 1, 1, 7),
    _CSmeClusterRowStatus_Type()
)
cSmeClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeClusterRowStatus.setStatus("current")
_CSmeClusterMembersTable_Object = MibTable
cSmeClusterMembersTable = _CSmeClusterMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cSmeClusterMembersTable.setStatus("current")
_CSmeClusterMembersEntry_Object = MibTableRow
cSmeClusterMembersEntry = _CSmeClusterMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1)
)
cSmeClusterMembersEntry.setIndexNames(
    (0, "CISCO-SME-MIB", "cSmeClusterId"),
    (0, "CISCO-SME-MIB", "cSmeMemberInetAddrType"),
    (0, "CISCO-SME-MIB", "cSmeMemberInetAddr"),
)
if mibBuilder.loadTexts:
    cSmeClusterMembersEntry.setStatus("current")
_CSmeMemberInetAddrType_Type = InetAddressType
_CSmeMemberInetAddrType_Object = MibTableColumn
cSmeMemberInetAddrType = _CSmeMemberInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 1),
    _CSmeMemberInetAddrType_Type()
)
cSmeMemberInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSmeMemberInetAddrType.setStatus("current")


class _CSmeMemberInetAddr_Type(InetAddress):
    """Custom type cSmeMemberInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSmeMemberInetAddr_Type.__name__ = "InetAddress"
_CSmeMemberInetAddr_Object = MibTableColumn
cSmeMemberInetAddr = _CSmeMemberInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 2),
    _CSmeMemberInetAddr_Type()
)
cSmeMemberInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSmeMemberInetAddr.setStatus("current")


class _CSmeFabric_Type(SnmpAdminString):
    """Custom type cSmeFabric based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CSmeFabric_Type.__name__ = "SnmpAdminString"
_CSmeFabric_Object = MibTableColumn
cSmeFabric = _CSmeFabric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 3),
    _CSmeFabric_Type()
)
cSmeFabric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeFabric.setStatus("current")
_CSmeIsMemberLocal_Type = TruthValue
_CSmeIsMemberLocal_Object = MibTableColumn
cSmeIsMemberLocal = _CSmeIsMemberLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 4),
    _CSmeIsMemberLocal_Type()
)
cSmeIsMemberLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeIsMemberLocal.setStatus("current")
_CSmeMemberIsMaster_Type = TruthValue
_CSmeMemberIsMaster_Object = MibTableColumn
cSmeMemberIsMaster = _CSmeMemberIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 5),
    _CSmeMemberIsMaster_Type()
)
cSmeMemberIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeMemberIsMaster.setStatus("current")
_CSmeClusterMemberStorageType_Type = StorageType
_CSmeClusterMemberStorageType_Object = MibTableColumn
cSmeClusterMemberStorageType = _CSmeClusterMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 6),
    _CSmeClusterMemberStorageType_Type()
)
cSmeClusterMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeClusterMemberStorageType.setStatus("current")
_CSmeClusterMemberRowStatus_Type = RowStatus
_CSmeClusterMemberRowStatus_Object = MibTableColumn
cSmeClusterMemberRowStatus = _CSmeClusterMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 2, 1, 7),
    _CSmeClusterMemberRowStatus_Type()
)
cSmeClusterMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeClusterMemberRowStatus.setStatus("current")
_CSmeClusterMemberIfTable_Object = MibTable
cSmeClusterMemberIfTable = _CSmeClusterMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cSmeClusterMemberIfTable.setStatus("current")
_CSmeClusterMemberIfEntry_Object = MibTableRow
cSmeClusterMemberIfEntry = _CSmeClusterMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3, 1)
)
cSmeClusterMemberIfEntry.setIndexNames(
    (0, "CISCO-SME-MIB", "cSmeClusterId"),
    (0, "CISCO-SME-MIB", "cSmeMemberInetAddrType"),
    (0, "CISCO-SME-MIB", "cSmeMemberInetAddr"),
    (0, "CISCO-SME-MIB", "cSmeClusterInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cSmeClusterMemberIfEntry.setStatus("current")
_CSmeClusterInterfaceIndex_Type = InterfaceIndex
_CSmeClusterInterfaceIndex_Object = MibTableColumn
cSmeClusterInterfaceIndex = _CSmeClusterInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3, 1, 1),
    _CSmeClusterInterfaceIndex_Type()
)
cSmeClusterInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSmeClusterInterfaceIndex.setStatus("current")
_CSmeClusterInterfaceState_Type = CiscoSmeInterfaceStatus
_CSmeClusterInterfaceState_Object = MibTableColumn
cSmeClusterInterfaceState = _CSmeClusterInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 3, 1, 2),
    _CSmeClusterInterfaceState_Type()
)
cSmeClusterInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeClusterInterfaceState.setStatus("current")
_CSmeInterfaceTable_Object = MibTable
cSmeInterfaceTable = _CSmeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cSmeInterfaceTable.setStatus("current")
_CSmeInterfaceEntry_Object = MibTableRow
cSmeInterfaceEntry = _CSmeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1)
)
cSmeInterfaceEntry.setIndexNames(
    (0, "CISCO-SME-MIB", "cSmeInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cSmeInterfaceEntry.setStatus("current")
_CSmeInterfaceIndex_Type = InterfaceIndex
_CSmeInterfaceIndex_Object = MibTableColumn
cSmeInterfaceIndex = _CSmeInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 1),
    _CSmeInterfaceIndex_Type()
)
cSmeInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSmeInterfaceIndex.setStatus("current")
_CSmeInterfaceState_Type = CiscoSmeInterfaceStatus
_CSmeInterfaceState_Object = MibTableColumn
cSmeInterfaceState = _CSmeInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 2),
    _CSmeInterfaceState_Type()
)
cSmeInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeInterfaceState.setStatus("current")
_CSmeInterfaceClusterId_Type = CiscoSmeClusterIndex
_CSmeInterfaceClusterId_Object = MibTableColumn
cSmeInterfaceClusterId = _CSmeInterfaceClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 3),
    _CSmeInterfaceClusterId_Type()
)
cSmeInterfaceClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeInterfaceClusterId.setStatus("current")
_CSmeInterfaceStorageType_Type = StorageType
_CSmeInterfaceStorageType_Object = MibTableColumn
cSmeInterfaceStorageType = _CSmeInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 4),
    _CSmeInterfaceStorageType_Type()
)
cSmeInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeInterfaceStorageType.setStatus("current")
_CSmeInterfaceRowStatus_Type = RowStatus
_CSmeInterfaceRowStatus_Object = MibTableColumn
cSmeInterfaceRowStatus = _CSmeInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 4, 1, 5),
    _CSmeInterfaceRowStatus_Type()
)
cSmeInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeInterfaceRowStatus.setStatus("current")
_CSmeHostPortTable_Object = MibTable
cSmeHostPortTable = _CSmeHostPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cSmeHostPortTable.setStatus("current")
_CSmeHostPortEntry_Object = MibTableRow
cSmeHostPortEntry = _CSmeHostPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1)
)
cSmeHostPortEntry.setIndexNames(
    (0, "CISCO-SME-MIB", "cSmeHostPortName"),
)
if mibBuilder.loadTexts:
    cSmeHostPortEntry.setStatus("current")
_CSmeHostPortName_Type = FcNameId
_CSmeHostPortName_Object = MibTableColumn
cSmeHostPortName = _CSmeHostPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 1),
    _CSmeHostPortName_Type()
)
cSmeHostPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSmeHostPortName.setStatus("current")
_CSmeHostPortClusterId_Type = CiscoSmeClusterIndex
_CSmeHostPortClusterId_Object = MibTableColumn
cSmeHostPortClusterId = _CSmeHostPortClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 2),
    _CSmeHostPortClusterId_Type()
)
cSmeHostPortClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeHostPortClusterId.setStatus("current")
_CSmeHostPortStorageType_Type = StorageType
_CSmeHostPortStorageType_Object = MibTableColumn
cSmeHostPortStorageType = _CSmeHostPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 3),
    _CSmeHostPortStorageType_Type()
)
cSmeHostPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeHostPortStorageType.setStatus("current")
_CSmeHostPortRowStatus_Type = RowStatus
_CSmeHostPortRowStatus_Object = MibTableColumn
cSmeHostPortRowStatus = _CSmeHostPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 5, 1, 4),
    _CSmeHostPortRowStatus_Type()
)
cSmeHostPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSmeHostPortRowStatus.setStatus("current")
_CSmeConfigTableLastChanged_Type = TimeStamp
_CSmeConfigTableLastChanged_Object = MibScalar
cSmeConfigTableLastChanged = _CSmeConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 6),
    _CSmeConfigTableLastChanged_Type()
)
cSmeConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeConfigTableLastChanged.setStatus("current")
_CSmeHostPortTableLastChanged_Type = TimeStamp
_CSmeHostPortTableLastChanged_Object = MibScalar
cSmeHostPortTableLastChanged = _CSmeHostPortTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 7),
    _CSmeHostPortTableLastChanged_Type()
)
cSmeHostPortTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSmeHostPortTableLastChanged.setStatus("current")


class _CSmeNotifyEnable_Type(TruthValue):
    """Custom type cSmeNotifyEnable based on TruthValue"""


_CSmeNotifyEnable_Object = MibScalar
cSmeNotifyEnable = _CSmeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 1, 1, 8),
    _CSmeNotifyEnable_Type()
)
cSmeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSmeNotifyEnable.setStatus("current")
_CiscoSmeMIBConform_ObjectIdentity = ObjectIdentity
ciscoSmeMIBConform = _CiscoSmeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2)
)
_CiscoSmeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSmeMIBCompliances = _CiscoSmeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 1)
)
_CiscoSmeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSmeMIBGroups = _CiscoSmeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2)
)

# Managed Objects groups

ciscoSmeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2, 1)
)
ciscoSmeConfigGroup.setObjects(
      *(("CISCO-SME-MIB", "cSmeClusterState"),
        ("CISCO-SME-MIB", "cSmeClusterMasterInetAddrType"),
        ("CISCO-SME-MIB", "cSmeClusterMasterInetAddr"),
        ("CISCO-SME-MIB", "cSmeIsMemberLocal"),
        ("CISCO-SME-MIB", "cSmeClusterInterfaceState"),
        ("CISCO-SME-MIB", "cSmeInterfaceState"),
        ("CISCO-SME-MIB", "cSmeInterfaceClusterId"),
        ("CISCO-SME-MIB", "cSmeHostPortClusterId"),
        ("CISCO-SME-MIB", "cSmeConfigTableLastChanged"),
        ("CISCO-SME-MIB", "cSmeHostPortTableLastChanged"),
        ("CISCO-SME-MIB", "cSmeFabric"),
        ("CISCO-SME-MIB", "cSmeClusterName"),
        ("CISCO-SME-MIB", "cSmeInterfaceRowStatus"),
        ("CISCO-SME-MIB", "cSmeClusterRowStatus"),
        ("CISCO-SME-MIB", "cSmeMemberIsMaster"),
        ("CISCO-SME-MIB", "cSmeClusterMemberRowStatus"),
        ("CISCO-SME-MIB", "cSmeClusterStorageType"),
        ("CISCO-SME-MIB", "cSmeClusterMemberStorageType"),
        ("CISCO-SME-MIB", "cSmeInterfaceStorageType"),
        ("CISCO-SME-MIB", "cSmeHostPortStorageType"),
        ("CISCO-SME-MIB", "cSmeHostPortRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSmeConfigGroup.setStatus("current")

ciscoSmeNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2, 2)
)
ciscoSmeNotifControlGroup.setObjects(
    ("CISCO-SME-MIB", "cSmeNotifyEnable")
)
if mibBuilder.loadTexts:
    ciscoSmeNotifControlGroup.setStatus("current")


# Notification objects

ciscoSmeInterfaceCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 0, 1)
)
ciscoSmeInterfaceCreate.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    ciscoSmeInterfaceCreate.setStatus(
        "current"
    )

ciscoSmeInterfaceDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 0, 2)
)
ciscoSmeInterfaceDelete.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    ciscoSmeInterfaceDelete.setStatus(
        "current"
    )

ciscoSmeClusterNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 0, 3)
)
ciscoSmeClusterNewMaster.setObjects(
      *(("CISCO-SME-MIB", "cSmeClusterName"),
        ("CISCO-SME-MIB", "cSmeClusterMasterInetAddrType"),
        ("CISCO-SME-MIB", "cSmeClusterMasterInetAddr"))
)
if mibBuilder.loadTexts:
    ciscoSmeClusterNewMaster.setStatus(
        "current"
    )


# Notifications groups

ciscoSmeNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 2, 3)
)
ciscoSmeNotifsGroup.setObjects(
      *(("CISCO-SME-MIB", "ciscoSmeInterfaceCreate"),
        ("CISCO-SME-MIB", "ciscoSmeInterfaceDelete"),
        ("CISCO-SME-MIB", "ciscoSmeClusterNewMaster"))
)
if mibBuilder.loadTexts:
    ciscoSmeNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSmeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 632, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSmeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SME-MIB",
    **{"CiscoSmeInterfaceStatus": CiscoSmeInterfaceStatus,
       "CiscoSmeClusterStatus": CiscoSmeClusterStatus,
       "CiscoSmeClusterIndex": CiscoSmeClusterIndex,
       "ciscoSmeMIB": ciscoSmeMIB,
       "ciscoSmeMIBNotifs": ciscoSmeMIBNotifs,
       "ciscoSmeInterfaceCreate": ciscoSmeInterfaceCreate,
       "ciscoSmeInterfaceDelete": ciscoSmeInterfaceDelete,
       "ciscoSmeClusterNewMaster": ciscoSmeClusterNewMaster,
       "ciscoSmeMIBObjects": ciscoSmeMIBObjects,
       "cSmeConfig": cSmeConfig,
       "cSmeClusterTable": cSmeClusterTable,
       "cSmeClusterEntry": cSmeClusterEntry,
       "cSmeClusterId": cSmeClusterId,
       "cSmeClusterName": cSmeClusterName,
       "cSmeClusterState": cSmeClusterState,
       "cSmeClusterMasterInetAddrType": cSmeClusterMasterInetAddrType,
       "cSmeClusterMasterInetAddr": cSmeClusterMasterInetAddr,
       "cSmeClusterStorageType": cSmeClusterStorageType,
       "cSmeClusterRowStatus": cSmeClusterRowStatus,
       "cSmeClusterMembersTable": cSmeClusterMembersTable,
       "cSmeClusterMembersEntry": cSmeClusterMembersEntry,
       "cSmeMemberInetAddrType": cSmeMemberInetAddrType,
       "cSmeMemberInetAddr": cSmeMemberInetAddr,
       "cSmeFabric": cSmeFabric,
       "cSmeIsMemberLocal": cSmeIsMemberLocal,
       "cSmeMemberIsMaster": cSmeMemberIsMaster,
       "cSmeClusterMemberStorageType": cSmeClusterMemberStorageType,
       "cSmeClusterMemberRowStatus": cSmeClusterMemberRowStatus,
       "cSmeClusterMemberIfTable": cSmeClusterMemberIfTable,
       "cSmeClusterMemberIfEntry": cSmeClusterMemberIfEntry,
       "cSmeClusterInterfaceIndex": cSmeClusterInterfaceIndex,
       "cSmeClusterInterfaceState": cSmeClusterInterfaceState,
       "cSmeInterfaceTable": cSmeInterfaceTable,
       "cSmeInterfaceEntry": cSmeInterfaceEntry,
       "cSmeInterfaceIndex": cSmeInterfaceIndex,
       "cSmeInterfaceState": cSmeInterfaceState,
       "cSmeInterfaceClusterId": cSmeInterfaceClusterId,
       "cSmeInterfaceStorageType": cSmeInterfaceStorageType,
       "cSmeInterfaceRowStatus": cSmeInterfaceRowStatus,
       "cSmeHostPortTable": cSmeHostPortTable,
       "cSmeHostPortEntry": cSmeHostPortEntry,
       "cSmeHostPortName": cSmeHostPortName,
       "cSmeHostPortClusterId": cSmeHostPortClusterId,
       "cSmeHostPortStorageType": cSmeHostPortStorageType,
       "cSmeHostPortRowStatus": cSmeHostPortRowStatus,
       "cSmeConfigTableLastChanged": cSmeConfigTableLastChanged,
       "cSmeHostPortTableLastChanged": cSmeHostPortTableLastChanged,
       "cSmeNotifyEnable": cSmeNotifyEnable,
       "ciscoSmeMIBConform": ciscoSmeMIBConform,
       "ciscoSmeMIBCompliances": ciscoSmeMIBCompliances,
       "ciscoSmeMIBCompliance": ciscoSmeMIBCompliance,
       "ciscoSmeMIBGroups": ciscoSmeMIBGroups,
       "ciscoSmeConfigGroup": ciscoSmeConfigGroup,
       "ciscoSmeNotifControlGroup": ciscoSmeNotifControlGroup,
       "ciscoSmeNotifsGroup": ciscoSmeNotifsGroup}
)
