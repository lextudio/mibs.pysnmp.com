# SNMP MIB module (REDLINE-AN50-PMP-V1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-AN50-PMP-V1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:26 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Redline_ObjectIdentity = ObjectIdentity
redline = _Redline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728)
)
_RedlineProducts_ObjectIdentity = ObjectIdentity
redlineProducts = _RedlineProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 1)
)
_RedlineAN50_ObjectIdentity = ObjectIdentity
redlineAN50 = _RedlineAN50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 1, 1)
)
_RedlineMgmt_ObjectIdentity = ObjectIdentity
redlineMgmt = _RedlineMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2)
)
_RedlineAN50PMPV1_ObjectIdentity = ObjectIdentity
redlineAN50PMPV1 = _RedlineAN50PMPV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51)
)
_An50pmpLinkTable_Object = MibTable
an50pmpLinkTable = _An50pmpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1)
)
if mibBuilder.loadTexts:
    an50pmpLinkTable.setStatus("mandatory")
_An50pmpLinkEntry_Object = MibTableRow
an50pmpLinkEntry = _An50pmpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1)
)
an50pmpLinkEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V1-MIB", "an50pmpLinkID"),
)
if mibBuilder.loadTexts:
    an50pmpLinkEntry.setStatus("mandatory")


class _An50pmpLinkID_Type(Integer32):
    """Custom type an50pmpLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_An50pmpLinkID_Type.__name__ = "Integer32"
_An50pmpLinkID_Object = MibTableColumn
an50pmpLinkID = _An50pmpLinkID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 1),
    _An50pmpLinkID_Type()
)
an50pmpLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkID.setStatus("mandatory")


class _An50pmpLinkName_Type(OctetString):
    """Custom type an50pmpLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_An50pmpLinkName_Type.__name__ = "OctetString"
_An50pmpLinkName_Object = MibTableColumn
an50pmpLinkName = _An50pmpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 2),
    _An50pmpLinkName_Type()
)
an50pmpLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkName.setStatus("mandatory")


class _An50pmpLinkGroupID_Type(Integer32):
    """Custom type an50pmpLinkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_An50pmpLinkGroupID_Type.__name__ = "Integer32"
_An50pmpLinkGroupID_Object = MibTableColumn
an50pmpLinkGroupID = _An50pmpLinkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 3),
    _An50pmpLinkGroupID_Type()
)
an50pmpLinkGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkGroupID.setStatus("mandatory")
_An50pmpLinkPeerMac_Type = OctetString
_An50pmpLinkPeerMac_Object = MibTableColumn
an50pmpLinkPeerMac = _An50pmpLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 4),
    _An50pmpLinkPeerMac_Type()
)
an50pmpLinkPeerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkPeerMac.setStatus("mandatory")


class _An50pmpLinkMaxDLBurstRate_Type(Integer32):
    """Custom type an50pmpLinkMaxDLBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_An50pmpLinkMaxDLBurstRate_Type.__name__ = "Integer32"
_An50pmpLinkMaxDLBurstRate_Object = MibTableColumn
an50pmpLinkMaxDLBurstRate = _An50pmpLinkMaxDLBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 5),
    _An50pmpLinkMaxDLBurstRate_Type()
)
an50pmpLinkMaxDLBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkMaxDLBurstRate.setStatus("mandatory")


class _An50pmpLinkMaxULBurstRate_Type(Integer32):
    """Custom type an50pmpLinkMaxULBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_An50pmpLinkMaxULBurstRate_Type.__name__ = "Integer32"
_An50pmpLinkMaxULBurstRate_Object = MibTableColumn
an50pmpLinkMaxULBurstRate = _An50pmpLinkMaxULBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 6),
    _An50pmpLinkMaxULBurstRate_Type()
)
an50pmpLinkMaxULBurstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkMaxULBurstRate.setStatus("mandatory")
_An50pmpLinkMaxHost_Type = Integer32
_An50pmpLinkMaxHost_Object = MibTableColumn
an50pmpLinkMaxHost = _An50pmpLinkMaxHost_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 7),
    _An50pmpLinkMaxHost_Type()
)
an50pmpLinkMaxHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkMaxHost.setStatus("mandatory")


class _An50pmpLinkCIDDLCIR_Type(Integer32):
    """Custom type an50pmpLinkCIDDLCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_An50pmpLinkCIDDLCIR_Type.__name__ = "Integer32"
_An50pmpLinkCIDDLCIR_Object = MibTableColumn
an50pmpLinkCIDDLCIR = _An50pmpLinkCIDDLCIR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 8),
    _An50pmpLinkCIDDLCIR_Type()
)
an50pmpLinkCIDDLCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkCIDDLCIR.setStatus("mandatory")


class _An50pmpLinkCIDDLPIR_Type(Integer32):
    """Custom type an50pmpLinkCIDDLPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_An50pmpLinkCIDDLPIR_Type.__name__ = "Integer32"
_An50pmpLinkCIDDLPIR_Object = MibTableColumn
an50pmpLinkCIDDLPIR = _An50pmpLinkCIDDLPIR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 9),
    _An50pmpLinkCIDDLPIR_Type()
)
an50pmpLinkCIDDLPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkCIDDLPIR.setStatus("mandatory")


class _An50pmpLinkCIDULCIR_Type(Integer32):
    """Custom type an50pmpLinkCIDULCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_An50pmpLinkCIDULCIR_Type.__name__ = "Integer32"
_An50pmpLinkCIDULCIR_Object = MibTableColumn
an50pmpLinkCIDULCIR = _An50pmpLinkCIDULCIR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 10),
    _An50pmpLinkCIDULCIR_Type()
)
an50pmpLinkCIDULCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkCIDULCIR.setStatus("mandatory")


class _An50pmpLinkCIDULPIR_Type(Integer32):
    """Custom type an50pmpLinkCIDULPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_An50pmpLinkCIDULPIR_Type.__name__ = "Integer32"
_An50pmpLinkCIDULPIR_Object = MibTableColumn
an50pmpLinkCIDULPIR = _An50pmpLinkCIDULPIR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 11),
    _An50pmpLinkCIDULPIR_Type()
)
an50pmpLinkCIDULPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkCIDULPIR.setStatus("mandatory")


class _An50pmpLinkDLQoS_Type(Integer32):
    """Custom type an50pmpLinkDLQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_An50pmpLinkDLQoS_Type.__name__ = "Integer32"
_An50pmpLinkDLQoS_Object = MibTableColumn
an50pmpLinkDLQoS = _An50pmpLinkDLQoS_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 12),
    _An50pmpLinkDLQoS_Type()
)
an50pmpLinkDLQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkDLQoS.setStatus("mandatory")


class _An50pmpLinkULQoS_Type(Integer32):
    """Custom type an50pmpLinkULQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_An50pmpLinkULQoS_Type.__name__ = "Integer32"
_An50pmpLinkULQoS_Object = MibTableColumn
an50pmpLinkULQoS = _An50pmpLinkULQoS_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 13),
    _An50pmpLinkULQoS_Type()
)
an50pmpLinkULQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkULQoS.setStatus("mandatory")
_An50pmpLinkRowStatus_Type = RowStatus
_An50pmpLinkRowStatus_Object = MibTableColumn
an50pmpLinkRowStatus = _An50pmpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 14),
    _An50pmpLinkRowStatus_Type()
)
an50pmpLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkRowStatus.setStatus("mandatory")
_An50pmpLinkStatusTable_Object = MibTable
an50pmpLinkStatusTable = _An50pmpLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2)
)
if mibBuilder.loadTexts:
    an50pmpLinkStatusTable.setStatus("mandatory")
_An50pmpLinkStatusEntry_Object = MibTableRow
an50pmpLinkStatusEntry = _An50pmpLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1)
)
an50pmpLinkStatusEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V1-MIB", "an50pmpLinkID"),
)
if mibBuilder.loadTexts:
    an50pmpLinkStatusEntry.setStatus("mandatory")


class _An50pmpLinkStatusID_Type(Integer32):
    """Custom type an50pmpLinkStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_An50pmpLinkStatusID_Type.__name__ = "Integer32"
_An50pmpLinkStatusID_Object = MibTableColumn
an50pmpLinkStatusID = _An50pmpLinkStatusID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 1),
    _An50pmpLinkStatusID_Type()
)
an50pmpLinkStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkStatusID.setStatus("mandatory")


class _An50pmpLinkStatus_Type(Integer32):
    """Custom type an50pmpLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_An50pmpLinkStatus_Type.__name__ = "Integer32"
_An50pmpLinkStatus_Object = MibTableColumn
an50pmpLinkStatus = _An50pmpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 2),
    _An50pmpLinkStatus_Type()
)
an50pmpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkStatus.setStatus("mandatory")
_An50pmpLinkStatusCode_Type = Integer32
_An50pmpLinkStatusCode_Object = MibTableColumn
an50pmpLinkStatusCode = _An50pmpLinkStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 3),
    _An50pmpLinkStatusCode_Type()
)
an50pmpLinkStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkStatusCode.setStatus("mandatory")


class _An50pmpLinkRegConn_Type(Integer32):
    """Custom type an50pmpLinkRegConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_An50pmpLinkRegConn_Type.__name__ = "Integer32"
_An50pmpLinkRegConn_Object = MibTableColumn
an50pmpLinkRegConn = _An50pmpLinkRegConn_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 4),
    _An50pmpLinkRegConn_Type()
)
an50pmpLinkRegConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkRegConn.setStatus("mandatory")


class _An50pmpLinkDLBurstRate_Type(Integer32):
    """Custom type an50pmpLinkDLBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_An50pmpLinkDLBurstRate_Type.__name__ = "Integer32"
_An50pmpLinkDLBurstRate_Object = MibTableColumn
an50pmpLinkDLBurstRate = _An50pmpLinkDLBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 5),
    _An50pmpLinkDLBurstRate_Type()
)
an50pmpLinkDLBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLBurstRate.setStatus("mandatory")
_An50pmpLinkDLRSSI_Type = Integer32
_An50pmpLinkDLRSSI_Object = MibTableColumn
an50pmpLinkDLRSSI = _An50pmpLinkDLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 6),
    _An50pmpLinkDLRSSI_Type()
)
an50pmpLinkDLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLRSSI.setStatus("mandatory")
_An50pmpLinkDLSINADR_Type = Integer32
_An50pmpLinkDLSINADR_Object = MibTableColumn
an50pmpLinkDLSINADR = _An50pmpLinkDLSINADR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 7),
    _An50pmpLinkDLSINADR_Type()
)
an50pmpLinkDLSINADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLSINADR.setStatus("mandatory")
_An50pmpLinkDLStatLostFrm_Type = Integer32
_An50pmpLinkDLStatLostFrm_Object = MibTableColumn
an50pmpLinkDLStatLostFrm = _An50pmpLinkDLStatLostFrm_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 8),
    _An50pmpLinkDLStatLostFrm_Type()
)
an50pmpLinkDLStatLostFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatLostFrm.setStatus("mandatory")
_An50pmpLinkDLStatBlksTot_Type = Integer32
_An50pmpLinkDLStatBlksTot_Object = MibTableColumn
an50pmpLinkDLStatBlksTot = _An50pmpLinkDLStatBlksTot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 9),
    _An50pmpLinkDLStatBlksTot_Type()
)
an50pmpLinkDLStatBlksTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatBlksTot.setStatus("mandatory")
_An50pmpLinkDLStatBlksRetr_Type = Integer32
_An50pmpLinkDLStatBlksRetr_Object = MibTableColumn
an50pmpLinkDLStatBlksRetr = _An50pmpLinkDLStatBlksRetr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 10),
    _An50pmpLinkDLStatBlksRetr_Type()
)
an50pmpLinkDLStatBlksRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatBlksRetr.setStatus("mandatory")
_An50pmpLinkDLStatBlksDisc_Type = Integer32
_An50pmpLinkDLStatBlksDisc_Object = MibTableColumn
an50pmpLinkDLStatBlksDisc = _An50pmpLinkDLStatBlksDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 11),
    _An50pmpLinkDLStatBlksDisc_Type()
)
an50pmpLinkDLStatBlksDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatBlksDisc.setStatus("mandatory")
_An50pmpLinkDLCIDStatPktDisc_Type = Integer32
_An50pmpLinkDLCIDStatPktDisc_Object = MibTableColumn
an50pmpLinkDLCIDStatPktDisc = _An50pmpLinkDLCIDStatPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 12),
    _An50pmpLinkDLCIDStatPktDisc_Type()
)
an50pmpLinkDLCIDStatPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLCIDStatPktDisc.setStatus("mandatory")
_An50pmpLinkDLCIDStatPktTran_Type = Integer32
_An50pmpLinkDLCIDStatPktTran_Object = MibTableColumn
an50pmpLinkDLCIDStatPktTran = _An50pmpLinkDLCIDStatPktTran_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 13),
    _An50pmpLinkDLCIDStatPktTran_Type()
)
an50pmpLinkDLCIDStatPktTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLCIDStatPktTran.setStatus("mandatory")
_An50pmpLinkDLCIDStatPktRecv_Type = Integer32
_An50pmpLinkDLCIDStatPktRecv_Object = MibTableColumn
an50pmpLinkDLCIDStatPktRecv = _An50pmpLinkDLCIDStatPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 14),
    _An50pmpLinkDLCIDStatPktRecv_Type()
)
an50pmpLinkDLCIDStatPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLCIDStatPktRecv.setStatus("mandatory")


class _An50pmpLinkULBurstRate_Type(Integer32):
    """Custom type an50pmpLinkULBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_An50pmpLinkULBurstRate_Type.__name__ = "Integer32"
_An50pmpLinkULBurstRate_Object = MibTableColumn
an50pmpLinkULBurstRate = _An50pmpLinkULBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 15),
    _An50pmpLinkULBurstRate_Type()
)
an50pmpLinkULBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULBurstRate.setStatus("mandatory")
_An50pmpLinkULRSSI_Type = Integer32
_An50pmpLinkULRSSI_Object = MibTableColumn
an50pmpLinkULRSSI = _An50pmpLinkULRSSI_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 16),
    _An50pmpLinkULRSSI_Type()
)
an50pmpLinkULRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULRSSI.setStatus("mandatory")
_An50pmpLinkULSINADR_Type = Integer32
_An50pmpLinkULSINADR_Object = MibTableColumn
an50pmpLinkULSINADR = _An50pmpLinkULSINADR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 17),
    _An50pmpLinkULSINADR_Type()
)
an50pmpLinkULSINADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULSINADR.setStatus("mandatory")
_An50pmpLinkULStatLostFrm_Type = Integer32
_An50pmpLinkULStatLostFrm_Object = MibTableColumn
an50pmpLinkULStatLostFrm = _An50pmpLinkULStatLostFrm_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 18),
    _An50pmpLinkULStatLostFrm_Type()
)
an50pmpLinkULStatLostFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatLostFrm.setStatus("mandatory")
_An50pmpLinkULStatBlksTot_Type = Integer32
_An50pmpLinkULStatBlksTot_Object = MibTableColumn
an50pmpLinkULStatBlksTot = _An50pmpLinkULStatBlksTot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 19),
    _An50pmpLinkULStatBlksTot_Type()
)
an50pmpLinkULStatBlksTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatBlksTot.setStatus("mandatory")
_An50pmpLinkULStatBlksRetr_Type = Integer32
_An50pmpLinkULStatBlksRetr_Object = MibTableColumn
an50pmpLinkULStatBlksRetr = _An50pmpLinkULStatBlksRetr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 20),
    _An50pmpLinkULStatBlksRetr_Type()
)
an50pmpLinkULStatBlksRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatBlksRetr.setStatus("mandatory")
_An50pmpLinkULStatBlksDisc_Type = Integer32
_An50pmpLinkULStatBlksDisc_Object = MibTableColumn
an50pmpLinkULStatBlksDisc = _An50pmpLinkULStatBlksDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 21),
    _An50pmpLinkULStatBlksDisc_Type()
)
an50pmpLinkULStatBlksDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatBlksDisc.setStatus("mandatory")
_An50pmpLinkULCIDStatPktDisc_Type = Integer32
_An50pmpLinkULCIDStatPktDisc_Object = MibTableColumn
an50pmpLinkULCIDStatPktDisc = _An50pmpLinkULCIDStatPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 22),
    _An50pmpLinkULCIDStatPktDisc_Type()
)
an50pmpLinkULCIDStatPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULCIDStatPktDisc.setStatus("mandatory")
_An50pmpLinkULCIDStatPktTran_Type = Integer32
_An50pmpLinkULCIDStatPktTran_Object = MibTableColumn
an50pmpLinkULCIDStatPktTran = _An50pmpLinkULCIDStatPktTran_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 23),
    _An50pmpLinkULCIDStatPktTran_Type()
)
an50pmpLinkULCIDStatPktTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULCIDStatPktTran.setStatus("mandatory")
_An50pmpLinkULCIDStatPktRecv_Type = Integer32
_An50pmpLinkULCIDStatPktRecv_Object = MibTableColumn
an50pmpLinkULCIDStatPktRecv = _An50pmpLinkULCIDStatPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 24),
    _An50pmpLinkULCIDStatPktRecv_Type()
)
an50pmpLinkULCIDStatPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULCIDStatPktRecv.setStatus("mandatory")
_An50pmpLinkUpTime_Type = TimeTicks
_An50pmpLinkUpTime_Object = MibTableColumn
an50pmpLinkUpTime = _An50pmpLinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 25),
    _An50pmpLinkUpTime_Type()
)
an50pmpLinkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkUpTime.setStatus("mandatory")
_An50pmpLinkLostCount_Type = Integer32
_An50pmpLinkLostCount_Object = MibTableColumn
an50pmpLinkLostCount = _An50pmpLinkLostCount_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 26),
    _An50pmpLinkLostCount_Type()
)
an50pmpLinkLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkLostCount.setStatus("mandatory")


class _An50pmpCIDSaveConfig_Type(Integer32):
    """Custom type an50pmpCIDSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 1),
          ("saveConfig", 2))
    )


_An50pmpCIDSaveConfig_Type.__name__ = "Integer32"
_An50pmpCIDSaveConfig_Object = MibScalar
an50pmpCIDSaveConfig = _An50pmpCIDSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 3),
    _An50pmpCIDSaveConfig_Type()
)
an50pmpCIDSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpCIDSaveConfig.setStatus("mandatory")


class _An50pmpLastModifiedCID_Type(Integer32):
    """Custom type an50pmpLastModifiedCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An50pmpLastModifiedCID_Type.__name__ = "Integer32"
_An50pmpLastModifiedCID_Object = MibScalar
an50pmpLastModifiedCID = _An50pmpLastModifiedCID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 4),
    _An50pmpLastModifiedCID_Type()
)
an50pmpLastModifiedCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLastModifiedCID.setStatus("mandatory")
_An50pmpLastMissedSsMacAddress_Type = OctetString
_An50pmpLastMissedSsMacAddress_Object = MibScalar
an50pmpLastMissedSsMacAddress = _An50pmpLastMissedSsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 5),
    _An50pmpLastMissedSsMacAddress_Type()
)
an50pmpLastMissedSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLastMissedSsMacAddress.setStatus("mandatory")
_An50pmpLastRegisteredSsMacAddress_Type = OctetString
_An50pmpLastRegisteredSsMacAddress_Object = MibScalar
an50pmpLastRegisteredSsMacAddress = _An50pmpLastRegisteredSsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 6),
    _An50pmpLastRegisteredSsMacAddress_Type()
)
an50pmpLastRegisteredSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLastRegisteredSsMacAddress.setStatus("mandatory")


class _An50pmpLastSuccessfulID_Type(Integer32):
    """Custom type an50pmpLastSuccessfulID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1023),
    )


_An50pmpLastSuccessfulID_Type.__name__ = "Integer32"
_An50pmpLastSuccessfulID_Object = MibScalar
an50pmpLastSuccessfulID = _An50pmpLastSuccessfulID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 7),
    _An50pmpLastSuccessfulID_Type()
)
an50pmpLastSuccessfulID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLastSuccessfulID.setStatus("mandatory")
_An50pmpLastDeniedSsMacAddress_Type = OctetString
_An50pmpLastDeniedSsMacAddress_Object = MibScalar
an50pmpLastDeniedSsMacAddress = _An50pmpLastDeniedSsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 8),
    _An50pmpLastDeniedSsMacAddress_Type()
)
an50pmpLastDeniedSsMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLastDeniedSsMacAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-AN50-PMP-V1-MIB",
    **{"redline": redline,
       "redlineProducts": redlineProducts,
       "redlineAN50": redlineAN50,
       "redlineMgmt": redlineMgmt,
       "redlineAN50PMPV1": redlineAN50PMPV1,
       "an50pmpLinkTable": an50pmpLinkTable,
       "an50pmpLinkEntry": an50pmpLinkEntry,
       "an50pmpLinkID": an50pmpLinkID,
       "an50pmpLinkName": an50pmpLinkName,
       "an50pmpLinkGroupID": an50pmpLinkGroupID,
       "an50pmpLinkPeerMac": an50pmpLinkPeerMac,
       "an50pmpLinkMaxDLBurstRate": an50pmpLinkMaxDLBurstRate,
       "an50pmpLinkMaxULBurstRate": an50pmpLinkMaxULBurstRate,
       "an50pmpLinkMaxHost": an50pmpLinkMaxHost,
       "an50pmpLinkCIDDLCIR": an50pmpLinkCIDDLCIR,
       "an50pmpLinkCIDDLPIR": an50pmpLinkCIDDLPIR,
       "an50pmpLinkCIDULCIR": an50pmpLinkCIDULCIR,
       "an50pmpLinkCIDULPIR": an50pmpLinkCIDULPIR,
       "an50pmpLinkDLQoS": an50pmpLinkDLQoS,
       "an50pmpLinkULQoS": an50pmpLinkULQoS,
       "an50pmpLinkRowStatus": an50pmpLinkRowStatus,
       "an50pmpLinkStatusTable": an50pmpLinkStatusTable,
       "an50pmpLinkStatusEntry": an50pmpLinkStatusEntry,
       "an50pmpLinkStatusID": an50pmpLinkStatusID,
       "an50pmpLinkStatus": an50pmpLinkStatus,
       "an50pmpLinkStatusCode": an50pmpLinkStatusCode,
       "an50pmpLinkRegConn": an50pmpLinkRegConn,
       "an50pmpLinkDLBurstRate": an50pmpLinkDLBurstRate,
       "an50pmpLinkDLRSSI": an50pmpLinkDLRSSI,
       "an50pmpLinkDLSINADR": an50pmpLinkDLSINADR,
       "an50pmpLinkDLStatLostFrm": an50pmpLinkDLStatLostFrm,
       "an50pmpLinkDLStatBlksTot": an50pmpLinkDLStatBlksTot,
       "an50pmpLinkDLStatBlksRetr": an50pmpLinkDLStatBlksRetr,
       "an50pmpLinkDLStatBlksDisc": an50pmpLinkDLStatBlksDisc,
       "an50pmpLinkDLCIDStatPktDisc": an50pmpLinkDLCIDStatPktDisc,
       "an50pmpLinkDLCIDStatPktTran": an50pmpLinkDLCIDStatPktTran,
       "an50pmpLinkDLCIDStatPktRecv": an50pmpLinkDLCIDStatPktRecv,
       "an50pmpLinkULBurstRate": an50pmpLinkULBurstRate,
       "an50pmpLinkULRSSI": an50pmpLinkULRSSI,
       "an50pmpLinkULSINADR": an50pmpLinkULSINADR,
       "an50pmpLinkULStatLostFrm": an50pmpLinkULStatLostFrm,
       "an50pmpLinkULStatBlksTot": an50pmpLinkULStatBlksTot,
       "an50pmpLinkULStatBlksRetr": an50pmpLinkULStatBlksRetr,
       "an50pmpLinkULStatBlksDisc": an50pmpLinkULStatBlksDisc,
       "an50pmpLinkULCIDStatPktDisc": an50pmpLinkULCIDStatPktDisc,
       "an50pmpLinkULCIDStatPktTran": an50pmpLinkULCIDStatPktTran,
       "an50pmpLinkULCIDStatPktRecv": an50pmpLinkULCIDStatPktRecv,
       "an50pmpLinkUpTime": an50pmpLinkUpTime,
       "an50pmpLinkLostCount": an50pmpLinkLostCount,
       "an50pmpCIDSaveConfig": an50pmpCIDSaveConfig,
       "an50pmpLastModifiedCID": an50pmpLastModifiedCID,
       "an50pmpLastMissedSsMacAddress": an50pmpLastMissedSsMacAddress,
       "an50pmpLastRegisteredSsMacAddress": an50pmpLastRegisteredSsMacAddress,
       "an50pmpLastSuccessfulID": an50pmpLastSuccessfulID,
       "an50pmpLastDeniedSsMacAddress": an50pmpLastDeniedSsMacAddress}
)
