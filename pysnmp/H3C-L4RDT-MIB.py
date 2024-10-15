# SNMP MIB module (H3C-L4RDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-L4RDT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:47 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cL4Redirect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cL4RedirectCacheTable_Object = MibTable
h3cL4RedirectCacheTable = _H3cL4RedirectCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1)
)
if mibBuilder.loadTexts:
    h3cL4RedirectCacheTable.setStatus("current")
_H3cL4RedirectCacheEntry_Object = MibTableRow
h3cL4RedirectCacheEntry = _H3cL4RedirectCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1)
)
h3cL4RedirectCacheEntry.setIndexNames(
    (0, "H3C-L4RDT-MIB", "h3cL4RedirectCacheIpAddress"),
)
if mibBuilder.loadTexts:
    h3cL4RedirectCacheEntry.setStatus("current")
_H3cL4RedirectCacheIpAddress_Type = IpAddress
_H3cL4RedirectCacheIpAddress_Object = MibTableColumn
h3cL4RedirectCacheIpAddress = _H3cL4RedirectCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 1),
    _H3cL4RedirectCacheIpAddress_Type()
)
h3cL4RedirectCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cL4RedirectCacheIpAddress.setStatus("current")


class _H3cL4RedirectCacheRedirectionStatus_Type(Integer32):
    """Custom type h3cL4RedirectCacheRedirectionStatus based on Integer32"""
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


_H3cL4RedirectCacheRedirectionStatus_Type.__name__ = "Integer32"
_H3cL4RedirectCacheRedirectionStatus_Object = MibTableColumn
h3cL4RedirectCacheRedirectionStatus = _H3cL4RedirectCacheRedirectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 2),
    _H3cL4RedirectCacheRedirectionStatus_Type()
)
h3cL4RedirectCacheRedirectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cL4RedirectCacheRedirectionStatus.setStatus("current")
_H3cL4RedirectCachePort_Type = Integer32
_H3cL4RedirectCachePort_Object = MibTableColumn
h3cL4RedirectCachePort = _H3cL4RedirectCachePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 3),
    _H3cL4RedirectCachePort_Type()
)
h3cL4RedirectCachePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectCachePort.setStatus("current")
_H3cL4RedirectCacheRowStatus_Type = RowStatus
_H3cL4RedirectCacheRowStatus_Object = MibTableColumn
h3cL4RedirectCacheRowStatus = _H3cL4RedirectCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 4),
    _H3cL4RedirectCacheRowStatus_Type()
)
h3cL4RedirectCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectCacheRowStatus.setStatus("current")
_H3cL4RedirectCacheMacAddress_Type = MacAddress
_H3cL4RedirectCacheMacAddress_Object = MibTableColumn
h3cL4RedirectCacheMacAddress = _H3cL4RedirectCacheMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 5),
    _H3cL4RedirectCacheMacAddress_Type()
)
h3cL4RedirectCacheMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectCacheMacAddress.setStatus("current")
_H3cL4RedirectCacheVlan_Type = Integer32
_H3cL4RedirectCacheVlan_Object = MibTableColumn
h3cL4RedirectCacheVlan = _H3cL4RedirectCacheVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 6),
    _H3cL4RedirectCacheVlan_Type()
)
h3cL4RedirectCacheVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectCacheVlan.setStatus("current")
_H3cL4RedirectCacheTcpPort_Type = Integer32
_H3cL4RedirectCacheTcpPort_Object = MibTableColumn
h3cL4RedirectCacheTcpPort = _H3cL4RedirectCacheTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 1, 1, 7),
    _H3cL4RedirectCacheTcpPort_Type()
)
h3cL4RedirectCacheTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectCacheTcpPort.setStatus("current")
_H3cL4RedirectIpExclusionTable_Object = MibTable
h3cL4RedirectIpExclusionTable = _H3cL4RedirectIpExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 2)
)
if mibBuilder.loadTexts:
    h3cL4RedirectIpExclusionTable.setStatus("current")
_H3cL4RedirectIpExclusionEntry_Object = MibTableRow
h3cL4RedirectIpExclusionEntry = _H3cL4RedirectIpExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 2, 1)
)
h3cL4RedirectIpExclusionEntry.setIndexNames(
    (0, "H3C-L4RDT-MIB", "h3cL4RedirectIpExclusionIpAddress"),
)
if mibBuilder.loadTexts:
    h3cL4RedirectIpExclusionEntry.setStatus("current")
_H3cL4RedirectIpExclusionIpAddress_Type = IpAddress
_H3cL4RedirectIpExclusionIpAddress_Object = MibTableColumn
h3cL4RedirectIpExclusionIpAddress = _H3cL4RedirectIpExclusionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 2, 1, 1),
    _H3cL4RedirectIpExclusionIpAddress_Type()
)
h3cL4RedirectIpExclusionIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cL4RedirectIpExclusionIpAddress.setStatus("current")


class _H3cL4RedirectIpExclusionMaskLen_Type(Integer32):
    """Custom type h3cL4RedirectIpExclusionMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_H3cL4RedirectIpExclusionMaskLen_Type.__name__ = "Integer32"
_H3cL4RedirectIpExclusionMaskLen_Object = MibTableColumn
h3cL4RedirectIpExclusionMaskLen = _H3cL4RedirectIpExclusionMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 2, 1, 2),
    _H3cL4RedirectIpExclusionMaskLen_Type()
)
h3cL4RedirectIpExclusionMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectIpExclusionMaskLen.setStatus("current")
_H3cL4RedirectIpExclusionRowStatus_Type = RowStatus
_H3cL4RedirectIpExclusionRowStatus_Object = MibTableColumn
h3cL4RedirectIpExclusionRowStatus = _H3cL4RedirectIpExclusionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 2, 1, 3),
    _H3cL4RedirectIpExclusionRowStatus_Type()
)
h3cL4RedirectIpExclusionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectIpExclusionRowStatus.setStatus("current")
_H3cL4RedirectVlanTable_Object = MibTable
h3cL4RedirectVlanTable = _H3cL4RedirectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 3)
)
if mibBuilder.loadTexts:
    h3cL4RedirectVlanTable.setStatus("current")
_H3cL4RedirectVlanEntry_Object = MibTableRow
h3cL4RedirectVlanEntry = _H3cL4RedirectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 3, 1)
)
h3cL4RedirectVlanEntry.setIndexNames(
    (0, "H3C-L4RDT-MIB", "h3cL4RedirectVlanID"),
)
if mibBuilder.loadTexts:
    h3cL4RedirectVlanEntry.setStatus("current")
_H3cL4RedirectVlanID_Type = Integer32
_H3cL4RedirectVlanID_Object = MibTableColumn
h3cL4RedirectVlanID = _H3cL4RedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 3, 1, 1),
    _H3cL4RedirectVlanID_Type()
)
h3cL4RedirectVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cL4RedirectVlanID.setStatus("current")
_H3cL4RedirectVlanRowStatus_Type = RowStatus
_H3cL4RedirectVlanRowStatus_Object = MibTableColumn
h3cL4RedirectVlanRowStatus = _H3cL4RedirectVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 3, 1, 2),
    _H3cL4RedirectVlanRowStatus_Type()
)
h3cL4RedirectVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL4RedirectVlanRowStatus.setStatus("current")


class _H3cL4RedirectInformationString_Type(DisplayString):
    """Custom type h3cL4RedirectInformationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_H3cL4RedirectInformationString_Type.__name__ = "DisplayString"
_H3cL4RedirectInformationString_Object = MibScalar
h3cL4RedirectInformationString = _H3cL4RedirectInformationString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 4),
    _H3cL4RedirectInformationString_Type()
)
h3cL4RedirectInformationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cL4RedirectInformationString.setStatus("current")
_H3cL4RedirectFreeCacheEntries_Type = Integer32
_H3cL4RedirectFreeCacheEntries_Object = MibScalar
h3cL4RedirectFreeCacheEntries = _H3cL4RedirectFreeCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 5),
    _H3cL4RedirectFreeCacheEntries_Type()
)
h3cL4RedirectFreeCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cL4RedirectFreeCacheEntries.setStatus("current")
_H3cL4RedirectFreeIpExclusionEntries_Type = Integer32
_H3cL4RedirectFreeIpExclusionEntries_Object = MibScalar
h3cL4RedirectFreeIpExclusionEntries = _H3cL4RedirectFreeIpExclusionEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 6),
    _H3cL4RedirectFreeIpExclusionEntries_Type()
)
h3cL4RedirectFreeIpExclusionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cL4RedirectFreeIpExclusionEntries.setStatus("current")
_H3cL4RedirectFreeVlanEntries_Type = Integer32
_H3cL4RedirectFreeVlanEntries_Object = MibScalar
h3cL4RedirectFreeVlanEntries = _H3cL4RedirectFreeVlanEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 10, 7),
    _H3cL4RedirectFreeVlanEntries_Type()
)
h3cL4RedirectFreeVlanEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cL4RedirectFreeVlanEntries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-L4RDT-MIB",
    **{"h3cL4Redirect": h3cL4Redirect,
       "h3cL4RedirectCacheTable": h3cL4RedirectCacheTable,
       "h3cL4RedirectCacheEntry": h3cL4RedirectCacheEntry,
       "h3cL4RedirectCacheIpAddress": h3cL4RedirectCacheIpAddress,
       "h3cL4RedirectCacheRedirectionStatus": h3cL4RedirectCacheRedirectionStatus,
       "h3cL4RedirectCachePort": h3cL4RedirectCachePort,
       "h3cL4RedirectCacheRowStatus": h3cL4RedirectCacheRowStatus,
       "h3cL4RedirectCacheMacAddress": h3cL4RedirectCacheMacAddress,
       "h3cL4RedirectCacheVlan": h3cL4RedirectCacheVlan,
       "h3cL4RedirectCacheTcpPort": h3cL4RedirectCacheTcpPort,
       "h3cL4RedirectIpExclusionTable": h3cL4RedirectIpExclusionTable,
       "h3cL4RedirectIpExclusionEntry": h3cL4RedirectIpExclusionEntry,
       "h3cL4RedirectIpExclusionIpAddress": h3cL4RedirectIpExclusionIpAddress,
       "h3cL4RedirectIpExclusionMaskLen": h3cL4RedirectIpExclusionMaskLen,
       "h3cL4RedirectIpExclusionRowStatus": h3cL4RedirectIpExclusionRowStatus,
       "h3cL4RedirectVlanTable": h3cL4RedirectVlanTable,
       "h3cL4RedirectVlanEntry": h3cL4RedirectVlanEntry,
       "h3cL4RedirectVlanID": h3cL4RedirectVlanID,
       "h3cL4RedirectVlanRowStatus": h3cL4RedirectVlanRowStatus,
       "h3cL4RedirectInformationString": h3cL4RedirectInformationString,
       "h3cL4RedirectFreeCacheEntries": h3cL4RedirectFreeCacheEntries,
       "h3cL4RedirectFreeIpExclusionEntries": h3cL4RedirectFreeIpExclusionEntries,
       "h3cL4RedirectFreeVlanEntries": h3cL4RedirectFreeVlanEntries}
)
