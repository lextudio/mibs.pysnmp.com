# SNMP MIB module (WWP-LEOS-VPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-VPLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:02 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosVplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28)
)
wwpLeosVplsMIB.setRevisions(
        ("2011-06-06 00:00",
         "2010-03-23 17:00",
         "2010-02-10 17:00",
         "2010-01-27 04:25",
         "2009-08-24 04:24",
         "2008-11-14 00:00",
         "2008-09-03 08:39",
         "2008-06-11 00:50",
         "2008-05-15 00:50",
         "2006-09-22 00:50",
         "2006-05-04 17:00",
         "2005-08-15 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )



class EtherType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosVplsMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBObjects = _WwpLeosVplsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1)
)
_WwpLeosVpls_ObjectIdentity = ObjectIdentity
wwpLeosVpls = _WwpLeosVpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1)
)
_WwpLeosVplsVirtualCircuitTable_Object = MibTable
wwpLeosVplsVirtualCircuitTable = _WwpLeosVplsVirtualCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitTable.setStatus("deprecated")
_WwpLeosVplsVirtualCircuitEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEntry = _WwpLeosVplsVirtualCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1)
)
wwpLeosVplsVirtualCircuitEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEntry.setStatus("deprecated")


class _WwpLeosVplsVirtualCircuitIndex_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitIndex_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitIndex_Object = MibTableColumn
wwpLeosVplsVirtualCircuitIndex = _WwpLeosVplsVirtualCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 1),
    _WwpLeosVplsVirtualCircuitIndex_Type()
)
wwpLeosVplsVirtualCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitIndex.setStatus("deprecated")
_WwpLeosVplsVirtualCircuitProviderVlanId_Type = VlanId
_WwpLeosVplsVirtualCircuitProviderVlanId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitProviderVlanId = _WwpLeosVplsVirtualCircuitProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 2),
    _WwpLeosVplsVirtualCircuitProviderVlanId_Type()
)
wwpLeosVplsVirtualCircuitProviderVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitProviderVlanId.setStatus("deprecated")


class _WwpLeosVplsVirtualCircuitType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosVplsVirtualCircuitType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitType_Object = MibTableColumn
wwpLeosVplsVirtualCircuitType = _WwpLeosVplsVirtualCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 3),
    _WwpLeosVplsVirtualCircuitType_Type()
)
wwpLeosVplsVirtualCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitType.setStatus("deprecated")


class _WwpLeosVplsVirtualCircuitName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualCircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsVirtualCircuitName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualCircuitName_Object = MibTableColumn
wwpLeosVplsVirtualCircuitName = _WwpLeosVplsVirtualCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 4),
    _WwpLeosVplsVirtualCircuitName_Type()
)
wwpLeosVplsVirtualCircuitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitName.setStatus("deprecated")


class _WwpLeosVplsVirtualCircuitIngressVcLabel_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitIngressVcLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsVirtualCircuitIngressVcLabel_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitIngressVcLabel_Object = MibTableColumn
wwpLeosVplsVirtualCircuitIngressVcLabel = _WwpLeosVplsVirtualCircuitIngressVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 5),
    _WwpLeosVplsVirtualCircuitIngressVcLabel_Type()
)
wwpLeosVplsVirtualCircuitIngressVcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitIngressVcLabel.setStatus("deprecated")


class _WwpLeosVplsVirtualCircuitEgressVcLabel_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEgressVcLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsVirtualCircuitEgressVcLabel_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEgressVcLabel_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEgressVcLabel = _WwpLeosVplsVirtualCircuitEgressVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 6),
    _WwpLeosVplsVirtualCircuitEgressVcLabel_Type()
)
wwpLeosVplsVirtualCircuitEgressVcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEgressVcLabel.setStatus("deprecated")


class _WwpLeosVplsVirtualCircuitTunnelIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitTunnelIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitTunnelIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitTunnelIndx_Object = MibTableColumn
wwpLeosVplsVirtualCircuitTunnelIndx = _WwpLeosVplsVirtualCircuitTunnelIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 7),
    _WwpLeosVplsVirtualCircuitTunnelIndx_Type()
)
wwpLeosVplsVirtualCircuitTunnelIndx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitTunnelIndx.setStatus("deprecated")
_WwpLeosVplsVirtualCircuitStatus_Type = RowStatus
_WwpLeosVplsVirtualCircuitStatus_Object = MibTableColumn
wwpLeosVplsVirtualCircuitStatus = _WwpLeosVplsVirtualCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 1, 1, 8),
    _WwpLeosVplsVirtualCircuitStatus_Type()
)
wwpLeosVplsVirtualCircuitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitStatus.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchTable_Object = MibTable
wwpLeosVplsVirtualSwitchTable = _WwpLeosVplsVirtualSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchTable.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEntry = _WwpLeosVplsVirtualSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1)
)
wwpLeosVplsVirtualSwitchEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEntry.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchIndx_Object = MibTableColumn
wwpLeosVplsVirtualSwitchIndx = _WwpLeosVplsVirtualSwitchIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 1),
    _WwpLeosVplsVirtualSwitchIndx_Type()
)
wwpLeosVplsVirtualSwitchIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchIndx.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchName_Type(OctetString):
    """Custom type wwpLeosVplsVirtualSwitchName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosVplsVirtualSwitchName_Type.__name__ = "OctetString"
_WwpLeosVplsVirtualSwitchName_Object = MibTableColumn
wwpLeosVplsVirtualSwitchName = _WwpLeosVplsVirtualSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 2),
    _WwpLeosVplsVirtualSwitchName_Type()
)
wwpLeosVplsVirtualSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchName.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchPriVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchPriVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualSwitchPriVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchPriVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchPriVc = _WwpLeosVplsVirtualSwitchPriVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 3),
    _WwpLeosVplsVirtualSwitchPriVc_Type()
)
wwpLeosVplsVirtualSwitchPriVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchPriVc.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchSecVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchSecVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualSwitchSecVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchSecVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchSecVc = _WwpLeosVplsVirtualSwitchSecVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 4),
    _WwpLeosVplsVirtualSwitchSecVc_Type()
)
wwpLeosVplsVirtualSwitchSecVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchSecVc.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchActiveVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchActiveVc based on Integer32"""
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
          ("primVc", 2),
          ("secVc", 3))
    )


_WwpLeosVplsVirtualSwitchActiveVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchActiveVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchActiveVc = _WwpLeosVplsVirtualSwitchActiveVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 5),
    _WwpLeosVplsVirtualSwitchActiveVc_Type()
)
wwpLeosVplsVirtualSwitchActiveVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchActiveVc.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEncapCosPolicy based on Integer32"""
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
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4))
    )


_WwpLeosVplsVirtualSwitchEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEncapCosPolicy = _WwpLeosVplsVirtualSwitchEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 6),
    _WwpLeosVplsVirtualSwitchEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEncapCosPolicy.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEncapFixedDot1dPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEncapFixedDot1dPri = _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 7),
    _WwpLeosVplsVirtualSwitchEncapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchEncapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEncapFixedDot1dPri.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchDecapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchDecapCosPolicy based on Integer32"""
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
        *(("fixed", 1),
          ("inheritTunnel", 3),
          ("inheritVc", 2),
          ("leave", 4))
    )


_WwpLeosVplsVirtualSwitchDecapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchDecapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchDecapCosPolicy = _WwpLeosVplsVirtualSwitchDecapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 8),
    _WwpLeosVplsVirtualSwitchDecapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchDecapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchDecapCosPolicy.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchDecapFixedDot1dPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchDecapFixedDot1dPri = _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 9),
    _WwpLeosVplsVirtualSwitchDecapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchDecapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchDecapFixedDot1dPri.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchSubscriberVlan_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchSubscriberVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosVplsVirtualSwitchSubscriberVlan_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchSubscriberVlan_Object = MibTableColumn
wwpLeosVplsVirtualSwitchSubscriberVlan = _WwpLeosVplsVirtualSwitchSubscriberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 10),
    _WwpLeosVplsVirtualSwitchSubscriberVlan_Type()
)
wwpLeosVplsVirtualSwitchSubscriberVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchSubscriberVlan.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState = _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 11),
    _WwpLeosVplsVirtualSwitchCtrlProtocolTunnelState_Type()
)
wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("mpls", 2))
    )


_WwpLeosVplsVirtualSwitchType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchType_Object = MibTableColumn
wwpLeosVplsVirtualSwitchType = _WwpLeosVplsVirtualSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 12),
    _WwpLeosVplsVirtualSwitchType_Type()
)
wwpLeosVplsVirtualSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchType.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchStatus = _WwpLeosVplsVirtualSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 5, 1, 13),
    _WwpLeosVplsVirtualSwitchStatus_Type()
)
wwpLeosVplsVirtualSwitchStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchStatus.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchMemberTable_Object = MibTable
wwpLeosVplsVirtualSwitchMemberTable = _WwpLeosVplsVirtualSwitchMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberTable.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchMemberEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMemberEntry = _WwpLeosVplsVirtualSwitchMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6, 1)
)
wwpLeosVplsVirtualSwitchMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberEntry.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchMemberPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMemberPortId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMemberPortId = _WwpLeosVplsVirtualSwitchMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6, 1, 1),
    _WwpLeosVplsVirtualSwitchMemberPortId_Type()
)
wwpLeosVplsVirtualSwitchMemberPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberPortId.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchMemberStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMemberStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMemberStatus = _WwpLeosVplsVirtualSwitchMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 6, 1, 2),
    _WwpLeosVplsVirtualSwitchMemberStatus_Type()
)
wwpLeosVplsVirtualSwitchMemberStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMemberStatus.setStatus("deprecated")
_WwpLeosVplsSwitchCtrlProtocolTable_Object = MibTable
wwpLeosVplsSwitchCtrlProtocolTable = _WwpLeosVplsSwitchCtrlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlProtocolTable.setStatus("deprecated")
_WwpLeosVplsSwitchCtrlProtocolEntry_Object = MibTableRow
wwpLeosVplsSwitchCtrlProtocolEntry = _WwpLeosVplsSwitchCtrlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7, 1)
)
wwpLeosVplsSwitchCtrlProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsSwitchCtrlProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlProtocolEntry.setStatus("deprecated")


class _WwpLeosVplsSwitchCtrlProtocolNum_Type(Integer32):
    """Custom type wwpLeosVplsSwitchCtrlProtocolNum based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUdlp", 8),
          ("ciscoUplinkFast", 7),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("l28021x", 1),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("lldp", 14),
          ("oam", 13),
          ("rstp", 2),
          ("vlanBridge", 15))
    )


_WwpLeosVplsSwitchCtrlProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchCtrlProtocolNum_Object = MibTableColumn
wwpLeosVplsSwitchCtrlProtocolNum = _WwpLeosVplsSwitchCtrlProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7, 1, 1),
    _WwpLeosVplsSwitchCtrlProtocolNum_Type()
)
wwpLeosVplsSwitchCtrlProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlProtocolNum.setStatus("deprecated")


class _WwpLeosVplsSwitchCtrlType_Type(Integer32):
    """Custom type wwpLeosVplsSwitchCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )


_WwpLeosVplsSwitchCtrlType_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchCtrlType_Object = MibTableColumn
wwpLeosVplsSwitchCtrlType = _WwpLeosVplsSwitchCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 7, 1, 2),
    _WwpLeosVplsSwitchCtrlType_Type()
)
wwpLeosVplsSwitchCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchCtrlType.setStatus("deprecated")
_WwpLeosVplsSwitchReservedVlanTable_Object = MibTable
wwpLeosVplsSwitchReservedVlanTable = _WwpLeosVplsSwitchReservedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanTable.setStatus("current")
_WwpLeosVplsSwitchReservedVlanEntry_Object = MibTableRow
wwpLeosVplsSwitchReservedVlanEntry = _WwpLeosVplsSwitchReservedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8, 1)
)
wwpLeosVplsSwitchReservedVlanEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsSwitchReservedVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanEntry.setStatus("current")


class _WwpLeosVplsSwitchReservedVlanId_Type(Integer32):
    """Custom type wwpLeosVplsSwitchReservedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosVplsSwitchReservedVlanId_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchReservedVlanId_Object = MibTableColumn
wwpLeosVplsSwitchReservedVlanId = _WwpLeosVplsSwitchReservedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8, 1, 1),
    _WwpLeosVplsSwitchReservedVlanId_Type()
)
wwpLeosVplsSwitchReservedVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanId.setStatus("current")
_WwpLeosVplsSwitchReservedVlanStatus_Type = RowStatus
_WwpLeosVplsSwitchReservedVlanStatus_Object = MibTableColumn
wwpLeosVplsSwitchReservedVlanStatus = _WwpLeosVplsSwitchReservedVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 8, 1, 2),
    _WwpLeosVplsSwitchReservedVlanStatus_Type()
)
wwpLeosVplsSwitchReservedVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchReservedVlanStatus.setStatus("current")
_WwpLeosVplsGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosVplsGlobalAttrs = _WwpLeosVplsGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9)
)


class _WwpLeosVplsTunnelFixedTTL_Type(Integer32):
    """Custom type wwpLeosVplsTunnelFixedTTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_WwpLeosVplsTunnelFixedTTL_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelFixedTTL_Object = MibScalar
wwpLeosVplsTunnelFixedTTL = _WwpLeosVplsTunnelFixedTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 1),
    _WwpLeosVplsTunnelFixedTTL_Type()
)
wwpLeosVplsTunnelFixedTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelFixedTTL.setStatus("current")


class _WwpLeosVplsResolverTimeout_Type(Integer32):
    """Custom type wwpLeosVplsResolverTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_WwpLeosVplsResolverTimeout_Type.__name__ = "Integer32"
_WwpLeosVplsResolverTimeout_Object = MibScalar
wwpLeosVplsResolverTimeout = _WwpLeosVplsResolverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 2),
    _WwpLeosVplsResolverTimeout_Type()
)
wwpLeosVplsResolverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsResolverTimeout.setStatus("current")


class _WwpLeosVplsStaticLabelRangeStart_Type(Unsigned32):
    """Custom type wwpLeosVplsStaticLabelRangeStart based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsStaticLabelRangeStart_Type.__name__ = "Unsigned32"
_WwpLeosVplsStaticLabelRangeStart_Object = MibScalar
wwpLeosVplsStaticLabelRangeStart = _WwpLeosVplsStaticLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 3),
    _WwpLeosVplsStaticLabelRangeStart_Type()
)
wwpLeosVplsStaticLabelRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsStaticLabelRangeStart.setStatus("current")


class _WwpLeosVplsStaticLabelRangeEnd_Type(Unsigned32):
    """Custom type wwpLeosVplsStaticLabelRangeEnd based on Unsigned32"""
    defaultValue = 2047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsStaticLabelRangeEnd_Type.__name__ = "Unsigned32"
_WwpLeosVplsStaticLabelRangeEnd_Object = MibScalar
wwpLeosVplsStaticLabelRangeEnd = _WwpLeosVplsStaticLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 4),
    _WwpLeosVplsStaticLabelRangeEnd_Type()
)
wwpLeosVplsStaticLabelRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsStaticLabelRangeEnd.setStatus("current")


class _WwpLeosVplsDynamicLabelRangeStart_Type(Unsigned32):
    """Custom type wwpLeosVplsDynamicLabelRangeStart based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsDynamicLabelRangeStart_Type.__name__ = "Unsigned32"
_WwpLeosVplsDynamicLabelRangeStart_Object = MibScalar
wwpLeosVplsDynamicLabelRangeStart = _WwpLeosVplsDynamicLabelRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 5),
    _WwpLeosVplsDynamicLabelRangeStart_Type()
)
wwpLeosVplsDynamicLabelRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsDynamicLabelRangeStart.setStatus("current")


class _WwpLeosVplsDynamicLabelRangeEnd_Type(Unsigned32):
    """Custom type wwpLeosVplsDynamicLabelRangeEnd based on Unsigned32"""
    defaultValue = 1048575

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_WwpLeosVplsDynamicLabelRangeEnd_Type.__name__ = "Unsigned32"
_WwpLeosVplsDynamicLabelRangeEnd_Object = MibScalar
wwpLeosVplsDynamicLabelRangeEnd = _WwpLeosVplsDynamicLabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 6),
    _WwpLeosVplsDynamicLabelRangeEnd_Type()
)
wwpLeosVplsDynamicLabelRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsDynamicLabelRangeEnd.setStatus("current")


class _WwpLeosVplsVirtualCircuitStatsClear_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosVplsVirtualCircuitStatsClear_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitStatsClear_Object = MibScalar
wwpLeosVplsVirtualCircuitStatsClear = _WwpLeosVplsVirtualCircuitStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 9, 7),
    _WwpLeosVplsVirtualCircuitStatsClear_Type()
)
wwpLeosVplsVirtualCircuitStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitStatsClear.setStatus("current")
_WwpLeosVplsMplsPathTable_Object = MibTable
wwpLeosVplsMplsPathTable = _WwpLeosVplsMplsPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathTable.setStatus("current")
_WwpLeosVplsMplsPathEntry_Object = MibTableRow
wwpLeosVplsMplsPathEntry = _WwpLeosVplsMplsPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1)
)
wwpLeosVplsMplsPathEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsMplsPathIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathEntry.setStatus("current")


class _WwpLeosVplsMplsPathIndex_Type(Integer32):
    """Custom type wwpLeosVplsMplsPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WwpLeosVplsMplsPathIndex_Type.__name__ = "Integer32"
_WwpLeosVplsMplsPathIndex_Object = MibTableColumn
wwpLeosVplsMplsPathIndex = _WwpLeosVplsMplsPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1, 1),
    _WwpLeosVplsMplsPathIndex_Type()
)
wwpLeosVplsMplsPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathIndex.setStatus("current")


class _WwpLeosVplsMplsPathName_Type(DisplayString):
    """Custom type wwpLeosVplsMplsPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsMplsPathName_Type.__name__ = "DisplayString"
_WwpLeosVplsMplsPathName_Object = MibTableColumn
wwpLeosVplsMplsPathName = _WwpLeosVplsMplsPathName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1, 2),
    _WwpLeosVplsMplsPathName_Type()
)
wwpLeosVplsMplsPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathName.setStatus("current")
_WwpLeosVplsMplsPathRowStatus_Type = RowStatus
_WwpLeosVplsMplsPathRowStatus_Object = MibTableColumn
wwpLeosVplsMplsPathRowStatus = _WwpLeosVplsMplsPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 10, 1, 3),
    _WwpLeosVplsMplsPathRowStatus_Type()
)
wwpLeosVplsMplsPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathRowStatus.setStatus("current")
_WwpLeosVplsMplsPathMemberTable_Object = MibTable
wwpLeosVplsMplsPathMemberTable = _WwpLeosVplsMplsPathMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathMemberTable.setStatus("current")
_WwpLeosVplsMplsPathMemberEntry_Object = MibTableRow
wwpLeosVplsMplsPathMemberEntry = _WwpLeosVplsMplsPathMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 11, 1)
)
wwpLeosVplsMplsPathMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsMplsPathIndex"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsMplsPathOptionIndex"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsMplsPathMemberIpIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathMemberEntry.setStatus("current")


class _WwpLeosVplsMplsPathOptionIndex_Type(Integer32):
    """Custom type wwpLeosVplsMplsPathOptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WwpLeosVplsMplsPathOptionIndex_Type.__name__ = "Integer32"
_WwpLeosVplsMplsPathOptionIndex_Object = MibTableColumn
wwpLeosVplsMplsPathOptionIndex = _WwpLeosVplsMplsPathOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 11, 1, 1),
    _WwpLeosVplsMplsPathOptionIndex_Type()
)
wwpLeosVplsMplsPathOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathOptionIndex.setStatus("current")


class _WwpLeosVplsMplsPathMemberIpIndex_Type(Integer32):
    """Custom type wwpLeosVplsMplsPathMemberIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WwpLeosVplsMplsPathMemberIpIndex_Type.__name__ = "Integer32"
_WwpLeosVplsMplsPathMemberIpIndex_Object = MibTableColumn
wwpLeosVplsMplsPathMemberIpIndex = _WwpLeosVplsMplsPathMemberIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 11, 1, 2),
    _WwpLeosVplsMplsPathMemberIpIndex_Type()
)
wwpLeosVplsMplsPathMemberIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathMemberIpIndex.setStatus("current")
_WwpLeosVplsMplsPathMemberIp_Type = IpAddress
_WwpLeosVplsMplsPathMemberIp_Object = MibTableColumn
wwpLeosVplsMplsPathMemberIp = _WwpLeosVplsMplsPathMemberIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 11, 1, 3),
    _WwpLeosVplsMplsPathMemberIp_Type()
)
wwpLeosVplsMplsPathMemberIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathMemberIp.setStatus("current")
_WwpLeosVplsMplsPathMemberRowStatus_Type = RowStatus
_WwpLeosVplsMplsPathMemberRowStatus_Object = MibTableColumn
wwpLeosVplsMplsPathMemberRowStatus = _WwpLeosVplsMplsPathMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 11, 1, 4),
    _WwpLeosVplsMplsPathMemberRowStatus_Type()
)
wwpLeosVplsMplsPathMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsMplsPathMemberRowStatus.setStatus("current")
_WwpLeosVplsRsvpAttrTable_Object = MibTable
wwpLeosVplsRsvpAttrTable = _WwpLeosVplsRsvpAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 12)
)
if mibBuilder.loadTexts:
    wwpLeosVplsRsvpAttrTable.setStatus("current")
_WwpLeosVplsRsvpAttrEntry_Object = MibTableRow
wwpLeosVplsRsvpAttrEntry = _WwpLeosVplsRsvpAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 12, 1)
)
wwpLeosVplsRsvpAttrEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsRsvpAttrIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsRsvpAttrEntry.setStatus("current")


class _WwpLeosVplsRsvpAttrIndex_Type(Integer32):
    """Custom type wwpLeosVplsRsvpAttrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsRsvpAttrIndex_Type.__name__ = "Integer32"
_WwpLeosVplsRsvpAttrIndex_Object = MibTableColumn
wwpLeosVplsRsvpAttrIndex = _WwpLeosVplsRsvpAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 12, 1, 1),
    _WwpLeosVplsRsvpAttrIndex_Type()
)
wwpLeosVplsRsvpAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsRsvpAttrIndex.setStatus("current")


class _WwpLeosVplsRsvpAttrHoldPri_Type(Integer32):
    """Custom type wwpLeosVplsRsvpAttrHoldPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsRsvpAttrHoldPri_Type.__name__ = "Integer32"
_WwpLeosVplsRsvpAttrHoldPri_Object = MibTableColumn
wwpLeosVplsRsvpAttrHoldPri = _WwpLeosVplsRsvpAttrHoldPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 12, 1, 2),
    _WwpLeosVplsRsvpAttrHoldPri_Type()
)
wwpLeosVplsRsvpAttrHoldPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsRsvpAttrHoldPri.setStatus("current")


class _WwpLeosVplsRsvpAttrSetupPri_Type(Integer32):
    """Custom type wwpLeosVplsRsvpAttrSetupPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsRsvpAttrSetupPri_Type.__name__ = "Integer32"
_WwpLeosVplsRsvpAttrSetupPri_Object = MibTableColumn
wwpLeosVplsRsvpAttrSetupPri = _WwpLeosVplsRsvpAttrSetupPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 12, 1, 3),
    _WwpLeosVplsRsvpAttrSetupPri_Type()
)
wwpLeosVplsRsvpAttrSetupPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsRsvpAttrSetupPri.setStatus("current")


class _WwpLeosVplsRsvpAttrRecordRoute_Type(TruthValue):
    """Custom type wwpLeosVplsRsvpAttrRecordRoute based on TruthValue"""


_WwpLeosVplsRsvpAttrRecordRoute_Object = MibTableColumn
wwpLeosVplsRsvpAttrRecordRoute = _WwpLeosVplsRsvpAttrRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 12, 1, 4),
    _WwpLeosVplsRsvpAttrRecordRoute_Type()
)
wwpLeosVplsRsvpAttrRecordRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsRsvpAttrRecordRoute.setStatus("current")
_WwpLeosVplsEncapTunnelTable_Object = MibTable
wwpLeosVplsEncapTunnelTable = _WwpLeosVplsEncapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13)
)
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelTable.setStatus("current")
_WwpLeosVplsEncapTunnelEntry_Object = MibTableRow
wwpLeosVplsEncapTunnelEntry = _WwpLeosVplsEncapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1)
)
wwpLeosVplsEncapTunnelEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelEntry.setStatus("current")


class _WwpLeosVplsEncapTunnelId_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsEncapTunnelId_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelId_Object = MibTableColumn
wwpLeosVplsEncapTunnelId = _WwpLeosVplsEncapTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 1),
    _WwpLeosVplsEncapTunnelId_Type()
)
wwpLeosVplsEncapTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelId.setStatus("current")


class _WwpLeosVplsEncapTunnelName_Type(DisplayString):
    """Custom type wwpLeosVplsEncapTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsEncapTunnelName_Type.__name__ = "DisplayString"
_WwpLeosVplsEncapTunnelName_Object = MibTableColumn
wwpLeosVplsEncapTunnelName = _WwpLeosVplsEncapTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 2),
    _WwpLeosVplsEncapTunnelName_Type()
)
wwpLeosVplsEncapTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelName.setStatus("current")


class _WwpLeosVplsEncapTunnelType_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("staticPbt", 3))
    )


_WwpLeosVplsEncapTunnelType_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelType_Object = MibTableColumn
wwpLeosVplsEncapTunnelType = _WwpLeosVplsEncapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 3),
    _WwpLeosVplsEncapTunnelType_Type()
)
wwpLeosVplsEncapTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelType.setStatus("current")
_WwpLeosVplsEncapTunnelDestAddr_Type = IpAddress
_WwpLeosVplsEncapTunnelDestAddr_Object = MibTableColumn
wwpLeosVplsEncapTunnelDestAddr = _WwpLeosVplsEncapTunnelDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 4),
    _WwpLeosVplsEncapTunnelDestAddr_Type()
)
wwpLeosVplsEncapTunnelDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelDestAddr.setStatus("current")
_WwpLeosVplsEncapTunnelPathIndex_Type = Integer32
_WwpLeosVplsEncapTunnelPathIndex_Object = MibTableColumn
wwpLeosVplsEncapTunnelPathIndex = _WwpLeosVplsEncapTunnelPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 5),
    _WwpLeosVplsEncapTunnelPathIndex_Type()
)
wwpLeosVplsEncapTunnelPathIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelPathIndex.setStatus("current")


class _WwpLeosVplsEncapTunnelEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelEncapCosPolicy based on Integer32"""
    defaultValue = 4

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
        *(("fixed", 1),
          ("inheritVc", 2),
          ("inheritVs", 3),
          ("rcosMapped", 4))
    )


_WwpLeosVplsEncapTunnelEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsEncapTunnelEncapCosPolicy = _WwpLeosVplsEncapTunnelEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 6),
    _WwpLeosVplsEncapTunnelEncapCosPolicy_Type()
)
wwpLeosVplsEncapTunnelEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelEncapCosPolicy.setStatus("current")


class _WwpLeosVplsEncapTunnelEncapFixedExp_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelEncapFixedExp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsEncapTunnelEncapFixedExp_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelEncapFixedExp_Object = MibTableColumn
wwpLeosVplsEncapTunnelEncapFixedExp = _WwpLeosVplsEncapTunnelEncapFixedExp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 7),
    _WwpLeosVplsEncapTunnelEncapFixedExp_Type()
)
wwpLeosVplsEncapTunnelEncapFixedExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelEncapFixedExp.setStatus("current")


class _WwpLeosVplsEncapTunnelTTLPolicy_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelTTLPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 1),
          ("uniform", 2))
    )


_WwpLeosVplsEncapTunnelTTLPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelTTLPolicy_Object = MibTableColumn
wwpLeosVplsEncapTunnelTTLPolicy = _WwpLeosVplsEncapTunnelTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 8),
    _WwpLeosVplsEncapTunnelTTLPolicy_Type()
)
wwpLeosVplsEncapTunnelTTLPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelTTLPolicy.setStatus("current")


class _WwpLeosVplsEncapTunnelEncapLabel_Type(Unsigned32):
    """Custom type wwpLeosVplsEncapTunnelEncapLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_WwpLeosVplsEncapTunnelEncapLabel_Type.__name__ = "Unsigned32"
_WwpLeosVplsEncapTunnelEncapLabel_Object = MibTableColumn
wwpLeosVplsEncapTunnelEncapLabel = _WwpLeosVplsEncapTunnelEncapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 9),
    _WwpLeosVplsEncapTunnelEncapLabel_Type()
)
wwpLeosVplsEncapTunnelEncapLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelEncapLabel.setStatus("current")


class _WwpLeosVplsEncapTunnelProtType_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelProtType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rsvp", 2))
    )


_WwpLeosVplsEncapTunnelProtType_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelProtType_Object = MibTableColumn
wwpLeosVplsEncapTunnelProtType = _WwpLeosVplsEncapTunnelProtType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 10),
    _WwpLeosVplsEncapTunnelProtType_Type()
)
wwpLeosVplsEncapTunnelProtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelProtType.setStatus("current")
_WwpLeosVplsEncapTunnelDestResolvedMac_Type = MacAddress
_WwpLeosVplsEncapTunnelDestResolvedMac_Object = MibTableColumn
wwpLeosVplsEncapTunnelDestResolvedMac = _WwpLeosVplsEncapTunnelDestResolvedMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 11),
    _WwpLeosVplsEncapTunnelDestResolvedMac_Type()
)
wwpLeosVplsEncapTunnelDestResolvedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelDestResolvedMac.setStatus("current")


class _WwpLeosVplsEncapTunnelOperStatus_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsEncapTunnelOperStatus_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelOperStatus_Object = MibTableColumn
wwpLeosVplsEncapTunnelOperStatus = _WwpLeosVplsEncapTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 12),
    _WwpLeosVplsEncapTunnelOperStatus_Type()
)
wwpLeosVplsEncapTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelOperStatus.setStatus("current")


class _WwpLeosVplsEncapTunnelAdminStatus_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsEncapTunnelAdminStatus_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelAdminStatus_Object = MibTableColumn
wwpLeosVplsEncapTunnelAdminStatus = _WwpLeosVplsEncapTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 13),
    _WwpLeosVplsEncapTunnelAdminStatus_Type()
)
wwpLeosVplsEncapTunnelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelAdminStatus.setStatus("current")


class _WwpLeosVplsEncapTunnelDestResolvedPort_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelDestResolvedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsEncapTunnelDestResolvedPort_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelDestResolvedPort_Object = MibTableColumn
wwpLeosVplsEncapTunnelDestResolvedPort = _WwpLeosVplsEncapTunnelDestResolvedPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 14),
    _WwpLeosVplsEncapTunnelDestResolvedPort_Type()
)
wwpLeosVplsEncapTunnelDestResolvedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelDestResolvedPort.setStatus("current")


class _WwpLeosVplsEncapTunnelDestResolvedVlan_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelDestResolvedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosVplsEncapTunnelDestResolvedVlan_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelDestResolvedVlan_Object = MibTableColumn
wwpLeosVplsEncapTunnelDestResolvedVlan = _WwpLeosVplsEncapTunnelDestResolvedVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 15),
    _WwpLeosVplsEncapTunnelDestResolvedVlan_Type()
)
wwpLeosVplsEncapTunnelDestResolvedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelDestResolvedVlan.setStatus("current")
_WwpLeosVplsEncapTunnelRowStatus_Type = RowStatus
_WwpLeosVplsEncapTunnelRowStatus_Object = MibTableColumn
wwpLeosVplsEncapTunnelRowStatus = _WwpLeosVplsEncapTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 16),
    _WwpLeosVplsEncapTunnelRowStatus_Type()
)
wwpLeosVplsEncapTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelRowStatus.setStatus("current")


class _WwpLeosVplsEncapTunnelFastReroute_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelFastReroute based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkProtect", 1),
          ("nodeProtect", 2))
    )


_WwpLeosVplsEncapTunnelFastReroute_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelFastReroute_Object = MibTableColumn
wwpLeosVplsEncapTunnelFastReroute = _WwpLeosVplsEncapTunnelFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 17),
    _WwpLeosVplsEncapTunnelFastReroute_Type()
)
wwpLeosVplsEncapTunnelFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelFastReroute.setStatus("current")


class _WwpLeosVplsEncapTunnelLspType_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelLspType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_WwpLeosVplsEncapTunnelLspType_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelLspType_Object = MibTableColumn
wwpLeosVplsEncapTunnelLspType = _WwpLeosVplsEncapTunnelLspType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 18),
    _WwpLeosVplsEncapTunnelLspType_Type()
)
wwpLeosVplsEncapTunnelLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelLspType.setStatus("current")


class _WwpLeosVplsEncapTunnelPartnerTunnelId_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelPartnerTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsEncapTunnelPartnerTunnelId_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelPartnerTunnelId_Object = MibTableColumn
wwpLeosVplsEncapTunnelPartnerTunnelId = _WwpLeosVplsEncapTunnelPartnerTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 19),
    _WwpLeosVplsEncapTunnelPartnerTunnelId_Type()
)
wwpLeosVplsEncapTunnelPartnerTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelPartnerTunnelId.setStatus("current")
_WwpLeosVplsEncapTunnelBVID_Type = VlanId
_WwpLeosVplsEncapTunnelBVID_Object = MibTableColumn
wwpLeosVplsEncapTunnelBVID = _WwpLeosVplsEncapTunnelBVID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 20),
    _WwpLeosVplsEncapTunnelBVID_Type()
)
wwpLeosVplsEncapTunnelBVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelBVID.setStatus("current")


class _WwpLeosVplsEncapTunnelDestBridgeIndex_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelDestBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosVplsEncapTunnelDestBridgeIndex_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelDestBridgeIndex_Object = MibTableColumn
wwpLeosVplsEncapTunnelDestBridgeIndex = _WwpLeosVplsEncapTunnelDestBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 21),
    _WwpLeosVplsEncapTunnelDestBridgeIndex_Type()
)
wwpLeosVplsEncapTunnelDestBridgeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelDestBridgeIndex.setStatus("current")
_WwpLeosVplsEncapTunnelEgressPort_Type = Integer32
_WwpLeosVplsEncapTunnelEgressPort_Object = MibTableColumn
wwpLeosVplsEncapTunnelEgressPort = _WwpLeosVplsEncapTunnelEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 22),
    _WwpLeosVplsEncapTunnelEgressPort_Type()
)
wwpLeosVplsEncapTunnelEgressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelEgressPort.setStatus("current")


class _WwpLeosVplsEncapTunnelEncapFixedPCP_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelEncapFixedPCP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsEncapTunnelEncapFixedPCP_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelEncapFixedPCP_Object = MibTableColumn
wwpLeosVplsEncapTunnelEncapFixedPCP = _WwpLeosVplsEncapTunnelEncapFixedPCP_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 23),
    _WwpLeosVplsEncapTunnelEncapFixedPCP_Type()
)
wwpLeosVplsEncapTunnelEncapFixedPCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelEncapFixedPCP.setStatus("current")


class _WwpLeosVplsEncapTunnelActive_Type(Integer32):
    """Custom type wwpLeosVplsEncapTunnelActive based on Integer32"""
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


_WwpLeosVplsEncapTunnelActive_Type.__name__ = "Integer32"
_WwpLeosVplsEncapTunnelActive_Object = MibTableColumn
wwpLeosVplsEncapTunnelActive = _WwpLeosVplsEncapTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 13, 1, 24),
    _WwpLeosVplsEncapTunnelActive_Type()
)
wwpLeosVplsEncapTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsEncapTunnelActive.setStatus("current")
_WwpLeosVplsDecapTunnelTable_Object = MibTable
wwpLeosVplsDecapTunnelTable = _WwpLeosVplsDecapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14)
)
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelTable.setStatus("current")
_WwpLeosVplsDecapTunnelEntry_Object = MibTableRow
wwpLeosVplsDecapTunnelEntry = _WwpLeosVplsDecapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1)
)
wwpLeosVplsDecapTunnelEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsDecapTunnelId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelEntry.setStatus("current")


class _WwpLeosVplsDecapTunnelId_Type(Integer32):
    """Custom type wwpLeosVplsDecapTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsDecapTunnelId_Type.__name__ = "Integer32"
_WwpLeosVplsDecapTunnelId_Object = MibTableColumn
wwpLeosVplsDecapTunnelId = _WwpLeosVplsDecapTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 1),
    _WwpLeosVplsDecapTunnelId_Type()
)
wwpLeosVplsDecapTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelId.setStatus("current")


class _WwpLeosVplsDecapTunnelName_Type(DisplayString):
    """Custom type wwpLeosVplsDecapTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsDecapTunnelName_Type.__name__ = "DisplayString"
_WwpLeosVplsDecapTunnelName_Object = MibTableColumn
wwpLeosVplsDecapTunnelName = _WwpLeosVplsDecapTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 2),
    _WwpLeosVplsDecapTunnelName_Type()
)
wwpLeosVplsDecapTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelName.setStatus("current")


class _WwpLeosVplsDecapTunnelLabel_Type(Unsigned32):
    """Custom type wwpLeosVplsDecapTunnelLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_WwpLeosVplsDecapTunnelLabel_Type.__name__ = "Unsigned32"
_WwpLeosVplsDecapTunnelLabel_Object = MibTableColumn
wwpLeosVplsDecapTunnelLabel = _WwpLeosVplsDecapTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 3),
    _WwpLeosVplsDecapTunnelLabel_Type()
)
wwpLeosVplsDecapTunnelLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelLabel.setStatus("current")


class _WwpLeosVplsDecapTunnelType_Type(Integer32):
    """Custom type wwpLeosVplsDecapTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("staticPbt", 3))
    )


_WwpLeosVplsDecapTunnelType_Type.__name__ = "Integer32"
_WwpLeosVplsDecapTunnelType_Object = MibTableColumn
wwpLeosVplsDecapTunnelType = _WwpLeosVplsDecapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 4),
    _WwpLeosVplsDecapTunnelType_Type()
)
wwpLeosVplsDecapTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelType.setStatus("current")
_WwpLeosVplsDecapTunnelRowStatus_Type = RowStatus
_WwpLeosVplsDecapTunnelRowStatus_Object = MibTableColumn
wwpLeosVplsDecapTunnelRowStatus = _WwpLeosVplsDecapTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 5),
    _WwpLeosVplsDecapTunnelRowStatus_Type()
)
wwpLeosVplsDecapTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelRowStatus.setStatus("current")
_WwpLeosVplsDecapTunnelBVID_Type = Integer32
_WwpLeosVplsDecapTunnelBVID_Object = MibTableColumn
wwpLeosVplsDecapTunnelBVID = _WwpLeosVplsDecapTunnelBVID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 6),
    _WwpLeosVplsDecapTunnelBVID_Type()
)
wwpLeosVplsDecapTunnelBVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelBVID.setStatus("current")


class _WwpLeosVplsDecapTunnelBridgeIndex_Type(Integer32):
    """Custom type wwpLeosVplsDecapTunnelBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosVplsDecapTunnelBridgeIndex_Type.__name__ = "Integer32"
_WwpLeosVplsDecapTunnelBridgeIndex_Object = MibTableColumn
wwpLeosVplsDecapTunnelBridgeIndex = _WwpLeosVplsDecapTunnelBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 7),
    _WwpLeosVplsDecapTunnelBridgeIndex_Type()
)
wwpLeosVplsDecapTunnelBridgeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelBridgeIndex.setStatus("current")
_WwpLeosVplsDecapTunnelPort_Type = Integer32
_WwpLeosVplsDecapTunnelPort_Object = MibTableColumn
wwpLeosVplsDecapTunnelPort = _WwpLeosVplsDecapTunnelPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 8),
    _WwpLeosVplsDecapTunnelPort_Type()
)
wwpLeosVplsDecapTunnelPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelPort.setStatus("current")
_WwpLeosVplsDecapTunnelMac_Type = MacAddress
_WwpLeosVplsDecapTunnelMac_Object = MibTableColumn
wwpLeosVplsDecapTunnelMac = _WwpLeosVplsDecapTunnelMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 9),
    _WwpLeosVplsDecapTunnelMac_Type()
)
wwpLeosVplsDecapTunnelMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelMac.setStatus("current")


class _WwpLeosVplsDecapTunnelOperStatus_Type(Integer32):
    """Custom type wwpLeosVplsDecapTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsDecapTunnelOperStatus_Type.__name__ = "Integer32"
_WwpLeosVplsDecapTunnelOperStatus_Object = MibTableColumn
wwpLeosVplsDecapTunnelOperStatus = _WwpLeosVplsDecapTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 14, 1, 10),
    _WwpLeosVplsDecapTunnelOperStatus_Type()
)
wwpLeosVplsDecapTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsDecapTunnelOperStatus.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTable_Object = MibTable
wwpLeosVplsVirtualCircuitMplsTable = _WwpLeosVplsVirtualCircuitMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTable.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitMplsEntry = _WwpLeosVplsVirtualCircuitMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1)
)
wwpLeosVplsVirtualCircuitMplsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitMplsIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsEntry.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsIndex_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitMplsIndex_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsIndex_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsIndex = _WwpLeosVplsVirtualCircuitMplsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 1),
    _WwpLeosVplsVirtualCircuitMplsIndex_Type()
)
wwpLeosVplsVirtualCircuitMplsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsIndex.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualCircuitMplsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsVirtualCircuitMplsName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualCircuitMplsName_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsName = _WwpLeosVplsVirtualCircuitMplsName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 2),
    _WwpLeosVplsVirtualCircuitMplsName_Type()
)
wwpLeosVplsVirtualCircuitMplsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsName.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_WwpLeosVplsVirtualCircuitMplsType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsType_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsType = _WwpLeosVplsVirtualCircuitMplsType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 3),
    _WwpLeosVplsVirtualCircuitMplsType_Type()
)
wwpLeosVplsVirtualCircuitMplsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsType.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsDestAddr_Type = IpAddress
_WwpLeosVplsVirtualCircuitMplsDestAddr_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsDestAddr = _WwpLeosVplsVirtualCircuitMplsDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 4),
    _WwpLeosVplsVirtualCircuitMplsDestAddr_Type()
)
wwpLeosVplsVirtualCircuitMplsDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsDestAddr.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsTunnelPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstAvailable", 2),
          ("fixed", 1))
    )


_WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTunnelPolicy = _WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 5),
    _WwpLeosVplsVirtualCircuitMplsTunnelPolicy_Type()
)
wwpLeosVplsVirtualCircuitMplsTunnelPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTunnelPolicy.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsFixedTunnelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsFixedTunnelId = _WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 6),
    _WwpLeosVplsVirtualCircuitMplsFixedTunnelId_Type()
)
wwpLeosVplsVirtualCircuitMplsFixedTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsFixedTunnelId.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsActiveTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsActiveTunnelId = _WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 7),
    _WwpLeosVplsVirtualCircuitMplsActiveTunnelId_Type()
)
wwpLeosVplsVirtualCircuitMplsActiveTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsActiveTunnelId.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsOperStatus_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualCircuitMplsOperStatus_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsOperStatus_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsOperStatus = _WwpLeosVplsVirtualCircuitMplsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 8),
    _WwpLeosVplsVirtualCircuitMplsOperStatus_Type()
)
wwpLeosVplsVirtualCircuitMplsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsOperStatus.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsEncapLabel_Type(Unsigned32):
    """Custom type wwpLeosVplsVirtualCircuitMplsEncapLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_WwpLeosVplsVirtualCircuitMplsEncapLabel_Type.__name__ = "Unsigned32"
_WwpLeosVplsVirtualCircuitMplsEncapLabel_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsEncapLabel = _WwpLeosVplsVirtualCircuitMplsEncapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 9),
    _WwpLeosVplsVirtualCircuitMplsEncapLabel_Type()
)
wwpLeosVplsVirtualCircuitMplsEncapLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsEncapLabel.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsDecapLabel_Type(Unsigned32):
    """Custom type wwpLeosVplsVirtualCircuitMplsDecapLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_WwpLeosVplsVirtualCircuitMplsDecapLabel_Type.__name__ = "Unsigned32"
_WwpLeosVplsVirtualCircuitMplsDecapLabel_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsDecapLabel = _WwpLeosVplsVirtualCircuitMplsDecapLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 10),
    _WwpLeosVplsVirtualCircuitMplsDecapLabel_Type()
)
wwpLeosVplsVirtualCircuitMplsDecapLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsDecapLabel.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsGroupId_Type(Unsigned32):
    """Custom type wwpLeosVplsVirtualCircuitMplsGroupId based on Unsigned32"""
    defaultValue = 0


_WwpLeosVplsVirtualCircuitMplsGroupId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsGroupId = _WwpLeosVplsVirtualCircuitMplsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 11),
    _WwpLeosVplsVirtualCircuitMplsGroupId_Type()
)
wwpLeosVplsVirtualCircuitMplsGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsGroupId.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsProtectionType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsProtectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WwpLeosVplsVirtualCircuitMplsProtectionType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsProtectionType_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsProtectionType = _WwpLeosVplsVirtualCircuitMplsProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 12),
    _WwpLeosVplsVirtualCircuitMplsProtectionType_Type()
)
wwpLeosVplsVirtualCircuitMplsProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsProtectionType.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsStatusTlv_Type(TruthValue):
    """Custom type wwpLeosVplsVirtualCircuitMplsStatusTlv based on TruthValue"""


_WwpLeosVplsVirtualCircuitMplsStatusTlv_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsStatusTlv = _WwpLeosVplsVirtualCircuitMplsStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 13),
    _WwpLeosVplsVirtualCircuitMplsStatusTlv_Type()
)
wwpLeosVplsVirtualCircuitMplsStatusTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsStatusTlv.setStatus("current")


class _WwpLeosVplsVirtualCircuitMplsMtu_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitMplsMtu based on Integer32"""
    defaultValue = 9190

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 9216),
    )


_WwpLeosVplsVirtualCircuitMplsMtu_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitMplsMtu_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsMtu = _WwpLeosVplsVirtualCircuitMplsMtu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 14),
    _WwpLeosVplsVirtualCircuitMplsMtu_Type()
)
wwpLeosVplsVirtualCircuitMplsMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsMtu.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsStatus_Type = RowStatus
_WwpLeosVplsVirtualCircuitMplsStatus_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsStatus = _WwpLeosVplsVirtualCircuitMplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 15, 1, 15),
    _WwpLeosVplsVirtualCircuitMplsStatus_Type()
)
wwpLeosVplsVirtualCircuitMplsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsStatus.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsStatsTable_Object = MibTable
wwpLeosVplsVirtualCircuitMplsStatsTable = _WwpLeosVplsVirtualCircuitMplsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 16)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsStatsTable.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitMplsStatsEntry = _WwpLeosVplsVirtualCircuitMplsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 16, 1)
)
wwpLeosVplsVirtualCircuitMplsStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitMplsIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsStatsEntry.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsTxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTxBytesHi = _WwpLeosVplsVirtualCircuitMplsTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 16, 1, 1),
    _WwpLeosVplsVirtualCircuitMplsTxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitMplsTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsTxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTxBytesLo = _WwpLeosVplsVirtualCircuitMplsTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 16, 1, 2),
    _WwpLeosVplsVirtualCircuitMplsTxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitMplsTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsRxBytesHi = _WwpLeosVplsVirtualCircuitMplsRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 16, 1, 3),
    _WwpLeosVplsVirtualCircuitMplsRxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitMplsRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsRxBytesLo = _WwpLeosVplsVirtualCircuitMplsRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 16, 1, 4),
    _WwpLeosVplsVirtualCircuitMplsRxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitMplsRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTable_Object = MibTable
wwpLeosVplsVirtualCircuitEthTable = _WwpLeosVplsVirtualCircuitEthTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTable.setStatus("current")
_WwpLeosVplsVirtualCircuitEthEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEthEntry = _WwpLeosVplsVirtualCircuitEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17, 1)
)
wwpLeosVplsVirtualCircuitEthEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitEthIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthEntry.setStatus("current")


class _WwpLeosVplsVirtualCircuitEthIndex_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitEthIndex_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEthIndex_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthIndex = _WwpLeosVplsVirtualCircuitEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17, 1, 1),
    _WwpLeosVplsVirtualCircuitEthIndex_Type()
)
wwpLeosVplsVirtualCircuitEthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthIndex.setStatus("current")


class _WwpLeosVplsVirtualCircuitEthName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualCircuitEthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsVirtualCircuitEthName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualCircuitEthName_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthName = _WwpLeosVplsVirtualCircuitEthName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17, 1, 2),
    _WwpLeosVplsVirtualCircuitEthName_Type()
)
wwpLeosVplsVirtualCircuitEthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthName.setStatus("current")
_WwpLeosVplsVirtualCircuitEthProviderVlanId_Type = VlanId
_WwpLeosVplsVirtualCircuitEthProviderVlanId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthProviderVlanId = _WwpLeosVplsVirtualCircuitEthProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17, 1, 3),
    _WwpLeosVplsVirtualCircuitEthProviderVlanId_Type()
)
wwpLeosVplsVirtualCircuitEthProviderVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthProviderVlanId.setStatus("current")
_WwpLeosVplsVirtualCircuitEthRowStatus_Type = RowStatus
_WwpLeosVplsVirtualCircuitEthRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthRowStatus = _WwpLeosVplsVirtualCircuitEthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17, 1, 4),
    _WwpLeosVplsVirtualCircuitEthRowStatus_Type()
)
wwpLeosVplsVirtualCircuitEthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthRowStatus.setStatus("current")


class _WwpLeosVplsVirtualCircuitEthStatsMonitor_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEthStatsMonitor based on Integer32"""
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


_WwpLeosVplsVirtualCircuitEthStatsMonitor_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEthStatsMonitor_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthStatsMonitor = _WwpLeosVplsVirtualCircuitEthStatsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 17, 1, 5),
    _WwpLeosVplsVirtualCircuitEthStatsMonitor_Type()
)
wwpLeosVplsVirtualCircuitEthStatsMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthStatsMonitor.setStatus("current")
_WwpLeosVplsVirtualCircuitEtherTypeTable_Object = MibTable
wwpLeosVplsVirtualCircuitEtherTypeTable = _WwpLeosVplsVirtualCircuitEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 18)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherTypeTable.setStatus("current")
_WwpLeosVplsVirtualCircuitEtherTypeEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEtherTypeEntry = _WwpLeosVplsVirtualCircuitEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 18, 1)
)
wwpLeosVplsVirtualCircuitEtherTypeEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherTypeEntry.setStatus("current")


class _WwpLeosVplsVirtualCircuitPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualCircuitPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitPortId_Object = MibTableColumn
wwpLeosVplsVirtualCircuitPortId = _WwpLeosVplsVirtualCircuitPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 18, 1, 1),
    _WwpLeosVplsVirtualCircuitPortId_Type()
)
wwpLeosVplsVirtualCircuitPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitPortId.setStatus("current")


class _WwpLeosVplsVirtualCircuitEtherType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEtherType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type8100", 1),
          ("type88A8", 3),
          ("type9100", 2))
    )


_WwpLeosVplsVirtualCircuitEtherType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEtherType_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEtherType = _WwpLeosVplsVirtualCircuitEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 18, 1, 2),
    _WwpLeosVplsVirtualCircuitEtherType_Type()
)
wwpLeosVplsVirtualCircuitEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherType.setStatus("current")


class _WwpLeosVplsVirtualCircuitEtherTypePolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualCircuitEtherTypePolicy based on Integer32"""
    defaultValue = 2

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
          ("encapOnly", 2),
          ("vlanTpid", 3))
    )


_WwpLeosVplsVirtualCircuitEtherTypePolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualCircuitEtherTypePolicy_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEtherTypePolicy = _WwpLeosVplsVirtualCircuitEtherTypePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 18, 1, 3),
    _WwpLeosVplsVirtualCircuitEtherTypePolicy_Type()
)
wwpLeosVplsVirtualCircuitEtherTypePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEtherTypePolicy.setStatus("current")
_WwpLeosVplsVirtualCircuitEthStatsTable_Object = MibTable
wwpLeosVplsVirtualCircuitEthStatsTable = _WwpLeosVplsVirtualCircuitEthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthStatsTable.setStatus("current")
_WwpLeosVplsVirtualCircuitEthStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEthStatsEntry = _WwpLeosVplsVirtualCircuitEthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19, 1)
)
wwpLeosVplsVirtualCircuitEthStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitEthIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthStatsEntry.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitEthTxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthTxBytesHi = _WwpLeosVplsVirtualCircuitEthTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19, 1, 1),
    _WwpLeosVplsVirtualCircuitEthTxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitEthTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitEthTxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthTxBytesLo = _WwpLeosVplsVirtualCircuitEthTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19, 1, 2),
    _WwpLeosVplsVirtualCircuitEthTxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitEthTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitEthRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitEthRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthRxBytesHi = _WwpLeosVplsVirtualCircuitEthRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19, 1, 3),
    _WwpLeosVplsVirtualCircuitEthRxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitEthRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitEthRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitEthRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthRxBytesLo = _WwpLeosVplsVirtualCircuitEthRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19, 1, 4),
    _WwpLeosVplsVirtualCircuitEthRxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitEthRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthRxBytesLo.setStatus("current")


class _WwpLeosVirtualCircuitEthStatsClear_Type(Integer32):
    """Custom type wwpLeosVirtualCircuitEthStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosVirtualCircuitEthStatsClear_Type.__name__ = "Integer32"
_WwpLeosVirtualCircuitEthStatsClear_Object = MibTableColumn
wwpLeosVirtualCircuitEthStatsClear = _WwpLeosVirtualCircuitEthStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 19, 1, 5),
    _WwpLeosVirtualCircuitEthStatsClear_Type()
)
wwpLeosVirtualCircuitEthStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVirtualCircuitEthStatsClear.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsTable = _WwpLeosVplsVirtualSwitchMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsEntry = _WwpLeosVplsVirtualSwitchMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1)
)
wwpLeosVplsVirtualSwitchMplsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMplsIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsIndx_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsIndx = _WwpLeosVplsVirtualSwitchMplsIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsIndx_Type()
)
wwpLeosVplsVirtualSwitchMplsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsIndx.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualSwitchMplsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsVirtualSwitchMplsName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualSwitchMplsName_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsName = _WwpLeosVplsVirtualSwitchMplsName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsName_Type()
)
wwpLeosVplsVirtualSwitchMplsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsName.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsVpnId_Type = Unsigned32
_WwpLeosVplsVirtualSwitchMplsVpnId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsVpnId = _WwpLeosVplsVirtualSwitchMplsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 3),
    _WwpLeosVplsVirtualSwitchMplsVpnId_Type()
)
wwpLeosVplsVirtualSwitchMplsVpnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsVpnId.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEncapCosPolicy based on Integer32"""
    defaultValue = 1

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
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4))
    )


_WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEncapCosPolicy = _WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 4),
    _WwpLeosVplsVirtualSwitchMplsEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri = _WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 5),
    _WwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsDecapCosPolicy based on Integer32"""
    defaultValue = 4

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
        *(("fixed", 1),
          ("inheritTunnel", 3),
          ("inheritVc", 2),
          ("leave", 4))
    )


_WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsDecapCosPolicy = _WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 6),
    _WwpLeosVplsVirtualSwitchMplsDecapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsDecapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsDecapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri = _WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 7),
    _WwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState = _WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 8),
    _WwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState_Type()
)
wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pipe", 1),
          ("uniform", 2))
    )


_WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy = _WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 9),
    _WwpLeosVplsVirtualSwitchMplsDecapTTLPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsType based on Integer32"""
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


_WwpLeosVplsVirtualSwitchMplsType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsType_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsType = _WwpLeosVplsVirtualSwitchMplsType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 10),
    _WwpLeosVplsVirtualSwitchMplsType_Type()
)
wwpLeosVplsVirtualSwitchMplsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsType.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMplsRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsRowStatus = _WwpLeosVplsVirtualSwitchMplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 11),
    _WwpLeosVplsVirtualSwitchMplsRowStatus_Type()
)
wwpLeosVplsVirtualSwitchMplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsRowStatus.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMacLrnState_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMacLrnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchMplsMacLrnState_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMacLrnState_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMacLrnState = _WwpLeosVplsVirtualSwitchMplsMacLrnState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 12),
    _WwpLeosVplsVirtualSwitchMplsMacLrnState_Type()
)
wwpLeosVplsVirtualSwitchMplsMacLrnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMacLrnState.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsTunnelMethod_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsTunnelMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2pt", 1),
          ("transparent", 2))
    )


_WwpLeosVplsVirtualSwitchMplsTunnelMethod_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsTunnelMethod_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsTunnelMethod = _WwpLeosVplsVirtualSwitchMplsTunnelMethod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 13),
    _WwpLeosVplsVirtualSwitchMplsTunnelMethod_Type()
)
wwpLeosVplsVirtualSwitchMplsTunnelMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsTunnelMethod.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri = _WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 14),
    _WwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leave", 1),
          ("provider-inherit", 2))
    )


_WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy = _WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 15),
    _WwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate = _WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 16),
    _WwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate_Type()
)
wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsHonorPriority_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsHonorPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c-vlan", 1),
          ("s-vlan", 2))
    )


_WwpLeosVplsVirtualSwitchMplsHonorPriority_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsHonorPriority_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsHonorPriority = _WwpLeosVplsVirtualSwitchMplsHonorPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 20, 1, 17),
    _WwpLeosVplsVirtualSwitchMplsHonorPriority_Type()
)
wwpLeosVplsVirtualSwitchMplsHonorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsHonorPriority.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsMemberTable = _WwpLeosVplsVirtualSwitchMplsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberTable.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchMplsMemberEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberEntry = _WwpLeosVplsVirtualSwitchMplsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1)
)
wwpLeosVplsVirtualSwitchMplsMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberEntry.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchMplsMemberPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMplsMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberPortId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberPortId = _WwpLeosVplsVirtualSwitchMplsMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsMemberPortId_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberPortId.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMemberVlanId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosVplsVirtualSwitchMplsMemberVlanId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberVlanId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberVlanId = _WwpLeosVplsVirtualSwitchMplsMemberVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsMemberVlanId_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberVlanId.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberRowStatus = _WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1, 3),
    _WwpLeosVplsVirtualSwitchMplsMemberRowStatus_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberRowStatus.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4),
          ("inheritVs", 5),
          ("port-inherit", 6))
    )


_WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy = _WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1, 4),
    _WwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri = _WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1, 5),
    _WwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inheritVs", 3),
          ("leave", 1),
          ("provider-inherit", 2))
    )


_WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy = _WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 21, 1, 6),
    _WwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsMemberStatsTable = _WwpLeosVplsVirtualSwitchMplsMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 22)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberStatsTable.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchMplsMemberStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberStatsEntry = _WwpLeosVplsVirtualSwitchMplsMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 22, 1)
)
wwpLeosVplsVirtualSwitchMplsMemberStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberStatsEntry.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi = _WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 22, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsMemberRxBytesHi_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo = _WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 22, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsMemberRxBytesLo_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable = _WwpLeosVplsVirtualSwitchMplsMemberMeshVcTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 23)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry = _WwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 23, 1)
)
wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc = _WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 23, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus = _WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 23, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberAcVcTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsMemberAcVcTable = _WwpLeosVplsVirtualSwitchMplsMemberAcVcTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 24)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberAcVcTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberAcVcEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry = _WwpLeosVplsVirtualSwitchMplsMemberAcVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 24, 1)
)
wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc = _WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 24, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus = _WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 24, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus_Type()
)
wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus.setStatus("current")
_WwpLeosVplsSwitchMplsCtrlProtocolTable_Object = MibTable
wwpLeosVplsSwitchMplsCtrlProtocolTable = _WwpLeosVplsSwitchMplsCtrlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 25)
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchMplsCtrlProtocolTable.setStatus("current")
_WwpLeosVplsSwitchMplsCtrlProtocolEntry_Object = MibTableRow
wwpLeosVplsSwitchMplsCtrlProtocolEntry = _WwpLeosVplsSwitchMplsCtrlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 25, 1)
)
wwpLeosVplsSwitchMplsCtrlProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsSwitchMplsCtrlProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchMplsCtrlProtocolEntry.setStatus("current")


class _WwpLeosVplsSwitchMplsCtrlProtocolNum_Type(Integer32):
    """Custom type wwpLeosVplsSwitchMplsCtrlProtocolNum based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUdlp", 8),
          ("ciscoUplinkFast", 7),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("l28021x", 1),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("lldp", 14),
          ("oam", 13),
          ("rstp", 2),
          ("vlanBridge", 15))
    )


_WwpLeosVplsSwitchMplsCtrlProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchMplsCtrlProtocolNum_Object = MibTableColumn
wwpLeosVplsSwitchMplsCtrlProtocolNum = _WwpLeosVplsSwitchMplsCtrlProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 25, 1, 1),
    _WwpLeosVplsSwitchMplsCtrlProtocolNum_Type()
)
wwpLeosVplsSwitchMplsCtrlProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchMplsCtrlProtocolNum.setStatus("current")


class _WwpLeosVplsSwitchMplsCtrlType_Type(Integer32):
    """Custom type wwpLeosVplsSwitchMplsCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )


_WwpLeosVplsSwitchMplsCtrlType_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchMplsCtrlType_Object = MibTableColumn
wwpLeosVplsSwitchMplsCtrlType = _WwpLeosVplsSwitchMplsCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 25, 1, 2),
    _WwpLeosVplsSwitchMplsCtrlType_Type()
)
wwpLeosVplsSwitchMplsCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchMplsCtrlType.setStatus("current")
_WwpLeosVplsVirtualSwitchEthTable_Object = MibTable
wwpLeosVplsVirtualSwitchEthTable = _WwpLeosVplsVirtualSwitchEthTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthTable.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEthEntry = _WwpLeosVplsVirtualSwitchEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1)
)
wwpLeosVplsVirtualSwitchEthEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchEthIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthIndx_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthIndx = _WwpLeosVplsVirtualSwitchEthIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 1),
    _WwpLeosVplsVirtualSwitchEthIndx_Type()
)
wwpLeosVplsVirtualSwitchEthIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthIndx.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthName_Type(DisplayString):
    """Custom type wwpLeosVplsVirtualSwitchEthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsVirtualSwitchEthName_Type.__name__ = "DisplayString"
_WwpLeosVplsVirtualSwitchEthName_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthName = _WwpLeosVplsVirtualSwitchEthName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 2),
    _WwpLeosVplsVirtualSwitchEthName_Type()
)
wwpLeosVplsVirtualSwitchEthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthName.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthVc_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosVplsVirtualSwitchEthVc_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthVc_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthVc = _WwpLeosVplsVirtualSwitchEthVc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 3),
    _WwpLeosVplsVirtualSwitchEthVc_Type()
)
wwpLeosVplsVirtualSwitchEthVc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthVc.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEncapCosPolicy based on Integer32"""
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
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4),
          ("port-inherit", 5))
    )


_WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEncapCosPolicy = _WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 4),
    _WwpLeosVplsVirtualSwitchEthEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri = _WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 5),
    _WwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthDecapCosPolicy based on Integer32"""
    defaultValue = 4

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
        *(("fixed", 1),
          ("inheritTunnel", 3),
          ("inheritVc", 2),
          ("leave", 4))
    )


_WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthDecapCosPolicy = _WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 6),
    _WwpLeosVplsVirtualSwitchEthDecapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthDecapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthDecapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri = _WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 7),
    _WwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState = _WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 8),
    _WwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState_Type()
)
wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState.setStatus("current")
_WwpLeosVplsVirtualSwitchEthRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchEthRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthRowStatus = _WwpLeosVplsVirtualSwitchEthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 9),
    _WwpLeosVplsVirtualSwitchEthRowStatus_Type()
)
wwpLeosVplsVirtualSwitchEthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthRowStatus.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthMacLrnState_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthMacLrnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchEthMacLrnState_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthMacLrnState_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMacLrnState = _WwpLeosVplsVirtualSwitchEthMacLrnState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 10),
    _WwpLeosVplsVirtualSwitchEthMacLrnState_Type()
)
wwpLeosVplsVirtualSwitchEthMacLrnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMacLrnState.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthTunnelMethod_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthTunnelMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2pt", 1),
          ("transparent", 2))
    )


_WwpLeosVplsVirtualSwitchEthTunnelMethod_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthTunnelMethod_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthTunnelMethod = _WwpLeosVplsVirtualSwitchEthTunnelMethod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 11),
    _WwpLeosVplsVirtualSwitchEthTunnelMethod_Type()
)
wwpLeosVplsVirtualSwitchEthTunnelMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthTunnelMethod.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri = _WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 12),
    _WwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leave", 1),
          ("provider-inherit", 2))
    )


_WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy = _WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 13),
    _WwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate = _WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 14),
    _WwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate_Type()
)
wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthVcType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthVcType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("none", 1),
          ("pbt", 3))
    )


_WwpLeosVplsVirtualSwitchEthVcType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthVcType_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthVcType = _WwpLeosVplsVirtualSwitchEthVcType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 15),
    _WwpLeosVplsVirtualSwitchEthVcType_Type()
)
wwpLeosVplsVirtualSwitchEthVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthVcType.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthHonorPriority_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthHonorPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c-vlan", 1),
          ("s-vlan", 2))
    )


_WwpLeosVplsVirtualSwitchEthHonorPriority_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthHonorPriority_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthHonorPriority = _WwpLeosVplsVirtualSwitchEthHonorPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 16),
    _WwpLeosVplsVirtualSwitchEthHonorPriority_Type()
)
wwpLeosVplsVirtualSwitchEthHonorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthHonorPriority.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthDescription_Type(OctetString):
    """Custom type wwpLeosVplsVirtualSwitchEthDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosVplsVirtualSwitchEthDescription_Type.__name__ = "OctetString"
_WwpLeosVplsVirtualSwitchEthDescription_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthDescription = _WwpLeosVplsVirtualSwitchEthDescription_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 17),
    _WwpLeosVplsVirtualSwitchEthDescription_Type()
)
wwpLeosVplsVirtualSwitchEthDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthDescription.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthReservedVlan_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthReservedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosVplsVirtualSwitchEthReservedVlan_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthReservedVlan_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthReservedVlan = _WwpLeosVplsVirtualSwitchEthReservedVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 26, 1, 18),
    _WwpLeosVplsVirtualSwitchEthReservedVlan_Type()
)
wwpLeosVplsVirtualSwitchEthReservedVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthReservedVlan.setStatus("current")
_WwpLeosVplsVirtualSwitchEthMemberTable_Object = MibTable
wwpLeosVplsVirtualSwitchEthMemberTable = _WwpLeosVplsVirtualSwitchEthMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberTable.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchEthMemberEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEthMemberEntry = _WwpLeosVplsVirtualSwitchEthMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1)
)
wwpLeosVplsVirtualSwitchEthMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberEntry.setStatus("deprecated")


class _WwpLeosVplsVirtualSwitchEthMemberPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchEthMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthMemberPortId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberPortId = _WwpLeosVplsVirtualSwitchEthMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1, 1),
    _WwpLeosVplsVirtualSwitchEthMemberPortId_Type()
)
wwpLeosVplsVirtualSwitchEthMemberPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberPortId.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthMemberVlan_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthMemberVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosVplsVirtualSwitchEthMemberVlan_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthMemberVlan_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberVlan = _WwpLeosVplsVirtualSwitchEthMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1, 2),
    _WwpLeosVplsVirtualSwitchEthMemberVlan_Type()
)
wwpLeosVplsVirtualSwitchEthMemberVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberVlan.setStatus("current")
_WwpLeosVplsVirtualSwitchEthMemberRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchEthMemberRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberRowStatus = _WwpLeosVplsVirtualSwitchEthMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1, 3),
    _WwpLeosVplsVirtualSwitchEthMemberRowStatus_Type()
)
wwpLeosVplsVirtualSwitchEthMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberRowStatus.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4),
          ("inheritVs", 5),
          ("port-inherit", 6))
    )


_WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy = _WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1, 4),
    _WwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri = _WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1, 5),
    _WwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri_Type()
)
wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inheritVs", 3),
          ("leave", 1),
          ("provider-inherit", 2))
    )


_WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy = _WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 27, 1, 6),
    _WwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy.setStatus("current")
_WwpLeosVplsVirtualSwitchEthMemberStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchEthMemberStatsTable = _WwpLeosVplsVirtualSwitchEthMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 28)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberStatsTable.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchEthMemberStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEthMemberStatsEntry = _WwpLeosVplsVirtualSwitchEthMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 28, 1)
)
wwpLeosVplsVirtualSwitchEthMemberStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthMemberPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberStatsEntry.setStatus("deprecated")
_WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberRxBytesHi = _WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 28, 1, 1),
    _WwpLeosVplsVirtualSwitchEthMemberRxBytesHi_Type()
)
wwpLeosVplsVirtualSwitchEthMemberRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthMemberRxBytesLo = _WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 28, 1, 2),
    _WwpLeosVplsVirtualSwitchEthMemberRxBytesLo_Type()
)
wwpLeosVplsVirtualSwitchEthMemberRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthMemberRxBytesLo.setStatus("current")
_WwpLeosVplsSwitchEthCtrlProtocolTable_Object = MibTable
wwpLeosVplsSwitchEthCtrlProtocolTable = _WwpLeosVplsSwitchEthCtrlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 29)
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchEthCtrlProtocolTable.setStatus("current")
_WwpLeosVplsSwitchEthCtrlProtocolEntry_Object = MibTableRow
wwpLeosVplsSwitchEthCtrlProtocolEntry = _WwpLeosVplsSwitchEthCtrlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 29, 1)
)
wwpLeosVplsSwitchEthCtrlProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsSwitchEthCtrlProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchEthCtrlProtocolEntry.setStatus("current")


class _WwpLeosVplsSwitchEthCtrlProtocolNum_Type(Integer32):
    """Custom type wwpLeosVplsSwitchEthCtrlProtocolNum based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUdlp", 8),
          ("ciscoUplinkFast", 7),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("l28021x", 1),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("lldp", 14),
          ("oam", 13),
          ("rstp", 2),
          ("vlanBridge", 15))
    )


_WwpLeosVplsSwitchEthCtrlProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchEthCtrlProtocolNum_Object = MibTableColumn
wwpLeosVplsSwitchEthCtrlProtocolNum = _WwpLeosVplsSwitchEthCtrlProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 29, 1, 1),
    _WwpLeosVplsSwitchEthCtrlProtocolNum_Type()
)
wwpLeosVplsSwitchEthCtrlProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchEthCtrlProtocolNum.setStatus("current")


class _WwpLeosVplsSwitchEthCtrlType_Type(Integer32):
    """Custom type wwpLeosVplsSwitchEthCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )


_WwpLeosVplsSwitchEthCtrlType_Type.__name__ = "Integer32"
_WwpLeosVplsSwitchEthCtrlType_Object = MibTableColumn
wwpLeosVplsSwitchEthCtrlType = _WwpLeosVplsSwitchEthCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 29, 1, 2),
    _WwpLeosVplsSwitchEthCtrlType_Type()
)
wwpLeosVplsSwitchEthCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsSwitchEthCtrlType.setStatus("current")
_WwpLeosVplsVirtualSwitchEtypeTranslationTable_Object = MibTable
wwpLeosVplsVirtualSwitchEtypeTranslationTable = _WwpLeosVplsVirtualSwitchEtypeTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 30)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEtypeTranslationTable.setStatus("current")
_WwpLeosVplsVirtualSwitchEtypeTranslationEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEtypeTranslationEntry = _WwpLeosVplsVirtualSwitchEtypeTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 30, 1)
)
wwpLeosVplsVirtualSwitchEtypeTranslationEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEtypeTranslationEntry.setStatus("current")
_WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Type = EtherType
_WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype = _WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 30, 1, 1),
    _WwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype_Type()
)
wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype.setStatus("current")
_WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Type = EtherType
_WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype = _WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 30, 1, 2),
    _WwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype_Type()
)
wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype.setStatus("current")
_WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus = _WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 30, 1, 3),
    _WwpLeosVplsVirtualSwitchEtypeTranslationRowStatus_Type()
)
wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus.setStatus("current")
_WwpLeosVplsTunnelPairTable_Object = MibTable
wwpLeosVplsTunnelPairTable = _WwpLeosVplsTunnelPairTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31)
)
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairTable.setStatus("current")
_WwpLeosVplsTunnelPairEntry_Object = MibTableRow
wwpLeosVplsTunnelPairEntry = _WwpLeosVplsTunnelPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31, 1)
)
wwpLeosVplsTunnelPairEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsTunnelPairIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairEntry.setStatus("current")


class _WwpLeosVplsTunnelPairIndx_Type(Integer32):
    """Custom type wwpLeosVplsTunnelPairIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsTunnelPairIndx_Type.__name__ = "Integer32"
_WwpLeosVplsTunnelPairIndx_Object = MibTableColumn
wwpLeosVplsTunnelPairIndx = _WwpLeosVplsTunnelPairIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31, 1, 1),
    _WwpLeosVplsTunnelPairIndx_Type()
)
wwpLeosVplsTunnelPairIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairIndx.setStatus("current")


class _WwpLeosVplsTunnelPairName_Type(DisplayString):
    """Custom type wwpLeosVplsTunnelPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosVplsTunnelPairName_Type.__name__ = "DisplayString"
_WwpLeosVplsTunnelPairName_Object = MibTableColumn
wwpLeosVplsTunnelPairName = _WwpLeosVplsTunnelPairName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31, 1, 2),
    _WwpLeosVplsTunnelPairName_Type()
)
wwpLeosVplsTunnelPairName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairName.setStatus("current")
_WwpLeosVplsTunnelPairEncapTunnelIndx_Type = Integer32
_WwpLeosVplsTunnelPairEncapTunnelIndx_Object = MibTableColumn
wwpLeosVplsTunnelPairEncapTunnelIndx = _WwpLeosVplsTunnelPairEncapTunnelIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31, 1, 3),
    _WwpLeosVplsTunnelPairEncapTunnelIndx_Type()
)
wwpLeosVplsTunnelPairEncapTunnelIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairEncapTunnelIndx.setStatus("current")
_WwpLeosVplsTunnelPairDecapTunnelIndx_Type = Integer32
_WwpLeosVplsTunnelPairDecapTunnelIndx_Object = MibTableColumn
wwpLeosVplsTunnelPairDecapTunnelIndx = _WwpLeosVplsTunnelPairDecapTunnelIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31, 1, 4),
    _WwpLeosVplsTunnelPairDecapTunnelIndx_Type()
)
wwpLeosVplsTunnelPairDecapTunnelIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairDecapTunnelIndx.setStatus("current")
_WwpLeosVplsTunnelPairRowStatus_Type = RowStatus
_WwpLeosVplsTunnelPairRowStatus_Object = MibTableColumn
wwpLeosVplsTunnelPairRowStatus = _WwpLeosVplsTunnelPairRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 31, 1, 5),
    _WwpLeosVplsTunnelPairRowStatus_Type()
)
wwpLeosVplsTunnelPairRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsTunnelPairRowStatus.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsEvplMemberTable = _WwpLeosVplsVirtualSwitchMplsEvplMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsEvplMemberEntry = _WwpLeosVplsVirtualSwitchMplsEvplMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1)
)
wwpLeosVplsVirtualSwitchMplsEvplMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsEvplMemberPortId"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEvplMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberPortId = _WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberPortId_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberPortId.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId = _WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberVlanId_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus = _WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1, 3),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4),
          ("inheritVs", 5),
          ("port-inherit", 6))
    )


_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy = _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1, 4),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri = _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1, 5),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inheritVs", 3),
          ("leave", 1),
          ("provider-inherit", 2))
    )


_WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy = _WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 32, 1, 6),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable = _WwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 33)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry = _WwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 33, 1)
)
wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsEvplMemberPortId"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi = _WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 33, 1, 1),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo = _WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 33, 1, 2),
    _WwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo_Type()
)
wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberTable_Object = MibTable
wwpLeosVplsVirtualSwitchEthEvplMemberTable = _WwpLeosVplsVirtualSwitchEthEvplMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberTable.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEthEvplMemberEntry = _WwpLeosVplsVirtualSwitchEthEvplMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1)
)
wwpLeosVplsVirtualSwitchEthEvplMemberEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthEvplMemberPortId"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthEvplMemberVlan"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberPortId = _WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 1),
    _WwpLeosVplsVirtualSwitchEthEvplMemberPortId_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberPortId.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberVlan = _WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 2),
    _WwpLeosVplsVirtualSwitchEthEvplMemberVlan_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberVlan.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus = _WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 3),
    _WwpLeosVplsVirtualSwitchEthEvplMemberRowStatus_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("inheritDot1dPri", 2),
          ("inheritIpPrec", 3),
          ("inheritPhbg", 4),
          ("inheritVs", 5),
          ("port-inherit", 6))
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy = _WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 4),
    _WwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri = _WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 5),
    _WwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inheritVs", 3),
          ("leave", 1),
          ("provider-inherit", 2))
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy = _WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 6),
    _WwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag = _WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 7),
    _WwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("none", 99),
          ("tpid8100", 1),
          ("tpid88A8", 3),
          ("tpid9100", 2))
    )


_WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid = _WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 34, 1, 8),
    _WwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable = _WwpLeosVplsVirtualSwitchEthEvplMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 35)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry = _WwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 35, 1)
)
wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthEvplMemberPortId"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthEvplMemberVlan"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi = _WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 35, 1, 1),
    _WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo = _WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 35, 1, 2),
    _WwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo_Type()
)
wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTotalStatsTable_Object = MibTable
wwpLeosVplsVirtualCircuitEthTotalStatsTable = _WwpLeosVplsVirtualCircuitEthTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 36)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTotalStatsTable.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTotalStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitEthTotalStatsEntry = _WwpLeosVplsVirtualCircuitEthTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 36, 1)
)
wwpLeosVplsVirtualCircuitEthTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitEthIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTotalStatsEntry.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalTxBytesHi = _WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 36, 1, 1),
    _WwpLeosVplsVirtualCircuitEthTotalTxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitEthTotalTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTotalTxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalTxBytesLo = _WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 36, 1, 2),
    _WwpLeosVplsVirtualCircuitEthTotalTxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitEthTotalTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTotalTxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalRxBytesHi = _WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 36, 1, 3),
    _WwpLeosVplsVirtualCircuitEthTotalRxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitEthTotalRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTotalRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitEthTotalRxBytesLo = _WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 36, 1, 4),
    _WwpLeosVplsVirtualCircuitEthTotalRxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitEthTotalRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitEthTotalRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTotalStatsTable_Object = MibTable
wwpLeosVplsVirtualCircuitMplsTotalStatsTable = _WwpLeosVplsVirtualCircuitMplsTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 37)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTotalStatsTable.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTotalStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualCircuitMplsTotalStatsEntry = _WwpLeosVplsVirtualCircuitMplsTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 37, 1)
)
wwpLeosVplsVirtualCircuitMplsTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualCircuitMplsIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTotalStatsEntry.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi = _WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 37, 1, 1),
    _WwpLeosVplsVirtualCircuitMplsTotalTxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo = _WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 37, 1, 2),
    _WwpLeosVplsVirtualCircuitMplsTotalTxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi = _WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 37, 1, 3),
    _WwpLeosVplsVirtualCircuitMplsTotalRxBytesHi_Type()
)
wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi.setStatus("current")
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Type = Counter32
_WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Object = MibTableColumn
wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo = _WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 37, 1, 4),
    _WwpLeosVplsVirtualCircuitMplsTotalRxBytesLo_Type()
)
wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo.setStatus("current")
_WwpLeosVplsVirtualSwitchEthL2CftProtocolTable_Object = MibTable
wwpLeosVplsVirtualSwitchEthL2CftProtocolTable = _WwpLeosVplsVirtualSwitchEthL2CftProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 49)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthL2CftProtocolTable.setStatus("current")
_WwpLeosVplsVirtualSwitchEthL2CftProtocolEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry = _WwpLeosVplsVirtualSwitchEthL2CftProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 49, 1)
)
wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchEthL2CftProtocolType"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthL2CftProtocolType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              32,
              33,
              34,
              99)
        )
    )
    namedValues = NamedValues(
        *(("allBridgesBlock", 33),
          ("brigeBlock", 32),
          ("ciscoCdp", 1),
          ("ciscoDtp", 2),
          ("ciscoPagp", 3),
          ("ciscoPvst", 6),
          ("ciscoStpUplinkFast", 7),
          ("ciscoUdld", 4),
          ("ciscoVtp", 5),
          ("garpBlock", 34),
          ("gmrp", 15),
          ("gvrp", 16),
          ("i8021x", 14),
          ("lacp", 10),
          ("lacpMarker", 11),
          ("lldp", 13),
          ("oam", 12),
          ("rstp", 9),
          ("unknown", 99),
          ("vlanBridge", 8))
    )


_WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthL2CftProtocolType = _WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 49, 1, 1),
    _WwpLeosVplsVirtualSwitchEthL2CftProtocolType_Type()
)
wwpLeosVplsVirtualSwitchEthL2CftProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthL2CftProtocolType.setStatus("current")


class _WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition = _WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 49, 1, 2),
    _WwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition_Type()
)
wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition.setStatus("current")
_WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Type = RowStatus
_WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Object = MibTableColumn
wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus = _WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 49, 1, 64),
    _WwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus_Type()
)
wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchCFTProtoStatsTable = _WwpLeosVplsVirtualSwitchCFTProtoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoStatsTable.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchCFTProtoStatsEntry = _WwpLeosVplsVirtualSwitchCFTProtoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1)
)
wwpLeosVplsVirtualSwitchCFTProtoStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoStatsEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx = _WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 1),
    _WwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2RxPkts = _WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 2),
    _WwpLeosVplsVirtualSwitchCFTProtol2RxPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2RxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2RxPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts = _WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 3),
    _WwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts = _WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 4),
    _WwpLeosVplsVirtualSwitchCFTProtol2PeerPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts = _WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 5),
    _WwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts = _WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 6),
    _WwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures = _WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 7),
    _WwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts = _WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 8),
    _WwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts.setStatus("current")


class _WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUdlp", 8),
          ("ciscoUplinkFast", 7),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("l28021x", 1),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("lldp", 13),
          ("oam", 14),
          ("rstp", 2),
          ("vlanBridge", 15))
    )


_WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum = _WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 50, 1, 9),
    _WwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum_Type()
)
wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable_Object = MibTable
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable = _WwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51)
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry_Object = MibTableRow
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry = _WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1)
)
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx"),
    (0, "WWP-LEOS-VPLS-MIB", "wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum"),
)
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry.setStatus("current")


class _WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx = _WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 1),
    _WwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts = _WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 2),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts = _WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 3),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts = _WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 4),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts = _WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 5),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts = _WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 6),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures = _WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 7),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures.setStatus("current")
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Type = Counter32
_WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts = _WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 8),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts.setStatus("current")


class _WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Type(Integer32):
    """Custom type wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCdp", 3),
          ("ciscoDtp", 4),
          ("ciscoPagp", 5),
          ("ciscoPvst", 6),
          ("ciscoUdlp", 8),
          ("ciscoUplinkFast", 7),
          ("ciscoVtp", 9),
          ("gvrp", 10),
          ("l28021x", 1),
          ("lacp", 11),
          ("lacpMarker", 12),
          ("lldp", 13),
          ("oam", 14),
          ("rstp", 2),
          ("vlanBridge", 15))
    )


_WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Type.__name__ = "Integer32"
_WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Object = MibTableColumn
wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum = _WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 1, 1, 51, 1, 9),
    _WwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum_Type()
)
wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum.setStatus("current")
_WwpLeosVplsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBNotificationPrefix = _WwpLeosVplsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 2)
)
_WwpLeosVplsMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBNotifications = _WwpLeosVplsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 2, 0)
)
_WwpLeosVplsMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBConformance = _WwpLeosVplsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 3)
)
_WwpLeosVplsMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBCompliances = _WwpLeosVplsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 3, 1)
)
_WwpLeosVplsMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosVplsMIBGroups = _WwpLeosVplsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 28, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-VPLS-MIB",
    **{"VlanId": VlanId,
       "EtherType": EtherType,
       "wwpLeosVplsMIB": wwpLeosVplsMIB,
       "wwpLeosVplsMIBObjects": wwpLeosVplsMIBObjects,
       "wwpLeosVpls": wwpLeosVpls,
       "wwpLeosVplsVirtualCircuitTable": wwpLeosVplsVirtualCircuitTable,
       "wwpLeosVplsVirtualCircuitEntry": wwpLeosVplsVirtualCircuitEntry,
       "wwpLeosVplsVirtualCircuitIndex": wwpLeosVplsVirtualCircuitIndex,
       "wwpLeosVplsVirtualCircuitProviderVlanId": wwpLeosVplsVirtualCircuitProviderVlanId,
       "wwpLeosVplsVirtualCircuitType": wwpLeosVplsVirtualCircuitType,
       "wwpLeosVplsVirtualCircuitName": wwpLeosVplsVirtualCircuitName,
       "wwpLeosVplsVirtualCircuitIngressVcLabel": wwpLeosVplsVirtualCircuitIngressVcLabel,
       "wwpLeosVplsVirtualCircuitEgressVcLabel": wwpLeosVplsVirtualCircuitEgressVcLabel,
       "wwpLeosVplsVirtualCircuitTunnelIndx": wwpLeosVplsVirtualCircuitTunnelIndx,
       "wwpLeosVplsVirtualCircuitStatus": wwpLeosVplsVirtualCircuitStatus,
       "wwpLeosVplsVirtualSwitchTable": wwpLeosVplsVirtualSwitchTable,
       "wwpLeosVplsVirtualSwitchEntry": wwpLeosVplsVirtualSwitchEntry,
       "wwpLeosVplsVirtualSwitchIndx": wwpLeosVplsVirtualSwitchIndx,
       "wwpLeosVplsVirtualSwitchName": wwpLeosVplsVirtualSwitchName,
       "wwpLeosVplsVirtualSwitchPriVc": wwpLeosVplsVirtualSwitchPriVc,
       "wwpLeosVplsVirtualSwitchSecVc": wwpLeosVplsVirtualSwitchSecVc,
       "wwpLeosVplsVirtualSwitchActiveVc": wwpLeosVplsVirtualSwitchActiveVc,
       "wwpLeosVplsVirtualSwitchEncapCosPolicy": wwpLeosVplsVirtualSwitchEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchEncapFixedDot1dPri": wwpLeosVplsVirtualSwitchEncapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchDecapCosPolicy": wwpLeosVplsVirtualSwitchDecapCosPolicy,
       "wwpLeosVplsVirtualSwitchDecapFixedDot1dPri": wwpLeosVplsVirtualSwitchDecapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchSubscriberVlan": wwpLeosVplsVirtualSwitchSubscriberVlan,
       "wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState": wwpLeosVplsVirtualSwitchCtrlProtocolTunnelState,
       "wwpLeosVplsVirtualSwitchType": wwpLeosVplsVirtualSwitchType,
       "wwpLeosVplsVirtualSwitchStatus": wwpLeosVplsVirtualSwitchStatus,
       "wwpLeosVplsVirtualSwitchMemberTable": wwpLeosVplsVirtualSwitchMemberTable,
       "wwpLeosVplsVirtualSwitchMemberEntry": wwpLeosVplsVirtualSwitchMemberEntry,
       "wwpLeosVplsVirtualSwitchMemberPortId": wwpLeosVplsVirtualSwitchMemberPortId,
       "wwpLeosVplsVirtualSwitchMemberStatus": wwpLeosVplsVirtualSwitchMemberStatus,
       "wwpLeosVplsSwitchCtrlProtocolTable": wwpLeosVplsSwitchCtrlProtocolTable,
       "wwpLeosVplsSwitchCtrlProtocolEntry": wwpLeosVplsSwitchCtrlProtocolEntry,
       "wwpLeosVplsSwitchCtrlProtocolNum": wwpLeosVplsSwitchCtrlProtocolNum,
       "wwpLeosVplsSwitchCtrlType": wwpLeosVplsSwitchCtrlType,
       "wwpLeosVplsSwitchReservedVlanTable": wwpLeosVplsSwitchReservedVlanTable,
       "wwpLeosVplsSwitchReservedVlanEntry": wwpLeosVplsSwitchReservedVlanEntry,
       "wwpLeosVplsSwitchReservedVlanId": wwpLeosVplsSwitchReservedVlanId,
       "wwpLeosVplsSwitchReservedVlanStatus": wwpLeosVplsSwitchReservedVlanStatus,
       "wwpLeosVplsGlobalAttrs": wwpLeosVplsGlobalAttrs,
       "wwpLeosVplsTunnelFixedTTL": wwpLeosVplsTunnelFixedTTL,
       "wwpLeosVplsResolverTimeout": wwpLeosVplsResolverTimeout,
       "wwpLeosVplsStaticLabelRangeStart": wwpLeosVplsStaticLabelRangeStart,
       "wwpLeosVplsStaticLabelRangeEnd": wwpLeosVplsStaticLabelRangeEnd,
       "wwpLeosVplsDynamicLabelRangeStart": wwpLeosVplsDynamicLabelRangeStart,
       "wwpLeosVplsDynamicLabelRangeEnd": wwpLeosVplsDynamicLabelRangeEnd,
       "wwpLeosVplsVirtualCircuitStatsClear": wwpLeosVplsVirtualCircuitStatsClear,
       "wwpLeosVplsMplsPathTable": wwpLeosVplsMplsPathTable,
       "wwpLeosVplsMplsPathEntry": wwpLeosVplsMplsPathEntry,
       "wwpLeosVplsMplsPathIndex": wwpLeosVplsMplsPathIndex,
       "wwpLeosVplsMplsPathName": wwpLeosVplsMplsPathName,
       "wwpLeosVplsMplsPathRowStatus": wwpLeosVplsMplsPathRowStatus,
       "wwpLeosVplsMplsPathMemberTable": wwpLeosVplsMplsPathMemberTable,
       "wwpLeosVplsMplsPathMemberEntry": wwpLeosVplsMplsPathMemberEntry,
       "wwpLeosVplsMplsPathOptionIndex": wwpLeosVplsMplsPathOptionIndex,
       "wwpLeosVplsMplsPathMemberIpIndex": wwpLeosVplsMplsPathMemberIpIndex,
       "wwpLeosVplsMplsPathMemberIp": wwpLeosVplsMplsPathMemberIp,
       "wwpLeosVplsMplsPathMemberRowStatus": wwpLeosVplsMplsPathMemberRowStatus,
       "wwpLeosVplsRsvpAttrTable": wwpLeosVplsRsvpAttrTable,
       "wwpLeosVplsRsvpAttrEntry": wwpLeosVplsRsvpAttrEntry,
       "wwpLeosVplsRsvpAttrIndex": wwpLeosVplsRsvpAttrIndex,
       "wwpLeosVplsRsvpAttrHoldPri": wwpLeosVplsRsvpAttrHoldPri,
       "wwpLeosVplsRsvpAttrSetupPri": wwpLeosVplsRsvpAttrSetupPri,
       "wwpLeosVplsRsvpAttrRecordRoute": wwpLeosVplsRsvpAttrRecordRoute,
       "wwpLeosVplsEncapTunnelTable": wwpLeosVplsEncapTunnelTable,
       "wwpLeosVplsEncapTunnelEntry": wwpLeosVplsEncapTunnelEntry,
       "wwpLeosVplsEncapTunnelId": wwpLeosVplsEncapTunnelId,
       "wwpLeosVplsEncapTunnelName": wwpLeosVplsEncapTunnelName,
       "wwpLeosVplsEncapTunnelType": wwpLeosVplsEncapTunnelType,
       "wwpLeosVplsEncapTunnelDestAddr": wwpLeosVplsEncapTunnelDestAddr,
       "wwpLeosVplsEncapTunnelPathIndex": wwpLeosVplsEncapTunnelPathIndex,
       "wwpLeosVplsEncapTunnelEncapCosPolicy": wwpLeosVplsEncapTunnelEncapCosPolicy,
       "wwpLeosVplsEncapTunnelEncapFixedExp": wwpLeosVplsEncapTunnelEncapFixedExp,
       "wwpLeosVplsEncapTunnelTTLPolicy": wwpLeosVplsEncapTunnelTTLPolicy,
       "wwpLeosVplsEncapTunnelEncapLabel": wwpLeosVplsEncapTunnelEncapLabel,
       "wwpLeosVplsEncapTunnelProtType": wwpLeosVplsEncapTunnelProtType,
       "wwpLeosVplsEncapTunnelDestResolvedMac": wwpLeosVplsEncapTunnelDestResolvedMac,
       "wwpLeosVplsEncapTunnelOperStatus": wwpLeosVplsEncapTunnelOperStatus,
       "wwpLeosVplsEncapTunnelAdminStatus": wwpLeosVplsEncapTunnelAdminStatus,
       "wwpLeosVplsEncapTunnelDestResolvedPort": wwpLeosVplsEncapTunnelDestResolvedPort,
       "wwpLeosVplsEncapTunnelDestResolvedVlan": wwpLeosVplsEncapTunnelDestResolvedVlan,
       "wwpLeosVplsEncapTunnelRowStatus": wwpLeosVplsEncapTunnelRowStatus,
       "wwpLeosVplsEncapTunnelFastReroute": wwpLeosVplsEncapTunnelFastReroute,
       "wwpLeosVplsEncapTunnelLspType": wwpLeosVplsEncapTunnelLspType,
       "wwpLeosVplsEncapTunnelPartnerTunnelId": wwpLeosVplsEncapTunnelPartnerTunnelId,
       "wwpLeosVplsEncapTunnelBVID": wwpLeosVplsEncapTunnelBVID,
       "wwpLeosVplsEncapTunnelDestBridgeIndex": wwpLeosVplsEncapTunnelDestBridgeIndex,
       "wwpLeosVplsEncapTunnelEgressPort": wwpLeosVplsEncapTunnelEgressPort,
       "wwpLeosVplsEncapTunnelEncapFixedPCP": wwpLeosVplsEncapTunnelEncapFixedPCP,
       "wwpLeosVplsEncapTunnelActive": wwpLeosVplsEncapTunnelActive,
       "wwpLeosVplsDecapTunnelTable": wwpLeosVplsDecapTunnelTable,
       "wwpLeosVplsDecapTunnelEntry": wwpLeosVplsDecapTunnelEntry,
       "wwpLeosVplsDecapTunnelId": wwpLeosVplsDecapTunnelId,
       "wwpLeosVplsDecapTunnelName": wwpLeosVplsDecapTunnelName,
       "wwpLeosVplsDecapTunnelLabel": wwpLeosVplsDecapTunnelLabel,
       "wwpLeosVplsDecapTunnelType": wwpLeosVplsDecapTunnelType,
       "wwpLeosVplsDecapTunnelRowStatus": wwpLeosVplsDecapTunnelRowStatus,
       "wwpLeosVplsDecapTunnelBVID": wwpLeosVplsDecapTunnelBVID,
       "wwpLeosVplsDecapTunnelBridgeIndex": wwpLeosVplsDecapTunnelBridgeIndex,
       "wwpLeosVplsDecapTunnelPort": wwpLeosVplsDecapTunnelPort,
       "wwpLeosVplsDecapTunnelMac": wwpLeosVplsDecapTunnelMac,
       "wwpLeosVplsDecapTunnelOperStatus": wwpLeosVplsDecapTunnelOperStatus,
       "wwpLeosVplsVirtualCircuitMplsTable": wwpLeosVplsVirtualCircuitMplsTable,
       "wwpLeosVplsVirtualCircuitMplsEntry": wwpLeosVplsVirtualCircuitMplsEntry,
       "wwpLeosVplsVirtualCircuitMplsIndex": wwpLeosVplsVirtualCircuitMplsIndex,
       "wwpLeosVplsVirtualCircuitMplsName": wwpLeosVplsVirtualCircuitMplsName,
       "wwpLeosVplsVirtualCircuitMplsType": wwpLeosVplsVirtualCircuitMplsType,
       "wwpLeosVplsVirtualCircuitMplsDestAddr": wwpLeosVplsVirtualCircuitMplsDestAddr,
       "wwpLeosVplsVirtualCircuitMplsTunnelPolicy": wwpLeosVplsVirtualCircuitMplsTunnelPolicy,
       "wwpLeosVplsVirtualCircuitMplsFixedTunnelId": wwpLeosVplsVirtualCircuitMplsFixedTunnelId,
       "wwpLeosVplsVirtualCircuitMplsActiveTunnelId": wwpLeosVplsVirtualCircuitMplsActiveTunnelId,
       "wwpLeosVplsVirtualCircuitMplsOperStatus": wwpLeosVplsVirtualCircuitMplsOperStatus,
       "wwpLeosVplsVirtualCircuitMplsEncapLabel": wwpLeosVplsVirtualCircuitMplsEncapLabel,
       "wwpLeosVplsVirtualCircuitMplsDecapLabel": wwpLeosVplsVirtualCircuitMplsDecapLabel,
       "wwpLeosVplsVirtualCircuitMplsGroupId": wwpLeosVplsVirtualCircuitMplsGroupId,
       "wwpLeosVplsVirtualCircuitMplsProtectionType": wwpLeosVplsVirtualCircuitMplsProtectionType,
       "wwpLeosVplsVirtualCircuitMplsStatusTlv": wwpLeosVplsVirtualCircuitMplsStatusTlv,
       "wwpLeosVplsVirtualCircuitMplsMtu": wwpLeosVplsVirtualCircuitMplsMtu,
       "wwpLeosVplsVirtualCircuitMplsStatus": wwpLeosVplsVirtualCircuitMplsStatus,
       "wwpLeosVplsVirtualCircuitMplsStatsTable": wwpLeosVplsVirtualCircuitMplsStatsTable,
       "wwpLeosVplsVirtualCircuitMplsStatsEntry": wwpLeosVplsVirtualCircuitMplsStatsEntry,
       "wwpLeosVplsVirtualCircuitMplsTxBytesHi": wwpLeosVplsVirtualCircuitMplsTxBytesHi,
       "wwpLeosVplsVirtualCircuitMplsTxBytesLo": wwpLeosVplsVirtualCircuitMplsTxBytesLo,
       "wwpLeosVplsVirtualCircuitMplsRxBytesHi": wwpLeosVplsVirtualCircuitMplsRxBytesHi,
       "wwpLeosVplsVirtualCircuitMplsRxBytesLo": wwpLeosVplsVirtualCircuitMplsRxBytesLo,
       "wwpLeosVplsVirtualCircuitEthTable": wwpLeosVplsVirtualCircuitEthTable,
       "wwpLeosVplsVirtualCircuitEthEntry": wwpLeosVplsVirtualCircuitEthEntry,
       "wwpLeosVplsVirtualCircuitEthIndex": wwpLeosVplsVirtualCircuitEthIndex,
       "wwpLeosVplsVirtualCircuitEthName": wwpLeosVplsVirtualCircuitEthName,
       "wwpLeosVplsVirtualCircuitEthProviderVlanId": wwpLeosVplsVirtualCircuitEthProviderVlanId,
       "wwpLeosVplsVirtualCircuitEthRowStatus": wwpLeosVplsVirtualCircuitEthRowStatus,
       "wwpLeosVplsVirtualCircuitEthStatsMonitor": wwpLeosVplsVirtualCircuitEthStatsMonitor,
       "wwpLeosVplsVirtualCircuitEtherTypeTable": wwpLeosVplsVirtualCircuitEtherTypeTable,
       "wwpLeosVplsVirtualCircuitEtherTypeEntry": wwpLeosVplsVirtualCircuitEtherTypeEntry,
       "wwpLeosVplsVirtualCircuitPortId": wwpLeosVplsVirtualCircuitPortId,
       "wwpLeosVplsVirtualCircuitEtherType": wwpLeosVplsVirtualCircuitEtherType,
       "wwpLeosVplsVirtualCircuitEtherTypePolicy": wwpLeosVplsVirtualCircuitEtherTypePolicy,
       "wwpLeosVplsVirtualCircuitEthStatsTable": wwpLeosVplsVirtualCircuitEthStatsTable,
       "wwpLeosVplsVirtualCircuitEthStatsEntry": wwpLeosVplsVirtualCircuitEthStatsEntry,
       "wwpLeosVplsVirtualCircuitEthTxBytesHi": wwpLeosVplsVirtualCircuitEthTxBytesHi,
       "wwpLeosVplsVirtualCircuitEthTxBytesLo": wwpLeosVplsVirtualCircuitEthTxBytesLo,
       "wwpLeosVplsVirtualCircuitEthRxBytesHi": wwpLeosVplsVirtualCircuitEthRxBytesHi,
       "wwpLeosVplsVirtualCircuitEthRxBytesLo": wwpLeosVplsVirtualCircuitEthRxBytesLo,
       "wwpLeosVirtualCircuitEthStatsClear": wwpLeosVirtualCircuitEthStatsClear,
       "wwpLeosVplsVirtualSwitchMplsTable": wwpLeosVplsVirtualSwitchMplsTable,
       "wwpLeosVplsVirtualSwitchMplsEntry": wwpLeosVplsVirtualSwitchMplsEntry,
       "wwpLeosVplsVirtualSwitchMplsIndx": wwpLeosVplsVirtualSwitchMplsIndx,
       "wwpLeosVplsVirtualSwitchMplsName": wwpLeosVplsVirtualSwitchMplsName,
       "wwpLeosVplsVirtualSwitchMplsVpnId": wwpLeosVplsVirtualSwitchMplsVpnId,
       "wwpLeosVplsVirtualSwitchMplsEncapCosPolicy": wwpLeosVplsVirtualSwitchMplsEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri": wwpLeosVplsVirtualSwitchMplsEncapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchMplsDecapCosPolicy": wwpLeosVplsVirtualSwitchMplsDecapCosPolicy,
       "wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri": wwpLeosVplsVirtualSwitchMplsDecapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState": wwpLeosVplsVirtualSwitchMplsCtrlProtocolTunnelState,
       "wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy": wwpLeosVplsVirtualSwitchMplsDecapTTLPolicy,
       "wwpLeosVplsVirtualSwitchMplsType": wwpLeosVplsVirtualSwitchMplsType,
       "wwpLeosVplsVirtualSwitchMplsRowStatus": wwpLeosVplsVirtualSwitchMplsRowStatus,
       "wwpLeosVplsVirtualSwitchMplsMacLrnState": wwpLeosVplsVirtualSwitchMplsMacLrnState,
       "wwpLeosVplsVirtualSwitchMplsTunnelMethod": wwpLeosVplsVirtualSwitchMplsTunnelMethod,
       "wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri": wwpLeosVplsVirtualSwitchMplsCtrlProtocolDot1dPri,
       "wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy": wwpLeosVplsVirtualSwitchMplsSubscriberDot1dPolicy,
       "wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate": wwpLeosVplsVirtualSwitchMplsCtrlProtTransFrameValidate,
       "wwpLeosVplsVirtualSwitchMplsHonorPriority": wwpLeosVplsVirtualSwitchMplsHonorPriority,
       "wwpLeosVplsVirtualSwitchMplsMemberTable": wwpLeosVplsVirtualSwitchMplsMemberTable,
       "wwpLeosVplsVirtualSwitchMplsMemberEntry": wwpLeosVplsVirtualSwitchMplsMemberEntry,
       "wwpLeosVplsVirtualSwitchMplsMemberPortId": wwpLeosVplsVirtualSwitchMplsMemberPortId,
       "wwpLeosVplsVirtualSwitchMplsMemberVlanId": wwpLeosVplsVirtualSwitchMplsMemberVlanId,
       "wwpLeosVplsVirtualSwitchMplsMemberRowStatus": wwpLeosVplsVirtualSwitchMplsMemberRowStatus,
       "wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy": wwpLeosVplsVirtualSwitchMplsMemberEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri": wwpLeosVplsVirtualSwitchMplsMemberEncapCosFixedDot1DPri,
       "wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy": wwpLeosVplsVirtualSwitchMplsMemberSubscriberDot1dPolicy,
       "wwpLeosVplsVirtualSwitchMplsMemberStatsTable": wwpLeosVplsVirtualSwitchMplsMemberStatsTable,
       "wwpLeosVplsVirtualSwitchMplsMemberStatsEntry": wwpLeosVplsVirtualSwitchMplsMemberStatsEntry,
       "wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi": wwpLeosVplsVirtualSwitchMplsMemberRxBytesHi,
       "wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo": wwpLeosVplsVirtualSwitchMplsMemberRxBytesLo,
       "wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable": wwpLeosVplsVirtualSwitchMplsMemberMeshVcTable,
       "wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry": wwpLeosVplsVirtualSwitchMplsMemberMeshVcEntry,
       "wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc": wwpLeosVplsVirtualSwitchMplsMemberMeshVcMeshVc,
       "wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus": wwpLeosVplsVirtualSwitchMplsMemberMeshVcRowStatus,
       "wwpLeosVplsVirtualSwitchMplsMemberAcVcTable": wwpLeosVplsVirtualSwitchMplsMemberAcVcTable,
       "wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry": wwpLeosVplsVirtualSwitchMplsMemberAcVcEntry,
       "wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc": wwpLeosVplsVirtualSwitchMplsMemberAcVcAcVc,
       "wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus": wwpLeosVplsVirtualSwitchMplsMemberAcVcRowStatus,
       "wwpLeosVplsSwitchMplsCtrlProtocolTable": wwpLeosVplsSwitchMplsCtrlProtocolTable,
       "wwpLeosVplsSwitchMplsCtrlProtocolEntry": wwpLeosVplsSwitchMplsCtrlProtocolEntry,
       "wwpLeosVplsSwitchMplsCtrlProtocolNum": wwpLeosVplsSwitchMplsCtrlProtocolNum,
       "wwpLeosVplsSwitchMplsCtrlType": wwpLeosVplsSwitchMplsCtrlType,
       "wwpLeosVplsVirtualSwitchEthTable": wwpLeosVplsVirtualSwitchEthTable,
       "wwpLeosVplsVirtualSwitchEthEntry": wwpLeosVplsVirtualSwitchEthEntry,
       "wwpLeosVplsVirtualSwitchEthIndx": wwpLeosVplsVirtualSwitchEthIndx,
       "wwpLeosVplsVirtualSwitchEthName": wwpLeosVplsVirtualSwitchEthName,
       "wwpLeosVplsVirtualSwitchEthVc": wwpLeosVplsVirtualSwitchEthVc,
       "wwpLeosVplsVirtualSwitchEthEncapCosPolicy": wwpLeosVplsVirtualSwitchEthEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri": wwpLeosVplsVirtualSwitchEthEncapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchEthDecapCosPolicy": wwpLeosVplsVirtualSwitchEthDecapCosPolicy,
       "wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri": wwpLeosVplsVirtualSwitchEthDecapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState": wwpLeosVplsVirtualSwitchEthCtrlProtocolTunnelState,
       "wwpLeosVplsVirtualSwitchEthRowStatus": wwpLeosVplsVirtualSwitchEthRowStatus,
       "wwpLeosVplsVirtualSwitchEthMacLrnState": wwpLeosVplsVirtualSwitchEthMacLrnState,
       "wwpLeosVplsVirtualSwitchEthTunnelMethod": wwpLeosVplsVirtualSwitchEthTunnelMethod,
       "wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri": wwpLeosVplsVirtualSwitchEthCtrlProtocolDot1dPri,
       "wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy": wwpLeosVplsVirtualSwitchEthSubscriberDot1dPolicy,
       "wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate": wwpLeosVplsVirtualSwitchEthCtrlProtTransFrameValidate,
       "wwpLeosVplsVirtualSwitchEthVcType": wwpLeosVplsVirtualSwitchEthVcType,
       "wwpLeosVplsVirtualSwitchEthHonorPriority": wwpLeosVplsVirtualSwitchEthHonorPriority,
       "wwpLeosVplsVirtualSwitchEthDescription": wwpLeosVplsVirtualSwitchEthDescription,
       "wwpLeosVplsVirtualSwitchEthReservedVlan": wwpLeosVplsVirtualSwitchEthReservedVlan,
       "wwpLeosVplsVirtualSwitchEthMemberTable": wwpLeosVplsVirtualSwitchEthMemberTable,
       "wwpLeosVplsVirtualSwitchEthMemberEntry": wwpLeosVplsVirtualSwitchEthMemberEntry,
       "wwpLeosVplsVirtualSwitchEthMemberPortId": wwpLeosVplsVirtualSwitchEthMemberPortId,
       "wwpLeosVplsVirtualSwitchEthMemberVlan": wwpLeosVplsVirtualSwitchEthMemberVlan,
       "wwpLeosVplsVirtualSwitchEthMemberRowStatus": wwpLeosVplsVirtualSwitchEthMemberRowStatus,
       "wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy": wwpLeosVplsVirtualSwitchEthMemberEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri": wwpLeosVplsVirtualSwitchEthMemberEncapCosFixedDot1DPri,
       "wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy": wwpLeosVplsVirtualSwitchEthMemberSubscriberDot1dPolicy,
       "wwpLeosVplsVirtualSwitchEthMemberStatsTable": wwpLeosVplsVirtualSwitchEthMemberStatsTable,
       "wwpLeosVplsVirtualSwitchEthMemberStatsEntry": wwpLeosVplsVirtualSwitchEthMemberStatsEntry,
       "wwpLeosVplsVirtualSwitchEthMemberRxBytesHi": wwpLeosVplsVirtualSwitchEthMemberRxBytesHi,
       "wwpLeosVplsVirtualSwitchEthMemberRxBytesLo": wwpLeosVplsVirtualSwitchEthMemberRxBytesLo,
       "wwpLeosVplsSwitchEthCtrlProtocolTable": wwpLeosVplsSwitchEthCtrlProtocolTable,
       "wwpLeosVplsSwitchEthCtrlProtocolEntry": wwpLeosVplsSwitchEthCtrlProtocolEntry,
       "wwpLeosVplsSwitchEthCtrlProtocolNum": wwpLeosVplsSwitchEthCtrlProtocolNum,
       "wwpLeosVplsSwitchEthCtrlType": wwpLeosVplsSwitchEthCtrlType,
       "wwpLeosVplsVirtualSwitchEtypeTranslationTable": wwpLeosVplsVirtualSwitchEtypeTranslationTable,
       "wwpLeosVplsVirtualSwitchEtypeTranslationEntry": wwpLeosVplsVirtualSwitchEtypeTranslationEntry,
       "wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype": wwpLeosVplsVirtualSwitchEtypeTranslationOriginalEtype,
       "wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype": wwpLeosVplsVirtualSwitchEtypeTranslationMappedEtype,
       "wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus": wwpLeosVplsVirtualSwitchEtypeTranslationRowStatus,
       "wwpLeosVplsTunnelPairTable": wwpLeosVplsTunnelPairTable,
       "wwpLeosVplsTunnelPairEntry": wwpLeosVplsTunnelPairEntry,
       "wwpLeosVplsTunnelPairIndx": wwpLeosVplsTunnelPairIndx,
       "wwpLeosVplsTunnelPairName": wwpLeosVplsTunnelPairName,
       "wwpLeosVplsTunnelPairEncapTunnelIndx": wwpLeosVplsTunnelPairEncapTunnelIndx,
       "wwpLeosVplsTunnelPairDecapTunnelIndx": wwpLeosVplsTunnelPairDecapTunnelIndx,
       "wwpLeosVplsTunnelPairRowStatus": wwpLeosVplsTunnelPairRowStatus,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberTable": wwpLeosVplsVirtualSwitchMplsEvplMemberTable,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberEntry": wwpLeosVplsVirtualSwitchMplsEvplMemberEntry,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberPortId": wwpLeosVplsVirtualSwitchMplsEvplMemberPortId,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId": wwpLeosVplsVirtualSwitchMplsEvplMemberVlanId,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus": wwpLeosVplsVirtualSwitchMplsEvplMemberRowStatus,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy": wwpLeosVplsVirtualSwitchMplsEvplMemberEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri": wwpLeosVplsVirtualSwitchMplsEvplMemberEncapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy": wwpLeosVplsVirtualSwitchMplsEvplMemberSubscriberDot1dPolicy,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable": wwpLeosVplsVirtualSwitchMplsEvplMemberStatsTable,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry": wwpLeosVplsVirtualSwitchMplsEvplMemberStatsEntry,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi": wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesHi,
       "wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo": wwpLeosVplsVirtualSwitchMplsEvplMemberRxBytesLo,
       "wwpLeosVplsVirtualSwitchEthEvplMemberTable": wwpLeosVplsVirtualSwitchEthEvplMemberTable,
       "wwpLeosVplsVirtualSwitchEthEvplMemberEntry": wwpLeosVplsVirtualSwitchEthEvplMemberEntry,
       "wwpLeosVplsVirtualSwitchEthEvplMemberPortId": wwpLeosVplsVirtualSwitchEthEvplMemberPortId,
       "wwpLeosVplsVirtualSwitchEthEvplMemberVlan": wwpLeosVplsVirtualSwitchEthEvplMemberVlan,
       "wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus": wwpLeosVplsVirtualSwitchEthEvplMemberRowStatus,
       "wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy": wwpLeosVplsVirtualSwitchEthEvplMemberEncapCosPolicy,
       "wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri": wwpLeosVplsVirtualSwitchEthEvplMemberEncapFixedDot1dPri,
       "wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy": wwpLeosVplsVirtualSwitchEthEvplMemberSubscriberDot1dPolicy,
       "wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag": wwpLeosVplsVirtualSwitchEthEvplMemberTranslateTag,
       "wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid": wwpLeosVplsVirtualSwitchEthEvplMemberServiceVlanTpid,
       "wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable": wwpLeosVplsVirtualSwitchEthEvplMemberStatsTable,
       "wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry": wwpLeosVplsVirtualSwitchEthEvplMemberStatsEntry,
       "wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi": wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesHi,
       "wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo": wwpLeosVplsVirtualSwitchEthEvplMemberRxBytesLo,
       "wwpLeosVplsVirtualCircuitEthTotalStatsTable": wwpLeosVplsVirtualCircuitEthTotalStatsTable,
       "wwpLeosVplsVirtualCircuitEthTotalStatsEntry": wwpLeosVplsVirtualCircuitEthTotalStatsEntry,
       "wwpLeosVplsVirtualCircuitEthTotalTxBytesHi": wwpLeosVplsVirtualCircuitEthTotalTxBytesHi,
       "wwpLeosVplsVirtualCircuitEthTotalTxBytesLo": wwpLeosVplsVirtualCircuitEthTotalTxBytesLo,
       "wwpLeosVplsVirtualCircuitEthTotalRxBytesHi": wwpLeosVplsVirtualCircuitEthTotalRxBytesHi,
       "wwpLeosVplsVirtualCircuitEthTotalRxBytesLo": wwpLeosVplsVirtualCircuitEthTotalRxBytesLo,
       "wwpLeosVplsVirtualCircuitMplsTotalStatsTable": wwpLeosVplsVirtualCircuitMplsTotalStatsTable,
       "wwpLeosVplsVirtualCircuitMplsTotalStatsEntry": wwpLeosVplsVirtualCircuitMplsTotalStatsEntry,
       "wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi": wwpLeosVplsVirtualCircuitMplsTotalTxBytesHi,
       "wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo": wwpLeosVplsVirtualCircuitMplsTotalTxBytesLo,
       "wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi": wwpLeosVplsVirtualCircuitMplsTotalRxBytesHi,
       "wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo": wwpLeosVplsVirtualCircuitMplsTotalRxBytesLo,
       "wwpLeosVplsVirtualSwitchEthL2CftProtocolTable": wwpLeosVplsVirtualSwitchEthL2CftProtocolTable,
       "wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry": wwpLeosVplsVirtualSwitchEthL2CftProtocolEntry,
       "wwpLeosVplsVirtualSwitchEthL2CftProtocolType": wwpLeosVplsVirtualSwitchEthL2CftProtocolType,
       "wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition": wwpLeosVplsVirtualSwitchEthL2CftProtocolDisposition,
       "wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus": wwpLeosVplsVirtualSwitchEthL2CftProtocolRowStatus,
       "wwpLeosVplsVirtualSwitchCFTProtoStatsTable": wwpLeosVplsVirtualSwitchCFTProtoStatsTable,
       "wwpLeosVplsVirtualSwitchCFTProtoStatsEntry": wwpLeosVplsVirtualSwitchCFTProtoStatsEntry,
       "wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx": wwpLeosVplsVirtualSwitchCFTProtoStatsEntryVirtualSwitchIndx,
       "wwpLeosVplsVirtualSwitchCFTProtol2RxPkts": wwpLeosVplsVirtualSwitchCFTProtol2RxPkts,
       "wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts": wwpLeosVplsVirtualSwitchCFTProtol2TunneledPkts,
       "wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts": wwpLeosVplsVirtualSwitchCFTProtol2PeerPkts,
       "wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts": wwpLeosVplsVirtualSwitchCFTProtol2DiscardedPkts,
       "wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts": wwpLeosVplsVirtualSwitchCFTProtol2DecodedPkts,
       "wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures": wwpLeosVplsVirtualSwitchCFTProtol2DecodedFailures,
       "wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts": wwpLeosVplsVirtualSwitchCFTProtol2TunneledSubcriberPortPkts,
       "wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum": wwpLeosVplsVirtualSwitchCFTProtol2ProtocolNum,
       "wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable": wwpLeosVplsVirtualSwitchCFTProtoTotalStatsTable,
       "wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry": wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntry,
       "wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx": wwpLeosVplsVirtualSwitchCFTProtoTotalStatsEntryVirtualSwitchIndx,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts": wwpLeosVplsVirtualSwitchCFTProtoTotall2RxPkts,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts": wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledPkts,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts": wwpLeosVplsVirtualSwitchCFTProtoTotall2PeerPkts,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts": wwpLeosVplsVirtualSwitchCFTProtoTotall2DiscardedPkts,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts": wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedPkts,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures": wwpLeosVplsVirtualSwitchCFTProtoTotall2DecodedFailures,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts": wwpLeosVplsVirtualSwitchCFTProtoTotall2TunneledSubcriberPortPkts,
       "wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum": wwpLeosVplsVirtualSwitchCFTProtoTotall2ProtocolNum,
       "wwpLeosVplsMIBNotificationPrefix": wwpLeosVplsMIBNotificationPrefix,
       "wwpLeosVplsMIBNotifications": wwpLeosVplsMIBNotifications,
       "wwpLeosVplsMIBConformance": wwpLeosVplsMIBConformance,
       "wwpLeosVplsMIBCompliances": wwpLeosVplsMIBCompliances,
       "wwpLeosVplsMIBGroups": wwpLeosVplsMIBGroups}
)
