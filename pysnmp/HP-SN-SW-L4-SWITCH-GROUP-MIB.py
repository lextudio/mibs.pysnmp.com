# SNMP MIB module (HP-SN-SW-L4-SWITCH-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-MIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:47 2024
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

(snL4,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snL4")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class L4RowSts(Integer32):
    """Custom type L4RowSts based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )





class L4Status(Integer32):
    """Custom type L4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class L4ServerName(OctetString):
    """Custom type L4ServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )





class L4Flag(Integer32):
    """Custom type L4Flag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )





class L4DeleteState(Integer32):
    """Custom type L4DeleteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 0),
          ("waitdelete", 2),
          ("waitunbind", 1))
    )





class WebCacheState(Integer32):
    """Custom type WebCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("disabled", 0),
          ("enabled", 1),
          ("failed", 2),
          ("shutdown", 5),
          ("suspect", 4),
          ("testing", 3))
    )





class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnL4Gen_ObjectIdentity = ObjectIdentity
snL4Gen = _SnL4Gen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1)
)


class _SnL4MaxSessionLimit_Type(Integer32):
    """Custom type snL4MaxSessionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SnL4MaxSessionLimit_Type.__name__ = "Integer32"
_SnL4MaxSessionLimit_Object = MibScalar
snL4MaxSessionLimit = _SnL4MaxSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 1),
    _SnL4MaxSessionLimit_Type()
)
snL4MaxSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4MaxSessionLimit.setStatus("mandatory")


class _SnL4TcpSynLimit_Type(Integer32):
    """Custom type snL4TcpSynLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4TcpSynLimit_Type.__name__ = "Integer32"
_SnL4TcpSynLimit_Object = MibScalar
snL4TcpSynLimit = _SnL4TcpSynLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 2),
    _SnL4TcpSynLimit_Type()
)
snL4TcpSynLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4TcpSynLimit.setStatus("mandatory")


class _SnL4slbGlobalSDAType_Type(Integer32):
    """Custom type snL4slbGlobalSDAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leastconnection", 1),
          ("roundrobin", 2),
          ("weighted", 3))
    )


_SnL4slbGlobalSDAType_Type.__name__ = "Integer32"
_SnL4slbGlobalSDAType_Object = MibScalar
snL4slbGlobalSDAType = _SnL4slbGlobalSDAType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 3),
    _SnL4slbGlobalSDAType_Type()
)
snL4slbGlobalSDAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4slbGlobalSDAType.setStatus("mandatory")
_SnL4slbTotalConnections_Type = Counter32
_SnL4slbTotalConnections_Object = MibScalar
snL4slbTotalConnections = _SnL4slbTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 4),
    _SnL4slbTotalConnections_Type()
)
snL4slbTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbTotalConnections.setStatus("mandatory")
_SnL4slbLimitExceeds_Type = Integer32
_SnL4slbLimitExceeds_Object = MibScalar
snL4slbLimitExceeds = _SnL4slbLimitExceeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 5),
    _SnL4slbLimitExceeds_Type()
)
snL4slbLimitExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbLimitExceeds.setStatus("mandatory")
_SnL4slbForwardTraffic_Type = Counter32
_SnL4slbForwardTraffic_Object = MibScalar
snL4slbForwardTraffic = _SnL4slbForwardTraffic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 6),
    _SnL4slbForwardTraffic_Type()
)
snL4slbForwardTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbForwardTraffic.setStatus("mandatory")
_SnL4slbReverseTraffic_Type = Counter32
_SnL4slbReverseTraffic_Object = MibScalar
snL4slbReverseTraffic = _SnL4slbReverseTraffic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 7),
    _SnL4slbReverseTraffic_Type()
)
snL4slbReverseTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbReverseTraffic.setStatus("mandatory")
_SnL4slbDrops_Type = Integer32
_SnL4slbDrops_Object = MibScalar
snL4slbDrops = _SnL4slbDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 8),
    _SnL4slbDrops_Type()
)
snL4slbDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbDrops.setStatus("mandatory")
_SnL4slbDangling_Type = Integer32
_SnL4slbDangling_Object = MibScalar
snL4slbDangling = _SnL4slbDangling_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 9),
    _SnL4slbDangling_Type()
)
snL4slbDangling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbDangling.setStatus("mandatory")
_SnL4slbDisableCount_Type = Integer32
_SnL4slbDisableCount_Object = MibScalar
snL4slbDisableCount = _SnL4slbDisableCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 10),
    _SnL4slbDisableCount_Type()
)
snL4slbDisableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbDisableCount.setStatus("mandatory")
_SnL4slbAged_Type = Integer32
_SnL4slbAged_Object = MibScalar
snL4slbAged = _SnL4slbAged_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 11),
    _SnL4slbAged_Type()
)
snL4slbAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbAged.setStatus("mandatory")
_SnL4slbFinished_Type = Integer32
_SnL4slbFinished_Object = MibScalar
snL4slbFinished = _SnL4slbFinished_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 12),
    _SnL4slbFinished_Type()
)
snL4slbFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4slbFinished.setStatus("mandatory")
_SnL4FreeSessionCount_Type = Integer32
_SnL4FreeSessionCount_Object = MibScalar
snL4FreeSessionCount = _SnL4FreeSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 13),
    _SnL4FreeSessionCount_Type()
)
snL4FreeSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4FreeSessionCount.setStatus("mandatory")


class _SnL4BackupInterface_Type(Integer32):
    """Custom type snL4BackupInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 26),
    )


_SnL4BackupInterface_Type.__name__ = "Integer32"
_SnL4BackupInterface_Object = MibScalar
snL4BackupInterface = _SnL4BackupInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 14),
    _SnL4BackupInterface_Type()
)
snL4BackupInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BackupInterface.setStatus("mandatory")
_SnL4BackupMacAddr_Type = PhysAddress
_SnL4BackupMacAddr_Object = MibScalar
snL4BackupMacAddr = _SnL4BackupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 15),
    _SnL4BackupMacAddr_Type()
)
snL4BackupMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BackupMacAddr.setStatus("mandatory")
_SnL4Active_Type = L4Flag
_SnL4Active_Object = MibScalar
snL4Active = _SnL4Active_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 16),
    _SnL4Active_Type()
)
snL4Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4Active.setStatus("mandatory")
_SnL4Redundancy_Type = Integer32
_SnL4Redundancy_Object = MibScalar
snL4Redundancy = _SnL4Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 17),
    _SnL4Redundancy_Type()
)
snL4Redundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4Redundancy.setStatus("mandatory")
_SnL4Backup_Type = L4Flag
_SnL4Backup_Object = MibScalar
snL4Backup = _SnL4Backup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 18),
    _SnL4Backup_Type()
)
snL4Backup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4Backup.setStatus("mandatory")
_SnL4BecomeActive_Type = Integer32
_SnL4BecomeActive_Object = MibScalar
snL4BecomeActive = _SnL4BecomeActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 19),
    _SnL4BecomeActive_Type()
)
snL4BecomeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4BecomeActive.setStatus("mandatory")
_SnL4BecomeStandBy_Type = Integer32
_SnL4BecomeStandBy_Object = MibScalar
snL4BecomeStandBy = _SnL4BecomeStandBy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 20),
    _SnL4BecomeStandBy_Type()
)
snL4BecomeStandBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4BecomeStandBy.setStatus("mandatory")


class _SnL4BackupState_Type(Integer32):
    """Custom type snL4BackupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("slbSyncComplete", 0),
          ("slbSyncReqL4", 4),
          ("slbSyncReqMap", 1),
          ("slbSyncreqMac", 2),
          ("slbSyncreqServers", 3))
    )


_SnL4BackupState_Type.__name__ = "Integer32"
_SnL4BackupState_Object = MibScalar
snL4BackupState = _SnL4BackupState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 21),
    _SnL4BackupState_Type()
)
snL4BackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4BackupState.setStatus("mandatory")
_SnL4NoPDUSent_Type = Integer32
_SnL4NoPDUSent_Object = MibScalar
snL4NoPDUSent = _SnL4NoPDUSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 22),
    _SnL4NoPDUSent_Type()
)
snL4NoPDUSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4NoPDUSent.setStatus("mandatory")
_SnL4NoPDUCount_Type = Integer32
_SnL4NoPDUCount_Object = MibScalar
snL4NoPDUCount = _SnL4NoPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 23),
    _SnL4NoPDUCount_Type()
)
snL4NoPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4NoPDUCount.setStatus("mandatory")
_SnL4NoPortMap_Type = Integer32
_SnL4NoPortMap_Object = MibScalar
snL4NoPortMap = _SnL4NoPortMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 24),
    _SnL4NoPortMap_Type()
)
snL4NoPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4NoPortMap.setStatus("mandatory")
_SnL4unsuccessfulConn_Type = Integer32
_SnL4unsuccessfulConn_Object = MibScalar
snL4unsuccessfulConn = _SnL4unsuccessfulConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 25),
    _SnL4unsuccessfulConn_Type()
)
snL4unsuccessfulConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4unsuccessfulConn.setStatus("mandatory")


class _SnL4PingInterval_Type(Integer32):
    """Custom type snL4PingInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SnL4PingInterval_Type.__name__ = "Integer32"
_SnL4PingInterval_Object = MibScalar
snL4PingInterval = _SnL4PingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 26),
    _SnL4PingInterval_Type()
)
snL4PingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PingInterval.setStatus("mandatory")


class _SnL4PingRetry_Type(Integer32):
    """Custom type snL4PingRetry based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SnL4PingRetry_Type.__name__ = "Integer32"
_SnL4PingRetry_Object = MibScalar
snL4PingRetry = _SnL4PingRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 27),
    _SnL4PingRetry_Type()
)
snL4PingRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PingRetry.setStatus("mandatory")


class _SnL4TcpAge_Type(Integer32):
    """Custom type snL4TcpAge based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_SnL4TcpAge_Type.__name__ = "Integer32"
_SnL4TcpAge_Object = MibScalar
snL4TcpAge = _SnL4TcpAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 28),
    _SnL4TcpAge_Type()
)
snL4TcpAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4TcpAge.setStatus("mandatory")


class _SnL4UdpAge_Type(Integer32):
    """Custom type snL4UdpAge based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 60),
    )


_SnL4UdpAge_Type.__name__ = "Integer32"
_SnL4UdpAge_Object = MibScalar
snL4UdpAge = _SnL4UdpAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 29),
    _SnL4UdpAge_Type()
)
snL4UdpAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4UdpAge.setStatus("mandatory")


class _SnL4EnableMaxSessionLimitReachedTrap_Type(Integer32):
    """Custom type snL4EnableMaxSessionLimitReachedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableMaxSessionLimitReachedTrap_Type.__name__ = "Integer32"
_SnL4EnableMaxSessionLimitReachedTrap_Object = MibScalar
snL4EnableMaxSessionLimitReachedTrap = _SnL4EnableMaxSessionLimitReachedTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 30),
    _SnL4EnableMaxSessionLimitReachedTrap_Type()
)
snL4EnableMaxSessionLimitReachedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableMaxSessionLimitReachedTrap.setStatus("mandatory")


class _SnL4EnableTcpSynLimitReachedTrap_Type(Integer32):
    """Custom type snL4EnableTcpSynLimitReachedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableTcpSynLimitReachedTrap_Type.__name__ = "Integer32"
_SnL4EnableTcpSynLimitReachedTrap_Object = MibScalar
snL4EnableTcpSynLimitReachedTrap = _SnL4EnableTcpSynLimitReachedTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 31),
    _SnL4EnableTcpSynLimitReachedTrap_Type()
)
snL4EnableTcpSynLimitReachedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableTcpSynLimitReachedTrap.setStatus("mandatory")


class _SnL4EnableRealServerUpTrap_Type(Integer32):
    """Custom type snL4EnableRealServerUpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableRealServerUpTrap_Type.__name__ = "Integer32"
_SnL4EnableRealServerUpTrap_Object = MibScalar
snL4EnableRealServerUpTrap = _SnL4EnableRealServerUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 32),
    _SnL4EnableRealServerUpTrap_Type()
)
snL4EnableRealServerUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableRealServerUpTrap.setStatus("mandatory")


class _SnL4EnableRealServerDownTrap_Type(Integer32):
    """Custom type snL4EnableRealServerDownTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableRealServerDownTrap_Type.__name__ = "Integer32"
_SnL4EnableRealServerDownTrap_Object = MibScalar
snL4EnableRealServerDownTrap = _SnL4EnableRealServerDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 33),
    _SnL4EnableRealServerDownTrap_Type()
)
snL4EnableRealServerDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableRealServerDownTrap.setStatus("mandatory")


class _SnL4EnableRealServerPortUpTrap_Type(Integer32):
    """Custom type snL4EnableRealServerPortUpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableRealServerPortUpTrap_Type.__name__ = "Integer32"
_SnL4EnableRealServerPortUpTrap_Object = MibScalar
snL4EnableRealServerPortUpTrap = _SnL4EnableRealServerPortUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 34),
    _SnL4EnableRealServerPortUpTrap_Type()
)
snL4EnableRealServerPortUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableRealServerPortUpTrap.setStatus("mandatory")


class _SnL4EnableRealServerPortDownTrap_Type(Integer32):
    """Custom type snL4EnableRealServerPortDownTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableRealServerPortDownTrap_Type.__name__ = "Integer32"
_SnL4EnableRealServerPortDownTrap_Object = MibScalar
snL4EnableRealServerPortDownTrap = _SnL4EnableRealServerPortDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 35),
    _SnL4EnableRealServerPortDownTrap_Type()
)
snL4EnableRealServerPortDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableRealServerPortDownTrap.setStatus("mandatory")


class _SnL4EnableRealServerMaxConnLimitReachedTrap_Type(Integer32):
    """Custom type snL4EnableRealServerMaxConnLimitReachedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableRealServerMaxConnLimitReachedTrap_Type.__name__ = "Integer32"
_SnL4EnableRealServerMaxConnLimitReachedTrap_Object = MibScalar
snL4EnableRealServerMaxConnLimitReachedTrap = _SnL4EnableRealServerMaxConnLimitReachedTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 36),
    _SnL4EnableRealServerMaxConnLimitReachedTrap_Type()
)
snL4EnableRealServerMaxConnLimitReachedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableRealServerMaxConnLimitReachedTrap.setStatus("mandatory")


class _SnL4EnableBecomeStandbyTrap_Type(Integer32):
    """Custom type snL4EnableBecomeStandbyTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableBecomeStandbyTrap_Type.__name__ = "Integer32"
_SnL4EnableBecomeStandbyTrap_Object = MibScalar
snL4EnableBecomeStandbyTrap = _SnL4EnableBecomeStandbyTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 37),
    _SnL4EnableBecomeStandbyTrap_Type()
)
snL4EnableBecomeStandbyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableBecomeStandbyTrap.setStatus("mandatory")


class _SnL4EnableBecomeActiveTrap_Type(Integer32):
    """Custom type snL4EnableBecomeActiveTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableBecomeActiveTrap_Type.__name__ = "Integer32"
_SnL4EnableBecomeActiveTrap_Object = MibScalar
snL4EnableBecomeActiveTrap = _SnL4EnableBecomeActiveTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 38),
    _SnL4EnableBecomeActiveTrap_Type()
)
snL4EnableBecomeActiveTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableBecomeActiveTrap.setStatus("mandatory")
_SnL4slbRouterInterfacePortMask_Type = Integer32
_SnL4slbRouterInterfacePortMask_Object = MibScalar
snL4slbRouterInterfacePortMask = _SnL4slbRouterInterfacePortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 39),
    _SnL4slbRouterInterfacePortMask_Type()
)
snL4slbRouterInterfacePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4slbRouterInterfacePortMask.setStatus("deprecated")
_SnL4MaxNumWebCacheGroup_Type = Integer32
_SnL4MaxNumWebCacheGroup_Object = MibScalar
snL4MaxNumWebCacheGroup = _SnL4MaxNumWebCacheGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 40),
    _SnL4MaxNumWebCacheGroup_Type()
)
snL4MaxNumWebCacheGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4MaxNumWebCacheGroup.setStatus("mandatory")
_SnL4MaxNumWebCachePerGroup_Type = Integer32
_SnL4MaxNumWebCachePerGroup_Object = MibScalar
snL4MaxNumWebCachePerGroup = _SnL4MaxNumWebCachePerGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 41),
    _SnL4MaxNumWebCachePerGroup_Type()
)
snL4MaxNumWebCachePerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4MaxNumWebCachePerGroup.setStatus("mandatory")
_SnL4WebCacheStateful_Type = L4Status
_SnL4WebCacheStateful_Object = MibScalar
snL4WebCacheStateful = _SnL4WebCacheStateful_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 42),
    _SnL4WebCacheStateful_Type()
)
snL4WebCacheStateful.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheStateful.setStatus("mandatory")


class _SnL4EnableGslbHealthCheckIpUpTrap_Type(Integer32):
    """Custom type snL4EnableGslbHealthCheckIpUpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbHealthCheckIpUpTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbHealthCheckIpUpTrap_Object = MibScalar
snL4EnableGslbHealthCheckIpUpTrap = _SnL4EnableGslbHealthCheckIpUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 43),
    _SnL4EnableGslbHealthCheckIpUpTrap_Type()
)
snL4EnableGslbHealthCheckIpUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbHealthCheckIpUpTrap.setStatus("mandatory")


class _SnL4EnableGslbHealthCheckIpDownTrap_Type(Integer32):
    """Custom type snL4EnableGslbHealthCheckIpDownTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbHealthCheckIpDownTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbHealthCheckIpDownTrap_Object = MibScalar
snL4EnableGslbHealthCheckIpDownTrap = _SnL4EnableGslbHealthCheckIpDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 44),
    _SnL4EnableGslbHealthCheckIpDownTrap_Type()
)
snL4EnableGslbHealthCheckIpDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbHealthCheckIpDownTrap.setStatus("mandatory")


class _SnL4EnableGslbHealthCheckIpPortUpTrap_Type(Integer32):
    """Custom type snL4EnableGslbHealthCheckIpPortUpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbHealthCheckIpPortUpTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbHealthCheckIpPortUpTrap_Object = MibScalar
snL4EnableGslbHealthCheckIpPortUpTrap = _SnL4EnableGslbHealthCheckIpPortUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 45),
    _SnL4EnableGslbHealthCheckIpPortUpTrap_Type()
)
snL4EnableGslbHealthCheckIpPortUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbHealthCheckIpPortUpTrap.setStatus("mandatory")


class _SnL4EnableGslbHealthCheckIpPortDownTrap_Type(Integer32):
    """Custom type snL4EnableGslbHealthCheckIpPortDownTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbHealthCheckIpPortDownTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbHealthCheckIpPortDownTrap_Object = MibScalar
snL4EnableGslbHealthCheckIpPortDownTrap = _SnL4EnableGslbHealthCheckIpPortDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 46),
    _SnL4EnableGslbHealthCheckIpPortDownTrap_Type()
)
snL4EnableGslbHealthCheckIpPortDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbHealthCheckIpPortDownTrap.setStatus("mandatory")


class _SnL4EnableGslbRemoteGslbSiDownTrap_Type(Integer32):
    """Custom type snL4EnableGslbRemoteGslbSiDownTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbRemoteGslbSiDownTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbRemoteGslbSiDownTrap_Object = MibScalar
snL4EnableGslbRemoteGslbSiDownTrap = _SnL4EnableGslbRemoteGslbSiDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 47),
    _SnL4EnableGslbRemoteGslbSiDownTrap_Type()
)
snL4EnableGslbRemoteGslbSiDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbRemoteGslbSiDownTrap.setStatus("mandatory")


class _SnL4EnableGslbRemoteGslbSiUpTrap_Type(Integer32):
    """Custom type snL4EnableGslbRemoteGslbSiUpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbRemoteGslbSiUpTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbRemoteGslbSiUpTrap_Object = MibScalar
snL4EnableGslbRemoteGslbSiUpTrap = _SnL4EnableGslbRemoteGslbSiUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 48),
    _SnL4EnableGslbRemoteGslbSiUpTrap_Type()
)
snL4EnableGslbRemoteGslbSiUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbRemoteGslbSiUpTrap.setStatus("mandatory")


class _SnL4EnableGslbRemoteSiDownTrap_Type(Integer32):
    """Custom type snL4EnableGslbRemoteSiDownTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbRemoteSiDownTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbRemoteSiDownTrap_Object = MibScalar
snL4EnableGslbRemoteSiDownTrap = _SnL4EnableGslbRemoteSiDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 49),
    _SnL4EnableGslbRemoteSiDownTrap_Type()
)
snL4EnableGslbRemoteSiDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbRemoteSiDownTrap.setStatus("mandatory")


class _SnL4EnableGslbRemoteSiUpTrap_Type(Integer32):
    """Custom type snL4EnableGslbRemoteSiUpTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4EnableGslbRemoteSiUpTrap_Type.__name__ = "Integer32"
_SnL4EnableGslbRemoteSiUpTrap_Object = MibScalar
snL4EnableGslbRemoteSiUpTrap = _SnL4EnableGslbRemoteSiUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 50),
    _SnL4EnableGslbRemoteSiUpTrap_Type()
)
snL4EnableGslbRemoteSiUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4EnableGslbRemoteSiUpTrap.setStatus("mandatory")
_SnL4slbRouterInterfacePortList_Type = OctetString
_SnL4slbRouterInterfacePortList_Object = MibScalar
snL4slbRouterInterfacePortList = _SnL4slbRouterInterfacePortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 1, 51),
    _SnL4slbRouterInterfacePortList_Type()
)
snL4slbRouterInterfacePortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4slbRouterInterfacePortList.setStatus("mandatory")
_SnL4VirtualServer_ObjectIdentity = ObjectIdentity
snL4VirtualServer = _SnL4VirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2)
)
_SnL4VirtualServerTable_Object = MibTable
snL4VirtualServerTable = _SnL4VirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerTable.setStatus("mandatory")
_SnL4VirtualServerEntry_Object = MibTableRow
snL4VirtualServerEntry = _SnL4VirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1)
)
snL4VirtualServerEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerEntry.setStatus("mandatory")


class _SnL4VirtualServerIndex_Type(Integer32):
    """Custom type snL4VirtualServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnL4VirtualServerIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerIndex_Object = MibTableColumn
snL4VirtualServerIndex = _SnL4VirtualServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 1),
    _SnL4VirtualServerIndex_Type()
)
snL4VirtualServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerIndex.setStatus("mandatory")
_SnL4VirtualServerName_Type = L4ServerName
_SnL4VirtualServerName_Object = MibTableColumn
snL4VirtualServerName = _SnL4VirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 2),
    _SnL4VirtualServerName_Type()
)
snL4VirtualServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerName.setStatus("mandatory")
_SnL4VirtualServerVirtualIP_Type = IpAddress
_SnL4VirtualServerVirtualIP_Object = MibTableColumn
snL4VirtualServerVirtualIP = _SnL4VirtualServerVirtualIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 3),
    _SnL4VirtualServerVirtualIP_Type()
)
snL4VirtualServerVirtualIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerVirtualIP.setStatus("mandatory")
_SnL4VirtualServerAdminStatus_Type = L4Status
_SnL4VirtualServerAdminStatus_Object = MibTableColumn
snL4VirtualServerAdminStatus = _SnL4VirtualServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 4),
    _SnL4VirtualServerAdminStatus_Type()
)
snL4VirtualServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerAdminStatus.setStatus("mandatory")


class _SnL4VirtualServerSDAType_Type(Integer32):
    """Custom type snL4VirtualServerSDAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("leastconnection", 1),
          ("roundrobin", 2),
          ("weighted", 3))
    )


_SnL4VirtualServerSDAType_Type.__name__ = "Integer32"
_SnL4VirtualServerSDAType_Object = MibTableColumn
snL4VirtualServerSDAType = _SnL4VirtualServerSDAType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 5),
    _SnL4VirtualServerSDAType_Type()
)
snL4VirtualServerSDAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerSDAType.setStatus("mandatory")
_SnL4VirtualServerRowStatus_Type = L4RowSts
_SnL4VirtualServerRowStatus_Object = MibTableColumn
snL4VirtualServerRowStatus = _SnL4VirtualServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 6),
    _SnL4VirtualServerRowStatus_Type()
)
snL4VirtualServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerRowStatus.setStatus("mandatory")
_SnL4VirtualServerDeleteState_Type = L4DeleteState
_SnL4VirtualServerDeleteState_Object = MibTableColumn
snL4VirtualServerDeleteState = _SnL4VirtualServerDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 2, 1, 1, 7),
    _SnL4VirtualServerDeleteState_Type()
)
snL4VirtualServerDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerDeleteState.setStatus("mandatory")
_SnL4RealServer_ObjectIdentity = ObjectIdentity
snL4RealServer = _SnL4RealServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3)
)
_SnL4RealServerTable_Object = MibTable
snL4RealServerTable = _SnL4RealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerTable.setStatus("mandatory")
_SnL4RealServerEntry_Object = MibTableRow
snL4RealServerEntry = _SnL4RealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1)
)
snL4RealServerEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerEntry.setStatus("mandatory")


class _SnL4RealServerIndex_Type(Integer32):
    """Custom type snL4RealServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SnL4RealServerIndex_Type.__name__ = "Integer32"
_SnL4RealServerIndex_Object = MibTableColumn
snL4RealServerIndex = _SnL4RealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 1),
    _SnL4RealServerIndex_Type()
)
snL4RealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerIndex.setStatus("mandatory")
_SnL4RealServerName_Type = L4ServerName
_SnL4RealServerName_Object = MibTableColumn
snL4RealServerName = _SnL4RealServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 2),
    _SnL4RealServerName_Type()
)
snL4RealServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerName.setStatus("mandatory")
_SnL4RealServerIP_Type = IpAddress
_SnL4RealServerIP_Object = MibTableColumn
snL4RealServerIP = _SnL4RealServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 3),
    _SnL4RealServerIP_Type()
)
snL4RealServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerIP.setStatus("mandatory")
_SnL4RealServerAdminStatus_Type = L4Status
_SnL4RealServerAdminStatus_Object = MibTableColumn
snL4RealServerAdminStatus = _SnL4RealServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 4),
    _SnL4RealServerAdminStatus_Type()
)
snL4RealServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerAdminStatus.setStatus("mandatory")


class _SnL4RealServerMaxConnections_Type(Integer32):
    """Custom type snL4RealServerMaxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SnL4RealServerMaxConnections_Type.__name__ = "Integer32"
_SnL4RealServerMaxConnections_Object = MibTableColumn
snL4RealServerMaxConnections = _SnL4RealServerMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 5),
    _SnL4RealServerMaxConnections_Type()
)
snL4RealServerMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerMaxConnections.setStatus("mandatory")


class _SnL4RealServerWeight_Type(Integer32):
    """Custom type snL4RealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SnL4RealServerWeight_Type.__name__ = "Integer32"
_SnL4RealServerWeight_Object = MibTableColumn
snL4RealServerWeight = _SnL4RealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 6),
    _SnL4RealServerWeight_Type()
)
snL4RealServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerWeight.setStatus("mandatory")
_SnL4RealServerRowStatus_Type = L4RowSts
_SnL4RealServerRowStatus_Object = MibTableColumn
snL4RealServerRowStatus = _SnL4RealServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 7),
    _SnL4RealServerRowStatus_Type()
)
snL4RealServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerRowStatus.setStatus("mandatory")
_SnL4RealServerDeleteState_Type = L4DeleteState
_SnL4RealServerDeleteState_Object = MibTableColumn
snL4RealServerDeleteState = _SnL4RealServerDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 3, 1, 1, 8),
    _SnL4RealServerDeleteState_Type()
)
snL4RealServerDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerDeleteState.setStatus("mandatory")
_SnL4VirtualServerPort_ObjectIdentity = ObjectIdentity
snL4VirtualServerPort = _SnL4VirtualServerPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4)
)
_SnL4VirtualServerPortTable_Object = MibTable
snL4VirtualServerPortTable = _SnL4VirtualServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortTable.setStatus("mandatory")
_SnL4VirtualServerPortEntry_Object = MibTableRow
snL4VirtualServerPortEntry = _SnL4VirtualServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1)
)
snL4VirtualServerPortEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortEntry.setStatus("mandatory")


class _SnL4VirtualServerPortIndex_Type(Integer32):
    """Custom type snL4VirtualServerPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SnL4VirtualServerPortIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerPortIndex_Object = MibTableColumn
snL4VirtualServerPortIndex = _SnL4VirtualServerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 1),
    _SnL4VirtualServerPortIndex_Type()
)
snL4VirtualServerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortIndex.setStatus("mandatory")
_SnL4VirtualServerPortServerName_Type = L4ServerName
_SnL4VirtualServerPortServerName_Object = MibTableColumn
snL4VirtualServerPortServerName = _SnL4VirtualServerPortServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 2),
    _SnL4VirtualServerPortServerName_Type()
)
snL4VirtualServerPortServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortServerName.setStatus("mandatory")


class _SnL4VirtualServerPortPort_Type(Integer32):
    """Custom type snL4VirtualServerPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4VirtualServerPortPort_Type.__name__ = "Integer32"
_SnL4VirtualServerPortPort_Object = MibTableColumn
snL4VirtualServerPortPort = _SnL4VirtualServerPortPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 3),
    _SnL4VirtualServerPortPort_Type()
)
snL4VirtualServerPortPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortPort.setStatus("mandatory")
_SnL4VirtualServerPortAdminStatus_Type = L4Status
_SnL4VirtualServerPortAdminStatus_Object = MibTableColumn
snL4VirtualServerPortAdminStatus = _SnL4VirtualServerPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 4),
    _SnL4VirtualServerPortAdminStatus_Type()
)
snL4VirtualServerPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortAdminStatus.setStatus("mandatory")


class _SnL4VirtualServerPortSticky_Type(Integer32):
    """Custom type snL4VirtualServerPortSticky based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4VirtualServerPortSticky_Type.__name__ = "Integer32"
_SnL4VirtualServerPortSticky_Object = MibTableColumn
snL4VirtualServerPortSticky = _SnL4VirtualServerPortSticky_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 5),
    _SnL4VirtualServerPortSticky_Type()
)
snL4VirtualServerPortSticky.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortSticky.setStatus("mandatory")


class _SnL4VirtualServerPortConcurrent_Type(Integer32):
    """Custom type snL4VirtualServerPortConcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4VirtualServerPortConcurrent_Type.__name__ = "Integer32"
_SnL4VirtualServerPortConcurrent_Object = MibTableColumn
snL4VirtualServerPortConcurrent = _SnL4VirtualServerPortConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 6),
    _SnL4VirtualServerPortConcurrent_Type()
)
snL4VirtualServerPortConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortConcurrent.setStatus("mandatory")
_SnL4VirtualServerPortRowStatus_Type = L4RowSts
_SnL4VirtualServerPortRowStatus_Object = MibTableColumn
snL4VirtualServerPortRowStatus = _SnL4VirtualServerPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 7),
    _SnL4VirtualServerPortRowStatus_Type()
)
snL4VirtualServerPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortRowStatus.setStatus("mandatory")
_SnL4VirtualServerPortDeleteState_Type = L4DeleteState
_SnL4VirtualServerPortDeleteState_Object = MibTableColumn
snL4VirtualServerPortDeleteState = _SnL4VirtualServerPortDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 4, 1, 1, 8),
    _SnL4VirtualServerPortDeleteState_Type()
)
snL4VirtualServerPortDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortDeleteState.setStatus("mandatory")
_SnL4RealServerPort_ObjectIdentity = ObjectIdentity
snL4RealServerPort = _SnL4RealServerPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5)
)
_SnL4RealServerPortTable_Object = MibTable
snL4RealServerPortTable = _SnL4RealServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerPortTable.setStatus("mandatory")
_SnL4RealServerPortEntry_Object = MibTableRow
snL4RealServerPortEntry = _SnL4RealServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1)
)
snL4RealServerPortEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerPortEntry.setStatus("mandatory")


class _SnL4RealServerPortIndex_Type(Integer32):
    """Custom type snL4RealServerPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SnL4RealServerPortIndex_Type.__name__ = "Integer32"
_SnL4RealServerPortIndex_Object = MibTableColumn
snL4RealServerPortIndex = _SnL4RealServerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1, 1),
    _SnL4RealServerPortIndex_Type()
)
snL4RealServerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortIndex.setStatus("mandatory")
_SnL4RealServerPortServerName_Type = L4ServerName
_SnL4RealServerPortServerName_Object = MibTableColumn
snL4RealServerPortServerName = _SnL4RealServerPortServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1, 2),
    _SnL4RealServerPortServerName_Type()
)
snL4RealServerPortServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortServerName.setStatus("mandatory")


class _SnL4RealServerPortPort_Type(Integer32):
    """Custom type snL4RealServerPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4RealServerPortPort_Type.__name__ = "Integer32"
_SnL4RealServerPortPort_Object = MibTableColumn
snL4RealServerPortPort = _SnL4RealServerPortPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1, 3),
    _SnL4RealServerPortPort_Type()
)
snL4RealServerPortPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortPort.setStatus("mandatory")
_SnL4RealServerPortAdminStatus_Type = L4Status
_SnL4RealServerPortAdminStatus_Object = MibTableColumn
snL4RealServerPortAdminStatus = _SnL4RealServerPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1, 4),
    _SnL4RealServerPortAdminStatus_Type()
)
snL4RealServerPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortAdminStatus.setStatus("mandatory")
_SnL4RealServerPortRowStatus_Type = L4RowSts
_SnL4RealServerPortRowStatus_Object = MibTableColumn
snL4RealServerPortRowStatus = _SnL4RealServerPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1, 5),
    _SnL4RealServerPortRowStatus_Type()
)
snL4RealServerPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortRowStatus.setStatus("mandatory")
_SnL4RealServerPortDeleteState_Type = L4DeleteState
_SnL4RealServerPortDeleteState_Object = MibTableColumn
snL4RealServerPortDeleteState = _SnL4RealServerPortDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 5, 1, 1, 6),
    _SnL4RealServerPortDeleteState_Type()
)
snL4RealServerPortDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortDeleteState.setStatus("mandatory")
_SnL4Bind_ObjectIdentity = ObjectIdentity
snL4Bind = _SnL4Bind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6)
)
_SnL4BindTable_Object = MibTable
snL4BindTable = _SnL4BindTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1)
)
if mibBuilder.loadTexts:
    snL4BindTable.setStatus("mandatory")
_SnL4BindEntry_Object = MibTableRow
snL4BindEntry = _SnL4BindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1)
)
snL4BindEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4BindIndex"),
)
if mibBuilder.loadTexts:
    snL4BindEntry.setStatus("mandatory")


class _SnL4BindIndex_Type(Integer32):
    """Custom type snL4BindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SnL4BindIndex_Type.__name__ = "Integer32"
_SnL4BindIndex_Object = MibTableColumn
snL4BindIndex = _SnL4BindIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1, 1),
    _SnL4BindIndex_Type()
)
snL4BindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4BindIndex.setStatus("mandatory")
_SnL4BindVirtualServerName_Type = L4ServerName
_SnL4BindVirtualServerName_Object = MibTableColumn
snL4BindVirtualServerName = _SnL4BindVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1, 2),
    _SnL4BindVirtualServerName_Type()
)
snL4BindVirtualServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BindVirtualServerName.setStatus("mandatory")


class _SnL4BindVirtualPortNumber_Type(Integer32):
    """Custom type snL4BindVirtualPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4BindVirtualPortNumber_Type.__name__ = "Integer32"
_SnL4BindVirtualPortNumber_Object = MibTableColumn
snL4BindVirtualPortNumber = _SnL4BindVirtualPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1, 3),
    _SnL4BindVirtualPortNumber_Type()
)
snL4BindVirtualPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BindVirtualPortNumber.setStatus("mandatory")
_SnL4BindRealServerName_Type = L4ServerName
_SnL4BindRealServerName_Object = MibTableColumn
snL4BindRealServerName = _SnL4BindRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1, 4),
    _SnL4BindRealServerName_Type()
)
snL4BindRealServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BindRealServerName.setStatus("mandatory")


class _SnL4BindRealPortNumber_Type(Integer32):
    """Custom type snL4BindRealPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4BindRealPortNumber_Type.__name__ = "Integer32"
_SnL4BindRealPortNumber_Object = MibTableColumn
snL4BindRealPortNumber = _SnL4BindRealPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1, 5),
    _SnL4BindRealPortNumber_Type()
)
snL4BindRealPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BindRealPortNumber.setStatus("mandatory")


class _SnL4BindRowStatus_Type(Integer32):
    """Custom type snL4BindRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnL4BindRowStatus_Type.__name__ = "Integer32"
_SnL4BindRowStatus_Object = MibTableColumn
snL4BindRowStatus = _SnL4BindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 6, 1, 1, 6),
    _SnL4BindRowStatus_Type()
)
snL4BindRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4BindRowStatus.setStatus("mandatory")
_SnL4VirtualServerStatus_ObjectIdentity = ObjectIdentity
snL4VirtualServerStatus = _SnL4VirtualServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7)
)
_SnL4VirtualServerStatusTable_Object = MibTable
snL4VirtualServerStatusTable = _SnL4VirtualServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerStatusTable.setStatus("mandatory")
_SnL4VirtualServerStatusEntry_Object = MibTableRow
snL4VirtualServerStatusEntry = _SnL4VirtualServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1, 1)
)
snL4VirtualServerStatusEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerStatusIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerStatusEntry.setStatus("mandatory")


class _SnL4VirtualServerStatusIndex_Type(Integer32):
    """Custom type snL4VirtualServerStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnL4VirtualServerStatusIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerStatusIndex_Object = MibTableColumn
snL4VirtualServerStatusIndex = _SnL4VirtualServerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1, 1, 1),
    _SnL4VirtualServerStatusIndex_Type()
)
snL4VirtualServerStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatusIndex.setStatus("mandatory")
_SnL4VirtualServerStatusName_Type = L4ServerName
_SnL4VirtualServerStatusName_Object = MibTableColumn
snL4VirtualServerStatusName = _SnL4VirtualServerStatusName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1, 1, 2),
    _SnL4VirtualServerStatusName_Type()
)
snL4VirtualServerStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatusName.setStatus("mandatory")
_SnL4VirtualServerStatusReceivePkts_Type = Counter32
_SnL4VirtualServerStatusReceivePkts_Object = MibTableColumn
snL4VirtualServerStatusReceivePkts = _SnL4VirtualServerStatusReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1, 1, 3),
    _SnL4VirtualServerStatusReceivePkts_Type()
)
snL4VirtualServerStatusReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatusReceivePkts.setStatus("mandatory")
_SnL4VirtualServerStatusTransmitPkts_Type = Counter32
_SnL4VirtualServerStatusTransmitPkts_Object = MibTableColumn
snL4VirtualServerStatusTransmitPkts = _SnL4VirtualServerStatusTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1, 1, 4),
    _SnL4VirtualServerStatusTransmitPkts_Type()
)
snL4VirtualServerStatusTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatusTransmitPkts.setStatus("mandatory")
_SnL4VirtualServerStatusTotalConnections_Type = Counter32
_SnL4VirtualServerStatusTotalConnections_Object = MibTableColumn
snL4VirtualServerStatusTotalConnections = _SnL4VirtualServerStatusTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 7, 1, 1, 5),
    _SnL4VirtualServerStatusTotalConnections_Type()
)
snL4VirtualServerStatusTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatusTotalConnections.setStatus("mandatory")
_SnL4RealServerStatus_ObjectIdentity = ObjectIdentity
snL4RealServerStatus = _SnL4RealServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8)
)
_SnL4RealServerStatusTable_Object = MibTable
snL4RealServerStatusTable = _SnL4RealServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerStatusTable.setStatus("mandatory")
_SnL4RealServerStatusEntry_Object = MibTableRow
snL4RealServerStatusEntry = _SnL4RealServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1)
)
snL4RealServerStatusEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerStatusIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerStatusEntry.setStatus("mandatory")


class _SnL4RealServerStatusIndex_Type(Integer32):
    """Custom type snL4RealServerStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SnL4RealServerStatusIndex_Type.__name__ = "Integer32"
_SnL4RealServerStatusIndex_Object = MibTableColumn
snL4RealServerStatusIndex = _SnL4RealServerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 1),
    _SnL4RealServerStatusIndex_Type()
)
snL4RealServerStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusIndex.setStatus("mandatory")
_SnL4RealServerStatusName_Type = L4ServerName
_SnL4RealServerStatusName_Object = MibTableColumn
snL4RealServerStatusName = _SnL4RealServerStatusName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 2),
    _SnL4RealServerStatusName_Type()
)
snL4RealServerStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusName.setStatus("mandatory")
_SnL4RealServerStatusRealIP_Type = IpAddress
_SnL4RealServerStatusRealIP_Object = MibTableColumn
snL4RealServerStatusRealIP = _SnL4RealServerStatusRealIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 3),
    _SnL4RealServerStatusRealIP_Type()
)
snL4RealServerStatusRealIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusRealIP.setStatus("mandatory")
_SnL4RealServerStatusReceivePkts_Type = Counter32
_SnL4RealServerStatusReceivePkts_Object = MibTableColumn
snL4RealServerStatusReceivePkts = _SnL4RealServerStatusReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 4),
    _SnL4RealServerStatusReceivePkts_Type()
)
snL4RealServerStatusReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusReceivePkts.setStatus("mandatory")
_SnL4RealServerStatusTransmitPkts_Type = Counter32
_SnL4RealServerStatusTransmitPkts_Object = MibTableColumn
snL4RealServerStatusTransmitPkts = _SnL4RealServerStatusTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 5),
    _SnL4RealServerStatusTransmitPkts_Type()
)
snL4RealServerStatusTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusTransmitPkts.setStatus("mandatory")
_SnL4RealServerStatusCurConnections_Type = Integer32
_SnL4RealServerStatusCurConnections_Object = MibTableColumn
snL4RealServerStatusCurConnections = _SnL4RealServerStatusCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 6),
    _SnL4RealServerStatusCurConnections_Type()
)
snL4RealServerStatusCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusCurConnections.setStatus("mandatory")
_SnL4RealServerStatusTotalConnections_Type = Counter32
_SnL4RealServerStatusTotalConnections_Object = MibTableColumn
snL4RealServerStatusTotalConnections = _SnL4RealServerStatusTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 7),
    _SnL4RealServerStatusTotalConnections_Type()
)
snL4RealServerStatusTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusTotalConnections.setStatus("mandatory")
_SnL4RealServerStatusAge_Type = Integer32
_SnL4RealServerStatusAge_Object = MibTableColumn
snL4RealServerStatusAge = _SnL4RealServerStatusAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 8),
    _SnL4RealServerStatusAge_Type()
)
snL4RealServerStatusAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusAge.setStatus("mandatory")


class _SnL4RealServerStatusState_Type(Integer32):
    """Custom type snL4RealServerStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("serveractive", 6),
          ("serverdisabled", 0),
          ("serverenabled", 1),
          ("serverfailed", 2),
          ("servershutdown", 5),
          ("serversuspect", 4),
          ("servertesting", 3))
    )


_SnL4RealServerStatusState_Type.__name__ = "Integer32"
_SnL4RealServerStatusState_Object = MibTableColumn
snL4RealServerStatusState = _SnL4RealServerStatusState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 9),
    _SnL4RealServerStatusState_Type()
)
snL4RealServerStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusState.setStatus("mandatory")
_SnL4RealServerStatusReassignments_Type = Integer32
_SnL4RealServerStatusReassignments_Object = MibTableColumn
snL4RealServerStatusReassignments = _SnL4RealServerStatusReassignments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 10),
    _SnL4RealServerStatusReassignments_Type()
)
snL4RealServerStatusReassignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusReassignments.setStatus("mandatory")
_SnL4RealServerStatusReassignmentLimit_Type = Integer32
_SnL4RealServerStatusReassignmentLimit_Object = MibTableColumn
snL4RealServerStatusReassignmentLimit = _SnL4RealServerStatusReassignmentLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 11),
    _SnL4RealServerStatusReassignmentLimit_Type()
)
snL4RealServerStatusReassignmentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusReassignmentLimit.setStatus("mandatory")
_SnL4RealServerStatusFailedPortExists_Type = Integer32
_SnL4RealServerStatusFailedPortExists_Object = MibTableColumn
snL4RealServerStatusFailedPortExists = _SnL4RealServerStatusFailedPortExists_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 12),
    _SnL4RealServerStatusFailedPortExists_Type()
)
snL4RealServerStatusFailedPortExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusFailedPortExists.setStatus("mandatory")
_SnL4RealServerStatusFailTime_Type = Integer32
_SnL4RealServerStatusFailTime_Object = MibTableColumn
snL4RealServerStatusFailTime = _SnL4RealServerStatusFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 13),
    _SnL4RealServerStatusFailTime_Type()
)
snL4RealServerStatusFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusFailTime.setStatus("mandatory")
_SnL4RealServerStatusPeakConnections_Type = Integer32
_SnL4RealServerStatusPeakConnections_Object = MibTableColumn
snL4RealServerStatusPeakConnections = _SnL4RealServerStatusPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 8, 1, 1, 14),
    _SnL4RealServerStatusPeakConnections_Type()
)
snL4RealServerStatusPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatusPeakConnections.setStatus("mandatory")
_SnL4VirtualServerPortStatus_ObjectIdentity = ObjectIdentity
snL4VirtualServerPortStatus = _SnL4VirtualServerPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9)
)
_SnL4VirtualServerPortStatusTable_Object = MibTable
snL4VirtualServerPortStatusTable = _SnL4VirtualServerPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusTable.setStatus("mandatory")
_SnL4VirtualServerPortStatusEntry_Object = MibTableRow
snL4VirtualServerPortStatusEntry = _SnL4VirtualServerPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1)
)
snL4VirtualServerPortStatusEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortStatusIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusEntry.setStatus("mandatory")
_SnL4VirtualServerPortStatusIndex_Type = Integer32
_SnL4VirtualServerPortStatusIndex_Object = MibTableColumn
snL4VirtualServerPortStatusIndex = _SnL4VirtualServerPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1, 1),
    _SnL4VirtualServerPortStatusIndex_Type()
)
snL4VirtualServerPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusIndex.setStatus("mandatory")


class _SnL4VirtualServerPortStatusPort_Type(Integer32):
    """Custom type snL4VirtualServerPortStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SnL4VirtualServerPortStatusPort_Type.__name__ = "Integer32"
_SnL4VirtualServerPortStatusPort_Object = MibTableColumn
snL4VirtualServerPortStatusPort = _SnL4VirtualServerPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1, 2),
    _SnL4VirtualServerPortStatusPort_Type()
)
snL4VirtualServerPortStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusPort.setStatus("mandatory")
_SnL4VirtualServerPortStatusServerName_Type = L4ServerName
_SnL4VirtualServerPortStatusServerName_Object = MibTableColumn
snL4VirtualServerPortStatusServerName = _SnL4VirtualServerPortStatusServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1, 3),
    _SnL4VirtualServerPortStatusServerName_Type()
)
snL4VirtualServerPortStatusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusServerName.setStatus("mandatory")
_SnL4VirtualServerPortStatusCurrentConnection_Type = Integer32
_SnL4VirtualServerPortStatusCurrentConnection_Object = MibTableColumn
snL4VirtualServerPortStatusCurrentConnection = _SnL4VirtualServerPortStatusCurrentConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1, 4),
    _SnL4VirtualServerPortStatusCurrentConnection_Type()
)
snL4VirtualServerPortStatusCurrentConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusCurrentConnection.setStatus("mandatory")
_SnL4VirtualServerPortStatusTotalConnection_Type = Counter32
_SnL4VirtualServerPortStatusTotalConnection_Object = MibTableColumn
snL4VirtualServerPortStatusTotalConnection = _SnL4VirtualServerPortStatusTotalConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1, 5),
    _SnL4VirtualServerPortStatusTotalConnection_Type()
)
snL4VirtualServerPortStatusTotalConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusTotalConnection.setStatus("mandatory")
_SnL4VirtualServerPortStatusPeakConnection_Type = Integer32
_SnL4VirtualServerPortStatusPeakConnection_Object = MibTableColumn
snL4VirtualServerPortStatusPeakConnection = _SnL4VirtualServerPortStatusPeakConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 9, 1, 1, 6),
    _SnL4VirtualServerPortStatusPeakConnection_Type()
)
snL4VirtualServerPortStatusPeakConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatusPeakConnection.setStatus("mandatory")
_SnL4RealServerPortStatus_ObjectIdentity = ObjectIdentity
snL4RealServerPortStatus = _SnL4RealServerPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10)
)
_SnL4RealServerPortStatusTable_Object = MibTable
snL4RealServerPortStatusTable = _SnL4RealServerPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerPortStatusTable.setStatus("mandatory")
_SnL4RealServerPortStatusEntry_Object = MibTableRow
snL4RealServerPortStatusEntry = _SnL4RealServerPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1)
)
snL4RealServerPortStatusEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortStatusIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerPortStatusEntry.setStatus("mandatory")


class _SnL4RealServerPortStatusIndex_Type(Integer32):
    """Custom type snL4RealServerPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SnL4RealServerPortStatusIndex_Type.__name__ = "Integer32"
_SnL4RealServerPortStatusIndex_Object = MibTableColumn
snL4RealServerPortStatusIndex = _SnL4RealServerPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 1),
    _SnL4RealServerPortStatusIndex_Type()
)
snL4RealServerPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusIndex.setStatus("mandatory")
_SnL4RealServerPortStatusPort_Type = Integer32
_SnL4RealServerPortStatusPort_Object = MibTableColumn
snL4RealServerPortStatusPort = _SnL4RealServerPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 2),
    _SnL4RealServerPortStatusPort_Type()
)
snL4RealServerPortStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusPort.setStatus("mandatory")
_SnL4RealServerPortStatusServerName_Type = L4ServerName
_SnL4RealServerPortStatusServerName_Object = MibTableColumn
snL4RealServerPortStatusServerName = _SnL4RealServerPortStatusServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 3),
    _SnL4RealServerPortStatusServerName_Type()
)
snL4RealServerPortStatusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusServerName.setStatus("mandatory")
_SnL4RealServerPortStatusReassignCount_Type = Integer32
_SnL4RealServerPortStatusReassignCount_Object = MibTableColumn
snL4RealServerPortStatusReassignCount = _SnL4RealServerPortStatusReassignCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 4),
    _SnL4RealServerPortStatusReassignCount_Type()
)
snL4RealServerPortStatusReassignCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusReassignCount.setStatus("mandatory")


class _SnL4RealServerPortStatusState_Type(Integer32):
    """Custom type snL4RealServerPortStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("active", 6),
          ("awaitDelete", 9),
          ("awaitUnbind", 8),
          ("disabled", 0),
          ("enabled", 1),
          ("failed", 2),
          ("shutdown", 5),
          ("suspect", 4),
          ("testing", 3),
          ("unbound", 7))
    )


_SnL4RealServerPortStatusState_Type.__name__ = "Integer32"
_SnL4RealServerPortStatusState_Object = MibTableColumn
snL4RealServerPortStatusState = _SnL4RealServerPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 5),
    _SnL4RealServerPortStatusState_Type()
)
snL4RealServerPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusState.setStatus("mandatory")
_SnL4RealServerPortStatusFailTime_Type = Integer32
_SnL4RealServerPortStatusFailTime_Object = MibTableColumn
snL4RealServerPortStatusFailTime = _SnL4RealServerPortStatusFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 6),
    _SnL4RealServerPortStatusFailTime_Type()
)
snL4RealServerPortStatusFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusFailTime.setStatus("mandatory")
_SnL4RealServerPortStatusCurrentConnection_Type = Integer32
_SnL4RealServerPortStatusCurrentConnection_Object = MibTableColumn
snL4RealServerPortStatusCurrentConnection = _SnL4RealServerPortStatusCurrentConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 7),
    _SnL4RealServerPortStatusCurrentConnection_Type()
)
snL4RealServerPortStatusCurrentConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusCurrentConnection.setStatus("mandatory")
_SnL4RealServerPortStatusTotalConnection_Type = Counter32
_SnL4RealServerPortStatusTotalConnection_Object = MibTableColumn
snL4RealServerPortStatusTotalConnection = _SnL4RealServerPortStatusTotalConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 8),
    _SnL4RealServerPortStatusTotalConnection_Type()
)
snL4RealServerPortStatusTotalConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusTotalConnection.setStatus("mandatory")
_SnL4RealServerPortStatusRxPkts_Type = Counter32
_SnL4RealServerPortStatusRxPkts_Object = MibTableColumn
snL4RealServerPortStatusRxPkts = _SnL4RealServerPortStatusRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 9),
    _SnL4RealServerPortStatusRxPkts_Type()
)
snL4RealServerPortStatusRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusRxPkts.setStatus("mandatory")
_SnL4RealServerPortStatusTxPkts_Type = Counter32
_SnL4RealServerPortStatusTxPkts_Object = MibTableColumn
snL4RealServerPortStatusTxPkts = _SnL4RealServerPortStatusTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 10),
    _SnL4RealServerPortStatusTxPkts_Type()
)
snL4RealServerPortStatusTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusTxPkts.setStatus("mandatory")
_SnL4RealServerPortStatusRxBytes_Type = Counter32
_SnL4RealServerPortStatusRxBytes_Object = MibTableColumn
snL4RealServerPortStatusRxBytes = _SnL4RealServerPortStatusRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 11),
    _SnL4RealServerPortStatusRxBytes_Type()
)
snL4RealServerPortStatusRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusRxBytes.setStatus("mandatory")
_SnL4RealServerPortStatusTxBytes_Type = Counter32
_SnL4RealServerPortStatusTxBytes_Object = MibTableColumn
snL4RealServerPortStatusTxBytes = _SnL4RealServerPortStatusTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 12),
    _SnL4RealServerPortStatusTxBytes_Type()
)
snL4RealServerPortStatusTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusTxBytes.setStatus("mandatory")
_SnL4RealServerPortStatusPeakConnection_Type = Integer32
_SnL4RealServerPortStatusPeakConnection_Object = MibTableColumn
snL4RealServerPortStatusPeakConnection = _SnL4RealServerPortStatusPeakConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 10, 1, 1, 13),
    _SnL4RealServerPortStatusPeakConnection_Type()
)
snL4RealServerPortStatusPeakConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatusPeakConnection.setStatus("mandatory")
_SnL4Policy_ObjectIdentity = ObjectIdentity
snL4Policy = _SnL4Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11)
)
_SnL4PolicyTable_Object = MibTable
snL4PolicyTable = _SnL4PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1)
)
if mibBuilder.loadTexts:
    snL4PolicyTable.setStatus("mandatory")
_SnL4PolicyEntry_Object = MibTableRow
snL4PolicyEntry = _SnL4PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1)
)
snL4PolicyEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4PolicyId"),
)
if mibBuilder.loadTexts:
    snL4PolicyEntry.setStatus("mandatory")


class _SnL4PolicyId_Type(Integer32):
    """Custom type snL4PolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnL4PolicyId_Type.__name__ = "Integer32"
_SnL4PolicyId_Object = MibTableColumn
snL4PolicyId = _SnL4PolicyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1, 1),
    _SnL4PolicyId_Type()
)
snL4PolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4PolicyId.setStatus("mandatory")


class _SnL4PolicyPriority_Type(Integer32):
    """Custom type snL4PolicyPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4),
          ("level5", 5),
          ("level6", 6),
          ("level7", 7))
    )


_SnL4PolicyPriority_Type.__name__ = "Integer32"
_SnL4PolicyPriority_Object = MibTableColumn
snL4PolicyPriority = _SnL4PolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1, 2),
    _SnL4PolicyPriority_Type()
)
snL4PolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyPriority.setStatus("mandatory")


class _SnL4PolicyScope_Type(Integer32):
    """Custom type snL4PolicyScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("global", 0),
          ("local", 1))
    )


_SnL4PolicyScope_Type.__name__ = "Integer32"
_SnL4PolicyScope_Object = MibTableColumn
snL4PolicyScope = _SnL4PolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1, 3),
    _SnL4PolicyScope_Type()
)
snL4PolicyScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyScope.setStatus("mandatory")


class _SnL4PolicyProtocol_Type(Integer32):
    """Custom type snL4PolicyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 0))
    )


_SnL4PolicyProtocol_Type.__name__ = "Integer32"
_SnL4PolicyProtocol_Object = MibTableColumn
snL4PolicyProtocol = _SnL4PolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1, 4),
    _SnL4PolicyProtocol_Type()
)
snL4PolicyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyProtocol.setStatus("mandatory")


class _SnL4PolicyPort_Type(Integer32):
    """Custom type snL4PolicyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4PolicyPort_Type.__name__ = "Integer32"
_SnL4PolicyPort_Object = MibTableColumn
snL4PolicyPort = _SnL4PolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1, 5),
    _SnL4PolicyPort_Type()
)
snL4PolicyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyPort.setStatus("mandatory")


class _SnL4PolicyRowStatus_Type(Integer32):
    """Custom type snL4PolicyRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnL4PolicyRowStatus_Type.__name__ = "Integer32"
_SnL4PolicyRowStatus_Object = MibTableColumn
snL4PolicyRowStatus = _SnL4PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 11, 1, 1, 6),
    _SnL4PolicyRowStatus_Type()
)
snL4PolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyRowStatus.setStatus("mandatory")
_SnL4PolicyPortAccess_ObjectIdentity = ObjectIdentity
snL4PolicyPortAccess = _SnL4PolicyPortAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 12)
)
_SnL4PolicyPortAccessTable_Object = MibTable
snL4PolicyPortAccessTable = _SnL4PolicyPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 12, 1)
)
if mibBuilder.loadTexts:
    snL4PolicyPortAccessTable.setStatus("mandatory")
_SnL4PolicyPortAccessEntry_Object = MibTableRow
snL4PolicyPortAccessEntry = _SnL4PolicyPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 12, 1, 1)
)
snL4PolicyPortAccessEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4PolicyPortAccessPort"),
)
if mibBuilder.loadTexts:
    snL4PolicyPortAccessEntry.setStatus("mandatory")
_SnL4PolicyPortAccessPort_Type = Integer32
_SnL4PolicyPortAccessPort_Object = MibTableColumn
snL4PolicyPortAccessPort = _SnL4PolicyPortAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 12, 1, 1, 1),
    _SnL4PolicyPortAccessPort_Type()
)
snL4PolicyPortAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4PolicyPortAccessPort.setStatus("mandatory")


class _SnL4PolicyPortAccessList_Type(OctetString):
    """Custom type snL4PolicyPortAccessList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnL4PolicyPortAccessList_Type.__name__ = "OctetString"
_SnL4PolicyPortAccessList_Object = MibTableColumn
snL4PolicyPortAccessList = _SnL4PolicyPortAccessList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 12, 1, 1, 2),
    _SnL4PolicyPortAccessList_Type()
)
snL4PolicyPortAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyPortAccessList.setStatus("mandatory")


class _SnL4PolicyPortAccessRowStatus_Type(Integer32):
    """Custom type snL4PolicyPortAccessRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnL4PolicyPortAccessRowStatus_Type.__name__ = "Integer32"
_SnL4PolicyPortAccessRowStatus_Object = MibTableColumn
snL4PolicyPortAccessRowStatus = _SnL4PolicyPortAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 12, 1, 1, 3),
    _SnL4PolicyPortAccessRowStatus_Type()
)
snL4PolicyPortAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4PolicyPortAccessRowStatus.setStatus("mandatory")
_SnL4Trap_ObjectIdentity = ObjectIdentity
snL4Trap = _SnL4Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 13)
)
_SnL4TrapRealServerIP_Type = IpAddress
_SnL4TrapRealServerIP_Object = MibScalar
snL4TrapRealServerIP = _SnL4TrapRealServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 13, 1),
    _SnL4TrapRealServerIP_Type()
)
snL4TrapRealServerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snL4TrapRealServerIP.setStatus("mandatory")
_SnL4TrapRealServerName_Type = L4ServerName
_SnL4TrapRealServerName_Object = MibScalar
snL4TrapRealServerName = _SnL4TrapRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 13, 2),
    _SnL4TrapRealServerName_Type()
)
snL4TrapRealServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snL4TrapRealServerName.setStatus("mandatory")
_SnL4TrapRealServerPort_Type = Integer32
_SnL4TrapRealServerPort_Object = MibScalar
snL4TrapRealServerPort = _SnL4TrapRealServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 13, 3),
    _SnL4TrapRealServerPort_Type()
)
snL4TrapRealServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snL4TrapRealServerPort.setStatus("mandatory")
_SnL4TrapRealServerCurConnections_Type = Integer32
_SnL4TrapRealServerCurConnections_Object = MibScalar
snL4TrapRealServerCurConnections = _SnL4TrapRealServerCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 13, 4),
    _SnL4TrapRealServerCurConnections_Type()
)
snL4TrapRealServerCurConnections.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snL4TrapRealServerCurConnections.setStatus("mandatory")
_SnL4WebCache_ObjectIdentity = ObjectIdentity
snL4WebCache = _SnL4WebCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14)
)
_SnL4WebCacheTable_Object = MibTable
snL4WebCacheTable = _SnL4WebCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1)
)
if mibBuilder.loadTexts:
    snL4WebCacheTable.setStatus("mandatory")
_SnL4WebCacheEntry_Object = MibTableRow
snL4WebCacheEntry = _SnL4WebCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1)
)
snL4WebCacheEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebCacheIP"),
)
if mibBuilder.loadTexts:
    snL4WebCacheEntry.setStatus("mandatory")
_SnL4WebCacheIP_Type = IpAddress
_SnL4WebCacheIP_Object = MibTableColumn
snL4WebCacheIP = _SnL4WebCacheIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 1),
    _SnL4WebCacheIP_Type()
)
snL4WebCacheIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheIP.setStatus("mandatory")
_SnL4WebCacheName_Type = L4ServerName
_SnL4WebCacheName_Object = MibTableColumn
snL4WebCacheName = _SnL4WebCacheName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 2),
    _SnL4WebCacheName_Type()
)
snL4WebCacheName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheName.setStatus("mandatory")
_SnL4WebCacheAdminStatus_Type = L4Status
_SnL4WebCacheAdminStatus_Object = MibTableColumn
snL4WebCacheAdminStatus = _SnL4WebCacheAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 3),
    _SnL4WebCacheAdminStatus_Type()
)
snL4WebCacheAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheAdminStatus.setStatus("mandatory")


class _SnL4WebCacheMaxConnections_Type(Integer32):
    """Custom type snL4WebCacheMaxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SnL4WebCacheMaxConnections_Type.__name__ = "Integer32"
_SnL4WebCacheMaxConnections_Object = MibTableColumn
snL4WebCacheMaxConnections = _SnL4WebCacheMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 4),
    _SnL4WebCacheMaxConnections_Type()
)
snL4WebCacheMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheMaxConnections.setStatus("mandatory")


class _SnL4WebCacheWeight_Type(Integer32):
    """Custom type snL4WebCacheWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_SnL4WebCacheWeight_Type.__name__ = "Integer32"
_SnL4WebCacheWeight_Object = MibTableColumn
snL4WebCacheWeight = _SnL4WebCacheWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 5),
    _SnL4WebCacheWeight_Type()
)
snL4WebCacheWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheWeight.setStatus("mandatory")
_SnL4WebCacheRowStatus_Type = L4RowSts
_SnL4WebCacheRowStatus_Object = MibTableColumn
snL4WebCacheRowStatus = _SnL4WebCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 6),
    _SnL4WebCacheRowStatus_Type()
)
snL4WebCacheRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheRowStatus.setStatus("mandatory")
_SnL4WebCacheDeleteState_Type = L4DeleteState
_SnL4WebCacheDeleteState_Object = MibTableColumn
snL4WebCacheDeleteState = _SnL4WebCacheDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 14, 1, 1, 7),
    _SnL4WebCacheDeleteState_Type()
)
snL4WebCacheDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheDeleteState.setStatus("mandatory")
_SnL4WebCacheGroup_ObjectIdentity = ObjectIdentity
snL4WebCacheGroup = _SnL4WebCacheGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15)
)
_SnL4WebCacheGroupTable_Object = MibTable
snL4WebCacheGroupTable = _SnL4WebCacheGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1)
)
if mibBuilder.loadTexts:
    snL4WebCacheGroupTable.setStatus("mandatory")
_SnL4WebCacheGroupEntry_Object = MibTableRow
snL4WebCacheGroupEntry = _SnL4WebCacheGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1)
)
snL4WebCacheGroupEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebCacheGroupId"),
)
if mibBuilder.loadTexts:
    snL4WebCacheGroupEntry.setStatus("mandatory")
_SnL4WebCacheGroupId_Type = Integer32
_SnL4WebCacheGroupId_Object = MibTableColumn
snL4WebCacheGroupId = _SnL4WebCacheGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 1),
    _SnL4WebCacheGroupId_Type()
)
snL4WebCacheGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheGroupId.setStatus("mandatory")
_SnL4WebCacheGroupName_Type = L4ServerName
_SnL4WebCacheGroupName_Object = MibTableColumn
snL4WebCacheGroupName = _SnL4WebCacheGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 2),
    _SnL4WebCacheGroupName_Type()
)
snL4WebCacheGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheGroupName.setStatus("mandatory")
_SnL4WebCacheGroupWebCacheIpList_Type = OctetString
_SnL4WebCacheGroupWebCacheIpList_Object = MibTableColumn
snL4WebCacheGroupWebCacheIpList = _SnL4WebCacheGroupWebCacheIpList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 3),
    _SnL4WebCacheGroupWebCacheIpList_Type()
)
snL4WebCacheGroupWebCacheIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheGroupWebCacheIpList.setStatus("mandatory")
_SnL4WebCacheGroupDestMask_Type = IpAddress
_SnL4WebCacheGroupDestMask_Object = MibTableColumn
snL4WebCacheGroupDestMask = _SnL4WebCacheGroupDestMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 4),
    _SnL4WebCacheGroupDestMask_Type()
)
snL4WebCacheGroupDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheGroupDestMask.setStatus("mandatory")
_SnL4WebCacheGroupSrcMask_Type = IpAddress
_SnL4WebCacheGroupSrcMask_Object = MibTableColumn
snL4WebCacheGroupSrcMask = _SnL4WebCacheGroupSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 5),
    _SnL4WebCacheGroupSrcMask_Type()
)
snL4WebCacheGroupSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheGroupSrcMask.setStatus("mandatory")


class _SnL4WebCacheGroupAdminStatus_Type(Integer32):
    """Custom type snL4WebCacheGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4WebCacheGroupAdminStatus_Type.__name__ = "Integer32"
_SnL4WebCacheGroupAdminStatus_Object = MibTableColumn
snL4WebCacheGroupAdminStatus = _SnL4WebCacheGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 6),
    _SnL4WebCacheGroupAdminStatus_Type()
)
snL4WebCacheGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheGroupAdminStatus.setStatus("mandatory")
_SnL4WebCacheGroupRowStatus_Type = L4RowSts
_SnL4WebCacheGroupRowStatus_Object = MibTableColumn
snL4WebCacheGroupRowStatus = _SnL4WebCacheGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 15, 1, 1, 7),
    _SnL4WebCacheGroupRowStatus_Type()
)
snL4WebCacheGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCacheGroupRowStatus.setStatus("mandatory")
_SnL4WebCacheTrafficStats_ObjectIdentity = ObjectIdentity
snL4WebCacheTrafficStats = _SnL4WebCacheTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16)
)
_SnL4WebCacheTrafficStatsTable_Object = MibTable
snL4WebCacheTrafficStatsTable = _SnL4WebCacheTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1)
)
if mibBuilder.loadTexts:
    snL4WebCacheTrafficStatsTable.setStatus("mandatory")
_SnL4WebCacheTrafficStatsEntry_Object = MibTableRow
snL4WebCacheTrafficStatsEntry = _SnL4WebCacheTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1)
)
snL4WebCacheTrafficStatsEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebCacheTrafficIp"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebCacheTrafficPort"),
)
if mibBuilder.loadTexts:
    snL4WebCacheTrafficStatsEntry.setStatus("mandatory")
_SnL4WebCacheTrafficIp_Type = IpAddress
_SnL4WebCacheTrafficIp_Object = MibTableColumn
snL4WebCacheTrafficIp = _SnL4WebCacheTrafficIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 1),
    _SnL4WebCacheTrafficIp_Type()
)
snL4WebCacheTrafficIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheTrafficIp.setStatus("mandatory")


class _SnL4WebCacheTrafficPort_Type(Integer32):
    """Custom type snL4WebCacheTrafficPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4WebCacheTrafficPort_Type.__name__ = "Integer32"
_SnL4WebCacheTrafficPort_Object = MibTableColumn
snL4WebCacheTrafficPort = _SnL4WebCacheTrafficPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 2),
    _SnL4WebCacheTrafficPort_Type()
)
snL4WebCacheTrafficPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheTrafficPort.setStatus("mandatory")
_SnL4WebCacheCurrConnections_Type = Integer32
_SnL4WebCacheCurrConnections_Object = MibTableColumn
snL4WebCacheCurrConnections = _SnL4WebCacheCurrConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 3),
    _SnL4WebCacheCurrConnections_Type()
)
snL4WebCacheCurrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheCurrConnections.setStatus("mandatory")
_SnL4WebCacheTotalConnections_Type = Integer32
_SnL4WebCacheTotalConnections_Object = MibTableColumn
snL4WebCacheTotalConnections = _SnL4WebCacheTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 4),
    _SnL4WebCacheTotalConnections_Type()
)
snL4WebCacheTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheTotalConnections.setStatus("mandatory")
_SnL4WebCacheTxPkts_Type = Counter32
_SnL4WebCacheTxPkts_Object = MibTableColumn
snL4WebCacheTxPkts = _SnL4WebCacheTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 5),
    _SnL4WebCacheTxPkts_Type()
)
snL4WebCacheTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheTxPkts.setStatus("mandatory")
_SnL4WebCacheRxPkts_Type = Counter32
_SnL4WebCacheRxPkts_Object = MibTableColumn
snL4WebCacheRxPkts = _SnL4WebCacheRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 6),
    _SnL4WebCacheRxPkts_Type()
)
snL4WebCacheRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheRxPkts.setStatus("mandatory")
_SnL4WebCacheTxOctets_Type = Counter32
_SnL4WebCacheTxOctets_Object = MibTableColumn
snL4WebCacheTxOctets = _SnL4WebCacheTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 7),
    _SnL4WebCacheTxOctets_Type()
)
snL4WebCacheTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheTxOctets.setStatus("mandatory")
_SnL4WebCacheRxOctets_Type = Counter32
_SnL4WebCacheRxOctets_Object = MibTableColumn
snL4WebCacheRxOctets = _SnL4WebCacheRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 8),
    _SnL4WebCacheRxOctets_Type()
)
snL4WebCacheRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCacheRxOctets.setStatus("mandatory")
_SnL4WebCachePortState_Type = WebCacheState
_SnL4WebCachePortState_Object = MibTableColumn
snL4WebCachePortState = _SnL4WebCachePortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 16, 1, 1, 9),
    _SnL4WebCachePortState_Type()
)
snL4WebCachePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCachePortState.setStatus("mandatory")
_SnL4WebUncachedTrafficStats_ObjectIdentity = ObjectIdentity
snL4WebUncachedTrafficStats = _SnL4WebUncachedTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17)
)
_SnL4WebUncachedTrafficStatsTable_Object = MibTable
snL4WebUncachedTrafficStatsTable = _SnL4WebUncachedTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1)
)
if mibBuilder.loadTexts:
    snL4WebUncachedTrafficStatsTable.setStatus("mandatory")
_SnL4WebUncachedTrafficStatsEntry_Object = MibTableRow
snL4WebUncachedTrafficStatsEntry = _SnL4WebUncachedTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1)
)
snL4WebUncachedTrafficStatsEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebServerPort"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebClientPort"),
)
if mibBuilder.loadTexts:
    snL4WebUncachedTrafficStatsEntry.setStatus("mandatory")
_SnL4WebServerPort_Type = Integer32
_SnL4WebServerPort_Object = MibTableColumn
snL4WebServerPort = _SnL4WebServerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 1),
    _SnL4WebServerPort_Type()
)
snL4WebServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebServerPort.setStatus("mandatory")
_SnL4WebClientPort_Type = Integer32
_SnL4WebClientPort_Object = MibTableColumn
snL4WebClientPort = _SnL4WebClientPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 2),
    _SnL4WebClientPort_Type()
)
snL4WebClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebClientPort.setStatus("mandatory")
_SnL4WebUncachedTxPkts_Type = Counter32
_SnL4WebUncachedTxPkts_Object = MibTableColumn
snL4WebUncachedTxPkts = _SnL4WebUncachedTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 3),
    _SnL4WebUncachedTxPkts_Type()
)
snL4WebUncachedTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebUncachedTxPkts.setStatus("mandatory")
_SnL4WebUncachedRxPkts_Type = Counter32
_SnL4WebUncachedRxPkts_Object = MibTableColumn
snL4WebUncachedRxPkts = _SnL4WebUncachedRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 4),
    _SnL4WebUncachedRxPkts_Type()
)
snL4WebUncachedRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebUncachedRxPkts.setStatus("mandatory")
_SnL4WebUncachedTxOctets_Type = Counter32
_SnL4WebUncachedTxOctets_Object = MibTableColumn
snL4WebUncachedTxOctets = _SnL4WebUncachedTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 5),
    _SnL4WebUncachedTxOctets_Type()
)
snL4WebUncachedTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebUncachedTxOctets.setStatus("mandatory")
_SnL4WebUncachedRxOctets_Type = Counter32
_SnL4WebUncachedRxOctets_Object = MibTableColumn
snL4WebUncachedRxOctets = _SnL4WebUncachedRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 6),
    _SnL4WebUncachedRxOctets_Type()
)
snL4WebUncachedRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebUncachedRxOctets.setStatus("mandatory")


class _SnL4WebServerPortName_Type(DisplayString):
    """Custom type snL4WebServerPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnL4WebServerPortName_Type.__name__ = "DisplayString"
_SnL4WebServerPortName_Object = MibTableColumn
snL4WebServerPortName = _SnL4WebServerPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 7),
    _SnL4WebServerPortName_Type()
)
snL4WebServerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebServerPortName.setStatus("mandatory")


class _SnL4WebClientPortName_Type(DisplayString):
    """Custom type snL4WebClientPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SnL4WebClientPortName_Type.__name__ = "DisplayString"
_SnL4WebClientPortName_Object = MibTableColumn
snL4WebClientPortName = _SnL4WebClientPortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 17, 1, 1, 8),
    _SnL4WebClientPortName_Type()
)
snL4WebClientPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebClientPortName.setStatus("mandatory")
_SnL4WebCachePort_ObjectIdentity = ObjectIdentity
snL4WebCachePort = _SnL4WebCachePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18)
)
_SnL4WebCachePortTable_Object = MibTable
snL4WebCachePortTable = _SnL4WebCachePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1)
)
if mibBuilder.loadTexts:
    snL4WebCachePortTable.setStatus("mandatory")
_SnL4WebCachePortEntry_Object = MibTableRow
snL4WebCachePortEntry = _SnL4WebCachePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1, 1)
)
snL4WebCachePortEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebCachePortServerIp"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4WebCachePortPort"),
)
if mibBuilder.loadTexts:
    snL4WebCachePortEntry.setStatus("mandatory")
_SnL4WebCachePortServerIp_Type = IpAddress
_SnL4WebCachePortServerIp_Object = MibTableColumn
snL4WebCachePortServerIp = _SnL4WebCachePortServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1, 1, 1),
    _SnL4WebCachePortServerIp_Type()
)
snL4WebCachePortServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCachePortServerIp.setStatus("mandatory")


class _SnL4WebCachePortPort_Type(Integer32):
    """Custom type snL4WebCachePortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4WebCachePortPort_Type.__name__ = "Integer32"
_SnL4WebCachePortPort_Object = MibTableColumn
snL4WebCachePortPort = _SnL4WebCachePortPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1, 1, 2),
    _SnL4WebCachePortPort_Type()
)
snL4WebCachePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCachePortPort.setStatus("mandatory")
_SnL4WebCachePortAdminStatus_Type = L4Status
_SnL4WebCachePortAdminStatus_Object = MibTableColumn
snL4WebCachePortAdminStatus = _SnL4WebCachePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1, 1, 3),
    _SnL4WebCachePortAdminStatus_Type()
)
snL4WebCachePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCachePortAdminStatus.setStatus("mandatory")
_SnL4WebCachePortRowStatus_Type = L4RowSts
_SnL4WebCachePortRowStatus_Object = MibTableColumn
snL4WebCachePortRowStatus = _SnL4WebCachePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1, 1, 4),
    _SnL4WebCachePortRowStatus_Type()
)
snL4WebCachePortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4WebCachePortRowStatus.setStatus("mandatory")
_SnL4WebCachePortDeleteState_Type = L4DeleteState
_SnL4WebCachePortDeleteState_Object = MibTableColumn
snL4WebCachePortDeleteState = _SnL4WebCachePortDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 18, 1, 1, 5),
    _SnL4WebCachePortDeleteState_Type()
)
snL4WebCachePortDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4WebCachePortDeleteState.setStatus("mandatory")
_SnL4RealServerCfg_ObjectIdentity = ObjectIdentity
snL4RealServerCfg = _SnL4RealServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19)
)
_SnL4RealServerCfgTable_Object = MibTable
snL4RealServerCfgTable = _SnL4RealServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerCfgTable.setStatus("mandatory")
_SnL4RealServerCfgEntry_Object = MibTableRow
snL4RealServerCfgEntry = _SnL4RealServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1)
)
snL4RealServerCfgEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerCfgIP"),
)
if mibBuilder.loadTexts:
    snL4RealServerCfgEntry.setStatus("mandatory")
_SnL4RealServerCfgIP_Type = IpAddress
_SnL4RealServerCfgIP_Object = MibTableColumn
snL4RealServerCfgIP = _SnL4RealServerCfgIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 1),
    _SnL4RealServerCfgIP_Type()
)
snL4RealServerCfgIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerCfgIP.setStatus("mandatory")
_SnL4RealServerCfgName_Type = L4ServerName
_SnL4RealServerCfgName_Object = MibTableColumn
snL4RealServerCfgName = _SnL4RealServerCfgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 2),
    _SnL4RealServerCfgName_Type()
)
snL4RealServerCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerCfgName.setStatus("mandatory")
_SnL4RealServerCfgAdminStatus_Type = L4Status
_SnL4RealServerCfgAdminStatus_Object = MibTableColumn
snL4RealServerCfgAdminStatus = _SnL4RealServerCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 3),
    _SnL4RealServerCfgAdminStatus_Type()
)
snL4RealServerCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerCfgAdminStatus.setStatus("mandatory")


class _SnL4RealServerCfgMaxConnections_Type(Integer32):
    """Custom type snL4RealServerCfgMaxConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SnL4RealServerCfgMaxConnections_Type.__name__ = "Integer32"
_SnL4RealServerCfgMaxConnections_Object = MibTableColumn
snL4RealServerCfgMaxConnections = _SnL4RealServerCfgMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 4),
    _SnL4RealServerCfgMaxConnections_Type()
)
snL4RealServerCfgMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerCfgMaxConnections.setStatus("mandatory")


class _SnL4RealServerCfgWeight_Type(Integer32):
    """Custom type snL4RealServerCfgWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SnL4RealServerCfgWeight_Type.__name__ = "Integer32"
_SnL4RealServerCfgWeight_Object = MibTableColumn
snL4RealServerCfgWeight = _SnL4RealServerCfgWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 5),
    _SnL4RealServerCfgWeight_Type()
)
snL4RealServerCfgWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerCfgWeight.setStatus("mandatory")
_SnL4RealServerCfgRowStatus_Type = L4RowSts
_SnL4RealServerCfgRowStatus_Object = MibTableColumn
snL4RealServerCfgRowStatus = _SnL4RealServerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 6),
    _SnL4RealServerCfgRowStatus_Type()
)
snL4RealServerCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerCfgRowStatus.setStatus("mandatory")
_SnL4RealServerCfgDeleteState_Type = L4DeleteState
_SnL4RealServerCfgDeleteState_Object = MibTableColumn
snL4RealServerCfgDeleteState = _SnL4RealServerCfgDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 19, 1, 1, 7),
    _SnL4RealServerCfgDeleteState_Type()
)
snL4RealServerCfgDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerCfgDeleteState.setStatus("mandatory")
_SnL4RealServerPortCfg_ObjectIdentity = ObjectIdentity
snL4RealServerPortCfg = _SnL4RealServerPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20)
)
_SnL4RealServerPortCfgTable_Object = MibTable
snL4RealServerPortCfgTable = _SnL4RealServerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerPortCfgTable.setStatus("mandatory")
_SnL4RealServerPortCfgEntry_Object = MibTableRow
snL4RealServerPortCfgEntry = _SnL4RealServerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1)
)
snL4RealServerPortCfgEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortCfgIP"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortCfgPort"),
)
if mibBuilder.loadTexts:
    snL4RealServerPortCfgEntry.setStatus("mandatory")
_SnL4RealServerPortCfgIP_Type = IpAddress
_SnL4RealServerPortCfgIP_Object = MibTableColumn
snL4RealServerPortCfgIP = _SnL4RealServerPortCfgIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1, 1),
    _SnL4RealServerPortCfgIP_Type()
)
snL4RealServerPortCfgIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortCfgIP.setStatus("mandatory")
_SnL4RealServerPortCfgServerName_Type = L4ServerName
_SnL4RealServerPortCfgServerName_Object = MibTableColumn
snL4RealServerPortCfgServerName = _SnL4RealServerPortCfgServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1, 2),
    _SnL4RealServerPortCfgServerName_Type()
)
snL4RealServerPortCfgServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortCfgServerName.setStatus("mandatory")


class _SnL4RealServerPortCfgPort_Type(Integer32):
    """Custom type snL4RealServerPortCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4RealServerPortCfgPort_Type.__name__ = "Integer32"
_SnL4RealServerPortCfgPort_Object = MibTableColumn
snL4RealServerPortCfgPort = _SnL4RealServerPortCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1, 3),
    _SnL4RealServerPortCfgPort_Type()
)
snL4RealServerPortCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortCfgPort.setStatus("mandatory")
_SnL4RealServerPortCfgAdminStatus_Type = L4Status
_SnL4RealServerPortCfgAdminStatus_Object = MibTableColumn
snL4RealServerPortCfgAdminStatus = _SnL4RealServerPortCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1, 4),
    _SnL4RealServerPortCfgAdminStatus_Type()
)
snL4RealServerPortCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortCfgAdminStatus.setStatus("mandatory")
_SnL4RealServerPortCfgRowStatus_Type = L4RowSts
_SnL4RealServerPortCfgRowStatus_Object = MibTableColumn
snL4RealServerPortCfgRowStatus = _SnL4RealServerPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1, 5),
    _SnL4RealServerPortCfgRowStatus_Type()
)
snL4RealServerPortCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortCfgRowStatus.setStatus("mandatory")
_SnL4RealServerPortCfgDeleteState_Type = L4DeleteState
_SnL4RealServerPortCfgDeleteState_Object = MibTableColumn
snL4RealServerPortCfgDeleteState = _SnL4RealServerPortCfgDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 20, 1, 1, 6),
    _SnL4RealServerPortCfgDeleteState_Type()
)
snL4RealServerPortCfgDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortCfgDeleteState.setStatus("mandatory")
_SnL4VirtualServerCfg_ObjectIdentity = ObjectIdentity
snL4VirtualServerCfg = _SnL4VirtualServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21)
)
_SnL4VirtualServerCfgTable_Object = MibTable
snL4VirtualServerCfgTable = _SnL4VirtualServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerCfgTable.setStatus("mandatory")
_SnL4VirtualServerCfgEntry_Object = MibTableRow
snL4VirtualServerCfgEntry = _SnL4VirtualServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1)
)
snL4VirtualServerCfgEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerCfgVirtualIP"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerCfgEntry.setStatus("mandatory")
_SnL4VirtualServerCfgVirtualIP_Type = IpAddress
_SnL4VirtualServerCfgVirtualIP_Object = MibTableColumn
snL4VirtualServerCfgVirtualIP = _SnL4VirtualServerCfgVirtualIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1, 1),
    _SnL4VirtualServerCfgVirtualIP_Type()
)
snL4VirtualServerCfgVirtualIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerCfgVirtualIP.setStatus("mandatory")
_SnL4VirtualServerCfgName_Type = L4ServerName
_SnL4VirtualServerCfgName_Object = MibTableColumn
snL4VirtualServerCfgName = _SnL4VirtualServerCfgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1, 2),
    _SnL4VirtualServerCfgName_Type()
)
snL4VirtualServerCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerCfgName.setStatus("mandatory")
_SnL4VirtualServerCfgAdminStatus_Type = L4Status
_SnL4VirtualServerCfgAdminStatus_Object = MibTableColumn
snL4VirtualServerCfgAdminStatus = _SnL4VirtualServerCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1, 3),
    _SnL4VirtualServerCfgAdminStatus_Type()
)
snL4VirtualServerCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerCfgAdminStatus.setStatus("mandatory")


class _SnL4VirtualServerCfgSDAType_Type(Integer32):
    """Custom type snL4VirtualServerCfgSDAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("leastconnection", 1),
          ("roundrobin", 2),
          ("weighted", 3))
    )


_SnL4VirtualServerCfgSDAType_Type.__name__ = "Integer32"
_SnL4VirtualServerCfgSDAType_Object = MibTableColumn
snL4VirtualServerCfgSDAType = _SnL4VirtualServerCfgSDAType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1, 4),
    _SnL4VirtualServerCfgSDAType_Type()
)
snL4VirtualServerCfgSDAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerCfgSDAType.setStatus("mandatory")
_SnL4VirtualServerCfgRowStatus_Type = L4RowSts
_SnL4VirtualServerCfgRowStatus_Object = MibTableColumn
snL4VirtualServerCfgRowStatus = _SnL4VirtualServerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1, 5),
    _SnL4VirtualServerCfgRowStatus_Type()
)
snL4VirtualServerCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerCfgRowStatus.setStatus("mandatory")
_SnL4VirtualServerCfgDeleteState_Type = L4DeleteState
_SnL4VirtualServerCfgDeleteState_Object = MibTableColumn
snL4VirtualServerCfgDeleteState = _SnL4VirtualServerCfgDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 21, 1, 1, 6),
    _SnL4VirtualServerCfgDeleteState_Type()
)
snL4VirtualServerCfgDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerCfgDeleteState.setStatus("mandatory")
_SnL4VirtualServerPortCfg_ObjectIdentity = ObjectIdentity
snL4VirtualServerPortCfg = _SnL4VirtualServerPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22)
)
_SnL4VirtualServerPortCfgTable_Object = MibTable
snL4VirtualServerPortCfgTable = _SnL4VirtualServerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgTable.setStatus("mandatory")
_SnL4VirtualServerPortCfgEntry_Object = MibTableRow
snL4VirtualServerPortCfgEntry = _SnL4VirtualServerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1)
)
snL4VirtualServerPortCfgEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortCfgIP"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortCfgPort"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgEntry.setStatus("mandatory")
_SnL4VirtualServerPortCfgIP_Type = IpAddress
_SnL4VirtualServerPortCfgIP_Object = MibTableColumn
snL4VirtualServerPortCfgIP = _SnL4VirtualServerPortCfgIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 1),
    _SnL4VirtualServerPortCfgIP_Type()
)
snL4VirtualServerPortCfgIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgIP.setStatus("mandatory")


class _SnL4VirtualServerPortCfgPort_Type(Integer32):
    """Custom type snL4VirtualServerPortCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnL4VirtualServerPortCfgPort_Type.__name__ = "Integer32"
_SnL4VirtualServerPortCfgPort_Object = MibTableColumn
snL4VirtualServerPortCfgPort = _SnL4VirtualServerPortCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 2),
    _SnL4VirtualServerPortCfgPort_Type()
)
snL4VirtualServerPortCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgPort.setStatus("mandatory")
_SnL4VirtualServerPortCfgServerName_Type = L4ServerName
_SnL4VirtualServerPortCfgServerName_Object = MibTableColumn
snL4VirtualServerPortCfgServerName = _SnL4VirtualServerPortCfgServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 3),
    _SnL4VirtualServerPortCfgServerName_Type()
)
snL4VirtualServerPortCfgServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgServerName.setStatus("mandatory")
_SnL4VirtualServerPortCfgAdminStatus_Type = L4Status
_SnL4VirtualServerPortCfgAdminStatus_Object = MibTableColumn
snL4VirtualServerPortCfgAdminStatus = _SnL4VirtualServerPortCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 4),
    _SnL4VirtualServerPortCfgAdminStatus_Type()
)
snL4VirtualServerPortCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgAdminStatus.setStatus("mandatory")


class _SnL4VirtualServerPortCfgSticky_Type(Integer32):
    """Custom type snL4VirtualServerPortCfgSticky based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4VirtualServerPortCfgSticky_Type.__name__ = "Integer32"
_SnL4VirtualServerPortCfgSticky_Object = MibTableColumn
snL4VirtualServerPortCfgSticky = _SnL4VirtualServerPortCfgSticky_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 5),
    _SnL4VirtualServerPortCfgSticky_Type()
)
snL4VirtualServerPortCfgSticky.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgSticky.setStatus("mandatory")


class _SnL4VirtualServerPortCfgConcurrent_Type(Integer32):
    """Custom type snL4VirtualServerPortCfgConcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnL4VirtualServerPortCfgConcurrent_Type.__name__ = "Integer32"
_SnL4VirtualServerPortCfgConcurrent_Object = MibTableColumn
snL4VirtualServerPortCfgConcurrent = _SnL4VirtualServerPortCfgConcurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 6),
    _SnL4VirtualServerPortCfgConcurrent_Type()
)
snL4VirtualServerPortCfgConcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgConcurrent.setStatus("mandatory")
_SnL4VirtualServerPortCfgRowStatus_Type = L4RowSts
_SnL4VirtualServerPortCfgRowStatus_Object = MibTableColumn
snL4VirtualServerPortCfgRowStatus = _SnL4VirtualServerPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 7),
    _SnL4VirtualServerPortCfgRowStatus_Type()
)
snL4VirtualServerPortCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgRowStatus.setStatus("mandatory")
_SnL4VirtualServerPortCfgDeleteState_Type = L4DeleteState
_SnL4VirtualServerPortCfgDeleteState_Object = MibTableColumn
snL4VirtualServerPortCfgDeleteState = _SnL4VirtualServerPortCfgDeleteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 22, 1, 1, 8),
    _SnL4VirtualServerPortCfgDeleteState_Type()
)
snL4VirtualServerPortCfgDeleteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortCfgDeleteState.setStatus("mandatory")
_SnL4RealServerStatistic_ObjectIdentity = ObjectIdentity
snL4RealServerStatistic = _SnL4RealServerStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23)
)
_SnL4RealServerStatisticTable_Object = MibTable
snL4RealServerStatisticTable = _SnL4RealServerStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerStatisticTable.setStatus("mandatory")
_SnL4RealServerStatisticEntry_Object = MibTableRow
snL4RealServerStatisticEntry = _SnL4RealServerStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1)
)
snL4RealServerStatisticEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerStatisticRealIP"),
)
if mibBuilder.loadTexts:
    snL4RealServerStatisticEntry.setStatus("mandatory")
_SnL4RealServerStatisticRealIP_Type = IpAddress
_SnL4RealServerStatisticRealIP_Object = MibTableColumn
snL4RealServerStatisticRealIP = _SnL4RealServerStatisticRealIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 1),
    _SnL4RealServerStatisticRealIP_Type()
)
snL4RealServerStatisticRealIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticRealIP.setStatus("mandatory")
_SnL4RealServerStatisticName_Type = L4ServerName
_SnL4RealServerStatisticName_Object = MibTableColumn
snL4RealServerStatisticName = _SnL4RealServerStatisticName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 2),
    _SnL4RealServerStatisticName_Type()
)
snL4RealServerStatisticName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticName.setStatus("mandatory")
_SnL4RealServerStatisticReceivePkts_Type = Counter32
_SnL4RealServerStatisticReceivePkts_Object = MibTableColumn
snL4RealServerStatisticReceivePkts = _SnL4RealServerStatisticReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 3),
    _SnL4RealServerStatisticReceivePkts_Type()
)
snL4RealServerStatisticReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticReceivePkts.setStatus("mandatory")
_SnL4RealServerStatisticTransmitPkts_Type = Counter32
_SnL4RealServerStatisticTransmitPkts_Object = MibTableColumn
snL4RealServerStatisticTransmitPkts = _SnL4RealServerStatisticTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 4),
    _SnL4RealServerStatisticTransmitPkts_Type()
)
snL4RealServerStatisticTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticTransmitPkts.setStatus("mandatory")
_SnL4RealServerStatisticCurConnections_Type = Integer32
_SnL4RealServerStatisticCurConnections_Object = MibTableColumn
snL4RealServerStatisticCurConnections = _SnL4RealServerStatisticCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 5),
    _SnL4RealServerStatisticCurConnections_Type()
)
snL4RealServerStatisticCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticCurConnections.setStatus("mandatory")
_SnL4RealServerStatisticTotalConnections_Type = Counter32
_SnL4RealServerStatisticTotalConnections_Object = MibTableColumn
snL4RealServerStatisticTotalConnections = _SnL4RealServerStatisticTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 6),
    _SnL4RealServerStatisticTotalConnections_Type()
)
snL4RealServerStatisticTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticTotalConnections.setStatus("mandatory")
_SnL4RealServerStatisticAge_Type = Integer32
_SnL4RealServerStatisticAge_Object = MibTableColumn
snL4RealServerStatisticAge = _SnL4RealServerStatisticAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 7),
    _SnL4RealServerStatisticAge_Type()
)
snL4RealServerStatisticAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticAge.setStatus("mandatory")


class _SnL4RealServerStatisticState_Type(Integer32):
    """Custom type snL4RealServerStatisticState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("serveractive", 6),
          ("serverdisabled", 0),
          ("serverenabled", 1),
          ("serverfailed", 2),
          ("servershutdown", 5),
          ("serversuspect", 4),
          ("servertesting", 3))
    )


_SnL4RealServerStatisticState_Type.__name__ = "Integer32"
_SnL4RealServerStatisticState_Object = MibTableColumn
snL4RealServerStatisticState = _SnL4RealServerStatisticState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 8),
    _SnL4RealServerStatisticState_Type()
)
snL4RealServerStatisticState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticState.setStatus("mandatory")
_SnL4RealServerStatisticReassignments_Type = Integer32
_SnL4RealServerStatisticReassignments_Object = MibTableColumn
snL4RealServerStatisticReassignments = _SnL4RealServerStatisticReassignments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 9),
    _SnL4RealServerStatisticReassignments_Type()
)
snL4RealServerStatisticReassignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticReassignments.setStatus("mandatory")
_SnL4RealServerStatisticReassignmentLimit_Type = Integer32
_SnL4RealServerStatisticReassignmentLimit_Object = MibTableColumn
snL4RealServerStatisticReassignmentLimit = _SnL4RealServerStatisticReassignmentLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 10),
    _SnL4RealServerStatisticReassignmentLimit_Type()
)
snL4RealServerStatisticReassignmentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticReassignmentLimit.setStatus("mandatory")
_SnL4RealServerStatisticFailedPortExists_Type = Integer32
_SnL4RealServerStatisticFailedPortExists_Object = MibTableColumn
snL4RealServerStatisticFailedPortExists = _SnL4RealServerStatisticFailedPortExists_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 11),
    _SnL4RealServerStatisticFailedPortExists_Type()
)
snL4RealServerStatisticFailedPortExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticFailedPortExists.setStatus("mandatory")
_SnL4RealServerStatisticFailTime_Type = Integer32
_SnL4RealServerStatisticFailTime_Object = MibTableColumn
snL4RealServerStatisticFailTime = _SnL4RealServerStatisticFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 12),
    _SnL4RealServerStatisticFailTime_Type()
)
snL4RealServerStatisticFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticFailTime.setStatus("mandatory")
_SnL4RealServerStatisticPeakConnections_Type = Integer32
_SnL4RealServerStatisticPeakConnections_Object = MibTableColumn
snL4RealServerStatisticPeakConnections = _SnL4RealServerStatisticPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 23, 1, 1, 13),
    _SnL4RealServerStatisticPeakConnections_Type()
)
snL4RealServerStatisticPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerStatisticPeakConnections.setStatus("mandatory")
_SnL4RealServerPortStatistic_ObjectIdentity = ObjectIdentity
snL4RealServerPortStatistic = _SnL4RealServerPortStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24)
)
_SnL4RealServerPortStatisticTable_Object = MibTable
snL4RealServerPortStatisticTable = _SnL4RealServerPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticTable.setStatus("mandatory")
_SnL4RealServerPortStatisticEntry_Object = MibTableRow
snL4RealServerPortStatisticEntry = _SnL4RealServerPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1)
)
snL4RealServerPortStatisticEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortStatisticIP"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortStatisticPort"),
)
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticEntry.setStatus("mandatory")
_SnL4RealServerPortStatisticIP_Type = IpAddress
_SnL4RealServerPortStatisticIP_Object = MibTableColumn
snL4RealServerPortStatisticIP = _SnL4RealServerPortStatisticIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 1),
    _SnL4RealServerPortStatisticIP_Type()
)
snL4RealServerPortStatisticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticIP.setStatus("mandatory")
_SnL4RealServerPortStatisticPort_Type = Integer32
_SnL4RealServerPortStatisticPort_Object = MibTableColumn
snL4RealServerPortStatisticPort = _SnL4RealServerPortStatisticPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 2),
    _SnL4RealServerPortStatisticPort_Type()
)
snL4RealServerPortStatisticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticPort.setStatus("mandatory")
_SnL4RealServerPortStatisticServerName_Type = L4ServerName
_SnL4RealServerPortStatisticServerName_Object = MibTableColumn
snL4RealServerPortStatisticServerName = _SnL4RealServerPortStatisticServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 3),
    _SnL4RealServerPortStatisticServerName_Type()
)
snL4RealServerPortStatisticServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticServerName.setStatus("mandatory")
_SnL4RealServerPortStatisticReassignCount_Type = Integer32
_SnL4RealServerPortStatisticReassignCount_Object = MibTableColumn
snL4RealServerPortStatisticReassignCount = _SnL4RealServerPortStatisticReassignCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 4),
    _SnL4RealServerPortStatisticReassignCount_Type()
)
snL4RealServerPortStatisticReassignCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticReassignCount.setStatus("mandatory")


class _SnL4RealServerPortStatisticState_Type(Integer32):
    """Custom type snL4RealServerPortStatisticState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("active", 6),
          ("awaitDelete", 9),
          ("awaitUnbind", 8),
          ("disabled", 0),
          ("enabled", 1),
          ("failed", 2),
          ("shutdown", 5),
          ("suspect", 4),
          ("testing", 3),
          ("unbound", 7))
    )


_SnL4RealServerPortStatisticState_Type.__name__ = "Integer32"
_SnL4RealServerPortStatisticState_Object = MibTableColumn
snL4RealServerPortStatisticState = _SnL4RealServerPortStatisticState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 5),
    _SnL4RealServerPortStatisticState_Type()
)
snL4RealServerPortStatisticState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticState.setStatus("mandatory")
_SnL4RealServerPortStatisticFailTime_Type = Integer32
_SnL4RealServerPortStatisticFailTime_Object = MibTableColumn
snL4RealServerPortStatisticFailTime = _SnL4RealServerPortStatisticFailTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 6),
    _SnL4RealServerPortStatisticFailTime_Type()
)
snL4RealServerPortStatisticFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticFailTime.setStatus("mandatory")
_SnL4RealServerPortStatisticCurrentConnection_Type = Integer32
_SnL4RealServerPortStatisticCurrentConnection_Object = MibTableColumn
snL4RealServerPortStatisticCurrentConnection = _SnL4RealServerPortStatisticCurrentConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 7),
    _SnL4RealServerPortStatisticCurrentConnection_Type()
)
snL4RealServerPortStatisticCurrentConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticCurrentConnection.setStatus("mandatory")
_SnL4RealServerPortStatisticTotalConnection_Type = Counter32
_SnL4RealServerPortStatisticTotalConnection_Object = MibTableColumn
snL4RealServerPortStatisticTotalConnection = _SnL4RealServerPortStatisticTotalConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 8),
    _SnL4RealServerPortStatisticTotalConnection_Type()
)
snL4RealServerPortStatisticTotalConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticTotalConnection.setStatus("mandatory")
_SnL4RealServerPortStatisticRxPkts_Type = Counter32
_SnL4RealServerPortStatisticRxPkts_Object = MibTableColumn
snL4RealServerPortStatisticRxPkts = _SnL4RealServerPortStatisticRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 9),
    _SnL4RealServerPortStatisticRxPkts_Type()
)
snL4RealServerPortStatisticRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticRxPkts.setStatus("mandatory")
_SnL4RealServerPortStatisticTxPkts_Type = Counter32
_SnL4RealServerPortStatisticTxPkts_Object = MibTableColumn
snL4RealServerPortStatisticTxPkts = _SnL4RealServerPortStatisticTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 10),
    _SnL4RealServerPortStatisticTxPkts_Type()
)
snL4RealServerPortStatisticTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticTxPkts.setStatus("mandatory")
_SnL4RealServerPortStatisticRxBytes_Type = Counter32
_SnL4RealServerPortStatisticRxBytes_Object = MibTableColumn
snL4RealServerPortStatisticRxBytes = _SnL4RealServerPortStatisticRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 11),
    _SnL4RealServerPortStatisticRxBytes_Type()
)
snL4RealServerPortStatisticRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticRxBytes.setStatus("mandatory")
_SnL4RealServerPortStatisticTxBytes_Type = Counter32
_SnL4RealServerPortStatisticTxBytes_Object = MibTableColumn
snL4RealServerPortStatisticTxBytes = _SnL4RealServerPortStatisticTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 12),
    _SnL4RealServerPortStatisticTxBytes_Type()
)
snL4RealServerPortStatisticTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticTxBytes.setStatus("mandatory")
_SnL4RealServerPortStatisticPeakConnection_Type = Integer32
_SnL4RealServerPortStatisticPeakConnection_Object = MibTableColumn
snL4RealServerPortStatisticPeakConnection = _SnL4RealServerPortStatisticPeakConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 24, 1, 1, 13),
    _SnL4RealServerPortStatisticPeakConnection_Type()
)
snL4RealServerPortStatisticPeakConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortStatisticPeakConnection.setStatus("mandatory")
_SnL4VirtualServerStatistic_ObjectIdentity = ObjectIdentity
snL4VirtualServerStatistic = _SnL4VirtualServerStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25)
)
_SnL4VirtualServerStatisticTable_Object = MibTable
snL4VirtualServerStatisticTable = _SnL4VirtualServerStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticTable.setStatus("mandatory")
_SnL4VirtualServerStatisticEntry_Object = MibTableRow
snL4VirtualServerStatisticEntry = _SnL4VirtualServerStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1)
)
snL4VirtualServerStatisticEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerStatisticIP"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticEntry.setStatus("mandatory")
_SnL4VirtualServerStatisticIP_Type = IpAddress
_SnL4VirtualServerStatisticIP_Object = MibTableColumn
snL4VirtualServerStatisticIP = _SnL4VirtualServerStatisticIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 1),
    _SnL4VirtualServerStatisticIP_Type()
)
snL4VirtualServerStatisticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticIP.setStatus("mandatory")
_SnL4VirtualServerStatisticName_Type = L4ServerName
_SnL4VirtualServerStatisticName_Object = MibTableColumn
snL4VirtualServerStatisticName = _SnL4VirtualServerStatisticName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 2),
    _SnL4VirtualServerStatisticName_Type()
)
snL4VirtualServerStatisticName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticName.setStatus("mandatory")
_SnL4VirtualServerStatisticReceivePkts_Type = Counter32
_SnL4VirtualServerStatisticReceivePkts_Object = MibTableColumn
snL4VirtualServerStatisticReceivePkts = _SnL4VirtualServerStatisticReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 3),
    _SnL4VirtualServerStatisticReceivePkts_Type()
)
snL4VirtualServerStatisticReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticReceivePkts.setStatus("mandatory")
_SnL4VirtualServerStatisticTransmitPkts_Type = Counter32
_SnL4VirtualServerStatisticTransmitPkts_Object = MibTableColumn
snL4VirtualServerStatisticTransmitPkts = _SnL4VirtualServerStatisticTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 4),
    _SnL4VirtualServerStatisticTransmitPkts_Type()
)
snL4VirtualServerStatisticTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticTransmitPkts.setStatus("mandatory")
_SnL4VirtualServerStatisticTotalConnections_Type = Counter32
_SnL4VirtualServerStatisticTotalConnections_Object = MibTableColumn
snL4VirtualServerStatisticTotalConnections = _SnL4VirtualServerStatisticTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 5),
    _SnL4VirtualServerStatisticTotalConnections_Type()
)
snL4VirtualServerStatisticTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticTotalConnections.setStatus("mandatory")
_SnL4VirtualServerStatisticReceiveBytes_Type = Counter64
_SnL4VirtualServerStatisticReceiveBytes_Object = MibTableColumn
snL4VirtualServerStatisticReceiveBytes = _SnL4VirtualServerStatisticReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 6),
    _SnL4VirtualServerStatisticReceiveBytes_Type()
)
snL4VirtualServerStatisticReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticReceiveBytes.setStatus("mandatory")
_SnL4VirtualServerStatisticTransmitBytes_Type = Counter64
_SnL4VirtualServerStatisticTransmitBytes_Object = MibTableColumn
snL4VirtualServerStatisticTransmitBytes = _SnL4VirtualServerStatisticTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 7),
    _SnL4VirtualServerStatisticTransmitBytes_Type()
)
snL4VirtualServerStatisticTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticTransmitBytes.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricState_Type = Integer32
_SnL4VirtualServerStatisticSymmetricState_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricState = _SnL4VirtualServerStatisticSymmetricState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 8),
    _SnL4VirtualServerStatisticSymmetricState_Type()
)
snL4VirtualServerStatisticSymmetricState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricState.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricPriority_Type = Integer32
_SnL4VirtualServerStatisticSymmetricPriority_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricPriority = _SnL4VirtualServerStatisticSymmetricPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 9),
    _SnL4VirtualServerStatisticSymmetricPriority_Type()
)
snL4VirtualServerStatisticSymmetricPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricPriority.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricKeep_Type = Integer32
_SnL4VirtualServerStatisticSymmetricKeep_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricKeep = _SnL4VirtualServerStatisticSymmetricKeep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 10),
    _SnL4VirtualServerStatisticSymmetricKeep_Type()
)
snL4VirtualServerStatisticSymmetricKeep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricKeep.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricActivates_Type = Counter32
_SnL4VirtualServerStatisticSymmetricActivates_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricActivates = _SnL4VirtualServerStatisticSymmetricActivates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 11),
    _SnL4VirtualServerStatisticSymmetricActivates_Type()
)
snL4VirtualServerStatisticSymmetricActivates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricActivates.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricInactives_Type = Counter32
_SnL4VirtualServerStatisticSymmetricInactives_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricInactives = _SnL4VirtualServerStatisticSymmetricInactives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 12),
    _SnL4VirtualServerStatisticSymmetricInactives_Type()
)
snL4VirtualServerStatisticSymmetricInactives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricInactives.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricBestStandbyMacAddr_Type = PhysAddress
_SnL4VirtualServerStatisticSymmetricBestStandbyMacAddr_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricBestStandbyMacAddr = _SnL4VirtualServerStatisticSymmetricBestStandbyMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 13),
    _SnL4VirtualServerStatisticSymmetricBestStandbyMacAddr_Type()
)
snL4VirtualServerStatisticSymmetricBestStandbyMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricBestStandbyMacAddr.setStatus("mandatory")
_SnL4VirtualServerStatisticSymmetricActiveMacAddr_Type = PhysAddress
_SnL4VirtualServerStatisticSymmetricActiveMacAddr_Object = MibTableColumn
snL4VirtualServerStatisticSymmetricActiveMacAddr = _SnL4VirtualServerStatisticSymmetricActiveMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 25, 1, 1, 14),
    _SnL4VirtualServerStatisticSymmetricActiveMacAddr_Type()
)
snL4VirtualServerStatisticSymmetricActiveMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerStatisticSymmetricActiveMacAddr.setStatus("mandatory")
_SnL4VirtualServerPortStatistic_ObjectIdentity = ObjectIdentity
snL4VirtualServerPortStatistic = _SnL4VirtualServerPortStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26)
)
_SnL4VirtualServerPortStatisticTable_Object = MibTable
snL4VirtualServerPortStatisticTable = _SnL4VirtualServerPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1)
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticTable.setStatus("mandatory")
_SnL4VirtualServerPortStatisticEntry_Object = MibTableRow
snL4VirtualServerPortStatisticEntry = _SnL4VirtualServerPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1)
)
snL4VirtualServerPortStatisticEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortStatisticIP"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortStatisticPort"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticEntry.setStatus("mandatory")
_SnL4VirtualServerPortStatisticIP_Type = IpAddress
_SnL4VirtualServerPortStatisticIP_Object = MibTableColumn
snL4VirtualServerPortStatisticIP = _SnL4VirtualServerPortStatisticIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1, 1),
    _SnL4VirtualServerPortStatisticIP_Type()
)
snL4VirtualServerPortStatisticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticIP.setStatus("mandatory")


class _SnL4VirtualServerPortStatisticPort_Type(Integer32):
    """Custom type snL4VirtualServerPortStatisticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_SnL4VirtualServerPortStatisticPort_Type.__name__ = "Integer32"
_SnL4VirtualServerPortStatisticPort_Object = MibTableColumn
snL4VirtualServerPortStatisticPort = _SnL4VirtualServerPortStatisticPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1, 2),
    _SnL4VirtualServerPortStatisticPort_Type()
)
snL4VirtualServerPortStatisticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticPort.setStatus("mandatory")
_SnL4VirtualServerPortStatisticServerName_Type = L4ServerName
_SnL4VirtualServerPortStatisticServerName_Object = MibTableColumn
snL4VirtualServerPortStatisticServerName = _SnL4VirtualServerPortStatisticServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1, 3),
    _SnL4VirtualServerPortStatisticServerName_Type()
)
snL4VirtualServerPortStatisticServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticServerName.setStatus("mandatory")
_SnL4VirtualServerPortStatisticCurrentConnection_Type = Integer32
_SnL4VirtualServerPortStatisticCurrentConnection_Object = MibTableColumn
snL4VirtualServerPortStatisticCurrentConnection = _SnL4VirtualServerPortStatisticCurrentConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1, 4),
    _SnL4VirtualServerPortStatisticCurrentConnection_Type()
)
snL4VirtualServerPortStatisticCurrentConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticCurrentConnection.setStatus("mandatory")
_SnL4VirtualServerPortStatisticTotalConnection_Type = Counter32
_SnL4VirtualServerPortStatisticTotalConnection_Object = MibTableColumn
snL4VirtualServerPortStatisticTotalConnection = _SnL4VirtualServerPortStatisticTotalConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1, 5),
    _SnL4VirtualServerPortStatisticTotalConnection_Type()
)
snL4VirtualServerPortStatisticTotalConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticTotalConnection.setStatus("mandatory")
_SnL4VirtualServerPortStatisticPeakConnection_Type = Integer32
_SnL4VirtualServerPortStatisticPeakConnection_Object = MibTableColumn
snL4VirtualServerPortStatisticPeakConnection = _SnL4VirtualServerPortStatisticPeakConnection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 26, 1, 1, 6),
    _SnL4VirtualServerPortStatisticPeakConnection_Type()
)
snL4VirtualServerPortStatisticPeakConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortStatisticPeakConnection.setStatus("mandatory")
_SnL4GslbSiteRemoteServerIrons_ObjectIdentity = ObjectIdentity
snL4GslbSiteRemoteServerIrons = _SnL4GslbSiteRemoteServerIrons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 27)
)
_SnL4GslbSiteRemoteServerIronTable_Object = MibTable
snL4GslbSiteRemoteServerIronTable = _SnL4GslbSiteRemoteServerIronTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 27, 1)
)
if mibBuilder.loadTexts:
    snL4GslbSiteRemoteServerIronTable.setStatus("mandatory")
_SnL4GslbSiteRemoteServerIronEntry_Object = MibTableRow
snL4GslbSiteRemoteServerIronEntry = _SnL4GslbSiteRemoteServerIronEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 27, 1, 1)
)
snL4GslbSiteRemoteServerIronEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4GslbSiteRemoteServerIronIP"),
)
if mibBuilder.loadTexts:
    snL4GslbSiteRemoteServerIronEntry.setStatus("mandatory")
_SnL4GslbSiteRemoteServerIronIP_Type = IpAddress
_SnL4GslbSiteRemoteServerIronIP_Object = MibTableColumn
snL4GslbSiteRemoteServerIronIP = _SnL4GslbSiteRemoteServerIronIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 27, 1, 1, 1),
    _SnL4GslbSiteRemoteServerIronIP_Type()
)
snL4GslbSiteRemoteServerIronIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4GslbSiteRemoteServerIronIP.setStatus("mandatory")


class _SnL4GslbSiteRemoteServerIronPreference_Type(Integer32):
    """Custom type snL4GslbSiteRemoteServerIronPreference based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnL4GslbSiteRemoteServerIronPreference_Type.__name__ = "Integer32"
_SnL4GslbSiteRemoteServerIronPreference_Object = MibTableColumn
snL4GslbSiteRemoteServerIronPreference = _SnL4GslbSiteRemoteServerIronPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 27, 1, 1, 2),
    _SnL4GslbSiteRemoteServerIronPreference_Type()
)
snL4GslbSiteRemoteServerIronPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4GslbSiteRemoteServerIronPreference.setStatus("mandatory")
_SnL4History_ObjectIdentity = ObjectIdentity
snL4History = _SnL4History_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28)
)
_SnL4RealServerHistoryControlTable_Object = MibTable
snL4RealServerHistoryControlTable = _SnL4RealServerHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1)
)
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlTable.setStatus("mandatory")
_SnL4RealServerHistoryControlEntry_Object = MibTableRow
snL4RealServerHistoryControlEntry = _SnL4RealServerHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1)
)
snL4RealServerHistoryControlEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlEntry.setStatus("mandatory")


class _SnL4RealServerHistoryControlIndex_Type(Integer32):
    """Custom type snL4RealServerHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerHistoryControlIndex_Type.__name__ = "Integer32"
_SnL4RealServerHistoryControlIndex_Object = MibTableColumn
snL4RealServerHistoryControlIndex = _SnL4RealServerHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 1),
    _SnL4RealServerHistoryControlIndex_Type()
)
snL4RealServerHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlIndex.setStatus("mandatory")
_SnL4RealServerHistoryControlDataSource_Type = ObjectIdentifier
_SnL4RealServerHistoryControlDataSource_Object = MibTableColumn
snL4RealServerHistoryControlDataSource = _SnL4RealServerHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 2),
    _SnL4RealServerHistoryControlDataSource_Type()
)
snL4RealServerHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlDataSource.setStatus("mandatory")


class _SnL4RealServerHistoryControlBucketsRequested_Type(Integer32):
    """Custom type snL4RealServerHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_SnL4RealServerHistoryControlBucketsRequested_Object = MibTableColumn
snL4RealServerHistoryControlBucketsRequested = _SnL4RealServerHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 3),
    _SnL4RealServerHistoryControlBucketsRequested_Type()
)
snL4RealServerHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlBucketsRequested.setStatus("mandatory")


class _SnL4RealServerHistoryControlBucketsGranted_Type(Integer32):
    """Custom type snL4RealServerHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_SnL4RealServerHistoryControlBucketsGranted_Object = MibTableColumn
snL4RealServerHistoryControlBucketsGranted = _SnL4RealServerHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 4),
    _SnL4RealServerHistoryControlBucketsGranted_Type()
)
snL4RealServerHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlBucketsGranted.setStatus("mandatory")


class _SnL4RealServerHistoryControlInterval_Type(Integer32):
    """Custom type snL4RealServerHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SnL4RealServerHistoryControlInterval_Type.__name__ = "Integer32"
_SnL4RealServerHistoryControlInterval_Object = MibTableColumn
snL4RealServerHistoryControlInterval = _SnL4RealServerHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 5),
    _SnL4RealServerHistoryControlInterval_Type()
)
snL4RealServerHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlInterval.setStatus("mandatory")
_SnL4RealServerHistoryControlOwner_Type = DisplayString
_SnL4RealServerHistoryControlOwner_Object = MibTableColumn
snL4RealServerHistoryControlOwner = _SnL4RealServerHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 6),
    _SnL4RealServerHistoryControlOwner_Type()
)
snL4RealServerHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlOwner.setStatus("mandatory")


class _SnL4RealServerHistoryControlStatus_Type(Integer32):
    """Custom type snL4RealServerHistoryControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_SnL4RealServerHistoryControlStatus_Type.__name__ = "Integer32"
_SnL4RealServerHistoryControlStatus_Object = MibTableColumn
snL4RealServerHistoryControlStatus = _SnL4RealServerHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 1, 1, 7),
    _SnL4RealServerHistoryControlStatus_Type()
)
snL4RealServerHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerHistoryControlStatus.setStatus("mandatory")
_SnL4RealServerHistoryTable_Object = MibTable
snL4RealServerHistoryTable = _SnL4RealServerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2)
)
if mibBuilder.loadTexts:
    snL4RealServerHistoryTable.setStatus("mandatory")
_SnL4RealServerHistoryEntry_Object = MibTableRow
snL4RealServerHistoryEntry = _SnL4RealServerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1)
)
snL4RealServerHistoryEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerHistoryIndex"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerHistoryEntry.setStatus("mandatory")


class _SnL4RealServerHistoryIndex_Type(Integer32):
    """Custom type snL4RealServerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerHistoryIndex_Type.__name__ = "Integer32"
_SnL4RealServerHistoryIndex_Object = MibTableColumn
snL4RealServerHistoryIndex = _SnL4RealServerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 1),
    _SnL4RealServerHistoryIndex_Type()
)
snL4RealServerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryIndex.setStatus("mandatory")


class _SnL4RealServerHistorySampleIndex_Type(Integer32):
    """Custom type snL4RealServerHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnL4RealServerHistorySampleIndex_Type.__name__ = "Integer32"
_SnL4RealServerHistorySampleIndex_Object = MibTableColumn
snL4RealServerHistorySampleIndex = _SnL4RealServerHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 2),
    _SnL4RealServerHistorySampleIndex_Type()
)
snL4RealServerHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistorySampleIndex.setStatus("mandatory")
_SnL4RealServerHistoryIntervalStart_Type = TimeTicks
_SnL4RealServerHistoryIntervalStart_Object = MibTableColumn
snL4RealServerHistoryIntervalStart = _SnL4RealServerHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 3),
    _SnL4RealServerHistoryIntervalStart_Type()
)
snL4RealServerHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryIntervalStart.setStatus("mandatory")
_SnL4RealServerHistoryReceivePkts_Type = Counter32
_SnL4RealServerHistoryReceivePkts_Object = MibTableColumn
snL4RealServerHistoryReceivePkts = _SnL4RealServerHistoryReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 4),
    _SnL4RealServerHistoryReceivePkts_Type()
)
snL4RealServerHistoryReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryReceivePkts.setStatus("mandatory")
_SnL4RealServerHistoryTransmitPkts_Type = Counter32
_SnL4RealServerHistoryTransmitPkts_Object = MibTableColumn
snL4RealServerHistoryTransmitPkts = _SnL4RealServerHistoryTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 5),
    _SnL4RealServerHistoryTransmitPkts_Type()
)
snL4RealServerHistoryTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryTransmitPkts.setStatus("mandatory")
_SnL4RealServerHistoryTotalConnections_Type = Counter32
_SnL4RealServerHistoryTotalConnections_Object = MibTableColumn
snL4RealServerHistoryTotalConnections = _SnL4RealServerHistoryTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 6),
    _SnL4RealServerHistoryTotalConnections_Type()
)
snL4RealServerHistoryTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryTotalConnections.setStatus("mandatory")
_SnL4RealServerHistoryCurConnections_Type = Integer32
_SnL4RealServerHistoryCurConnections_Object = MibTableColumn
snL4RealServerHistoryCurConnections = _SnL4RealServerHistoryCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 7),
    _SnL4RealServerHistoryCurConnections_Type()
)
snL4RealServerHistoryCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryCurConnections.setStatus("mandatory")
_SnL4RealServerHistoryPeakConnections_Type = Integer32
_SnL4RealServerHistoryPeakConnections_Object = MibTableColumn
snL4RealServerHistoryPeakConnections = _SnL4RealServerHistoryPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 8),
    _SnL4RealServerHistoryPeakConnections_Type()
)
snL4RealServerHistoryPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryPeakConnections.setStatus("mandatory")
_SnL4RealServerHistoryReassignments_Type = Integer32
_SnL4RealServerHistoryReassignments_Object = MibTableColumn
snL4RealServerHistoryReassignments = _SnL4RealServerHistoryReassignments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 2, 1, 9),
    _SnL4RealServerHistoryReassignments_Type()
)
snL4RealServerHistoryReassignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerHistoryReassignments.setStatus("mandatory")
_SnL4RealServerPortHistoryControlTable_Object = MibTable
snL4RealServerPortHistoryControlTable = _SnL4RealServerPortHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3)
)
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlTable.setStatus("mandatory")
_SnL4RealServerPortHistoryControlEntry_Object = MibTableRow
snL4RealServerPortHistoryControlEntry = _SnL4RealServerPortHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1)
)
snL4RealServerPortHistoryControlEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlEntry.setStatus("mandatory")


class _SnL4RealServerPortHistoryControlIndex_Type(Integer32):
    """Custom type snL4RealServerPortHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerPortHistoryControlIndex_Type.__name__ = "Integer32"
_SnL4RealServerPortHistoryControlIndex_Object = MibTableColumn
snL4RealServerPortHistoryControlIndex = _SnL4RealServerPortHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 1),
    _SnL4RealServerPortHistoryControlIndex_Type()
)
snL4RealServerPortHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlIndex.setStatus("mandatory")
_SnL4RealServerPortHistoryControlDataSource_Type = ObjectIdentifier
_SnL4RealServerPortHistoryControlDataSource_Object = MibTableColumn
snL4RealServerPortHistoryControlDataSource = _SnL4RealServerPortHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 2),
    _SnL4RealServerPortHistoryControlDataSource_Type()
)
snL4RealServerPortHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlDataSource.setStatus("mandatory")


class _SnL4RealServerPortHistoryControlBucketsRequested_Type(Integer32):
    """Custom type snL4RealServerPortHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerPortHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_SnL4RealServerPortHistoryControlBucketsRequested_Object = MibTableColumn
snL4RealServerPortHistoryControlBucketsRequested = _SnL4RealServerPortHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 3),
    _SnL4RealServerPortHistoryControlBucketsRequested_Type()
)
snL4RealServerPortHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlBucketsRequested.setStatus("mandatory")


class _SnL4RealServerPortHistoryControlBucketsGranted_Type(Integer32):
    """Custom type snL4RealServerPortHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerPortHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_SnL4RealServerPortHistoryControlBucketsGranted_Object = MibTableColumn
snL4RealServerPortHistoryControlBucketsGranted = _SnL4RealServerPortHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 4),
    _SnL4RealServerPortHistoryControlBucketsGranted_Type()
)
snL4RealServerPortHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlBucketsGranted.setStatus("mandatory")


class _SnL4RealServerPortHistoryControlInterval_Type(Integer32):
    """Custom type snL4RealServerPortHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SnL4RealServerPortHistoryControlInterval_Type.__name__ = "Integer32"
_SnL4RealServerPortHistoryControlInterval_Object = MibTableColumn
snL4RealServerPortHistoryControlInterval = _SnL4RealServerPortHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 5),
    _SnL4RealServerPortHistoryControlInterval_Type()
)
snL4RealServerPortHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlInterval.setStatus("mandatory")
_SnL4RealServerPortHistoryControlOwner_Type = DisplayString
_SnL4RealServerPortHistoryControlOwner_Object = MibTableColumn
snL4RealServerPortHistoryControlOwner = _SnL4RealServerPortHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 6),
    _SnL4RealServerPortHistoryControlOwner_Type()
)
snL4RealServerPortHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlOwner.setStatus("mandatory")


class _SnL4RealServerPortHistoryControlStatus_Type(Integer32):
    """Custom type snL4RealServerPortHistoryControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_SnL4RealServerPortHistoryControlStatus_Type.__name__ = "Integer32"
_SnL4RealServerPortHistoryControlStatus_Object = MibTableColumn
snL4RealServerPortHistoryControlStatus = _SnL4RealServerPortHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 3, 1, 7),
    _SnL4RealServerPortHistoryControlStatus_Type()
)
snL4RealServerPortHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryControlStatus.setStatus("mandatory")
_SnL4RealServerPortHistoryTable_Object = MibTable
snL4RealServerPortHistoryTable = _SnL4RealServerPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4)
)
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryTable.setStatus("mandatory")
_SnL4RealServerPortHistoryEntry_Object = MibTableRow
snL4RealServerPortHistoryEntry = _SnL4RealServerPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1)
)
snL4RealServerPortHistoryEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortHistoryIndex"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4RealServerPortHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryEntry.setStatus("mandatory")


class _SnL4RealServerPortHistoryIndex_Type(Integer32):
    """Custom type snL4RealServerPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4RealServerPortHistoryIndex_Type.__name__ = "Integer32"
_SnL4RealServerPortHistoryIndex_Object = MibTableColumn
snL4RealServerPortHistoryIndex = _SnL4RealServerPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 1),
    _SnL4RealServerPortHistoryIndex_Type()
)
snL4RealServerPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryIndex.setStatus("mandatory")


class _SnL4RealServerPortHistorySampleIndex_Type(Integer32):
    """Custom type snL4RealServerPortHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnL4RealServerPortHistorySampleIndex_Type.__name__ = "Integer32"
_SnL4RealServerPortHistorySampleIndex_Object = MibTableColumn
snL4RealServerPortHistorySampleIndex = _SnL4RealServerPortHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 2),
    _SnL4RealServerPortHistorySampleIndex_Type()
)
snL4RealServerPortHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistorySampleIndex.setStatus("mandatory")
_SnL4RealServerPortHistoryIntervalStart_Type = TimeTicks
_SnL4RealServerPortHistoryIntervalStart_Object = MibTableColumn
snL4RealServerPortHistoryIntervalStart = _SnL4RealServerPortHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 3),
    _SnL4RealServerPortHistoryIntervalStart_Type()
)
snL4RealServerPortHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryIntervalStart.setStatus("mandatory")
_SnL4RealServerPortHistoryReceivePkts_Type = Counter32
_SnL4RealServerPortHistoryReceivePkts_Object = MibTableColumn
snL4RealServerPortHistoryReceivePkts = _SnL4RealServerPortHistoryReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 4),
    _SnL4RealServerPortHistoryReceivePkts_Type()
)
snL4RealServerPortHistoryReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryReceivePkts.setStatus("mandatory")
_SnL4RealServerPortHistoryTransmitPkts_Type = Counter32
_SnL4RealServerPortHistoryTransmitPkts_Object = MibTableColumn
snL4RealServerPortHistoryTransmitPkts = _SnL4RealServerPortHistoryTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 5),
    _SnL4RealServerPortHistoryTransmitPkts_Type()
)
snL4RealServerPortHistoryTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryTransmitPkts.setStatus("mandatory")
_SnL4RealServerPortHistoryTotalConnections_Type = Counter32
_SnL4RealServerPortHistoryTotalConnections_Object = MibTableColumn
snL4RealServerPortHistoryTotalConnections = _SnL4RealServerPortHistoryTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 6),
    _SnL4RealServerPortHistoryTotalConnections_Type()
)
snL4RealServerPortHistoryTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryTotalConnections.setStatus("mandatory")
_SnL4RealServerPortHistoryCurConnections_Type = Integer32
_SnL4RealServerPortHistoryCurConnections_Object = MibTableColumn
snL4RealServerPortHistoryCurConnections = _SnL4RealServerPortHistoryCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 7),
    _SnL4RealServerPortHistoryCurConnections_Type()
)
snL4RealServerPortHistoryCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryCurConnections.setStatus("mandatory")
_SnL4RealServerPortHistoryPeakConnections_Type = Integer32
_SnL4RealServerPortHistoryPeakConnections_Object = MibTableColumn
snL4RealServerPortHistoryPeakConnections = _SnL4RealServerPortHistoryPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 8),
    _SnL4RealServerPortHistoryPeakConnections_Type()
)
snL4RealServerPortHistoryPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryPeakConnections.setStatus("mandatory")
_SnL4RealServerPortHistoryResponseTime_Type = Integer32
_SnL4RealServerPortHistoryResponseTime_Object = MibTableColumn
snL4RealServerPortHistoryResponseTime = _SnL4RealServerPortHistoryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 4, 1, 9),
    _SnL4RealServerPortHistoryResponseTime_Type()
)
snL4RealServerPortHistoryResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4RealServerPortHistoryResponseTime.setStatus("mandatory")
_SnL4VirtualServerHistoryControlTable_Object = MibTable
snL4VirtualServerHistoryControlTable = _SnL4VirtualServerHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5)
)
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlTable.setStatus("mandatory")
_SnL4VirtualServerHistoryControlEntry_Object = MibTableRow
snL4VirtualServerHistoryControlEntry = _SnL4VirtualServerHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1)
)
snL4VirtualServerHistoryControlEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlEntry.setStatus("mandatory")


class _SnL4VirtualServerHistoryControlIndex_Type(Integer32):
    """Custom type snL4VirtualServerHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerHistoryControlIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerHistoryControlIndex_Object = MibTableColumn
snL4VirtualServerHistoryControlIndex = _SnL4VirtualServerHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 1),
    _SnL4VirtualServerHistoryControlIndex_Type()
)
snL4VirtualServerHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlIndex.setStatus("mandatory")
_SnL4VirtualServerHistoryControlDataSource_Type = ObjectIdentifier
_SnL4VirtualServerHistoryControlDataSource_Object = MibTableColumn
snL4VirtualServerHistoryControlDataSource = _SnL4VirtualServerHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 2),
    _SnL4VirtualServerHistoryControlDataSource_Type()
)
snL4VirtualServerHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlDataSource.setStatus("mandatory")


class _SnL4VirtualServerHistoryControlBucketsRequested_Type(Integer32):
    """Custom type snL4VirtualServerHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_SnL4VirtualServerHistoryControlBucketsRequested_Object = MibTableColumn
snL4VirtualServerHistoryControlBucketsRequested = _SnL4VirtualServerHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 3),
    _SnL4VirtualServerHistoryControlBucketsRequested_Type()
)
snL4VirtualServerHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlBucketsRequested.setStatus("mandatory")


class _SnL4VirtualServerHistoryControlBucketsGranted_Type(Integer32):
    """Custom type snL4VirtualServerHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_SnL4VirtualServerHistoryControlBucketsGranted_Object = MibTableColumn
snL4VirtualServerHistoryControlBucketsGranted = _SnL4VirtualServerHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 4),
    _SnL4VirtualServerHistoryControlBucketsGranted_Type()
)
snL4VirtualServerHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlBucketsGranted.setStatus("mandatory")


class _SnL4VirtualServerHistoryControlInterval_Type(Integer32):
    """Custom type snL4VirtualServerHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SnL4VirtualServerHistoryControlInterval_Type.__name__ = "Integer32"
_SnL4VirtualServerHistoryControlInterval_Object = MibTableColumn
snL4VirtualServerHistoryControlInterval = _SnL4VirtualServerHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 5),
    _SnL4VirtualServerHistoryControlInterval_Type()
)
snL4VirtualServerHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlInterval.setStatus("mandatory")
_SnL4VirtualServerHistoryControlOwner_Type = DisplayString
_SnL4VirtualServerHistoryControlOwner_Object = MibTableColumn
snL4VirtualServerHistoryControlOwner = _SnL4VirtualServerHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 6),
    _SnL4VirtualServerHistoryControlOwner_Type()
)
snL4VirtualServerHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlOwner.setStatus("mandatory")


class _SnL4VirtualServerHistoryControlStatus_Type(Integer32):
    """Custom type snL4VirtualServerHistoryControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_SnL4VirtualServerHistoryControlStatus_Type.__name__ = "Integer32"
_SnL4VirtualServerHistoryControlStatus_Object = MibTableColumn
snL4VirtualServerHistoryControlStatus = _SnL4VirtualServerHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 5, 1, 7),
    _SnL4VirtualServerHistoryControlStatus_Type()
)
snL4VirtualServerHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryControlStatus.setStatus("mandatory")
_SnL4VirtualServerHistoryTable_Object = MibTable
snL4VirtualServerHistoryTable = _SnL4VirtualServerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6)
)
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryTable.setStatus("mandatory")
_SnL4VirtualServerHistoryEntry_Object = MibTableRow
snL4VirtualServerHistoryEntry = _SnL4VirtualServerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1)
)
snL4VirtualServerHistoryEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerHistoryIndex"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryEntry.setStatus("mandatory")


class _SnL4VirtualServerHistoryIndex_Type(Integer32):
    """Custom type snL4VirtualServerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerHistoryIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerHistoryIndex_Object = MibTableColumn
snL4VirtualServerHistoryIndex = _SnL4VirtualServerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 1),
    _SnL4VirtualServerHistoryIndex_Type()
)
snL4VirtualServerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryIndex.setStatus("mandatory")


class _SnL4VirtualServerHistorySampleIndex_Type(Integer32):
    """Custom type snL4VirtualServerHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnL4VirtualServerHistorySampleIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerHistorySampleIndex_Object = MibTableColumn
snL4VirtualServerHistorySampleIndex = _SnL4VirtualServerHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 2),
    _SnL4VirtualServerHistorySampleIndex_Type()
)
snL4VirtualServerHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistorySampleIndex.setStatus("mandatory")
_SnL4VirtualServerHistoryIntervalStart_Type = TimeTicks
_SnL4VirtualServerHistoryIntervalStart_Object = MibTableColumn
snL4VirtualServerHistoryIntervalStart = _SnL4VirtualServerHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 3),
    _SnL4VirtualServerHistoryIntervalStart_Type()
)
snL4VirtualServerHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryIntervalStart.setStatus("mandatory")
_SnL4VirtualServerHistoryReceivePkts_Type = Counter32
_SnL4VirtualServerHistoryReceivePkts_Object = MibTableColumn
snL4VirtualServerHistoryReceivePkts = _SnL4VirtualServerHistoryReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 4),
    _SnL4VirtualServerHistoryReceivePkts_Type()
)
snL4VirtualServerHistoryReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryReceivePkts.setStatus("mandatory")
_SnL4VirtualServerHistoryTransmitPkts_Type = Counter32
_SnL4VirtualServerHistoryTransmitPkts_Object = MibTableColumn
snL4VirtualServerHistoryTransmitPkts = _SnL4VirtualServerHistoryTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 5),
    _SnL4VirtualServerHistoryTransmitPkts_Type()
)
snL4VirtualServerHistoryTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryTransmitPkts.setStatus("mandatory")
_SnL4VirtualServerHistoryTotalConnections_Type = Counter32
_SnL4VirtualServerHistoryTotalConnections_Object = MibTableColumn
snL4VirtualServerHistoryTotalConnections = _SnL4VirtualServerHistoryTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 6),
    _SnL4VirtualServerHistoryTotalConnections_Type()
)
snL4VirtualServerHistoryTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryTotalConnections.setStatus("mandatory")
_SnL4VirtualServerHistoryCurConnections_Type = Integer32
_SnL4VirtualServerHistoryCurConnections_Object = MibTableColumn
snL4VirtualServerHistoryCurConnections = _SnL4VirtualServerHistoryCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 7),
    _SnL4VirtualServerHistoryCurConnections_Type()
)
snL4VirtualServerHistoryCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryCurConnections.setStatus("mandatory")
_SnL4VirtualServerHistoryPeakConnections_Type = Integer32
_SnL4VirtualServerHistoryPeakConnections_Object = MibTableColumn
snL4VirtualServerHistoryPeakConnections = _SnL4VirtualServerHistoryPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 6, 1, 8),
    _SnL4VirtualServerHistoryPeakConnections_Type()
)
snL4VirtualServerHistoryPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerHistoryPeakConnections.setStatus("mandatory")
_SnL4VirtualServerPortHistoryControlTable_Object = MibTable
snL4VirtualServerPortHistoryControlTable = _SnL4VirtualServerPortHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7)
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlTable.setStatus("mandatory")
_SnL4VirtualServerPortHistoryControlEntry_Object = MibTableRow
snL4VirtualServerPortHistoryControlEntry = _SnL4VirtualServerPortHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1)
)
snL4VirtualServerPortHistoryControlEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortHistoryControlIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlEntry.setStatus("mandatory")


class _SnL4VirtualServerPortHistoryControlIndex_Type(Integer32):
    """Custom type snL4VirtualServerPortHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerPortHistoryControlIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistoryControlIndex_Object = MibTableColumn
snL4VirtualServerPortHistoryControlIndex = _SnL4VirtualServerPortHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 1),
    _SnL4VirtualServerPortHistoryControlIndex_Type()
)
snL4VirtualServerPortHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlIndex.setStatus("mandatory")
_SnL4VirtualServerPortHistoryControlDataSource_Type = ObjectIdentifier
_SnL4VirtualServerPortHistoryControlDataSource_Object = MibTableColumn
snL4VirtualServerPortHistoryControlDataSource = _SnL4VirtualServerPortHistoryControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 2),
    _SnL4VirtualServerPortHistoryControlDataSource_Type()
)
snL4VirtualServerPortHistoryControlDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlDataSource.setStatus("mandatory")


class _SnL4VirtualServerPortHistoryControlBucketsRequested_Type(Integer32):
    """Custom type snL4VirtualServerPortHistoryControlBucketsRequested based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerPortHistoryControlBucketsRequested_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistoryControlBucketsRequested_Object = MibTableColumn
snL4VirtualServerPortHistoryControlBucketsRequested = _SnL4VirtualServerPortHistoryControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 3),
    _SnL4VirtualServerPortHistoryControlBucketsRequested_Type()
)
snL4VirtualServerPortHistoryControlBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlBucketsRequested.setStatus("mandatory")


class _SnL4VirtualServerPortHistoryControlBucketsGranted_Type(Integer32):
    """Custom type snL4VirtualServerPortHistoryControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerPortHistoryControlBucketsGranted_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistoryControlBucketsGranted_Object = MibTableColumn
snL4VirtualServerPortHistoryControlBucketsGranted = _SnL4VirtualServerPortHistoryControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 4),
    _SnL4VirtualServerPortHistoryControlBucketsGranted_Type()
)
snL4VirtualServerPortHistoryControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlBucketsGranted.setStatus("mandatory")


class _SnL4VirtualServerPortHistoryControlInterval_Type(Integer32):
    """Custom type snL4VirtualServerPortHistoryControlInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SnL4VirtualServerPortHistoryControlInterval_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistoryControlInterval_Object = MibTableColumn
snL4VirtualServerPortHistoryControlInterval = _SnL4VirtualServerPortHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 5),
    _SnL4VirtualServerPortHistoryControlInterval_Type()
)
snL4VirtualServerPortHistoryControlInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlInterval.setStatus("mandatory")
_SnL4VirtualServerPortHistoryControlOwner_Type = DisplayString
_SnL4VirtualServerPortHistoryControlOwner_Object = MibTableColumn
snL4VirtualServerPortHistoryControlOwner = _SnL4VirtualServerPortHistoryControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 6),
    _SnL4VirtualServerPortHistoryControlOwner_Type()
)
snL4VirtualServerPortHistoryControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlOwner.setStatus("mandatory")


class _SnL4VirtualServerPortHistoryControlStatus_Type(Integer32):
    """Custom type snL4VirtualServerPortHistoryControlStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_SnL4VirtualServerPortHistoryControlStatus_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistoryControlStatus_Object = MibTableColumn
snL4VirtualServerPortHistoryControlStatus = _SnL4VirtualServerPortHistoryControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 7, 1, 7),
    _SnL4VirtualServerPortHistoryControlStatus_Type()
)
snL4VirtualServerPortHistoryControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryControlStatus.setStatus("mandatory")
_SnL4VirtualServerPortHistoryTable_Object = MibTable
snL4VirtualServerPortHistoryTable = _SnL4VirtualServerPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8)
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryTable.setStatus("mandatory")
_SnL4VirtualServerPortHistoryEntry_Object = MibTableRow
snL4VirtualServerPortHistoryEntry = _SnL4VirtualServerPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1)
)
snL4VirtualServerPortHistoryEntry.setIndexNames(
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortHistoryIndex"),
    (0, "HP-SN-SW-L4-SWITCH-GROUP-MIB", "snL4VirtualServerPortHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryEntry.setStatus("mandatory")


class _SnL4VirtualServerPortHistoryIndex_Type(Integer32):
    """Custom type snL4VirtualServerPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnL4VirtualServerPortHistoryIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistoryIndex_Object = MibTableColumn
snL4VirtualServerPortHistoryIndex = _SnL4VirtualServerPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 1),
    _SnL4VirtualServerPortHistoryIndex_Type()
)
snL4VirtualServerPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryIndex.setStatus("mandatory")


class _SnL4VirtualServerPortHistorySampleIndex_Type(Integer32):
    """Custom type snL4VirtualServerPortHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnL4VirtualServerPortHistorySampleIndex_Type.__name__ = "Integer32"
_SnL4VirtualServerPortHistorySampleIndex_Object = MibTableColumn
snL4VirtualServerPortHistorySampleIndex = _SnL4VirtualServerPortHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 2),
    _SnL4VirtualServerPortHistorySampleIndex_Type()
)
snL4VirtualServerPortHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistorySampleIndex.setStatus("mandatory")
_SnL4VirtualServerPortHistoryIntervalStart_Type = TimeTicks
_SnL4VirtualServerPortHistoryIntervalStart_Object = MibTableColumn
snL4VirtualServerPortHistoryIntervalStart = _SnL4VirtualServerPortHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 3),
    _SnL4VirtualServerPortHistoryIntervalStart_Type()
)
snL4VirtualServerPortHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryIntervalStart.setStatus("mandatory")
_SnL4VirtualServerPortHistoryReceivePkts_Type = Counter32
_SnL4VirtualServerPortHistoryReceivePkts_Object = MibTableColumn
snL4VirtualServerPortHistoryReceivePkts = _SnL4VirtualServerPortHistoryReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 4),
    _SnL4VirtualServerPortHistoryReceivePkts_Type()
)
snL4VirtualServerPortHistoryReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryReceivePkts.setStatus("mandatory")
_SnL4VirtualServerPortHistoryTransmitPkts_Type = Counter32
_SnL4VirtualServerPortHistoryTransmitPkts_Object = MibTableColumn
snL4VirtualServerPortHistoryTransmitPkts = _SnL4VirtualServerPortHistoryTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 5),
    _SnL4VirtualServerPortHistoryTransmitPkts_Type()
)
snL4VirtualServerPortHistoryTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryTransmitPkts.setStatus("mandatory")
_SnL4VirtualServerPortHistoryTotalConnections_Type = Counter32
_SnL4VirtualServerPortHistoryTotalConnections_Object = MibTableColumn
snL4VirtualServerPortHistoryTotalConnections = _SnL4VirtualServerPortHistoryTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 6),
    _SnL4VirtualServerPortHistoryTotalConnections_Type()
)
snL4VirtualServerPortHistoryTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryTotalConnections.setStatus("mandatory")
_SnL4VirtualServerPortHistoryCurConnections_Type = Integer32
_SnL4VirtualServerPortHistoryCurConnections_Object = MibTableColumn
snL4VirtualServerPortHistoryCurConnections = _SnL4VirtualServerPortHistoryCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 7),
    _SnL4VirtualServerPortHistoryCurConnections_Type()
)
snL4VirtualServerPortHistoryCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryCurConnections.setStatus("mandatory")
_SnL4VirtualServerPortHistoryPeakConnections_Type = Integer32
_SnL4VirtualServerPortHistoryPeakConnections_Object = MibTableColumn
snL4VirtualServerPortHistoryPeakConnections = _SnL4VirtualServerPortHistoryPeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4, 28, 8, 1, 8),
    _SnL4VirtualServerPortHistoryPeakConnections_Type()
)
snL4VirtualServerPortHistoryPeakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snL4VirtualServerPortHistoryPeakConnections.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-SW-L4-SWITCH-GROUP-MIB",
    **{"L4RowSts": L4RowSts,
       "L4Status": L4Status,
       "L4ServerName": L4ServerName,
       "L4Flag": L4Flag,
       "L4DeleteState": L4DeleteState,
       "WebCacheState": WebCacheState,
       "PhysAddress": PhysAddress,
       "DisplayString": DisplayString,
       "snL4Gen": snL4Gen,
       "snL4MaxSessionLimit": snL4MaxSessionLimit,
       "snL4TcpSynLimit": snL4TcpSynLimit,
       "snL4slbGlobalSDAType": snL4slbGlobalSDAType,
       "snL4slbTotalConnections": snL4slbTotalConnections,
       "snL4slbLimitExceeds": snL4slbLimitExceeds,
       "snL4slbForwardTraffic": snL4slbForwardTraffic,
       "snL4slbReverseTraffic": snL4slbReverseTraffic,
       "snL4slbDrops": snL4slbDrops,
       "snL4slbDangling": snL4slbDangling,
       "snL4slbDisableCount": snL4slbDisableCount,
       "snL4slbAged": snL4slbAged,
       "snL4slbFinished": snL4slbFinished,
       "snL4FreeSessionCount": snL4FreeSessionCount,
       "snL4BackupInterface": snL4BackupInterface,
       "snL4BackupMacAddr": snL4BackupMacAddr,
       "snL4Active": snL4Active,
       "snL4Redundancy": snL4Redundancy,
       "snL4Backup": snL4Backup,
       "snL4BecomeActive": snL4BecomeActive,
       "snL4BecomeStandBy": snL4BecomeStandBy,
       "snL4BackupState": snL4BackupState,
       "snL4NoPDUSent": snL4NoPDUSent,
       "snL4NoPDUCount": snL4NoPDUCount,
       "snL4NoPortMap": snL4NoPortMap,
       "snL4unsuccessfulConn": snL4unsuccessfulConn,
       "snL4PingInterval": snL4PingInterval,
       "snL4PingRetry": snL4PingRetry,
       "snL4TcpAge": snL4TcpAge,
       "snL4UdpAge": snL4UdpAge,
       "snL4EnableMaxSessionLimitReachedTrap": snL4EnableMaxSessionLimitReachedTrap,
       "snL4EnableTcpSynLimitReachedTrap": snL4EnableTcpSynLimitReachedTrap,
       "snL4EnableRealServerUpTrap": snL4EnableRealServerUpTrap,
       "snL4EnableRealServerDownTrap": snL4EnableRealServerDownTrap,
       "snL4EnableRealServerPortUpTrap": snL4EnableRealServerPortUpTrap,
       "snL4EnableRealServerPortDownTrap": snL4EnableRealServerPortDownTrap,
       "snL4EnableRealServerMaxConnLimitReachedTrap": snL4EnableRealServerMaxConnLimitReachedTrap,
       "snL4EnableBecomeStandbyTrap": snL4EnableBecomeStandbyTrap,
       "snL4EnableBecomeActiveTrap": snL4EnableBecomeActiveTrap,
       "snL4slbRouterInterfacePortMask": snL4slbRouterInterfacePortMask,
       "snL4MaxNumWebCacheGroup": snL4MaxNumWebCacheGroup,
       "snL4MaxNumWebCachePerGroup": snL4MaxNumWebCachePerGroup,
       "snL4WebCacheStateful": snL4WebCacheStateful,
       "snL4EnableGslbHealthCheckIpUpTrap": snL4EnableGslbHealthCheckIpUpTrap,
       "snL4EnableGslbHealthCheckIpDownTrap": snL4EnableGslbHealthCheckIpDownTrap,
       "snL4EnableGslbHealthCheckIpPortUpTrap": snL4EnableGslbHealthCheckIpPortUpTrap,
       "snL4EnableGslbHealthCheckIpPortDownTrap": snL4EnableGslbHealthCheckIpPortDownTrap,
       "snL4EnableGslbRemoteGslbSiDownTrap": snL4EnableGslbRemoteGslbSiDownTrap,
       "snL4EnableGslbRemoteGslbSiUpTrap": snL4EnableGslbRemoteGslbSiUpTrap,
       "snL4EnableGslbRemoteSiDownTrap": snL4EnableGslbRemoteSiDownTrap,
       "snL4EnableGslbRemoteSiUpTrap": snL4EnableGslbRemoteSiUpTrap,
       "snL4slbRouterInterfacePortList": snL4slbRouterInterfacePortList,
       "snL4VirtualServer": snL4VirtualServer,
       "snL4VirtualServerTable": snL4VirtualServerTable,
       "snL4VirtualServerEntry": snL4VirtualServerEntry,
       "snL4VirtualServerIndex": snL4VirtualServerIndex,
       "snL4VirtualServerName": snL4VirtualServerName,
       "snL4VirtualServerVirtualIP": snL4VirtualServerVirtualIP,
       "snL4VirtualServerAdminStatus": snL4VirtualServerAdminStatus,
       "snL4VirtualServerSDAType": snL4VirtualServerSDAType,
       "snL4VirtualServerRowStatus": snL4VirtualServerRowStatus,
       "snL4VirtualServerDeleteState": snL4VirtualServerDeleteState,
       "snL4RealServer": snL4RealServer,
       "snL4RealServerTable": snL4RealServerTable,
       "snL4RealServerEntry": snL4RealServerEntry,
       "snL4RealServerIndex": snL4RealServerIndex,
       "snL4RealServerName": snL4RealServerName,
       "snL4RealServerIP": snL4RealServerIP,
       "snL4RealServerAdminStatus": snL4RealServerAdminStatus,
       "snL4RealServerMaxConnections": snL4RealServerMaxConnections,
       "snL4RealServerWeight": snL4RealServerWeight,
       "snL4RealServerRowStatus": snL4RealServerRowStatus,
       "snL4RealServerDeleteState": snL4RealServerDeleteState,
       "snL4VirtualServerPort": snL4VirtualServerPort,
       "snL4VirtualServerPortTable": snL4VirtualServerPortTable,
       "snL4VirtualServerPortEntry": snL4VirtualServerPortEntry,
       "snL4VirtualServerPortIndex": snL4VirtualServerPortIndex,
       "snL4VirtualServerPortServerName": snL4VirtualServerPortServerName,
       "snL4VirtualServerPortPort": snL4VirtualServerPortPort,
       "snL4VirtualServerPortAdminStatus": snL4VirtualServerPortAdminStatus,
       "snL4VirtualServerPortSticky": snL4VirtualServerPortSticky,
       "snL4VirtualServerPortConcurrent": snL4VirtualServerPortConcurrent,
       "snL4VirtualServerPortRowStatus": snL4VirtualServerPortRowStatus,
       "snL4VirtualServerPortDeleteState": snL4VirtualServerPortDeleteState,
       "snL4RealServerPort": snL4RealServerPort,
       "snL4RealServerPortTable": snL4RealServerPortTable,
       "snL4RealServerPortEntry": snL4RealServerPortEntry,
       "snL4RealServerPortIndex": snL4RealServerPortIndex,
       "snL4RealServerPortServerName": snL4RealServerPortServerName,
       "snL4RealServerPortPort": snL4RealServerPortPort,
       "snL4RealServerPortAdminStatus": snL4RealServerPortAdminStatus,
       "snL4RealServerPortRowStatus": snL4RealServerPortRowStatus,
       "snL4RealServerPortDeleteState": snL4RealServerPortDeleteState,
       "snL4Bind": snL4Bind,
       "snL4BindTable": snL4BindTable,
       "snL4BindEntry": snL4BindEntry,
       "snL4BindIndex": snL4BindIndex,
       "snL4BindVirtualServerName": snL4BindVirtualServerName,
       "snL4BindVirtualPortNumber": snL4BindVirtualPortNumber,
       "snL4BindRealServerName": snL4BindRealServerName,
       "snL4BindRealPortNumber": snL4BindRealPortNumber,
       "snL4BindRowStatus": snL4BindRowStatus,
       "snL4VirtualServerStatus": snL4VirtualServerStatus,
       "snL4VirtualServerStatusTable": snL4VirtualServerStatusTable,
       "snL4VirtualServerStatusEntry": snL4VirtualServerStatusEntry,
       "snL4VirtualServerStatusIndex": snL4VirtualServerStatusIndex,
       "snL4VirtualServerStatusName": snL4VirtualServerStatusName,
       "snL4VirtualServerStatusReceivePkts": snL4VirtualServerStatusReceivePkts,
       "snL4VirtualServerStatusTransmitPkts": snL4VirtualServerStatusTransmitPkts,
       "snL4VirtualServerStatusTotalConnections": snL4VirtualServerStatusTotalConnections,
       "snL4RealServerStatus": snL4RealServerStatus,
       "snL4RealServerStatusTable": snL4RealServerStatusTable,
       "snL4RealServerStatusEntry": snL4RealServerStatusEntry,
       "snL4RealServerStatusIndex": snL4RealServerStatusIndex,
       "snL4RealServerStatusName": snL4RealServerStatusName,
       "snL4RealServerStatusRealIP": snL4RealServerStatusRealIP,
       "snL4RealServerStatusReceivePkts": snL4RealServerStatusReceivePkts,
       "snL4RealServerStatusTransmitPkts": snL4RealServerStatusTransmitPkts,
       "snL4RealServerStatusCurConnections": snL4RealServerStatusCurConnections,
       "snL4RealServerStatusTotalConnections": snL4RealServerStatusTotalConnections,
       "snL4RealServerStatusAge": snL4RealServerStatusAge,
       "snL4RealServerStatusState": snL4RealServerStatusState,
       "snL4RealServerStatusReassignments": snL4RealServerStatusReassignments,
       "snL4RealServerStatusReassignmentLimit": snL4RealServerStatusReassignmentLimit,
       "snL4RealServerStatusFailedPortExists": snL4RealServerStatusFailedPortExists,
       "snL4RealServerStatusFailTime": snL4RealServerStatusFailTime,
       "snL4RealServerStatusPeakConnections": snL4RealServerStatusPeakConnections,
       "snL4VirtualServerPortStatus": snL4VirtualServerPortStatus,
       "snL4VirtualServerPortStatusTable": snL4VirtualServerPortStatusTable,
       "snL4VirtualServerPortStatusEntry": snL4VirtualServerPortStatusEntry,
       "snL4VirtualServerPortStatusIndex": snL4VirtualServerPortStatusIndex,
       "snL4VirtualServerPortStatusPort": snL4VirtualServerPortStatusPort,
       "snL4VirtualServerPortStatusServerName": snL4VirtualServerPortStatusServerName,
       "snL4VirtualServerPortStatusCurrentConnection": snL4VirtualServerPortStatusCurrentConnection,
       "snL4VirtualServerPortStatusTotalConnection": snL4VirtualServerPortStatusTotalConnection,
       "snL4VirtualServerPortStatusPeakConnection": snL4VirtualServerPortStatusPeakConnection,
       "snL4RealServerPortStatus": snL4RealServerPortStatus,
       "snL4RealServerPortStatusTable": snL4RealServerPortStatusTable,
       "snL4RealServerPortStatusEntry": snL4RealServerPortStatusEntry,
       "snL4RealServerPortStatusIndex": snL4RealServerPortStatusIndex,
       "snL4RealServerPortStatusPort": snL4RealServerPortStatusPort,
       "snL4RealServerPortStatusServerName": snL4RealServerPortStatusServerName,
       "snL4RealServerPortStatusReassignCount": snL4RealServerPortStatusReassignCount,
       "snL4RealServerPortStatusState": snL4RealServerPortStatusState,
       "snL4RealServerPortStatusFailTime": snL4RealServerPortStatusFailTime,
       "snL4RealServerPortStatusCurrentConnection": snL4RealServerPortStatusCurrentConnection,
       "snL4RealServerPortStatusTotalConnection": snL4RealServerPortStatusTotalConnection,
       "snL4RealServerPortStatusRxPkts": snL4RealServerPortStatusRxPkts,
       "snL4RealServerPortStatusTxPkts": snL4RealServerPortStatusTxPkts,
       "snL4RealServerPortStatusRxBytes": snL4RealServerPortStatusRxBytes,
       "snL4RealServerPortStatusTxBytes": snL4RealServerPortStatusTxBytes,
       "snL4RealServerPortStatusPeakConnection": snL4RealServerPortStatusPeakConnection,
       "snL4Policy": snL4Policy,
       "snL4PolicyTable": snL4PolicyTable,
       "snL4PolicyEntry": snL4PolicyEntry,
       "snL4PolicyId": snL4PolicyId,
       "snL4PolicyPriority": snL4PolicyPriority,
       "snL4PolicyScope": snL4PolicyScope,
       "snL4PolicyProtocol": snL4PolicyProtocol,
       "snL4PolicyPort": snL4PolicyPort,
       "snL4PolicyRowStatus": snL4PolicyRowStatus,
       "snL4PolicyPortAccess": snL4PolicyPortAccess,
       "snL4PolicyPortAccessTable": snL4PolicyPortAccessTable,
       "snL4PolicyPortAccessEntry": snL4PolicyPortAccessEntry,
       "snL4PolicyPortAccessPort": snL4PolicyPortAccessPort,
       "snL4PolicyPortAccessList": snL4PolicyPortAccessList,
       "snL4PolicyPortAccessRowStatus": snL4PolicyPortAccessRowStatus,
       "snL4Trap": snL4Trap,
       "snL4TrapRealServerIP": snL4TrapRealServerIP,
       "snL4TrapRealServerName": snL4TrapRealServerName,
       "snL4TrapRealServerPort": snL4TrapRealServerPort,
       "snL4TrapRealServerCurConnections": snL4TrapRealServerCurConnections,
       "snL4WebCache": snL4WebCache,
       "snL4WebCacheTable": snL4WebCacheTable,
       "snL4WebCacheEntry": snL4WebCacheEntry,
       "snL4WebCacheIP": snL4WebCacheIP,
       "snL4WebCacheName": snL4WebCacheName,
       "snL4WebCacheAdminStatus": snL4WebCacheAdminStatus,
       "snL4WebCacheMaxConnections": snL4WebCacheMaxConnections,
       "snL4WebCacheWeight": snL4WebCacheWeight,
       "snL4WebCacheRowStatus": snL4WebCacheRowStatus,
       "snL4WebCacheDeleteState": snL4WebCacheDeleteState,
       "snL4WebCacheGroup": snL4WebCacheGroup,
       "snL4WebCacheGroupTable": snL4WebCacheGroupTable,
       "snL4WebCacheGroupEntry": snL4WebCacheGroupEntry,
       "snL4WebCacheGroupId": snL4WebCacheGroupId,
       "snL4WebCacheGroupName": snL4WebCacheGroupName,
       "snL4WebCacheGroupWebCacheIpList": snL4WebCacheGroupWebCacheIpList,
       "snL4WebCacheGroupDestMask": snL4WebCacheGroupDestMask,
       "snL4WebCacheGroupSrcMask": snL4WebCacheGroupSrcMask,
       "snL4WebCacheGroupAdminStatus": snL4WebCacheGroupAdminStatus,
       "snL4WebCacheGroupRowStatus": snL4WebCacheGroupRowStatus,
       "snL4WebCacheTrafficStats": snL4WebCacheTrafficStats,
       "snL4WebCacheTrafficStatsTable": snL4WebCacheTrafficStatsTable,
       "snL4WebCacheTrafficStatsEntry": snL4WebCacheTrafficStatsEntry,
       "snL4WebCacheTrafficIp": snL4WebCacheTrafficIp,
       "snL4WebCacheTrafficPort": snL4WebCacheTrafficPort,
       "snL4WebCacheCurrConnections": snL4WebCacheCurrConnections,
       "snL4WebCacheTotalConnections": snL4WebCacheTotalConnections,
       "snL4WebCacheTxPkts": snL4WebCacheTxPkts,
       "snL4WebCacheRxPkts": snL4WebCacheRxPkts,
       "snL4WebCacheTxOctets": snL4WebCacheTxOctets,
       "snL4WebCacheRxOctets": snL4WebCacheRxOctets,
       "snL4WebCachePortState": snL4WebCachePortState,
       "snL4WebUncachedTrafficStats": snL4WebUncachedTrafficStats,
       "snL4WebUncachedTrafficStatsTable": snL4WebUncachedTrafficStatsTable,
       "snL4WebUncachedTrafficStatsEntry": snL4WebUncachedTrafficStatsEntry,
       "snL4WebServerPort": snL4WebServerPort,
       "snL4WebClientPort": snL4WebClientPort,
       "snL4WebUncachedTxPkts": snL4WebUncachedTxPkts,
       "snL4WebUncachedRxPkts": snL4WebUncachedRxPkts,
       "snL4WebUncachedTxOctets": snL4WebUncachedTxOctets,
       "snL4WebUncachedRxOctets": snL4WebUncachedRxOctets,
       "snL4WebServerPortName": snL4WebServerPortName,
       "snL4WebClientPortName": snL4WebClientPortName,
       "snL4WebCachePort": snL4WebCachePort,
       "snL4WebCachePortTable": snL4WebCachePortTable,
       "snL4WebCachePortEntry": snL4WebCachePortEntry,
       "snL4WebCachePortServerIp": snL4WebCachePortServerIp,
       "snL4WebCachePortPort": snL4WebCachePortPort,
       "snL4WebCachePortAdminStatus": snL4WebCachePortAdminStatus,
       "snL4WebCachePortRowStatus": snL4WebCachePortRowStatus,
       "snL4WebCachePortDeleteState": snL4WebCachePortDeleteState,
       "snL4RealServerCfg": snL4RealServerCfg,
       "snL4RealServerCfgTable": snL4RealServerCfgTable,
       "snL4RealServerCfgEntry": snL4RealServerCfgEntry,
       "snL4RealServerCfgIP": snL4RealServerCfgIP,
       "snL4RealServerCfgName": snL4RealServerCfgName,
       "snL4RealServerCfgAdminStatus": snL4RealServerCfgAdminStatus,
       "snL4RealServerCfgMaxConnections": snL4RealServerCfgMaxConnections,
       "snL4RealServerCfgWeight": snL4RealServerCfgWeight,
       "snL4RealServerCfgRowStatus": snL4RealServerCfgRowStatus,
       "snL4RealServerCfgDeleteState": snL4RealServerCfgDeleteState,
       "snL4RealServerPortCfg": snL4RealServerPortCfg,
       "snL4RealServerPortCfgTable": snL4RealServerPortCfgTable,
       "snL4RealServerPortCfgEntry": snL4RealServerPortCfgEntry,
       "snL4RealServerPortCfgIP": snL4RealServerPortCfgIP,
       "snL4RealServerPortCfgServerName": snL4RealServerPortCfgServerName,
       "snL4RealServerPortCfgPort": snL4RealServerPortCfgPort,
       "snL4RealServerPortCfgAdminStatus": snL4RealServerPortCfgAdminStatus,
       "snL4RealServerPortCfgRowStatus": snL4RealServerPortCfgRowStatus,
       "snL4RealServerPortCfgDeleteState": snL4RealServerPortCfgDeleteState,
       "snL4VirtualServerCfg": snL4VirtualServerCfg,
       "snL4VirtualServerCfgTable": snL4VirtualServerCfgTable,
       "snL4VirtualServerCfgEntry": snL4VirtualServerCfgEntry,
       "snL4VirtualServerCfgVirtualIP": snL4VirtualServerCfgVirtualIP,
       "snL4VirtualServerCfgName": snL4VirtualServerCfgName,
       "snL4VirtualServerCfgAdminStatus": snL4VirtualServerCfgAdminStatus,
       "snL4VirtualServerCfgSDAType": snL4VirtualServerCfgSDAType,
       "snL4VirtualServerCfgRowStatus": snL4VirtualServerCfgRowStatus,
       "snL4VirtualServerCfgDeleteState": snL4VirtualServerCfgDeleteState,
       "snL4VirtualServerPortCfg": snL4VirtualServerPortCfg,
       "snL4VirtualServerPortCfgTable": snL4VirtualServerPortCfgTable,
       "snL4VirtualServerPortCfgEntry": snL4VirtualServerPortCfgEntry,
       "snL4VirtualServerPortCfgIP": snL4VirtualServerPortCfgIP,
       "snL4VirtualServerPortCfgPort": snL4VirtualServerPortCfgPort,
       "snL4VirtualServerPortCfgServerName": snL4VirtualServerPortCfgServerName,
       "snL4VirtualServerPortCfgAdminStatus": snL4VirtualServerPortCfgAdminStatus,
       "snL4VirtualServerPortCfgSticky": snL4VirtualServerPortCfgSticky,
       "snL4VirtualServerPortCfgConcurrent": snL4VirtualServerPortCfgConcurrent,
       "snL4VirtualServerPortCfgRowStatus": snL4VirtualServerPortCfgRowStatus,
       "snL4VirtualServerPortCfgDeleteState": snL4VirtualServerPortCfgDeleteState,
       "snL4RealServerStatistic": snL4RealServerStatistic,
       "snL4RealServerStatisticTable": snL4RealServerStatisticTable,
       "snL4RealServerStatisticEntry": snL4RealServerStatisticEntry,
       "snL4RealServerStatisticRealIP": snL4RealServerStatisticRealIP,
       "snL4RealServerStatisticName": snL4RealServerStatisticName,
       "snL4RealServerStatisticReceivePkts": snL4RealServerStatisticReceivePkts,
       "snL4RealServerStatisticTransmitPkts": snL4RealServerStatisticTransmitPkts,
       "snL4RealServerStatisticCurConnections": snL4RealServerStatisticCurConnections,
       "snL4RealServerStatisticTotalConnections": snL4RealServerStatisticTotalConnections,
       "snL4RealServerStatisticAge": snL4RealServerStatisticAge,
       "snL4RealServerStatisticState": snL4RealServerStatisticState,
       "snL4RealServerStatisticReassignments": snL4RealServerStatisticReassignments,
       "snL4RealServerStatisticReassignmentLimit": snL4RealServerStatisticReassignmentLimit,
       "snL4RealServerStatisticFailedPortExists": snL4RealServerStatisticFailedPortExists,
       "snL4RealServerStatisticFailTime": snL4RealServerStatisticFailTime,
       "snL4RealServerStatisticPeakConnections": snL4RealServerStatisticPeakConnections,
       "snL4RealServerPortStatistic": snL4RealServerPortStatistic,
       "snL4RealServerPortStatisticTable": snL4RealServerPortStatisticTable,
       "snL4RealServerPortStatisticEntry": snL4RealServerPortStatisticEntry,
       "snL4RealServerPortStatisticIP": snL4RealServerPortStatisticIP,
       "snL4RealServerPortStatisticPort": snL4RealServerPortStatisticPort,
       "snL4RealServerPortStatisticServerName": snL4RealServerPortStatisticServerName,
       "snL4RealServerPortStatisticReassignCount": snL4RealServerPortStatisticReassignCount,
       "snL4RealServerPortStatisticState": snL4RealServerPortStatisticState,
       "snL4RealServerPortStatisticFailTime": snL4RealServerPortStatisticFailTime,
       "snL4RealServerPortStatisticCurrentConnection": snL4RealServerPortStatisticCurrentConnection,
       "snL4RealServerPortStatisticTotalConnection": snL4RealServerPortStatisticTotalConnection,
       "snL4RealServerPortStatisticRxPkts": snL4RealServerPortStatisticRxPkts,
       "snL4RealServerPortStatisticTxPkts": snL4RealServerPortStatisticTxPkts,
       "snL4RealServerPortStatisticRxBytes": snL4RealServerPortStatisticRxBytes,
       "snL4RealServerPortStatisticTxBytes": snL4RealServerPortStatisticTxBytes,
       "snL4RealServerPortStatisticPeakConnection": snL4RealServerPortStatisticPeakConnection,
       "snL4VirtualServerStatistic": snL4VirtualServerStatistic,
       "snL4VirtualServerStatisticTable": snL4VirtualServerStatisticTable,
       "snL4VirtualServerStatisticEntry": snL4VirtualServerStatisticEntry,
       "snL4VirtualServerStatisticIP": snL4VirtualServerStatisticIP,
       "snL4VirtualServerStatisticName": snL4VirtualServerStatisticName,
       "snL4VirtualServerStatisticReceivePkts": snL4VirtualServerStatisticReceivePkts,
       "snL4VirtualServerStatisticTransmitPkts": snL4VirtualServerStatisticTransmitPkts,
       "snL4VirtualServerStatisticTotalConnections": snL4VirtualServerStatisticTotalConnections,
       "snL4VirtualServerStatisticReceiveBytes": snL4VirtualServerStatisticReceiveBytes,
       "snL4VirtualServerStatisticTransmitBytes": snL4VirtualServerStatisticTransmitBytes,
       "snL4VirtualServerStatisticSymmetricState": snL4VirtualServerStatisticSymmetricState,
       "snL4VirtualServerStatisticSymmetricPriority": snL4VirtualServerStatisticSymmetricPriority,
       "snL4VirtualServerStatisticSymmetricKeep": snL4VirtualServerStatisticSymmetricKeep,
       "snL4VirtualServerStatisticSymmetricActivates": snL4VirtualServerStatisticSymmetricActivates,
       "snL4VirtualServerStatisticSymmetricInactives": snL4VirtualServerStatisticSymmetricInactives,
       "snL4VirtualServerStatisticSymmetricBestStandbyMacAddr": snL4VirtualServerStatisticSymmetricBestStandbyMacAddr,
       "snL4VirtualServerStatisticSymmetricActiveMacAddr": snL4VirtualServerStatisticSymmetricActiveMacAddr,
       "snL4VirtualServerPortStatistic": snL4VirtualServerPortStatistic,
       "snL4VirtualServerPortStatisticTable": snL4VirtualServerPortStatisticTable,
       "snL4VirtualServerPortStatisticEntry": snL4VirtualServerPortStatisticEntry,
       "snL4VirtualServerPortStatisticIP": snL4VirtualServerPortStatisticIP,
       "snL4VirtualServerPortStatisticPort": snL4VirtualServerPortStatisticPort,
       "snL4VirtualServerPortStatisticServerName": snL4VirtualServerPortStatisticServerName,
       "snL4VirtualServerPortStatisticCurrentConnection": snL4VirtualServerPortStatisticCurrentConnection,
       "snL4VirtualServerPortStatisticTotalConnection": snL4VirtualServerPortStatisticTotalConnection,
       "snL4VirtualServerPortStatisticPeakConnection": snL4VirtualServerPortStatisticPeakConnection,
       "snL4GslbSiteRemoteServerIrons": snL4GslbSiteRemoteServerIrons,
       "snL4GslbSiteRemoteServerIronTable": snL4GslbSiteRemoteServerIronTable,
       "snL4GslbSiteRemoteServerIronEntry": snL4GslbSiteRemoteServerIronEntry,
       "snL4GslbSiteRemoteServerIronIP": snL4GslbSiteRemoteServerIronIP,
       "snL4GslbSiteRemoteServerIronPreference": snL4GslbSiteRemoteServerIronPreference,
       "snL4History": snL4History,
       "snL4RealServerHistoryControlTable": snL4RealServerHistoryControlTable,
       "snL4RealServerHistoryControlEntry": snL4RealServerHistoryControlEntry,
       "snL4RealServerHistoryControlIndex": snL4RealServerHistoryControlIndex,
       "snL4RealServerHistoryControlDataSource": snL4RealServerHistoryControlDataSource,
       "snL4RealServerHistoryControlBucketsRequested": snL4RealServerHistoryControlBucketsRequested,
       "snL4RealServerHistoryControlBucketsGranted": snL4RealServerHistoryControlBucketsGranted,
       "snL4RealServerHistoryControlInterval": snL4RealServerHistoryControlInterval,
       "snL4RealServerHistoryControlOwner": snL4RealServerHistoryControlOwner,
       "snL4RealServerHistoryControlStatus": snL4RealServerHistoryControlStatus,
       "snL4RealServerHistoryTable": snL4RealServerHistoryTable,
       "snL4RealServerHistoryEntry": snL4RealServerHistoryEntry,
       "snL4RealServerHistoryIndex": snL4RealServerHistoryIndex,
       "snL4RealServerHistorySampleIndex": snL4RealServerHistorySampleIndex,
       "snL4RealServerHistoryIntervalStart": snL4RealServerHistoryIntervalStart,
       "snL4RealServerHistoryReceivePkts": snL4RealServerHistoryReceivePkts,
       "snL4RealServerHistoryTransmitPkts": snL4RealServerHistoryTransmitPkts,
       "snL4RealServerHistoryTotalConnections": snL4RealServerHistoryTotalConnections,
       "snL4RealServerHistoryCurConnections": snL4RealServerHistoryCurConnections,
       "snL4RealServerHistoryPeakConnections": snL4RealServerHistoryPeakConnections,
       "snL4RealServerHistoryReassignments": snL4RealServerHistoryReassignments,
       "snL4RealServerPortHistoryControlTable": snL4RealServerPortHistoryControlTable,
       "snL4RealServerPortHistoryControlEntry": snL4RealServerPortHistoryControlEntry,
       "snL4RealServerPortHistoryControlIndex": snL4RealServerPortHistoryControlIndex,
       "snL4RealServerPortHistoryControlDataSource": snL4RealServerPortHistoryControlDataSource,
       "snL4RealServerPortHistoryControlBucketsRequested": snL4RealServerPortHistoryControlBucketsRequested,
       "snL4RealServerPortHistoryControlBucketsGranted": snL4RealServerPortHistoryControlBucketsGranted,
       "snL4RealServerPortHistoryControlInterval": snL4RealServerPortHistoryControlInterval,
       "snL4RealServerPortHistoryControlOwner": snL4RealServerPortHistoryControlOwner,
       "snL4RealServerPortHistoryControlStatus": snL4RealServerPortHistoryControlStatus,
       "snL4RealServerPortHistoryTable": snL4RealServerPortHistoryTable,
       "snL4RealServerPortHistoryEntry": snL4RealServerPortHistoryEntry,
       "snL4RealServerPortHistoryIndex": snL4RealServerPortHistoryIndex,
       "snL4RealServerPortHistorySampleIndex": snL4RealServerPortHistorySampleIndex,
       "snL4RealServerPortHistoryIntervalStart": snL4RealServerPortHistoryIntervalStart,
       "snL4RealServerPortHistoryReceivePkts": snL4RealServerPortHistoryReceivePkts,
       "snL4RealServerPortHistoryTransmitPkts": snL4RealServerPortHistoryTransmitPkts,
       "snL4RealServerPortHistoryTotalConnections": snL4RealServerPortHistoryTotalConnections,
       "snL4RealServerPortHistoryCurConnections": snL4RealServerPortHistoryCurConnections,
       "snL4RealServerPortHistoryPeakConnections": snL4RealServerPortHistoryPeakConnections,
       "snL4RealServerPortHistoryResponseTime": snL4RealServerPortHistoryResponseTime,
       "snL4VirtualServerHistoryControlTable": snL4VirtualServerHistoryControlTable,
       "snL4VirtualServerHistoryControlEntry": snL4VirtualServerHistoryControlEntry,
       "snL4VirtualServerHistoryControlIndex": snL4VirtualServerHistoryControlIndex,
       "snL4VirtualServerHistoryControlDataSource": snL4VirtualServerHistoryControlDataSource,
       "snL4VirtualServerHistoryControlBucketsRequested": snL4VirtualServerHistoryControlBucketsRequested,
       "snL4VirtualServerHistoryControlBucketsGranted": snL4VirtualServerHistoryControlBucketsGranted,
       "snL4VirtualServerHistoryControlInterval": snL4VirtualServerHistoryControlInterval,
       "snL4VirtualServerHistoryControlOwner": snL4VirtualServerHistoryControlOwner,
       "snL4VirtualServerHistoryControlStatus": snL4VirtualServerHistoryControlStatus,
       "snL4VirtualServerHistoryTable": snL4VirtualServerHistoryTable,
       "snL4VirtualServerHistoryEntry": snL4VirtualServerHistoryEntry,
       "snL4VirtualServerHistoryIndex": snL4VirtualServerHistoryIndex,
       "snL4VirtualServerHistorySampleIndex": snL4VirtualServerHistorySampleIndex,
       "snL4VirtualServerHistoryIntervalStart": snL4VirtualServerHistoryIntervalStart,
       "snL4VirtualServerHistoryReceivePkts": snL4VirtualServerHistoryReceivePkts,
       "snL4VirtualServerHistoryTransmitPkts": snL4VirtualServerHistoryTransmitPkts,
       "snL4VirtualServerHistoryTotalConnections": snL4VirtualServerHistoryTotalConnections,
       "snL4VirtualServerHistoryCurConnections": snL4VirtualServerHistoryCurConnections,
       "snL4VirtualServerHistoryPeakConnections": snL4VirtualServerHistoryPeakConnections,
       "snL4VirtualServerPortHistoryControlTable": snL4VirtualServerPortHistoryControlTable,
       "snL4VirtualServerPortHistoryControlEntry": snL4VirtualServerPortHistoryControlEntry,
       "snL4VirtualServerPortHistoryControlIndex": snL4VirtualServerPortHistoryControlIndex,
       "snL4VirtualServerPortHistoryControlDataSource": snL4VirtualServerPortHistoryControlDataSource,
       "snL4VirtualServerPortHistoryControlBucketsRequested": snL4VirtualServerPortHistoryControlBucketsRequested,
       "snL4VirtualServerPortHistoryControlBucketsGranted": snL4VirtualServerPortHistoryControlBucketsGranted,
       "snL4VirtualServerPortHistoryControlInterval": snL4VirtualServerPortHistoryControlInterval,
       "snL4VirtualServerPortHistoryControlOwner": snL4VirtualServerPortHistoryControlOwner,
       "snL4VirtualServerPortHistoryControlStatus": snL4VirtualServerPortHistoryControlStatus,
       "snL4VirtualServerPortHistoryTable": snL4VirtualServerPortHistoryTable,
       "snL4VirtualServerPortHistoryEntry": snL4VirtualServerPortHistoryEntry,
       "snL4VirtualServerPortHistoryIndex": snL4VirtualServerPortHistoryIndex,
       "snL4VirtualServerPortHistorySampleIndex": snL4VirtualServerPortHistorySampleIndex,
       "snL4VirtualServerPortHistoryIntervalStart": snL4VirtualServerPortHistoryIntervalStart,
       "snL4VirtualServerPortHistoryReceivePkts": snL4VirtualServerPortHistoryReceivePkts,
       "snL4VirtualServerPortHistoryTransmitPkts": snL4VirtualServerPortHistoryTransmitPkts,
       "snL4VirtualServerPortHistoryTotalConnections": snL4VirtualServerPortHistoryTotalConnections,
       "snL4VirtualServerPortHistoryCurConnections": snL4VirtualServerPortHistoryCurConnections,
       "snL4VirtualServerPortHistoryPeakConnections": snL4VirtualServerPortHistoryPeakConnections}
)
