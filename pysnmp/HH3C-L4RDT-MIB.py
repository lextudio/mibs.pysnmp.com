# SNMP MIB module (HH3C-L4RDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-L4RDT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:44 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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


# MODULE-IDENTITY

hh3cL4Redirect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cL4RedirectCacheTable_Object = MibTable
hh3cL4RedirectCacheTable = _Hh3cL4RedirectCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1)
)
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheTable.setStatus("current")
_Hh3cL4RedirectCacheEntry_Object = MibTableRow
hh3cL4RedirectCacheEntry = _Hh3cL4RedirectCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1)
)
hh3cL4RedirectCacheEntry.setIndexNames(
    (0, "HH3C-L4RDT-MIB", "hh3cL4RedirectCacheIpAddress"),
)
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheEntry.setStatus("current")
_Hh3cL4RedirectCacheIpAddress_Type = IpAddress
_Hh3cL4RedirectCacheIpAddress_Object = MibTableColumn
hh3cL4RedirectCacheIpAddress = _Hh3cL4RedirectCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 1),
    _Hh3cL4RedirectCacheIpAddress_Type()
)
hh3cL4RedirectCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheIpAddress.setStatus("current")


class _Hh3cL4RedirectCacheRedirectionStatus_Type(Integer32):
    """Custom type hh3cL4RedirectCacheRedirectionStatus based on Integer32"""
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
        *(("disabledNotRedirecting", 1),
          ("enabledHealthCheckFailed", 5),
          ("enabledHealthCheckOKNotRedirecting", 4),
          ("enabledHealthChecking", 3),
          ("enabledNoHealthChecker", 2),
          ("enabledRedirecting", 6))
    )


_Hh3cL4RedirectCacheRedirectionStatus_Type.__name__ = "Integer32"
_Hh3cL4RedirectCacheRedirectionStatus_Object = MibTableColumn
hh3cL4RedirectCacheRedirectionStatus = _Hh3cL4RedirectCacheRedirectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 2),
    _Hh3cL4RedirectCacheRedirectionStatus_Type()
)
hh3cL4RedirectCacheRedirectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheRedirectionStatus.setStatus("current")
_Hh3cL4RedirectCachePort_Type = Integer32
_Hh3cL4RedirectCachePort_Object = MibTableColumn
hh3cL4RedirectCachePort = _Hh3cL4RedirectCachePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 3),
    _Hh3cL4RedirectCachePort_Type()
)
hh3cL4RedirectCachePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectCachePort.setStatus("current")
_Hh3cL4RedirectCacheRowStatus_Type = RowStatus
_Hh3cL4RedirectCacheRowStatus_Object = MibTableColumn
hh3cL4RedirectCacheRowStatus = _Hh3cL4RedirectCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 4),
    _Hh3cL4RedirectCacheRowStatus_Type()
)
hh3cL4RedirectCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheRowStatus.setStatus("current")
_Hh3cL4RedirectCacheMacAddress_Type = MacAddress
_Hh3cL4RedirectCacheMacAddress_Object = MibTableColumn
hh3cL4RedirectCacheMacAddress = _Hh3cL4RedirectCacheMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 5),
    _Hh3cL4RedirectCacheMacAddress_Type()
)
hh3cL4RedirectCacheMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheMacAddress.setStatus("current")
_Hh3cL4RedirectCacheVlan_Type = Integer32
_Hh3cL4RedirectCacheVlan_Object = MibTableColumn
hh3cL4RedirectCacheVlan = _Hh3cL4RedirectCacheVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 6),
    _Hh3cL4RedirectCacheVlan_Type()
)
hh3cL4RedirectCacheVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheVlan.setStatus("current")
_Hh3cL4RedirectCacheTcpPort_Type = Integer32
_Hh3cL4RedirectCacheTcpPort_Object = MibTableColumn
hh3cL4RedirectCacheTcpPort = _Hh3cL4RedirectCacheTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 1, 1, 7),
    _Hh3cL4RedirectCacheTcpPort_Type()
)
hh3cL4RedirectCacheTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectCacheTcpPort.setStatus("current")
_Hh3cL4RedirectIpExclusionTable_Object = MibTable
hh3cL4RedirectIpExclusionTable = _Hh3cL4RedirectIpExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hh3cL4RedirectIpExclusionTable.setStatus("current")
_Hh3cL4RedirectIpExclusionEntry_Object = MibTableRow
hh3cL4RedirectIpExclusionEntry = _Hh3cL4RedirectIpExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 2, 1)
)
hh3cL4RedirectIpExclusionEntry.setIndexNames(
    (0, "HH3C-L4RDT-MIB", "hh3cL4RedirectIpExclusionIpAddress"),
)
if mibBuilder.loadTexts:
    hh3cL4RedirectIpExclusionEntry.setStatus("current")
_Hh3cL4RedirectIpExclusionIpAddress_Type = IpAddress
_Hh3cL4RedirectIpExclusionIpAddress_Object = MibTableColumn
hh3cL4RedirectIpExclusionIpAddress = _Hh3cL4RedirectIpExclusionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 2, 1, 1),
    _Hh3cL4RedirectIpExclusionIpAddress_Type()
)
hh3cL4RedirectIpExclusionIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL4RedirectIpExclusionIpAddress.setStatus("current")


class _Hh3cL4RedirectIpExclusionMaskLen_Type(Integer32):
    """Custom type hh3cL4RedirectIpExclusionMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cL4RedirectIpExclusionMaskLen_Type.__name__ = "Integer32"
_Hh3cL4RedirectIpExclusionMaskLen_Object = MibTableColumn
hh3cL4RedirectIpExclusionMaskLen = _Hh3cL4RedirectIpExclusionMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 2, 1, 2),
    _Hh3cL4RedirectIpExclusionMaskLen_Type()
)
hh3cL4RedirectIpExclusionMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectIpExclusionMaskLen.setStatus("current")
_Hh3cL4RedirectIpExclusionRowStatus_Type = RowStatus
_Hh3cL4RedirectIpExclusionRowStatus_Object = MibTableColumn
hh3cL4RedirectIpExclusionRowStatus = _Hh3cL4RedirectIpExclusionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 2, 1, 3),
    _Hh3cL4RedirectIpExclusionRowStatus_Type()
)
hh3cL4RedirectIpExclusionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectIpExclusionRowStatus.setStatus("current")
_Hh3cL4RedirectVlanTable_Object = MibTable
hh3cL4RedirectVlanTable = _Hh3cL4RedirectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 3)
)
if mibBuilder.loadTexts:
    hh3cL4RedirectVlanTable.setStatus("current")
_Hh3cL4RedirectVlanEntry_Object = MibTableRow
hh3cL4RedirectVlanEntry = _Hh3cL4RedirectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 3, 1)
)
hh3cL4RedirectVlanEntry.setIndexNames(
    (0, "HH3C-L4RDT-MIB", "hh3cL4RedirectVlanID"),
)
if mibBuilder.loadTexts:
    hh3cL4RedirectVlanEntry.setStatus("current")
_Hh3cL4RedirectVlanID_Type = Integer32
_Hh3cL4RedirectVlanID_Object = MibTableColumn
hh3cL4RedirectVlanID = _Hh3cL4RedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 3, 1, 1),
    _Hh3cL4RedirectVlanID_Type()
)
hh3cL4RedirectVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cL4RedirectVlanID.setStatus("current")
_Hh3cL4RedirectVlanRowStatus_Type = RowStatus
_Hh3cL4RedirectVlanRowStatus_Object = MibTableColumn
hh3cL4RedirectVlanRowStatus = _Hh3cL4RedirectVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 3, 1, 2),
    _Hh3cL4RedirectVlanRowStatus_Type()
)
hh3cL4RedirectVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cL4RedirectVlanRowStatus.setStatus("current")


class _Hh3cL4RedirectInformationString_Type(DisplayString):
    """Custom type hh3cL4RedirectInformationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hh3cL4RedirectInformationString_Type.__name__ = "DisplayString"
_Hh3cL4RedirectInformationString_Object = MibScalar
hh3cL4RedirectInformationString = _Hh3cL4RedirectInformationString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 4),
    _Hh3cL4RedirectInformationString_Type()
)
hh3cL4RedirectInformationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL4RedirectInformationString.setStatus("current")
_Hh3cL4RedirectFreeCacheEntries_Type = Integer32
_Hh3cL4RedirectFreeCacheEntries_Object = MibScalar
hh3cL4RedirectFreeCacheEntries = _Hh3cL4RedirectFreeCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 5),
    _Hh3cL4RedirectFreeCacheEntries_Type()
)
hh3cL4RedirectFreeCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL4RedirectFreeCacheEntries.setStatus("current")
_Hh3cL4RedirectFreeIpExclusionEntries_Type = Integer32
_Hh3cL4RedirectFreeIpExclusionEntries_Object = MibScalar
hh3cL4RedirectFreeIpExclusionEntries = _Hh3cL4RedirectFreeIpExclusionEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 6),
    _Hh3cL4RedirectFreeIpExclusionEntries_Type()
)
hh3cL4RedirectFreeIpExclusionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL4RedirectFreeIpExclusionEntries.setStatus("current")
_Hh3cL4RedirectFreeVlanEntries_Type = Integer32
_Hh3cL4RedirectFreeVlanEntries_Object = MibScalar
hh3cL4RedirectFreeVlanEntries = _Hh3cL4RedirectFreeVlanEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10, 7),
    _Hh3cL4RedirectFreeVlanEntries_Type()
)
hh3cL4RedirectFreeVlanEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cL4RedirectFreeVlanEntries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-L4RDT-MIB",
    **{"hh3cL4Redirect": hh3cL4Redirect,
       "hh3cL4RedirectCacheTable": hh3cL4RedirectCacheTable,
       "hh3cL4RedirectCacheEntry": hh3cL4RedirectCacheEntry,
       "hh3cL4RedirectCacheIpAddress": hh3cL4RedirectCacheIpAddress,
       "hh3cL4RedirectCacheRedirectionStatus": hh3cL4RedirectCacheRedirectionStatus,
       "hh3cL4RedirectCachePort": hh3cL4RedirectCachePort,
       "hh3cL4RedirectCacheRowStatus": hh3cL4RedirectCacheRowStatus,
       "hh3cL4RedirectCacheMacAddress": hh3cL4RedirectCacheMacAddress,
       "hh3cL4RedirectCacheVlan": hh3cL4RedirectCacheVlan,
       "hh3cL4RedirectCacheTcpPort": hh3cL4RedirectCacheTcpPort,
       "hh3cL4RedirectIpExclusionTable": hh3cL4RedirectIpExclusionTable,
       "hh3cL4RedirectIpExclusionEntry": hh3cL4RedirectIpExclusionEntry,
       "hh3cL4RedirectIpExclusionIpAddress": hh3cL4RedirectIpExclusionIpAddress,
       "hh3cL4RedirectIpExclusionMaskLen": hh3cL4RedirectIpExclusionMaskLen,
       "hh3cL4RedirectIpExclusionRowStatus": hh3cL4RedirectIpExclusionRowStatus,
       "hh3cL4RedirectVlanTable": hh3cL4RedirectVlanTable,
       "hh3cL4RedirectVlanEntry": hh3cL4RedirectVlanEntry,
       "hh3cL4RedirectVlanID": hh3cL4RedirectVlanID,
       "hh3cL4RedirectVlanRowStatus": hh3cL4RedirectVlanRowStatus,
       "hh3cL4RedirectInformationString": hh3cL4RedirectInformationString,
       "hh3cL4RedirectFreeCacheEntries": hh3cL4RedirectFreeCacheEntries,
       "hh3cL4RedirectFreeIpExclusionEntries": hh3cL4RedirectFreeIpExclusionEntries,
       "hh3cL4RedirectFreeVlanEntries": hh3cL4RedirectFreeVlanEntries}
)
