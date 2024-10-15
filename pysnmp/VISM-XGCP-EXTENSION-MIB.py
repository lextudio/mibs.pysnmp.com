# SNMP MIB module (VISM-XGCP-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VISM-XGCP-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:42 2024
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

(voice,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "voice")

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

_VismXgcpExtensionGrp_ObjectIdentity = ObjectIdentity
vismXgcpExtensionGrp = _VismXgcpExtensionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5)
)
_VismXgcpCoreObjects_ObjectIdentity = ObjectIdentity
vismXgcpCoreObjects = _VismXgcpCoreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1)
)


class _VismXgcpRequestMaxTimeout_Type(Integer32):
    """Custom type vismXgcpRequestMaxTimeout based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VismXgcpRequestMaxTimeout_Type.__name__ = "Integer32"
_VismXgcpRequestMaxTimeout_Object = MibScalar
vismXgcpRequestMaxTimeout = _VismXgcpRequestMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 1),
    _VismXgcpRequestMaxTimeout_Type()
)
vismXgcpRequestMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRequestMaxTimeout.setStatus("mandatory")


class _VismXgcpPort_Type(Integer32):
    """Custom type vismXgcpPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_VismXgcpPort_Type.__name__ = "Integer32"
_VismXgcpPort_Object = MibScalar
vismXgcpPort = _VismXgcpPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 2),
    _VismXgcpPort_Type()
)
vismXgcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpPort.setStatus("mandatory")
_VismXgcpPeerTable_Object = MibTable
vismXgcpPeerTable = _VismXgcpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    vismXgcpPeerTable.setStatus("mandatory")
_VismXgcpPeerEntry_Object = MibTableRow
vismXgcpPeerEntry = _VismXgcpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1)
)
vismXgcpPeerEntry.setIndexNames(
    (0, "VISM-XGCP-EXTENSION-MIB", "vismXgcpPeerNumber"),
    (0, "VISM-XGCP-EXTENSION-MIB", "vismXgcpPeerProtocolNumber"),
)
if mibBuilder.loadTexts:
    vismXgcpPeerEntry.setStatus("mandatory")


class _VismXgcpPeerNumber_Type(Integer32):
    """Custom type vismXgcpPeerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VismXgcpPeerNumber_Type.__name__ = "Integer32"
_VismXgcpPeerNumber_Object = MibTableColumn
vismXgcpPeerNumber = _VismXgcpPeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 1),
    _VismXgcpPeerNumber_Type()
)
vismXgcpPeerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpPeerNumber.setStatus("mandatory")


class _VismXgcpPeerProtocolNumber_Type(Integer32):
    """Custom type vismXgcpPeerProtocolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VismXgcpPeerProtocolNumber_Type.__name__ = "Integer32"
_VismXgcpPeerProtocolNumber_Object = MibTableColumn
vismXgcpPeerProtocolNumber = _VismXgcpPeerProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 2),
    _VismXgcpPeerProtocolNumber_Type()
)
vismXgcpPeerProtocolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpPeerProtocolNumber.setStatus("mandatory")


class _VismXgcpPeerPort_Type(Integer32):
    """Custom type vismXgcpPeerPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_VismXgcpPeerPort_Type.__name__ = "Integer32"
_VismXgcpPeerPort_Object = MibTableColumn
vismXgcpPeerPort = _VismXgcpPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 3, 1, 3),
    _VismXgcpPeerPort_Type()
)
vismXgcpPeerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpPeerPort.setStatus("mandatory")
_VismXgcpMsgStatTable_Object = MibTable
vismXgcpMsgStatTable = _VismXgcpMsgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4)
)
if mibBuilder.loadTexts:
    vismXgcpMsgStatTable.setStatus("mandatory")
_VismXgcpMsgStatEntry_Object = MibTableRow
vismXgcpMsgStatEntry = _VismXgcpMsgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1)
)
vismXgcpMsgStatEntry.setIndexNames(
    (0, "VISM-XGCP-EXTENSION-MIB", "vismXgcpIpAddress"),
)
if mibBuilder.loadTexts:
    vismXgcpMsgStatEntry.setStatus("mandatory")
_VismXgcpIpAddress_Type = IpAddress
_VismXgcpIpAddress_Object = MibTableColumn
vismXgcpIpAddress = _VismXgcpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 1),
    _VismXgcpIpAddress_Type()
)
vismXgcpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpIpAddress.setStatus("mandatory")
_VismXgcpCrcxCnts_Type = Counter32
_VismXgcpCrcxCnts_Object = MibTableColumn
vismXgcpCrcxCnts = _VismXgcpCrcxCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 2),
    _VismXgcpCrcxCnts_Type()
)
vismXgcpCrcxCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpCrcxCnts.setStatus("mandatory")
_VismXgcpCrcxFailCnts_Type = Counter32
_VismXgcpCrcxFailCnts_Object = MibTableColumn
vismXgcpCrcxFailCnts = _VismXgcpCrcxFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 3),
    _VismXgcpCrcxFailCnts_Type()
)
vismXgcpCrcxFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpCrcxFailCnts.setStatus("mandatory")
_VismXgcpMdcxCnts_Type = Counter32
_VismXgcpMdcxCnts_Object = MibTableColumn
vismXgcpMdcxCnts = _VismXgcpMdcxCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 4),
    _VismXgcpMdcxCnts_Type()
)
vismXgcpMdcxCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpMdcxCnts.setStatus("mandatory")
_VismXgcpMdcxFailCnts_Type = Counter32
_VismXgcpMdcxFailCnts_Object = MibTableColumn
vismXgcpMdcxFailCnts = _VismXgcpMdcxFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 5),
    _VismXgcpMdcxFailCnts_Type()
)
vismXgcpMdcxFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpMdcxFailCnts.setStatus("mandatory")
_VismXgcpDlcxRcvCnts_Type = Counter32
_VismXgcpDlcxRcvCnts_Object = MibTableColumn
vismXgcpDlcxRcvCnts = _VismXgcpDlcxRcvCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 6),
    _VismXgcpDlcxRcvCnts_Type()
)
vismXgcpDlcxRcvCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxRcvCnts.setStatus("mandatory")
_VismXgcpDlcxRcvFailCnts_Type = Counter32
_VismXgcpDlcxRcvFailCnts_Object = MibTableColumn
vismXgcpDlcxRcvFailCnts = _VismXgcpDlcxRcvFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 7),
    _VismXgcpDlcxRcvFailCnts_Type()
)
vismXgcpDlcxRcvFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxRcvFailCnts.setStatus("mandatory")
_VismXgcpDlcxSentCnts_Type = Counter32
_VismXgcpDlcxSentCnts_Object = MibTableColumn
vismXgcpDlcxSentCnts = _VismXgcpDlcxSentCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 8),
    _VismXgcpDlcxSentCnts_Type()
)
vismXgcpDlcxSentCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxSentCnts.setStatus("mandatory")
_VismXgcpDlcxSentFailCnts_Type = Counter32
_VismXgcpDlcxSentFailCnts_Object = MibTableColumn
vismXgcpDlcxSentFailCnts = _VismXgcpDlcxSentFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 9),
    _VismXgcpDlcxSentFailCnts_Type()
)
vismXgcpDlcxSentFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpDlcxSentFailCnts.setStatus("mandatory")
_VismXgcpRqntCnts_Type = Counter32
_VismXgcpRqntCnts_Object = MibTableColumn
vismXgcpRqntCnts = _VismXgcpRqntCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 10),
    _VismXgcpRqntCnts_Type()
)
vismXgcpRqntCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRqntCnts.setStatus("mandatory")
_VismXgcpRqntFailCnts_Type = Counter32
_VismXgcpRqntFailCnts_Object = MibTableColumn
vismXgcpRqntFailCnts = _VismXgcpRqntFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 11),
    _VismXgcpRqntFailCnts_Type()
)
vismXgcpRqntFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRqntFailCnts.setStatus("mandatory")
_VismXgcpNtfyCnts_Type = Counter32
_VismXgcpNtfyCnts_Object = MibTableColumn
vismXgcpNtfyCnts = _VismXgcpNtfyCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 12),
    _VismXgcpNtfyCnts_Type()
)
vismXgcpNtfyCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpNtfyCnts.setStatus("mandatory")
_VismXgcpNtfyFailCnts_Type = Counter32
_VismXgcpNtfyFailCnts_Object = MibTableColumn
vismXgcpNtfyFailCnts = _VismXgcpNtfyFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 13),
    _VismXgcpNtfyFailCnts_Type()
)
vismXgcpNtfyFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpNtfyFailCnts.setStatus("mandatory")
_VismXgcpAuepCnts_Type = Counter32
_VismXgcpAuepCnts_Object = MibTableColumn
vismXgcpAuepCnts = _VismXgcpAuepCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 14),
    _VismXgcpAuepCnts_Type()
)
vismXgcpAuepCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAuepCnts.setStatus("mandatory")
_VismXgcpAuepFailCnts_Type = Counter32
_VismXgcpAuepFailCnts_Object = MibTableColumn
vismXgcpAuepFailCnts = _VismXgcpAuepFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 15),
    _VismXgcpAuepFailCnts_Type()
)
vismXgcpAuepFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAuepFailCnts.setStatus("mandatory")
_VismXgcpAucxCnts_Type = Counter32
_VismXgcpAucxCnts_Object = MibTableColumn
vismXgcpAucxCnts = _VismXgcpAucxCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 16),
    _VismXgcpAucxCnts_Type()
)
vismXgcpAucxCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAucxCnts.setStatus("mandatory")
_VismXgcpAucxFailCnts_Type = Counter32
_VismXgcpAucxFailCnts_Object = MibTableColumn
vismXgcpAucxFailCnts = _VismXgcpAucxFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 17),
    _VismXgcpAucxFailCnts_Type()
)
vismXgcpAucxFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpAucxFailCnts.setStatus("mandatory")
_VismXgcpRsipCnts_Type = Counter32
_VismXgcpRsipCnts_Object = MibTableColumn
vismXgcpRsipCnts = _VismXgcpRsipCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 18),
    _VismXgcpRsipCnts_Type()
)
vismXgcpRsipCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRsipCnts.setStatus("mandatory")
_VismXgcpRsipFailCnts_Type = Counter32
_VismXgcpRsipFailCnts_Object = MibTableColumn
vismXgcpRsipFailCnts = _VismXgcpRsipFailCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 1, 4, 1, 19),
    _VismXgcpRsipFailCnts_Type()
)
vismXgcpRsipFailCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismXgcpRsipFailCnts.setStatus("mandatory")
_VismXgcpEnhancementsObjects_ObjectIdentity = ObjectIdentity
vismXgcpEnhancementsObjects = _VismXgcpEnhancementsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2)
)


class _VismXgcpRestartInProgressTdinit_Type(Integer32):
    """Custom type vismXgcpRestartInProgressTdinit based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VismXgcpRestartInProgressTdinit_Type.__name__ = "Integer32"
_VismXgcpRestartInProgressTdinit_Object = MibScalar
vismXgcpRestartInProgressTdinit = _VismXgcpRestartInProgressTdinit_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 1),
    _VismXgcpRestartInProgressTdinit_Type()
)
vismXgcpRestartInProgressTdinit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRestartInProgressTdinit.setStatus("mandatory")


class _VismXgcpRestartInProgressTdmin_Type(Integer32):
    """Custom type vismXgcpRestartInProgressTdmin based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VismXgcpRestartInProgressTdmin_Type.__name__ = "Integer32"
_VismXgcpRestartInProgressTdmin_Object = MibScalar
vismXgcpRestartInProgressTdmin = _VismXgcpRestartInProgressTdmin_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 2),
    _VismXgcpRestartInProgressTdmin_Type()
)
vismXgcpRestartInProgressTdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRestartInProgressTdmin.setStatus("mandatory")


class _VismXgcpRestartInProgressTdmax_Type(Integer32):
    """Custom type vismXgcpRestartInProgressTdmax based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_VismXgcpRestartInProgressTdmax_Type.__name__ = "Integer32"
_VismXgcpRestartInProgressTdmax_Object = MibScalar
vismXgcpRestartInProgressTdmax = _VismXgcpRestartInProgressTdmax_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 5, 2, 3),
    _VismXgcpRestartInProgressTdmax_Type()
)
vismXgcpRestartInProgressTdmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismXgcpRestartInProgressTdmax.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VISM-XGCP-EXTENSION-MIB",
    **{"vismXgcpExtensionGrp": vismXgcpExtensionGrp,
       "vismXgcpCoreObjects": vismXgcpCoreObjects,
       "vismXgcpRequestMaxTimeout": vismXgcpRequestMaxTimeout,
       "vismXgcpPort": vismXgcpPort,
       "vismXgcpPeerTable": vismXgcpPeerTable,
       "vismXgcpPeerEntry": vismXgcpPeerEntry,
       "vismXgcpPeerNumber": vismXgcpPeerNumber,
       "vismXgcpPeerProtocolNumber": vismXgcpPeerProtocolNumber,
       "vismXgcpPeerPort": vismXgcpPeerPort,
       "vismXgcpMsgStatTable": vismXgcpMsgStatTable,
       "vismXgcpMsgStatEntry": vismXgcpMsgStatEntry,
       "vismXgcpIpAddress": vismXgcpIpAddress,
       "vismXgcpCrcxCnts": vismXgcpCrcxCnts,
       "vismXgcpCrcxFailCnts": vismXgcpCrcxFailCnts,
       "vismXgcpMdcxCnts": vismXgcpMdcxCnts,
       "vismXgcpMdcxFailCnts": vismXgcpMdcxFailCnts,
       "vismXgcpDlcxRcvCnts": vismXgcpDlcxRcvCnts,
       "vismXgcpDlcxRcvFailCnts": vismXgcpDlcxRcvFailCnts,
       "vismXgcpDlcxSentCnts": vismXgcpDlcxSentCnts,
       "vismXgcpDlcxSentFailCnts": vismXgcpDlcxSentFailCnts,
       "vismXgcpRqntCnts": vismXgcpRqntCnts,
       "vismXgcpRqntFailCnts": vismXgcpRqntFailCnts,
       "vismXgcpNtfyCnts": vismXgcpNtfyCnts,
       "vismXgcpNtfyFailCnts": vismXgcpNtfyFailCnts,
       "vismXgcpAuepCnts": vismXgcpAuepCnts,
       "vismXgcpAuepFailCnts": vismXgcpAuepFailCnts,
       "vismXgcpAucxCnts": vismXgcpAucxCnts,
       "vismXgcpAucxFailCnts": vismXgcpAucxFailCnts,
       "vismXgcpRsipCnts": vismXgcpRsipCnts,
       "vismXgcpRsipFailCnts": vismXgcpRsipFailCnts,
       "vismXgcpEnhancementsObjects": vismXgcpEnhancementsObjects,
       "vismXgcpRestartInProgressTdinit": vismXgcpRestartInProgressTdinit,
       "vismXgcpRestartInProgressTdmin": vismXgcpRestartInProgressTdmin,
       "vismXgcpRestartInProgressTdmax": vismXgcpRestartInProgressTdmax}
)
