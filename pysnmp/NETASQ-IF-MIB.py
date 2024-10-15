# SNMP MIB module (NETASQ-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETASQ-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:32 2024
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

(ntqif,) = mibBuilder.importSymbols(
    "NETASQ-SMI-MIB",
    "ntqif")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtqifTable_Object = MibTable
ntqifTable = _NtqifTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ntqifTable.setStatus("current")
_NtqifEntry_Object = MibTableRow
ntqifEntry = _NtqifEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1)
)
ntqifEntry.setIndexNames(
    (0, "NETASQ-IF-MIB", "ntqifIndex"),
)
if mibBuilder.loadTexts:
    ntqifEntry.setStatus("current")
_NtqifIndex_Type = Integer32
_NtqifIndex_Object = MibTableColumn
ntqifIndex = _NtqifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 1),
    _NtqifIndex_Type()
)
ntqifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifIndex.setStatus("current")
_NtqifUserName_Type = SnmpAdminString
_NtqifUserName_Object = MibTableColumn
ntqifUserName = _NtqifUserName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 2),
    _NtqifUserName_Type()
)
ntqifUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifUserName.setStatus("current")
_NtqifName_Type = DisplayString
_NtqifName_Object = MibTableColumn
ntqifName = _NtqifName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 3),
    _NtqifName_Type()
)
ntqifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifName.setStatus("current")
_NtqifAddr_Type = DisplayString
_NtqifAddr_Object = MibTableColumn
ntqifAddr = _NtqifAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 4),
    _NtqifAddr_Type()
)
ntqifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifAddr.setStatus("current")
_NtqifMask_Type = DisplayString
_NtqifMask_Object = MibTableColumn
ntqifMask = _NtqifMask_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 5),
    _NtqifMask_Type()
)
ntqifMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifMask.setStatus("current")
_NtqifType_Type = DisplayString
_NtqifType_Object = MibTableColumn
ntqifType = _NtqifType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 6),
    _NtqifType_Type()
)
ntqifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifType.setStatus("current")
_NtqifColor_Type = Integer32
_NtqifColor_Object = MibTableColumn
ntqifColor = _NtqifColor_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 7),
    _NtqifColor_Type()
)
ntqifColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifColor.setStatus("current")
_NtqifMacThroughput_Type = Integer32
_NtqifMacThroughput_Object = MibTableColumn
ntqifMacThroughput = _NtqifMacThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 8),
    _NtqifMacThroughput_Type()
)
ntqifMacThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifMacThroughput.setStatus("current")
_NtqifCurThroughput_Type = Integer32
_NtqifCurThroughput_Object = MibTableColumn
ntqifCurThroughput = _NtqifCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 9),
    _NtqifCurThroughput_Type()
)
ntqifCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifCurThroughput.setStatus("current")
_NtqifMaxThroughput_Type = Integer32
_NtqifMaxThroughput_Object = MibTableColumn
ntqifMaxThroughput = _NtqifMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 10),
    _NtqifMaxThroughput_Type()
)
ntqifMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifMaxThroughput.setStatus("current")
_NtqifPktAccepted_Type = Counter64
_NtqifPktAccepted_Object = MibTableColumn
ntqifPktAccepted = _NtqifPktAccepted_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 11),
    _NtqifPktAccepted_Type()
)
ntqifPktAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifPktAccepted.setStatus("current")
_NtqifPktBlocked_Type = Counter64
_NtqifPktBlocked_Object = MibTableColumn
ntqifPktBlocked = _NtqifPktBlocked_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 12),
    _NtqifPktBlocked_Type()
)
ntqifPktBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifPktBlocked.setStatus("current")
_NtqifPktFragmented_Type = Counter64
_NtqifPktFragmented_Object = MibTableColumn
ntqifPktFragmented = _NtqifPktFragmented_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 13),
    _NtqifPktFragmented_Type()
)
ntqifPktFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifPktFragmented.setStatus("current")
_NtqifPktTcp_Type = Counter64
_NtqifPktTcp_Object = MibTableColumn
ntqifPktTcp = _NtqifPktTcp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 14),
    _NtqifPktTcp_Type()
)
ntqifPktTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifPktTcp.setStatus("current")
_NtqifPktUdp_Type = Counter64
_NtqifPktUdp_Object = MibTableColumn
ntqifPktUdp = _NtqifPktUdp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 15),
    _NtqifPktUdp_Type()
)
ntqifPktUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifPktUdp.setStatus("current")
_NtqifPktIcmp_Type = Counter64
_NtqifPktIcmp_Object = MibTableColumn
ntqifPktIcmp = _NtqifPktIcmp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 16),
    _NtqifPktIcmp_Type()
)
ntqifPktIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifPktIcmp.setStatus("current")
_NtqifTotalBytes_Type = Counter64
_NtqifTotalBytes_Object = MibTableColumn
ntqifTotalBytes = _NtqifTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 17),
    _NtqifTotalBytes_Type()
)
ntqifTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifTotalBytes.setStatus("current")
_NtqifTcpBytes_Type = Counter64
_NtqifTcpBytes_Object = MibTableColumn
ntqifTcpBytes = _NtqifTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 18),
    _NtqifTcpBytes_Type()
)
ntqifTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifTcpBytes.setStatus("current")
_NtqifUdpBytes_Type = Counter64
_NtqifUdpBytes_Object = MibTableColumn
ntqifUdpBytes = _NtqifUdpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 19),
    _NtqifUdpBytes_Type()
)
ntqifUdpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifUdpBytes.setStatus("current")
_NtqifIcmpBytes_Type = Counter64
_NtqifIcmpBytes_Object = MibTableColumn
ntqifIcmpBytes = _NtqifIcmpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 20),
    _NtqifIcmpBytes_Type()
)
ntqifIcmpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifIcmpBytes.setStatus("current")
_NtqifTcpConn_Type = Counter64
_NtqifTcpConn_Object = MibTableColumn
ntqifTcpConn = _NtqifTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 21),
    _NtqifTcpConn_Type()
)
ntqifTcpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifTcpConn.setStatus("current")
_NtqifUdpConn_Type = Counter64
_NtqifUdpConn_Object = MibTableColumn
ntqifUdpConn = _NtqifUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 22),
    _NtqifUdpConn_Type()
)
ntqifUdpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifUdpConn.setStatus("current")
_NtqifTcpConnCount_Type = Integer32
_NtqifTcpConnCount_Object = MibTableColumn
ntqifTcpConnCount = _NtqifTcpConnCount_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 23),
    _NtqifTcpConnCount_Type()
)
ntqifTcpConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifTcpConnCount.setStatus("current")
_NtqifUdpConnCount_Type = Integer32
_NtqifUdpConnCount_Object = MibTableColumn
ntqifUdpConnCount = _NtqifUdpConnCount_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 24),
    _NtqifUdpConnCount_Type()
)
ntqifUdpConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifUdpConnCount.setStatus("current")
_NtqifInCurThroughput_Type = Integer32
_NtqifInCurThroughput_Object = MibTableColumn
ntqifInCurThroughput = _NtqifInCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 25),
    _NtqifInCurThroughput_Type()
)
ntqifInCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifInCurThroughput.setStatus("current")
_NtqifOutCurThroughput_Type = Integer32
_NtqifOutCurThroughput_Object = MibTableColumn
ntqifOutCurThroughput = _NtqifOutCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 26),
    _NtqifOutCurThroughput_Type()
)
ntqifOutCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifOutCurThroughput.setStatus("current")
_NtqifInMaxThroughput_Type = Integer32
_NtqifInMaxThroughput_Object = MibTableColumn
ntqifInMaxThroughput = _NtqifInMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 27),
    _NtqifInMaxThroughput_Type()
)
ntqifInMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifInMaxThroughput.setStatus("current")
_NtqifOutMaxThroughput_Type = Integer32
_NtqifOutMaxThroughput_Object = MibTableColumn
ntqifOutMaxThroughput = _NtqifOutMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 28),
    _NtqifOutMaxThroughput_Type()
)
ntqifOutMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifOutMaxThroughput.setStatus("current")
_NtqifInTotalBytes_Type = Counter64
_NtqifInTotalBytes_Object = MibTableColumn
ntqifInTotalBytes = _NtqifInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 29),
    _NtqifInTotalBytes_Type()
)
ntqifInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifInTotalBytes.setStatus("current")
_NtqifOutTotalBytes_Type = Counter64
_NtqifOutTotalBytes_Object = MibTableColumn
ntqifOutTotalBytes = _NtqifOutTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 30),
    _NtqifOutTotalBytes_Type()
)
ntqifOutTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifOutTotalBytes.setStatus("current")
_NtqifInTcpBytes_Type = Counter64
_NtqifInTcpBytes_Object = MibTableColumn
ntqifInTcpBytes = _NtqifInTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 31),
    _NtqifInTcpBytes_Type()
)
ntqifInTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifInTcpBytes.setStatus("current")
_NtqifOutTcpBytes_Type = Counter64
_NtqifOutTcpBytes_Object = MibTableColumn
ntqifOutTcpBytes = _NtqifOutTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 32),
    _NtqifOutTcpBytes_Type()
)
ntqifOutTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifOutTcpBytes.setStatus("current")
_NtqifInUdpBytes_Type = Counter64
_NtqifInUdpBytes_Object = MibTableColumn
ntqifInUdpBytes = _NtqifInUdpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 33),
    _NtqifInUdpBytes_Type()
)
ntqifInUdpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifInUdpBytes.setStatus("current")
_NtqifOutUdpBytes_Type = Counter64
_NtqifOutUdpBytes_Object = MibTableColumn
ntqifOutUdpBytes = _NtqifOutUdpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 34),
    _NtqifOutUdpBytes_Type()
)
ntqifOutUdpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifOutUdpBytes.setStatus("current")
_NtqifInIcmpBytes_Type = Counter64
_NtqifInIcmpBytes_Object = MibTableColumn
ntqifInIcmpBytes = _NtqifInIcmpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 35),
    _NtqifInIcmpBytes_Type()
)
ntqifInIcmpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifInIcmpBytes.setStatus("current")
_NtqifIOutIcmpBytes_Type = Counter64
_NtqifIOutIcmpBytes_Object = MibScalar
ntqifIOutIcmpBytes = _NtqifIOutIcmpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 36),
    _NtqifIOutIcmpBytes_Type()
)
ntqifIOutIcmpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntqifIOutIcmpBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETASQ-IF-MIB",
    **{"ntqifTable": ntqifTable,
       "ntqifEntry": ntqifEntry,
       "ntqifIndex": ntqifIndex,
       "ntqifUserName": ntqifUserName,
       "ntqifName": ntqifName,
       "ntqifAddr": ntqifAddr,
       "ntqifMask": ntqifMask,
       "ntqifType": ntqifType,
       "ntqifColor": ntqifColor,
       "ntqifMacThroughput": ntqifMacThroughput,
       "ntqifCurThroughput": ntqifCurThroughput,
       "ntqifMaxThroughput": ntqifMaxThroughput,
       "ntqifPktAccepted": ntqifPktAccepted,
       "ntqifPktBlocked": ntqifPktBlocked,
       "ntqifPktFragmented": ntqifPktFragmented,
       "ntqifPktTcp": ntqifPktTcp,
       "ntqifPktUdp": ntqifPktUdp,
       "ntqifPktIcmp": ntqifPktIcmp,
       "ntqifTotalBytes": ntqifTotalBytes,
       "ntqifTcpBytes": ntqifTcpBytes,
       "ntqifUdpBytes": ntqifUdpBytes,
       "ntqifIcmpBytes": ntqifIcmpBytes,
       "ntqifTcpConn": ntqifTcpConn,
       "ntqifUdpConn": ntqifUdpConn,
       "ntqifTcpConnCount": ntqifTcpConnCount,
       "ntqifUdpConnCount": ntqifUdpConnCount,
       "ntqifInCurThroughput": ntqifInCurThroughput,
       "ntqifOutCurThroughput": ntqifOutCurThroughput,
       "ntqifInMaxThroughput": ntqifInMaxThroughput,
       "ntqifOutMaxThroughput": ntqifOutMaxThroughput,
       "ntqifInTotalBytes": ntqifInTotalBytes,
       "ntqifOutTotalBytes": ntqifOutTotalBytes,
       "ntqifInTcpBytes": ntqifInTcpBytes,
       "ntqifOutTcpBytes": ntqifOutTcpBytes,
       "ntqifInUdpBytes": ntqifInUdpBytes,
       "ntqifOutUdpBytes": ntqifOutUdpBytes,
       "ntqifInIcmpBytes": ntqifInIcmpBytes,
       "ntqifIOutIcmpBytes": ntqifIOutIcmpBytes}
)
