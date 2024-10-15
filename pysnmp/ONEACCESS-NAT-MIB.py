# SNMP MIB module (ONEACCESS-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:59 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(oacExpIMIpNatNotifications,
 oacExpIMIpNatStatistics,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIpNatNotifications",
    "oacExpIMIpNatStatistics",
    "oacMIBModules")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

oacNatMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 668)
)
oacNatMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacNatStatObjects_ObjectIdentity = ObjectIdentity
oacNatStatObjects = _OacNatStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1)
)
_OacNatStatGlobal_ObjectIdentity = ObjectIdentity
oacNatStatGlobal = _OacNatStatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1)
)
_OacNatActiveSessions_Type = Counter32
_OacNatActiveSessions_Object = MibScalar
oacNatActiveSessions = _OacNatActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 1),
    _OacNatActiveSessions_Type()
)
oacNatActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatActiveSessions.setStatus("current")
_OacNatSessionsClosed_Type = Counter32
_OacNatSessionsClosed_Object = MibScalar
oacNatSessionsClosed = _OacNatSessionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 2),
    _OacNatSessionsClosed_Type()
)
oacNatSessionsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionsClosed.setStatus("current")
_OacNatInTranslations_Type = Counter32
_OacNatInTranslations_Object = MibScalar
oacNatInTranslations = _OacNatInTranslations_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 3),
    _OacNatInTranslations_Type()
)
oacNatInTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatInTranslations.setStatus("current")
_OacNatOutTranslations_Type = Counter32
_OacNatOutTranslations_Object = MibScalar
oacNatOutTranslations = _OacNatOutTranslations_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 4),
    _OacNatOutTranslations_Type()
)
oacNatOutTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatOutTranslations.setStatus("current")
_OacNatInsideAddrMaps_Type = Counter32
_OacNatInsideAddrMaps_Object = MibScalar
oacNatInsideAddrMaps = _OacNatInsideAddrMaps_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 5),
    _OacNatInsideAddrMaps_Type()
)
oacNatInsideAddrMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatInsideAddrMaps.setStatus("current")
_OacNatOutsideAddrMaps_Type = Counter32
_OacNatOutsideAddrMaps_Object = MibScalar
oacNatOutsideAddrMaps = _OacNatOutsideAddrMaps_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 6),
    _OacNatOutsideAddrMaps_Type()
)
oacNatOutsideAddrMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatOutsideAddrMaps.setStatus("current")
_OacNatInPktsDropped_Type = Counter32
_OacNatInPktsDropped_Object = MibScalar
oacNatInPktsDropped = _OacNatInPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 7),
    _OacNatInPktsDropped_Type()
)
oacNatInPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatInPktsDropped.setStatus("current")
_OacNatOutPktsDropped_Type = Counter32
_OacNatOutPktsDropped_Object = MibScalar
oacNatOutPktsDropped = _OacNatOutPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 8),
    _OacNatOutPktsDropped_Type()
)
oacNatOutPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatOutPktsDropped.setStatus("current")
_OacNatDynamicAllocFailures_Type = Counter32
_OacNatDynamicAllocFailures_Object = MibScalar
oacNatDynamicAllocFailures = _OacNatDynamicAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 1, 9),
    _OacNatDynamicAllocFailures_Type()
)
oacNatDynamicAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatDynamicAllocFailures.setStatus("current")
_OacNatSessionTable_Object = MibTable
oacNatSessionTable = _OacNatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oacNatSessionTable.setStatus("current")
_OacNatSessionEntry_Object = MibTableRow
oacNatSessionEntry = _OacNatSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1)
)
oacNatSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-NAT-MIB", "oacNatSessionID"),
)
if mibBuilder.loadTexts:
    oacNatSessionEntry.setStatus("current")
_OacNatSessionID_Type = Unsigned32
_OacNatSessionID_Object = MibTableColumn
oacNatSessionID = _OacNatSessionID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 1),
    _OacNatSessionID_Type()
)
oacNatSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacNatSessionID.setStatus("current")


class _OacNatSessionProtocol_Type(Integer32):
    """Custom type oacNatSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OacNatSessionProtocol_Type.__name__ = "Integer32"
_OacNatSessionProtocol_Object = MibTableColumn
oacNatSessionProtocol = _OacNatSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 2),
    _OacNatSessionProtocol_Type()
)
oacNatSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionProtocol.setStatus("current")
_OacNatSessionInsideLocalAddr_Type = IpAddress
_OacNatSessionInsideLocalAddr_Object = MibTableColumn
oacNatSessionInsideLocalAddr = _OacNatSessionInsideLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 3),
    _OacNatSessionInsideLocalAddr_Type()
)
oacNatSessionInsideLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionInsideLocalAddr.setStatus("current")


class _OacNatSessionInsideLocalPort_Type(Integer32):
    """Custom type oacNatSessionInsideLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OacNatSessionInsideLocalPort_Type.__name__ = "Integer32"
_OacNatSessionInsideLocalPort_Object = MibTableColumn
oacNatSessionInsideLocalPort = _OacNatSessionInsideLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 4),
    _OacNatSessionInsideLocalPort_Type()
)
oacNatSessionInsideLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionInsideLocalPort.setStatus("current")
_OacNatSessionOutsideLocalAddr_Type = IpAddress
_OacNatSessionOutsideLocalAddr_Object = MibTableColumn
oacNatSessionOutsideLocalAddr = _OacNatSessionOutsideLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 5),
    _OacNatSessionOutsideLocalAddr_Type()
)
oacNatSessionOutsideLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionOutsideLocalAddr.setStatus("current")


class _OacNatSessionOutsidePort_Type(Integer32):
    """Custom type oacNatSessionOutsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OacNatSessionOutsidePort_Type.__name__ = "Integer32"
_OacNatSessionOutsidePort_Object = MibTableColumn
oacNatSessionOutsidePort = _OacNatSessionOutsidePort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 6),
    _OacNatSessionOutsidePort_Type()
)
oacNatSessionOutsidePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionOutsidePort.setStatus("current")
_OacNatSessionInsideGlobalAddr_Type = IpAddress
_OacNatSessionInsideGlobalAddr_Object = MibTableColumn
oacNatSessionInsideGlobalAddr = _OacNatSessionInsideGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 7),
    _OacNatSessionInsideGlobalAddr_Type()
)
oacNatSessionInsideGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionInsideGlobalAddr.setStatus("current")


class _OacNatSessionInsideGlobalPort_Type(Integer32):
    """Custom type oacNatSessionInsideGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OacNatSessionInsideGlobalPort_Type.__name__ = "Integer32"
_OacNatSessionInsideGlobalPort_Object = MibTableColumn
oacNatSessionInsideGlobalPort = _OacNatSessionInsideGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 8),
    _OacNatSessionInsideGlobalPort_Type()
)
oacNatSessionInsideGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionInsideGlobalPort.setStatus("current")
_OacNatSessionOutsideGlobalAddr_Type = IpAddress
_OacNatSessionOutsideGlobalAddr_Object = MibTableColumn
oacNatSessionOutsideGlobalAddr = _OacNatSessionOutsideGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 9),
    _OacNatSessionOutsideGlobalAddr_Type()
)
oacNatSessionOutsideGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionOutsideGlobalAddr.setStatus("current")
_OacNatSessionInPkts_Type = Counter32
_OacNatSessionInPkts_Object = MibTableColumn
oacNatSessionInPkts = _OacNatSessionInPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 10),
    _OacNatSessionInPkts_Type()
)
oacNatSessionInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionInPkts.setStatus("current")
_OacNatSessionOutPkts_Type = Counter32
_OacNatSessionOutPkts_Object = MibTableColumn
oacNatSessionOutPkts = _OacNatSessionOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 11),
    _OacNatSessionOutPkts_Type()
)
oacNatSessionOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionOutPkts.setStatus("current")
_OacNatSessionTimeout_Type = TimeInterval
_OacNatSessionTimeout_Object = MibTableColumn
oacNatSessionTimeout = _OacNatSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 2, 1, 12),
    _OacNatSessionTimeout_Type()
)
oacNatSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatSessionTimeout.setStatus("current")
_OacNatInsideMapTable_Object = MibTable
oacNatInsideMapTable = _OacNatInsideMapTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    oacNatInsideMapTable.setStatus("current")
_OacNatInsideMapEntry_Object = MibTableRow
oacNatInsideMapEntry = _OacNatInsideMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 3, 1)
)
oacNatInsideMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-NAT-MIB", "oacNatIMLocalAddr"),
)
if mibBuilder.loadTexts:
    oacNatInsideMapEntry.setStatus("current")
_OacNatIMLocalAddr_Type = IpAddress
_OacNatIMLocalAddr_Object = MibTableColumn
oacNatIMLocalAddr = _OacNatIMLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 3, 1, 1),
    _OacNatIMLocalAddr_Type()
)
oacNatIMLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacNatIMLocalAddr.setStatus("current")
_OacNatIMGlobalAddr_Type = IpAddress
_OacNatIMGlobalAddr_Object = MibTableColumn
oacNatIMGlobalAddr = _OacNatIMGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 3, 1, 2),
    _OacNatIMGlobalAddr_Type()
)
oacNatIMGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatIMGlobalAddr.setStatus("current")
_OacNatIMSessions_Type = Integer32
_OacNatIMSessions_Object = MibTableColumn
oacNatIMSessions = _OacNatIMSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 3, 1, 3),
    _OacNatIMSessions_Type()
)
oacNatIMSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatIMSessions.setStatus("current")
_OacNatIMTimeout_Type = TimeInterval
_OacNatIMTimeout_Object = MibTableColumn
oacNatIMTimeout = _OacNatIMTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 3, 1, 4),
    _OacNatIMTimeout_Type()
)
oacNatIMTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatIMTimeout.setStatus("current")
_OacNatOutsideMapTable_Object = MibTable
oacNatOutsideMapTable = _OacNatOutsideMapTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    oacNatOutsideMapTable.setStatus("current")
_OacNatOutsideMapEntry_Object = MibTableRow
oacNatOutsideMapEntry = _OacNatOutsideMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 4, 1)
)
oacNatOutsideMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-NAT-MIB", "oacNatOMGlobalAddr"),
)
if mibBuilder.loadTexts:
    oacNatOutsideMapEntry.setStatus("current")
_OacNatOMGlobalAddr_Type = IpAddress
_OacNatOMGlobalAddr_Object = MibTableColumn
oacNatOMGlobalAddr = _OacNatOMGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 4, 1, 1),
    _OacNatOMGlobalAddr_Type()
)
oacNatOMGlobalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacNatOMGlobalAddr.setStatus("current")
_OacNatOMLocalAddr_Type = IpAddress
_OacNatOMLocalAddr_Object = MibTableColumn
oacNatOMLocalAddr = _OacNatOMLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 4, 1, 2),
    _OacNatOMLocalAddr_Type()
)
oacNatOMLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatOMLocalAddr.setStatus("current")
_OacNatOMSessions_Type = Integer32
_OacNatOMSessions_Object = MibTableColumn
oacNatOMSessions = _OacNatOMSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 4, 1, 3),
    _OacNatOMSessions_Type()
)
oacNatOMSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatOMSessions.setStatus("current")
_OacNatOMTimeout_Type = TimeInterval
_OacNatOMTimeout_Object = MibTableColumn
oacNatOMTimeout = _OacNatOMTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 1, 4, 1, 4),
    _OacNatOMTimeout_Type()
)
oacNatOMTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacNatOMTimeout.setStatus("current")
_OacNatStatNotifications_ObjectIdentity = ObjectIdentity
oacNatStatNotifications = _OacNatStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 2)
)
_OacNatStatConformance_ObjectIdentity = ObjectIdentity
oacNatStatConformance = _OacNatStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 3)
)
_OacNatStatGroups_ObjectIdentity = ObjectIdentity
oacNatStatGroups = _OacNatStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 3, 1)
)
_OacNatStatCompliances_ObjectIdentity = ObjectIdentity
oacNatStatCompliances = _OacNatStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 3, 2)
)

# Managed Objects groups

oacNatStatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 3, 1, 1)
)
oacNatStatGeneralGroup.setObjects(
      *(("ONEACCESS-NAT-MIB", "oacNatActiveSessions"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionsClosed"),
        ("ONEACCESS-NAT-MIB", "oacNatInTranslations"),
        ("ONEACCESS-NAT-MIB", "oacNatOutTranslations"),
        ("ONEACCESS-NAT-MIB", "oacNatInsideAddrMaps"),
        ("ONEACCESS-NAT-MIB", "oacNatOutsideAddrMaps"),
        ("ONEACCESS-NAT-MIB", "oacNatInPktsDropped"),
        ("ONEACCESS-NAT-MIB", "oacNatOutPktsDropped"),
        ("ONEACCESS-NAT-MIB", "oacNatDynamicAllocFailures"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionProtocol"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionInsideLocalAddr"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionInsideLocalPort"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionOutsideLocalAddr"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionOutsidePort"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionInsideGlobalAddr"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionInsideGlobalPort"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionOutsideGlobalAddr"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionInPkts"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionOutPkts"),
        ("ONEACCESS-NAT-MIB", "oacNatSessionTimeout"),
        ("ONEACCESS-NAT-MIB", "oacNatIMGlobalAddr"),
        ("ONEACCESS-NAT-MIB", "oacNatIMSessions"),
        ("ONEACCESS-NAT-MIB", "oacNatIMTimeout"),
        ("ONEACCESS-NAT-MIB", "oacNatOMLocalAddr"),
        ("ONEACCESS-NAT-MIB", "oacNatOMSessions"),
        ("ONEACCESS-NAT-MIB", "oacNatOMTimeout"))
)
if mibBuilder.loadTexts:
    oacNatStatGeneralGroup.setStatus("current")


# Notification objects

oacNatNotificationMaximumSessionReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oacNatNotificationMaximumSessionReached.setStatus(
        "current"
    )

oacNatNotificationWarningSessionReachingLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    oacNatNotificationWarningSessionReachingLimit.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

oacNatStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oacNatStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-NAT-MIB",
    **{"oacNatMIBModule": oacNatMIBModule,
       "oacNatStatObjects": oacNatStatObjects,
       "oacNatStatGlobal": oacNatStatGlobal,
       "oacNatActiveSessions": oacNatActiveSessions,
       "oacNatSessionsClosed": oacNatSessionsClosed,
       "oacNatInTranslations": oacNatInTranslations,
       "oacNatOutTranslations": oacNatOutTranslations,
       "oacNatInsideAddrMaps": oacNatInsideAddrMaps,
       "oacNatOutsideAddrMaps": oacNatOutsideAddrMaps,
       "oacNatInPktsDropped": oacNatInPktsDropped,
       "oacNatOutPktsDropped": oacNatOutPktsDropped,
       "oacNatDynamicAllocFailures": oacNatDynamicAllocFailures,
       "oacNatSessionTable": oacNatSessionTable,
       "oacNatSessionEntry": oacNatSessionEntry,
       "oacNatSessionID": oacNatSessionID,
       "oacNatSessionProtocol": oacNatSessionProtocol,
       "oacNatSessionInsideLocalAddr": oacNatSessionInsideLocalAddr,
       "oacNatSessionInsideLocalPort": oacNatSessionInsideLocalPort,
       "oacNatSessionOutsideLocalAddr": oacNatSessionOutsideLocalAddr,
       "oacNatSessionOutsidePort": oacNatSessionOutsidePort,
       "oacNatSessionInsideGlobalAddr": oacNatSessionInsideGlobalAddr,
       "oacNatSessionInsideGlobalPort": oacNatSessionInsideGlobalPort,
       "oacNatSessionOutsideGlobalAddr": oacNatSessionOutsideGlobalAddr,
       "oacNatSessionInPkts": oacNatSessionInPkts,
       "oacNatSessionOutPkts": oacNatSessionOutPkts,
       "oacNatSessionTimeout": oacNatSessionTimeout,
       "oacNatInsideMapTable": oacNatInsideMapTable,
       "oacNatInsideMapEntry": oacNatInsideMapEntry,
       "oacNatIMLocalAddr": oacNatIMLocalAddr,
       "oacNatIMGlobalAddr": oacNatIMGlobalAddr,
       "oacNatIMSessions": oacNatIMSessions,
       "oacNatIMTimeout": oacNatIMTimeout,
       "oacNatOutsideMapTable": oacNatOutsideMapTable,
       "oacNatOutsideMapEntry": oacNatOutsideMapEntry,
       "oacNatOMGlobalAddr": oacNatOMGlobalAddr,
       "oacNatOMLocalAddr": oacNatOMLocalAddr,
       "oacNatOMSessions": oacNatOMSessions,
       "oacNatOMTimeout": oacNatOMTimeout,
       "oacNatStatNotifications": oacNatStatNotifications,
       "oacNatStatConformance": oacNatStatConformance,
       "oacNatStatGroups": oacNatStatGroups,
       "oacNatStatGeneralGroup": oacNatStatGeneralGroup,
       "oacNatStatCompliances": oacNatStatCompliances,
       "oacNatStatCompliance": oacNatStatCompliance,
       "oacNatNotificationMaximumSessionReached": oacNatNotificationMaximumSessionReached,
       "oacNatNotificationWarningSessionReachingLimit": oacNatNotificationWarningSessionReachingLimit}
)
