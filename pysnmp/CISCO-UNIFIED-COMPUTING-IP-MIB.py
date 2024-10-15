# SNMP MIB module (CISCO-UNIFIED-COMPUTING-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:44 2024
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

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsIpIPv4DnsPref,
 CucsIpIpV4StaticAddrPref,
 CucsIpServiceIfPref) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsIpIPv4DnsPref",
    "CucsIpIpV4StaticAddrPref",
    "CucsIpServiceIfPref")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsIpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsIpIPv4DnsTable_Object = MibTable
cucsIpIPv4DnsTable = _CucsIpIPv4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1)
)
if mibBuilder.loadTexts:
    cucsIpIPv4DnsTable.setStatus("current")
_CucsIpIPv4DnsEntry_Object = MibTableRow
cucsIpIPv4DnsEntry = _CucsIpIPv4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1)
)
cucsIpIPv4DnsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IP-MIB", "cucsIpIPv4DnsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIpIPv4DnsEntry.setStatus("current")
_CucsIpIPv4DnsInstanceId_Type = CucsManagedObjectId
_CucsIpIPv4DnsInstanceId_Object = MibTableColumn
cucsIpIPv4DnsInstanceId = _CucsIpIPv4DnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 1),
    _CucsIpIPv4DnsInstanceId_Type()
)
cucsIpIPv4DnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsInstanceId.setStatus("current")
_CucsIpIPv4DnsDn_Type = CucsManagedObjectDn
_CucsIpIPv4DnsDn_Object = MibTableColumn
cucsIpIPv4DnsDn = _CucsIpIPv4DnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 2),
    _CucsIpIPv4DnsDn_Type()
)
cucsIpIPv4DnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsDn.setStatus("current")
_CucsIpIPv4DnsRn_Type = SnmpAdminString
_CucsIpIPv4DnsRn_Object = MibTableColumn
cucsIpIPv4DnsRn = _CucsIpIPv4DnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 3),
    _CucsIpIPv4DnsRn_Type()
)
cucsIpIPv4DnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsRn.setStatus("current")
_CucsIpIPv4DnsAddr_Type = InetAddressIPv4
_CucsIpIPv4DnsAddr_Object = MibTableColumn
cucsIpIPv4DnsAddr = _CucsIpIPv4DnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 4),
    _CucsIpIPv4DnsAddr_Type()
)
cucsIpIPv4DnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsAddr.setStatus("current")
_CucsIpIPv4DnsDefGw_Type = InetAddressIPv4
_CucsIpIPv4DnsDefGw_Object = MibTableColumn
cucsIpIPv4DnsDefGw = _CucsIpIPv4DnsDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 5),
    _CucsIpIPv4DnsDefGw_Type()
)
cucsIpIPv4DnsDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsDefGw.setStatus("current")
_CucsIpIPv4DnsPref_Type = CucsIpIPv4DnsPref
_CucsIpIPv4DnsPref_Object = MibTableColumn
cucsIpIPv4DnsPref = _CucsIpIPv4DnsPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 6),
    _CucsIpIPv4DnsPref_Type()
)
cucsIpIPv4DnsPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsPref.setStatus("current")
_CucsIpIPv4DnsSubnet_Type = InetAddressIPv4
_CucsIpIPv4DnsSubnet_Object = MibTableColumn
cucsIpIPv4DnsSubnet = _CucsIpIPv4DnsSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 1, 1, 7),
    _CucsIpIPv4DnsSubnet_Type()
)
cucsIpIPv4DnsSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4DnsSubnet.setStatus("current")
_CucsIpIpV4StaticAddrTable_Object = MibTable
cucsIpIpV4StaticAddrTable = _CucsIpIpV4StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2)
)
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrTable.setStatus("current")
_CucsIpIpV4StaticAddrEntry_Object = MibTableRow
cucsIpIpV4StaticAddrEntry = _CucsIpIpV4StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1)
)
cucsIpIpV4StaticAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IP-MIB", "cucsIpIpV4StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrEntry.setStatus("current")
_CucsIpIpV4StaticAddrInstanceId_Type = CucsManagedObjectId
_CucsIpIpV4StaticAddrInstanceId_Object = MibTableColumn
cucsIpIpV4StaticAddrInstanceId = _CucsIpIpV4StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 1),
    _CucsIpIpV4StaticAddrInstanceId_Type()
)
cucsIpIpV4StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrInstanceId.setStatus("current")
_CucsIpIpV4StaticAddrDn_Type = CucsManagedObjectDn
_CucsIpIpV4StaticAddrDn_Object = MibTableColumn
cucsIpIpV4StaticAddrDn = _CucsIpIpV4StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 2),
    _CucsIpIpV4StaticAddrDn_Type()
)
cucsIpIpV4StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrDn.setStatus("current")
_CucsIpIpV4StaticAddrRn_Type = SnmpAdminString
_CucsIpIpV4StaticAddrRn_Object = MibTableColumn
cucsIpIpV4StaticAddrRn = _CucsIpIpV4StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 3),
    _CucsIpIpV4StaticAddrRn_Type()
)
cucsIpIpV4StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrRn.setStatus("current")
_CucsIpIpV4StaticAddrAddr_Type = InetAddressIPv4
_CucsIpIpV4StaticAddrAddr_Object = MibTableColumn
cucsIpIpV4StaticAddrAddr = _CucsIpIpV4StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 4),
    _CucsIpIpV4StaticAddrAddr_Type()
)
cucsIpIpV4StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrAddr.setStatus("current")
_CucsIpIpV4StaticAddrDefGw_Type = InetAddressIPv4
_CucsIpIpV4StaticAddrDefGw_Object = MibTableColumn
cucsIpIpV4StaticAddrDefGw = _CucsIpIpV4StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 5),
    _CucsIpIpV4StaticAddrDefGw_Type()
)
cucsIpIpV4StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrDefGw.setStatus("current")
_CucsIpIpV4StaticAddrPref_Type = CucsIpIpV4StaticAddrPref
_CucsIpIpV4StaticAddrPref_Object = MibTableColumn
cucsIpIpV4StaticAddrPref = _CucsIpIpV4StaticAddrPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 6),
    _CucsIpIpV4StaticAddrPref_Type()
)
cucsIpIpV4StaticAddrPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrPref.setStatus("current")
_CucsIpIpV4StaticAddrSubnet_Type = InetAddressIPv4
_CucsIpIpV4StaticAddrSubnet_Object = MibTableColumn
cucsIpIpV4StaticAddrSubnet = _CucsIpIpV4StaticAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 2, 1, 7),
    _CucsIpIpV4StaticAddrSubnet_Type()
)
cucsIpIpV4StaticAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticAddrSubnet.setStatus("current")
_CucsIpServiceIfTable_Object = MibTable
cucsIpServiceIfTable = _CucsIpServiceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3)
)
if mibBuilder.loadTexts:
    cucsIpServiceIfTable.setStatus("current")
_CucsIpServiceIfEntry_Object = MibTableRow
cucsIpServiceIfEntry = _CucsIpServiceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1)
)
cucsIpServiceIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IP-MIB", "cucsIpServiceIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIpServiceIfEntry.setStatus("current")
_CucsIpServiceIfInstanceId_Type = CucsManagedObjectId
_CucsIpServiceIfInstanceId_Object = MibTableColumn
cucsIpServiceIfInstanceId = _CucsIpServiceIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 1),
    _CucsIpServiceIfInstanceId_Type()
)
cucsIpServiceIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIpServiceIfInstanceId.setStatus("current")
_CucsIpServiceIfDn_Type = CucsManagedObjectDn
_CucsIpServiceIfDn_Object = MibTableColumn
cucsIpServiceIfDn = _CucsIpServiceIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 2),
    _CucsIpServiceIfDn_Type()
)
cucsIpServiceIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfDn.setStatus("current")
_CucsIpServiceIfRn_Type = SnmpAdminString
_CucsIpServiceIfRn_Object = MibTableColumn
cucsIpServiceIfRn = _CucsIpServiceIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 3),
    _CucsIpServiceIfRn_Type()
)
cucsIpServiceIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfRn.setStatus("current")
_CucsIpServiceIfAddr_Type = InetAddressIPv4
_CucsIpServiceIfAddr_Object = MibTableColumn
cucsIpServiceIfAddr = _CucsIpServiceIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 4),
    _CucsIpServiceIfAddr_Type()
)
cucsIpServiceIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfAddr.setStatus("current")
_CucsIpServiceIfDefGw_Type = InetAddressIPv4
_CucsIpServiceIfDefGw_Object = MibTableColumn
cucsIpServiceIfDefGw = _CucsIpServiceIfDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 5),
    _CucsIpServiceIfDefGw_Type()
)
cucsIpServiceIfDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfDefGw.setStatus("current")
_CucsIpServiceIfPort_Type = Gauge32
_CucsIpServiceIfPort_Object = MibTableColumn
cucsIpServiceIfPort = _CucsIpServiceIfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 6),
    _CucsIpServiceIfPort_Type()
)
cucsIpServiceIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfPort.setStatus("current")
_CucsIpServiceIfPref_Type = CucsIpServiceIfPref
_CucsIpServiceIfPref_Object = MibTableColumn
cucsIpServiceIfPref = _CucsIpServiceIfPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 7),
    _CucsIpServiceIfPref_Type()
)
cucsIpServiceIfPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfPref.setStatus("current")
_CucsIpServiceIfSubnet_Type = InetAddressIPv4
_CucsIpServiceIfSubnet_Object = MibTableColumn
cucsIpServiceIfSubnet = _CucsIpServiceIfSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 3, 1, 8),
    _CucsIpServiceIfSubnet_Type()
)
cucsIpServiceIfSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpServiceIfSubnet.setStatus("current")
_CucsIpDnsSuffixTable_Object = MibTable
cucsIpDnsSuffixTable = _CucsIpDnsSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4)
)
if mibBuilder.loadTexts:
    cucsIpDnsSuffixTable.setStatus("current")
_CucsIpDnsSuffixEntry_Object = MibTableRow
cucsIpDnsSuffixEntry = _CucsIpDnsSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1)
)
cucsIpDnsSuffixEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IP-MIB", "cucsIpDnsSuffixInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIpDnsSuffixEntry.setStatus("current")
_CucsIpDnsSuffixInstanceId_Type = CucsManagedObjectId
_CucsIpDnsSuffixInstanceId_Object = MibTableColumn
cucsIpDnsSuffixInstanceId = _CucsIpDnsSuffixInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1, 1),
    _CucsIpDnsSuffixInstanceId_Type()
)
cucsIpDnsSuffixInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIpDnsSuffixInstanceId.setStatus("current")
_CucsIpDnsSuffixDn_Type = CucsManagedObjectDn
_CucsIpDnsSuffixDn_Object = MibTableColumn
cucsIpDnsSuffixDn = _CucsIpDnsSuffixDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1, 2),
    _CucsIpDnsSuffixDn_Type()
)
cucsIpDnsSuffixDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpDnsSuffixDn.setStatus("current")
_CucsIpDnsSuffixRn_Type = SnmpAdminString
_CucsIpDnsSuffixRn_Object = MibTableColumn
cucsIpDnsSuffixRn = _CucsIpDnsSuffixRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1, 3),
    _CucsIpDnsSuffixRn_Type()
)
cucsIpDnsSuffixRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpDnsSuffixRn.setStatus("current")
_CucsIpDnsSuffixGuid_Type = SnmpAdminString
_CucsIpDnsSuffixGuid_Object = MibTableColumn
cucsIpDnsSuffixGuid = _CucsIpDnsSuffixGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1, 4),
    _CucsIpDnsSuffixGuid_Type()
)
cucsIpDnsSuffixGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpDnsSuffixGuid.setStatus("current")
_CucsIpDnsSuffixHost_Type = SnmpAdminString
_CucsIpDnsSuffixHost_Object = MibTableColumn
cucsIpDnsSuffixHost = _CucsIpDnsSuffixHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1, 5),
    _CucsIpDnsSuffixHost_Type()
)
cucsIpDnsSuffixHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpDnsSuffixHost.setStatus("current")
_CucsIpDnsSuffixName_Type = SnmpAdminString
_CucsIpDnsSuffixName_Object = MibTableColumn
cucsIpDnsSuffixName = _CucsIpDnsSuffixName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 4, 1, 6),
    _CucsIpDnsSuffixName_Type()
)
cucsIpDnsSuffixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpDnsSuffixName.setStatus("current")
_CucsIpIPv4WinsServerTable_Object = MibTable
cucsIpIPv4WinsServerTable = _CucsIpIPv4WinsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5)
)
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerTable.setStatus("current")
_CucsIpIPv4WinsServerEntry_Object = MibTableRow
cucsIpIPv4WinsServerEntry = _CucsIpIPv4WinsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1)
)
cucsIpIPv4WinsServerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IP-MIB", "cucsIpIPv4WinsServerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerEntry.setStatus("current")
_CucsIpIPv4WinsServerInstanceId_Type = CucsManagedObjectId
_CucsIpIPv4WinsServerInstanceId_Object = MibTableColumn
cucsIpIPv4WinsServerInstanceId = _CucsIpIPv4WinsServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 1),
    _CucsIpIPv4WinsServerInstanceId_Type()
)
cucsIpIPv4WinsServerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerInstanceId.setStatus("current")
_CucsIpIPv4WinsServerDn_Type = CucsManagedObjectDn
_CucsIpIPv4WinsServerDn_Object = MibTableColumn
cucsIpIPv4WinsServerDn = _CucsIpIPv4WinsServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 2),
    _CucsIpIPv4WinsServerDn_Type()
)
cucsIpIPv4WinsServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerDn.setStatus("current")
_CucsIpIPv4WinsServerRn_Type = SnmpAdminString
_CucsIpIPv4WinsServerRn_Object = MibTableColumn
cucsIpIPv4WinsServerRn = _CucsIpIPv4WinsServerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 3),
    _CucsIpIPv4WinsServerRn_Type()
)
cucsIpIPv4WinsServerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerRn.setStatus("current")
_CucsIpIPv4WinsServerIPv4Address_Type = InetAddressIPv4
_CucsIpIPv4WinsServerIPv4Address_Object = MibTableColumn
cucsIpIPv4WinsServerIPv4Address = _CucsIpIPv4WinsServerIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 4),
    _CucsIpIPv4WinsServerIPv4Address_Type()
)
cucsIpIPv4WinsServerIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerIPv4Address.setStatus("current")
_CucsIpIPv4WinsServerGuid_Type = SnmpAdminString
_CucsIpIPv4WinsServerGuid_Object = MibTableColumn
cucsIpIPv4WinsServerGuid = _CucsIpIPv4WinsServerGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 5),
    _CucsIpIPv4WinsServerGuid_Type()
)
cucsIpIPv4WinsServerGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerGuid.setStatus("current")
_CucsIpIPv4WinsServerHost_Type = SnmpAdminString
_CucsIpIPv4WinsServerHost_Object = MibTableColumn
cucsIpIPv4WinsServerHost = _CucsIpIPv4WinsServerHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 6),
    _CucsIpIPv4WinsServerHost_Type()
)
cucsIpIPv4WinsServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerHost.setStatus("current")
_CucsIpIPv4WinsServerName_Type = SnmpAdminString
_CucsIpIPv4WinsServerName_Object = MibTableColumn
cucsIpIPv4WinsServerName = _CucsIpIPv4WinsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 5, 1, 7),
    _CucsIpIPv4WinsServerName_Type()
)
cucsIpIPv4WinsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIPv4WinsServerName.setStatus("current")
_CucsIpIpV4StaticTargetAddrTable_Object = MibTable
cucsIpIpV4StaticTargetAddrTable = _CucsIpIpV4StaticTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6)
)
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrTable.setStatus("current")
_CucsIpIpV4StaticTargetAddrEntry_Object = MibTableRow
cucsIpIpV4StaticTargetAddrEntry = _CucsIpIpV4StaticTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1)
)
cucsIpIpV4StaticTargetAddrEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IP-MIB", "cucsIpIpV4StaticTargetAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrEntry.setStatus("current")
_CucsIpIpV4StaticTargetAddrInstanceId_Type = CucsManagedObjectId
_CucsIpIpV4StaticTargetAddrInstanceId_Object = MibTableColumn
cucsIpIpV4StaticTargetAddrInstanceId = _CucsIpIpV4StaticTargetAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1, 1),
    _CucsIpIpV4StaticTargetAddrInstanceId_Type()
)
cucsIpIpV4StaticTargetAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrInstanceId.setStatus("current")
_CucsIpIpV4StaticTargetAddrDn_Type = CucsManagedObjectDn
_CucsIpIpV4StaticTargetAddrDn_Object = MibTableColumn
cucsIpIpV4StaticTargetAddrDn = _CucsIpIpV4StaticTargetAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1, 2),
    _CucsIpIpV4StaticTargetAddrDn_Type()
)
cucsIpIpV4StaticTargetAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrDn.setStatus("current")
_CucsIpIpV4StaticTargetAddrRn_Type = SnmpAdminString
_CucsIpIpV4StaticTargetAddrRn_Object = MibTableColumn
cucsIpIpV4StaticTargetAddrRn = _CucsIpIpV4StaticTargetAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1, 3),
    _CucsIpIpV4StaticTargetAddrRn_Type()
)
cucsIpIpV4StaticTargetAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrRn.setStatus("current")
_CucsIpIpV4StaticTargetAddrAddr_Type = InetAddressIPv4
_CucsIpIpV4StaticTargetAddrAddr_Object = MibTableColumn
cucsIpIpV4StaticTargetAddrAddr = _CucsIpIpV4StaticTargetAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1, 4),
    _CucsIpIpV4StaticTargetAddrAddr_Type()
)
cucsIpIpV4StaticTargetAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrAddr.setStatus("current")
_CucsIpIpV4StaticTargetAddrDefGw_Type = InetAddressIPv4
_CucsIpIpV4StaticTargetAddrDefGw_Object = MibTableColumn
cucsIpIpV4StaticTargetAddrDefGw = _CucsIpIpV4StaticTargetAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1, 5),
    _CucsIpIpV4StaticTargetAddrDefGw_Type()
)
cucsIpIpV4StaticTargetAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrDefGw.setStatus("current")
_CucsIpIpV4StaticTargetAddrSubnet_Type = InetAddressIPv4
_CucsIpIpV4StaticTargetAddrSubnet_Object = MibTableColumn
cucsIpIpV4StaticTargetAddrSubnet = _CucsIpIpV4StaticTargetAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 66, 6, 1, 6),
    _CucsIpIpV4StaticTargetAddrSubnet_Type()
)
cucsIpIpV4StaticTargetAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIpIpV4StaticTargetAddrSubnet.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-IP-MIB",
    **{"cucsIpObjects": cucsIpObjects,
       "cucsIpIPv4DnsTable": cucsIpIPv4DnsTable,
       "cucsIpIPv4DnsEntry": cucsIpIPv4DnsEntry,
       "cucsIpIPv4DnsInstanceId": cucsIpIPv4DnsInstanceId,
       "cucsIpIPv4DnsDn": cucsIpIPv4DnsDn,
       "cucsIpIPv4DnsRn": cucsIpIPv4DnsRn,
       "cucsIpIPv4DnsAddr": cucsIpIPv4DnsAddr,
       "cucsIpIPv4DnsDefGw": cucsIpIPv4DnsDefGw,
       "cucsIpIPv4DnsPref": cucsIpIPv4DnsPref,
       "cucsIpIPv4DnsSubnet": cucsIpIPv4DnsSubnet,
       "cucsIpIpV4StaticAddrTable": cucsIpIpV4StaticAddrTable,
       "cucsIpIpV4StaticAddrEntry": cucsIpIpV4StaticAddrEntry,
       "cucsIpIpV4StaticAddrInstanceId": cucsIpIpV4StaticAddrInstanceId,
       "cucsIpIpV4StaticAddrDn": cucsIpIpV4StaticAddrDn,
       "cucsIpIpV4StaticAddrRn": cucsIpIpV4StaticAddrRn,
       "cucsIpIpV4StaticAddrAddr": cucsIpIpV4StaticAddrAddr,
       "cucsIpIpV4StaticAddrDefGw": cucsIpIpV4StaticAddrDefGw,
       "cucsIpIpV4StaticAddrPref": cucsIpIpV4StaticAddrPref,
       "cucsIpIpV4StaticAddrSubnet": cucsIpIpV4StaticAddrSubnet,
       "cucsIpServiceIfTable": cucsIpServiceIfTable,
       "cucsIpServiceIfEntry": cucsIpServiceIfEntry,
       "cucsIpServiceIfInstanceId": cucsIpServiceIfInstanceId,
       "cucsIpServiceIfDn": cucsIpServiceIfDn,
       "cucsIpServiceIfRn": cucsIpServiceIfRn,
       "cucsIpServiceIfAddr": cucsIpServiceIfAddr,
       "cucsIpServiceIfDefGw": cucsIpServiceIfDefGw,
       "cucsIpServiceIfPort": cucsIpServiceIfPort,
       "cucsIpServiceIfPref": cucsIpServiceIfPref,
       "cucsIpServiceIfSubnet": cucsIpServiceIfSubnet,
       "cucsIpDnsSuffixTable": cucsIpDnsSuffixTable,
       "cucsIpDnsSuffixEntry": cucsIpDnsSuffixEntry,
       "cucsIpDnsSuffixInstanceId": cucsIpDnsSuffixInstanceId,
       "cucsIpDnsSuffixDn": cucsIpDnsSuffixDn,
       "cucsIpDnsSuffixRn": cucsIpDnsSuffixRn,
       "cucsIpDnsSuffixGuid": cucsIpDnsSuffixGuid,
       "cucsIpDnsSuffixHost": cucsIpDnsSuffixHost,
       "cucsIpDnsSuffixName": cucsIpDnsSuffixName,
       "cucsIpIPv4WinsServerTable": cucsIpIPv4WinsServerTable,
       "cucsIpIPv4WinsServerEntry": cucsIpIPv4WinsServerEntry,
       "cucsIpIPv4WinsServerInstanceId": cucsIpIPv4WinsServerInstanceId,
       "cucsIpIPv4WinsServerDn": cucsIpIPv4WinsServerDn,
       "cucsIpIPv4WinsServerRn": cucsIpIPv4WinsServerRn,
       "cucsIpIPv4WinsServerIPv4Address": cucsIpIPv4WinsServerIPv4Address,
       "cucsIpIPv4WinsServerGuid": cucsIpIPv4WinsServerGuid,
       "cucsIpIPv4WinsServerHost": cucsIpIPv4WinsServerHost,
       "cucsIpIPv4WinsServerName": cucsIpIPv4WinsServerName,
       "cucsIpIpV4StaticTargetAddrTable": cucsIpIpV4StaticTargetAddrTable,
       "cucsIpIpV4StaticTargetAddrEntry": cucsIpIpV4StaticTargetAddrEntry,
       "cucsIpIpV4StaticTargetAddrInstanceId": cucsIpIpV4StaticTargetAddrInstanceId,
       "cucsIpIpV4StaticTargetAddrDn": cucsIpIpV4StaticTargetAddrDn,
       "cucsIpIpV4StaticTargetAddrRn": cucsIpIpV4StaticTargetAddrRn,
       "cucsIpIpV4StaticTargetAddrAddr": cucsIpIpV4StaticTargetAddrAddr,
       "cucsIpIpV4StaticTargetAddrDefGw": cucsIpIpV4StaticTargetAddrDefGw,
       "cucsIpIpV4StaticTargetAddrSubnet": cucsIpIpV4StaticTargetAddrSubnet}
)
