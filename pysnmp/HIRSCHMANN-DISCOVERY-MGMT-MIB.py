# SNMP MIB module (HIRSCHMANN-DISCOVERY-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-DISCOVERY-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:32 2024
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

(hmManagement,) = mibBuilder.importSymbols(
    "HIRSCHMANN-MGMT-MIB",
    "hmManagement")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hmMgmtDiscoveryGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 100)
)
hmMgmtDiscoveryGroup.setRevisions(
        ("2014-07-07 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmMgmtDiscoveryStatusGroup_ObjectIdentity = ObjectIdentity
hmMgmtDiscoveryStatusGroup = _HmMgmtDiscoveryStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 1)
)


class _HmMgmtDiscMode_Type(Integer32):
    """Custom type hmMgmtDiscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_HmMgmtDiscMode_Type.__name__ = "Integer32"
_HmMgmtDiscMode_Object = MibScalar
hmMgmtDiscMode = _HmMgmtDiscMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 1, 1),
    _HmMgmtDiscMode_Type()
)
hmMgmtDiscMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtDiscMode.setStatus("current")
_HmMgmtDiscMacAddr_Type = MacAddress
_HmMgmtDiscMacAddr_Object = MibScalar
hmMgmtDiscMacAddr = _HmMgmtDiscMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 1, 2),
    _HmMgmtDiscMacAddr_Type()
)
hmMgmtDiscMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtDiscMacAddr.setStatus("current")


class _HmMgmtDiscIpIntfType_Type(Integer32):
    """Custom type hmMgmtDiscIpIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback-intf", 1),
          ("mgmt-intf", 3),
          ("router-intf", 2))
    )


_HmMgmtDiscIpIntfType_Type.__name__ = "Integer32"
_HmMgmtDiscIpIntfType_Object = MibScalar
hmMgmtDiscIpIntfType = _HmMgmtDiscIpIntfType_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 1, 3),
    _HmMgmtDiscIpIntfType_Type()
)
hmMgmtDiscIpIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtDiscIpIntfType.setStatus("current")
_HmMgmtDiscSwVersion_Type = SnmpAdminString
_HmMgmtDiscSwVersion_Object = MibScalar
hmMgmtDiscSwVersion = _HmMgmtDiscSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 1, 4),
    _HmMgmtDiscSwVersion_Type()
)
hmMgmtDiscSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtDiscSwVersion.setStatus("current")
_HmMgmtDiscProductDescr_Type = SnmpAdminString
_HmMgmtDiscProductDescr_Object = MibScalar
hmMgmtDiscProductDescr = _HmMgmtDiscProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 1, 5),
    _HmMgmtDiscProductDescr_Type()
)
hmMgmtDiscProductDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmMgmtDiscProductDescr.setStatus("current")
_HmMgmtDiscoveryCfgGroup_ObjectIdentity = ObjectIdentity
hmMgmtDiscoveryCfgGroup = _HmMgmtDiscoveryCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2)
)
_HmMgmtDiscCfgUUID_Type = OctetString
_HmMgmtDiscCfgUUID_Object = MibScalar
hmMgmtDiscCfgUUID = _HmMgmtDiscCfgUUID_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 1),
    _HmMgmtDiscCfgUUID_Type()
)
hmMgmtDiscCfgUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgUUID.setStatus("current")


class _HmMgmtDiscCfgProto_Type(Integer32):
    """Custom type hmMgmtDiscCfgProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_HmMgmtDiscCfgProto_Type.__name__ = "Integer32"
_HmMgmtDiscCfgProto_Object = MibScalar
hmMgmtDiscCfgProto = _HmMgmtDiscCfgProto_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 2),
    _HmMgmtDiscCfgProto_Type()
)
hmMgmtDiscCfgProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgProto.setStatus("current")
_HmMgmtDiscCfgIPAddrType_Type = InetAddressType
_HmMgmtDiscCfgIPAddrType_Object = MibScalar
hmMgmtDiscCfgIPAddrType = _HmMgmtDiscCfgIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 3),
    _HmMgmtDiscCfgIPAddrType_Type()
)
hmMgmtDiscCfgIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgIPAddrType.setStatus("current")
_HmMgmtDiscCfgIPAddr_Type = InetAddress
_HmMgmtDiscCfgIPAddr_Object = MibScalar
hmMgmtDiscCfgIPAddr = _HmMgmtDiscCfgIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 4),
    _HmMgmtDiscCfgIPAddr_Type()
)
hmMgmtDiscCfgIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgIPAddr.setStatus("current")
_HmMgmtDiscCfgPrefLen_Type = InetAddressPrefixLength
_HmMgmtDiscCfgPrefLen_Object = MibScalar
hmMgmtDiscCfgPrefLen = _HmMgmtDiscCfgPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 5),
    _HmMgmtDiscCfgPrefLen_Type()
)
hmMgmtDiscCfgPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgPrefLen.setStatus("current")
_HmMgmtDiscCfgGwIPAddrType_Type = InetAddressType
_HmMgmtDiscCfgGwIPAddrType_Object = MibScalar
hmMgmtDiscCfgGwIPAddrType = _HmMgmtDiscCfgGwIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 6),
    _HmMgmtDiscCfgGwIPAddrType_Type()
)
hmMgmtDiscCfgGwIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgGwIPAddrType.setStatus("current")
_HmMgmtDiscCfgGwIPAddr_Type = InetAddress
_HmMgmtDiscCfgGwIPAddr_Object = MibScalar
hmMgmtDiscCfgGwIPAddr = _HmMgmtDiscCfgGwIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 7),
    _HmMgmtDiscCfgGwIPAddr_Type()
)
hmMgmtDiscCfgGwIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgGwIPAddr.setStatus("current")


class _HmMgmtDiscCfgAction_Type(Integer32):
    """Custom type hmMgmtDiscCfgAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1))
    )


_HmMgmtDiscCfgAction_Type.__name__ = "Integer32"
_HmMgmtDiscCfgAction_Object = MibScalar
hmMgmtDiscCfgAction = _HmMgmtDiscCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 8),
    _HmMgmtDiscCfgAction_Type()
)
hmMgmtDiscCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgAction.setStatus("current")


class _HmMgmtDiscCfgBlinking_Type(Integer32):
    """Custom type hmMgmtDiscCfgBlinking based on Integer32"""
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


_HmMgmtDiscCfgBlinking_Type.__name__ = "Integer32"
_HmMgmtDiscCfgBlinking_Object = MibScalar
hmMgmtDiscCfgBlinking = _HmMgmtDiscCfgBlinking_Object(
    (1, 3, 6, 1, 4, 1, 248, 16, 100, 2, 9),
    _HmMgmtDiscCfgBlinking_Type()
)
hmMgmtDiscCfgBlinking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmMgmtDiscCfgBlinking.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-DISCOVERY-MGMT-MIB",
    **{"hmMgmtDiscoveryGroup": hmMgmtDiscoveryGroup,
       "hmMgmtDiscoveryStatusGroup": hmMgmtDiscoveryStatusGroup,
       "hmMgmtDiscMode": hmMgmtDiscMode,
       "hmMgmtDiscMacAddr": hmMgmtDiscMacAddr,
       "hmMgmtDiscIpIntfType": hmMgmtDiscIpIntfType,
       "hmMgmtDiscSwVersion": hmMgmtDiscSwVersion,
       "hmMgmtDiscProductDescr": hmMgmtDiscProductDescr,
       "hmMgmtDiscoveryCfgGroup": hmMgmtDiscoveryCfgGroup,
       "hmMgmtDiscCfgUUID": hmMgmtDiscCfgUUID,
       "hmMgmtDiscCfgProto": hmMgmtDiscCfgProto,
       "hmMgmtDiscCfgIPAddrType": hmMgmtDiscCfgIPAddrType,
       "hmMgmtDiscCfgIPAddr": hmMgmtDiscCfgIPAddr,
       "hmMgmtDiscCfgPrefLen": hmMgmtDiscCfgPrefLen,
       "hmMgmtDiscCfgGwIPAddrType": hmMgmtDiscCfgGwIPAddrType,
       "hmMgmtDiscCfgGwIPAddr": hmMgmtDiscCfgGwIPAddr,
       "hmMgmtDiscCfgAction": hmMgmtDiscCfgAction,
       "hmMgmtDiscCfgBlinking": hmMgmtDiscCfgBlinking}
)
