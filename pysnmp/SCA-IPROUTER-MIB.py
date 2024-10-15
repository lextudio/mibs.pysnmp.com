# SNMP MIB module (SCA-IPROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-IPROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:52 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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

_Iprouter_ObjectIdentity = ObjectIdentity
iprouter = _Iprouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42)
)
_Conf_ObjectIdentity = ObjectIdentity
conf = _Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 1)
)
_ConfIfTable_Object = MibTable
confIfTable = _ConfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1)
)
if mibBuilder.loadTexts:
    confIfTable.setStatus("mandatory")
_ConfIfEntry_Object = MibTableRow
confIfEntry = _ConfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1)
)
confIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "confIfIndex"),
)
if mibBuilder.loadTexts:
    confIfEntry.setStatus("mandatory")
_ConfIfIndex_Type = Integer32
_ConfIfIndex_Object = MibTableColumn
confIfIndex = _ConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 1),
    _ConfIfIndex_Type()
)
confIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confIfIndex.setStatus("mandatory")


class _ConfIfAddrAndMask1_Type(OctetString):
    """Custom type confIfAddrAndMask1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConfIfAddrAndMask1_Type.__name__ = "OctetString"
_ConfIfAddrAndMask1_Object = MibTableColumn
confIfAddrAndMask1 = _ConfIfAddrAndMask1_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 2),
    _ConfIfAddrAndMask1_Type()
)
confIfAddrAndMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfAddrAndMask1.setStatus("mandatory")


class _ConfIfAddrAndMask2_Type(OctetString):
    """Custom type confIfAddrAndMask2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConfIfAddrAndMask2_Type.__name__ = "OctetString"
_ConfIfAddrAndMask2_Object = MibTableColumn
confIfAddrAndMask2 = _ConfIfAddrAndMask2_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 3),
    _ConfIfAddrAndMask2_Type()
)
confIfAddrAndMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfAddrAndMask2.setStatus("mandatory")


class _ConfIfAddrAndMask3_Type(OctetString):
    """Custom type confIfAddrAndMask3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConfIfAddrAndMask3_Type.__name__ = "OctetString"
_ConfIfAddrAndMask3_Object = MibTableColumn
confIfAddrAndMask3 = _ConfIfAddrAndMask3_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 4),
    _ConfIfAddrAndMask3_Type()
)
confIfAddrAndMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfAddrAndMask3.setStatus("mandatory")


class _ConfIfAddrAndMask4_Type(OctetString):
    """Custom type confIfAddrAndMask4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConfIfAddrAndMask4_Type.__name__ = "OctetString"
_ConfIfAddrAndMask4_Object = MibTableColumn
confIfAddrAndMask4 = _ConfIfAddrAndMask4_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 5),
    _ConfIfAddrAndMask4_Type()
)
confIfAddrAndMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfAddrAndMask4.setStatus("mandatory")


class _ConfIfRouteProto_Type(Integer32):
    """Custom type confIfRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip-1", 2),
          ("rip-2", 3))
    )


_ConfIfRouteProto_Type.__name__ = "Integer32"
_ConfIfRouteProto_Object = MibTableColumn
confIfRouteProto = _ConfIfRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 6),
    _ConfIfRouteProto_Type()
)
confIfRouteProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRouteProto.setStatus("mandatory")


class _ConfIfTrigRip_Type(Integer32):
    """Custom type confIfTrigRip based on Integer32"""
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


_ConfIfTrigRip_Type.__name__ = "Integer32"
_ConfIfTrigRip_Object = MibTableColumn
confIfTrigRip = _ConfIfTrigRip_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 7),
    _ConfIfTrigRip_Type()
)
confIfTrigRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfTrigRip.setStatus("mandatory")


class _ConfIfRipMetric_Type(Integer32):
    """Custom type confIfRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ConfIfRipMetric_Type.__name__ = "Integer32"
_ConfIfRipMetric_Object = MibTableColumn
confIfRipMetric = _ConfIfRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 8),
    _ConfIfRipMetric_Type()
)
confIfRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRipMetric.setStatus("mandatory")


class _ConfIfRip2AuthType_Type(Integer32):
    """Custom type confIfRip2AuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple-password", 2))
    )


_ConfIfRip2AuthType_Type.__name__ = "Integer32"
_ConfIfRip2AuthType_Object = MibTableColumn
confIfRip2AuthType = _ConfIfRip2AuthType_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 9),
    _ConfIfRip2AuthType_Type()
)
confIfRip2AuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRip2AuthType.setStatus("mandatory")


class _ConfIfRip2AuthKey_Type(OctetString):
    """Custom type confIfRip2AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConfIfRip2AuthKey_Type.__name__ = "OctetString"
_ConfIfRip2AuthKey_Object = MibTableColumn
confIfRip2AuthKey = _ConfIfRip2AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 10),
    _ConfIfRip2AuthKey_Type()
)
confIfRip2AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRip2AuthKey.setStatus("mandatory")


class _ConfIfBootpReqForw_Type(Integer32):
    """Custom type confIfBootpReqForw based on Integer32"""
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


_ConfIfBootpReqForw_Type.__name__ = "Integer32"
_ConfIfBootpReqForw_Object = MibTableColumn
confIfBootpReqForw = _ConfIfBootpReqForw_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 11),
    _ConfIfBootpReqForw_Type()
)
confIfBootpReqForw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfBootpReqForw.setStatus("mandatory")


class _ConfIfProxyArp_Type(Integer32):
    """Custom type confIfProxyArp based on Integer32"""
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


_ConfIfProxyArp_Type.__name__ = "Integer32"
_ConfIfProxyArp_Object = MibTableColumn
confIfProxyArp = _ConfIfProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 12),
    _ConfIfProxyArp_Type()
)
confIfProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfProxyArp.setStatus("mandatory")


class _ConfIfFiltering_Type(Integer32):
    """Custom type confIfFiltering based on Integer32"""
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


_ConfIfFiltering_Type.__name__ = "Integer32"
_ConfIfFiltering_Object = MibTableColumn
confIfFiltering = _ConfIfFiltering_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 13),
    _ConfIfFiltering_Type()
)
confIfFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfFiltering.setStatus("mandatory")


class _ConfIfRxDefAction_Type(Integer32):
    """Custom type confIfRxDefAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("pass", 2))
    )


_ConfIfRxDefAction_Type.__name__ = "Integer32"
_ConfIfRxDefAction_Object = MibTableColumn
confIfRxDefAction = _ConfIfRxDefAction_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 14),
    _ConfIfRxDefAction_Type()
)
confIfRxDefAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRxDefAction.setStatus("mandatory")


class _ConfIfTxDefAction_Type(Integer32):
    """Custom type confIfTxDefAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("pass", 2))
    )


_ConfIfTxDefAction_Type.__name__ = "Integer32"
_ConfIfTxDefAction_Object = MibTableColumn
confIfTxDefAction = _ConfIfTxDefAction_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 15),
    _ConfIfTxDefAction_Type()
)
confIfTxDefAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfTxDefAction.setStatus("mandatory")


class _ConfIfRxDefLogging_Type(Integer32):
    """Custom type confIfRxDefLogging based on Integer32"""
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


_ConfIfRxDefLogging_Type.__name__ = "Integer32"
_ConfIfRxDefLogging_Object = MibTableColumn
confIfRxDefLogging = _ConfIfRxDefLogging_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 16),
    _ConfIfRxDefLogging_Type()
)
confIfRxDefLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfRxDefLogging.setStatus("mandatory")


class _ConfIfTxDefLogging_Type(Integer32):
    """Custom type confIfTxDefLogging based on Integer32"""
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


_ConfIfTxDefLogging_Type.__name__ = "Integer32"
_ConfIfTxDefLogging_Object = MibTableColumn
confIfTxDefLogging = _ConfIfTxDefLogging_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 17),
    _ConfIfTxDefLogging_Type()
)
confIfTxDefLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfTxDefLogging.setStatus("mandatory")


class _ConfIfCreateObj_Type(OctetString):
    """Custom type confIfCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(59, 59),
    )


_ConfIfCreateObj_Type.__name__ = "OctetString"
_ConfIfCreateObj_Object = MibTableColumn
confIfCreateObj = _ConfIfCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 18),
    _ConfIfCreateObj_Type()
)
confIfCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfCreateObj.setStatus("mandatory")


class _ConfIfDeleteObj_Type(Integer32):
    """Custom type confIfDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_ConfIfDeleteObj_Type.__name__ = "Integer32"
_ConfIfDeleteObj_Object = MibTableColumn
confIfDeleteObj = _ConfIfDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 1, 1, 19),
    _ConfIfDeleteObj_Type()
)
confIfDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIfDeleteObj.setStatus("mandatory")
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1)
)
filterEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "filterIfIndex"),
    (0, "SCA-IPROUTER-MIB", "filterDirIndex"),
    (0, "SCA-IPROUTER-MIB", "filterIndex"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterIfIndex_Type = Integer32
_FilterIfIndex_Object = MibTableColumn
filterIfIndex = _FilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 1),
    _FilterIfIndex_Type()
)
filterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIfIndex.setStatus("mandatory")


class _FilterDirIndex_Type(Integer32):
    """Custom type filterDirIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_FilterDirIndex_Type.__name__ = "Integer32"
_FilterDirIndex_Object = MibTableColumn
filterDirIndex = _FilterDirIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 2),
    _FilterDirIndex_Type()
)
filterDirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterDirIndex.setStatus("mandatory")
_FilterIndex_Type = Integer32
_FilterIndex_Object = MibTableColumn
filterIndex = _FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 3),
    _FilterIndex_Type()
)
filterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIndex.setStatus("mandatory")


class _FilterAction_Type(Integer32):
    """Custom type filterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("discard", 1),
          ("pass", 2))
    )


_FilterAction_Type.__name__ = "Integer32"
_FilterAction_Object = MibTableColumn
filterAction = _FilterAction_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 4),
    _FilterAction_Type()
)
filterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterAction.setStatus("mandatory")


class _FilterLogging_Type(Integer32):
    """Custom type filterLogging based on Integer32"""
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


_FilterLogging_Type.__name__ = "Integer32"
_FilterLogging_Object = MibTableColumn
filterLogging = _FilterLogging_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 5),
    _FilterLogging_Type()
)
filterLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterLogging.setStatus("mandatory")


class _FilterProtocol_Type(Integer32):
    """Custom type filterProtocol based on Integer32"""
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
        *(("all", 1),
          ("icmp", 3),
          ("other", 2),
          ("tcp", 4),
          ("udp", 5))
    )


_FilterProtocol_Type.__name__ = "Integer32"
_FilterProtocol_Object = MibTableColumn
filterProtocol = _FilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 6),
    _FilterProtocol_Type()
)
filterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProtocol.setStatus("mandatory")


class _FilterProtocolValue_Type(Integer32):
    """Custom type filterProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FilterProtocolValue_Type.__name__ = "Integer32"
_FilterProtocolValue_Object = MibTableColumn
filterProtocolValue = _FilterProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 7),
    _FilterProtocolValue_Type()
)
filterProtocolValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProtocolValue.setStatus("mandatory")


class _FilterTcpFlags_Type(Integer32):
    """Custom type filterTcpFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ack", 2),
          ("all", 1))
    )


_FilterTcpFlags_Type.__name__ = "Integer32"
_FilterTcpFlags_Object = MibTableColumn
filterTcpFlags = _FilterTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 8),
    _FilterTcpFlags_Type()
)
filterTcpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTcpFlags.setStatus("mandatory")


class _FilterSrcAddrType_Type(Integer32):
    """Custom type filterSrcAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 3),
          ("network", 2))
    )


_FilterSrcAddrType_Type.__name__ = "Integer32"
_FilterSrcAddrType_Object = MibTableColumn
filterSrcAddrType = _FilterSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 9),
    _FilterSrcAddrType_Type()
)
filterSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcAddrType.setStatus("mandatory")
_FilterSrcAddr_Type = IpAddress
_FilterSrcAddr_Object = MibTableColumn
filterSrcAddr = _FilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 10),
    _FilterSrcAddr_Type()
)
filterSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcAddr.setStatus("mandatory")
_FilterSrcMask_Type = IpAddress
_FilterSrcMask_Object = MibTableColumn
filterSrcMask = _FilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 11),
    _FilterSrcMask_Type()
)
filterSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcMask.setStatus("mandatory")


class _FilterSrcPort_Type(Integer32):
    """Custom type filterSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              20,
              21,
              23,
              25,
              53,
              67,
              68,
              69,
              70,
              80,
              161,
              162,
              520,
              2049)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bootp-client", 68),
          ("bootp-server", 67),
          ("dns", 53),
          ("ftp-control", 21),
          ("ftp-data", 20),
          ("gopher", 70),
          ("nfs", 2049),
          ("other", 2),
          ("rip", 520),
          ("smtp", 25),
          ("snmp", 161),
          ("snmp-trap", 162),
          ("telnet", 23),
          ("tftp", 69),
          ("www", 80))
    )


_FilterSrcPort_Type.__name__ = "Integer32"
_FilterSrcPort_Object = MibTableColumn
filterSrcPort = _FilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 12),
    _FilterSrcPort_Type()
)
filterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcPort.setStatus("mandatory")


class _FilterSrcPortValue_Type(Integer32):
    """Custom type filterSrcPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterSrcPortValue_Type.__name__ = "Integer32"
_FilterSrcPortValue_Object = MibTableColumn
filterSrcPortValue = _FilterSrcPortValue_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 13),
    _FilterSrcPortValue_Type()
)
filterSrcPortValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcPortValue.setStatus("mandatory")


class _FilterSrcPortOper_Type(Integer32):
    """Custom type filterSrcPortOper based on Integer32"""
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
        *(("equal-to", 1),
          ("greater-than", 3),
          ("less-than", 4),
          ("not-equal-to", 2))
    )


_FilterSrcPortOper_Type.__name__ = "Integer32"
_FilterSrcPortOper_Object = MibTableColumn
filterSrcPortOper = _FilterSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 14),
    _FilterSrcPortOper_Type()
)
filterSrcPortOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcPortOper.setStatus("mandatory")


class _FilterDestAddrType_Type(Integer32):
    """Custom type filterDestAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("host", 3),
          ("network", 2))
    )


_FilterDestAddrType_Type.__name__ = "Integer32"
_FilterDestAddrType_Object = MibTableColumn
filterDestAddrType = _FilterDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 15),
    _FilterDestAddrType_Type()
)
filterDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestAddrType.setStatus("mandatory")
_FilterDestAddr_Type = IpAddress
_FilterDestAddr_Object = MibTableColumn
filterDestAddr = _FilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 16),
    _FilterDestAddr_Type()
)
filterDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestAddr.setStatus("mandatory")
_FilterDestMask_Type = IpAddress
_FilterDestMask_Object = MibTableColumn
filterDestMask = _FilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 17),
    _FilterDestMask_Type()
)
filterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestMask.setStatus("mandatory")


class _FilterDestPort_Type(Integer32):
    """Custom type filterDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              20,
              21,
              23,
              25,
              53,
              67,
              68,
              69,
              70,
              80,
              161,
              162,
              520,
              2049)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bootp-client", 68),
          ("bootp-server", 67),
          ("dns", 53),
          ("ftp-control", 21),
          ("ftp-data", 20),
          ("gopher", 70),
          ("nfs", 2049),
          ("other", 2),
          ("rip", 520),
          ("smtp", 25),
          ("snmp", 161),
          ("snmp-trap", 162),
          ("telnet", 23),
          ("tftp", 69),
          ("www", 80))
    )


_FilterDestPort_Type.__name__ = "Integer32"
_FilterDestPort_Object = MibTableColumn
filterDestPort = _FilterDestPort_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 18),
    _FilterDestPort_Type()
)
filterDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestPort.setStatus("mandatory")


class _FilterDestPortValue_Type(Integer32):
    """Custom type filterDestPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterDestPortValue_Type.__name__ = "Integer32"
_FilterDestPortValue_Object = MibTableColumn
filterDestPortValue = _FilterDestPortValue_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 19),
    _FilterDestPortValue_Type()
)
filterDestPortValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestPortValue.setStatus("mandatory")


class _FilterDestPortOper_Type(Integer32):
    """Custom type filterDestPortOper based on Integer32"""
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
        *(("equal-to", 1),
          ("greater-than", 3),
          ("less-than", 4),
          ("not-equal-to", 2))
    )


_FilterDestPortOper_Type.__name__ = "Integer32"
_FilterDestPortOper_Object = MibTableColumn
filterDestPortOper = _FilterDestPortOper_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 20),
    _FilterDestPortOper_Type()
)
filterDestPortOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestPortOper.setStatus("mandatory")
_FilterHits_Type = Counter32
_FilterHits_Object = MibTableColumn
filterHits = _FilterHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 2, 1, 21),
    _FilterHits_Type()
)
filterHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterHits.setStatus("mandatory")
_NatTable_Object = MibTable
natTable = _NatTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3)
)
if mibBuilder.loadTexts:
    natTable.setStatus("mandatory")
_NatEntry_Object = MibTableRow
natEntry = _NatEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1)
)
natEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "natIfIndex"),
    (0, "SCA-IPROUTER-MIB", "natIndex"),
)
if mibBuilder.loadTexts:
    natEntry.setStatus("mandatory")
_NatIfIndex_Type = Integer32
_NatIfIndex_Object = MibTableColumn
natIfIndex = _NatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 1),
    _NatIfIndex_Type()
)
natIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIfIndex.setStatus("mandatory")
_NatIndex_Type = Integer32
_NatIndex_Object = MibTableColumn
natIndex = _NatIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 2),
    _NatIndex_Type()
)
natIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIndex.setStatus("mandatory")
_NatIntAddr_Type = IpAddress
_NatIntAddr_Object = MibTableColumn
natIntAddr = _NatIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 3),
    _NatIntAddr_Type()
)
natIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIntAddr.setStatus("mandatory")
_NatIntMask_Type = IpAddress
_NatIntMask_Object = MibTableColumn
natIntMask = _NatIntMask_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 4),
    _NatIntMask_Type()
)
natIntMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natIntMask.setStatus("mandatory")
_NatExtAddr_Type = IpAddress
_NatExtAddr_Object = MibTableColumn
natExtAddr = _NatExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 5),
    _NatExtAddr_Type()
)
natExtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natExtAddr.setStatus("mandatory")
_NatExtMask_Type = IpAddress
_NatExtMask_Object = MibTableColumn
natExtMask = _NatExtMask_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 6),
    _NatExtMask_Type()
)
natExtMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natExtMask.setStatus("mandatory")


class _NatType_Type(Integer32):
    """Custom type natType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_NatType_Type.__name__ = "Integer32"
_NatType_Object = MibTableColumn
natType = _NatType_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 7),
    _NatType_Type()
)
natType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natType.setStatus("mandatory")


class _NatAuto_Type(Integer32):
    """Custom type natAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NatAuto_Type.__name__ = "Integer32"
_NatAuto_Object = MibTableColumn
natAuto = _NatAuto_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 8),
    _NatAuto_Type()
)
natAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natAuto.setStatus("mandatory")
_NatTime_Type = Integer32
_NatTime_Object = MibTableColumn
natTime = _NatTime_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 3, 1, 9),
    _NatTime_Type()
)
natTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natTime.setStatus("mandatory")
_StatRoutTable_Object = MibTable
statRoutTable = _StatRoutTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4)
)
if mibBuilder.loadTexts:
    statRoutTable.setStatus("mandatory")
_StatRoutEntry_Object = MibTableRow
statRoutEntry = _StatRoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1)
)
statRoutEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "statRoutIfIndex"),
    (0, "SCA-IPROUTER-MIB", "statRoutNetwork"),
)
if mibBuilder.loadTexts:
    statRoutEntry.setStatus("mandatory")
_StatRoutIfIndex_Type = Integer32
_StatRoutIfIndex_Object = MibTableColumn
statRoutIfIndex = _StatRoutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 1),
    _StatRoutIfIndex_Type()
)
statRoutIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutIfIndex.setStatus("mandatory")
_StatRoutNetwork_Type = IpAddress
_StatRoutNetwork_Object = MibTableColumn
statRoutNetwork = _StatRoutNetwork_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 2),
    _StatRoutNetwork_Type()
)
statRoutNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutNetwork.setStatus("mandatory")
_StatRoutMask_Type = IpAddress
_StatRoutMask_Object = MibTableColumn
statRoutMask = _StatRoutMask_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 3),
    _StatRoutMask_Type()
)
statRoutMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutMask.setStatus("mandatory")
_StatRoutNextHop_Type = IpAddress
_StatRoutNextHop_Object = MibTableColumn
statRoutNextHop = _StatRoutNextHop_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 4),
    _StatRoutNextHop_Type()
)
statRoutNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutNextHop.setStatus("mandatory")
_StatRoutMetric_Type = Integer32
_StatRoutMetric_Object = MibTableColumn
statRoutMetric = _StatRoutMetric_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 5),
    _StatRoutMetric_Type()
)
statRoutMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutMetric.setStatus("mandatory")


class _StatRoutCreateObj_Type(OctetString):
    """Custom type statRoutCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_StatRoutCreateObj_Type.__name__ = "OctetString"
_StatRoutCreateObj_Object = MibTableColumn
statRoutCreateObj = _StatRoutCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 6),
    _StatRoutCreateObj_Type()
)
statRoutCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutCreateObj.setStatus("mandatory")


class _StatRoutDeleteObj_Type(Integer32):
    """Custom type statRoutDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_StatRoutDeleteObj_Type.__name__ = "Integer32"
_StatRoutDeleteObj_Object = MibTableColumn
statRoutDeleteObj = _StatRoutDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 1, 4, 1, 7),
    _StatRoutDeleteObj_Type()
)
statRoutDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statRoutDeleteObj.setStatus("mandatory")
_Stat_ObjectIdentity = ObjectIdentity
stat = _Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 2)
)
_StatIfTable_Object = MibTable
statIfTable = _StatIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1)
)
if mibBuilder.loadTexts:
    statIfTable.setStatus("mandatory")
_StatIfEntry_Object = MibTableRow
statIfEntry = _StatIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1)
)
statIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "statIfIndex"),
)
if mibBuilder.loadTexts:
    statIfEntry.setStatus("mandatory")
_StatIfIndex_Type = Integer32
_StatIfIndex_Object = MibTableColumn
statIfIndex = _StatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1, 1),
    _StatIfIndex_Type()
)
statIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfIndex.setStatus("mandatory")


class _StatIfType_Type(Integer32):
    """Custom type statIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_StatIfType_Type.__name__ = "Integer32"
_StatIfType_Object = MibTableColumn
statIfType = _StatIfType_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1, 2),
    _StatIfType_Type()
)
statIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfType.setStatus("mandatory")


class _StatIfState_Type(Integer32):
    """Custom type statIfState based on Integer32"""
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


_StatIfState_Type.__name__ = "Integer32"
_StatIfState_Object = MibTableColumn
statIfState = _StatIfState_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1, 3),
    _StatIfState_Type()
)
statIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfState.setStatus("mandatory")
_StatIfMTU_Type = Integer32
_StatIfMTU_Object = MibTableColumn
statIfMTU = _StatIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1, 4),
    _StatIfMTU_Type()
)
statIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfMTU.setStatus("mandatory")
_StatIfRxDefHits_Type = Counter32
_StatIfRxDefHits_Object = MibTableColumn
statIfRxDefHits = _StatIfRxDefHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1, 5),
    _StatIfRxDefHits_Type()
)
statIfRxDefHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfRxDefHits.setStatus("mandatory")
_StatIfTxDefHits_Type = Counter32
_StatIfTxDefHits_Object = MibTableColumn
statIfTxDefHits = _StatIfTxDefHits_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 2, 1, 1, 6),
    _StatIfTxDefHits_Type()
)
statIfTxDefHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfTxDefHits.setStatus("mandatory")
_Arp_ObjectIdentity = ObjectIdentity
arp = _Arp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 3)
)
_ArpIfTable_Object = MibTable
arpIfTable = _ArpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1)
)
if mibBuilder.loadTexts:
    arpIfTable.setStatus("mandatory")
_ArpIfEntry_Object = MibTableRow
arpIfEntry = _ArpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1)
)
arpIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "arpIfIndex"),
)
if mibBuilder.loadTexts:
    arpIfEntry.setStatus("mandatory")
_ArpIfIndex_Type = Integer32
_ArpIfIndex_Object = MibTableColumn
arpIfIndex = _ArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1, 1),
    _ArpIfIndex_Type()
)
arpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIfIndex.setStatus("mandatory")
_ArpIfInReq_Type = Counter32
_ArpIfInReq_Object = MibTableColumn
arpIfInReq = _ArpIfInReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1, 2),
    _ArpIfInReq_Type()
)
arpIfInReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIfInReq.setStatus("mandatory")
_ArpIfOutRep_Type = Counter32
_ArpIfOutRep_Object = MibTableColumn
arpIfOutRep = _ArpIfOutRep_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1, 3),
    _ArpIfOutRep_Type()
)
arpIfOutRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIfOutRep.setStatus("mandatory")
_ArpIfOutReq_Type = Counter32
_ArpIfOutReq_Object = MibTableColumn
arpIfOutReq = _ArpIfOutReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1, 4),
    _ArpIfOutReq_Type()
)
arpIfOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIfOutReq.setStatus("mandatory")
_ArpIfInRep_Type = Counter32
_ArpIfInRep_Object = MibTableColumn
arpIfInRep = _ArpIfInRep_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1, 5),
    _ArpIfInRep_Type()
)
arpIfInRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIfInRep.setStatus("mandatory")
_ArpIfInHdrErrors_Type = Counter32
_ArpIfInHdrErrors_Object = MibTableColumn
arpIfInHdrErrors = _ArpIfInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 1, 1, 6),
    _ArpIfInHdrErrors_Type()
)
arpIfInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIfInHdrErrors.setStatus("mandatory")
_ArpInReq_Type = Counter32
_ArpInReq_Object = MibScalar
arpInReq = _ArpInReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 2),
    _ArpInReq_Type()
)
arpInReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInReq.setStatus("mandatory")
_ArpOutRep_Type = Counter32
_ArpOutRep_Object = MibScalar
arpOutRep = _ArpOutRep_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 3),
    _ArpOutRep_Type()
)
arpOutRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpOutRep.setStatus("mandatory")
_ArpOutReq_Type = Counter32
_ArpOutReq_Object = MibScalar
arpOutReq = _ArpOutReq_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 4),
    _ArpOutReq_Type()
)
arpOutReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpOutReq.setStatus("mandatory")
_ArpInRep_Type = Counter32
_ArpInRep_Object = MibScalar
arpInRep = _ArpInRep_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 5),
    _ArpInRep_Type()
)
arpInRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInRep.setStatus("mandatory")
_ArpInHdrErrors_Type = Counter32
_ArpInHdrErrors_Object = MibScalar
arpInHdrErrors = _ArpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 3, 6),
    _ArpInHdrErrors_Type()
)
arpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInHdrErrors.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 4)
)
_IpIfTable_Object = MibTable
ipIfTable = _IpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1)
)
if mibBuilder.loadTexts:
    ipIfTable.setStatus("mandatory")
_IpIfEntry_Object = MibTableRow
ipIfEntry = _IpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1)
)
ipIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "ipIfIndex"),
)
if mibBuilder.loadTexts:
    ipIfEntry.setStatus("mandatory")
_IpIfIndex_Type = Integer32
_IpIfIndex_Object = MibTableColumn
ipIfIndex = _IpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 1),
    _IpIfIndex_Type()
)
ipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfIndex.setStatus("mandatory")
_IpIfInReceives_Type = Counter32
_IpIfInReceives_Object = MibTableColumn
ipIfInReceives = _IpIfInReceives_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 2),
    _IpIfInReceives_Type()
)
ipIfInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfInReceives.setStatus("mandatory")
_IpIfInHdrErrors_Type = Counter32
_IpIfInHdrErrors_Object = MibTableColumn
ipIfInHdrErrors = _IpIfInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 3),
    _IpIfInHdrErrors_Type()
)
ipIfInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfInHdrErrors.setStatus("mandatory")
_IpIfInAddrErrors_Type = Counter32
_IpIfInAddrErrors_Object = MibTableColumn
ipIfInAddrErrors = _IpIfInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 4),
    _IpIfInAddrErrors_Type()
)
ipIfInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfInAddrErrors.setStatus("mandatory")
_IpIfInDiscards_Type = Counter32
_IpIfInDiscards_Object = MibTableColumn
ipIfInDiscards = _IpIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 5),
    _IpIfInDiscards_Type()
)
ipIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfInDiscards.setStatus("mandatory")
_IpIfForwDatagrams_Type = Counter32
_IpIfForwDatagrams_Object = MibTableColumn
ipIfForwDatagrams = _IpIfForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 6),
    _IpIfForwDatagrams_Type()
)
ipIfForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfForwDatagrams.setStatus("mandatory")
_IpIfOutRequests_Type = Counter32
_IpIfOutRequests_Object = MibTableColumn
ipIfOutRequests = _IpIfOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 7),
    _IpIfOutRequests_Type()
)
ipIfOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfOutRequests.setStatus("mandatory")
_IpIfOutDiscards_Type = Counter32
_IpIfOutDiscards_Object = MibTableColumn
ipIfOutDiscards = _IpIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 4, 1, 1, 8),
    _IpIfOutDiscards_Type()
)
ipIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfOutDiscards.setStatus("mandatory")
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 5)
)
_IcmpIfTable_Object = MibTable
icmpIfTable = _IcmpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1)
)
if mibBuilder.loadTexts:
    icmpIfTable.setStatus("mandatory")
_IcmpIfEntry_Object = MibTableRow
icmpIfEntry = _IcmpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1)
)
icmpIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "icmpIfIndex"),
)
if mibBuilder.loadTexts:
    icmpIfEntry.setStatus("mandatory")
_IcmpIfIndex_Type = Integer32
_IcmpIfIndex_Object = MibTableColumn
icmpIfIndex = _IcmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 1),
    _IcmpIfIndex_Type()
)
icmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfIndex.setStatus("mandatory")
_IcmpIfInMsgs_Type = Counter32
_IcmpIfInMsgs_Object = MibTableColumn
icmpIfInMsgs = _IcmpIfInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 2),
    _IcmpIfInMsgs_Type()
)
icmpIfInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfInMsgs.setStatus("mandatory")
_IcmpIfInErrors_Type = Counter32
_IcmpIfInErrors_Object = MibTableColumn
icmpIfInErrors = _IcmpIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 3),
    _IcmpIfInErrors_Type()
)
icmpIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfInErrors.setStatus("mandatory")
_IcmpIfInEchos_Type = Counter32
_IcmpIfInEchos_Object = MibTableColumn
icmpIfInEchos = _IcmpIfInEchos_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 4),
    _IcmpIfInEchos_Type()
)
icmpIfInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfInEchos.setStatus("mandatory")
_IcmpIfInEchoReps_Type = Counter32
_IcmpIfInEchoReps_Object = MibTableColumn
icmpIfInEchoReps = _IcmpIfInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 5),
    _IcmpIfInEchoReps_Type()
)
icmpIfInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfInEchoReps.setStatus("mandatory")
_IcmpIfOutMsgs_Type = Counter32
_IcmpIfOutMsgs_Object = MibTableColumn
icmpIfOutMsgs = _IcmpIfOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 6),
    _IcmpIfOutMsgs_Type()
)
icmpIfOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfOutMsgs.setStatus("mandatory")
_IcmpIfOutEchos_Type = Counter32
_IcmpIfOutEchos_Object = MibTableColumn
icmpIfOutEchos = _IcmpIfOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 7),
    _IcmpIfOutEchos_Type()
)
icmpIfOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfOutEchos.setStatus("mandatory")
_IcmpIfOutEchoReps_Type = Counter32
_IcmpIfOutEchoReps_Object = MibTableColumn
icmpIfOutEchoReps = _IcmpIfOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 1, 1, 8),
    _IcmpIfOutEchoReps_Type()
)
icmpIfOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpIfOutEchoReps.setStatus("mandatory")
_IcmpInRouterAdvs_Type = Counter32
_IcmpInRouterAdvs_Object = MibScalar
icmpInRouterAdvs = _IcmpInRouterAdvs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 2),
    _IcmpInRouterAdvs_Type()
)
icmpInRouterAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInRouterAdvs.setStatus("mandatory")
_IcmpInRouterSols_Type = Counter32
_IcmpInRouterSols_Object = MibScalar
icmpInRouterSols = _IcmpInRouterSols_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 3),
    _IcmpInRouterSols_Type()
)
icmpInRouterSols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInRouterSols.setStatus("mandatory")
_IcmpOutRouterAdvs_Type = Counter32
_IcmpOutRouterAdvs_Object = MibScalar
icmpOutRouterAdvs = _IcmpOutRouterAdvs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 4),
    _IcmpOutRouterAdvs_Type()
)
icmpOutRouterAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutRouterAdvs.setStatus("mandatory")
_IcmpOutRouterSols_Type = Counter32
_IcmpOutRouterSols_Object = MibScalar
icmpOutRouterSols = _IcmpOutRouterSols_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 5, 5),
    _IcmpOutRouterSols_Type()
)
icmpOutRouterSols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutRouterSols.setStatus("mandatory")
_Rip_ObjectIdentity = ObjectIdentity
rip = _Rip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 6)
)
_RipIfTable_Object = MibTable
ripIfTable = _RipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1)
)
if mibBuilder.loadTexts:
    ripIfTable.setStatus("mandatory")
_RipIfEntry_Object = MibTableRow
ripIfEntry = _RipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1)
)
ripIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "ripIfIndex"),
)
if mibBuilder.loadTexts:
    ripIfEntry.setStatus("mandatory")
_RipIfIndex_Type = Integer32
_RipIfIndex_Object = MibTableColumn
ripIfIndex = _RipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 1),
    _RipIfIndex_Type()
)
ripIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfIndex.setStatus("mandatory")
_RipIfInReceives_Type = Counter32
_RipIfInReceives_Object = MibTableColumn
ripIfInReceives = _RipIfInReceives_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 2),
    _RipIfInReceives_Type()
)
ripIfInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInReceives.setStatus("mandatory")
_RipIfInHdrErrors_Type = Counter32
_RipIfInHdrErrors_Object = MibTableColumn
ripIfInHdrErrors = _RipIfInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 3),
    _RipIfInHdrErrors_Type()
)
ripIfInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInHdrErrors.setStatus("mandatory")
_RipIfInBadSrcAddrs_Type = Counter32
_RipIfInBadSrcAddrs_Object = MibTableColumn
ripIfInBadSrcAddrs = _RipIfInBadSrcAddrs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 4),
    _RipIfInBadSrcAddrs_Type()
)
ripIfInBadSrcAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInBadSrcAddrs.setStatus("mandatory")
_RipIfInBadVers_Type = Counter32
_RipIfInBadVers_Object = MibTableColumn
ripIfInBadVers = _RipIfInBadVers_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 5),
    _RipIfInBadVers_Type()
)
ripIfInBadVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInBadVers.setStatus("mandatory")
_RipIfInAuthFails_Type = Counter32
_RipIfInAuthFails_Object = MibTableColumn
ripIfInAuthFails = _RipIfInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 6),
    _RipIfInAuthFails_Type()
)
ripIfInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInAuthFails.setStatus("mandatory")
_RipIfInUnknComs_Type = Counter32
_RipIfInUnknComs_Object = MibTableColumn
ripIfInUnknComs = _RipIfInUnknComs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 7),
    _RipIfInUnknComs_Type()
)
ripIfInUnknComs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfInUnknComs.setStatus("mandatory")
_RipIfOutSent_Type = Counter32
_RipIfOutSent_Object = MibTableColumn
ripIfOutSent = _RipIfOutSent_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 8),
    _RipIfOutSent_Type()
)
ripIfOutSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfOutSent.setStatus("mandatory")
_RipIfOutDiscards_Type = Counter32
_RipIfOutDiscards_Object = MibTableColumn
ripIfOutDiscards = _RipIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 1, 1, 9),
    _RipIfOutDiscards_Type()
)
ripIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripIfOutDiscards.setStatus("mandatory")
_RipInReceives_Type = Counter32
_RipInReceives_Object = MibScalar
ripInReceives = _RipInReceives_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 2),
    _RipInReceives_Type()
)
ripInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInReceives.setStatus("mandatory")
_RipInHdrErrors_Type = Counter32
_RipInHdrErrors_Object = MibScalar
ripInHdrErrors = _RipInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 3),
    _RipInHdrErrors_Type()
)
ripInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInHdrErrors.setStatus("mandatory")
_RipInBadSrcAddrs_Type = Counter32
_RipInBadSrcAddrs_Object = MibScalar
ripInBadSrcAddrs = _RipInBadSrcAddrs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 4),
    _RipInBadSrcAddrs_Type()
)
ripInBadSrcAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInBadSrcAddrs.setStatus("mandatory")
_RipInBadVers_Type = Counter32
_RipInBadVers_Object = MibScalar
ripInBadVers = _RipInBadVers_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 5),
    _RipInBadVers_Type()
)
ripInBadVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInBadVers.setStatus("mandatory")
_RipInAuthFails_Type = Counter32
_RipInAuthFails_Object = MibScalar
ripInAuthFails = _RipInAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 6),
    _RipInAuthFails_Type()
)
ripInAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInAuthFails.setStatus("mandatory")
_RipInUnknComs_Type = Counter32
_RipInUnknComs_Object = MibScalar
ripInUnknComs = _RipInUnknComs_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 7),
    _RipInUnknComs_Type()
)
ripInUnknComs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInUnknComs.setStatus("mandatory")
_RipOutSent_Type = Counter32
_RipOutSent_Object = MibScalar
ripOutSent = _RipOutSent_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 8),
    _RipOutSent_Type()
)
ripOutSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripOutSent.setStatus("mandatory")
_RipOutDiscards_Type = Counter32
_RipOutDiscards_Object = MibScalar
ripOutDiscards = _RipOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 6, 9),
    _RipOutDiscards_Type()
)
ripOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripOutDiscards.setStatus("mandatory")
_Bootp_ObjectIdentity = ObjectIdentity
bootp = _Bootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 7)
)
_BootpIfTable_Object = MibTable
bootpIfTable = _BootpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1)
)
if mibBuilder.loadTexts:
    bootpIfTable.setStatus("mandatory")
_BootpIfEntry_Object = MibTableRow
bootpIfEntry = _BootpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1)
)
bootpIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "bootpIfIndex"),
)
if mibBuilder.loadTexts:
    bootpIfEntry.setStatus("mandatory")
_BootpIfIndex_Type = Integer32
_BootpIfIndex_Object = MibTableColumn
bootpIfIndex = _BootpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 1),
    _BootpIfIndex_Type()
)
bootpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfIndex.setStatus("mandatory")
_BootpIfInRequests_Type = Counter32
_BootpIfInRequests_Object = MibTableColumn
bootpIfInRequests = _BootpIfInRequests_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 2),
    _BootpIfInRequests_Type()
)
bootpIfInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfInRequests.setStatus("mandatory")
_BootpIfInReplies_Type = Counter32
_BootpIfInReplies_Object = MibTableColumn
bootpIfInReplies = _BootpIfInReplies_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 3),
    _BootpIfInReplies_Type()
)
bootpIfInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfInReplies.setStatus("mandatory")
_BootpIfInErrors_Type = Counter32
_BootpIfInErrors_Object = MibTableColumn
bootpIfInErrors = _BootpIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 4),
    _BootpIfInErrors_Type()
)
bootpIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfInErrors.setStatus("mandatory")
_BootpIfInDiscards_Type = Counter32
_BootpIfInDiscards_Object = MibTableColumn
bootpIfInDiscards = _BootpIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 5),
    _BootpIfInDiscards_Type()
)
bootpIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfInDiscards.setStatus("mandatory")
_BootpIfOutRequests_Type = Counter32
_BootpIfOutRequests_Object = MibTableColumn
bootpIfOutRequests = _BootpIfOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 6),
    _BootpIfOutRequests_Type()
)
bootpIfOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfOutRequests.setStatus("mandatory")
_BootpIfOutReplies_Type = Counter32
_BootpIfOutReplies_Object = MibTableColumn
bootpIfOutReplies = _BootpIfOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 7),
    _BootpIfOutReplies_Type()
)
bootpIfOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfOutReplies.setStatus("mandatory")
_BootpIfOutDiscards_Type = Counter32
_BootpIfOutDiscards_Object = MibTableColumn
bootpIfOutDiscards = _BootpIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 1, 1, 8),
    _BootpIfOutDiscards_Type()
)
bootpIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpIfOutDiscards.setStatus("mandatory")
_BootpInRequests_Type = Counter32
_BootpInRequests_Object = MibScalar
bootpInRequests = _BootpInRequests_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 2),
    _BootpInRequests_Type()
)
bootpInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpInRequests.setStatus("mandatory")
_BootpInReplies_Type = Counter32
_BootpInReplies_Object = MibScalar
bootpInReplies = _BootpInReplies_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 3),
    _BootpInReplies_Type()
)
bootpInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpInReplies.setStatus("mandatory")
_BootpInErrors_Type = Counter32
_BootpInErrors_Object = MibScalar
bootpInErrors = _BootpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 4),
    _BootpInErrors_Type()
)
bootpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpInErrors.setStatus("mandatory")
_BootpInDiscards_Type = Counter32
_BootpInDiscards_Object = MibScalar
bootpInDiscards = _BootpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 5),
    _BootpInDiscards_Type()
)
bootpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpInDiscards.setStatus("mandatory")
_BootpOutRequests_Type = Counter32
_BootpOutRequests_Object = MibScalar
bootpOutRequests = _BootpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 6),
    _BootpOutRequests_Type()
)
bootpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpOutRequests.setStatus("mandatory")
_BootpOutReplies_Type = Counter32
_BootpOutReplies_Object = MibScalar
bootpOutReplies = _BootpOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 7),
    _BootpOutReplies_Type()
)
bootpOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpOutReplies.setStatus("mandatory")
_BootpOutDiscards_Type = Counter32
_BootpOutDiscards_Object = MibScalar
bootpOutDiscards = _BootpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 8),
    _BootpOutDiscards_Type()
)
bootpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootpOutDiscards.setStatus("mandatory")
_BootpMaxHops_Type = Integer32
_BootpMaxHops_Object = MibScalar
bootpMaxHops = _BootpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 7, 9),
    _BootpMaxHops_Type()
)
bootpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpMaxHops.setStatus("mandatory")
_Octetcounters_ObjectIdentity = ObjectIdentity
octetcounters = _Octetcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 42, 8)
)
_OctetIfTable_Object = MibTable
octetIfTable = _OctetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1)
)
if mibBuilder.loadTexts:
    octetIfTable.setStatus("mandatory")
_OctetIfEntry_Object = MibTableRow
octetIfEntry = _OctetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1)
)
octetIfEntry.setIndexNames(
    (0, "SCA-IPROUTER-MIB", "octetIfIndex"),
)
if mibBuilder.loadTexts:
    octetIfEntry.setStatus("mandatory")
_OctetIfIndex_Type = Integer32
_OctetIfIndex_Object = MibTableColumn
octetIfIndex = _OctetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 1),
    _OctetIfIndex_Type()
)
octetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfIndex.setStatus("mandatory")
_OctetIfInTotal_Type = Counter32
_OctetIfInTotal_Object = MibTableColumn
octetIfInTotal = _OctetIfInTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 2),
    _OctetIfInTotal_Type()
)
octetIfInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInTotal.setStatus("mandatory")
_OctetIfOutTotal_Type = Counter32
_OctetIfOutTotal_Object = MibTableColumn
octetIfOutTotal = _OctetIfOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 3),
    _OctetIfOutTotal_Type()
)
octetIfOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutTotal.setStatus("mandatory")
_OctetIfInOther_Type = Counter32
_OctetIfInOther_Object = MibTableColumn
octetIfInOther = _OctetIfInOther_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 4),
    _OctetIfInOther_Type()
)
octetIfInOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInOther.setStatus("mandatory")
_OctetIfOutOther_Type = Counter32
_OctetIfOutOther_Object = MibTableColumn
octetIfOutOther = _OctetIfOutOther_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 5),
    _OctetIfOutOther_Type()
)
octetIfOutOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutOther.setStatus("mandatory")
_OctetIfInFtp_Type = Counter32
_OctetIfInFtp_Object = MibTableColumn
octetIfInFtp = _OctetIfInFtp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 6),
    _OctetIfInFtp_Type()
)
octetIfInFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInFtp.setStatus("mandatory")
_OctetIfOutFtp_Type = Counter32
_OctetIfOutFtp_Object = MibTableColumn
octetIfOutFtp = _OctetIfOutFtp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 7),
    _OctetIfOutFtp_Type()
)
octetIfOutFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutFtp.setStatus("mandatory")
_OctetIfInTelnet_Type = Counter32
_OctetIfInTelnet_Object = MibTableColumn
octetIfInTelnet = _OctetIfInTelnet_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 8),
    _OctetIfInTelnet_Type()
)
octetIfInTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInTelnet.setStatus("mandatory")
_OctetIfOutTelnet_Type = Counter32
_OctetIfOutTelnet_Object = MibTableColumn
octetIfOutTelnet = _OctetIfOutTelnet_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 9),
    _OctetIfOutTelnet_Type()
)
octetIfOutTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutTelnet.setStatus("mandatory")
_OctetIfInSmtp_Type = Counter32
_OctetIfInSmtp_Object = MibTableColumn
octetIfInSmtp = _OctetIfInSmtp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 10),
    _OctetIfInSmtp_Type()
)
octetIfInSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInSmtp.setStatus("mandatory")
_OctetIfOutSmtp_Type = Counter32
_OctetIfOutSmtp_Object = MibTableColumn
octetIfOutSmtp = _OctetIfOutSmtp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 11),
    _OctetIfOutSmtp_Type()
)
octetIfOutSmtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutSmtp.setStatus("mandatory")
_OctetIfInDns_Type = Counter32
_OctetIfInDns_Object = MibTableColumn
octetIfInDns = _OctetIfInDns_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 12),
    _OctetIfInDns_Type()
)
octetIfInDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInDns.setStatus("mandatory")
_OctetIfOutDns_Type = Counter32
_OctetIfOutDns_Object = MibTableColumn
octetIfOutDns = _OctetIfOutDns_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 13),
    _OctetIfOutDns_Type()
)
octetIfOutDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutDns.setStatus("mandatory")
_OctetIfInBootp_Type = Counter32
_OctetIfInBootp_Object = MibTableColumn
octetIfInBootp = _OctetIfInBootp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 14),
    _OctetIfInBootp_Type()
)
octetIfInBootp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInBootp.setStatus("mandatory")
_OctetIfOutBootp_Type = Counter32
_OctetIfOutBootp_Object = MibTableColumn
octetIfOutBootp = _OctetIfOutBootp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 15),
    _OctetIfOutBootp_Type()
)
octetIfOutBootp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutBootp.setStatus("mandatory")
_OctetIfInHttp_Type = Counter32
_OctetIfInHttp_Object = MibTableColumn
octetIfInHttp = _OctetIfInHttp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 16),
    _OctetIfInHttp_Type()
)
octetIfInHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInHttp.setStatus("mandatory")
_OctetIfOutHttp_Type = Counter32
_OctetIfOutHttp_Object = MibTableColumn
octetIfOutHttp = _OctetIfOutHttp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 17),
    _OctetIfOutHttp_Type()
)
octetIfOutHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutHttp.setStatus("mandatory")
_OctetIfInSnmp_Type = Counter32
_OctetIfInSnmp_Object = MibTableColumn
octetIfInSnmp = _OctetIfInSnmp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 18),
    _OctetIfInSnmp_Type()
)
octetIfInSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInSnmp.setStatus("mandatory")
_OctetIfOutSnmp_Type = Counter32
_OctetIfOutSnmp_Object = MibTableColumn
octetIfOutSnmp = _OctetIfOutSnmp_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 19),
    _OctetIfOutSnmp_Type()
)
octetIfOutSnmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutSnmp.setStatus("mandatory")
_OctetIfInRip_Type = Counter32
_OctetIfInRip_Object = MibTableColumn
octetIfInRip = _OctetIfInRip_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 20),
    _OctetIfInRip_Type()
)
octetIfInRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInRip.setStatus("mandatory")
_OctetIfOutRip_Type = Counter32
_OctetIfOutRip_Object = MibTableColumn
octetIfOutRip = _OctetIfOutRip_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 21),
    _OctetIfOutRip_Type()
)
octetIfOutRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutRip.setStatus("mandatory")
_OctetIfInTunnel_Type = Counter32
_OctetIfInTunnel_Object = MibTableColumn
octetIfInTunnel = _OctetIfInTunnel_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 22),
    _OctetIfInTunnel_Type()
)
octetIfInTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfInTunnel.setStatus("mandatory")
_OctetIfOutTunnel_Type = Counter32
_OctetIfOutTunnel_Object = MibTableColumn
octetIfOutTunnel = _OctetIfOutTunnel_Object(
    (1, 3, 6, 1, 4, 1, 208, 42, 8, 1, 1, 23),
    _OctetIfOutTunnel_Type()
)
octetIfOutTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    octetIfOutTunnel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-IPROUTER-MIB",
    **{"iprouter": iprouter,
       "conf": conf,
       "confIfTable": confIfTable,
       "confIfEntry": confIfEntry,
       "confIfIndex": confIfIndex,
       "confIfAddrAndMask1": confIfAddrAndMask1,
       "confIfAddrAndMask2": confIfAddrAndMask2,
       "confIfAddrAndMask3": confIfAddrAndMask3,
       "confIfAddrAndMask4": confIfAddrAndMask4,
       "confIfRouteProto": confIfRouteProto,
       "confIfTrigRip": confIfTrigRip,
       "confIfRipMetric": confIfRipMetric,
       "confIfRip2AuthType": confIfRip2AuthType,
       "confIfRip2AuthKey": confIfRip2AuthKey,
       "confIfBootpReqForw": confIfBootpReqForw,
       "confIfProxyArp": confIfProxyArp,
       "confIfFiltering": confIfFiltering,
       "confIfRxDefAction": confIfRxDefAction,
       "confIfTxDefAction": confIfTxDefAction,
       "confIfRxDefLogging": confIfRxDefLogging,
       "confIfTxDefLogging": confIfTxDefLogging,
       "confIfCreateObj": confIfCreateObj,
       "confIfDeleteObj": confIfDeleteObj,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterIfIndex": filterIfIndex,
       "filterDirIndex": filterDirIndex,
       "filterIndex": filterIndex,
       "filterAction": filterAction,
       "filterLogging": filterLogging,
       "filterProtocol": filterProtocol,
       "filterProtocolValue": filterProtocolValue,
       "filterTcpFlags": filterTcpFlags,
       "filterSrcAddrType": filterSrcAddrType,
       "filterSrcAddr": filterSrcAddr,
       "filterSrcMask": filterSrcMask,
       "filterSrcPort": filterSrcPort,
       "filterSrcPortValue": filterSrcPortValue,
       "filterSrcPortOper": filterSrcPortOper,
       "filterDestAddrType": filterDestAddrType,
       "filterDestAddr": filterDestAddr,
       "filterDestMask": filterDestMask,
       "filterDestPort": filterDestPort,
       "filterDestPortValue": filterDestPortValue,
       "filterDestPortOper": filterDestPortOper,
       "filterHits": filterHits,
       "natTable": natTable,
       "natEntry": natEntry,
       "natIfIndex": natIfIndex,
       "natIndex": natIndex,
       "natIntAddr": natIntAddr,
       "natIntMask": natIntMask,
       "natExtAddr": natExtAddr,
       "natExtMask": natExtMask,
       "natType": natType,
       "natAuto": natAuto,
       "natTime": natTime,
       "statRoutTable": statRoutTable,
       "statRoutEntry": statRoutEntry,
       "statRoutIfIndex": statRoutIfIndex,
       "statRoutNetwork": statRoutNetwork,
       "statRoutMask": statRoutMask,
       "statRoutNextHop": statRoutNextHop,
       "statRoutMetric": statRoutMetric,
       "statRoutCreateObj": statRoutCreateObj,
       "statRoutDeleteObj": statRoutDeleteObj,
       "stat": stat,
       "statIfTable": statIfTable,
       "statIfEntry": statIfEntry,
       "statIfIndex": statIfIndex,
       "statIfType": statIfType,
       "statIfState": statIfState,
       "statIfMTU": statIfMTU,
       "statIfRxDefHits": statIfRxDefHits,
       "statIfTxDefHits": statIfTxDefHits,
       "arp": arp,
       "arpIfTable": arpIfTable,
       "arpIfEntry": arpIfEntry,
       "arpIfIndex": arpIfIndex,
       "arpIfInReq": arpIfInReq,
       "arpIfOutRep": arpIfOutRep,
       "arpIfOutReq": arpIfOutReq,
       "arpIfInRep": arpIfInRep,
       "arpIfInHdrErrors": arpIfInHdrErrors,
       "arpInReq": arpInReq,
       "arpOutRep": arpOutRep,
       "arpOutReq": arpOutReq,
       "arpInRep": arpInRep,
       "arpInHdrErrors": arpInHdrErrors,
       "ip": ip,
       "ipIfTable": ipIfTable,
       "ipIfEntry": ipIfEntry,
       "ipIfIndex": ipIfIndex,
       "ipIfInReceives": ipIfInReceives,
       "ipIfInHdrErrors": ipIfInHdrErrors,
       "ipIfInAddrErrors": ipIfInAddrErrors,
       "ipIfInDiscards": ipIfInDiscards,
       "ipIfForwDatagrams": ipIfForwDatagrams,
       "ipIfOutRequests": ipIfOutRequests,
       "ipIfOutDiscards": ipIfOutDiscards,
       "icmp": icmp,
       "icmpIfTable": icmpIfTable,
       "icmpIfEntry": icmpIfEntry,
       "icmpIfIndex": icmpIfIndex,
       "icmpIfInMsgs": icmpIfInMsgs,
       "icmpIfInErrors": icmpIfInErrors,
       "icmpIfInEchos": icmpIfInEchos,
       "icmpIfInEchoReps": icmpIfInEchoReps,
       "icmpIfOutMsgs": icmpIfOutMsgs,
       "icmpIfOutEchos": icmpIfOutEchos,
       "icmpIfOutEchoReps": icmpIfOutEchoReps,
       "icmpInRouterAdvs": icmpInRouterAdvs,
       "icmpInRouterSols": icmpInRouterSols,
       "icmpOutRouterAdvs": icmpOutRouterAdvs,
       "icmpOutRouterSols": icmpOutRouterSols,
       "rip": rip,
       "ripIfTable": ripIfTable,
       "ripIfEntry": ripIfEntry,
       "ripIfIndex": ripIfIndex,
       "ripIfInReceives": ripIfInReceives,
       "ripIfInHdrErrors": ripIfInHdrErrors,
       "ripIfInBadSrcAddrs": ripIfInBadSrcAddrs,
       "ripIfInBadVers": ripIfInBadVers,
       "ripIfInAuthFails": ripIfInAuthFails,
       "ripIfInUnknComs": ripIfInUnknComs,
       "ripIfOutSent": ripIfOutSent,
       "ripIfOutDiscards": ripIfOutDiscards,
       "ripInReceives": ripInReceives,
       "ripInHdrErrors": ripInHdrErrors,
       "ripInBadSrcAddrs": ripInBadSrcAddrs,
       "ripInBadVers": ripInBadVers,
       "ripInAuthFails": ripInAuthFails,
       "ripInUnknComs": ripInUnknComs,
       "ripOutSent": ripOutSent,
       "ripOutDiscards": ripOutDiscards,
       "bootp": bootp,
       "bootpIfTable": bootpIfTable,
       "bootpIfEntry": bootpIfEntry,
       "bootpIfIndex": bootpIfIndex,
       "bootpIfInRequests": bootpIfInRequests,
       "bootpIfInReplies": bootpIfInReplies,
       "bootpIfInErrors": bootpIfInErrors,
       "bootpIfInDiscards": bootpIfInDiscards,
       "bootpIfOutRequests": bootpIfOutRequests,
       "bootpIfOutReplies": bootpIfOutReplies,
       "bootpIfOutDiscards": bootpIfOutDiscards,
       "bootpInRequests": bootpInRequests,
       "bootpInReplies": bootpInReplies,
       "bootpInErrors": bootpInErrors,
       "bootpInDiscards": bootpInDiscards,
       "bootpOutRequests": bootpOutRequests,
       "bootpOutReplies": bootpOutReplies,
       "bootpOutDiscards": bootpOutDiscards,
       "bootpMaxHops": bootpMaxHops,
       "octetcounters": octetcounters,
       "octetIfTable": octetIfTable,
       "octetIfEntry": octetIfEntry,
       "octetIfIndex": octetIfIndex,
       "octetIfInTotal": octetIfInTotal,
       "octetIfOutTotal": octetIfOutTotal,
       "octetIfInOther": octetIfInOther,
       "octetIfOutOther": octetIfOutOther,
       "octetIfInFtp": octetIfInFtp,
       "octetIfOutFtp": octetIfOutFtp,
       "octetIfInTelnet": octetIfInTelnet,
       "octetIfOutTelnet": octetIfOutTelnet,
       "octetIfInSmtp": octetIfInSmtp,
       "octetIfOutSmtp": octetIfOutSmtp,
       "octetIfInDns": octetIfInDns,
       "octetIfOutDns": octetIfOutDns,
       "octetIfInBootp": octetIfInBootp,
       "octetIfOutBootp": octetIfOutBootp,
       "octetIfInHttp": octetIfInHttp,
       "octetIfOutHttp": octetIfOutHttp,
       "octetIfInSnmp": octetIfInSnmp,
       "octetIfOutSnmp": octetIfOutSnmp,
       "octetIfInRip": octetIfInRip,
       "octetIfOutRip": octetIfOutRip,
       "octetIfInTunnel": octetIfInTunnel,
       "octetIfOutTunnel": octetIfOutTunnel}
)
