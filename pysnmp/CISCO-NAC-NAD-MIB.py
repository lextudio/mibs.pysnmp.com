# SNMP MIB module (CISCO-NAC-NAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NAC-NAD-MIB
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

(CnnEouAuthType,
 CnnEouDeviceType,
 CnnEouPostureToken,
 CnnEouPostureTokenString,
 CnnEouState) = mibBuilder.importSymbols(
    "CISCO-NAC-TC-MIB",
    "CnnEouAuthType",
    "CnnEouDeviceType",
    "CnnEouPostureToken",
    "CnnEouPostureTokenString",
    "CnnEouState")

(CpgPolicyNameOrEmpty,) = mibBuilder.importSymbols(
    "CISCO-POLICY-GROUP-MIB",
    "CpgPolicyNameOrEmpty")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoNacNadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484)
)
ciscoNacNadMIB.setRevisions(
        ("2008-06-23 00:00",
         "2007-11-12 00:00",
         "2007-02-23 00:00",
         "2005-06-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNacNadMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNacNadMIBNotifs = _CiscoNacNadMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 0)
)
_CiscoNacNadMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNacNadMIBObjects = _CiscoNacNadMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1)
)
_CnnEouGlobalObjects_ObjectIdentity = ObjectIdentity
cnnEouGlobalObjects = _CnnEouGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1)
)
_CnnEouVersion_Type = Unsigned32
_CnnEouVersion_Object = MibScalar
cnnEouVersion = _CnnEouVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 1),
    _CnnEouVersion_Type()
)
cnnEouVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouVersion.setStatus("current")
_CnnEouEnabled_Type = TruthValue
_CnnEouEnabled_Object = MibScalar
cnnEouEnabled = _CnnEouEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 2),
    _CnnEouEnabled_Type()
)
cnnEouEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouEnabled.setStatus("current")
_CnnEouAllowClientless_Type = TruthValue
_CnnEouAllowClientless_Object = MibScalar
cnnEouAllowClientless = _CnnEouAllowClientless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 3),
    _CnnEouAllowClientless_Type()
)
cnnEouAllowClientless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouAllowClientless.setStatus("current")
_CnnEouAllowIpStationId_Type = TruthValue
_CnnEouAllowIpStationId_Object = MibScalar
cnnEouAllowIpStationId = _CnnEouAllowIpStationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 4),
    _CnnEouAllowIpStationId_Type()
)
cnnEouAllowIpStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouAllowIpStationId.setStatus("current")
_CnnEouLoggingEnabled_Type = TruthValue
_CnnEouLoggingEnabled_Object = MibScalar
cnnEouLoggingEnabled = _CnnEouLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 5),
    _CnnEouLoggingEnabled_Type()
)
cnnEouLoggingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouLoggingEnabled.setStatus("current")
_CnnEouMaxRetry_Type = Integer32
_CnnEouMaxRetry_Object = MibScalar
cnnEouMaxRetry = _CnnEouMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 6),
    _CnnEouMaxRetry_Type()
)
cnnEouMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouMaxRetry.setStatus("current")
_CnnEouPort_Type = InetPortNumber
_CnnEouPort_Object = MibScalar
cnnEouPort = _CnnEouPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 7),
    _CnnEouPort_Type()
)
cnnEouPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouPort.setStatus("current")
_CnnEouRateLimit_Type = Unsigned32
_CnnEouRateLimit_Object = MibScalar
cnnEouRateLimit = _CnnEouRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 8),
    _CnnEouRateLimit_Type()
)
cnnEouRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouRateLimit.setStatus("current")
_CnnEouTimeoutAAA_Type = Unsigned32
_CnnEouTimeoutAAA_Object = MibScalar
cnnEouTimeoutAAA = _CnnEouTimeoutAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 9),
    _CnnEouTimeoutAAA_Type()
)
cnnEouTimeoutAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouTimeoutAAA.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouTimeoutAAA.setUnits("seconds")
_CnnEouTimeoutHoldPeriod_Type = Unsigned32
_CnnEouTimeoutHoldPeriod_Object = MibScalar
cnnEouTimeoutHoldPeriod = _CnnEouTimeoutHoldPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 10),
    _CnnEouTimeoutHoldPeriod_Type()
)
cnnEouTimeoutHoldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouTimeoutHoldPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouTimeoutHoldPeriod.setUnits("seconds")
_CnnEouTimeoutRetransmit_Type = Unsigned32
_CnnEouTimeoutRetransmit_Object = MibScalar
cnnEouTimeoutRetransmit = _CnnEouTimeoutRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 11),
    _CnnEouTimeoutRetransmit_Type()
)
cnnEouTimeoutRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouTimeoutRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouTimeoutRetransmit.setUnits("seconds")
_CnnEouTimeoutRevalidation_Type = Unsigned32
_CnnEouTimeoutRevalidation_Object = MibScalar
cnnEouTimeoutRevalidation = _CnnEouTimeoutRevalidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 12),
    _CnnEouTimeoutRevalidation_Type()
)
cnnEouTimeoutRevalidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouTimeoutRevalidation.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouTimeoutRevalidation.setUnits("seconds")
_CnnEouTimeoutStatusQuery_Type = Unsigned32
_CnnEouTimeoutStatusQuery_Object = MibScalar
cnnEouTimeoutStatusQuery = _CnnEouTimeoutStatusQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 13),
    _CnnEouTimeoutStatusQuery_Type()
)
cnnEouTimeoutStatusQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouTimeoutStatusQuery.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouTimeoutStatusQuery.setUnits("seconds")
_CnnEouCriticalRecoveryDelay_Type = Unsigned32
_CnnEouCriticalRecoveryDelay_Object = MibScalar
cnnEouCriticalRecoveryDelay = _CnnEouCriticalRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 14),
    _CnnEouCriticalRecoveryDelay_Type()
)
cnnEouCriticalRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouCriticalRecoveryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouCriticalRecoveryDelay.setUnits("milliseconds")
_CnnEouRevalidationEnabled_Type = TruthValue
_CnnEouRevalidationEnabled_Object = MibScalar
cnnEouRevalidationEnabled = _CnnEouRevalidationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 1, 15),
    _CnnEouRevalidationEnabled_Type()
)
cnnEouRevalidationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouRevalidationEnabled.setStatus("current")
_CnnEouAuthorizeLists_ObjectIdentity = ObjectIdentity
cnnEouAuthorizeLists = _CnnEouAuthorizeLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2)
)
_CnnEouAuthIpTable_Object = MibTable
cnnEouAuthIpTable = _CnnEouAuthIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cnnEouAuthIpTable.setStatus("current")
_CnnEouAuthIpEntry_Object = MibTableRow
cnnEouAuthIpEntry = _CnnEouAuthIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1)
)
cnnEouAuthIpEntry.setIndexNames(
    (0, "CISCO-NAC-NAD-MIB", "cnnEouAuthIpAddrType"),
    (0, "CISCO-NAC-NAD-MIB", "cnnEouAuthIpAddr"),
)
if mibBuilder.loadTexts:
    cnnEouAuthIpEntry.setStatus("current")
_CnnEouAuthIpAddrType_Type = InetAddressType
_CnnEouAuthIpAddrType_Object = MibTableColumn
cnnEouAuthIpAddrType = _CnnEouAuthIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1, 1),
    _CnnEouAuthIpAddrType_Type()
)
cnnEouAuthIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnnEouAuthIpAddrType.setStatus("current")


class _CnnEouAuthIpAddr_Type(InetAddress):
    """Custom type cnnEouAuthIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CnnEouAuthIpAddr_Type.__name__ = "InetAddress"
_CnnEouAuthIpAddr_Object = MibTableColumn
cnnEouAuthIpAddr = _CnnEouAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1, 2),
    _CnnEouAuthIpAddr_Type()
)
cnnEouAuthIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnnEouAuthIpAddr.setStatus("current")
_CnnEouAuthIpAddrMask_Type = InetAddressPrefixLength
_CnnEouAuthIpAddrMask_Object = MibTableColumn
cnnEouAuthIpAddrMask = _CnnEouAuthIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1, 3),
    _CnnEouAuthIpAddrMask_Type()
)
cnnEouAuthIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthIpAddrMask.setStatus("current")
_CnnEouAuthIpPolicy_Type = SnmpAdminString
_CnnEouAuthIpPolicy_Object = MibTableColumn
cnnEouAuthIpPolicy = _CnnEouAuthIpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1, 4),
    _CnnEouAuthIpPolicy_Type()
)
cnnEouAuthIpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthIpPolicy.setStatus("current")


class _CnnEouAuthIpStorageType_Type(StorageType):
    """Custom type cnnEouAuthIpStorageType based on StorageType"""


_CnnEouAuthIpStorageType_Object = MibTableColumn
cnnEouAuthIpStorageType = _CnnEouAuthIpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1, 5),
    _CnnEouAuthIpStorageType_Type()
)
cnnEouAuthIpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthIpStorageType.setStatus("current")
_CnnEouAuthIpRowStatus_Type = RowStatus
_CnnEouAuthIpRowStatus_Object = MibTableColumn
cnnEouAuthIpRowStatus = _CnnEouAuthIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 1, 1, 6),
    _CnnEouAuthIpRowStatus_Type()
)
cnnEouAuthIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthIpRowStatus.setStatus("current")
_CnnEouAuthMacTable_Object = MibTable
cnnEouAuthMacTable = _CnnEouAuthMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cnnEouAuthMacTable.setStatus("current")
_CnnEouAuthMacEntry_Object = MibTableRow
cnnEouAuthMacEntry = _CnnEouAuthMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2, 1)
)
cnnEouAuthMacEntry.setIndexNames(
    (0, "CISCO-NAC-NAD-MIB", "cnnEouAuthMacAddr"),
)
if mibBuilder.loadTexts:
    cnnEouAuthMacEntry.setStatus("current")
_CnnEouAuthMacAddr_Type = MacAddress
_CnnEouAuthMacAddr_Object = MibTableColumn
cnnEouAuthMacAddr = _CnnEouAuthMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2, 1, 1),
    _CnnEouAuthMacAddr_Type()
)
cnnEouAuthMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnnEouAuthMacAddr.setStatus("current")
_CnnEouAuthMacAddrMask_Type = MacAddress
_CnnEouAuthMacAddrMask_Object = MibTableColumn
cnnEouAuthMacAddrMask = _CnnEouAuthMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2, 1, 2),
    _CnnEouAuthMacAddrMask_Type()
)
cnnEouAuthMacAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthMacAddrMask.setStatus("current")
_CnnEouAuthMacPolicy_Type = SnmpAdminString
_CnnEouAuthMacPolicy_Object = MibTableColumn
cnnEouAuthMacPolicy = _CnnEouAuthMacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2, 1, 3),
    _CnnEouAuthMacPolicy_Type()
)
cnnEouAuthMacPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthMacPolicy.setStatus("current")


class _CnnEouAuthMacStorageType_Type(StorageType):
    """Custom type cnnEouAuthMacStorageType based on StorageType"""


_CnnEouAuthMacStorageType_Object = MibTableColumn
cnnEouAuthMacStorageType = _CnnEouAuthMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2, 1, 4),
    _CnnEouAuthMacStorageType_Type()
)
cnnEouAuthMacStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthMacStorageType.setStatus("current")
_CnnEouAuthMacRowStatus_Type = RowStatus
_CnnEouAuthMacRowStatus_Object = MibTableColumn
cnnEouAuthMacRowStatus = _CnnEouAuthMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 2, 1, 5),
    _CnnEouAuthMacRowStatus_Type()
)
cnnEouAuthMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthMacRowStatus.setStatus("current")
_CnnEouAuthDeviceTypeTable_Object = MibTable
cnnEouAuthDeviceTypeTable = _CnnEouAuthDeviceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cnnEouAuthDeviceTypeTable.setStatus("current")
_CnnEouAuthDeviceTypeEntry_Object = MibTableRow
cnnEouAuthDeviceTypeEntry = _CnnEouAuthDeviceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 3, 1)
)
cnnEouAuthDeviceTypeEntry.setIndexNames(
    (0, "CISCO-NAC-NAD-MIB", "cnnEouAuthDeviceType"),
)
if mibBuilder.loadTexts:
    cnnEouAuthDeviceTypeEntry.setStatus("current")
_CnnEouAuthDeviceType_Type = CnnEouDeviceType
_CnnEouAuthDeviceType_Object = MibTableColumn
cnnEouAuthDeviceType = _CnnEouAuthDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 3, 1, 1),
    _CnnEouAuthDeviceType_Type()
)
cnnEouAuthDeviceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnnEouAuthDeviceType.setStatus("current")


class _CnnEouAuthDeviceTypeStorageType_Type(StorageType):
    """Custom type cnnEouAuthDeviceTypeStorageType based on StorageType"""


_CnnEouAuthDeviceTypeStorageType_Object = MibTableColumn
cnnEouAuthDeviceTypeStorageType = _CnnEouAuthDeviceTypeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 3, 1, 2),
    _CnnEouAuthDeviceTypeStorageType_Type()
)
cnnEouAuthDeviceTypeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthDeviceTypeStorageType.setStatus("current")
_CnnEouAuthDeviceTypeRowStatus_Type = RowStatus
_CnnEouAuthDeviceTypeRowStatus_Object = MibTableColumn
cnnEouAuthDeviceTypeRowStatus = _CnnEouAuthDeviceTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 2, 3, 1, 3),
    _CnnEouAuthDeviceTypeRowStatus_Type()
)
cnnEouAuthDeviceTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouAuthDeviceTypeRowStatus.setStatus("current")
_CnnEouIfMIBObjects_ObjectIdentity = ObjectIdentity
cnnEouIfMIBObjects = _CnnEouIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3)
)
_CnnEouIfConfigTable_Object = MibTable
cnnEouIfConfigTable = _CnnEouIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cnnEouIfConfigTable.setStatus("current")
_CnnEouIfConfigEntry_Object = MibTableRow
cnnEouIfConfigEntry = _CnnEouIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1)
)
cnnEouIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnnEouIfConfigEntry.setStatus("current")


class _CnnEouIfAdminStatus_Type(Integer32):
    """Custom type cnnEouIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("bypass", 3),
          ("disabled", 2))
    )


_CnnEouIfAdminStatus_Type.__name__ = "Integer32"
_CnnEouIfAdminStatus_Object = MibTableColumn
cnnEouIfAdminStatus = _CnnEouIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 1),
    _CnnEouIfAdminStatus_Type()
)
cnnEouIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfAdminStatus.setStatus("current")
_CnnEouIfMaxRetry_Type = Integer32
_CnnEouIfMaxRetry_Object = MibTableColumn
cnnEouIfMaxRetry = _CnnEouIfMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 2),
    _CnnEouIfMaxRetry_Type()
)
cnnEouIfMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfMaxRetry.setStatus("current")


class _CnnEouIfValidateAction_Type(Integer32):
    """Custom type cnnEouIfValidateAction based on Integer32"""
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
        *(("initialize", 2),
          ("noRevalidate", 4),
          ("none", 1),
          ("revalidate", 3))
    )


_CnnEouIfValidateAction_Type.__name__ = "Integer32"
_CnnEouIfValidateAction_Object = MibTableColumn
cnnEouIfValidateAction = _CnnEouIfValidateAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 3),
    _CnnEouIfValidateAction_Type()
)
cnnEouIfValidateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfValidateAction.setStatus("current")


class _CnnEouIfTimeoutGlobalConfig_Type(Bits):
    """Custom type cnnEouIfTimeoutGlobalConfig based on Bits"""
    namedValues = NamedValues(
        *(("aaa", 0),
          ("clientless", 6),
          ("holdPeriod", 1),
          ("ipStationId", 7),
          ("maxRetry", 5),
          ("retransmit", 2),
          ("revalidation", 3),
          ("statusQuery", 4))
    )

_CnnEouIfTimeoutGlobalConfig_Type.__name__ = "Bits"
_CnnEouIfTimeoutGlobalConfig_Object = MibTableColumn
cnnEouIfTimeoutGlobalConfig = _CnnEouIfTimeoutGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 4),
    _CnnEouIfTimeoutGlobalConfig_Type()
)
cnnEouIfTimeoutGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutGlobalConfig.setStatus("current")
_CnnEouIfTimeoutAAA_Type = Unsigned32
_CnnEouIfTimeoutAAA_Object = MibTableColumn
cnnEouIfTimeoutAAA = _CnnEouIfTimeoutAAA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 5),
    _CnnEouIfTimeoutAAA_Type()
)
cnnEouIfTimeoutAAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutAAA.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutAAA.setUnits("seconds")
_CnnEouIfTimeoutHoldPeriod_Type = Unsigned32
_CnnEouIfTimeoutHoldPeriod_Object = MibTableColumn
cnnEouIfTimeoutHoldPeriod = _CnnEouIfTimeoutHoldPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 6),
    _CnnEouIfTimeoutHoldPeriod_Type()
)
cnnEouIfTimeoutHoldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutHoldPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutHoldPeriod.setUnits("seconds")
_CnnEouIfTimeoutRetransmit_Type = Unsigned32
_CnnEouIfTimeoutRetransmit_Object = MibTableColumn
cnnEouIfTimeoutRetransmit = _CnnEouIfTimeoutRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 7),
    _CnnEouIfTimeoutRetransmit_Type()
)
cnnEouIfTimeoutRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutRetransmit.setUnits("seconds")
_CnnEouIfTimeoutRevalidation_Type = Unsigned32
_CnnEouIfTimeoutRevalidation_Object = MibTableColumn
cnnEouIfTimeoutRevalidation = _CnnEouIfTimeoutRevalidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 8),
    _CnnEouIfTimeoutRevalidation_Type()
)
cnnEouIfTimeoutRevalidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutRevalidation.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutRevalidation.setUnits("seconds")
_CnnEouIfTimeoutStatusQuery_Type = Unsigned32
_CnnEouIfTimeoutStatusQuery_Object = MibTableColumn
cnnEouIfTimeoutStatusQuery = _CnnEouIfTimeoutStatusQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 9),
    _CnnEouIfTimeoutStatusQuery_Type()
)
cnnEouIfTimeoutStatusQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutStatusQuery.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouIfTimeoutStatusQuery.setUnits("seconds")
_CnnEouIfAaaFailPolicy_Type = CpgPolicyNameOrEmpty
_CnnEouIfAaaFailPolicy_Object = MibTableColumn
cnnEouIfAaaFailPolicy = _CnnEouIfAaaFailPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 10),
    _CnnEouIfAaaFailPolicy_Type()
)
cnnEouIfAaaFailPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfAaaFailPolicy.setStatus("current")
_CnnEouIfAllowClientless_Type = TruthValue
_CnnEouIfAllowClientless_Object = MibTableColumn
cnnEouIfAllowClientless = _CnnEouIfAllowClientless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 11),
    _CnnEouIfAllowClientless_Type()
)
cnnEouIfAllowClientless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfAllowClientless.setStatus("current")
_CnnEouIfAllowIpStationId_Type = TruthValue
_CnnEouIfAllowIpStationId_Object = MibTableColumn
cnnEouIfAllowIpStationId = _CnnEouIfAllowIpStationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 3, 1, 1, 12),
    _CnnEouIfAllowIpStationId_Type()
)
cnnEouIfAllowIpStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfAllowIpStationId.setStatus("current")
_CnnEouHostMIBObjects_ObjectIdentity = ObjectIdentity
cnnEouHostMIBObjects = _CnnEouHostMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4)
)


class _CnnEouHostValidateAction_Type(Integer32):
    """Custom type cnnEouHostValidateAction based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("initializeAll", 2),
          ("initializeAuthClientless", 3),
          ("initializeAuthEap", 4),
          ("initializeAuthStatic", 5),
          ("initializeIp", 6),
          ("initializeMac", 7),
          ("initializePostureToken", 8),
          ("initializePostureTokenStr", 23),
          ("noRevalidateAll", 16),
          ("noRevalidateAuthClientless", 17),
          ("noRevalidateAuthEap", 18),
          ("noRevalidateAuthStatic", 19),
          ("noRevalidateIp", 20),
          ("noRevalidateMac", 21),
          ("noRevalidatePostureToken", 22),
          ("noRevalidatePostureTokenStr", 25),
          ("none", 1),
          ("revalidateAll", 9),
          ("revalidateAuthClientless", 10),
          ("revalidateAuthEap", 11),
          ("revalidateAuthStatic", 12),
          ("revalidateIp", 13),
          ("revalidateMac", 14),
          ("revalidatePostureToken", 15),
          ("revalidatePostureTokenStr", 24))
    )


_CnnEouHostValidateAction_Type.__name__ = "Integer32"
_CnnEouHostValidateAction_Object = MibScalar
cnnEouHostValidateAction = _CnnEouHostValidateAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 1),
    _CnnEouHostValidateAction_Type()
)
cnnEouHostValidateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouHostValidateAction.setStatus("current")
_CnnEouHostValidateIpAddrType_Type = InetAddressType
_CnnEouHostValidateIpAddrType_Object = MibScalar
cnnEouHostValidateIpAddrType = _CnnEouHostValidateIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 2),
    _CnnEouHostValidateIpAddrType_Type()
)
cnnEouHostValidateIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouHostValidateIpAddrType.setStatus("current")
_CnnEouHostValidateIpAddr_Type = InetAddress
_CnnEouHostValidateIpAddr_Object = MibScalar
cnnEouHostValidateIpAddr = _CnnEouHostValidateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 3),
    _CnnEouHostValidateIpAddr_Type()
)
cnnEouHostValidateIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouHostValidateIpAddr.setStatus("current")
_CnnEouHostValidateMacAddr_Type = MacAddress
_CnnEouHostValidateMacAddr_Object = MibScalar
cnnEouHostValidateMacAddr = _CnnEouHostValidateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 4),
    _CnnEouHostValidateMacAddr_Type()
)
cnnEouHostValidateMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouHostValidateMacAddr.setStatus("current")
_CnnEouHostValidatePostureToken_Type = CnnEouPostureToken
_CnnEouHostValidatePostureToken_Object = MibScalar
cnnEouHostValidatePostureToken = _CnnEouHostValidatePostureToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 5),
    _CnnEouHostValidatePostureToken_Type()
)
cnnEouHostValidatePostureToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouHostValidatePostureToken.setStatus("deprecated")
_CnnEouHostMaxQueries_Type = Unsigned32
_CnnEouHostMaxQueries_Object = MibScalar
cnnEouHostMaxQueries = _CnnEouHostMaxQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 6),
    _CnnEouHostMaxQueries_Type()
)
cnnEouHostMaxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostMaxQueries.setStatus("current")
_CnnEouHostQueryTable_Object = MibTable
cnnEouHostQueryTable = _CnnEouHostQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7)
)
if mibBuilder.loadTexts:
    cnnEouHostQueryTable.setStatus("current")
_CnnEouHostQueryEntry_Object = MibTableRow
cnnEouHostQueryEntry = _CnnEouHostQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1)
)
cnnEouHostQueryEntry.setIndexNames(
    (0, "CISCO-NAC-NAD-MIB", "cnnEouHostQueryIndex"),
)
if mibBuilder.loadTexts:
    cnnEouHostQueryEntry.setStatus("current")
_CnnEouHostQueryIndex_Type = Unsigned32
_CnnEouHostQueryIndex_Object = MibTableColumn
cnnEouHostQueryIndex = _CnnEouHostQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 1),
    _CnnEouHostQueryIndex_Type()
)
cnnEouHostQueryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnnEouHostQueryIndex.setStatus("current")


class _CnnEouHostQueryMask_Type(Integer32):
    """Custom type cnnEouHostQueryMask based on Integer32"""
    defaultValue = 8

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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 8),
          ("authenClientless", 1),
          ("authenEap", 2),
          ("authenStatic", 3),
          ("interface", 4),
          ("ip", 5),
          ("mac", 6),
          ("postureToken", 7),
          ("postureTokenString", 9))
    )


_CnnEouHostQueryMask_Type.__name__ = "Integer32"
_CnnEouHostQueryMask_Object = MibTableColumn
cnnEouHostQueryMask = _CnnEouHostQueryMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 2),
    _CnnEouHostQueryMask_Type()
)
cnnEouHostQueryMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryMask.setStatus("current")


class _CnnEouHostQueryInterface_Type(InterfaceIndexOrZero):
    """Custom type cnnEouHostQueryInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CnnEouHostQueryInterface_Object = MibTableColumn
cnnEouHostQueryInterface = _CnnEouHostQueryInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 3),
    _CnnEouHostQueryInterface_Type()
)
cnnEouHostQueryInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryInterface.setStatus("current")


class _CnnEouHostQueryIpAddrType_Type(InetAddressType):
    """Custom type cnnEouHostQueryIpAddrType based on InetAddressType"""


_CnnEouHostQueryIpAddrType_Object = MibTableColumn
cnnEouHostQueryIpAddrType = _CnnEouHostQueryIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 4),
    _CnnEouHostQueryIpAddrType_Type()
)
cnnEouHostQueryIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryIpAddrType.setStatus("current")


class _CnnEouHostQueryIpAddr_Type(InetAddress):
    """Custom type cnnEouHostQueryIpAddr based on InetAddress"""
    defaultHexValue = "00000000"


_CnnEouHostQueryIpAddr_Object = MibTableColumn
cnnEouHostQueryIpAddr = _CnnEouHostQueryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 5),
    _CnnEouHostQueryIpAddr_Type()
)
cnnEouHostQueryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryIpAddr.setStatus("current")


class _CnnEouHostQueryMacAddr_Type(MacAddress):
    """Custom type cnnEouHostQueryMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CnnEouHostQueryMacAddr_Object = MibTableColumn
cnnEouHostQueryMacAddr = _CnnEouHostQueryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 6),
    _CnnEouHostQueryMacAddr_Type()
)
cnnEouHostQueryMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryMacAddr.setStatus("current")


class _CnnEouHostQueryPostureToken_Type(CnnEouPostureToken):
    """Custom type cnnEouHostQueryPostureToken based on CnnEouPostureToken"""


_CnnEouHostQueryPostureToken_Object = MibTableColumn
cnnEouHostQueryPostureToken = _CnnEouHostQueryPostureToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 7),
    _CnnEouHostQueryPostureToken_Type()
)
cnnEouHostQueryPostureToken.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryPostureToken.setStatus("deprecated")
_CnnEouHostQuerySkipNHosts_Type = Unsigned32
_CnnEouHostQuerySkipNHosts_Object = MibTableColumn
cnnEouHostQuerySkipNHosts = _CnnEouHostQuerySkipNHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 8),
    _CnnEouHostQuerySkipNHosts_Type()
)
cnnEouHostQuerySkipNHosts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQuerySkipNHosts.setStatus("current")
_CnnEouHostQueryMaxResultRows_Type = Unsigned32
_CnnEouHostQueryMaxResultRows_Object = MibTableColumn
cnnEouHostQueryMaxResultRows = _CnnEouHostQueryMaxResultRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 9),
    _CnnEouHostQueryMaxResultRows_Type()
)
cnnEouHostQueryMaxResultRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryMaxResultRows.setStatus("current")


class _CnnEouHostQueryTotalHosts_Type(Integer32):
    """Custom type cnnEouHostQueryTotalHosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CnnEouHostQueryTotalHosts_Type.__name__ = "Integer32"
_CnnEouHostQueryTotalHosts_Object = MibTableColumn
cnnEouHostQueryTotalHosts = _CnnEouHostQueryTotalHosts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 10),
    _CnnEouHostQueryTotalHosts_Type()
)
cnnEouHostQueryTotalHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostQueryTotalHosts.setStatus("current")


class _CnnEouHostQueryRows_Type(Integer32):
    """Custom type cnnEouHostQueryRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CnnEouHostQueryRows_Type.__name__ = "Integer32"
_CnnEouHostQueryRows_Object = MibTableColumn
cnnEouHostQueryRows = _CnnEouHostQueryRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 11),
    _CnnEouHostQueryRows_Type()
)
cnnEouHostQueryRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostQueryRows.setStatus("current")
_CnnEouHostQueryCreateTime_Type = TimeStamp
_CnnEouHostQueryCreateTime_Object = MibTableColumn
cnnEouHostQueryCreateTime = _CnnEouHostQueryCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 12),
    _CnnEouHostQueryCreateTime_Type()
)
cnnEouHostQueryCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostQueryCreateTime.setStatus("current")
_CnnEouHostQueryStatus_Type = RowStatus
_CnnEouHostQueryStatus_Object = MibTableColumn
cnnEouHostQueryStatus = _CnnEouHostQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 13),
    _CnnEouHostQueryStatus_Type()
)
cnnEouHostQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryStatus.setStatus("current")
_CnnEouHostQueryPostureTokenStr_Type = CnnEouPostureTokenString
_CnnEouHostQueryPostureTokenStr_Object = MibTableColumn
cnnEouHostQueryPostureTokenStr = _CnnEouHostQueryPostureTokenStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 7, 1, 14),
    _CnnEouHostQueryPostureTokenStr_Type()
)
cnnEouHostQueryPostureTokenStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnnEouHostQueryPostureTokenStr.setStatus("current")
_CnnEouHostResultTable_Object = MibTable
cnnEouHostResultTable = _CnnEouHostResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8)
)
if mibBuilder.loadTexts:
    cnnEouHostResultTable.setStatus("current")
_CnnEouHostResultEntry_Object = MibTableRow
cnnEouHostResultEntry = _CnnEouHostResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1)
)
cnnEouHostResultEntry.setIndexNames(
    (0, "CISCO-NAC-NAD-MIB", "cnnEouHostQueryIndex"),
    (0, "CISCO-NAC-NAD-MIB", "cnnEouHostResultIndex"),
)
if mibBuilder.loadTexts:
    cnnEouHostResultEntry.setStatus("current")
_CnnEouHostResultIndex_Type = Unsigned32
_CnnEouHostResultIndex_Object = MibTableColumn
cnnEouHostResultIndex = _CnnEouHostResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 1),
    _CnnEouHostResultIndex_Type()
)
cnnEouHostResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnnEouHostResultIndex.setStatus("current")
_CnnEouHostResultAssocIf_Type = InterfaceIndex
_CnnEouHostResultAssocIf_Object = MibTableColumn
cnnEouHostResultAssocIf = _CnnEouHostResultAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 2),
    _CnnEouHostResultAssocIf_Type()
)
cnnEouHostResultAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultAssocIf.setStatus("current")
_CnnEouHostResultIpAddrType_Type = InetAddressType
_CnnEouHostResultIpAddrType_Object = MibTableColumn
cnnEouHostResultIpAddrType = _CnnEouHostResultIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 3),
    _CnnEouHostResultIpAddrType_Type()
)
cnnEouHostResultIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultIpAddrType.setStatus("current")
_CnnEouHostResultIpAddr_Type = InetAddress
_CnnEouHostResultIpAddr_Object = MibTableColumn
cnnEouHostResultIpAddr = _CnnEouHostResultIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 4),
    _CnnEouHostResultIpAddr_Type()
)
cnnEouHostResultIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultIpAddr.setStatus("current")
_CnnEouHostResultMacAddr_Type = MacAddress
_CnnEouHostResultMacAddr_Object = MibTableColumn
cnnEouHostResultMacAddr = _CnnEouHostResultMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 5),
    _CnnEouHostResultMacAddr_Type()
)
cnnEouHostResultMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultMacAddr.setStatus("current")
_CnnEouHostResultAuthType_Type = CnnEouAuthType
_CnnEouHostResultAuthType_Object = MibTableColumn
cnnEouHostResultAuthType = _CnnEouHostResultAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 6),
    _CnnEouHostResultAuthType_Type()
)
cnnEouHostResultAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultAuthType.setStatus("current")
_CnnEouHostResultPostureToken_Type = CnnEouPostureToken
_CnnEouHostResultPostureToken_Object = MibTableColumn
cnnEouHostResultPostureToken = _CnnEouHostResultPostureToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 7),
    _CnnEouHostResultPostureToken_Type()
)
cnnEouHostResultPostureToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultPostureToken.setStatus("deprecated")
_CnnEouHostResultAge_Type = Unsigned32
_CnnEouHostResultAge_Object = MibTableColumn
cnnEouHostResultAge = _CnnEouHostResultAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 8),
    _CnnEouHostResultAge_Type()
)
cnnEouHostResultAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultAge.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouHostResultAge.setUnits("minutes")
_CnnEouHostResultUrlRedir_Type = CiscoURLString
_CnnEouHostResultUrlRedir_Object = MibTableColumn
cnnEouHostResultUrlRedir = _CnnEouHostResultUrlRedir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 9),
    _CnnEouHostResultUrlRedir_Type()
)
cnnEouHostResultUrlRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultUrlRedir.setStatus("current")
_CnnEouHostResultAclName_Type = SnmpAdminString
_CnnEouHostResultAclName_Object = MibTableColumn
cnnEouHostResultAclName = _CnnEouHostResultAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 10),
    _CnnEouHostResultAclName_Type()
)
cnnEouHostResultAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultAclName.setStatus("current")
_CnnEouHostResultStatusQryPeriod_Type = Unsigned32
_CnnEouHostResultStatusQryPeriod_Object = MibTableColumn
cnnEouHostResultStatusQryPeriod = _CnnEouHostResultStatusQryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 11),
    _CnnEouHostResultStatusQryPeriod_Type()
)
cnnEouHostResultStatusQryPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultStatusQryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouHostResultStatusQryPeriod.setUnits("seconds")
_CnnEouHostResultRevalidatePeriod_Type = Unsigned32
_CnnEouHostResultRevalidatePeriod_Object = MibTableColumn
cnnEouHostResultRevalidatePeriod = _CnnEouHostResultRevalidatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 12),
    _CnnEouHostResultRevalidatePeriod_Type()
)
cnnEouHostResultRevalidatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultRevalidatePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cnnEouHostResultRevalidatePeriod.setUnits("seconds")
_CnnEouHostResultState_Type = CnnEouState
_CnnEouHostResultState_Object = MibTableColumn
cnnEouHostResultState = _CnnEouHostResultState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 13),
    _CnnEouHostResultState_Type()
)
cnnEouHostResultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultState.setStatus("current")
_CnnEouHostResultPostureTokenStr_Type = CnnEouPostureTokenString
_CnnEouHostResultPostureTokenStr_Object = MibTableColumn
cnnEouHostResultPostureTokenStr = _CnnEouHostResultPostureTokenStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 14),
    _CnnEouHostResultPostureTokenStr_Type()
)
cnnEouHostResultPostureTokenStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultPostureTokenStr.setStatus("current")
_CnnEouHostResultUrlRedirectAcl_Type = SnmpAdminString
_CnnEouHostResultUrlRedirectAcl_Object = MibTableColumn
cnnEouHostResultUrlRedirectAcl = _CnnEouHostResultUrlRedirectAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 15),
    _CnnEouHostResultUrlRedirectAcl_Type()
)
cnnEouHostResultUrlRedirectAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultUrlRedirectAcl.setStatus("current")
_CnnEouHostResultTagName_Type = SnmpAdminString
_CnnEouHostResultTagName_Object = MibTableColumn
cnnEouHostResultTagName = _CnnEouHostResultTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 16),
    _CnnEouHostResultTagName_Type()
)
cnnEouHostResultTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultTagName.setStatus("current")
_CnnEouHostResultAuditSessionId_Type = SnmpAdminString
_CnnEouHostResultAuditSessionId_Object = MibTableColumn
cnnEouHostResultAuditSessionId = _CnnEouHostResultAuditSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 17),
    _CnnEouHostResultAuditSessionId_Type()
)
cnnEouHostResultAuditSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultAuditSessionId.setStatus("current")
_CnnEouHostResultAaaFailPolicy_Type = SnmpAdminString
_CnnEouHostResultAaaFailPolicy_Object = MibTableColumn
cnnEouHostResultAaaFailPolicy = _CnnEouHostResultAaaFailPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 8, 1, 18),
    _CnnEouHostResultAaaFailPolicy_Type()
)
cnnEouHostResultAaaFailPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnnEouHostResultAaaFailPolicy.setStatus("current")
_CnnEouHostValidatePostureTokenStr_Type = CnnEouPostureTokenString
_CnnEouHostValidatePostureTokenStr_Object = MibScalar
cnnEouHostValidatePostureTokenStr = _CnnEouHostValidatePostureTokenStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 4, 9),
    _CnnEouHostValidatePostureTokenStr_Type()
)
cnnEouHostValidatePostureTokenStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouHostValidatePostureTokenStr.setStatus("current")
_CnnIpDeviceTrackingObjects_ObjectIdentity = ObjectIdentity
cnnIpDeviceTrackingObjects = _CnnIpDeviceTrackingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5)
)
_CnnIpDeviceTrackingEnabled_Type = TruthValue
_CnnIpDeviceTrackingEnabled_Object = MibScalar
cnnIpDeviceTrackingEnabled = _CnnIpDeviceTrackingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5, 1),
    _CnnIpDeviceTrackingEnabled_Type()
)
cnnIpDeviceTrackingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnIpDeviceTrackingEnabled.setStatus("current")
_CnnIpDeviceTrackingProbeCount_Type = Unsigned32
_CnnIpDeviceTrackingProbeCount_Object = MibScalar
cnnIpDeviceTrackingProbeCount = _CnnIpDeviceTrackingProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5, 2),
    _CnnIpDeviceTrackingProbeCount_Type()
)
cnnIpDeviceTrackingProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnIpDeviceTrackingProbeCount.setStatus("current")
_CnnIpDeviceTrackingProbeInterval_Type = Unsigned32
_CnnIpDeviceTrackingProbeInterval_Object = MibScalar
cnnIpDeviceTrackingProbeInterval = _CnnIpDeviceTrackingProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5, 3),
    _CnnIpDeviceTrackingProbeInterval_Type()
)
cnnIpDeviceTrackingProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnIpDeviceTrackingProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    cnnIpDeviceTrackingProbeInterval.setUnits("seconds")
_CnnEouIfIpDevTrackConfigTable_Object = MibTable
cnnEouIfIpDevTrackConfigTable = _CnnEouIfIpDevTrackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cnnEouIfIpDevTrackConfigTable.setStatus("current")
_CnnEouIfIpDevTrackConfigEntry_Object = MibTableRow
cnnEouIfIpDevTrackConfigEntry = _CnnEouIfIpDevTrackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5, 4, 1)
)
cnnEouIfIpDevTrackConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnnEouIfIpDevTrackConfigEntry.setStatus("current")
_CnnEouIfIpDevTrackEnabled_Type = TruthValue
_CnnEouIfIpDevTrackEnabled_Object = MibTableColumn
cnnEouIfIpDevTrackEnabled = _CnnEouIfIpDevTrackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 1, 5, 4, 1, 1),
    _CnnEouIfIpDevTrackEnabled_Type()
)
cnnEouIfIpDevTrackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnnEouIfIpDevTrackEnabled.setStatus("current")
_CiscoNacNadMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNacNadMIBConformance = _CiscoNacNadMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2)
)
_CiscoNacNadMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNacNadMIBCompliances = _CiscoNacNadMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 1)
)
_CiscoNacNadMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNacNadMIBGroups = _CiscoNacNadMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2)
)

# Managed Objects groups

ciscoNacNadEouGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 1)
)
ciscoNacNadEouGlobalGroup.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouVersion"),
        ("CISCO-NAC-NAD-MIB", "cnnEouEnabled"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAllowClientless"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAllowIpStationId"),
        ("CISCO-NAC-NAD-MIB", "cnnEouLoggingEnabled"),
        ("CISCO-NAC-NAD-MIB", "cnnEouMaxRetry"),
        ("CISCO-NAC-NAD-MIB", "cnnEouPort"),
        ("CISCO-NAC-NAD-MIB", "cnnEouTimeoutAAA"),
        ("CISCO-NAC-NAD-MIB", "cnnEouTimeoutHoldPeriod"),
        ("CISCO-NAC-NAD-MIB", "cnnEouTimeoutRetransmit"),
        ("CISCO-NAC-NAD-MIB", "cnnEouTimeoutRevalidation"),
        ("CISCO-NAC-NAD-MIB", "cnnEouTimeoutStatusQuery"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouGlobalGroup.setStatus("current")

ciscoNacNadEouAuthIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 2)
)
ciscoNacNadEouAuthIpGroup.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouAuthIpAddrMask"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthIpPolicy"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthIpStorageType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthIpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouAuthIpGroup.setStatus("current")

ciscoNacNadEouAuthMacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 3)
)
ciscoNacNadEouAuthMacGroup.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouAuthMacAddrMask"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthMacPolicy"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthMacStorageType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthMacRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouAuthMacGroup.setStatus("current")

ciscoNacNadEouAuthDeviceTypeGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 4)
)
ciscoNacNadEouAuthDeviceTypeGrp.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouAuthDeviceTypeStorageType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouAuthDeviceTypeRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouAuthDeviceTypeGrp.setStatus("current")

ciscoNacNadEouIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 5)
)
ciscoNacNadEouIfConfigGroup.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouIfValidateAction")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouIfConfigGroup.setStatus("current")

ciscoNacNadEouHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 6)
)
ciscoNacNadEouHostGroup.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouHostValidateAction"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidateIpAddrType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidateIpAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidateMacAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidatePostureToken"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostMaxQueries"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryMask"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryInterface"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryIpAddrType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryIpAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryMacAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryPostureToken"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQuerySkipNHosts"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryMaxResultRows"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryTotalHosts"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryRows"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryCreateTime"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryStatus"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAssocIf"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultIpAddrType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultIpAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultMacAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAuthType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultPostureToken"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultStatusQryPeriod"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultRevalidatePeriod"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultState"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouHostGroup.setStatus("deprecated")

ciscoNacNadEouIfTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 7)
)
ciscoNacNadEouIfTimeoutGroup.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouIfTimeoutGlobalConfig"),
        ("CISCO-NAC-NAD-MIB", "cnnEouIfTimeoutAAA"),
        ("CISCO-NAC-NAD-MIB", "cnnEouIfTimeoutHoldPeriod"),
        ("CISCO-NAC-NAD-MIB", "cnnEouIfTimeoutRetransmit"),
        ("CISCO-NAC-NAD-MIB", "cnnEouIfTimeoutRevalidation"),
        ("CISCO-NAC-NAD-MIB", "cnnEouIfTimeoutStatusQuery"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouIfTimeoutGroup.setStatus("current")

ciscoNacNadEouIfMaxRetryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 8)
)
ciscoNacNadEouIfMaxRetryGroup.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouIfMaxRetry")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouIfMaxRetryGroup.setStatus("current")

ciscoNacNadEouRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 9)
)
ciscoNacNadEouRateLimitGroup.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouRateLimit")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouRateLimitGroup.setStatus("current")

ciscoNacNadEouIfAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 10)
)
ciscoNacNadEouIfAdminGroup.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouIfAdminStatus")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouIfAdminGroup.setStatus("current")

ciscoNacNadEouHostAgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 11)
)
ciscoNacNadEouHostAgeGroup.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAge")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouHostAgeGroup.setStatus("current")

ciscoNacNadEouHostUrlRedir = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 12)
)
ciscoNacNadEouHostUrlRedir.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouHostResultUrlRedir")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouHostUrlRedir.setStatus("current")

ciscoNacNadEouHostAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 13)
)
ciscoNacNadEouHostAclGroup.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAclName")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouHostAclGroup.setStatus("current")

ciscoNacNadEouIfAaaFailPolicyGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 14)
)
ciscoNacNadEouIfAaaFailPolicyGrp.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouIfAaaFailPolicy")
)
if mibBuilder.loadTexts:
    ciscoNacNadEouIfAaaFailPolicyGrp.setStatus("current")

ciscoNacNadEouHostGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 15)
)
ciscoNacNadEouHostGrp.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouHostValidateAction"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidateIpAddrType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidateIpAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidateMacAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostValidatePostureTokenStr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostMaxQueries"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryMask"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryInterface"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryIpAddrType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryIpAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryMacAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryPostureTokenStr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQuerySkipNHosts"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryMaxResultRows"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryTotalHosts"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryRows"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryCreateTime"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostQueryStatus"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAssocIf"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultIpAddrType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultIpAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultMacAddr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAuthType"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultPostureTokenStr"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultStatusQryPeriod"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultRevalidatePeriod"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultState"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouHostGrp.setStatus("current")

cnnIpDeviceTrackingConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 16)
)
cnnIpDeviceTrackingConfigGrp.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnIpDeviceTrackingEnabled"),
        ("CISCO-NAC-NAD-MIB", "cnnIpDeviceTrackingProbeCount"),
        ("CISCO-NAC-NAD-MIB", "cnnIpDeviceTrackingProbeInterval"))
)
if mibBuilder.loadTexts:
    cnnIpDeviceTrackingConfigGrp.setStatus("current")

cnnEouCriticalRecoveryDelayGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 17)
)
cnnEouCriticalRecoveryDelayGrp.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouCriticalRecoveryDelay")
)
if mibBuilder.loadTexts:
    cnnEouCriticalRecoveryDelayGrp.setStatus("current")

cnnEouIfIpDevTrackConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 18)
)
cnnEouIfIpDevTrackConfigGrp.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouIfIpDevTrackEnabled")
)
if mibBuilder.loadTexts:
    cnnEouIfIpDevTrackConfigGrp.setStatus("current")

ciscoNacNadRevalidateConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 19)
)
ciscoNacNadRevalidateConfigGrp.setObjects(
    ("CISCO-NAC-NAD-MIB", "cnnEouRevalidationEnabled")
)
if mibBuilder.loadTexts:
    ciscoNacNadRevalidateConfigGrp.setStatus("current")

ciscoNacNadEouHostGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 20)
)
ciscoNacNadEouHostGroup1.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouHostResultUrlRedirectAcl"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultTagName"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAuditSessionId"),
        ("CISCO-NAC-NAD-MIB", "cnnEouHostResultAaaFailPolicy"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouHostGroup1.setStatus("current")

ciscoNacNadEouIfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 2, 21)
)
ciscoNacNadEouIfExtGroup.setObjects(
      *(("CISCO-NAC-NAD-MIB", "cnnEouIfAllowClientless"),
        ("CISCO-NAC-NAD-MIB", "cnnEouIfAllowIpStationId"))
)
if mibBuilder.loadTexts:
    ciscoNacNadEouIfExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNacNadMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNacNadMIBCompliance.setStatus(
        "deprecated"
    )

ciscoNacNadMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoNacNadMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoNacNadMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoNacNadMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoNacNadMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 484, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoNacNadMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NAC-NAD-MIB",
    **{"ciscoNacNadMIB": ciscoNacNadMIB,
       "ciscoNacNadMIBNotifs": ciscoNacNadMIBNotifs,
       "ciscoNacNadMIBObjects": ciscoNacNadMIBObjects,
       "cnnEouGlobalObjects": cnnEouGlobalObjects,
       "cnnEouVersion": cnnEouVersion,
       "cnnEouEnabled": cnnEouEnabled,
       "cnnEouAllowClientless": cnnEouAllowClientless,
       "cnnEouAllowIpStationId": cnnEouAllowIpStationId,
       "cnnEouLoggingEnabled": cnnEouLoggingEnabled,
       "cnnEouMaxRetry": cnnEouMaxRetry,
       "cnnEouPort": cnnEouPort,
       "cnnEouRateLimit": cnnEouRateLimit,
       "cnnEouTimeoutAAA": cnnEouTimeoutAAA,
       "cnnEouTimeoutHoldPeriod": cnnEouTimeoutHoldPeriod,
       "cnnEouTimeoutRetransmit": cnnEouTimeoutRetransmit,
       "cnnEouTimeoutRevalidation": cnnEouTimeoutRevalidation,
       "cnnEouTimeoutStatusQuery": cnnEouTimeoutStatusQuery,
       "cnnEouCriticalRecoveryDelay": cnnEouCriticalRecoveryDelay,
       "cnnEouRevalidationEnabled": cnnEouRevalidationEnabled,
       "cnnEouAuthorizeLists": cnnEouAuthorizeLists,
       "cnnEouAuthIpTable": cnnEouAuthIpTable,
       "cnnEouAuthIpEntry": cnnEouAuthIpEntry,
       "cnnEouAuthIpAddrType": cnnEouAuthIpAddrType,
       "cnnEouAuthIpAddr": cnnEouAuthIpAddr,
       "cnnEouAuthIpAddrMask": cnnEouAuthIpAddrMask,
       "cnnEouAuthIpPolicy": cnnEouAuthIpPolicy,
       "cnnEouAuthIpStorageType": cnnEouAuthIpStorageType,
       "cnnEouAuthIpRowStatus": cnnEouAuthIpRowStatus,
       "cnnEouAuthMacTable": cnnEouAuthMacTable,
       "cnnEouAuthMacEntry": cnnEouAuthMacEntry,
       "cnnEouAuthMacAddr": cnnEouAuthMacAddr,
       "cnnEouAuthMacAddrMask": cnnEouAuthMacAddrMask,
       "cnnEouAuthMacPolicy": cnnEouAuthMacPolicy,
       "cnnEouAuthMacStorageType": cnnEouAuthMacStorageType,
       "cnnEouAuthMacRowStatus": cnnEouAuthMacRowStatus,
       "cnnEouAuthDeviceTypeTable": cnnEouAuthDeviceTypeTable,
       "cnnEouAuthDeviceTypeEntry": cnnEouAuthDeviceTypeEntry,
       "cnnEouAuthDeviceType": cnnEouAuthDeviceType,
       "cnnEouAuthDeviceTypeStorageType": cnnEouAuthDeviceTypeStorageType,
       "cnnEouAuthDeviceTypeRowStatus": cnnEouAuthDeviceTypeRowStatus,
       "cnnEouIfMIBObjects": cnnEouIfMIBObjects,
       "cnnEouIfConfigTable": cnnEouIfConfigTable,
       "cnnEouIfConfigEntry": cnnEouIfConfigEntry,
       "cnnEouIfAdminStatus": cnnEouIfAdminStatus,
       "cnnEouIfMaxRetry": cnnEouIfMaxRetry,
       "cnnEouIfValidateAction": cnnEouIfValidateAction,
       "cnnEouIfTimeoutGlobalConfig": cnnEouIfTimeoutGlobalConfig,
       "cnnEouIfTimeoutAAA": cnnEouIfTimeoutAAA,
       "cnnEouIfTimeoutHoldPeriod": cnnEouIfTimeoutHoldPeriod,
       "cnnEouIfTimeoutRetransmit": cnnEouIfTimeoutRetransmit,
       "cnnEouIfTimeoutRevalidation": cnnEouIfTimeoutRevalidation,
       "cnnEouIfTimeoutStatusQuery": cnnEouIfTimeoutStatusQuery,
       "cnnEouIfAaaFailPolicy": cnnEouIfAaaFailPolicy,
       "cnnEouIfAllowClientless": cnnEouIfAllowClientless,
       "cnnEouIfAllowIpStationId": cnnEouIfAllowIpStationId,
       "cnnEouHostMIBObjects": cnnEouHostMIBObjects,
       "cnnEouHostValidateAction": cnnEouHostValidateAction,
       "cnnEouHostValidateIpAddrType": cnnEouHostValidateIpAddrType,
       "cnnEouHostValidateIpAddr": cnnEouHostValidateIpAddr,
       "cnnEouHostValidateMacAddr": cnnEouHostValidateMacAddr,
       "cnnEouHostValidatePostureToken": cnnEouHostValidatePostureToken,
       "cnnEouHostMaxQueries": cnnEouHostMaxQueries,
       "cnnEouHostQueryTable": cnnEouHostQueryTable,
       "cnnEouHostQueryEntry": cnnEouHostQueryEntry,
       "cnnEouHostQueryIndex": cnnEouHostQueryIndex,
       "cnnEouHostQueryMask": cnnEouHostQueryMask,
       "cnnEouHostQueryInterface": cnnEouHostQueryInterface,
       "cnnEouHostQueryIpAddrType": cnnEouHostQueryIpAddrType,
       "cnnEouHostQueryIpAddr": cnnEouHostQueryIpAddr,
       "cnnEouHostQueryMacAddr": cnnEouHostQueryMacAddr,
       "cnnEouHostQueryPostureToken": cnnEouHostQueryPostureToken,
       "cnnEouHostQuerySkipNHosts": cnnEouHostQuerySkipNHosts,
       "cnnEouHostQueryMaxResultRows": cnnEouHostQueryMaxResultRows,
       "cnnEouHostQueryTotalHosts": cnnEouHostQueryTotalHosts,
       "cnnEouHostQueryRows": cnnEouHostQueryRows,
       "cnnEouHostQueryCreateTime": cnnEouHostQueryCreateTime,
       "cnnEouHostQueryStatus": cnnEouHostQueryStatus,
       "cnnEouHostQueryPostureTokenStr": cnnEouHostQueryPostureTokenStr,
       "cnnEouHostResultTable": cnnEouHostResultTable,
       "cnnEouHostResultEntry": cnnEouHostResultEntry,
       "cnnEouHostResultIndex": cnnEouHostResultIndex,
       "cnnEouHostResultAssocIf": cnnEouHostResultAssocIf,
       "cnnEouHostResultIpAddrType": cnnEouHostResultIpAddrType,
       "cnnEouHostResultIpAddr": cnnEouHostResultIpAddr,
       "cnnEouHostResultMacAddr": cnnEouHostResultMacAddr,
       "cnnEouHostResultAuthType": cnnEouHostResultAuthType,
       "cnnEouHostResultPostureToken": cnnEouHostResultPostureToken,
       "cnnEouHostResultAge": cnnEouHostResultAge,
       "cnnEouHostResultUrlRedir": cnnEouHostResultUrlRedir,
       "cnnEouHostResultAclName": cnnEouHostResultAclName,
       "cnnEouHostResultStatusQryPeriod": cnnEouHostResultStatusQryPeriod,
       "cnnEouHostResultRevalidatePeriod": cnnEouHostResultRevalidatePeriod,
       "cnnEouHostResultState": cnnEouHostResultState,
       "cnnEouHostResultPostureTokenStr": cnnEouHostResultPostureTokenStr,
       "cnnEouHostResultUrlRedirectAcl": cnnEouHostResultUrlRedirectAcl,
       "cnnEouHostResultTagName": cnnEouHostResultTagName,
       "cnnEouHostResultAuditSessionId": cnnEouHostResultAuditSessionId,
       "cnnEouHostResultAaaFailPolicy": cnnEouHostResultAaaFailPolicy,
       "cnnEouHostValidatePostureTokenStr": cnnEouHostValidatePostureTokenStr,
       "cnnIpDeviceTrackingObjects": cnnIpDeviceTrackingObjects,
       "cnnIpDeviceTrackingEnabled": cnnIpDeviceTrackingEnabled,
       "cnnIpDeviceTrackingProbeCount": cnnIpDeviceTrackingProbeCount,
       "cnnIpDeviceTrackingProbeInterval": cnnIpDeviceTrackingProbeInterval,
       "cnnEouIfIpDevTrackConfigTable": cnnEouIfIpDevTrackConfigTable,
       "cnnEouIfIpDevTrackConfigEntry": cnnEouIfIpDevTrackConfigEntry,
       "cnnEouIfIpDevTrackEnabled": cnnEouIfIpDevTrackEnabled,
       "ciscoNacNadMIBConformance": ciscoNacNadMIBConformance,
       "ciscoNacNadMIBCompliances": ciscoNacNadMIBCompliances,
       "ciscoNacNadMIBCompliance": ciscoNacNadMIBCompliance,
       "ciscoNacNadMIBCompliance2": ciscoNacNadMIBCompliance2,
       "ciscoNacNadMIBCompliance3": ciscoNacNadMIBCompliance3,
       "ciscoNacNadMIBCompliance4": ciscoNacNadMIBCompliance4,
       "ciscoNacNadMIBGroups": ciscoNacNadMIBGroups,
       "ciscoNacNadEouGlobalGroup": ciscoNacNadEouGlobalGroup,
       "ciscoNacNadEouAuthIpGroup": ciscoNacNadEouAuthIpGroup,
       "ciscoNacNadEouAuthMacGroup": ciscoNacNadEouAuthMacGroup,
       "ciscoNacNadEouAuthDeviceTypeGrp": ciscoNacNadEouAuthDeviceTypeGrp,
       "ciscoNacNadEouIfConfigGroup": ciscoNacNadEouIfConfigGroup,
       "ciscoNacNadEouHostGroup": ciscoNacNadEouHostGroup,
       "ciscoNacNadEouIfTimeoutGroup": ciscoNacNadEouIfTimeoutGroup,
       "ciscoNacNadEouIfMaxRetryGroup": ciscoNacNadEouIfMaxRetryGroup,
       "ciscoNacNadEouRateLimitGroup": ciscoNacNadEouRateLimitGroup,
       "ciscoNacNadEouIfAdminGroup": ciscoNacNadEouIfAdminGroup,
       "ciscoNacNadEouHostAgeGroup": ciscoNacNadEouHostAgeGroup,
       "ciscoNacNadEouHostUrlRedir": ciscoNacNadEouHostUrlRedir,
       "ciscoNacNadEouHostAclGroup": ciscoNacNadEouHostAclGroup,
       "ciscoNacNadEouIfAaaFailPolicyGrp": ciscoNacNadEouIfAaaFailPolicyGrp,
       "ciscoNacNadEouHostGrp": ciscoNacNadEouHostGrp,
       "cnnIpDeviceTrackingConfigGrp": cnnIpDeviceTrackingConfigGrp,
       "cnnEouCriticalRecoveryDelayGrp": cnnEouCriticalRecoveryDelayGrp,
       "cnnEouIfIpDevTrackConfigGrp": cnnEouIfIpDevTrackConfigGrp,
       "ciscoNacNadRevalidateConfigGrp": ciscoNacNadRevalidateConfigGrp,
       "ciscoNacNadEouHostGroup1": ciscoNacNadEouHostGroup1,
       "ciscoNacNadEouIfExtGroup": ciscoNacNadEouIfExtGroup}
)
