# SNMP MIB module (ALCATEL-IND1-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:19 2024
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

(routingIND1Ipx,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ipx")

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

alcatelIND1IPXMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1)
)
alcatelIND1IPXMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NetNumber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class HostAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPXMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPXMIBObjects = _AlcatelIND1IPXMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1)
)
_AlaIpxRoutingGroup_ObjectIdentity = ObjectIdentity
alaIpxRoutingGroup = _AlaIpxRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaIpxRoutingGroup.setStatus("current")
_AlaIpxStaticRouteTable_Object = MibTable
alaIpxStaticRouteTable = _AlaIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaIpxStaticRouteTable.setStatus("current")
_AlaIpxStaticRouteEntry_Object = MibTableRow
alaIpxStaticRouteEntry = _AlaIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1)
)
alaIpxStaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxStaticRouteNetNum"),
)
if mibBuilder.loadTexts:
    alaIpxStaticRouteEntry.setStatus("current")


class _AlaIpxStaticRouteNetNum_Type(NetNumber):
    """Custom type alaIpxStaticRouteNetNum based on NetNumber"""
    defaultHexValue = "00000000"


_AlaIpxStaticRouteNetNum_Object = MibTableColumn
alaIpxStaticRouteNetNum = _AlaIpxStaticRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1, 1),
    _AlaIpxStaticRouteNetNum_Type()
)
alaIpxStaticRouteNetNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxStaticRouteNetNum.setStatus("current")


class _AlaIpxStaticRouteNextHopNet_Type(NetNumber):
    """Custom type alaIpxStaticRouteNextHopNet based on NetNumber"""
    defaultHexValue = "00000000"


_AlaIpxStaticRouteNextHopNet_Object = MibTableColumn
alaIpxStaticRouteNextHopNet = _AlaIpxStaticRouteNextHopNet_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1, 2),
    _AlaIpxStaticRouteNextHopNet_Type()
)
alaIpxStaticRouteNextHopNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxStaticRouteNextHopNet.setStatus("current")


class _AlaIpxStaticRouteNextHopNode_Type(HostAddress):
    """Custom type alaIpxStaticRouteNextHopNode based on HostAddress"""
    defaultHexValue = "000000000000"


_AlaIpxStaticRouteNextHopNode_Object = MibTableColumn
alaIpxStaticRouteNextHopNode = _AlaIpxStaticRouteNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1, 3),
    _AlaIpxStaticRouteNextHopNode_Type()
)
alaIpxStaticRouteNextHopNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxStaticRouteNextHopNode.setStatus("current")


class _AlaIpxStaticRouteTicks_Type(Integer32):
    """Custom type alaIpxStaticRouteTicks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaIpxStaticRouteTicks_Type.__name__ = "Integer32"
_AlaIpxStaticRouteTicks_Object = MibTableColumn
alaIpxStaticRouteTicks = _AlaIpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1, 4),
    _AlaIpxStaticRouteTicks_Type()
)
alaIpxStaticRouteTicks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxStaticRouteTicks.setStatus("current")


class _AlaIpxStaticRouteHopCount_Type(Integer32):
    """Custom type alaIpxStaticRouteHopCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlaIpxStaticRouteHopCount_Type.__name__ = "Integer32"
_AlaIpxStaticRouteHopCount_Object = MibTableColumn
alaIpxStaticRouteHopCount = _AlaIpxStaticRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1, 5),
    _AlaIpxStaticRouteHopCount_Type()
)
alaIpxStaticRouteHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxStaticRouteHopCount.setStatus("current")
_AlaIpxStaticRouteRowStatus_Type = RowStatus
_AlaIpxStaticRouteRowStatus_Object = MibTableColumn
alaIpxStaticRouteRowStatus = _AlaIpxStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 1, 1, 6),
    _AlaIpxStaticRouteRowStatus_Type()
)
alaIpxStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxStaticRouteRowStatus.setStatus("current")
_AlaIpxDefRouteTable_Object = MibTable
alaIpxDefRouteTable = _AlaIpxDefRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpxDefRouteTable.setStatus("current")
_AlaIpxDefRouteEntry_Object = MibTableRow
alaIpxDefRouteEntry = _AlaIpxDefRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 2, 1)
)
alaIpxDefRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxDefRouteVlanId"),
)
if mibBuilder.loadTexts:
    alaIpxDefRouteEntry.setStatus("current")


class _AlaIpxDefRouteVlanId_Type(Integer32):
    """Custom type alaIpxDefRouteVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxDefRouteVlanId_Type.__name__ = "Integer32"
_AlaIpxDefRouteVlanId_Object = MibTableColumn
alaIpxDefRouteVlanId = _AlaIpxDefRouteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 2, 1, 1),
    _AlaIpxDefRouteVlanId_Type()
)
alaIpxDefRouteVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxDefRouteVlanId.setStatus("current")


class _AlaIpxDefRouteNet_Type(NetNumber):
    """Custom type alaIpxDefRouteNet based on NetNumber"""
    defaultHexValue = "00000000"


_AlaIpxDefRouteNet_Object = MibTableColumn
alaIpxDefRouteNet = _AlaIpxDefRouteNet_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 2, 1, 2),
    _AlaIpxDefRouteNet_Type()
)
alaIpxDefRouteNet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxDefRouteNet.setStatus("current")


class _AlaIpxDefRouteNode_Type(HostAddress):
    """Custom type alaIpxDefRouteNode based on HostAddress"""
    defaultHexValue = "000000000000"


_AlaIpxDefRouteNode_Object = MibTableColumn
alaIpxDefRouteNode = _AlaIpxDefRouteNode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 2, 1, 3),
    _AlaIpxDefRouteNode_Type()
)
alaIpxDefRouteNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxDefRouteNode.setStatus("current")
_AlaIpxDefRouteRowStatus_Type = RowStatus
_AlaIpxDefRouteRowStatus_Object = MibTableColumn
alaIpxDefRouteRowStatus = _AlaIpxDefRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 2, 1, 4),
    _AlaIpxDefRouteRowStatus_Type()
)
alaIpxDefRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxDefRouteRowStatus.setStatus("current")
_AlaIpxExtMsgTable_Object = MibTable
alaIpxExtMsgTable = _AlaIpxExtMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaIpxExtMsgTable.setStatus("current")
_AlaIpxExtMsgEntry_Object = MibTableRow
alaIpxExtMsgEntry = _AlaIpxExtMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 3, 1)
)
alaIpxExtMsgEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxExtMsgVlanId"),
)
if mibBuilder.loadTexts:
    alaIpxExtMsgEntry.setStatus("current")


class _AlaIpxExtMsgVlanId_Type(Integer32):
    """Custom type alaIpxExtMsgVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxExtMsgVlanId_Type.__name__ = "Integer32"
_AlaIpxExtMsgVlanId_Object = MibTableColumn
alaIpxExtMsgVlanId = _AlaIpxExtMsgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 3, 1, 1),
    _AlaIpxExtMsgVlanId_Type()
)
alaIpxExtMsgVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxExtMsgVlanId.setStatus("current")


class _AlaIpxExtMsgMode_Type(Integer32):
    """Custom type alaIpxExtMsgMode based on Integer32"""
    defaultValue = 1

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


_AlaIpxExtMsgMode_Type.__name__ = "Integer32"
_AlaIpxExtMsgMode_Object = MibTableColumn
alaIpxExtMsgMode = _AlaIpxExtMsgMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 3, 1, 2),
    _AlaIpxExtMsgMode_Type()
)
alaIpxExtMsgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxExtMsgMode.setStatus("current")
_AlaIpxExtMsgRowStatus_Type = RowStatus
_AlaIpxExtMsgRowStatus_Object = MibTableColumn
alaIpxExtMsgRowStatus = _AlaIpxExtMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 3, 1, 3),
    _AlaIpxExtMsgRowStatus_Type()
)
alaIpxExtMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxExtMsgRowStatus.setStatus("current")


class _AlaIpxFlush_Type(Integer32):
    """Custom type alaIpxFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("rip", 1),
          ("sap", 2))
    )


_AlaIpxFlush_Type.__name__ = "Integer32"
_AlaIpxFlush_Object = MibScalar
alaIpxFlush = _AlaIpxFlush_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 1, 4),
    _AlaIpxFlush_Type()
)
alaIpxFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpxFlush.setStatus("current")
_AlaIpxFilterGroup_ObjectIdentity = ObjectIdentity
alaIpxFilterGroup = _AlaIpxFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpxFilterGroup.setStatus("current")
_AlaIpxRipSapFilterTable_Object = MibTable
alaIpxRipSapFilterTable = _AlaIpxRipSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIpxRipSapFilterTable.setStatus("current")
_AlaIpxRipSapFilterEntry_Object = MibTableRow
alaIpxRipSapFilterEntry = _AlaIpxRipSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1)
)
alaIpxRipSapFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterVlanId"),
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterType"),
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterNet"),
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterNetMask"),
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterNode"),
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterNodeMask"),
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterSvcType"),
)
if mibBuilder.loadTexts:
    alaIpxRipSapFilterEntry.setStatus("current")


class _AlaIpxRipSapFilterVlanId_Type(Integer32):
    """Custom type alaIpxRipSapFilterVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxRipSapFilterVlanId_Type.__name__ = "Integer32"
_AlaIpxRipSapFilterVlanId_Object = MibTableColumn
alaIpxRipSapFilterVlanId = _AlaIpxRipSapFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 1),
    _AlaIpxRipSapFilterVlanId_Type()
)
alaIpxRipSapFilterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterVlanId.setStatus("current")


class _AlaIpxRipSapFilterType_Type(Integer32):
    """Custom type alaIpxRipSapFilterType based on Integer32"""
    defaultValue = 1

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
        *(("gnsOutput", 3),
          ("ripInput", 5),
          ("ripOutput", 4),
          ("sapInput", 2),
          ("sapOutput", 1))
    )


_AlaIpxRipSapFilterType_Type.__name__ = "Integer32"
_AlaIpxRipSapFilterType_Object = MibTableColumn
alaIpxRipSapFilterType = _AlaIpxRipSapFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 2),
    _AlaIpxRipSapFilterType_Type()
)
alaIpxRipSapFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterType.setStatus("current")


class _AlaIpxRipSapFilterNet_Type(NetNumber):
    """Custom type alaIpxRipSapFilterNet based on NetNumber"""
    defaultHexValue = "00000000"


_AlaIpxRipSapFilterNet_Object = MibTableColumn
alaIpxRipSapFilterNet = _AlaIpxRipSapFilterNet_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 3),
    _AlaIpxRipSapFilterNet_Type()
)
alaIpxRipSapFilterNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterNet.setStatus("current")


class _AlaIpxRipSapFilterNetMask_Type(NetNumber):
    """Custom type alaIpxRipSapFilterNetMask based on NetNumber"""
    defaultHexValue = "ffffffff"


_AlaIpxRipSapFilterNetMask_Object = MibTableColumn
alaIpxRipSapFilterNetMask = _AlaIpxRipSapFilterNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 4),
    _AlaIpxRipSapFilterNetMask_Type()
)
alaIpxRipSapFilterNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterNetMask.setStatus("current")


class _AlaIpxRipSapFilterNode_Type(HostAddress):
    """Custom type alaIpxRipSapFilterNode based on HostAddress"""
    defaultHexValue = "000000000000"


_AlaIpxRipSapFilterNode_Object = MibTableColumn
alaIpxRipSapFilterNode = _AlaIpxRipSapFilterNode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 5),
    _AlaIpxRipSapFilterNode_Type()
)
alaIpxRipSapFilterNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterNode.setStatus("current")


class _AlaIpxRipSapFilterNodeMask_Type(HostAddress):
    """Custom type alaIpxRipSapFilterNodeMask based on HostAddress"""
    defaultHexValue = "ffffffffffff"


_AlaIpxRipSapFilterNodeMask_Object = MibTableColumn
alaIpxRipSapFilterNodeMask = _AlaIpxRipSapFilterNodeMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 6),
    _AlaIpxRipSapFilterNodeMask_Type()
)
alaIpxRipSapFilterNodeMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterNodeMask.setStatus("current")


class _AlaIpxRipSapFilterSvcType_Type(Integer32):
    """Custom type alaIpxRipSapFilterSvcType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaIpxRipSapFilterSvcType_Type.__name__ = "Integer32"
_AlaIpxRipSapFilterSvcType_Object = MibTableColumn
alaIpxRipSapFilterSvcType = _AlaIpxRipSapFilterSvcType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 7),
    _AlaIpxRipSapFilterSvcType_Type()
)
alaIpxRipSapFilterSvcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterSvcType.setStatus("current")


class _AlaIpxRipSapFilterMode_Type(Integer32):
    """Custom type alaIpxRipSapFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_AlaIpxRipSapFilterMode_Type.__name__ = "Integer32"
_AlaIpxRipSapFilterMode_Object = MibTableColumn
alaIpxRipSapFilterMode = _AlaIpxRipSapFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 8),
    _AlaIpxRipSapFilterMode_Type()
)
alaIpxRipSapFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterMode.setStatus("current")
_AlaIpxRipSapFilterRowStatus_Type = RowStatus
_AlaIpxRipSapFilterRowStatus_Object = MibTableColumn
alaIpxRipSapFilterRowStatus = _AlaIpxRipSapFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 1, 1, 10),
    _AlaIpxRipSapFilterRowStatus_Type()
)
alaIpxRipSapFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxRipSapFilterRowStatus.setStatus("current")
_AlaIpxWatchdogSpoofTable_Object = MibTable
alaIpxWatchdogSpoofTable = _AlaIpxWatchdogSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaIpxWatchdogSpoofTable.setStatus("current")
_AlaIpxWatchdogSpoofEntry_Object = MibTableRow
alaIpxWatchdogSpoofEntry = _AlaIpxWatchdogSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 2, 1)
)
alaIpxWatchdogSpoofEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxWatchdogSpoofVlanId"),
)
if mibBuilder.loadTexts:
    alaIpxWatchdogSpoofEntry.setStatus("current")


class _AlaIpxWatchdogSpoofVlanId_Type(Integer32):
    """Custom type alaIpxWatchdogSpoofVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxWatchdogSpoofVlanId_Type.__name__ = "Integer32"
_AlaIpxWatchdogSpoofVlanId_Object = MibTableColumn
alaIpxWatchdogSpoofVlanId = _AlaIpxWatchdogSpoofVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 2, 1, 1),
    _AlaIpxWatchdogSpoofVlanId_Type()
)
alaIpxWatchdogSpoofVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxWatchdogSpoofVlanId.setStatus("current")


class _AlaIpxWatchdogSpoofMode_Type(Integer32):
    """Custom type alaIpxWatchdogSpoofMode based on Integer32"""
    defaultValue = 2

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


_AlaIpxWatchdogSpoofMode_Type.__name__ = "Integer32"
_AlaIpxWatchdogSpoofMode_Object = MibTableColumn
alaIpxWatchdogSpoofMode = _AlaIpxWatchdogSpoofMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 2, 1, 2),
    _AlaIpxWatchdogSpoofMode_Type()
)
alaIpxWatchdogSpoofMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxWatchdogSpoofMode.setStatus("current")
_AlaIpxWatchdogSpoofRowStatus_Type = RowStatus
_AlaIpxWatchdogSpoofRowStatus_Object = MibTableColumn
alaIpxWatchdogSpoofRowStatus = _AlaIpxWatchdogSpoofRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 2, 1, 3),
    _AlaIpxWatchdogSpoofRowStatus_Type()
)
alaIpxWatchdogSpoofRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxWatchdogSpoofRowStatus.setStatus("current")
_AlaIpxSerialFilterTable_Object = MibTable
alaIpxSerialFilterTable = _AlaIpxSerialFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alaIpxSerialFilterTable.setStatus("current")
_AlaIpxSerialFilterEntry_Object = MibTableRow
alaIpxSerialFilterEntry = _AlaIpxSerialFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 3, 1)
)
alaIpxSerialFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxSerialFilterVlanId"),
)
if mibBuilder.loadTexts:
    alaIpxSerialFilterEntry.setStatus("current")


class _AlaIpxSerialFilterVlanId_Type(Integer32):
    """Custom type alaIpxSerialFilterVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxSerialFilterVlanId_Type.__name__ = "Integer32"
_AlaIpxSerialFilterVlanId_Object = MibTableColumn
alaIpxSerialFilterVlanId = _AlaIpxSerialFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 3, 1, 1),
    _AlaIpxSerialFilterVlanId_Type()
)
alaIpxSerialFilterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxSerialFilterVlanId.setStatus("current")


class _AlaIpxSerialFilterMode_Type(Integer32):
    """Custom type alaIpxSerialFilterMode based on Integer32"""
    defaultValue = 2

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


_AlaIpxSerialFilterMode_Type.__name__ = "Integer32"
_AlaIpxSerialFilterMode_Object = MibTableColumn
alaIpxSerialFilterMode = _AlaIpxSerialFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 3, 1, 2),
    _AlaIpxSerialFilterMode_Type()
)
alaIpxSerialFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxSerialFilterMode.setStatus("current")
_AlaIpxSerialFilterRowStatus_Type = RowStatus
_AlaIpxSerialFilterRowStatus_Object = MibTableColumn
alaIpxSerialFilterRowStatus = _AlaIpxSerialFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 3, 1, 3),
    _AlaIpxSerialFilterRowStatus_Type()
)
alaIpxSerialFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxSerialFilterRowStatus.setStatus("current")
_AlaSpxKeepaliveSpoofTable_Object = MibTable
alaSpxKeepaliveSpoofTable = _AlaSpxKeepaliveSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alaSpxKeepaliveSpoofTable.setStatus("current")
_AlaSpxKeepaliveSpoofEntry_Object = MibTableRow
alaSpxKeepaliveSpoofEntry = _AlaSpxKeepaliveSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 4, 1)
)
alaSpxKeepaliveSpoofEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaSpxKeepaliveSpoofVlanId"),
)
if mibBuilder.loadTexts:
    alaSpxKeepaliveSpoofEntry.setStatus("current")


class _AlaSpxKeepaliveSpoofVlanId_Type(Integer32):
    """Custom type alaSpxKeepaliveSpoofVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaSpxKeepaliveSpoofVlanId_Type.__name__ = "Integer32"
_AlaSpxKeepaliveSpoofVlanId_Object = MibTableColumn
alaSpxKeepaliveSpoofVlanId = _AlaSpxKeepaliveSpoofVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 4, 1, 1),
    _AlaSpxKeepaliveSpoofVlanId_Type()
)
alaSpxKeepaliveSpoofVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaSpxKeepaliveSpoofVlanId.setStatus("current")


class _AlaSpxKeepaliveSpoofMode_Type(Integer32):
    """Custom type alaSpxKeepaliveSpoofMode based on Integer32"""
    defaultValue = 2

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


_AlaSpxKeepaliveSpoofMode_Type.__name__ = "Integer32"
_AlaSpxKeepaliveSpoofMode_Object = MibTableColumn
alaSpxKeepaliveSpoofMode = _AlaSpxKeepaliveSpoofMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 4, 1, 2),
    _AlaSpxKeepaliveSpoofMode_Type()
)
alaSpxKeepaliveSpoofMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSpxKeepaliveSpoofMode.setStatus("current")
_AlaSpxKeepaliveSpoofRowStatus_Type = RowStatus
_AlaSpxKeepaliveSpoofRowStatus_Object = MibTableColumn
alaSpxKeepaliveSpoofRowStatus = _AlaSpxKeepaliveSpoofRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 4, 1, 3),
    _AlaSpxKeepaliveSpoofRowStatus_Type()
)
alaSpxKeepaliveSpoofRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaSpxKeepaliveSpoofRowStatus.setStatus("current")
_AlaIpxType20Table_Object = MibTable
alaIpxType20Table = _AlaIpxType20Table_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    alaIpxType20Table.setStatus("current")
_AlaIpxType20Entry_Object = MibTableRow
alaIpxType20Entry = _AlaIpxType20Entry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 5, 1)
)
alaIpxType20Entry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxType20VlanId"),
)
if mibBuilder.loadTexts:
    alaIpxType20Entry.setStatus("current")


class _AlaIpxType20VlanId_Type(Integer32):
    """Custom type alaIpxType20VlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxType20VlanId_Type.__name__ = "Integer32"
_AlaIpxType20VlanId_Object = MibTableColumn
alaIpxType20VlanId = _AlaIpxType20VlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 5, 1, 1),
    _AlaIpxType20VlanId_Type()
)
alaIpxType20VlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxType20VlanId.setStatus("current")


class _AlaIpxType20Mode_Type(Integer32):
    """Custom type alaIpxType20Mode based on Integer32"""
    defaultValue = 2

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


_AlaIpxType20Mode_Type.__name__ = "Integer32"
_AlaIpxType20Mode_Object = MibTableColumn
alaIpxType20Mode = _AlaIpxType20Mode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 5, 1, 2),
    _AlaIpxType20Mode_Type()
)
alaIpxType20Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxType20Mode.setStatus("current")
_AlaIpxType20RowStatus_Type = RowStatus
_AlaIpxType20RowStatus_Object = MibTableColumn
alaIpxType20RowStatus = _AlaIpxType20RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 2, 5, 1, 3),
    _AlaIpxType20RowStatus_Type()
)
alaIpxType20RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxType20RowStatus.setStatus("current")
_AlaIpxTimerGroup_ObjectIdentity = ObjectIdentity
alaIpxTimerGroup = _AlaIpxTimerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaIpxTimerGroup.setStatus("current")
_AlaIpxTimerTable_Object = MibTable
alaIpxTimerTable = _AlaIpxTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaIpxTimerTable.setStatus("current")
_AlaIpxTimerEntry_Object = MibTableRow
alaIpxTimerEntry = _AlaIpxTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3, 1, 1)
)
alaIpxTimerEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPX-MIB", "alaIpxTimerVlanId"),
)
if mibBuilder.loadTexts:
    alaIpxTimerEntry.setStatus("current")


class _AlaIpxTimerVlanId_Type(Integer32):
    """Custom type alaIpxTimerVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpxTimerVlanId_Type.__name__ = "Integer32"
_AlaIpxTimerVlanId_Object = MibTableColumn
alaIpxTimerVlanId = _AlaIpxTimerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3, 1, 1, 1),
    _AlaIpxTimerVlanId_Type()
)
alaIpxTimerVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpxTimerVlanId.setStatus("current")


class _AlaIpxTimerSap_Type(Integer32):
    """Custom type alaIpxTimerSap based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_AlaIpxTimerSap_Type.__name__ = "Integer32"
_AlaIpxTimerSap_Object = MibTableColumn
alaIpxTimerSap = _AlaIpxTimerSap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3, 1, 1, 2),
    _AlaIpxTimerSap_Type()
)
alaIpxTimerSap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxTimerSap.setStatus("current")


class _AlaIpxTimerRip_Type(Integer32):
    """Custom type alaIpxTimerRip based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_AlaIpxTimerRip_Type.__name__ = "Integer32"
_AlaIpxTimerRip_Object = MibTableColumn
alaIpxTimerRip = _AlaIpxTimerRip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3, 1, 1, 3),
    _AlaIpxTimerRip_Type()
)
alaIpxTimerRip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxTimerRip.setStatus("current")
_AlaIpxTimerRowStatus_Type = RowStatus
_AlaIpxTimerRowStatus_Object = MibTableColumn
alaIpxTimerRowStatus = _AlaIpxTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 1, 3, 1, 1, 4),
    _AlaIpxTimerRowStatus_Type()
)
alaIpxTimerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpxTimerRowStatus.setStatus("current")
_AlcatelIND1IPXMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPXMIBConformance = _AlcatelIND1IPXMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2)
)
_AlcatelIND1IPXMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPXMIBCompliances = _AlcatelIND1IPXMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 1)
)
_AlcatelIND1IPXMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPXMIBGroups = _AlcatelIND1IPXMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2)
)

# Managed Objects groups

alcatelIND1IPXMIBStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 1)
)
alcatelIND1IPXMIBStaticRouteGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxStaticRouteNextHopNet"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxStaticRouteNextHopNode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxStaticRouteTicks"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxStaticRouteHopCount"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxStaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBStaticRouteGroup.setStatus("current")

alcatelIND1IPXMIBDefRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 2)
)
alcatelIND1IPXMIBDefRouteGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxDefRouteNet"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxDefRouteNode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxDefRouteRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBDefRouteGroup.setStatus("current")

alcatelIND1IPXMIBExtMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 3)
)
alcatelIND1IPXMIBExtMsgGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxExtMsgMode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxExtMsgRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBExtMsgGroup.setStatus("current")

alcatelIND1IPXMIBFlushGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 4)
)
alcatelIND1IPXMIBFlushGroup.setObjects(
    ("ALCATEL-IND1-IPX-MIB", "alaIpxFlush")
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBFlushGroup.setStatus("current")

alcatelIND1IPXMIBRipSapFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 5)
)
alcatelIND1IPXMIBRipSapFilterGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterMode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxRipSapFilterRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBRipSapFilterGroup.setStatus("current")

alcatelIND1IPXMIBWatchdogSpoofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 6)
)
alcatelIND1IPXMIBWatchdogSpoofGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxWatchdogSpoofMode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxWatchdogSpoofRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBWatchdogSpoofGroup.setStatus("current")

alcatelIND1IPXMIBSerialFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 7)
)
alcatelIND1IPXMIBSerialFilterGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxSerialFilterMode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxSerialFilterRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBSerialFilterGroup.setStatus("current")

alcatelIND1IPXMIBKeepaliveSpoofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 8)
)
alcatelIND1IPXMIBKeepaliveSpoofGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaSpxKeepaliveSpoofMode"),
        ("ALCATEL-IND1-IPX-MIB", "alaSpxKeepaliveSpoofRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBKeepaliveSpoofGroup.setStatus("current")

alcatelIND1IPXMIBType20Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 9)
)
alcatelIND1IPXMIBType20Group.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxType20Mode"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxType20RowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBType20Group.setStatus("current")

alcatelIND1IPXMIBTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 2, 10)
)
alcatelIND1IPXMIBTimerGroup.setObjects(
      *(("ALCATEL-IND1-IPX-MIB", "alaIpxTimerRip"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxTimerSap"),
        ("ALCATEL-IND1-IPX-MIB", "alaIpxTimerRowStatus"))
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBTimerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1IPXMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 8, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPXMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPX-MIB",
    **{"NetNumber": NetNumber,
       "HostAddress": HostAddress,
       "alcatelIND1IPXMIB": alcatelIND1IPXMIB,
       "alcatelIND1IPXMIBObjects": alcatelIND1IPXMIBObjects,
       "alaIpxRoutingGroup": alaIpxRoutingGroup,
       "alaIpxStaticRouteTable": alaIpxStaticRouteTable,
       "alaIpxStaticRouteEntry": alaIpxStaticRouteEntry,
       "alaIpxStaticRouteNetNum": alaIpxStaticRouteNetNum,
       "alaIpxStaticRouteNextHopNet": alaIpxStaticRouteNextHopNet,
       "alaIpxStaticRouteNextHopNode": alaIpxStaticRouteNextHopNode,
       "alaIpxStaticRouteTicks": alaIpxStaticRouteTicks,
       "alaIpxStaticRouteHopCount": alaIpxStaticRouteHopCount,
       "alaIpxStaticRouteRowStatus": alaIpxStaticRouteRowStatus,
       "alaIpxDefRouteTable": alaIpxDefRouteTable,
       "alaIpxDefRouteEntry": alaIpxDefRouteEntry,
       "alaIpxDefRouteVlanId": alaIpxDefRouteVlanId,
       "alaIpxDefRouteNet": alaIpxDefRouteNet,
       "alaIpxDefRouteNode": alaIpxDefRouteNode,
       "alaIpxDefRouteRowStatus": alaIpxDefRouteRowStatus,
       "alaIpxExtMsgTable": alaIpxExtMsgTable,
       "alaIpxExtMsgEntry": alaIpxExtMsgEntry,
       "alaIpxExtMsgVlanId": alaIpxExtMsgVlanId,
       "alaIpxExtMsgMode": alaIpxExtMsgMode,
       "alaIpxExtMsgRowStatus": alaIpxExtMsgRowStatus,
       "alaIpxFlush": alaIpxFlush,
       "alaIpxFilterGroup": alaIpxFilterGroup,
       "alaIpxRipSapFilterTable": alaIpxRipSapFilterTable,
       "alaIpxRipSapFilterEntry": alaIpxRipSapFilterEntry,
       "alaIpxRipSapFilterVlanId": alaIpxRipSapFilterVlanId,
       "alaIpxRipSapFilterType": alaIpxRipSapFilterType,
       "alaIpxRipSapFilterNet": alaIpxRipSapFilterNet,
       "alaIpxRipSapFilterNetMask": alaIpxRipSapFilterNetMask,
       "alaIpxRipSapFilterNode": alaIpxRipSapFilterNode,
       "alaIpxRipSapFilterNodeMask": alaIpxRipSapFilterNodeMask,
       "alaIpxRipSapFilterSvcType": alaIpxRipSapFilterSvcType,
       "alaIpxRipSapFilterMode": alaIpxRipSapFilterMode,
       "alaIpxRipSapFilterRowStatus": alaIpxRipSapFilterRowStatus,
       "alaIpxWatchdogSpoofTable": alaIpxWatchdogSpoofTable,
       "alaIpxWatchdogSpoofEntry": alaIpxWatchdogSpoofEntry,
       "alaIpxWatchdogSpoofVlanId": alaIpxWatchdogSpoofVlanId,
       "alaIpxWatchdogSpoofMode": alaIpxWatchdogSpoofMode,
       "alaIpxWatchdogSpoofRowStatus": alaIpxWatchdogSpoofRowStatus,
       "alaIpxSerialFilterTable": alaIpxSerialFilterTable,
       "alaIpxSerialFilterEntry": alaIpxSerialFilterEntry,
       "alaIpxSerialFilterVlanId": alaIpxSerialFilterVlanId,
       "alaIpxSerialFilterMode": alaIpxSerialFilterMode,
       "alaIpxSerialFilterRowStatus": alaIpxSerialFilterRowStatus,
       "alaSpxKeepaliveSpoofTable": alaSpxKeepaliveSpoofTable,
       "alaSpxKeepaliveSpoofEntry": alaSpxKeepaliveSpoofEntry,
       "alaSpxKeepaliveSpoofVlanId": alaSpxKeepaliveSpoofVlanId,
       "alaSpxKeepaliveSpoofMode": alaSpxKeepaliveSpoofMode,
       "alaSpxKeepaliveSpoofRowStatus": alaSpxKeepaliveSpoofRowStatus,
       "alaIpxType20Table": alaIpxType20Table,
       "alaIpxType20Entry": alaIpxType20Entry,
       "alaIpxType20VlanId": alaIpxType20VlanId,
       "alaIpxType20Mode": alaIpxType20Mode,
       "alaIpxType20RowStatus": alaIpxType20RowStatus,
       "alaIpxTimerGroup": alaIpxTimerGroup,
       "alaIpxTimerTable": alaIpxTimerTable,
       "alaIpxTimerEntry": alaIpxTimerEntry,
       "alaIpxTimerVlanId": alaIpxTimerVlanId,
       "alaIpxTimerSap": alaIpxTimerSap,
       "alaIpxTimerRip": alaIpxTimerRip,
       "alaIpxTimerRowStatus": alaIpxTimerRowStatus,
       "alcatelIND1IPXMIBConformance": alcatelIND1IPXMIBConformance,
       "alcatelIND1IPXMIBCompliances": alcatelIND1IPXMIBCompliances,
       "alcatelIND1IPXMIBCompliance": alcatelIND1IPXMIBCompliance,
       "alcatelIND1IPXMIBGroups": alcatelIND1IPXMIBGroups,
       "alcatelIND1IPXMIBStaticRouteGroup": alcatelIND1IPXMIBStaticRouteGroup,
       "alcatelIND1IPXMIBDefRouteGroup": alcatelIND1IPXMIBDefRouteGroup,
       "alcatelIND1IPXMIBExtMsgGroup": alcatelIND1IPXMIBExtMsgGroup,
       "alcatelIND1IPXMIBFlushGroup": alcatelIND1IPXMIBFlushGroup,
       "alcatelIND1IPXMIBRipSapFilterGroup": alcatelIND1IPXMIBRipSapFilterGroup,
       "alcatelIND1IPXMIBWatchdogSpoofGroup": alcatelIND1IPXMIBWatchdogSpoofGroup,
       "alcatelIND1IPXMIBSerialFilterGroup": alcatelIND1IPXMIBSerialFilterGroup,
       "alcatelIND1IPXMIBKeepaliveSpoofGroup": alcatelIND1IPXMIBKeepaliveSpoofGroup,
       "alcatelIND1IPXMIBType20Group": alcatelIND1IPXMIBType20Group,
       "alcatelIND1IPXMIBTimerGroup": alcatelIND1IPXMIBTimerGroup}
)
