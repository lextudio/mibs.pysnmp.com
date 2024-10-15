# SNMP MIB module (PLUCEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PLUCEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:01 2024
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

(plucExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "plucExt")

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


# MODULE-IDENTITY

apPlucExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApPlucCacheSize_Type(Integer32):
    """Custom type apPlucCacheSize based on Integer32"""
    defaultValue = 16000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48000),
    )


_ApPlucCacheSize_Type.__name__ = "Integer32"
_ApPlucCacheSize_Object = MibScalar
apPlucCacheSize = _ApPlucCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 2),
    _ApPlucCacheSize_Type()
)
apPlucCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPlucCacheSize.setStatus("current")
_ApPlucCacheTable_Object = MibTable
apPlucCacheTable = _ApPlucCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3)
)
if mibBuilder.loadTexts:
    apPlucCacheTable.setStatus("current")
_ApPlucCacheEntry_Object = MibTableRow
apPlucCacheEntry = _ApPlucCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3, 1)
)
apPlucCacheEntry.setIndexNames(
    (0, "PLUCEXT-MIB", "apPlucCacheIpAddress"),
    (0, "PLUCEXT-MIB", "apPlucCacheIpPrefix"),
)
if mibBuilder.loadTexts:
    apPlucCacheEntry.setStatus("current")
_ApPlucCacheIpAddress_Type = IpAddress
_ApPlucCacheIpAddress_Object = MibTableColumn
apPlucCacheIpAddress = _ApPlucCacheIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3, 1, 1),
    _ApPlucCacheIpAddress_Type()
)
apPlucCacheIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIpAddress.setStatus("current")
_ApPlucCacheIpPrefix_Type = Integer32
_ApPlucCacheIpPrefix_Object = MibTableColumn
apPlucCacheIpPrefix = _ApPlucCacheIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3, 1, 2),
    _ApPlucCacheIpPrefix_Type()
)
apPlucCacheIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIpPrefix.setStatus("current")
_ApPlucCacheTTL_Type = Integer32
_ApPlucCacheTTL_Object = MibTableColumn
apPlucCacheTTL = _ApPlucCacheTTL_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3, 1, 3),
    _ApPlucCacheTTL_Type()
)
apPlucCacheTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheTTL.setStatus("current")
_ApPlucCacheHits_Type = Integer32
_ApPlucCacheHits_Object = MibTableColumn
apPlucCacheHits = _ApPlucCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3, 1, 4),
    _ApPlucCacheHits_Type()
)
apPlucCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheHits.setStatus("current")
_ApPlucCacheIndexCount_Type = Integer32
_ApPlucCacheIndexCount_Object = MibTableColumn
apPlucCacheIndexCount = _ApPlucCacheIndexCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 3, 1, 5),
    _ApPlucCacheIndexCount_Type()
)
apPlucCacheIndexCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIndexCount.setStatus("current")
_ApPlucCacheIndexTable_Object = MibTable
apPlucCacheIndexTable = _ApPlucCacheIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 4)
)
if mibBuilder.loadTexts:
    apPlucCacheIndexTable.setStatus("current")
_ApPlucCacheIndexEntry_Object = MibTableRow
apPlucCacheIndexEntry = _ApPlucCacheIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 4, 1)
)
apPlucCacheIndexEntry.setIndexNames(
    (0, "PLUCEXT-MIB", "apPlucCacheIndexIpAddress"),
    (0, "PLUCEXT-MIB", "apPlucCacheIndexIpPrefix"),
    (0, "PLUCEXT-MIB", "apPlucCacheIndexZoneIndex"),
)
if mibBuilder.loadTexts:
    apPlucCacheIndexEntry.setStatus("current")
_ApPlucCacheIndexIpAddress_Type = IpAddress
_ApPlucCacheIndexIpAddress_Object = MibTableColumn
apPlucCacheIndexIpAddress = _ApPlucCacheIndexIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 4, 1, 1),
    _ApPlucCacheIndexIpAddress_Type()
)
apPlucCacheIndexIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIndexIpAddress.setStatus("current")
_ApPlucCacheIndexIpPrefix_Type = Integer32
_ApPlucCacheIndexIpPrefix_Object = MibTableColumn
apPlucCacheIndexIpPrefix = _ApPlucCacheIndexIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 4, 1, 2),
    _ApPlucCacheIndexIpPrefix_Type()
)
apPlucCacheIndexIpPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIndexIpPrefix.setStatus("current")
_ApPlucCacheIndexZoneIndex_Type = Integer32
_ApPlucCacheIndexZoneIndex_Object = MibTableColumn
apPlucCacheIndexZoneIndex = _ApPlucCacheIndexZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 4, 1, 3),
    _ApPlucCacheIndexZoneIndex_Type()
)
apPlucCacheIndexZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIndexZoneIndex.setStatus("current")
_ApPlucCacheIndexValue_Type = Integer32
_ApPlucCacheIndexValue_Object = MibTableColumn
apPlucCacheIndexValue = _ApPlucCacheIndexValue_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 56, 4, 1, 4),
    _ApPlucCacheIndexValue_Type()
)
apPlucCacheIndexValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPlucCacheIndexValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PLUCEXT-MIB",
    **{"apPlucExtMib": apPlucExtMib,
       "apPlucCacheSize": apPlucCacheSize,
       "apPlucCacheTable": apPlucCacheTable,
       "apPlucCacheEntry": apPlucCacheEntry,
       "apPlucCacheIpAddress": apPlucCacheIpAddress,
       "apPlucCacheIpPrefix": apPlucCacheIpPrefix,
       "apPlucCacheTTL": apPlucCacheTTL,
       "apPlucCacheHits": apPlucCacheHits,
       "apPlucCacheIndexCount": apPlucCacheIndexCount,
       "apPlucCacheIndexTable": apPlucCacheIndexTable,
       "apPlucCacheIndexEntry": apPlucCacheIndexEntry,
       "apPlucCacheIndexIpAddress": apPlucCacheIndexIpAddress,
       "apPlucCacheIndexIpPrefix": apPlucCacheIndexIpPrefix,
       "apPlucCacheIndexZoneIndex": apPlucCacheIndexZoneIndex,
       "apPlucCacheIndexValue": apPlucCacheIndexValue}
)
