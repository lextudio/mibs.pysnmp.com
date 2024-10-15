# SNMP MIB module (CISCO-TRUSTSEC-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TRUSTSEC-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:52 2024
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

(CtsAcsAuthorityIdentity,) = mibBuilder.importSymbols(
    "CISCO-TRUSTSEC-TC-MIB",
    "CtsAcsAuthorityIdentity")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTrustSecServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741)
)
ciscoTrustSecServerMIB.setRevisions(
        ("2011-12-07 00:00",
         "2010-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTrustSecServerMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTrustSecServerMIBNotifs = _CiscoTrustSecServerMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 0)
)
_CiscoTrustSecServerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTrustSecServerMIBObjects = _CiscoTrustSecServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1)
)
_CtsvGlobalServerConfigObjects_ObjectIdentity = ObjectIdentity
ctsvGlobalServerConfigObjects = _CtsvGlobalServerConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1)
)
_CtsvAuthorizationList_Type = SnmpAdminString
_CtsvAuthorizationList_Object = MibScalar
ctsvAuthorizationList = _CtsvAuthorizationList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 1),
    _CtsvAuthorizationList_Type()
)
ctsvAuthorizationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvAuthorizationList.setStatus("current")
_CtsvServerDeadTime_Type = Unsigned32
_CtsvServerDeadTime_Object = MibScalar
ctsvServerDeadTime = _CtsvServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 2),
    _CtsvServerDeadTime_Type()
)
ctsvServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvServerDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsvServerDeadTime.setUnits("seconds")


class _CtsvServerLoadBalanceMethod_Type(Integer32):
    """Custom type ctsvServerLoadBalanceMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leastOutstanding", 2),
          ("none", 1))
    )


_CtsvServerLoadBalanceMethod_Type.__name__ = "Integer32"
_CtsvServerLoadBalanceMethod_Object = MibScalar
ctsvServerLoadBalanceMethod = _CtsvServerLoadBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 3),
    _CtsvServerLoadBalanceMethod_Type()
)
ctsvServerLoadBalanceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvServerLoadBalanceMethod.setStatus("current")
_CtsvServerLoadBalanceBatchSize_Type = Unsigned32
_CtsvServerLoadBalanceBatchSize_Object = MibScalar
ctsvServerLoadBalanceBatchSize = _CtsvServerLoadBalanceBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 4),
    _CtsvServerLoadBalanceBatchSize_Type()
)
ctsvServerLoadBalanceBatchSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvServerLoadBalanceBatchSize.setStatus("current")
_CtsvUseSameProvisionedServer_Type = TruthValue
_CtsvUseSameProvisionedServer_Object = MibScalar
ctsvUseSameProvisionedServer = _CtsvUseSameProvisionedServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 5),
    _CtsvUseSameProvisionedServer_Type()
)
ctsvUseSameProvisionedServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvUseSameProvisionedServer.setStatus("current")
_CtsvAllServerTestEnabled_Type = TruthValue
_CtsvAllServerTestEnabled_Object = MibScalar
ctsvAllServerTestEnabled = _CtsvAllServerTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 6),
    _CtsvAllServerTestEnabled_Type()
)
ctsvAllServerTestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvAllServerTestEnabled.setStatus("current")
_CtsvAllServerTestDeadTime_Type = Unsigned32
_CtsvAllServerTestDeadTime_Object = MibScalar
ctsvAllServerTestDeadTime = _CtsvAllServerTestDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 7),
    _CtsvAllServerTestDeadTime_Type()
)
ctsvAllServerTestDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvAllServerTestDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsvAllServerTestDeadTime.setUnits("seconds")
_CtsvAllServerTestInterval_Type = Unsigned32
_CtsvAllServerTestInterval_Object = MibScalar
ctsvAllServerTestInterval = _CtsvAllServerTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 8),
    _CtsvAllServerTestInterval_Type()
)
ctsvAllServerTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvAllServerTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsvAllServerTestInterval.setUnits("minutes")
_CtsvServerKeyWrapEnabled_Type = TruthValue
_CtsvServerKeyWrapEnabled_Object = MibScalar
ctsvServerKeyWrapEnabled = _CtsvServerKeyWrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 1, 9),
    _CtsvServerKeyWrapEnabled_Type()
)
ctsvServerKeyWrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvServerKeyWrapEnabled.setStatus("current")
_CtsvServerTestConfigObjects_ObjectIdentity = ObjectIdentity
ctsvServerTestConfigObjects = _CtsvServerTestConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2)
)
_CtsvServerTestConfigTable_Object = MibTable
ctsvServerTestConfigTable = _CtsvServerTestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctsvServerTestConfigTable.setStatus("current")
_CtsvServerTestConfigEntry_Object = MibTableRow
ctsvServerTestConfigEntry = _CtsvServerTestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1)
)
ctsvServerTestConfigEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestAddrType"),
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestAddr"),
)
if mibBuilder.loadTexts:
    ctsvServerTestConfigEntry.setStatus("current")
_CtsvServerTestAddrType_Type = InetAddressType
_CtsvServerTestAddrType_Object = MibTableColumn
ctsvServerTestAddrType = _CtsvServerTestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 1),
    _CtsvServerTestAddrType_Type()
)
ctsvServerTestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvServerTestAddrType.setStatus("current")


class _CtsvServerTestAddr_Type(InetAddress):
    """Custom type ctsvServerTestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsvServerTestAddr_Type.__name__ = "InetAddress"
_CtsvServerTestAddr_Object = MibTableColumn
ctsvServerTestAddr = _CtsvServerTestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 2),
    _CtsvServerTestAddr_Type()
)
ctsvServerTestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvServerTestAddr.setStatus("current")
_CtsvServerTestEnabled_Type = TruthValue
_CtsvServerTestEnabled_Object = MibTableColumn
ctsvServerTestEnabled = _CtsvServerTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 3),
    _CtsvServerTestEnabled_Type()
)
ctsvServerTestEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsvServerTestEnabled.setStatus("current")
_CtsvServerTestDeadTime_Type = Unsigned32
_CtsvServerTestDeadTime_Object = MibTableColumn
ctsvServerTestDeadTime = _CtsvServerTestDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 4),
    _CtsvServerTestDeadTime_Type()
)
ctsvServerTestDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsvServerTestDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsvServerTestDeadTime.setUnits("seconds")
_CtsvServerTestInterval_Type = Unsigned32
_CtsvServerTestInterval_Object = MibTableColumn
ctsvServerTestInterval = _CtsvServerTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 5),
    _CtsvServerTestInterval_Type()
)
ctsvServerTestInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsvServerTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsvServerTestInterval.setUnits("minutes")


class _CtsvServerTestStorageType_Type(StorageType):
    """Custom type ctsvServerTestStorageType based on StorageType"""


_CtsvServerTestStorageType_Object = MibTableColumn
ctsvServerTestStorageType = _CtsvServerTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 6),
    _CtsvServerTestStorageType_Type()
)
ctsvServerTestStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsvServerTestStorageType.setStatus("current")
_CtsvServerTestRowStatus_Type = RowStatus
_CtsvServerTestRowStatus_Object = MibTableColumn
ctsvServerTestRowStatus = _CtsvServerTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 2, 1, 1, 7),
    _CtsvServerTestRowStatus_Type()
)
ctsvServerTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsvServerTestRowStatus.setStatus("current")
_CtsvProvisionedServerObjects_ObjectIdentity = ObjectIdentity
ctsvProvisionedServerObjects = _CtsvProvisionedServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3)
)
_CtsvProvisionedServerTable_Object = MibTable
ctsvProvisionedServerTable = _CtsvProvisionedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctsvProvisionedServerTable.setStatus("current")
_CtsvProvisionedServerEntry_Object = MibTableRow
ctsvProvisionedServerEntry = _CtsvProvisionedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1)
)
ctsvProvisionedServerEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerAddrType"),
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerAddr"),
)
if mibBuilder.loadTexts:
    ctsvProvisionedServerEntry.setStatus("current")
_CtsvProvisionedServerAddrType_Type = InetAddressType
_CtsvProvisionedServerAddrType_Object = MibTableColumn
ctsvProvisionedServerAddrType = _CtsvProvisionedServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 1),
    _CtsvProvisionedServerAddrType_Type()
)
ctsvProvisionedServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvProvisionedServerAddrType.setStatus("current")


class _CtsvProvisionedServerAddr_Type(InetAddress):
    """Custom type ctsvProvisionedServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsvProvisionedServerAddr_Type.__name__ = "InetAddress"
_CtsvProvisionedServerAddr_Object = MibTableColumn
ctsvProvisionedServerAddr = _CtsvProvisionedServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 2),
    _CtsvProvisionedServerAddr_Type()
)
ctsvProvisionedServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvProvisionedServerAddr.setStatus("current")
_CtsvProvisionedServerPort_Type = InetPortNumber
_CtsvProvisionedServerPort_Object = MibTableColumn
ctsvProvisionedServerPort = _CtsvProvisionedServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 3),
    _CtsvProvisionedServerPort_Type()
)
ctsvProvisionedServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerPort.setStatus("current")
_CtsvProvisionedServerAuthorityId_Type = CtsAcsAuthorityIdentity
_CtsvProvisionedServerAuthorityId_Object = MibTableColumn
ctsvProvisionedServerAuthorityId = _CtsvProvisionedServerAuthorityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 4),
    _CtsvProvisionedServerAuthorityId_Type()
)
ctsvProvisionedServerAuthorityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerAuthorityId.setStatus("current")


class _CtsvProvisionedServerStatus_Type(Integer32):
    """Custom type ctsvProvisionedServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_CtsvProvisionedServerStatus_Type.__name__ = "Integer32"
_CtsvProvisionedServerStatus_Object = MibTableColumn
ctsvProvisionedServerStatus = _CtsvProvisionedServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 5),
    _CtsvProvisionedServerStatus_Type()
)
ctsvProvisionedServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerStatus.setStatus("current")
_CtsvProvisionedServerTestEnabled_Type = TruthValue
_CtsvProvisionedServerTestEnabled_Object = MibTableColumn
ctsvProvisionedServerTestEnabled = _CtsvProvisionedServerTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 6),
    _CtsvProvisionedServerTestEnabled_Type()
)
ctsvProvisionedServerTestEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerTestEnabled.setStatus("current")
_CtsvProvisionedServerTestInterval_Type = Unsigned32
_CtsvProvisionedServerTestInterval_Object = MibTableColumn
ctsvProvisionedServerTestInterval = _CtsvProvisionedServerTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 7),
    _CtsvProvisionedServerTestInterval_Type()
)
ctsvProvisionedServerTestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsvProvisionedServerTestInterval.setUnits("minutes")
_CtsvProvisionedServerTestDeadTime_Type = Unsigned32
_CtsvProvisionedServerTestDeadTime_Object = MibTableColumn
ctsvProvisionedServerTestDeadTime = _CtsvProvisionedServerTestDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 8),
    _CtsvProvisionedServerTestDeadTime_Type()
)
ctsvProvisionedServerTestDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerTestDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsvProvisionedServerTestDeadTime.setUnits("seconds")
_CtsvProvisionedServerKeyWrapEnabled_Type = TruthValue
_CtsvProvisionedServerKeyWrapEnabled_Object = MibTableColumn
ctsvProvisionedServerKeyWrapEnabled = _CtsvProvisionedServerKeyWrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 3, 1, 1, 9),
    _CtsvProvisionedServerKeyWrapEnabled_Type()
)
ctsvProvisionedServerKeyWrapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvProvisionedServerKeyWrapEnabled.setStatus("current")
_CtsvDownloadServerListObjects_ObjectIdentity = ObjectIdentity
ctsvDownloadServerListObjects = _CtsvDownloadServerListObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 4)
)
_CtsvDownloadServerListTable_Object = MibTable
ctsvDownloadServerListTable = _CtsvDownloadServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ctsvDownloadServerListTable.setStatus("current")
_CtsvDownloadServerListEntry_Object = MibTableRow
ctsvDownloadServerListEntry = _CtsvDownloadServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 4, 1, 1)
)
ctsvDownloadServerListEntry.setIndexNames(
    (1, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerListName"),
)
if mibBuilder.loadTexts:
    ctsvDownloadServerListEntry.setStatus("current")


class _CtsvDownloadServerListName_Type(SnmpAdminString):
    """Custom type ctsvDownloadServerListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CtsvDownloadServerListName_Type.__name__ = "SnmpAdminString"
_CtsvDownloadServerListName_Object = MibTableColumn
ctsvDownloadServerListName = _CtsvDownloadServerListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 4, 1, 1, 1),
    _CtsvDownloadServerListName_Type()
)
ctsvDownloadServerListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvDownloadServerListName.setStatus("current")


class _CtsvDownloadServerListGenNum_Type(OctetString):
    """Custom type ctsvDownloadServerListGenNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CtsvDownloadServerListGenNum_Type.__name__ = "OctetString"
_CtsvDownloadServerListGenNum_Object = MibTableColumn
ctsvDownloadServerListGenNum = _CtsvDownloadServerListGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 4, 1, 1, 2),
    _CtsvDownloadServerListGenNum_Type()
)
ctsvDownloadServerListGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerListGenNum.setStatus("current")
_CtsvDownloadServerListServerCount_Type = Unsigned32
_CtsvDownloadServerListServerCount_Object = MibTableColumn
ctsvDownloadServerListServerCount = _CtsvDownloadServerListServerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 4, 1, 1, 3),
    _CtsvDownloadServerListServerCount_Type()
)
ctsvDownloadServerListServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerListServerCount.setStatus("current")
_CtsvDownloadServerObjects_ObjectIdentity = ObjectIdentity
ctsvDownloadServerObjects = _CtsvDownloadServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5)
)
_CtsvDownloadServerTable_Object = MibTable
ctsvDownloadServerTable = _CtsvDownloadServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ctsvDownloadServerTable.setStatus("current")
_CtsvDownloadServerEntry_Object = MibTableRow
ctsvDownloadServerEntry = _CtsvDownloadServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1)
)
ctsvDownloadServerEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerListName"),
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerAddrType"),
    (0, "CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerAddr"),
)
if mibBuilder.loadTexts:
    ctsvDownloadServerEntry.setStatus("current")
_CtsvDownloadServerAddrType_Type = InetAddressType
_CtsvDownloadServerAddrType_Object = MibTableColumn
ctsvDownloadServerAddrType = _CtsvDownloadServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 1),
    _CtsvDownloadServerAddrType_Type()
)
ctsvDownloadServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvDownloadServerAddrType.setStatus("current")


class _CtsvDownloadServerAddr_Type(InetAddress):
    """Custom type ctsvDownloadServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsvDownloadServerAddr_Type.__name__ = "InetAddress"
_CtsvDownloadServerAddr_Object = MibTableColumn
ctsvDownloadServerAddr = _CtsvDownloadServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 2),
    _CtsvDownloadServerAddr_Type()
)
ctsvDownloadServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsvDownloadServerAddr.setStatus("current")
_CtsvDownloadServerPort_Type = InetPortNumber
_CtsvDownloadServerPort_Object = MibTableColumn
ctsvDownloadServerPort = _CtsvDownloadServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 3),
    _CtsvDownloadServerPort_Type()
)
ctsvDownloadServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerPort.setStatus("current")
_CtsvDownloadServerProvisioned_Type = TruthValue
_CtsvDownloadServerProvisioned_Object = MibTableColumn
ctsvDownloadServerProvisioned = _CtsvDownloadServerProvisioned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 4),
    _CtsvDownloadServerProvisioned_Type()
)
ctsvDownloadServerProvisioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerProvisioned.setStatus("current")
_CtsvDownloadServerAuthorityId_Type = CtsAcsAuthorityIdentity
_CtsvDownloadServerAuthorityId_Object = MibTableColumn
ctsvDownloadServerAuthorityId = _CtsvDownloadServerAuthorityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 5),
    _CtsvDownloadServerAuthorityId_Type()
)
ctsvDownloadServerAuthorityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerAuthorityId.setStatus("current")


class _CtsvDownloadServerStatus_Type(Integer32):
    """Custom type ctsvDownloadServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_CtsvDownloadServerStatus_Type.__name__ = "Integer32"
_CtsvDownloadServerStatus_Object = MibTableColumn
ctsvDownloadServerStatus = _CtsvDownloadServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 6),
    _CtsvDownloadServerStatus_Type()
)
ctsvDownloadServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerStatus.setStatus("current")
_CtsvDownloadServerTestEnabled_Type = TruthValue
_CtsvDownloadServerTestEnabled_Object = MibTableColumn
ctsvDownloadServerTestEnabled = _CtsvDownloadServerTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 7),
    _CtsvDownloadServerTestEnabled_Type()
)
ctsvDownloadServerTestEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerTestEnabled.setStatus("current")
_CtsvDownloadServerTestInterval_Type = Unsigned32
_CtsvDownloadServerTestInterval_Object = MibTableColumn
ctsvDownloadServerTestInterval = _CtsvDownloadServerTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 8),
    _CtsvDownloadServerTestInterval_Type()
)
ctsvDownloadServerTestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsvDownloadServerTestInterval.setUnits("minutes")
_CtsvDownloadServerTestDeadTime_Type = Unsigned32
_CtsvDownloadServerTestDeadTime_Object = MibTableColumn
ctsvDownloadServerTestDeadTime = _CtsvDownloadServerTestDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 9),
    _CtsvDownloadServerTestDeadTime_Type()
)
ctsvDownloadServerTestDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerTestDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    ctsvDownloadServerTestDeadTime.setUnits("seconds")
_CtsvDownloadServerKeyWrapEnabled_Type = TruthValue
_CtsvDownloadServerKeyWrapEnabled_Object = MibTableColumn
ctsvDownloadServerKeyWrapEnabled = _CtsvDownloadServerKeyWrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 5, 1, 1, 10),
    _CtsvDownloadServerKeyWrapEnabled_Type()
)
ctsvDownloadServerKeyWrapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsvDownloadServerKeyWrapEnabled.setStatus("current")
_CtsvNotificationControlObjects_ObjectIdentity = ObjectIdentity
ctsvNotificationControlObjects = _CtsvNotificationControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 6)
)
_CtsvNoRadiusServerNotifEnable_Type = TruthValue
_CtsvNoRadiusServerNotifEnable_Object = MibScalar
ctsvNoRadiusServerNotifEnable = _CtsvNoRadiusServerNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 6, 1),
    _CtsvNoRadiusServerNotifEnable_Type()
)
ctsvNoRadiusServerNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvNoRadiusServerNotifEnable.setStatus("current")
_CtsvNoProvisionSecretNotifEnable_Type = TruthValue
_CtsvNoProvisionSecretNotifEnable_Object = MibScalar
ctsvNoProvisionSecretNotifEnable = _CtsvNoProvisionSecretNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 6, 2),
    _CtsvNoProvisionSecretNotifEnable_Type()
)
ctsvNoProvisionSecretNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsvNoProvisionSecretNotifEnable.setStatus("current")
_CtsvNotificationOnlyInfoObjects_ObjectIdentity = ObjectIdentity
ctsvNotificationOnlyInfoObjects = _CtsvNotificationOnlyInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 7)
)
_CtsvServerNotifMsg_Type = SnmpAdminString
_CtsvServerNotifMsg_Object = MibScalar
ctsvServerNotifMsg = _CtsvServerNotifMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 7, 1),
    _CtsvServerNotifMsg_Type()
)
ctsvServerNotifMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsvServerNotifMsg.setStatus("current")
_CtsvServerNoProvisionSecretAddrType_Type = InetAddressType
_CtsvServerNoProvisionSecretAddrType_Object = MibScalar
ctsvServerNoProvisionSecretAddrType = _CtsvServerNoProvisionSecretAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 7, 2),
    _CtsvServerNoProvisionSecretAddrType_Type()
)
ctsvServerNoProvisionSecretAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsvServerNoProvisionSecretAddrType.setStatus("current")
_CtsvServerNoProvisionSecretAddr_Type = InetAddress
_CtsvServerNoProvisionSecretAddr_Object = MibScalar
ctsvServerNoProvisionSecretAddr = _CtsvServerNoProvisionSecretAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 1, 7, 3),
    _CtsvServerNoProvisionSecretAddr_Type()
)
ctsvServerNoProvisionSecretAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsvServerNoProvisionSecretAddr.setStatus("current")
_CiscoTrustSecServerMIBConform_ObjectIdentity = ObjectIdentity
ciscoTrustSecServerMIBConform = _CiscoTrustSecServerMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2)
)
_CiscoTrustSecServerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTrustSecServerMIBCompliances = _CiscoTrustSecServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 1)
)
_CiscoTrustSecServerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTrustSecServerMIBGroups = _CiscoTrustSecServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2)
)

# Managed Objects groups

ciscoTrustSecMIBServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 1)
)
ciscoTrustSecMIBServerConfigGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvAuthorizationList"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerDeadTime"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerLoadBalanceMethod"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerLoadBalanceBatchSize"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvUseSameProvisionedServer"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBServerConfigGroup.setStatus("current")

ciscoTrustSecMIBGlobalServerTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 2)
)
ciscoTrustSecMIBGlobalServerTestGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvAllServerTestEnabled"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvAllServerTestDeadTime"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvAllServerTestInterval"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBGlobalServerTestGroup.setStatus("current")

ciscoTrustSecMIBServerTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 3)
)
ciscoTrustSecMIBServerTestGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestEnabled"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestDeadTime"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestInterval"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestStorageType"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerTestRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBServerTestGroup.setStatus("current")

ciscoTrustSecMIBProvisionedServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 4)
)
ciscoTrustSecMIBProvisionedServerGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerPort"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerAuthorityId"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerStatus"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerTestEnabled"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerTestInterval"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerTestDeadTime"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBProvisionedServerGroup.setStatus("current")

ciscoTrustSecMIBDownloadServerListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 5)
)
ciscoTrustSecMIBDownloadServerListGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerListGenNum"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerListServerCount"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBDownloadServerListGroup.setStatus("current")

ciscoTrustSecMIBDownloadServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 6)
)
ciscoTrustSecMIBDownloadServerGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerPort"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerProvisioned"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerAuthorityId"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerStatus"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerTestEnabled"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerTestInterval"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerTestDeadTime"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBDownloadServerGroup.setStatus("current")

ciscoTrustSecServerMIBKeyWrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 7)
)
ciscoTrustSecServerMIBKeyWrapGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerKeyWrapEnabled"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvProvisionedServerKeyWrapEnabled"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvDownloadServerKeyWrapEnabled"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecServerMIBKeyWrapGroup.setStatus("current")

ciscoTrustSecServerMIBNotifsCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 8)
)
ciscoTrustSecServerMIBNotifsCtrlGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvNoRadiusServerNotifEnable"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvNoProvisionSecretNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecServerMIBNotifsCtrlGroup.setStatus("current")

ciscoTrustSecServerMIBNotifsOnlyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 9)
)
ciscoTrustSecServerMIBNotifsOnlyInfoGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerNotifMsg"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerNoProvisionSecretAddrType"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerNoProvisionSecretAddr"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecServerMIBNotifsOnlyInfoGroup.setStatus("current")


# Notification objects

ctsvNoRadiusServerNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 0, 1)
)
ctsvNoRadiusServerNotif.setObjects(
    ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerNotifMsg")
)
if mibBuilder.loadTexts:
    ctsvNoRadiusServerNotif.setStatus(
        "current"
    )

ctsvNoProvisionSecretNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 0, 2)
)
ctsvNoProvisionSecretNotif.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerNoProvisionSecretAddrType"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvServerNoProvisionSecretAddr"))
)
if mibBuilder.loadTexts:
    ctsvNoProvisionSecretNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoTrustSecServerMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 2, 10)
)
ciscoTrustSecServerMIBNotifsGroup.setObjects(
      *(("CISCO-TRUSTSEC-SERVER-MIB", "ctsvNoRadiusServerNotif"),
        ("CISCO-TRUSTSEC-SERVER-MIB", "ctsvNoProvisionSecretNotif"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecServerMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTrustSecServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTrustSecServerMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTrustSecServerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 741, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTrustSecServerMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TRUSTSEC-SERVER-MIB",
    **{"ciscoTrustSecServerMIB": ciscoTrustSecServerMIB,
       "ciscoTrustSecServerMIBNotifs": ciscoTrustSecServerMIBNotifs,
       "ctsvNoRadiusServerNotif": ctsvNoRadiusServerNotif,
       "ctsvNoProvisionSecretNotif": ctsvNoProvisionSecretNotif,
       "ciscoTrustSecServerMIBObjects": ciscoTrustSecServerMIBObjects,
       "ctsvGlobalServerConfigObjects": ctsvGlobalServerConfigObjects,
       "ctsvAuthorizationList": ctsvAuthorizationList,
       "ctsvServerDeadTime": ctsvServerDeadTime,
       "ctsvServerLoadBalanceMethod": ctsvServerLoadBalanceMethod,
       "ctsvServerLoadBalanceBatchSize": ctsvServerLoadBalanceBatchSize,
       "ctsvUseSameProvisionedServer": ctsvUseSameProvisionedServer,
       "ctsvAllServerTestEnabled": ctsvAllServerTestEnabled,
       "ctsvAllServerTestDeadTime": ctsvAllServerTestDeadTime,
       "ctsvAllServerTestInterval": ctsvAllServerTestInterval,
       "ctsvServerKeyWrapEnabled": ctsvServerKeyWrapEnabled,
       "ctsvServerTestConfigObjects": ctsvServerTestConfigObjects,
       "ctsvServerTestConfigTable": ctsvServerTestConfigTable,
       "ctsvServerTestConfigEntry": ctsvServerTestConfigEntry,
       "ctsvServerTestAddrType": ctsvServerTestAddrType,
       "ctsvServerTestAddr": ctsvServerTestAddr,
       "ctsvServerTestEnabled": ctsvServerTestEnabled,
       "ctsvServerTestDeadTime": ctsvServerTestDeadTime,
       "ctsvServerTestInterval": ctsvServerTestInterval,
       "ctsvServerTestStorageType": ctsvServerTestStorageType,
       "ctsvServerTestRowStatus": ctsvServerTestRowStatus,
       "ctsvProvisionedServerObjects": ctsvProvisionedServerObjects,
       "ctsvProvisionedServerTable": ctsvProvisionedServerTable,
       "ctsvProvisionedServerEntry": ctsvProvisionedServerEntry,
       "ctsvProvisionedServerAddrType": ctsvProvisionedServerAddrType,
       "ctsvProvisionedServerAddr": ctsvProvisionedServerAddr,
       "ctsvProvisionedServerPort": ctsvProvisionedServerPort,
       "ctsvProvisionedServerAuthorityId": ctsvProvisionedServerAuthorityId,
       "ctsvProvisionedServerStatus": ctsvProvisionedServerStatus,
       "ctsvProvisionedServerTestEnabled": ctsvProvisionedServerTestEnabled,
       "ctsvProvisionedServerTestInterval": ctsvProvisionedServerTestInterval,
       "ctsvProvisionedServerTestDeadTime": ctsvProvisionedServerTestDeadTime,
       "ctsvProvisionedServerKeyWrapEnabled": ctsvProvisionedServerKeyWrapEnabled,
       "ctsvDownloadServerListObjects": ctsvDownloadServerListObjects,
       "ctsvDownloadServerListTable": ctsvDownloadServerListTable,
       "ctsvDownloadServerListEntry": ctsvDownloadServerListEntry,
       "ctsvDownloadServerListName": ctsvDownloadServerListName,
       "ctsvDownloadServerListGenNum": ctsvDownloadServerListGenNum,
       "ctsvDownloadServerListServerCount": ctsvDownloadServerListServerCount,
       "ctsvDownloadServerObjects": ctsvDownloadServerObjects,
       "ctsvDownloadServerTable": ctsvDownloadServerTable,
       "ctsvDownloadServerEntry": ctsvDownloadServerEntry,
       "ctsvDownloadServerAddrType": ctsvDownloadServerAddrType,
       "ctsvDownloadServerAddr": ctsvDownloadServerAddr,
       "ctsvDownloadServerPort": ctsvDownloadServerPort,
       "ctsvDownloadServerProvisioned": ctsvDownloadServerProvisioned,
       "ctsvDownloadServerAuthorityId": ctsvDownloadServerAuthorityId,
       "ctsvDownloadServerStatus": ctsvDownloadServerStatus,
       "ctsvDownloadServerTestEnabled": ctsvDownloadServerTestEnabled,
       "ctsvDownloadServerTestInterval": ctsvDownloadServerTestInterval,
       "ctsvDownloadServerTestDeadTime": ctsvDownloadServerTestDeadTime,
       "ctsvDownloadServerKeyWrapEnabled": ctsvDownloadServerKeyWrapEnabled,
       "ctsvNotificationControlObjects": ctsvNotificationControlObjects,
       "ctsvNoRadiusServerNotifEnable": ctsvNoRadiusServerNotifEnable,
       "ctsvNoProvisionSecretNotifEnable": ctsvNoProvisionSecretNotifEnable,
       "ctsvNotificationOnlyInfoObjects": ctsvNotificationOnlyInfoObjects,
       "ctsvServerNotifMsg": ctsvServerNotifMsg,
       "ctsvServerNoProvisionSecretAddrType": ctsvServerNoProvisionSecretAddrType,
       "ctsvServerNoProvisionSecretAddr": ctsvServerNoProvisionSecretAddr,
       "ciscoTrustSecServerMIBConform": ciscoTrustSecServerMIBConform,
       "ciscoTrustSecServerMIBCompliances": ciscoTrustSecServerMIBCompliances,
       "ciscoTrustSecServerMIBCompliance": ciscoTrustSecServerMIBCompliance,
       "ciscoTrustSecServerMIBCompliance2": ciscoTrustSecServerMIBCompliance2,
       "ciscoTrustSecServerMIBGroups": ciscoTrustSecServerMIBGroups,
       "ciscoTrustSecMIBServerConfigGroup": ciscoTrustSecMIBServerConfigGroup,
       "ciscoTrustSecMIBGlobalServerTestGroup": ciscoTrustSecMIBGlobalServerTestGroup,
       "ciscoTrustSecMIBServerTestGroup": ciscoTrustSecMIBServerTestGroup,
       "ciscoTrustSecMIBProvisionedServerGroup": ciscoTrustSecMIBProvisionedServerGroup,
       "ciscoTrustSecMIBDownloadServerListGroup": ciscoTrustSecMIBDownloadServerListGroup,
       "ciscoTrustSecMIBDownloadServerGroup": ciscoTrustSecMIBDownloadServerGroup,
       "ciscoTrustSecServerMIBKeyWrapGroup": ciscoTrustSecServerMIBKeyWrapGroup,
       "ciscoTrustSecServerMIBNotifsCtrlGroup": ciscoTrustSecServerMIBNotifsCtrlGroup,
       "ciscoTrustSecServerMIBNotifsOnlyInfoGroup": ciscoTrustSecServerMIBNotifsOnlyInfoGroup,
       "ciscoTrustSecServerMIBNotifsGroup": ciscoTrustSecServerMIBNotifsGroup}
)
