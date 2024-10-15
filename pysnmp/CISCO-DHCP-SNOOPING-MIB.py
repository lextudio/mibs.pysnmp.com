# SNMP MIB module (CISCO-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DHCP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:58 2024
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

(InterfaceIndex,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380)
)
ciscoDhcpSnoopingMIB.setRevisions(
        ("2009-08-26 00:00",
         "2009-08-10 00:00",
         "2009-04-12 00:00",
         "2007-11-13 00:00",
         "2007-07-12 00:00",
         "2007-05-30 00:00",
         "2006-03-16 16:00",
         "2005-10-26 00:00",
         "2004-03-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDhcpSnoopingMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDhcpSnoopingMIBNotifs = _CiscoDhcpSnoopingMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 0)
)
_CiscoDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDhcpSnoopingMIBObjects = _CiscoDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1)
)
_CdsGlobal_ObjectIdentity = ObjectIdentity
cdsGlobal = _CdsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1)
)
_CdsFeatureEnable_Type = TruthValue
_CdsFeatureEnable_Object = MibScalar
cdsFeatureEnable = _CdsFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 1),
    _CdsFeatureEnable_Type()
)
cdsFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsFeatureEnable.setStatus("current")
_CdsDatabaseFile_Type = SnmpAdminString
_CdsDatabaseFile_Object = MibScalar
cdsDatabaseFile = _CdsDatabaseFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 2),
    _CdsDatabaseFile_Type()
)
cdsDatabaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsDatabaseFile.setStatus("current")
_CdsDatabaseUpdateInterval_Type = Unsigned32
_CdsDatabaseUpdateInterval_Object = MibScalar
cdsDatabaseUpdateInterval = _CdsDatabaseUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 3),
    _CdsDatabaseUpdateInterval_Type()
)
cdsDatabaseUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsDatabaseUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdsDatabaseUpdateInterval.setUnits("seconds")
_CdsRelayAgentInfoOptEnable_Type = TruthValue
_CdsRelayAgentInfoOptEnable_Object = MibScalar
cdsRelayAgentInfoOptEnable = _CdsRelayAgentInfoOptEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 4),
    _CdsRelayAgentInfoOptEnable_Type()
)
cdsRelayAgentInfoOptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsRelayAgentInfoOptEnable.setStatus("current")
_CdsRelayAgentInfoOptRemoteId_Type = MacAddress
_CdsRelayAgentInfoOptRemoteId_Object = MibScalar
cdsRelayAgentInfoOptRemoteId = _CdsRelayAgentInfoOptRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 5),
    _CdsRelayAgentInfoOptRemoteId_Type()
)
cdsRelayAgentInfoOptRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsRelayAgentInfoOptRemoteId.setStatus("deprecated")
_CdsMatchMacAddressEnable_Type = TruthValue
_CdsMatchMacAddressEnable_Object = MibScalar
cdsMatchMacAddressEnable = _CdsMatchMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 6),
    _CdsMatchMacAddressEnable_Type()
)
cdsMatchMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsMatchMacAddressEnable.setStatus("current")
_CdsGlobalMaxBindingsLimit_Type = Unsigned32
_CdsGlobalMaxBindingsLimit_Object = MibScalar
cdsGlobalMaxBindingsLimit = _CdsGlobalMaxBindingsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 7),
    _CdsGlobalMaxBindingsLimit_Type()
)
cdsGlobalMaxBindingsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsGlobalMaxBindingsLimit.setStatus("current")


class _CdsRelayAgentInfoOptRemoteIdSub_Type(OctetString):
    """Custom type cdsRelayAgentInfoOptRemoteIdSub based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CdsRelayAgentInfoOptRemoteIdSub_Type.__name__ = "OctetString"
_CdsRelayAgentInfoOptRemoteIdSub_Object = MibScalar
cdsRelayAgentInfoOptRemoteIdSub = _CdsRelayAgentInfoOptRemoteIdSub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 8),
    _CdsRelayAgentInfoOptRemoteIdSub_Type()
)
cdsRelayAgentInfoOptRemoteIdSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsRelayAgentInfoOptRemoteIdSub.setStatus("current")
_CdsBindingsNotifEnabled_Type = TruthValue
_CdsBindingsNotifEnabled_Object = MibScalar
cdsBindingsNotifEnabled = _CdsBindingsNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 1, 9),
    _CdsBindingsNotifEnabled_Type()
)
cdsBindingsNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsBindingsNotifEnabled.setStatus("current")
_CdsVlan_ObjectIdentity = ObjectIdentity
cdsVlan = _CdsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 2)
)
_CdsVlanConfigTable_Object = MibTable
cdsVlanConfigTable = _CdsVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdsVlanConfigTable.setStatus("current")
_CdsVlanConfigEntry_Object = MibTableRow
cdsVlanConfigEntry = _CdsVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 2, 1, 1)
)
cdsVlanConfigEntry.setIndexNames(
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsVlanIndex"),
)
if mibBuilder.loadTexts:
    cdsVlanConfigEntry.setStatus("current")
_CdsVlanIndex_Type = VlanIndex
_CdsVlanIndex_Object = MibTableColumn
cdsVlanIndex = _CdsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 2, 1, 1, 1),
    _CdsVlanIndex_Type()
)
cdsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsVlanIndex.setStatus("current")
_CdsVlanDhcpSnoopingEnable_Type = TruthValue
_CdsVlanDhcpSnoopingEnable_Object = MibTableColumn
cdsVlanDhcpSnoopingEnable = _CdsVlanDhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 2, 1, 1, 2),
    _CdsVlanDhcpSnoopingEnable_Type()
)
cdsVlanDhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsVlanDhcpSnoopingEnable.setStatus("current")


class _CdsVlanDhcpSnoopingOperStatus_Type(Integer32):
    """Custom type cdsVlanDhcpSnoopingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("operational", 1))
    )


_CdsVlanDhcpSnoopingOperStatus_Type.__name__ = "Integer32"
_CdsVlanDhcpSnoopingOperStatus_Object = MibTableColumn
cdsVlanDhcpSnoopingOperStatus = _CdsVlanDhcpSnoopingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 2, 1, 1, 3),
    _CdsVlanDhcpSnoopingOperStatus_Type()
)
cdsVlanDhcpSnoopingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsVlanDhcpSnoopingOperStatus.setStatus("current")
_CdsInterface_ObjectIdentity = ObjectIdentity
cdsInterface = _CdsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3)
)
_CdsIfConfigTable_Object = MibTable
cdsIfConfigTable = _CdsIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdsIfConfigTable.setStatus("current")
_CdsIfConfigEntry_Object = MibTableRow
cdsIfConfigEntry = _CdsIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 1, 1)
)
cdsIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdsIfConfigEntry.setStatus("current")
_CdsIfTrustEnable_Type = TruthValue
_CdsIfTrustEnable_Object = MibTableColumn
cdsIfTrustEnable = _CdsIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 1, 1, 1),
    _CdsIfTrustEnable_Type()
)
cdsIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsIfTrustEnable.setStatus("current")
_CdsIfRateLimitTable_Object = MibTable
cdsIfRateLimitTable = _CdsIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdsIfRateLimitTable.setStatus("current")
_CdsIfRateLimitEntry_Object = MibTableRow
cdsIfRateLimitEntry = _CdsIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 2, 1)
)
cdsIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdsIfRateLimitEntry.setStatus("current")
_CdsIfRateLimit_Type = Unsigned32
_CdsIfRateLimit_Object = MibTableColumn
cdsIfRateLimit = _CdsIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 2, 1, 1),
    _CdsIfRateLimit_Type()
)
cdsIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cdsIfRateLimit.setUnits("packets per second")
_CdsIfFeatureConfigTable_Object = MibTable
cdsIfFeatureConfigTable = _CdsIfFeatureConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cdsIfFeatureConfigTable.setStatus("current")
_CdsIfFeatureConfigEntry_Object = MibTableRow
cdsIfFeatureConfigEntry = _CdsIfFeatureConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 3, 1)
)
cdsIfFeatureConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdsIfFeatureConfigEntry.setStatus("current")
_CdsIfFeatureEnable_Type = TruthValue
_CdsIfFeatureEnable_Object = MibTableColumn
cdsIfFeatureEnable = _CdsIfFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 3, 1, 1),
    _CdsIfFeatureEnable_Type()
)
cdsIfFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsIfFeatureEnable.setStatus("current")
_CdsIfBindingsLimitTable_Object = MibTable
cdsIfBindingsLimitTable = _CdsIfBindingsLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cdsIfBindingsLimitTable.setStatus("current")
_CdsIfBindingsLimitEntry_Object = MibTableRow
cdsIfBindingsLimitEntry = _CdsIfBindingsLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 4, 1)
)
cdsIfBindingsLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdsIfBindingsLimitEntry.setStatus("current")
_CdsIfBindingsLimit_Type = Unsigned32
_CdsIfBindingsLimit_Object = MibTableColumn
cdsIfBindingsLimit = _CdsIfBindingsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 4, 1, 1),
    _CdsIfBindingsLimit_Type()
)
cdsIfBindingsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsIfBindingsLimit.setStatus("current")
_CdsIfVlanRelayInfoOptCircuitIdTable_Object = MibTable
cdsIfVlanRelayInfoOptCircuitIdTable = _CdsIfVlanRelayInfoOptCircuitIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitIdTable.setStatus("current")
_CdsIfVlanRelayInfoOptCircuitIdEntry_Object = MibTableRow
cdsIfVlanRelayInfoOptCircuitIdEntry = _CdsIfVlanRelayInfoOptCircuitIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 5, 1)
)
cdsIfVlanRelayInfoOptCircuitIdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsIfVlan"),
)
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitIdEntry.setStatus("current")
_CdsIfVlan_Type = VlanIndex
_CdsIfVlan_Object = MibTableColumn
cdsIfVlan = _CdsIfVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 5, 1, 1),
    _CdsIfVlan_Type()
)
cdsIfVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsIfVlan.setStatus("current")


class _CdsIfVlanRelayInfoOptCircuitId_Type(OctetString):
    """Custom type cdsIfVlanRelayInfoOptCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CdsIfVlanRelayInfoOptCircuitId_Type.__name__ = "OctetString"
_CdsIfVlanRelayInfoOptCircuitId_Object = MibTableColumn
cdsIfVlanRelayInfoOptCircuitId = _CdsIfVlanRelayInfoOptCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 5, 1, 2),
    _CdsIfVlanRelayInfoOptCircuitId_Type()
)
cdsIfVlanRelayInfoOptCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitId.setStatus("current")
_CdsIfVlanRelayInfoOptCircuitIdStatus_Type = RowStatus
_CdsIfVlanRelayInfoOptCircuitIdStatus_Object = MibTableColumn
cdsIfVlanRelayInfoOptCircuitIdStatus = _CdsIfVlanRelayInfoOptCircuitIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 5, 1, 3),
    _CdsIfVlanRelayInfoOptCircuitIdStatus_Type()
)
cdsIfVlanRelayInfoOptCircuitIdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitIdStatus.setStatus("current")
_CdsIfVlanRelayInfoOptCircuitIdDirect_Type = TruthValue
_CdsIfVlanRelayInfoOptCircuitIdDirect_Object = MibTableColumn
cdsIfVlanRelayInfoOptCircuitIdDirect = _CdsIfVlanRelayInfoOptCircuitIdDirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 3, 5, 1, 4),
    _CdsIfVlanRelayInfoOptCircuitIdDirect_Type()
)
cdsIfVlanRelayInfoOptCircuitIdDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitIdDirect.setStatus("current")
_CdsBindings_ObjectIdentity = ObjectIdentity
cdsBindings = _CdsBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4)
)
_CdsBindingsTable_Object = MibTable
cdsBindingsTable = _CdsBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdsBindingsTable.setStatus("current")
_CdsBindingsEntry_Object = MibTableRow
cdsBindingsEntry = _CdsBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1)
)
cdsBindingsEntry.setIndexNames(
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsBindingsVlan"),
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    cdsBindingsEntry.setStatus("current")
_CdsBindingsVlan_Type = VlanIndex
_CdsBindingsVlan_Object = MibTableColumn
cdsBindingsVlan = _CdsBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 1),
    _CdsBindingsVlan_Type()
)
cdsBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsBindingsVlan.setStatus("current")
_CdsBindingsMacAddress_Type = MacAddress
_CdsBindingsMacAddress_Object = MibTableColumn
cdsBindingsMacAddress = _CdsBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 2),
    _CdsBindingsMacAddress_Type()
)
cdsBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsBindingsMacAddress.setStatus("current")
_CdsBindingsAddrType_Type = InetAddressType
_CdsBindingsAddrType_Object = MibTableColumn
cdsBindingsAddrType = _CdsBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 3),
    _CdsBindingsAddrType_Type()
)
cdsBindingsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsBindingsAddrType.setStatus("current")
_CdsBindingsIpAddress_Type = InetAddress
_CdsBindingsIpAddress_Object = MibTableColumn
cdsBindingsIpAddress = _CdsBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 4),
    _CdsBindingsIpAddress_Type()
)
cdsBindingsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsBindingsIpAddress.setStatus("current")
_CdsBindingsInterface_Type = InterfaceIndex
_CdsBindingsInterface_Object = MibTableColumn
cdsBindingsInterface = _CdsBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 5),
    _CdsBindingsInterface_Type()
)
cdsBindingsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsBindingsInterface.setStatus("current")
_CdsBindingsLeasedTime_Type = Unsigned32
_CdsBindingsLeasedTime_Object = MibTableColumn
cdsBindingsLeasedTime = _CdsBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 6),
    _CdsBindingsLeasedTime_Type()
)
cdsBindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsBindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    cdsBindingsLeasedTime.setUnits("seconds")
_CdsBindingsStatus_Type = RowStatus
_CdsBindingsStatus_Object = MibTableColumn
cdsBindingsStatus = _CdsBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 7),
    _CdsBindingsStatus_Type()
)
cdsBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsBindingsStatus.setStatus("current")
_CdsBindingsHostname_Type = SnmpAdminString
_CdsBindingsHostname_Object = MibTableColumn
cdsBindingsHostname = _CdsBindingsHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 1, 1, 8),
    _CdsBindingsHostname_Type()
)
cdsBindingsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsBindingsHostname.setStatus("current")
_CdsStaticBindingsTable_Object = MibTable
cdsStaticBindingsTable = _CdsStaticBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cdsStaticBindingsTable.setStatus("current")
_CdsStaticBindingsEntry_Object = MibTableRow
cdsStaticBindingsEntry = _CdsStaticBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1)
)
cdsStaticBindingsEntry.setIndexNames(
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsStaticBindingsVlan"),
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsStaticBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    cdsStaticBindingsEntry.setStatus("current")
_CdsStaticBindingsVlan_Type = VlanIndex
_CdsStaticBindingsVlan_Object = MibTableColumn
cdsStaticBindingsVlan = _CdsStaticBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1, 1),
    _CdsStaticBindingsVlan_Type()
)
cdsStaticBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsStaticBindingsVlan.setStatus("current")
_CdsStaticBindingsMacAddress_Type = MacAddress
_CdsStaticBindingsMacAddress_Object = MibTableColumn
cdsStaticBindingsMacAddress = _CdsStaticBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1, 2),
    _CdsStaticBindingsMacAddress_Type()
)
cdsStaticBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsStaticBindingsMacAddress.setStatus("current")
_CdsStaticBindingsAddrType_Type = InetAddressType
_CdsStaticBindingsAddrType_Object = MibTableColumn
cdsStaticBindingsAddrType = _CdsStaticBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1, 3),
    _CdsStaticBindingsAddrType_Type()
)
cdsStaticBindingsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsStaticBindingsAddrType.setStatus("current")
_CdsStaticBindingsIpAddress_Type = InetAddress
_CdsStaticBindingsIpAddress_Object = MibTableColumn
cdsStaticBindingsIpAddress = _CdsStaticBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1, 4),
    _CdsStaticBindingsIpAddress_Type()
)
cdsStaticBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsStaticBindingsIpAddress.setStatus("current")
_CdsStaticBindingsInterface_Type = InterfaceIndex
_CdsStaticBindingsInterface_Object = MibTableColumn
cdsStaticBindingsInterface = _CdsStaticBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1, 5),
    _CdsStaticBindingsInterface_Type()
)
cdsStaticBindingsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsStaticBindingsInterface.setStatus("current")
_CdsStaticBindingsStatus_Type = RowStatus
_CdsStaticBindingsStatus_Object = MibTableColumn
cdsStaticBindingsStatus = _CdsStaticBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 4, 2, 1, 6),
    _CdsStaticBindingsStatus_Type()
)
cdsStaticBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsStaticBindingsStatus.setStatus("current")
_CdsStatistics_ObjectIdentity = ObjectIdentity
cdsStatistics = _CdsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 5)
)
_CdsTotalForwardedPkts_Type = Counter64
_CdsTotalForwardedPkts_Object = MibScalar
cdsTotalForwardedPkts = _CdsTotalForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 5, 1),
    _CdsTotalForwardedPkts_Type()
)
cdsTotalForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsTotalForwardedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cdsTotalForwardedPkts.setUnits("packets")
_CdsTotalDroppedPkts_Type = Counter64
_CdsTotalDroppedPkts_Object = MibScalar
cdsTotalDroppedPkts = _CdsTotalDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 5, 2),
    _CdsTotalDroppedPkts_Type()
)
cdsTotalDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsTotalDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cdsTotalDroppedPkts.setUnits("packets")
_CdsUntrustedPortDroppedPkts_Type = Counter64
_CdsUntrustedPortDroppedPkts_Object = MibScalar
cdsUntrustedPortDroppedPkts = _CdsUntrustedPortDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 5, 3),
    _CdsUntrustedPortDroppedPkts_Type()
)
cdsUntrustedPortDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsUntrustedPortDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cdsUntrustedPortDroppedPkts.setUnits("packets")
_CdsForwardedWithoutOption82Pkts_Type = Counter32
_CdsForwardedWithoutOption82Pkts_Object = MibScalar
cdsForwardedWithoutOption82Pkts = _CdsForwardedWithoutOption82Pkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 5, 4),
    _CdsForwardedWithoutOption82Pkts_Type()
)
cdsForwardedWithoutOption82Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsForwardedWithoutOption82Pkts.setStatus("current")
if mibBuilder.loadTexts:
    cdsForwardedWithoutOption82Pkts.setUnits("packets")
_CdsSrcGuard_ObjectIdentity = ObjectIdentity
cdsSrcGuard = _CdsSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6)
)
_CdsIfSrcGuardConfigTable_Object = MibTable
cdsIfSrcGuardConfigTable = _CdsIfSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardConfigTable.setStatus("current")
_CdsIfSrcGuardConfigEntry_Object = MibTableRow
cdsIfSrcGuardConfigEntry = _CdsIfSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 1, 1)
)
cdsIfSrcGuardConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardConfigEntry.setStatus("current")
_CdsIfSrcGuardEnable_Type = TruthValue
_CdsIfSrcGuardEnable_Object = MibTableColumn
cdsIfSrcGuardEnable = _CdsIfSrcGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 1, 1, 1),
    _CdsIfSrcGuardEnable_Type()
)
cdsIfSrcGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsIfSrcGuardEnable.setStatus("deprecated")


class _CdsIfSrcGuardFilterType_Type(Integer32):
    """Custom type cdsIfSrcGuardFilterType based on Integer32"""
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
        *(("disable", 1),
          ("ip", 2),
          ("ipMac", 3),
          ("strictIpMac", 4))
    )


_CdsIfSrcGuardFilterType_Type.__name__ = "Integer32"
_CdsIfSrcGuardFilterType_Object = MibTableColumn
cdsIfSrcGuardFilterType = _CdsIfSrcGuardFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 1, 1, 2),
    _CdsIfSrcGuardFilterType_Type()
)
cdsIfSrcGuardFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsIfSrcGuardFilterType.setStatus("current")
_CdsIfSrcGuardAddrTable_Object = MibTable
cdsIfSrcGuardAddrTable = _CdsIfSrcGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardAddrTable.setStatus("current")
_CdsIfSrcGuardAddrEntry_Object = MibTableRow
cdsIfSrcGuardAddrEntry = _CdsIfSrcGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1)
)
cdsIfSrcGuardAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardAddrEntry.setStatus("current")
_CdsIfSrcGuardIndex_Type = Unsigned32
_CdsIfSrcGuardIndex_Object = MibTableColumn
cdsIfSrcGuardIndex = _CdsIfSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 1),
    _CdsIfSrcGuardIndex_Type()
)
cdsIfSrcGuardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsIfSrcGuardIndex.setStatus("current")
_CdsIfSrcGuardAddrType_Type = InetAddressType
_CdsIfSrcGuardAddrType_Object = MibTableColumn
cdsIfSrcGuardAddrType = _CdsIfSrcGuardAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 2),
    _CdsIfSrcGuardAddrType_Type()
)
cdsIfSrcGuardAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardAddrType.setStatus("current")
_CdsIfSrcGuardAddress_Type = InetAddress
_CdsIfSrcGuardAddress_Object = MibTableColumn
cdsIfSrcGuardAddress = _CdsIfSrcGuardAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 3),
    _CdsIfSrcGuardAddress_Type()
)
cdsIfSrcGuardAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardAddress.setStatus("current")


class _CdsIfSrcGuardIpFilterAction_Type(Integer32):
    """Custom type cdsIfSrcGuardIpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denyAllIpAddress", 2),
          ("permitIpAddress", 1))
    )


_CdsIfSrcGuardIpFilterAction_Type.__name__ = "Integer32"
_CdsIfSrcGuardIpFilterAction_Object = MibTableColumn
cdsIfSrcGuardIpFilterAction = _CdsIfSrcGuardIpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 4),
    _CdsIfSrcGuardIpFilterAction_Type()
)
cdsIfSrcGuardIpFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardIpFilterAction.setStatus("current")


class _CdsIfSrcGuardFilterMode_Type(Integer32):
    """Custom type cdsIfSrcGuardFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactiveNoSnoopingVlan", 3),
          ("inactiveTrustPort", 2))
    )


_CdsIfSrcGuardFilterMode_Type.__name__ = "Integer32"
_CdsIfSrcGuardFilterMode_Object = MibTableColumn
cdsIfSrcGuardFilterMode = _CdsIfSrcGuardFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 5),
    _CdsIfSrcGuardFilterMode_Type()
)
cdsIfSrcGuardFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardFilterMode.setStatus("current")
_CdsIfSrcGuardMacAddress_Type = MacAddress
_CdsIfSrcGuardMacAddress_Object = MibTableColumn
cdsIfSrcGuardMacAddress = _CdsIfSrcGuardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 6),
    _CdsIfSrcGuardMacAddress_Type()
)
cdsIfSrcGuardMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardMacAddress.setStatus("current")


class _CdsIfSrcGuardMacFilterAction_Type(Integer32):
    """Custom type cdsIfSrcGuardMacFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowMacAddress", 1),
          ("denyAllMacAddresses", 2),
          ("permitAllMacAddresses", 3))
    )


_CdsIfSrcGuardMacFilterAction_Type.__name__ = "Integer32"
_CdsIfSrcGuardMacFilterAction_Object = MibTableColumn
cdsIfSrcGuardMacFilterAction = _CdsIfSrcGuardMacFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 7),
    _CdsIfSrcGuardMacFilterAction_Type()
)
cdsIfSrcGuardMacFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardMacFilterAction.setStatus("current")


class _CdsIfSrcGuardVlansLow_Type(OctetString):
    """Custom type cdsIfSrcGuardVlansLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CdsIfSrcGuardVlansLow_Type.__name__ = "OctetString"
_CdsIfSrcGuardVlansLow_Object = MibTableColumn
cdsIfSrcGuardVlansLow = _CdsIfSrcGuardVlansLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 8),
    _CdsIfSrcGuardVlansLow_Type()
)
cdsIfSrcGuardVlansLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardVlansLow.setStatus("current")


class _CdsIfSrcGuardVlansHigh_Type(OctetString):
    """Custom type cdsIfSrcGuardVlansHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CdsIfSrcGuardVlansHigh_Type.__name__ = "OctetString"
_CdsIfSrcGuardVlansHigh_Object = MibTableColumn
cdsIfSrcGuardVlansHigh = _CdsIfSrcGuardVlansHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 1, 6, 2, 1, 9),
    _CdsIfSrcGuardVlansHigh_Type()
)
cdsIfSrcGuardVlansHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsIfSrcGuardVlansHigh.setStatus("current")
_CiscoDhcpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDhcpSnoopingMIBConformance = _CiscoDhcpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2)
)
_CdsMIBCompliances_ObjectIdentity = ObjectIdentity
cdsMIBCompliances = _CdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1)
)
_CdsMIBGroups_ObjectIdentity = ObjectIdentity
cdsMIBGroups = _CdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2)
)

# Managed Objects groups

cdsGlobalEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 1)
)
cdsGlobalEnableGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsFeatureEnable")
)
if mibBuilder.loadTexts:
    cdsGlobalEnableGroup.setStatus("current")

cdsDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 2)
)
cdsDatabaseGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsDatabaseFile"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsDatabaseUpdateInterval"))
)
if mibBuilder.loadTexts:
    cdsDatabaseGroup.setStatus("current")

cdsVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 3)
)
cdsVlanConfigGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsVlanDhcpSnoopingEnable")
)
if mibBuilder.loadTexts:
    cdsVlanConfigGroup.setStatus("current")

cdsIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 4)
)
cdsIfConfigGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsIfTrustEnable")
)
if mibBuilder.loadTexts:
    cdsIfConfigGroup.setStatus("current")

cdsIfRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 5)
)
cdsIfRateLimitGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsIfRateLimit")
)
if mibBuilder.loadTexts:
    cdsIfRateLimitGroup.setStatus("current")

cdsBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 6)
)
cdsBindingsGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsAddrType"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsIpAddress"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsInterface"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsLeasedTime"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsStatus"))
)
if mibBuilder.loadTexts:
    cdsBindingsGroup.setStatus("current")

cdsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 7)
)
cdsStatisticsGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsTotalForwardedPkts"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsTotalDroppedPkts"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsUntrustedPortDroppedPkts"))
)
if mibBuilder.loadTexts:
    cdsStatisticsGroup.setStatus("current")

cdsRelayAgentInfoOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 8)
)
cdsRelayAgentInfoOptGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsRelayAgentInfoOptEnable")
)
if mibBuilder.loadTexts:
    cdsRelayAgentInfoOptGroup.setStatus("current")

cdsIfSrcGuardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 9)
)
cdsIfSrcGuardGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardEnable"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardAddrType"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardAddress"))
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardGroup.setStatus("deprecated")

cdsRelayAgentRemoteIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 10)
)
cdsRelayAgentRemoteIdGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsRelayAgentInfoOptRemoteId")
)
if mibBuilder.loadTexts:
    cdsRelayAgentRemoteIdGroup.setStatus("deprecated")

cdsMatchMacAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 11)
)
cdsMatchMacAddressGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsMatchMacAddressEnable")
)
if mibBuilder.loadTexts:
    cdsMatchMacAddressGroup.setStatus("current")

cdsIfFeatureConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 12)
)
cdsIfFeatureConfigGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsIfFeatureEnable")
)
if mibBuilder.loadTexts:
    cdsIfFeatureConfigGroup.setStatus("current")

cdsBindingsLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 13)
)
cdsBindingsLimitGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsGlobalMaxBindingsLimit"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfBindingsLimit"))
)
if mibBuilder.loadTexts:
    cdsBindingsLimitGroup.setStatus("current")

cdsStaticBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 14)
)
cdsStaticBindingsGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsStaticBindingsAddrType"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsStaticBindingsIpAddress"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsStaticBindingsInterface"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsStaticBindingsStatus"))
)
if mibBuilder.loadTexts:
    cdsStaticBindingsGroup.setStatus("current")

cdsIfSrcGuardIpFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 15)
)
cdsIfSrcGuardIpFilterGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardIpFilterAction"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardFilterMode"))
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardIpFilterGroup.setStatus("current")

cdsIfSrcGuardExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 16)
)
cdsIfSrcGuardExtGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardMacAddress"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardMacFilterAction"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardVlansLow"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardVlansHigh"))
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardExtGroup.setStatus("current")

cdsIfSrcGuardTrafficFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 17)
)
cdsIfSrcGuardTrafficFilterGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardFilterType")
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardTrafficFilterGroup.setStatus("current")

cdsIfSrcGuardGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 18)
)
cdsIfSrcGuardGroupRev1.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardAddrType"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfSrcGuardAddress"))
)
if mibBuilder.loadTexts:
    cdsIfSrcGuardGroupRev1.setStatus("current")

cdsBindingsHostnameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 19)
)
cdsBindingsHostnameGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsHostname")
)
if mibBuilder.loadTexts:
    cdsBindingsHostnameGroup.setStatus("current")

cdsRelayAgentInfoOptRemoteIdSubGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 20)
)
cdsRelayAgentInfoOptRemoteIdSubGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsRelayAgentInfoOptRemoteIdSub")
)
if mibBuilder.loadTexts:
    cdsRelayAgentInfoOptRemoteIdSubGroup.setStatus("current")

cdsIfVlanRelayInfoOptCircuitIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 21)
)
cdsIfVlanRelayInfoOptCircuitIdGroup.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsIfVlanRelayInfoOptCircuitId"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsIfVlanRelayInfoOptCircuitIdStatus"))
)
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitIdGroup.setStatus("current")

cdsStatisticsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 22)
)
cdsStatisticsExtGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsForwardedWithoutOption82Pkts")
)
if mibBuilder.loadTexts:
    cdsStatisticsExtGroup.setStatus("current")

cdsNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 23)
)
cdsNotifControlGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsNotifEnabled")
)
if mibBuilder.loadTexts:
    cdsNotifControlGroup.setStatus("current")

cdsIfVlanRelayInfoOptCircuitIdGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 25)
)
cdsIfVlanRelayInfoOptCircuitIdGroupSup1.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsIfVlanRelayInfoOptCircuitIdDirect")
)
if mibBuilder.loadTexts:
    cdsIfVlanRelayInfoOptCircuitIdGroupSup1.setStatus("current")

cdsVlanOperStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 26)
)
cdsVlanOperStatusGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsVlanDhcpSnoopingOperStatus")
)
if mibBuilder.loadTexts:
    cdsVlanOperStatusGroup.setStatus("current")


# Notification objects

cdsBindingsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 0, 1)
)
cdsBindingsNotification.setObjects(
      *(("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsAddrType"),
        ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsIpAddress"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    cdsBindingsNotification.setStatus(
        "current"
    )


# Notifications groups

cdsBindingsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 2, 24)
)
cdsBindingsNotificationGroup.setObjects(
    ("CISCO-DHCP-SNOOPING-MIB", "cdsBindingsNotification")
)
if mibBuilder.loadTexts:
    cdsBindingsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance.setStatus(
        "deprecated"
    )

cdsMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance2.setStatus(
        "deprecated"
    )

cdsMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance3.setStatus(
        "deprecated"
    )

cdsMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance4.setStatus(
        "deprecated"
    )

cdsMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance5.setStatus(
        "deprecated"
    )

cdsMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance6.setStatus(
        "deprecated"
    )

cdsMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 380, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cdsMIBCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DHCP-SNOOPING-MIB",
    **{"ciscoDhcpSnoopingMIB": ciscoDhcpSnoopingMIB,
       "ciscoDhcpSnoopingMIBNotifs": ciscoDhcpSnoopingMIBNotifs,
       "cdsBindingsNotification": cdsBindingsNotification,
       "ciscoDhcpSnoopingMIBObjects": ciscoDhcpSnoopingMIBObjects,
       "cdsGlobal": cdsGlobal,
       "cdsFeatureEnable": cdsFeatureEnable,
       "cdsDatabaseFile": cdsDatabaseFile,
       "cdsDatabaseUpdateInterval": cdsDatabaseUpdateInterval,
       "cdsRelayAgentInfoOptEnable": cdsRelayAgentInfoOptEnable,
       "cdsRelayAgentInfoOptRemoteId": cdsRelayAgentInfoOptRemoteId,
       "cdsMatchMacAddressEnable": cdsMatchMacAddressEnable,
       "cdsGlobalMaxBindingsLimit": cdsGlobalMaxBindingsLimit,
       "cdsRelayAgentInfoOptRemoteIdSub": cdsRelayAgentInfoOptRemoteIdSub,
       "cdsBindingsNotifEnabled": cdsBindingsNotifEnabled,
       "cdsVlan": cdsVlan,
       "cdsVlanConfigTable": cdsVlanConfigTable,
       "cdsVlanConfigEntry": cdsVlanConfigEntry,
       "cdsVlanIndex": cdsVlanIndex,
       "cdsVlanDhcpSnoopingEnable": cdsVlanDhcpSnoopingEnable,
       "cdsVlanDhcpSnoopingOperStatus": cdsVlanDhcpSnoopingOperStatus,
       "cdsInterface": cdsInterface,
       "cdsIfConfigTable": cdsIfConfigTable,
       "cdsIfConfigEntry": cdsIfConfigEntry,
       "cdsIfTrustEnable": cdsIfTrustEnable,
       "cdsIfRateLimitTable": cdsIfRateLimitTable,
       "cdsIfRateLimitEntry": cdsIfRateLimitEntry,
       "cdsIfRateLimit": cdsIfRateLimit,
       "cdsIfFeatureConfigTable": cdsIfFeatureConfigTable,
       "cdsIfFeatureConfigEntry": cdsIfFeatureConfigEntry,
       "cdsIfFeatureEnable": cdsIfFeatureEnable,
       "cdsIfBindingsLimitTable": cdsIfBindingsLimitTable,
       "cdsIfBindingsLimitEntry": cdsIfBindingsLimitEntry,
       "cdsIfBindingsLimit": cdsIfBindingsLimit,
       "cdsIfVlanRelayInfoOptCircuitIdTable": cdsIfVlanRelayInfoOptCircuitIdTable,
       "cdsIfVlanRelayInfoOptCircuitIdEntry": cdsIfVlanRelayInfoOptCircuitIdEntry,
       "cdsIfVlan": cdsIfVlan,
       "cdsIfVlanRelayInfoOptCircuitId": cdsIfVlanRelayInfoOptCircuitId,
       "cdsIfVlanRelayInfoOptCircuitIdStatus": cdsIfVlanRelayInfoOptCircuitIdStatus,
       "cdsIfVlanRelayInfoOptCircuitIdDirect": cdsIfVlanRelayInfoOptCircuitIdDirect,
       "cdsBindings": cdsBindings,
       "cdsBindingsTable": cdsBindingsTable,
       "cdsBindingsEntry": cdsBindingsEntry,
       "cdsBindingsVlan": cdsBindingsVlan,
       "cdsBindingsMacAddress": cdsBindingsMacAddress,
       "cdsBindingsAddrType": cdsBindingsAddrType,
       "cdsBindingsIpAddress": cdsBindingsIpAddress,
       "cdsBindingsInterface": cdsBindingsInterface,
       "cdsBindingsLeasedTime": cdsBindingsLeasedTime,
       "cdsBindingsStatus": cdsBindingsStatus,
       "cdsBindingsHostname": cdsBindingsHostname,
       "cdsStaticBindingsTable": cdsStaticBindingsTable,
       "cdsStaticBindingsEntry": cdsStaticBindingsEntry,
       "cdsStaticBindingsVlan": cdsStaticBindingsVlan,
       "cdsStaticBindingsMacAddress": cdsStaticBindingsMacAddress,
       "cdsStaticBindingsAddrType": cdsStaticBindingsAddrType,
       "cdsStaticBindingsIpAddress": cdsStaticBindingsIpAddress,
       "cdsStaticBindingsInterface": cdsStaticBindingsInterface,
       "cdsStaticBindingsStatus": cdsStaticBindingsStatus,
       "cdsStatistics": cdsStatistics,
       "cdsTotalForwardedPkts": cdsTotalForwardedPkts,
       "cdsTotalDroppedPkts": cdsTotalDroppedPkts,
       "cdsUntrustedPortDroppedPkts": cdsUntrustedPortDroppedPkts,
       "cdsForwardedWithoutOption82Pkts": cdsForwardedWithoutOption82Pkts,
       "cdsSrcGuard": cdsSrcGuard,
       "cdsIfSrcGuardConfigTable": cdsIfSrcGuardConfigTable,
       "cdsIfSrcGuardConfigEntry": cdsIfSrcGuardConfigEntry,
       "cdsIfSrcGuardEnable": cdsIfSrcGuardEnable,
       "cdsIfSrcGuardFilterType": cdsIfSrcGuardFilterType,
       "cdsIfSrcGuardAddrTable": cdsIfSrcGuardAddrTable,
       "cdsIfSrcGuardAddrEntry": cdsIfSrcGuardAddrEntry,
       "cdsIfSrcGuardIndex": cdsIfSrcGuardIndex,
       "cdsIfSrcGuardAddrType": cdsIfSrcGuardAddrType,
       "cdsIfSrcGuardAddress": cdsIfSrcGuardAddress,
       "cdsIfSrcGuardIpFilterAction": cdsIfSrcGuardIpFilterAction,
       "cdsIfSrcGuardFilterMode": cdsIfSrcGuardFilterMode,
       "cdsIfSrcGuardMacAddress": cdsIfSrcGuardMacAddress,
       "cdsIfSrcGuardMacFilterAction": cdsIfSrcGuardMacFilterAction,
       "cdsIfSrcGuardVlansLow": cdsIfSrcGuardVlansLow,
       "cdsIfSrcGuardVlansHigh": cdsIfSrcGuardVlansHigh,
       "ciscoDhcpSnoopingMIBConformance": ciscoDhcpSnoopingMIBConformance,
       "cdsMIBCompliances": cdsMIBCompliances,
       "cdsMIBCompliance": cdsMIBCompliance,
       "cdsMIBCompliance2": cdsMIBCompliance2,
       "cdsMIBCompliance3": cdsMIBCompliance3,
       "cdsMIBCompliance4": cdsMIBCompliance4,
       "cdsMIBCompliance5": cdsMIBCompliance5,
       "cdsMIBCompliance6": cdsMIBCompliance6,
       "cdsMIBCompliance7": cdsMIBCompliance7,
       "cdsMIBGroups": cdsMIBGroups,
       "cdsGlobalEnableGroup": cdsGlobalEnableGroup,
       "cdsDatabaseGroup": cdsDatabaseGroup,
       "cdsVlanConfigGroup": cdsVlanConfigGroup,
       "cdsIfConfigGroup": cdsIfConfigGroup,
       "cdsIfRateLimitGroup": cdsIfRateLimitGroup,
       "cdsBindingsGroup": cdsBindingsGroup,
       "cdsStatisticsGroup": cdsStatisticsGroup,
       "cdsRelayAgentInfoOptGroup": cdsRelayAgentInfoOptGroup,
       "cdsIfSrcGuardGroup": cdsIfSrcGuardGroup,
       "cdsRelayAgentRemoteIdGroup": cdsRelayAgentRemoteIdGroup,
       "cdsMatchMacAddressGroup": cdsMatchMacAddressGroup,
       "cdsIfFeatureConfigGroup": cdsIfFeatureConfigGroup,
       "cdsBindingsLimitGroup": cdsBindingsLimitGroup,
       "cdsStaticBindingsGroup": cdsStaticBindingsGroup,
       "cdsIfSrcGuardIpFilterGroup": cdsIfSrcGuardIpFilterGroup,
       "cdsIfSrcGuardExtGroup": cdsIfSrcGuardExtGroup,
       "cdsIfSrcGuardTrafficFilterGroup": cdsIfSrcGuardTrafficFilterGroup,
       "cdsIfSrcGuardGroupRev1": cdsIfSrcGuardGroupRev1,
       "cdsBindingsHostnameGroup": cdsBindingsHostnameGroup,
       "cdsRelayAgentInfoOptRemoteIdSubGroup": cdsRelayAgentInfoOptRemoteIdSubGroup,
       "cdsIfVlanRelayInfoOptCircuitIdGroup": cdsIfVlanRelayInfoOptCircuitIdGroup,
       "cdsStatisticsExtGroup": cdsStatisticsExtGroup,
       "cdsNotifControlGroup": cdsNotifControlGroup,
       "cdsBindingsNotificationGroup": cdsBindingsNotificationGroup,
       "cdsIfVlanRelayInfoOptCircuitIdGroupSup1": cdsIfVlanRelayInfoOptCircuitIdGroupSup1,
       "cdsVlanOperStatusGroup": cdsVlanOperStatusGroup}
)
