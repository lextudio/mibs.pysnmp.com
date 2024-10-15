# SNMP MIB module (XYLAN-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:17 2024
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

(BridgeId,
 MacAddress,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout")

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

(xylanVlanArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanVlanArch")

(XylanPortFuncCodes,) = mibBuilder.importSymbols(
    "XYLAN-PORT-MIB",
    "XylanPortFuncCodes")


# MODULE-IDENTITY


# Types definitions



class XylanVlanAdminStatCodes(Integer32):
    """Custom type XylanVlanAdminStatCodes based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("disable", 1),
          ("enable", 2),
          ("modify", 5))
    )





class XylanVlanOperStatCodes(Integer32):
    """Custom type XylanVlanOperStatCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )





class XylanVlanModes(Integer32):
    """Custom type XylanVlanModes based on Integer32"""
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
        *(("atmCIP", 4),
          ("frRouter", 5),
          ("invalid", 1),
          ("other", 2),
          ("standard", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class VIPRouterRelayServType(Integer32):
    """Custom type VIPRouterRelayServType based on Integer32"""
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
        *(("vIPRouterRelayBootp", 1),
          ("vIPRouterRelayGen1", 4),
          ("vIPRouterRelayGen2", 5),
          ("vIPRouterRelayGen3", 6),
          ("vIPRouterRelayGen4", 7),
          ("vIPRouterRelayGen5", 8),
          ("vIPRouterRelayNBDD", 3),
          ("vIPRouterRelayNBNS", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VLanInfo_ObjectIdentity = ObjectIdentity
vLanInfo = _VLanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1)
)


class _VLanCurrentNumber_Type(Integer32):
    """Custom type vLanCurrentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VLanCurrentNumber_Type.__name__ = "Integer32"
_VLanCurrentNumber_Object = MibScalar
vLanCurrentNumber = _VLanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 1),
    _VLanCurrentNumber_Type()
)
vLanCurrentNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanCurrentNumber.setStatus("mandatory")
_VLanTable_Object = MibTable
vLanTable = _VLanTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vLanTable.setStatus("mandatory")
_VLanEntry_Object = MibTableRow
vLanEntry = _VLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1)
)
vLanEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vLanNumber"),
)
if mibBuilder.loadTexts:
    vLanEntry.setStatus("mandatory")


class _VLanNumber_Type(Integer32):
    """Custom type vLanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VLanNumber_Type.__name__ = "Integer32"
_VLanNumber_Object = MibTableColumn
vLanNumber = _VLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 1),
    _VLanNumber_Type()
)
vLanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanNumber.setStatus("mandatory")
_VLanBridgeAddress_Type = MacAddress
_VLanBridgeAddress_Object = MibTableColumn
vLanBridgeAddress = _VLanBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 2),
    _VLanBridgeAddress_Type()
)
vLanBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLanBridgeAddress.setStatus("mandatory")


class _VLanBridgeType_Type(Integer32):
    """Custom type vLanBridgeType based on Integer32"""
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
        *(("not-supported", 6),
          ("other", 2),
          ("sourceroute-only", 4),
          ("srt", 5),
          ("transparent-only", 3),
          ("unknown", 1))
    )


_VLanBridgeType_Type.__name__ = "Integer32"
_VLanBridgeType_Object = MibTableColumn
vLanBridgeType = _VLanBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 3),
    _VLanBridgeType_Type()
)
vLanBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLanBridgeType.setStatus("deprecated")


class _VLanDescription_Type(DisplayString):
    """Custom type vLanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VLanDescription_Type.__name__ = "DisplayString"
_VLanDescription_Object = MibTableColumn
vLanDescription = _VLanDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 4),
    _VLanDescription_Type()
)
vLanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanDescription.setStatus("mandatory")
_VLanAdmStatus_Type = XylanVlanAdminStatCodes
_VLanAdmStatus_Object = MibTableColumn
vLanAdmStatus = _VLanAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 5),
    _VLanAdmStatus_Type()
)
vLanAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanAdmStatus.setStatus("mandatory")
_VLanOperStatus_Type = XylanVlanOperStatCodes
_VLanOperStatus_Object = MibTableColumn
vLanOperStatus = _VLanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 6),
    _VLanOperStatus_Type()
)
vLanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLanOperStatus.setStatus("mandatory")
_VLanMode_Type = XylanVlanModes
_VLanMode_Object = MibTableColumn
vLanMode = _VLanMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 7),
    _VLanMode_Type()
)
vLanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanMode.setStatus("mandatory")
_VLanFloodOverride_Type = Integer32
_VLanFloodOverride_Object = MibTableColumn
vLanFloodOverride = _VLanFloodOverride_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 8),
    _VLanFloodOverride_Type()
)
vLanFloodOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanFloodOverride.setStatus("mandatory")
_VLanRouterAddress_Type = MacAddress
_VLanRouterAddress_Object = MibTableColumn
vLanRouterAddress = _VLanRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 9),
    _VLanRouterAddress_Type()
)
vLanRouterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanRouterAddress.setStatus("mandatory")


class _VLanMobileGroup_Type(Integer32):
    """Custom type vLanMobileGroup based on Integer32"""
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


_VLanMobileGroup_Type.__name__ = "Integer32"
_VLanMobileGroup_Object = MibTableColumn
vLanMobileGroup = _VLanMobileGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 10),
    _VLanMobileGroup_Type()
)
vLanMobileGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanMobileGroup.setStatus("mandatory")


class _VLanAuthGroup_Type(Integer32):
    """Custom type vLanAuthGroup based on Integer32"""
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


_VLanAuthGroup_Type.__name__ = "Integer32"
_VLanAuthGroup_Object = MibTableColumn
vLanAuthGroup = _VLanAuthGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 11),
    _VLanAuthGroup_Type()
)
vLanAuthGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanAuthGroup.setStatus("mandatory")
_VLanAuthGroupProtocol_Type = OctetString
_VLanAuthGroupProtocol_Object = MibTableColumn
vLanAuthGroupProtocol = _VLanAuthGroupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 12),
    _VLanAuthGroupProtocol_Type()
)
vLanAuthGroupProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanAuthGroupProtocol.setStatus("mandatory")


class _VLanStpStatus_Type(Integer32):
    """Custom type vLanStpStatus based on Integer32"""
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


_VLanStpStatus_Type.__name__ = "Integer32"
_VLanStpStatus_Object = MibTableColumn
vLanStpStatus = _VLanStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 13),
    _VLanStpStatus_Type()
)
vLanStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanStpStatus.setStatus("mandatory")


class _VLanBrdgTpExtendedAgeingTime_Type(Integer32):
    """Custom type vLanBrdgTpExtendedAgeingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VLanBrdgTpExtendedAgeingTime_Type.__name__ = "Integer32"
_VLanBrdgTpExtendedAgeingTime_Object = MibTableColumn
vLanBrdgTpExtendedAgeingTime = _VLanBrdgTpExtendedAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 14),
    _VLanBrdgTpExtendedAgeingTime_Type()
)
vLanBrdgTpExtendedAgeingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanBrdgTpExtendedAgeingTime.setStatus("mandatory")
_VLanPriority_Type = Integer32
_VLanPriority_Object = MibTableColumn
vLanPriority = _VLanPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 2, 1, 15),
    _VLanPriority_Type()
)
vLanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLanPriority.setStatus("mandatory")


class _VLanNextFreeNumber_Type(Integer32):
    """Custom type vLanNextFreeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VLanNextFreeNumber_Type.__name__ = "Integer32"
_VLanNextFreeNumber_Object = MibScalar
vLanNextFreeNumber = _VLanNextFreeNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 1, 3),
    _VLanNextFreeNumber_Type()
)
vLanNextFreeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLanNextFreeNumber.setStatus("mandatory")
_VIPRouterInfo_ObjectIdentity = ObjectIdentity
vIPRouterInfo = _VIPRouterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2)
)
_VIPRouterTable_Object = MibTable
vIPRouterTable = _VIPRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vIPRouterTable.setStatus("mandatory")
_VIPRouterEntry_Object = MibTableRow
vIPRouterEntry = _VIPRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1)
)
vIPRouterEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vIPRouterVLan"),
)
if mibBuilder.loadTexts:
    vIPRouterEntry.setStatus("mandatory")


class _VIPRouterVLan_Type(Integer32):
    """Custom type vIPRouterVLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VIPRouterVLan_Type.__name__ = "Integer32"
_VIPRouterVLan_Object = MibTableColumn
vIPRouterVLan = _VIPRouterVLan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 1),
    _VIPRouterVLan_Type()
)
vIPRouterVLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterVLan.setStatus("mandatory")


class _VIPRouterProtocol_Type(OctetString):
    """Custom type vIPRouterProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VIPRouterProtocol_Type.__name__ = "OctetString"
_VIPRouterProtocol_Object = MibTableColumn
vIPRouterProtocol = _VIPRouterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 2),
    _VIPRouterProtocol_Type()
)
vIPRouterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterProtocol.setStatus("mandatory")
_VIPRouterNetAddress_Type = IpAddress
_VIPRouterNetAddress_Object = MibTableColumn
vIPRouterNetAddress = _VIPRouterNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 3),
    _VIPRouterNetAddress_Type()
)
vIPRouterNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterNetAddress.setStatus("mandatory")
_VIPRouterSubNetMask_Type = IpAddress
_VIPRouterSubNetMask_Object = MibTableColumn
vIPRouterSubNetMask = _VIPRouterSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 4),
    _VIPRouterSubNetMask_Type()
)
vIPRouterSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterSubNetMask.setStatus("mandatory")
_VIPRouterBcastAddress_Type = IpAddress
_VIPRouterBcastAddress_Object = MibTableColumn
vIPRouterBcastAddress = _VIPRouterBcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 5),
    _VIPRouterBcastAddress_Type()
)
vIPRouterBcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterBcastAddress.setStatus("mandatory")


class _VIPRouterDescription_Type(DisplayString):
    """Custom type vIPRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VIPRouterDescription_Type.__name__ = "DisplayString"
_VIPRouterDescription_Object = MibTableColumn
vIPRouterDescription = _VIPRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 6),
    _VIPRouterDescription_Type()
)
vIPRouterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterDescription.setStatus("optional")
_VIPRouterAdmStatus_Type = XylanVlanAdminStatCodes
_VIPRouterAdmStatus_Object = MibTableColumn
vIPRouterAdmStatus = _VIPRouterAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 7),
    _VIPRouterAdmStatus_Type()
)
vIPRouterAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterAdmStatus.setStatus("mandatory")
_VIPRouterOperStatus_Type = XylanVlanOperStatCodes
_VIPRouterOperStatus_Object = MibTableColumn
vIPRouterOperStatus = _VIPRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 8),
    _VIPRouterOperStatus_Type()
)
vIPRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vIPRouterOperStatus.setStatus("mandatory")


class _VIPRouterFramingType_Type(Integer32):
    """Custom type vIPRouterFramingType based on Integer32"""
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
        *(("atm-1483", 6),
          ("ethernet-2", 1),
          ("ethernet-802-3", 2),
          ("fddi", 3),
          ("token-ring", 4),
          ("token-ring-source-routed", 5))
    )


_VIPRouterFramingType_Type.__name__ = "Integer32"
_VIPRouterFramingType_Object = MibTableColumn
vIPRouterFramingType = _VIPRouterFramingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 9),
    _VIPRouterFramingType_Type()
)
vIPRouterFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterFramingType.setStatus("mandatory")


class _VIPRouterRipConfigMode_Type(Integer32):
    """Custom type vIPRouterRipConfigMode based on Integer32"""
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
        *(("active", 3),
          ("deaf", 2),
          ("inactive", 4),
          ("silent", 1))
    )


_VIPRouterRipConfigMode_Type.__name__ = "Integer32"
_VIPRouterRipConfigMode_Object = MibTableColumn
vIPRouterRipConfigMode = _VIPRouterRipConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 1, 1, 10),
    _VIPRouterRipConfigMode_Type()
)
vIPRouterRipConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterRipConfigMode.setStatus("mandatory")
_VIPRouterRelayTable_Object = MibTable
vIPRouterRelayTable = _VIPRouterRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    vIPRouterRelayTable.setStatus("mandatory")
_VIPRouterRelayEntry_Object = MibTableRow
vIPRouterRelayEntry = _VIPRouterRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1)
)
vIPRouterRelayEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vIPRouterRelayService"),
)
if mibBuilder.loadTexts:
    vIPRouterRelayEntry.setStatus("mandatory")
_VIPRouterRelayService_Type = VIPRouterRelayServType
_VIPRouterRelayService_Object = MibTableColumn
vIPRouterRelayService = _VIPRouterRelayService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1, 1),
    _VIPRouterRelayService_Type()
)
vIPRouterRelayService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vIPRouterRelayService.setStatus("mandatory")
_VIPRouterRelayMode_Type = Integer32
_VIPRouterRelayMode_Object = MibTableColumn
vIPRouterRelayMode = _VIPRouterRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1, 2),
    _VIPRouterRelayMode_Type()
)
vIPRouterRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterRelayMode.setStatus("mandatory")
_VIPRouterRelayNextHop_Type = IpAddress
_VIPRouterRelayNextHop_Object = MibTableColumn
vIPRouterRelayNextHop = _VIPRouterRelayNextHop_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1, 3),
    _VIPRouterRelayNextHop_Type()
)
vIPRouterRelayNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterRelayNextHop.setStatus("mandatory")


class _VIPRouterRelayParam1_Type(Integer32):
    """Custom type vIPRouterRelayParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_VIPRouterRelayParam1_Type.__name__ = "Integer32"
_VIPRouterRelayParam1_Object = MibTableColumn
vIPRouterRelayParam1 = _VIPRouterRelayParam1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1, 4),
    _VIPRouterRelayParam1_Type()
)
vIPRouterRelayParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterRelayParam1.setStatus("mandatory")


class _VIPRouterRelayParam2_Type(Integer32):
    """Custom type vIPRouterRelayParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VIPRouterRelayParam2_Type.__name__ = "Integer32"
_VIPRouterRelayParam2_Object = MibTableColumn
vIPRouterRelayParam2 = _VIPRouterRelayParam2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1, 5),
    _VIPRouterRelayParam2_Type()
)
vIPRouterRelayParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterRelayParam2.setStatus("mandatory")


class _VIPRouterRelayDescription_Type(DisplayString):
    """Custom type vIPRouterRelayDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VIPRouterRelayDescription_Type.__name__ = "DisplayString"
_VIPRouterRelayDescription_Object = MibTableColumn
vIPRouterRelayDescription = _VIPRouterRelayDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 2, 2, 1, 6),
    _VIPRouterRelayDescription_Type()
)
vIPRouterRelayDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPRouterRelayDescription.setStatus("mandatory")
_VIPXRouterInfo_ObjectIdentity = ObjectIdentity
vIPXRouterInfo = _VIPXRouterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3)
)
_VIPXRouterTable_Object = MibTable
vIPXRouterTable = _VIPXRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vIPXRouterTable.setStatus("mandatory")
_VIPXRouterEntry_Object = MibTableRow
vIPXRouterEntry = _VIPXRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1)
)
vIPXRouterEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vIPXRouterVLan"),
)
if mibBuilder.loadTexts:
    vIPXRouterEntry.setStatus("mandatory")


class _VIPXRouterVLan_Type(Integer32):
    """Custom type vIPXRouterVLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VIPXRouterVLan_Type.__name__ = "Integer32"
_VIPXRouterVLan_Object = MibTableColumn
vIPXRouterVLan = _VIPXRouterVLan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 1),
    _VIPXRouterVLan_Type()
)
vIPXRouterVLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXRouterVLan.setStatus("mandatory")
_VIPXRouterProtocol_Type = Integer32
_VIPXRouterProtocol_Object = MibTableColumn
vIPXRouterProtocol = _VIPXRouterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 2),
    _VIPXRouterProtocol_Type()
)
vIPXRouterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXRouterProtocol.setStatus("mandatory")


class _VIPXRouterNetAddress_Type(OctetString):
    """Custom type vIPXRouterNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VIPXRouterNetAddress_Type.__name__ = "OctetString"
_VIPXRouterNetAddress_Object = MibTableColumn
vIPXRouterNetAddress = _VIPXRouterNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 3),
    _VIPXRouterNetAddress_Type()
)
vIPXRouterNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXRouterNetAddress.setStatus("mandatory")


class _VIPXRouterFramingType_Type(Integer32):
    """Custom type vIPXRouterFramingType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-2", 1),
          ("ethernet-802-3-llc", 2),
          ("ethernet-802-3-raw", 4),
          ("ethernet-802-3-snap", 3),
          ("fddi-llc", 7),
          ("fddi-llc-sr", 8),
          ("fddi-snap", 5),
          ("fddi-snap-sr", 6),
          ("token-ring-llc", 11),
          ("token-ring-llc-sr", 12),
          ("token-ring-snap", 9),
          ("token-ring-snap-sr", 10))
    )


_VIPXRouterFramingType_Type.__name__ = "Integer32"
_VIPXRouterFramingType_Object = MibTableColumn
vIPXRouterFramingType = _VIPXRouterFramingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 4),
    _VIPXRouterFramingType_Type()
)
vIPXRouterFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXRouterFramingType.setStatus("mandatory")


class _VIPXRouterDescription_Type(DisplayString):
    """Custom type vIPXRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VIPXRouterDescription_Type.__name__ = "DisplayString"
_VIPXRouterDescription_Object = MibTableColumn
vIPXRouterDescription = _VIPXRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 5),
    _VIPXRouterDescription_Type()
)
vIPXRouterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXRouterDescription.setStatus("optional")
_VIPXRouterAdmStatus_Type = XylanVlanAdminStatCodes
_VIPXRouterAdmStatus_Object = MibTableColumn
vIPXRouterAdmStatus = _VIPXRouterAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 6),
    _VIPXRouterAdmStatus_Type()
)
vIPXRouterAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXRouterAdmStatus.setStatus("mandatory")
_VIPXRouterOperStatus_Type = XylanVlanOperStatCodes
_VIPXRouterOperStatus_Object = MibTableColumn
vIPXRouterOperStatus = _VIPXRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 7),
    _VIPXRouterOperStatus_Type()
)
vIPXRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vIPXRouterOperStatus.setStatus("mandatory")


class _VIPXSrcRteType_Type(Integer32):
    """Custom type vIPXSrcRteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("are", 1),
          ("not-applicable", 3),
          ("ste", 2))
    )


_VIPXSrcRteType_Type.__name__ = "Integer32"
_VIPXSrcRteType_Object = MibTableColumn
vIPXSrcRteType = _VIPXSrcRteType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 3, 1, 1, 8),
    _VIPXSrcRteType_Type()
)
vIPXSrcRteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIPXSrcRteType.setStatus("mandatory")
_VBrdgInfo_ObjectIdentity = ObjectIdentity
vBrdgInfo = _VBrdgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4)
)
_VBrdgTpLearnEntryDiscards_Type = Counter32
_VBrdgTpLearnEntryDiscards_Object = MibScalar
vBrdgTpLearnEntryDiscards = _VBrdgTpLearnEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 1),
    _VBrdgTpLearnEntryDiscards_Type()
)
vBrdgTpLearnEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpLearnEntryDiscards.setStatus("mandatory")


class _VBrdgTpAgingTime_Type(Integer32):
    """Custom type vBrdgTpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VBrdgTpAgingTime_Type.__name__ = "Integer32"
_VBrdgTpAgingTime_Object = MibScalar
vBrdgTpAgingTime = _VBrdgTpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 2),
    _VBrdgTpAgingTime_Type()
)
vBrdgTpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgTpAgingTime.setStatus("mandatory")
_VBrdgTpFdbTable_Object = MibTable
vBrdgTpFdbTable = _VBrdgTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    vBrdgTpFdbTable.setStatus("mandatory")
_VBrdgTpFdbEntry_Object = MibTableRow
vBrdgTpFdbEntry = _VBrdgTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1)
)
vBrdgTpFdbEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vBrdgTpFdbGroupId"),
    (0, "XYLAN-VLAN-MIB", "vBrdgTpFdbAddress"),
)
if mibBuilder.loadTexts:
    vBrdgTpFdbEntry.setStatus("mandatory")
_VBrdgTpFdbGroupId_Type = Integer32
_VBrdgTpFdbGroupId_Object = MibTableColumn
vBrdgTpFdbGroupId = _VBrdgTpFdbGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 1),
    _VBrdgTpFdbGroupId_Type()
)
vBrdgTpFdbGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbGroupId.setStatus("mandatory")
_VBrdgTpFdbAddress_Type = MacAddress
_VBrdgTpFdbAddress_Object = MibTableColumn
vBrdgTpFdbAddress = _VBrdgTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 2),
    _VBrdgTpFdbAddress_Type()
)
vBrdgTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbAddress.setStatus("mandatory")
_VBrdgTpFdbRcvPortSlot_Type = Integer32
_VBrdgTpFdbRcvPortSlot_Object = MibTableColumn
vBrdgTpFdbRcvPortSlot = _VBrdgTpFdbRcvPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 3),
    _VBrdgTpFdbRcvPortSlot_Type()
)
vBrdgTpFdbRcvPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbRcvPortSlot.setStatus("mandatory")
_VBrdgTpFdbRcvPortIF_Type = Integer32
_VBrdgTpFdbRcvPortIF_Object = MibTableColumn
vBrdgTpFdbRcvPortIF = _VBrdgTpFdbRcvPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 4),
    _VBrdgTpFdbRcvPortIF_Type()
)
vBrdgTpFdbRcvPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbRcvPortIF.setStatus("mandatory")
_VBrdgTpFdbRcvPortFuncTyp_Type = XylanPortFuncCodes
_VBrdgTpFdbRcvPortFuncTyp_Object = MibTableColumn
vBrdgTpFdbRcvPortFuncTyp = _VBrdgTpFdbRcvPortFuncTyp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 5),
    _VBrdgTpFdbRcvPortFuncTyp_Type()
)
vBrdgTpFdbRcvPortFuncTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbRcvPortFuncTyp.setStatus("mandatory")
_VBrdgTpFdbRcvPortFuncTypInst_Type = Integer32
_VBrdgTpFdbRcvPortFuncTypInst_Object = MibTableColumn
vBrdgTpFdbRcvPortFuncTypInst = _VBrdgTpFdbRcvPortFuncTypInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 6),
    _VBrdgTpFdbRcvPortFuncTypInst_Type()
)
vBrdgTpFdbRcvPortFuncTypInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbRcvPortFuncTypInst.setStatus("mandatory")


class _VBrdgTpFdbRcvStatus_Type(Integer32):
    """Custom type vBrdgTpFdbRcvStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_VBrdgTpFdbRcvStatus_Type.__name__ = "Integer32"
_VBrdgTpFdbRcvStatus_Object = MibTableColumn
vBrdgTpFdbRcvStatus = _VBrdgTpFdbRcvStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 7),
    _VBrdgTpFdbRcvStatus_Type()
)
vBrdgTpFdbRcvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbRcvStatus.setStatus("mandatory")
_VBrdgTpFdbRcvVLANMembership_Type = Integer32
_VBrdgTpFdbRcvVLANMembership_Object = MibTableColumn
vBrdgTpFdbRcvVLANMembership = _VBrdgTpFdbRcvVLANMembership_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 8),
    _VBrdgTpFdbRcvVLANMembership_Type()
)
vBrdgTpFdbRcvVLANMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbRcvVLANMembership.setStatus("mandatory")
_VBrdgTpFdbDupStatus_Type = Integer32
_VBrdgTpFdbDupStatus_Object = MibTableColumn
vBrdgTpFdbDupStatus = _VBrdgTpFdbDupStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 9),
    _VBrdgTpFdbDupStatus_Type()
)
vBrdgTpFdbDupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbDupStatus.setStatus("mandatory")
_VBrdgTpFdbLastSeenTime_Type = Counter32
_VBrdgTpFdbLastSeenTime_Object = MibTableColumn
vBrdgTpFdbLastSeenTime = _VBrdgTpFdbLastSeenTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 3, 1, 10),
    _VBrdgTpFdbLastSeenTime_Type()
)
vBrdgTpFdbLastSeenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vBrdgTpFdbLastSeenTime.setStatus("mandatory")
_VBrdgStaticTable_Object = MibTable
vBrdgStaticTable = _VBrdgStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    vBrdgStaticTable.setStatus("mandatory")
_VBrdgStaticEntry_Object = MibTableRow
vBrdgStaticEntry = _VBrdgStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1)
)
vBrdgStaticEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vBrdgStaticAddress"),
)
if mibBuilder.loadTexts:
    vBrdgStaticEntry.setStatus("mandatory")
_VBrdgStaticAddress_Type = MacAddress
_VBrdgStaticAddress_Object = MibTableColumn
vBrdgStaticAddress = _VBrdgStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1, 1),
    _VBrdgStaticAddress_Type()
)
vBrdgStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgStaticAddress.setStatus("mandatory")
_VBrdgStaticPortSlot_Type = Integer32
_VBrdgStaticPortSlot_Object = MibTableColumn
vBrdgStaticPortSlot = _VBrdgStaticPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1, 2),
    _VBrdgStaticPortSlot_Type()
)
vBrdgStaticPortSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgStaticPortSlot.setStatus("mandatory")
_VBrdgStaticPortIF_Type = Integer32
_VBrdgStaticPortIF_Object = MibTableColumn
vBrdgStaticPortIF = _VBrdgStaticPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1, 3),
    _VBrdgStaticPortIF_Type()
)
vBrdgStaticPortIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgStaticPortIF.setStatus("mandatory")
_VBrdgStaticPortFuncTyp_Type = XylanPortFuncCodes
_VBrdgStaticPortFuncTyp_Object = MibTableColumn
vBrdgStaticPortFuncTyp = _VBrdgStaticPortFuncTyp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1, 4),
    _VBrdgStaticPortFuncTyp_Type()
)
vBrdgStaticPortFuncTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgStaticPortFuncTyp.setStatus("mandatory")
_VBrdgStaticPortFuncTypInst_Type = Integer32
_VBrdgStaticPortFuncTypInst_Object = MibTableColumn
vBrdgStaticPortFuncTypInst = _VBrdgStaticPortFuncTypInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1, 5),
    _VBrdgStaticPortFuncTypInst_Type()
)
vBrdgStaticPortFuncTypInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgStaticPortFuncTypInst.setStatus("mandatory")


class _VBrdgStaticStatus_Type(Integer32):
    """Custom type vBrdgStaticStatus based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_VBrdgStaticStatus_Type.__name__ = "Integer32"
_VBrdgStaticStatus_Object = MibTableColumn
vBrdgStaticStatus = _VBrdgStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 4, 1, 6),
    _VBrdgStaticStatus_Type()
)
vBrdgStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgStaticStatus.setStatus("mandatory")


class _VBrdgTpATVLANAgeingTime_Type(Integer32):
    """Custom type vBrdgTpATVLANAgeingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_VBrdgTpATVLANAgeingTime_Type.__name__ = "Integer32"
_VBrdgTpATVLANAgeingTime_Object = MibScalar
vBrdgTpATVLANAgeingTime = _VBrdgTpATVLANAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 4, 5),
    _VBrdgTpATVLANAgeingTime_Type()
)
vBrdgTpATVLANAgeingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vBrdgTpATVLANAgeingTime.setStatus("mandatory")
_VStpInfo_ObjectIdentity = ObjectIdentity
vStpInfo = _VStpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5)
)


class _VStpProtocolSpecification_Type(Integer32):
    """Custom type vStpProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decLb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_VStpProtocolSpecification_Type.__name__ = "Integer32"
_VStpProtocolSpecification_Object = MibScalar
vStpProtocolSpecification = _VStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 1),
    _VStpProtocolSpecification_Type()
)
vStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpProtocolSpecification.setStatus("mandatory")


class _VStpPriority_Type(Integer32):
    """Custom type vStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VStpPriority_Type.__name__ = "Integer32"
_VStpPriority_Object = MibScalar
vStpPriority = _VStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 2),
    _VStpPriority_Type()
)
vStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpPriority.setStatus("mandatory")
_VStpBridgeAddress_Type = BridgeId
_VStpBridgeAddress_Object = MibScalar
vStpBridgeAddress = _VStpBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 3),
    _VStpBridgeAddress_Type()
)
vStpBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpBridgeAddress.setStatus("mandatory")
_VStpTimeSinceTopologyChange_Type = TimeTicks
_VStpTimeSinceTopologyChange_Object = MibScalar
vStpTimeSinceTopologyChange = _VStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 4),
    _VStpTimeSinceTopologyChange_Type()
)
vStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpTimeSinceTopologyChange.setStatus("mandatory")
_VStpTopChanges_Type = Counter32
_VStpTopChanges_Object = MibScalar
vStpTopChanges = _VStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 5),
    _VStpTopChanges_Type()
)
vStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpTopChanges.setStatus("mandatory")
_VStpDesignatedRoot_Type = BridgeId
_VStpDesignatedRoot_Object = MibScalar
vStpDesignatedRoot = _VStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 6),
    _VStpDesignatedRoot_Type()
)
vStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpDesignatedRoot.setStatus("mandatory")
_VStpRootCost_Type = Integer32
_VStpRootCost_Object = MibScalar
vStpRootCost = _VStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 7),
    _VStpRootCost_Type()
)
vStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpRootCost.setStatus("mandatory")
_VStpRootPortSlot_Type = Integer32
_VStpRootPortSlot_Object = MibScalar
vStpRootPortSlot = _VStpRootPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 8),
    _VStpRootPortSlot_Type()
)
vStpRootPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpRootPortSlot.setStatus("mandatory")
_VStpRootPortIF_Type = Integer32
_VStpRootPortIF_Object = MibScalar
vStpRootPortIF = _VStpRootPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 9),
    _VStpRootPortIF_Type()
)
vStpRootPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpRootPortIF.setStatus("mandatory")
_VStpRootPortFuncTyp_Type = XylanPortFuncCodes
_VStpRootPortFuncTyp_Object = MibScalar
vStpRootPortFuncTyp = _VStpRootPortFuncTyp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 10),
    _VStpRootPortFuncTyp_Type()
)
vStpRootPortFuncTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpRootPortFuncTyp.setStatus("mandatory")
_VStpRootPortFuncTypInst_Type = Integer32
_VStpRootPortFuncTypInst_Object = MibScalar
vStpRootPortFuncTypInst = _VStpRootPortFuncTypInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 11),
    _VStpRootPortFuncTypInst_Type()
)
vStpRootPortFuncTypInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpRootPortFuncTypInst.setStatus("mandatory")
_VStpMaxAge_Type = Timeout
_VStpMaxAge_Object = MibScalar
vStpMaxAge = _VStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 12),
    _VStpMaxAge_Type()
)
vStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpMaxAge.setStatus("mandatory")
_VStpHelloTime_Type = Timeout
_VStpHelloTime_Object = MibScalar
vStpHelloTime = _VStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 13),
    _VStpHelloTime_Type()
)
vStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpHelloTime.setStatus("mandatory")
_VStpHoldTime_Type = Integer32
_VStpHoldTime_Object = MibScalar
vStpHoldTime = _VStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 14),
    _VStpHoldTime_Type()
)
vStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpHoldTime.setStatus("mandatory")
_VStpForwardDelay_Type = Integer32
_VStpForwardDelay_Object = MibScalar
vStpForwardDelay = _VStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 15),
    _VStpForwardDelay_Type()
)
vStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpForwardDelay.setStatus("mandatory")


class _VStpBridgeMaxAge_Type(Timeout):
    """Custom type vStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_VStpBridgeMaxAge_Type.__name__ = "Timeout"
_VStpBridgeMaxAge_Object = MibScalar
vStpBridgeMaxAge = _VStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 16),
    _VStpBridgeMaxAge_Type()
)
vStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgeMaxAge.setStatus("mandatory")


class _VStpBridgeHelloTime_Type(Timeout):
    """Custom type vStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_VStpBridgeHelloTime_Type.__name__ = "Timeout"
_VStpBridgeHelloTime_Object = MibScalar
vStpBridgeHelloTime = _VStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 17),
    _VStpBridgeHelloTime_Type()
)
vStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgeHelloTime.setStatus("mandatory")


class _VStpBridgeForwardDelay_Type(Timeout):
    """Custom type vStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_VStpBridgeForwardDelay_Type.__name__ = "Timeout"
_VStpBridgeForwardDelay_Object = MibScalar
vStpBridgeForwardDelay = _VStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 18),
    _VStpBridgeForwardDelay_Type()
)
vStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpBridgeForwardDelay.setStatus("mandatory")
_VStpPortTable_Object = MibTable
vStpPortTable = _VStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19)
)
if mibBuilder.loadTexts:
    vStpPortTable.setStatus("mandatory")
_VStpPortEntry_Object = MibTableRow
vStpPortEntry = _VStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1)
)
vStpPortEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vStpPortSlot"),
    (0, "XYLAN-VLAN-MIB", "vStpPortIF"),
    (0, "XYLAN-VLAN-MIB", "vStpPortFuncTyp"),
    (0, "XYLAN-VLAN-MIB", "vStpPortFuncTypInst"),
)
if mibBuilder.loadTexts:
    vStpPortEntry.setStatus("mandatory")
_VStpPortSlot_Type = Integer32
_VStpPortSlot_Object = MibTableColumn
vStpPortSlot = _VStpPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 1),
    _VStpPortSlot_Type()
)
vStpPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortSlot.setStatus("mandatory")
_VStpPortIF_Type = Integer32
_VStpPortIF_Object = MibTableColumn
vStpPortIF = _VStpPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 2),
    _VStpPortIF_Type()
)
vStpPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortIF.setStatus("mandatory")
_VStpPortFuncTyp_Type = Integer32
_VStpPortFuncTyp_Object = MibTableColumn
vStpPortFuncTyp = _VStpPortFuncTyp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 3),
    _VStpPortFuncTyp_Type()
)
vStpPortFuncTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortFuncTyp.setStatus("mandatory")
_VStpPortFuncTypInst_Type = Integer32
_VStpPortFuncTypInst_Object = MibTableColumn
vStpPortFuncTypInst = _VStpPortFuncTypInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 4),
    _VStpPortFuncTypInst_Type()
)
vStpPortFuncTypInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortFuncTypInst.setStatus("mandatory")
_VStpPortPriority_Type = Integer32
_VStpPortPriority_Object = MibTableColumn
vStpPortPriority = _VStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 5),
    _VStpPortPriority_Type()
)
vStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpPortPriority.setStatus("mandatory")


class _VStpPortState_Type(Integer32):
    """Custom type vStpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_VStpPortState_Type.__name__ = "Integer32"
_VStpPortState_Object = MibTableColumn
vStpPortState = _VStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 6),
    _VStpPortState_Type()
)
vStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortState.setStatus("mandatory")


class _VStpPortEnable_Type(Integer32):
    """Custom type vStpPortEnable based on Integer32"""
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


_VStpPortEnable_Type.__name__ = "Integer32"
_VStpPortEnable_Object = MibTableColumn
vStpPortEnable = _VStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 7),
    _VStpPortEnable_Type()
)
vStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpPortEnable.setStatus("mandatory")


class _VStpPortPathCost_Type(Integer32):
    """Custom type vStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VStpPortPathCost_Type.__name__ = "Integer32"
_VStpPortPathCost_Object = MibTableColumn
vStpPortPathCost = _VStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 8),
    _VStpPortPathCost_Type()
)
vStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpPortPathCost.setStatus("mandatory")
_VStpPortDesignatedRoot_Type = BridgeId
_VStpPortDesignatedRoot_Object = MibTableColumn
vStpPortDesignatedRoot = _VStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 9),
    _VStpPortDesignatedRoot_Type()
)
vStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedRoot.setStatus("mandatory")
_VStpPortDesignatedCost_Type = Integer32
_VStpPortDesignatedCost_Object = MibTableColumn
vStpPortDesignatedCost = _VStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 10),
    _VStpPortDesignatedCost_Type()
)
vStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedCost.setStatus("mandatory")
_VStpPortDesignatedBridge_Type = BridgeId
_VStpPortDesignatedBridge_Object = MibTableColumn
vStpPortDesignatedBridge = _VStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 11),
    _VStpPortDesignatedBridge_Type()
)
vStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedBridge.setStatus("mandatory")
_VStpPortDesignatedPtPrio_Type = Integer32
_VStpPortDesignatedPtPrio_Object = MibTableColumn
vStpPortDesignatedPtPrio = _VStpPortDesignatedPtPrio_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 12),
    _VStpPortDesignatedPtPrio_Type()
)
vStpPortDesignatedPtPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedPtPrio.setStatus("mandatory")
_VStpPortDesignatedPtSlot_Type = Integer32
_VStpPortDesignatedPtSlot_Object = MibTableColumn
vStpPortDesignatedPtSlot = _VStpPortDesignatedPtSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 13),
    _VStpPortDesignatedPtSlot_Type()
)
vStpPortDesignatedPtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedPtSlot.setStatus("mandatory")
_VStpPortDesignatedPtIF_Type = Integer32
_VStpPortDesignatedPtIF_Object = MibTableColumn
vStpPortDesignatedPtIF = _VStpPortDesignatedPtIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 14),
    _VStpPortDesignatedPtIF_Type()
)
vStpPortDesignatedPtIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedPtIF.setStatus("mandatory")
_VStpPortDesignatedPtFuncTyp_Type = XylanPortFuncCodes
_VStpPortDesignatedPtFuncTyp_Object = MibTableColumn
vStpPortDesignatedPtFuncTyp = _VStpPortDesignatedPtFuncTyp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 15),
    _VStpPortDesignatedPtFuncTyp_Type()
)
vStpPortDesignatedPtFuncTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedPtFuncTyp.setStatus("mandatory")
_VStpPortDesignatedPtFuncTypInst_Type = Integer32
_VStpPortDesignatedPtFuncTypInst_Object = MibTableColumn
vStpPortDesignatedPtFuncTypInst = _VStpPortDesignatedPtFuncTypInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 16),
    _VStpPortDesignatedPtFuncTypInst_Type()
)
vStpPortDesignatedPtFuncTypInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortDesignatedPtFuncTypInst.setStatus("mandatory")
_VStpPortForwardTransitions_Type = Integer32
_VStpPortForwardTransitions_Object = MibTableColumn
vStpPortForwardTransitions = _VStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 19, 1, 17),
    _VStpPortForwardTransitions_Type()
)
vStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vStpPortForwardTransitions.setStatus("mandatory")


class _VStpLanMode_Type(Integer32):
    """Custom type vStpLanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ibm-stap", 2),
          ("ieee-stap", 1))
    )


_VStpLanMode_Type.__name__ = "Integer32"
_VStpLanMode_Object = MibScalar
vStpLanMode = _VStpLanMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 20),
    _VStpLanMode_Type()
)
vStpLanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpLanMode.setStatus("mandatory")
_VStpStatus_Type = XylanVlanOperStatCodes
_VStpStatus_Object = MibScalar
vStpStatus = _VStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 5, 21),
    _VStpStatus_Type()
)
vStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vStpStatus.setStatus("mandatory")
_VRipInfo_ObjectIdentity = ObjectIdentity
vRipInfo = _VRipInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7)
)
_VRipInfoTable_Object = MibTable
vRipInfoTable = _VRipInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vRipInfoTable.setStatus("mandatory")
_VRipInfoEntry_Object = MibTableRow
vRipInfoEntry = _VRipInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1)
)
vRipInfoEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vRipInfovLanNumber"),
)
if mibBuilder.loadTexts:
    vRipInfoEntry.setStatus("mandatory")


class _VRipInfovLanNumber_Type(Integer32):
    """Custom type vRipInfovLanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRipInfovLanNumber_Type.__name__ = "Integer32"
_VRipInfovLanNumber_Object = MibTableColumn
vRipInfovLanNumber = _VRipInfovLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 1),
    _VRipInfovLanNumber_Type()
)
vRipInfovLanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipInfovLanNumber.setStatus("mandatory")
_VRipInPkts_Type = Counter32
_VRipInPkts_Object = MibTableColumn
vRipInPkts = _VRipInPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 2),
    _VRipInPkts_Type()
)
vRipInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipInPkts.setStatus("mandatory")
_VRipOutPkts_Type = Counter32
_VRipOutPkts_Object = MibTableColumn
vRipOutPkts = _VRipOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 3),
    _VRipOutPkts_Type()
)
vRipOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipOutPkts.setStatus("mandatory")
_VRipBadSize_Type = Counter32
_VRipBadSize_Object = MibTableColumn
vRipBadSize = _VRipBadSize_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 4),
    _VRipBadSize_Type()
)
vRipBadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipBadSize.setStatus("mandatory")
_VRipBadVersion_Type = Counter32
_VRipBadVersion_Object = MibTableColumn
vRipBadVersion = _VRipBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 5),
    _VRipBadVersion_Type()
)
vRipBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipBadVersion.setStatus("mandatory")
_VRipNonZero_Type = Counter32
_VRipNonZero_Object = MibTableColumn
vRipNonZero = _VRipNonZero_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 6),
    _VRipNonZero_Type()
)
vRipNonZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipNonZero.setStatus("mandatory")
_VRipBadFamily_Type = Counter32
_VRipBadFamily_Object = MibTableColumn
vRipBadFamily = _VRipBadFamily_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 7),
    _VRipBadFamily_Type()
)
vRipBadFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipBadFamily.setStatus("mandatory")
_VRipBadMetric_Type = Counter32
_VRipBadMetric_Object = MibTableColumn
vRipBadMetric = _VRipBadMetric_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 8),
    _VRipBadMetric_Type()
)
vRipBadMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipBadMetric.setStatus("mandatory")
_VRipBadAddr_Type = Counter32
_VRipBadAddr_Object = MibTableColumn
vRipBadAddr = _VRipBadAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 9),
    _VRipBadAddr_Type()
)
vRipBadAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipBadAddr.setStatus("mandatory")
_VRipBadCommand_Type = Counter32
_VRipBadCommand_Object = MibTableColumn
vRipBadCommand = _VRipBadCommand_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 10),
    _VRipBadCommand_Type()
)
vRipBadCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipBadCommand.setStatus("mandatory")
_VRipTransmitsFailed_Type = Counter32
_VRipTransmitsFailed_Object = MibTableColumn
vRipTransmitsFailed = _VRipTransmitsFailed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 7, 1, 1, 13),
    _VRipTransmitsFailed_Type()
)
vRipTransmitsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRipTransmitsFailed.setStatus("mandatory")
_VSr_ObjectIdentity = ObjectIdentity
vSr = _VSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8)
)
_VSrTable_Object = MibTable
vSrTable = _VSrTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    vSrTable.setStatus("mandatory")
_VSrPortEntry_Object = MibTableRow
vSrPortEntry = _VSrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1)
)
vSrPortEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vSrSlot"),
    (0, "XYLAN-VLAN-MIB", "vSrInterface"),
    (0, "XYLAN-VLAN-MIB", "vSrFuncType"),
    (0, "XYLAN-VLAN-MIB", "vSrInstance"),
)
if mibBuilder.loadTexts:
    vSrPortEntry.setStatus("mandatory")


class _VSrSlot_Type(Integer32):
    """Custom type vSrSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VSrSlot_Type.__name__ = "Integer32"
_VSrSlot_Object = MibTableColumn
vSrSlot = _VSrSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 1),
    _VSrSlot_Type()
)
vSrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrSlot.setStatus("mandatory")


class _VSrInterface_Type(Integer32):
    """Custom type vSrInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VSrInterface_Type.__name__ = "Integer32"
_VSrInterface_Object = MibTableColumn
vSrInterface = _VSrInterface_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 2),
    _VSrInterface_Type()
)
vSrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrInterface.setStatus("mandatory")


class _VSrFuncType_Type(Integer32):
    """Custom type vSrFuncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VSrFuncType_Type.__name__ = "Integer32"
_VSrFuncType_Object = MibTableColumn
vSrFuncType = _VSrFuncType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 3),
    _VSrFuncType_Type()
)
vSrFuncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrFuncType.setStatus("mandatory")


class _VSrInstance_Type(Integer32):
    """Custom type vSrInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_VSrInstance_Type.__name__ = "Integer32"
_VSrInstance_Object = MibTableColumn
vSrInstance = _VSrInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 4),
    _VSrInstance_Type()
)
vSrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrInstance.setStatus("mandatory")
_VSrHopCount_Type = Integer32
_VSrHopCount_Object = MibTableColumn
vSrHopCount = _VSrHopCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 5),
    _VSrHopCount_Type()
)
vSrHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrHopCount.setStatus("mandatory")
_VSrLocalSegment_Type = Integer32
_VSrLocalSegment_Object = MibTableColumn
vSrLocalSegment = _VSrLocalSegment_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 6),
    _VSrLocalSegment_Type()
)
vSrLocalSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrLocalSegment.setStatus("mandatory")
_VSrBridgeNum_Type = Integer32
_VSrBridgeNum_Object = MibTableColumn
vSrBridgeNum = _VSrBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 7),
    _VSrBridgeNum_Type()
)
vSrBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrBridgeNum.setStatus("mandatory")
_VSrVirtualRing_Type = Integer32
_VSrVirtualRing_Object = MibTableColumn
vSrVirtualRing = _VSrVirtualRing_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 8),
    _VSrVirtualRing_Type()
)
vSrVirtualRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrVirtualRing.setStatus("mandatory")
_VSrLargestFrame_Type = Integer32
_VSrLargestFrame_Object = MibTableColumn
vSrLargestFrame = _VSrLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 9),
    _VSrLargestFrame_Type()
)
vSrLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrLargestFrame.setStatus("mandatory")


class _VSrSTESpanMode_Type(Integer32):
    """Custom type vSrSTESpanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-span", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_VSrSTESpanMode_Type.__name__ = "Integer32"
_VSrSTESpanMode_Object = MibTableColumn
vSrSTESpanMode = _VSrSTESpanMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 10),
    _VSrSTESpanMode_Type()
)
vSrSTESpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrSTESpanMode.setStatus("mandatory")
_VSrSpecInFrames_Type = Counter32
_VSrSpecInFrames_Object = MibTableColumn
vSrSpecInFrames = _VSrSpecInFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 11),
    _VSrSpecInFrames_Type()
)
vSrSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrSpecInFrames.setStatus("mandatory")
_VSrSpecOutFrames_Type = Counter32
_VSrSpecOutFrames_Object = MibTableColumn
vSrSpecOutFrames = _VSrSpecOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 12),
    _VSrSpecOutFrames_Type()
)
vSrSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrSpecOutFrames.setStatus("mandatory")
_VSrApeInFrames_Type = Counter32
_VSrApeInFrames_Object = MibTableColumn
vSrApeInFrames = _VSrApeInFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 13),
    _VSrApeInFrames_Type()
)
vSrApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrApeInFrames.setStatus("mandatory")
_VSrApeOutFrames_Type = Counter32
_VSrApeOutFrames_Object = MibTableColumn
vSrApeOutFrames = _VSrApeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 14),
    _VSrApeOutFrames_Type()
)
vSrApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrApeOutFrames.setStatus("mandatory")
_VSrSteInFrames_Type = Counter32
_VSrSteInFrames_Object = MibTableColumn
vSrSteInFrames = _VSrSteInFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 15),
    _VSrSteInFrames_Type()
)
vSrSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrSteInFrames.setStatus("mandatory")
_VSrSteOutFrames_Type = Counter32
_VSrSteOutFrames_Object = MibTableColumn
vSrSteOutFrames = _VSrSteOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 16),
    _VSrSteOutFrames_Type()
)
vSrSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrSteOutFrames.setStatus("mandatory")
_VSrInvalidRif_Type = Counter32
_VSrInvalidRif_Object = MibTableColumn
vSrInvalidRif = _VSrInvalidRif_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 17),
    _VSrInvalidRif_Type()
)
vSrInvalidRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrInvalidRif.setStatus("mandatory")
_VSrDuplicateSegmentDiscards_Type = Counter32
_VSrDuplicateSegmentDiscards_Object = MibTableColumn
vSrDuplicateSegmentDiscards = _VSrDuplicateSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 18),
    _VSrDuplicateSegmentDiscards_Type()
)
vSrDuplicateSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrDuplicateSegmentDiscards.setStatus("mandatory")
_VSrHopCountExceededDiscards_Type = Counter32
_VSrHopCountExceededDiscards_Object = MibTableColumn
vSrHopCountExceededDiscards = _VSrHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 19),
    _VSrHopCountExceededDiscards_Type()
)
vSrHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrHopCountExceededDiscards.setStatus("mandatory")
_VSrDupLanIdOrTreeErrors_Type = Counter32
_VSrDupLanIdOrTreeErrors_Object = MibTableColumn
vSrDupLanIdOrTreeErrors = _VSrDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 20),
    _VSrDupLanIdOrTreeErrors_Type()
)
vSrDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrDupLanIdOrTreeErrors.setStatus("mandatory")
_VSrLanIdMismatches_Type = Counter32
_VSrLanIdMismatches_Object = MibTableColumn
vSrLanIdMismatches = _VSrLanIdMismatches_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 21),
    _VSrLanIdMismatches_Type()
)
vSrLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrLanIdMismatches.setStatus("mandatory")


class _VSrBridgeLfMode_Type(Integer32):
    """Custom type vSrBridgeLfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode3", 1),
          ("mode6", 2))
    )


_VSrBridgeLfMode_Type.__name__ = "Integer32"
_VSrBridgeLfMode_Object = MibTableColumn
vSrBridgeLfMode = _VSrBridgeLfMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 22),
    _VSrBridgeLfMode_Type()
)
vSrBridgeLfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSrBridgeLfMode.setStatus("mandatory")
_VSrPortType_Type = Integer32
_VSrPortType_Object = MibTableColumn
vSrPortType = _VSrPortType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 23),
    _VSrPortType_Type()
)
vSrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrPortType.setStatus("mandatory")
_VSrAREblock_Type = Integer32
_VSrAREblock_Object = MibTableColumn
vSrAREblock = _VSrAREblock_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 24),
    _VSrAREblock_Type()
)
vSrAREblock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrAREblock.setStatus("mandatory")
_VSrHopCountIn_Type = Integer32
_VSrHopCountIn_Object = MibTableColumn
vSrHopCountIn = _VSrHopCountIn_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 25),
    _VSrHopCountIn_Type()
)
vSrHopCountIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrHopCountIn.setStatus("mandatory")
_VSrSapDenyFilter1_Type = Integer32
_VSrSapDenyFilter1_Object = MibTableColumn
vSrSapDenyFilter1 = _VSrSapDenyFilter1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 26),
    _VSrSapDenyFilter1_Type()
)
vSrSapDenyFilter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrSapDenyFilter1.setStatus("mandatory")
_VSrSapDenyFilter2_Type = Integer32
_VSrSapDenyFilter2_Object = MibTableColumn
vSrSapDenyFilter2 = _VSrSapDenyFilter2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 27),
    _VSrSapDenyFilter2_Type()
)
vSrSapDenyFilter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrSapDenyFilter2.setStatus("mandatory")
_VSrSapPermitFilter1_Type = Integer32
_VSrSapPermitFilter1_Object = MibTableColumn
vSrSapPermitFilter1 = _VSrSapPermitFilter1_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 28),
    _VSrSapPermitFilter1_Type()
)
vSrSapPermitFilter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrSapPermitFilter1.setStatus("mandatory")
_VSrSapPermitFilter2_Type = Integer32
_VSrSapPermitFilter2_Object = MibTableColumn
vSrSapPermitFilter2 = _VSrSapPermitFilter2_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 1, 1, 29),
    _VSrSapPermitFilter2_Type()
)
vSrSapPermitFilter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrSapPermitFilter2.setStatus("mandatory")


class _VSrSapFilterEnable_Type(Integer32):
    """Custom type vSrSapFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("turnOffAndClearAll", 3))
    )


_VSrSapFilterEnable_Type.__name__ = "Integer32"
_VSrSapFilterEnable_Object = MibScalar
vSrSapFilterEnable = _VSrSapFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 8, 2),
    _VSrSapFilterEnable_Type()
)
vSrSapFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSrSapFilterEnable.setStatus("mandatory")
_VTrunking_ObjectIdentity = ObjectIdentity
vTrunking = _VTrunking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9)
)
_VTrunkingServicesTable_Object = MibTable
vTrunkingServicesTable = _VTrunkingServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    vTrunkingServicesTable.setStatus("mandatory")
_VTrunkingServicesEntry_Object = MibTableRow
vTrunkingServicesEntry = _VTrunkingServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 1, 1)
)
vTrunkingServicesEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vTrunkingServicesSlot"),
    (0, "XYLAN-VLAN-MIB", "vTrunkingServicesStation"),
)
if mibBuilder.loadTexts:
    vTrunkingServicesEntry.setStatus("mandatory")
_VTrunkingServicesSlot_Type = Integer32
_VTrunkingServicesSlot_Object = MibTableColumn
vTrunkingServicesSlot = _VTrunkingServicesSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 1, 1, 1),
    _VTrunkingServicesSlot_Type()
)
vTrunkingServicesSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTrunkingServicesSlot.setStatus("mandatory")
_VTrunkingServicesStation_Type = Integer32
_VTrunkingServicesStation_Object = MibTableColumn
vTrunkingServicesStation = _VTrunkingServicesStation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 1, 1, 2),
    _VTrunkingServicesStation_Type()
)
vTrunkingServicesStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTrunkingServicesStation.setStatus("mandatory")
_VTrunkingServicesDescription_Type = DisplayString
_VTrunkingServicesDescription_Object = MibTableColumn
vTrunkingServicesDescription = _VTrunkingServicesDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 1, 1, 3),
    _VTrunkingServicesDescription_Type()
)
vTrunkingServicesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTrunkingServicesDescription.setStatus("mandatory")


class _VTrunkingServicesBridgeID_Type(Integer32):
    """Custom type vTrunkingServicesBridgeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VTrunkingServicesBridgeID_Type.__name__ = "Integer32"
_VTrunkingServicesBridgeID_Object = MibTableColumn
vTrunkingServicesBridgeID = _VTrunkingServicesBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 1, 1, 4),
    _VTrunkingServicesBridgeID_Type()
)
vTrunkingServicesBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTrunkingServicesBridgeID.setStatus("mandatory")
_VTrunkingVlanTable_Object = MibTable
vTrunkingVlanTable = _VTrunkingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    vTrunkingVlanTable.setStatus("mandatory")
_VTrunkingVlanEntry_Object = MibTableRow
vTrunkingVlanEntry = _VTrunkingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 2, 1)
)
vTrunkingVlanEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vTrunkingSlot"),
    (0, "XYLAN-VLAN-MIB", "vTrunkingStation"),
    (0, "XYLAN-VLAN-MIB", "vTrunkingLanNumber"),
)
if mibBuilder.loadTexts:
    vTrunkingVlanEntry.setStatus("mandatory")
_VTrunkingSlot_Type = Integer32
_VTrunkingSlot_Object = MibTableColumn
vTrunkingSlot = _VTrunkingSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 2, 1, 1),
    _VTrunkingSlot_Type()
)
vTrunkingSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTrunkingSlot.setStatus("mandatory")
_VTrunkingStation_Type = Integer32
_VTrunkingStation_Object = MibTableColumn
vTrunkingStation = _VTrunkingStation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 2, 1, 2),
    _VTrunkingStation_Type()
)
vTrunkingStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTrunkingStation.setStatus("mandatory")


class _VTrunkingLanNumber_Type(Integer32):
    """Custom type vTrunkingLanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VTrunkingLanNumber_Type.__name__ = "Integer32"
_VTrunkingLanNumber_Object = MibTableColumn
vTrunkingLanNumber = _VTrunkingLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 2, 1, 3),
    _VTrunkingLanNumber_Type()
)
vTrunkingLanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTrunkingLanNumber.setStatus("mandatory")


class _VTrunkingCommand_Type(Integer32):
    """Custom type vTrunkingCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_VTrunkingCommand_Type.__name__ = "Integer32"
_VTrunkingCommand_Object = MibTableColumn
vTrunkingCommand = _VTrunkingCommand_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 9, 2, 1, 4),
    _VTrunkingCommand_Type()
)
vTrunkingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTrunkingCommand.setStatus("mandatory")
_VAutoTracker_ObjectIdentity = ObjectIdentity
vAutoTracker = _VAutoTracker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10)
)
_AtportRuleTable_Object = MibTable
atportRuleTable = _AtportRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    atportRuleTable.setStatus("mandatory")
_AtportRuleEntry_Object = MibTableRow
atportRuleEntry = _AtportRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1, 1)
)
atportRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atportRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atportRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atportRuleIdx"),
    (0, "XYLAN-VLAN-MIB", "atportRulePortId"),
)
if mibBuilder.loadTexts:
    atportRuleEntry.setStatus("mandatory")


class _AtportRuleGroupId_Type(Integer32):
    """Custom type atportRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtportRuleGroupId_Type.__name__ = "Integer32"
_AtportRuleGroupId_Object = MibTableColumn
atportRuleGroupId = _AtportRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1, 1, 1),
    _AtportRuleGroupId_Type()
)
atportRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportRuleGroupId.setStatus("mandatory")


class _AtportRuleVLANId_Type(Integer32):
    """Custom type atportRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtportRuleVLANId_Type.__name__ = "Integer32"
_AtportRuleVLANId_Object = MibTableColumn
atportRuleVLANId = _AtportRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1, 1, 2),
    _AtportRuleVLANId_Type()
)
atportRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportRuleVLANId.setStatus("mandatory")


class _AtportRuleIdx_Type(Integer32):
    """Custom type atportRuleIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtportRuleIdx_Type.__name__ = "Integer32"
_AtportRuleIdx_Object = MibTableColumn
atportRuleIdx = _AtportRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1, 1, 3),
    _AtportRuleIdx_Type()
)
atportRuleIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportRuleIdx.setStatus("mandatory")


class _AtportRulePortId_Type(OctetString):
    """Custom type atportRulePortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AtportRulePortId_Type.__name__ = "OctetString"
_AtportRulePortId_Object = MibTableColumn
atportRulePortId = _AtportRulePortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1, 1, 4),
    _AtportRulePortId_Type()
)
atportRulePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportRulePortId.setStatus("mandatory")


class _AtportRulePortState_Type(Integer32):
    """Custom type atportRulePortState based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtportRulePortState_Type.__name__ = "Integer32"
_AtportRulePortState_Object = MibTableColumn
atportRulePortState = _AtportRulePortState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 1, 1, 5),
    _AtportRulePortState_Type()
)
atportRulePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atportRulePortState.setStatus("mandatory")
_AtMacRuleTable_Object = MibTable
atMacRuleTable = _AtMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    atMacRuleTable.setStatus("mandatory")
_AtMacRuleEntry_Object = MibTableRow
atMacRuleEntry = _AtMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2, 1)
)
atMacRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atMacRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atMacRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atMacRuleIndex"),
    (0, "XYLAN-VLAN-MIB", "atMacRuleMacAddress"),
)
if mibBuilder.loadTexts:
    atMacRuleEntry.setStatus("mandatory")


class _AtMacRuleGroupId_Type(Integer32):
    """Custom type atMacRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtMacRuleGroupId_Type.__name__ = "Integer32"
_AtMacRuleGroupId_Object = MibTableColumn
atMacRuleGroupId = _AtMacRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2, 1, 1),
    _AtMacRuleGroupId_Type()
)
atMacRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMacRuleGroupId.setStatus("mandatory")


class _AtMacRuleVLANId_Type(Integer32):
    """Custom type atMacRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtMacRuleVLANId_Type.__name__ = "Integer32"
_AtMacRuleVLANId_Object = MibTableColumn
atMacRuleVLANId = _AtMacRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2, 1, 2),
    _AtMacRuleVLANId_Type()
)
atMacRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMacRuleVLANId.setStatus("mandatory")


class _AtMacRuleIndex_Type(Integer32):
    """Custom type atMacRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtMacRuleIndex_Type.__name__ = "Integer32"
_AtMacRuleIndex_Object = MibTableColumn
atMacRuleIndex = _AtMacRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2, 1, 3),
    _AtMacRuleIndex_Type()
)
atMacRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMacRuleIndex.setStatus("mandatory")
_AtMacRuleMacAddress_Type = MacAddress
_AtMacRuleMacAddress_Object = MibTableColumn
atMacRuleMacAddress = _AtMacRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2, 1, 4),
    _AtMacRuleMacAddress_Type()
)
atMacRuleMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMacRuleMacAddress.setStatus("mandatory")


class _AtMacRuleMacAddressState_Type(Integer32):
    """Custom type atMacRuleMacAddressState based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtMacRuleMacAddressState_Type.__name__ = "Integer32"
_AtMacRuleMacAddressState_Object = MibTableColumn
atMacRuleMacAddressState = _AtMacRuleMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 2, 1, 5),
    _AtMacRuleMacAddressState_Type()
)
atMacRuleMacAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMacRuleMacAddressState.setStatus("mandatory")
_AtProtoRuleTable_Object = MibTable
atProtoRuleTable = _AtProtoRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3)
)
if mibBuilder.loadTexts:
    atProtoRuleTable.setStatus("mandatory")
_AtProtoRuleEntry_Object = MibTableRow
atProtoRuleEntry = _AtProtoRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3, 1)
)
atProtoRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atProtoRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atProtoRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atProtoRuleIndex"),
)
if mibBuilder.loadTexts:
    atProtoRuleEntry.setStatus("mandatory")


class _AtProtoRuleGroupId_Type(Integer32):
    """Custom type atProtoRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtProtoRuleGroupId_Type.__name__ = "Integer32"
_AtProtoRuleGroupId_Object = MibTableColumn
atProtoRuleGroupId = _AtProtoRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3, 1, 1),
    _AtProtoRuleGroupId_Type()
)
atProtoRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atProtoRuleGroupId.setStatus("mandatory")


class _AtProtoRuleVLANId_Type(Integer32):
    """Custom type atProtoRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtProtoRuleVLANId_Type.__name__ = "Integer32"
_AtProtoRuleVLANId_Object = MibTableColumn
atProtoRuleVLANId = _AtProtoRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3, 1, 2),
    _AtProtoRuleVLANId_Type()
)
atProtoRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atProtoRuleVLANId.setStatus("mandatory")


class _AtProtoRuleIndex_Type(Integer32):
    """Custom type atProtoRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtProtoRuleIndex_Type.__name__ = "Integer32"
_AtProtoRuleIndex_Object = MibTableColumn
atProtoRuleIndex = _AtProtoRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3, 1, 3),
    _AtProtoRuleIndex_Type()
)
atProtoRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atProtoRuleIndex.setStatus("mandatory")


class _AtProtoRule_Type(OctetString):
    """Custom type atProtoRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_AtProtoRule_Type.__name__ = "OctetString"
_AtProtoRule_Object = MibTableColumn
atProtoRule = _AtProtoRule_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3, 1, 4),
    _AtProtoRule_Type()
)
atProtoRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atProtoRule.setStatus("mandatory")


class _AtProtoRuleStatus_Type(Integer32):
    """Custom type atProtoRuleStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtProtoRuleStatus_Type.__name__ = "Integer32"
_AtProtoRuleStatus_Object = MibTableColumn
atProtoRuleStatus = _AtProtoRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 3, 1, 5),
    _AtProtoRuleStatus_Type()
)
atProtoRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atProtoRuleStatus.setStatus("mandatory")
_AtNetRuleTable_Object = MibTable
atNetRuleTable = _AtNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    atNetRuleTable.setStatus("mandatory")
_AtNetRuleEntry_Object = MibTableRow
atNetRuleEntry = _AtNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1)
)
atNetRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atNetRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atNetRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atNetRuleIndex"),
)
if mibBuilder.loadTexts:
    atNetRuleEntry.setStatus("mandatory")


class _AtNetRuleGroupId_Type(Integer32):
    """Custom type atNetRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtNetRuleGroupId_Type.__name__ = "Integer32"
_AtNetRuleGroupId_Object = MibTableColumn
atNetRuleGroupId = _AtNetRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1, 1),
    _AtNetRuleGroupId_Type()
)
atNetRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetRuleGroupId.setStatus("mandatory")


class _AtNetRuleVLANId_Type(Integer32):
    """Custom type atNetRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtNetRuleVLANId_Type.__name__ = "Integer32"
_AtNetRuleVLANId_Object = MibTableColumn
atNetRuleVLANId = _AtNetRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1, 2),
    _AtNetRuleVLANId_Type()
)
atNetRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetRuleVLANId.setStatus("mandatory")


class _AtNetRuleIndex_Type(Integer32):
    """Custom type atNetRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtNetRuleIndex_Type.__name__ = "Integer32"
_AtNetRuleIndex_Object = MibTableColumn
atNetRuleIndex = _AtNetRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1, 3),
    _AtNetRuleIndex_Type()
)
atNetRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetRuleIndex.setStatus("mandatory")


class _AtNetRuleProtocolId_Type(Integer32):
    """Custom type atNetRuleProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 3),
          ("ip", 1),
          ("ipx", 2))
    )


_AtNetRuleProtocolId_Type.__name__ = "Integer32"
_AtNetRuleProtocolId_Object = MibTableColumn
atNetRuleProtocolId = _AtNetRuleProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1, 4),
    _AtNetRuleProtocolId_Type()
)
atNetRuleProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetRuleProtocolId.setStatus("mandatory")
_AtNetRuleNetAddr_Type = OctetString
_AtNetRuleNetAddr_Object = MibTableColumn
atNetRuleNetAddr = _AtNetRuleNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1, 5),
    _AtNetRuleNetAddr_Type()
)
atNetRuleNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetRuleNetAddr.setStatus("mandatory")


class _AtNetRuleStatus_Type(Integer32):
    """Custom type atNetRuleStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtNetRuleStatus_Type.__name__ = "Integer32"
_AtNetRuleStatus_Object = MibTableColumn
atNetRuleStatus = _AtNetRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 4, 1, 6),
    _AtNetRuleStatus_Type()
)
atNetRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetRuleStatus.setStatus("mandatory")
_AtUserRuleTable_Object = MibTable
atUserRuleTable = _AtUserRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5)
)
if mibBuilder.loadTexts:
    atUserRuleTable.setStatus("mandatory")
_AtUserRuleEntry_Object = MibTableRow
atUserRuleEntry = _AtUserRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1)
)
atUserRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atUserRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atUserRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atUserRuleIndex"),
)
if mibBuilder.loadTexts:
    atUserRuleEntry.setStatus("mandatory")


class _AtUserRuleGroupId_Type(Integer32):
    """Custom type atUserRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtUserRuleGroupId_Type.__name__ = "Integer32"
_AtUserRuleGroupId_Object = MibTableColumn
atUserRuleGroupId = _AtUserRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 1),
    _AtUserRuleGroupId_Type()
)
atUserRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleGroupId.setStatus("mandatory")


class _AtUserRuleVLANId_Type(Integer32):
    """Custom type atUserRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtUserRuleVLANId_Type.__name__ = "Integer32"
_AtUserRuleVLANId_Object = MibTableColumn
atUserRuleVLANId = _AtUserRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 2),
    _AtUserRuleVLANId_Type()
)
atUserRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleVLANId.setStatus("mandatory")


class _AtUserRuleIndex_Type(Integer32):
    """Custom type atUserRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtUserRuleIndex_Type.__name__ = "Integer32"
_AtUserRuleIndex_Object = MibTableColumn
atUserRuleIndex = _AtUserRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 3),
    _AtUserRuleIndex_Type()
)
atUserRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleIndex.setStatus("mandatory")


class _AtUserRuleOffset_Type(Integer32):
    """Custom type atUserRuleOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AtUserRuleOffset_Type.__name__ = "Integer32"
_AtUserRuleOffset_Object = MibTableColumn
atUserRuleOffset = _AtUserRuleOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 4),
    _AtUserRuleOffset_Type()
)
atUserRuleOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleOffset.setStatus("mandatory")


class _AtUserRuleValue_Type(OctetString):
    """Custom type atUserRuleValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AtUserRuleValue_Type.__name__ = "OctetString"
_AtUserRuleValue_Object = MibTableColumn
atUserRuleValue = _AtUserRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 5),
    _AtUserRuleValue_Type()
)
atUserRuleValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleValue.setStatus("mandatory")


class _AtUserRuleMask_Type(OctetString):
    """Custom type atUserRuleMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AtUserRuleMask_Type.__name__ = "OctetString"
_AtUserRuleMask_Object = MibTableColumn
atUserRuleMask = _AtUserRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 6),
    _AtUserRuleMask_Type()
)
atUserRuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleMask.setStatus("mandatory")


class _AtUserRuleStatus_Type(Integer32):
    """Custom type atUserRuleStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtUserRuleStatus_Type.__name__ = "Integer32"
_AtUserRuleStatus_Object = MibTableColumn
atUserRuleStatus = _AtUserRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 5, 1, 7),
    _AtUserRuleStatus_Type()
)
atUserRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atUserRuleStatus.setStatus("mandatory")
_AtVLANRuleSumTable_Object = MibTable
atVLANRuleSumTable = _AtVLANRuleSumTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6)
)
if mibBuilder.loadTexts:
    atVLANRuleSumTable.setStatus("mandatory")
_AtVLANRuleSumEntry_Object = MibTableRow
atVLANRuleSumEntry = _AtVLANRuleSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6, 1)
)
atVLANRuleSumEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atVLANRuleSumGroupId"),
    (0, "XYLAN-VLAN-MIB", "atVLANRuleSumVLANId"),
    (0, "XYLAN-VLAN-MIB", "atVLANRuleIndex"),
)
if mibBuilder.loadTexts:
    atVLANRuleSumEntry.setStatus("mandatory")


class _AtVLANRuleSumGroupId_Type(Integer32):
    """Custom type atVLANRuleSumGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtVLANRuleSumGroupId_Type.__name__ = "Integer32"
_AtVLANRuleSumGroupId_Object = MibTableColumn
atVLANRuleSumGroupId = _AtVLANRuleSumGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6, 1, 1),
    _AtVLANRuleSumGroupId_Type()
)
atVLANRuleSumGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVLANRuleSumGroupId.setStatus("mandatory")


class _AtVLANRuleSumVLANId_Type(Integer32):
    """Custom type atVLANRuleSumVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtVLANRuleSumVLANId_Type.__name__ = "Integer32"
_AtVLANRuleSumVLANId_Object = MibTableColumn
atVLANRuleSumVLANId = _AtVLANRuleSumVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6, 1, 2),
    _AtVLANRuleSumVLANId_Type()
)
atVLANRuleSumVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVLANRuleSumVLANId.setStatus("mandatory")
_AtVLANRuleIndex_Type = Integer32
_AtVLANRuleIndex_Object = MibTableColumn
atVLANRuleIndex = _AtVLANRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6, 1, 3),
    _AtVLANRuleIndex_Type()
)
atVLANRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVLANRuleIndex.setStatus("mandatory")
_AtVLANRuleSubIndex_Type = Integer32
_AtVLANRuleSubIndex_Object = MibTableColumn
atVLANRuleSubIndex = _AtVLANRuleSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6, 1, 4),
    _AtVLANRuleSubIndex_Type()
)
atVLANRuleSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVLANRuleSubIndex.setStatus("mandatory")


class _AtVLANRuleType_Type(Integer32):
    """Custom type atVLANRuleType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("binding-rule", 7),
          ("dhcp-mac-rule", 9),
          ("dhcp-port-rule", 8),
          ("mac-rule", 2),
          ("mcast-rule", 6),
          ("network-rule", 4),
          ("port-rule", 1),
          ("protocol-rule", 3),
          ("user-defined-rule", 5))
    )


_AtVLANRuleType_Type.__name__ = "Integer32"
_AtVLANRuleType_Object = MibTableColumn
atVLANRuleType = _AtVLANRuleType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 6, 1, 5),
    _AtVLANRuleType_Type()
)
atVLANRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVLANRuleType.setStatus("mandatory")
_AtVLANControlTable_Object = MibTable
atVLANControlTable = _AtVLANControlTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7)
)
if mibBuilder.loadTexts:
    atVLANControlTable.setStatus("mandatory")
_AtVLANControlEntry_Object = MibTableRow
atVLANControlEntry = _AtVLANControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7, 1)
)
atVLANControlEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atVLANGroupId"),
    (0, "XYLAN-VLAN-MIB", "atVLANId"),
)
if mibBuilder.loadTexts:
    atVLANControlEntry.setStatus("mandatory")
_AtVLANGroupId_Type = Integer32
_AtVLANGroupId_Object = MibTableColumn
atVLANGroupId = _AtVLANGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7, 1, 1),
    _AtVLANGroupId_Type()
)
atVLANGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atVLANGroupId.setStatus("mandatory")
_AtVLANId_Type = Integer32
_AtVLANId_Object = MibTableColumn
atVLANId = _AtVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7, 1, 2),
    _AtVLANId_Type()
)
atVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atVLANId.setStatus("mandatory")


class _AtVLANDesc_Type(DisplayString):
    """Custom type atVLANDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtVLANDesc_Type.__name__ = "DisplayString"
_AtVLANDesc_Object = MibTableColumn
atVLANDesc = _AtVLANDesc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7, 1, 3),
    _AtVLANDesc_Type()
)
atVLANDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atVLANDesc.setStatus("mandatory")


class _AtVLANAdminStatus_Type(Integer32):
    """Custom type atVLANAdminStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtVLANAdminStatus_Type.__name__ = "Integer32"
_AtVLANAdminStatus_Object = MibTableColumn
atVLANAdminStatus = _AtVLANAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7, 1, 4),
    _AtVLANAdminStatus_Type()
)
atVLANAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atVLANAdminStatus.setStatus("mandatory")


class _AtVLANOperStatus_Type(Integer32):
    """Custom type atVLANOperStatus based on Integer32"""
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


_AtVLANOperStatus_Type.__name__ = "Integer32"
_AtVLANOperStatus_Object = MibTableColumn
atVLANOperStatus = _AtVLANOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 7, 1, 5),
    _AtVLANOperStatus_Type()
)
atVLANOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atVLANOperStatus.setStatus("mandatory")


class _AtDefaultVlan_Type(Integer32):
    """Custom type atDefaultVlan based on Integer32"""
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


_AtDefaultVlan_Type.__name__ = "Integer32"
_AtDefaultVlan_Object = MibScalar
atDefaultVlan = _AtDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 8),
    _AtDefaultVlan_Type()
)
atDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDefaultVlan.setStatus("mandatory")
_AtmcportRuleTable_Object = MibTable
atmcportRuleTable = _AtmcportRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9)
)
if mibBuilder.loadTexts:
    atmcportRuleTable.setStatus("mandatory")
_AtmcportRuleEntry_Object = MibTableRow
atmcportRuleEntry = _AtmcportRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9, 1)
)
atmcportRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atmcportRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atmcportRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atmcportRuleIdx"),
    (0, "XYLAN-VLAN-MIB", "atmcportRulePortId"),
)
if mibBuilder.loadTexts:
    atmcportRuleEntry.setStatus("mandatory")


class _AtmcportRuleGroupId_Type(Integer32):
    """Custom type atmcportRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmcportRuleGroupId_Type.__name__ = "Integer32"
_AtmcportRuleGroupId_Object = MibTableColumn
atmcportRuleGroupId = _AtmcportRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9, 1, 1),
    _AtmcportRuleGroupId_Type()
)
atmcportRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcportRuleGroupId.setStatus("mandatory")


class _AtmcportRuleVLANId_Type(Integer32):
    """Custom type atmcportRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtmcportRuleVLANId_Type.__name__ = "Integer32"
_AtmcportRuleVLANId_Object = MibTableColumn
atmcportRuleVLANId = _AtmcportRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9, 1, 2),
    _AtmcportRuleVLANId_Type()
)
atmcportRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcportRuleVLANId.setStatus("mandatory")


class _AtmcportRuleIdx_Type(Integer32):
    """Custom type atmcportRuleIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtmcportRuleIdx_Type.__name__ = "Integer32"
_AtmcportRuleIdx_Object = MibTableColumn
atmcportRuleIdx = _AtmcportRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9, 1, 3),
    _AtmcportRuleIdx_Type()
)
atmcportRuleIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcportRuleIdx.setStatus("mandatory")


class _AtmcportRulePortId_Type(OctetString):
    """Custom type atmcportRulePortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AtmcportRulePortId_Type.__name__ = "OctetString"
_AtmcportRulePortId_Object = MibTableColumn
atmcportRulePortId = _AtmcportRulePortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9, 1, 4),
    _AtmcportRulePortId_Type()
)
atmcportRulePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcportRulePortId.setStatus("mandatory")


class _AtmcportRulePortState_Type(Integer32):
    """Custom type atmcportRulePortState based on Integer32"""
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


_AtmcportRulePortState_Type.__name__ = "Integer32"
_AtmcportRulePortState_Object = MibTableColumn
atmcportRulePortState = _AtmcportRulePortState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 9, 1, 5),
    _AtmcportRulePortState_Type()
)
atmcportRulePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcportRulePortState.setStatus("mandatory")
_AtmcMacRuleTable_Object = MibTable
atmcMacRuleTable = _AtmcMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10)
)
if mibBuilder.loadTexts:
    atmcMacRuleTable.setStatus("mandatory")
_AtmcMacRuleEntry_Object = MibTableRow
atmcMacRuleEntry = _AtmcMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10, 1)
)
atmcMacRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atmcMacRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atmcMacRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atmcMacRuleIndex"),
    (0, "XYLAN-VLAN-MIB", "atmcMacRuleMacAddress"),
)
if mibBuilder.loadTexts:
    atmcMacRuleEntry.setStatus("mandatory")


class _AtmcMacRuleGroupId_Type(Integer32):
    """Custom type atmcMacRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmcMacRuleGroupId_Type.__name__ = "Integer32"
_AtmcMacRuleGroupId_Object = MibTableColumn
atmcMacRuleGroupId = _AtmcMacRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10, 1, 1),
    _AtmcMacRuleGroupId_Type()
)
atmcMacRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcMacRuleGroupId.setStatus("mandatory")


class _AtmcMacRuleVLANId_Type(Integer32):
    """Custom type atmcMacRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtmcMacRuleVLANId_Type.__name__ = "Integer32"
_AtmcMacRuleVLANId_Object = MibTableColumn
atmcMacRuleVLANId = _AtmcMacRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10, 1, 2),
    _AtmcMacRuleVLANId_Type()
)
atmcMacRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcMacRuleVLANId.setStatus("mandatory")


class _AtmcMacRuleIndex_Type(Integer32):
    """Custom type atmcMacRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtmcMacRuleIndex_Type.__name__ = "Integer32"
_AtmcMacRuleIndex_Object = MibTableColumn
atmcMacRuleIndex = _AtmcMacRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10, 1, 3),
    _AtmcMacRuleIndex_Type()
)
atmcMacRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcMacRuleIndex.setStatus("mandatory")
_AtmcMacRuleMacAddress_Type = MacAddress
_AtmcMacRuleMacAddress_Object = MibTableColumn
atmcMacRuleMacAddress = _AtmcMacRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10, 1, 4),
    _AtmcMacRuleMacAddress_Type()
)
atmcMacRuleMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcMacRuleMacAddress.setStatus("mandatory")


class _AtmcMacRuleMacAddressState_Type(Integer32):
    """Custom type atmcMacRuleMacAddressState based on Integer32"""
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


_AtmcMacRuleMacAddressState_Type.__name__ = "Integer32"
_AtmcMacRuleMacAddressState_Object = MibTableColumn
atmcMacRuleMacAddressState = _AtmcMacRuleMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 10, 1, 5),
    _AtmcMacRuleMacAddressState_Type()
)
atmcMacRuleMacAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcMacRuleMacAddressState.setStatus("mandatory")
_AtMcastRuleTable_Object = MibTable
atMcastRuleTable = _AtMcastRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11)
)
if mibBuilder.loadTexts:
    atMcastRuleTable.setStatus("mandatory")
_AtMcastRuleEntry_Object = MibTableRow
atMcastRuleEntry = _AtMcastRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11, 1)
)
atMcastRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atMcastRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atMcastRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atMcastRuleIndex"),
    (0, "XYLAN-VLAN-MIB", "atMcastRuleMacAddress"),
)
if mibBuilder.loadTexts:
    atMcastRuleEntry.setStatus("mandatory")


class _AtMcastRuleGroupId_Type(Integer32):
    """Custom type atMcastRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtMcastRuleGroupId_Type.__name__ = "Integer32"
_AtMcastRuleGroupId_Object = MibTableColumn
atMcastRuleGroupId = _AtMcastRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11, 1, 1),
    _AtMcastRuleGroupId_Type()
)
atMcastRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMcastRuleGroupId.setStatus("mandatory")


class _AtMcastRuleVLANId_Type(Integer32):
    """Custom type atMcastRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AtMcastRuleVLANId_Type.__name__ = "Integer32"
_AtMcastRuleVLANId_Object = MibTableColumn
atMcastRuleVLANId = _AtMcastRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11, 1, 2),
    _AtMcastRuleVLANId_Type()
)
atMcastRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMcastRuleVLANId.setStatus("mandatory")


class _AtMcastRuleIndex_Type(Integer32):
    """Custom type atMcastRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtMcastRuleIndex_Type.__name__ = "Integer32"
_AtMcastRuleIndex_Object = MibTableColumn
atMcastRuleIndex = _AtMcastRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11, 1, 3),
    _AtMcastRuleIndex_Type()
)
atMcastRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMcastRuleIndex.setStatus("mandatory")
_AtMcastRuleMacAddress_Type = MacAddress
_AtMcastRuleMacAddress_Object = MibTableColumn
atMcastRuleMacAddress = _AtMcastRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11, 1, 4),
    _AtMcastRuleMacAddress_Type()
)
atMcastRuleMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMcastRuleMacAddress.setStatus("mandatory")


class _AtMcastRuleMacAddressState_Type(Integer32):
    """Custom type atMcastRuleMacAddressState based on Integer32"""
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
          ("disable", 2),
          ("enable", 1))
    )


_AtMcastRuleMacAddressState_Type.__name__ = "Integer32"
_AtMcastRuleMacAddressState_Object = MibTableColumn
atMcastRuleMacAddressState = _AtMcastRuleMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 11, 1, 5),
    _AtMcastRuleMacAddressState_Type()
)
atMcastRuleMacAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atMcastRuleMacAddressState.setStatus("mandatory")
_AtmcVLANRuleSumTable_Object = MibTable
atmcVLANRuleSumTable = _AtmcVLANRuleSumTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12)
)
if mibBuilder.loadTexts:
    atmcVLANRuleSumTable.setStatus("mandatory")
_AtmcVLANRuleSumEntry_Object = MibTableRow
atmcVLANRuleSumEntry = _AtmcVLANRuleSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12, 1)
)
atmcVLANRuleSumEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atmcVLANRuleSumGroupId"),
    (0, "XYLAN-VLAN-MIB", "atmcVLANRuleSumVLANId"),
    (0, "XYLAN-VLAN-MIB", "atmcVLANRuleIndex"),
)
if mibBuilder.loadTexts:
    atmcVLANRuleSumEntry.setStatus("mandatory")


class _AtmcVLANRuleSumGroupId_Type(Integer32):
    """Custom type atmcVLANRuleSumGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmcVLANRuleSumGroupId_Type.__name__ = "Integer32"
_AtmcVLANRuleSumGroupId_Object = MibTableColumn
atmcVLANRuleSumGroupId = _AtmcVLANRuleSumGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12, 1, 1),
    _AtmcVLANRuleSumGroupId_Type()
)
atmcVLANRuleSumGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmcVLANRuleSumGroupId.setStatus("mandatory")


class _AtmcVLANRuleSumVLANId_Type(Integer32):
    """Custom type atmcVLANRuleSumVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtmcVLANRuleSumVLANId_Type.__name__ = "Integer32"
_AtmcVLANRuleSumVLANId_Object = MibTableColumn
atmcVLANRuleSumVLANId = _AtmcVLANRuleSumVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12, 1, 2),
    _AtmcVLANRuleSumVLANId_Type()
)
atmcVLANRuleSumVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmcVLANRuleSumVLANId.setStatus("mandatory")
_AtmcVLANRuleIndex_Type = Integer32
_AtmcVLANRuleIndex_Object = MibTableColumn
atmcVLANRuleIndex = _AtmcVLANRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12, 1, 3),
    _AtmcVLANRuleIndex_Type()
)
atmcVLANRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmcVLANRuleIndex.setStatus("mandatory")
_AtmcVLANRuleSubIndex_Type = Integer32
_AtmcVLANRuleSubIndex_Object = MibTableColumn
atmcVLANRuleSubIndex = _AtmcVLANRuleSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12, 1, 4),
    _AtmcVLANRuleSubIndex_Type()
)
atmcVLANRuleSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmcVLANRuleSubIndex.setStatus("mandatory")


class _AtmcVLANRuleType_Type(Integer32):
    """Custom type atmcVLANRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac-rule", 2),
          ("mcast-rule", 3),
          ("port-rule", 1))
    )


_AtmcVLANRuleType_Type.__name__ = "Integer32"
_AtmcVLANRuleType_Object = MibTableColumn
atmcVLANRuleType = _AtmcVLANRuleType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 12, 1, 5),
    _AtmcVLANRuleType_Type()
)
atmcVLANRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmcVLANRuleType.setStatus("mandatory")
_AtmcVLANControlTable_Object = MibTable
atmcVLANControlTable = _AtmcVLANControlTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13)
)
if mibBuilder.loadTexts:
    atmcVLANControlTable.setStatus("mandatory")
_AtmcVLANControlEntry_Object = MibTableRow
atmcVLANControlEntry = _AtmcVLANControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13, 1)
)
atmcVLANControlEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atmcVLANGroupId"),
    (0, "XYLAN-VLAN-MIB", "atmcVLANId"),
)
if mibBuilder.loadTexts:
    atmcVLANControlEntry.setStatus("mandatory")
_AtmcVLANGroupId_Type = Integer32
_AtmcVLANGroupId_Object = MibTableColumn
atmcVLANGroupId = _AtmcVLANGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13, 1, 1),
    _AtmcVLANGroupId_Type()
)
atmcVLANGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcVLANGroupId.setStatus("mandatory")
_AtmcVLANId_Type = Integer32
_AtmcVLANId_Object = MibTableColumn
atmcVLANId = _AtmcVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13, 1, 2),
    _AtmcVLANId_Type()
)
atmcVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcVLANId.setStatus("mandatory")


class _AtmcVLANDesc_Type(DisplayString):
    """Custom type atmcVLANDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtmcVLANDesc_Type.__name__ = "DisplayString"
_AtmcVLANDesc_Object = MibTableColumn
atmcVLANDesc = _AtmcVLANDesc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13, 1, 3),
    _AtmcVLANDesc_Type()
)
atmcVLANDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcVLANDesc.setStatus("mandatory")


class _AtmcVLANAdminStatus_Type(Integer32):
    """Custom type atmcVLANAdminStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 1))
    )


_AtmcVLANAdminStatus_Type.__name__ = "Integer32"
_AtmcVLANAdminStatus_Object = MibTableColumn
atmcVLANAdminStatus = _AtmcVLANAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13, 1, 4),
    _AtmcVLANAdminStatus_Type()
)
atmcVLANAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmcVLANAdminStatus.setStatus("mandatory")


class _AtmcVLANOperStatus_Type(Integer32):
    """Custom type atmcVLANOperStatus based on Integer32"""
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


_AtmcVLANOperStatus_Type.__name__ = "Integer32"
_AtmcVLANOperStatus_Object = MibTableColumn
atmcVLANOperStatus = _AtmcVLANOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 13, 1, 5),
    _AtmcVLANOperStatus_Type()
)
atmcVLANOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmcVLANOperStatus.setStatus("mandatory")
_GmAutoServiceTable_Object = MibTable
gmAutoServiceTable = _GmAutoServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14)
)
if mibBuilder.loadTexts:
    gmAutoServiceTable.setStatus("mandatory")
_GmAutoServiceEntry_Object = MibTableRow
gmAutoServiceEntry = _GmAutoServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1)
)
gmAutoServiceEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "gmAutoServiceGroupId"),
    (0, "XYLAN-VLAN-MIB", "gmAutoServicePrimarySlot"),
    (0, "XYLAN-VLAN-MIB", "gmAutoServicePrimaryPort"),
    (0, "XYLAN-VLAN-MIB", "gmAutoServiceIndex"),
)
if mibBuilder.loadTexts:
    gmAutoServiceEntry.setStatus("mandatory")
_GmAutoServiceGroupId_Type = Integer32
_GmAutoServiceGroupId_Object = MibTableColumn
gmAutoServiceGroupId = _GmAutoServiceGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 1),
    _GmAutoServiceGroupId_Type()
)
gmAutoServiceGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceGroupId.setStatus("mandatory")
_GmAutoServicePrimarySlot_Type = Integer32
_GmAutoServicePrimarySlot_Object = MibTableColumn
gmAutoServicePrimarySlot = _GmAutoServicePrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 2),
    _GmAutoServicePrimarySlot_Type()
)
gmAutoServicePrimarySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServicePrimarySlot.setStatus("mandatory")
_GmAutoServicePrimaryPort_Type = Integer32
_GmAutoServicePrimaryPort_Object = MibTableColumn
gmAutoServicePrimaryPort = _GmAutoServicePrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 3),
    _GmAutoServicePrimaryPort_Type()
)
gmAutoServicePrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServicePrimaryPort.setStatus("mandatory")
_GmAutoServiceIndex_Type = Integer32
_GmAutoServiceIndex_Object = MibTableColumn
gmAutoServiceIndex = _GmAutoServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 4),
    _GmAutoServiceIndex_Type()
)
gmAutoServiceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceIndex.setStatus("mandatory")


class _GmAutoServiceType_Type(Integer32):
    """Custom type gmAutoServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth-lane", 1),
          ("token-ring-lane", 2))
    )


_GmAutoServiceType_Type.__name__ = "Integer32"
_GmAutoServiceType_Object = MibTableColumn
gmAutoServiceType = _GmAutoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 5),
    _GmAutoServiceType_Type()
)
gmAutoServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceType.setStatus("mandatory")
_GmAutoServiceName_Type = DisplayString
_GmAutoServiceName_Object = MibTableColumn
gmAutoServiceName = _GmAutoServiceName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 6),
    _GmAutoServiceName_Type()
)
gmAutoServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceName.setStatus("mandatory")
_GmAutoServiceSecondarySlot_Type = Integer32
_GmAutoServiceSecondarySlot_Object = MibTableColumn
gmAutoServiceSecondarySlot = _GmAutoServiceSecondarySlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 7),
    _GmAutoServiceSecondarySlot_Type()
)
gmAutoServiceSecondarySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceSecondarySlot.setStatus("mandatory")
_GmAutoServiceSecondaryPort_Type = Integer32
_GmAutoServiceSecondaryPort_Object = MibTableColumn
gmAutoServiceSecondaryPort = _GmAutoServiceSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 8),
    _GmAutoServiceSecondaryPort_Type()
)
gmAutoServiceSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceSecondaryPort.setStatus("mandatory")


class _GmAutoServiceAdminState_Type(Integer32):
    """Custom type gmAutoServiceAdminState based on Integer32"""
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
          ("disable", 2),
          ("enable", 1))
    )


_GmAutoServiceAdminState_Type.__name__ = "Integer32"
_GmAutoServiceAdminState_Object = MibTableColumn
gmAutoServiceAdminState = _GmAutoServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 9),
    _GmAutoServiceAdminState_Type()
)
gmAutoServiceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceAdminState.setStatus("mandatory")


class _GmAutoServiceOperState_Type(Integer32):
    """Custom type gmAutoServiceOperState based on Integer32"""
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


_GmAutoServiceOperState_Type.__name__ = "Integer32"
_GmAutoServiceOperState_Object = MibTableColumn
gmAutoServiceOperState = _GmAutoServiceOperState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 10),
    _GmAutoServiceOperState_Type()
)
gmAutoServiceOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceOperState.setStatus("mandatory")
_GmAutoServiceActiveSlot_Type = Integer32
_GmAutoServiceActiveSlot_Object = MibTableColumn
gmAutoServiceActiveSlot = _GmAutoServiceActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 11),
    _GmAutoServiceActiveSlot_Type()
)
gmAutoServiceActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmAutoServiceActiveSlot.setStatus("mandatory")
_GmAutoServiceActivePort_Type = Integer32
_GmAutoServiceActivePort_Object = MibTableColumn
gmAutoServiceActivePort = _GmAutoServiceActivePort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 12),
    _GmAutoServiceActivePort_Type()
)
gmAutoServiceActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmAutoServiceActivePort.setStatus("mandatory")
_GmAutoServiceNumber_Type = Integer32
_GmAutoServiceNumber_Object = MibTableColumn
gmAutoServiceNumber = _GmAutoServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 13),
    _GmAutoServiceNumber_Type()
)
gmAutoServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmAutoServiceNumber.setStatus("mandatory")


class _GmAutoServiceTranslations_Type(Integer32):
    """Custom type gmAutoServiceTranslations based on Integer32"""
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


_GmAutoServiceTranslations_Type.__name__ = "Integer32"
_GmAutoServiceTranslations_Object = MibTableColumn
gmAutoServiceTranslations = _GmAutoServiceTranslations_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 14, 1, 14),
    _GmAutoServiceTranslations_Type()
)
gmAutoServiceTranslations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmAutoServiceTranslations.setStatus("mandatory")
_AtBindRuleTable_Object = MibTable
atBindRuleTable = _AtBindRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16)
)
if mibBuilder.loadTexts:
    atBindRuleTable.setStatus("mandatory")
_AtBindRuleEntry_Object = MibTableRow
atBindRuleEntry = _AtBindRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1)
)
atBindRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atBindRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atBindRuleVlanId"),
    (0, "XYLAN-VLAN-MIB", "atBindRuleIndex"),
)
if mibBuilder.loadTexts:
    atBindRuleEntry.setStatus("mandatory")
_AtBindRuleGroupId_Type = Integer32
_AtBindRuleGroupId_Object = MibTableColumn
atBindRuleGroupId = _AtBindRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 1),
    _AtBindRuleGroupId_Type()
)
atBindRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleGroupId.setStatus("mandatory")
_AtBindRuleVlanId_Type = Integer32
_AtBindRuleVlanId_Object = MibTableColumn
atBindRuleVlanId = _AtBindRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 2),
    _AtBindRuleVlanId_Type()
)
atBindRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleVlanId.setStatus("mandatory")
_AtBindRuleIndex_Type = Integer32
_AtBindRuleIndex_Object = MibTableColumn
atBindRuleIndex = _AtBindRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 3),
    _AtBindRuleIndex_Type()
)
atBindRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleIndex.setStatus("mandatory")


class _AtBindRulePortId_Type(OctetString):
    """Custom type atBindRulePortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AtBindRulePortId_Type.__name__ = "OctetString"
_AtBindRulePortId_Object = MibTableColumn
atBindRulePortId = _AtBindRulePortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 4),
    _AtBindRulePortId_Type()
)
atBindRulePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRulePortId.setStatus("mandatory")
_AtBindRuleIPAddress_Type = IpAddress
_AtBindRuleIPAddress_Object = MibTableColumn
atBindRuleIPAddress = _AtBindRuleIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 5),
    _AtBindRuleIPAddress_Type()
)
atBindRuleIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleIPAddress.setStatus("mandatory")
_AtBindRuleMacAddress_Type = MacAddress
_AtBindRuleMacAddress_Object = MibTableColumn
atBindRuleMacAddress = _AtBindRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 6),
    _AtBindRuleMacAddress_Type()
)
atBindRuleMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleMacAddress.setStatus("mandatory")
_AtBindRuleProtocol_Type = OctetString
_AtBindRuleProtocol_Object = MibTableColumn
atBindRuleProtocol = _AtBindRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 7),
    _AtBindRuleProtocol_Type()
)
atBindRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleProtocol.setStatus("mandatory")


class _AtBindRuleBindParameter_Type(Integer32):
    """Custom type atBindRuleBindParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              9,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ip-mac", 6),
          ("ip-port", 3),
          ("mac-port", 5),
          ("port-ip-mac", 7),
          ("port-mac-protocol", 13),
          ("port-protocol", 9))
    )


_AtBindRuleBindParameter_Type.__name__ = "Integer32"
_AtBindRuleBindParameter_Object = MibTableColumn
atBindRuleBindParameter = _AtBindRuleBindParameter_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 8),
    _AtBindRuleBindParameter_Type()
)
atBindRuleBindParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleBindParameter.setStatus("mandatory")


class _AtBindRuleStatus_Type(Integer32):
    """Custom type atBindRuleStatus based on Integer32"""
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
          ("disable", 2),
          ("enable", 1))
    )


_AtBindRuleStatus_Type.__name__ = "Integer32"
_AtBindRuleStatus_Object = MibTableColumn
atBindRuleStatus = _AtBindRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 16, 1, 9),
    _AtBindRuleStatus_Type()
)
atBindRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atBindRuleStatus.setStatus("mandatory")
_GmGroupListTable_Object = MibTable
gmGroupListTable = _GmGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 17)
)
if mibBuilder.loadTexts:
    gmGroupListTable.setStatus("mandatory")
_GmGroupListEntry_Object = MibTableRow
gmGroupListEntry = _GmGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 17, 1)
)
gmGroupListEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "gmGroupListPortSlot"),
    (0, "XYLAN-VLAN-MIB", "gmGroupListPortInterface"),
    (0, "XYLAN-VLAN-MIB", "gmGroupListGroupId"),
)
if mibBuilder.loadTexts:
    gmGroupListEntry.setStatus("mandatory")
_GmGroupListPortSlot_Type = Integer32
_GmGroupListPortSlot_Object = MibTableColumn
gmGroupListPortSlot = _GmGroupListPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 17, 1, 1),
    _GmGroupListPortSlot_Type()
)
gmGroupListPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmGroupListPortSlot.setStatus("mandatory")
_GmGroupListPortInterface_Type = Integer32
_GmGroupListPortInterface_Object = MibTableColumn
gmGroupListPortInterface = _GmGroupListPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 17, 1, 2),
    _GmGroupListPortInterface_Type()
)
gmGroupListPortInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmGroupListPortInterface.setStatus("mandatory")
_GmGroupListGroupId_Type = Integer32
_GmGroupListGroupId_Object = MibTableColumn
gmGroupListGroupId = _GmGroupListGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 17, 1, 3),
    _GmGroupListGroupId_Type()
)
gmGroupListGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmGroupListGroupId.setStatus("mandatory")
_AtDHCPportRuleTable_Object = MibTable
atDHCPportRuleTable = _AtDHCPportRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18)
)
if mibBuilder.loadTexts:
    atDHCPportRuleTable.setStatus("mandatory")
_AtDHCPportRuleEntry_Object = MibTableRow
atDHCPportRuleEntry = _AtDHCPportRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18, 1)
)
atDHCPportRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atDHCPportRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atDHCPportRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atDHCPportRuleIdx"),
    (0, "XYLAN-VLAN-MIB", "atDHCPportRulePortId"),
)
if mibBuilder.loadTexts:
    atDHCPportRuleEntry.setStatus("mandatory")


class _AtDHCPportRuleGroupId_Type(Integer32):
    """Custom type atDHCPportRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtDHCPportRuleGroupId_Type.__name__ = "Integer32"
_AtDHCPportRuleGroupId_Object = MibTableColumn
atDHCPportRuleGroupId = _AtDHCPportRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18, 1, 1),
    _AtDHCPportRuleGroupId_Type()
)
atDHCPportRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPportRuleGroupId.setStatus("mandatory")


class _AtDHCPportRuleVLANId_Type(Integer32):
    """Custom type atDHCPportRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtDHCPportRuleVLANId_Type.__name__ = "Integer32"
_AtDHCPportRuleVLANId_Object = MibTableColumn
atDHCPportRuleVLANId = _AtDHCPportRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18, 1, 2),
    _AtDHCPportRuleVLANId_Type()
)
atDHCPportRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPportRuleVLANId.setStatus("mandatory")


class _AtDHCPportRuleIdx_Type(Integer32):
    """Custom type atDHCPportRuleIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtDHCPportRuleIdx_Type.__name__ = "Integer32"
_AtDHCPportRuleIdx_Object = MibTableColumn
atDHCPportRuleIdx = _AtDHCPportRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18, 1, 3),
    _AtDHCPportRuleIdx_Type()
)
atDHCPportRuleIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPportRuleIdx.setStatus("mandatory")


class _AtDHCPportRulePortId_Type(OctetString):
    """Custom type atDHCPportRulePortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AtDHCPportRulePortId_Type.__name__ = "OctetString"
_AtDHCPportRulePortId_Object = MibTableColumn
atDHCPportRulePortId = _AtDHCPportRulePortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18, 1, 4),
    _AtDHCPportRulePortId_Type()
)
atDHCPportRulePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPportRulePortId.setStatus("mandatory")


class _AtDHCPportRulePortState_Type(Integer32):
    """Custom type atDHCPportRulePortState based on Integer32"""
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


_AtDHCPportRulePortState_Type.__name__ = "Integer32"
_AtDHCPportRulePortState_Object = MibTableColumn
atDHCPportRulePortState = _AtDHCPportRulePortState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 18, 1, 5),
    _AtDHCPportRulePortState_Type()
)
atDHCPportRulePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPportRulePortState.setStatus("mandatory")
_AtDHCPMacRuleTable_Object = MibTable
atDHCPMacRuleTable = _AtDHCPMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19)
)
if mibBuilder.loadTexts:
    atDHCPMacRuleTable.setStatus("mandatory")
_AtDHCPMacRuleEntry_Object = MibTableRow
atDHCPMacRuleEntry = _AtDHCPMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19, 1)
)
atDHCPMacRuleEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atDHCPMacRuleGroupId"),
    (0, "XYLAN-VLAN-MIB", "atDHCPMacRuleVLANId"),
    (0, "XYLAN-VLAN-MIB", "atDHCPMacRuleIndex"),
    (0, "XYLAN-VLAN-MIB", "atDHCPMacRuleMacAddress"),
)
if mibBuilder.loadTexts:
    atDHCPMacRuleEntry.setStatus("mandatory")


class _AtDHCPMacRuleGroupId_Type(Integer32):
    """Custom type atDHCPMacRuleGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtDHCPMacRuleGroupId_Type.__name__ = "Integer32"
_AtDHCPMacRuleGroupId_Object = MibTableColumn
atDHCPMacRuleGroupId = _AtDHCPMacRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19, 1, 1),
    _AtDHCPMacRuleGroupId_Type()
)
atDHCPMacRuleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPMacRuleGroupId.setStatus("mandatory")


class _AtDHCPMacRuleVLANId_Type(Integer32):
    """Custom type atDHCPMacRuleVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtDHCPMacRuleVLANId_Type.__name__ = "Integer32"
_AtDHCPMacRuleVLANId_Object = MibTableColumn
atDHCPMacRuleVLANId = _AtDHCPMacRuleVLANId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19, 1, 2),
    _AtDHCPMacRuleVLANId_Type()
)
atDHCPMacRuleVLANId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPMacRuleVLANId.setStatus("mandatory")


class _AtDHCPMacRuleIndex_Type(Integer32):
    """Custom type atDHCPMacRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AtDHCPMacRuleIndex_Type.__name__ = "Integer32"
_AtDHCPMacRuleIndex_Object = MibTableColumn
atDHCPMacRuleIndex = _AtDHCPMacRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19, 1, 3),
    _AtDHCPMacRuleIndex_Type()
)
atDHCPMacRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPMacRuleIndex.setStatus("mandatory")
_AtDHCPMacRuleMacAddress_Type = MacAddress
_AtDHCPMacRuleMacAddress_Object = MibTableColumn
atDHCPMacRuleMacAddress = _AtDHCPMacRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19, 1, 4),
    _AtDHCPMacRuleMacAddress_Type()
)
atDHCPMacRuleMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPMacRuleMacAddress.setStatus("mandatory")


class _AtDHCPMacRuleMacAddressState_Type(Integer32):
    """Custom type atDHCPMacRuleMacAddressState based on Integer32"""
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


_AtDHCPMacRuleMacAddressState_Type.__name__ = "Integer32"
_AtDHCPMacRuleMacAddressState_Object = MibTableColumn
atDHCPMacRuleMacAddressState = _AtDHCPMacRuleMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 19, 1, 5),
    _AtDHCPMacRuleMacAddressState_Type()
)
atDHCPMacRuleMacAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDHCPMacRuleMacAddressState.setStatus("mandatory")


class _GroupMobilityStatus_Type(Integer32):
    """Custom type groupMobilityStatus based on Integer32"""
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


_GroupMobilityStatus_Type.__name__ = "Integer32"
_GroupMobilityStatus_Object = MibScalar
groupMobilityStatus = _GroupMobilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 20),
    _GroupMobilityStatus_Type()
)
groupMobilityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupMobilityStatus.setStatus("mandatory")


class _GmMoveToDefGroup_Type(Integer32):
    """Custom type gmMoveToDefGroup based on Integer32"""
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


_GmMoveToDefGroup_Type.__name__ = "Integer32"
_GmMoveToDefGroup_Object = MibScalar
gmMoveToDefGroup = _GmMoveToDefGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 21),
    _GmMoveToDefGroup_Type()
)
gmMoveToDefGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmMoveToDefGroup.setStatus("mandatory")


class _GmDefGroup_Type(Integer32):
    """Custom type gmDefGroup based on Integer32"""
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


_GmDefGroup_Type.__name__ = "Integer32"
_GmDefGroup_Object = MibScalar
gmDefGroup = _GmDefGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 10, 22),
    _GmDefGroup_Type()
)
gmDefGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmDefGroup.setStatus("mandatory")
_AtvIPRouterInfo_ObjectIdentity = ObjectIdentity
atvIPRouterInfo = _AtvIPRouterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11)
)
_AtvIPRouterTable_Object = MibTable
atvIPRouterTable = _AtvIPRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    atvIPRouterTable.setStatus("mandatory")
_AtvIPRouterEntry_Object = MibTableRow
atvIPRouterEntry = _AtvIPRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1)
)
atvIPRouterEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atvIPRouterVLanGroup"),
    (0, "XYLAN-VLAN-MIB", "atvIPRouterVLan"),
)
if mibBuilder.loadTexts:
    atvIPRouterEntry.setStatus("mandatory")


class _AtvIPRouterVLanGroup_Type(Integer32):
    """Custom type atvIPRouterVLanGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtvIPRouterVLanGroup_Type.__name__ = "Integer32"
_AtvIPRouterVLanGroup_Object = MibTableColumn
atvIPRouterVLanGroup = _AtvIPRouterVLanGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 1),
    _AtvIPRouterVLanGroup_Type()
)
atvIPRouterVLanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterVLanGroup.setStatus("mandatory")


class _AtvIPRouterVLan_Type(Integer32):
    """Custom type atvIPRouterVLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtvIPRouterVLan_Type.__name__ = "Integer32"
_AtvIPRouterVLan_Object = MibTableColumn
atvIPRouterVLan = _AtvIPRouterVLan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 2),
    _AtvIPRouterVLan_Type()
)
atvIPRouterVLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterVLan.setStatus("mandatory")


class _AtvIPRouterProtocol_Type(OctetString):
    """Custom type atvIPRouterProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AtvIPRouterProtocol_Type.__name__ = "OctetString"
_AtvIPRouterProtocol_Object = MibTableColumn
atvIPRouterProtocol = _AtvIPRouterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 3),
    _AtvIPRouterProtocol_Type()
)
atvIPRouterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterProtocol.setStatus("mandatory")
_AtvIPRouterNetAddress_Type = IpAddress
_AtvIPRouterNetAddress_Object = MibTableColumn
atvIPRouterNetAddress = _AtvIPRouterNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 4),
    _AtvIPRouterNetAddress_Type()
)
atvIPRouterNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterNetAddress.setStatus("mandatory")
_AtvIPRouterSubNetMask_Type = IpAddress
_AtvIPRouterSubNetMask_Object = MibTableColumn
atvIPRouterSubNetMask = _AtvIPRouterSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 5),
    _AtvIPRouterSubNetMask_Type()
)
atvIPRouterSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterSubNetMask.setStatus("mandatory")
_AtvIPRouterBcastAddress_Type = IpAddress
_AtvIPRouterBcastAddress_Object = MibTableColumn
atvIPRouterBcastAddress = _AtvIPRouterBcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 6),
    _AtvIPRouterBcastAddress_Type()
)
atvIPRouterBcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterBcastAddress.setStatus("mandatory")


class _AtvIPRouterDescription_Type(DisplayString):
    """Custom type atvIPRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtvIPRouterDescription_Type.__name__ = "DisplayString"
_AtvIPRouterDescription_Object = MibTableColumn
atvIPRouterDescription = _AtvIPRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 7),
    _AtvIPRouterDescription_Type()
)
atvIPRouterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterDescription.setStatus("optional")
_AtvIPRouterAdmStatus_Type = XylanVlanAdminStatCodes
_AtvIPRouterAdmStatus_Object = MibTableColumn
atvIPRouterAdmStatus = _AtvIPRouterAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 8),
    _AtvIPRouterAdmStatus_Type()
)
atvIPRouterAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterAdmStatus.setStatus("mandatory")
_AtvIPRouterOperStatus_Type = XylanVlanOperStatCodes
_AtvIPRouterOperStatus_Object = MibTableColumn
atvIPRouterOperStatus = _AtvIPRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 9),
    _AtvIPRouterOperStatus_Type()
)
atvIPRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atvIPRouterOperStatus.setStatus("mandatory")


class _AtvIPRouterFramingType_Type(Integer32):
    """Custom type atvIPRouterFramingType based on Integer32"""
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
        *(("ethernet-2", 1),
          ("ethernet-802-3", 2),
          ("fddi", 3),
          ("token-ring", 4),
          ("token-ring-source-routed", 5))
    )


_AtvIPRouterFramingType_Type.__name__ = "Integer32"
_AtvIPRouterFramingType_Object = MibTableColumn
atvIPRouterFramingType = _AtvIPRouterFramingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 10),
    _AtvIPRouterFramingType_Type()
)
atvIPRouterFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterFramingType.setStatus("mandatory")


class _AtvIPRouterRipConfigMode_Type(Integer32):
    """Custom type atvIPRouterRipConfigMode based on Integer32"""
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
        *(("active", 3),
          ("deaf", 2),
          ("inactive", 4),
          ("silent", 1))
    )


_AtvIPRouterRipConfigMode_Type.__name__ = "Integer32"
_AtvIPRouterRipConfigMode_Object = MibTableColumn
atvIPRouterRipConfigMode = _AtvIPRouterRipConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 11),
    _AtvIPRouterRipConfigMode_Type()
)
atvIPRouterRipConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterRipConfigMode.setStatus("mandatory")


class _AtvIPRouterRelayServicesFwd_Type(Integer32):
    """Custom type atvIPRouterRelayServicesFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtvIPRouterRelayServicesFwd_Type.__name__ = "Integer32"
_AtvIPRouterRelayServicesFwd_Object = MibTableColumn
atvIPRouterRelayServicesFwd = _AtvIPRouterRelayServicesFwd_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 11, 1, 1, 12),
    _AtvIPRouterRelayServicesFwd_Type()
)
atvIPRouterRelayServicesFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPRouterRelayServicesFwd.setStatus("mandatory")
_AtvIPXRouterInfo_ObjectIdentity = ObjectIdentity
atvIPXRouterInfo = _AtvIPXRouterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12)
)
_AtvIPXRouterTable_Object = MibTable
atvIPXRouterTable = _AtvIPXRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    atvIPXRouterTable.setStatus("mandatory")
_AtvIPXRouterEntry_Object = MibTableRow
atvIPXRouterEntry = _AtvIPXRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1)
)
atvIPXRouterEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "atvIPXRouterVLanGroup"),
    (0, "XYLAN-VLAN-MIB", "atvIPXRouterVLan"),
)
if mibBuilder.loadTexts:
    atvIPXRouterEntry.setStatus("mandatory")


class _AtvIPXRouterVLanGroup_Type(Integer32):
    """Custom type atvIPXRouterVLanGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtvIPXRouterVLanGroup_Type.__name__ = "Integer32"
_AtvIPXRouterVLanGroup_Object = MibTableColumn
atvIPXRouterVLanGroup = _AtvIPXRouterVLanGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 1),
    _AtvIPXRouterVLanGroup_Type()
)
atvIPXRouterVLanGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterVLanGroup.setStatus("mandatory")


class _AtvIPXRouterVLan_Type(Integer32):
    """Custom type atvIPXRouterVLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AtvIPXRouterVLan_Type.__name__ = "Integer32"
_AtvIPXRouterVLan_Object = MibTableColumn
atvIPXRouterVLan = _AtvIPXRouterVLan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 2),
    _AtvIPXRouterVLan_Type()
)
atvIPXRouterVLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterVLan.setStatus("mandatory")
_AtvIPXRouterProtocol_Type = Integer32
_AtvIPXRouterProtocol_Object = MibTableColumn
atvIPXRouterProtocol = _AtvIPXRouterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 3),
    _AtvIPXRouterProtocol_Type()
)
atvIPXRouterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterProtocol.setStatus("mandatory")
_AtvIPXRouterNetAddress_Type = NetNumber
_AtvIPXRouterNetAddress_Object = MibTableColumn
atvIPXRouterNetAddress = _AtvIPXRouterNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 4),
    _AtvIPXRouterNetAddress_Type()
)
atvIPXRouterNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterNetAddress.setStatus("mandatory")


class _AtvIPXRouterFramingType_Type(Integer32):
    """Custom type atvIPXRouterFramingType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-2", 1),
          ("ethernet-802-3-llc", 2),
          ("ethernet-802-3-raw", 4),
          ("ethernet-802-3-snap", 3),
          ("fddi-llc", 7),
          ("fddi-llc-sr", 8),
          ("fddi-snap", 5),
          ("fddi-snap-sr", 6),
          ("token-ring-llc", 11),
          ("token-ring-llc-sr", 12),
          ("token-ring-snap", 9),
          ("token-ring-snap-sr", 10))
    )


_AtvIPXRouterFramingType_Type.__name__ = "Integer32"
_AtvIPXRouterFramingType_Object = MibTableColumn
atvIPXRouterFramingType = _AtvIPXRouterFramingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 5),
    _AtvIPXRouterFramingType_Type()
)
atvIPXRouterFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterFramingType.setStatus("mandatory")


class _AtvIPXRouterDescription_Type(DisplayString):
    """Custom type atvIPXRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtvIPXRouterDescription_Type.__name__ = "DisplayString"
_AtvIPXRouterDescription_Object = MibTableColumn
atvIPXRouterDescription = _AtvIPXRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 6),
    _AtvIPXRouterDescription_Type()
)
atvIPXRouterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterDescription.setStatus("optional")
_AtvIPXRouterAdmStatus_Type = XylanVlanAdminStatCodes
_AtvIPXRouterAdmStatus_Object = MibTableColumn
atvIPXRouterAdmStatus = _AtvIPXRouterAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 7),
    _AtvIPXRouterAdmStatus_Type()
)
atvIPXRouterAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXRouterAdmStatus.setStatus("mandatory")
_AtvIPXRouterOperStatus_Type = XylanVlanOperStatCodes
_AtvIPXRouterOperStatus_Object = MibTableColumn
atvIPXRouterOperStatus = _AtvIPXRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 8),
    _AtvIPXRouterOperStatus_Type()
)
atvIPXRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atvIPXRouterOperStatus.setStatus("mandatory")


class _AtvIPXSrcRteType_Type(Integer32):
    """Custom type atvIPXSrcRteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("are", 1),
          ("not-applicable", 3),
          ("ste", 2))
    )


_AtvIPXSrcRteType_Type.__name__ = "Integer32"
_AtvIPXSrcRteType_Object = MibTableColumn
atvIPXSrcRteType = _AtvIPXSrcRteType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 12, 1, 1, 9),
    _AtvIPXSrcRteType_Type()
)
atvIPXSrcRteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atvIPXSrcRteType.setStatus("mandatory")
_V80210_ObjectIdentity = ObjectIdentity
v80210 = _V80210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13)
)
_V80210ServicesTable_Object = MibTable
v80210ServicesTable = _V80210ServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    v80210ServicesTable.setStatus("mandatory")
_V80210ServicesEntry_Object = MibTableRow
v80210ServicesEntry = _V80210ServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 1, 1)
)
v80210ServicesEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "v80210ServicesSlot"),
    (0, "XYLAN-VLAN-MIB", "v80210ServicesStation"),
)
if mibBuilder.loadTexts:
    v80210ServicesEntry.setStatus("mandatory")
_V80210ServicesSlot_Type = Integer32
_V80210ServicesSlot_Object = MibTableColumn
v80210ServicesSlot = _V80210ServicesSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 1, 1, 1),
    _V80210ServicesSlot_Type()
)
v80210ServicesSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v80210ServicesSlot.setStatus("mandatory")
_V80210ServicesStation_Type = Integer32
_V80210ServicesStation_Object = MibTableColumn
v80210ServicesStation = _V80210ServicesStation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 1, 1, 2),
    _V80210ServicesStation_Type()
)
v80210ServicesStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v80210ServicesStation.setStatus("mandatory")
_V80210ServicesDescription_Type = DisplayString
_V80210ServicesDescription_Object = MibTableColumn
v80210ServicesDescription = _V80210ServicesDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 1, 1, 3),
    _V80210ServicesDescription_Type()
)
v80210ServicesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v80210ServicesDescription.setStatus("mandatory")


class _V80210ServicesBridgeID_Type(Integer32):
    """Custom type v80210ServicesBridgeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_V80210ServicesBridgeID_Type.__name__ = "Integer32"
_V80210ServicesBridgeID_Object = MibTableColumn
v80210ServicesBridgeID = _V80210ServicesBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 1, 1, 4),
    _V80210ServicesBridgeID_Type()
)
v80210ServicesBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v80210ServicesBridgeID.setStatus("mandatory")
_V80210VlanTable_Object = MibTable
v80210VlanTable = _V80210VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 2)
)
if mibBuilder.loadTexts:
    v80210VlanTable.setStatus("mandatory")
_V80210VlanEntry_Object = MibTableRow
v80210VlanEntry = _V80210VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 2, 1)
)
v80210VlanEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "v80210Slot"),
    (0, "XYLAN-VLAN-MIB", "v80210Station"),
    (0, "XYLAN-VLAN-MIB", "v80210LanNumber"),
)
if mibBuilder.loadTexts:
    v80210VlanEntry.setStatus("mandatory")
_V80210Slot_Type = Integer32
_V80210Slot_Object = MibTableColumn
v80210Slot = _V80210Slot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 2, 1, 1),
    _V80210Slot_Type()
)
v80210Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v80210Slot.setStatus("mandatory")
_V80210Station_Type = Integer32
_V80210Station_Object = MibTableColumn
v80210Station = _V80210Station_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 2, 1, 2),
    _V80210Station_Type()
)
v80210Station.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v80210Station.setStatus("mandatory")


class _V80210LanNumber_Type(Integer32):
    """Custom type v80210LanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_V80210LanNumber_Type.__name__ = "Integer32"
_V80210LanNumber_Object = MibTableColumn
v80210LanNumber = _V80210LanNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 2, 1, 3),
    _V80210LanNumber_Type()
)
v80210LanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v80210LanNumber.setStatus("mandatory")


class _V80210Command_Type(Integer32):
    """Custom type v80210Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_V80210Command_Type.__name__ = "Integer32"
_V80210Command_Object = MibTableColumn
v80210Command = _V80210Command_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 13, 2, 1, 4),
    _V80210Command_Type()
)
v80210Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v80210Command.setStatus("mandatory")
_VDBr_ObjectIdentity = ObjectIdentity
vDBr = _VDBr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14)
)
_VDBrServicesTable_Object = MibTable
vDBrServicesTable = _VDBrServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 1)
)
if mibBuilder.loadTexts:
    vDBrServicesTable.setStatus("mandatory")
_VDBrServicesEntry_Object = MibTableRow
vDBrServicesEntry = _VDBrServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 1, 1)
)
vDBrServicesEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vDBrServicesSlot"),
    (0, "XYLAN-VLAN-MIB", "vDBrServicesStation"),
)
if mibBuilder.loadTexts:
    vDBrServicesEntry.setStatus("mandatory")
_VDBrServicesSlot_Type = Integer32
_VDBrServicesSlot_Object = MibTableColumn
vDBrServicesSlot = _VDBrServicesSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 1, 1, 1),
    _VDBrServicesSlot_Type()
)
vDBrServicesSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDBrServicesSlot.setStatus("mandatory")
_VDBrServicesStation_Type = Integer32
_VDBrServicesStation_Object = MibTableColumn
vDBrServicesStation = _VDBrServicesStation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 1, 1, 2),
    _VDBrServicesStation_Type()
)
vDBrServicesStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDBrServicesStation.setStatus("mandatory")
_VDBrServicesDescription_Type = DisplayString
_VDBrServicesDescription_Object = MibTableColumn
vDBrServicesDescription = _VDBrServicesDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 1, 1, 3),
    _VDBrServicesDescription_Type()
)
vDBrServicesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDBrServicesDescription.setStatus("mandatory")


class _VDBrServicesBridgeID_Type(Integer32):
    """Custom type vDBrServicesBridgeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VDBrServicesBridgeID_Type.__name__ = "Integer32"
_VDBrServicesBridgeID_Object = MibTableColumn
vDBrServicesBridgeID = _VDBrServicesBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 1, 1, 4),
    _VDBrServicesBridgeID_Type()
)
vDBrServicesBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDBrServicesBridgeID.setStatus("mandatory")
_VDBrVlanTable_Object = MibTable
vDBrVlanTable = _VDBrVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 2)
)
if mibBuilder.loadTexts:
    vDBrVlanTable.setStatus("mandatory")
_VDBrVlanEntry_Object = MibTableRow
vDBrVlanEntry = _VDBrVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 2, 1)
)
vDBrVlanEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "vDBrSlot"),
    (0, "XYLAN-VLAN-MIB", "vDBrStation"),
    (0, "XYLAN-VLAN-MIB", "vDBrLanNumber"),
)
if mibBuilder.loadTexts:
    vDBrVlanEntry.setStatus("mandatory")
_VDBrSlot_Type = Integer32
_VDBrSlot_Object = MibTableColumn
vDBrSlot = _VDBrSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 2, 1, 1),
    _VDBrSlot_Type()
)
vDBrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDBrSlot.setStatus("mandatory")
_VDBrStation_Type = Integer32
_VDBrStation_Object = MibTableColumn
vDBrStation = _VDBrStation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 2, 1, 2),
    _VDBrStation_Type()
)
vDBrStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDBrStation.setStatus("mandatory")


class _VDBrLanNumber_Type(Integer32):
    """Custom type vDBrLanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VDBrLanNumber_Type.__name__ = "Integer32"
_VDBrLanNumber_Object = MibTableColumn
vDBrLanNumber = _VDBrLanNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 2, 1, 3),
    _VDBrLanNumber_Type()
)
vDBrLanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDBrLanNumber.setStatus("mandatory")


class _VDBrCommand_Type(Integer32):
    """Custom type vDBrCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_VDBrCommand_Type.__name__ = "Integer32"
_VDBrCommand_Object = MibTableColumn
vDBrCommand = _VDBrCommand_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 14, 2, 1, 4),
    _VDBrCommand_Type()
)
vDBrCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vDBrCommand.setStatus("mandatory")
_V8021Q_ObjectIdentity = ObjectIdentity
v8021Q = _V8021Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15)
)
_QGroupTable_Object = MibTable
qGroupTable = _QGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    qGroupTable.setStatus("mandatory")
_QGroupEntry_Object = MibTableRow
qGroupEntry = _QGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1)
)
qGroupEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "qGroupSlot"),
    (0, "XYLAN-VLAN-MIB", "qGroupPort"),
    (0, "XYLAN-VLAN-MIB", "qGroupGroupId"),
)
if mibBuilder.loadTexts:
    qGroupEntry.setStatus("mandatory")
_QGroupSlot_Type = Integer32
_QGroupSlot_Object = MibTableColumn
qGroupSlot = _QGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 1),
    _QGroupSlot_Type()
)
qGroupSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupSlot.setStatus("mandatory")
_QGroupPort_Type = Integer32
_QGroupPort_Object = MibTableColumn
qGroupPort = _QGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 2),
    _QGroupPort_Type()
)
qGroupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupPort.setStatus("mandatory")
_QGroupGroupId_Type = Integer32
_QGroupGroupId_Object = MibTableColumn
qGroupGroupId = _QGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 3),
    _QGroupGroupId_Type()
)
qGroupGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupGroupId.setStatus("mandatory")


class _QGroupMode_Type(Integer32):
    """Custom type qGroupMode based on Integer32"""
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
        *(("gstsieee", 2),
          ("gstsxylan", 1),
          ("msts", 3),
          ("ssts", 4))
    )


_QGroupMode_Type.__name__ = "Integer32"
_QGroupMode_Object = MibTableColumn
qGroupMode = _QGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 4),
    _QGroupMode_Type()
)
qGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupMode.setStatus("mandatory")


class _QGroupDescription_Type(DisplayString):
    """Custom type qGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QGroupDescription_Type.__name__ = "DisplayString"
_QGroupDescription_Object = MibTableColumn
qGroupDescription = _QGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 5),
    _QGroupDescription_Type()
)
qGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupDescription.setStatus("mandatory")
_QGroupTag_Type = Integer32
_QGroupTag_Object = MibTableColumn
qGroupTag = _QGroupTag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 6),
    _QGroupTag_Type()
)
qGroupTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupTag.setStatus("mandatory")
_QGroupPriority_Type = Integer32
_QGroupPriority_Object = MibTableColumn
qGroupPriority = _QGroupPriority_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 7),
    _QGroupPriority_Type()
)
qGroupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupPriority.setStatus("mandatory")


class _QGroupAdminStatus_Type(Integer32):
    """Custom type qGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 0))
    )


_QGroupAdminStatus_Type.__name__ = "Integer32"
_QGroupAdminStatus_Object = MibTableColumn
qGroupAdminStatus = _QGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 8),
    _QGroupAdminStatus_Type()
)
qGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qGroupAdminStatus.setStatus("mandatory")
_QGroupTxPkts_Type = Counter32
_QGroupTxPkts_Object = MibTableColumn
qGroupTxPkts = _QGroupTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 9),
    _QGroupTxPkts_Type()
)
qGroupTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qGroupTxPkts.setStatus("mandatory")
_QGroupRxPkts_Type = Counter32
_QGroupRxPkts_Object = MibTableColumn
qGroupRxPkts = _QGroupRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 10),
    _QGroupRxPkts_Type()
)
qGroupRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qGroupRxPkts.setStatus("mandatory")
_QGroupTxOctets_Type = Counter32
_QGroupTxOctets_Object = MibTableColumn
qGroupTxOctets = _QGroupTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 11),
    _QGroupTxOctets_Type()
)
qGroupTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qGroupTxOctets.setStatus("mandatory")
_QGroupRxOctets_Type = Counter32
_QGroupRxOctets_Object = MibTableColumn
qGroupRxOctets = _QGroupRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 15, 1, 1, 12),
    _QGroupRxOctets_Type()
)
qGroupRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qGroupRxOctets.setStatus("mandatory")
_VDupMac_ObjectIdentity = ObjectIdentity
vDupMac = _VDupMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 16)
)
_VDupMacMac_Type = MacAddress
_VDupMacMac_Object = MibScalar
vDupMacMac = _VDupMacMac_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 16, 1),
    _VDupMacMac_Type()
)
vDupMacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDupMacMac.setStatus("mandatory")
_VDupMacSlot_Type = Integer32
_VDupMacSlot_Object = MibScalar
vDupMacSlot = _VDupMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 16, 2),
    _VDupMacSlot_Type()
)
vDupMacSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDupMacSlot.setStatus("mandatory")
_VDupMacIntf_Type = Integer32
_VDupMacIntf_Object = MibScalar
vDupMacIntf = _VDupMacIntf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 16, 3),
    _VDupMacIntf_Type()
)
vDupMacIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDupMacIntf.setStatus("mandatory")
_VDupMacTime_Type = Integer32
_VDupMacTime_Object = MibScalar
vDupMacTime = _VDupMacTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 16, 4),
    _VDupMacTime_Type()
)
vDupMacTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDupMacTime.setStatus("mandatory")
_VPmap_ObjectIdentity = ObjectIdentity
vPmap = _VPmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17)
)
_VPmapIngressTable_Object = MibTable
vPmapIngressTable = _VPmapIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1)
)
if mibBuilder.loadTexts:
    vPmapIngressTable.setStatus("mandatory")
_VPmapIngressEntry_Object = MibTableRow
vPmapIngressEntry = _VPmapIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1)
)
vPmapIngressEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "pMapIngressId"),
    (0, "XYLAN-VLAN-MIB", "pMapIngressSlot"),
    (0, "XYLAN-VLAN-MIB", "pMapIngressPort"),
    (0, "XYLAN-VLAN-MIB", "pMapIngressSrvc"),
    (0, "XYLAN-VLAN-MIB", "pMapIngressInst"),
)
if mibBuilder.loadTexts:
    vPmapIngressEntry.setStatus("mandatory")


class _PMapIngressId_Type(Integer32):
    """Custom type pMapIngressId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PMapIngressId_Type.__name__ = "Integer32"
_PMapIngressId_Object = MibTableColumn
pMapIngressId = _PMapIngressId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1, 1),
    _PMapIngressId_Type()
)
pMapIngressId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapIngressId.setStatus("mandatory")


class _PMapIngressSlot_Type(Integer32):
    """Custom type pMapIngressSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PMapIngressSlot_Type.__name__ = "Integer32"
_PMapIngressSlot_Object = MibTableColumn
pMapIngressSlot = _PMapIngressSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1, 2),
    _PMapIngressSlot_Type()
)
pMapIngressSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapIngressSlot.setStatus("mandatory")


class _PMapIngressPort_Type(Integer32):
    """Custom type pMapIngressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PMapIngressPort_Type.__name__ = "Integer32"
_PMapIngressPort_Object = MibTableColumn
pMapIngressPort = _PMapIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1, 3),
    _PMapIngressPort_Type()
)
pMapIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapIngressPort.setStatus("mandatory")
_PMapIngressSrvc_Type = Integer32
_PMapIngressSrvc_Object = MibTableColumn
pMapIngressSrvc = _PMapIngressSrvc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1, 4),
    _PMapIngressSrvc_Type()
)
pMapIngressSrvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapIngressSrvc.setStatus("mandatory")
_PMapIngressInst_Type = Integer32
_PMapIngressInst_Object = MibTableColumn
pMapIngressInst = _PMapIngressInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1, 5),
    _PMapIngressInst_Type()
)
pMapIngressInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapIngressInst.setStatus("mandatory")


class _PMapIngressAdminStatus_Type(Integer32):
    """Custom type pMapIngressAdminStatus based on Integer32"""
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


_PMapIngressAdminStatus_Type.__name__ = "Integer32"
_PMapIngressAdminStatus_Object = MibTableColumn
pMapIngressAdminStatus = _PMapIngressAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 1, 1, 6),
    _PMapIngressAdminStatus_Type()
)
pMapIngressAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapIngressAdminStatus.setStatus("mandatory")
_VPmapEgressTable_Object = MibTable
vPmapEgressTable = _VPmapEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2)
)
if mibBuilder.loadTexts:
    vPmapEgressTable.setStatus("mandatory")
_VPmapEgressEntry_Object = MibTableRow
vPmapEgressEntry = _VPmapEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1)
)
vPmapEgressEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "pMapEgressId"),
    (0, "XYLAN-VLAN-MIB", "pMapEgressSlot"),
    (0, "XYLAN-VLAN-MIB", "pMapEgressPort"),
    (0, "XYLAN-VLAN-MIB", "pMapEgressSrvc"),
    (0, "XYLAN-VLAN-MIB", "pMapEgressInst"),
)
if mibBuilder.loadTexts:
    vPmapEgressEntry.setStatus("mandatory")


class _PMapEgressId_Type(Integer32):
    """Custom type pMapEgressId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_PMapEgressId_Type.__name__ = "Integer32"
_PMapEgressId_Object = MibTableColumn
pMapEgressId = _PMapEgressId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1, 1),
    _PMapEgressId_Type()
)
pMapEgressId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapEgressId.setStatus("mandatory")


class _PMapEgressSlot_Type(Integer32):
    """Custom type pMapEgressSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PMapEgressSlot_Type.__name__ = "Integer32"
_PMapEgressSlot_Object = MibTableColumn
pMapEgressSlot = _PMapEgressSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1, 2),
    _PMapEgressSlot_Type()
)
pMapEgressSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapEgressSlot.setStatus("mandatory")


class _PMapEgressPort_Type(Integer32):
    """Custom type pMapEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PMapEgressPort_Type.__name__ = "Integer32"
_PMapEgressPort_Object = MibTableColumn
pMapEgressPort = _PMapEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1, 3),
    _PMapEgressPort_Type()
)
pMapEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapEgressPort.setStatus("mandatory")
_PMapEgressSrvc_Type = Integer32
_PMapEgressSrvc_Object = MibTableColumn
pMapEgressSrvc = _PMapEgressSrvc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1, 4),
    _PMapEgressSrvc_Type()
)
pMapEgressSrvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapEgressSrvc.setStatus("mandatory")
_PMapEgressInst_Type = Integer32
_PMapEgressInst_Object = MibTableColumn
pMapEgressInst = _PMapEgressInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1, 5),
    _PMapEgressInst_Type()
)
pMapEgressInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapEgressInst.setStatus("mandatory")


class _PMapEgressAdminStatus_Type(Integer32):
    """Custom type pMapEgressAdminStatus based on Integer32"""
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


_PMapEgressAdminStatus_Type.__name__ = "Integer32"
_PMapEgressAdminStatus_Object = MibTableColumn
pMapEgressAdminStatus = _PMapEgressAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 2, 1, 6),
    _PMapEgressAdminStatus_Type()
)
pMapEgressAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapEgressAdminStatus.setStatus("mandatory")
_VPmapConfigTable_Object = MibTable
vPmapConfigTable = _VPmapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 3)
)
if mibBuilder.loadTexts:
    vPmapConfigTable.setStatus("mandatory")
_VPmapConfigEntry_Object = MibTableRow
vPmapConfigEntry = _VPmapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 3, 1)
)
vPmapConfigEntry.setIndexNames(
    (0, "XYLAN-VLAN-MIB", "pMapConfigId"),
)
if mibBuilder.loadTexts:
    vPmapConfigEntry.setStatus("mandatory")


class _PMapConfigId_Type(Integer32):
    """Custom type pMapConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PMapConfigId_Type.__name__ = "Integer32"
_PMapConfigId_Object = MibTableColumn
pMapConfigId = _PMapConfigId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 3, 1, 1),
    _PMapConfigId_Type()
)
pMapConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pMapConfigId.setStatus("mandatory")


class _PMapConfigStatus_Type(Integer32):
    """Custom type pMapConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("set", 1))
    )


_PMapConfigStatus_Type.__name__ = "Integer32"
_PMapConfigStatus_Object = MibTableColumn
pMapConfigStatus = _PMapConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 3, 1, 2),
    _PMapConfigStatus_Type()
)
pMapConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pMapConfigStatus.setStatus("mandatory")


class _VPmapNextId_Type(Integer32):
    """Custom type vPmapNextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_VPmapNextId_Type.__name__ = "Integer32"
_VPmapNextId_Object = MibScalar
vPmapNextId = _VPmapNextId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 2, 17, 4),
    _VPmapNextId_Type()
)
vPmapNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPmapNextId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-VLAN-MIB",
    **{"XylanVlanAdminStatCodes": XylanVlanAdminStatCodes,
       "XylanVlanOperStatCodes": XylanVlanOperStatCodes,
       "XylanVlanModes": XylanVlanModes,
       "NetNumber": NetNumber,
       "VIPRouterRelayServType": VIPRouterRelayServType,
       "vLanInfo": vLanInfo,
       "vLanCurrentNumber": vLanCurrentNumber,
       "vLanTable": vLanTable,
       "vLanEntry": vLanEntry,
       "vLanNumber": vLanNumber,
       "vLanBridgeAddress": vLanBridgeAddress,
       "vLanBridgeType": vLanBridgeType,
       "vLanDescription": vLanDescription,
       "vLanAdmStatus": vLanAdmStatus,
       "vLanOperStatus": vLanOperStatus,
       "vLanMode": vLanMode,
       "vLanFloodOverride": vLanFloodOverride,
       "vLanRouterAddress": vLanRouterAddress,
       "vLanMobileGroup": vLanMobileGroup,
       "vLanAuthGroup": vLanAuthGroup,
       "vLanAuthGroupProtocol": vLanAuthGroupProtocol,
       "vLanStpStatus": vLanStpStatus,
       "vLanBrdgTpExtendedAgeingTime": vLanBrdgTpExtendedAgeingTime,
       "vLanPriority": vLanPriority,
       "vLanNextFreeNumber": vLanNextFreeNumber,
       "vIPRouterInfo": vIPRouterInfo,
       "vIPRouterTable": vIPRouterTable,
       "vIPRouterEntry": vIPRouterEntry,
       "vIPRouterVLan": vIPRouterVLan,
       "vIPRouterProtocol": vIPRouterProtocol,
       "vIPRouterNetAddress": vIPRouterNetAddress,
       "vIPRouterSubNetMask": vIPRouterSubNetMask,
       "vIPRouterBcastAddress": vIPRouterBcastAddress,
       "vIPRouterDescription": vIPRouterDescription,
       "vIPRouterAdmStatus": vIPRouterAdmStatus,
       "vIPRouterOperStatus": vIPRouterOperStatus,
       "vIPRouterFramingType": vIPRouterFramingType,
       "vIPRouterRipConfigMode": vIPRouterRipConfigMode,
       "vIPRouterRelayTable": vIPRouterRelayTable,
       "vIPRouterRelayEntry": vIPRouterRelayEntry,
       "vIPRouterRelayService": vIPRouterRelayService,
       "vIPRouterRelayMode": vIPRouterRelayMode,
       "vIPRouterRelayNextHop": vIPRouterRelayNextHop,
       "vIPRouterRelayParam1": vIPRouterRelayParam1,
       "vIPRouterRelayParam2": vIPRouterRelayParam2,
       "vIPRouterRelayDescription": vIPRouterRelayDescription,
       "vIPXRouterInfo": vIPXRouterInfo,
       "vIPXRouterTable": vIPXRouterTable,
       "vIPXRouterEntry": vIPXRouterEntry,
       "vIPXRouterVLan": vIPXRouterVLan,
       "vIPXRouterProtocol": vIPXRouterProtocol,
       "vIPXRouterNetAddress": vIPXRouterNetAddress,
       "vIPXRouterFramingType": vIPXRouterFramingType,
       "vIPXRouterDescription": vIPXRouterDescription,
       "vIPXRouterAdmStatus": vIPXRouterAdmStatus,
       "vIPXRouterOperStatus": vIPXRouterOperStatus,
       "vIPXSrcRteType": vIPXSrcRteType,
       "vBrdgInfo": vBrdgInfo,
       "vBrdgTpLearnEntryDiscards": vBrdgTpLearnEntryDiscards,
       "vBrdgTpAgingTime": vBrdgTpAgingTime,
       "vBrdgTpFdbTable": vBrdgTpFdbTable,
       "vBrdgTpFdbEntry": vBrdgTpFdbEntry,
       "vBrdgTpFdbGroupId": vBrdgTpFdbGroupId,
       "vBrdgTpFdbAddress": vBrdgTpFdbAddress,
       "vBrdgTpFdbRcvPortSlot": vBrdgTpFdbRcvPortSlot,
       "vBrdgTpFdbRcvPortIF": vBrdgTpFdbRcvPortIF,
       "vBrdgTpFdbRcvPortFuncTyp": vBrdgTpFdbRcvPortFuncTyp,
       "vBrdgTpFdbRcvPortFuncTypInst": vBrdgTpFdbRcvPortFuncTypInst,
       "vBrdgTpFdbRcvStatus": vBrdgTpFdbRcvStatus,
       "vBrdgTpFdbRcvVLANMembership": vBrdgTpFdbRcvVLANMembership,
       "vBrdgTpFdbDupStatus": vBrdgTpFdbDupStatus,
       "vBrdgTpFdbLastSeenTime": vBrdgTpFdbLastSeenTime,
       "vBrdgStaticTable": vBrdgStaticTable,
       "vBrdgStaticEntry": vBrdgStaticEntry,
       "vBrdgStaticAddress": vBrdgStaticAddress,
       "vBrdgStaticPortSlot": vBrdgStaticPortSlot,
       "vBrdgStaticPortIF": vBrdgStaticPortIF,
       "vBrdgStaticPortFuncTyp": vBrdgStaticPortFuncTyp,
       "vBrdgStaticPortFuncTypInst": vBrdgStaticPortFuncTypInst,
       "vBrdgStaticStatus": vBrdgStaticStatus,
       "vBrdgTpATVLANAgeingTime": vBrdgTpATVLANAgeingTime,
       "vStpInfo": vStpInfo,
       "vStpProtocolSpecification": vStpProtocolSpecification,
       "vStpPriority": vStpPriority,
       "vStpBridgeAddress": vStpBridgeAddress,
       "vStpTimeSinceTopologyChange": vStpTimeSinceTopologyChange,
       "vStpTopChanges": vStpTopChanges,
       "vStpDesignatedRoot": vStpDesignatedRoot,
       "vStpRootCost": vStpRootCost,
       "vStpRootPortSlot": vStpRootPortSlot,
       "vStpRootPortIF": vStpRootPortIF,
       "vStpRootPortFuncTyp": vStpRootPortFuncTyp,
       "vStpRootPortFuncTypInst": vStpRootPortFuncTypInst,
       "vStpMaxAge": vStpMaxAge,
       "vStpHelloTime": vStpHelloTime,
       "vStpHoldTime": vStpHoldTime,
       "vStpForwardDelay": vStpForwardDelay,
       "vStpBridgeMaxAge": vStpBridgeMaxAge,
       "vStpBridgeHelloTime": vStpBridgeHelloTime,
       "vStpBridgeForwardDelay": vStpBridgeForwardDelay,
       "vStpPortTable": vStpPortTable,
       "vStpPortEntry": vStpPortEntry,
       "vStpPortSlot": vStpPortSlot,
       "vStpPortIF": vStpPortIF,
       "vStpPortFuncTyp": vStpPortFuncTyp,
       "vStpPortFuncTypInst": vStpPortFuncTypInst,
       "vStpPortPriority": vStpPortPriority,
       "vStpPortState": vStpPortState,
       "vStpPortEnable": vStpPortEnable,
       "vStpPortPathCost": vStpPortPathCost,
       "vStpPortDesignatedRoot": vStpPortDesignatedRoot,
       "vStpPortDesignatedCost": vStpPortDesignatedCost,
       "vStpPortDesignatedBridge": vStpPortDesignatedBridge,
       "vStpPortDesignatedPtPrio": vStpPortDesignatedPtPrio,
       "vStpPortDesignatedPtSlot": vStpPortDesignatedPtSlot,
       "vStpPortDesignatedPtIF": vStpPortDesignatedPtIF,
       "vStpPortDesignatedPtFuncTyp": vStpPortDesignatedPtFuncTyp,
       "vStpPortDesignatedPtFuncTypInst": vStpPortDesignatedPtFuncTypInst,
       "vStpPortForwardTransitions": vStpPortForwardTransitions,
       "vStpLanMode": vStpLanMode,
       "vStpStatus": vStpStatus,
       "vRipInfo": vRipInfo,
       "vRipInfoTable": vRipInfoTable,
       "vRipInfoEntry": vRipInfoEntry,
       "vRipInfovLanNumber": vRipInfovLanNumber,
       "vRipInPkts": vRipInPkts,
       "vRipOutPkts": vRipOutPkts,
       "vRipBadSize": vRipBadSize,
       "vRipBadVersion": vRipBadVersion,
       "vRipNonZero": vRipNonZero,
       "vRipBadFamily": vRipBadFamily,
       "vRipBadMetric": vRipBadMetric,
       "vRipBadAddr": vRipBadAddr,
       "vRipBadCommand": vRipBadCommand,
       "vRipTransmitsFailed": vRipTransmitsFailed,
       "vSr": vSr,
       "vSrTable": vSrTable,
       "vSrPortEntry": vSrPortEntry,
       "vSrSlot": vSrSlot,
       "vSrInterface": vSrInterface,
       "vSrFuncType": vSrFuncType,
       "vSrInstance": vSrInstance,
       "vSrHopCount": vSrHopCount,
       "vSrLocalSegment": vSrLocalSegment,
       "vSrBridgeNum": vSrBridgeNum,
       "vSrVirtualRing": vSrVirtualRing,
       "vSrLargestFrame": vSrLargestFrame,
       "vSrSTESpanMode": vSrSTESpanMode,
       "vSrSpecInFrames": vSrSpecInFrames,
       "vSrSpecOutFrames": vSrSpecOutFrames,
       "vSrApeInFrames": vSrApeInFrames,
       "vSrApeOutFrames": vSrApeOutFrames,
       "vSrSteInFrames": vSrSteInFrames,
       "vSrSteOutFrames": vSrSteOutFrames,
       "vSrInvalidRif": vSrInvalidRif,
       "vSrDuplicateSegmentDiscards": vSrDuplicateSegmentDiscards,
       "vSrHopCountExceededDiscards": vSrHopCountExceededDiscards,
       "vSrDupLanIdOrTreeErrors": vSrDupLanIdOrTreeErrors,
       "vSrLanIdMismatches": vSrLanIdMismatches,
       "vSrBridgeLfMode": vSrBridgeLfMode,
       "vSrPortType": vSrPortType,
       "vSrAREblock": vSrAREblock,
       "vSrHopCountIn": vSrHopCountIn,
       "vSrSapDenyFilter1": vSrSapDenyFilter1,
       "vSrSapDenyFilter2": vSrSapDenyFilter2,
       "vSrSapPermitFilter1": vSrSapPermitFilter1,
       "vSrSapPermitFilter2": vSrSapPermitFilter2,
       "vSrSapFilterEnable": vSrSapFilterEnable,
       "vTrunking": vTrunking,
       "vTrunkingServicesTable": vTrunkingServicesTable,
       "vTrunkingServicesEntry": vTrunkingServicesEntry,
       "vTrunkingServicesSlot": vTrunkingServicesSlot,
       "vTrunkingServicesStation": vTrunkingServicesStation,
       "vTrunkingServicesDescription": vTrunkingServicesDescription,
       "vTrunkingServicesBridgeID": vTrunkingServicesBridgeID,
       "vTrunkingVlanTable": vTrunkingVlanTable,
       "vTrunkingVlanEntry": vTrunkingVlanEntry,
       "vTrunkingSlot": vTrunkingSlot,
       "vTrunkingStation": vTrunkingStation,
       "vTrunkingLanNumber": vTrunkingLanNumber,
       "vTrunkingCommand": vTrunkingCommand,
       "vAutoTracker": vAutoTracker,
       "atportRuleTable": atportRuleTable,
       "atportRuleEntry": atportRuleEntry,
       "atportRuleGroupId": atportRuleGroupId,
       "atportRuleVLANId": atportRuleVLANId,
       "atportRuleIdx": atportRuleIdx,
       "atportRulePortId": atportRulePortId,
       "atportRulePortState": atportRulePortState,
       "atMacRuleTable": atMacRuleTable,
       "atMacRuleEntry": atMacRuleEntry,
       "atMacRuleGroupId": atMacRuleGroupId,
       "atMacRuleVLANId": atMacRuleVLANId,
       "atMacRuleIndex": atMacRuleIndex,
       "atMacRuleMacAddress": atMacRuleMacAddress,
       "atMacRuleMacAddressState": atMacRuleMacAddressState,
       "atProtoRuleTable": atProtoRuleTable,
       "atProtoRuleEntry": atProtoRuleEntry,
       "atProtoRuleGroupId": atProtoRuleGroupId,
       "atProtoRuleVLANId": atProtoRuleVLANId,
       "atProtoRuleIndex": atProtoRuleIndex,
       "atProtoRule": atProtoRule,
       "atProtoRuleStatus": atProtoRuleStatus,
       "atNetRuleTable": atNetRuleTable,
       "atNetRuleEntry": atNetRuleEntry,
       "atNetRuleGroupId": atNetRuleGroupId,
       "atNetRuleVLANId": atNetRuleVLANId,
       "atNetRuleIndex": atNetRuleIndex,
       "atNetRuleProtocolId": atNetRuleProtocolId,
       "atNetRuleNetAddr": atNetRuleNetAddr,
       "atNetRuleStatus": atNetRuleStatus,
       "atUserRuleTable": atUserRuleTable,
       "atUserRuleEntry": atUserRuleEntry,
       "atUserRuleGroupId": atUserRuleGroupId,
       "atUserRuleVLANId": atUserRuleVLANId,
       "atUserRuleIndex": atUserRuleIndex,
       "atUserRuleOffset": atUserRuleOffset,
       "atUserRuleValue": atUserRuleValue,
       "atUserRuleMask": atUserRuleMask,
       "atUserRuleStatus": atUserRuleStatus,
       "atVLANRuleSumTable": atVLANRuleSumTable,
       "atVLANRuleSumEntry": atVLANRuleSumEntry,
       "atVLANRuleSumGroupId": atVLANRuleSumGroupId,
       "atVLANRuleSumVLANId": atVLANRuleSumVLANId,
       "atVLANRuleIndex": atVLANRuleIndex,
       "atVLANRuleSubIndex": atVLANRuleSubIndex,
       "atVLANRuleType": atVLANRuleType,
       "atVLANControlTable": atVLANControlTable,
       "atVLANControlEntry": atVLANControlEntry,
       "atVLANGroupId": atVLANGroupId,
       "atVLANId": atVLANId,
       "atVLANDesc": atVLANDesc,
       "atVLANAdminStatus": atVLANAdminStatus,
       "atVLANOperStatus": atVLANOperStatus,
       "atDefaultVlan": atDefaultVlan,
       "atmcportRuleTable": atmcportRuleTable,
       "atmcportRuleEntry": atmcportRuleEntry,
       "atmcportRuleGroupId": atmcportRuleGroupId,
       "atmcportRuleVLANId": atmcportRuleVLANId,
       "atmcportRuleIdx": atmcportRuleIdx,
       "atmcportRulePortId": atmcportRulePortId,
       "atmcportRulePortState": atmcportRulePortState,
       "atmcMacRuleTable": atmcMacRuleTable,
       "atmcMacRuleEntry": atmcMacRuleEntry,
       "atmcMacRuleGroupId": atmcMacRuleGroupId,
       "atmcMacRuleVLANId": atmcMacRuleVLANId,
       "atmcMacRuleIndex": atmcMacRuleIndex,
       "atmcMacRuleMacAddress": atmcMacRuleMacAddress,
       "atmcMacRuleMacAddressState": atmcMacRuleMacAddressState,
       "atMcastRuleTable": atMcastRuleTable,
       "atMcastRuleEntry": atMcastRuleEntry,
       "atMcastRuleGroupId": atMcastRuleGroupId,
       "atMcastRuleVLANId": atMcastRuleVLANId,
       "atMcastRuleIndex": atMcastRuleIndex,
       "atMcastRuleMacAddress": atMcastRuleMacAddress,
       "atMcastRuleMacAddressState": atMcastRuleMacAddressState,
       "atmcVLANRuleSumTable": atmcVLANRuleSumTable,
       "atmcVLANRuleSumEntry": atmcVLANRuleSumEntry,
       "atmcVLANRuleSumGroupId": atmcVLANRuleSumGroupId,
       "atmcVLANRuleSumVLANId": atmcVLANRuleSumVLANId,
       "atmcVLANRuleIndex": atmcVLANRuleIndex,
       "atmcVLANRuleSubIndex": atmcVLANRuleSubIndex,
       "atmcVLANRuleType": atmcVLANRuleType,
       "atmcVLANControlTable": atmcVLANControlTable,
       "atmcVLANControlEntry": atmcVLANControlEntry,
       "atmcVLANGroupId": atmcVLANGroupId,
       "atmcVLANId": atmcVLANId,
       "atmcVLANDesc": atmcVLANDesc,
       "atmcVLANAdminStatus": atmcVLANAdminStatus,
       "atmcVLANOperStatus": atmcVLANOperStatus,
       "gmAutoServiceTable": gmAutoServiceTable,
       "gmAutoServiceEntry": gmAutoServiceEntry,
       "gmAutoServiceGroupId": gmAutoServiceGroupId,
       "gmAutoServicePrimarySlot": gmAutoServicePrimarySlot,
       "gmAutoServicePrimaryPort": gmAutoServicePrimaryPort,
       "gmAutoServiceIndex": gmAutoServiceIndex,
       "gmAutoServiceType": gmAutoServiceType,
       "gmAutoServiceName": gmAutoServiceName,
       "gmAutoServiceSecondarySlot": gmAutoServiceSecondarySlot,
       "gmAutoServiceSecondaryPort": gmAutoServiceSecondaryPort,
       "gmAutoServiceAdminState": gmAutoServiceAdminState,
       "gmAutoServiceOperState": gmAutoServiceOperState,
       "gmAutoServiceActiveSlot": gmAutoServiceActiveSlot,
       "gmAutoServiceActivePort": gmAutoServiceActivePort,
       "gmAutoServiceNumber": gmAutoServiceNumber,
       "gmAutoServiceTranslations": gmAutoServiceTranslations,
       "atBindRuleTable": atBindRuleTable,
       "atBindRuleEntry": atBindRuleEntry,
       "atBindRuleGroupId": atBindRuleGroupId,
       "atBindRuleVlanId": atBindRuleVlanId,
       "atBindRuleIndex": atBindRuleIndex,
       "atBindRulePortId": atBindRulePortId,
       "atBindRuleIPAddress": atBindRuleIPAddress,
       "atBindRuleMacAddress": atBindRuleMacAddress,
       "atBindRuleProtocol": atBindRuleProtocol,
       "atBindRuleBindParameter": atBindRuleBindParameter,
       "atBindRuleStatus": atBindRuleStatus,
       "gmGroupListTable": gmGroupListTable,
       "gmGroupListEntry": gmGroupListEntry,
       "gmGroupListPortSlot": gmGroupListPortSlot,
       "gmGroupListPortInterface": gmGroupListPortInterface,
       "gmGroupListGroupId": gmGroupListGroupId,
       "atDHCPportRuleTable": atDHCPportRuleTable,
       "atDHCPportRuleEntry": atDHCPportRuleEntry,
       "atDHCPportRuleGroupId": atDHCPportRuleGroupId,
       "atDHCPportRuleVLANId": atDHCPportRuleVLANId,
       "atDHCPportRuleIdx": atDHCPportRuleIdx,
       "atDHCPportRulePortId": atDHCPportRulePortId,
       "atDHCPportRulePortState": atDHCPportRulePortState,
       "atDHCPMacRuleTable": atDHCPMacRuleTable,
       "atDHCPMacRuleEntry": atDHCPMacRuleEntry,
       "atDHCPMacRuleGroupId": atDHCPMacRuleGroupId,
       "atDHCPMacRuleVLANId": atDHCPMacRuleVLANId,
       "atDHCPMacRuleIndex": atDHCPMacRuleIndex,
       "atDHCPMacRuleMacAddress": atDHCPMacRuleMacAddress,
       "atDHCPMacRuleMacAddressState": atDHCPMacRuleMacAddressState,
       "groupMobilityStatus": groupMobilityStatus,
       "gmMoveToDefGroup": gmMoveToDefGroup,
       "gmDefGroup": gmDefGroup,
       "atvIPRouterInfo": atvIPRouterInfo,
       "atvIPRouterTable": atvIPRouterTable,
       "atvIPRouterEntry": atvIPRouterEntry,
       "atvIPRouterVLanGroup": atvIPRouterVLanGroup,
       "atvIPRouterVLan": atvIPRouterVLan,
       "atvIPRouterProtocol": atvIPRouterProtocol,
       "atvIPRouterNetAddress": atvIPRouterNetAddress,
       "atvIPRouterSubNetMask": atvIPRouterSubNetMask,
       "atvIPRouterBcastAddress": atvIPRouterBcastAddress,
       "atvIPRouterDescription": atvIPRouterDescription,
       "atvIPRouterAdmStatus": atvIPRouterAdmStatus,
       "atvIPRouterOperStatus": atvIPRouterOperStatus,
       "atvIPRouterFramingType": atvIPRouterFramingType,
       "atvIPRouterRipConfigMode": atvIPRouterRipConfigMode,
       "atvIPRouterRelayServicesFwd": atvIPRouterRelayServicesFwd,
       "atvIPXRouterInfo": atvIPXRouterInfo,
       "atvIPXRouterTable": atvIPXRouterTable,
       "atvIPXRouterEntry": atvIPXRouterEntry,
       "atvIPXRouterVLanGroup": atvIPXRouterVLanGroup,
       "atvIPXRouterVLan": atvIPXRouterVLan,
       "atvIPXRouterProtocol": atvIPXRouterProtocol,
       "atvIPXRouterNetAddress": atvIPXRouterNetAddress,
       "atvIPXRouterFramingType": atvIPXRouterFramingType,
       "atvIPXRouterDescription": atvIPXRouterDescription,
       "atvIPXRouterAdmStatus": atvIPXRouterAdmStatus,
       "atvIPXRouterOperStatus": atvIPXRouterOperStatus,
       "atvIPXSrcRteType": atvIPXSrcRteType,
       "v80210": v80210,
       "v80210ServicesTable": v80210ServicesTable,
       "v80210ServicesEntry": v80210ServicesEntry,
       "v80210ServicesSlot": v80210ServicesSlot,
       "v80210ServicesStation": v80210ServicesStation,
       "v80210ServicesDescription": v80210ServicesDescription,
       "v80210ServicesBridgeID": v80210ServicesBridgeID,
       "v80210VlanTable": v80210VlanTable,
       "v80210VlanEntry": v80210VlanEntry,
       "v80210Slot": v80210Slot,
       "v80210Station": v80210Station,
       "v80210LanNumber": v80210LanNumber,
       "v80210Command": v80210Command,
       "vDBr": vDBr,
       "vDBrServicesTable": vDBrServicesTable,
       "vDBrServicesEntry": vDBrServicesEntry,
       "vDBrServicesSlot": vDBrServicesSlot,
       "vDBrServicesStation": vDBrServicesStation,
       "vDBrServicesDescription": vDBrServicesDescription,
       "vDBrServicesBridgeID": vDBrServicesBridgeID,
       "vDBrVlanTable": vDBrVlanTable,
       "vDBrVlanEntry": vDBrVlanEntry,
       "vDBrSlot": vDBrSlot,
       "vDBrStation": vDBrStation,
       "vDBrLanNumber": vDBrLanNumber,
       "vDBrCommand": vDBrCommand,
       "v8021Q": v8021Q,
       "qGroupTable": qGroupTable,
       "qGroupEntry": qGroupEntry,
       "qGroupSlot": qGroupSlot,
       "qGroupPort": qGroupPort,
       "qGroupGroupId": qGroupGroupId,
       "qGroupMode": qGroupMode,
       "qGroupDescription": qGroupDescription,
       "qGroupTag": qGroupTag,
       "qGroupPriority": qGroupPriority,
       "qGroupAdminStatus": qGroupAdminStatus,
       "qGroupTxPkts": qGroupTxPkts,
       "qGroupRxPkts": qGroupRxPkts,
       "qGroupTxOctets": qGroupTxOctets,
       "qGroupRxOctets": qGroupRxOctets,
       "vDupMac": vDupMac,
       "vDupMacMac": vDupMacMac,
       "vDupMacSlot": vDupMacSlot,
       "vDupMacIntf": vDupMacIntf,
       "vDupMacTime": vDupMacTime,
       "vPmap": vPmap,
       "vPmapIngressTable": vPmapIngressTable,
       "vPmapIngressEntry": vPmapIngressEntry,
       "pMapIngressId": pMapIngressId,
       "pMapIngressSlot": pMapIngressSlot,
       "pMapIngressPort": pMapIngressPort,
       "pMapIngressSrvc": pMapIngressSrvc,
       "pMapIngressInst": pMapIngressInst,
       "pMapIngressAdminStatus": pMapIngressAdminStatus,
       "vPmapEgressTable": vPmapEgressTable,
       "vPmapEgressEntry": vPmapEgressEntry,
       "pMapEgressId": pMapEgressId,
       "pMapEgressSlot": pMapEgressSlot,
       "pMapEgressPort": pMapEgressPort,
       "pMapEgressSrvc": pMapEgressSrvc,
       "pMapEgressInst": pMapEgressInst,
       "pMapEgressAdminStatus": pMapEgressAdminStatus,
       "vPmapConfigTable": vPmapConfigTable,
       "vPmapConfigEntry": vPmapConfigEntry,
       "pMapConfigId": pMapConfigId,
       "pMapConfigStatus": pMapConfigStatus,
       "vPmapNextId": vPmapNextId}
)
