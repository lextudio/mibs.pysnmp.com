# SNMP MIB module (BLADETYPE2-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADETYPE2-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:01 2024
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

(hpSwitchBladeType2_Mgmt,) = mibBuilder.importSymbols(
    "HP-SWITCH-PL-MIB",
    "hpSwitchBladeType2-Mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

acl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcConfig_ObjectIdentity = ObjectIdentity
acConfig = _AcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1)
)
_AcList_ObjectIdentity = ObjectIdentity
acList = _AcList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1)
)
_AclCurCfgTable_Object = MibTable
aclCurCfgTable = _AclCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aclCurCfgTable.setStatus("current")
_AclCurCfgEntry_Object = MibTableRow
aclCurCfgEntry = _AclCurCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1)
)
aclCurCfgEntry.setIndexNames(
    (0, "BLADETYPE2-ACL-MIB", "aclCurCfgIndex"),
)
if mibBuilder.loadTexts:
    aclCurCfgEntry.setStatus("current")
_AclCurCfgIndex_Type = Unsigned32
_AclCurCfgIndex_Object = MibTableColumn
aclCurCfgIndex = _AclCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 1),
    _AclCurCfgIndex_Type()
)
aclCurCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclCurCfgIndex.setStatus("current")
_AclCurCfgBlock_Type = Unsigned32
_AclCurCfgBlock_Object = MibTableColumn
aclCurCfgBlock = _AclCurCfgBlock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 2),
    _AclCurCfgBlock_Type()
)
aclCurCfgBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgBlock.setStatus("current")
_AclCurCfgGroup_Type = Unsigned32
_AclCurCfgGroup_Object = MibTableColumn
aclCurCfgGroup = _AclCurCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 3),
    _AclCurCfgGroup_Type()
)
aclCurCfgGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgGroup.setStatus("current")


class _AclCurCfgFilterAction_Type(Integer32):
    """Custom type aclCurCfgFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("none", 0),
          ("permit", 1),
          ("setcos", 3))
    )


_AclCurCfgFilterAction_Type.__name__ = "Integer32"
_AclCurCfgFilterAction_Object = MibTableColumn
aclCurCfgFilterAction = _AclCurCfgFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 4),
    _AclCurCfgFilterAction_Type()
)
aclCurCfgFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgFilterAction.setStatus("current")


class _AclCurCfgFilterActionSetCOS_Type(Integer32):
    """Custom type aclCurCfgFilterActionSetCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("none", 0))
    )


_AclCurCfgFilterActionSetCOS_Type.__name__ = "Integer32"
_AclCurCfgFilterActionSetCOS_Object = MibTableColumn
aclCurCfgFilterActionSetCOS = _AclCurCfgFilterActionSetCOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 5),
    _AclCurCfgFilterActionSetCOS_Type()
)
aclCurCfgFilterActionSetCOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgFilterActionSetCOS.setStatus("current")


class _AclCurCfgEthFmt_Type(Integer32):
    """Custom type aclCurCfgEthFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 1),
          ("ieee802dot3", 4),
          ("llc", 3),
          ("none", 0),
          ("snap", 2))
    )


_AclCurCfgEthFmt_Type.__name__ = "Integer32"
_AclCurCfgEthFmt_Object = MibTableColumn
aclCurCfgEthFmt = _AclCurCfgEthFmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 6),
    _AclCurCfgEthFmt_Type()
)
aclCurCfgEthFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgEthFmt.setStatus("current")


class _AclCurCfgTagFmt_Type(Integer32):
    """Custom type aclCurCfgTagFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 1))
    )


_AclCurCfgTagFmt_Type.__name__ = "Integer32"
_AclCurCfgTagFmt_Object = MibTableColumn
aclCurCfgTagFmt = _AclCurCfgTagFmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 7),
    _AclCurCfgTagFmt_Type()
)
aclCurCfgTagFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgTagFmt.setStatus("current")
_AclCurCfgSrcMACAddress_Type = MacAddress
_AclCurCfgSrcMACAddress_Object = MibTableColumn
aclCurCfgSrcMACAddress = _AclCurCfgSrcMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 9),
    _AclCurCfgSrcMACAddress_Type()
)
aclCurCfgSrcMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgSrcMACAddress.setStatus("current")
_AclCurCfgSrcMACMask_Type = MacAddress
_AclCurCfgSrcMACMask_Object = MibTableColumn
aclCurCfgSrcMACMask = _AclCurCfgSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 10),
    _AclCurCfgSrcMACMask_Type()
)
aclCurCfgSrcMACMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgSrcMACMask.setStatus("current")
_AclCurCfgDstMACAddress_Type = MacAddress
_AclCurCfgDstMACAddress_Object = MibTableColumn
aclCurCfgDstMACAddress = _AclCurCfgDstMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 11),
    _AclCurCfgDstMACAddress_Type()
)
aclCurCfgDstMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgDstMACAddress.setStatus("current")
_AclCurCfgDstMACMask_Type = MacAddress
_AclCurCfgDstMACMask_Object = MibTableColumn
aclCurCfgDstMACMask = _AclCurCfgDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 12),
    _AclCurCfgDstMACMask_Type()
)
aclCurCfgDstMACMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgDstMACMask.setStatus("current")


class _AclCurCfgEthernetTypeName_Type(Integer32):
    """Custom type aclCurCfgEthernetTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 6),
          ("arp", 1),
          ("ipv4", 2),
          ("ipv6", 3),
          ("mpls", 4),
          ("none", 0),
          ("other", 7),
          ("rarp", 5))
    )


_AclCurCfgEthernetTypeName_Type.__name__ = "Integer32"
_AclCurCfgEthernetTypeName_Object = MibTableColumn
aclCurCfgEthernetTypeName = _AclCurCfgEthernetTypeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 13),
    _AclCurCfgEthernetTypeName_Type()
)
aclCurCfgEthernetTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgEthernetTypeName.setStatus("current")


class _AclCurCfgEthernetTypeValue_Type(Integer32):
    """Custom type aclCurCfgEthernetTypeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclCurCfgEthernetTypeValue_Type.__name__ = "Integer32"
_AclCurCfgEthernetTypeValue_Object = MibTableColumn
aclCurCfgEthernetTypeValue = _AclCurCfgEthernetTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 14),
    _AclCurCfgEthernetTypeValue_Type()
)
aclCurCfgEthernetTypeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgEthernetTypeValue.setStatus("current")


class _AclCurCfgVLanId_Type(Integer32):
    """Custom type aclCurCfgVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclCurCfgVLanId_Type.__name__ = "Integer32"
_AclCurCfgVLanId_Object = MibTableColumn
aclCurCfgVLanId = _AclCurCfgVLanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 15),
    _AclCurCfgVLanId_Type()
)
aclCurCfgVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgVLanId.setStatus("current")


class _AclCurCfgVLanMask_Type(Integer32):
    """Custom type aclCurCfgVLanMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclCurCfgVLanMask_Type.__name__ = "Integer32"
_AclCurCfgVLanMask_Object = MibTableColumn
aclCurCfgVLanMask = _AclCurCfgVLanMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 16),
    _AclCurCfgVLanMask_Type()
)
aclCurCfgVLanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgVLanMask.setStatus("current")


class _AclCurCfg8021pPriority_Type(Integer32):
    """Custom type aclCurCfg8021pPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("none", 0),
          ("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )


_AclCurCfg8021pPriority_Type.__name__ = "Integer32"
_AclCurCfg8021pPriority_Object = MibTableColumn
aclCurCfg8021pPriority = _AclCurCfg8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 17),
    _AclCurCfg8021pPriority_Type()
)
aclCurCfg8021pPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfg8021pPriority.setStatus("current")


class _AclCurCfgTypeOfService_Type(Integer32):
    """Custom type aclCurCfgTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclCurCfgTypeOfService_Type.__name__ = "Integer32"
_AclCurCfgTypeOfService_Object = MibTableColumn
aclCurCfgTypeOfService = _AclCurCfgTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 18),
    _AclCurCfgTypeOfService_Type()
)
aclCurCfgTypeOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgTypeOfService.setStatus("current")


class _AclCurCfgProtocol_Type(Integer32):
    """Custom type aclCurCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclCurCfgProtocol_Type.__name__ = "Integer32"
_AclCurCfgProtocol_Object = MibTableColumn
aclCurCfgProtocol = _AclCurCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 19),
    _AclCurCfgProtocol_Type()
)
aclCurCfgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgProtocol.setStatus("current")
_AclCurCfgSrcIPAddress_Type = IpAddress
_AclCurCfgSrcIPAddress_Object = MibTableColumn
aclCurCfgSrcIPAddress = _AclCurCfgSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 20),
    _AclCurCfgSrcIPAddress_Type()
)
aclCurCfgSrcIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgSrcIPAddress.setStatus("current")
_AclCurCfgSrcIPMask_Type = IpAddress
_AclCurCfgSrcIPMask_Object = MibTableColumn
aclCurCfgSrcIPMask = _AclCurCfgSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 21),
    _AclCurCfgSrcIPMask_Type()
)
aclCurCfgSrcIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgSrcIPMask.setStatus("current")
_AclCurCfgDstIPAddress_Type = IpAddress
_AclCurCfgDstIPAddress_Object = MibTableColumn
aclCurCfgDstIPAddress = _AclCurCfgDstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 22),
    _AclCurCfgDstIPAddress_Type()
)
aclCurCfgDstIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgDstIPAddress.setStatus("current")
_AclCurCfgDstIPMask_Type = IpAddress
_AclCurCfgDstIPMask_Object = MibTableColumn
aclCurCfgDstIPMask = _AclCurCfgDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 23),
    _AclCurCfgDstIPMask_Type()
)
aclCurCfgDstIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgDstIPMask.setStatus("current")


class _AclCurCfgSrcPort_Type(Integer32):
    """Custom type aclCurCfgSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclCurCfgSrcPort_Type.__name__ = "Integer32"
_AclCurCfgSrcPort_Object = MibTableColumn
aclCurCfgSrcPort = _AclCurCfgSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 24),
    _AclCurCfgSrcPort_Type()
)
aclCurCfgSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgSrcPort.setStatus("current")


class _AclCurCfgSrcPortMask_Type(Integer32):
    """Custom type aclCurCfgSrcPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclCurCfgSrcPortMask_Type.__name__ = "Integer32"
_AclCurCfgSrcPortMask_Object = MibTableColumn
aclCurCfgSrcPortMask = _AclCurCfgSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 25),
    _AclCurCfgSrcPortMask_Type()
)
aclCurCfgSrcPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgSrcPortMask.setStatus("current")


class _AclCurCfgDstPort_Type(Integer32):
    """Custom type aclCurCfgDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclCurCfgDstPort_Type.__name__ = "Integer32"
_AclCurCfgDstPort_Object = MibTableColumn
aclCurCfgDstPort = _AclCurCfgDstPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 26),
    _AclCurCfgDstPort_Type()
)
aclCurCfgDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgDstPort.setStatus("current")


class _AclCurCfgDstPortMask_Type(Integer32):
    """Custom type aclCurCfgDstPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclCurCfgDstPortMask_Type.__name__ = "Integer32"
_AclCurCfgDstPortMask_Object = MibTableColumn
aclCurCfgDstPortMask = _AclCurCfgDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 27),
    _AclCurCfgDstPortMask_Type()
)
aclCurCfgDstPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgDstPortMask.setStatus("current")


class _AclCurCfgTCPFlags_Type(Bits):
    """Custom type aclCurCfgTCPFlags based on Bits"""
    namedValues = NamedValues(
        *(("reserved1", 0),
          ("reserved2", 1),
          ("tcpACK", 3),
          ("tcpFIN", 7),
          ("tcpPSH", 4),
          ("tcpRST", 5),
          ("tcpSYN", 6),
          ("tcpURG", 2))
    )

_AclCurCfgTCPFlags_Type.__name__ = "Bits"
_AclCurCfgTCPFlags_Object = MibTableColumn
aclCurCfgTCPFlags = _AclCurCfgTCPFlags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 28),
    _AclCurCfgTCPFlags_Type()
)
aclCurCfgTCPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgTCPFlags.setStatus("current")
_AclCurCfgEgressPorts_Type = OctetString
_AclCurCfgEgressPorts_Object = MibTableColumn
aclCurCfgEgressPorts = _AclCurCfgEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 29),
    _AclCurCfgEgressPorts_Type()
)
aclCurCfgEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgEgressPorts.setStatus("current")


class _AclCurCfgStatistics_Type(Integer32):
    """Custom type aclCurCfgStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AclCurCfgStatistics_Type.__name__ = "Integer32"
_AclCurCfgStatistics_Object = MibTableColumn
aclCurCfgStatistics = _AclCurCfgStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 30),
    _AclCurCfgStatistics_Type()
)
aclCurCfgStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgStatistics.setStatus("current")


class _AclCurCfgTCPFlagsMask_Type(Bits):
    """Custom type aclCurCfgTCPFlagsMask based on Bits"""
    namedValues = NamedValues(
        *(("reserved1", 0),
          ("reserved2", 1),
          ("tcpACK", 3),
          ("tcpFIN", 7),
          ("tcpPSH", 4),
          ("tcpRST", 5),
          ("tcpSYN", 6),
          ("tcpURG", 2))
    )

_AclCurCfgTCPFlagsMask_Type.__name__ = "Bits"
_AclCurCfgTCPFlagsMask_Object = MibTableColumn
aclCurCfgTCPFlagsMask = _AclCurCfgTCPFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 1, 1, 39),
    _AclCurCfgTCPFlagsMask_Type()
)
aclCurCfgTCPFlagsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclCurCfgTCPFlagsMask.setStatus("current")
_AclNewCfgTable_Object = MibTable
aclNewCfgTable = _AclNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aclNewCfgTable.setStatus("current")
_AclNewCfgEntry_Object = MibTableRow
aclNewCfgEntry = _AclNewCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1)
)
aclNewCfgEntry.setIndexNames(
    (0, "BLADETYPE2-ACL-MIB", "aclNewCfgIndex"),
)
if mibBuilder.loadTexts:
    aclNewCfgEntry.setStatus("current")
_AclNewCfgIndex_Type = Unsigned32
_AclNewCfgIndex_Object = MibTableColumn
aclNewCfgIndex = _AclNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 1),
    _AclNewCfgIndex_Type()
)
aclNewCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclNewCfgIndex.setStatus("current")
_AclNewCfgBlock_Type = Unsigned32
_AclNewCfgBlock_Object = MibTableColumn
aclNewCfgBlock = _AclNewCfgBlock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 2),
    _AclNewCfgBlock_Type()
)
aclNewCfgBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgBlock.setStatus("current")
_AclNewCfgGroup_Type = Unsigned32
_AclNewCfgGroup_Object = MibTableColumn
aclNewCfgGroup = _AclNewCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 3),
    _AclNewCfgGroup_Type()
)
aclNewCfgGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgGroup.setStatus("current")


class _AclNewCfgFilterAction_Type(Integer32):
    """Custom type aclNewCfgFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("none", 0),
          ("permit", 1),
          ("setcos", 3))
    )


_AclNewCfgFilterAction_Type.__name__ = "Integer32"
_AclNewCfgFilterAction_Object = MibTableColumn
aclNewCfgFilterAction = _AclNewCfgFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 4),
    _AclNewCfgFilterAction_Type()
)
aclNewCfgFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgFilterAction.setStatus("current")


class _AclNewCfgFilterActionSetCOS_Type(Integer32):
    """Custom type aclNewCfgFilterActionSetCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("cos0", 1),
          ("cos1", 2),
          ("cos2", 3),
          ("cos3", 4),
          ("cos4", 5),
          ("cos5", 6),
          ("cos6", 7),
          ("cos7", 8),
          ("none", 0))
    )


_AclNewCfgFilterActionSetCOS_Type.__name__ = "Integer32"
_AclNewCfgFilterActionSetCOS_Object = MibTableColumn
aclNewCfgFilterActionSetCOS = _AclNewCfgFilterActionSetCOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 5),
    _AclNewCfgFilterActionSetCOS_Type()
)
aclNewCfgFilterActionSetCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgFilterActionSetCOS.setStatus("current")


class _AclNewCfgEthFmt_Type(Integer32):
    """Custom type aclNewCfgEthFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 1),
          ("ieee802dot3", 4),
          ("llc", 3),
          ("none", 0),
          ("snap", 2))
    )


_AclNewCfgEthFmt_Type.__name__ = "Integer32"
_AclNewCfgEthFmt_Object = MibTableColumn
aclNewCfgEthFmt = _AclNewCfgEthFmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 6),
    _AclNewCfgEthFmt_Type()
)
aclNewCfgEthFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgEthFmt.setStatus("current")


class _AclNewCfgTagFmt_Type(Integer32):
    """Custom type aclNewCfgTagFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tagged", 2))
    )


_AclNewCfgTagFmt_Type.__name__ = "Integer32"
_AclNewCfgTagFmt_Object = MibTableColumn
aclNewCfgTagFmt = _AclNewCfgTagFmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 7),
    _AclNewCfgTagFmt_Type()
)
aclNewCfgTagFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgTagFmt.setStatus("current")
_AclNewCfgSrcMACAddress_Type = MacAddress
_AclNewCfgSrcMACAddress_Object = MibTableColumn
aclNewCfgSrcMACAddress = _AclNewCfgSrcMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 9),
    _AclNewCfgSrcMACAddress_Type()
)
aclNewCfgSrcMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgSrcMACAddress.setStatus("current")
_AclNewCfgSrcMACMask_Type = MacAddress
_AclNewCfgSrcMACMask_Object = MibTableColumn
aclNewCfgSrcMACMask = _AclNewCfgSrcMACMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 10),
    _AclNewCfgSrcMACMask_Type()
)
aclNewCfgSrcMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgSrcMACMask.setStatus("current")
_AclNewCfgDstMACAddress_Type = MacAddress
_AclNewCfgDstMACAddress_Object = MibTableColumn
aclNewCfgDstMACAddress = _AclNewCfgDstMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 11),
    _AclNewCfgDstMACAddress_Type()
)
aclNewCfgDstMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDstMACAddress.setStatus("current")
_AclNewCfgDstMACMask_Type = MacAddress
_AclNewCfgDstMACMask_Object = MibTableColumn
aclNewCfgDstMACMask = _AclNewCfgDstMACMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 12),
    _AclNewCfgDstMACMask_Type()
)
aclNewCfgDstMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDstMACMask.setStatus("current")


class _AclNewCfgEthernetTypeName_Type(Integer32):
    """Custom type aclNewCfgEthernetTypeName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", 6),
          ("arp", 1),
          ("ipv4", 2),
          ("ipv6", 3),
          ("mpls", 4),
          ("none", 0),
          ("other", 7),
          ("rarp", 5))
    )


_AclNewCfgEthernetTypeName_Type.__name__ = "Integer32"
_AclNewCfgEthernetTypeName_Object = MibTableColumn
aclNewCfgEthernetTypeName = _AclNewCfgEthernetTypeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 13),
    _AclNewCfgEthernetTypeName_Type()
)
aclNewCfgEthernetTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgEthernetTypeName.setStatus("current")


class _AclNewCfgEthernetTypeValue_Type(Integer32):
    """Custom type aclNewCfgEthernetTypeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNewCfgEthernetTypeValue_Type.__name__ = "Integer32"
_AclNewCfgEthernetTypeValue_Object = MibTableColumn
aclNewCfgEthernetTypeValue = _AclNewCfgEthernetTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 14),
    _AclNewCfgEthernetTypeValue_Type()
)
aclNewCfgEthernetTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgEthernetTypeValue.setStatus("current")


class _AclNewCfgVLanId_Type(Integer32):
    """Custom type aclNewCfgVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AclNewCfgVLanId_Type.__name__ = "Integer32"
_AclNewCfgVLanId_Object = MibTableColumn
aclNewCfgVLanId = _AclNewCfgVLanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 15),
    _AclNewCfgVLanId_Type()
)
aclNewCfgVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgVLanId.setStatus("current")


class _AclNewCfgVLanMask_Type(Integer32):
    """Custom type aclNewCfgVLanMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclNewCfgVLanMask_Type.__name__ = "Integer32"
_AclNewCfgVLanMask_Object = MibTableColumn
aclNewCfgVLanMask = _AclNewCfgVLanMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 16),
    _AclNewCfgVLanMask_Type()
)
aclNewCfgVLanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgVLanMask.setStatus("current")


class _AclNewCfg8021pPriority_Type(Integer32):
    """Custom type aclNewCfg8021pPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("none", 0),
          ("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )


_AclNewCfg8021pPriority_Type.__name__ = "Integer32"
_AclNewCfg8021pPriority_Object = MibTableColumn
aclNewCfg8021pPriority = _AclNewCfg8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 17),
    _AclNewCfg8021pPriority_Type()
)
aclNewCfg8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfg8021pPriority.setStatus("current")


class _AclNewCfgTypeOfService_Type(Integer32):
    """Custom type aclNewCfgTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclNewCfgTypeOfService_Type.__name__ = "Integer32"
_AclNewCfgTypeOfService_Object = MibTableColumn
aclNewCfgTypeOfService = _AclNewCfgTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 18),
    _AclNewCfgTypeOfService_Type()
)
aclNewCfgTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgTypeOfService.setStatus("current")


class _AclNewCfgProtocol_Type(Integer32):
    """Custom type aclNewCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclNewCfgProtocol_Type.__name__ = "Integer32"
_AclNewCfgProtocol_Object = MibTableColumn
aclNewCfgProtocol = _AclNewCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 19),
    _AclNewCfgProtocol_Type()
)
aclNewCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgProtocol.setStatus("current")
_AclNewCfgSrcIPAddress_Type = IpAddress
_AclNewCfgSrcIPAddress_Object = MibTableColumn
aclNewCfgSrcIPAddress = _AclNewCfgSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 20),
    _AclNewCfgSrcIPAddress_Type()
)
aclNewCfgSrcIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgSrcIPAddress.setStatus("current")
_AclNewCfgSrcIPMask_Type = IpAddress
_AclNewCfgSrcIPMask_Object = MibTableColumn
aclNewCfgSrcIPMask = _AclNewCfgSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 21),
    _AclNewCfgSrcIPMask_Type()
)
aclNewCfgSrcIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgSrcIPMask.setStatus("current")
_AclNewCfgDstIPAddress_Type = IpAddress
_AclNewCfgDstIPAddress_Object = MibTableColumn
aclNewCfgDstIPAddress = _AclNewCfgDstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 22),
    _AclNewCfgDstIPAddress_Type()
)
aclNewCfgDstIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDstIPAddress.setStatus("current")
_AclNewCfgDstIPMask_Type = IpAddress
_AclNewCfgDstIPMask_Object = MibTableColumn
aclNewCfgDstIPMask = _AclNewCfgDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 23),
    _AclNewCfgDstIPMask_Type()
)
aclNewCfgDstIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDstIPMask.setStatus("current")


class _AclNewCfgSrcPort_Type(Integer32):
    """Custom type aclNewCfgSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclNewCfgSrcPort_Type.__name__ = "Integer32"
_AclNewCfgSrcPort_Object = MibTableColumn
aclNewCfgSrcPort = _AclNewCfgSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 24),
    _AclNewCfgSrcPort_Type()
)
aclNewCfgSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgSrcPort.setStatus("current")


class _AclNewCfgSrcPortMask_Type(Integer32):
    """Custom type aclNewCfgSrcPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNewCfgSrcPortMask_Type.__name__ = "Integer32"
_AclNewCfgSrcPortMask_Object = MibTableColumn
aclNewCfgSrcPortMask = _AclNewCfgSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 25),
    _AclNewCfgSrcPortMask_Type()
)
aclNewCfgSrcPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgSrcPortMask.setStatus("current")


class _AclNewCfgDstPort_Type(Integer32):
    """Custom type aclNewCfgDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AclNewCfgDstPort_Type.__name__ = "Integer32"
_AclNewCfgDstPort_Object = MibTableColumn
aclNewCfgDstPort = _AclNewCfgDstPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 26),
    _AclNewCfgDstPort_Type()
)
aclNewCfgDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDstPort.setStatus("current")


class _AclNewCfgDstPortMask_Type(Integer32):
    """Custom type aclNewCfgDstPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNewCfgDstPortMask_Type.__name__ = "Integer32"
_AclNewCfgDstPortMask_Object = MibTableColumn
aclNewCfgDstPortMask = _AclNewCfgDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 27),
    _AclNewCfgDstPortMask_Type()
)
aclNewCfgDstPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDstPortMask.setStatus("current")


class _AclNewCfgTCPFlags_Type(Bits):
    """Custom type aclNewCfgTCPFlags based on Bits"""
    namedValues = NamedValues(
        *(("reserved1", 0),
          ("reserved2", 1),
          ("tcpACK", 3),
          ("tcpFIN", 7),
          ("tcpPSH", 4),
          ("tcpRST", 5),
          ("tcpSYN", 6),
          ("tcpURG", 2))
    )

_AclNewCfgTCPFlags_Type.__name__ = "Bits"
_AclNewCfgTCPFlags_Object = MibTableColumn
aclNewCfgTCPFlags = _AclNewCfgTCPFlags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 28),
    _AclNewCfgTCPFlags_Type()
)
aclNewCfgTCPFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgTCPFlags.setStatus("current")
_AclNewCfgEgressPorts_Type = OctetString
_AclNewCfgEgressPorts_Object = MibTableColumn
aclNewCfgEgressPorts = _AclNewCfgEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 29),
    _AclNewCfgEgressPorts_Type()
)
aclNewCfgEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNewCfgEgressPorts.setStatus("current")


class _AclNewCfgStatistics_Type(Integer32):
    """Custom type aclNewCfgStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AclNewCfgStatistics_Type.__name__ = "Integer32"
_AclNewCfgStatistics_Object = MibTableColumn
aclNewCfgStatistics = _AclNewCfgStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 30),
    _AclNewCfgStatistics_Type()
)
aclNewCfgStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgStatistics.setStatus("current")
_AclNewCfgAddEgressPort_Type = Unsigned32
_AclNewCfgAddEgressPort_Object = MibTableColumn
aclNewCfgAddEgressPort = _AclNewCfgAddEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 31),
    _AclNewCfgAddEgressPort_Type()
)
aclNewCfgAddEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgAddEgressPort.setStatus("current")
_AclNewCfgRemoveEgressPort_Type = Unsigned32
_AclNewCfgRemoveEgressPort_Object = MibTableColumn
aclNewCfgRemoveEgressPort = _AclNewCfgRemoveEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 32),
    _AclNewCfgRemoveEgressPort_Type()
)
aclNewCfgRemoveEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgRemoveEgressPort.setStatus("current")


class _AclNewCfgDelete_Type(Integer32):
    """Custom type aclNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_AclNewCfgDelete_Type.__name__ = "Integer32"
_AclNewCfgDelete_Object = MibTableColumn
aclNewCfgDelete = _AclNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 33),
    _AclNewCfgDelete_Type()
)
aclNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgDelete.setStatus("current")


class _AclNewCfgTCPFlagsMask_Type(Bits):
    """Custom type aclNewCfgTCPFlagsMask based on Bits"""
    namedValues = NamedValues(
        *(("reserved1", 0),
          ("reserved2", 1),
          ("tcpACK", 3),
          ("tcpFIN", 7),
          ("tcpPSH", 4),
          ("tcpRST", 5),
          ("tcpSYN", 6),
          ("tcpURG", 2))
    )

_AclNewCfgTCPFlagsMask_Type.__name__ = "Bits"
_AclNewCfgTCPFlagsMask_Object = MibTableColumn
aclNewCfgTCPFlagsMask = _AclNewCfgTCPFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 1, 2, 1, 39),
    _AclNewCfgTCPFlagsMask_Type()
)
aclNewCfgTCPFlagsMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNewCfgTCPFlagsMask.setStatus("current")
_AclBlock_ObjectIdentity = ObjectIdentity
aclBlock = _AclBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2)
)
_AclBlockCurCfgTable_Object = MibTable
aclBlockCurCfgTable = _AclBlockCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aclBlockCurCfgTable.setStatus("current")
_AclBlockCurCfgEntry_Object = MibTableRow
aclBlockCurCfgEntry = _AclBlockCurCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 1, 1)
)
aclBlockCurCfgEntry.setIndexNames(
    (0, "BLADETYPE2-ACL-MIB", "aclBlockCurCfgIndex"),
)
if mibBuilder.loadTexts:
    aclBlockCurCfgEntry.setStatus("current")
_AclBlockCurCfgIndex_Type = Unsigned32
_AclBlockCurCfgIndex_Object = MibTableColumn
aclBlockCurCfgIndex = _AclBlockCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 1, 1, 1),
    _AclBlockCurCfgIndex_Type()
)
aclBlockCurCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclBlockCurCfgIndex.setStatus("current")
_AclBlockCurCfgMemberAcls_Type = OctetString
_AclBlockCurCfgMemberAcls_Object = MibTableColumn
aclBlockCurCfgMemberAcls = _AclBlockCurCfgMemberAcls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 1, 1, 2),
    _AclBlockCurCfgMemberAcls_Type()
)
aclBlockCurCfgMemberAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclBlockCurCfgMemberAcls.setStatus("current")
_AclBlockNewCfgTable_Object = MibTable
aclBlockNewCfgTable = _AclBlockNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aclBlockNewCfgTable.setStatus("current")
_AclBlockNewCfgEntry_Object = MibTableRow
aclBlockNewCfgEntry = _AclBlockNewCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2, 1)
)
aclBlockNewCfgEntry.setIndexNames(
    (0, "BLADETYPE2-ACL-MIB", "aclBlockNewCfgIndex"),
)
if mibBuilder.loadTexts:
    aclBlockNewCfgEntry.setStatus("current")
_AclBlockNewCfgIndex_Type = Unsigned32
_AclBlockNewCfgIndex_Object = MibTableColumn
aclBlockNewCfgIndex = _AclBlockNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2, 1, 1),
    _AclBlockNewCfgIndex_Type()
)
aclBlockNewCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclBlockNewCfgIndex.setStatus("current")
_AclBlockNewCfgMemberAcls_Type = OctetString
_AclBlockNewCfgMemberAcls_Object = MibTableColumn
aclBlockNewCfgMemberAcls = _AclBlockNewCfgMemberAcls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2, 1, 2),
    _AclBlockNewCfgMemberAcls_Type()
)
aclBlockNewCfgMemberAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclBlockNewCfgMemberAcls.setStatus("current")
_AclBlockNewCfgAddAcl_Type = Unsigned32
_AclBlockNewCfgAddAcl_Object = MibTableColumn
aclBlockNewCfgAddAcl = _AclBlockNewCfgAddAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2, 1, 3),
    _AclBlockNewCfgAddAcl_Type()
)
aclBlockNewCfgAddAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclBlockNewCfgAddAcl.setStatus("current")
_AclBlockNewCfgRemoveAcl_Type = Unsigned32
_AclBlockNewCfgRemoveAcl_Object = MibTableColumn
aclBlockNewCfgRemoveAcl = _AclBlockNewCfgRemoveAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2, 1, 4),
    _AclBlockNewCfgRemoveAcl_Type()
)
aclBlockNewCfgRemoveAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclBlockNewCfgRemoveAcl.setStatus("current")


class _AclBlockNewCfgDelete_Type(Integer32):
    """Custom type aclBlockNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_AclBlockNewCfgDelete_Type.__name__ = "Integer32"
_AclBlockNewCfgDelete_Object = MibTableColumn
aclBlockNewCfgDelete = _AclBlockNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 2, 2, 1, 5),
    _AclBlockNewCfgDelete_Type()
)
aclBlockNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclBlockNewCfgDelete.setStatus("current")
_AclGroup_ObjectIdentity = ObjectIdentity
aclGroup = _AclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3)
)
_AclGroupCurCfgTable_Object = MibTable
aclGroupCurCfgTable = _AclGroupCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aclGroupCurCfgTable.setStatus("current")
_AclGroupCurCfgEntry_Object = MibTableRow
aclGroupCurCfgEntry = _AclGroupCurCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 1, 1)
)
aclGroupCurCfgEntry.setIndexNames(
    (0, "BLADETYPE2-ACL-MIB", "aclGroupCurCfgIndex"),
)
if mibBuilder.loadTexts:
    aclGroupCurCfgEntry.setStatus("current")
_AclGroupCurCfgIndex_Type = Unsigned32
_AclGroupCurCfgIndex_Object = MibTableColumn
aclGroupCurCfgIndex = _AclGroupCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 1, 1, 1),
    _AclGroupCurCfgIndex_Type()
)
aclGroupCurCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclGroupCurCfgIndex.setStatus("current")
_AclGroupCurCfgMemberAcls_Type = OctetString
_AclGroupCurCfgMemberAcls_Object = MibTableColumn
aclGroupCurCfgMemberAcls = _AclGroupCurCfgMemberAcls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 1, 1, 2),
    _AclGroupCurCfgMemberAcls_Type()
)
aclGroupCurCfgMemberAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclGroupCurCfgMemberAcls.setStatus("current")
_AclGroupCurCfgMemberBlocks_Type = OctetString
_AclGroupCurCfgMemberBlocks_Object = MibTableColumn
aclGroupCurCfgMemberBlocks = _AclGroupCurCfgMemberBlocks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 1, 1, 3),
    _AclGroupCurCfgMemberBlocks_Type()
)
aclGroupCurCfgMemberBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclGroupCurCfgMemberBlocks.setStatus("current")
_AclGroupNewCfgTable_Object = MibTable
aclGroupNewCfgTable = _AclGroupNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    aclGroupNewCfgTable.setStatus("current")
_AclGroupNewCfgEntry_Object = MibTableRow
aclGroupNewCfgEntry = _AclGroupNewCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1)
)
aclGroupNewCfgEntry.setIndexNames(
    (0, "BLADETYPE2-ACL-MIB", "aclGroupNewCfgIndex"),
)
if mibBuilder.loadTexts:
    aclGroupNewCfgEntry.setStatus("current")
_AclGroupNewCfgIndex_Type = Unsigned32
_AclGroupNewCfgIndex_Object = MibTableColumn
aclGroupNewCfgIndex = _AclGroupNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 1),
    _AclGroupNewCfgIndex_Type()
)
aclGroupNewCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclGroupNewCfgIndex.setStatus("current")
_AclGroupNewCfgMemberAcls_Type = OctetString
_AclGroupNewCfgMemberAcls_Object = MibTableColumn
aclGroupNewCfgMemberAcls = _AclGroupNewCfgMemberAcls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 2),
    _AclGroupNewCfgMemberAcls_Type()
)
aclGroupNewCfgMemberAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclGroupNewCfgMemberAcls.setStatus("current")
_AclGroupNewCfgMemberBlocks_Type = OctetString
_AclGroupNewCfgMemberBlocks_Object = MibTableColumn
aclGroupNewCfgMemberBlocks = _AclGroupNewCfgMemberBlocks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 3),
    _AclGroupNewCfgMemberBlocks_Type()
)
aclGroupNewCfgMemberBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclGroupNewCfgMemberBlocks.setStatus("current")
_AclGroupNewCfgAddAcl_Type = Unsigned32
_AclGroupNewCfgAddAcl_Object = MibTableColumn
aclGroupNewCfgAddAcl = _AclGroupNewCfgAddAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 4),
    _AclGroupNewCfgAddAcl_Type()
)
aclGroupNewCfgAddAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclGroupNewCfgAddAcl.setStatus("current")
_AclGroupNewCfgRemoveAcl_Type = Unsigned32
_AclGroupNewCfgRemoveAcl_Object = MibTableColumn
aclGroupNewCfgRemoveAcl = _AclGroupNewCfgRemoveAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 5),
    _AclGroupNewCfgRemoveAcl_Type()
)
aclGroupNewCfgRemoveAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclGroupNewCfgRemoveAcl.setStatus("current")
_AclGroupNewCfgAddBlock_Type = Unsigned32
_AclGroupNewCfgAddBlock_Object = MibTableColumn
aclGroupNewCfgAddBlock = _AclGroupNewCfgAddBlock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 6),
    _AclGroupNewCfgAddBlock_Type()
)
aclGroupNewCfgAddBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclGroupNewCfgAddBlock.setStatus("current")
_AclGroupNewCfgRemoveBlock_Type = Unsigned32
_AclGroupNewCfgRemoveBlock_Object = MibTableColumn
aclGroupNewCfgRemoveBlock = _AclGroupNewCfgRemoveBlock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 7),
    _AclGroupNewCfgRemoveBlock_Type()
)
aclGroupNewCfgRemoveBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclGroupNewCfgRemoveBlock.setStatus("current")


class _AclGroupNewCfgDelete_Type(Integer32):
    """Custom type aclGroupNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_AclGroupNewCfgDelete_Type.__name__ = "Integer32"
_AclGroupNewCfgDelete_Object = MibTableColumn
aclGroupNewCfgDelete = _AclGroupNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 9, 1, 3, 2, 1, 8),
    _AclGroupNewCfgDelete_Type()
)
aclGroupNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclGroupNewCfgDelete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADETYPE2-ACL-MIB",
    **{"acl": acl,
       "acConfig": acConfig,
       "acList": acList,
       "aclCurCfgTable": aclCurCfgTable,
       "aclCurCfgEntry": aclCurCfgEntry,
       "aclCurCfgIndex": aclCurCfgIndex,
       "aclCurCfgBlock": aclCurCfgBlock,
       "aclCurCfgGroup": aclCurCfgGroup,
       "aclCurCfgFilterAction": aclCurCfgFilterAction,
       "aclCurCfgFilterActionSetCOS": aclCurCfgFilterActionSetCOS,
       "aclCurCfgEthFmt": aclCurCfgEthFmt,
       "aclCurCfgTagFmt": aclCurCfgTagFmt,
       "aclCurCfgSrcMACAddress": aclCurCfgSrcMACAddress,
       "aclCurCfgSrcMACMask": aclCurCfgSrcMACMask,
       "aclCurCfgDstMACAddress": aclCurCfgDstMACAddress,
       "aclCurCfgDstMACMask": aclCurCfgDstMACMask,
       "aclCurCfgEthernetTypeName": aclCurCfgEthernetTypeName,
       "aclCurCfgEthernetTypeValue": aclCurCfgEthernetTypeValue,
       "aclCurCfgVLanId": aclCurCfgVLanId,
       "aclCurCfgVLanMask": aclCurCfgVLanMask,
       "aclCurCfg8021pPriority": aclCurCfg8021pPriority,
       "aclCurCfgTypeOfService": aclCurCfgTypeOfService,
       "aclCurCfgProtocol": aclCurCfgProtocol,
       "aclCurCfgSrcIPAddress": aclCurCfgSrcIPAddress,
       "aclCurCfgSrcIPMask": aclCurCfgSrcIPMask,
       "aclCurCfgDstIPAddress": aclCurCfgDstIPAddress,
       "aclCurCfgDstIPMask": aclCurCfgDstIPMask,
       "aclCurCfgSrcPort": aclCurCfgSrcPort,
       "aclCurCfgSrcPortMask": aclCurCfgSrcPortMask,
       "aclCurCfgDstPort": aclCurCfgDstPort,
       "aclCurCfgDstPortMask": aclCurCfgDstPortMask,
       "aclCurCfgTCPFlags": aclCurCfgTCPFlags,
       "aclCurCfgEgressPorts": aclCurCfgEgressPorts,
       "aclCurCfgStatistics": aclCurCfgStatistics,
       "aclCurCfgTCPFlagsMask": aclCurCfgTCPFlagsMask,
       "aclNewCfgTable": aclNewCfgTable,
       "aclNewCfgEntry": aclNewCfgEntry,
       "aclNewCfgIndex": aclNewCfgIndex,
       "aclNewCfgBlock": aclNewCfgBlock,
       "aclNewCfgGroup": aclNewCfgGroup,
       "aclNewCfgFilterAction": aclNewCfgFilterAction,
       "aclNewCfgFilterActionSetCOS": aclNewCfgFilterActionSetCOS,
       "aclNewCfgEthFmt": aclNewCfgEthFmt,
       "aclNewCfgTagFmt": aclNewCfgTagFmt,
       "aclNewCfgSrcMACAddress": aclNewCfgSrcMACAddress,
       "aclNewCfgSrcMACMask": aclNewCfgSrcMACMask,
       "aclNewCfgDstMACAddress": aclNewCfgDstMACAddress,
       "aclNewCfgDstMACMask": aclNewCfgDstMACMask,
       "aclNewCfgEthernetTypeName": aclNewCfgEthernetTypeName,
       "aclNewCfgEthernetTypeValue": aclNewCfgEthernetTypeValue,
       "aclNewCfgVLanId": aclNewCfgVLanId,
       "aclNewCfgVLanMask": aclNewCfgVLanMask,
       "aclNewCfg8021pPriority": aclNewCfg8021pPriority,
       "aclNewCfgTypeOfService": aclNewCfgTypeOfService,
       "aclNewCfgProtocol": aclNewCfgProtocol,
       "aclNewCfgSrcIPAddress": aclNewCfgSrcIPAddress,
       "aclNewCfgSrcIPMask": aclNewCfgSrcIPMask,
       "aclNewCfgDstIPAddress": aclNewCfgDstIPAddress,
       "aclNewCfgDstIPMask": aclNewCfgDstIPMask,
       "aclNewCfgSrcPort": aclNewCfgSrcPort,
       "aclNewCfgSrcPortMask": aclNewCfgSrcPortMask,
       "aclNewCfgDstPort": aclNewCfgDstPort,
       "aclNewCfgDstPortMask": aclNewCfgDstPortMask,
       "aclNewCfgTCPFlags": aclNewCfgTCPFlags,
       "aclNewCfgEgressPorts": aclNewCfgEgressPorts,
       "aclNewCfgStatistics": aclNewCfgStatistics,
       "aclNewCfgAddEgressPort": aclNewCfgAddEgressPort,
       "aclNewCfgRemoveEgressPort": aclNewCfgRemoveEgressPort,
       "aclNewCfgDelete": aclNewCfgDelete,
       "aclNewCfgTCPFlagsMask": aclNewCfgTCPFlagsMask,
       "aclBlock": aclBlock,
       "aclBlockCurCfgTable": aclBlockCurCfgTable,
       "aclBlockCurCfgEntry": aclBlockCurCfgEntry,
       "aclBlockCurCfgIndex": aclBlockCurCfgIndex,
       "aclBlockCurCfgMemberAcls": aclBlockCurCfgMemberAcls,
       "aclBlockNewCfgTable": aclBlockNewCfgTable,
       "aclBlockNewCfgEntry": aclBlockNewCfgEntry,
       "aclBlockNewCfgIndex": aclBlockNewCfgIndex,
       "aclBlockNewCfgMemberAcls": aclBlockNewCfgMemberAcls,
       "aclBlockNewCfgAddAcl": aclBlockNewCfgAddAcl,
       "aclBlockNewCfgRemoveAcl": aclBlockNewCfgRemoveAcl,
       "aclBlockNewCfgDelete": aclBlockNewCfgDelete,
       "aclGroup": aclGroup,
       "aclGroupCurCfgTable": aclGroupCurCfgTable,
       "aclGroupCurCfgEntry": aclGroupCurCfgEntry,
       "aclGroupCurCfgIndex": aclGroupCurCfgIndex,
       "aclGroupCurCfgMemberAcls": aclGroupCurCfgMemberAcls,
       "aclGroupCurCfgMemberBlocks": aclGroupCurCfgMemberBlocks,
       "aclGroupNewCfgTable": aclGroupNewCfgTable,
       "aclGroupNewCfgEntry": aclGroupNewCfgEntry,
       "aclGroupNewCfgIndex": aclGroupNewCfgIndex,
       "aclGroupNewCfgMemberAcls": aclGroupNewCfgMemberAcls,
       "aclGroupNewCfgMemberBlocks": aclGroupNewCfgMemberBlocks,
       "aclGroupNewCfgAddAcl": aclGroupNewCfgAddAcl,
       "aclGroupNewCfgRemoveAcl": aclGroupNewCfgRemoveAcl,
       "aclGroupNewCfgAddBlock": aclGroupNewCfgAddBlock,
       "aclGroupNewCfgRemoveBlock": aclGroupNewCfgRemoveBlock,
       "aclGroupNewCfgDelete": aclGroupNewCfgDelete}
)
