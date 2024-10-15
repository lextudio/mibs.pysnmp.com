# SNMP MIB module (DNSHOTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNSHOTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:26 2024
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

(dnshotExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "dnshotExt")

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

apDnshotExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApDnshotExtEnable_Type(Integer32):
    """Custom type apDnshotExtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApDnshotExtEnable_Type.__name__ = "Integer32"
_ApDnshotExtEnable_Object = MibScalar
apDnshotExtEnable = _ApDnshotExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 2),
    _ApDnshotExtEnable_Type()
)
apDnshotExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnshotExtEnable.setStatus("current")


class _ApDnshotExtSize_Type(Integer32):
    """Custom type apDnshotExtSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ApDnshotExtSize_Type.__name__ = "Integer32"
_ApDnshotExtSize_Object = MibScalar
apDnshotExtSize = _ApDnshotExtSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 3),
    _ApDnshotExtSize_Type()
)
apDnshotExtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDnshotExtSize.setStatus("current")


class _ApDnshotExtInterval_Type(Integer32):
    """Custom type apDnshotExtInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ApDnshotExtInterval_Type.__name__ = "Integer32"
_ApDnshotExtInterval_Object = MibScalar
apDnshotExtInterval = _ApDnshotExtInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 4),
    _ApDnshotExtInterval_Type()
)
apDnshotExtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDnshotExtInterval.setStatus("current")


class _ApDnshotExtThreshold_Type(Integer32):
    """Custom type apDnshotExtThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApDnshotExtThreshold_Type.__name__ = "Integer32"
_ApDnshotExtThreshold_Object = MibScalar
apDnshotExtThreshold = _ApDnshotExtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 5),
    _ApDnshotExtThreshold_Type()
)
apDnshotExtThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apDnshotExtThreshold.setStatus("current")
_ApDnshotExtTable_Object = MibTable
apDnshotExtTable = _ApDnshotExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 6)
)
if mibBuilder.loadTexts:
    apDnshotExtTable.setStatus("current")
_ApDnshotEntry_Object = MibTableRow
apDnshotEntry = _ApDnshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 6, 1)
)
apDnshotEntry.setIndexNames(
    (0, "DNSHOTEXT-MIB", "apDnshotIndex"),
)
if mibBuilder.loadTexts:
    apDnshotEntry.setStatus("current")


class _ApDnshotIndex_Type(Integer32):
    """Custom type apDnshotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApDnshotIndex_Type.__name__ = "Integer32"
_ApDnshotIndex_Object = MibTableColumn
apDnshotIndex = _ApDnshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 6, 1, 1),
    _ApDnshotIndex_Type()
)
apDnshotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnshotIndex.setStatus("current")


class _ApDnshotName_Type(DisplayString):
    """Custom type apDnshotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApDnshotName_Type.__name__ = "DisplayString"
_ApDnshotName_Object = MibTableColumn
apDnshotName = _ApDnshotName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 6, 1, 2),
    _ApDnshotName_Type()
)
apDnshotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnshotName.setStatus("current")
_ApDnshotHits_Type = Counter32
_ApDnshotHits_Object = MibTableColumn
apDnshotHits = _ApDnshotHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 48, 6, 1, 3),
    _ApDnshotHits_Type()
)
apDnshotHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDnshotHits.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNSHOTEXT-MIB",
    **{"apDnshotExtMib": apDnshotExtMib,
       "apDnshotExtEnable": apDnshotExtEnable,
       "apDnshotExtSize": apDnshotExtSize,
       "apDnshotExtInterval": apDnshotExtInterval,
       "apDnshotExtThreshold": apDnshotExtThreshold,
       "apDnshotExtTable": apDnshotExtTable,
       "apDnshotEntry": apDnshotEntry,
       "apDnshotIndex": apDnshotIndex,
       "apDnshotName": apDnshotName,
       "apDnshotHits": apDnshotHits}
)
