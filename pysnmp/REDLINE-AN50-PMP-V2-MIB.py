# SNMP MIB module (REDLINE-AN50-PMP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-AN50-PMP-V2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:27 2024
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

(redlineMgmt,) = mibBuilder.importSymbols(
    "REDLINE-MIB",
    "redlineMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

redlineAN50PMPV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_An50pmpLinkTable_Object = MibTable
an50pmpLinkTable = _An50pmpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1)
)
if mibBuilder.loadTexts:
    an50pmpLinkTable.setStatus("current")
_An50pmpLinkEntry_Object = MibTableRow
an50pmpLinkEntry = _An50pmpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1)
)
an50pmpLinkEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkID"),
)
if mibBuilder.loadTexts:
    an50pmpLinkEntry.setStatus("current")


class _An50pmpLinkID_Type(Integer32):
    """Custom type an50pmpLinkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpLinkID_Type.__name__ = "Integer32"
_An50pmpLinkID_Object = MibTableColumn
an50pmpLinkID = _An50pmpLinkID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 1),
    _An50pmpLinkID_Type()
)
an50pmpLinkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an50pmpLinkID.setStatus("current")


class _An50pmpLinkName_Type(OctetString):
    """Custom type an50pmpLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_An50pmpLinkName_Type.__name__ = "OctetString"
_An50pmpLinkName_Object = MibTableColumn
an50pmpLinkName = _An50pmpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 2),
    _An50pmpLinkName_Type()
)
an50pmpLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkName.setStatus("current")


class _An50pmpLinkGroupId_Type(Integer32):
    """Custom type an50pmpLinkGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_An50pmpLinkGroupId_Type.__name__ = "Integer32"
_An50pmpLinkGroupId_Object = MibTableColumn
an50pmpLinkGroupId = _An50pmpLinkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 3),
    _An50pmpLinkGroupId_Type()
)
an50pmpLinkGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkGroupId.setStatus("obsolete")


class _An50pmpLinkPeerMac_Type(OctetString):
    """Custom type an50pmpLinkPeerMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_An50pmpLinkPeerMac_Type.__name__ = "OctetString"
_An50pmpLinkPeerMac_Object = MibTableColumn
an50pmpLinkPeerMac = _An50pmpLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 4),
    _An50pmpLinkPeerMac_Type()
)
an50pmpLinkPeerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkPeerMac.setStatus("current")


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
    an50pmpLinkMaxDLBurstRate.setStatus("current")


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
    an50pmpLinkMaxULBurstRate.setStatus("current")
_An50pmpLinkMaxHost_Type = Integer32
_An50pmpLinkMaxHost_Object = MibTableColumn
an50pmpLinkMaxHost = _An50pmpLinkMaxHost_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 7),
    _An50pmpLinkMaxHost_Type()
)
an50pmpLinkMaxHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkMaxHost.setStatus("obsolete")


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
    an50pmpLinkCIDDLCIR.setStatus("obsolete")


class _An50pmpLinkCIDDLPIR_Type(Integer32):
    """Custom type an50pmpLinkCIDDLPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_An50pmpLinkCIDDLPIR_Type.__name__ = "Integer32"
_An50pmpLinkCIDDLPIR_Object = MibTableColumn
an50pmpLinkCIDDLPIR = _An50pmpLinkCIDDLPIR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 9),
    _An50pmpLinkCIDDLPIR_Type()
)
an50pmpLinkCIDDLPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkCIDDLPIR.setStatus("obsolete")


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
    an50pmpLinkCIDULCIR.setStatus("obsolete")


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
    an50pmpLinkCIDULPIR.setStatus("obsolete")


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
    an50pmpLinkDLQoS.setStatus("obsolete")


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
    an50pmpLinkULQoS.setStatus("obsolete")


class _An50pmpLinkRowStatus_Type(RowStatus):
    """Custom type an50pmpLinkRowStatus based on RowStatus"""


_An50pmpLinkRowStatus_Object = MibTableColumn
an50pmpLinkRowStatus = _An50pmpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 14),
    _An50pmpLinkRowStatus_Type()
)
an50pmpLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkRowStatus.setStatus("current")


class _An50pmpLinkEncryptionKey_Type(OctetString):
    """Custom type an50pmpLinkEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_An50pmpLinkEncryptionKey_Type.__name__ = "OctetString"
_An50pmpLinkEncryptionKey_Object = MibTableColumn
an50pmpLinkEncryptionKey = _An50pmpLinkEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 1, 1, 15),
    _An50pmpLinkEncryptionKey_Type()
)
an50pmpLinkEncryptionKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLinkEncryptionKey.setStatus("current")
_An50pmpLinkStatusTable_Object = MibTable
an50pmpLinkStatusTable = _An50pmpLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2)
)
if mibBuilder.loadTexts:
    an50pmpLinkStatusTable.setStatus("current")
_An50pmpLinkStatusEntry_Object = MibTableRow
an50pmpLinkStatusEntry = _An50pmpLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1)
)
an50pmpLinkStatusEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkStatusID"),
)
if mibBuilder.loadTexts:
    an50pmpLinkStatusEntry.setStatus("current")


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
an50pmpLinkStatusID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an50pmpLinkStatusID.setStatus("current")


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
    an50pmpLinkStatus.setStatus("current")
_An50pmpLinkStatusCode_Type = Integer32
_An50pmpLinkStatusCode_Object = MibTableColumn
an50pmpLinkStatusCode = _An50pmpLinkStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 3),
    _An50pmpLinkStatusCode_Type()
)
an50pmpLinkStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkStatusCode.setStatus("current")


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
    an50pmpLinkRegConn.setStatus("current")


class _An50pmpLinkDLBurstRate_Type(Integer32):
    """Custom type an50pmpLinkDLBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("tx12Mbs", 3),
          ("tx18Mbs", 4),
          ("tx24Mbs", 5),
          ("tx36Mbs", 6),
          ("tx48Mbs", 7),
          ("tx54Mbs", 8),
          ("tx6Mbs", 1),
          ("tx9Mbs", 2))
    )


_An50pmpLinkDLBurstRate_Type.__name__ = "Integer32"
_An50pmpLinkDLBurstRate_Object = MibTableColumn
an50pmpLinkDLBurstRate = _An50pmpLinkDLBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 5),
    _An50pmpLinkDLBurstRate_Type()
)
an50pmpLinkDLBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLBurstRate.setStatus("current")
_An50pmpLinkDLRSSI_Type = Integer32
_An50pmpLinkDLRSSI_Object = MibTableColumn
an50pmpLinkDLRSSI = _An50pmpLinkDLRSSI_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 6),
    _An50pmpLinkDLRSSI_Type()
)
an50pmpLinkDLRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLRSSI.setStatus("current")
_An50pmpLinkDLSINADR_Type = Integer32
_An50pmpLinkDLSINADR_Object = MibTableColumn
an50pmpLinkDLSINADR = _An50pmpLinkDLSINADR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 7),
    _An50pmpLinkDLSINADR_Type()
)
an50pmpLinkDLSINADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLSINADR.setStatus("current")
_An50pmpLinkDLStatLostFrm_Type = Integer32
_An50pmpLinkDLStatLostFrm_Object = MibTableColumn
an50pmpLinkDLStatLostFrm = _An50pmpLinkDLStatLostFrm_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 8),
    _An50pmpLinkDLStatLostFrm_Type()
)
an50pmpLinkDLStatLostFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatLostFrm.setStatus("current")
_An50pmpLinkDLStatBlksTot_Type = Integer32
_An50pmpLinkDLStatBlksTot_Object = MibTableColumn
an50pmpLinkDLStatBlksTot = _An50pmpLinkDLStatBlksTot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 9),
    _An50pmpLinkDLStatBlksTot_Type()
)
an50pmpLinkDLStatBlksTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatBlksTot.setStatus("current")
_An50pmpLinkDLStatBlksRetr_Type = Integer32
_An50pmpLinkDLStatBlksRetr_Object = MibTableColumn
an50pmpLinkDLStatBlksRetr = _An50pmpLinkDLStatBlksRetr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 10),
    _An50pmpLinkDLStatBlksRetr_Type()
)
an50pmpLinkDLStatBlksRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatBlksRetr.setStatus("current")
_An50pmpLinkDLStatBlksDisc_Type = Integer32
_An50pmpLinkDLStatBlksDisc_Object = MibTableColumn
an50pmpLinkDLStatBlksDisc = _An50pmpLinkDLStatBlksDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 11),
    _An50pmpLinkDLStatBlksDisc_Type()
)
an50pmpLinkDLStatBlksDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLStatBlksDisc.setStatus("current")
_An50pmpLinkDLCIDStatPktDisc_Type = Integer32
_An50pmpLinkDLCIDStatPktDisc_Object = MibTableColumn
an50pmpLinkDLCIDStatPktDisc = _An50pmpLinkDLCIDStatPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 12),
    _An50pmpLinkDLCIDStatPktDisc_Type()
)
an50pmpLinkDLCIDStatPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLCIDStatPktDisc.setStatus("current")
_An50pmpLinkDLCIDStatPktTran_Type = Integer32
_An50pmpLinkDLCIDStatPktTran_Object = MibTableColumn
an50pmpLinkDLCIDStatPktTran = _An50pmpLinkDLCIDStatPktTran_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 13),
    _An50pmpLinkDLCIDStatPktTran_Type()
)
an50pmpLinkDLCIDStatPktTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLCIDStatPktTran.setStatus("current")
_An50pmpLinkDLCIDStatPktRecv_Type = Integer32
_An50pmpLinkDLCIDStatPktRecv_Object = MibTableColumn
an50pmpLinkDLCIDStatPktRecv = _An50pmpLinkDLCIDStatPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 14),
    _An50pmpLinkDLCIDStatPktRecv_Type()
)
an50pmpLinkDLCIDStatPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkDLCIDStatPktRecv.setStatus("current")


class _An50pmpLinkULBurstRate_Type(Integer32):
    """Custom type an50pmpLinkULBurstRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("tx12Mbs", 3),
          ("tx18Mbs", 4),
          ("tx24Mbs", 5),
          ("tx36Mbs", 6),
          ("tx48Mbs", 7),
          ("tx54Mbs", 8),
          ("tx6Mbs", 1),
          ("tx9Mbs", 2))
    )


_An50pmpLinkULBurstRate_Type.__name__ = "Integer32"
_An50pmpLinkULBurstRate_Object = MibTableColumn
an50pmpLinkULBurstRate = _An50pmpLinkULBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 15),
    _An50pmpLinkULBurstRate_Type()
)
an50pmpLinkULBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULBurstRate.setStatus("current")
_An50pmpLinkULRSSI_Type = Integer32
_An50pmpLinkULRSSI_Object = MibTableColumn
an50pmpLinkULRSSI = _An50pmpLinkULRSSI_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 16),
    _An50pmpLinkULRSSI_Type()
)
an50pmpLinkULRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULRSSI.setStatus("current")
_An50pmpLinkULSINADR_Type = Integer32
_An50pmpLinkULSINADR_Object = MibTableColumn
an50pmpLinkULSINADR = _An50pmpLinkULSINADR_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 17),
    _An50pmpLinkULSINADR_Type()
)
an50pmpLinkULSINADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULSINADR.setStatus("current")
_An50pmpLinkULStatLostFrm_Type = Integer32
_An50pmpLinkULStatLostFrm_Object = MibTableColumn
an50pmpLinkULStatLostFrm = _An50pmpLinkULStatLostFrm_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 18),
    _An50pmpLinkULStatLostFrm_Type()
)
an50pmpLinkULStatLostFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatLostFrm.setStatus("current")
_An50pmpLinkULStatBlksTot_Type = Integer32
_An50pmpLinkULStatBlksTot_Object = MibTableColumn
an50pmpLinkULStatBlksTot = _An50pmpLinkULStatBlksTot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 19),
    _An50pmpLinkULStatBlksTot_Type()
)
an50pmpLinkULStatBlksTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatBlksTot.setStatus("current")
_An50pmpLinkULStatBlksRetr_Type = Integer32
_An50pmpLinkULStatBlksRetr_Object = MibTableColumn
an50pmpLinkULStatBlksRetr = _An50pmpLinkULStatBlksRetr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 20),
    _An50pmpLinkULStatBlksRetr_Type()
)
an50pmpLinkULStatBlksRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatBlksRetr.setStatus("current")
_An50pmpLinkULStatBlksDisc_Type = Integer32
_An50pmpLinkULStatBlksDisc_Object = MibTableColumn
an50pmpLinkULStatBlksDisc = _An50pmpLinkULStatBlksDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 21),
    _An50pmpLinkULStatBlksDisc_Type()
)
an50pmpLinkULStatBlksDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULStatBlksDisc.setStatus("current")
_An50pmpLinkULCIDStatPktDisc_Type = Integer32
_An50pmpLinkULCIDStatPktDisc_Object = MibTableColumn
an50pmpLinkULCIDStatPktDisc = _An50pmpLinkULCIDStatPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 22),
    _An50pmpLinkULCIDStatPktDisc_Type()
)
an50pmpLinkULCIDStatPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULCIDStatPktDisc.setStatus("current")
_An50pmpLinkULCIDStatPktTran_Type = Integer32
_An50pmpLinkULCIDStatPktTran_Object = MibTableColumn
an50pmpLinkULCIDStatPktTran = _An50pmpLinkULCIDStatPktTran_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 23),
    _An50pmpLinkULCIDStatPktTran_Type()
)
an50pmpLinkULCIDStatPktTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULCIDStatPktTran.setStatus("current")
_An50pmpLinkULCIDStatPktRecv_Type = Integer32
_An50pmpLinkULCIDStatPktRecv_Object = MibTableColumn
an50pmpLinkULCIDStatPktRecv = _An50pmpLinkULCIDStatPktRecv_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 24),
    _An50pmpLinkULCIDStatPktRecv_Type()
)
an50pmpLinkULCIDStatPktRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkULCIDStatPktRecv.setStatus("current")
_An50pmpLinkUpTime_Type = TimeTicks
_An50pmpLinkUpTime_Object = MibTableColumn
an50pmpLinkUpTime = _An50pmpLinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 25),
    _An50pmpLinkUpTime_Type()
)
an50pmpLinkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkUpTime.setStatus("current")
_An50pmpLinkLostCount_Type = Integer32
_An50pmpLinkLostCount_Object = MibTableColumn
an50pmpLinkLostCount = _An50pmpLinkLostCount_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 2, 1, 26),
    _An50pmpLinkLostCount_Type()
)
an50pmpLinkLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLinkLostCount.setStatus("current")


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
        *(("doNothing", 1),
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
    an50pmpCIDSaveConfig.setStatus("current")


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
    an50pmpLastModifiedCID.setStatus("current")
_An50pmpLastMissedSsMacAddress_Type = OctetString
_An50pmpLastMissedSsMacAddress_Object = MibScalar
an50pmpLastMissedSsMacAddress = _An50pmpLastMissedSsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 5),
    _An50pmpLastMissedSsMacAddress_Type()
)
an50pmpLastMissedSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLastMissedSsMacAddress.setStatus("current")
_An50pmpLastRegisteredSsMacAddress_Type = OctetString
_An50pmpLastRegisteredSsMacAddress_Object = MibScalar
an50pmpLastRegisteredSsMacAddress = _An50pmpLastRegisteredSsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 6),
    _An50pmpLastRegisteredSsMacAddress_Type()
)
an50pmpLastRegisteredSsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpLastRegisteredSsMacAddress.setStatus("current")


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
    an50pmpLastSuccessfulID.setStatus("current")
_An50pmpLastDeniedSsMacAddress_Type = OctetString
_An50pmpLastDeniedSsMacAddress_Object = MibScalar
an50pmpLastDeniedSsMacAddress = _An50pmpLastDeniedSsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 8),
    _An50pmpLastDeniedSsMacAddress_Type()
)
an50pmpLastDeniedSsMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpLastDeniedSsMacAddress.setStatus("current")
_An50pmpGroupTable_Object = MibTable
an50pmpGroupTable = _An50pmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9)
)
if mibBuilder.loadTexts:
    an50pmpGroupTable.setStatus("current")
_An50pmpGroupEntry_Object = MibTableRow
an50pmpGroupEntry = _An50pmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1)
)
an50pmpGroupEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupId"),
)
if mibBuilder.loadTexts:
    an50pmpGroupEntry.setStatus("current")


class _An50pmpGroupId_Type(Integer32):
    """Custom type an50pmpGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_An50pmpGroupId_Type.__name__ = "Integer32"
_An50pmpGroupId_Object = MibTableColumn
an50pmpGroupId = _An50pmpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 1),
    _An50pmpGroupId_Type()
)
an50pmpGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an50pmpGroupId.setStatus("current")


class _An50pmpGroupName_Type(OctetString):
    """Custom type an50pmpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_An50pmpGroupName_Type.__name__ = "OctetString"
_An50pmpGroupName_Object = MibTableColumn
an50pmpGroupName = _An50pmpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 2),
    _An50pmpGroupName_Type()
)
an50pmpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupName.setStatus("current")


class _An50pmpGroupBSPortTagging_Type(Integer32):
    """Custom type an50pmpGroupBSPortTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passThrough", 1),
          ("tagged", 2))
    )


_An50pmpGroupBSPortTagging_Type.__name__ = "Integer32"
_An50pmpGroupBSPortTagging_Object = MibTableColumn
an50pmpGroupBSPortTagging = _An50pmpGroupBSPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 3),
    _An50pmpGroupBSPortTagging_Type()
)
an50pmpGroupBSPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupBSPortTagging.setStatus("current")


class _An50pmpGroupVlanId_Type(Integer32):
    """Custom type an50pmpGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_An50pmpGroupVlanId_Type.__name__ = "Integer32"
_An50pmpGroupVlanId_Object = MibTableColumn
an50pmpGroupVlanId = _An50pmpGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 4),
    _An50pmpGroupVlanId_Type()
)
an50pmpGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupVlanId.setStatus("current")


class _An50pmpGroupDefaultPriority_Type(Integer32):
    """Custom type an50pmpGroupDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpGroupDefaultPriority_Type.__name__ = "Integer32"
_An50pmpGroupDefaultPriority_Object = MibTableColumn
an50pmpGroupDefaultPriority = _An50pmpGroupDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 5),
    _An50pmpGroupDefaultPriority_Type()
)
an50pmpGroupDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupDefaultPriority.setStatus("current")


class _An50pmpGroupBSPortEnabled_Type(Integer32):
    """Custom type an50pmpGroupBSPortEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_An50pmpGroupBSPortEnabled_Type.__name__ = "Integer32"
_An50pmpGroupBSPortEnabled_Object = MibTableColumn
an50pmpGroupBSPortEnabled = _An50pmpGroupBSPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 6),
    _An50pmpGroupBSPortEnabled_Type()
)
an50pmpGroupBSPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupBSPortEnabled.setStatus("current")


class _An50pmpGroupQos_Type(Integer32):
    """Custom type an50pmpGroupQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpGroupQos_Type.__name__ = "Integer32"
_An50pmpGroupQos_Object = MibTableColumn
an50pmpGroupQos = _An50pmpGroupQos_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 7),
    _An50pmpGroupQos_Type()
)
an50pmpGroupQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupQos.setStatus("current")


class _An50pmpGroupRowStatus_Type(RowStatus):
    """Custom type an50pmpGroupRowStatus based on RowStatus"""


_An50pmpGroupRowStatus_Object = MibTableColumn
an50pmpGroupRowStatus = _An50pmpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 9, 1, 8),
    _An50pmpGroupRowStatus_Type()
)
an50pmpGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpGroupRowStatus.setStatus("current")
_An50pmpConnectionTable_Object = MibTable
an50pmpConnectionTable = _An50pmpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10)
)
if mibBuilder.loadTexts:
    an50pmpConnectionTable.setStatus("current")
_An50pmpConnectionEntry_Object = MibTableRow
an50pmpConnectionEntry = _An50pmpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1)
)
an50pmpConnectionEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionId"),
)
if mibBuilder.loadTexts:
    an50pmpConnectionEntry.setStatus("current")


class _An50pmpConnectionId_Type(Integer32):
    """Custom type an50pmpConnectionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_An50pmpConnectionId_Type.__name__ = "Integer32"
_An50pmpConnectionId_Object = MibTableColumn
an50pmpConnectionId = _An50pmpConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 1),
    _An50pmpConnectionId_Type()
)
an50pmpConnectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an50pmpConnectionId.setStatus("current")


class _An50pmpConnectionName_Type(OctetString):
    """Custom type an50pmpConnectionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_An50pmpConnectionName_Type.__name__ = "OctetString"
_An50pmpConnectionName_Object = MibTableColumn
an50pmpConnectionName = _An50pmpConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 2),
    _An50pmpConnectionName_Type()
)
an50pmpConnectionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionName.setStatus("current")


class _An50pmpConnectionPortTagging_Type(Integer32):
    """Custom type an50pmpConnectionPortTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passThrough", 1),
          ("tagged", 2))
    )


_An50pmpConnectionPortTagging_Type.__name__ = "Integer32"
_An50pmpConnectionPortTagging_Object = MibTableColumn
an50pmpConnectionPortTagging = _An50pmpConnectionPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 3),
    _An50pmpConnectionPortTagging_Type()
)
an50pmpConnectionPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionPortTagging.setStatus("current")


class _An50pmpConnectionVlanId_Type(Integer32):
    """Custom type an50pmpConnectionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpConnectionVlanId_Type.__name__ = "Integer32"
_An50pmpConnectionVlanId_Object = MibTableColumn
an50pmpConnectionVlanId = _An50pmpConnectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 4),
    _An50pmpConnectionVlanId_Type()
)
an50pmpConnectionVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionVlanId.setStatus("current")


class _An50pmpConnectionDefaultPriority_Type(Integer32):
    """Custom type an50pmpConnectionDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpConnectionDefaultPriority_Type.__name__ = "Integer32"
_An50pmpConnectionDefaultPriority_Object = MibTableColumn
an50pmpConnectionDefaultPriority = _An50pmpConnectionDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 5),
    _An50pmpConnectionDefaultPriority_Type()
)
an50pmpConnectionDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionDefaultPriority.setStatus("current")


class _An50pmpConnectionParentLink_Type(Integer32):
    """Custom type an50pmpConnectionParentLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpConnectionParentLink_Type.__name__ = "Integer32"
_An50pmpConnectionParentLink_Object = MibTableColumn
an50pmpConnectionParentLink = _An50pmpConnectionParentLink_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 6),
    _An50pmpConnectionParentLink_Type()
)
an50pmpConnectionParentLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionParentLink.setStatus("current")


class _An50pmpConnectionParentGroup_Type(Integer32):
    """Custom type an50pmpConnectionParentGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpConnectionParentGroup_Type.__name__ = "Integer32"
_An50pmpConnectionParentGroup_Object = MibTableColumn
an50pmpConnectionParentGroup = _An50pmpConnectionParentGroup_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 7),
    _An50pmpConnectionParentGroup_Type()
)
an50pmpConnectionParentGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionParentGroup.setStatus("current")


class _An50pmpConnectionDLQoS_Type(Integer32):
    """Custom type an50pmpConnectionDLQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpConnectionDLQoS_Type.__name__ = "Integer32"
_An50pmpConnectionDLQoS_Object = MibTableColumn
an50pmpConnectionDLQoS = _An50pmpConnectionDLQoS_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 8),
    _An50pmpConnectionDLQoS_Type()
)
an50pmpConnectionDLQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionDLQoS.setStatus("current")


class _An50pmpConnectionULQoS_Type(Integer32):
    """Custom type an50pmpConnectionULQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_An50pmpConnectionULQoS_Type.__name__ = "Integer32"
_An50pmpConnectionULQoS_Object = MibTableColumn
an50pmpConnectionULQoS = _An50pmpConnectionULQoS_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 9),
    _An50pmpConnectionULQoS_Type()
)
an50pmpConnectionULQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionULQoS.setStatus("current")


class _An50pmpConnectionRowStatus_Type(RowStatus):
    """Custom type an50pmpConnectionRowStatus based on RowStatus"""


_An50pmpConnectionRowStatus_Object = MibTableColumn
an50pmpConnectionRowStatus = _An50pmpConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 10, 1, 10),
    _An50pmpConnectionRowStatus_Type()
)
an50pmpConnectionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    an50pmpConnectionRowStatus.setStatus("current")
_An50pmpGroupStatusTable_Object = MibTable
an50pmpGroupStatusTable = _An50pmpGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11)
)
if mibBuilder.loadTexts:
    an50pmpGroupStatusTable.setStatus("current")
_An50pmpGroupStatusEntry_Object = MibTableRow
an50pmpGroupStatusEntry = _An50pmpGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1)
)
an50pmpGroupStatusEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusId"),
)
if mibBuilder.loadTexts:
    an50pmpGroupStatusEntry.setStatus("current")


class _An50pmpGroupStatusId_Type(Integer32):
    """Custom type an50pmpGroupStatusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_An50pmpGroupStatusId_Type.__name__ = "Integer32"
_An50pmpGroupStatusId_Object = MibTableColumn
an50pmpGroupStatusId = _An50pmpGroupStatusId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 1),
    _An50pmpGroupStatusId_Type()
)
an50pmpGroupStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an50pmpGroupStatusId.setStatus("current")
_An50pmpGroupStatusDLPacketsDiscards_Type = Counter32
_An50pmpGroupStatusDLPacketsDiscards_Object = MibTableColumn
an50pmpGroupStatusDLPacketsDiscards = _An50pmpGroupStatusDLPacketsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 2),
    _An50pmpGroupStatusDLPacketsDiscards_Type()
)
an50pmpGroupStatusDLPacketsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpGroupStatusDLPacketsDiscards.setStatus("current")
_An50pmpGroupStatusDLPacketsTx_Type = Counter32
_An50pmpGroupStatusDLPacketsTx_Object = MibTableColumn
an50pmpGroupStatusDLPacketsTx = _An50pmpGroupStatusDLPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 3),
    _An50pmpGroupStatusDLPacketsTx_Type()
)
an50pmpGroupStatusDLPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpGroupStatusDLPacketsTx.setStatus("current")
_An50pmpGroupStatusDLPacketsRx_Type = Counter32
_An50pmpGroupStatusDLPacketsRx_Object = MibTableColumn
an50pmpGroupStatusDLPacketsRx = _An50pmpGroupStatusDLPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 4),
    _An50pmpGroupStatusDLPacketsRx_Type()
)
an50pmpGroupStatusDLPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpGroupStatusDLPacketsRx.setStatus("current")
_An50pmpGroupStatusULPacketsDiscards_Type = Counter32
_An50pmpGroupStatusULPacketsDiscards_Object = MibTableColumn
an50pmpGroupStatusULPacketsDiscards = _An50pmpGroupStatusULPacketsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 5),
    _An50pmpGroupStatusULPacketsDiscards_Type()
)
an50pmpGroupStatusULPacketsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpGroupStatusULPacketsDiscards.setStatus("current")
_An50pmpGroupStatusULPacketsTx_Type = Counter32
_An50pmpGroupStatusULPacketsTx_Object = MibTableColumn
an50pmpGroupStatusULPacketsTx = _An50pmpGroupStatusULPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 6),
    _An50pmpGroupStatusULPacketsTx_Type()
)
an50pmpGroupStatusULPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpGroupStatusULPacketsTx.setStatus("current")
_An50pmpGroupStatusULPacketsRx_Type = Counter32
_An50pmpGroupStatusULPacketsRx_Object = MibTableColumn
an50pmpGroupStatusULPacketsRx = _An50pmpGroupStatusULPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 11, 1, 7),
    _An50pmpGroupStatusULPacketsRx_Type()
)
an50pmpGroupStatusULPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpGroupStatusULPacketsRx.setStatus("current")
_An50pmpConnectionStatusTable_Object = MibTable
an50pmpConnectionStatusTable = _An50pmpConnectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12)
)
if mibBuilder.loadTexts:
    an50pmpConnectionStatusTable.setStatus("current")
_An50pmpConnectionStatusEntry_Object = MibTableRow
an50pmpConnectionStatusEntry = _An50pmpConnectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1)
)
an50pmpConnectionStatusEntry.setIndexNames(
    (0, "REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusId"),
)
if mibBuilder.loadTexts:
    an50pmpConnectionStatusEntry.setStatus("current")


class _An50pmpConnectionStatusId_Type(Integer32):
    """Custom type an50pmpConnectionStatusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_An50pmpConnectionStatusId_Type.__name__ = "Integer32"
_An50pmpConnectionStatusId_Object = MibTableColumn
an50pmpConnectionStatusId = _An50pmpConnectionStatusId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 1),
    _An50pmpConnectionStatusId_Type()
)
an50pmpConnectionStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusId.setStatus("current")
_An50pmpConnectionStatusDLPacketsDiscards_Type = Counter32
_An50pmpConnectionStatusDLPacketsDiscards_Object = MibTableColumn
an50pmpConnectionStatusDLPacketsDiscards = _An50pmpConnectionStatusDLPacketsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 2),
    _An50pmpConnectionStatusDLPacketsDiscards_Type()
)
an50pmpConnectionStatusDLPacketsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusDLPacketsDiscards.setStatus("current")
_An50pmpConnectionStatusDLPacketsTx_Type = Counter32
_An50pmpConnectionStatusDLPacketsTx_Object = MibTableColumn
an50pmpConnectionStatusDLPacketsTx = _An50pmpConnectionStatusDLPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 3),
    _An50pmpConnectionStatusDLPacketsTx_Type()
)
an50pmpConnectionStatusDLPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusDLPacketsTx.setStatus("current")
_An50pmpConnectionStatusDLPacketsRx_Type = Counter32
_An50pmpConnectionStatusDLPacketsRx_Object = MibTableColumn
an50pmpConnectionStatusDLPacketsRx = _An50pmpConnectionStatusDLPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 4),
    _An50pmpConnectionStatusDLPacketsRx_Type()
)
an50pmpConnectionStatusDLPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusDLPacketsRx.setStatus("current")
_An50pmpConnectionStatusULPacketsDiscards_Type = Counter32
_An50pmpConnectionStatusULPacketsDiscards_Object = MibTableColumn
an50pmpConnectionStatusULPacketsDiscards = _An50pmpConnectionStatusULPacketsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 5),
    _An50pmpConnectionStatusULPacketsDiscards_Type()
)
an50pmpConnectionStatusULPacketsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusULPacketsDiscards.setStatus("current")
_An50pmpConnectionStatusULPacketsTx_Type = Counter32
_An50pmpConnectionStatusULPacketsTx_Object = MibTableColumn
an50pmpConnectionStatusULPacketsTx = _An50pmpConnectionStatusULPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 6),
    _An50pmpConnectionStatusULPacketsTx_Type()
)
an50pmpConnectionStatusULPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusULPacketsTx.setStatus("current")
_An50pmpConnectionStatusULPacketsRx_Type = Counter32
_An50pmpConnectionStatusULPacketsRx_Object = MibTableColumn
an50pmpConnectionStatusULPacketsRx = _An50pmpConnectionStatusULPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 12, 1, 7),
    _An50pmpConnectionStatusULPacketsRx_Type()
)
an50pmpConnectionStatusULPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    an50pmpConnectionStatusULPacketsRx.setStatus("current")

# Managed Objects groups

an50PMPObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 13)
)
an50PMPObjectGroup.setObjects(
      *(("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkName"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkPeerMac"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkMaxDLBurstRate"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkMaxULBurstRate"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkEncryptionKey"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkRowStatus"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkStatus"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkStatusCode"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkRegConn"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLBurstRate"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLRSSI"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLSINADR"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLStatLostFrm"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLStatBlksTot"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLStatBlksRetr"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLStatBlksDisc"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLCIDStatPktDisc"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLCIDStatPktTran"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLCIDStatPktRecv"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULBurstRate"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULRSSI"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULSINADR"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULStatLostFrm"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULStatBlksTot"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULStatBlksRetr"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULStatBlksDisc"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULCIDStatPktDisc"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULCIDStatPktTran"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULCIDStatPktRecv"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkUpTime"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkLostCount"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpCIDSaveConfig"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLastModifiedCID"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLastMissedSsMacAddress"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLastRegisteredSsMacAddress"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLastSuccessfulID"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLastDeniedSsMacAddress"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupName"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupBSPortTagging"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupVlanId"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupDefaultPriority"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupBSPortEnabled"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupQos"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupRowStatus"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionName"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionPortTagging"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionVlanId"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionDefaultPriority"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionParentLink"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionParentGroup"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionDLQoS"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionULQoS"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionRowStatus"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusDLPacketsDiscards"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusDLPacketsTx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusDLPacketsRx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusULPacketsDiscards"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusULPacketsTx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpGroupStatusULPacketsRx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusDLPacketsDiscards"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusDLPacketsTx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusDLPacketsRx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusULPacketsDiscards"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusULPacketsTx"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpConnectionStatusULPacketsRx"))
)
if mibBuilder.loadTexts:
    an50PMPObjectGroup.setStatus("current")

an50PMPObsoleteObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 51, 14)
)
an50PMPObsoleteObjectGroup.setObjects(
      *(("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkGroupId"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkMaxHost"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkCIDDLCIR"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkCIDDLPIR"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkCIDULCIR"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkCIDULPIR"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkDLQoS"),
        ("REDLINE-AN50-PMP-V2-MIB", "an50pmpLinkULQoS"))
)
if mibBuilder.loadTexts:
    an50PMPObsoleteObjectGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-AN50-PMP-V2-MIB",
    **{"redlineAN50PMPV2": redlineAN50PMPV2,
       "an50pmpLinkTable": an50pmpLinkTable,
       "an50pmpLinkEntry": an50pmpLinkEntry,
       "an50pmpLinkID": an50pmpLinkID,
       "an50pmpLinkName": an50pmpLinkName,
       "an50pmpLinkGroupId": an50pmpLinkGroupId,
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
       "an50pmpLinkEncryptionKey": an50pmpLinkEncryptionKey,
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
       "an50pmpLastDeniedSsMacAddress": an50pmpLastDeniedSsMacAddress,
       "an50pmpGroupTable": an50pmpGroupTable,
       "an50pmpGroupEntry": an50pmpGroupEntry,
       "an50pmpGroupId": an50pmpGroupId,
       "an50pmpGroupName": an50pmpGroupName,
       "an50pmpGroupBSPortTagging": an50pmpGroupBSPortTagging,
       "an50pmpGroupVlanId": an50pmpGroupVlanId,
       "an50pmpGroupDefaultPriority": an50pmpGroupDefaultPriority,
       "an50pmpGroupBSPortEnabled": an50pmpGroupBSPortEnabled,
       "an50pmpGroupQos": an50pmpGroupQos,
       "an50pmpGroupRowStatus": an50pmpGroupRowStatus,
       "an50pmpConnectionTable": an50pmpConnectionTable,
       "an50pmpConnectionEntry": an50pmpConnectionEntry,
       "an50pmpConnectionId": an50pmpConnectionId,
       "an50pmpConnectionName": an50pmpConnectionName,
       "an50pmpConnectionPortTagging": an50pmpConnectionPortTagging,
       "an50pmpConnectionVlanId": an50pmpConnectionVlanId,
       "an50pmpConnectionDefaultPriority": an50pmpConnectionDefaultPriority,
       "an50pmpConnectionParentLink": an50pmpConnectionParentLink,
       "an50pmpConnectionParentGroup": an50pmpConnectionParentGroup,
       "an50pmpConnectionDLQoS": an50pmpConnectionDLQoS,
       "an50pmpConnectionULQoS": an50pmpConnectionULQoS,
       "an50pmpConnectionRowStatus": an50pmpConnectionRowStatus,
       "an50pmpGroupStatusTable": an50pmpGroupStatusTable,
       "an50pmpGroupStatusEntry": an50pmpGroupStatusEntry,
       "an50pmpGroupStatusId": an50pmpGroupStatusId,
       "an50pmpGroupStatusDLPacketsDiscards": an50pmpGroupStatusDLPacketsDiscards,
       "an50pmpGroupStatusDLPacketsTx": an50pmpGroupStatusDLPacketsTx,
       "an50pmpGroupStatusDLPacketsRx": an50pmpGroupStatusDLPacketsRx,
       "an50pmpGroupStatusULPacketsDiscards": an50pmpGroupStatusULPacketsDiscards,
       "an50pmpGroupStatusULPacketsTx": an50pmpGroupStatusULPacketsTx,
       "an50pmpGroupStatusULPacketsRx": an50pmpGroupStatusULPacketsRx,
       "an50pmpConnectionStatusTable": an50pmpConnectionStatusTable,
       "an50pmpConnectionStatusEntry": an50pmpConnectionStatusEntry,
       "an50pmpConnectionStatusId": an50pmpConnectionStatusId,
       "an50pmpConnectionStatusDLPacketsDiscards": an50pmpConnectionStatusDLPacketsDiscards,
       "an50pmpConnectionStatusDLPacketsTx": an50pmpConnectionStatusDLPacketsTx,
       "an50pmpConnectionStatusDLPacketsRx": an50pmpConnectionStatusDLPacketsRx,
       "an50pmpConnectionStatusULPacketsDiscards": an50pmpConnectionStatusULPacketsDiscards,
       "an50pmpConnectionStatusULPacketsTx": an50pmpConnectionStatusULPacketsTx,
       "an50pmpConnectionStatusULPacketsRx": an50pmpConnectionStatusULPacketsRx,
       "an50PMPObjectGroup": an50PMPObjectGroup,
       "an50PMPObsoleteObjectGroup": an50PMPObsoleteObjectGroup}
)
