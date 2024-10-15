# SNMP MIB module (CISCO-UNIFIED-COMPUTING-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:14 2024
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

cucsDhcpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsDhcpAcquiredTable_Object = MibTable
cucsDhcpAcquiredTable = _CucsDhcpAcquiredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cucsDhcpAcquiredTable.setStatus("current")
_CucsDhcpAcquiredEntry_Object = MibTableRow
cucsDhcpAcquiredEntry = _CucsDhcpAcquiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1)
)
cucsDhcpAcquiredEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DHCP-MIB", "cucsDhcpAcquiredInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDhcpAcquiredEntry.setStatus("current")
_CucsDhcpAcquiredInstanceId_Type = CucsManagedObjectId
_CucsDhcpAcquiredInstanceId_Object = MibTableColumn
cucsDhcpAcquiredInstanceId = _CucsDhcpAcquiredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 1),
    _CucsDhcpAcquiredInstanceId_Type()
)
cucsDhcpAcquiredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredInstanceId.setStatus("current")
_CucsDhcpAcquiredDn_Type = CucsManagedObjectDn
_CucsDhcpAcquiredDn_Object = MibTableColumn
cucsDhcpAcquiredDn = _CucsDhcpAcquiredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 2),
    _CucsDhcpAcquiredDn_Type()
)
cucsDhcpAcquiredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredDn.setStatus("current")
_CucsDhcpAcquiredRn_Type = SnmpAdminString
_CucsDhcpAcquiredRn_Object = MibTableColumn
cucsDhcpAcquiredRn = _CucsDhcpAcquiredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 3),
    _CucsDhcpAcquiredRn_Type()
)
cucsDhcpAcquiredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredRn.setStatus("current")
_CucsDhcpAcquiredAcqts_Type = DateAndTime
_CucsDhcpAcquiredAcqts_Object = MibTableColumn
cucsDhcpAcquiredAcqts = _CucsDhcpAcquiredAcqts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 4),
    _CucsDhcpAcquiredAcqts_Type()
)
cucsDhcpAcquiredAcqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredAcqts.setStatus("current")
_CucsDhcpAcquiredCookie_Type = SnmpAdminString
_CucsDhcpAcquiredCookie_Object = MibTableColumn
cucsDhcpAcquiredCookie = _CucsDhcpAcquiredCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 5),
    _CucsDhcpAcquiredCookie_Type()
)
cucsDhcpAcquiredCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredCookie.setStatus("current")
_CucsDhcpAcquiredEnds_Type = DateAndTime
_CucsDhcpAcquiredEnds_Object = MibTableColumn
cucsDhcpAcquiredEnds = _CucsDhcpAcquiredEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 6),
    _CucsDhcpAcquiredEnds_Type()
)
cucsDhcpAcquiredEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredEnds.setStatus("current")
_CucsDhcpAcquiredIp_Type = InetAddressIPv4
_CucsDhcpAcquiredIp_Object = MibTableColumn
cucsDhcpAcquiredIp = _CucsDhcpAcquiredIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 7),
    _CucsDhcpAcquiredIp_Type()
)
cucsDhcpAcquiredIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredIp.setStatus("current")
_CucsDhcpAcquiredSysId_Type = SnmpAdminString
_CucsDhcpAcquiredSysId_Object = MibTableColumn
cucsDhcpAcquiredSysId = _CucsDhcpAcquiredSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 8),
    _CucsDhcpAcquiredSysId_Type()
)
cucsDhcpAcquiredSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredSysId.setStatus("current")
_CucsDhcpAcquiredMac_Type = MacAddress
_CucsDhcpAcquiredMac_Object = MibTableColumn
cucsDhcpAcquiredMac = _CucsDhcpAcquiredMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 1, 1, 9),
    _CucsDhcpAcquiredMac_Type()
)
cucsDhcpAcquiredMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpAcquiredMac.setStatus("current")
_CucsDhcpInstTable_Object = MibTable
cucsDhcpInstTable = _CucsDhcpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 2)
)
if mibBuilder.loadTexts:
    cucsDhcpInstTable.setStatus("current")
_CucsDhcpInstEntry_Object = MibTableRow
cucsDhcpInstEntry = _CucsDhcpInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 2, 1)
)
cucsDhcpInstEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DHCP-MIB", "cucsDhcpInstInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDhcpInstEntry.setStatus("current")
_CucsDhcpInstInstanceId_Type = CucsManagedObjectId
_CucsDhcpInstInstanceId_Object = MibTableColumn
cucsDhcpInstInstanceId = _CucsDhcpInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 2, 1, 1),
    _CucsDhcpInstInstanceId_Type()
)
cucsDhcpInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDhcpInstInstanceId.setStatus("current")
_CucsDhcpInstDn_Type = CucsManagedObjectDn
_CucsDhcpInstDn_Object = MibTableColumn
cucsDhcpInstDn = _CucsDhcpInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 2, 1, 2),
    _CucsDhcpInstDn_Type()
)
cucsDhcpInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpInstDn.setStatus("current")
_CucsDhcpInstRn_Type = SnmpAdminString
_CucsDhcpInstRn_Object = MibTableColumn
cucsDhcpInstRn = _CucsDhcpInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 2, 1, 3),
    _CucsDhcpInstRn_Type()
)
cucsDhcpInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpInstRn.setStatus("current")
_CucsDhcpLeaseTable_Object = MibTable
cucsDhcpLeaseTable = _CucsDhcpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3)
)
if mibBuilder.loadTexts:
    cucsDhcpLeaseTable.setStatus("current")
_CucsDhcpLeaseEntry_Object = MibTableRow
cucsDhcpLeaseEntry = _CucsDhcpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1)
)
cucsDhcpLeaseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DHCP-MIB", "cucsDhcpLeaseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDhcpLeaseEntry.setStatus("current")
_CucsDhcpLeaseInstanceId_Type = CucsManagedObjectId
_CucsDhcpLeaseInstanceId_Object = MibTableColumn
cucsDhcpLeaseInstanceId = _CucsDhcpLeaseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 1),
    _CucsDhcpLeaseInstanceId_Type()
)
cucsDhcpLeaseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDhcpLeaseInstanceId.setStatus("current")
_CucsDhcpLeaseDn_Type = CucsManagedObjectDn
_CucsDhcpLeaseDn_Object = MibTableColumn
cucsDhcpLeaseDn = _CucsDhcpLeaseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 2),
    _CucsDhcpLeaseDn_Type()
)
cucsDhcpLeaseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseDn.setStatus("current")
_CucsDhcpLeaseRn_Type = SnmpAdminString
_CucsDhcpLeaseRn_Object = MibTableColumn
cucsDhcpLeaseRn = _CucsDhcpLeaseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 3),
    _CucsDhcpLeaseRn_Type()
)
cucsDhcpLeaseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseRn.setStatus("current")
_CucsDhcpLeaseCliId_Type = SnmpAdminString
_CucsDhcpLeaseCliId_Object = MibTableColumn
cucsDhcpLeaseCliId = _CucsDhcpLeaseCliId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 4),
    _CucsDhcpLeaseCliId_Type()
)
cucsDhcpLeaseCliId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseCliId.setStatus("current")
_CucsDhcpLeaseCookie_Type = SnmpAdminString
_CucsDhcpLeaseCookie_Object = MibTableColumn
cucsDhcpLeaseCookie = _CucsDhcpLeaseCookie_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 5),
    _CucsDhcpLeaseCookie_Type()
)
cucsDhcpLeaseCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseCookie.setStatus("current")
_CucsDhcpLeaseEnds_Type = DateAndTime
_CucsDhcpLeaseEnds_Object = MibTableColumn
cucsDhcpLeaseEnds = _CucsDhcpLeaseEnds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 6),
    _CucsDhcpLeaseEnds_Type()
)
cucsDhcpLeaseEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseEnds.setStatus("current")
_CucsDhcpLeaseHostname_Type = SnmpAdminString
_CucsDhcpLeaseHostname_Object = MibTableColumn
cucsDhcpLeaseHostname = _CucsDhcpLeaseHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 7),
    _CucsDhcpLeaseHostname_Type()
)
cucsDhcpLeaseHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseHostname.setStatus("current")
_CucsDhcpLeaseIntf_Type = SnmpAdminString
_CucsDhcpLeaseIntf_Object = MibTableColumn
cucsDhcpLeaseIntf = _CucsDhcpLeaseIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 8),
    _CucsDhcpLeaseIntf_Type()
)
cucsDhcpLeaseIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseIntf.setStatus("current")
_CucsDhcpLeaseIp_Type = InetAddressIPv4
_CucsDhcpLeaseIp_Object = MibTableColumn
cucsDhcpLeaseIp = _CucsDhcpLeaseIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 9),
    _CucsDhcpLeaseIp_Type()
)
cucsDhcpLeaseIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseIp.setStatus("current")
_CucsDhcpLeaseMac_Type = MacAddress
_CucsDhcpLeaseMac_Object = MibTableColumn
cucsDhcpLeaseMac = _CucsDhcpLeaseMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 10),
    _CucsDhcpLeaseMac_Type()
)
cucsDhcpLeaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseMac.setStatus("current")
_CucsDhcpLeaseStarts_Type = DateAndTime
_CucsDhcpLeaseStarts_Object = MibTableColumn
cucsDhcpLeaseStarts = _CucsDhcpLeaseStarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 11, 3, 1, 11),
    _CucsDhcpLeaseStarts_Type()
)
cucsDhcpLeaseStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDhcpLeaseStarts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-DHCP-MIB",
    **{"cucsDhcpObjects": cucsDhcpObjects,
       "cucsDhcpAcquiredTable": cucsDhcpAcquiredTable,
       "cucsDhcpAcquiredEntry": cucsDhcpAcquiredEntry,
       "cucsDhcpAcquiredInstanceId": cucsDhcpAcquiredInstanceId,
       "cucsDhcpAcquiredDn": cucsDhcpAcquiredDn,
       "cucsDhcpAcquiredRn": cucsDhcpAcquiredRn,
       "cucsDhcpAcquiredAcqts": cucsDhcpAcquiredAcqts,
       "cucsDhcpAcquiredCookie": cucsDhcpAcquiredCookie,
       "cucsDhcpAcquiredEnds": cucsDhcpAcquiredEnds,
       "cucsDhcpAcquiredIp": cucsDhcpAcquiredIp,
       "cucsDhcpAcquiredSysId": cucsDhcpAcquiredSysId,
       "cucsDhcpAcquiredMac": cucsDhcpAcquiredMac,
       "cucsDhcpInstTable": cucsDhcpInstTable,
       "cucsDhcpInstEntry": cucsDhcpInstEntry,
       "cucsDhcpInstInstanceId": cucsDhcpInstInstanceId,
       "cucsDhcpInstDn": cucsDhcpInstDn,
       "cucsDhcpInstRn": cucsDhcpInstRn,
       "cucsDhcpLeaseTable": cucsDhcpLeaseTable,
       "cucsDhcpLeaseEntry": cucsDhcpLeaseEntry,
       "cucsDhcpLeaseInstanceId": cucsDhcpLeaseInstanceId,
       "cucsDhcpLeaseDn": cucsDhcpLeaseDn,
       "cucsDhcpLeaseRn": cucsDhcpLeaseRn,
       "cucsDhcpLeaseCliId": cucsDhcpLeaseCliId,
       "cucsDhcpLeaseCookie": cucsDhcpLeaseCookie,
       "cucsDhcpLeaseEnds": cucsDhcpLeaseEnds,
       "cucsDhcpLeaseHostname": cucsDhcpLeaseHostname,
       "cucsDhcpLeaseIntf": cucsDhcpLeaseIntf,
       "cucsDhcpLeaseIp": cucsDhcpLeaseIp,
       "cucsDhcpLeaseMac": cucsDhcpLeaseMac,
       "cucsDhcpLeaseStarts": cucsDhcpLeaseStarts}
)
