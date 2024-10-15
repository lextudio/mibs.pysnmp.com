# SNMP MIB module (INTEL-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:56 2024
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



class PppProtocolState(Integer32):
    """Custom type PppProtocolState based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 8),
          ("acksent", 9),
          ("closed", 3),
          ("closing", 5),
          ("disabled", 11),
          ("initial", 1),
          ("opened", 10),
          ("reqsent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 23)
)
_PppLink_ObjectIdentity = ObjectIdentity
pppLink = _PppLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1)
)
_PppLinkProtoStateTable_Object = MibTable
pppLinkProtoStateTable = _PppLinkProtoStateTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1)
)
if mibBuilder.loadTexts:
    pppLinkProtoStateTable.setStatus("mandatory")
_PppLinkProtoStateEntry_Object = MibTableRow
pppLinkProtoStateEntry = _PppLinkProtoStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1)
)
pppLinkProtoStateEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkProtoStateIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkProtoStateEntry.setStatus("mandatory")
_PppLinkProtoStateIfIndex_Type = Integer32
_PppLinkProtoStateIfIndex_Object = MibTableColumn
pppLinkProtoStateIfIndex = _PppLinkProtoStateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 1),
    _PppLinkProtoStateIfIndex_Type()
)
pppLinkProtoStateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateIfIndex.setStatus("mandatory")


class _PppLinkProtoStatePppLinkType_Type(Integer32):
    """Custom type pppLinkProtoStatePppLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multilinkmaster", 2),
          ("multilinkslave", 3),
          ("standard", 1))
    )


_PppLinkProtoStatePppLinkType_Type.__name__ = "Integer32"
_PppLinkProtoStatePppLinkType_Object = MibTableColumn
pppLinkProtoStatePppLinkType = _PppLinkProtoStatePppLinkType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 2),
    _PppLinkProtoStatePppLinkType_Type()
)
pppLinkProtoStatePppLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStatePppLinkType.setStatus("mandatory")
_PppLinkProtoStateLcpState_Type = PppProtocolState
_PppLinkProtoStateLcpState_Object = MibTableColumn
pppLinkProtoStateLcpState = _PppLinkProtoStateLcpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 3),
    _PppLinkProtoStateLcpState_Type()
)
pppLinkProtoStateLcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateLcpState.setStatus("mandatory")
_PppLinkProtoStateIpcpState_Type = PppProtocolState
_PppLinkProtoStateIpcpState_Object = MibTableColumn
pppLinkProtoStateIpcpState = _PppLinkProtoStateIpcpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 4),
    _PppLinkProtoStateIpcpState_Type()
)
pppLinkProtoStateIpcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateIpcpState.setStatus("mandatory")
_PppLinkProtoStateIpxcpState_Type = PppProtocolState
_PppLinkProtoStateIpxcpState_Object = MibTableColumn
pppLinkProtoStateIpxcpState = _PppLinkProtoStateIpxcpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 5),
    _PppLinkProtoStateIpxcpState_Type()
)
pppLinkProtoStateIpxcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateIpxcpState.setStatus("mandatory")
_PppLinkProtoStateBcpState_Type = PppProtocolState
_PppLinkProtoStateBcpState_Object = MibTableColumn
pppLinkProtoStateBcpState = _PppLinkProtoStateBcpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 6),
    _PppLinkProtoStateBcpState_Type()
)
pppLinkProtoStateBcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateBcpState.setStatus("mandatory")
_PppLinkProtoStateCcpState_Type = PppProtocolState
_PppLinkProtoStateCcpState_Object = MibTableColumn
pppLinkProtoStateCcpState = _PppLinkProtoStateCcpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 7),
    _PppLinkProtoStateCcpState_Type()
)
pppLinkProtoStateCcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateCcpState.setStatus("mandatory")
_PppLinkProtoStateEcpState_Type = PppProtocolState
_PppLinkProtoStateEcpState_Object = MibTableColumn
pppLinkProtoStateEcpState = _PppLinkProtoStateEcpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 8),
    _PppLinkProtoStateEcpState_Type()
)
pppLinkProtoStateEcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateEcpState.setStatus("mandatory")
_PppLinkProtoStateBacpState_Type = PppProtocolState
_PppLinkProtoStateBacpState_Object = MibTableColumn
pppLinkProtoStateBacpState = _PppLinkProtoStateBacpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 1, 1, 9),
    _PppLinkProtoStateBacpState_Type()
)
pppLinkProtoStateBacpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtoStateBacpState.setStatus("mandatory")
_PppLinkLcpTable_Object = MibTable
pppLinkLcpTable = _PppLinkLcpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2)
)
if mibBuilder.loadTexts:
    pppLinkLcpTable.setStatus("mandatory")
_PppLinkLcpEntry_Object = MibTableRow
pppLinkLcpEntry = _PppLinkLcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1)
)
pppLinkLcpEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkLcpIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkLcpEntry.setStatus("mandatory")
_PppLinkLcpIfIndex_Type = Integer32
_PppLinkLcpIfIndex_Object = MibTableColumn
pppLinkLcpIfIndex = _PppLinkLcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 1),
    _PppLinkLcpIfIndex_Type()
)
pppLinkLcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLcpIfIndex.setStatus("mandatory")
_PppLinkLcpMRUInc_Type = Integer32
_PppLinkLcpMRUInc_Object = MibTableColumn
pppLinkLcpMRUInc = _PppLinkLcpMRUInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 2),
    _PppLinkLcpMRUInc_Type()
)
pppLinkLcpMRUInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLcpMRUInc.setStatus("mandatory")
_PppLinkLcpMRUOut_Type = Integer32
_PppLinkLcpMRUOut_Object = MibTableColumn
pppLinkLcpMRUOut = _PppLinkLcpMRUOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 3),
    _PppLinkLcpMRUOut_Type()
)
pppLinkLcpMRUOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLcpMRUOut.setStatus("mandatory")
_PppLinkLcpACCMapInc_Type = Integer32
_PppLinkLcpACCMapInc_Object = MibTableColumn
pppLinkLcpACCMapInc = _PppLinkLcpACCMapInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 4),
    _PppLinkLcpACCMapInc_Type()
)
pppLinkLcpACCMapInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLcpACCMapInc.setStatus("mandatory")
_PppLinkLcpACCMapOut_Type = Integer32
_PppLinkLcpACCMapOut_Object = MibTableColumn
pppLinkLcpACCMapOut = _PppLinkLcpACCMapOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 5),
    _PppLinkLcpACCMapOut_Type()
)
pppLinkLcpACCMapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLcpACCMapOut.setStatus("mandatory")


class _PppLinkProtocolCompressionInc_Type(Integer32):
    """Custom type pppLinkProtocolCompressionInc based on Integer32"""
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


_PppLinkProtocolCompressionInc_Type.__name__ = "Integer32"
_PppLinkProtocolCompressionInc_Object = MibTableColumn
pppLinkProtocolCompressionInc = _PppLinkProtocolCompressionInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 6),
    _PppLinkProtocolCompressionInc_Type()
)
pppLinkProtocolCompressionInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtocolCompressionInc.setStatus("mandatory")


class _PppLinkProtocolCompressionOut_Type(Integer32):
    """Custom type pppLinkProtocolCompressionOut based on Integer32"""
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


_PppLinkProtocolCompressionOut_Type.__name__ = "Integer32"
_PppLinkProtocolCompressionOut_Object = MibTableColumn
pppLinkProtocolCompressionOut = _PppLinkProtocolCompressionOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 7),
    _PppLinkProtocolCompressionOut_Type()
)
pppLinkProtocolCompressionOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkProtocolCompressionOut.setStatus("mandatory")


class _PppLinkACCompressionInc_Type(Integer32):
    """Custom type pppLinkACCompressionInc based on Integer32"""
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


_PppLinkACCompressionInc_Type.__name__ = "Integer32"
_PppLinkACCompressionInc_Object = MibTableColumn
pppLinkACCompressionInc = _PppLinkACCompressionInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 8),
    _PppLinkACCompressionInc_Type()
)
pppLinkACCompressionInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkACCompressionInc.setStatus("mandatory")


class _PppLinkACCompressionOut_Type(Integer32):
    """Custom type pppLinkACCompressionOut based on Integer32"""
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


_PppLinkACCompressionOut_Type.__name__ = "Integer32"
_PppLinkACCompressionOut_Object = MibTableColumn
pppLinkACCompressionOut = _PppLinkACCompressionOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 9),
    _PppLinkACCompressionOut_Type()
)
pppLinkACCompressionOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkACCompressionOut.setStatus("mandatory")
_PppLinkMagicNumberInc_Type = Integer32
_PppLinkMagicNumberInc_Object = MibTableColumn
pppLinkMagicNumberInc = _PppLinkMagicNumberInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 10),
    _PppLinkMagicNumberInc_Type()
)
pppLinkMagicNumberInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMagicNumberInc.setStatus("mandatory")
_PppLinkMagicNumberOut_Type = Integer32
_PppLinkMagicNumberOut_Object = MibTableColumn
pppLinkMagicNumberOut = _PppLinkMagicNumberOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 11),
    _PppLinkMagicNumberOut_Type()
)
pppLinkMagicNumberOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMagicNumberOut.setStatus("mandatory")
_PppLinkLinkDiscriminatorInc_Type = Integer32
_PppLinkLinkDiscriminatorInc_Object = MibTableColumn
pppLinkLinkDiscriminatorInc = _PppLinkLinkDiscriminatorInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 12),
    _PppLinkLinkDiscriminatorInc_Type()
)
pppLinkLinkDiscriminatorInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLinkDiscriminatorInc.setStatus("mandatory")
_PppLinkLinkDiscriminatorOut_Type = Integer32
_PppLinkLinkDiscriminatorOut_Object = MibTableColumn
pppLinkLinkDiscriminatorOut = _PppLinkLinkDiscriminatorOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 2, 1, 13),
    _PppLinkLinkDiscriminatorOut_Type()
)
pppLinkLinkDiscriminatorOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkLinkDiscriminatorOut.setStatus("mandatory")
_PppLinkBcpTable_Object = MibTable
pppLinkBcpTable = _PppLinkBcpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3)
)
if mibBuilder.loadTexts:
    pppLinkBcpTable.setStatus("mandatory")
_PppLinkBcpEntry_Object = MibTableRow
pppLinkBcpEntry = _PppLinkBcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3, 1)
)
pppLinkBcpEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkBcpIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkBcpEntry.setStatus("mandatory")
_PppLinkBcpIfIndex_Type = Integer32
_PppLinkBcpIfIndex_Object = MibTableColumn
pppLinkBcpIfIndex = _PppLinkBcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3, 1, 1),
    _PppLinkBcpIfIndex_Type()
)
pppLinkBcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBcpIfIndex.setStatus("mandatory")


class _PppLinkBcpMACTypeInc_Type(Integer32):
    """Custom type pppLinkBcpMACTypeInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("notnegotiated", 1))
    )


_PppLinkBcpMACTypeInc_Type.__name__ = "Integer32"
_PppLinkBcpMACTypeInc_Object = MibTableColumn
pppLinkBcpMACTypeInc = _PppLinkBcpMACTypeInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3, 1, 2),
    _PppLinkBcpMACTypeInc_Type()
)
pppLinkBcpMACTypeInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBcpMACTypeInc.setStatus("mandatory")


class _PppLinkBcpMACTypeOut_Type(Integer32):
    """Custom type pppLinkBcpMACTypeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("notnegotiated", 1))
    )


_PppLinkBcpMACTypeOut_Type.__name__ = "Integer32"
_PppLinkBcpMACTypeOut_Object = MibTableColumn
pppLinkBcpMACTypeOut = _PppLinkBcpMACTypeOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3, 1, 3),
    _PppLinkBcpMACTypeOut_Type()
)
pppLinkBcpMACTypeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBcpMACTypeOut.setStatus("mandatory")


class _PppLinkBcpBridgingProtInc_Type(Integer32):
    """Custom type pppLinkBcpBridgingProtInc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notnegotiated", 1),
          ("spanningtree", 2))
    )


_PppLinkBcpBridgingProtInc_Type.__name__ = "Integer32"
_PppLinkBcpBridgingProtInc_Object = MibTableColumn
pppLinkBcpBridgingProtInc = _PppLinkBcpBridgingProtInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3, 1, 4),
    _PppLinkBcpBridgingProtInc_Type()
)
pppLinkBcpBridgingProtInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBcpBridgingProtInc.setStatus("mandatory")


class _PppLinkBcpBridgingProtOut_Type(Integer32):
    """Custom type pppLinkBcpBridgingProtOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notnegotiated", 1),
          ("spanningtree", 2))
    )


_PppLinkBcpBridgingProtOut_Type.__name__ = "Integer32"
_PppLinkBcpBridgingProtOut_Object = MibTableColumn
pppLinkBcpBridgingProtOut = _PppLinkBcpBridgingProtOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 3, 1, 5),
    _PppLinkBcpBridgingProtOut_Type()
)
pppLinkBcpBridgingProtOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBcpBridgingProtOut.setStatus("mandatory")
_PppLinkCcpTable_Object = MibTable
pppLinkCcpTable = _PppLinkCcpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4)
)
if mibBuilder.loadTexts:
    pppLinkCcpTable.setStatus("mandatory")
_PppLinkCcpEntry_Object = MibTableRow
pppLinkCcpEntry = _PppLinkCcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4, 1)
)
pppLinkCcpEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkCcpIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkCcpEntry.setStatus("mandatory")
_PppLinkCcpIfIndex_Type = Integer32
_PppLinkCcpIfIndex_Object = MibTableColumn
pppLinkCcpIfIndex = _PppLinkCcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4, 1, 1),
    _PppLinkCcpIfIndex_Type()
)
pppLinkCcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCcpIfIndex.setStatus("mandatory")
_PppLinkCcpHistorySizeIncoming_Type = Integer32
_PppLinkCcpHistorySizeIncoming_Object = MibTableColumn
pppLinkCcpHistorySizeIncoming = _PppLinkCcpHistorySizeIncoming_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4, 1, 2),
    _PppLinkCcpHistorySizeIncoming_Type()
)
pppLinkCcpHistorySizeIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCcpHistorySizeIncoming.setStatus("mandatory")
_PppLinkCcpHistorySizeOutgoing_Type = Integer32
_PppLinkCcpHistorySizeOutgoing_Object = MibTableColumn
pppLinkCcpHistorySizeOutgoing = _PppLinkCcpHistorySizeOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4, 1, 3),
    _PppLinkCcpHistorySizeOutgoing_Type()
)
pppLinkCcpHistorySizeOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCcpHistorySizeOutgoing.setStatus("mandatory")


class _PppLinkCcpCheckTypeIncoming_Type(Integer32):
    """Custom type pppLinkCcpCheckTypeIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extms", 3),
          ("none", 1),
          ("sequenceno", 2))
    )


_PppLinkCcpCheckTypeIncoming_Type.__name__ = "Integer32"
_PppLinkCcpCheckTypeIncoming_Object = MibTableColumn
pppLinkCcpCheckTypeIncoming = _PppLinkCcpCheckTypeIncoming_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4, 1, 4),
    _PppLinkCcpCheckTypeIncoming_Type()
)
pppLinkCcpCheckTypeIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCcpCheckTypeIncoming.setStatus("mandatory")


class _PppLinkCcpCheckTypeOutgoing_Type(Integer32):
    """Custom type pppLinkCcpCheckTypeOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extms", 3),
          ("none", 1),
          ("sequenceno", 2))
    )


_PppLinkCcpCheckTypeOutgoing_Type.__name__ = "Integer32"
_PppLinkCcpCheckTypeOutgoing_Object = MibTableColumn
pppLinkCcpCheckTypeOutgoing = _PppLinkCcpCheckTypeOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 4, 1, 5),
    _PppLinkCcpCheckTypeOutgoing_Type()
)
pppLinkCcpCheckTypeOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCcpCheckTypeOutgoing.setStatus("mandatory")
_PppLinkEcpTable_Object = MibTable
pppLinkEcpTable = _PppLinkEcpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5)
)
if mibBuilder.loadTexts:
    pppLinkEcpTable.setStatus("mandatory")
_PppLinkEcpEntry_Object = MibTableRow
pppLinkEcpEntry = _PppLinkEcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1)
)
pppLinkEcpEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkEcpIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkEcpEntry.setStatus("mandatory")
_PppLinkEcpIfIndex_Type = Integer32
_PppLinkEcpIfIndex_Object = MibTableColumn
pppLinkEcpIfIndex = _PppLinkEcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 1),
    _PppLinkEcpIfIndex_Type()
)
pppLinkEcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpIfIndex.setStatus("mandatory")
_PppLinkEcpResetRequestsRx_Type = Counter32
_PppLinkEcpResetRequestsRx_Object = MibTableColumn
pppLinkEcpResetRequestsRx = _PppLinkEcpResetRequestsRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 2),
    _PppLinkEcpResetRequestsRx_Type()
)
pppLinkEcpResetRequestsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpResetRequestsRx.setStatus("mandatory")
_PppLinkEcpResetRequestsTx_Type = Counter32
_PppLinkEcpResetRequestsTx_Object = MibTableColumn
pppLinkEcpResetRequestsTx = _PppLinkEcpResetRequestsTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 3),
    _PppLinkEcpResetRequestsTx_Type()
)
pppLinkEcpResetRequestsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpResetRequestsTx.setStatus("mandatory")
_PppLinkEcpResetAcksRx_Type = Counter32
_PppLinkEcpResetAcksRx_Object = MibTableColumn
pppLinkEcpResetAcksRx = _PppLinkEcpResetAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 4),
    _PppLinkEcpResetAcksRx_Type()
)
pppLinkEcpResetAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpResetAcksRx.setStatus("mandatory")
_PppLinkEcpResetAcksTx_Type = Counter32
_PppLinkEcpResetAcksTx_Object = MibTableColumn
pppLinkEcpResetAcksTx = _PppLinkEcpResetAcksTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 5),
    _PppLinkEcpResetAcksTx_Type()
)
pppLinkEcpResetAcksTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpResetAcksTx.setStatus("mandatory")
_PppLinkEcpRxDiscarded_Type = Counter32
_PppLinkEcpRxDiscarded_Object = MibTableColumn
pppLinkEcpRxDiscarded = _PppLinkEcpRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 6),
    _PppLinkEcpRxDiscarded_Type()
)
pppLinkEcpRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpRxDiscarded.setStatus("mandatory")
_PppLinkEcpTxDiscarded_Type = Counter32
_PppLinkEcpTxDiscarded_Object = MibTableColumn
pppLinkEcpTxDiscarded = _PppLinkEcpTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 7),
    _PppLinkEcpTxDiscarded_Type()
)
pppLinkEcpTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpTxDiscarded.setStatus("mandatory")


class _PppLinkEcpReceiverState_Type(Integer32):
    """Custom type pppLinkEcpReceiverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_PppLinkEcpReceiverState_Type.__name__ = "Integer32"
_PppLinkEcpReceiverState_Object = MibTableColumn
pppLinkEcpReceiverState = _PppLinkEcpReceiverState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 5, 1, 8),
    _PppLinkEcpReceiverState_Type()
)
pppLinkEcpReceiverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkEcpReceiverState.setStatus("mandatory")
_PppLinkCompTable_Object = MibTable
pppLinkCompTable = _PppLinkCompTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6)
)
if mibBuilder.loadTexts:
    pppLinkCompTable.setStatus("mandatory")
_PppLinkCompEntry_Object = MibTableRow
pppLinkCompEntry = _PppLinkCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1)
)
pppLinkCompEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkCompIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkCompEntry.setStatus("mandatory")
_PppLinkCompIfIndex_Type = Integer32
_PppLinkCompIfIndex_Object = MibTableColumn
pppLinkCompIfIndex = _PppLinkCompIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 1),
    _PppLinkCompIfIndex_Type()
)
pppLinkCompIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompIfIndex.setStatus("mandatory")
_PppLinkCompDecoderBytesIn_Type = Counter32
_PppLinkCompDecoderBytesIn_Object = MibTableColumn
pppLinkCompDecoderBytesIn = _PppLinkCompDecoderBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 2),
    _PppLinkCompDecoderBytesIn_Type()
)
pppLinkCompDecoderBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderBytesIn.setStatus("mandatory")
_PppLinkCompDecoderDecompBytesOut_Type = Counter32
_PppLinkCompDecoderDecompBytesOut_Object = MibTableColumn
pppLinkCompDecoderDecompBytesOut = _PppLinkCompDecoderDecompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 3),
    _PppLinkCompDecoderDecompBytesOut_Type()
)
pppLinkCompDecoderDecompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderDecompBytesOut.setStatus("mandatory")
_PppLinkCompDecoderUncompBytesOut_Type = Counter32
_PppLinkCompDecoderUncompBytesOut_Object = MibTableColumn
pppLinkCompDecoderUncompBytesOut = _PppLinkCompDecoderUncompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 4),
    _PppLinkCompDecoderUncompBytesOut_Type()
)
pppLinkCompDecoderUncompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderUncompBytesOut.setStatus("mandatory")
_PppLinkCompDecoderCompPacketsIn_Type = Counter32
_PppLinkCompDecoderCompPacketsIn_Object = MibTableColumn
pppLinkCompDecoderCompPacketsIn = _PppLinkCompDecoderCompPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 5),
    _PppLinkCompDecoderCompPacketsIn_Type()
)
pppLinkCompDecoderCompPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderCompPacketsIn.setStatus("mandatory")
_PppLinkCompDecoderUncompPacketsIn_Type = Counter32
_PppLinkCompDecoderUncompPacketsIn_Object = MibTableColumn
pppLinkCompDecoderUncompPacketsIn = _PppLinkCompDecoderUncompPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 6),
    _PppLinkCompDecoderUncompPacketsIn_Type()
)
pppLinkCompDecoderUncompPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderUncompPacketsIn.setStatus("mandatory")
_PppLinkCompDecoderDecompQueueLength_Type = Counter32
_PppLinkCompDecoderDecompQueueLength_Object = MibTableColumn
pppLinkCompDecoderDecompQueueLength = _PppLinkCompDecoderDecompQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 7),
    _PppLinkCompDecoderDecompQueueLength_Type()
)
pppLinkCompDecoderDecompQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderDecompQueueLength.setStatus("mandatory")
_PppLinkCompDecoderCompressionRatio_Type = Counter32
_PppLinkCompDecoderCompressionRatio_Object = MibTableColumn
pppLinkCompDecoderCompressionRatio = _PppLinkCompDecoderCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 8),
    _PppLinkCompDecoderCompressionRatio_Type()
)
pppLinkCompDecoderCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderCompressionRatio.setStatus("mandatory")
_PppLinkCompDecoderResetRequestTx_Type = Counter32
_PppLinkCompDecoderResetRequestTx_Object = MibTableColumn
pppLinkCompDecoderResetRequestTx = _PppLinkCompDecoderResetRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 9),
    _PppLinkCompDecoderResetRequestTx_Type()
)
pppLinkCompDecoderResetRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderResetRequestTx.setStatus("mandatory")
_PppLinkCompDecoderResetAcksRx_Type = Counter32
_PppLinkCompDecoderResetAcksRx_Object = MibTableColumn
pppLinkCompDecoderResetAcksRx = _PppLinkCompDecoderResetAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 10),
    _PppLinkCompDecoderResetAcksRx_Type()
)
pppLinkCompDecoderResetAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderResetAcksRx.setStatus("mandatory")
_PppLinkCompDecoderRxDiscarded_Type = Counter32
_PppLinkCompDecoderRxDiscarded_Object = MibTableColumn
pppLinkCompDecoderRxDiscarded = _PppLinkCompDecoderRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 11),
    _PppLinkCompDecoderRxDiscarded_Type()
)
pppLinkCompDecoderRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderRxDiscarded.setStatus("mandatory")


class _PppLinkCompDecoderState_Type(Integer32):
    """Custom type pppLinkCompDecoderState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_PppLinkCompDecoderState_Type.__name__ = "Integer32"
_PppLinkCompDecoderState_Object = MibTableColumn
pppLinkCompDecoderState = _PppLinkCompDecoderState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 12),
    _PppLinkCompDecoderState_Type()
)
pppLinkCompDecoderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderState.setStatus("mandatory")
_PppLinkCompEncoderBytesIn_Type = Counter32
_PppLinkCompEncoderBytesIn_Object = MibTableColumn
pppLinkCompEncoderBytesIn = _PppLinkCompEncoderBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 13),
    _PppLinkCompEncoderBytesIn_Type()
)
pppLinkCompEncoderBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderBytesIn.setStatus("mandatory")
_PppLinkCompEncoderCompBytesOut_Type = Counter32
_PppLinkCompEncoderCompBytesOut_Object = MibTableColumn
pppLinkCompEncoderCompBytesOut = _PppLinkCompEncoderCompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 14),
    _PppLinkCompEncoderCompBytesOut_Type()
)
pppLinkCompEncoderCompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderCompBytesOut.setStatus("mandatory")
_PppLinkCompEncoderUncompBytesOut_Type = Counter32
_PppLinkCompEncoderUncompBytesOut_Object = MibTableColumn
pppLinkCompEncoderUncompBytesOut = _PppLinkCompEncoderUncompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 15),
    _PppLinkCompEncoderUncompBytesOut_Type()
)
pppLinkCompEncoderUncompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderUncompBytesOut.setStatus("mandatory")
_PppLinkCompEncoderCompPacketsOut_Type = Counter32
_PppLinkCompEncoderCompPacketsOut_Object = MibTableColumn
pppLinkCompEncoderCompPacketsOut = _PppLinkCompEncoderCompPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 16),
    _PppLinkCompEncoderCompPacketsOut_Type()
)
pppLinkCompEncoderCompPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderCompPacketsOut.setStatus("mandatory")
_PppLinkCompEncoderUncompPacketsOut_Type = Counter32
_PppLinkCompEncoderUncompPacketsOut_Object = MibTableColumn
pppLinkCompEncoderUncompPacketsOut = _PppLinkCompEncoderUncompPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 17),
    _PppLinkCompEncoderUncompPacketsOut_Type()
)
pppLinkCompEncoderUncompPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderUncompPacketsOut.setStatus("mandatory")
_PppLinkCompEncoderCompQueueLength_Type = Counter32
_PppLinkCompEncoderCompQueueLength_Object = MibTableColumn
pppLinkCompEncoderCompQueueLength = _PppLinkCompEncoderCompQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 18),
    _PppLinkCompEncoderCompQueueLength_Type()
)
pppLinkCompEncoderCompQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderCompQueueLength.setStatus("mandatory")
_PppLinkCompEncoderCompressionRation_Type = Counter32
_PppLinkCompEncoderCompressionRation_Object = MibTableColumn
pppLinkCompEncoderCompressionRation = _PppLinkCompEncoderCompressionRation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 19),
    _PppLinkCompEncoderCompressionRation_Type()
)
pppLinkCompEncoderCompressionRation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderCompressionRation.setStatus("mandatory")
_PppLinkCompEncoderResetRequestRx_Type = Counter32
_PppLinkCompEncoderResetRequestRx_Object = MibTableColumn
pppLinkCompEncoderResetRequestRx = _PppLinkCompEncoderResetRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 20),
    _PppLinkCompEncoderResetRequestRx_Type()
)
pppLinkCompEncoderResetRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderResetRequestRx.setStatus("mandatory")
_PppLinkCompEncoderResetAckTx_Type = Counter32
_PppLinkCompEncoderResetAckTx_Object = MibTableColumn
pppLinkCompEncoderResetAckTx = _PppLinkCompEncoderResetAckTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 21),
    _PppLinkCompEncoderResetAckTx_Type()
)
pppLinkCompEncoderResetAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderResetAckTx.setStatus("mandatory")
_PppLinkCompEncoderTxDiscarded_Type = Counter32
_PppLinkCompEncoderTxDiscarded_Object = MibTableColumn
pppLinkCompEncoderTxDiscarded = _PppLinkCompEncoderTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 22),
    _PppLinkCompEncoderTxDiscarded_Type()
)
pppLinkCompEncoderTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderTxDiscarded.setStatus("mandatory")
_PppLinkCompDecoderBytesInUpper_Type = Counter32
_PppLinkCompDecoderBytesInUpper_Object = MibTableColumn
pppLinkCompDecoderBytesInUpper = _PppLinkCompDecoderBytesInUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 23),
    _PppLinkCompDecoderBytesInUpper_Type()
)
pppLinkCompDecoderBytesInUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderBytesInUpper.setStatus("mandatory")
_PppLinkCompDecoderDecompBytesOutUpper_Type = Counter32
_PppLinkCompDecoderDecompBytesOutUpper_Object = MibTableColumn
pppLinkCompDecoderDecompBytesOutUpper = _PppLinkCompDecoderDecompBytesOutUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 24),
    _PppLinkCompDecoderDecompBytesOutUpper_Type()
)
pppLinkCompDecoderDecompBytesOutUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderDecompBytesOutUpper.setStatus("mandatory")
_PppLinkCompDecoderUncompBytesOutUpper_Type = Counter32
_PppLinkCompDecoderUncompBytesOutUpper_Object = MibTableColumn
pppLinkCompDecoderUncompBytesOutUpper = _PppLinkCompDecoderUncompBytesOutUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 25),
    _PppLinkCompDecoderUncompBytesOutUpper_Type()
)
pppLinkCompDecoderUncompBytesOutUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompDecoderUncompBytesOutUpper.setStatus("mandatory")
_PppLinkCompEncoderBytesInUpper_Type = Counter32
_PppLinkCompEncoderBytesInUpper_Object = MibTableColumn
pppLinkCompEncoderBytesInUpper = _PppLinkCompEncoderBytesInUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 26),
    _PppLinkCompEncoderBytesInUpper_Type()
)
pppLinkCompEncoderBytesInUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderBytesInUpper.setStatus("mandatory")
_PppLinkCompEncoderCompBytesOutUpper_Type = Counter32
_PppLinkCompEncoderCompBytesOutUpper_Object = MibTableColumn
pppLinkCompEncoderCompBytesOutUpper = _PppLinkCompEncoderCompBytesOutUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 27),
    _PppLinkCompEncoderCompBytesOutUpper_Type()
)
pppLinkCompEncoderCompBytesOutUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderCompBytesOutUpper.setStatus("mandatory")
_PppLinkCompEncoderUncompBytesOutUpper_Type = Counter32
_PppLinkCompEncoderUncompBytesOutUpper_Object = MibTableColumn
pppLinkCompEncoderUncompBytesOutUpper = _PppLinkCompEncoderUncompBytesOutUpper_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 6, 1, 28),
    _PppLinkCompEncoderUncompBytesOutUpper_Type()
)
pppLinkCompEncoderUncompBytesOutUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkCompEncoderUncompBytesOutUpper.setStatus("mandatory")
_PppLinkChapTable_Object = MibTable
pppLinkChapTable = _PppLinkChapTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7)
)
if mibBuilder.loadTexts:
    pppLinkChapTable.setStatus("mandatory")
_PppLinkChapEntry_Object = MibTableRow
pppLinkChapEntry = _PppLinkChapEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1)
)
pppLinkChapEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkChapIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkChapEntry.setStatus("mandatory")
_PppLinkChapIfIndex_Type = Integer32
_PppLinkChapIfIndex_Object = MibTableColumn
pppLinkChapIfIndex = _PppLinkChapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 1),
    _PppLinkChapIfIndex_Type()
)
pppLinkChapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapIfIndex.setStatus("mandatory")


class _PppLinkChapIncoming_Type(Integer32):
    """Custom type pppLinkChapIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notnegotiated", 1),
          ("yes", 2))
    )


_PppLinkChapIncoming_Type.__name__ = "Integer32"
_PppLinkChapIncoming_Object = MibTableColumn
pppLinkChapIncoming = _PppLinkChapIncoming_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 2),
    _PppLinkChapIncoming_Type()
)
pppLinkChapIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapIncoming.setStatus("mandatory")


class _PppLinkChapOutgoing_Type(Integer32):
    """Custom type pppLinkChapOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notnegotiated", 1),
          ("yes", 2))
    )


_PppLinkChapOutgoing_Type.__name__ = "Integer32"
_PppLinkChapOutgoing_Object = MibTableColumn
pppLinkChapOutgoing = _PppLinkChapOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 3),
    _PppLinkChapOutgoing_Type()
)
pppLinkChapOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapOutgoing.setStatus("mandatory")
_PppLinkChapChallengeRx_Type = Counter32
_PppLinkChapChallengeRx_Object = MibTableColumn
pppLinkChapChallengeRx = _PppLinkChapChallengeRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 4),
    _PppLinkChapChallengeRx_Type()
)
pppLinkChapChallengeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapChallengeRx.setStatus("mandatory")
_PppLinkChapChallengeTx_Type = Counter32
_PppLinkChapChallengeTx_Object = MibTableColumn
pppLinkChapChallengeTx = _PppLinkChapChallengeTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 5),
    _PppLinkChapChallengeTx_Type()
)
pppLinkChapChallengeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapChallengeTx.setStatus("mandatory")
_PppLinkChapResponseRx_Type = Counter32
_PppLinkChapResponseRx_Object = MibTableColumn
pppLinkChapResponseRx = _PppLinkChapResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 6),
    _PppLinkChapResponseRx_Type()
)
pppLinkChapResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapResponseRx.setStatus("mandatory")
_PppLinkChapResponseTx_Type = Counter32
_PppLinkChapResponseTx_Object = MibTableColumn
pppLinkChapResponseTx = _PppLinkChapResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 7),
    _PppLinkChapResponseTx_Type()
)
pppLinkChapResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapResponseTx.setStatus("mandatory")
_PppLinkChapSuccesRx_Type = Counter32
_PppLinkChapSuccesRx_Object = MibTableColumn
pppLinkChapSuccesRx = _PppLinkChapSuccesRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 8),
    _PppLinkChapSuccesRx_Type()
)
pppLinkChapSuccesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapSuccesRx.setStatus("mandatory")
_PppLinkChapSuccesTx_Type = Counter32
_PppLinkChapSuccesTx_Object = MibTableColumn
pppLinkChapSuccesTx = _PppLinkChapSuccesTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 9),
    _PppLinkChapSuccesTx_Type()
)
pppLinkChapSuccesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapSuccesTx.setStatus("mandatory")
_PppLinkChapFailureRx_Type = Counter32
_PppLinkChapFailureRx_Object = MibTableColumn
pppLinkChapFailureRx = _PppLinkChapFailureRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 10),
    _PppLinkChapFailureRx_Type()
)
pppLinkChapFailureRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapFailureRx.setStatus("mandatory")
_PppLinkChapFailureTx_Type = Counter32
_PppLinkChapFailureTx_Object = MibTableColumn
pppLinkChapFailureTx = _PppLinkChapFailureTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 7, 1, 11),
    _PppLinkChapFailureTx_Type()
)
pppLinkChapFailureTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkChapFailureTx.setStatus("mandatory")
_PppLinkPapTable_Object = MibTable
pppLinkPapTable = _PppLinkPapTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8)
)
if mibBuilder.loadTexts:
    pppLinkPapTable.setStatus("mandatory")
_PppLinkPapEntry_Object = MibTableRow
pppLinkPapEntry = _PppLinkPapEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1)
)
pppLinkPapEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkPapIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkPapEntry.setStatus("mandatory")
_PppLinkPapIfIndex_Type = Integer32
_PppLinkPapIfIndex_Object = MibTableColumn
pppLinkPapIfIndex = _PppLinkPapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 1),
    _PppLinkPapIfIndex_Type()
)
pppLinkPapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapIfIndex.setStatus("mandatory")


class _PppLinkPapIncoming_Type(Integer32):
    """Custom type pppLinkPapIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notnegotiated", 1),
          ("yes", 2))
    )


_PppLinkPapIncoming_Type.__name__ = "Integer32"
_PppLinkPapIncoming_Object = MibTableColumn
pppLinkPapIncoming = _PppLinkPapIncoming_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 2),
    _PppLinkPapIncoming_Type()
)
pppLinkPapIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapIncoming.setStatus("mandatory")


class _PppLinkPapOutgoing_Type(Integer32):
    """Custom type pppLinkPapOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notnegotiated", 1),
          ("yes", 2))
    )


_PppLinkPapOutgoing_Type.__name__ = "Integer32"
_PppLinkPapOutgoing_Object = MibTableColumn
pppLinkPapOutgoing = _PppLinkPapOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 3),
    _PppLinkPapOutgoing_Type()
)
pppLinkPapOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapOutgoing.setStatus("mandatory")
_PppLinkPapAuthReqRx_Type = Counter32
_PppLinkPapAuthReqRx_Object = MibTableColumn
pppLinkPapAuthReqRx = _PppLinkPapAuthReqRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 4),
    _PppLinkPapAuthReqRx_Type()
)
pppLinkPapAuthReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapAuthReqRx.setStatus("mandatory")
_PppLinkPapAuthReqTx_Type = Counter32
_PppLinkPapAuthReqTx_Object = MibTableColumn
pppLinkPapAuthReqTx = _PppLinkPapAuthReqTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 5),
    _PppLinkPapAuthReqTx_Type()
)
pppLinkPapAuthReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapAuthReqTx.setStatus("mandatory")
_PppLinkPapAuthAckRx_Type = Counter32
_PppLinkPapAuthAckRx_Object = MibTableColumn
pppLinkPapAuthAckRx = _PppLinkPapAuthAckRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 6),
    _PppLinkPapAuthAckRx_Type()
)
pppLinkPapAuthAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapAuthAckRx.setStatus("mandatory")
_PppLinkPapAuthAckTx_Type = Counter32
_PppLinkPapAuthAckTx_Object = MibTableColumn
pppLinkPapAuthAckTx = _PppLinkPapAuthAckTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 7),
    _PppLinkPapAuthAckTx_Type()
)
pppLinkPapAuthAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapAuthAckTx.setStatus("mandatory")
_PppLinkPapAuthNackRx_Type = Counter32
_PppLinkPapAuthNackRx_Object = MibTableColumn
pppLinkPapAuthNackRx = _PppLinkPapAuthNackRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 8),
    _PppLinkPapAuthNackRx_Type()
)
pppLinkPapAuthNackRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapAuthNackRx.setStatus("mandatory")
_PppLinkPapAuthNackTx_Type = Counter32
_PppLinkPapAuthNackTx_Object = MibTableColumn
pppLinkPapAuthNackTx = _PppLinkPapAuthNackTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 8, 1, 9),
    _PppLinkPapAuthNackTx_Type()
)
pppLinkPapAuthNackTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkPapAuthNackTx.setStatus("mandatory")
_PppLinkMlMasterTable_Object = MibTable
pppLinkMlMasterTable = _PppLinkMlMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9)
)
if mibBuilder.loadTexts:
    pppLinkMlMasterTable.setStatus("mandatory")
_PppLinkMlMasterEntry_Object = MibTableRow
pppLinkMlMasterEntry = _PppLinkMlMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1)
)
pppLinkMlMasterEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkMlMasterIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkMlMasterEntry.setStatus("mandatory")
_PppLinkMlMasterIfIndex_Type = Integer32
_PppLinkMlMasterIfIndex_Object = MibTableColumn
pppLinkMlMasterIfIndex = _PppLinkMlMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 1),
    _PppLinkMlMasterIfIndex_Type()
)
pppLinkMlMasterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterIfIndex.setStatus("mandatory")
_PppLinkMlMasterSlaveCount_Type = Counter32
_PppLinkMlMasterSlaveCount_Object = MibTableColumn
pppLinkMlMasterSlaveCount = _PppLinkMlMasterSlaveCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 2),
    _PppLinkMlMasterSlaveCount_Type()
)
pppLinkMlMasterSlaveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterSlaveCount.setStatus("mandatory")
_PppLinkMlMasterTxUtilization_Type = Counter32
_PppLinkMlMasterTxUtilization_Object = MibTableColumn
pppLinkMlMasterTxUtilization = _PppLinkMlMasterTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 3),
    _PppLinkMlMasterTxUtilization_Type()
)
pppLinkMlMasterTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterTxUtilization.setStatus("mandatory")
_PppLinkMlMasterRxUtilization_Type = Counter32
_PppLinkMlMasterRxUtilization_Object = MibTableColumn
pppLinkMlMasterRxUtilization = _PppLinkMlMasterRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 4),
    _PppLinkMlMasterRxUtilization_Type()
)
pppLinkMlMasterRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterRxUtilization.setStatus("mandatory")
_PppLinkMlMasterSlavesForwarding_Type = Counter32
_PppLinkMlMasterSlavesForwarding_Object = MibTableColumn
pppLinkMlMasterSlavesForwarding = _PppLinkMlMasterSlavesForwarding_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 5),
    _PppLinkMlMasterSlavesForwarding_Type()
)
pppLinkMlMasterSlavesForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterSlavesForwarding.setStatus("mandatory")
_PppLinkMlMasterLinkAddThreshold_Type = Counter32
_PppLinkMlMasterLinkAddThreshold_Object = MibTableColumn
pppLinkMlMasterLinkAddThreshold = _PppLinkMlMasterLinkAddThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 6),
    _PppLinkMlMasterLinkAddThreshold_Type()
)
pppLinkMlMasterLinkAddThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterLinkAddThreshold.setStatus("mandatory")
_PppLinkMlMasterSamplingTime_Type = Counter32
_PppLinkMlMasterSamplingTime_Object = MibTableColumn
pppLinkMlMasterSamplingTime = _PppLinkMlMasterSamplingTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 7),
    _PppLinkMlMasterSamplingTime_Type()
)
pppLinkMlMasterSamplingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterSamplingTime.setStatus("mandatory")


class _PppLinkMlMasterSlavesWithBOD_Type(Integer32):
    """Custom type pppLinkMlMasterSlavesWithBOD based on Integer32"""
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


_PppLinkMlMasterSlavesWithBOD_Type.__name__ = "Integer32"
_PppLinkMlMasterSlavesWithBOD_Object = MibTableColumn
pppLinkMlMasterSlavesWithBOD = _PppLinkMlMasterSlavesWithBOD_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 8),
    _PppLinkMlMasterSlavesWithBOD_Type()
)
pppLinkMlMasterSlavesWithBOD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterSlavesWithBOD.setStatus("mandatory")


class _PppLinkMlMasterMeasuringMode_Type(Integer32):
    """Custom type pppLinkMlMasterMeasuringMode based on Integer32"""
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
        *(("all", 4),
          ("none", 1),
          ("rx", 2),
          ("tx", 3))
    )


_PppLinkMlMasterMeasuringMode_Type.__name__ = "Integer32"
_PppLinkMlMasterMeasuringMode_Object = MibTableColumn
pppLinkMlMasterMeasuringMode = _PppLinkMlMasterMeasuringMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 9, 1, 9),
    _PppLinkMlMasterMeasuringMode_Type()
)
pppLinkMlMasterMeasuringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlMasterMeasuringMode.setStatus("mandatory")
_PppLinkMlSlaveTable_Object = MibTable
pppLinkMlSlaveTable = _PppLinkMlSlaveTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 10)
)
if mibBuilder.loadTexts:
    pppLinkMlSlaveTable.setStatus("mandatory")
_PppLinkMlSlaveEntry_Object = MibTableRow
pppLinkMlSlaveEntry = _PppLinkMlSlaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 10, 1)
)
pppLinkMlSlaveEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkMlSlaveIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkMlSlaveEntry.setStatus("mandatory")
_PppLinkMlSlaveIfIndex_Type = Integer32
_PppLinkMlSlaveIfIndex_Object = MibTableColumn
pppLinkMlSlaveIfIndex = _PppLinkMlSlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 10, 1, 1),
    _PppLinkMlSlaveIfIndex_Type()
)
pppLinkMlSlaveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlSlaveIfIndex.setStatus("mandatory")


class _PppLinkMlSlaveBodEnabled_Type(Integer32):
    """Custom type pppLinkMlSlaveBodEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_PppLinkMlSlaveBodEnabled_Type.__name__ = "Integer32"
_PppLinkMlSlaveBodEnabled_Object = MibTableColumn
pppLinkMlSlaveBodEnabled = _PppLinkMlSlaveBodEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 10, 1, 2),
    _PppLinkMlSlaveBodEnabled_Type()
)
pppLinkMlSlaveBodEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlSlaveBodEnabled.setStatus("mandatory")
_PppLinkMlSlaveMasterIfIndex_Type = Integer32
_PppLinkMlSlaveMasterIfIndex_Object = MibTableColumn
pppLinkMlSlaveMasterIfIndex = _PppLinkMlSlaveMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 10, 1, 3),
    _PppLinkMlSlaveMasterIfIndex_Type()
)
pppLinkMlSlaveMasterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkMlSlaveMasterIfIndex.setStatus("mandatory")
_PppLinkBacpTable_Object = MibTable
pppLinkBacpTable = _PppLinkBacpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11)
)
if mibBuilder.loadTexts:
    pppLinkBacpTable.setStatus("mandatory")
_PppLinkBacpEntry_Object = MibTableRow
pppLinkBacpEntry = _PppLinkBacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1)
)
pppLinkBacpEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkBacpIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkBacpEntry.setStatus("mandatory")
_PppLinkBacpIfIndex_Type = Integer32
_PppLinkBacpIfIndex_Object = MibTableColumn
pppLinkBacpIfIndex = _PppLinkBacpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 1),
    _PppLinkBacpIfIndex_Type()
)
pppLinkBacpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpIfIndex.setStatus("mandatory")
_PppLinkBacpMagicInc_Type = Integer32
_PppLinkBacpMagicInc_Object = MibTableColumn
pppLinkBacpMagicInc = _PppLinkBacpMagicInc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 2),
    _PppLinkBacpMagicInc_Type()
)
pppLinkBacpMagicInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpMagicInc.setStatus("mandatory")
_PppLinkBacpMagicOut_Type = Integer32
_PppLinkBacpMagicOut_Object = MibTableColumn
pppLinkBacpMagicOut = _PppLinkBacpMagicOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 3),
    _PppLinkBacpMagicOut_Type()
)
pppLinkBacpMagicOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpMagicOut.setStatus("mandatory")
_PppLinkBacpCallReqTx_Type = Counter32
_PppLinkBacpCallReqTx_Object = MibTableColumn
pppLinkBacpCallReqTx = _PppLinkBacpCallReqTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 4),
    _PppLinkBacpCallReqTx_Type()
)
pppLinkBacpCallReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallReqTx.setStatus("mandatory")
_PppLinkBacpCallReqRx_Type = Counter32
_PppLinkBacpCallReqRx_Object = MibTableColumn
pppLinkBacpCallReqRx = _PppLinkBacpCallReqRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 5),
    _PppLinkBacpCallReqRx_Type()
)
pppLinkBacpCallReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallReqRx.setStatus("mandatory")
_PppLinkBacpCallRespTx_Type = Counter32
_PppLinkBacpCallRespTx_Object = MibTableColumn
pppLinkBacpCallRespTx = _PppLinkBacpCallRespTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 6),
    _PppLinkBacpCallRespTx_Type()
)
pppLinkBacpCallRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallRespTx.setStatus("mandatory")
_PppLinkBacpCallRespRx_Type = Counter32
_PppLinkBacpCallRespRx_Object = MibTableColumn
pppLinkBacpCallRespRx = _PppLinkBacpCallRespRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 7),
    _PppLinkBacpCallRespRx_Type()
)
pppLinkBacpCallRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallRespRx.setStatus("mandatory")
_PppLinkBacpCallbackReqTx_Type = Counter32
_PppLinkBacpCallbackReqTx_Object = MibTableColumn
pppLinkBacpCallbackReqTx = _PppLinkBacpCallbackReqTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 8),
    _PppLinkBacpCallbackReqTx_Type()
)
pppLinkBacpCallbackReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallbackReqTx.setStatus("mandatory")
_PppLinkBacpCallbackReqRx_Type = Counter32
_PppLinkBacpCallbackReqRx_Object = MibTableColumn
pppLinkBacpCallbackReqRx = _PppLinkBacpCallbackReqRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 9),
    _PppLinkBacpCallbackReqRx_Type()
)
pppLinkBacpCallbackReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallbackReqRx.setStatus("mandatory")
_PppLinkBacpCallbackRespTx_Type = Counter32
_PppLinkBacpCallbackRespTx_Object = MibTableColumn
pppLinkBacpCallbackRespTx = _PppLinkBacpCallbackRespTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 10),
    _PppLinkBacpCallbackRespTx_Type()
)
pppLinkBacpCallbackRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallbackRespTx.setStatus("mandatory")
_PppLinkBacpCallbackRespRx_Type = Counter32
_PppLinkBacpCallbackRespRx_Object = MibTableColumn
pppLinkBacpCallbackRespRx = _PppLinkBacpCallbackRespRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 11),
    _PppLinkBacpCallbackRespRx_Type()
)
pppLinkBacpCallbackRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallbackRespRx.setStatus("mandatory")
_PppLinkBacpLinkDropReqTx_Type = Counter32
_PppLinkBacpLinkDropReqTx_Object = MibTableColumn
pppLinkBacpLinkDropReqTx = _PppLinkBacpLinkDropReqTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 12),
    _PppLinkBacpLinkDropReqTx_Type()
)
pppLinkBacpLinkDropReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpLinkDropReqTx.setStatus("mandatory")
_PppLinkBacpLinkDropReqRx_Type = Counter32
_PppLinkBacpLinkDropReqRx_Object = MibTableColumn
pppLinkBacpLinkDropReqRx = _PppLinkBacpLinkDropReqRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 13),
    _PppLinkBacpLinkDropReqRx_Type()
)
pppLinkBacpLinkDropReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpLinkDropReqRx.setStatus("mandatory")
_PppLinkBacpLinkDropRespTx_Type = Counter32
_PppLinkBacpLinkDropRespTx_Object = MibTableColumn
pppLinkBacpLinkDropRespTx = _PppLinkBacpLinkDropRespTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 14),
    _PppLinkBacpLinkDropRespTx_Type()
)
pppLinkBacpLinkDropRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpLinkDropRespTx.setStatus("mandatory")
_PppLinkBacpLinkDropRespRx_Type = Counter32
_PppLinkBacpLinkDropRespRx_Object = MibTableColumn
pppLinkBacpLinkDropRespRx = _PppLinkBacpLinkDropRespRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 15),
    _PppLinkBacpLinkDropRespRx_Type()
)
pppLinkBacpLinkDropRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpLinkDropRespRx.setStatus("mandatory")
_PppLinkBacpCallStatusIndTx_Type = Counter32
_PppLinkBacpCallStatusIndTx_Object = MibTableColumn
pppLinkBacpCallStatusIndTx = _PppLinkBacpCallStatusIndTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 16),
    _PppLinkBacpCallStatusIndTx_Type()
)
pppLinkBacpCallStatusIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallStatusIndTx.setStatus("mandatory")
_PppLinkBacpCallStatusIndRx_Type = Counter32
_PppLinkBacpCallStatusIndRx_Object = MibTableColumn
pppLinkBacpCallStatusIndRx = _PppLinkBacpCallStatusIndRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 17),
    _PppLinkBacpCallStatusIndRx_Type()
)
pppLinkBacpCallStatusIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallStatusIndRx.setStatus("mandatory")
_PppLinkBacpCallStatusRespTx_Type = Counter32
_PppLinkBacpCallStatusRespTx_Object = MibTableColumn
pppLinkBacpCallStatusRespTx = _PppLinkBacpCallStatusRespTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 18),
    _PppLinkBacpCallStatusRespTx_Type()
)
pppLinkBacpCallStatusRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallStatusRespTx.setStatus("mandatory")
_PppLinkBacpCallStatusRespRx_Type = Counter32
_PppLinkBacpCallStatusRespRx_Object = MibTableColumn
pppLinkBacpCallStatusRespRx = _PppLinkBacpCallStatusRespRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 19),
    _PppLinkBacpCallStatusRespRx_Type()
)
pppLinkBacpCallStatusRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpCallStatusRespRx.setStatus("mandatory")
_PppLinkBacpNoFreeSlavesFound_Type = Counter32
_PppLinkBacpNoFreeSlavesFound_Object = MibTableColumn
pppLinkBacpNoFreeSlavesFound = _PppLinkBacpNoFreeSlavesFound_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 20),
    _PppLinkBacpNoFreeSlavesFound_Type()
)
pppLinkBacpNoFreeSlavesFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpNoFreeSlavesFound.setStatus("mandatory")
_PppLinkBacpMaxBundleSizeRejects_Type = Counter32
_PppLinkBacpMaxBundleSizeRejects_Object = MibTableColumn
pppLinkBacpMaxBundleSizeRejects = _PppLinkBacpMaxBundleSizeRejects_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 21),
    _PppLinkBacpMaxBundleSizeRejects_Type()
)
pppLinkBacpMaxBundleSizeRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpMaxBundleSizeRejects.setStatus("mandatory")
_PppLinkBacpChannelLackDisconnects_Type = Counter32
_PppLinkBacpChannelLackDisconnects_Object = MibTableColumn
pppLinkBacpChannelLackDisconnects = _PppLinkBacpChannelLackDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 22),
    _PppLinkBacpChannelLackDisconnects_Type()
)
pppLinkBacpChannelLackDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpChannelLackDisconnects.setStatus("mandatory")


class _PppLinkBacpOldProtocolIdsUsed_Type(Integer32):
    """Custom type pppLinkBacpOldProtocolIdsUsed based on Integer32"""
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


_PppLinkBacpOldProtocolIdsUsed_Type.__name__ = "Integer32"
_PppLinkBacpOldProtocolIdsUsed_Object = MibTableColumn
pppLinkBacpOldProtocolIdsUsed = _PppLinkBacpOldProtocolIdsUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 11, 1, 23),
    _PppLinkBacpOldProtocolIdsUsed_Type()
)
pppLinkBacpOldProtocolIdsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkBacpOldProtocolIdsUsed.setStatus("mandatory")
_PppLinkIpcpTable_Object = MibTable
pppLinkIpcpTable = _PppLinkIpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 12)
)
if mibBuilder.loadTexts:
    pppLinkIpcpTable.setStatus("mandatory")
_PppLinkIpcpEntry_Object = MibTableRow
pppLinkIpcpEntry = _PppLinkIpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 12, 1)
)
pppLinkIpcpEntry.setIndexNames(
    (0, "INTEL-PPP-MIB", "pppLinkIpcpIfIndex"),
)
if mibBuilder.loadTexts:
    pppLinkIpcpEntry.setStatus("mandatory")
_PppLinkIpcpIfIndex_Type = Integer32
_PppLinkIpcpIfIndex_Object = MibTableColumn
pppLinkIpcpIfIndex = _PppLinkIpcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 12, 1, 1),
    _PppLinkIpcpIfIndex_Type()
)
pppLinkIpcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkIpcpIfIndex.setStatus("mandatory")
_PppLinkIpcpIpAddressLocal_Type = IpAddress
_PppLinkIpcpIpAddressLocal_Object = MibTableColumn
pppLinkIpcpIpAddressLocal = _PppLinkIpcpIpAddressLocal_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 12, 1, 2),
    _PppLinkIpcpIpAddressLocal_Type()
)
pppLinkIpcpIpAddressLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkIpcpIpAddressLocal.setStatus("mandatory")
_PppLinkIpcpIpAddressRemote_Type = IpAddress
_PppLinkIpcpIpAddressRemote_Object = MibTableColumn
pppLinkIpcpIpAddressRemote = _PppLinkIpcpIpAddressRemote_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 23, 1, 12, 1, 3),
    _PppLinkIpcpIpAddressRemote_Type()
)
pppLinkIpcpIpAddressRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkIpcpIpAddressRemote.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-PPP-MIB",
    **{"PppProtocolState": PppProtocolState,
       "ppp": ppp,
       "pppLink": pppLink,
       "pppLinkProtoStateTable": pppLinkProtoStateTable,
       "pppLinkProtoStateEntry": pppLinkProtoStateEntry,
       "pppLinkProtoStateIfIndex": pppLinkProtoStateIfIndex,
       "pppLinkProtoStatePppLinkType": pppLinkProtoStatePppLinkType,
       "pppLinkProtoStateLcpState": pppLinkProtoStateLcpState,
       "pppLinkProtoStateIpcpState": pppLinkProtoStateIpcpState,
       "pppLinkProtoStateIpxcpState": pppLinkProtoStateIpxcpState,
       "pppLinkProtoStateBcpState": pppLinkProtoStateBcpState,
       "pppLinkProtoStateCcpState": pppLinkProtoStateCcpState,
       "pppLinkProtoStateEcpState": pppLinkProtoStateEcpState,
       "pppLinkProtoStateBacpState": pppLinkProtoStateBacpState,
       "pppLinkLcpTable": pppLinkLcpTable,
       "pppLinkLcpEntry": pppLinkLcpEntry,
       "pppLinkLcpIfIndex": pppLinkLcpIfIndex,
       "pppLinkLcpMRUInc": pppLinkLcpMRUInc,
       "pppLinkLcpMRUOut": pppLinkLcpMRUOut,
       "pppLinkLcpACCMapInc": pppLinkLcpACCMapInc,
       "pppLinkLcpACCMapOut": pppLinkLcpACCMapOut,
       "pppLinkProtocolCompressionInc": pppLinkProtocolCompressionInc,
       "pppLinkProtocolCompressionOut": pppLinkProtocolCompressionOut,
       "pppLinkACCompressionInc": pppLinkACCompressionInc,
       "pppLinkACCompressionOut": pppLinkACCompressionOut,
       "pppLinkMagicNumberInc": pppLinkMagicNumberInc,
       "pppLinkMagicNumberOut": pppLinkMagicNumberOut,
       "pppLinkLinkDiscriminatorInc": pppLinkLinkDiscriminatorInc,
       "pppLinkLinkDiscriminatorOut": pppLinkLinkDiscriminatorOut,
       "pppLinkBcpTable": pppLinkBcpTable,
       "pppLinkBcpEntry": pppLinkBcpEntry,
       "pppLinkBcpIfIndex": pppLinkBcpIfIndex,
       "pppLinkBcpMACTypeInc": pppLinkBcpMACTypeInc,
       "pppLinkBcpMACTypeOut": pppLinkBcpMACTypeOut,
       "pppLinkBcpBridgingProtInc": pppLinkBcpBridgingProtInc,
       "pppLinkBcpBridgingProtOut": pppLinkBcpBridgingProtOut,
       "pppLinkCcpTable": pppLinkCcpTable,
       "pppLinkCcpEntry": pppLinkCcpEntry,
       "pppLinkCcpIfIndex": pppLinkCcpIfIndex,
       "pppLinkCcpHistorySizeIncoming": pppLinkCcpHistorySizeIncoming,
       "pppLinkCcpHistorySizeOutgoing": pppLinkCcpHistorySizeOutgoing,
       "pppLinkCcpCheckTypeIncoming": pppLinkCcpCheckTypeIncoming,
       "pppLinkCcpCheckTypeOutgoing": pppLinkCcpCheckTypeOutgoing,
       "pppLinkEcpTable": pppLinkEcpTable,
       "pppLinkEcpEntry": pppLinkEcpEntry,
       "pppLinkEcpIfIndex": pppLinkEcpIfIndex,
       "pppLinkEcpResetRequestsRx": pppLinkEcpResetRequestsRx,
       "pppLinkEcpResetRequestsTx": pppLinkEcpResetRequestsTx,
       "pppLinkEcpResetAcksRx": pppLinkEcpResetAcksRx,
       "pppLinkEcpResetAcksTx": pppLinkEcpResetAcksTx,
       "pppLinkEcpRxDiscarded": pppLinkEcpRxDiscarded,
       "pppLinkEcpTxDiscarded": pppLinkEcpTxDiscarded,
       "pppLinkEcpReceiverState": pppLinkEcpReceiverState,
       "pppLinkCompTable": pppLinkCompTable,
       "pppLinkCompEntry": pppLinkCompEntry,
       "pppLinkCompIfIndex": pppLinkCompIfIndex,
       "pppLinkCompDecoderBytesIn": pppLinkCompDecoderBytesIn,
       "pppLinkCompDecoderDecompBytesOut": pppLinkCompDecoderDecompBytesOut,
       "pppLinkCompDecoderUncompBytesOut": pppLinkCompDecoderUncompBytesOut,
       "pppLinkCompDecoderCompPacketsIn": pppLinkCompDecoderCompPacketsIn,
       "pppLinkCompDecoderUncompPacketsIn": pppLinkCompDecoderUncompPacketsIn,
       "pppLinkCompDecoderDecompQueueLength": pppLinkCompDecoderDecompQueueLength,
       "pppLinkCompDecoderCompressionRatio": pppLinkCompDecoderCompressionRatio,
       "pppLinkCompDecoderResetRequestTx": pppLinkCompDecoderResetRequestTx,
       "pppLinkCompDecoderResetAcksRx": pppLinkCompDecoderResetAcksRx,
       "pppLinkCompDecoderRxDiscarded": pppLinkCompDecoderRxDiscarded,
       "pppLinkCompDecoderState": pppLinkCompDecoderState,
       "pppLinkCompEncoderBytesIn": pppLinkCompEncoderBytesIn,
       "pppLinkCompEncoderCompBytesOut": pppLinkCompEncoderCompBytesOut,
       "pppLinkCompEncoderUncompBytesOut": pppLinkCompEncoderUncompBytesOut,
       "pppLinkCompEncoderCompPacketsOut": pppLinkCompEncoderCompPacketsOut,
       "pppLinkCompEncoderUncompPacketsOut": pppLinkCompEncoderUncompPacketsOut,
       "pppLinkCompEncoderCompQueueLength": pppLinkCompEncoderCompQueueLength,
       "pppLinkCompEncoderCompressionRation": pppLinkCompEncoderCompressionRation,
       "pppLinkCompEncoderResetRequestRx": pppLinkCompEncoderResetRequestRx,
       "pppLinkCompEncoderResetAckTx": pppLinkCompEncoderResetAckTx,
       "pppLinkCompEncoderTxDiscarded": pppLinkCompEncoderTxDiscarded,
       "pppLinkCompDecoderBytesInUpper": pppLinkCompDecoderBytesInUpper,
       "pppLinkCompDecoderDecompBytesOutUpper": pppLinkCompDecoderDecompBytesOutUpper,
       "pppLinkCompDecoderUncompBytesOutUpper": pppLinkCompDecoderUncompBytesOutUpper,
       "pppLinkCompEncoderBytesInUpper": pppLinkCompEncoderBytesInUpper,
       "pppLinkCompEncoderCompBytesOutUpper": pppLinkCompEncoderCompBytesOutUpper,
       "pppLinkCompEncoderUncompBytesOutUpper": pppLinkCompEncoderUncompBytesOutUpper,
       "pppLinkChapTable": pppLinkChapTable,
       "pppLinkChapEntry": pppLinkChapEntry,
       "pppLinkChapIfIndex": pppLinkChapIfIndex,
       "pppLinkChapIncoming": pppLinkChapIncoming,
       "pppLinkChapOutgoing": pppLinkChapOutgoing,
       "pppLinkChapChallengeRx": pppLinkChapChallengeRx,
       "pppLinkChapChallengeTx": pppLinkChapChallengeTx,
       "pppLinkChapResponseRx": pppLinkChapResponseRx,
       "pppLinkChapResponseTx": pppLinkChapResponseTx,
       "pppLinkChapSuccesRx": pppLinkChapSuccesRx,
       "pppLinkChapSuccesTx": pppLinkChapSuccesTx,
       "pppLinkChapFailureRx": pppLinkChapFailureRx,
       "pppLinkChapFailureTx": pppLinkChapFailureTx,
       "pppLinkPapTable": pppLinkPapTable,
       "pppLinkPapEntry": pppLinkPapEntry,
       "pppLinkPapIfIndex": pppLinkPapIfIndex,
       "pppLinkPapIncoming": pppLinkPapIncoming,
       "pppLinkPapOutgoing": pppLinkPapOutgoing,
       "pppLinkPapAuthReqRx": pppLinkPapAuthReqRx,
       "pppLinkPapAuthReqTx": pppLinkPapAuthReqTx,
       "pppLinkPapAuthAckRx": pppLinkPapAuthAckRx,
       "pppLinkPapAuthAckTx": pppLinkPapAuthAckTx,
       "pppLinkPapAuthNackRx": pppLinkPapAuthNackRx,
       "pppLinkPapAuthNackTx": pppLinkPapAuthNackTx,
       "pppLinkMlMasterTable": pppLinkMlMasterTable,
       "pppLinkMlMasterEntry": pppLinkMlMasterEntry,
       "pppLinkMlMasterIfIndex": pppLinkMlMasterIfIndex,
       "pppLinkMlMasterSlaveCount": pppLinkMlMasterSlaveCount,
       "pppLinkMlMasterTxUtilization": pppLinkMlMasterTxUtilization,
       "pppLinkMlMasterRxUtilization": pppLinkMlMasterRxUtilization,
       "pppLinkMlMasterSlavesForwarding": pppLinkMlMasterSlavesForwarding,
       "pppLinkMlMasterLinkAddThreshold": pppLinkMlMasterLinkAddThreshold,
       "pppLinkMlMasterSamplingTime": pppLinkMlMasterSamplingTime,
       "pppLinkMlMasterSlavesWithBOD": pppLinkMlMasterSlavesWithBOD,
       "pppLinkMlMasterMeasuringMode": pppLinkMlMasterMeasuringMode,
       "pppLinkMlSlaveTable": pppLinkMlSlaveTable,
       "pppLinkMlSlaveEntry": pppLinkMlSlaveEntry,
       "pppLinkMlSlaveIfIndex": pppLinkMlSlaveIfIndex,
       "pppLinkMlSlaveBodEnabled": pppLinkMlSlaveBodEnabled,
       "pppLinkMlSlaveMasterIfIndex": pppLinkMlSlaveMasterIfIndex,
       "pppLinkBacpTable": pppLinkBacpTable,
       "pppLinkBacpEntry": pppLinkBacpEntry,
       "pppLinkBacpIfIndex": pppLinkBacpIfIndex,
       "pppLinkBacpMagicInc": pppLinkBacpMagicInc,
       "pppLinkBacpMagicOut": pppLinkBacpMagicOut,
       "pppLinkBacpCallReqTx": pppLinkBacpCallReqTx,
       "pppLinkBacpCallReqRx": pppLinkBacpCallReqRx,
       "pppLinkBacpCallRespTx": pppLinkBacpCallRespTx,
       "pppLinkBacpCallRespRx": pppLinkBacpCallRespRx,
       "pppLinkBacpCallbackReqTx": pppLinkBacpCallbackReqTx,
       "pppLinkBacpCallbackReqRx": pppLinkBacpCallbackReqRx,
       "pppLinkBacpCallbackRespTx": pppLinkBacpCallbackRespTx,
       "pppLinkBacpCallbackRespRx": pppLinkBacpCallbackRespRx,
       "pppLinkBacpLinkDropReqTx": pppLinkBacpLinkDropReqTx,
       "pppLinkBacpLinkDropReqRx": pppLinkBacpLinkDropReqRx,
       "pppLinkBacpLinkDropRespTx": pppLinkBacpLinkDropRespTx,
       "pppLinkBacpLinkDropRespRx": pppLinkBacpLinkDropRespRx,
       "pppLinkBacpCallStatusIndTx": pppLinkBacpCallStatusIndTx,
       "pppLinkBacpCallStatusIndRx": pppLinkBacpCallStatusIndRx,
       "pppLinkBacpCallStatusRespTx": pppLinkBacpCallStatusRespTx,
       "pppLinkBacpCallStatusRespRx": pppLinkBacpCallStatusRespRx,
       "pppLinkBacpNoFreeSlavesFound": pppLinkBacpNoFreeSlavesFound,
       "pppLinkBacpMaxBundleSizeRejects": pppLinkBacpMaxBundleSizeRejects,
       "pppLinkBacpChannelLackDisconnects": pppLinkBacpChannelLackDisconnects,
       "pppLinkBacpOldProtocolIdsUsed": pppLinkBacpOldProtocolIdsUsed,
       "pppLinkIpcpTable": pppLinkIpcpTable,
       "pppLinkIpcpEntry": pppLinkIpcpEntry,
       "pppLinkIpcpIfIndex": pppLinkIpcpIfIndex,
       "pppLinkIpcpIpAddressLocal": pppLinkIpcpIpAddressLocal,
       "pppLinkIpcpIpAddressRemote": pppLinkIpcpIpAddressRemote}
)
