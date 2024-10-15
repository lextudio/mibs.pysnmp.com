# SNMP MIB module (HP-VSF-VC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-VSF-VC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:13 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(hpSwitchBaseMACAddress,) = mibBuilder.importSymbols(
    "NETSWITCH-MIB",
    "hpSwitchBaseMACAddress")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfVsfVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116)
)
hpicfVsfVCMIB.setRevisions(
        ("2016-06-22 00:00",
         "2016-05-09 00:00",
         "2015-03-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfVsfVCNotifications_ObjectIdentity = ObjectIdentity
hpicfVsfVCNotifications = _HpicfVsfVCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 0)
)
_HpicfVsfVCObjects_ObjectIdentity = ObjectIdentity
hpicfVsfVCObjects = _HpicfVsfVCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1)
)
_HpicfVsfVCConfig_ObjectIdentity = ObjectIdentity
hpicfVsfVCConfig = _HpicfVsfVCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1)
)
_HpicfVsfVCDomainId_Type = Unsigned32
_HpicfVsfVCDomainId_Object = MibScalar
hpicfVsfVCDomainId = _HpicfVsfVCDomainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 1),
    _HpicfVsfVCDomainId_Type()
)
hpicfVsfVCDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCDomainId.setStatus("current")


class _HpicfVsfVCOperStatus_Type(Integer32):
    """Custom type hpicfVsfVCOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 1),
          ("fragmentActive", 4),
          ("fragmentInactive", 3),
          ("unAvailable", 0))
    )


_HpicfVsfVCOperStatus_Type.__name__ = "Integer32"
_HpicfVsfVCOperStatus_Object = MibScalar
hpicfVsfVCOperStatus = _HpicfVsfVCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 2),
    _HpicfVsfVCOperStatus_Type()
)
hpicfVsfVCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCOperStatus.setStatus("current")


class _HpicfVsfVCAdminStatus_Type(Integer32):
    """Custom type hpicfVsfVCAdminStatus based on Integer32"""
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


_HpicfVsfVCAdminStatus_Type.__name__ = "Integer32"
_HpicfVsfVCAdminStatus_Object = MibScalar
hpicfVsfVCAdminStatus = _HpicfVsfVCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 3),
    _HpicfVsfVCAdminStatus_Type()
)
hpicfVsfVCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCAdminStatus.setStatus("current")


class _HpicfVsfVCTopology_Type(Integer32):
    """Custom type hpicfVsfVCTopology based on Integer32"""
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
        *(("chain", 1),
          ("mesh", 3),
          ("partialMesh", 4),
          ("ring", 2),
          ("unknown", 0))
    )


_HpicfVsfVCTopology_Type.__name__ = "Integer32"
_HpicfVsfVCTopology_Object = MibScalar
hpicfVsfVCTopology = _HpicfVsfVCTopology_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 4),
    _HpicfVsfVCTopology_Type()
)
hpicfVsfVCTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCTopology.setStatus("current")


class _HpicfVsfVCTrapEnable_Type(Integer32):
    """Custom type hpicfVsfVCTrapEnable based on Integer32"""
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


_HpicfVsfVCTrapEnable_Type.__name__ = "Integer32"
_HpicfVsfVCTrapEnable_Object = MibScalar
hpicfVsfVCTrapEnable = _HpicfVsfVCTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 5),
    _HpicfVsfVCTrapEnable_Type()
)
hpicfVsfVCTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCTrapEnable.setStatus("current")


class _HpicfVsfVCOobmMADEnable_Type(Integer32):
    """Custom type hpicfVsfVCOobmMADEnable based on Integer32"""
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


_HpicfVsfVCOobmMADEnable_Type.__name__ = "Integer32"
_HpicfVsfVCOobmMADEnable_Object = MibScalar
hpicfVsfVCOobmMADEnable = _HpicfVsfVCOobmMADEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 6),
    _HpicfVsfVCOobmMADEnable_Type()
)
hpicfVsfVCOobmMADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCOobmMADEnable.setStatus("current")


class _HpicfVsfLldpMADEnable_Type(Integer32):
    """Custom type hpicfVsfLldpMADEnable based on Integer32"""
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


_HpicfVsfLldpMADEnable_Type.__name__ = "Integer32"
_HpicfVsfLldpMADEnable_Object = MibScalar
hpicfVsfLldpMADEnable = _HpicfVsfLldpMADEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 7),
    _HpicfVsfLldpMADEnable_Type()
)
hpicfVsfLldpMADEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfLldpMADEnable.setStatus("current")
_HpicfVsfVCLldpMADDeviceIpType_Type = InetAddressType
_HpicfVsfVCLldpMADDeviceIpType_Object = MibScalar
hpicfVsfVCLldpMADDeviceIpType = _HpicfVsfVCLldpMADDeviceIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 8),
    _HpicfVsfVCLldpMADDeviceIpType_Type()
)
hpicfVsfVCLldpMADDeviceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADDeviceIpType.setStatus("current")
_HpicfVsfVCLldpMADDeviceIpAddr_Type = InetAddress
_HpicfVsfVCLldpMADDeviceIpAddr_Object = MibScalar
hpicfVsfVCLldpMADDeviceIpAddr = _HpicfVsfVCLldpMADDeviceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 9),
    _HpicfVsfVCLldpMADDeviceIpAddr_Type()
)
hpicfVsfVCLldpMADDeviceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADDeviceIpAddr.setStatus("current")


class _HpicfVsfVCLldpMADSnmpVersion_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("v2c", 2)
    )


_HpicfVsfVCLldpMADSnmpVersion_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADSnmpVersion_Object = MibScalar
hpicfVsfVCLldpMADSnmpVersion = _HpicfVsfVCLldpMADSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 10),
    _HpicfVsfVCLldpMADSnmpVersion_Type()
)
hpicfVsfVCLldpMADSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADSnmpVersion.setStatus("current")


class _HpicfVsfVCLldpMADSnmpCommunity_Type(OctetString):
    """Custom type hpicfVsfVCLldpMADSnmpCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfVsfVCLldpMADSnmpCommunity_Type.__name__ = "OctetString"
_HpicfVsfVCLldpMADSnmpCommunity_Object = MibScalar
hpicfVsfVCLldpMADSnmpCommunity = _HpicfVsfVCLldpMADSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 11),
    _HpicfVsfVCLldpMADSnmpCommunity_Type()
)
hpicfVsfVCLldpMADSnmpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADSnmpCommunity.setStatus("current")


class _HpicfVsfMADVlan_Type(Integer32):
    """Custom type hpicfVsfMADVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfVsfMADVlan_Type.__name__ = "Integer32"
_HpicfVsfMADVlan_Object = MibScalar
hpicfVsfMADVlan = _HpicfVsfMADVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 12),
    _HpicfVsfMADVlan_Type()
)
hpicfVsfMADVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfMADVlan.setStatus("current")


class _HpicfVsfMADVlanConnectivity_Type(Integer32):
    """Custom type hpicfVsfMADVlanConnectivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("none", 1),
          ("partial", 3))
    )


_HpicfVsfMADVlanConnectivity_Type.__name__ = "Integer32"
_HpicfVsfMADVlanConnectivity_Object = MibScalar
hpicfVsfMADVlanConnectivity = _HpicfVsfMADVlanConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 13),
    _HpicfVsfMADVlanConnectivity_Type()
)
hpicfVsfMADVlanConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfMADVlanConnectivity.setStatus("current")


class _HpicfVsfVCPortSpeed_Type(Integer32):
    """Custom type hpicfVsfVCPortSpeed based on Integer32"""
    defaultValue = 0

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
        *(("fortyGbps", 3),
          ("none", 0),
          ("oneGbps", 1),
          ("tenGbps", 2))
    )


_HpicfVsfVCPortSpeed_Type.__name__ = "Integer32"
_HpicfVsfVCPortSpeed_Object = MibScalar
hpicfVsfVCPortSpeed = _HpicfVsfVCPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 1, 14),
    _HpicfVsfVCPortSpeed_Type()
)
hpicfVsfVCPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCPortSpeed.setStatus("current")
_HpicfVsfVCStatus_ObjectIdentity = ObjectIdentity
hpicfVsfVCStatus = _HpicfVsfVCStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2)
)


class _HpicfVsfVCLldpMADReadinessStatus_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADReadinessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("none", 0),
          ("success", 1))
    )


_HpicfVsfVCLldpMADReadinessStatus_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADReadinessStatus_Object = MibScalar
hpicfVsfVCLldpMADReadinessStatus = _HpicfVsfVCLldpMADReadinessStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 1),
    _HpicfVsfVCLldpMADReadinessStatus_Type()
)
hpicfVsfVCLldpMADReadinessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADReadinessStatus.setStatus("current")


class _HpicfVsfVCLldpMADDeviceMAC_Type(OctetString):
    """Custom type hpicfVsfVCLldpMADDeviceMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_HpicfVsfVCLldpMADDeviceMAC_Type.__name__ = "OctetString"
_HpicfVsfVCLldpMADDeviceMAC_Object = MibScalar
hpicfVsfVCLldpMADDeviceMAC = _HpicfVsfVCLldpMADDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 2),
    _HpicfVsfVCLldpMADDeviceMAC_Type()
)
hpicfVsfVCLldpMADDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADDeviceMAC.setStatus("current")


class _HpicfVsfVCLldpMADVlanId_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HpicfVsfVCLldpMADVlanId_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADVlanId_Object = MibScalar
hpicfVsfVCLldpMADVlanId = _HpicfVsfVCLldpMADVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 3),
    _HpicfVsfVCLldpMADVlanId_Type()
)
hpicfVsfVCLldpMADVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADVlanId.setStatus("current")
_HpicfVsfVCLldpMADTrunkIfIndex_Type = InterfaceIndexOrZero
_HpicfVsfVCLldpMADTrunkIfIndex_Object = MibScalar
hpicfVsfVCLldpMADTrunkIfIndex = _HpicfVsfVCLldpMADTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 4),
    _HpicfVsfVCLldpMADTrunkIfIndex_Type()
)
hpicfVsfVCLldpMADTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADTrunkIfIndex.setStatus("current")
_HpicfVsfVCLldpMADProbePortSet_Type = PortList
_HpicfVsfVCLldpMADProbePortSet_Object = MibScalar
hpicfVsfVCLldpMADProbePortSet = _HpicfVsfVCLldpMADProbePortSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 5),
    _HpicfVsfVCLldpMADProbePortSet_Type()
)
hpicfVsfVCLldpMADProbePortSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADProbePortSet.setStatus("current")


class _HpicfVsfVCLldpMADConnectivity_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADConnectivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("none", 1),
          ("partial", 3))
    )


_HpicfVsfVCLldpMADConnectivity_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADConnectivity_Object = MibScalar
hpicfVsfVCLldpMADConnectivity = _HpicfVsfVCLldpMADConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 6),
    _HpicfVsfVCLldpMADConnectivity_Type()
)
hpicfVsfVCLldpMADConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADConnectivity.setStatus("current")


class _HpicfVsfVCLldpMADSplitStatus_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADSplitStatus based on Integer32"""
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


_HpicfVsfVCLldpMADSplitStatus_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADSplitStatus_Object = MibScalar
hpicfVsfVCLldpMADSplitStatus = _HpicfVsfVCLldpMADSplitStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 7),
    _HpicfVsfVCLldpMADSplitStatus_Type()
)
hpicfVsfVCLldpMADSplitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADSplitStatus.setStatus("current")


class _HpicfVsfVCLldpMADProbeOriginator_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADProbeOriginator based on Integer32"""
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


_HpicfVsfVCLldpMADProbeOriginator_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADProbeOriginator_Object = MibScalar
hpicfVsfVCLldpMADProbeOriginator = _HpicfVsfVCLldpMADProbeOriginator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 8),
    _HpicfVsfVCLldpMADProbeOriginator_Type()
)
hpicfVsfVCLldpMADProbeOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADProbeOriginator.setStatus("current")
_HpicfVsfVCLldpMADProbeRequestsSent_Type = Counter32
_HpicfVsfVCLldpMADProbeRequestsSent_Object = MibScalar
hpicfVsfVCLldpMADProbeRequestsSent = _HpicfVsfVCLldpMADProbeRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 9),
    _HpicfVsfVCLldpMADProbeRequestsSent_Type()
)
hpicfVsfVCLldpMADProbeRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADProbeRequestsSent.setStatus("current")
_HpicfVsfVCLldpMADProbeResponseRcvd_Type = Counter32
_HpicfVsfVCLldpMADProbeResponseRcvd_Object = MibScalar
hpicfVsfVCLldpMADProbeResponseRcvd = _HpicfVsfVCLldpMADProbeResponseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 10),
    _HpicfVsfVCLldpMADProbeResponseRcvd_Type()
)
hpicfVsfVCLldpMADProbeResponseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADProbeResponseRcvd.setStatus("current")


class _HpicfVsfVCLldpMADActiveFragment_Type(Integer32):
    """Custom type hpicfVsfVCLldpMADActiveFragment based on Integer32"""
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


_HpicfVsfVCLldpMADActiveFragment_Type.__name__ = "Integer32"
_HpicfVsfVCLldpMADActiveFragment_Object = MibScalar
hpicfVsfVCLldpMADActiveFragment = _HpicfVsfVCLldpMADActiveFragment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 2, 11),
    _HpicfVsfVCLldpMADActiveFragment_Type()
)
hpicfVsfVCLldpMADActiveFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLldpMADActiveFragment.setStatus("current")
_HpicfVsfVCMemberTable_Object = MibTable
hpicfVsfVCMemberTable = _HpicfVsfVCMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfVsfVCMemberTable.setStatus("current")
_HpicfVsfVCMemberEntry_Object = MibTableRow
hpicfVsfVCMemberEntry = _HpicfVsfVCMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1)
)
hpicfVsfVCMemberEntry.setIndexNames(
    (0, "HP-VSF-VC-MIB", "hpicfVsfVCMemberId"),
)
if mibBuilder.loadTexts:
    hpicfVsfVCMemberEntry.setStatus("current")


class _HpicfVsfVCMemberId_Type(Integer32):
    """Custom type hpicfVsfVCMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfVsfVCMemberId_Type.__name__ = "Integer32"
_HpicfVsfVCMemberId_Object = MibTableColumn
hpicfVsfVCMemberId = _HpicfVsfVCMemberId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 1),
    _HpicfVsfVCMemberId_Type()
)
hpicfVsfVCMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberId.setStatus("current")
_HpicfVsfVCMemberProductId_Type = DisplayString
_HpicfVsfVCMemberProductId_Object = MibTableColumn
hpicfVsfVCMemberProductId = _HpicfVsfVCMemberProductId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 2),
    _HpicfVsfVCMemberProductId_Type()
)
hpicfVsfVCMemberProductId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberProductId.setStatus("current")


class _HpicfVsfVCMemberMacAddr_Type(OctetString):
    """Custom type hpicfVsfVCMemberMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_HpicfVsfVCMemberMacAddr_Type.__name__ = "OctetString"
_HpicfVsfVCMemberMacAddr_Object = MibTableColumn
hpicfVsfVCMemberMacAddr = _HpicfVsfVCMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 3),
    _HpicfVsfVCMemberMacAddr_Type()
)
hpicfVsfVCMemberMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberMacAddr.setStatus("current")
_HpicfVsfVCMemberShutdown_Type = TruthValue
_HpicfVsfVCMemberShutdown_Object = MibTableColumn
hpicfVsfVCMemberShutdown = _HpicfVsfVCMemberShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 4),
    _HpicfVsfVCMemberShutdown_Type()
)
hpicfVsfVCMemberShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberShutdown.setStatus("current")
_HpicfVsfVCMemberReboot_Type = TruthValue
_HpicfVsfVCMemberReboot_Object = MibTableColumn
hpicfVsfVCMemberReboot = _HpicfVsfVCMemberReboot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 5),
    _HpicfVsfVCMemberReboot_Type()
)
hpicfVsfVCMemberReboot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberReboot.setStatus("current")


class _HpicfVsfVCMemberAdminPriority_Type(Integer32):
    """Custom type hpicfVsfVCMemberAdminPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfVsfVCMemberAdminPriority_Type.__name__ = "Integer32"
_HpicfVsfVCMemberAdminPriority_Object = MibTableColumn
hpicfVsfVCMemberAdminPriority = _HpicfVsfVCMemberAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 6),
    _HpicfVsfVCMemberAdminPriority_Type()
)
hpicfVsfVCMemberAdminPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberAdminPriority.setStatus("current")
_HpicfVsfVCMemberEntryStatus_Type = RowStatus
_HpicfVsfVCMemberEntryStatus_Object = MibTableColumn
hpicfVsfVCMemberEntryStatus = _HpicfVsfVCMemberEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 7),
    _HpicfVsfVCMemberEntryStatus_Type()
)
hpicfVsfVCMemberEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberEntryStatus.setStatus("current")
_HpicfVsfVCMemberEntPhysicalIndex_Type = PhysicalIndex
_HpicfVsfVCMemberEntPhysicalIndex_Object = MibTableColumn
hpicfVsfVCMemberEntPhysicalIndex = _HpicfVsfVCMemberEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 8),
    _HpicfVsfVCMemberEntPhysicalIndex_Type()
)
hpicfVsfVCMemberEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberEntPhysicalIndex.setStatus("current")


class _HpicfVsfVCMemberState_Type(Integer32):
    """Custom type hpicfVsfVCMemberState based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("booting", 7),
          ("commander", 3),
          ("communicationFailure", 8),
          ("incompatibleOS", 9),
          ("member", 5),
          ("missing", 1),
          ("provision", 2),
          ("shutdown", 6),
          ("standby", 4),
          ("standbyBooting", 11),
          ("unknownState", 10),
          ("unusedId", 0))
    )


_HpicfVsfVCMemberState_Type.__name__ = "Integer32"
_HpicfVsfVCMemberState_Object = MibTableColumn
hpicfVsfVCMemberState = _HpicfVsfVCMemberState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 9),
    _HpicfVsfVCMemberState_Type()
)
hpicfVsfVCMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberState.setStatus("current")
_HpicfVsfVCMemberProductName_Type = SnmpAdminString
_HpicfVsfVCMemberProductName_Object = MibTableColumn
hpicfVsfVCMemberProductName = _HpicfVsfVCMemberProductName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 10),
    _HpicfVsfVCMemberProductName_Type()
)
hpicfVsfVCMemberProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberProductName.setStatus("current")
_HpicfVsfVCMemberUpTime_Type = TimeTicks
_HpicfVsfVCMemberUpTime_Object = MibTableColumn
hpicfVsfVCMemberUpTime = _HpicfVsfVCMemberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 11),
    _HpicfVsfVCMemberUpTime_Type()
)
hpicfVsfVCMemberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberUpTime.setStatus("current")
_HpicfVsfVCMemberSysOid_Type = ObjectIdentifier
_HpicfVsfVCMemberSysOid_Object = MibTableColumn
hpicfVsfVCMemberSysOid = _HpicfVsfVCMemberSysOid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 12),
    _HpicfVsfVCMemberSysOid_Type()
)
hpicfVsfVCMemberSysOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberSysOid.setStatus("current")
_HpicfVsfVCMemberIdForTrap_Type = Integer32
_HpicfVsfVCMemberIdForTrap_Object = MibTableColumn
hpicfVsfVCMemberIdForTrap = _HpicfVsfVCMemberIdForTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 13),
    _HpicfVsfVCMemberIdForTrap_Type()
)
hpicfVsfVCMemberIdForTrap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberIdForTrap.setStatus("current")
_HpicfVsfVCMemberSerialNum_Type = DisplayString
_HpicfVsfVCMemberSerialNum_Object = MibTableColumn
hpicfVsfVCMemberSerialNum = _HpicfVsfVCMemberSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 14),
    _HpicfVsfVCMemberSerialNum_Type()
)
hpicfVsfVCMemberSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberSerialNum.setStatus("current")
_HpicfVsfVCMemberBootRomVersion_Type = DisplayString
_HpicfVsfVCMemberBootRomVersion_Object = MibTableColumn
hpicfVsfVCMemberBootRomVersion = _HpicfVsfVCMemberBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 15),
    _HpicfVsfVCMemberBootRomVersion_Type()
)
hpicfVsfVCMemberBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberBootRomVersion.setStatus("current")
_HpicfVsfVCMemberOsVersion_Type = DisplayString
_HpicfVsfVCMemberOsVersion_Object = MibTableColumn
hpicfVsfVCMemberOsVersion = _HpicfVsfVCMemberOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 16),
    _HpicfVsfVCMemberOsVersion_Type()
)
hpicfVsfVCMemberOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberOsVersion.setStatus("current")


class _HpicfVsfVCMemberBootImage_Type(Integer32):
    """Custom type hpicfVsfVCMemberBootImage based on Integer32"""
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


_HpicfVsfVCMemberBootImage_Type.__name__ = "Integer32"
_HpicfVsfVCMemberBootImage_Object = MibTableColumn
hpicfVsfVCMemberBootImage = _HpicfVsfVCMemberBootImage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 17),
    _HpicfVsfVCMemberBootImage_Type()
)
hpicfVsfVCMemberBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberBootImage.setStatus("current")
_HpicfVsfVCMemberRenumber_Type = Integer32
_HpicfVsfVCMemberRenumber_Object = MibTableColumn
hpicfVsfVCMemberRenumber = _HpicfVsfVCMemberRenumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 18),
    _HpicfVsfVCMemberRenumber_Type()
)
hpicfVsfVCMemberRenumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberRenumber.setStatus("current")
_HpicfVsfVCMemberCpuUtil_Type = Integer32
_HpicfVsfVCMemberCpuUtil_Object = MibTableColumn
hpicfVsfVCMemberCpuUtil = _HpicfVsfVCMemberCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 19),
    _HpicfVsfVCMemberCpuUtil_Type()
)
hpicfVsfVCMemberCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberCpuUtil.setStatus("current")
_HpicfVsfVCMemberTotalMemory_Type = Integer32
_HpicfVsfVCMemberTotalMemory_Object = MibTableColumn
hpicfVsfVCMemberTotalMemory = _HpicfVsfVCMemberTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 20),
    _HpicfVsfVCMemberTotalMemory_Type()
)
hpicfVsfVCMemberTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberTotalMemory.setStatus("current")
_HpicfVsfVCMemberFreeMemory_Type = Integer32
_HpicfVsfVCMemberFreeMemory_Object = MibTableColumn
hpicfVsfVCMemberFreeMemory = _HpicfVsfVCMemberFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 3, 1, 21),
    _HpicfVsfVCMemberFreeMemory_Type()
)
hpicfVsfVCMemberFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCMemberFreeMemory.setStatus("current")
_HpicfVsfVCLinkTable_Object = MibTable
hpicfVsfVCLinkTable = _HpicfVsfVCLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfVsfVCLinkTable.setStatus("current")
_HpicfVsfVCLinkEntry_Object = MibTableRow
hpicfVsfVCLinkEntry = _HpicfVsfVCLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1)
)
hpicfVsfVCLinkEntry.setIndexNames(
    (0, "HP-VSF-VC-MIB", "hpicfVsfVCLinkMemberId"),
    (0, "HP-VSF-VC-MIB", "hpicfVsfVCLinkId"),
)
if mibBuilder.loadTexts:
    hpicfVsfVCLinkEntry.setStatus("current")


class _HpicfVsfVCLinkMemberId_Type(Integer32):
    """Custom type hpicfVsfVCLinkMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfVsfVCLinkMemberId_Type.__name__ = "Integer32"
_HpicfVsfVCLinkMemberId_Object = MibTableColumn
hpicfVsfVCLinkMemberId = _HpicfVsfVCLinkMemberId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 1),
    _HpicfVsfVCLinkMemberId_Type()
)
hpicfVsfVCLinkMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkMemberId.setStatus("current")


class _HpicfVsfVCLinkId_Type(Integer32):
    """Custom type hpicfVsfVCLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HpicfVsfVCLinkId_Type.__name__ = "Integer32"
_HpicfVsfVCLinkId_Object = MibTableColumn
hpicfVsfVCLinkId = _HpicfVsfVCLinkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 2),
    _HpicfVsfVCLinkId_Type()
)
hpicfVsfVCLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkId.setStatus("current")


class _HpicfVsfVCLinkName_Type(DisplayString):
    """Custom type hpicfVsfVCLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpicfVsfVCLinkName_Type.__name__ = "DisplayString"
_HpicfVsfVCLinkName_Object = MibTableColumn
hpicfVsfVCLinkName = _HpicfVsfVCLinkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 3),
    _HpicfVsfVCLinkName_Type()
)
hpicfVsfVCLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkName.setStatus("current")


class _HpicfVsfVCLinkOperStatus_Type(Integer32):
    """Custom type hpicfVsfVCLinkOperStatus based on Integer32"""
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
          ("down", 2),
          ("up", 1))
    )


_HpicfVsfVCLinkOperStatus_Type.__name__ = "Integer32"
_HpicfVsfVCLinkOperStatus_Object = MibTableColumn
hpicfVsfVCLinkOperStatus = _HpicfVsfVCLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 4),
    _HpicfVsfVCLinkOperStatus_Type()
)
hpicfVsfVCLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkOperStatus.setStatus("current")
_HpicfVsfVCPeerMemberId_Type = Integer32
_HpicfVsfVCPeerMemberId_Object = MibTableColumn
hpicfVsfVCPeerMemberId = _HpicfVsfVCPeerMemberId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 5),
    _HpicfVsfVCPeerMemberId_Type()
)
hpicfVsfVCPeerMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCPeerMemberId.setStatus("current")
_HpicfVsfVCPeerLinkId_Type = Integer32
_HpicfVsfVCPeerLinkId_Object = MibTableColumn
hpicfVsfVCPeerLinkId = _HpicfVsfVCPeerLinkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 6),
    _HpicfVsfVCPeerLinkId_Type()
)
hpicfVsfVCPeerLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCPeerLinkId.setStatus("current")
_HpicfVsfVCLinkPortList_Type = PortList
_HpicfVsfVCLinkPortList_Object = MibTableColumn
hpicfVsfVCLinkPortList = _HpicfVsfVCLinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 7),
    _HpicfVsfVCLinkPortList_Type()
)
hpicfVsfVCLinkPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkPortList.setStatus("current")
_HpicfVsfVCLinkEntryStatus_Type = RowStatus
_HpicfVsfVCLinkEntryStatus_Object = MibTableColumn
hpicfVsfVCLinkEntryStatus = _HpicfVsfVCLinkEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 8),
    _HpicfVsfVCLinkEntryStatus_Type()
)
hpicfVsfVCLinkEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkEntryStatus.setStatus("current")
_HpicfVsfVCLinkIdForTrap_Type = Integer32
_HpicfVsfVCLinkIdForTrap_Object = MibTableColumn
hpicfVsfVCLinkIdForTrap = _HpicfVsfVCLinkIdForTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 9),
    _HpicfVsfVCLinkIdForTrap_Type()
)
hpicfVsfVCLinkIdForTrap.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkIdForTrap.setStatus("current")


class _HpicfVsfVCLinkPortStartState_Type(Integer32):
    """Custom type hpicfVsfVCLinkPortStartState based on Integer32"""
    defaultValue = 1

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


_HpicfVsfVCLinkPortStartState_Type.__name__ = "Integer32"
_HpicfVsfVCLinkPortStartState_Object = MibTableColumn
hpicfVsfVCLinkPortStartState = _HpicfVsfVCLinkPortStartState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 4, 1, 10),
    _HpicfVsfVCLinkPortStartState_Type()
)
hpicfVsfVCLinkPortStartState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfVsfVCLinkPortStartState.setStatus("current")
_HpicfVsfVCPortTable_Object = MibTable
hpicfVsfVCPortTable = _HpicfVsfVCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfVsfVCPortTable.setStatus("current")
_HpicfVsfVCPortEntry_Object = MibTableRow
hpicfVsfVCPortEntry = _HpicfVsfVCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 5, 1)
)
hpicfVsfVCPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfVsfVCPortEntry.setStatus("current")


class _HpicfVsfVCPortOperStatus_Type(Integer32):
    """Custom type hpicfVsfVCPortOperStatus based on Integer32"""
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
        *(("disabled", 4),
          ("down", 2),
          ("error", 3),
          ("provisioned", 5),
          ("up", 1))
    )


_HpicfVsfVCPortOperStatus_Type.__name__ = "Integer32"
_HpicfVsfVCPortOperStatus_Object = MibTableColumn
hpicfVsfVCPortOperStatus = _HpicfVsfVCPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 5, 1, 1),
    _HpicfVsfVCPortOperStatus_Type()
)
hpicfVsfVCPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCPortOperStatus.setStatus("current")
_HpicfVsfVCPortOperStatusErrorStr_Type = DisplayString
_HpicfVsfVCPortOperStatusErrorStr_Object = MibTableColumn
hpicfVsfVCPortOperStatusErrorStr = _HpicfVsfVCPortOperStatusErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 1, 5, 1, 2),
    _HpicfVsfVCPortOperStatusErrorStr_Type()
)
hpicfVsfVCPortOperStatusErrorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfVsfVCPortOperStatusErrorStr.setStatus("current")
_HpicfVsfVCConformance_ObjectIdentity = ObjectIdentity
hpicfVsfVCConformance = _HpicfVsfVCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2)
)
_HpicfVsfVCCompliances_ObjectIdentity = ObjectIdentity
hpicfVsfVCCompliances = _HpicfVsfVCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 1)
)
_HpicfVsfVCGroups_ObjectIdentity = ObjectIdentity
hpicfVsfVCGroups = _HpicfVsfVCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2)
)

# Managed Objects groups

hpicfVsfVCConfigScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 1)
)
hpicfVsfVCConfigScalarGroup.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCDomainId"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCOperStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCAdminStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCTopology"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCTrapEnable"),
        ("HP-VSF-VC-MIB", "hpicfVsfLldpMADEnable"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCOobmMADEnable"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADDeviceIpType"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADDeviceIpAddr"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADSnmpVersion"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADSnmpCommunity"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCConfigScalarGroup.setStatus("deprecated")

hpicfVsfVCMemberTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 2)
)
hpicfVsfVCMemberTableGroup.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCMemberProductId"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberMacAddr"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberShutdown"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberReboot"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberAdminPriority"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberEntryStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberEntPhysicalIndex"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberState"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberProductName"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberUpTime"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberSysOid"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberIdForTrap"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberSerialNum"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberBootRomVersion"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberOsVersion"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberBootImage"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberRenumber"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberCpuUtil"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberTotalMemory"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberFreeMemory"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCMemberTableGroup.setStatus("current")

hpicfVsfVCLinkTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 3)
)
hpicfVsfVCLinkTableGroup.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCLinkName"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLinkOperStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCPeerMemberId"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCPeerLinkId"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLinkPortList"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLinkEntryStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLinkIdForTrap"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLinkPortStartState"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCLinkTableGroup.setStatus("current")

hpicfVsfVCStatusScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 5)
)
hpicfVsfVCStatusScalarGroup.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADReadinessStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADDeviceMAC"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADVlanId"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADTrunkIfIndex"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADProbePortSet"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADConnectivity"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADSplitStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADProbeOriginator"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADProbeRequestsSent"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADProbeResponseRcvd"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADActiveFragment"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCStatusScalarGroup.setStatus("current")

hpicfVsfVCPortTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 6)
)
hpicfVsfVCPortTableGroup.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCPortOperStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCPortOperStatusErrorStr"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCPortTableGroup.setStatus("current")

hpicfVsfVCConfigScalarGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 7)
)
hpicfVsfVCConfigScalarGroup1.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCDomainId"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCOperStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCAdminStatus"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCTopology"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCTrapEnable"),
        ("HP-VSF-VC-MIB", "hpicfVsfLldpMADEnable"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCOobmMADEnable"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADDeviceIpType"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADDeviceIpAddr"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADSnmpVersion"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCLldpMADSnmpCommunity"),
        ("HP-VSF-VC-MIB", "hpicfVsfMADVlan"),
        ("HP-VSF-VC-MIB", "hpicfVsfMADVlanConnectivity"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCPortSpeed"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCConfigScalarGroup1.setStatus("current")


# Notification objects

hpicfVsfVCCommanderChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 0, 2)
)
hpicfVsfVCCommanderChange.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCMemberIdForTrap"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberState"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCCommanderChange.setStatus(
        "current"
    )

hpicfVsfVCMemberChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 0, 3)
)
hpicfVsfVCMemberChange.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCMemberIdForTrap"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberState"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCMemberChange.setStatus(
        "current"
    )

hpicfVsfVCMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 0, 4)
)
hpicfVsfVCMemberStatusChange.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCMemberIdForTrap"),
        ("NETSWITCH-MIB", "hpSwitchBaseMACAddress"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberState"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCMemberStatusChange.setStatus(
        "current"
    )


# Notifications groups

hpicfVsfVCNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 2, 4)
)
hpicfVsfVCNotificationsGroup.setObjects(
      *(("HP-VSF-VC-MIB", "hpicfVsfVCCommanderChange"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberChange"),
        ("HP-VSF-VC-MIB", "hpicfVsfVCMemberStatusChange"))
)
if mibBuilder.loadTexts:
    hpicfVsfVCNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfVsfVCMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVsfVCMibCompliance.setStatus(
        "deprecated"
    )

hpicfVsfVCMibCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfVsfVCMibCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-VSF-VC-MIB",
    **{"hpicfVsfVCMIB": hpicfVsfVCMIB,
       "hpicfVsfVCNotifications": hpicfVsfVCNotifications,
       "hpicfVsfVCCommanderChange": hpicfVsfVCCommanderChange,
       "hpicfVsfVCMemberChange": hpicfVsfVCMemberChange,
       "hpicfVsfVCMemberStatusChange": hpicfVsfVCMemberStatusChange,
       "hpicfVsfVCObjects": hpicfVsfVCObjects,
       "hpicfVsfVCConfig": hpicfVsfVCConfig,
       "hpicfVsfVCDomainId": hpicfVsfVCDomainId,
       "hpicfVsfVCOperStatus": hpicfVsfVCOperStatus,
       "hpicfVsfVCAdminStatus": hpicfVsfVCAdminStatus,
       "hpicfVsfVCTopology": hpicfVsfVCTopology,
       "hpicfVsfVCTrapEnable": hpicfVsfVCTrapEnable,
       "hpicfVsfVCOobmMADEnable": hpicfVsfVCOobmMADEnable,
       "hpicfVsfLldpMADEnable": hpicfVsfLldpMADEnable,
       "hpicfVsfVCLldpMADDeviceIpType": hpicfVsfVCLldpMADDeviceIpType,
       "hpicfVsfVCLldpMADDeviceIpAddr": hpicfVsfVCLldpMADDeviceIpAddr,
       "hpicfVsfVCLldpMADSnmpVersion": hpicfVsfVCLldpMADSnmpVersion,
       "hpicfVsfVCLldpMADSnmpCommunity": hpicfVsfVCLldpMADSnmpCommunity,
       "hpicfVsfMADVlan": hpicfVsfMADVlan,
       "hpicfVsfMADVlanConnectivity": hpicfVsfMADVlanConnectivity,
       "hpicfVsfVCPortSpeed": hpicfVsfVCPortSpeed,
       "hpicfVsfVCStatus": hpicfVsfVCStatus,
       "hpicfVsfVCLldpMADReadinessStatus": hpicfVsfVCLldpMADReadinessStatus,
       "hpicfVsfVCLldpMADDeviceMAC": hpicfVsfVCLldpMADDeviceMAC,
       "hpicfVsfVCLldpMADVlanId": hpicfVsfVCLldpMADVlanId,
       "hpicfVsfVCLldpMADTrunkIfIndex": hpicfVsfVCLldpMADTrunkIfIndex,
       "hpicfVsfVCLldpMADProbePortSet": hpicfVsfVCLldpMADProbePortSet,
       "hpicfVsfVCLldpMADConnectivity": hpicfVsfVCLldpMADConnectivity,
       "hpicfVsfVCLldpMADSplitStatus": hpicfVsfVCLldpMADSplitStatus,
       "hpicfVsfVCLldpMADProbeOriginator": hpicfVsfVCLldpMADProbeOriginator,
       "hpicfVsfVCLldpMADProbeRequestsSent": hpicfVsfVCLldpMADProbeRequestsSent,
       "hpicfVsfVCLldpMADProbeResponseRcvd": hpicfVsfVCLldpMADProbeResponseRcvd,
       "hpicfVsfVCLldpMADActiveFragment": hpicfVsfVCLldpMADActiveFragment,
       "hpicfVsfVCMemberTable": hpicfVsfVCMemberTable,
       "hpicfVsfVCMemberEntry": hpicfVsfVCMemberEntry,
       "hpicfVsfVCMemberId": hpicfVsfVCMemberId,
       "hpicfVsfVCMemberProductId": hpicfVsfVCMemberProductId,
       "hpicfVsfVCMemberMacAddr": hpicfVsfVCMemberMacAddr,
       "hpicfVsfVCMemberShutdown": hpicfVsfVCMemberShutdown,
       "hpicfVsfVCMemberReboot": hpicfVsfVCMemberReboot,
       "hpicfVsfVCMemberAdminPriority": hpicfVsfVCMemberAdminPriority,
       "hpicfVsfVCMemberEntryStatus": hpicfVsfVCMemberEntryStatus,
       "hpicfVsfVCMemberEntPhysicalIndex": hpicfVsfVCMemberEntPhysicalIndex,
       "hpicfVsfVCMemberState": hpicfVsfVCMemberState,
       "hpicfVsfVCMemberProductName": hpicfVsfVCMemberProductName,
       "hpicfVsfVCMemberUpTime": hpicfVsfVCMemberUpTime,
       "hpicfVsfVCMemberSysOid": hpicfVsfVCMemberSysOid,
       "hpicfVsfVCMemberIdForTrap": hpicfVsfVCMemberIdForTrap,
       "hpicfVsfVCMemberSerialNum": hpicfVsfVCMemberSerialNum,
       "hpicfVsfVCMemberBootRomVersion": hpicfVsfVCMemberBootRomVersion,
       "hpicfVsfVCMemberOsVersion": hpicfVsfVCMemberOsVersion,
       "hpicfVsfVCMemberBootImage": hpicfVsfVCMemberBootImage,
       "hpicfVsfVCMemberRenumber": hpicfVsfVCMemberRenumber,
       "hpicfVsfVCMemberCpuUtil": hpicfVsfVCMemberCpuUtil,
       "hpicfVsfVCMemberTotalMemory": hpicfVsfVCMemberTotalMemory,
       "hpicfVsfVCMemberFreeMemory": hpicfVsfVCMemberFreeMemory,
       "hpicfVsfVCLinkTable": hpicfVsfVCLinkTable,
       "hpicfVsfVCLinkEntry": hpicfVsfVCLinkEntry,
       "hpicfVsfVCLinkMemberId": hpicfVsfVCLinkMemberId,
       "hpicfVsfVCLinkId": hpicfVsfVCLinkId,
       "hpicfVsfVCLinkName": hpicfVsfVCLinkName,
       "hpicfVsfVCLinkOperStatus": hpicfVsfVCLinkOperStatus,
       "hpicfVsfVCPeerMemberId": hpicfVsfVCPeerMemberId,
       "hpicfVsfVCPeerLinkId": hpicfVsfVCPeerLinkId,
       "hpicfVsfVCLinkPortList": hpicfVsfVCLinkPortList,
       "hpicfVsfVCLinkEntryStatus": hpicfVsfVCLinkEntryStatus,
       "hpicfVsfVCLinkIdForTrap": hpicfVsfVCLinkIdForTrap,
       "hpicfVsfVCLinkPortStartState": hpicfVsfVCLinkPortStartState,
       "hpicfVsfVCPortTable": hpicfVsfVCPortTable,
       "hpicfVsfVCPortEntry": hpicfVsfVCPortEntry,
       "hpicfVsfVCPortOperStatus": hpicfVsfVCPortOperStatus,
       "hpicfVsfVCPortOperStatusErrorStr": hpicfVsfVCPortOperStatusErrorStr,
       "hpicfVsfVCConformance": hpicfVsfVCConformance,
       "hpicfVsfVCCompliances": hpicfVsfVCCompliances,
       "hpicfVsfVCMibCompliance": hpicfVsfVCMibCompliance,
       "hpicfVsfVCMibCompliance1": hpicfVsfVCMibCompliance1,
       "hpicfVsfVCGroups": hpicfVsfVCGroups,
       "hpicfVsfVCConfigScalarGroup": hpicfVsfVCConfigScalarGroup,
       "hpicfVsfVCMemberTableGroup": hpicfVsfVCMemberTableGroup,
       "hpicfVsfVCLinkTableGroup": hpicfVsfVCLinkTableGroup,
       "hpicfVsfVCNotificationsGroup": hpicfVsfVCNotificationsGroup,
       "hpicfVsfVCStatusScalarGroup": hpicfVsfVCStatusScalarGroup,
       "hpicfVsfVCPortTableGroup": hpicfVsfVCPortTableGroup,
       "hpicfVsfVCConfigScalarGroup1": hpicfVsfVCConfigScalarGroup1}
)
