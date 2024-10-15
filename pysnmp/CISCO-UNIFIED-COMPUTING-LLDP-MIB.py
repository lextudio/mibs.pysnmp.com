# SNMP MIB module (CISCO-UNIFIED-COMPUTING-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:50 2024
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

cucsLldpObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsLldpAcquiredTable_Object = MibTable
cucsLldpAcquiredTable = _CucsLldpAcquiredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1)
)
if mibBuilder.loadTexts:
    cucsLldpAcquiredTable.setStatus("current")
_CucsLldpAcquiredEntry_Object = MibTableRow
cucsLldpAcquiredEntry = _CucsLldpAcquiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1)
)
cucsLldpAcquiredEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LLDP-MIB", "cucsLldpAcquiredInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLldpAcquiredEntry.setStatus("current")
_CucsLldpAcquiredInstanceId_Type = CucsManagedObjectId
_CucsLldpAcquiredInstanceId_Object = MibTableColumn
cucsLldpAcquiredInstanceId = _CucsLldpAcquiredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 1),
    _CucsLldpAcquiredInstanceId_Type()
)
cucsLldpAcquiredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLldpAcquiredInstanceId.setStatus("current")
_CucsLldpAcquiredDn_Type = CucsManagedObjectDn
_CucsLldpAcquiredDn_Object = MibTableColumn
cucsLldpAcquiredDn = _CucsLldpAcquiredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 2),
    _CucsLldpAcquiredDn_Type()
)
cucsLldpAcquiredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLldpAcquiredDn.setStatus("current")
_CucsLldpAcquiredRn_Type = SnmpAdminString
_CucsLldpAcquiredRn_Object = MibTableColumn
cucsLldpAcquiredRn = _CucsLldpAcquiredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 3),
    _CucsLldpAcquiredRn_Type()
)
cucsLldpAcquiredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLldpAcquiredRn.setStatus("current")
_CucsLldpAcquiredAcqts_Type = DateAndTime
_CucsLldpAcquiredAcqts_Object = MibTableColumn
cucsLldpAcquiredAcqts = _CucsLldpAcquiredAcqts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 4),
    _CucsLldpAcquiredAcqts_Type()
)
cucsLldpAcquiredAcqts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLldpAcquiredAcqts.setStatus("current")
_CucsLldpAcquiredChassisMac_Type = MacAddress
_CucsLldpAcquiredChassisMac_Object = MibTableColumn
cucsLldpAcquiredChassisMac = _CucsLldpAcquiredChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 5),
    _CucsLldpAcquiredChassisMac_Type()
)
cucsLldpAcquiredChassisMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLldpAcquiredChassisMac.setStatus("current")
_CucsLldpAcquiredPeerDn_Type = SnmpAdminString
_CucsLldpAcquiredPeerDn_Object = MibTableColumn
cucsLldpAcquiredPeerDn = _CucsLldpAcquiredPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 6),
    _CucsLldpAcquiredPeerDn_Type()
)
cucsLldpAcquiredPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLldpAcquiredPeerDn.setStatus("current")
_CucsLldpAcquiredPortMac_Type = MacAddress
_CucsLldpAcquiredPortMac_Object = MibTableColumn
cucsLldpAcquiredPortMac = _CucsLldpAcquiredPortMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 58, 1, 1, 7),
    _CucsLldpAcquiredPortMac_Type()
)
cucsLldpAcquiredPortMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLldpAcquiredPortMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-LLDP-MIB",
    **{"cucsLldpObjects": cucsLldpObjects,
       "cucsLldpAcquiredTable": cucsLldpAcquiredTable,
       "cucsLldpAcquiredEntry": cucsLldpAcquiredEntry,
       "cucsLldpAcquiredInstanceId": cucsLldpAcquiredInstanceId,
       "cucsLldpAcquiredDn": cucsLldpAcquiredDn,
       "cucsLldpAcquiredRn": cucsLldpAcquiredRn,
       "cucsLldpAcquiredAcqts": cucsLldpAcquiredAcqts,
       "cucsLldpAcquiredChassisMac": cucsLldpAcquiredChassisMac,
       "cucsLldpAcquiredPeerDn": cucsLldpAcquiredPeerDn,
       "cucsLldpAcquiredPortMac": cucsLldpAcquiredPortMac}
)
