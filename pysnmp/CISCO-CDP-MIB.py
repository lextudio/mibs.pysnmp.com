# SNMP MIB module (CISCO-CDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:14 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoNetworkAddress,
 CiscoNetworkProtocol) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoNetworkAddress",
    "CiscoNetworkProtocol")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23)
)
ciscoCdpMIB.setRevisions(
        ("2005-03-21 00:00",
         "2005-03-14 00:00",
         "2001-11-23 00:00",
         "2001-04-23 00:00",
         "2000-11-22 00:00",
         "1998-12-10 00:00",
         "1998-09-16 00:00",
         "1996-07-08 00:00",
         "1995-08-15 00:00",
         "1995-07-27 00:00",
         "1995-01-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdpMIBObjects = _CiscoCdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1)
)
_CdpInterface_ObjectIdentity = ObjectIdentity
cdpInterface = _CdpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1)
)
_CdpInterfaceTable_Object = MibTable
cdpInterfaceTable = _CdpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdpInterfaceTable.setStatus("current")
_CdpInterfaceEntry_Object = MibTableRow
cdpInterfaceEntry = _CdpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1)
)
cdpInterfaceEntry.setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    cdpInterfaceEntry.setStatus("current")


class _CdpInterfaceIfIndex_Type(Integer32):
    """Custom type cdpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdpInterfaceIfIndex_Type.__name__ = "Integer32"
_CdpInterfaceIfIndex_Object = MibTableColumn
cdpInterfaceIfIndex = _CdpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 1),
    _CdpInterfaceIfIndex_Type()
)
cdpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpInterfaceIfIndex.setStatus("current")
_CdpInterfaceEnable_Type = TruthValue
_CdpInterfaceEnable_Object = MibTableColumn
cdpInterfaceEnable = _CdpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 2),
    _CdpInterfaceEnable_Type()
)
cdpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpInterfaceEnable.setStatus("current")


class _CdpInterfaceMessageInterval_Type(Integer32):
    """Custom type cdpInterfaceMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_CdpInterfaceMessageInterval_Type.__name__ = "Integer32"
_CdpInterfaceMessageInterval_Object = MibTableColumn
cdpInterfaceMessageInterval = _CdpInterfaceMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 3),
    _CdpInterfaceMessageInterval_Type()
)
cdpInterfaceMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpInterfaceMessageInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    cdpInterfaceMessageInterval.setUnits("seconds")
_CdpInterfaceGroup_Type = Integer32
_CdpInterfaceGroup_Object = MibTableColumn
cdpInterfaceGroup = _CdpInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 4),
    _CdpInterfaceGroup_Type()
)
cdpInterfaceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpInterfaceGroup.setStatus("current")
_CdpInterfacePort_Type = Integer32
_CdpInterfacePort_Object = MibTableColumn
cdpInterfacePort = _CdpInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 5),
    _CdpInterfacePort_Type()
)
cdpInterfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpInterfacePort.setStatus("current")
_CdpInterfaceName_Type = DisplayString
_CdpInterfaceName_Object = MibTableColumn
cdpInterfaceName = _CdpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 6),
    _CdpInterfaceName_Type()
)
cdpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpInterfaceName.setStatus("current")
_CdpInterfaceExtTable_Object = MibTable
cdpInterfaceExtTable = _CdpInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cdpInterfaceExtTable.setStatus("current")
_CdpInterfaceExtEntry_Object = MibTableRow
cdpInterfaceExtEntry = _CdpInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1)
)
cdpInterfaceExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cdpInterfaceExtEntry.setStatus("current")


class _CdpInterfaceExtendedTrust_Type(Integer32):
    """Custom type cdpInterfaceExtendedTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTrust", 2),
          ("trusted", 1))
    )


_CdpInterfaceExtendedTrust_Type.__name__ = "Integer32"
_CdpInterfaceExtendedTrust_Object = MibTableColumn
cdpInterfaceExtendedTrust = _CdpInterfaceExtendedTrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1, 1),
    _CdpInterfaceExtendedTrust_Type()
)
cdpInterfaceExtendedTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpInterfaceExtendedTrust.setStatus("current")


class _CdpInterfaceCosForUntrustedPort_Type(Unsigned32):
    """Custom type cdpInterfaceCosForUntrustedPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CdpInterfaceCosForUntrustedPort_Type.__name__ = "Unsigned32"
_CdpInterfaceCosForUntrustedPort_Object = MibTableColumn
cdpInterfaceCosForUntrustedPort = _CdpInterfaceCosForUntrustedPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1, 2),
    _CdpInterfaceCosForUntrustedPort_Type()
)
cdpInterfaceCosForUntrustedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpInterfaceCosForUntrustedPort.setStatus("current")
_CdpCache_ObjectIdentity = ObjectIdentity
cdpCache = _CdpCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2)
)
_CdpCacheTable_Object = MibTable
cdpCacheTable = _CdpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdpCacheTable.setStatus("current")
_CdpCacheEntry_Object = MibTableRow
cdpCacheEntry = _CdpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1)
)
cdpCacheEntry.setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"),
    (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    cdpCacheEntry.setStatus("current")


class _CdpCacheIfIndex_Type(Integer32):
    """Custom type cdpCacheIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdpCacheIfIndex_Type.__name__ = "Integer32"
_CdpCacheIfIndex_Object = MibTableColumn
cdpCacheIfIndex = _CdpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 1),
    _CdpCacheIfIndex_Type()
)
cdpCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpCacheIfIndex.setStatus("current")


class _CdpCacheDeviceIndex_Type(Integer32):
    """Custom type cdpCacheDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CdpCacheDeviceIndex_Type.__name__ = "Integer32"
_CdpCacheDeviceIndex_Object = MibTableColumn
cdpCacheDeviceIndex = _CdpCacheDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 2),
    _CdpCacheDeviceIndex_Type()
)
cdpCacheDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpCacheDeviceIndex.setStatus("current")
_CdpCacheAddressType_Type = CiscoNetworkProtocol
_CdpCacheAddressType_Object = MibTableColumn
cdpCacheAddressType = _CdpCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 3),
    _CdpCacheAddressType_Type()
)
cdpCacheAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheAddressType.setStatus("current")
_CdpCacheAddress_Type = CiscoNetworkAddress
_CdpCacheAddress_Object = MibTableColumn
cdpCacheAddress = _CdpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 4),
    _CdpCacheAddress_Type()
)
cdpCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheAddress.setStatus("current")
_CdpCacheVersion_Type = DisplayString
_CdpCacheVersion_Object = MibTableColumn
cdpCacheVersion = _CdpCacheVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 5),
    _CdpCacheVersion_Type()
)
cdpCacheVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheVersion.setStatus("current")
_CdpCacheDeviceId_Type = DisplayString
_CdpCacheDeviceId_Object = MibTableColumn
cdpCacheDeviceId = _CdpCacheDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 6),
    _CdpCacheDeviceId_Type()
)
cdpCacheDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheDeviceId.setStatus("current")
_CdpCacheDevicePort_Type = DisplayString
_CdpCacheDevicePort_Object = MibTableColumn
cdpCacheDevicePort = _CdpCacheDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 7),
    _CdpCacheDevicePort_Type()
)
cdpCacheDevicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheDevicePort.setStatus("current")
_CdpCachePlatform_Type = DisplayString
_CdpCachePlatform_Object = MibTableColumn
cdpCachePlatform = _CdpCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 8),
    _CdpCachePlatform_Type()
)
cdpCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCachePlatform.setStatus("current")


class _CdpCacheCapabilities_Type(OctetString):
    """Custom type cdpCacheCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CdpCacheCapabilities_Type.__name__ = "OctetString"
_CdpCacheCapabilities_Object = MibTableColumn
cdpCacheCapabilities = _CdpCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 9),
    _CdpCacheCapabilities_Type()
)
cdpCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheCapabilities.setStatus("current")


class _CdpCacheVTPMgmtDomain_Type(DisplayString):
    """Custom type cdpCacheVTPMgmtDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CdpCacheVTPMgmtDomain_Type.__name__ = "DisplayString"
_CdpCacheVTPMgmtDomain_Object = MibTableColumn
cdpCacheVTPMgmtDomain = _CdpCacheVTPMgmtDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 10),
    _CdpCacheVTPMgmtDomain_Type()
)
cdpCacheVTPMgmtDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheVTPMgmtDomain.setStatus("current")
_CdpCacheNativeVLAN_Type = VlanIndex
_CdpCacheNativeVLAN_Object = MibTableColumn
cdpCacheNativeVLAN = _CdpCacheNativeVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 11),
    _CdpCacheNativeVLAN_Type()
)
cdpCacheNativeVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheNativeVLAN.setStatus("current")


class _CdpCacheDuplex_Type(Integer32):
    """Custom type cdpCacheDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 3),
          ("halfduplex", 2),
          ("unknown", 1))
    )


_CdpCacheDuplex_Type.__name__ = "Integer32"
_CdpCacheDuplex_Object = MibTableColumn
cdpCacheDuplex = _CdpCacheDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 12),
    _CdpCacheDuplex_Type()
)
cdpCacheDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheDuplex.setStatus("current")


class _CdpCacheApplianceID_Type(Unsigned32):
    """Custom type cdpCacheApplianceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdpCacheApplianceID_Type.__name__ = "Unsigned32"
_CdpCacheApplianceID_Object = MibTableColumn
cdpCacheApplianceID = _CdpCacheApplianceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 13),
    _CdpCacheApplianceID_Type()
)
cdpCacheApplianceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheApplianceID.setStatus("current")


class _CdpCacheVlanID_Type(Unsigned32):
    """Custom type cdpCacheVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CdpCacheVlanID_Type.__name__ = "Unsigned32"
_CdpCacheVlanID_Object = MibTableColumn
cdpCacheVlanID = _CdpCacheVlanID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 14),
    _CdpCacheVlanID_Type()
)
cdpCacheVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheVlanID.setStatus("current")
_CdpCachePowerConsumption_Type = Unsigned32
_CdpCachePowerConsumption_Object = MibTableColumn
cdpCachePowerConsumption = _CdpCachePowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 15),
    _CdpCachePowerConsumption_Type()
)
cdpCachePowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCachePowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    cdpCachePowerConsumption.setUnits("milliwatts")
_CdpCacheMTU_Type = Unsigned32
_CdpCacheMTU_Object = MibTableColumn
cdpCacheMTU = _CdpCacheMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 16),
    _CdpCacheMTU_Type()
)
cdpCacheMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheMTU.setStatus("current")


class _CdpCacheSysName_Type(DisplayString):
    """Custom type cdpCacheSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdpCacheSysName_Type.__name__ = "DisplayString"
_CdpCacheSysName_Object = MibTableColumn
cdpCacheSysName = _CdpCacheSysName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 17),
    _CdpCacheSysName_Type()
)
cdpCacheSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheSysName.setStatus("current")
_CdpCacheSysObjectID_Type = ObjectIdentifier
_CdpCacheSysObjectID_Object = MibTableColumn
cdpCacheSysObjectID = _CdpCacheSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 18),
    _CdpCacheSysObjectID_Type()
)
cdpCacheSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheSysObjectID.setStatus("current")
_CdpCachePrimaryMgmtAddrType_Type = CiscoNetworkProtocol
_CdpCachePrimaryMgmtAddrType_Object = MibTableColumn
cdpCachePrimaryMgmtAddrType = _CdpCachePrimaryMgmtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 19),
    _CdpCachePrimaryMgmtAddrType_Type()
)
cdpCachePrimaryMgmtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCachePrimaryMgmtAddrType.setStatus("current")
_CdpCachePrimaryMgmtAddr_Type = CiscoNetworkAddress
_CdpCachePrimaryMgmtAddr_Object = MibTableColumn
cdpCachePrimaryMgmtAddr = _CdpCachePrimaryMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 20),
    _CdpCachePrimaryMgmtAddr_Type()
)
cdpCachePrimaryMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCachePrimaryMgmtAddr.setStatus("current")
_CdpCacheSecondaryMgmtAddrType_Type = CiscoNetworkProtocol
_CdpCacheSecondaryMgmtAddrType_Object = MibTableColumn
cdpCacheSecondaryMgmtAddrType = _CdpCacheSecondaryMgmtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 21),
    _CdpCacheSecondaryMgmtAddrType_Type()
)
cdpCacheSecondaryMgmtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheSecondaryMgmtAddrType.setStatus("current")
_CdpCacheSecondaryMgmtAddr_Type = CiscoNetworkAddress
_CdpCacheSecondaryMgmtAddr_Object = MibTableColumn
cdpCacheSecondaryMgmtAddr = _CdpCacheSecondaryMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 22),
    _CdpCacheSecondaryMgmtAddr_Type()
)
cdpCacheSecondaryMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheSecondaryMgmtAddr.setStatus("current")
_CdpCachePhysLocation_Type = DisplayString
_CdpCachePhysLocation_Object = MibTableColumn
cdpCachePhysLocation = _CdpCachePhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 23),
    _CdpCachePhysLocation_Type()
)
cdpCachePhysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCachePhysLocation.setStatus("current")
_CdpCacheLastChange_Type = TimeStamp
_CdpCacheLastChange_Object = MibTableColumn
cdpCacheLastChange = _CdpCacheLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 24),
    _CdpCacheLastChange_Type()
)
cdpCacheLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCacheLastChange.setStatus("current")
_CdpCtAddressTable_Object = MibTable
cdpCtAddressTable = _CdpCtAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdpCtAddressTable.setStatus("current")
_CdpCtAddressEntry_Object = MibTableRow
cdpCtAddressEntry = _CdpCtAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1)
)
cdpCtAddressEntry.setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"),
    (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"),
    (0, "CISCO-CDP-MIB", "cdpCtAddressIndex"),
)
if mibBuilder.loadTexts:
    cdpCtAddressEntry.setStatus("current")


class _CdpCtAddressIndex_Type(Integer32):
    """Custom type cdpCtAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CdpCtAddressIndex_Type.__name__ = "Integer32"
_CdpCtAddressIndex_Object = MibTableColumn
cdpCtAddressIndex = _CdpCtAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 3),
    _CdpCtAddressIndex_Type()
)
cdpCtAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdpCtAddressIndex.setStatus("current")
_CdpCtAddressType_Type = CiscoNetworkProtocol
_CdpCtAddressType_Object = MibTableColumn
cdpCtAddressType = _CdpCtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 4),
    _CdpCtAddressType_Type()
)
cdpCtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCtAddressType.setStatus("current")
_CdpCtAddress_Type = CiscoNetworkAddress
_CdpCtAddress_Object = MibTableColumn
cdpCtAddress = _CdpCtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 5),
    _CdpCtAddress_Type()
)
cdpCtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpCtAddress.setStatus("current")
_CdpGlobal_ObjectIdentity = ObjectIdentity
cdpGlobal = _CdpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3)
)


class _CdpGlobalRun_Type(TruthValue):
    """Custom type cdpGlobalRun based on TruthValue"""


_CdpGlobalRun_Object = MibScalar
cdpGlobalRun = _CdpGlobalRun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 1),
    _CdpGlobalRun_Type()
)
cdpGlobalRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpGlobalRun.setStatus("current")


class _CdpGlobalMessageInterval_Type(Integer32):
    """Custom type cdpGlobalMessageInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_CdpGlobalMessageInterval_Type.__name__ = "Integer32"
_CdpGlobalMessageInterval_Object = MibScalar
cdpGlobalMessageInterval = _CdpGlobalMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 2),
    _CdpGlobalMessageInterval_Type()
)
cdpGlobalMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpGlobalMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdpGlobalMessageInterval.setUnits("seconds")


class _CdpGlobalHoldTime_Type(Integer32):
    """Custom type cdpGlobalHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_CdpGlobalHoldTime_Type.__name__ = "Integer32"
_CdpGlobalHoldTime_Object = MibScalar
cdpGlobalHoldTime = _CdpGlobalHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 3),
    _CdpGlobalHoldTime_Type()
)
cdpGlobalHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpGlobalHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cdpGlobalHoldTime.setUnits("seconds")
_CdpGlobalDeviceId_Type = DisplayString
_CdpGlobalDeviceId_Object = MibScalar
cdpGlobalDeviceId = _CdpGlobalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 4),
    _CdpGlobalDeviceId_Type()
)
cdpGlobalDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpGlobalDeviceId.setStatus("current")
_CdpGlobalLastChange_Type = TimeStamp
_CdpGlobalLastChange_Object = MibScalar
cdpGlobalLastChange = _CdpGlobalLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 5),
    _CdpGlobalLastChange_Type()
)
cdpGlobalLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpGlobalLastChange.setStatus("current")


class _CdpGlobalDeviceIdFormatCpb_Type(Bits):
    """Custom type cdpGlobalDeviceIdFormatCpb based on Bits"""
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("other", 2),
          ("serialNumber", 0))
    )

_CdpGlobalDeviceIdFormatCpb_Type.__name__ = "Bits"
_CdpGlobalDeviceIdFormatCpb_Object = MibScalar
cdpGlobalDeviceIdFormatCpb = _CdpGlobalDeviceIdFormatCpb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 6),
    _CdpGlobalDeviceIdFormatCpb_Type()
)
cdpGlobalDeviceIdFormatCpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdpGlobalDeviceIdFormatCpb.setStatus("current")


class _CdpGlobalDeviceIdFormat_Type(Integer32):
    """Custom type cdpGlobalDeviceIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 2),
          ("other", 3),
          ("serialNumber", 1))
    )


_CdpGlobalDeviceIdFormat_Type.__name__ = "Integer32"
_CdpGlobalDeviceIdFormat_Object = MibScalar
cdpGlobalDeviceIdFormat = _CdpGlobalDeviceIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 7),
    _CdpGlobalDeviceIdFormat_Type()
)
cdpGlobalDeviceIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdpGlobalDeviceIdFormat.setStatus("current")
_CiscoCdpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCdpMIBConformance = _CiscoCdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2)
)
_CiscoCdpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdpMIBCompliances = _CiscoCdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1)
)
_CiscoCdpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdpMIBGroups = _CiscoCdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2)
)

# Managed Objects groups

ciscoCdpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 1)
)
ciscoCdpMIBGroup.setObjects(
      *(("CISCO-CDP-MIB", "cdpInterfaceEnable"),
        ("CISCO-CDP-MIB", "cdpInterfaceMessageInterval"),
        ("CISCO-CDP-MIB", "cdpCacheAddressType"),
        ("CISCO-CDP-MIB", "cdpCacheAddress"),
        ("CISCO-CDP-MIB", "cdpCacheVersion"),
        ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
        ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
        ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
        ("CISCO-CDP-MIB", "cdpCachePlatform"))
)
if mibBuilder.loadTexts:
    ciscoCdpMIBGroup.setStatus("obsolete")

ciscoCdpMIBGroupV11R01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 2)
)
ciscoCdpMIBGroupV11R01.setObjects(
      *(("CISCO-CDP-MIB", "cdpInterfaceEnable"),
        ("CISCO-CDP-MIB", "cdpInterfaceMessageInterval"),
        ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
        ("CISCO-CDP-MIB", "cdpInterfacePort"),
        ("CISCO-CDP-MIB", "cdpCacheAddressType"),
        ("CISCO-CDP-MIB", "cdpCacheAddress"),
        ("CISCO-CDP-MIB", "cdpCacheVersion"),
        ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
        ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
        ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
        ("CISCO-CDP-MIB", "cdpCachePlatform"))
)
if mibBuilder.loadTexts:
    ciscoCdpMIBGroupV11R01.setStatus("obsolete")

ciscoCdpMIBGroupV11R02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 3)
)
ciscoCdpMIBGroupV11R02.setObjects(
      *(("CISCO-CDP-MIB", "cdpInterfaceEnable"),
        ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
        ("CISCO-CDP-MIB", "cdpInterfacePort"),
        ("CISCO-CDP-MIB", "cdpCacheAddressType"),
        ("CISCO-CDP-MIB", "cdpCacheAddress"),
        ("CISCO-CDP-MIB", "cdpCacheVersion"),
        ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
        ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
        ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
        ("CISCO-CDP-MIB", "cdpCachePlatform"),
        ("CISCO-CDP-MIB", "cdpGlobalRun"),
        ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"),
        ("CISCO-CDP-MIB", "cdpGlobalHoldTime"))
)
if mibBuilder.loadTexts:
    ciscoCdpMIBGroupV11R02.setStatus("obsolete")

ciscoCdpMIBGroupV12R02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 5)
)
ciscoCdpMIBGroupV12R02.setObjects(
      *(("CISCO-CDP-MIB", "cdpInterfaceEnable"),
        ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
        ("CISCO-CDP-MIB", "cdpInterfacePort"),
        ("CISCO-CDP-MIB", "cdpCacheAddressType"),
        ("CISCO-CDP-MIB", "cdpCacheAddress"),
        ("CISCO-CDP-MIB", "cdpCacheVersion"),
        ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
        ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
        ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
        ("CISCO-CDP-MIB", "cdpCachePlatform"),
        ("CISCO-CDP-MIB", "cdpCacheVTPMgmtDomain"),
        ("CISCO-CDP-MIB", "cdpCacheNativeVLAN"),
        ("CISCO-CDP-MIB", "cdpCacheDuplex"),
        ("CISCO-CDP-MIB", "cdpGlobalRun"),
        ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"),
        ("CISCO-CDP-MIB", "cdpGlobalHoldTime"),
        ("CISCO-CDP-MIB", "cdpGlobalDeviceId"))
)
if mibBuilder.loadTexts:
    ciscoCdpMIBGroupV12R02.setStatus("deprecated")

ciscoCdpV2MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 6)
)
ciscoCdpV2MIBGroup.setObjects(
      *(("CISCO-CDP-MIB", "cdpCacheApplianceID"),
        ("CISCO-CDP-MIB", "cdpCacheVlanID"),
        ("CISCO-CDP-MIB", "cdpCachePowerConsumption"),
        ("CISCO-CDP-MIB", "cdpCacheMTU"),
        ("CISCO-CDP-MIB", "cdpCacheSysName"),
        ("CISCO-CDP-MIB", "cdpCacheSysObjectID"),
        ("CISCO-CDP-MIB", "cdpCacheLastChange"),
        ("CISCO-CDP-MIB", "cdpCachePhysLocation"),
        ("CISCO-CDP-MIB", "cdpCachePrimaryMgmtAddrType"),
        ("CISCO-CDP-MIB", "cdpCachePrimaryMgmtAddr"),
        ("CISCO-CDP-MIB", "cdpCacheSecondaryMgmtAddrType"),
        ("CISCO-CDP-MIB", "cdpCacheSecondaryMgmtAddr"),
        ("CISCO-CDP-MIB", "cdpGlobalLastChange"),
        ("CISCO-CDP-MIB", "cdpGlobalDeviceIdFormatCpb"),
        ("CISCO-CDP-MIB", "cdpGlobalDeviceIdFormat"))
)
if mibBuilder.loadTexts:
    ciscoCdpV2MIBGroup.setStatus("current")

ciscoCdpV2IfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 7)
)
ciscoCdpV2IfExtGroup.setObjects(
      *(("CISCO-CDP-MIB", "cdpInterfaceExtendedTrust"),
        ("CISCO-CDP-MIB", "cdpInterfaceCosForUntrustedPort"))
)
if mibBuilder.loadTexts:
    ciscoCdpV2IfExtGroup.setStatus("current")

ciscoCdpCtAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 8)
)
ciscoCdpCtAddressGroup.setObjects(
      *(("CISCO-CDP-MIB", "cdpCtAddressType"),
        ("CISCO-CDP-MIB", "cdpCtAddress"))
)
if mibBuilder.loadTexts:
    ciscoCdpCtAddressGroup.setStatus("current")

ciscoCdpMIBGroupV12R03 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 9)
)
ciscoCdpMIBGroupV12R03.setObjects(
      *(("CISCO-CDP-MIB", "cdpInterfaceEnable"),
        ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
        ("CISCO-CDP-MIB", "cdpInterfacePort"),
        ("CISCO-CDP-MIB", "cdpInterfaceName"),
        ("CISCO-CDP-MIB", "cdpCacheAddressType"),
        ("CISCO-CDP-MIB", "cdpCacheAddress"),
        ("CISCO-CDP-MIB", "cdpCacheVersion"),
        ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
        ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
        ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
        ("CISCO-CDP-MIB", "cdpCachePlatform"),
        ("CISCO-CDP-MIB", "cdpCacheVTPMgmtDomain"),
        ("CISCO-CDP-MIB", "cdpCacheNativeVLAN"),
        ("CISCO-CDP-MIB", "cdpCacheDuplex"),
        ("CISCO-CDP-MIB", "cdpGlobalRun"),
        ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"),
        ("CISCO-CDP-MIB", "cdpGlobalHoldTime"),
        ("CISCO-CDP-MIB", "cdpGlobalDeviceId"))
)
if mibBuilder.loadTexts:
    ciscoCdpMIBGroupV12R03.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdpMIBCompliance.setStatus(
        "obsolete"
    )

ciscoCdpMIBComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCdpMIBComplianceV11R01.setStatus(
        "obsolete"
    )

ciscoCdpMIBComplianceV11R02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCdpMIBComplianceV11R02.setStatus(
        "obsolete"
    )

ciscoCdpMIBComplianceV12R02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCdpMIBComplianceV12R02.setStatus(
        "obsolete"
    )

ciscoCdpMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoCdpMIBCompliance5.setStatus(
        "deprecated"
    )

ciscoCdpMIBComplianceV12R03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoCdpMIBComplianceV12R03.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDP-MIB",
    **{"ciscoCdpMIB": ciscoCdpMIB,
       "ciscoCdpMIBObjects": ciscoCdpMIBObjects,
       "cdpInterface": cdpInterface,
       "cdpInterfaceTable": cdpInterfaceTable,
       "cdpInterfaceEntry": cdpInterfaceEntry,
       "cdpInterfaceIfIndex": cdpInterfaceIfIndex,
       "cdpInterfaceEnable": cdpInterfaceEnable,
       "cdpInterfaceMessageInterval": cdpInterfaceMessageInterval,
       "cdpInterfaceGroup": cdpInterfaceGroup,
       "cdpInterfacePort": cdpInterfacePort,
       "cdpInterfaceName": cdpInterfaceName,
       "cdpInterfaceExtTable": cdpInterfaceExtTable,
       "cdpInterfaceExtEntry": cdpInterfaceExtEntry,
       "cdpInterfaceExtendedTrust": cdpInterfaceExtendedTrust,
       "cdpInterfaceCosForUntrustedPort": cdpInterfaceCosForUntrustedPort,
       "cdpCache": cdpCache,
       "cdpCacheTable": cdpCacheTable,
       "cdpCacheEntry": cdpCacheEntry,
       "cdpCacheIfIndex": cdpCacheIfIndex,
       "cdpCacheDeviceIndex": cdpCacheDeviceIndex,
       "cdpCacheAddressType": cdpCacheAddressType,
       "cdpCacheAddress": cdpCacheAddress,
       "cdpCacheVersion": cdpCacheVersion,
       "cdpCacheDeviceId": cdpCacheDeviceId,
       "cdpCacheDevicePort": cdpCacheDevicePort,
       "cdpCachePlatform": cdpCachePlatform,
       "cdpCacheCapabilities": cdpCacheCapabilities,
       "cdpCacheVTPMgmtDomain": cdpCacheVTPMgmtDomain,
       "cdpCacheNativeVLAN": cdpCacheNativeVLAN,
       "cdpCacheDuplex": cdpCacheDuplex,
       "cdpCacheApplianceID": cdpCacheApplianceID,
       "cdpCacheVlanID": cdpCacheVlanID,
       "cdpCachePowerConsumption": cdpCachePowerConsumption,
       "cdpCacheMTU": cdpCacheMTU,
       "cdpCacheSysName": cdpCacheSysName,
       "cdpCacheSysObjectID": cdpCacheSysObjectID,
       "cdpCachePrimaryMgmtAddrType": cdpCachePrimaryMgmtAddrType,
       "cdpCachePrimaryMgmtAddr": cdpCachePrimaryMgmtAddr,
       "cdpCacheSecondaryMgmtAddrType": cdpCacheSecondaryMgmtAddrType,
       "cdpCacheSecondaryMgmtAddr": cdpCacheSecondaryMgmtAddr,
       "cdpCachePhysLocation": cdpCachePhysLocation,
       "cdpCacheLastChange": cdpCacheLastChange,
       "cdpCtAddressTable": cdpCtAddressTable,
       "cdpCtAddressEntry": cdpCtAddressEntry,
       "cdpCtAddressIndex": cdpCtAddressIndex,
       "cdpCtAddressType": cdpCtAddressType,
       "cdpCtAddress": cdpCtAddress,
       "cdpGlobal": cdpGlobal,
       "cdpGlobalRun": cdpGlobalRun,
       "cdpGlobalMessageInterval": cdpGlobalMessageInterval,
       "cdpGlobalHoldTime": cdpGlobalHoldTime,
       "cdpGlobalDeviceId": cdpGlobalDeviceId,
       "cdpGlobalLastChange": cdpGlobalLastChange,
       "cdpGlobalDeviceIdFormatCpb": cdpGlobalDeviceIdFormatCpb,
       "cdpGlobalDeviceIdFormat": cdpGlobalDeviceIdFormat,
       "ciscoCdpMIBConformance": ciscoCdpMIBConformance,
       "ciscoCdpMIBCompliances": ciscoCdpMIBCompliances,
       "ciscoCdpMIBCompliance": ciscoCdpMIBCompliance,
       "ciscoCdpMIBComplianceV11R01": ciscoCdpMIBComplianceV11R01,
       "ciscoCdpMIBComplianceV11R02": ciscoCdpMIBComplianceV11R02,
       "ciscoCdpMIBComplianceV12R02": ciscoCdpMIBComplianceV12R02,
       "ciscoCdpMIBCompliance5": ciscoCdpMIBCompliance5,
       "ciscoCdpMIBComplianceV12R03": ciscoCdpMIBComplianceV12R03,
       "ciscoCdpMIBGroups": ciscoCdpMIBGroups,
       "ciscoCdpMIBGroup": ciscoCdpMIBGroup,
       "ciscoCdpMIBGroupV11R01": ciscoCdpMIBGroupV11R01,
       "ciscoCdpMIBGroupV11R02": ciscoCdpMIBGroupV11R02,
       "ciscoCdpMIBGroupV12R02": ciscoCdpMIBGroupV12R02,
       "ciscoCdpV2MIBGroup": ciscoCdpV2MIBGroup,
       "ciscoCdpV2IfExtGroup": ciscoCdpV2IfExtGroup,
       "ciscoCdpCtAddressGroup": ciscoCdpCtAddressGroup,
       "ciscoCdpMIBGroupV12R03": ciscoCdpMIBGroupV12R03}
)
