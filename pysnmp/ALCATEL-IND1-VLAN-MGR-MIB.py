# SNMP MIB module (ALCATEL-IND1-VLAN-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VLAN-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:32 2024
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

(softentIND1VlanMgt,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1VlanMgt")

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

alcatelIND1VLANMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1)
)
alcatelIND1VLANMgrMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpxNetworkAddress(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VLANMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBObjects = _AlcatelIND1VLANMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBObjects.setStatus("current")
_VlanMgrVlan_ObjectIdentity = ObjectIdentity
vlanMgrVlan = _VlanMgrVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vlanNumber"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanNumber_Type(Integer32):
    """Custom type vlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanNumber_Type.__name__ = "Integer32"
_VlanNumber_Object = MibTableColumn
vlanNumber = _VlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1),
    _VlanNumber_Type()
)
vlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNumber.setStatus("current")


class _VlanDescription_Type(DisplayString):
    """Custom type vlanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanDescription_Type.__name__ = "DisplayString"
_VlanDescription_Object = MibTableColumn
vlanDescription = _VlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2),
    _VlanDescription_Type()
)
vlanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDescription.setStatus("current")


class _VlanAdmStatus_Type(Integer32):
    """Custom type vlanAdmStatus based on Integer32"""
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


_VlanAdmStatus_Type.__name__ = "Integer32"
_VlanAdmStatus_Object = MibTableColumn
vlanAdmStatus = _VlanAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 3),
    _VlanAdmStatus_Type()
)
vlanAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAdmStatus.setStatus("current")


class _VlanOperStatus_Type(Integer32):
    """Custom type vlanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_VlanOperStatus_Type.__name__ = "Integer32"
_VlanOperStatus_Object = MibTableColumn
vlanOperStatus = _VlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 4),
    _VlanOperStatus_Type()
)
vlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanOperStatus.setStatus("current")
_VlanStatus_Type = RowStatus
_VlanStatus_Object = MibTableColumn
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 5),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")


class _VlanStpStatus_Type(Integer32):
    """Custom type vlanStpStatus based on Integer32"""
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


_VlanStpStatus_Type.__name__ = "Integer32"
_VlanStpStatus_Object = MibTableColumn
vlanStpStatus = _VlanStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 6),
    _VlanStpStatus_Type()
)
vlanStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStpStatus.setStatus("current")


class _VlanAuthentStatus_Type(Integer32):
    """Custom type vlanAuthentStatus based on Integer32"""
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


_VlanAuthentStatus_Type.__name__ = "Integer32"
_VlanAuthentStatus_Object = MibTableColumn
vlanAuthentStatus = _VlanAuthentStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 7),
    _VlanAuthentStatus_Type()
)
vlanAuthentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAuthentStatus.setStatus("current")


class _VlanVoiceStatus_Type(Integer32):
    """Custom type vlanVoiceStatus based on Integer32"""
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


_VlanVoiceStatus_Type.__name__ = "Integer32"
_VlanVoiceStatus_Object = MibTableColumn
vlanVoiceStatus = _VlanVoiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 8),
    _VlanVoiceStatus_Type()
)
vlanVoiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceStatus.setStatus("current")
_VlanIpAddress_Type = IpAddress
_VlanIpAddress_Object = MibTableColumn
vlanIpAddress = _VlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 9),
    _VlanIpAddress_Type()
)
vlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpAddress.setStatus("current")
_VlanIpMask_Type = IpAddress
_VlanIpMask_Object = MibTableColumn
vlanIpMask = _VlanIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 10),
    _VlanIpMask_Type()
)
vlanIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpMask.setStatus("current")


class _VlanIpEncap_Type(Integer32):
    """Custom type vlanIpEncap based on Integer32"""
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
        *(("ethernet2", 1),
          ("notApplicable", 3),
          ("snap", 2))
    )


_VlanIpEncap_Type.__name__ = "Integer32"
_VlanIpEncap_Object = MibTableColumn
vlanIpEncap = _VlanIpEncap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 11),
    _VlanIpEncap_Type()
)
vlanIpEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpEncap.setStatus("current")


class _VlanIpForward_Type(Integer32):
    """Custom type vlanIpForward based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 3))
    )


_VlanIpForward_Type.__name__ = "Integer32"
_VlanIpForward_Object = MibTableColumn
vlanIpForward = _VlanIpForward_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 12),
    _VlanIpForward_Type()
)
vlanIpForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpForward.setStatus("current")


class _VlanIpStatus_Type(Integer32):
    """Custom type vlanIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_VlanIpStatus_Type.__name__ = "Integer32"
_VlanIpStatus_Object = MibTableColumn
vlanIpStatus = _VlanIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 13),
    _VlanIpStatus_Type()
)
vlanIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpStatus.setStatus("current")
_VlanIpxNet_Type = IpxNetworkAddress
_VlanIpxNet_Object = MibTableColumn
vlanIpxNet = _VlanIpxNet_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 14),
    _VlanIpxNet_Type()
)
vlanIpxNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpxNet.setStatus("current")


class _VlanIpxEncap_Type(Integer32):
    """Custom type vlanIpxEncap based on Integer32"""
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
        *(("ethernet2", 1),
          ("llc", 3),
          ("notApplicable", 5),
          ("novellraw", 2),
          ("snap", 4))
    )


_VlanIpxEncap_Type.__name__ = "Integer32"
_VlanIpxEncap_Object = MibTableColumn
vlanIpxEncap = _VlanIpxEncap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 15),
    _VlanIpxEncap_Type()
)
vlanIpxEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpxEncap.setStatus("current")


class _VlanIpxRipSapMode_Type(Integer32):
    """Custom type vlanIpxRipSapMode based on Integer32"""
    defaultValue = 2

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
        *(("inactive", 4),
          ("notApplicable", 5),
          ("riponly", 1),
          ("ripsap", 2),
          ("triggered", 3))
    )


_VlanIpxRipSapMode_Type.__name__ = "Integer32"
_VlanIpxRipSapMode_Object = MibTableColumn
vlanIpxRipSapMode = _VlanIpxRipSapMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 16),
    _VlanIpxRipSapMode_Type()
)
vlanIpxRipSapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpxRipSapMode.setStatus("current")


class _VlanIpxDelayTicks_Type(Integer32):
    """Custom type vlanIpxDelayTicks based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanIpxDelayTicks_Type.__name__ = "Integer32"
_VlanIpxDelayTicks_Object = MibTableColumn
vlanIpxDelayTicks = _VlanIpxDelayTicks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 17),
    _VlanIpxDelayTicks_Type()
)
vlanIpxDelayTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpxDelayTicks.setStatus("current")


class _VlanIpxStatus_Type(Integer32):
    """Custom type vlanIpxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_VlanIpxStatus_Type.__name__ = "Integer32"
_VlanIpxStatus_Object = MibTableColumn
vlanIpxStatus = _VlanIpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 18),
    _VlanIpxStatus_Type()
)
vlanIpxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIpxStatus.setStatus("current")


class _VlanTagMobilePortStatus_Type(Integer32):
    """Custom type vlanTagMobilePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VlanTagMobilePortStatus_Type.__name__ = "Integer32"
_VlanTagMobilePortStatus_Object = MibTableColumn
vlanTagMobilePortStatus = _VlanTagMobilePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 19),
    _VlanTagMobilePortStatus_Type()
)
vlanTagMobilePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagMobilePortStatus.setStatus("current")


class _VlanPortMacStatus_Type(Integer32):
    """Custom type vlanPortMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VlanPortMacStatus_Type.__name__ = "Integer32"
_VlanPortMacStatus_Object = MibTableColumn
vlanPortMacStatus = _VlanPortMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 20),
    _VlanPortMacStatus_Type()
)
vlanPortMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortMacStatus.setStatus("current")


class _VlanLocalProxyArp_Type(Integer32):
    """Custom type vlanLocalProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VlanLocalProxyArp_Type.__name__ = "Integer32"
_VlanLocalProxyArp_Object = MibTableColumn
vlanLocalProxyArp = _VlanLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 21),
    _VlanLocalProxyArp_Type()
)
vlanLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanLocalProxyArp.setStatus("current")


class _VlanMtu_Type(Integer32):
    """Custom type vlanMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 9198),
    )


_VlanMtu_Type.__name__ = "Integer32"
_VlanMtu_Object = MibTableColumn
vlanMtu = _VlanMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 22),
    _VlanMtu_Type()
)
vlanMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMtu.setStatus("current")


class _Vlan1x1StpStatus_Type(Integer32):
    """Custom type vlan1x1StpStatus based on Integer32"""
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


_Vlan1x1StpStatus_Type.__name__ = "Integer32"
_Vlan1x1StpStatus_Object = MibTableColumn
vlan1x1StpStatus = _Vlan1x1StpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 23),
    _Vlan1x1StpStatus_Type()
)
vlan1x1StpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlan1x1StpStatus.setStatus("current")


class _VlanflatStpStatus_Type(Integer32):
    """Custom type vlanflatStpStatus based on Integer32"""
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


_VlanflatStpStatus_Type.__name__ = "Integer32"
_VlanflatStpStatus_Object = MibTableColumn
vlanflatStpStatus = _VlanflatStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 24),
    _VlanflatStpStatus_Type()
)
vlanflatStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanflatStpStatus.setStatus("current")


class _VlanHABandwidth_Type(Integer32):
    """Custom type vlanHABandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_VlanHABandwidth_Type.__name__ = "Integer32"
_VlanHABandwidth_Object = MibTableColumn
vlanHABandwidth = _VlanHABandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 25),
    _VlanHABandwidth_Type()
)
vlanHABandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanHABandwidth.setStatus("current")


class _VlanSvlanTrafficType_Type(Integer32):
    """Custom type vlanSvlanTrafficType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("customer", 1),
          ("eServiceCustomer", 6),
          ("eServiceManagement", 7),
          ("eServiceMulticastVlanStacking", 8),
          ("multicastEnterprise", 3),
          ("multicastVlanStacking", 4),
          ("notApplicable", 0),
          ("provider", 2))
    )


_VlanSvlanTrafficType_Type.__name__ = "Integer32"
_VlanSvlanTrafficType_Object = MibTableColumn
vlanSvlanTrafficType = _VlanSvlanTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 26),
    _VlanSvlanTrafficType_Type()
)
vlanSvlanTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSvlanTrafficType.setStatus("current")


class _VlanSvlanPriority_Type(Integer32):
    """Custom type vlanSvlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_VlanSvlanPriority_Type.__name__ = "Integer32"
_VlanSvlanPriority_Object = MibTableColumn
vlanSvlanPriority = _VlanSvlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 27),
    _VlanSvlanPriority_Type()
)
vlanSvlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSvlanPriority.setStatus("current")


class _VlanMacLearningControlStatus_Type(Integer32):
    """Custom type vlanMacLearningControlStatus based on Integer32"""
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


_VlanMacLearningControlStatus_Type.__name__ = "Integer32"
_VlanMacLearningControlStatus_Object = MibTableColumn
vlanMacLearningControlStatus = _VlanMacLearningControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 28),
    _VlanMacLearningControlStatus_Type()
)
vlanMacLearningControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMacLearningControlStatus.setStatus("current")
_VlanMgrVpa_ObjectIdentity = ObjectIdentity
vlanMgrVpa = _VlanMgrVpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2)
)
_VpaTable_Object = MibTable
vpaTable = _VpaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vpaTable.setStatus("current")
_VpaEntry_Object = MibTableRow
vpaEntry = _VpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1)
)
vpaEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vpaVlanNumber"),
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vpaIfIndex"),
)
if mibBuilder.loadTexts:
    vpaEntry.setStatus("current")


class _VpaVlanNumber_Type(Integer32):
    """Custom type vpaVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VpaVlanNumber_Type.__name__ = "Integer32"
_VpaVlanNumber_Object = MibTableColumn
vpaVlanNumber = _VpaVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 1),
    _VpaVlanNumber_Type()
)
vpaVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpaVlanNumber.setStatus("current")


class _VpaIfIndex_Type(Unsigned32):
    """Custom type vpaIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VpaIfIndex_Type.__name__ = "Unsigned32"
_VpaIfIndex_Object = MibTableColumn
vpaIfIndex = _VpaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 2),
    _VpaIfIndex_Type()
)
vpaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpaIfIndex.setStatus("current")


class _VpaType_Type(Integer32):
    """Custom type vpaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cfgDefault", 1),
          ("dynamic", 7),
          ("mirrored", 4),
          ("mobile", 3),
          ("qTagged", 2),
          ("svlan", 6))
    )


_VpaType_Type.__name__ = "Integer32"
_VpaType_Object = MibTableColumn
vpaType = _VpaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 3),
    _VpaType_Type()
)
vpaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpaType.setStatus("current")


class _VpaState_Type(Integer32):
    """Custom type vpaState based on Integer32"""
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
        *(("blocking", 2),
          ("filtering", 4),
          ("forwarding", 3),
          ("inactive", 1))
    )


_VpaState_Type.__name__ = "Integer32"
_VpaState_Object = MibTableColumn
vpaState = _VpaState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 4),
    _VpaState_Type()
)
vpaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpaState.setStatus("current")
_VpaStatus_Type = RowStatus
_VpaStatus_Object = MibTableColumn
vpaStatus = _VpaStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 5),
    _VpaStatus_Type()
)
vpaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpaStatus.setStatus("current")


class _VpaPortMacType_Type(Integer32):
    """Custom type vpaPortMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("inapplicable", 3),
          ("ingress", 1))
    )


_VpaPortMacType_Type.__name__ = "Integer32"
_VpaPortMacType_Object = MibTableColumn
vpaPortMacType = _VpaPortMacType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 6),
    _VpaPortMacType_Type()
)
vpaPortMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpaPortMacType.setStatus("current")
_VlanMgrVlanSet_ObjectIdentity = ObjectIdentity
vlanMgrVlanSet = _VlanMgrVlanSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3)
)


class _VlanSetVlanCount_Type(Integer32):
    """Custom type vlanSetVlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanSetVlanCount_Type.__name__ = "Integer32"
_VlanSetVlanCount_Object = MibScalar
vlanSetVlanCount = _VlanSetVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 1),
    _VlanSetVlanCount_Type()
)
vlanSetVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetVlanCount.setStatus("current")


class _VlanSetVlanRouterCount_Type(Integer32):
    """Custom type vlanSetVlanRouterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanSetVlanRouterCount_Type.__name__ = "Integer32"
_VlanSetVlanRouterCount_Object = MibScalar
vlanSetVlanRouterCount = _VlanSetVlanRouterCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 2),
    _VlanSetVlanRouterCount_Type()
)
vlanSetVlanRouterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetVlanRouterCount.setStatus("current")


class _VlanSetIpRouterCount_Type(Integer32):
    """Custom type vlanSetIpRouterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanSetIpRouterCount_Type.__name__ = "Integer32"
_VlanSetIpRouterCount_Object = MibScalar
vlanSetIpRouterCount = _VlanSetIpRouterCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 3),
    _VlanSetIpRouterCount_Type()
)
vlanSetIpRouterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetIpRouterCount.setStatus("current")


class _VlanSetIpxRouterCount_Type(Integer32):
    """Custom type vlanSetIpxRouterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_VlanSetIpxRouterCount_Type.__name__ = "Integer32"
_VlanSetIpxRouterCount_Object = MibScalar
vlanSetIpxRouterCount = _VlanSetIpxRouterCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 4),
    _VlanSetIpxRouterCount_Type()
)
vlanSetIpxRouterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetIpxRouterCount.setStatus("current")


class _VlanSetMultiRtrMacStatus_Type(Integer32):
    """Custom type vlanSetMultiRtrMacStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_VlanSetMultiRtrMacStatus_Type.__name__ = "Integer32"
_VlanSetMultiRtrMacStatus_Object = MibScalar
vlanSetMultiRtrMacStatus = _VlanSetMultiRtrMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 5),
    _VlanSetMultiRtrMacStatus_Type()
)
vlanSetMultiRtrMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSetMultiRtrMacStatus.setStatus("current")
_VlanMgrHAPort_ObjectIdentity = ObjectIdentity
vlanMgrHAPort = _VlanMgrHAPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4)
)
_VlanHAPortTable_Object = MibTable
vlanHAPortTable = _VlanHAPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vlanHAPortTable.setStatus("current")
_VlanHAPortEntry_Object = MibTableRow
vlanHAPortEntry = _VlanHAPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4, 1, 1)
)
vlanHAPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vlanHAPortVlanId"),
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vlanHAPortIfIndex"),
    (0, "ALCATEL-IND1-VLAN-MGR-MIB", "vlanHAPortType"),
)
if mibBuilder.loadTexts:
    vlanHAPortEntry.setStatus("current")


class _VlanHAPortVlanId_Type(Integer32):
    """Custom type vlanHAPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanHAPortVlanId_Type.__name__ = "Integer32"
_VlanHAPortVlanId_Object = MibTableColumn
vlanHAPortVlanId = _VlanHAPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4, 1, 1, 1),
    _VlanHAPortVlanId_Type()
)
vlanHAPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanHAPortVlanId.setStatus("current")
_VlanHAPortIfIndex_Type = Unsigned32
_VlanHAPortIfIndex_Object = MibTableColumn
vlanHAPortIfIndex = _VlanHAPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4, 1, 1, 2),
    _VlanHAPortIfIndex_Type()
)
vlanHAPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanHAPortIfIndex.setStatus("current")


class _VlanHAPortType_Type(Integer32):
    """Custom type vlanHAPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_VlanHAPortType_Type.__name__ = "Integer32"
_VlanHAPortType_Object = MibTableColumn
vlanHAPortType = _VlanHAPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4, 1, 1, 3),
    _VlanHAPortType_Type()
)
vlanHAPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanHAPortType.setStatus("current")
_VlanHAPortRowStatus_Type = RowStatus
_VlanHAPortRowStatus_Object = MibTableColumn
vlanHAPortRowStatus = _VlanHAPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 4, 1, 1, 4),
    _VlanHAPortRowStatus_Type()
)
vlanHAPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanHAPortRowStatus.setStatus("current")
_AlcatelIND1VLANMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBConformance = _AlcatelIND1VLANMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBConformance.setStatus("current")
_AlcatelIND1VLANMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBGroups = _AlcatelIND1VLANMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBGroups.setStatus("current")
_AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBCompliances = _AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBCompliances.setStatus("current")

# Managed Objects groups

vlanMgrVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1, 1)
)
vlanMgrVlanGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-MGR-MIB", "vlanNumber"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanDescription"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanAdmStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanOperStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlan1x1StpStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanflatStpStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanStpStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanAuthentStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanVoiceStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpAddress"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpMask"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpEncap"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpForward"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpStatus"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpxNet"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpxEncap"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpxRipSapMode"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpxDelayTicks"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanIpxStatus"))
)
if mibBuilder.loadTexts:
    vlanMgrVlanGroup.setStatus("current")

vlanMgrVpaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1, 2)
)
vlanMgrVpaGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-MGR-MIB", "vpaVlanNumber"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vpaIfIndex"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vpaType"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vpaState"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vpaStatus"))
)
if mibBuilder.loadTexts:
    vlanMgrVpaGroup.setStatus("current")

vlanMgrVlanSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1, 3)
)
vlanMgrVlanSetGroup.setObjects(
      *(("ALCATEL-IND1-VLAN-MGR-MIB", "vlanSetVlanCount"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanSetVlanRouterCount"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanSetIpRouterCount"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanSetIpxRouterCount"),
        ("ALCATEL-IND1-VLAN-MGR-MIB", "vlanSetMultiRtrMacStatus"))
)
if mibBuilder.loadTexts:
    vlanMgrVlanSetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1VLANMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VLAN-MGR-MIB",
    **{"IpxNetworkAddress": IpxNetworkAddress,
       "alcatelIND1VLANMgrMIB": alcatelIND1VLANMgrMIB,
       "alcatelIND1VLANMgrMIBObjects": alcatelIND1VLANMgrMIBObjects,
       "vlanMgrVlan": vlanMgrVlan,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanNumber": vlanNumber,
       "vlanDescription": vlanDescription,
       "vlanAdmStatus": vlanAdmStatus,
       "vlanOperStatus": vlanOperStatus,
       "vlanStatus": vlanStatus,
       "vlanStpStatus": vlanStpStatus,
       "vlanAuthentStatus": vlanAuthentStatus,
       "vlanVoiceStatus": vlanVoiceStatus,
       "vlanIpAddress": vlanIpAddress,
       "vlanIpMask": vlanIpMask,
       "vlanIpEncap": vlanIpEncap,
       "vlanIpForward": vlanIpForward,
       "vlanIpStatus": vlanIpStatus,
       "vlanIpxNet": vlanIpxNet,
       "vlanIpxEncap": vlanIpxEncap,
       "vlanIpxRipSapMode": vlanIpxRipSapMode,
       "vlanIpxDelayTicks": vlanIpxDelayTicks,
       "vlanIpxStatus": vlanIpxStatus,
       "vlanTagMobilePortStatus": vlanTagMobilePortStatus,
       "vlanPortMacStatus": vlanPortMacStatus,
       "vlanLocalProxyArp": vlanLocalProxyArp,
       "vlanMtu": vlanMtu,
       "vlan1x1StpStatus": vlan1x1StpStatus,
       "vlanflatStpStatus": vlanflatStpStatus,
       "vlanHABandwidth": vlanHABandwidth,
       "vlanSvlanTrafficType": vlanSvlanTrafficType,
       "vlanSvlanPriority": vlanSvlanPriority,
       "vlanMacLearningControlStatus": vlanMacLearningControlStatus,
       "vlanMgrVpa": vlanMgrVpa,
       "vpaTable": vpaTable,
       "vpaEntry": vpaEntry,
       "vpaVlanNumber": vpaVlanNumber,
       "vpaIfIndex": vpaIfIndex,
       "vpaType": vpaType,
       "vpaState": vpaState,
       "vpaStatus": vpaStatus,
       "vpaPortMacType": vpaPortMacType,
       "vlanMgrVlanSet": vlanMgrVlanSet,
       "vlanSetVlanCount": vlanSetVlanCount,
       "vlanSetVlanRouterCount": vlanSetVlanRouterCount,
       "vlanSetIpRouterCount": vlanSetIpRouterCount,
       "vlanSetIpxRouterCount": vlanSetIpxRouterCount,
       "vlanSetMultiRtrMacStatus": vlanSetMultiRtrMacStatus,
       "vlanMgrHAPort": vlanMgrHAPort,
       "vlanHAPortTable": vlanHAPortTable,
       "vlanHAPortEntry": vlanHAPortEntry,
       "vlanHAPortVlanId": vlanHAPortVlanId,
       "vlanHAPortIfIndex": vlanHAPortIfIndex,
       "vlanHAPortType": vlanHAPortType,
       "vlanHAPortRowStatus": vlanHAPortRowStatus,
       "alcatelIND1VLANMgrMIBConformance": alcatelIND1VLANMgrMIBConformance,
       "alcatelIND1VLANMgrMIBGroups": alcatelIND1VLANMgrMIBGroups,
       "vlanMgrVlanGroup": vlanMgrVlanGroup,
       "vlanMgrVpaGroup": vlanMgrVpaGroup,
       "vlanMgrVlanSetGroup": vlanMgrVlanSetGroup,
       "alcatelIND1VLANMgrMIBCompliances": alcatelIND1VLANMgrMIBCompliances,
       "alcatelIND1VLANMgrMIBCompliance": alcatelIND1VLANMgrMIBCompliance}
)
