# SNMP MIB module (CISCO-DNS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DNS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:39 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDNSClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436)
)
ciscoDNSClientMIB.setRevisions(
        ("2004-09-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDNSClientMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDNSClientMIBNotifs = _CiscoDNSClientMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 0)
)
_CiscoDNSClientMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDNSClientMIBObjects = _CiscoDNSClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1)
)
_CdcConfigGroup_ObjectIdentity = ObjectIdentity
cdcConfigGroup = _CdcConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1)
)


class _CdcDNSConfigEnable_Type(Integer32):
    """Custom type cdcDNSConfigEnable based on Integer32"""
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


_CdcDNSConfigEnable_Type.__name__ = "Integer32"
_CdcDNSConfigEnable_Object = MibScalar
cdcDNSConfigEnable = _CdcDNSConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 1),
    _CdcDNSConfigEnable_Type()
)
cdcDNSConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdcDNSConfigEnable.setStatus("current")


class _CdcNoOfDNSServerConfig_Type(Unsigned32):
    """Custom type cdcNoOfDNSServerConfig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CdcNoOfDNSServerConfig_Type.__name__ = "Unsigned32"
_CdcNoOfDNSServerConfig_Object = MibScalar
cdcNoOfDNSServerConfig = _CdcNoOfDNSServerConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 2),
    _CdcNoOfDNSServerConfig_Type()
)
cdcNoOfDNSServerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcNoOfDNSServerConfig.setStatus("current")


class _CdcDNSServerNextAvailIndex_Type(Unsigned32):
    """Custom type cdcDNSServerNextAvailIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdcDNSServerNextAvailIndex_Type.__name__ = "Unsigned32"
_CdcDNSServerNextAvailIndex_Object = MibScalar
cdcDNSServerNextAvailIndex = _CdcDNSServerNextAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 3),
    _CdcDNSServerNextAvailIndex_Type()
)
cdcDNSServerNextAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcDNSServerNextAvailIndex.setStatus("current")
_CdcDNSServerTable_Object = MibTable
cdcDNSServerTable = _CdcDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdcDNSServerTable.setStatus("current")
_CdcDNSServerEntry_Object = MibTableRow
cdcDNSServerEntry = _CdcDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1)
)
cdcDNSServerEntry.setIndexNames(
    (0, "CISCO-DNS-CLIENT-MIB", "cdcDNSServerIndex"),
)
if mibBuilder.loadTexts:
    cdcDNSServerEntry.setStatus("current")


class _CdcDNSServerIndex_Type(Unsigned32):
    """Custom type cdcDNSServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdcDNSServerIndex_Type.__name__ = "Unsigned32"
_CdcDNSServerIndex_Object = MibTableColumn
cdcDNSServerIndex = _CdcDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 1),
    _CdcDNSServerIndex_Type()
)
cdcDNSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDNSServerIndex.setStatus("current")


class _CdcDNSServerAddrType_Type(InetAddressType):
    """Custom type cdcDNSServerAddrType based on InetAddressType"""


_CdcDNSServerAddrType_Object = MibTableColumn
cdcDNSServerAddrType = _CdcDNSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 2),
    _CdcDNSServerAddrType_Type()
)
cdcDNSServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDNSServerAddrType.setStatus("current")
_CdcDNSServerAddr_Type = InetAddress
_CdcDNSServerAddr_Object = MibTableColumn
cdcDNSServerAddr = _CdcDNSServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 3),
    _CdcDNSServerAddr_Type()
)
cdcDNSServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDNSServerAddr.setStatus("current")
_CdcDNSServerStatus_Type = RowStatus
_CdcDNSServerStatus_Object = MibTableColumn
cdcDNSServerStatus = _CdcDNSServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 4),
    _CdcDNSServerStatus_Type()
)
cdcDNSServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDNSServerStatus.setStatus("current")


class _CdcDefaultDNSDomainName_Type(SnmpAdminString):
    """Custom type cdcDefaultDNSDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CdcDefaultDNSDomainName_Type.__name__ = "SnmpAdminString"
_CdcDefaultDNSDomainName_Object = MibScalar
cdcDefaultDNSDomainName = _CdcDefaultDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 5),
    _CdcDefaultDNSDomainName_Type()
)
cdcDefaultDNSDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdcDefaultDNSDomainName.setStatus("current")
_CdcDNSDomainNameTable_Object = MibTable
cdcDNSDomainNameTable = _CdcDNSDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cdcDNSDomainNameTable.setStatus("current")
_CdcDNSDomainNameEntry_Object = MibTableRow
cdcDNSDomainNameEntry = _CdcDNSDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1)
)
cdcDNSDomainNameEntry.setIndexNames(
    (0, "CISCO-DNS-CLIENT-MIB", "cdcDNSDomainNameIndex"),
)
if mibBuilder.loadTexts:
    cdcDNSDomainNameEntry.setStatus("current")


class _CdcDNSDomainNameIndex_Type(Unsigned32):
    """Custom type cdcDNSDomainNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CdcDNSDomainNameIndex_Type.__name__ = "Unsigned32"
_CdcDNSDomainNameIndex_Object = MibTableColumn
cdcDNSDomainNameIndex = _CdcDNSDomainNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1, 1),
    _CdcDNSDomainNameIndex_Type()
)
cdcDNSDomainNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDNSDomainNameIndex.setStatus("current")


class _CdcDNSDomainName_Type(SnmpAdminString):
    """Custom type cdcDNSDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CdcDNSDomainName_Type.__name__ = "SnmpAdminString"
_CdcDNSDomainName_Object = MibTableColumn
cdcDNSDomainName = _CdcDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1, 2),
    _CdcDNSDomainName_Type()
)
cdcDNSDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDNSDomainName.setStatus("current")
_CdcDNSDomainNameStatus_Type = RowStatus
_CdcDNSDomainNameStatus_Object = MibTableColumn
cdcDNSDomainNameStatus = _CdcDNSDomainNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1, 3),
    _CdcDNSDomainNameStatus_Type()
)
cdcDNSDomainNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDNSDomainNameStatus.setStatus("current")
_CiscoDNSClientMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDNSClientMIBConformance = _CiscoDNSClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 2)
)
_CiscoDNSClientMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDNSClientMIBCompliances = _CiscoDNSClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 1)
)
_CiscoDNSClientMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDNSClientMIBGroups = _CiscoDNSClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 2)
)

# Managed Objects groups

ciscoDNSServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 2, 1)
)
ciscoDNSServerConfigGroup.setObjects(
      *(("CISCO-DNS-CLIENT-MIB", "cdcDNSConfigEnable"),
        ("CISCO-DNS-CLIENT-MIB", "cdcNoOfDNSServerConfig"),
        ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerNextAvailIndex"),
        ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerAddrType"),
        ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerAddr"),
        ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerStatus"))
)
if mibBuilder.loadTexts:
    ciscoDNSServerConfigGroup.setStatus("current")

ciscoDNSDomainNameConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 2, 2)
)
ciscoDNSDomainNameConfigGroup.setObjects(
      *(("CISCO-DNS-CLIENT-MIB", "cdcDefaultDNSDomainName"),
        ("CISCO-DNS-CLIENT-MIB", "cdcDNSDomainName"),
        ("CISCO-DNS-CLIENT-MIB", "cdcDNSDomainNameStatus"))
)
if mibBuilder.loadTexts:
    ciscoDNSDomainNameConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDNSClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDNSClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DNS-CLIENT-MIB",
    **{"ciscoDNSClientMIB": ciscoDNSClientMIB,
       "ciscoDNSClientMIBNotifs": ciscoDNSClientMIBNotifs,
       "ciscoDNSClientMIBObjects": ciscoDNSClientMIBObjects,
       "cdcConfigGroup": cdcConfigGroup,
       "cdcDNSConfigEnable": cdcDNSConfigEnable,
       "cdcNoOfDNSServerConfig": cdcNoOfDNSServerConfig,
       "cdcDNSServerNextAvailIndex": cdcDNSServerNextAvailIndex,
       "cdcDNSServerTable": cdcDNSServerTable,
       "cdcDNSServerEntry": cdcDNSServerEntry,
       "cdcDNSServerIndex": cdcDNSServerIndex,
       "cdcDNSServerAddrType": cdcDNSServerAddrType,
       "cdcDNSServerAddr": cdcDNSServerAddr,
       "cdcDNSServerStatus": cdcDNSServerStatus,
       "cdcDefaultDNSDomainName": cdcDefaultDNSDomainName,
       "cdcDNSDomainNameTable": cdcDNSDomainNameTable,
       "cdcDNSDomainNameEntry": cdcDNSDomainNameEntry,
       "cdcDNSDomainNameIndex": cdcDNSDomainNameIndex,
       "cdcDNSDomainName": cdcDNSDomainName,
       "cdcDNSDomainNameStatus": cdcDNSDomainNameStatus,
       "ciscoDNSClientMIBConformance": ciscoDNSClientMIBConformance,
       "ciscoDNSClientMIBCompliances": ciscoDNSClientMIBCompliances,
       "ciscoDNSClientMIBCompliance": ciscoDNSClientMIBCompliance,
       "ciscoDNSClientMIBGroups": ciscoDNSClientMIBGroups,
       "ciscoDNSServerConfigGroup": ciscoDNSServerConfigGroup,
       "ciscoDNSDomainNameConfigGroup": ciscoDNSDomainNameConfigGroup}
)
