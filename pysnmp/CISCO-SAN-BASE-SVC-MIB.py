# SNMP MIB module (CISCO-SAN-BASE-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SAN-BASE-SVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:55 2024
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

ciscoSanBaseSvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702)
)
ciscoSanBaseSvcMIB.setRevisions(
        ("2009-06-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoSanBaseSvcInterfaceStatus(Integer32, TextualConvention):
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



class CiscoSanBaseSvcClusterStatus(Integer32, TextualConvention):
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



class CiscoSanBaseSvcClusterIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSanBaseSvcMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSanBaseSvcMIBNotifs = _CiscoSanBaseSvcMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 0)
)
_CiscoSanBaseSvcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSanBaseSvcMIBObjects = _CiscoSanBaseSvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1)
)
_CSanBaseSvcConfig_ObjectIdentity = ObjectIdentity
cSanBaseSvcConfig = _CSanBaseSvcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1)
)
_CSanBaseSvcClusterTable_Object = MibTable
cSanBaseSvcClusterTable = _CSanBaseSvcClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cSanBaseSvcClusterTable.setStatus("current")
_CSanBaseSvcClusterEntry_Object = MibTableRow
cSanBaseSvcClusterEntry = _CSanBaseSvcClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1)
)
cSanBaseSvcClusterEntry.setIndexNames(
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterId"),
)
if mibBuilder.loadTexts:
    cSanBaseSvcClusterEntry.setStatus("current")
_CSanBaseSvcClusterId_Type = CiscoSanBaseSvcClusterIndex
_CSanBaseSvcClusterId_Object = MibTableColumn
cSanBaseSvcClusterId = _CSanBaseSvcClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 1),
    _CSanBaseSvcClusterId_Type()
)
cSanBaseSvcClusterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterId.setStatus("current")


class _CSanBaseSvcClusterName_Type(SnmpAdminString):
    """Custom type cSanBaseSvcClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSanBaseSvcClusterName_Type.__name__ = "SnmpAdminString"
_CSanBaseSvcClusterName_Object = MibTableColumn
cSanBaseSvcClusterName = _CSanBaseSvcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 2),
    _CSanBaseSvcClusterName_Type()
)
cSanBaseSvcClusterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterName.setStatus("current")
_CSanBaseSvcClusterState_Type = CiscoSanBaseSvcClusterStatus
_CSanBaseSvcClusterState_Object = MibTableColumn
cSanBaseSvcClusterState = _CSanBaseSvcClusterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 3),
    _CSanBaseSvcClusterState_Type()
)
cSanBaseSvcClusterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterState.setStatus("current")
_CSanBaseSvcClusterMasterInetAddrType_Type = InetAddressType
_CSanBaseSvcClusterMasterInetAddrType_Object = MibTableColumn
cSanBaseSvcClusterMasterInetAddrType = _CSanBaseSvcClusterMasterInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 4),
    _CSanBaseSvcClusterMasterInetAddrType_Type()
)
cSanBaseSvcClusterMasterInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMasterInetAddrType.setStatus("current")
_CSanBaseSvcClusterMasterInetAddr_Type = InetAddress
_CSanBaseSvcClusterMasterInetAddr_Object = MibTableColumn
cSanBaseSvcClusterMasterInetAddr = _CSanBaseSvcClusterMasterInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 5),
    _CSanBaseSvcClusterMasterInetAddr_Type()
)
cSanBaseSvcClusterMasterInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMasterInetAddr.setStatus("current")
_CSanBaseSvcClusterStorageType_Type = StorageType
_CSanBaseSvcClusterStorageType_Object = MibTableColumn
cSanBaseSvcClusterStorageType = _CSanBaseSvcClusterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 6),
    _CSanBaseSvcClusterStorageType_Type()
)
cSanBaseSvcClusterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterStorageType.setStatus("current")
_CSanBaseSvcClusterRowStatus_Type = RowStatus
_CSanBaseSvcClusterRowStatus_Object = MibTableColumn
cSanBaseSvcClusterRowStatus = _CSanBaseSvcClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 7),
    _CSanBaseSvcClusterRowStatus_Type()
)
cSanBaseSvcClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterRowStatus.setStatus("current")
_CSanBaseSvcClusterApplication_Type = SnmpAdminString
_CSanBaseSvcClusterApplication_Object = MibTableColumn
cSanBaseSvcClusterApplication = _CSanBaseSvcClusterApplication_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 8),
    _CSanBaseSvcClusterApplication_Type()
)
cSanBaseSvcClusterApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterApplication.setStatus("current")
_CSanBaseSvcClusterMembersTable_Object = MibTable
cSanBaseSvcClusterMembersTable = _CSanBaseSvcClusterMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMembersTable.setStatus("current")
_CSanBaseSvcClusterMembersEntry_Object = MibTableRow
cSanBaseSvcClusterMembersEntry = _CSanBaseSvcClusterMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1)
)
cSanBaseSvcClusterMembersEntry.setIndexNames(
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterId"),
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddrType"),
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddr"),
)
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMembersEntry.setStatus("current")
_CSanBaseSvcClusterMemberInetAddrType_Type = InetAddressType
_CSanBaseSvcClusterMemberInetAddrType_Object = MibTableColumn
cSanBaseSvcClusterMemberInetAddrType = _CSanBaseSvcClusterMemberInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 1),
    _CSanBaseSvcClusterMemberInetAddrType_Type()
)
cSanBaseSvcClusterMemberInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberInetAddrType.setStatus("current")


class _CSanBaseSvcClusterMemberInetAddr_Type(InetAddress):
    """Custom type cSanBaseSvcClusterMemberInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CSanBaseSvcClusterMemberInetAddr_Type.__name__ = "InetAddress"
_CSanBaseSvcClusterMemberInetAddr_Object = MibTableColumn
cSanBaseSvcClusterMemberInetAddr = _CSanBaseSvcClusterMemberInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 2),
    _CSanBaseSvcClusterMemberInetAddr_Type()
)
cSanBaseSvcClusterMemberInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberInetAddr.setStatus("current")


class _CSanBaseSvcClusterMemberFabric_Type(SnmpAdminString):
    """Custom type cSanBaseSvcClusterMemberFabric based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CSanBaseSvcClusterMemberFabric_Type.__name__ = "SnmpAdminString"
_CSanBaseSvcClusterMemberFabric_Object = MibTableColumn
cSanBaseSvcClusterMemberFabric = _CSanBaseSvcClusterMemberFabric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 3),
    _CSanBaseSvcClusterMemberFabric_Type()
)
cSanBaseSvcClusterMemberFabric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberFabric.setStatus("current")
_CSanBaseSvcClusterMemberIsLocal_Type = TruthValue
_CSanBaseSvcClusterMemberIsLocal_Object = MibTableColumn
cSanBaseSvcClusterMemberIsLocal = _CSanBaseSvcClusterMemberIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 4),
    _CSanBaseSvcClusterMemberIsLocal_Type()
)
cSanBaseSvcClusterMemberIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberIsLocal.setStatus("current")
_CSanBaseSvcClusterMemberIsMaster_Type = TruthValue
_CSanBaseSvcClusterMemberIsMaster_Object = MibTableColumn
cSanBaseSvcClusterMemberIsMaster = _CSanBaseSvcClusterMemberIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 5),
    _CSanBaseSvcClusterMemberIsMaster_Type()
)
cSanBaseSvcClusterMemberIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberIsMaster.setStatus("current")
_CSanBaseSvcClusterMemberStorageType_Type = StorageType
_CSanBaseSvcClusterMemberStorageType_Object = MibTableColumn
cSanBaseSvcClusterMemberStorageType = _CSanBaseSvcClusterMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 6),
    _CSanBaseSvcClusterMemberStorageType_Type()
)
cSanBaseSvcClusterMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberStorageType.setStatus("current")
_CSanBaseSvcClusterMemberRowStatus_Type = RowStatus
_CSanBaseSvcClusterMemberRowStatus_Object = MibTableColumn
cSanBaseSvcClusterMemberRowStatus = _CSanBaseSvcClusterMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 7),
    _CSanBaseSvcClusterMemberRowStatus_Type()
)
cSanBaseSvcClusterMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberRowStatus.setStatus("current")
_CSanBaseSvcInterfaceTable_Object = MibTable
cSanBaseSvcInterfaceTable = _CSanBaseSvcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceTable.setStatus("current")
_CSanBaseSvcInterfaceEntry_Object = MibTableRow
cSanBaseSvcInterfaceEntry = _CSanBaseSvcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1)
)
cSanBaseSvcInterfaceEntry.setIndexNames(
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceEntry.setStatus("current")
_CSanBaseSvcInterfaceIndex_Type = InterfaceIndex
_CSanBaseSvcInterfaceIndex_Object = MibTableColumn
cSanBaseSvcInterfaceIndex = _CSanBaseSvcInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 1),
    _CSanBaseSvcInterfaceIndex_Type()
)
cSanBaseSvcInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceIndex.setStatus("current")
_CSanBaseSvcInterfaceState_Type = CiscoSanBaseSvcInterfaceStatus
_CSanBaseSvcInterfaceState_Object = MibTableColumn
cSanBaseSvcInterfaceState = _CSanBaseSvcInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 2),
    _CSanBaseSvcInterfaceState_Type()
)
cSanBaseSvcInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceState.setStatus("current")
_CSanBaseSvcInterfaceClusterId_Type = CiscoSanBaseSvcClusterIndex
_CSanBaseSvcInterfaceClusterId_Object = MibTableColumn
cSanBaseSvcInterfaceClusterId = _CSanBaseSvcInterfaceClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 3),
    _CSanBaseSvcInterfaceClusterId_Type()
)
cSanBaseSvcInterfaceClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceClusterId.setStatus("current")
_CSanBaseSvcInterfaceStorageType_Type = StorageType
_CSanBaseSvcInterfaceStorageType_Object = MibTableColumn
cSanBaseSvcInterfaceStorageType = _CSanBaseSvcInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 4),
    _CSanBaseSvcInterfaceStorageType_Type()
)
cSanBaseSvcInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceStorageType.setStatus("current")
_CSanBaseSvcInterfaceRowStatus_Type = RowStatus
_CSanBaseSvcInterfaceRowStatus_Object = MibTableColumn
cSanBaseSvcInterfaceRowStatus = _CSanBaseSvcInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 5),
    _CSanBaseSvcInterfaceRowStatus_Type()
)
cSanBaseSvcInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcInterfaceRowStatus.setStatus("current")
_CSanBaseSvcDevicePortTable_Object = MibTable
cSanBaseSvcDevicePortTable = _CSanBaseSvcDevicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortTable.setStatus("current")
_CSanBaseSvcDevicePortEntry_Object = MibTableRow
cSanBaseSvcDevicePortEntry = _CSanBaseSvcDevicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1)
)
cSanBaseSvcDevicePortEntry.setIndexNames(
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortName"),
)
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortEntry.setStatus("current")
_CSanBaseSvcDevicePortName_Type = FcNameId
_CSanBaseSvcDevicePortName_Object = MibTableColumn
cSanBaseSvcDevicePortName = _CSanBaseSvcDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 1),
    _CSanBaseSvcDevicePortName_Type()
)
cSanBaseSvcDevicePortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortName.setStatus("current")
_CSanBaseSvcDevicePortClusterId_Type = CiscoSanBaseSvcClusterIndex
_CSanBaseSvcDevicePortClusterId_Object = MibTableColumn
cSanBaseSvcDevicePortClusterId = _CSanBaseSvcDevicePortClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 2),
    _CSanBaseSvcDevicePortClusterId_Type()
)
cSanBaseSvcDevicePortClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortClusterId.setStatus("current")
_CSanBaseSvcDevicePortStorageType_Type = StorageType
_CSanBaseSvcDevicePortStorageType_Object = MibTableColumn
cSanBaseSvcDevicePortStorageType = _CSanBaseSvcDevicePortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 3),
    _CSanBaseSvcDevicePortStorageType_Type()
)
cSanBaseSvcDevicePortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortStorageType.setStatus("current")
_CSanBaseSvcDevicePortRowStatus_Type = RowStatus
_CSanBaseSvcDevicePortRowStatus_Object = MibTableColumn
cSanBaseSvcDevicePortRowStatus = _CSanBaseSvcDevicePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 4),
    _CSanBaseSvcDevicePortRowStatus_Type()
)
cSanBaseSvcDevicePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortRowStatus.setStatus("current")
_CSanBaseSvcConfigTableLastChanged_Type = TimeStamp
_CSanBaseSvcConfigTableLastChanged_Object = MibScalar
cSanBaseSvcConfigTableLastChanged = _CSanBaseSvcConfigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 5),
    _CSanBaseSvcConfigTableLastChanged_Type()
)
cSanBaseSvcConfigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcConfigTableLastChanged.setStatus("current")
_CSanBaseSvcDevicePortTableLastChanged_Type = TimeStamp
_CSanBaseSvcDevicePortTableLastChanged_Object = MibScalar
cSanBaseSvcDevicePortTableLastChanged = _CSanBaseSvcDevicePortTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 6),
    _CSanBaseSvcDevicePortTableLastChanged_Type()
)
cSanBaseSvcDevicePortTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcDevicePortTableLastChanged.setStatus("current")


class _CSanBaseSvcNotifyEnable_Type(TruthValue):
    """Custom type cSanBaseSvcNotifyEnable based on TruthValue"""


_CSanBaseSvcNotifyEnable_Object = MibScalar
cSanBaseSvcNotifyEnable = _CSanBaseSvcNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 7),
    _CSanBaseSvcNotifyEnable_Type()
)
cSanBaseSvcNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSanBaseSvcNotifyEnable.setStatus("current")
_CSanBaseSvcInterface_ObjectIdentity = ObjectIdentity
cSanBaseSvcInterface = _CSanBaseSvcInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2)
)
_CSanBaseSvcClusterMemberIfTable_Object = MibTable
cSanBaseSvcClusterMemberIfTable = _CSanBaseSvcClusterMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberIfTable.setStatus("current")
_CSanBaseSvcClusterMemberIfEntry_Object = MibTableRow
cSanBaseSvcClusterMemberIfEntry = _CSanBaseSvcClusterMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1, 1)
)
cSanBaseSvcClusterMemberIfEntry.setIndexNames(
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterId"),
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddrType"),
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddr"),
    (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cSanBaseSvcClusterMemberIfEntry.setStatus("current")
_CSanBaseSvcClusterInterfaceIndex_Type = InterfaceIndex
_CSanBaseSvcClusterInterfaceIndex_Object = MibTableColumn
cSanBaseSvcClusterInterfaceIndex = _CSanBaseSvcClusterInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1, 1, 1),
    _CSanBaseSvcClusterInterfaceIndex_Type()
)
cSanBaseSvcClusterInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterInterfaceIndex.setStatus("current")
_CSanBaseSvcClusterInterfaceState_Type = CiscoSanBaseSvcInterfaceStatus
_CSanBaseSvcClusterInterfaceState_Object = MibTableColumn
cSanBaseSvcClusterInterfaceState = _CSanBaseSvcClusterInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1, 1, 2),
    _CSanBaseSvcClusterInterfaceState_Type()
)
cSanBaseSvcClusterInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSanBaseSvcClusterInterfaceState.setStatus("current")
_CiscoSanBaseSvcMIBConform_ObjectIdentity = ObjectIdentity
ciscoSanBaseSvcMIBConform = _CiscoSanBaseSvcMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2)
)
_CiscoSanBaseSvcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSanBaseSvcMIBCompliances = _CiscoSanBaseSvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 1)
)
_CiscoSanBaseSvcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSanBaseSvcMIBGroups = _CiscoSanBaseSvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2)
)

# Managed Objects groups

ciscoSanBaseSvcConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 1)
)
ciscoSanBaseSvcConfigGroup.setObjects(
      *(("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterState"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddrType"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddr"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberIsLocal"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceState"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceClusterId"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortClusterId"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcConfigTableLastChanged"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberFabric"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterName"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceRowStatus"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterRowStatus"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberIsMaster"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberRowStatus"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterStorageType"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberStorageType"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceStorageType"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortStorageType"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortRowStatus"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterApplication"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortTableLastChanged"))
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcConfigGroup.setStatus("current")

ciscoSanBaseSvcNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 2)
)
ciscoSanBaseSvcNotifControlGroup.setObjects(
    ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcNotifyEnable")
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcNotifControlGroup.setStatus("current")

ciscoSanBaseSvcInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 4)
)
ciscoSanBaseSvcInterfaceGroup.setObjects(
    ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterInterfaceState")
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcInterfaceGroup.setStatus("current")


# Notification objects

ciscoSanBaseSvcInterfaceCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 0, 1)
)
ciscoSanBaseSvcInterfaceCreate.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcInterfaceCreate.setStatus(
        "current"
    )

ciscoSanBaseSvcInterfaceDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 0, 2)
)
ciscoSanBaseSvcInterfaceDelete.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcInterfaceDelete.setStatus(
        "current"
    )

ciscoSanBaseSvcClusterNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 0, 3)
)
ciscoSanBaseSvcClusterNewMaster.setObjects(
      *(("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterName"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddrType"),
        ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddr"))
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcClusterNewMaster.setStatus(
        "current"
    )


# Notifications groups

ciscoSanBaseSvcNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 3)
)
ciscoSanBaseSvcNotifsGroup.setObjects(
      *(("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcInterfaceCreate"),
        ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcInterfaceDelete"),
        ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcClusterNewMaster"))
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSanBaseSvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSanBaseSvcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SAN-BASE-SVC-MIB",
    **{"CiscoSanBaseSvcInterfaceStatus": CiscoSanBaseSvcInterfaceStatus,
       "CiscoSanBaseSvcClusterStatus": CiscoSanBaseSvcClusterStatus,
       "CiscoSanBaseSvcClusterIndex": CiscoSanBaseSvcClusterIndex,
       "ciscoSanBaseSvcMIB": ciscoSanBaseSvcMIB,
       "ciscoSanBaseSvcMIBNotifs": ciscoSanBaseSvcMIBNotifs,
       "ciscoSanBaseSvcInterfaceCreate": ciscoSanBaseSvcInterfaceCreate,
       "ciscoSanBaseSvcInterfaceDelete": ciscoSanBaseSvcInterfaceDelete,
       "ciscoSanBaseSvcClusterNewMaster": ciscoSanBaseSvcClusterNewMaster,
       "ciscoSanBaseSvcMIBObjects": ciscoSanBaseSvcMIBObjects,
       "cSanBaseSvcConfig": cSanBaseSvcConfig,
       "cSanBaseSvcClusterTable": cSanBaseSvcClusterTable,
       "cSanBaseSvcClusterEntry": cSanBaseSvcClusterEntry,
       "cSanBaseSvcClusterId": cSanBaseSvcClusterId,
       "cSanBaseSvcClusterName": cSanBaseSvcClusterName,
       "cSanBaseSvcClusterState": cSanBaseSvcClusterState,
       "cSanBaseSvcClusterMasterInetAddrType": cSanBaseSvcClusterMasterInetAddrType,
       "cSanBaseSvcClusterMasterInetAddr": cSanBaseSvcClusterMasterInetAddr,
       "cSanBaseSvcClusterStorageType": cSanBaseSvcClusterStorageType,
       "cSanBaseSvcClusterRowStatus": cSanBaseSvcClusterRowStatus,
       "cSanBaseSvcClusterApplication": cSanBaseSvcClusterApplication,
       "cSanBaseSvcClusterMembersTable": cSanBaseSvcClusterMembersTable,
       "cSanBaseSvcClusterMembersEntry": cSanBaseSvcClusterMembersEntry,
       "cSanBaseSvcClusterMemberInetAddrType": cSanBaseSvcClusterMemberInetAddrType,
       "cSanBaseSvcClusterMemberInetAddr": cSanBaseSvcClusterMemberInetAddr,
       "cSanBaseSvcClusterMemberFabric": cSanBaseSvcClusterMemberFabric,
       "cSanBaseSvcClusterMemberIsLocal": cSanBaseSvcClusterMemberIsLocal,
       "cSanBaseSvcClusterMemberIsMaster": cSanBaseSvcClusterMemberIsMaster,
       "cSanBaseSvcClusterMemberStorageType": cSanBaseSvcClusterMemberStorageType,
       "cSanBaseSvcClusterMemberRowStatus": cSanBaseSvcClusterMemberRowStatus,
       "cSanBaseSvcInterfaceTable": cSanBaseSvcInterfaceTable,
       "cSanBaseSvcInterfaceEntry": cSanBaseSvcInterfaceEntry,
       "cSanBaseSvcInterfaceIndex": cSanBaseSvcInterfaceIndex,
       "cSanBaseSvcInterfaceState": cSanBaseSvcInterfaceState,
       "cSanBaseSvcInterfaceClusterId": cSanBaseSvcInterfaceClusterId,
       "cSanBaseSvcInterfaceStorageType": cSanBaseSvcInterfaceStorageType,
       "cSanBaseSvcInterfaceRowStatus": cSanBaseSvcInterfaceRowStatus,
       "cSanBaseSvcDevicePortTable": cSanBaseSvcDevicePortTable,
       "cSanBaseSvcDevicePortEntry": cSanBaseSvcDevicePortEntry,
       "cSanBaseSvcDevicePortName": cSanBaseSvcDevicePortName,
       "cSanBaseSvcDevicePortClusterId": cSanBaseSvcDevicePortClusterId,
       "cSanBaseSvcDevicePortStorageType": cSanBaseSvcDevicePortStorageType,
       "cSanBaseSvcDevicePortRowStatus": cSanBaseSvcDevicePortRowStatus,
       "cSanBaseSvcConfigTableLastChanged": cSanBaseSvcConfigTableLastChanged,
       "cSanBaseSvcDevicePortTableLastChanged": cSanBaseSvcDevicePortTableLastChanged,
       "cSanBaseSvcNotifyEnable": cSanBaseSvcNotifyEnable,
       "cSanBaseSvcInterface": cSanBaseSvcInterface,
       "cSanBaseSvcClusterMemberIfTable": cSanBaseSvcClusterMemberIfTable,
       "cSanBaseSvcClusterMemberIfEntry": cSanBaseSvcClusterMemberIfEntry,
       "cSanBaseSvcClusterInterfaceIndex": cSanBaseSvcClusterInterfaceIndex,
       "cSanBaseSvcClusterInterfaceState": cSanBaseSvcClusterInterfaceState,
       "ciscoSanBaseSvcMIBConform": ciscoSanBaseSvcMIBConform,
       "ciscoSanBaseSvcMIBCompliances": ciscoSanBaseSvcMIBCompliances,
       "ciscoSanBaseSvcMIBCompliance": ciscoSanBaseSvcMIBCompliance,
       "ciscoSanBaseSvcMIBGroups": ciscoSanBaseSvcMIBGroups,
       "ciscoSanBaseSvcConfigGroup": ciscoSanBaseSvcConfigGroup,
       "ciscoSanBaseSvcNotifControlGroup": ciscoSanBaseSvcNotifControlGroup,
       "ciscoSanBaseSvcNotifsGroup": ciscoSanBaseSvcNotifsGroup,
       "ciscoSanBaseSvcInterfaceGroup": ciscoSanBaseSvcInterfaceGroup}
)
