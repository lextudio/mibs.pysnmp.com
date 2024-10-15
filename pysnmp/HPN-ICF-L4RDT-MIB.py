# SNMP MIB module (HPN-ICF-L4RDT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-L4RDT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:43 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfL4Redirect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfL4RedirectCacheTable_Object = MibTable
hpnicfL4RedirectCacheTable = _HpnicfL4RedirectCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1)
)
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheTable.setStatus("current")
_HpnicfL4RedirectCacheEntry_Object = MibTableRow
hpnicfL4RedirectCacheEntry = _HpnicfL4RedirectCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1)
)
hpnicfL4RedirectCacheEntry.setIndexNames(
    (0, "HPN-ICF-L4RDT-MIB", "hpnicfL4RedirectCacheIpAddress"),
)
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheEntry.setStatus("current")
_HpnicfL4RedirectCacheIpAddress_Type = IpAddress
_HpnicfL4RedirectCacheIpAddress_Object = MibTableColumn
hpnicfL4RedirectCacheIpAddress = _HpnicfL4RedirectCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 1),
    _HpnicfL4RedirectCacheIpAddress_Type()
)
hpnicfL4RedirectCacheIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheIpAddress.setStatus("current")


class _HpnicfL4RedirectCacheRedirectionStatus_Type(Integer32):
    """Custom type hpnicfL4RedirectCacheRedirectionStatus based on Integer32"""
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


_HpnicfL4RedirectCacheRedirectionStatus_Type.__name__ = "Integer32"
_HpnicfL4RedirectCacheRedirectionStatus_Object = MibTableColumn
hpnicfL4RedirectCacheRedirectionStatus = _HpnicfL4RedirectCacheRedirectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 2),
    _HpnicfL4RedirectCacheRedirectionStatus_Type()
)
hpnicfL4RedirectCacheRedirectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheRedirectionStatus.setStatus("current")
_HpnicfL4RedirectCachePort_Type = Integer32
_HpnicfL4RedirectCachePort_Object = MibTableColumn
hpnicfL4RedirectCachePort = _HpnicfL4RedirectCachePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 3),
    _HpnicfL4RedirectCachePort_Type()
)
hpnicfL4RedirectCachePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCachePort.setStatus("current")
_HpnicfL4RedirectCacheRowStatus_Type = RowStatus
_HpnicfL4RedirectCacheRowStatus_Object = MibTableColumn
hpnicfL4RedirectCacheRowStatus = _HpnicfL4RedirectCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 4),
    _HpnicfL4RedirectCacheRowStatus_Type()
)
hpnicfL4RedirectCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheRowStatus.setStatus("current")
_HpnicfL4RedirectCacheMacAddress_Type = MacAddress
_HpnicfL4RedirectCacheMacAddress_Object = MibTableColumn
hpnicfL4RedirectCacheMacAddress = _HpnicfL4RedirectCacheMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 5),
    _HpnicfL4RedirectCacheMacAddress_Type()
)
hpnicfL4RedirectCacheMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheMacAddress.setStatus("current")
_HpnicfL4RedirectCacheVlan_Type = Integer32
_HpnicfL4RedirectCacheVlan_Object = MibTableColumn
hpnicfL4RedirectCacheVlan = _HpnicfL4RedirectCacheVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 6),
    _HpnicfL4RedirectCacheVlan_Type()
)
hpnicfL4RedirectCacheVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheVlan.setStatus("current")
_HpnicfL4RedirectCacheTcpPort_Type = Integer32
_HpnicfL4RedirectCacheTcpPort_Object = MibTableColumn
hpnicfL4RedirectCacheTcpPort = _HpnicfL4RedirectCacheTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 1, 1, 7),
    _HpnicfL4RedirectCacheTcpPort_Type()
)
hpnicfL4RedirectCacheTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectCacheTcpPort.setStatus("current")
_HpnicfL4RedirectIpExclusionTable_Object = MibTable
hpnicfL4RedirectIpExclusionTable = _HpnicfL4RedirectIpExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hpnicfL4RedirectIpExclusionTable.setStatus("current")
_HpnicfL4RedirectIpExclusionEntry_Object = MibTableRow
hpnicfL4RedirectIpExclusionEntry = _HpnicfL4RedirectIpExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 2, 1)
)
hpnicfL4RedirectIpExclusionEntry.setIndexNames(
    (0, "HPN-ICF-L4RDT-MIB", "hpnicfL4RedirectIpExclusionIpAddress"),
)
if mibBuilder.loadTexts:
    hpnicfL4RedirectIpExclusionEntry.setStatus("current")
_HpnicfL4RedirectIpExclusionIpAddress_Type = IpAddress
_HpnicfL4RedirectIpExclusionIpAddress_Object = MibTableColumn
hpnicfL4RedirectIpExclusionIpAddress = _HpnicfL4RedirectIpExclusionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 2, 1, 1),
    _HpnicfL4RedirectIpExclusionIpAddress_Type()
)
hpnicfL4RedirectIpExclusionIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfL4RedirectIpExclusionIpAddress.setStatus("current")


class _HpnicfL4RedirectIpExclusionMaskLen_Type(Integer32):
    """Custom type hpnicfL4RedirectIpExclusionMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpnicfL4RedirectIpExclusionMaskLen_Type.__name__ = "Integer32"
_HpnicfL4RedirectIpExclusionMaskLen_Object = MibTableColumn
hpnicfL4RedirectIpExclusionMaskLen = _HpnicfL4RedirectIpExclusionMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 2, 1, 2),
    _HpnicfL4RedirectIpExclusionMaskLen_Type()
)
hpnicfL4RedirectIpExclusionMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectIpExclusionMaskLen.setStatus("current")
_HpnicfL4RedirectIpExclusionRowStatus_Type = RowStatus
_HpnicfL4RedirectIpExclusionRowStatus_Object = MibTableColumn
hpnicfL4RedirectIpExclusionRowStatus = _HpnicfL4RedirectIpExclusionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 2, 1, 3),
    _HpnicfL4RedirectIpExclusionRowStatus_Type()
)
hpnicfL4RedirectIpExclusionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectIpExclusionRowStatus.setStatus("current")
_HpnicfL4RedirectVlanTable_Object = MibTable
hpnicfL4RedirectVlanTable = _HpnicfL4RedirectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 3)
)
if mibBuilder.loadTexts:
    hpnicfL4RedirectVlanTable.setStatus("current")
_HpnicfL4RedirectVlanEntry_Object = MibTableRow
hpnicfL4RedirectVlanEntry = _HpnicfL4RedirectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 3, 1)
)
hpnicfL4RedirectVlanEntry.setIndexNames(
    (0, "HPN-ICF-L4RDT-MIB", "hpnicfL4RedirectVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfL4RedirectVlanEntry.setStatus("current")
_HpnicfL4RedirectVlanID_Type = Integer32
_HpnicfL4RedirectVlanID_Object = MibTableColumn
hpnicfL4RedirectVlanID = _HpnicfL4RedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 3, 1, 1),
    _HpnicfL4RedirectVlanID_Type()
)
hpnicfL4RedirectVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfL4RedirectVlanID.setStatus("current")
_HpnicfL4RedirectVlanRowStatus_Type = RowStatus
_HpnicfL4RedirectVlanRowStatus_Object = MibTableColumn
hpnicfL4RedirectVlanRowStatus = _HpnicfL4RedirectVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 3, 1, 2),
    _HpnicfL4RedirectVlanRowStatus_Type()
)
hpnicfL4RedirectVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL4RedirectVlanRowStatus.setStatus("current")


class _HpnicfL4RedirectInformationString_Type(DisplayString):
    """Custom type hpnicfL4RedirectInformationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnicfL4RedirectInformationString_Type.__name__ = "DisplayString"
_HpnicfL4RedirectInformationString_Object = MibScalar
hpnicfL4RedirectInformationString = _HpnicfL4RedirectInformationString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 4),
    _HpnicfL4RedirectInformationString_Type()
)
hpnicfL4RedirectInformationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL4RedirectInformationString.setStatus("current")
_HpnicfL4RedirectFreeCacheEntries_Type = Integer32
_HpnicfL4RedirectFreeCacheEntries_Object = MibScalar
hpnicfL4RedirectFreeCacheEntries = _HpnicfL4RedirectFreeCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 5),
    _HpnicfL4RedirectFreeCacheEntries_Type()
)
hpnicfL4RedirectFreeCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL4RedirectFreeCacheEntries.setStatus("current")
_HpnicfL4RedirectFreeIpExclusionEntries_Type = Integer32
_HpnicfL4RedirectFreeIpExclusionEntries_Object = MibScalar
hpnicfL4RedirectFreeIpExclusionEntries = _HpnicfL4RedirectFreeIpExclusionEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 6),
    _HpnicfL4RedirectFreeIpExclusionEntries_Type()
)
hpnicfL4RedirectFreeIpExclusionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL4RedirectFreeIpExclusionEntries.setStatus("current")
_HpnicfL4RedirectFreeVlanEntries_Type = Integer32
_HpnicfL4RedirectFreeVlanEntries_Object = MibScalar
hpnicfL4RedirectFreeVlanEntries = _HpnicfL4RedirectFreeVlanEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10, 7),
    _HpnicfL4RedirectFreeVlanEntries_Type()
)
hpnicfL4RedirectFreeVlanEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfL4RedirectFreeVlanEntries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-L4RDT-MIB",
    **{"hpnicfL4Redirect": hpnicfL4Redirect,
       "hpnicfL4RedirectCacheTable": hpnicfL4RedirectCacheTable,
       "hpnicfL4RedirectCacheEntry": hpnicfL4RedirectCacheEntry,
       "hpnicfL4RedirectCacheIpAddress": hpnicfL4RedirectCacheIpAddress,
       "hpnicfL4RedirectCacheRedirectionStatus": hpnicfL4RedirectCacheRedirectionStatus,
       "hpnicfL4RedirectCachePort": hpnicfL4RedirectCachePort,
       "hpnicfL4RedirectCacheRowStatus": hpnicfL4RedirectCacheRowStatus,
       "hpnicfL4RedirectCacheMacAddress": hpnicfL4RedirectCacheMacAddress,
       "hpnicfL4RedirectCacheVlan": hpnicfL4RedirectCacheVlan,
       "hpnicfL4RedirectCacheTcpPort": hpnicfL4RedirectCacheTcpPort,
       "hpnicfL4RedirectIpExclusionTable": hpnicfL4RedirectIpExclusionTable,
       "hpnicfL4RedirectIpExclusionEntry": hpnicfL4RedirectIpExclusionEntry,
       "hpnicfL4RedirectIpExclusionIpAddress": hpnicfL4RedirectIpExclusionIpAddress,
       "hpnicfL4RedirectIpExclusionMaskLen": hpnicfL4RedirectIpExclusionMaskLen,
       "hpnicfL4RedirectIpExclusionRowStatus": hpnicfL4RedirectIpExclusionRowStatus,
       "hpnicfL4RedirectVlanTable": hpnicfL4RedirectVlanTable,
       "hpnicfL4RedirectVlanEntry": hpnicfL4RedirectVlanEntry,
       "hpnicfL4RedirectVlanID": hpnicfL4RedirectVlanID,
       "hpnicfL4RedirectVlanRowStatus": hpnicfL4RedirectVlanRowStatus,
       "hpnicfL4RedirectInformationString": hpnicfL4RedirectInformationString,
       "hpnicfL4RedirectFreeCacheEntries": hpnicfL4RedirectFreeCacheEntries,
       "hpnicfL4RedirectFreeIpExclusionEntries": hpnicfL4RedirectFreeIpExclusionEntries,
       "hpnicfL4RedirectFreeVlanEntries": hpnicfL4RedirectFreeVlanEntries}
)
