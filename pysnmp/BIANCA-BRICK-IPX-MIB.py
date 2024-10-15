# SNMP MIB module (BIANCA-BRICK-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:31 2024
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

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboipx_ObjectIdentity = ObjectIdentity
biboipx = _Biboipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 9)
)
_IpxClientTable_Object = MibTable
ipxClientTable = _IpxClientTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ipxClientTable.setStatus("mandatory")
_IpxClientEntry_Object = MibTableRow
ipxClientEntry = _IpxClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1)
)
ipxClientEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPX-MIB", "ipxClientCircIndex"),
)
if mibBuilder.loadTexts:
    ipxClientEntry.setStatus("mandatory")


class _IpxClientNode_Type(OctetString):
    """Custom type ipxClientNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxClientNode_Type.__name__ = "OctetString"
_IpxClientNode_Object = MibTableColumn
ipxClientNode = _IpxClientNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1, 1),
    _IpxClientNode_Type()
)
ipxClientNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxClientNode.setStatus("mandatory")
_IpxClientCircIndex_Type = Integer32
_IpxClientCircIndex_Object = MibTableColumn
ipxClientCircIndex = _IpxClientCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1, 2),
    _IpxClientCircIndex_Type()
)
ipxClientCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxClientCircIndex.setStatus("mandatory")
_IpxClientReconns_Type = Counter32
_IpxClientReconns_Object = MibTableColumn
ipxClientReconns = _IpxClientReconns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 1, 1, 3),
    _IpxClientReconns_Type()
)
ipxClientReconns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxClientReconns.setStatus("mandatory")
_IpxAllowTable_Object = MibTable
ipxAllowTable = _IpxAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2)
)
if mibBuilder.loadTexts:
    ipxAllowTable.setStatus("mandatory")
_IpxAllowEntry_Object = MibTableRow
ipxAllowEntry = _IpxAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1)
)
ipxAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPX-MIB", "ipxAllowPktTypeMode"),
    (0, "BIANCA-BRICK-IPX-MIB", "ipxAllowSrcIfIndexMode"),
)
if mibBuilder.loadTexts:
    ipxAllowEntry.setStatus("mandatory")


class _IpxAllowPktTypeMode_Type(Integer32):
    """Custom type ipxAllowPktTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowPktTypeMode_Type.__name__ = "Integer32"
_IpxAllowPktTypeMode_Object = MibTableColumn
ipxAllowPktTypeMode = _IpxAllowPktTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 1),
    _IpxAllowPktTypeMode_Type()
)
ipxAllowPktTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowPktTypeMode.setStatus("mandatory")


class _IpxAllowPktType_Type(Integer32):
    """Custom type ipxAllowPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              17,
              20,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ncp", 17),
          ("netbios", 20),
          ("rip", 1),
          ("sap", 4),
          ("spx", 5),
          ("unknown", 256))
    )


_IpxAllowPktType_Type.__name__ = "Integer32"
_IpxAllowPktType_Object = MibTableColumn
ipxAllowPktType = _IpxAllowPktType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 2),
    _IpxAllowPktType_Type()
)
ipxAllowPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowPktType.setStatus("mandatory")


class _IpxAllowDstIfStatus_Type(Integer32):
    """Custom type ipxAllowDstIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("up", 2))
    )


_IpxAllowDstIfStatus_Type.__name__ = "Integer32"
_IpxAllowDstIfStatus_Object = MibTableColumn
ipxAllowDstIfStatus = _IpxAllowDstIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 3),
    _IpxAllowDstIfStatus_Type()
)
ipxAllowDstIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstIfStatus.setStatus("mandatory")


class _IpxAllowDstNetMode_Type(Integer32):
    """Custom type ipxAllowDstNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowDstNetMode_Type.__name__ = "Integer32"
_IpxAllowDstNetMode_Object = MibTableColumn
ipxAllowDstNetMode = _IpxAllowDstNetMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 4),
    _IpxAllowDstNetMode_Type()
)
ipxAllowDstNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstNetMode.setStatus("mandatory")
_IpxAllowDstNet_Type = Integer32
_IpxAllowDstNet_Object = MibTableColumn
ipxAllowDstNet = _IpxAllowDstNet_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 5),
    _IpxAllowDstNet_Type()
)
ipxAllowDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstNet.setStatus("mandatory")


class _IpxAllowDstNodeMode_Type(Integer32):
    """Custom type ipxAllowDstNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowDstNodeMode_Type.__name__ = "Integer32"
_IpxAllowDstNodeMode_Object = MibTableColumn
ipxAllowDstNodeMode = _IpxAllowDstNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 6),
    _IpxAllowDstNodeMode_Type()
)
ipxAllowDstNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstNodeMode.setStatus("mandatory")


class _IpxAllowDstNode_Type(OctetString):
    """Custom type ipxAllowDstNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxAllowDstNode_Type.__name__ = "OctetString"
_IpxAllowDstNode_Object = MibTableColumn
ipxAllowDstNode = _IpxAllowDstNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 7),
    _IpxAllowDstNode_Type()
)
ipxAllowDstNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstNode.setStatus("mandatory")


class _IpxAllowDstSockMode_Type(Integer32):
    """Custom type ipxAllowDstSockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowDstSockMode_Type.__name__ = "Integer32"
_IpxAllowDstSockMode_Object = MibTableColumn
ipxAllowDstSockMode = _IpxAllowDstSockMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 8),
    _IpxAllowDstSockMode_Type()
)
ipxAllowDstSockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstSockMode.setStatus("mandatory")
_IpxAllowDstSock_Type = Integer32
_IpxAllowDstSock_Object = MibTableColumn
ipxAllowDstSock = _IpxAllowDstSock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 9),
    _IpxAllowDstSock_Type()
)
ipxAllowDstSock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowDstSock.setStatus("mandatory")


class _IpxAllowSrcIfIndexMode_Type(Integer32):
    """Custom type ipxAllowSrcIfIndexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowSrcIfIndexMode_Type.__name__ = "Integer32"
_IpxAllowSrcIfIndexMode_Object = MibTableColumn
ipxAllowSrcIfIndexMode = _IpxAllowSrcIfIndexMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 10),
    _IpxAllowSrcIfIndexMode_Type()
)
ipxAllowSrcIfIndexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcIfIndexMode.setStatus("mandatory")
_IpxAllowSrcIfIndex_Type = Integer32
_IpxAllowSrcIfIndex_Object = MibTableColumn
ipxAllowSrcIfIndex = _IpxAllowSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 11),
    _IpxAllowSrcIfIndex_Type()
)
ipxAllowSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcIfIndex.setStatus("mandatory")


class _IpxAllowSrcNetMode_Type(Integer32):
    """Custom type ipxAllowSrcNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowSrcNetMode_Type.__name__ = "Integer32"
_IpxAllowSrcNetMode_Object = MibTableColumn
ipxAllowSrcNetMode = _IpxAllowSrcNetMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 12),
    _IpxAllowSrcNetMode_Type()
)
ipxAllowSrcNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcNetMode.setStatus("mandatory")
_IpxAllowSrcNet_Type = Integer32
_IpxAllowSrcNet_Object = MibTableColumn
ipxAllowSrcNet = _IpxAllowSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 13),
    _IpxAllowSrcNet_Type()
)
ipxAllowSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcNet.setStatus("mandatory")


class _IpxAllowSrcNodeMode_Type(Integer32):
    """Custom type ipxAllowSrcNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowSrcNodeMode_Type.__name__ = "Integer32"
_IpxAllowSrcNodeMode_Object = MibTableColumn
ipxAllowSrcNodeMode = _IpxAllowSrcNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 14),
    _IpxAllowSrcNodeMode_Type()
)
ipxAllowSrcNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcNodeMode.setStatus("mandatory")


class _IpxAllowSrcNode_Type(OctetString):
    """Custom type ipxAllowSrcNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxAllowSrcNode_Type.__name__ = "OctetString"
_IpxAllowSrcNode_Object = MibTableColumn
ipxAllowSrcNode = _IpxAllowSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 15),
    _IpxAllowSrcNode_Type()
)
ipxAllowSrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcNode.setStatus("mandatory")


class _IpxAllowSrcSockMode_Type(Integer32):
    """Custom type ipxAllowSrcSockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxAllowSrcSockMode_Type.__name__ = "Integer32"
_IpxAllowSrcSockMode_Object = MibTableColumn
ipxAllowSrcSockMode = _IpxAllowSrcSockMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 16),
    _IpxAllowSrcSockMode_Type()
)
ipxAllowSrcSockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcSockMode.setStatus("mandatory")
_IpxAllowSrcSock_Type = Integer32
_IpxAllowSrcSock_Object = MibTableColumn
ipxAllowSrcSock = _IpxAllowSrcSock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 2, 1, 17),
    _IpxAllowSrcSock_Type()
)
ipxAllowSrcSock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAllowSrcSock.setStatus("mandatory")
_IpxDenyTable_Object = MibTable
ipxDenyTable = _IpxDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3)
)
if mibBuilder.loadTexts:
    ipxDenyTable.setStatus("mandatory")
_IpxDenyEntry_Object = MibTableRow
ipxDenyEntry = _IpxDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1)
)
ipxDenyEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPX-MIB", "ipxDenyPktTypeMode"),
    (0, "BIANCA-BRICK-IPX-MIB", "ipxDenySrcIfIndexMode"),
)
if mibBuilder.loadTexts:
    ipxDenyEntry.setStatus("mandatory")


class _IpxDenyPktTypeMode_Type(Integer32):
    """Custom type ipxDenyPktTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenyPktTypeMode_Type.__name__ = "Integer32"
_IpxDenyPktTypeMode_Object = MibTableColumn
ipxDenyPktTypeMode = _IpxDenyPktTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 1),
    _IpxDenyPktTypeMode_Type()
)
ipxDenyPktTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyPktTypeMode.setStatus("mandatory")


class _IpxDenyPktType_Type(Integer32):
    """Custom type ipxDenyPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              17,
              20,
              256)
        )
    )
    namedValues = NamedValues(
        *(("ncp", 17),
          ("netbios", 20),
          ("rip", 1),
          ("sap", 4),
          ("spx", 5),
          ("unknown", 256))
    )


_IpxDenyPktType_Type.__name__ = "Integer32"
_IpxDenyPktType_Object = MibTableColumn
ipxDenyPktType = _IpxDenyPktType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 2),
    _IpxDenyPktType_Type()
)
ipxDenyPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyPktType.setStatus("mandatory")


class _IpxDenyDstIfStatus_Type(Integer32):
    """Custom type ipxDenyDstIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("dormant", 2))
    )


_IpxDenyDstIfStatus_Type.__name__ = "Integer32"
_IpxDenyDstIfStatus_Object = MibTableColumn
ipxDenyDstIfStatus = _IpxDenyDstIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 3),
    _IpxDenyDstIfStatus_Type()
)
ipxDenyDstIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstIfStatus.setStatus("mandatory")


class _IpxDenyDstNetMode_Type(Integer32):
    """Custom type ipxDenyDstNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenyDstNetMode_Type.__name__ = "Integer32"
_IpxDenyDstNetMode_Object = MibTableColumn
ipxDenyDstNetMode = _IpxDenyDstNetMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 4),
    _IpxDenyDstNetMode_Type()
)
ipxDenyDstNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstNetMode.setStatus("mandatory")
_IpxDenyDstNet_Type = Integer32
_IpxDenyDstNet_Object = MibTableColumn
ipxDenyDstNet = _IpxDenyDstNet_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 5),
    _IpxDenyDstNet_Type()
)
ipxDenyDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstNet.setStatus("mandatory")


class _IpxDenyDstNodeMode_Type(Integer32):
    """Custom type ipxDenyDstNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenyDstNodeMode_Type.__name__ = "Integer32"
_IpxDenyDstNodeMode_Object = MibTableColumn
ipxDenyDstNodeMode = _IpxDenyDstNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 6),
    _IpxDenyDstNodeMode_Type()
)
ipxDenyDstNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstNodeMode.setStatus("mandatory")


class _IpxDenyDstNode_Type(OctetString):
    """Custom type ipxDenyDstNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxDenyDstNode_Type.__name__ = "OctetString"
_IpxDenyDstNode_Object = MibTableColumn
ipxDenyDstNode = _IpxDenyDstNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 7),
    _IpxDenyDstNode_Type()
)
ipxDenyDstNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstNode.setStatus("mandatory")


class _IpxDenyDstSockMode_Type(Integer32):
    """Custom type ipxDenyDstSockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenyDstSockMode_Type.__name__ = "Integer32"
_IpxDenyDstSockMode_Object = MibTableColumn
ipxDenyDstSockMode = _IpxDenyDstSockMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 8),
    _IpxDenyDstSockMode_Type()
)
ipxDenyDstSockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstSockMode.setStatus("mandatory")
_IpxDenyDstSock_Type = Integer32
_IpxDenyDstSock_Object = MibTableColumn
ipxDenyDstSock = _IpxDenyDstSock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 9),
    _IpxDenyDstSock_Type()
)
ipxDenyDstSock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenyDstSock.setStatus("mandatory")


class _IpxDenySrcIfIndexMode_Type(Integer32):
    """Custom type ipxDenySrcIfIndexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenySrcIfIndexMode_Type.__name__ = "Integer32"
_IpxDenySrcIfIndexMode_Object = MibTableColumn
ipxDenySrcIfIndexMode = _IpxDenySrcIfIndexMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 10),
    _IpxDenySrcIfIndexMode_Type()
)
ipxDenySrcIfIndexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcIfIndexMode.setStatus("mandatory")
_IpxDenySrcIfIndex_Type = Integer32
_IpxDenySrcIfIndex_Object = MibTableColumn
ipxDenySrcIfIndex = _IpxDenySrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 11),
    _IpxDenySrcIfIndex_Type()
)
ipxDenySrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcIfIndex.setStatus("mandatory")


class _IpxDenySrcNetMode_Type(Integer32):
    """Custom type ipxDenySrcNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenySrcNetMode_Type.__name__ = "Integer32"
_IpxDenySrcNetMode_Object = MibTableColumn
ipxDenySrcNetMode = _IpxDenySrcNetMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 12),
    _IpxDenySrcNetMode_Type()
)
ipxDenySrcNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcNetMode.setStatus("mandatory")
_IpxDenySrcNet_Type = Integer32
_IpxDenySrcNet_Object = MibTableColumn
ipxDenySrcNet = _IpxDenySrcNet_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 13),
    _IpxDenySrcNet_Type()
)
ipxDenySrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcNet.setStatus("mandatory")


class _IpxDenySrcNodeMode_Type(Integer32):
    """Custom type ipxDenySrcNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenySrcNodeMode_Type.__name__ = "Integer32"
_IpxDenySrcNodeMode_Object = MibTableColumn
ipxDenySrcNodeMode = _IpxDenySrcNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 14),
    _IpxDenySrcNodeMode_Type()
)
ipxDenySrcNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcNodeMode.setStatus("mandatory")


class _IpxDenySrcNode_Type(OctetString):
    """Custom type ipxDenySrcNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxDenySrcNode_Type.__name__ = "OctetString"
_IpxDenySrcNode_Object = MibTableColumn
ipxDenySrcNode = _IpxDenySrcNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 15),
    _IpxDenySrcNode_Type()
)
ipxDenySrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcNode.setStatus("mandatory")


class _IpxDenySrcSockMode_Type(Integer32):
    """Custom type ipxDenySrcSockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_IpxDenySrcSockMode_Type.__name__ = "Integer32"
_IpxDenySrcSockMode_Object = MibTableColumn
ipxDenySrcSockMode = _IpxDenySrcSockMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 16),
    _IpxDenySrcSockMode_Type()
)
ipxDenySrcSockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcSockMode.setStatus("mandatory")
_IpxDenySrcSock_Type = Integer32
_IpxDenySrcSock_Object = MibTableColumn
ipxDenySrcSock = _IpxDenySrcSock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 3, 1, 17),
    _IpxDenySrcSock_Type()
)
ipxDenySrcSock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDenySrcSock.setStatus("mandatory")
_IpxAdmin_ObjectIdentity = ObjectIdentity
ipxAdmin = _IpxAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4)
)


class _IpxAdmSpxSpoofing_Type(Integer32):
    """Custom type ipxAdmSpxSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpxAdmSpxSpoofing_Type.__name__ = "Integer32"
_IpxAdmSpxSpoofing_Object = MibScalar
ipxAdmSpxSpoofing = _IpxAdmSpxSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 1),
    _IpxAdmSpxSpoofing_Type()
)
ipxAdmSpxSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmSpxSpoofing.setStatus("mandatory")


class _IpxAdmIpxSpoofing_Type(Integer32):
    """Custom type ipxAdmIpxSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IpxAdmIpxSpoofing_Type.__name__ = "Integer32"
_IpxAdmIpxSpoofing_Object = MibScalar
ipxAdmIpxSpoofing = _IpxAdmIpxSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 2),
    _IpxAdmIpxSpoofing_Type()
)
ipxAdmIpxSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmIpxSpoofing.setStatus("mandatory")


class _IpxAdmNETBIOSRepl_Type(Integer32):
    """Custom type ipxAdmNETBIOSRepl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan-only", 3),
          ("off", 2),
          ("on", 1))
    )


_IpxAdmNETBIOSRepl_Type.__name__ = "Integer32"
_IpxAdmNETBIOSRepl_Object = MibScalar
ipxAdmNETBIOSRepl = _IpxAdmNETBIOSRepl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 3),
    _IpxAdmNETBIOSRepl_Type()
)
ipxAdmNETBIOSRepl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmNETBIOSRepl.setStatus("mandatory")
_IpxAdmSpxVerTimeout_Type = Integer32
_IpxAdmSpxVerTimeout_Object = MibScalar
ipxAdmSpxVerTimeout = _IpxAdmSpxVerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 4),
    _IpxAdmSpxVerTimeout_Type()
)
ipxAdmSpxVerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmSpxVerTimeout.setStatus("mandatory")
_IpxAdmSpxAbrTimeout_Type = Integer32
_IpxAdmSpxAbrTimeout_Object = MibScalar
ipxAdmSpxAbrTimeout = _IpxAdmSpxAbrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 5),
    _IpxAdmSpxAbrTimeout_Type()
)
ipxAdmSpxAbrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmSpxAbrTimeout.setStatus("mandatory")
_IpxAdmRIPSAPOffset_Type = Integer32
_IpxAdmRIPSAPOffset_Object = MibScalar
ipxAdmRIPSAPOffset = _IpxAdmRIPSAPOffset_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 6),
    _IpxAdmRIPSAPOffset_Type()
)
ipxAdmRIPSAPOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmRIPSAPOffset.setStatus("mandatory")


class _IpxAdmLearnStatics_Type(Integer32):
    """Custom type ipxAdmLearnStatics based on Integer32"""
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
        *(("both", 4),
          ("done", 1),
          ("rip", 2),
          ("sap", 3))
    )


_IpxAdmLearnStatics_Type.__name__ = "Integer32"
_IpxAdmLearnStatics_Object = MibScalar
ipxAdmLearnStatics = _IpxAdmLearnStatics_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 7),
    _IpxAdmLearnStatics_Type()
)
ipxAdmLearnStatics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdmLearnStatics.setStatus("mandatory")
_IpxAdmSpxConns_Type = Integer32
_IpxAdmSpxConns_Object = MibScalar
ipxAdmSpxConns = _IpxAdmSpxConns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 4, 8),
    _IpxAdmSpxConns_Type()
)
ipxAdmSpxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdmSpxConns.setStatus("mandatory")
_SapAllowTable_Object = MibTable
sapAllowTable = _SapAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5)
)
if mibBuilder.loadTexts:
    sapAllowTable.setStatus("mandatory")
_SapAllowEntry_Object = MibTableRow
sapAllowEntry = _SapAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1)
)
sapAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPX-MIB", "sapAllowIfIndex"),
)
if mibBuilder.loadTexts:
    sapAllowEntry.setStatus("mandatory")


class _SapAllowIfIndexMode_Type(Integer32):
    """Custom type sapAllowIfIndexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("dont-verify", 1),
          ("verify", 2))
    )


_SapAllowIfIndexMode_Type.__name__ = "Integer32"
_SapAllowIfIndexMode_Object = MibTableColumn
sapAllowIfIndexMode = _SapAllowIfIndexMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 1),
    _SapAllowIfIndexMode_Type()
)
sapAllowIfIndexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowIfIndexMode.setStatus("mandatory")
_SapAllowIfIndex_Type = Integer32
_SapAllowIfIndex_Object = MibTableColumn
sapAllowIfIndex = _SapAllowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 2),
    _SapAllowIfIndex_Type()
)
sapAllowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowIfIndex.setStatus("mandatory")


class _SapAllowDirection_Type(Integer32):
    """Custom type sapAllowDirection based on Integer32"""
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
        *(("both", 4),
          ("dont-verify", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_SapAllowDirection_Type.__name__ = "Integer32"
_SapAllowDirection_Object = MibTableColumn
sapAllowDirection = _SapAllowDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 3),
    _SapAllowDirection_Type()
)
sapAllowDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowDirection.setStatus("mandatory")


class _SapAllowTypeMode_Type(Integer32):
    """Custom type sapAllowTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapAllowTypeMode_Type.__name__ = "Integer32"
_SapAllowTypeMode_Object = MibTableColumn
sapAllowTypeMode = _SapAllowTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 4),
    _SapAllowTypeMode_Type()
)
sapAllowTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowTypeMode.setStatus("mandatory")


class _SapAllowType_Type(OctetString):
    """Custom type sapAllowType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SapAllowType_Type.__name__ = "OctetString"
_SapAllowType_Object = MibTableColumn
sapAllowType = _SapAllowType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 5),
    _SapAllowType_Type()
)
sapAllowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowType.setStatus("mandatory")


class _SapAllowNetMode_Type(Integer32):
    """Custom type sapAllowNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapAllowNetMode_Type.__name__ = "Integer32"
_SapAllowNetMode_Object = MibTableColumn
sapAllowNetMode = _SapAllowNetMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 6),
    _SapAllowNetMode_Type()
)
sapAllowNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowNetMode.setStatus("mandatory")


class _SapAllowNet_Type(OctetString):
    """Custom type sapAllowNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SapAllowNet_Type.__name__ = "OctetString"
_SapAllowNet_Object = MibTableColumn
sapAllowNet = _SapAllowNet_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 7),
    _SapAllowNet_Type()
)
sapAllowNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowNet.setStatus("mandatory")


class _SapAllowNodeMode_Type(Integer32):
    """Custom type sapAllowNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapAllowNodeMode_Type.__name__ = "Integer32"
_SapAllowNodeMode_Object = MibTableColumn
sapAllowNodeMode = _SapAllowNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 8),
    _SapAllowNodeMode_Type()
)
sapAllowNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowNodeMode.setStatus("mandatory")


class _SapAllowNode_Type(OctetString):
    """Custom type sapAllowNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SapAllowNode_Type.__name__ = "OctetString"
_SapAllowNode_Object = MibTableColumn
sapAllowNode = _SapAllowNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 9),
    _SapAllowNode_Type()
)
sapAllowNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowNode.setStatus("mandatory")


class _SapAllowSockMode_Type(Integer32):
    """Custom type sapAllowSockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapAllowSockMode_Type.__name__ = "Integer32"
_SapAllowSockMode_Object = MibTableColumn
sapAllowSockMode = _SapAllowSockMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 10),
    _SapAllowSockMode_Type()
)
sapAllowSockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowSockMode.setStatus("mandatory")


class _SapAllowSock_Type(OctetString):
    """Custom type sapAllowSock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SapAllowSock_Type.__name__ = "OctetString"
_SapAllowSock_Object = MibTableColumn
sapAllowSock = _SapAllowSock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 11),
    _SapAllowSock_Type()
)
sapAllowSock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowSock.setStatus("mandatory")


class _SapAllowName_Type(DisplayString):
    """Custom type sapAllowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SapAllowName_Type.__name__ = "DisplayString"
_SapAllowName_Object = MibTableColumn
sapAllowName = _SapAllowName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 5, 1, 12),
    _SapAllowName_Type()
)
sapAllowName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAllowName.setStatus("mandatory")
_SapDenyTable_Object = MibTable
sapDenyTable = _SapDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6)
)
if mibBuilder.loadTexts:
    sapDenyTable.setStatus("mandatory")
_SapDenyEntry_Object = MibTableRow
sapDenyEntry = _SapDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1)
)
sapDenyEntry.setIndexNames(
    (0, "BIANCA-BRICK-IPX-MIB", "sapDenyIfIndex"),
)
if mibBuilder.loadTexts:
    sapDenyEntry.setStatus("mandatory")


class _SapDenyIfIndexMode_Type(Integer32):
    """Custom type sapDenyIfIndexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("dont-verify", 1),
          ("verify", 2))
    )


_SapDenyIfIndexMode_Type.__name__ = "Integer32"
_SapDenyIfIndexMode_Object = MibTableColumn
sapDenyIfIndexMode = _SapDenyIfIndexMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 1),
    _SapDenyIfIndexMode_Type()
)
sapDenyIfIndexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyIfIndexMode.setStatus("mandatory")
_SapDenyIfIndex_Type = Integer32
_SapDenyIfIndex_Object = MibTableColumn
sapDenyIfIndex = _SapDenyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 2),
    _SapDenyIfIndex_Type()
)
sapDenyIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyIfIndex.setStatus("mandatory")


class _SapDenyDirection_Type(Integer32):
    """Custom type sapDenyDirection based on Integer32"""
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
        *(("both", 4),
          ("dont-verify", 1),
          ("incoming", 3),
          ("outgoing", 2))
    )


_SapDenyDirection_Type.__name__ = "Integer32"
_SapDenyDirection_Object = MibTableColumn
sapDenyDirection = _SapDenyDirection_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 3),
    _SapDenyDirection_Type()
)
sapDenyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyDirection.setStatus("mandatory")


class _SapDenyTypeMode_Type(Integer32):
    """Custom type sapDenyTypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapDenyTypeMode_Type.__name__ = "Integer32"
_SapDenyTypeMode_Object = MibTableColumn
sapDenyTypeMode = _SapDenyTypeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 4),
    _SapDenyTypeMode_Type()
)
sapDenyTypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyTypeMode.setStatus("mandatory")


class _SapDenyType_Type(OctetString):
    """Custom type sapDenyType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SapDenyType_Type.__name__ = "OctetString"
_SapDenyType_Object = MibTableColumn
sapDenyType = _SapDenyType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 5),
    _SapDenyType_Type()
)
sapDenyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyType.setStatus("mandatory")


class _SapDenyNetMode_Type(Integer32):
    """Custom type sapDenyNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapDenyNetMode_Type.__name__ = "Integer32"
_SapDenyNetMode_Object = MibTableColumn
sapDenyNetMode = _SapDenyNetMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 6),
    _SapDenyNetMode_Type()
)
sapDenyNetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyNetMode.setStatus("mandatory")


class _SapDenyNet_Type(OctetString):
    """Custom type sapDenyNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SapDenyNet_Type.__name__ = "OctetString"
_SapDenyNet_Object = MibTableColumn
sapDenyNet = _SapDenyNet_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 7),
    _SapDenyNet_Type()
)
sapDenyNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyNet.setStatus("mandatory")


class _SapDenyNodeMode_Type(Integer32):
    """Custom type sapDenyNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapDenyNodeMode_Type.__name__ = "Integer32"
_SapDenyNodeMode_Object = MibTableColumn
sapDenyNodeMode = _SapDenyNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 8),
    _SapDenyNodeMode_Type()
)
sapDenyNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyNodeMode.setStatus("mandatory")


class _SapDenyNode_Type(OctetString):
    """Custom type sapDenyNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SapDenyNode_Type.__name__ = "OctetString"
_SapDenyNode_Object = MibTableColumn
sapDenyNode = _SapDenyNode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 9),
    _SapDenyNode_Type()
)
sapDenyNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyNode.setStatus("mandatory")


class _SapDenySockMode_Type(Integer32):
    """Custom type sapDenySockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_SapDenySockMode_Type.__name__ = "Integer32"
_SapDenySockMode_Object = MibTableColumn
sapDenySockMode = _SapDenySockMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 10),
    _SapDenySockMode_Type()
)
sapDenySockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenySockMode.setStatus("mandatory")


class _SapDenySock_Type(OctetString):
    """Custom type sapDenySock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SapDenySock_Type.__name__ = "OctetString"
_SapDenySock_Object = MibTableColumn
sapDenySock = _SapDenySock_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 11),
    _SapDenySock_Type()
)
sapDenySock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenySock.setStatus("mandatory")


class _SapDenyName_Type(DisplayString):
    """Custom type sapDenyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SapDenyName_Type.__name__ = "DisplayString"
_SapDenyName_Object = MibTableColumn
sapDenyName = _SapDenyName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 9, 6, 1, 12),
    _SapDenyName_Type()
)
sapDenyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapDenyName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-IPX-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboipx": biboipx,
       "ipxClientTable": ipxClientTable,
       "ipxClientEntry": ipxClientEntry,
       "ipxClientNode": ipxClientNode,
       "ipxClientCircIndex": ipxClientCircIndex,
       "ipxClientReconns": ipxClientReconns,
       "ipxAllowTable": ipxAllowTable,
       "ipxAllowEntry": ipxAllowEntry,
       "ipxAllowPktTypeMode": ipxAllowPktTypeMode,
       "ipxAllowPktType": ipxAllowPktType,
       "ipxAllowDstIfStatus": ipxAllowDstIfStatus,
       "ipxAllowDstNetMode": ipxAllowDstNetMode,
       "ipxAllowDstNet": ipxAllowDstNet,
       "ipxAllowDstNodeMode": ipxAllowDstNodeMode,
       "ipxAllowDstNode": ipxAllowDstNode,
       "ipxAllowDstSockMode": ipxAllowDstSockMode,
       "ipxAllowDstSock": ipxAllowDstSock,
       "ipxAllowSrcIfIndexMode": ipxAllowSrcIfIndexMode,
       "ipxAllowSrcIfIndex": ipxAllowSrcIfIndex,
       "ipxAllowSrcNetMode": ipxAllowSrcNetMode,
       "ipxAllowSrcNet": ipxAllowSrcNet,
       "ipxAllowSrcNodeMode": ipxAllowSrcNodeMode,
       "ipxAllowSrcNode": ipxAllowSrcNode,
       "ipxAllowSrcSockMode": ipxAllowSrcSockMode,
       "ipxAllowSrcSock": ipxAllowSrcSock,
       "ipxDenyTable": ipxDenyTable,
       "ipxDenyEntry": ipxDenyEntry,
       "ipxDenyPktTypeMode": ipxDenyPktTypeMode,
       "ipxDenyPktType": ipxDenyPktType,
       "ipxDenyDstIfStatus": ipxDenyDstIfStatus,
       "ipxDenyDstNetMode": ipxDenyDstNetMode,
       "ipxDenyDstNet": ipxDenyDstNet,
       "ipxDenyDstNodeMode": ipxDenyDstNodeMode,
       "ipxDenyDstNode": ipxDenyDstNode,
       "ipxDenyDstSockMode": ipxDenyDstSockMode,
       "ipxDenyDstSock": ipxDenyDstSock,
       "ipxDenySrcIfIndexMode": ipxDenySrcIfIndexMode,
       "ipxDenySrcIfIndex": ipxDenySrcIfIndex,
       "ipxDenySrcNetMode": ipxDenySrcNetMode,
       "ipxDenySrcNet": ipxDenySrcNet,
       "ipxDenySrcNodeMode": ipxDenySrcNodeMode,
       "ipxDenySrcNode": ipxDenySrcNode,
       "ipxDenySrcSockMode": ipxDenySrcSockMode,
       "ipxDenySrcSock": ipxDenySrcSock,
       "ipxAdmin": ipxAdmin,
       "ipxAdmSpxSpoofing": ipxAdmSpxSpoofing,
       "ipxAdmIpxSpoofing": ipxAdmIpxSpoofing,
       "ipxAdmNETBIOSRepl": ipxAdmNETBIOSRepl,
       "ipxAdmSpxVerTimeout": ipxAdmSpxVerTimeout,
       "ipxAdmSpxAbrTimeout": ipxAdmSpxAbrTimeout,
       "ipxAdmRIPSAPOffset": ipxAdmRIPSAPOffset,
       "ipxAdmLearnStatics": ipxAdmLearnStatics,
       "ipxAdmSpxConns": ipxAdmSpxConns,
       "sapAllowTable": sapAllowTable,
       "sapAllowEntry": sapAllowEntry,
       "sapAllowIfIndexMode": sapAllowIfIndexMode,
       "sapAllowIfIndex": sapAllowIfIndex,
       "sapAllowDirection": sapAllowDirection,
       "sapAllowTypeMode": sapAllowTypeMode,
       "sapAllowType": sapAllowType,
       "sapAllowNetMode": sapAllowNetMode,
       "sapAllowNet": sapAllowNet,
       "sapAllowNodeMode": sapAllowNodeMode,
       "sapAllowNode": sapAllowNode,
       "sapAllowSockMode": sapAllowSockMode,
       "sapAllowSock": sapAllowSock,
       "sapAllowName": sapAllowName,
       "sapDenyTable": sapDenyTable,
       "sapDenyEntry": sapDenyEntry,
       "sapDenyIfIndexMode": sapDenyIfIndexMode,
       "sapDenyIfIndex": sapDenyIfIndex,
       "sapDenyDirection": sapDenyDirection,
       "sapDenyTypeMode": sapDenyTypeMode,
       "sapDenyType": sapDenyType,
       "sapDenyNetMode": sapDenyNetMode,
       "sapDenyNet": sapDenyNet,
       "sapDenyNodeMode": sapDenyNodeMode,
       "sapDenyNode": sapDenyNode,
       "sapDenySockMode": sapDenySockMode,
       "sapDenySock": sapDenySock,
       "sapDenyName": sapDenyName}
)
