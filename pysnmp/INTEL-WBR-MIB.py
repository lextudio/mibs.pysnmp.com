# SNMP MIB module (INTEL-WBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-WBR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:03 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Wbr_ObjectIdentity = ObjectIdentity
wbr = _Wbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 25)
)
_WbrBase_ObjectIdentity = ObjectIdentity
wbrBase = _WbrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 1)
)
_WbrBaseLastConfigTime_Type = TimeTicks
_WbrBaseLastConfigTime_Object = MibScalar
wbrBaseLastConfigTime = _WbrBaseLastConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 1),
    _WbrBaseLastConfigTime_Type()
)
wbrBaseLastConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrBaseLastConfigTime.setStatus("mandatory")


class _WbrBaseBridging_Type(Integer32):
    """Custom type wbrBaseBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WbrBaseBridging_Type.__name__ = "Integer32"
_WbrBaseBridging_Object = MibScalar
wbrBaseBridging = _WbrBaseBridging_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 2),
    _WbrBaseBridging_Type()
)
wbrBaseBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrBaseBridging.setStatus("mandatory")


class _WbrBaseBridgingIP_Type(Integer32):
    """Custom type wbrBaseBridgingIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WbrBaseBridgingIP_Type.__name__ = "Integer32"
_WbrBaseBridgingIP_Object = MibScalar
wbrBaseBridgingIP = _WbrBaseBridgingIP_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 3),
    _WbrBaseBridgingIP_Type()
)
wbrBaseBridgingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrBaseBridgingIP.setStatus("mandatory")


class _WbrBaseBridgingIPX_Type(Integer32):
    """Custom type wbrBaseBridgingIPX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WbrBaseBridgingIPX_Type.__name__ = "Integer32"
_WbrBaseBridgingIPX_Object = MibScalar
wbrBaseBridgingIPX = _WbrBaseBridgingIPX_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 1, 4),
    _WbrBaseBridgingIPX_Type()
)
wbrBaseBridgingIPX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrBaseBridgingIPX.setStatus("mandatory")
_WbrStp_ObjectIdentity = ObjectIdentity
wbrStp = _WbrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2)
)
_WbrStpBridgeAgeingTime_Type = Integer32
_WbrStpBridgeAgeingTime_Object = MibScalar
wbrStpBridgeAgeingTime = _WbrStpBridgeAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 1),
    _WbrStpBridgeAgeingTime_Type()
)
wbrStpBridgeAgeingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpBridgeAgeingTime.setStatus("mandatory")


class _WbrStpBridgeIsRoot_Type(Integer32):
    """Custom type wbrStpBridgeIsRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WbrStpBridgeIsRoot_Type.__name__ = "Integer32"
_WbrStpBridgeIsRoot_Object = MibScalar
wbrStpBridgeIsRoot = _WbrStpBridgeIsRoot_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 2),
    _WbrStpBridgeIsRoot_Type()
)
wbrStpBridgeIsRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpBridgeIsRoot.setStatus("mandatory")
_WbrStpRxBPDUs_Type = Counter32
_WbrStpRxBPDUs_Object = MibScalar
wbrStpRxBPDUs = _WbrStpRxBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 3),
    _WbrStpRxBPDUs_Type()
)
wbrStpRxBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpRxBPDUs.setStatus("mandatory")
_WbrStpTxBPDUs_Type = Counter32
_WbrStpTxBPDUs_Object = MibScalar
wbrStpTxBPDUs = _WbrStpTxBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 4),
    _WbrStpTxBPDUs_Type()
)
wbrStpTxBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpTxBPDUs.setStatus("mandatory")
_WbrStpTxBPDUsFailed_Type = Counter32
_WbrStpTxBPDUsFailed_Object = MibScalar
wbrStpTxBPDUsFailed = _WbrStpTxBPDUsFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 5),
    _WbrStpTxBPDUsFailed_Type()
)
wbrStpTxBPDUsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpTxBPDUsFailed.setStatus("mandatory")
_WbrStpRxSpoofBPDUs_Type = Counter32
_WbrStpRxSpoofBPDUs_Object = MibScalar
wbrStpRxSpoofBPDUs = _WbrStpRxSpoofBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 6),
    _WbrStpRxSpoofBPDUs_Type()
)
wbrStpRxSpoofBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpRxSpoofBPDUs.setStatus("mandatory")
_WbrStpTxSpoofBPDUs_Type = Counter32
_WbrStpTxSpoofBPDUs_Object = MibScalar
wbrStpTxSpoofBPDUs = _WbrStpTxSpoofBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 7),
    _WbrStpTxSpoofBPDUs_Type()
)
wbrStpTxSpoofBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpTxSpoofBPDUs.setStatus("mandatory")
_WbrStpTxSpoofFailed_Type = Counter32
_WbrStpTxSpoofFailed_Object = MibScalar
wbrStpTxSpoofFailed = _WbrStpTxSpoofFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 8),
    _WbrStpTxSpoofFailed_Type()
)
wbrStpTxSpoofFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpTxSpoofFailed.setStatus("mandatory")
_WbrStpTxSpoofData_Type = Counter32
_WbrStpTxSpoofData_Object = MibScalar
wbrStpTxSpoofData = _WbrStpTxSpoofData_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 9),
    _WbrStpTxSpoofData_Type()
)
wbrStpTxSpoofData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpTxSpoofData.setStatus("mandatory")
_WbrStpLinkTable_Object = MibTable
wbrStpLinkTable = _WbrStpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10)
)
if mibBuilder.loadTexts:
    wbrStpLinkTable.setStatus("mandatory")
_WbrStpLinkEntry_Object = MibTableRow
wbrStpLinkEntry = _WbrStpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1)
)
wbrStpLinkEntry.setIndexNames(
    (0, "INTEL-WBR-MIB", "wbrStpLinkIfIndex"),
)
if mibBuilder.loadTexts:
    wbrStpLinkEntry.setStatus("mandatory")
_WbrStpLinkIfIndex_Type = Integer32
_WbrStpLinkIfIndex_Object = MibTableColumn
wbrStpLinkIfIndex = _WbrStpLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 1),
    _WbrStpLinkIfIndex_Type()
)
wbrStpLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkIfIndex.setStatus("mandatory")
_WbrStpLinkRxProtocolBytes_Type = Counter32
_WbrStpLinkRxProtocolBytes_Object = MibTableColumn
wbrStpLinkRxProtocolBytes = _WbrStpLinkRxProtocolBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 2),
    _WbrStpLinkRxProtocolBytes_Type()
)
wbrStpLinkRxProtocolBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkRxProtocolBytes.setStatus("mandatory")
_WbrStpLinkTxProtocolBytes_Type = Counter32
_WbrStpLinkTxProtocolBytes_Object = MibTableColumn
wbrStpLinkTxProtocolBytes = _WbrStpLinkTxProtocolBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 3),
    _WbrStpLinkTxProtocolBytes_Type()
)
wbrStpLinkTxProtocolBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTxProtocolBytes.setStatus("mandatory")
_WbrStpLinkRxBPDUs_Type = Counter32
_WbrStpLinkRxBPDUs_Object = MibTableColumn
wbrStpLinkRxBPDUs = _WbrStpLinkRxBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 4),
    _WbrStpLinkRxBPDUs_Type()
)
wbrStpLinkRxBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkRxBPDUs.setStatus("mandatory")
_WbrStpLinkTxBPDUs_Type = Counter32
_WbrStpLinkTxBPDUs_Object = MibTableColumn
wbrStpLinkTxBPDUs = _WbrStpLinkTxBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 5),
    _WbrStpLinkTxBPDUs_Type()
)
wbrStpLinkTxBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTxBPDUs.setStatus("mandatory")
_WbrStpLinkTxBPDUsFailed_Type = Counter32
_WbrStpLinkTxBPDUsFailed_Object = MibTableColumn
wbrStpLinkTxBPDUsFailed = _WbrStpLinkTxBPDUsFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 6),
    _WbrStpLinkTxBPDUsFailed_Type()
)
wbrStpLinkTxBPDUsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTxBPDUsFailed.setStatus("mandatory")
_WbrStpLinkRxSpoofBPDUs_Type = Counter32
_WbrStpLinkRxSpoofBPDUs_Object = MibTableColumn
wbrStpLinkRxSpoofBPDUs = _WbrStpLinkRxSpoofBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 7),
    _WbrStpLinkRxSpoofBPDUs_Type()
)
wbrStpLinkRxSpoofBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkRxSpoofBPDUs.setStatus("mandatory")
_WbrStpLinkTxSpoofBPDUs_Type = Counter32
_WbrStpLinkTxSpoofBPDUs_Object = MibTableColumn
wbrStpLinkTxSpoofBPDUs = _WbrStpLinkTxSpoofBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 8),
    _WbrStpLinkTxSpoofBPDUs_Type()
)
wbrStpLinkTxSpoofBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTxSpoofBPDUs.setStatus("mandatory")
_WbrStpLinkTxSpoofFailed_Type = Counter32
_WbrStpLinkTxSpoofFailed_Object = MibTableColumn
wbrStpLinkTxSpoofFailed = _WbrStpLinkTxSpoofFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 9),
    _WbrStpLinkTxSpoofFailed_Type()
)
wbrStpLinkTxSpoofFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTxSpoofFailed.setStatus("mandatory")
_WbrStpLinkTxSpoofData_Type = Counter32
_WbrStpLinkTxSpoofData_Object = MibTableColumn
wbrStpLinkTxSpoofData = _WbrStpLinkTxSpoofData_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 10),
    _WbrStpLinkTxSpoofData_Type()
)
wbrStpLinkTxSpoofData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTxSpoofData.setStatus("mandatory")


class _WbrStpLinkSPTStatus_Type(OctetString):
    """Custom type wbrStpLinkSPTStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_WbrStpLinkSPTStatus_Type.__name__ = "OctetString"
_WbrStpLinkSPTStatus_Object = MibTableColumn
wbrStpLinkSPTStatus = _WbrStpLinkSPTStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 11),
    _WbrStpLinkSPTStatus_Type()
)
wbrStpLinkSPTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkSPTStatus.setStatus("mandatory")


class _WbrStpLinkConfigBPDUPending_Type(Integer32):
    """Custom type wbrStpLinkConfigBPDUPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WbrStpLinkConfigBPDUPending_Type.__name__ = "Integer32"
_WbrStpLinkConfigBPDUPending_Object = MibTableColumn
wbrStpLinkConfigBPDUPending = _WbrStpLinkConfigBPDUPending_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 12),
    _WbrStpLinkConfigBPDUPending_Type()
)
wbrStpLinkConfigBPDUPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkConfigBPDUPending.setStatus("mandatory")


class _WbrStpLinkTopologyChangeAck_Type(Integer32):
    """Custom type wbrStpLinkTopologyChangeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WbrStpLinkTopologyChangeAck_Type.__name__ = "Integer32"
_WbrStpLinkTopologyChangeAck_Object = MibTableColumn
wbrStpLinkTopologyChangeAck = _WbrStpLinkTopologyChangeAck_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 13),
    _WbrStpLinkTopologyChangeAck_Type()
)
wbrStpLinkTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkTopologyChangeAck.setStatus("mandatory")


class _WbrStpLinkConfigBPDUAgeActive_Type(Integer32):
    """Custom type wbrStpLinkConfigBPDUAgeActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_WbrStpLinkConfigBPDUAgeActive_Type.__name__ = "Integer32"
_WbrStpLinkConfigBPDUAgeActive_Object = MibTableColumn
wbrStpLinkConfigBPDUAgeActive = _WbrStpLinkConfigBPDUAgeActive_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 14),
    _WbrStpLinkConfigBPDUAgeActive_Type()
)
wbrStpLinkConfigBPDUAgeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkConfigBPDUAgeActive.setStatus("mandatory")
_WbrStpLinkConfigBPDUAge_Type = Integer32
_WbrStpLinkConfigBPDUAge_Object = MibTableColumn
wbrStpLinkConfigBPDUAge = _WbrStpLinkConfigBPDUAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 15),
    _WbrStpLinkConfigBPDUAge_Type()
)
wbrStpLinkConfigBPDUAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkConfigBPDUAge.setStatus("mandatory")


class _WbrStpLinkBPDUSpoofing_Type(OctetString):
    """Custom type wbrStpLinkBPDUSpoofing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_WbrStpLinkBPDUSpoofing_Type.__name__ = "OctetString"
_WbrStpLinkBPDUSpoofing_Object = MibTableColumn
wbrStpLinkBPDUSpoofing = _WbrStpLinkBPDUSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 16),
    _WbrStpLinkBPDUSpoofing_Type()
)
wbrStpLinkBPDUSpoofing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkBPDUSpoofing.setStatus("mandatory")


class _WbrStpLinkNonBPDUSpoofing_Type(OctetString):
    """Custom type wbrStpLinkNonBPDUSpoofing based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_WbrStpLinkNonBPDUSpoofing_Type.__name__ = "OctetString"
_WbrStpLinkNonBPDUSpoofing_Object = MibTableColumn
wbrStpLinkNonBPDUSpoofing = _WbrStpLinkNonBPDUSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 17),
    _WbrStpLinkNonBPDUSpoofing_Type()
)
wbrStpLinkNonBPDUSpoofing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkNonBPDUSpoofing.setStatus("mandatory")


class _WbrStpLinkSpoofing_Type(Integer32):
    """Custom type wbrStpLinkSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WbrStpLinkSpoofing_Type.__name__ = "Integer32"
_WbrStpLinkSpoofing_Object = MibTableColumn
wbrStpLinkSpoofing = _WbrStpLinkSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 2, 10, 1, 18),
    _WbrStpLinkSpoofing_Type()
)
wbrStpLinkSpoofing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrStpLinkSpoofing.setStatus("mandatory")
_WbrTp_ObjectIdentity = ObjectIdentity
wbrTp = _WbrTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3)
)
_WbrTpRxPackets_Type = Counter32
_WbrTpRxPackets_Object = MibScalar
wbrTpRxPackets = _WbrTpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 1),
    _WbrTpRxPackets_Type()
)
wbrTpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRxPackets.setStatus("mandatory")
_WbrTpTxPackets_Type = Counter32
_WbrTpTxPackets_Object = MibScalar
wbrTpTxPackets = _WbrTpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 2),
    _WbrTpTxPackets_Type()
)
wbrTpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpTxPackets.setStatus("mandatory")
_WbrTpTxFailed_Type = Counter32
_WbrTpTxFailed_Object = MibScalar
wbrTpTxFailed = _WbrTpTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 3),
    _WbrTpTxFailed_Type()
)
wbrTpTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpTxFailed.setStatus("mandatory")
_WbrTpRxRejUnknown_Type = Counter32
_WbrTpRxRejUnknown_Object = MibScalar
wbrTpRxRejUnknown = _WbrTpRxRejUnknown_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 4),
    _WbrTpRxRejUnknown_Type()
)
wbrTpRxRejUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRxRejUnknown.setStatus("mandatory")
_WbrTpRxRejTotal_Type = Counter32
_WbrTpRxRejTotal_Object = MibScalar
wbrTpRxRejTotal = _WbrTpRxRejTotal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 5),
    _WbrTpRxRejTotal_Type()
)
wbrTpRxRejTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRxRejTotal.setStatus("mandatory")
_WbrTpRxInvalid_Type = Counter32
_WbrTpRxInvalid_Object = MibScalar
wbrTpRxInvalid = _WbrTpRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 6),
    _WbrTpRxInvalid_Type()
)
wbrTpRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRxInvalid.setStatus("mandatory")
_WbrTpRejUnicast_Type = Counter32
_WbrTpRejUnicast_Object = MibScalar
wbrTpRejUnicast = _WbrTpRejUnicast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 7),
    _WbrTpRejUnicast_Type()
)
wbrTpRejUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejUnicast.setStatus("mandatory")
_WbrTpRejDefaultUnicast_Type = Counter32
_WbrTpRejDefaultUnicast_Object = MibScalar
wbrTpRejDefaultUnicast = _WbrTpRejDefaultUnicast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 8),
    _WbrTpRejDefaultUnicast_Type()
)
wbrTpRejDefaultUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejDefaultUnicast.setStatus("mandatory")
_WbrTpRejMulticast_Type = Counter32
_WbrTpRejMulticast_Object = MibScalar
wbrTpRejMulticast = _WbrTpRejMulticast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 9),
    _WbrTpRejMulticast_Type()
)
wbrTpRejMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejMulticast.setStatus("mandatory")
_WbrTpRejDefaultMulticast_Type = Counter32
_WbrTpRejDefaultMulticast_Object = MibScalar
wbrTpRejDefaultMulticast = _WbrTpRejDefaultMulticast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 10),
    _WbrTpRejDefaultMulticast_Type()
)
wbrTpRejDefaultMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejDefaultMulticast.setStatus("mandatory")
_WbrTpRejSource_Type = Counter32
_WbrTpRejSource_Object = MibScalar
wbrTpRejSource = _WbrTpRejSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 11),
    _WbrTpRejSource_Type()
)
wbrTpRejSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejSource.setStatus("mandatory")
_WbrTpRejDefaultSource_Type = Counter32
_WbrTpRejDefaultSource_Object = MibScalar
wbrTpRejDefaultSource = _WbrTpRejDefaultSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 12),
    _WbrTpRejDefaultSource_Type()
)
wbrTpRejDefaultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejDefaultSource.setStatus("mandatory")
_WbrTpRejType_Type = Counter32
_WbrTpRejType_Object = MibScalar
wbrTpRejType = _WbrTpRejType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 13),
    _WbrTpRejType_Type()
)
wbrTpRejType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejType.setStatus("mandatory")
_WbrTpRejDefaultType_Type = Counter32
_WbrTpRejDefaultType_Object = MibScalar
wbrTpRejDefaultType = _WbrTpRejDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 14),
    _WbrTpRejDefaultType_Type()
)
wbrTpRejDefaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpRejDefaultType.setStatus("mandatory")
_WbrTpLinkTable_Object = MibTable
wbrTpLinkTable = _WbrTpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15)
)
if mibBuilder.loadTexts:
    wbrTpLinkTable.setStatus("mandatory")
_WbrTpLinkEntry_Object = MibTableRow
wbrTpLinkEntry = _WbrTpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1)
)
wbrTpLinkEntry.setIndexNames(
    (0, "INTEL-WBR-MIB", "wbrTpLinkIfIndex"),
)
if mibBuilder.loadTexts:
    wbrTpLinkEntry.setStatus("mandatory")
_WbrTpLinkIfIndex_Type = Integer32
_WbrTpLinkIfIndex_Object = MibTableColumn
wbrTpLinkIfIndex = _WbrTpLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 1),
    _WbrTpLinkIfIndex_Type()
)
wbrTpLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkIfIndex.setStatus("mandatory")
_WbrTpLinkRxOtherBytes_Type = Counter32
_WbrTpLinkRxOtherBytes_Object = MibTableColumn
wbrTpLinkRxOtherBytes = _WbrTpLinkRxOtherBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 2),
    _WbrTpLinkRxOtherBytes_Type()
)
wbrTpLinkRxOtherBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxOtherBytes.setStatus("mandatory")
_WbrTpLinkTxOtherBytes_Type = Counter32
_WbrTpLinkTxOtherBytes_Object = MibTableColumn
wbrTpLinkTxOtherBytes = _WbrTpLinkTxOtherBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 3),
    _WbrTpLinkTxOtherBytes_Type()
)
wbrTpLinkTxOtherBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkTxOtherBytes.setStatus("mandatory")
_WbrTpLinkRxRejectedBytes_Type = Counter32
_WbrTpLinkRxRejectedBytes_Object = MibTableColumn
wbrTpLinkRxRejectedBytes = _WbrTpLinkRxRejectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 4),
    _WbrTpLinkRxRejectedBytes_Type()
)
wbrTpLinkRxRejectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejectedBytes.setStatus("mandatory")
_WbrTpLinkTxRejectedBytes_Type = Counter32
_WbrTpLinkTxRejectedBytes_Object = MibTableColumn
wbrTpLinkTxRejectedBytes = _WbrTpLinkTxRejectedBytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 5),
    _WbrTpLinkTxRejectedBytes_Type()
)
wbrTpLinkTxRejectedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkTxRejectedBytes.setStatus("mandatory")
_WbrTpLinkRxRejUnknown_Type = Counter32
_WbrTpLinkRxRejUnknown_Object = MibTableColumn
wbrTpLinkRxRejUnknown = _WbrTpLinkRxRejUnknown_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 6),
    _WbrTpLinkRxRejUnknown_Type()
)
wbrTpLinkRxRejUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejUnknown.setStatus("mandatory")
_WbrTpLinkRxInvalid_Type = Counter32
_WbrTpLinkRxInvalid_Object = MibTableColumn
wbrTpLinkRxInvalid = _WbrTpLinkRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 7),
    _WbrTpLinkRxInvalid_Type()
)
wbrTpLinkRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxInvalid.setStatus("mandatory")
_WbrTpLinkTxFailed_Type = Counter32
_WbrTpLinkTxFailed_Object = MibTableColumn
wbrTpLinkTxFailed = _WbrTpLinkTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 8),
    _WbrTpLinkTxFailed_Type()
)
wbrTpLinkTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkTxFailed.setStatus("mandatory")
_WbrTpLinkRxRejUnicast_Type = Counter32
_WbrTpLinkRxRejUnicast_Object = MibTableColumn
wbrTpLinkRxRejUnicast = _WbrTpLinkRxRejUnicast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 9),
    _WbrTpLinkRxRejUnicast_Type()
)
wbrTpLinkRxRejUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejUnicast.setStatus("mandatory")
_WbrTpLinkRxRejMulticast_Type = Counter32
_WbrTpLinkRxRejMulticast_Object = MibTableColumn
wbrTpLinkRxRejMulticast = _WbrTpLinkRxRejMulticast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 10),
    _WbrTpLinkRxRejMulticast_Type()
)
wbrTpLinkRxRejMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejMulticast.setStatus("mandatory")
_WbrTpLinkRxRejSource_Type = Counter32
_WbrTpLinkRxRejSource_Object = MibTableColumn
wbrTpLinkRxRejSource = _WbrTpLinkRxRejSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 11),
    _WbrTpLinkRxRejSource_Type()
)
wbrTpLinkRxRejSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejSource.setStatus("mandatory")
_WbrTpLinkRxRejType_Type = Counter32
_WbrTpLinkRxRejType_Object = MibTableColumn
wbrTpLinkRxRejType = _WbrTpLinkRxRejType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 12),
    _WbrTpLinkRxRejType_Type()
)
wbrTpLinkRxRejType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejType.setStatus("mandatory")
_WbrTpLinkRxRejDefaultUnicast_Type = Counter32
_WbrTpLinkRxRejDefaultUnicast_Object = MibTableColumn
wbrTpLinkRxRejDefaultUnicast = _WbrTpLinkRxRejDefaultUnicast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 13),
    _WbrTpLinkRxRejDefaultUnicast_Type()
)
wbrTpLinkRxRejDefaultUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejDefaultUnicast.setStatus("mandatory")
_WbrTpLinkRxRejDefaultMulticast_Type = Counter32
_WbrTpLinkRxRejDefaultMulticast_Object = MibTableColumn
wbrTpLinkRxRejDefaultMulticast = _WbrTpLinkRxRejDefaultMulticast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 14),
    _WbrTpLinkRxRejDefaultMulticast_Type()
)
wbrTpLinkRxRejDefaultMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejDefaultMulticast.setStatus("mandatory")
_WbrTpLinkRxRejDefaultSource_Type = Counter32
_WbrTpLinkRxRejDefaultSource_Object = MibTableColumn
wbrTpLinkRxRejDefaultSource = _WbrTpLinkRxRejDefaultSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 15),
    _WbrTpLinkRxRejDefaultSource_Type()
)
wbrTpLinkRxRejDefaultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejDefaultSource.setStatus("mandatory")
_WbrTpLinkRxRejDefaultType_Type = Counter32
_WbrTpLinkRxRejDefaultType_Object = MibTableColumn
wbrTpLinkRxRejDefaultType = _WbrTpLinkRxRejDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 25, 3, 15, 1, 16),
    _WbrTpLinkRxRejDefaultType_Type()
)
wbrTpLinkRxRejDefaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wbrTpLinkRxRejDefaultType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-WBR-MIB",
    **{"wbr": wbr,
       "wbrBase": wbrBase,
       "wbrBaseLastConfigTime": wbrBaseLastConfigTime,
       "wbrBaseBridging": wbrBaseBridging,
       "wbrBaseBridgingIP": wbrBaseBridgingIP,
       "wbrBaseBridgingIPX": wbrBaseBridgingIPX,
       "wbrStp": wbrStp,
       "wbrStpBridgeAgeingTime": wbrStpBridgeAgeingTime,
       "wbrStpBridgeIsRoot": wbrStpBridgeIsRoot,
       "wbrStpRxBPDUs": wbrStpRxBPDUs,
       "wbrStpTxBPDUs": wbrStpTxBPDUs,
       "wbrStpTxBPDUsFailed": wbrStpTxBPDUsFailed,
       "wbrStpRxSpoofBPDUs": wbrStpRxSpoofBPDUs,
       "wbrStpTxSpoofBPDUs": wbrStpTxSpoofBPDUs,
       "wbrStpTxSpoofFailed": wbrStpTxSpoofFailed,
       "wbrStpTxSpoofData": wbrStpTxSpoofData,
       "wbrStpLinkTable": wbrStpLinkTable,
       "wbrStpLinkEntry": wbrStpLinkEntry,
       "wbrStpLinkIfIndex": wbrStpLinkIfIndex,
       "wbrStpLinkRxProtocolBytes": wbrStpLinkRxProtocolBytes,
       "wbrStpLinkTxProtocolBytes": wbrStpLinkTxProtocolBytes,
       "wbrStpLinkRxBPDUs": wbrStpLinkRxBPDUs,
       "wbrStpLinkTxBPDUs": wbrStpLinkTxBPDUs,
       "wbrStpLinkTxBPDUsFailed": wbrStpLinkTxBPDUsFailed,
       "wbrStpLinkRxSpoofBPDUs": wbrStpLinkRxSpoofBPDUs,
       "wbrStpLinkTxSpoofBPDUs": wbrStpLinkTxSpoofBPDUs,
       "wbrStpLinkTxSpoofFailed": wbrStpLinkTxSpoofFailed,
       "wbrStpLinkTxSpoofData": wbrStpLinkTxSpoofData,
       "wbrStpLinkSPTStatus": wbrStpLinkSPTStatus,
       "wbrStpLinkConfigBPDUPending": wbrStpLinkConfigBPDUPending,
       "wbrStpLinkTopologyChangeAck": wbrStpLinkTopologyChangeAck,
       "wbrStpLinkConfigBPDUAgeActive": wbrStpLinkConfigBPDUAgeActive,
       "wbrStpLinkConfigBPDUAge": wbrStpLinkConfigBPDUAge,
       "wbrStpLinkBPDUSpoofing": wbrStpLinkBPDUSpoofing,
       "wbrStpLinkNonBPDUSpoofing": wbrStpLinkNonBPDUSpoofing,
       "wbrStpLinkSpoofing": wbrStpLinkSpoofing,
       "wbrTp": wbrTp,
       "wbrTpRxPackets": wbrTpRxPackets,
       "wbrTpTxPackets": wbrTpTxPackets,
       "wbrTpTxFailed": wbrTpTxFailed,
       "wbrTpRxRejUnknown": wbrTpRxRejUnknown,
       "wbrTpRxRejTotal": wbrTpRxRejTotal,
       "wbrTpRxInvalid": wbrTpRxInvalid,
       "wbrTpRejUnicast": wbrTpRejUnicast,
       "wbrTpRejDefaultUnicast": wbrTpRejDefaultUnicast,
       "wbrTpRejMulticast": wbrTpRejMulticast,
       "wbrTpRejDefaultMulticast": wbrTpRejDefaultMulticast,
       "wbrTpRejSource": wbrTpRejSource,
       "wbrTpRejDefaultSource": wbrTpRejDefaultSource,
       "wbrTpRejType": wbrTpRejType,
       "wbrTpRejDefaultType": wbrTpRejDefaultType,
       "wbrTpLinkTable": wbrTpLinkTable,
       "wbrTpLinkEntry": wbrTpLinkEntry,
       "wbrTpLinkIfIndex": wbrTpLinkIfIndex,
       "wbrTpLinkRxOtherBytes": wbrTpLinkRxOtherBytes,
       "wbrTpLinkTxOtherBytes": wbrTpLinkTxOtherBytes,
       "wbrTpLinkRxRejectedBytes": wbrTpLinkRxRejectedBytes,
       "wbrTpLinkTxRejectedBytes": wbrTpLinkTxRejectedBytes,
       "wbrTpLinkRxRejUnknown": wbrTpLinkRxRejUnknown,
       "wbrTpLinkRxInvalid": wbrTpLinkRxInvalid,
       "wbrTpLinkTxFailed": wbrTpLinkTxFailed,
       "wbrTpLinkRxRejUnicast": wbrTpLinkRxRejUnicast,
       "wbrTpLinkRxRejMulticast": wbrTpLinkRxRejMulticast,
       "wbrTpLinkRxRejSource": wbrTpLinkRxRejSource,
       "wbrTpLinkRxRejType": wbrTpLinkRxRejType,
       "wbrTpLinkRxRejDefaultUnicast": wbrTpLinkRxRejDefaultUnicast,
       "wbrTpLinkRxRejDefaultMulticast": wbrTpLinkRxRejDefaultMulticast,
       "wbrTpLinkRxRejDefaultSource": wbrTpLinkRxRejDefaultSource,
       "wbrTpLinkRxRejDefaultType": wbrTpLinkRxRejDefaultType}
)
