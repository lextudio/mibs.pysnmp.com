# SNMP MIB module (RUCKUS-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:37 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ruckusCommonDeviceModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonDeviceModule")

(RuckusCountryCode,) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusCountryCode")

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

ruckusDeviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusDeviceObjects_ObjectIdentity = ObjectIdentity
ruckusDeviceObjects = _RuckusDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1)
)
_RuckusDeviceInfo_ObjectIdentity = ObjectIdentity
ruckusDeviceInfo = _RuckusDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1)
)


class _RuckusDeviceName_Type(DisplayString):
    """Custom type ruckusDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusDeviceName_Type.__name__ = "DisplayString"
_RuckusDeviceName_Object = MibScalar
ruckusDeviceName = _RuckusDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 1),
    _RuckusDeviceName_Type()
)
ruckusDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceName.setStatus("current")


class _RuckusDeviceReboot_Type(TruthValue):
    """Custom type ruckusDeviceReboot based on TruthValue"""


_RuckusDeviceReboot_Object = MibScalar
ruckusDeviceReboot = _RuckusDeviceReboot_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 2),
    _RuckusDeviceReboot_Type()
)
ruckusDeviceReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceReboot.setStatus("current")


class _RuckusDeviceRebootWithDefaults_Type(TruthValue):
    """Custom type ruckusDeviceRebootWithDefaults based on TruthValue"""


_RuckusDeviceRebootWithDefaults_Object = MibScalar
ruckusDeviceRebootWithDefaults = _RuckusDeviceRebootWithDefaults_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 3),
    _RuckusDeviceRebootWithDefaults_Type()
)
ruckusDeviceRebootWithDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceRebootWithDefaults.setStatus("current")
_RuckusDeviceCountryCode_Type = RuckusCountryCode
_RuckusDeviceCountryCode_Object = MibScalar
ruckusDeviceCountryCode = _RuckusDeviceCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 4),
    _RuckusDeviceCountryCode_Type()
)
ruckusDeviceCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceCountryCode.setStatus("current")


class _RuckusDeviceGPS_Type(DisplayString):
    """Custom type ruckusDeviceGPS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusDeviceGPS_Type.__name__ = "DisplayString"
_RuckusDeviceGPS_Object = MibScalar
ruckusDeviceGPS = _RuckusDeviceGPS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 5),
    _RuckusDeviceGPS_Type()
)
ruckusDeviceGPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceGPS.setStatus("current")


class _RuckusDeviceNEId_Type(DisplayString):
    """Custom type ruckusDeviceNEId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusDeviceNEId_Type.__name__ = "DisplayString"
_RuckusDeviceNEId_Object = MibScalar
ruckusDeviceNEId = _RuckusDeviceNEId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 6),
    _RuckusDeviceNEId_Type()
)
ruckusDeviceNEId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceNEId.setStatus("current")


class _RuckusDeviceLocation_Type(DisplayString):
    """Custom type ruckusDeviceLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusDeviceLocation_Type.__name__ = "DisplayString"
_RuckusDeviceLocation_Object = MibScalar
ruckusDeviceLocation = _RuckusDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 1, 10),
    _RuckusDeviceLocation_Type()
)
ruckusDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceLocation.setStatus("current")
_RuckusDeviceTrapInfo_ObjectIdentity = ObjectIdentity
ruckusDeviceTrapInfo = _RuckusDeviceTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 2)
)


class _RuckusDeviceTrapDestination_Type(OctetString):
    """Custom type ruckusDeviceTrapDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusDeviceTrapDestination_Type.__name__ = "OctetString"
_RuckusDeviceTrapDestination_Object = MibScalar
ruckusDeviceTrapDestination = _RuckusDeviceTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 2, 1),
    _RuckusDeviceTrapDestination_Type()
)
ruckusDeviceTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceTrapDestination.setStatus("current")


class _RuckusDeviceTrapDestination2_Type(OctetString):
    """Custom type ruckusDeviceTrapDestination2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusDeviceTrapDestination2_Type.__name__ = "OctetString"
_RuckusDeviceTrapDestination2_Object = MibScalar
ruckusDeviceTrapDestination2 = _RuckusDeviceTrapDestination2_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 2, 2),
    _RuckusDeviceTrapDestination2_Type()
)
ruckusDeviceTrapDestination2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceTrapDestination2.setStatus("current")
_RuckusDeviceIPInfo_ObjectIdentity = ObjectIdentity
ruckusDeviceIPInfo = _RuckusDeviceIPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3)
)
_RuckusDevicePrimaryDNS_Type = IpAddress
_RuckusDevicePrimaryDNS_Object = MibScalar
ruckusDevicePrimaryDNS = _RuckusDevicePrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 1),
    _RuckusDevicePrimaryDNS_Type()
)
ruckusDevicePrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDevicePrimaryDNS.setStatus("current")
_RuckusDeviceSecondaryDNS_Type = IpAddress
_RuckusDeviceSecondaryDNS_Object = MibScalar
ruckusDeviceSecondaryDNS = _RuckusDeviceSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 2),
    _RuckusDeviceSecondaryDNS_Type()
)
ruckusDeviceSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceSecondaryDNS.setStatus("current")


class _RuckusDevicePrimaryDNSIPV6_Type(OctetString):
    """Custom type ruckusDevicePrimaryDNSIPV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusDevicePrimaryDNSIPV6_Type.__name__ = "OctetString"
_RuckusDevicePrimaryDNSIPV6_Object = MibScalar
ruckusDevicePrimaryDNSIPV6 = _RuckusDevicePrimaryDNSIPV6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 3),
    _RuckusDevicePrimaryDNSIPV6_Type()
)
ruckusDevicePrimaryDNSIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDevicePrimaryDNSIPV6.setStatus("current")


class _RuckusDeviceSecondaryDNSIPV6_Type(OctetString):
    """Custom type ruckusDeviceSecondaryDNSIPV6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusDeviceSecondaryDNSIPV6_Type.__name__ = "OctetString"
_RuckusDeviceSecondaryDNSIPV6_Object = MibScalar
ruckusDeviceSecondaryDNSIPV6 = _RuckusDeviceSecondaryDNSIPV6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 3, 4),
    _RuckusDeviceSecondaryDNSIPV6_Type()
)
ruckusDeviceSecondaryDNSIPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceSecondaryDNSIPV6.setStatus("current")
_RuckusDeviceWanInfo_ObjectIdentity = ObjectIdentity
ruckusDeviceWanInfo = _RuckusDeviceWanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4)
)
_RuckusDeviceWanTable_Object = MibTable
ruckusDeviceWanTable = _RuckusDeviceWanTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruckusDeviceWanTable.setStatus("current")
_RuckusDeviceWanEntry_Object = MibTableRow
ruckusDeviceWanEntry = _RuckusDeviceWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1)
)
ruckusDeviceWanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusDeviceWanEntry.setStatus("current")


class _RuckusDeviceWanIPAddrMode_Type(Integer32):
    """Custom type ruckusDeviceWanIPAddrMode based on Integer32"""
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
        *(("dhcp", 3),
          ("none", 1),
          ("pppoe", 4),
          ("static", 2))
    )


_RuckusDeviceWanIPAddrMode_Type.__name__ = "Integer32"
_RuckusDeviceWanIPAddrMode_Object = MibTableColumn
ruckusDeviceWanIPAddrMode = _RuckusDeviceWanIPAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 1),
    _RuckusDeviceWanIPAddrMode_Type()
)
ruckusDeviceWanIPAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPAddrMode.setStatus("current")
_RuckusDeviceWanIPAddr_Type = IpAddress
_RuckusDeviceWanIPAddr_Object = MibTableColumn
ruckusDeviceWanIPAddr = _RuckusDeviceWanIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 2),
    _RuckusDeviceWanIPAddr_Type()
)
ruckusDeviceWanIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPAddr.setStatus("current")
_RuckusDeviceWanName_Type = DisplayString
_RuckusDeviceWanName_Object = MibTableColumn
ruckusDeviceWanName = _RuckusDeviceWanName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 3),
    _RuckusDeviceWanName_Type()
)
ruckusDeviceWanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDeviceWanName.setStatus("current")
_RuckusDeviceWanNetmask_Type = IpAddress
_RuckusDeviceWanNetmask_Object = MibTableColumn
ruckusDeviceWanNetmask = _RuckusDeviceWanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 4),
    _RuckusDeviceWanNetmask_Type()
)
ruckusDeviceWanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanNetmask.setStatus("current")
_RuckusDeviceWanGateway_Type = IpAddress
_RuckusDeviceWanGateway_Object = MibTableColumn
ruckusDeviceWanGateway = _RuckusDeviceWanGateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 5),
    _RuckusDeviceWanGateway_Type()
)
ruckusDeviceWanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanGateway.setStatus("current")


class _RuckusDeviceWanIPVersion_Type(Integer32):
    """Custom type ruckusDeviceWanIPVersion based on Integer32"""
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
        *(("dualstack", 3),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_RuckusDeviceWanIPVersion_Type.__name__ = "Integer32"
_RuckusDeviceWanIPVersion_Object = MibTableColumn
ruckusDeviceWanIPVersion = _RuckusDeviceWanIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 8),
    _RuckusDeviceWanIPVersion_Type()
)
ruckusDeviceWanIPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPVersion.setStatus("current")


class _RuckusDeviceWanIPV6AddrMode_Type(Integer32):
    """Custom type ruckusDeviceWanIPV6AddrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-configuration", 1),
          ("static", 2))
    )


_RuckusDeviceWanIPV6AddrMode_Type.__name__ = "Integer32"
_RuckusDeviceWanIPV6AddrMode_Object = MibTableColumn
ruckusDeviceWanIPV6AddrMode = _RuckusDeviceWanIPV6AddrMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 10),
    _RuckusDeviceWanIPV6AddrMode_Type()
)
ruckusDeviceWanIPV6AddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPV6AddrMode.setStatus("current")


class _RuckusDeviceWanIPV6Addr_Type(OctetString):
    """Custom type ruckusDeviceWanIPV6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusDeviceWanIPV6Addr_Type.__name__ = "OctetString"
_RuckusDeviceWanIPV6Addr_Object = MibTableColumn
ruckusDeviceWanIPV6Addr = _RuckusDeviceWanIPV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 11),
    _RuckusDeviceWanIPV6Addr_Type()
)
ruckusDeviceWanIPV6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPV6Addr.setStatus("current")


class _RuckusDeviceWanIPV6PrefixLen_Type(Integer32):
    """Custom type ruckusDeviceWanIPV6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_RuckusDeviceWanIPV6PrefixLen_Type.__name__ = "Integer32"
_RuckusDeviceWanIPV6PrefixLen_Object = MibTableColumn
ruckusDeviceWanIPV6PrefixLen = _RuckusDeviceWanIPV6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 12),
    _RuckusDeviceWanIPV6PrefixLen_Type()
)
ruckusDeviceWanIPV6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPV6PrefixLen.setStatus("current")


class _RuckusDeviceWanIPV6Gateway_Type(OctetString):
    """Custom type ruckusDeviceWanIPV6Gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusDeviceWanIPV6Gateway_Type.__name__ = "OctetString"
_RuckusDeviceWanIPV6Gateway_Object = MibTableColumn
ruckusDeviceWanIPV6Gateway = _RuckusDeviceWanIPV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 1, 4, 1, 1, 13),
    _RuckusDeviceWanIPV6Gateway_Type()
)
ruckusDeviceWanIPV6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDeviceWanIPV6Gateway.setStatus("current")
_RuckusDeviceEvents_ObjectIdentity = ObjectIdentity
ruckusDeviceEvents = _RuckusDeviceEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-DEVICE-MIB",
    **{"ruckusDeviceMIB": ruckusDeviceMIB,
       "ruckusDeviceObjects": ruckusDeviceObjects,
       "ruckusDeviceInfo": ruckusDeviceInfo,
       "ruckusDeviceName": ruckusDeviceName,
       "ruckusDeviceReboot": ruckusDeviceReboot,
       "ruckusDeviceRebootWithDefaults": ruckusDeviceRebootWithDefaults,
       "ruckusDeviceCountryCode": ruckusDeviceCountryCode,
       "ruckusDeviceGPS": ruckusDeviceGPS,
       "ruckusDeviceNEId": ruckusDeviceNEId,
       "ruckusDeviceLocation": ruckusDeviceLocation,
       "ruckusDeviceTrapInfo": ruckusDeviceTrapInfo,
       "ruckusDeviceTrapDestination": ruckusDeviceTrapDestination,
       "ruckusDeviceTrapDestination2": ruckusDeviceTrapDestination2,
       "ruckusDeviceIPInfo": ruckusDeviceIPInfo,
       "ruckusDevicePrimaryDNS": ruckusDevicePrimaryDNS,
       "ruckusDeviceSecondaryDNS": ruckusDeviceSecondaryDNS,
       "ruckusDevicePrimaryDNSIPV6": ruckusDevicePrimaryDNSIPV6,
       "ruckusDeviceSecondaryDNSIPV6": ruckusDeviceSecondaryDNSIPV6,
       "ruckusDeviceWanInfo": ruckusDeviceWanInfo,
       "ruckusDeviceWanTable": ruckusDeviceWanTable,
       "ruckusDeviceWanEntry": ruckusDeviceWanEntry,
       "ruckusDeviceWanIPAddrMode": ruckusDeviceWanIPAddrMode,
       "ruckusDeviceWanIPAddr": ruckusDeviceWanIPAddr,
       "ruckusDeviceWanName": ruckusDeviceWanName,
       "ruckusDeviceWanNetmask": ruckusDeviceWanNetmask,
       "ruckusDeviceWanGateway": ruckusDeviceWanGateway,
       "ruckusDeviceWanIPVersion": ruckusDeviceWanIPVersion,
       "ruckusDeviceWanIPV6AddrMode": ruckusDeviceWanIPV6AddrMode,
       "ruckusDeviceWanIPV6Addr": ruckusDeviceWanIPV6Addr,
       "ruckusDeviceWanIPV6PrefixLen": ruckusDeviceWanIPV6PrefixLen,
       "ruckusDeviceWanIPV6Gateway": ruckusDeviceWanIPV6Gateway,
       "ruckusDeviceEvents": ruckusDeviceEvents}
)
