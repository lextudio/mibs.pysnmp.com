# SNMP MIB module (CISCO-WAN-SRCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-SRCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(mgcRedundancyGrpNum,) = mibBuilder.importSymbols(
    "CISCO-WAN-MGC-REDUN-MIB",
    "mgcRedundancyGrpNum")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanSrcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11)
)
ciscoWanSrcpMIB.setRevisions(
        ("2004-01-30 00:00",
         "2000-12-26 00:00",
         "2000-08-31 00:00",
         "2000-07-21 00:00",
         "2000-05-28 00:00",
         "2000-05-24 00:00",
         "1999-11-23 00:00",
         "1999-11-01 00:00",
         "1999-10-21 00:00",
         "1999-06-23 00:00",
         "1999-06-07 00:00",
         "1999-04-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SrcpObjects_ObjectIdentity = ObjectIdentity
srcpObjects = _SrcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1)
)
_SrcpAdminObjects_ObjectIdentity = ObjectIdentity
srcpAdminObjects = _SrcpAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1)
)


class _SrcpVersion_Type(DisplayString):
    """Custom type srcpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SrcpVersion_Type.__name__ = "DisplayString"
_SrcpVersion_Object = MibScalar
srcpVersion = _SrcpVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 1),
    _SrcpVersion_Type()
)
srcpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcpVersion.setStatus("current")


class _SrcpPortNumber_Type(Integer32):
    """Custom type srcpPortNumber based on Integer32"""
    defaultValue = 2428

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SrcpPortNumber_Type.__name__ = "Integer32"
_SrcpPortNumber_Object = MibScalar
srcpPortNumber = _SrcpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 2),
    _SrcpPortNumber_Type()
)
srcpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpPortNumber.setStatus("current")
_SrcpPeerTable_Object = MibTable
srcpPeerTable = _SrcpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    srcpPeerTable.setStatus("current")
_SrcpPeerEntry_Object = MibTableRow
srcpPeerEntry = _SrcpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1)
)
srcpPeerEntry.setIndexNames(
    (0, "CISCO-WAN-SRCP-MIB", "srcpPeerId"),
)
if mibBuilder.loadTexts:
    srcpPeerEntry.setStatus("current")


class _SrcpPeerId_Type(Integer32):
    """Custom type srcpPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SrcpPeerId_Type.__name__ = "Integer32"
_SrcpPeerId_Object = MibTableColumn
srcpPeerId = _SrcpPeerId_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 1),
    _SrcpPeerId_Type()
)
srcpPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srcpPeerId.setStatus("current")


class _SrcpPeerName_Type(DisplayString):
    """Custom type srcpPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SrcpPeerName_Type.__name__ = "DisplayString"
_SrcpPeerName_Object = MibTableColumn
srcpPeerName = _SrcpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 2),
    _SrcpPeerName_Type()
)
srcpPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcpPeerName.setStatus("current")


class _SrcpPeerPortNumber_Type(Integer32):
    """Custom type srcpPeerPortNumber based on Integer32"""
    defaultValue = 2428

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SrcpPeerPortNumber_Type.__name__ = "Integer32"
_SrcpPeerPortNumber_Object = MibTableColumn
srcpPeerPortNumber = _SrcpPeerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 3),
    _SrcpPeerPortNumber_Type()
)
srcpPeerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpPeerPortNumber.setStatus("current")


class _SrcpPeerHeartbeatInterval_Type(Integer32):
    """Custom type srcpPeerHeartbeatInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SrcpPeerHeartbeatInterval_Type.__name__ = "Integer32"
_SrcpPeerHeartbeatInterval_Object = MibTableColumn
srcpPeerHeartbeatInterval = _SrcpPeerHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 4),
    _SrcpPeerHeartbeatInterval_Type()
)
srcpPeerHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpPeerHeartbeatInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    srcpPeerHeartbeatInterval.setUnits("milliseconds")


class _SrcpPeerTimeSinceHeartbeat_Type(Integer32):
    """Custom type srcpPeerTimeSinceHeartbeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SrcpPeerTimeSinceHeartbeat_Type.__name__ = "Integer32"
_SrcpPeerTimeSinceHeartbeat_Object = MibTableColumn
srcpPeerTimeSinceHeartbeat = _SrcpPeerTimeSinceHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 5),
    _SrcpPeerTimeSinceHeartbeat_Type()
)
srcpPeerTimeSinceHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcpPeerTimeSinceHeartbeat.setStatus("deprecated")
if mibBuilder.loadTexts:
    srcpPeerTimeSinceHeartbeat.setUnits("milliseconds")


class _SrcpPeerMaxPduSize_Type(Integer32):
    """Custom type srcpPeerMaxPduSize based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4095, 65535),
    )


_SrcpPeerMaxPduSize_Type.__name__ = "Integer32"
_SrcpPeerMaxPduSize_Object = MibTableColumn
srcpPeerMaxPduSize = _SrcpPeerMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 6),
    _SrcpPeerMaxPduSize_Type()
)
srcpPeerMaxPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpPeerMaxPduSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    srcpPeerMaxPduSize.setUnits("octets")
_SrcpPeerGrpParamTable_Object = MibTable
srcpPeerGrpParamTable = _SrcpPeerGrpParamTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    srcpPeerGrpParamTable.setStatus("current")
_SrcpPeerGrpParamEntry_Object = MibTableRow
srcpPeerGrpParamEntry = _SrcpPeerGrpParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1)
)
srcpPeerGrpParamEntry.setIndexNames(
    (0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"),
)
if mibBuilder.loadTexts:
    srcpPeerGrpParamEntry.setStatus("current")


class _SrcpPeerGrpHeartbeatInterval_Type(Integer32):
    """Custom type srcpPeerGrpHeartbeatInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SrcpPeerGrpHeartbeatInterval_Type.__name__ = "Integer32"
_SrcpPeerGrpHeartbeatInterval_Object = MibTableColumn
srcpPeerGrpHeartbeatInterval = _SrcpPeerGrpHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1, 1),
    _SrcpPeerGrpHeartbeatInterval_Type()
)
srcpPeerGrpHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpPeerGrpHeartbeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    srcpPeerGrpHeartbeatInterval.setUnits("milliseconds")


class _SrcpPeerGrpTimeSinceHeartbeat_Type(Integer32):
    """Custom type srcpPeerGrpTimeSinceHeartbeat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SrcpPeerGrpTimeSinceHeartbeat_Type.__name__ = "Integer32"
_SrcpPeerGrpTimeSinceHeartbeat_Object = MibTableColumn
srcpPeerGrpTimeSinceHeartbeat = _SrcpPeerGrpTimeSinceHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1, 2),
    _SrcpPeerGrpTimeSinceHeartbeat_Type()
)
srcpPeerGrpTimeSinceHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcpPeerGrpTimeSinceHeartbeat.setStatus("current")
if mibBuilder.loadTexts:
    srcpPeerGrpTimeSinceHeartbeat.setUnits("milliseconds")


class _SrcpPeerGrpMaxPduSize_Type(Integer32):
    """Custom type srcpPeerGrpMaxPduSize based on Integer32"""
    defaultValue = 16384

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4095, 65535),
    )


_SrcpPeerGrpMaxPduSize_Type.__name__ = "Integer32"
_SrcpPeerGrpMaxPduSize_Object = MibTableColumn
srcpPeerGrpMaxPduSize = _SrcpPeerGrpMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1, 3),
    _SrcpPeerGrpMaxPduSize_Type()
)
srcpPeerGrpMaxPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpPeerGrpMaxPduSize.setStatus("current")
if mibBuilder.loadTexts:
    srcpPeerGrpMaxPduSize.setUnits("octets")
_SrcpStatsObjects_ObjectIdentity = ObjectIdentity
srcpStatsObjects = _SrcpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2)
)
_SrcpPeerStatsTable_Object = MibTable
srcpPeerStatsTable = _SrcpPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    srcpPeerStatsTable.setStatus("current")
_SrcpPeerStatsEntry_Object = MibTableRow
srcpPeerStatsEntry = _SrcpPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1)
)
srcpPeerStatsEntry.setIndexNames(
    (0, "CISCO-WAN-SRCP-MIB", "srcpStatsPeerIpAddress"),
)
if mibBuilder.loadTexts:
    srcpPeerStatsEntry.setStatus("current")
_SrcpStatsPeerIpAddress_Type = IpAddress
_SrcpStatsPeerIpAddress_Object = MibTableColumn
srcpStatsPeerIpAddress = _SrcpStatsPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 1),
    _SrcpStatsPeerIpAddress_Type()
)
srcpStatsPeerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srcpStatsPeerIpAddress.setStatus("current")


class _SrcpStatsPeerName_Type(DisplayString):
    """Custom type srcpStatsPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SrcpStatsPeerName_Type.__name__ = "DisplayString"
_SrcpStatsPeerName_Object = MibTableColumn
srcpStatsPeerName = _SrcpStatsPeerName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 2),
    _SrcpStatsPeerName_Type()
)
srcpStatsPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcpStatsPeerName.setStatus("current")
_PacketsDiscardedCnts_Type = Counter32
_PacketsDiscardedCnts_Object = MibTableColumn
packetsDiscardedCnts = _PacketsDiscardedCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 3),
    _PacketsDiscardedCnts_Type()
)
packetsDiscardedCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsDiscardedCnts.setStatus("current")
_AugwCnts_Type = Counter32
_AugwCnts_Object = MibTableColumn
augwCnts = _AugwCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 4),
    _AugwCnts_Type()
)
augwCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    augwCnts.setStatus("current")
_AulnCnts_Type = Counter32
_AulnCnts_Object = MibTableColumn
aulnCnts = _AulnCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 5),
    _AulnCnts_Type()
)
aulnCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aulnCnts.setStatus("current")
_RqntCnts_Type = Counter32
_RqntCnts_Object = MibTableColumn
rqntCnts = _RqntCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 6),
    _RqntCnts_Type()
)
rqntCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rqntCnts.setStatus("current")
_NtfyCnts_Type = Counter32
_NtfyCnts_Object = MibTableColumn
ntfyCnts = _NtfyCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 7),
    _NtfyCnts_Type()
)
ntfyCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntfyCnts.setStatus("current")
_AugwFailCnts_Type = Counter32
_AugwFailCnts_Object = MibTableColumn
augwFailCnts = _AugwFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 8),
    _AugwFailCnts_Type()
)
augwFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    augwFailCnts.setStatus("current")
_AulnFailCnts_Type = Counter32
_AulnFailCnts_Object = MibTableColumn
aulnFailCnts = _AulnFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 9),
    _AulnFailCnts_Type()
)
aulnFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aulnFailCnts.setStatus("current")
_RqntFailCnts_Type = Counter32
_RqntFailCnts_Object = MibTableColumn
rqntFailCnts = _RqntFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 10),
    _RqntFailCnts_Type()
)
rqntFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rqntFailCnts.setStatus("current")
_NtfyFailCnts_Type = Counter32
_NtfyFailCnts_Object = MibTableColumn
ntfyFailCnts = _NtfyFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 11),
    _NtfyFailCnts_Type()
)
ntfyFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntfyFailCnts.setStatus("current")
_SrcpAdminRetyObjects_ObjectIdentity = ObjectIdentity
srcpAdminRetyObjects = _SrcpAdminRetyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3)
)


class _SrcpRequestTimeOut_Type(Integer32):
    """Custom type srcpRequestTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SrcpRequestTimeOut_Type.__name__ = "Integer32"
_SrcpRequestTimeOut_Object = MibScalar
srcpRequestTimeOut = _SrcpRequestTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3, 1),
    _SrcpRequestTimeOut_Type()
)
srcpRequestTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpRequestTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    srcpRequestTimeOut.setUnits("milliseconds")


class _SrcpRequestRetries_Type(Integer32):
    """Custom type srcpRequestRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SrcpRequestRetries_Type.__name__ = "Integer32"
_SrcpRequestRetries_Object = MibScalar
srcpRequestRetries = _SrcpRequestRetries_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3, 2),
    _SrcpRequestRetries_Type()
)
srcpRequestRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpRequestRetries.setStatus("current")


class _SrcpRequestMaxTimeout_Type(Integer32):
    """Custom type srcpRequestMaxTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SrcpRequestMaxTimeout_Type.__name__ = "Integer32"
_SrcpRequestMaxTimeout_Object = MibScalar
srcpRequestMaxTimeout = _SrcpRequestMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3, 3),
    _SrcpRequestMaxTimeout_Type()
)
srcpRequestMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcpRequestMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    srcpRequestMaxTimeout.setUnits("milliseconds")
_SrcpMIBConformance_ObjectIdentity = ObjectIdentity
srcpMIBConformance = _SrcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3)
)
_SrcpMIBCompliances_ObjectIdentity = ObjectIdentity
srcpMIBCompliances = _SrcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1)
)
_SrcpMIBGroups_ObjectIdentity = ObjectIdentity
srcpMIBGroups = _SrcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2)
)

# Managed Objects groups

srcpConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 1)
)
srcpConfigurationGroup.setObjects(
      *(("CISCO-WAN-SRCP-MIB", "srcpVersion"),
        ("CISCO-WAN-SRCP-MIB", "srcpPortNumber"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerName"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerPortNumber"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerHeartbeatInterval"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerTimeSinceHeartbeat"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerMaxPduSize"))
)
if mibBuilder.loadTexts:
    srcpConfigurationGroup.setStatus("deprecated")

srcpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 2)
)
srcpStatisticsGroup.setObjects(
      *(("CISCO-WAN-SRCP-MIB", "srcpStatsPeerName"),
        ("CISCO-WAN-SRCP-MIB", "packetsDiscardedCnts"),
        ("CISCO-WAN-SRCP-MIB", "augwCnts"),
        ("CISCO-WAN-SRCP-MIB", "aulnCnts"),
        ("CISCO-WAN-SRCP-MIB", "rqntCnts"),
        ("CISCO-WAN-SRCP-MIB", "ntfyCnts"),
        ("CISCO-WAN-SRCP-MIB", "augwFailCnts"),
        ("CISCO-WAN-SRCP-MIB", "aulnFailCnts"),
        ("CISCO-WAN-SRCP-MIB", "rqntFailCnts"),
        ("CISCO-WAN-SRCP-MIB", "ntfyFailCnts"))
)
if mibBuilder.loadTexts:
    srcpStatisticsGroup.setStatus("deprecated")

srcpConfigurationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 3)
)
srcpConfigurationGroup2.setObjects(
      *(("CISCO-WAN-SRCP-MIB", "srcpVersion"),
        ("CISCO-WAN-SRCP-MIB", "srcpPortNumber"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerName"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerPortNumber"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerHeartbeatInterval"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerTimeSinceHeartbeat"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerMaxPduSize"),
        ("CISCO-WAN-SRCP-MIB", "srcpRequestTimeOut"),
        ("CISCO-WAN-SRCP-MIB", "srcpRequestRetries"),
        ("CISCO-WAN-SRCP-MIB", "srcpRequestMaxTimeout"))
)
if mibBuilder.loadTexts:
    srcpConfigurationGroup2.setStatus("deprecated")

srcpStatisticsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 4)
)
srcpStatisticsGroup2.setObjects(
      *(("CISCO-WAN-SRCP-MIB", "srcpStatsPeerName"),
        ("CISCO-WAN-SRCP-MIB", "packetsDiscardedCnts"),
        ("CISCO-WAN-SRCP-MIB", "augwCnts"),
        ("CISCO-WAN-SRCP-MIB", "aulnCnts"),
        ("CISCO-WAN-SRCP-MIB", "rqntCnts"),
        ("CISCO-WAN-SRCP-MIB", "ntfyCnts"),
        ("CISCO-WAN-SRCP-MIB", "augwFailCnts"),
        ("CISCO-WAN-SRCP-MIB", "aulnFailCnts"),
        ("CISCO-WAN-SRCP-MIB", "rqntFailCnts"),
        ("CISCO-WAN-SRCP-MIB", "ntfyFailCnts"))
)
if mibBuilder.loadTexts:
    srcpStatisticsGroup2.setStatus("current")

srcpConfigurationGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 5)
)
srcpConfigurationGroup3.setObjects(
      *(("CISCO-WAN-SRCP-MIB", "srcpVersion"),
        ("CISCO-WAN-SRCP-MIB", "srcpPortNumber"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerName"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerPortNumber"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpHeartbeatInterval"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpTimeSinceHeartbeat"),
        ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpMaxPduSize"),
        ("CISCO-WAN-SRCP-MIB", "srcpRequestTimeOut"),
        ("CISCO-WAN-SRCP-MIB", "srcpRequestRetries"),
        ("CISCO-WAN-SRCP-MIB", "srcpRequestMaxTimeout"))
)
if mibBuilder.loadTexts:
    srcpConfigurationGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

srcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    srcpMIBCompliance.setStatus(
        "deprecated"
    )

srcpMIBComplaince2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1, 2)
)
if mibBuilder.loadTexts:
    srcpMIBComplaince2.setStatus(
        "deprecated"
    )

srcpMIBComplaince3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1, 3)
)
if mibBuilder.loadTexts:
    srcpMIBComplaince3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-SRCP-MIB",
    **{"ciscoWanSrcpMIB": ciscoWanSrcpMIB,
       "srcpObjects": srcpObjects,
       "srcpAdminObjects": srcpAdminObjects,
       "srcpVersion": srcpVersion,
       "srcpPortNumber": srcpPortNumber,
       "srcpPeerTable": srcpPeerTable,
       "srcpPeerEntry": srcpPeerEntry,
       "srcpPeerId": srcpPeerId,
       "srcpPeerName": srcpPeerName,
       "srcpPeerPortNumber": srcpPeerPortNumber,
       "srcpPeerHeartbeatInterval": srcpPeerHeartbeatInterval,
       "srcpPeerTimeSinceHeartbeat": srcpPeerTimeSinceHeartbeat,
       "srcpPeerMaxPduSize": srcpPeerMaxPduSize,
       "srcpPeerGrpParamTable": srcpPeerGrpParamTable,
       "srcpPeerGrpParamEntry": srcpPeerGrpParamEntry,
       "srcpPeerGrpHeartbeatInterval": srcpPeerGrpHeartbeatInterval,
       "srcpPeerGrpTimeSinceHeartbeat": srcpPeerGrpTimeSinceHeartbeat,
       "srcpPeerGrpMaxPduSize": srcpPeerGrpMaxPduSize,
       "srcpStatsObjects": srcpStatsObjects,
       "srcpPeerStatsTable": srcpPeerStatsTable,
       "srcpPeerStatsEntry": srcpPeerStatsEntry,
       "srcpStatsPeerIpAddress": srcpStatsPeerIpAddress,
       "srcpStatsPeerName": srcpStatsPeerName,
       "packetsDiscardedCnts": packetsDiscardedCnts,
       "augwCnts": augwCnts,
       "aulnCnts": aulnCnts,
       "rqntCnts": rqntCnts,
       "ntfyCnts": ntfyCnts,
       "augwFailCnts": augwFailCnts,
       "aulnFailCnts": aulnFailCnts,
       "rqntFailCnts": rqntFailCnts,
       "ntfyFailCnts": ntfyFailCnts,
       "srcpAdminRetyObjects": srcpAdminRetyObjects,
       "srcpRequestTimeOut": srcpRequestTimeOut,
       "srcpRequestRetries": srcpRequestRetries,
       "srcpRequestMaxTimeout": srcpRequestMaxTimeout,
       "srcpMIBConformance": srcpMIBConformance,
       "srcpMIBCompliances": srcpMIBCompliances,
       "srcpMIBCompliance": srcpMIBCompliance,
       "srcpMIBComplaince2": srcpMIBComplaince2,
       "srcpMIBComplaince3": srcpMIBComplaince3,
       "srcpMIBGroups": srcpMIBGroups,
       "srcpConfigurationGroup": srcpConfigurationGroup,
       "srcpStatisticsGroup": srcpStatisticsGroup,
       "srcpConfigurationGroup2": srcpConfigurationGroup2,
       "srcpStatisticsGroup2": srcpStatisticsGroup2,
       "srcpConfigurationGroup3": srcpConfigurationGroup3}
)
