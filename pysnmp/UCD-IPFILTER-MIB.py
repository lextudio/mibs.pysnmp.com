# SNMP MIB module (UCD-IPFILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UCD-IPFILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:21 2024
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

(ucdExperimental,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental")


# MODULE-IDENTITY

ucdIpFilter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2)
)
ucdIpFilter.setRevisions(
        ("2000-01-26 00:00",
         "1999-12-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpfInTable_Object = MibTable
ipfInTable = _IpfInTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 1)
)
if mibBuilder.loadTexts:
    ipfInTable.setStatus("current")
_IpfInEntry_Object = MibTableRow
ipfInEntry = _IpfInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 1, 1)
)
ipfInEntry.setIndexNames(
    (0, "UCD-IPFILTER-MIB", "ipfInIndex"),
)
if mibBuilder.loadTexts:
    ipfInEntry.setStatus("current")


class _IpfInIndex_Type(Integer32):
    """Custom type ipfInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpfInIndex_Type.__name__ = "Integer32"
_IpfInIndex_Object = MibTableColumn
ipfInIndex = _IpfInIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 1, 1, 1),
    _IpfInIndex_Type()
)
ipfInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInIndex.setStatus("current")
_IpfInRule_Type = OctetString
_IpfInRule_Object = MibTableColumn
ipfInRule = _IpfInRule_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 1, 1, 2),
    _IpfInRule_Type()
)
ipfInRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInRule.setStatus("current")
_IpfInHits_Type = Counter32
_IpfInHits_Object = MibTableColumn
ipfInHits = _IpfInHits_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 1, 1, 3),
    _IpfInHits_Type()
)
ipfInHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfInHits.setStatus("current")
_IpfOutTable_Object = MibTable
ipfOutTable = _IpfOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 2)
)
if mibBuilder.loadTexts:
    ipfOutTable.setStatus("current")
_IpfOutEntry_Object = MibTableRow
ipfOutEntry = _IpfOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 2, 1)
)
ipfOutEntry.setIndexNames(
    (0, "UCD-IPFILTER-MIB", "ipfOutIndex"),
)
if mibBuilder.loadTexts:
    ipfOutEntry.setStatus("current")


class _IpfOutIndex_Type(Integer32):
    """Custom type ipfOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfOutIndex_Type.__name__ = "Integer32"
_IpfOutIndex_Object = MibTableColumn
ipfOutIndex = _IpfOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 2, 1, 1),
    _IpfOutIndex_Type()
)
ipfOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfOutIndex.setStatus("current")
_IpfOutRule_Type = OctetString
_IpfOutRule_Object = MibTableColumn
ipfOutRule = _IpfOutRule_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 2, 1, 2),
    _IpfOutRule_Type()
)
ipfOutRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfOutRule.setStatus("current")
_IpfOutHits_Type = Counter32
_IpfOutHits_Object = MibTableColumn
ipfOutHits = _IpfOutHits_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 2, 1, 3),
    _IpfOutHits_Type()
)
ipfOutHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfOutHits.setStatus("current")
_IpfAccInTable_Object = MibTable
ipfAccInTable = _IpfAccInTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 3)
)
if mibBuilder.loadTexts:
    ipfAccInTable.setStatus("current")
_IpfAccInEntry_Object = MibTableRow
ipfAccInEntry = _IpfAccInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 3, 1)
)
ipfAccInEntry.setIndexNames(
    (0, "UCD-IPFILTER-MIB", "ipfAccInIndex"),
)
if mibBuilder.loadTexts:
    ipfAccInEntry.setStatus("current")


class _IpfAccInIndex_Type(Integer32):
    """Custom type ipfAccInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfAccInIndex_Type.__name__ = "Integer32"
_IpfAccInIndex_Object = MibTableColumn
ipfAccInIndex = _IpfAccInIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 3, 1, 1),
    _IpfAccInIndex_Type()
)
ipfAccInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccInIndex.setStatus("current")
_IpfAccInRule_Type = OctetString
_IpfAccInRule_Object = MibTableColumn
ipfAccInRule = _IpfAccInRule_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 3, 1, 2),
    _IpfAccInRule_Type()
)
ipfAccInRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccInRule.setStatus("current")
_IpfAccInHits_Type = Counter32
_IpfAccInHits_Object = MibTableColumn
ipfAccInHits = _IpfAccInHits_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 3, 1, 3),
    _IpfAccInHits_Type()
)
ipfAccInHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccInHits.setStatus("current")
_IpfAccInBytes_Type = Counter32
_IpfAccInBytes_Object = MibTableColumn
ipfAccInBytes = _IpfAccInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 3, 1, 4),
    _IpfAccInBytes_Type()
)
ipfAccInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccInBytes.setStatus("current")
_IpfAccOutTable_Object = MibTable
ipfAccOutTable = _IpfAccOutTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 4)
)
if mibBuilder.loadTexts:
    ipfAccOutTable.setStatus("current")
_IpfAccOutEntry_Object = MibTableRow
ipfAccOutEntry = _IpfAccOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 4, 1)
)
ipfAccOutEntry.setIndexNames(
    (0, "UCD-IPFILTER-MIB", "ipfAccOutIndex"),
)
if mibBuilder.loadTexts:
    ipfAccOutEntry.setStatus("current")


class _IpfAccOutIndex_Type(Integer32):
    """Custom type ipfAccOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfAccOutIndex_Type.__name__ = "Integer32"
_IpfAccOutIndex_Object = MibTableColumn
ipfAccOutIndex = _IpfAccOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 4, 1, 1),
    _IpfAccOutIndex_Type()
)
ipfAccOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccOutIndex.setStatus("current")
_IpfAccOutRule_Type = OctetString
_IpfAccOutRule_Object = MibTableColumn
ipfAccOutRule = _IpfAccOutRule_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 4, 1, 2),
    _IpfAccOutRule_Type()
)
ipfAccOutRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccOutRule.setStatus("current")
_IpfAccOutHits_Type = Counter32
_IpfAccOutHits_Object = MibTableColumn
ipfAccOutHits = _IpfAccOutHits_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 4, 1, 3),
    _IpfAccOutHits_Type()
)
ipfAccOutHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccOutHits.setStatus("current")
_IpfAccOutBytes_Type = Counter32
_IpfAccOutBytes_Object = MibTableColumn
ipfAccOutBytes = _IpfAccOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 2, 4, 1, 4),
    _IpfAccOutBytes_Type()
)
ipfAccOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfAccOutBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UCD-IPFILTER-MIB",
    **{"ucdIpFilter": ucdIpFilter,
       "ipfInTable": ipfInTable,
       "ipfInEntry": ipfInEntry,
       "ipfInIndex": ipfInIndex,
       "ipfInRule": ipfInRule,
       "ipfInHits": ipfInHits,
       "ipfOutTable": ipfOutTable,
       "ipfOutEntry": ipfOutEntry,
       "ipfOutIndex": ipfOutIndex,
       "ipfOutRule": ipfOutRule,
       "ipfOutHits": ipfOutHits,
       "ipfAccInTable": ipfAccInTable,
       "ipfAccInEntry": ipfAccInEntry,
       "ipfAccInIndex": ipfAccInIndex,
       "ipfAccInRule": ipfAccInRule,
       "ipfAccInHits": ipfAccInHits,
       "ipfAccInBytes": ipfAccInBytes,
       "ipfAccOutTable": ipfAccOutTable,
       "ipfAccOutEntry": ipfAccOutEntry,
       "ipfAccOutIndex": ipfAccOutIndex,
       "ipfAccOutRule": ipfAccOutRule,
       "ipfAccOutHits": ipfAccOutHits,
       "ipfAccOutBytes": ipfAccOutBytes}
)
