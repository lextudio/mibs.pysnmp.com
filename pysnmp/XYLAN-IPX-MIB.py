# SNMP MIB module (XYLAN-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:07 2024
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

(xylanIpxArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanIpxArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanIpxRoutingGroup_ObjectIdentity = ObjectIdentity
xylanIpxRoutingGroup = _XylanIpxRoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1)
)
_XylanIpxStaticRouteTable_Object = MibTable
xylanIpxStaticRouteTable = _XylanIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    xylanIpxStaticRouteTable.setStatus("mandatory")
_XylanIpxStaticRouteEntry_Object = MibTableRow
xylanIpxStaticRouteEntry = _XylanIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1)
)
xylanIpxStaticRouteEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxStaticRouteNetNum"),
)
if mibBuilder.loadTexts:
    xylanIpxStaticRouteEntry.setStatus("mandatory")


class _XylanIpxStaticRouteNetNum_Type(OctetString):
    """Custom type xylanIpxStaticRouteNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanIpxStaticRouteNetNum_Type.__name__ = "OctetString"
_XylanIpxStaticRouteNetNum_Object = MibTableColumn
xylanIpxStaticRouteNetNum = _XylanIpxStaticRouteNetNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1, 1),
    _XylanIpxStaticRouteNetNum_Type()
)
xylanIpxStaticRouteNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxStaticRouteNetNum.setStatus("mandatory")


class _XylanIpxStaticRouteAdminState_Type(Integer32):
    """Custom type xylanIpxStaticRouteAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanIpxStaticRouteAdminState_Type.__name__ = "Integer32"
_XylanIpxStaticRouteAdminState_Object = MibTableColumn
xylanIpxStaticRouteAdminState = _XylanIpxStaticRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1, 2),
    _XylanIpxStaticRouteAdminState_Type()
)
xylanIpxStaticRouteAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxStaticRouteAdminState.setStatus("mandatory")


class _XylanIpxStaticRouteNextHopNet_Type(OctetString):
    """Custom type xylanIpxStaticRouteNextHopNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanIpxStaticRouteNextHopNet_Type.__name__ = "OctetString"
_XylanIpxStaticRouteNextHopNet_Object = MibTableColumn
xylanIpxStaticRouteNextHopNet = _XylanIpxStaticRouteNextHopNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1, 3),
    _XylanIpxStaticRouteNextHopNet_Type()
)
xylanIpxStaticRouteNextHopNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxStaticRouteNextHopNet.setStatus("mandatory")


class _XylanIpxStaticRouteNextHopNode_Type(OctetString):
    """Custom type xylanIpxStaticRouteNextHopNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanIpxStaticRouteNextHopNode_Type.__name__ = "OctetString"
_XylanIpxStaticRouteNextHopNode_Object = MibTableColumn
xylanIpxStaticRouteNextHopNode = _XylanIpxStaticRouteNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1, 4),
    _XylanIpxStaticRouteNextHopNode_Type()
)
xylanIpxStaticRouteNextHopNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxStaticRouteNextHopNode.setStatus("mandatory")
_XylanIpxStaticRouteTicks_Type = Integer32
_XylanIpxStaticRouteTicks_Object = MibTableColumn
xylanIpxStaticRouteTicks = _XylanIpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1, 5),
    _XylanIpxStaticRouteTicks_Type()
)
xylanIpxStaticRouteTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpxStaticRouteTicks.setStatus("mandatory")
_XylanIpxStaticRouteHopCount_Type = Integer32
_XylanIpxStaticRouteHopCount_Object = MibTableColumn
xylanIpxStaticRouteHopCount = _XylanIpxStaticRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 1, 1, 1, 6),
    _XylanIpxStaticRouteHopCount_Type()
)
xylanIpxStaticRouteHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpxStaticRouteHopCount.setStatus("mandatory")
_XylanIpxFilterGroup_ObjectIdentity = ObjectIdentity
xylanIpxFilterGroup = _XylanIpxFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2)
)
_XylanIpxRipSapFilterTable_Object = MibTable
xylanIpxRipSapFilterTable = _XylanIpxRipSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterTable.setStatus("mandatory")
_XylanIpxRipSapFilterEntry_Object = MibTableRow
xylanIpxRipSapFilterEntry = _XylanIpxRipSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1)
)
xylanIpxRipSapFilterEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxRipSapFilterNum"),
)
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterEntry.setStatus("mandatory")
_XylanIpxRipSapFilterNum_Type = Integer32
_XylanIpxRipSapFilterNum_Object = MibTableColumn
xylanIpxRipSapFilterNum = _XylanIpxRipSapFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 1),
    _XylanIpxRipSapFilterNum_Type()
)
xylanIpxRipSapFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterNum.setStatus("mandatory")


class _XylanIpxRipSapFilterAdminState_Type(Integer32):
    """Custom type xylanIpxRipSapFilterAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanIpxRipSapFilterAdminState_Type.__name__ = "Integer32"
_XylanIpxRipSapFilterAdminState_Object = MibTableColumn
xylanIpxRipSapFilterAdminState = _XylanIpxRipSapFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 2),
    _XylanIpxRipSapFilterAdminState_Type()
)
xylanIpxRipSapFilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterAdminState.setStatus("mandatory")


class _XylanIpxRipSapFilterType_Type(Integer32):
    """Custom type xylanIpxRipSapFilterType based on Integer32"""
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
        *(("gns-output", 3),
          ("rip-input", 5),
          ("rip-output", 4),
          ("sap-input", 2),
          ("sap-output", 1))
    )


_XylanIpxRipSapFilterType_Type.__name__ = "Integer32"
_XylanIpxRipSapFilterType_Object = MibTableColumn
xylanIpxRipSapFilterType = _XylanIpxRipSapFilterType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 3),
    _XylanIpxRipSapFilterType_Type()
)
xylanIpxRipSapFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterType.setStatus("mandatory")


class _XylanIpxRipSapFilterNet_Type(OctetString):
    """Custom type xylanIpxRipSapFilterNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanIpxRipSapFilterNet_Type.__name__ = "OctetString"
_XylanIpxRipSapFilterNet_Object = MibTableColumn
xylanIpxRipSapFilterNet = _XylanIpxRipSapFilterNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 4),
    _XylanIpxRipSapFilterNet_Type()
)
xylanIpxRipSapFilterNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterNet.setStatus("mandatory")


class _XylanIpxRipSapFilterNetMask_Type(OctetString):
    """Custom type xylanIpxRipSapFilterNetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanIpxRipSapFilterNetMask_Type.__name__ = "OctetString"
_XylanIpxRipSapFilterNetMask_Object = MibTableColumn
xylanIpxRipSapFilterNetMask = _XylanIpxRipSapFilterNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 5),
    _XylanIpxRipSapFilterNetMask_Type()
)
xylanIpxRipSapFilterNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterNetMask.setStatus("mandatory")


class _XylanIpxRipSapFilterNode_Type(OctetString):
    """Custom type xylanIpxRipSapFilterNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanIpxRipSapFilterNode_Type.__name__ = "OctetString"
_XylanIpxRipSapFilterNode_Object = MibTableColumn
xylanIpxRipSapFilterNode = _XylanIpxRipSapFilterNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 6),
    _XylanIpxRipSapFilterNode_Type()
)
xylanIpxRipSapFilterNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterNode.setStatus("mandatory")


class _XylanIpxRipSapFilterNodeMask_Type(OctetString):
    """Custom type xylanIpxRipSapFilterNodeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanIpxRipSapFilterNodeMask_Type.__name__ = "OctetString"
_XylanIpxRipSapFilterNodeMask_Object = MibTableColumn
xylanIpxRipSapFilterNodeMask = _XylanIpxRipSapFilterNodeMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 7),
    _XylanIpxRipSapFilterNodeMask_Type()
)
xylanIpxRipSapFilterNodeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterNodeMask.setStatus("mandatory")


class _XylanIpxRipSapFilterSvcType_Type(Integer32):
    """Custom type xylanIpxRipSapFilterSvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanIpxRipSapFilterSvcType_Type.__name__ = "Integer32"
_XylanIpxRipSapFilterSvcType_Object = MibTableColumn
xylanIpxRipSapFilterSvcType = _XylanIpxRipSapFilterSvcType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 8),
    _XylanIpxRipSapFilterSvcType_Type()
)
xylanIpxRipSapFilterSvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterSvcType.setStatus("mandatory")


class _XylanIpxRipSapFilterMode_Type(Integer32):
    """Custom type xylanIpxRipSapFilterMode based on Integer32"""
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


_XylanIpxRipSapFilterMode_Type.__name__ = "Integer32"
_XylanIpxRipSapFilterMode_Object = MibTableColumn
xylanIpxRipSapFilterMode = _XylanIpxRipSapFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 9),
    _XylanIpxRipSapFilterMode_Type()
)
xylanIpxRipSapFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterMode.setStatus("mandatory")
_XylanIpxRipSapFilterGroupId_Type = Integer32
_XylanIpxRipSapFilterGroupId_Object = MibTableColumn
xylanIpxRipSapFilterGroupId = _XylanIpxRipSapFilterGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 10),
    _XylanIpxRipSapFilterGroupId_Type()
)
xylanIpxRipSapFilterGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterGroupId.setStatus("mandatory")
_XylanIpxRipSapFilterVlanId_Type = Integer32
_XylanIpxRipSapFilterVlanId_Object = MibTableColumn
xylanIpxRipSapFilterVlanId = _XylanIpxRipSapFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 11),
    _XylanIpxRipSapFilterVlanId_Type()
)
xylanIpxRipSapFilterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterVlanId.setStatus("mandatory")


class _XylanIpxRipSapFilterWanType_Type(Integer32):
    """Custom type xylanIpxRipSapFilterWanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 2),
          ("not-used", 1),
          ("ppp", 3))
    )


_XylanIpxRipSapFilterWanType_Type.__name__ = "Integer32"
_XylanIpxRipSapFilterWanType_Object = MibTableColumn
xylanIpxRipSapFilterWanType = _XylanIpxRipSapFilterWanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 12),
    _XylanIpxRipSapFilterWanType_Type()
)
xylanIpxRipSapFilterWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterWanType.setStatus("mandatory")
_XylanIpxRipSapFilterSlot_Type = Integer32
_XylanIpxRipSapFilterSlot_Object = MibTableColumn
xylanIpxRipSapFilterSlot = _XylanIpxRipSapFilterSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 13),
    _XylanIpxRipSapFilterSlot_Type()
)
xylanIpxRipSapFilterSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterSlot.setStatus("mandatory")
_XylanIpxRipSapFilterPort_Type = Integer32
_XylanIpxRipSapFilterPort_Object = MibTableColumn
xylanIpxRipSapFilterPort = _XylanIpxRipSapFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 14),
    _XylanIpxRipSapFilterPort_Type()
)
xylanIpxRipSapFilterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterPort.setStatus("mandatory")
_XylanIpxRipSapFilterVc_Type = Integer32
_XylanIpxRipSapFilterVc_Object = MibTableColumn
xylanIpxRipSapFilterVc = _XylanIpxRipSapFilterVc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 15),
    _XylanIpxRipSapFilterVc_Type()
)
xylanIpxRipSapFilterVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterVc.setStatus("mandatory")
_XylanIpxRipSapFilterPeerId_Type = Integer32
_XylanIpxRipSapFilterPeerId_Object = MibTableColumn
xylanIpxRipSapFilterPeerId = _XylanIpxRipSapFilterPeerId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 2, 1, 1, 16),
    _XylanIpxRipSapFilterPeerId_Type()
)
xylanIpxRipSapFilterPeerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxRipSapFilterPeerId.setStatus("mandatory")
_XylanIpxWatchdogSpoofGroup_ObjectIdentity = ObjectIdentity
xylanIpxWatchdogSpoofGroup = _XylanIpxWatchdogSpoofGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 3)
)
_XylanIpxWatchdogSpoofTable_Object = MibTable
xylanIpxWatchdogSpoofTable = _XylanIpxWatchdogSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    xylanIpxWatchdogSpoofTable.setStatus("mandatory")
_XylanIpxWatchdogSpoofEntry_Object = MibTableRow
xylanIpxWatchdogSpoofEntry = _XylanIpxWatchdogSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 3, 1, 1)
)
xylanIpxWatchdogSpoofEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxWatchdogSpoofGroupId"),
)
if mibBuilder.loadTexts:
    xylanIpxWatchdogSpoofEntry.setStatus("mandatory")


class _XylanIpxWatchdogSpoofGroupId_Type(Integer32):
    """Custom type xylanIpxWatchdogSpoofGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanIpxWatchdogSpoofGroupId_Type.__name__ = "Integer32"
_XylanIpxWatchdogSpoofGroupId_Object = MibTableColumn
xylanIpxWatchdogSpoofGroupId = _XylanIpxWatchdogSpoofGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 3, 1, 1, 1),
    _XylanIpxWatchdogSpoofGroupId_Type()
)
xylanIpxWatchdogSpoofGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxWatchdogSpoofGroupId.setStatus("mandatory")


class _XylanIpxWatchdogSpoofMode_Type(Integer32):
    """Custom type xylanIpxWatchdogSpoofMode based on Integer32"""
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


_XylanIpxWatchdogSpoofMode_Type.__name__ = "Integer32"
_XylanIpxWatchdogSpoofMode_Object = MibTableColumn
xylanIpxWatchdogSpoofMode = _XylanIpxWatchdogSpoofMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 3, 1, 1, 2),
    _XylanIpxWatchdogSpoofMode_Type()
)
xylanIpxWatchdogSpoofMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxWatchdogSpoofMode.setStatus("mandatory")
_XylanIpxSerialFilterGroup_ObjectIdentity = ObjectIdentity
xylanIpxSerialFilterGroup = _XylanIpxSerialFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 4)
)
_XylanIpxSerialFilterTable_Object = MibTable
xylanIpxSerialFilterTable = _XylanIpxSerialFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    xylanIpxSerialFilterTable.setStatus("mandatory")
_XylanIpxSerialFilterEntry_Object = MibTableRow
xylanIpxSerialFilterEntry = _XylanIpxSerialFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 4, 1, 1)
)
xylanIpxSerialFilterEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxSerialFilterGroupId"),
)
if mibBuilder.loadTexts:
    xylanIpxSerialFilterEntry.setStatus("mandatory")


class _XylanIpxSerialFilterGroupId_Type(Integer32):
    """Custom type xylanIpxSerialFilterGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanIpxSerialFilterGroupId_Type.__name__ = "Integer32"
_XylanIpxSerialFilterGroupId_Object = MibTableColumn
xylanIpxSerialFilterGroupId = _XylanIpxSerialFilterGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 4, 1, 1, 1),
    _XylanIpxSerialFilterGroupId_Type()
)
xylanIpxSerialFilterGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxSerialFilterGroupId.setStatus("mandatory")


class _XylanIpxSerialFilterMode_Type(Integer32):
    """Custom type xylanIpxSerialFilterMode based on Integer32"""
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


_XylanIpxSerialFilterMode_Type.__name__ = "Integer32"
_XylanIpxSerialFilterMode_Object = MibTableColumn
xylanIpxSerialFilterMode = _XylanIpxSerialFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 4, 1, 1, 2),
    _XylanIpxSerialFilterMode_Type()
)
xylanIpxSerialFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxSerialFilterMode.setStatus("mandatory")
_XylanSpxKeepaliveSpoofGroup_ObjectIdentity = ObjectIdentity
xylanSpxKeepaliveSpoofGroup = _XylanSpxKeepaliveSpoofGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 5)
)
_XylanSpxKeepaliveSpoofTable_Object = MibTable
xylanSpxKeepaliveSpoofTable = _XylanSpxKeepaliveSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 5, 1)
)
if mibBuilder.loadTexts:
    xylanSpxKeepaliveSpoofTable.setStatus("mandatory")
_XylanSpxKeepaliveSpoofEntry_Object = MibTableRow
xylanSpxKeepaliveSpoofEntry = _XylanSpxKeepaliveSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 5, 1, 1)
)
xylanSpxKeepaliveSpoofEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanSpxKeepaliveSpoofGroupId"),
)
if mibBuilder.loadTexts:
    xylanSpxKeepaliveSpoofEntry.setStatus("mandatory")


class _XylanSpxKeepaliveSpoofGroupId_Type(Integer32):
    """Custom type xylanSpxKeepaliveSpoofGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanSpxKeepaliveSpoofGroupId_Type.__name__ = "Integer32"
_XylanSpxKeepaliveSpoofGroupId_Object = MibTableColumn
xylanSpxKeepaliveSpoofGroupId = _XylanSpxKeepaliveSpoofGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 5, 1, 1, 1),
    _XylanSpxKeepaliveSpoofGroupId_Type()
)
xylanSpxKeepaliveSpoofGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanSpxKeepaliveSpoofGroupId.setStatus("mandatory")


class _XylanSpxKeepaliveSpoofMode_Type(Integer32):
    """Custom type xylanSpxKeepaliveSpoofMode based on Integer32"""
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


_XylanSpxKeepaliveSpoofMode_Type.__name__ = "Integer32"
_XylanSpxKeepaliveSpoofMode_Object = MibTableColumn
xylanSpxKeepaliveSpoofMode = _XylanSpxKeepaliveSpoofMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 5, 1, 1, 2),
    _XylanSpxKeepaliveSpoofMode_Type()
)
xylanSpxKeepaliveSpoofMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanSpxKeepaliveSpoofMode.setStatus("mandatory")
_XylanIpxType20Group_ObjectIdentity = ObjectIdentity
xylanIpxType20Group = _XylanIpxType20Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 6)
)
_XylanIpxType20Table_Object = MibTable
xylanIpxType20Table = _XylanIpxType20Table_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 6, 1)
)
if mibBuilder.loadTexts:
    xylanIpxType20Table.setStatus("mandatory")
_XylanIpxType20Entry_Object = MibTableRow
xylanIpxType20Entry = _XylanIpxType20Entry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 6, 1, 1)
)
xylanIpxType20Entry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxType20VlanId"),
)
if mibBuilder.loadTexts:
    xylanIpxType20Entry.setStatus("mandatory")


class _XylanIpxType20VlanId_Type(Integer32):
    """Custom type xylanIpxType20VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanIpxType20VlanId_Type.__name__ = "Integer32"
_XylanIpxType20VlanId_Object = MibTableColumn
xylanIpxType20VlanId = _XylanIpxType20VlanId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 6, 1, 1, 1),
    _XylanIpxType20VlanId_Type()
)
xylanIpxType20VlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxType20VlanId.setStatus("mandatory")


class _XylanIpxType20Mode_Type(Integer32):
    """Custom type xylanIpxType20Mode based on Integer32"""
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


_XylanIpxType20Mode_Type.__name__ = "Integer32"
_XylanIpxType20Mode_Object = MibTableColumn
xylanIpxType20Mode = _XylanIpxType20Mode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 6, 1, 1, 2),
    _XylanIpxType20Mode_Type()
)
xylanIpxType20Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxType20Mode.setStatus("mandatory")
_XylanIpxTimerGroup_ObjectIdentity = ObjectIdentity
xylanIpxTimerGroup = _XylanIpxTimerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 7)
)
_XylanIpxTimerTable_Object = MibTable
xylanIpxTimerTable = _XylanIpxTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 7, 1)
)
if mibBuilder.loadTexts:
    xylanIpxTimerTable.setStatus("mandatory")
_XylanIpxTimerEntry_Object = MibTableRow
xylanIpxTimerEntry = _XylanIpxTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 7, 1, 1)
)
xylanIpxTimerEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxTimerVlanId"),
)
if mibBuilder.loadTexts:
    xylanIpxTimerEntry.setStatus("mandatory")


class _XylanIpxTimerVlanId_Type(Integer32):
    """Custom type xylanIpxTimerVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XylanIpxTimerVlanId_Type.__name__ = "Integer32"
_XylanIpxTimerVlanId_Object = MibTableColumn
xylanIpxTimerVlanId = _XylanIpxTimerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 7, 1, 1, 1),
    _XylanIpxTimerVlanId_Type()
)
xylanIpxTimerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxTimerVlanId.setStatus("mandatory")


class _XylanIpxTimerSap_Type(Integer32):
    """Custom type xylanIpxTimerSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_XylanIpxTimerSap_Type.__name__ = "Integer32"
_XylanIpxTimerSap_Object = MibTableColumn
xylanIpxTimerSap = _XylanIpxTimerSap_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 7, 1, 1, 2),
    _XylanIpxTimerSap_Type()
)
xylanIpxTimerSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxTimerSap.setStatus("mandatory")


class _XylanIpxTimerRip_Type(Integer32):
    """Custom type xylanIpxTimerRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_XylanIpxTimerRip_Type.__name__ = "Integer32"
_XylanIpxTimerRip_Object = MibTableColumn
xylanIpxTimerRip = _XylanIpxTimerRip_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 7, 1, 1, 3),
    _XylanIpxTimerRip_Type()
)
xylanIpxTimerRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxTimerRip.setStatus("mandatory")
_XylanIpxDefRouteGroup_ObjectIdentity = ObjectIdentity
xylanIpxDefRouteGroup = _XylanIpxDefRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 8)
)
_XylanIpxDefRouteTable_Object = MibTable
xylanIpxDefRouteTable = _XylanIpxDefRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 8, 1)
)
if mibBuilder.loadTexts:
    xylanIpxDefRouteTable.setStatus("mandatory")
_XylanIpxDefRouteEntry_Object = MibTableRow
xylanIpxDefRouteEntry = _XylanIpxDefRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 8, 1, 1)
)
xylanIpxDefRouteEntry.setIndexNames(
    (0, "XYLAN-IPX-MIB", "xylanIpxDefRouteNum"),
)
if mibBuilder.loadTexts:
    xylanIpxDefRouteEntry.setStatus("mandatory")
_XylanIpxDefRouteNum_Type = Integer32
_XylanIpxDefRouteNum_Object = MibTableColumn
xylanIpxDefRouteNum = _XylanIpxDefRouteNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 8, 1, 1, 1),
    _XylanIpxDefRouteNum_Type()
)
xylanIpxDefRouteNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxDefRouteNum.setStatus("mandatory")


class _XylanIpxDefRouteNet_Type(OctetString):
    """Custom type xylanIpxDefRouteNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_XylanIpxDefRouteNet_Type.__name__ = "OctetString"
_XylanIpxDefRouteNet_Object = MibTableColumn
xylanIpxDefRouteNet = _XylanIpxDefRouteNet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 8, 1, 1, 2),
    _XylanIpxDefRouteNet_Type()
)
xylanIpxDefRouteNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxDefRouteNet.setStatus("mandatory")


class _XylanIpxDefRouteNode_Type(OctetString):
    """Custom type xylanIpxDefRouteNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_XylanIpxDefRouteNode_Type.__name__ = "OctetString"
_XylanIpxDefRouteNode_Object = MibTableColumn
xylanIpxDefRouteNode = _XylanIpxDefRouteNode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 8, 1, 1, 3),
    _XylanIpxDefRouteNode_Type()
)
xylanIpxDefRouteNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxDefRouteNode.setStatus("mandatory")
_XylanIpxExtGroup_ObjectIdentity = ObjectIdentity
xylanIpxExtGroup = _XylanIpxExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 9)
)
_XylanIpxExtMsg_Type = Integer32
_XylanIpxExtMsg_Object = MibScalar
xylanIpxExtMsg = _XylanIpxExtMsg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 6, 9, 1),
    _XylanIpxExtMsg_Type()
)
xylanIpxExtMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanIpxExtMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-IPX-MIB",
    **{"xylanIpxRoutingGroup": xylanIpxRoutingGroup,
       "xylanIpxStaticRouteTable": xylanIpxStaticRouteTable,
       "xylanIpxStaticRouteEntry": xylanIpxStaticRouteEntry,
       "xylanIpxStaticRouteNetNum": xylanIpxStaticRouteNetNum,
       "xylanIpxStaticRouteAdminState": xylanIpxStaticRouteAdminState,
       "xylanIpxStaticRouteNextHopNet": xylanIpxStaticRouteNextHopNet,
       "xylanIpxStaticRouteNextHopNode": xylanIpxStaticRouteNextHopNode,
       "xylanIpxStaticRouteTicks": xylanIpxStaticRouteTicks,
       "xylanIpxStaticRouteHopCount": xylanIpxStaticRouteHopCount,
       "xylanIpxFilterGroup": xylanIpxFilterGroup,
       "xylanIpxRipSapFilterTable": xylanIpxRipSapFilterTable,
       "xylanIpxRipSapFilterEntry": xylanIpxRipSapFilterEntry,
       "xylanIpxRipSapFilterNum": xylanIpxRipSapFilterNum,
       "xylanIpxRipSapFilterAdminState": xylanIpxRipSapFilterAdminState,
       "xylanIpxRipSapFilterType": xylanIpxRipSapFilterType,
       "xylanIpxRipSapFilterNet": xylanIpxRipSapFilterNet,
       "xylanIpxRipSapFilterNetMask": xylanIpxRipSapFilterNetMask,
       "xylanIpxRipSapFilterNode": xylanIpxRipSapFilterNode,
       "xylanIpxRipSapFilterNodeMask": xylanIpxRipSapFilterNodeMask,
       "xylanIpxRipSapFilterSvcType": xylanIpxRipSapFilterSvcType,
       "xylanIpxRipSapFilterMode": xylanIpxRipSapFilterMode,
       "xylanIpxRipSapFilterGroupId": xylanIpxRipSapFilterGroupId,
       "xylanIpxRipSapFilterVlanId": xylanIpxRipSapFilterVlanId,
       "xylanIpxRipSapFilterWanType": xylanIpxRipSapFilterWanType,
       "xylanIpxRipSapFilterSlot": xylanIpxRipSapFilterSlot,
       "xylanIpxRipSapFilterPort": xylanIpxRipSapFilterPort,
       "xylanIpxRipSapFilterVc": xylanIpxRipSapFilterVc,
       "xylanIpxRipSapFilterPeerId": xylanIpxRipSapFilterPeerId,
       "xylanIpxWatchdogSpoofGroup": xylanIpxWatchdogSpoofGroup,
       "xylanIpxWatchdogSpoofTable": xylanIpxWatchdogSpoofTable,
       "xylanIpxWatchdogSpoofEntry": xylanIpxWatchdogSpoofEntry,
       "xylanIpxWatchdogSpoofGroupId": xylanIpxWatchdogSpoofGroupId,
       "xylanIpxWatchdogSpoofMode": xylanIpxWatchdogSpoofMode,
       "xylanIpxSerialFilterGroup": xylanIpxSerialFilterGroup,
       "xylanIpxSerialFilterTable": xylanIpxSerialFilterTable,
       "xylanIpxSerialFilterEntry": xylanIpxSerialFilterEntry,
       "xylanIpxSerialFilterGroupId": xylanIpxSerialFilterGroupId,
       "xylanIpxSerialFilterMode": xylanIpxSerialFilterMode,
       "xylanSpxKeepaliveSpoofGroup": xylanSpxKeepaliveSpoofGroup,
       "xylanSpxKeepaliveSpoofTable": xylanSpxKeepaliveSpoofTable,
       "xylanSpxKeepaliveSpoofEntry": xylanSpxKeepaliveSpoofEntry,
       "xylanSpxKeepaliveSpoofGroupId": xylanSpxKeepaliveSpoofGroupId,
       "xylanSpxKeepaliveSpoofMode": xylanSpxKeepaliveSpoofMode,
       "xylanIpxType20Group": xylanIpxType20Group,
       "xylanIpxType20Table": xylanIpxType20Table,
       "xylanIpxType20Entry": xylanIpxType20Entry,
       "xylanIpxType20VlanId": xylanIpxType20VlanId,
       "xylanIpxType20Mode": xylanIpxType20Mode,
       "xylanIpxTimerGroup": xylanIpxTimerGroup,
       "xylanIpxTimerTable": xylanIpxTimerTable,
       "xylanIpxTimerEntry": xylanIpxTimerEntry,
       "xylanIpxTimerVlanId": xylanIpxTimerVlanId,
       "xylanIpxTimerSap": xylanIpxTimerSap,
       "xylanIpxTimerRip": xylanIpxTimerRip,
       "xylanIpxDefRouteGroup": xylanIpxDefRouteGroup,
       "xylanIpxDefRouteTable": xylanIpxDefRouteTable,
       "xylanIpxDefRouteEntry": xylanIpxDefRouteEntry,
       "xylanIpxDefRouteNum": xylanIpxDefRouteNum,
       "xylanIpxDefRouteNet": xylanIpxDefRouteNet,
       "xylanIpxDefRouteNode": xylanIpxDefRouteNode,
       "xylanIpxExtGroup": xylanIpxExtGroup,
       "xylanIpxExtMsg": xylanIpxExtMsg}
)
