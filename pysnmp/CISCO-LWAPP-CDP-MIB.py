# SNMP MIB module (CISCO-LWAPP-CDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-CDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:13 2024
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

(cLApSysMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress")

(CLCdpAdvtVersionType,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLCdpAdvtVersionType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappCdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623)
)
ciscoLwappCdpMIB.setRevisions(
        ("2009-11-23 00:00",
         "2007-03-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappCdpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappCdpMIBNotifs = _CiscoLwappCdpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 0)
)
_CiscoLwappCdpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappCdpMIBObjects = _CiscoLwappCdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1)
)
_ClcCdpTraffic_ObjectIdentity = ObjectIdentity
clcCdpTraffic = _ClcCdpTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1)
)
_ClcCdpInPackets_Type = Counter32
_ClcCdpInPackets_Object = MibScalar
clcCdpInPackets = _ClcCdpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 1),
    _ClcCdpInPackets_Type()
)
clcCdpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpInPackets.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpInPackets.setUnits("packets")
_ClcCdpOutPackets_Type = Counter32
_ClcCdpOutPackets_Object = MibScalar
clcCdpOutPackets = _ClcCdpOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 2),
    _ClcCdpOutPackets_Type()
)
clcCdpOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpOutPackets.setUnits("packets")
_ClcCdpChecksumErrorPackets_Type = Counter32
_ClcCdpChecksumErrorPackets_Object = MibScalar
clcCdpChecksumErrorPackets = _ClcCdpChecksumErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 3),
    _ClcCdpChecksumErrorPackets_Type()
)
clcCdpChecksumErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpChecksumErrorPackets.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpChecksumErrorPackets.setUnits("packets")
_ClcCdpNoMemoryPackets_Type = Counter32
_ClcCdpNoMemoryPackets_Object = MibScalar
clcCdpNoMemoryPackets = _ClcCdpNoMemoryPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 4),
    _ClcCdpNoMemoryPackets_Type()
)
clcCdpNoMemoryPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpNoMemoryPackets.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpNoMemoryPackets.setUnits("packets")
_ClcCdpInvalidPackets_Type = Counter32
_ClcCdpInvalidPackets_Object = MibScalar
clcCdpInvalidPackets = _ClcCdpInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 1, 5),
    _ClcCdpInvalidPackets_Type()
)
clcCdpInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpInvalidPackets.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpInvalidPackets.setUnits("packets")
_ClcCdpGlobalConfig_ObjectIdentity = ObjectIdentity
clcCdpGlobalConfig = _ClcCdpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2)
)


class _ClcCdpAdvtVersion_Type(CLCdpAdvtVersionType):
    """Custom type clcCdpAdvtVersion based on CLCdpAdvtVersionType"""


_ClcCdpAdvtVersion_Object = MibScalar
clcCdpAdvtVersion = _ClcCdpAdvtVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2, 1),
    _ClcCdpAdvtVersion_Type()
)
clcCdpAdvtVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcCdpAdvtVersion.setStatus("current")


class _ClcCdpMessageInterval_Type(Unsigned32):
    """Custom type clcCdpMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_ClcCdpMessageInterval_Type.__name__ = "Unsigned32"
_ClcCdpMessageInterval_Object = MibScalar
clcCdpMessageInterval = _ClcCdpMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2, 2),
    _ClcCdpMessageInterval_Type()
)
clcCdpMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcCdpMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpMessageInterval.setUnits("seconds")


class _ClcCdpGlobalEnable_Type(TruthValue):
    """Custom type clcCdpGlobalEnable based on TruthValue"""


_ClcCdpGlobalEnable_Object = MibScalar
clcCdpGlobalEnable = _ClcCdpGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 2, 3),
    _ClcCdpGlobalEnable_Type()
)
clcCdpGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcCdpGlobalEnable.setStatus("current")
_ClcCdpApCacheStatus_ObjectIdentity = ObjectIdentity
clcCdpApCacheStatus = _ClcCdpApCacheStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3)
)
_ClcCdpApCacheTable_Object = MibTable
clcCdpApCacheTable = _ClcCdpApCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clcCdpApCacheTable.setStatus("current")
_ClcCdpApCacheEntry_Object = MibTableRow
clcCdpApCacheEntry = _ClcCdpApCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1)
)
clcCdpApCacheEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-CDP-MIB", "clcCdpApCacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    clcCdpApCacheEntry.setStatus("current")


class _ClcCdpApCacheDeviceIndex_Type(Unsigned32):
    """Custom type clcCdpApCacheDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ClcCdpApCacheDeviceIndex_Type.__name__ = "Unsigned32"
_ClcCdpApCacheDeviceIndex_Object = MibTableColumn
clcCdpApCacheDeviceIndex = _ClcCdpApCacheDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 1),
    _ClcCdpApCacheDeviceIndex_Type()
)
clcCdpApCacheDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clcCdpApCacheDeviceIndex.setStatus("current")
_ClcCdpApCacheApName_Type = SnmpAdminString
_ClcCdpApCacheApName_Object = MibTableColumn
clcCdpApCacheApName = _ClcCdpApCacheApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 2),
    _ClcCdpApCacheApName_Type()
)
clcCdpApCacheApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheApName.setStatus("current")
_ClcCdpApCacheApAddressType_Type = InetAddressType
_ClcCdpApCacheApAddressType_Object = MibTableColumn
clcCdpApCacheApAddressType = _ClcCdpApCacheApAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 3),
    _ClcCdpApCacheApAddressType_Type()
)
clcCdpApCacheApAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheApAddressType.setStatus("current")
_ClcCdpApCacheApAddress_Type = InetAddress
_ClcCdpApCacheApAddress_Object = MibTableColumn
clcCdpApCacheApAddress = _ClcCdpApCacheApAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 4),
    _ClcCdpApCacheApAddress_Type()
)
clcCdpApCacheApAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheApAddress.setStatus("current")
_ClcCdpApCacheLocalInterface_Type = InterfaceIndexOrZero
_ClcCdpApCacheLocalInterface_Object = MibTableColumn
clcCdpApCacheLocalInterface = _ClcCdpApCacheLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 5),
    _ClcCdpApCacheLocalInterface_Type()
)
clcCdpApCacheLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheLocalInterface.setStatus("current")
_ClcCdpApCacheNeighName_Type = DisplayString
_ClcCdpApCacheNeighName_Object = MibTableColumn
clcCdpApCacheNeighName = _ClcCdpApCacheNeighName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 6),
    _ClcCdpApCacheNeighName_Type()
)
clcCdpApCacheNeighName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheNeighName.setStatus("current")
_ClcCdpApCacheNeighAddressType_Type = InetAddressType
_ClcCdpApCacheNeighAddressType_Object = MibTableColumn
clcCdpApCacheNeighAddressType = _ClcCdpApCacheNeighAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 7),
    _ClcCdpApCacheNeighAddressType_Type()
)
clcCdpApCacheNeighAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheNeighAddressType.setStatus("current")
_ClcCdpApCacheNeighAddress_Type = InetAddress
_ClcCdpApCacheNeighAddress_Object = MibTableColumn
clcCdpApCacheNeighAddress = _ClcCdpApCacheNeighAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 8),
    _ClcCdpApCacheNeighAddress_Type()
)
clcCdpApCacheNeighAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheNeighAddress.setStatus("current")
_ClcCdpApCacheNeighInterface_Type = DisplayString
_ClcCdpApCacheNeighInterface_Object = MibTableColumn
clcCdpApCacheNeighInterface = _ClcCdpApCacheNeighInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 9),
    _ClcCdpApCacheNeighInterface_Type()
)
clcCdpApCacheNeighInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheNeighInterface.setStatus("current")
_ClcCdpApCacheNeighVersion_Type = DisplayString
_ClcCdpApCacheNeighVersion_Object = MibTableColumn
clcCdpApCacheNeighVersion = _ClcCdpApCacheNeighVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 10),
    _ClcCdpApCacheNeighVersion_Type()
)
clcCdpApCacheNeighVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheNeighVersion.setStatus("current")


class _ClcCdpApCacheAdvtVersion_Type(CLCdpAdvtVersionType):
    """Custom type clcCdpApCacheAdvtVersion based on CLCdpAdvtVersionType"""


_ClcCdpApCacheAdvtVersion_Object = MibTableColumn
clcCdpApCacheAdvtVersion = _ClcCdpApCacheAdvtVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 11),
    _ClcCdpApCacheAdvtVersion_Type()
)
clcCdpApCacheAdvtVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcCdpApCacheAdvtVersion.setStatus("current")
_ClcCdpApCachePlatform_Type = DisplayString
_ClcCdpApCachePlatform_Object = MibTableColumn
clcCdpApCachePlatform = _ClcCdpApCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 12),
    _ClcCdpApCachePlatform_Type()
)
clcCdpApCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCachePlatform.setStatus("current")


class _ClcCdpApCacheCapabilities_Type(OctetString):
    """Custom type clcCdpApCacheCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClcCdpApCacheCapabilities_Type.__name__ = "OctetString"
_ClcCdpApCacheCapabilities_Object = MibTableColumn
clcCdpApCacheCapabilities = _ClcCdpApCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 13),
    _ClcCdpApCacheCapabilities_Type()
)
clcCdpApCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheCapabilities.setStatus("current")


class _ClcCdpApCacheHoldtimeLeft_Type(Unsigned32):
    """Custom type clcCdpApCacheHoldtimeLeft based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_ClcCdpApCacheHoldtimeLeft_Type.__name__ = "Unsigned32"
_ClcCdpApCacheHoldtimeLeft_Object = MibTableColumn
clcCdpApCacheHoldtimeLeft = _ClcCdpApCacheHoldtimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 14),
    _ClcCdpApCacheHoldtimeLeft_Type()
)
clcCdpApCacheHoldtimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheHoldtimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpApCacheHoldtimeLeft.setUnits("seconds")


class _ClcCdpApCacheDuplex_Type(Integer32):
    """Custom type clcCdpApCacheDuplex based on Integer32"""
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
        *(("auto", 4),
          ("fullduplex", 2),
          ("halfduplex", 3),
          ("unknown", 1))
    )


_ClcCdpApCacheDuplex_Type.__name__ = "Integer32"
_ClcCdpApCacheDuplex_Object = MibTableColumn
clcCdpApCacheDuplex = _ClcCdpApCacheDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 15),
    _ClcCdpApCacheDuplex_Type()
)
clcCdpApCacheDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheDuplex.setStatus("current")


class _ClcCdpApCacheInterfaceSpeed_Type(Integer32):
    """Custom type clcCdpApCacheInterfaceSpeed based on Integer32"""
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
        *(("auto", 5),
          ("hundredMbps", 3),
          ("none", 1),
          ("tenMbps", 2),
          ("thousandMbps", 4))
    )


_ClcCdpApCacheInterfaceSpeed_Type.__name__ = "Integer32"
_ClcCdpApCacheInterfaceSpeed_Object = MibTableColumn
clcCdpApCacheInterfaceSpeed = _ClcCdpApCacheInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 3, 1, 1, 16),
    _ClcCdpApCacheInterfaceSpeed_Type()
)
clcCdpApCacheInterfaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clcCdpApCacheInterfaceSpeed.setStatus("current")
if mibBuilder.loadTexts:
    clcCdpApCacheInterfaceSpeed.setUnits("Mbps")
_ClcCdpApCacheConfig_ObjectIdentity = ObjectIdentity
clcCdpApCacheConfig = _ClcCdpApCacheConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4)
)
_ClcCdpApTable_Object = MibTable
clcCdpApTable = _ClcCdpApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clcCdpApTable.setStatus("current")
_ClcCdpApEntry_Object = MibTableRow
clcCdpApEntry = _ClcCdpApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4, 1, 1)
)
clcCdpApEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clcCdpApEntry.setStatus("current")


class _ClcCdpApCdpEnable_Type(TruthValue):
    """Custom type clcCdpApCdpEnable based on TruthValue"""


_ClcCdpApCdpEnable_Object = MibTableColumn
clcCdpApCdpEnable = _ClcCdpApCdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 1, 4, 1, 1, 1),
    _ClcCdpApCdpEnable_Type()
)
clcCdpApCdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clcCdpApCdpEnable.setStatus("current")
_CiscoLwappCdpMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappCdpMIBConform = _CiscoLwappCdpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2)
)
_CiscoLwappCdpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappCdpMIBCompliances = _CiscoLwappCdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 1)
)
_CiscoLwappCdpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappCdpMIBGroups = _CiscoLwappCdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2)
)

# Managed Objects groups

clcCdpRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2, 1)
)
clcCdpRev01ConfigGroup.setObjects(
      *(("CISCO-LWAPP-CDP-MIB", "clcCdpApCdpEnable"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpAdvtVersion"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpMessageInterval"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpGlobalEnable"))
)
if mibBuilder.loadTexts:
    clcCdpRev01ConfigGroup.setStatus("current")

clcCdpRev01StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2, 2)
)
clcCdpRev01StatusGroup.setObjects(
      *(("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheApName"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheApAddressType"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheApAddress"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheLocalInterface"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighName"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighAddressType"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighAddress"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighInterface"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheNeighVersion"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheAdvtVersion"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCachePlatform"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheCapabilities"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheHoldtimeLeft"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpInPackets"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpOutPackets"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpChecksumErrorPackets"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpNoMemoryPackets"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpInvalidPackets"))
)
if mibBuilder.loadTexts:
    clcCdpRev01StatusGroup.setStatus("current")

clcCdpRev02StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 2, 3)
)
clcCdpRev02StatusGroup.setObjects(
      *(("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheDuplex"),
        ("CISCO-LWAPP-CDP-MIB", "clcCdpApCacheInterfaceSpeed"))
)
if mibBuilder.loadTexts:
    clcCdpRev02StatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappCdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappCdpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappCdpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 623, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappCdpMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-CDP-MIB",
    **{"ciscoLwappCdpMIB": ciscoLwappCdpMIB,
       "ciscoLwappCdpMIBNotifs": ciscoLwappCdpMIBNotifs,
       "ciscoLwappCdpMIBObjects": ciscoLwappCdpMIBObjects,
       "clcCdpTraffic": clcCdpTraffic,
       "clcCdpInPackets": clcCdpInPackets,
       "clcCdpOutPackets": clcCdpOutPackets,
       "clcCdpChecksumErrorPackets": clcCdpChecksumErrorPackets,
       "clcCdpNoMemoryPackets": clcCdpNoMemoryPackets,
       "clcCdpInvalidPackets": clcCdpInvalidPackets,
       "clcCdpGlobalConfig": clcCdpGlobalConfig,
       "clcCdpAdvtVersion": clcCdpAdvtVersion,
       "clcCdpMessageInterval": clcCdpMessageInterval,
       "clcCdpGlobalEnable": clcCdpGlobalEnable,
       "clcCdpApCacheStatus": clcCdpApCacheStatus,
       "clcCdpApCacheTable": clcCdpApCacheTable,
       "clcCdpApCacheEntry": clcCdpApCacheEntry,
       "clcCdpApCacheDeviceIndex": clcCdpApCacheDeviceIndex,
       "clcCdpApCacheApName": clcCdpApCacheApName,
       "clcCdpApCacheApAddressType": clcCdpApCacheApAddressType,
       "clcCdpApCacheApAddress": clcCdpApCacheApAddress,
       "clcCdpApCacheLocalInterface": clcCdpApCacheLocalInterface,
       "clcCdpApCacheNeighName": clcCdpApCacheNeighName,
       "clcCdpApCacheNeighAddressType": clcCdpApCacheNeighAddressType,
       "clcCdpApCacheNeighAddress": clcCdpApCacheNeighAddress,
       "clcCdpApCacheNeighInterface": clcCdpApCacheNeighInterface,
       "clcCdpApCacheNeighVersion": clcCdpApCacheNeighVersion,
       "clcCdpApCacheAdvtVersion": clcCdpApCacheAdvtVersion,
       "clcCdpApCachePlatform": clcCdpApCachePlatform,
       "clcCdpApCacheCapabilities": clcCdpApCacheCapabilities,
       "clcCdpApCacheHoldtimeLeft": clcCdpApCacheHoldtimeLeft,
       "clcCdpApCacheDuplex": clcCdpApCacheDuplex,
       "clcCdpApCacheInterfaceSpeed": clcCdpApCacheInterfaceSpeed,
       "clcCdpApCacheConfig": clcCdpApCacheConfig,
       "clcCdpApTable": clcCdpApTable,
       "clcCdpApEntry": clcCdpApEntry,
       "clcCdpApCdpEnable": clcCdpApCdpEnable,
       "ciscoLwappCdpMIBConform": ciscoLwappCdpMIBConform,
       "ciscoLwappCdpMIBCompliances": ciscoLwappCdpMIBCompliances,
       "ciscoLwappCdpMIBCompliance": ciscoLwappCdpMIBCompliance,
       "ciscoLwappCdpMIBComplianceRev1": ciscoLwappCdpMIBComplianceRev1,
       "ciscoLwappCdpMIBGroups": ciscoLwappCdpMIBGroups,
       "clcCdpRev01ConfigGroup": clcCdpRev01ConfigGroup,
       "clcCdpRev01StatusGroup": clcCdpRev01StatusGroup,
       "clcCdpRev02StatusGroup": clcCdpRev02StatusGroup}
)
