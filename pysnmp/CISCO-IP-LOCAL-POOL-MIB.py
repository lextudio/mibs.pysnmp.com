# SNMP MIB module (CISCO-IP-LOCAL-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-LOCAL-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:39 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpLocalPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326)
)
ciscoIpLocalPoolMIB.setRevisions(
        ("2007-11-12 00:00",
         "2005-01-11 00:00",
         "2003-04-03 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIpLocalPoolName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )



class CIpLocalPoolGroupNameOrNull(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



class CIpLocalPoolPercentage(Gauge32, TextualConvention):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIpLocalPoolMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpLocalPoolMIBNotifs = _CiscoIpLocalPoolMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 0)
)
_CiscoIpLocalPoolMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpLocalPoolMIBObjects = _CiscoIpLocalPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1)
)
_CIpLocalPoolConfig_ObjectIdentity = ObjectIdentity
cIpLocalPoolConfig = _CIpLocalPoolConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1)
)
_CIpLocalPoolNotificationsEnable_Type = TruthValue
_CIpLocalPoolNotificationsEnable_Object = MibScalar
cIpLocalPoolNotificationsEnable = _CIpLocalPoolNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 1),
    _CIpLocalPoolNotificationsEnable_Type()
)
cIpLocalPoolNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpLocalPoolNotificationsEnable.setStatus("current")
_CIpLocalPoolConfigTable_Object = MibTable
cIpLocalPoolConfigTable = _CIpLocalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cIpLocalPoolConfigTable.setStatus("current")
_CIpLocalPoolConfigEntry_Object = MibTableRow
cIpLocalPoolConfigEntry = _CIpLocalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1)
)
cIpLocalPoolConfigEntry.setIndexNames(
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolName"),
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAddrType"),
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAddressLo"),
)
if mibBuilder.loadTexts:
    cIpLocalPoolConfigEntry.setStatus("current")
_CIpLocalPoolName_Type = CIpLocalPoolName
_CIpLocalPoolName_Object = MibTableColumn
cIpLocalPoolName = _CIpLocalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 1),
    _CIpLocalPoolName_Type()
)
cIpLocalPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpLocalPoolName.setStatus("current")
_CIpLocalPoolAddrType_Type = InetAddressType
_CIpLocalPoolAddrType_Object = MibTableColumn
cIpLocalPoolAddrType = _CIpLocalPoolAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 2),
    _CIpLocalPoolAddrType_Type()
)
cIpLocalPoolAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpLocalPoolAddrType.setStatus("current")
_CIpLocalPoolAddressLo_Type = InetAddress
_CIpLocalPoolAddressLo_Object = MibTableColumn
cIpLocalPoolAddressLo = _CIpLocalPoolAddressLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 3),
    _CIpLocalPoolAddressLo_Type()
)
cIpLocalPoolAddressLo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpLocalPoolAddressLo.setStatus("current")
_CIpLocalPoolAddressHi_Type = InetAddress
_CIpLocalPoolAddressHi_Object = MibTableColumn
cIpLocalPoolAddressHi = _CIpLocalPoolAddressHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 4),
    _CIpLocalPoolAddressHi_Type()
)
cIpLocalPoolAddressHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpLocalPoolAddressHi.setStatus("current")
_CIpLocalPoolFreeAddrs_Type = Gauge32
_CIpLocalPoolFreeAddrs_Object = MibTableColumn
cIpLocalPoolFreeAddrs = _CIpLocalPoolFreeAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 5),
    _CIpLocalPoolFreeAddrs_Type()
)
cIpLocalPoolFreeAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolFreeAddrs.setStatus("current")
_CIpLocalPoolInUseAddrs_Type = Gauge32
_CIpLocalPoolInUseAddrs_Object = MibTableColumn
cIpLocalPoolInUseAddrs = _CIpLocalPoolInUseAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 6),
    _CIpLocalPoolInUseAddrs_Type()
)
cIpLocalPoolInUseAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolInUseAddrs.setStatus("current")
_CIpLocalPoolGroupContainedIn_Type = CIpLocalPoolGroupNameOrNull
_CIpLocalPoolGroupContainedIn_Object = MibTableColumn
cIpLocalPoolGroupContainedIn = _CIpLocalPoolGroupContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 7),
    _CIpLocalPoolGroupContainedIn_Type()
)
cIpLocalPoolGroupContainedIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpLocalPoolGroupContainedIn.setStatus("current")
_CIpLocalPoolRowStatus_Type = RowStatus
_CIpLocalPoolRowStatus_Object = MibTableColumn
cIpLocalPoolRowStatus = _CIpLocalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 8),
    _CIpLocalPoolRowStatus_Type()
)
cIpLocalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpLocalPoolRowStatus.setStatus("current")


class _CIpLocalPoolPriority_Type(Unsigned32):
    """Custom type cIpLocalPoolPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CIpLocalPoolPriority_Type.__name__ = "Unsigned32"
_CIpLocalPoolPriority_Object = MibTableColumn
cIpLocalPoolPriority = _CIpLocalPoolPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 1, 2, 1, 9),
    _CIpLocalPoolPriority_Type()
)
cIpLocalPoolPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpLocalPoolPriority.setStatus("current")
_CIpLocalPoolGroup_ObjectIdentity = ObjectIdentity
cIpLocalPoolGroup = _CIpLocalPoolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2)
)
_CIpLocalPoolGroupContainsTable_Object = MibTable
cIpLocalPoolGroupContainsTable = _CIpLocalPoolGroupContainsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIpLocalPoolGroupContainsTable.setStatus("current")
_CIpLocalPoolGroupContainsEntry_Object = MibTableRow
cIpLocalPoolGroupContainsEntry = _CIpLocalPoolGroupContainsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 1, 1)
)
cIpLocalPoolGroupContainsEntry.setIndexNames(
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolGroupName"),
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolChildIndex"),
)
if mibBuilder.loadTexts:
    cIpLocalPoolGroupContainsEntry.setStatus("current")
_CIpLocalPoolGroupName_Type = CIpLocalPoolGroupNameOrNull
_CIpLocalPoolGroupName_Object = MibTableColumn
cIpLocalPoolGroupName = _CIpLocalPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 1, 1, 1),
    _CIpLocalPoolGroupName_Type()
)
cIpLocalPoolGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpLocalPoolGroupName.setStatus("current")
_CIpLocalPoolChildIndex_Type = CIpLocalPoolName
_CIpLocalPoolChildIndex_Object = MibTableColumn
cIpLocalPoolChildIndex = _CIpLocalPoolChildIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 1, 1, 2),
    _CIpLocalPoolChildIndex_Type()
)
cIpLocalPoolChildIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolChildIndex.setStatus("current")
_CIpLocalPoolGroupTable_Object = MibTable
cIpLocalPoolGroupTable = _CIpLocalPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cIpLocalPoolGroupTable.setStatus("current")
_CIpLocalPoolGroupEntry_Object = MibTableRow
cIpLocalPoolGroupEntry = _CIpLocalPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 2, 1)
)
cIpLocalPoolGroupEntry.setIndexNames(
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolGroupName"),
)
if mibBuilder.loadTexts:
    cIpLocalPoolGroupEntry.setStatus("current")
_CIpLocalPoolGroupFreeAddrs_Type = Gauge32
_CIpLocalPoolGroupFreeAddrs_Object = MibTableColumn
cIpLocalPoolGroupFreeAddrs = _CIpLocalPoolGroupFreeAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 2, 1, 1),
    _CIpLocalPoolGroupFreeAddrs_Type()
)
cIpLocalPoolGroupFreeAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolGroupFreeAddrs.setStatus("current")
_CIpLocalPoolGroupInUseAddrs_Type = Gauge32
_CIpLocalPoolGroupInUseAddrs_Object = MibTableColumn
cIpLocalPoolGroupInUseAddrs = _CIpLocalPoolGroupInUseAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 2, 2, 1, 2),
    _CIpLocalPoolGroupInUseAddrs_Type()
)
cIpLocalPoolGroupInUseAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolGroupInUseAddrs.setStatus("current")
_CIpLocalPoolStats_ObjectIdentity = ObjectIdentity
cIpLocalPoolStats = _CIpLocalPoolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3)
)
_CIpLocalPoolStatsTable_Object = MibTable
cIpLocalPoolStatsTable = _CIpLocalPoolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cIpLocalPoolStatsTable.setStatus("current")
_CIpLocalPoolStatsEntry_Object = MibTableRow
cIpLocalPoolStatsEntry = _CIpLocalPoolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1)
)
cIpLocalPoolStatsEntry.setIndexNames(
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolName"),
)
if mibBuilder.loadTexts:
    cIpLocalPoolStatsEntry.setStatus("current")
_CIpLocalPoolStatFreeAddrs_Type = Gauge32
_CIpLocalPoolStatFreeAddrs_Object = MibTableColumn
cIpLocalPoolStatFreeAddrs = _CIpLocalPoolStatFreeAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 1),
    _CIpLocalPoolStatFreeAddrs_Type()
)
cIpLocalPoolStatFreeAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolStatFreeAddrs.setStatus("current")
_CIpLocalPoolStatInUseAddrs_Type = Gauge32
_CIpLocalPoolStatInUseAddrs_Object = MibTableColumn
cIpLocalPoolStatInUseAddrs = _CIpLocalPoolStatInUseAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 2),
    _CIpLocalPoolStatInUseAddrs_Type()
)
cIpLocalPoolStatInUseAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolStatInUseAddrs.setStatus("current")
_CIpLocalPoolStatHiWaterUsedAddrs_Type = Unsigned32
_CIpLocalPoolStatHiWaterUsedAddrs_Object = MibTableColumn
cIpLocalPoolStatHiWaterUsedAddrs = _CIpLocalPoolStatHiWaterUsedAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 3),
    _CIpLocalPoolStatHiWaterUsedAddrs_Type()
)
cIpLocalPoolStatHiWaterUsedAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpLocalPoolStatHiWaterUsedAddrs.setStatus("current")


class _CIpLocalPoolStatInUseAddrThldLo_Type(Unsigned32):
    """Custom type cIpLocalPoolStatInUseAddrThldLo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIpLocalPoolStatInUseAddrThldLo_Type.__name__ = "Unsigned32"
_CIpLocalPoolStatInUseAddrThldLo_Object = MibTableColumn
cIpLocalPoolStatInUseAddrThldLo = _CIpLocalPoolStatInUseAddrThldLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 4),
    _CIpLocalPoolStatInUseAddrThldLo_Type()
)
cIpLocalPoolStatInUseAddrThldLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpLocalPoolStatInUseAddrThldLo.setStatus("current")


class _CIpLocalPoolStatInUseAddrThldHi_Type(Unsigned32):
    """Custom type cIpLocalPoolStatInUseAddrThldHi based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CIpLocalPoolStatInUseAddrThldHi_Type.__name__ = "Unsigned32"
_CIpLocalPoolStatInUseAddrThldHi_Object = MibTableColumn
cIpLocalPoolStatInUseAddrThldHi = _CIpLocalPoolStatInUseAddrThldHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 5),
    _CIpLocalPoolStatInUseAddrThldHi_Type()
)
cIpLocalPoolStatInUseAddrThldHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpLocalPoolStatInUseAddrThldHi.setStatus("current")


class _CIpLocalPoolPercentAddrThldLo_Type(CIpLocalPoolPercentage):
    """Custom type cIpLocalPoolPercentAddrThldLo based on CIpLocalPoolPercentage"""
    defaultValue = 0


_CIpLocalPoolPercentAddrThldLo_Object = MibTableColumn
cIpLocalPoolPercentAddrThldLo = _CIpLocalPoolPercentAddrThldLo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 6),
    _CIpLocalPoolPercentAddrThldLo_Type()
)
cIpLocalPoolPercentAddrThldLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpLocalPoolPercentAddrThldLo.setStatus("current")


class _CIpLocalPoolPercentAddrThldHi_Type(CIpLocalPoolPercentage):
    """Custom type cIpLocalPoolPercentAddrThldHi based on CIpLocalPoolPercentage"""
    defaultValue = 100


_CIpLocalPoolPercentAddrThldHi_Object = MibTableColumn
cIpLocalPoolPercentAddrThldHi = _CIpLocalPoolPercentAddrThldHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 1, 1, 7),
    _CIpLocalPoolPercentAddrThldHi_Type()
)
cIpLocalPoolPercentAddrThldHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpLocalPoolPercentAddrThldHi.setStatus("current")
_CIpLocalPoolAllocTable_Object = MibTable
cIpLocalPoolAllocTable = _CIpLocalPoolAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cIpLocalPoolAllocTable.setStatus("current")
_CIpLocalPoolAllocEntry_Object = MibTableRow
cIpLocalPoolAllocEntry = _CIpLocalPoolAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 2, 1)
)
cIpLocalPoolAllocEntry.setIndexNames(
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolName"),
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAllocAddrType"),
    (0, "CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAllocAddr"),
)
if mibBuilder.loadTexts:
    cIpLocalPoolAllocEntry.setStatus("current")
_CIpLocalPoolAllocAddrType_Type = InetAddressType
_CIpLocalPoolAllocAddrType_Object = MibTableColumn
cIpLocalPoolAllocAddrType = _CIpLocalPoolAllocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 2, 1, 1),
    _CIpLocalPoolAllocAddrType_Type()
)
cIpLocalPoolAllocAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpLocalPoolAllocAddrType.setStatus("current")
_CIpLocalPoolAllocAddr_Type = InetAddress
_CIpLocalPoolAllocAddr_Object = MibTableColumn
cIpLocalPoolAllocAddr = _CIpLocalPoolAllocAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 2, 1, 2),
    _CIpLocalPoolAllocAddr_Type()
)
cIpLocalPoolAllocAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpLocalPoolAllocAddr.setStatus("current")
_CIpLocalPoolAllocIfIndex_Type = InterfaceIndexOrZero
_CIpLocalPoolAllocIfIndex_Object = MibTableColumn
cIpLocalPoolAllocIfIndex = _CIpLocalPoolAllocIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 2, 1, 3),
    _CIpLocalPoolAllocIfIndex_Type()
)
cIpLocalPoolAllocIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolAllocIfIndex.setStatus("current")
_CIpLocalPoolAllocUser_Type = SnmpAdminString
_CIpLocalPoolAllocUser_Object = MibTableColumn
cIpLocalPoolAllocUser = _CIpLocalPoolAllocUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 1, 3, 2, 1, 4),
    _CIpLocalPoolAllocUser_Type()
)
cIpLocalPoolAllocUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpLocalPoolAllocUser.setStatus("current")
_CiscoIpLocalPoolMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpLocalPoolMIBConform = _CiscoIpLocalPoolMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2)
)
_CiscoIpLocalPoolMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpLocalPoolMIBCompliances = _CiscoIpLocalPoolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 1)
)
_CiscoIpLocalPoolMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpLocalPoolMIBGroups = _CiscoIpLocalPoolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2)
)

# Managed Objects groups

ciscoIpLocalPoolConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 1)
)
ciscoIpLocalPoolConfigGroup.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolNotificationsEnable"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAddressHi"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolFreeAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolInUseAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolGroupContainedIn"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolConfigGroup.setStatus("current")

ciscoIpLocalPoolGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 2)
)
ciscoIpLocalPoolGroupGroup.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolChildIndex"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolGroupFreeAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolGroupInUseAddrs"))
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolGroupGroup.setStatus("current")

ciscoIpLocalPoolStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 3)
)
ciscoIpLocalPoolStatsGroup.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatFreeAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatInUseAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatHiWaterUsedAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatInUseAddrThldLo"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatInUseAddrThldHi"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAllocIfIndex"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolAllocUser"))
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolStatsGroup.setStatus("current")

ciscoIpLocalPoolStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 5)
)
ciscoIpLocalPoolStatsGroupSup1.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolPercentAddrThldLo"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolPercentAddrThldHi"))
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolStatsGroupSup1.setStatus("current")

ciscoIpLocalPoolPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 7)
)
ciscoIpLocalPoolPriorityGroup.setObjects(
    ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolPriority")
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolPriorityGroup.setStatus("current")


# Notification objects

ciscoIpLocalPoolInUseAddrNoti = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 0, 1)
)
ciscoIpLocalPoolInUseAddrNoti.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatFreeAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatInUseAddrs"))
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolInUseAddrNoti.setStatus(
        "current"
    )

cilpPercentAddrUsedLoNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 0, 2)
)
cilpPercentAddrUsedLoNotif.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatFreeAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatInUseAddrs"))
)
if mibBuilder.loadTexts:
    cilpPercentAddrUsedLoNotif.setStatus(
        "current"
    )

cilpPercentAddrUsedHiNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 0, 3)
)
cilpPercentAddrUsedHiNotif.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatFreeAddrs"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cIpLocalPoolStatInUseAddrs"))
)
if mibBuilder.loadTexts:
    cilpPercentAddrUsedHiNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoIpLocalPoolNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 4)
)
ciscoIpLocalPoolNotifGroup.setObjects(
    ("CISCO-IP-LOCAL-POOL-MIB", "ciscoIpLocalPoolInUseAddrNoti")
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolNotifGroup.setStatus(
        "current"
    )

ciscoIpLocalPoolNotifGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 2, 6)
)
ciscoIpLocalPoolNotifGroupSup1.setObjects(
      *(("CISCO-IP-LOCAL-POOL-MIB", "cilpPercentAddrUsedLoNotif"),
        ("CISCO-IP-LOCAL-POOL-MIB", "cilpPercentAddrUsedHiNotif"))
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolNotifGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIpLocalPoolMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIpLocalPoolMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoIpLocalPoolMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 326, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIpLocalPoolMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-LOCAL-POOL-MIB",
    **{"CIpLocalPoolName": CIpLocalPoolName,
       "CIpLocalPoolGroupNameOrNull": CIpLocalPoolGroupNameOrNull,
       "CIpLocalPoolPercentage": CIpLocalPoolPercentage,
       "ciscoIpLocalPoolMIB": ciscoIpLocalPoolMIB,
       "ciscoIpLocalPoolMIBNotifs": ciscoIpLocalPoolMIBNotifs,
       "ciscoIpLocalPoolInUseAddrNoti": ciscoIpLocalPoolInUseAddrNoti,
       "cilpPercentAddrUsedLoNotif": cilpPercentAddrUsedLoNotif,
       "cilpPercentAddrUsedHiNotif": cilpPercentAddrUsedHiNotif,
       "ciscoIpLocalPoolMIBObjects": ciscoIpLocalPoolMIBObjects,
       "cIpLocalPoolConfig": cIpLocalPoolConfig,
       "cIpLocalPoolNotificationsEnable": cIpLocalPoolNotificationsEnable,
       "cIpLocalPoolConfigTable": cIpLocalPoolConfigTable,
       "cIpLocalPoolConfigEntry": cIpLocalPoolConfigEntry,
       "cIpLocalPoolName": cIpLocalPoolName,
       "cIpLocalPoolAddrType": cIpLocalPoolAddrType,
       "cIpLocalPoolAddressLo": cIpLocalPoolAddressLo,
       "cIpLocalPoolAddressHi": cIpLocalPoolAddressHi,
       "cIpLocalPoolFreeAddrs": cIpLocalPoolFreeAddrs,
       "cIpLocalPoolInUseAddrs": cIpLocalPoolInUseAddrs,
       "cIpLocalPoolGroupContainedIn": cIpLocalPoolGroupContainedIn,
       "cIpLocalPoolRowStatus": cIpLocalPoolRowStatus,
       "cIpLocalPoolPriority": cIpLocalPoolPriority,
       "cIpLocalPoolGroup": cIpLocalPoolGroup,
       "cIpLocalPoolGroupContainsTable": cIpLocalPoolGroupContainsTable,
       "cIpLocalPoolGroupContainsEntry": cIpLocalPoolGroupContainsEntry,
       "cIpLocalPoolGroupName": cIpLocalPoolGroupName,
       "cIpLocalPoolChildIndex": cIpLocalPoolChildIndex,
       "cIpLocalPoolGroupTable": cIpLocalPoolGroupTable,
       "cIpLocalPoolGroupEntry": cIpLocalPoolGroupEntry,
       "cIpLocalPoolGroupFreeAddrs": cIpLocalPoolGroupFreeAddrs,
       "cIpLocalPoolGroupInUseAddrs": cIpLocalPoolGroupInUseAddrs,
       "cIpLocalPoolStats": cIpLocalPoolStats,
       "cIpLocalPoolStatsTable": cIpLocalPoolStatsTable,
       "cIpLocalPoolStatsEntry": cIpLocalPoolStatsEntry,
       "cIpLocalPoolStatFreeAddrs": cIpLocalPoolStatFreeAddrs,
       "cIpLocalPoolStatInUseAddrs": cIpLocalPoolStatInUseAddrs,
       "cIpLocalPoolStatHiWaterUsedAddrs": cIpLocalPoolStatHiWaterUsedAddrs,
       "cIpLocalPoolStatInUseAddrThldLo": cIpLocalPoolStatInUseAddrThldLo,
       "cIpLocalPoolStatInUseAddrThldHi": cIpLocalPoolStatInUseAddrThldHi,
       "cIpLocalPoolPercentAddrThldLo": cIpLocalPoolPercentAddrThldLo,
       "cIpLocalPoolPercentAddrThldHi": cIpLocalPoolPercentAddrThldHi,
       "cIpLocalPoolAllocTable": cIpLocalPoolAllocTable,
       "cIpLocalPoolAllocEntry": cIpLocalPoolAllocEntry,
       "cIpLocalPoolAllocAddrType": cIpLocalPoolAllocAddrType,
       "cIpLocalPoolAllocAddr": cIpLocalPoolAllocAddr,
       "cIpLocalPoolAllocIfIndex": cIpLocalPoolAllocIfIndex,
       "cIpLocalPoolAllocUser": cIpLocalPoolAllocUser,
       "ciscoIpLocalPoolMIBConform": ciscoIpLocalPoolMIBConform,
       "ciscoIpLocalPoolMIBCompliances": ciscoIpLocalPoolMIBCompliances,
       "ciscoIpLocalPoolMIBCompliance": ciscoIpLocalPoolMIBCompliance,
       "ciscoIpLocalPoolMIBCompliance1": ciscoIpLocalPoolMIBCompliance1,
       "ciscoIpLocalPoolMIBCompliance2": ciscoIpLocalPoolMIBCompliance2,
       "ciscoIpLocalPoolMIBGroups": ciscoIpLocalPoolMIBGroups,
       "ciscoIpLocalPoolConfigGroup": ciscoIpLocalPoolConfigGroup,
       "ciscoIpLocalPoolGroupGroup": ciscoIpLocalPoolGroupGroup,
       "ciscoIpLocalPoolStatsGroup": ciscoIpLocalPoolStatsGroup,
       "ciscoIpLocalPoolNotifGroup": ciscoIpLocalPoolNotifGroup,
       "ciscoIpLocalPoolStatsGroupSup1": ciscoIpLocalPoolStatsGroupSup1,
       "ciscoIpLocalPoolNotifGroupSup1": ciscoIpLocalPoolNotifGroupSup1,
       "ciscoIpLocalPoolPriorityGroup": ciscoIpLocalPoolPriorityGroup}
)
