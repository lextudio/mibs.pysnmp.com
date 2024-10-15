# SNMP MIB module (BAY-STACK-LLDP-EXT-DOT3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-LLDP-EXT-DOT3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:07 2024
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

(lldpXdot3LocPowerEntry,
 lldpXdot3RemPowerEntry) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT3-MIB",
    "lldpXdot3LocPowerEntry",
    "lldpXdot3RemPowerEntry")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackLldpXDot3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 47)
)
bayStackLldpXDot3Mib.setRevisions(
        ("2014-10-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsLldpXDot3Notifications_ObjectIdentity = ObjectIdentity
bsLldpXDot3Notifications = _BsLldpXDot3Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 0)
)
_BsLldpXDot3Objects_ObjectIdentity = ObjectIdentity
bsLldpXDot3Objects = _BsLldpXDot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1)
)
_BsLldpXdot3Config_ObjectIdentity = ObjectIdentity
bsLldpXdot3Config = _BsLldpXdot3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 1)
)
_BsLldpXdot3LocalData_ObjectIdentity = ObjectIdentity
bsLldpXdot3LocalData = _BsLldpXdot3LocalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2)
)
_BsLldpXdot3LocPowerTable_Object = MibTable
bsLldpXdot3LocPowerTable = _BsLldpXdot3LocPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bsLldpXdot3LocPowerTable.setStatus("current")
_BsLldpXdot3LocPowerEntry_Object = MibTableRow
bsLldpXdot3LocPowerEntry = _BsLldpXdot3LocPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    bsLldpXdot3LocPowerEntry.setStatus("current")


class _BsLldpXdot3LocPowerType_Type(Integer32):
    """Custom type bsLldpXdot3LocPowerType based on Integer32"""
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
        *(("type1pd", 4),
          ("type1pse", 3),
          ("type2pd", 2),
          ("type2pse", 1))
    )


_BsLldpXdot3LocPowerType_Type.__name__ = "Integer32"
_BsLldpXdot3LocPowerType_Object = MibTableColumn
bsLldpXdot3LocPowerType = _BsLldpXdot3LocPowerType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 1),
    _BsLldpXdot3LocPowerType_Type()
)
bsLldpXdot3LocPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPowerType.setStatus("current")


class _BsLldpXdot3LocPowerSource_Type(Integer32):
    """Custom type bsLldpXdot3LocPowerSource based on Integer32"""
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
        *(("backupPs", 3),
          ("primaryPs", 2),
          ("reserved", 4),
          ("unknown", 1))
    )


_BsLldpXdot3LocPowerSource_Type.__name__ = "Integer32"
_BsLldpXdot3LocPowerSource_Object = MibTableColumn
bsLldpXdot3LocPowerSource = _BsLldpXdot3LocPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 2),
    _BsLldpXdot3LocPowerSource_Type()
)
bsLldpXdot3LocPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPowerSource.setStatus("current")


class _BsLldpXdot3LocPowerPriority_Type(Integer32):
    """Custom type bsLldpXdot3LocPowerPriority based on Integer32"""
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
        *(("critical", 2),
          ("high", 3),
          ("low", 4),
          ("unknown", 1))
    )


_BsLldpXdot3LocPowerPriority_Type.__name__ = "Integer32"
_BsLldpXdot3LocPowerPriority_Object = MibTableColumn
bsLldpXdot3LocPowerPriority = _BsLldpXdot3LocPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 3),
    _BsLldpXdot3LocPowerPriority_Type()
)
bsLldpXdot3LocPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPowerPriority.setStatus("current")


class _BsLldpXdot3LocPDRequestedPowerValue_Type(Integer32):
    """Custom type bsLldpXdot3LocPDRequestedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsLldpXdot3LocPDRequestedPowerValue_Type.__name__ = "Integer32"
_BsLldpXdot3LocPDRequestedPowerValue_Object = MibTableColumn
bsLldpXdot3LocPDRequestedPowerValue = _BsLldpXdot3LocPDRequestedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 4),
    _BsLldpXdot3LocPDRequestedPowerValue_Type()
)
bsLldpXdot3LocPDRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPDRequestedPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPDRequestedPowerValue.setUnits("tenth of watt")


class _BsLldpXdot3LocPSEAllocatedPowerValue_Type(Integer32):
    """Custom type bsLldpXdot3LocPSEAllocatedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsLldpXdot3LocPSEAllocatedPowerValue_Type.__name__ = "Integer32"
_BsLldpXdot3LocPSEAllocatedPowerValue_Object = MibTableColumn
bsLldpXdot3LocPSEAllocatedPowerValue = _BsLldpXdot3LocPSEAllocatedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 2, 1, 1, 5),
    _BsLldpXdot3LocPSEAllocatedPowerValue_Type()
)
bsLldpXdot3LocPSEAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPSEAllocatedPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    bsLldpXdot3LocPSEAllocatedPowerValue.setUnits("tenth of watt")
_BsLldpXdot3RemoteData_ObjectIdentity = ObjectIdentity
bsLldpXdot3RemoteData = _BsLldpXdot3RemoteData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3)
)
_BsLldpXdot3RemPowerTable_Object = MibTable
bsLldpXdot3RemPowerTable = _BsLldpXdot3RemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bsLldpXdot3RemPowerTable.setStatus("current")
_BsLldpXdot3RemPowerEntry_Object = MibTableRow
bsLldpXdot3RemPowerEntry = _BsLldpXdot3RemPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bsLldpXdot3RemPowerEntry.setStatus("current")


class _BsLldpXdot3RemPowerType_Type(Integer32):
    """Custom type bsLldpXdot3RemPowerType based on Integer32"""
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
        *(("type1pd", 4),
          ("type1pse", 3),
          ("type2pd", 2),
          ("type2pse", 1))
    )


_BsLldpXdot3RemPowerType_Type.__name__ = "Integer32"
_BsLldpXdot3RemPowerType_Object = MibTableColumn
bsLldpXdot3RemPowerType = _BsLldpXdot3RemPowerType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 1),
    _BsLldpXdot3RemPowerType_Type()
)
bsLldpXdot3RemPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPowerType.setStatus("current")


class _BsLldpXdot3RemPowerSource_Type(Integer32):
    """Custom type bsLldpXdot3RemPowerSource based on Integer32"""
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
        *(("pse", 2),
          ("pseAndLocal", 4),
          ("reserved", 3),
          ("unknown", 1))
    )


_BsLldpXdot3RemPowerSource_Type.__name__ = "Integer32"
_BsLldpXdot3RemPowerSource_Object = MibTableColumn
bsLldpXdot3RemPowerSource = _BsLldpXdot3RemPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 2),
    _BsLldpXdot3RemPowerSource_Type()
)
bsLldpXdot3RemPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPowerSource.setStatus("current")


class _BsLldpXdot3RemPowerPriority_Type(Integer32):
    """Custom type bsLldpXdot3RemPowerPriority based on Integer32"""
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
        *(("critical", 2),
          ("high", 3),
          ("low", 4),
          ("unknown", 1))
    )


_BsLldpXdot3RemPowerPriority_Type.__name__ = "Integer32"
_BsLldpXdot3RemPowerPriority_Object = MibTableColumn
bsLldpXdot3RemPowerPriority = _BsLldpXdot3RemPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 3),
    _BsLldpXdot3RemPowerPriority_Type()
)
bsLldpXdot3RemPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPowerPriority.setStatus("current")


class _BsLldpXdot3RemPDRequestedPowerValue_Type(Integer32):
    """Custom type bsLldpXdot3RemPDRequestedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsLldpXdot3RemPDRequestedPowerValue_Type.__name__ = "Integer32"
_BsLldpXdot3RemPDRequestedPowerValue_Object = MibTableColumn
bsLldpXdot3RemPDRequestedPowerValue = _BsLldpXdot3RemPDRequestedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 4),
    _BsLldpXdot3RemPDRequestedPowerValue_Type()
)
bsLldpXdot3RemPDRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPDRequestedPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPDRequestedPowerValue.setUnits("tenth of watt")


class _BsLldpXdot3RemPSEAllocatedPowerValue_Type(Integer32):
    """Custom type bsLldpXdot3RemPSEAllocatedPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsLldpXdot3RemPSEAllocatedPowerValue_Type.__name__ = "Integer32"
_BsLldpXdot3RemPSEAllocatedPowerValue_Object = MibTableColumn
bsLldpXdot3RemPSEAllocatedPowerValue = _BsLldpXdot3RemPSEAllocatedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 47, 1, 3, 1, 1, 5),
    _BsLldpXdot3RemPSEAllocatedPowerValue_Type()
)
bsLldpXdot3RemPSEAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPSEAllocatedPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    bsLldpXdot3RemPSEAllocatedPowerValue.setUnits("tenth of watt")
lldpXdot3LocPowerEntry.registerAugmentions(
    ("BAY-STACK-LLDP-EXT-DOT3-MIB",
     "bsLldpXdot3LocPowerEntry")
)
bsLldpXdot3LocPowerEntry.setIndexNames(*lldpXdot3LocPowerEntry.getIndexNames())
lldpXdot3RemPowerEntry.registerAugmentions(
    ("BAY-STACK-LLDP-EXT-DOT3-MIB",
     "bsLldpXdot3RemPowerEntry")
)
bsLldpXdot3RemPowerEntry.setIndexNames(*lldpXdot3RemPowerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-LLDP-EXT-DOT3-MIB",
    **{"bayStackLldpXDot3Mib": bayStackLldpXDot3Mib,
       "bsLldpXDot3Notifications": bsLldpXDot3Notifications,
       "bsLldpXDot3Objects": bsLldpXDot3Objects,
       "bsLldpXdot3Config": bsLldpXdot3Config,
       "bsLldpXdot3LocalData": bsLldpXdot3LocalData,
       "bsLldpXdot3LocPowerTable": bsLldpXdot3LocPowerTable,
       "bsLldpXdot3LocPowerEntry": bsLldpXdot3LocPowerEntry,
       "bsLldpXdot3LocPowerType": bsLldpXdot3LocPowerType,
       "bsLldpXdot3LocPowerSource": bsLldpXdot3LocPowerSource,
       "bsLldpXdot3LocPowerPriority": bsLldpXdot3LocPowerPriority,
       "bsLldpXdot3LocPDRequestedPowerValue": bsLldpXdot3LocPDRequestedPowerValue,
       "bsLldpXdot3LocPSEAllocatedPowerValue": bsLldpXdot3LocPSEAllocatedPowerValue,
       "bsLldpXdot3RemoteData": bsLldpXdot3RemoteData,
       "bsLldpXdot3RemPowerTable": bsLldpXdot3RemPowerTable,
       "bsLldpXdot3RemPowerEntry": bsLldpXdot3RemPowerEntry,
       "bsLldpXdot3RemPowerType": bsLldpXdot3RemPowerType,
       "bsLldpXdot3RemPowerSource": bsLldpXdot3RemPowerSource,
       "bsLldpXdot3RemPowerPriority": bsLldpXdot3RemPowerPriority,
       "bsLldpXdot3RemPDRequestedPowerValue": bsLldpXdot3RemPDRequestedPowerValue,
       "bsLldpXdot3RemPSEAllocatedPowerValue": bsLldpXdot3RemPSEAllocatedPowerValue}
)
