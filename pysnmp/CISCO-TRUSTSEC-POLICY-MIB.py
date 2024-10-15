# SNMP MIB module (CISCO-TRUSTSEC-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TRUSTSEC-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:51 2024
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

(Cisco2KVlanList,
 CiscoVrfName) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList",
    "CiscoVrfName")

(CtsAclList,
 CtsAclListOrEmpty,
 CtsAclName,
 CtsAclNameOrEmpty,
 CtsGenerationId,
 CtsSecurityGroupTag,
 CtsSgaclMonitorMode) = mibBuilder.importSymbols(
    "CISCO-TRUSTSEC-TC-MIB",
    "CtsAclList",
    "CtsAclListOrEmpty",
    "CtsAclName",
    "CtsAclNameOrEmpty",
    "CtsGenerationId",
    "CtsSecurityGroupTag",
    "CtsSgaclMonitorMode")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTrustSecPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713)
)
ciscoTrustSecPolicyMIB.setRevisions(
        ("2012-12-19 00:00",
         "2009-11-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTrustSecPolicyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTrustSecPolicyMIBNotifs = _CiscoTrustSecPolicyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 0)
)
_CiscoTrustSecPolicyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTrustSecPolicyMIBObjects = _CiscoTrustSecPolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1)
)
_CtspSgacl_ObjectIdentity = ObjectIdentity
ctspSgacl = _CtspSgacl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1)
)
_CtspSgaclGlobals_ObjectIdentity = ObjectIdentity
ctspSgaclGlobals = _CtspSgaclGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1)
)


class _CtspSgaclEnforcementEnable_Type(Integer32):
    """Custom type ctspSgaclEnforcementEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l3Only", 2),
          ("none", 1))
    )


_CtspSgaclEnforcementEnable_Type.__name__ = "Integer32"
_CtspSgaclEnforcementEnable_Object = MibScalar
ctspSgaclEnforcementEnable = _CtspSgaclEnforcementEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 1),
    _CtspSgaclEnforcementEnable_Type()
)
ctspSgaclEnforcementEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgaclEnforcementEnable.setStatus("current")
_CtspSgaclIpv4DropNetflowMonitor_Type = SnmpAdminString
_CtspSgaclIpv4DropNetflowMonitor_Object = MibScalar
ctspSgaclIpv4DropNetflowMonitor = _CtspSgaclIpv4DropNetflowMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 2),
    _CtspSgaclIpv4DropNetflowMonitor_Type()
)
ctspSgaclIpv4DropNetflowMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgaclIpv4DropNetflowMonitor.setStatus("current")
_CtspSgaclIpv6DropNetflowMonitor_Type = SnmpAdminString
_CtspSgaclIpv6DropNetflowMonitor_Object = MibScalar
ctspSgaclIpv6DropNetflowMonitor = _CtspSgaclIpv6DropNetflowMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 3),
    _CtspSgaclIpv6DropNetflowMonitor_Type()
)
ctspSgaclIpv6DropNetflowMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgaclIpv6DropNetflowMonitor.setStatus("current")
_CtspVlanConfigTable_Object = MibTable
ctspVlanConfigTable = _CtspVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ctspVlanConfigTable.setStatus("current")
_CtspVlanConfigEntry_Object = MibTableRow
ctspVlanConfigEntry = _CtspVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1)
)
ctspVlanConfigEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanConfigIndex"),
)
if mibBuilder.loadTexts:
    ctspVlanConfigEntry.setStatus("current")
_CtspVlanConfigIndex_Type = VlanIndex
_CtspVlanConfigIndex_Object = MibTableColumn
ctspVlanConfigIndex = _CtspVlanConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1, 1),
    _CtspVlanConfigIndex_Type()
)
ctspVlanConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspVlanConfigIndex.setStatus("current")
_CtspVlanConfigSgaclEnforcement_Type = TruthValue
_CtspVlanConfigSgaclEnforcement_Object = MibTableColumn
ctspVlanConfigSgaclEnforcement = _CtspVlanConfigSgaclEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1, 2),
    _CtspVlanConfigSgaclEnforcement_Type()
)
ctspVlanConfigSgaclEnforcement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanConfigSgaclEnforcement.setStatus("current")
_CtspVlanSviActive_Type = TruthValue
_CtspVlanSviActive_Object = MibTableColumn
ctspVlanSviActive = _CtspVlanSviActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1, 3),
    _CtspVlanSviActive_Type()
)
ctspVlanSviActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspVlanSviActive.setStatus("current")
_CtspVlanConfigVrfName_Type = CiscoVrfName
_CtspVlanConfigVrfName_Object = MibTableColumn
ctspVlanConfigVrfName = _CtspVlanConfigVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1, 4),
    _CtspVlanConfigVrfName_Type()
)
ctspVlanConfigVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanConfigVrfName.setStatus("current")


class _CtspVlanConfigStorageType_Type(StorageType):
    """Custom type ctspVlanConfigStorageType based on StorageType"""


_CtspVlanConfigStorageType_Object = MibTableColumn
ctspVlanConfigStorageType = _CtspVlanConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1, 5),
    _CtspVlanConfigStorageType_Type()
)
ctspVlanConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanConfigStorageType.setStatus("current")
_CtspVlanConfigRowStatus_Type = RowStatus
_CtspVlanConfigRowStatus_Object = MibTableColumn
ctspVlanConfigRowStatus = _CtspVlanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 1, 4, 1, 6),
    _CtspVlanConfigRowStatus_Type()
)
ctspVlanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanConfigRowStatus.setStatus("current")
_CtspSgaclMappings_ObjectIdentity = ObjectIdentity
ctspSgaclMappings = _CtspSgaclMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2)
)
_CtspConfigSgaclMappingTable_Object = MibTable
ctspConfigSgaclMappingTable = _CtspConfigSgaclMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingTable.setStatus("current")
_CtspConfigSgaclMappingEntry_Object = MibTableRow
ctspConfigSgaclMappingEntry = _CtspConfigSgaclMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1)
)
ctspConfigSgaclMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMappingIpTrafficType"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMappingDestSgt"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMappingSourceSgt"),
)
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingEntry.setStatus("current")


class _CtspConfigSgaclMappingIpTrafficType_Type(Integer32):
    """Custom type ctspConfigSgaclMappingIpTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CtspConfigSgaclMappingIpTrafficType_Type.__name__ = "Integer32"
_CtspConfigSgaclMappingIpTrafficType_Object = MibTableColumn
ctspConfigSgaclMappingIpTrafficType = _CtspConfigSgaclMappingIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 1),
    _CtspConfigSgaclMappingIpTrafficType_Type()
)
ctspConfigSgaclMappingIpTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingIpTrafficType.setStatus("current")
_CtspConfigSgaclMappingDestSgt_Type = CtsSecurityGroupTag
_CtspConfigSgaclMappingDestSgt_Object = MibTableColumn
ctspConfigSgaclMappingDestSgt = _CtspConfigSgaclMappingDestSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 2),
    _CtspConfigSgaclMappingDestSgt_Type()
)
ctspConfigSgaclMappingDestSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingDestSgt.setStatus("current")
_CtspConfigSgaclMappingSourceSgt_Type = CtsSecurityGroupTag
_CtspConfigSgaclMappingSourceSgt_Object = MibTableColumn
ctspConfigSgaclMappingSourceSgt = _CtspConfigSgaclMappingSourceSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 3),
    _CtspConfigSgaclMappingSourceSgt_Type()
)
ctspConfigSgaclMappingSourceSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingSourceSgt.setStatus("current")
_CtspConfigSgaclMappingSgaclName_Type = CtsAclList
_CtspConfigSgaclMappingSgaclName_Object = MibTableColumn
ctspConfigSgaclMappingSgaclName = _CtspConfigSgaclMappingSgaclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 4),
    _CtspConfigSgaclMappingSgaclName_Type()
)
ctspConfigSgaclMappingSgaclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingSgaclName.setStatus("current")


class _CtspConfigSgaclMappingStorageType_Type(StorageType):
    """Custom type ctspConfigSgaclMappingStorageType based on StorageType"""


_CtspConfigSgaclMappingStorageType_Object = MibTableColumn
ctspConfigSgaclMappingStorageType = _CtspConfigSgaclMappingStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 5),
    _CtspConfigSgaclMappingStorageType_Type()
)
ctspConfigSgaclMappingStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingStorageType.setStatus("current")
_CtspConfigSgaclMappingRowStatus_Type = RowStatus
_CtspConfigSgaclMappingRowStatus_Object = MibTableColumn
ctspConfigSgaclMappingRowStatus = _CtspConfigSgaclMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 6),
    _CtspConfigSgaclMappingRowStatus_Type()
)
ctspConfigSgaclMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingRowStatus.setStatus("current")


class _CtspConfigSgaclMonitor_Type(CtsSgaclMonitorMode):
    """Custom type ctspConfigSgaclMonitor based on CtsSgaclMonitorMode"""


_CtspConfigSgaclMonitor_Object = MibTableColumn
ctspConfigSgaclMonitor = _CtspConfigSgaclMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 1, 1, 7),
    _CtspConfigSgaclMonitor_Type()
)
ctspConfigSgaclMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspConfigSgaclMonitor.setStatus("current")
_CtspDefConfigIpv4Sgacls_Type = CtsAclListOrEmpty
_CtspDefConfigIpv4Sgacls_Object = MibScalar
ctspDefConfigIpv4Sgacls = _CtspDefConfigIpv4Sgacls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 2),
    _CtspDefConfigIpv4Sgacls_Type()
)
ctspDefConfigIpv4Sgacls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspDefConfigIpv4Sgacls.setStatus("current")
_CtspDefConfigIpv6Sgacls_Type = CtsAclListOrEmpty
_CtspDefConfigIpv6Sgacls_Object = MibScalar
ctspDefConfigIpv6Sgacls = _CtspDefConfigIpv6Sgacls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 3),
    _CtspDefConfigIpv6Sgacls_Type()
)
ctspDefConfigIpv6Sgacls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspDefConfigIpv6Sgacls.setStatus("current")
_CtspDownloadedSgaclMappingTable_Object = MibTable
ctspDownloadedSgaclMappingTable = _CtspDownloadedSgaclMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ctspDownloadedSgaclMappingTable.setStatus("current")
_CtspDownloadedSgaclMappingEntry_Object = MibTableRow
ctspDownloadedSgaclMappingEntry = _CtspDownloadedSgaclMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1)
)
ctspDownloadedSgaclMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgaclDestSgt"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgaclSourceSgt"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgaclIndex"),
)
if mibBuilder.loadTexts:
    ctspDownloadedSgaclMappingEntry.setStatus("current")
_CtspDownloadedSgaclDestSgt_Type = CtsSecurityGroupTag
_CtspDownloadedSgaclDestSgt_Object = MibTableColumn
ctspDownloadedSgaclDestSgt = _CtspDownloadedSgaclDestSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 1),
    _CtspDownloadedSgaclDestSgt_Type()
)
ctspDownloadedSgaclDestSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDownloadedSgaclDestSgt.setStatus("current")
_CtspDownloadedSgaclSourceSgt_Type = CtsSecurityGroupTag
_CtspDownloadedSgaclSourceSgt_Object = MibTableColumn
ctspDownloadedSgaclSourceSgt = _CtspDownloadedSgaclSourceSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 2),
    _CtspDownloadedSgaclSourceSgt_Type()
)
ctspDownloadedSgaclSourceSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDownloadedSgaclSourceSgt.setStatus("current")


class _CtspDownloadedSgaclIndex_Type(Unsigned32):
    """Custom type ctspDownloadedSgaclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtspDownloadedSgaclIndex_Type.__name__ = "Unsigned32"
_CtspDownloadedSgaclIndex_Object = MibTableColumn
ctspDownloadedSgaclIndex = _CtspDownloadedSgaclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 3),
    _CtspDownloadedSgaclIndex_Type()
)
ctspDownloadedSgaclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDownloadedSgaclIndex.setStatus("current")
_CtspDownloadedSgaclName_Type = CtsAclName
_CtspDownloadedSgaclName_Object = MibTableColumn
ctspDownloadedSgaclName = _CtspDownloadedSgaclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 4),
    _CtspDownloadedSgaclName_Type()
)
ctspDownloadedSgaclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedSgaclName.setStatus("current")
_CtspDownloadedSgaclGenId_Type = CtsGenerationId
_CtspDownloadedSgaclGenId_Object = MibTableColumn
ctspDownloadedSgaclGenId = _CtspDownloadedSgaclGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 5),
    _CtspDownloadedSgaclGenId_Type()
)
ctspDownloadedSgaclGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedSgaclGenId.setStatus("current")


class _CtspDownloadedIpTrafficType_Type(Bits):
    """Custom type ctspDownloadedIpTrafficType based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_CtspDownloadedIpTrafficType_Type.__name__ = "Bits"
_CtspDownloadedIpTrafficType_Object = MibTableColumn
ctspDownloadedIpTrafficType = _CtspDownloadedIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 6),
    _CtspDownloadedIpTrafficType_Type()
)
ctspDownloadedIpTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedIpTrafficType.setStatus("current")
_CtspDownloadedSgaclMonitor_Type = CtsSgaclMonitorMode
_CtspDownloadedSgaclMonitor_Object = MibTableColumn
ctspDownloadedSgaclMonitor = _CtspDownloadedSgaclMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 4, 1, 7),
    _CtspDownloadedSgaclMonitor_Type()
)
ctspDownloadedSgaclMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedSgaclMonitor.setStatus("current")
_CtspDefDownloadedSgaclMappingTable_Object = MibTable
ctspDefDownloadedSgaclMappingTable = _CtspDefDownloadedSgaclMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ctspDefDownloadedSgaclMappingTable.setStatus("current")
_CtspDefDownloadedSgaclMappingEntry_Object = MibTableRow
ctspDefDownloadedSgaclMappingEntry = _CtspDefDownloadedSgaclMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5, 1)
)
ctspDefDownloadedSgaclMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDefDownloadedSgaclIndex"),
)
if mibBuilder.loadTexts:
    ctspDefDownloadedSgaclMappingEntry.setStatus("current")


class _CtspDefDownloadedSgaclIndex_Type(Unsigned32):
    """Custom type ctspDefDownloadedSgaclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtspDefDownloadedSgaclIndex_Type.__name__ = "Unsigned32"
_CtspDefDownloadedSgaclIndex_Object = MibTableColumn
ctspDefDownloadedSgaclIndex = _CtspDefDownloadedSgaclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5, 1, 1),
    _CtspDefDownloadedSgaclIndex_Type()
)
ctspDefDownloadedSgaclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDefDownloadedSgaclIndex.setStatus("current")
_CtspDefDownloadedSgaclName_Type = CtsAclName
_CtspDefDownloadedSgaclName_Object = MibTableColumn
ctspDefDownloadedSgaclName = _CtspDefDownloadedSgaclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5, 1, 2),
    _CtspDefDownloadedSgaclName_Type()
)
ctspDefDownloadedSgaclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefDownloadedSgaclName.setStatus("current")
_CtspDefDownloadedSgaclGenId_Type = CtsGenerationId
_CtspDefDownloadedSgaclGenId_Object = MibTableColumn
ctspDefDownloadedSgaclGenId = _CtspDefDownloadedSgaclGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5, 1, 3),
    _CtspDefDownloadedSgaclGenId_Type()
)
ctspDefDownloadedSgaclGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefDownloadedSgaclGenId.setStatus("current")


class _CtspDefDownloadedIpTrafficType_Type(Bits):
    """Custom type ctspDefDownloadedIpTrafficType based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_CtspDefDownloadedIpTrafficType_Type.__name__ = "Bits"
_CtspDefDownloadedIpTrafficType_Object = MibTableColumn
ctspDefDownloadedIpTrafficType = _CtspDefDownloadedIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5, 1, 4),
    _CtspDefDownloadedIpTrafficType_Type()
)
ctspDefDownloadedIpTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefDownloadedIpTrafficType.setStatus("current")
_CtspDefDownloadedSgaclMonitor_Type = CtsSgaclMonitorMode
_CtspDefDownloadedSgaclMonitor_Object = MibTableColumn
ctspDefDownloadedSgaclMonitor = _CtspDefDownloadedSgaclMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 5, 1, 5),
    _CtspDefDownloadedSgaclMonitor_Type()
)
ctspDefDownloadedSgaclMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefDownloadedSgaclMonitor.setStatus("current")
_CtspOperSgaclMappingTable_Object = MibTable
ctspOperSgaclMappingTable = _CtspOperSgaclMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ctspOperSgaclMappingTable.setStatus("current")
_CtspOperSgaclMappingEntry_Object = MibTableRow
ctspOperSgaclMappingEntry = _CtspOperSgaclMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1)
)
ctspOperSgaclMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspOperIpTrafficType"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspOperSgaclDestSgt"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspOperSgaclSourceSgt"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspOperSgaclIndex"),
)
if mibBuilder.loadTexts:
    ctspOperSgaclMappingEntry.setStatus("current")


class _CtspOperIpTrafficType_Type(Integer32):
    """Custom type ctspOperIpTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CtspOperIpTrafficType_Type.__name__ = "Integer32"
_CtspOperIpTrafficType_Object = MibTableColumn
ctspOperIpTrafficType = _CtspOperIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 1),
    _CtspOperIpTrafficType_Type()
)
ctspOperIpTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspOperIpTrafficType.setStatus("current")
_CtspOperSgaclDestSgt_Type = CtsSecurityGroupTag
_CtspOperSgaclDestSgt_Object = MibTableColumn
ctspOperSgaclDestSgt = _CtspOperSgaclDestSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 2),
    _CtspOperSgaclDestSgt_Type()
)
ctspOperSgaclDestSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspOperSgaclDestSgt.setStatus("current")
_CtspOperSgaclSourceSgt_Type = CtsSecurityGroupTag
_CtspOperSgaclSourceSgt_Object = MibTableColumn
ctspOperSgaclSourceSgt = _CtspOperSgaclSourceSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 3),
    _CtspOperSgaclSourceSgt_Type()
)
ctspOperSgaclSourceSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspOperSgaclSourceSgt.setStatus("current")


class _CtspOperSgaclIndex_Type(Unsigned32):
    """Custom type ctspOperSgaclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtspOperSgaclIndex_Type.__name__ = "Unsigned32"
_CtspOperSgaclIndex_Object = MibTableColumn
ctspOperSgaclIndex = _CtspOperSgaclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 4),
    _CtspOperSgaclIndex_Type()
)
ctspOperSgaclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspOperSgaclIndex.setStatus("current")
_CtspOperationalSgaclName_Type = CtsAclName
_CtspOperationalSgaclName_Object = MibTableColumn
ctspOperationalSgaclName = _CtspOperationalSgaclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 5),
    _CtspOperationalSgaclName_Type()
)
ctspOperationalSgaclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspOperationalSgaclName.setStatus("current")
_CtspOperationalSgaclGenId_Type = CtsGenerationId
_CtspOperationalSgaclGenId_Object = MibTableColumn
ctspOperationalSgaclGenId = _CtspOperationalSgaclGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 6),
    _CtspOperationalSgaclGenId_Type()
)
ctspOperationalSgaclGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspOperationalSgaclGenId.setStatus("current")


class _CtspOperSgaclMappingSource_Type(Integer32):
    """Custom type ctspOperSgaclMappingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("downloaded", 2))
    )


_CtspOperSgaclMappingSource_Type.__name__ = "Integer32"
_CtspOperSgaclMappingSource_Object = MibTableColumn
ctspOperSgaclMappingSource = _CtspOperSgaclMappingSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 7),
    _CtspOperSgaclMappingSource_Type()
)
ctspOperSgaclMappingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspOperSgaclMappingSource.setStatus("current")


class _CtspOperSgaclConfigSource_Type(Integer32):
    """Custom type ctspOperSgaclConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("downloaded", 2))
    )


_CtspOperSgaclConfigSource_Type.__name__ = "Integer32"
_CtspOperSgaclConfigSource_Object = MibTableColumn
ctspOperSgaclConfigSource = _CtspOperSgaclConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 8),
    _CtspOperSgaclConfigSource_Type()
)
ctspOperSgaclConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspOperSgaclConfigSource.setStatus("current")
_CtspOperSgaclMonitor_Type = CtsSgaclMonitorMode
_CtspOperSgaclMonitor_Object = MibTableColumn
ctspOperSgaclMonitor = _CtspOperSgaclMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 6, 1, 9),
    _CtspOperSgaclMonitor_Type()
)
ctspOperSgaclMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspOperSgaclMonitor.setStatus("current")
_CtspDefOperSgaclMappingTable_Object = MibTable
ctspDefOperSgaclMappingTable = _CtspDefOperSgaclMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ctspDefOperSgaclMappingTable.setStatus("current")
_CtspDefOperSgaclMappingEntry_Object = MibTableRow
ctspDefOperSgaclMappingEntry = _CtspDefOperSgaclMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1)
)
ctspDefOperSgaclMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperIpTrafficType"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperSgaclIndex"),
)
if mibBuilder.loadTexts:
    ctspDefOperSgaclMappingEntry.setStatus("current")


class _CtspDefOperIpTrafficType_Type(Integer32):
    """Custom type ctspDefOperIpTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CtspDefOperIpTrafficType_Type.__name__ = "Integer32"
_CtspDefOperIpTrafficType_Object = MibTableColumn
ctspDefOperIpTrafficType = _CtspDefOperIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 1),
    _CtspDefOperIpTrafficType_Type()
)
ctspDefOperIpTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDefOperIpTrafficType.setStatus("current")


class _CtspDefOperSgaclIndex_Type(Unsigned32):
    """Custom type ctspDefOperSgaclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtspDefOperSgaclIndex_Type.__name__ = "Unsigned32"
_CtspDefOperSgaclIndex_Object = MibTableColumn
ctspDefOperSgaclIndex = _CtspDefOperSgaclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 2),
    _CtspDefOperSgaclIndex_Type()
)
ctspDefOperSgaclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDefOperSgaclIndex.setStatus("current")
_CtspDefOperationalSgaclName_Type = CtsAclName
_CtspDefOperationalSgaclName_Object = MibTableColumn
ctspDefOperationalSgaclName = _CtspDefOperationalSgaclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 3),
    _CtspDefOperationalSgaclName_Type()
)
ctspDefOperationalSgaclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefOperationalSgaclName.setStatus("current")
_CtspDefOperationalSgaclGenId_Type = CtsGenerationId
_CtspDefOperationalSgaclGenId_Object = MibTableColumn
ctspDefOperationalSgaclGenId = _CtspDefOperationalSgaclGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 4),
    _CtspDefOperationalSgaclGenId_Type()
)
ctspDefOperationalSgaclGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefOperationalSgaclGenId.setStatus("current")


class _CtspDefOperSgaclMappingSource_Type(Integer32):
    """Custom type ctspDefOperSgaclMappingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("downloaded", 2))
    )


_CtspDefOperSgaclMappingSource_Type.__name__ = "Integer32"
_CtspDefOperSgaclMappingSource_Object = MibTableColumn
ctspDefOperSgaclMappingSource = _CtspDefOperSgaclMappingSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 5),
    _CtspDefOperSgaclMappingSource_Type()
)
ctspDefOperSgaclMappingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefOperSgaclMappingSource.setStatus("current")


class _CtspDefOperSgaclConfigSource_Type(Integer32):
    """Custom type ctspDefOperSgaclConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("downloaded", 2))
    )


_CtspDefOperSgaclConfigSource_Type.__name__ = "Integer32"
_CtspDefOperSgaclConfigSource_Object = MibTableColumn
ctspDefOperSgaclConfigSource = _CtspDefOperSgaclConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 6),
    _CtspDefOperSgaclConfigSource_Type()
)
ctspDefOperSgaclConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefOperSgaclConfigSource.setStatus("current")
_CtspDefOperSgaclMonitor_Type = CtsSgaclMonitorMode
_CtspDefOperSgaclMonitor_Object = MibTableColumn
ctspDefOperSgaclMonitor = _CtspDefOperSgaclMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 7, 1, 7),
    _CtspDefOperSgaclMonitor_Type()
)
ctspDefOperSgaclMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefOperSgaclMonitor.setStatus("current")
_CtspDefConfigIpv4SgaclsMonitor_Type = CtsSgaclMonitorMode
_CtspDefConfigIpv4SgaclsMonitor_Object = MibScalar
ctspDefConfigIpv4SgaclsMonitor = _CtspDefConfigIpv4SgaclsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 8),
    _CtspDefConfigIpv4SgaclsMonitor_Type()
)
ctspDefConfigIpv4SgaclsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspDefConfigIpv4SgaclsMonitor.setStatus("current")
_CtspDefConfigIpv6SgaclsMonitor_Type = CtsSgaclMonitorMode
_CtspDefConfigIpv6SgaclsMonitor_Object = MibScalar
ctspDefConfigIpv6SgaclsMonitor = _CtspDefConfigIpv6SgaclsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 9),
    _CtspDefConfigIpv6SgaclsMonitor_Type()
)
ctspDefConfigIpv6SgaclsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspDefConfigIpv6SgaclsMonitor.setStatus("current")
_CtspSgaclMonitorEnable_Type = CtsSgaclMonitorMode
_CtspSgaclMonitorEnable_Object = MibScalar
ctspSgaclMonitorEnable = _CtspSgaclMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 2, 10),
    _CtspSgaclMonitorEnable_Type()
)
ctspSgaclMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgaclMonitorEnable.setStatus("current")
_CtspSgaclStatistics_ObjectIdentity = ObjectIdentity
ctspSgaclStatistics = _CtspSgaclStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3)
)
_CtspSgtStatsTable_Object = MibTable
ctspSgtStatsTable = _CtspSgtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctspSgtStatsTable.setStatus("current")
_CtspSgtStatsEntry_Object = MibTableRow
ctspSgtStatsEntry = _CtspSgtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1)
)
ctspSgtStatsEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpTrafficType"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsDestSgt"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsSourceSgt"),
)
if mibBuilder.loadTexts:
    ctspSgtStatsEntry.setStatus("current")


class _CtspStatsIpTrafficType_Type(Integer32):
    """Custom type ctspStatsIpTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CtspStatsIpTrafficType_Type.__name__ = "Integer32"
_CtspStatsIpTrafficType_Object = MibTableColumn
ctspStatsIpTrafficType = _CtspStatsIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 1),
    _CtspStatsIpTrafficType_Type()
)
ctspStatsIpTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspStatsIpTrafficType.setStatus("current")
_CtspStatsDestSgt_Type = CtsSecurityGroupTag
_CtspStatsDestSgt_Object = MibTableColumn
ctspStatsDestSgt = _CtspStatsDestSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 2),
    _CtspStatsDestSgt_Type()
)
ctspStatsDestSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspStatsDestSgt.setStatus("current")
_CtspStatsSourceSgt_Type = CtsSecurityGroupTag
_CtspStatsSourceSgt_Object = MibTableColumn
ctspStatsSourceSgt = _CtspStatsSourceSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 3),
    _CtspStatsSourceSgt_Type()
)
ctspStatsSourceSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspStatsSourceSgt.setStatus("current")
_CtspStatsIpSwDropPkts_Type = Counter64
_CtspStatsIpSwDropPkts_Object = MibTableColumn
ctspStatsIpSwDropPkts = _CtspStatsIpSwDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 4),
    _CtspStatsIpSwDropPkts_Type()
)
ctspStatsIpSwDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspStatsIpSwDropPkts.setStatus("current")
_CtspStatsIpHwDropPkts_Type = Counter64
_CtspStatsIpHwDropPkts_Object = MibTableColumn
ctspStatsIpHwDropPkts = _CtspStatsIpHwDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 5),
    _CtspStatsIpHwDropPkts_Type()
)
ctspStatsIpHwDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspStatsIpHwDropPkts.setStatus("current")
_CtspStatsIpSwPermitPkts_Type = Counter64
_CtspStatsIpSwPermitPkts_Object = MibTableColumn
ctspStatsIpSwPermitPkts = _CtspStatsIpSwPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 6),
    _CtspStatsIpSwPermitPkts_Type()
)
ctspStatsIpSwPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspStatsIpSwPermitPkts.setStatus("current")
_CtspStatsIpHwPermitPkts_Type = Counter64
_CtspStatsIpHwPermitPkts_Object = MibTableColumn
ctspStatsIpHwPermitPkts = _CtspStatsIpHwPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 7),
    _CtspStatsIpHwPermitPkts_Type()
)
ctspStatsIpHwPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspStatsIpHwPermitPkts.setStatus("current")
_CtspStatsIpSwMonitorPkts_Type = Counter64
_CtspStatsIpSwMonitorPkts_Object = MibTableColumn
ctspStatsIpSwMonitorPkts = _CtspStatsIpSwMonitorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 8),
    _CtspStatsIpSwMonitorPkts_Type()
)
ctspStatsIpSwMonitorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspStatsIpSwMonitorPkts.setStatus("current")
_CtspStatsIpHwMonitorPkts_Type = Counter64
_CtspStatsIpHwMonitorPkts_Object = MibTableColumn
ctspStatsIpHwMonitorPkts = _CtspStatsIpHwMonitorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 1, 1, 9),
    _CtspStatsIpHwMonitorPkts_Type()
)
ctspStatsIpHwMonitorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspStatsIpHwMonitorPkts.setStatus("current")
_CtspDefStatsTable_Object = MibTable
ctspDefStatsTable = _CtspDefStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctspDefStatsTable.setStatus("current")
_CtspDefStatsEntry_Object = MibTableRow
ctspDefStatsEntry = _CtspDefStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1)
)
ctspDefStatsEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpTrafficType"),
)
if mibBuilder.loadTexts:
    ctspDefStatsEntry.setStatus("current")


class _CtspDefIpTrafficType_Type(Integer32):
    """Custom type ctspDefIpTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CtspDefIpTrafficType_Type.__name__ = "Integer32"
_CtspDefIpTrafficType_Object = MibTableColumn
ctspDefIpTrafficType = _CtspDefIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 1),
    _CtspDefIpTrafficType_Type()
)
ctspDefIpTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDefIpTrafficType.setStatus("current")
_CtspDefIpSwDropPkts_Type = Counter64
_CtspDefIpSwDropPkts_Object = MibTableColumn
ctspDefIpSwDropPkts = _CtspDefIpSwDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 2),
    _CtspDefIpSwDropPkts_Type()
)
ctspDefIpSwDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefIpSwDropPkts.setStatus("current")
_CtspDefIpHwDropPkts_Type = Counter64
_CtspDefIpHwDropPkts_Object = MibTableColumn
ctspDefIpHwDropPkts = _CtspDefIpHwDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 3),
    _CtspDefIpHwDropPkts_Type()
)
ctspDefIpHwDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefIpHwDropPkts.setStatus("current")
_CtspDefIpSwPermitPkts_Type = Counter64
_CtspDefIpSwPermitPkts_Object = MibTableColumn
ctspDefIpSwPermitPkts = _CtspDefIpSwPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 4),
    _CtspDefIpSwPermitPkts_Type()
)
ctspDefIpSwPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefIpSwPermitPkts.setStatus("current")
_CtspDefIpHwPermitPkts_Type = Counter64
_CtspDefIpHwPermitPkts_Object = MibTableColumn
ctspDefIpHwPermitPkts = _CtspDefIpHwPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 5),
    _CtspDefIpHwPermitPkts_Type()
)
ctspDefIpHwPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefIpHwPermitPkts.setStatus("current")
_CtspDefIpSwMonitorPkts_Type = Counter64
_CtspDefIpSwMonitorPkts_Object = MibTableColumn
ctspDefIpSwMonitorPkts = _CtspDefIpSwMonitorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 6),
    _CtspDefIpSwMonitorPkts_Type()
)
ctspDefIpSwMonitorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefIpSwMonitorPkts.setStatus("current")
_CtspDefIpHwMonitorPkts_Type = Counter64
_CtspDefIpHwMonitorPkts_Object = MibTableColumn
ctspDefIpHwMonitorPkts = _CtspDefIpHwMonitorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 1, 3, 2, 1, 7),
    _CtspDefIpHwMonitorPkts_Type()
)
ctspDefIpHwMonitorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDefIpHwMonitorPkts.setStatus("current")
_CtspPeerPolicy_ObjectIdentity = ObjectIdentity
ctspPeerPolicy = _CtspPeerPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2)
)


class _CtspAllPeerPolicyAction_Type(Integer32):
    """Custom type ctspAllPeerPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_CtspAllPeerPolicyAction_Type.__name__ = "Integer32"
_CtspAllPeerPolicyAction_Object = MibScalar
ctspAllPeerPolicyAction = _CtspAllPeerPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 1),
    _CtspAllPeerPolicyAction_Type()
)
ctspAllPeerPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspAllPeerPolicyAction.setStatus("current")
_CtspPeerPolicyTable_Object = MibTable
ctspPeerPolicyTable = _CtspPeerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ctspPeerPolicyTable.setStatus("current")
_CtspPeerPolicyEntry_Object = MibTableRow
ctspPeerPolicyEntry = _CtspPeerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1)
)
ctspPeerPolicyEntry.setIndexNames(
    (1, "CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerName"),
)
if mibBuilder.loadTexts:
    ctspPeerPolicyEntry.setStatus("current")


class _CtspPeerName_Type(SnmpAdminString):
    """Custom type ctspPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CtspPeerName_Type.__name__ = "SnmpAdminString"
_CtspPeerName_Object = MibTableColumn
ctspPeerName = _CtspPeerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 1),
    _CtspPeerName_Type()
)
ctspPeerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspPeerName.setStatus("current")
_CtspPeerSgt_Type = CtsSecurityGroupTag
_CtspPeerSgt_Object = MibTableColumn
ctspPeerSgt = _CtspPeerSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 2),
    _CtspPeerSgt_Type()
)
ctspPeerSgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspPeerSgt.setStatus("current")
_CtspPeerSgtGenId_Type = CtsGenerationId
_CtspPeerSgtGenId_Object = MibTableColumn
ctspPeerSgtGenId = _CtspPeerSgtGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 3),
    _CtspPeerSgtGenId_Type()
)
ctspPeerSgtGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspPeerSgtGenId.setStatus("current")


class _CtspPeerTrustState_Type(Integer32):
    """Custom type ctspPeerTrustState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTrust", 2),
          ("trusted", 1))
    )


_CtspPeerTrustState_Type.__name__ = "Integer32"
_CtspPeerTrustState_Object = MibTableColumn
ctspPeerTrustState = _CtspPeerTrustState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 4),
    _CtspPeerTrustState_Type()
)
ctspPeerTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspPeerTrustState.setStatus("current")
_CtspPeerPolicyLifeTime_Type = Unsigned32
_CtspPeerPolicyLifeTime_Object = MibTableColumn
ctspPeerPolicyLifeTime = _CtspPeerPolicyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 5),
    _CtspPeerPolicyLifeTime_Type()
)
ctspPeerPolicyLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspPeerPolicyLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    ctspPeerPolicyLifeTime.setUnits("seconds")
_CtspPeerPolicyLastUpdate_Type = DateAndTime
_CtspPeerPolicyLastUpdate_Object = MibTableColumn
ctspPeerPolicyLastUpdate = _CtspPeerPolicyLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 6),
    _CtspPeerPolicyLastUpdate_Type()
)
ctspPeerPolicyLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspPeerPolicyLastUpdate.setStatus("current")


class _CtspPeerPolicyAction_Type(Integer32):
    """Custom type ctspPeerPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_CtspPeerPolicyAction_Type.__name__ = "Integer32"
_CtspPeerPolicyAction_Object = MibTableColumn
ctspPeerPolicyAction = _CtspPeerPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 2, 2, 1, 7),
    _CtspPeerPolicyAction_Type()
)
ctspPeerPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspPeerPolicyAction.setStatus("current")
_CtspLayer3Transport_ObjectIdentity = ObjectIdentity
ctspLayer3Transport = _CtspLayer3Transport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3)
)
_CtspLayer3PolicyTable_Object = MibTable
ctspLayer3PolicyTable = _CtspLayer3PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctspLayer3PolicyTable.setStatus("current")
_CtspLayer3PolicyEntry_Object = MibTableRow
ctspLayer3PolicyEntry = _CtspLayer3PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1, 1)
)
ctspLayer3PolicyEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspLayer3PolicyIpTrafficType"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspLayer3PolicyType"),
)
if mibBuilder.loadTexts:
    ctspLayer3PolicyEntry.setStatus("current")


class _CtspLayer3PolicyIpTrafficType_Type(Integer32):
    """Custom type ctspLayer3PolicyIpTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CtspLayer3PolicyIpTrafficType_Type.__name__ = "Integer32"
_CtspLayer3PolicyIpTrafficType_Object = MibTableColumn
ctspLayer3PolicyIpTrafficType = _CtspLayer3PolicyIpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1, 1, 1),
    _CtspLayer3PolicyIpTrafficType_Type()
)
ctspLayer3PolicyIpTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspLayer3PolicyIpTrafficType.setStatus("current")


class _CtspLayer3PolicyType_Type(Integer32):
    """Custom type ctspLayer3PolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exception", 2),
          ("permit", 1))
    )


_CtspLayer3PolicyType_Type.__name__ = "Integer32"
_CtspLayer3PolicyType_Object = MibTableColumn
ctspLayer3PolicyType = _CtspLayer3PolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1, 1, 2),
    _CtspLayer3PolicyType_Type()
)
ctspLayer3PolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspLayer3PolicyType.setStatus("current")
_CtspLayer3PolicyLocalConfig_Type = CtsAclNameOrEmpty
_CtspLayer3PolicyLocalConfig_Object = MibTableColumn
ctspLayer3PolicyLocalConfig = _CtspLayer3PolicyLocalConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1, 1, 3),
    _CtspLayer3PolicyLocalConfig_Type()
)
ctspLayer3PolicyLocalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspLayer3PolicyLocalConfig.setStatus("current")
_CtspLayer3PolicyDownloaded_Type = CtsAclNameOrEmpty
_CtspLayer3PolicyDownloaded_Object = MibTableColumn
ctspLayer3PolicyDownloaded = _CtspLayer3PolicyDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1, 1, 4),
    _CtspLayer3PolicyDownloaded_Type()
)
ctspLayer3PolicyDownloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspLayer3PolicyDownloaded.setStatus("current")
_CtspLayer3PolicyOperational_Type = CtsAclNameOrEmpty
_CtspLayer3PolicyOperational_Object = MibTableColumn
ctspLayer3PolicyOperational = _CtspLayer3PolicyOperational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 1, 1, 5),
    _CtspLayer3PolicyOperational_Type()
)
ctspLayer3PolicyOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspLayer3PolicyOperational.setStatus("current")
_CtspIfL3PolicyConfigTable_Object = MibTable
ctspIfL3PolicyConfigTable = _CtspIfL3PolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ctspIfL3PolicyConfigTable.setStatus("current")
_CtspIfL3PolicyConfigEntry_Object = MibTableRow
ctspIfL3PolicyConfigEntry = _CtspIfL3PolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 2, 1)
)
ctspIfL3PolicyConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctspIfL3PolicyConfigEntry.setStatus("current")
_CtspIfL3Ipv4PolicyEnabled_Type = TruthValue
_CtspIfL3Ipv4PolicyEnabled_Object = MibTableColumn
ctspIfL3Ipv4PolicyEnabled = _CtspIfL3Ipv4PolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 2, 1, 1),
    _CtspIfL3Ipv4PolicyEnabled_Type()
)
ctspIfL3Ipv4PolicyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspIfL3Ipv4PolicyEnabled.setStatus("current")
_CtspIfL3Ipv6PolicyEnabled_Type = TruthValue
_CtspIfL3Ipv6PolicyEnabled_Object = MibTableColumn
ctspIfL3Ipv6PolicyEnabled = _CtspIfL3Ipv6PolicyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 3, 2, 1, 2),
    _CtspIfL3Ipv6PolicyEnabled_Type()
)
ctspIfL3Ipv6PolicyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspIfL3Ipv6PolicyEnabled.setStatus("current")
_CtspIpSgtMappings_ObjectIdentity = ObjectIdentity
ctspIpSgtMappings = _CtspIpSgtMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4)
)
_CtspIpSgtMappingTable_Object = MibTable
ctspIpSgtMappingTable = _CtspIpSgtMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ctspIpSgtMappingTable.setStatus("current")
_CtspIpSgtMappingEntry_Object = MibTableRow
ctspIpSgtMappingEntry = _CtspIpSgtMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1)
)
ctspIpSgtMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtVrfName"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtAddressType"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtIpAddress"),
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtAddressLength"),
)
if mibBuilder.loadTexts:
    ctspIpSgtMappingEntry.setStatus("current")
_CtspIpSgtVrfName_Type = CiscoVrfName
_CtspIpSgtVrfName_Object = MibTableColumn
ctspIpSgtVrfName = _CtspIpSgtVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 1),
    _CtspIpSgtVrfName_Type()
)
ctspIpSgtVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspIpSgtVrfName.setStatus("current")
_CtspIpSgtAddressType_Type = InetAddressType
_CtspIpSgtAddressType_Object = MibTableColumn
ctspIpSgtAddressType = _CtspIpSgtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 2),
    _CtspIpSgtAddressType_Type()
)
ctspIpSgtAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspIpSgtAddressType.setStatus("current")
_CtspIpSgtIpAddress_Type = InetAddress
_CtspIpSgtIpAddress_Object = MibTableColumn
ctspIpSgtIpAddress = _CtspIpSgtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 3),
    _CtspIpSgtIpAddress_Type()
)
ctspIpSgtIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspIpSgtIpAddress.setStatus("current")
_CtspIpSgtAddressLength_Type = InetAddressPrefixLength
_CtspIpSgtAddressLength_Object = MibTableColumn
ctspIpSgtAddressLength = _CtspIpSgtAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 4),
    _CtspIpSgtAddressLength_Type()
)
ctspIpSgtAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspIpSgtAddressLength.setStatus("current")
_CtspIpSgtValue_Type = CtsSecurityGroupTag
_CtspIpSgtValue_Object = MibTableColumn
ctspIpSgtValue = _CtspIpSgtValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 5),
    _CtspIpSgtValue_Type()
)
ctspIpSgtValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIpSgtValue.setStatus("current")


class _CtspIpSgtSource_Type(Integer32):
    """Custom type ctspIpSgtSource based on Integer32"""
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
        *(("arp", 2),
          ("caching", 8),
          ("configured", 1),
          ("internal", 5),
          ("l3if", 6),
          ("localAuthenticated", 3),
          ("sxp", 4),
          ("vlan", 7))
    )


_CtspIpSgtSource_Type.__name__ = "Integer32"
_CtspIpSgtSource_Object = MibTableColumn
ctspIpSgtSource = _CtspIpSgtSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 6),
    _CtspIpSgtSource_Type()
)
ctspIpSgtSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIpSgtSource.setStatus("current")


class _CtspIpSgtStorageType_Type(StorageType):
    """Custom type ctspIpSgtStorageType based on StorageType"""


_CtspIpSgtStorageType_Object = MibTableColumn
ctspIpSgtStorageType = _CtspIpSgtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 7),
    _CtspIpSgtStorageType_Type()
)
ctspIpSgtStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIpSgtStorageType.setStatus("current")
_CtspIpSgtRowStatus_Type = RowStatus
_CtspIpSgtRowStatus_Object = MibTableColumn
ctspIpSgtRowStatus = _CtspIpSgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 4, 1, 1, 8),
    _CtspIpSgtRowStatus_Type()
)
ctspIpSgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIpSgtRowStatus.setStatus("current")
_CtspSgtPolicy_ObjectIdentity = ObjectIdentity
ctspSgtPolicy = _CtspSgtPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5)
)


class _CtspAllSgtPolicyAction_Type(Integer32):
    """Custom type ctspAllSgtPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_CtspAllSgtPolicyAction_Type.__name__ = "Integer32"
_CtspAllSgtPolicyAction_Object = MibScalar
ctspAllSgtPolicyAction = _CtspAllSgtPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 1),
    _CtspAllSgtPolicyAction_Type()
)
ctspAllSgtPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspAllSgtPolicyAction.setStatus("current")
_CtspDownloadedSgtPolicyTable_Object = MibTable
ctspDownloadedSgtPolicyTable = _CtspDownloadedSgtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicyTable.setStatus("current")
_CtspDownloadedSgtPolicyEntry_Object = MibTableRow
ctspDownloadedSgtPolicyEntry = _CtspDownloadedSgtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2, 1)
)
ctspDownloadedSgtPolicyEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgtPolicySgt"),
)
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicyEntry.setStatus("current")
_CtspDownloadedSgtPolicySgt_Type = CtsSecurityGroupTag
_CtspDownloadedSgtPolicySgt_Object = MibTableColumn
ctspDownloadedSgtPolicySgt = _CtspDownloadedSgtPolicySgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2, 1, 1),
    _CtspDownloadedSgtPolicySgt_Type()
)
ctspDownloadedSgtPolicySgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicySgt.setStatus("current")
_CtspDownloadedSgtPolicySgtGenId_Type = CtsGenerationId
_CtspDownloadedSgtPolicySgtGenId_Object = MibTableColumn
ctspDownloadedSgtPolicySgtGenId = _CtspDownloadedSgtPolicySgtGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2, 1, 2),
    _CtspDownloadedSgtPolicySgtGenId_Type()
)
ctspDownloadedSgtPolicySgtGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicySgtGenId.setStatus("current")
_CtspDownloadedSgtPolicyLifeTime_Type = Unsigned32
_CtspDownloadedSgtPolicyLifeTime_Object = MibTableColumn
ctspDownloadedSgtPolicyLifeTime = _CtspDownloadedSgtPolicyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2, 1, 3),
    _CtspDownloadedSgtPolicyLifeTime_Type()
)
ctspDownloadedSgtPolicyLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicyLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicyLifeTime.setUnits("seconds")
_CtspDownloadedSgtPolicyLastUpdate_Type = DateAndTime
_CtspDownloadedSgtPolicyLastUpdate_Object = MibTableColumn
ctspDownloadedSgtPolicyLastUpdate = _CtspDownloadedSgtPolicyLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2, 1, 4),
    _CtspDownloadedSgtPolicyLastUpdate_Type()
)
ctspDownloadedSgtPolicyLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicyLastUpdate.setStatus("current")


class _CtspDownloadedSgtPolicyAction_Type(Integer32):
    """Custom type ctspDownloadedSgtPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_CtspDownloadedSgtPolicyAction_Type.__name__ = "Integer32"
_CtspDownloadedSgtPolicyAction_Object = MibTableColumn
ctspDownloadedSgtPolicyAction = _CtspDownloadedSgtPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 2, 1, 5),
    _CtspDownloadedSgtPolicyAction_Type()
)
ctspDownloadedSgtPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspDownloadedSgtPolicyAction.setStatus("current")
_CtspDownloadedDefSgtPolicyTable_Object = MibTable
ctspDownloadedDefSgtPolicyTable = _CtspDownloadedDefSgtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyTable.setStatus("current")
_CtspDownloadedDefSgtPolicyEntry_Object = MibTableRow
ctspDownloadedDefSgtPolicyEntry = _CtspDownloadedDefSgtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3, 1)
)
ctspDownloadedDefSgtPolicyEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedDefSgtPolicyType"),
)
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyEntry.setStatus("current")


class _CtspDownloadedDefSgtPolicyType_Type(Integer32):
    """Custom type ctspDownloadedDefSgtPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicastDefault", 1)
    )


_CtspDownloadedDefSgtPolicyType_Type.__name__ = "Integer32"
_CtspDownloadedDefSgtPolicyType_Object = MibTableColumn
ctspDownloadedDefSgtPolicyType = _CtspDownloadedDefSgtPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3, 1, 1),
    _CtspDownloadedDefSgtPolicyType_Type()
)
ctspDownloadedDefSgtPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyType.setStatus("current")
_CtspDownloadedDefSgtPolicySgtGenId_Type = CtsGenerationId
_CtspDownloadedDefSgtPolicySgtGenId_Object = MibTableColumn
ctspDownloadedDefSgtPolicySgtGenId = _CtspDownloadedDefSgtPolicySgtGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3, 1, 2),
    _CtspDownloadedDefSgtPolicySgtGenId_Type()
)
ctspDownloadedDefSgtPolicySgtGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicySgtGenId.setStatus("current")
_CtspDownloadedDefSgtPolicyLifeTime_Type = Unsigned32
_CtspDownloadedDefSgtPolicyLifeTime_Object = MibTableColumn
ctspDownloadedDefSgtPolicyLifeTime = _CtspDownloadedDefSgtPolicyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3, 1, 3),
    _CtspDownloadedDefSgtPolicyLifeTime_Type()
)
ctspDownloadedDefSgtPolicyLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyLifeTime.setUnits("seconds")
_CtspDownloadedDefSgtPolicyLastUpdate_Type = DateAndTime
_CtspDownloadedDefSgtPolicyLastUpdate_Object = MibTableColumn
ctspDownloadedDefSgtPolicyLastUpdate = _CtspDownloadedDefSgtPolicyLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3, 1, 4),
    _CtspDownloadedDefSgtPolicyLastUpdate_Type()
)
ctspDownloadedDefSgtPolicyLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyLastUpdate.setStatus("current")


class _CtspDownloadedDefSgtPolicyAction_Type(Integer32):
    """Custom type ctspDownloadedDefSgtPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_CtspDownloadedDefSgtPolicyAction_Type.__name__ = "Integer32"
_CtspDownloadedDefSgtPolicyAction_Object = MibTableColumn
ctspDownloadedDefSgtPolicyAction = _CtspDownloadedDefSgtPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 5, 3, 1, 5),
    _CtspDownloadedDefSgtPolicyAction_Type()
)
ctspDownloadedDefSgtPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspDownloadedDefSgtPolicyAction.setStatus("current")
_CtspIfSgtMappings_ObjectIdentity = ObjectIdentity
ctspIfSgtMappings = _CtspIfSgtMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6)
)
_CtspIfSgtMappingTable_Object = MibTable
ctspIfSgtMappingTable = _CtspIfSgtMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ctspIfSgtMappingTable.setStatus("current")
_CtspIfSgtMappingEntry_Object = MibTableRow
ctspIfSgtMappingEntry = _CtspIfSgtMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 1, 1)
)
ctspIfSgtMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctspIfSgtMappingEntry.setStatus("current")
_CtspIfSgtValue_Type = CtsSecurityGroupTag
_CtspIfSgtValue_Object = MibTableColumn
ctspIfSgtValue = _CtspIfSgtValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 1, 1, 1),
    _CtspIfSgtValue_Type()
)
ctspIfSgtValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIfSgtValue.setStatus("current")
_CtspIfSgName_Type = SnmpAdminString
_CtspIfSgName_Object = MibTableColumn
ctspIfSgName = _CtspIfSgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 1, 1, 2),
    _CtspIfSgName_Type()
)
ctspIfSgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIfSgName.setStatus("current")


class _CtspIfSgtStorageType_Type(StorageType):
    """Custom type ctspIfSgtStorageType based on StorageType"""


_CtspIfSgtStorageType_Object = MibTableColumn
ctspIfSgtStorageType = _CtspIfSgtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 1, 1, 3),
    _CtspIfSgtStorageType_Type()
)
ctspIfSgtStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIfSgtStorageType.setStatus("current")
_CtspIfSgtRowStatus_Type = RowStatus
_CtspIfSgtRowStatus_Object = MibTableColumn
ctspIfSgtRowStatus = _CtspIfSgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 1, 1, 4),
    _CtspIfSgtRowStatus_Type()
)
ctspIfSgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspIfSgtRowStatus.setStatus("current")
_CtspIfSgtMappingInfoTable_Object = MibTable
ctspIfSgtMappingInfoTable = _CtspIfSgtMappingInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ctspIfSgtMappingInfoTable.setStatus("current")
_CtspIfSgtMappingInfoEntry_Object = MibTableRow
ctspIfSgtMappingInfoEntry = _CtspIfSgtMappingInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 2, 1)
)
ctspIfSgtMappingInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctspIfSgtMappingInfoEntry.setStatus("current")


class _CtspL3IPMStatus_Type(Integer32):
    """Custom type ctspL3IPMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 1),
          ("inactive", 3))
    )


_CtspL3IPMStatus_Type.__name__ = "Integer32"
_CtspL3IPMStatus_Object = MibTableColumn
ctspL3IPMStatus = _CtspL3IPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 6, 2, 1, 1),
    _CtspL3IPMStatus_Type()
)
ctspL3IPMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctspL3IPMStatus.setStatus("current")
_CtspVlanSgtMappings_ObjectIdentity = ObjectIdentity
ctspVlanSgtMappings = _CtspVlanSgtMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7)
)
_CtspVlanSgtMappingTable_Object = MibTable
ctspVlanSgtMappingTable = _CtspVlanSgtMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ctspVlanSgtMappingTable.setStatus("current")
_CtspVlanSgtMappingEntry_Object = MibTableRow
ctspVlanSgtMappingEntry = _CtspVlanSgtMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7, 1, 1)
)
ctspVlanSgtMappingEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanSgtMappingIndex"),
)
if mibBuilder.loadTexts:
    ctspVlanSgtMappingEntry.setStatus("current")
_CtspVlanSgtMappingIndex_Type = VlanIndex
_CtspVlanSgtMappingIndex_Object = MibTableColumn
ctspVlanSgtMappingIndex = _CtspVlanSgtMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7, 1, 1, 1),
    _CtspVlanSgtMappingIndex_Type()
)
ctspVlanSgtMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctspVlanSgtMappingIndex.setStatus("current")
_CtspVlanSgtMapValue_Type = CtsSecurityGroupTag
_CtspVlanSgtMapValue_Object = MibTableColumn
ctspVlanSgtMapValue = _CtspVlanSgtMapValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7, 1, 1, 2),
    _CtspVlanSgtMapValue_Type()
)
ctspVlanSgtMapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanSgtMapValue.setStatus("current")


class _CtspVlanSgtStorageType_Type(StorageType):
    """Custom type ctspVlanSgtStorageType based on StorageType"""


_CtspVlanSgtStorageType_Object = MibTableColumn
ctspVlanSgtStorageType = _CtspVlanSgtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7, 1, 1, 3),
    _CtspVlanSgtStorageType_Type()
)
ctspVlanSgtStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanSgtStorageType.setStatus("current")
_CtspVlanSgtRowStatus_Type = RowStatus
_CtspVlanSgtRowStatus_Object = MibTableColumn
ctspVlanSgtRowStatus = _CtspVlanSgtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 7, 1, 1, 4),
    _CtspVlanSgtRowStatus_Type()
)
ctspVlanSgtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctspVlanSgtRowStatus.setStatus("current")
_CtspSgtCaching_ObjectIdentity = ObjectIdentity
ctspSgtCaching = _CtspSgtCaching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 8)
)


class _CtspSgtCachingMode_Type(Integer32):
    """Custom type ctspSgtCachingMode based on Integer32"""
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
        *(("none", 1),
          ("standAlone", 2),
          ("vlan", 4),
          ("withEnforcement", 3))
    )


_CtspSgtCachingMode_Type.__name__ = "Integer32"
_CtspSgtCachingMode_Object = MibScalar
ctspSgtCachingMode = _CtspSgtCachingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 8, 1),
    _CtspSgtCachingMode_Type()
)
ctspSgtCachingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgtCachingMode.setStatus("current")
_CtspSgtCachingVlansFirst2K_Type = Cisco2KVlanList
_CtspSgtCachingVlansFirst2K_Object = MibScalar
ctspSgtCachingVlansFirst2K = _CtspSgtCachingVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 8, 2),
    _CtspSgtCachingVlansFirst2K_Type()
)
ctspSgtCachingVlansFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgtCachingVlansFirst2K.setStatus("current")
_CtspSgtCachingVlansSecond2K_Type = Cisco2KVlanList
_CtspSgtCachingVlansSecond2K_Object = MibScalar
ctspSgtCachingVlansSecond2K = _CtspSgtCachingVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 8, 3),
    _CtspSgtCachingVlansSecond2K_Type()
)
ctspSgtCachingVlansSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspSgtCachingVlansSecond2K.setStatus("current")
_CtspNotifsControl_ObjectIdentity = ObjectIdentity
ctspNotifsControl = _CtspNotifsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 9)
)
_CtspPeerPolicyUpdatedNotifEnable_Type = TruthValue
_CtspPeerPolicyUpdatedNotifEnable_Object = MibScalar
ctspPeerPolicyUpdatedNotifEnable = _CtspPeerPolicyUpdatedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 9, 1),
    _CtspPeerPolicyUpdatedNotifEnable_Type()
)
ctspPeerPolicyUpdatedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspPeerPolicyUpdatedNotifEnable.setStatus("current")
_CtspAuthorizationSgaclFailNotifEnable_Type = TruthValue
_CtspAuthorizationSgaclFailNotifEnable_Object = MibScalar
ctspAuthorizationSgaclFailNotifEnable = _CtspAuthorizationSgaclFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 9, 2),
    _CtspAuthorizationSgaclFailNotifEnable_Type()
)
ctspAuthorizationSgaclFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctspAuthorizationSgaclFailNotifEnable.setStatus("current")
_CtspNotifsOnlyInfo_ObjectIdentity = ObjectIdentity
ctspNotifsOnlyInfo = _CtspNotifsOnlyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 10)
)
_CtspOldPeerSgt_Type = CtsSecurityGroupTag
_CtspOldPeerSgt_Object = MibScalar
ctspOldPeerSgt = _CtspOldPeerSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 10, 1),
    _CtspOldPeerSgt_Type()
)
ctspOldPeerSgt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctspOldPeerSgt.setStatus("current")


class _CtspAuthorizationSgaclFailReason_Type(Integer32):
    """Custom type ctspAuthorizationSgaclFailReason based on Integer32"""
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
        *(("downloadACE", 1),
          ("downloadDst", 3),
          ("downloadSrc", 2),
          ("installForIP", 6),
          ("installPolicy", 4),
          ("installPolicyStandby", 5),
          ("uninstall", 7))
    )


_CtspAuthorizationSgaclFailReason_Type.__name__ = "Integer32"
_CtspAuthorizationSgaclFailReason_Object = MibScalar
ctspAuthorizationSgaclFailReason = _CtspAuthorizationSgaclFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 10, 2),
    _CtspAuthorizationSgaclFailReason_Type()
)
ctspAuthorizationSgaclFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctspAuthorizationSgaclFailReason.setStatus("current")
_CtspAuthorizationSgaclFailInfo_Type = SnmpAdminString
_CtspAuthorizationSgaclFailInfo_Object = MibScalar
ctspAuthorizationSgaclFailInfo = _CtspAuthorizationSgaclFailInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 1, 10, 3),
    _CtspAuthorizationSgaclFailInfo_Type()
)
ctspAuthorizationSgaclFailInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctspAuthorizationSgaclFailInfo.setStatus("current")
_CiscoTrustSecPolicyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoTrustSecPolicyMIBConformance = _CiscoTrustSecPolicyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2)
)
_CiscoTrustSecPolicyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTrustSecPolicyMIBCompliances = _CiscoTrustSecPolicyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 1)
)
_CiscoTrustSecPolicyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTrustSecPolicyMIBGroups = _CiscoTrustSecPolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2)
)

# Managed Objects groups

ctspGlobalSgaclEnforcementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 1)
)
ctspGlobalSgaclEnforcementGroup.setObjects(
    ("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgaclEnforcementEnable")
)
if mibBuilder.loadTexts:
    ctspGlobalSgaclEnforcementGroup.setStatus("current")

ctspSgaclIpv4DropNetflowMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 2)
)
ctspSgaclIpv4DropNetflowMonitorGroup.setObjects(
    ("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgaclIpv4DropNetflowMonitor")
)
if mibBuilder.loadTexts:
    ctspSgaclIpv4DropNetflowMonitorGroup.setStatus("current")

ctspSgaclIpv6DropNetflowMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 3)
)
ctspSgaclIpv6DropNetflowMonitorGroup.setObjects(
    ("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgaclIpv6DropNetflowMonitor")
)
if mibBuilder.loadTexts:
    ctspSgaclIpv6DropNetflowMonitorGroup.setStatus("current")

ctspVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 4)
)
ctspVlanConfigGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanConfigSgaclEnforcement"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanSviActive"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanConfigVrfName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanConfigStorageType"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ctspVlanConfigGroup.setStatus("current")

ctspConfigSgaclMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 5)
)
ctspConfigSgaclMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMappingSgaclName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMappingStorageType"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMappingRowStatus"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefConfigIpv4Sgacls"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefConfigIpv6Sgacls"))
)
if mibBuilder.loadTexts:
    ctspConfigSgaclMappingGroup.setStatus("current")

ctspDownloadedSgaclMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 6)
)
ctspDownloadedSgaclMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgaclName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgaclGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedIpTrafficType"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefDownloadedSgaclName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefDownloadedSgaclGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefDownloadedIpTrafficType"))
)
if mibBuilder.loadTexts:
    ctspDownloadedSgaclMappingGroup.setStatus("current")

ctspOperSgaclMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 7)
)
ctspOperSgaclMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspOperationalSgaclName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspOperationalSgaclGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspOperSgaclMappingSource"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspOperSgaclConfigSource"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperationalSgaclName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperationalSgaclGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperSgaclMappingSource"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperSgaclConfigSource"))
)
if mibBuilder.loadTexts:
    ctspOperSgaclMappingGroup.setStatus("current")

ctspIpSwStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 8)
)
ctspIpSwStatisticsGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpSwDropPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpSwPermitPkts"))
)
if mibBuilder.loadTexts:
    ctspIpSwStatisticsGroup.setStatus("current")

ctspIpHwStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 9)
)
ctspIpHwStatisticsGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpHwDropPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpHwPermitPkts"))
)
if mibBuilder.loadTexts:
    ctspIpHwStatisticsGroup.setStatus("current")

ctspDefSwStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 10)
)
ctspDefSwStatisticsGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpSwDropPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpSwPermitPkts"))
)
if mibBuilder.loadTexts:
    ctspDefSwStatisticsGroup.setStatus("current")

ctspDefHwStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 11)
)
ctspDefHwStatisticsGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpHwDropPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpHwPermitPkts"))
)
if mibBuilder.loadTexts:
    ctspDefHwStatisticsGroup.setStatus("current")

ctspPeerPolicyActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 12)
)
ctspPeerPolicyActionGroup.setObjects(
    ("CISCO-TRUSTSEC-POLICY-MIB", "ctspAllPeerPolicyAction")
)
if mibBuilder.loadTexts:
    ctspPeerPolicyActionGroup.setStatus("current")

ctspPeerPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 13)
)
ctspPeerPolicyGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerSgt"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerSgtGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerTrustState"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerPolicyLifeTime"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerPolicyLastUpdate"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerPolicyAction"))
)
if mibBuilder.loadTexts:
    ctspPeerPolicyGroup.setStatus("current")

ctspLayer3TransportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 14)
)
ctspLayer3TransportGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspLayer3PolicyLocalConfig"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspLayer3PolicyDownloaded"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspLayer3PolicyOperational"))
)
if mibBuilder.loadTexts:
    ctspLayer3TransportGroup.setStatus("current")

ctspIfL3PolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 15)
)
ctspIfL3PolicyConfigGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspIfL3Ipv4PolicyEnabled"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIfL3Ipv6PolicyEnabled"))
)
if mibBuilder.loadTexts:
    ctspIfL3PolicyConfigGroup.setStatus("current")

ctspIpSgtMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 16)
)
ctspIpSgtMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtValue"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtSource"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtStorageType"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIpSgtRowStatus"))
)
if mibBuilder.loadTexts:
    ctspIpSgtMappingGroup.setStatus("current")

ctspSgtPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 17)
)
ctspSgtPolicyGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspAllSgtPolicyAction"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgtPolicySgtGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgtPolicyLifeTime"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgtPolicyLastUpdate"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgtPolicyAction"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedDefSgtPolicySgtGenId"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedDefSgtPolicyLifeTime"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedDefSgtPolicyLastUpdate"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedDefSgtPolicyAction"))
)
if mibBuilder.loadTexts:
    ctspSgtPolicyGroup.setStatus("current")

ctspIfSgtMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 18)
)
ctspIfSgtMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspIfSgtValue"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIfSgName"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspL3IPMStatus"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIfSgtStorageType"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspIfSgtRowStatus"))
)
if mibBuilder.loadTexts:
    ctspIfSgtMappingGroup.setStatus("current")

ctspVlanSgtMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 19)
)
ctspVlanSgtMappingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanSgtMapValue"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanSgtStorageType"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspVlanSgtRowStatus"))
)
if mibBuilder.loadTexts:
    ctspVlanSgtMappingGroup.setStatus("current")

ctspSgtCachingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 20)
)
ctspSgtCachingGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgtCachingMode"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgtCachingVlansFirst2K"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgtCachingVlansSecond2K"))
)
if mibBuilder.loadTexts:
    ctspSgtCachingGroup.setStatus("current")

ctspSgaclMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 21)
)
ctspSgaclMonitorGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspSgaclMonitorEnable"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspConfigSgaclMonitor"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefConfigIpv4SgaclsMonitor"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefConfigIpv6SgaclsMonitor"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDownloadedSgaclMonitor"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefDownloadedSgaclMonitor"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspOperSgaclMonitor"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefOperSgaclMonitor"))
)
if mibBuilder.loadTexts:
    ctspSgaclMonitorGroup.setStatus("current")

ctspSgaclMonitorStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 22)
)
ctspSgaclMonitorStatisticGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpSwMonitorPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspStatsIpHwMonitorPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpSwMonitorPkts"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspDefIpHwMonitorPkts"))
)
if mibBuilder.loadTexts:
    ctspSgaclMonitorStatisticGroup.setStatus("current")

ctspNotifCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 23)
)
ctspNotifCtrlGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerPolicyUpdatedNotifEnable"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspAuthorizationSgaclFailNotifEnable"))
)
if mibBuilder.loadTexts:
    ctspNotifCtrlGroup.setStatus("current")

ctspNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 25)
)
ctspNotifInfoGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspOldPeerSgt"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspAuthorizationSgaclFailReason"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspAuthorizationSgaclFailInfo"))
)
if mibBuilder.loadTexts:
    ctspNotifInfoGroup.setStatus("current")


# Notification objects

ctspPeerPolicyUpdatedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 0, 1)
)
ctspPeerPolicyUpdatedNotif.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspOldPeerSgt"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerSgt"))
)
if mibBuilder.loadTexts:
    ctspPeerPolicyUpdatedNotif.setStatus(
        "current"
    )

ctspAuthorizationSgaclFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 0, 2)
)
ctspAuthorizationSgaclFailNotif.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspAuthorizationSgaclFailReason"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspAuthorizationSgaclFailInfo"))
)
if mibBuilder.loadTexts:
    ctspAuthorizationSgaclFailNotif.setStatus(
        "current"
    )


# Notifications groups

ctspNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 2, 24)
)
ctspNotifGroup.setObjects(
      *(("CISCO-TRUSTSEC-POLICY-MIB", "ctspPeerPolicyUpdatedNotif"),
        ("CISCO-TRUSTSEC-POLICY-MIB", "ctspAuthorizationSgaclFailNotif"))
)
if mibBuilder.loadTexts:
    ctspNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTrustSecPolicyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTrustSecPolicyMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTrustSecPolicyMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 713, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTrustSecPolicyMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TRUSTSEC-POLICY-MIB",
    **{"ciscoTrustSecPolicyMIB": ciscoTrustSecPolicyMIB,
       "ciscoTrustSecPolicyMIBNotifs": ciscoTrustSecPolicyMIBNotifs,
       "ctspPeerPolicyUpdatedNotif": ctspPeerPolicyUpdatedNotif,
       "ctspAuthorizationSgaclFailNotif": ctspAuthorizationSgaclFailNotif,
       "ciscoTrustSecPolicyMIBObjects": ciscoTrustSecPolicyMIBObjects,
       "ctspSgacl": ctspSgacl,
       "ctspSgaclGlobals": ctspSgaclGlobals,
       "ctspSgaclEnforcementEnable": ctspSgaclEnforcementEnable,
       "ctspSgaclIpv4DropNetflowMonitor": ctspSgaclIpv4DropNetflowMonitor,
       "ctspSgaclIpv6DropNetflowMonitor": ctspSgaclIpv6DropNetflowMonitor,
       "ctspVlanConfigTable": ctspVlanConfigTable,
       "ctspVlanConfigEntry": ctspVlanConfigEntry,
       "ctspVlanConfigIndex": ctspVlanConfigIndex,
       "ctspVlanConfigSgaclEnforcement": ctspVlanConfigSgaclEnforcement,
       "ctspVlanSviActive": ctspVlanSviActive,
       "ctspVlanConfigVrfName": ctspVlanConfigVrfName,
       "ctspVlanConfigStorageType": ctspVlanConfigStorageType,
       "ctspVlanConfigRowStatus": ctspVlanConfigRowStatus,
       "ctspSgaclMappings": ctspSgaclMappings,
       "ctspConfigSgaclMappingTable": ctspConfigSgaclMappingTable,
       "ctspConfigSgaclMappingEntry": ctspConfigSgaclMappingEntry,
       "ctspConfigSgaclMappingIpTrafficType": ctspConfigSgaclMappingIpTrafficType,
       "ctspConfigSgaclMappingDestSgt": ctspConfigSgaclMappingDestSgt,
       "ctspConfigSgaclMappingSourceSgt": ctspConfigSgaclMappingSourceSgt,
       "ctspConfigSgaclMappingSgaclName": ctspConfigSgaclMappingSgaclName,
       "ctspConfigSgaclMappingStorageType": ctspConfigSgaclMappingStorageType,
       "ctspConfigSgaclMappingRowStatus": ctspConfigSgaclMappingRowStatus,
       "ctspConfigSgaclMonitor": ctspConfigSgaclMonitor,
       "ctspDefConfigIpv4Sgacls": ctspDefConfigIpv4Sgacls,
       "ctspDefConfigIpv6Sgacls": ctspDefConfigIpv6Sgacls,
       "ctspDownloadedSgaclMappingTable": ctspDownloadedSgaclMappingTable,
       "ctspDownloadedSgaclMappingEntry": ctspDownloadedSgaclMappingEntry,
       "ctspDownloadedSgaclDestSgt": ctspDownloadedSgaclDestSgt,
       "ctspDownloadedSgaclSourceSgt": ctspDownloadedSgaclSourceSgt,
       "ctspDownloadedSgaclIndex": ctspDownloadedSgaclIndex,
       "ctspDownloadedSgaclName": ctspDownloadedSgaclName,
       "ctspDownloadedSgaclGenId": ctspDownloadedSgaclGenId,
       "ctspDownloadedIpTrafficType": ctspDownloadedIpTrafficType,
       "ctspDownloadedSgaclMonitor": ctspDownloadedSgaclMonitor,
       "ctspDefDownloadedSgaclMappingTable": ctspDefDownloadedSgaclMappingTable,
       "ctspDefDownloadedSgaclMappingEntry": ctspDefDownloadedSgaclMappingEntry,
       "ctspDefDownloadedSgaclIndex": ctspDefDownloadedSgaclIndex,
       "ctspDefDownloadedSgaclName": ctspDefDownloadedSgaclName,
       "ctspDefDownloadedSgaclGenId": ctspDefDownloadedSgaclGenId,
       "ctspDefDownloadedIpTrafficType": ctspDefDownloadedIpTrafficType,
       "ctspDefDownloadedSgaclMonitor": ctspDefDownloadedSgaclMonitor,
       "ctspOperSgaclMappingTable": ctspOperSgaclMappingTable,
       "ctspOperSgaclMappingEntry": ctspOperSgaclMappingEntry,
       "ctspOperIpTrafficType": ctspOperIpTrafficType,
       "ctspOperSgaclDestSgt": ctspOperSgaclDestSgt,
       "ctspOperSgaclSourceSgt": ctspOperSgaclSourceSgt,
       "ctspOperSgaclIndex": ctspOperSgaclIndex,
       "ctspOperationalSgaclName": ctspOperationalSgaclName,
       "ctspOperationalSgaclGenId": ctspOperationalSgaclGenId,
       "ctspOperSgaclMappingSource": ctspOperSgaclMappingSource,
       "ctspOperSgaclConfigSource": ctspOperSgaclConfigSource,
       "ctspOperSgaclMonitor": ctspOperSgaclMonitor,
       "ctspDefOperSgaclMappingTable": ctspDefOperSgaclMappingTable,
       "ctspDefOperSgaclMappingEntry": ctspDefOperSgaclMappingEntry,
       "ctspDefOperIpTrafficType": ctspDefOperIpTrafficType,
       "ctspDefOperSgaclIndex": ctspDefOperSgaclIndex,
       "ctspDefOperationalSgaclName": ctspDefOperationalSgaclName,
       "ctspDefOperationalSgaclGenId": ctspDefOperationalSgaclGenId,
       "ctspDefOperSgaclMappingSource": ctspDefOperSgaclMappingSource,
       "ctspDefOperSgaclConfigSource": ctspDefOperSgaclConfigSource,
       "ctspDefOperSgaclMonitor": ctspDefOperSgaclMonitor,
       "ctspDefConfigIpv4SgaclsMonitor": ctspDefConfigIpv4SgaclsMonitor,
       "ctspDefConfigIpv6SgaclsMonitor": ctspDefConfigIpv6SgaclsMonitor,
       "ctspSgaclMonitorEnable": ctspSgaclMonitorEnable,
       "ctspSgaclStatistics": ctspSgaclStatistics,
       "ctspSgtStatsTable": ctspSgtStatsTable,
       "ctspSgtStatsEntry": ctspSgtStatsEntry,
       "ctspStatsIpTrafficType": ctspStatsIpTrafficType,
       "ctspStatsDestSgt": ctspStatsDestSgt,
       "ctspStatsSourceSgt": ctspStatsSourceSgt,
       "ctspStatsIpSwDropPkts": ctspStatsIpSwDropPkts,
       "ctspStatsIpHwDropPkts": ctspStatsIpHwDropPkts,
       "ctspStatsIpSwPermitPkts": ctspStatsIpSwPermitPkts,
       "ctspStatsIpHwPermitPkts": ctspStatsIpHwPermitPkts,
       "ctspStatsIpSwMonitorPkts": ctspStatsIpSwMonitorPkts,
       "ctspStatsIpHwMonitorPkts": ctspStatsIpHwMonitorPkts,
       "ctspDefStatsTable": ctspDefStatsTable,
       "ctspDefStatsEntry": ctspDefStatsEntry,
       "ctspDefIpTrafficType": ctspDefIpTrafficType,
       "ctspDefIpSwDropPkts": ctspDefIpSwDropPkts,
       "ctspDefIpHwDropPkts": ctspDefIpHwDropPkts,
       "ctspDefIpSwPermitPkts": ctspDefIpSwPermitPkts,
       "ctspDefIpHwPermitPkts": ctspDefIpHwPermitPkts,
       "ctspDefIpSwMonitorPkts": ctspDefIpSwMonitorPkts,
       "ctspDefIpHwMonitorPkts": ctspDefIpHwMonitorPkts,
       "ctspPeerPolicy": ctspPeerPolicy,
       "ctspAllPeerPolicyAction": ctspAllPeerPolicyAction,
       "ctspPeerPolicyTable": ctspPeerPolicyTable,
       "ctspPeerPolicyEntry": ctspPeerPolicyEntry,
       "ctspPeerName": ctspPeerName,
       "ctspPeerSgt": ctspPeerSgt,
       "ctspPeerSgtGenId": ctspPeerSgtGenId,
       "ctspPeerTrustState": ctspPeerTrustState,
       "ctspPeerPolicyLifeTime": ctspPeerPolicyLifeTime,
       "ctspPeerPolicyLastUpdate": ctspPeerPolicyLastUpdate,
       "ctspPeerPolicyAction": ctspPeerPolicyAction,
       "ctspLayer3Transport": ctspLayer3Transport,
       "ctspLayer3PolicyTable": ctspLayer3PolicyTable,
       "ctspLayer3PolicyEntry": ctspLayer3PolicyEntry,
       "ctspLayer3PolicyIpTrafficType": ctspLayer3PolicyIpTrafficType,
       "ctspLayer3PolicyType": ctspLayer3PolicyType,
       "ctspLayer3PolicyLocalConfig": ctspLayer3PolicyLocalConfig,
       "ctspLayer3PolicyDownloaded": ctspLayer3PolicyDownloaded,
       "ctspLayer3PolicyOperational": ctspLayer3PolicyOperational,
       "ctspIfL3PolicyConfigTable": ctspIfL3PolicyConfigTable,
       "ctspIfL3PolicyConfigEntry": ctspIfL3PolicyConfigEntry,
       "ctspIfL3Ipv4PolicyEnabled": ctspIfL3Ipv4PolicyEnabled,
       "ctspIfL3Ipv6PolicyEnabled": ctspIfL3Ipv6PolicyEnabled,
       "ctspIpSgtMappings": ctspIpSgtMappings,
       "ctspIpSgtMappingTable": ctspIpSgtMappingTable,
       "ctspIpSgtMappingEntry": ctspIpSgtMappingEntry,
       "ctspIpSgtVrfName": ctspIpSgtVrfName,
       "ctspIpSgtAddressType": ctspIpSgtAddressType,
       "ctspIpSgtIpAddress": ctspIpSgtIpAddress,
       "ctspIpSgtAddressLength": ctspIpSgtAddressLength,
       "ctspIpSgtValue": ctspIpSgtValue,
       "ctspIpSgtSource": ctspIpSgtSource,
       "ctspIpSgtStorageType": ctspIpSgtStorageType,
       "ctspIpSgtRowStatus": ctspIpSgtRowStatus,
       "ctspSgtPolicy": ctspSgtPolicy,
       "ctspAllSgtPolicyAction": ctspAllSgtPolicyAction,
       "ctspDownloadedSgtPolicyTable": ctspDownloadedSgtPolicyTable,
       "ctspDownloadedSgtPolicyEntry": ctspDownloadedSgtPolicyEntry,
       "ctspDownloadedSgtPolicySgt": ctspDownloadedSgtPolicySgt,
       "ctspDownloadedSgtPolicySgtGenId": ctspDownloadedSgtPolicySgtGenId,
       "ctspDownloadedSgtPolicyLifeTime": ctspDownloadedSgtPolicyLifeTime,
       "ctspDownloadedSgtPolicyLastUpdate": ctspDownloadedSgtPolicyLastUpdate,
       "ctspDownloadedSgtPolicyAction": ctspDownloadedSgtPolicyAction,
       "ctspDownloadedDefSgtPolicyTable": ctspDownloadedDefSgtPolicyTable,
       "ctspDownloadedDefSgtPolicyEntry": ctspDownloadedDefSgtPolicyEntry,
       "ctspDownloadedDefSgtPolicyType": ctspDownloadedDefSgtPolicyType,
       "ctspDownloadedDefSgtPolicySgtGenId": ctspDownloadedDefSgtPolicySgtGenId,
       "ctspDownloadedDefSgtPolicyLifeTime": ctspDownloadedDefSgtPolicyLifeTime,
       "ctspDownloadedDefSgtPolicyLastUpdate": ctspDownloadedDefSgtPolicyLastUpdate,
       "ctspDownloadedDefSgtPolicyAction": ctspDownloadedDefSgtPolicyAction,
       "ctspIfSgtMappings": ctspIfSgtMappings,
       "ctspIfSgtMappingTable": ctspIfSgtMappingTable,
       "ctspIfSgtMappingEntry": ctspIfSgtMappingEntry,
       "ctspIfSgtValue": ctspIfSgtValue,
       "ctspIfSgName": ctspIfSgName,
       "ctspIfSgtStorageType": ctspIfSgtStorageType,
       "ctspIfSgtRowStatus": ctspIfSgtRowStatus,
       "ctspIfSgtMappingInfoTable": ctspIfSgtMappingInfoTable,
       "ctspIfSgtMappingInfoEntry": ctspIfSgtMappingInfoEntry,
       "ctspL3IPMStatus": ctspL3IPMStatus,
       "ctspVlanSgtMappings": ctspVlanSgtMappings,
       "ctspVlanSgtMappingTable": ctspVlanSgtMappingTable,
       "ctspVlanSgtMappingEntry": ctspVlanSgtMappingEntry,
       "ctspVlanSgtMappingIndex": ctspVlanSgtMappingIndex,
       "ctspVlanSgtMapValue": ctspVlanSgtMapValue,
       "ctspVlanSgtStorageType": ctspVlanSgtStorageType,
       "ctspVlanSgtRowStatus": ctspVlanSgtRowStatus,
       "ctspSgtCaching": ctspSgtCaching,
       "ctspSgtCachingMode": ctspSgtCachingMode,
       "ctspSgtCachingVlansFirst2K": ctspSgtCachingVlansFirst2K,
       "ctspSgtCachingVlansSecond2K": ctspSgtCachingVlansSecond2K,
       "ctspNotifsControl": ctspNotifsControl,
       "ctspPeerPolicyUpdatedNotifEnable": ctspPeerPolicyUpdatedNotifEnable,
       "ctspAuthorizationSgaclFailNotifEnable": ctspAuthorizationSgaclFailNotifEnable,
       "ctspNotifsOnlyInfo": ctspNotifsOnlyInfo,
       "ctspOldPeerSgt": ctspOldPeerSgt,
       "ctspAuthorizationSgaclFailReason": ctspAuthorizationSgaclFailReason,
       "ctspAuthorizationSgaclFailInfo": ctspAuthorizationSgaclFailInfo,
       "ciscoTrustSecPolicyMIBConformance": ciscoTrustSecPolicyMIBConformance,
       "ciscoTrustSecPolicyMIBCompliances": ciscoTrustSecPolicyMIBCompliances,
       "ciscoTrustSecPolicyMIBCompliance": ciscoTrustSecPolicyMIBCompliance,
       "ciscoTrustSecPolicyMIBComplianceRev2": ciscoTrustSecPolicyMIBComplianceRev2,
       "ciscoTrustSecPolicyMIBGroups": ciscoTrustSecPolicyMIBGroups,
       "ctspGlobalSgaclEnforcementGroup": ctspGlobalSgaclEnforcementGroup,
       "ctspSgaclIpv4DropNetflowMonitorGroup": ctspSgaclIpv4DropNetflowMonitorGroup,
       "ctspSgaclIpv6DropNetflowMonitorGroup": ctspSgaclIpv6DropNetflowMonitorGroup,
       "ctspVlanConfigGroup": ctspVlanConfigGroup,
       "ctspConfigSgaclMappingGroup": ctspConfigSgaclMappingGroup,
       "ctspDownloadedSgaclMappingGroup": ctspDownloadedSgaclMappingGroup,
       "ctspOperSgaclMappingGroup": ctspOperSgaclMappingGroup,
       "ctspIpSwStatisticsGroup": ctspIpSwStatisticsGroup,
       "ctspIpHwStatisticsGroup": ctspIpHwStatisticsGroup,
       "ctspDefSwStatisticsGroup": ctspDefSwStatisticsGroup,
       "ctspDefHwStatisticsGroup": ctspDefHwStatisticsGroup,
       "ctspPeerPolicyActionGroup": ctspPeerPolicyActionGroup,
       "ctspPeerPolicyGroup": ctspPeerPolicyGroup,
       "ctspLayer3TransportGroup": ctspLayer3TransportGroup,
       "ctspIfL3PolicyConfigGroup": ctspIfL3PolicyConfigGroup,
       "ctspIpSgtMappingGroup": ctspIpSgtMappingGroup,
       "ctspSgtPolicyGroup": ctspSgtPolicyGroup,
       "ctspIfSgtMappingGroup": ctspIfSgtMappingGroup,
       "ctspVlanSgtMappingGroup": ctspVlanSgtMappingGroup,
       "ctspSgtCachingGroup": ctspSgtCachingGroup,
       "ctspSgaclMonitorGroup": ctspSgaclMonitorGroup,
       "ctspSgaclMonitorStatisticGroup": ctspSgaclMonitorStatisticGroup,
       "ctspNotifCtrlGroup": ctspNotifCtrlGroup,
       "ctspNotifGroup": ctspNotifGroup,
       "ctspNotifInfoGroup": ctspNotifInfoGroup}
)
