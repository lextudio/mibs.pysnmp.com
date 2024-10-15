# SNMP MIB module (MITEL-BCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-BCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:12 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(mitelPropTransmission,) = mibBuilder.importSymbols(
    "MITEL-MIB",
    "mitelPropTransmission")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mitelBCM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1)
)
mitelBCM.setRevisions(
        ("2009-03-17 00:00",
         "2006-01-10 00:00",
         "2005-10-04 01:00",
         "2005-10-03 01:00",
         "2005-09-30 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MitelBCMObjects_ObjectIdentity = ObjectIdentity
mitelBCMObjects = _MitelBCMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1)
)
_MitelBCMPortTable_Object = MibTable
mitelBCMPortTable = _MitelBCMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mitelBCMPortTable.setStatus("current")
_MitelBCMPortTableEntry_Object = MibTableRow
mitelBCMPortTableEntry = _MitelBCMPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 1, 1)
)
mitelBCMPortTableEntry.setIndexNames(
    (0, "MITEL-BCM-MIB", "mitelBCMPortIndex"),
)
if mibBuilder.loadTexts:
    mitelBCMPortTableEntry.setStatus("current")
_MitelBCMPortIndex_Type = InterfaceIndex
_MitelBCMPortIndex_Object = MibTableColumn
mitelBCMPortIndex = _MitelBCMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 1, 1, 1),
    _MitelBCMPortIndex_Type()
)
mitelBCMPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMPortIndex.setStatus("current")
_MitelBCMPortRxSAChanges_Type = Counter32
_MitelBCMPortRxSAChanges_Object = MibTableColumn
mitelBCMPortRxSAChanges = _MitelBCMPortRxSAChanges_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 1, 1, 2),
    _MitelBCMPortRxSAChanges_Type()
)
mitelBCMPortRxSAChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMPortRxSAChanges.setStatus("current")
_MitelBCMPortRxLastSA_Type = PhysAddress
_MitelBCMPortRxLastSA_Object = MibTableColumn
mitelBCMPortRxLastSA = _MitelBCMPortRxLastSA_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 1, 1, 3),
    _MitelBCMPortRxLastSA_Type()
)
mitelBCMPortRxLastSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMPortRxLastSA.setStatus("current")
_MitelBCMChipCount_Type = Integer32
_MitelBCMChipCount_Object = MibScalar
mitelBCMChipCount = _MitelBCMChipCount_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 2),
    _MitelBCMChipCount_Type()
)
mitelBCMChipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMChipCount.setStatus("current")
_MitelBCMChipTable_Object = MibTable
mitelBCMChipTable = _MitelBCMChipTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mitelBCMChipTable.setStatus("current")
_MitelBCMChipTableEntry_Object = MibTableRow
mitelBCMChipTableEntry = _MitelBCMChipTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 3, 1)
)
mitelBCMChipTableEntry.setIndexNames(
    (0, "MITEL-BCM-MIB", "mitelBCMChipIndex"),
)
if mibBuilder.loadTexts:
    mitelBCMChipTableEntry.setStatus("current")


class _MitelBCMChipIndex_Type(Integer32):
    """Custom type mitelBCMChipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MitelBCMChipIndex_Type.__name__ = "Integer32"
_MitelBCMChipIndex_Object = MibTableColumn
mitelBCMChipIndex = _MitelBCMChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 3, 1, 1),
    _MitelBCMChipIndex_Type()
)
mitelBCMChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMChipIndex.setStatus("current")


class _MitelBCMChipBIST_Type(Bits):
    """Custom type mitelBCMChipBIST based on Bits"""
    namedValues = NamedValues(
        *(("bcRam", 0),
          ("gmRam", 3),
          ("ipDbm", 1),
          ("mRam", 2))
    )

_MitelBCMChipBIST_Type.__name__ = "Bits"
_MitelBCMChipBIST_Object = MibTableColumn
mitelBCMChipBIST = _MitelBCMChipBIST_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 3, 1, 2),
    _MitelBCMChipBIST_Type()
)
mitelBCMChipBIST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMChipBIST.setStatus("current")
_MitelBCMChipRev_Type = DisplayString
_MitelBCMChipRev_Object = MibTableColumn
mitelBCMChipRev = _MitelBCMChipRev_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 3, 1, 3),
    _MitelBCMChipRev_Type()
)
mitelBCMChipRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMChipRev.setStatus("current")


class _MitelBCMChipType_Type(Integer32):
    """Custom type mitelBCMChipType based on Integer32"""
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
        *(("bcm5324m", 3),
          ("bcm5325e", 2),
          ("bcm5380m", 1),
          ("bcmOther", 4))
    )


_MitelBCMChipType_Type.__name__ = "Integer32"
_MitelBCMChipType_Object = MibTableColumn
mitelBCMChipType = _MitelBCMChipType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 1, 3, 1, 4),
    _MitelBCMChipType_Type()
)
mitelBCMChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBCMChipType.setStatus("current")
_MitelBCMConformance_ObjectIdentity = ObjectIdentity
mitelBCMConformance = _MitelBCMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 2)
)
_MitelBCMCompliances_ObjectIdentity = ObjectIdentity
mitelBCMCompliances = _MitelBCMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 2, 1)
)
_MitelBCMGroups_ObjectIdentity = ObjectIdentity
mitelBCMGroups = _MitelBCMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 2, 2)
)

# Managed Objects groups

mitelBCMPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 2, 2, 1)
)
mitelBCMPortGroup.setObjects(
      *(("MITEL-BCM-MIB", "mitelBCMPortIndex"),
        ("MITEL-BCM-MIB", "mitelBCMPortRxSAChanges"),
        ("MITEL-BCM-MIB", "mitelBCMPortRxLastSA"))
)
if mibBuilder.loadTexts:
    mitelBCMPortGroup.setStatus("current")

mitelBCMChipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 2, 2, 2)
)
mitelBCMChipGroup.setObjects(
      *(("MITEL-BCM-MIB", "mitelBCMChipCount"),
        ("MITEL-BCM-MIB", "mitelBCMChipIndex"),
        ("MITEL-BCM-MIB", "mitelBCMChipBIST"),
        ("MITEL-BCM-MIB", "mitelBCMChipRev"),
        ("MITEL-BCM-MIB", "mitelBCMChipType"))
)
if mibBuilder.loadTexts:
    mitelBCMChipGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mitelBCMSwitchCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1027, 4, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mitelBCMSwitchCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-BCM-MIB",
    **{"mitelBCM": mitelBCM,
       "mitelBCMObjects": mitelBCMObjects,
       "mitelBCMPortTable": mitelBCMPortTable,
       "mitelBCMPortTableEntry": mitelBCMPortTableEntry,
       "mitelBCMPortIndex": mitelBCMPortIndex,
       "mitelBCMPortRxSAChanges": mitelBCMPortRxSAChanges,
       "mitelBCMPortRxLastSA": mitelBCMPortRxLastSA,
       "mitelBCMChipCount": mitelBCMChipCount,
       "mitelBCMChipTable": mitelBCMChipTable,
       "mitelBCMChipTableEntry": mitelBCMChipTableEntry,
       "mitelBCMChipIndex": mitelBCMChipIndex,
       "mitelBCMChipBIST": mitelBCMChipBIST,
       "mitelBCMChipRev": mitelBCMChipRev,
       "mitelBCMChipType": mitelBCMChipType,
       "mitelBCMConformance": mitelBCMConformance,
       "mitelBCMCompliances": mitelBCMCompliances,
       "mitelBCMSwitchCompliance": mitelBCMSwitchCompliance,
       "mitelBCMGroups": mitelBCMGroups,
       "mitelBCMPortGroup": mitelBCMPortGroup,
       "mitelBCMChipGroup": mitelBCMChipGroup}
)
