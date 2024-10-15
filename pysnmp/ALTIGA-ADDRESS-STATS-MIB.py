# SNMP MIB module (ALTIGA-ADDRESS-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-ADDRESS-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:03 2024
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

(alAddressMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alAddressMibModule")

(alAddressGroup,
 alStatsAddress) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alAddressGroup",
    "alStatsAddress")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

altigaAddressStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 24, 2)
)
altigaAddressStatsMibModule.setRevisions(
        ("2005-01-25 00:00",
         "2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IPAddressHeldReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delayReuse", 1),
          ("foundInUse", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AltigaAddressStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaAddressStatsMibConformance = _AltigaAddressStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 24, 2, 1)
)
_AltigaAddressStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaAddressStatsMibCompliances = _AltigaAddressStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 24, 2, 1, 1)
)
_AlAddressStatsGlobal_ObjectIdentity = ObjectIdentity
alAddressStatsGlobal = _AlAddressStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 1)
)
_AlAddressStatsPoolTable_Object = MibTable
alAddressStatsPoolTable = _AlAddressStatsPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2)
)
if mibBuilder.loadTexts:
    alAddressStatsPoolTable.setStatus("current")
_AlAddressStatsPoolEntry_Object = MibTableRow
alAddressStatsPoolEntry = _AlAddressStatsPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1)
)
alAddressStatsPoolEntry.setIndexNames(
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsPoolId"),
)
if mibBuilder.loadTexts:
    alAddressStatsPoolEntry.setStatus("current")


class _AlAddressStatsPoolId_Type(Integer32):
    """Custom type alAddressStatsPoolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsPoolId_Type.__name__ = "Integer32"
_AlAddressStatsPoolId_Object = MibTableColumn
alAddressStatsPoolId = _AlAddressStatsPoolId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1, 1),
    _AlAddressStatsPoolId_Type()
)
alAddressStatsPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsPoolId.setStatus("current")


class _AlAddressStatsTotalPoolAddresses_Type(Integer32):
    """Custom type alAddressStatsTotalPoolAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsTotalPoolAddresses_Type.__name__ = "Integer32"
_AlAddressStatsTotalPoolAddresses_Object = MibTableColumn
alAddressStatsTotalPoolAddresses = _AlAddressStatsTotalPoolAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1, 2),
    _AlAddressStatsTotalPoolAddresses_Type()
)
alAddressStatsTotalPoolAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsTotalPoolAddresses.setStatus("current")
_AlAddressStatsCurrAllocAddresses_Type = Gauge32
_AlAddressStatsCurrAllocAddresses_Object = MibTableColumn
alAddressStatsCurrAllocAddresses = _AlAddressStatsCurrAllocAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1, 3),
    _AlAddressStatsCurrAllocAddresses_Type()
)
alAddressStatsCurrAllocAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsCurrAllocAddresses.setStatus("current")
_AlAddressStatsCurrAvailAddresses_Type = Gauge32
_AlAddressStatsCurrAvailAddresses_Object = MibTableColumn
alAddressStatsCurrAvailAddresses = _AlAddressStatsCurrAvailAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1, 4),
    _AlAddressStatsCurrAvailAddresses_Type()
)
alAddressStatsCurrAvailAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsCurrAvailAddresses.setStatus("current")
_AlAddressStatsMaxAddressesAssigned_Type = Gauge32
_AlAddressStatsMaxAddressesAssigned_Object = MibTableColumn
alAddressStatsMaxAddressesAssigned = _AlAddressStatsMaxAddressesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1, 5),
    _AlAddressStatsMaxAddressesAssigned_Type()
)
alAddressStatsMaxAddressesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsMaxAddressesAssigned.setStatus("current")
_AlAddressStatsHeldAddresses_Type = Gauge32
_AlAddressStatsHeldAddresses_Object = MibTableColumn
alAddressStatsHeldAddresses = _AlAddressStatsHeldAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 2, 1, 6),
    _AlAddressStatsHeldAddresses_Type()
)
alAddressStatsHeldAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsHeldAddresses.setStatus("current")
_AlAddressStatsPoolGroupTable_Object = MibTable
alAddressStatsPoolGroupTable = _AlAddressStatsPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3)
)
if mibBuilder.loadTexts:
    alAddressStatsPoolGroupTable.setStatus("current")
_AlAddressStatsPoolGroupEntry_Object = MibTableRow
alAddressStatsPoolGroupEntry = _AlAddressStatsPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1)
)
alAddressStatsPoolGroupEntry.setIndexNames(
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpId"),
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpPoolId"),
)
if mibBuilder.loadTexts:
    alAddressStatsPoolGroupEntry.setStatus("current")


class _AlAddressStatsGrpId_Type(Integer32):
    """Custom type alAddressStatsGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsGrpId_Type.__name__ = "Integer32"
_AlAddressStatsGrpId_Object = MibTableColumn
alAddressStatsGrpId = _AlAddressStatsGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 1),
    _AlAddressStatsGrpId_Type()
)
alAddressStatsGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpId.setStatus("current")


class _AlAddressStatsGrpPoolId_Type(Integer32):
    """Custom type alAddressStatsGrpPoolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsGrpPoolId_Type.__name__ = "Integer32"
_AlAddressStatsGrpPoolId_Object = MibTableColumn
alAddressStatsGrpPoolId = _AlAddressStatsGrpPoolId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 2),
    _AlAddressStatsGrpPoolId_Type()
)
alAddressStatsGrpPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpPoolId.setStatus("current")


class _AlAddressStatsGrpTotalPoolAddresses_Type(Integer32):
    """Custom type alAddressStatsGrpTotalPoolAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsGrpTotalPoolAddresses_Type.__name__ = "Integer32"
_AlAddressStatsGrpTotalPoolAddresses_Object = MibTableColumn
alAddressStatsGrpTotalPoolAddresses = _AlAddressStatsGrpTotalPoolAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 3),
    _AlAddressStatsGrpTotalPoolAddresses_Type()
)
alAddressStatsGrpTotalPoolAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpTotalPoolAddresses.setStatus("current")
_AlAddressStatsGrpCurrAllocAddresses_Type = Gauge32
_AlAddressStatsGrpCurrAllocAddresses_Object = MibTableColumn
alAddressStatsGrpCurrAllocAddresses = _AlAddressStatsGrpCurrAllocAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 4),
    _AlAddressStatsGrpCurrAllocAddresses_Type()
)
alAddressStatsGrpCurrAllocAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpCurrAllocAddresses.setStatus("current")
_AlAddressStatsGrpCurrAvailAddresses_Type = Gauge32
_AlAddressStatsGrpCurrAvailAddresses_Object = MibTableColumn
alAddressStatsGrpCurrAvailAddresses = _AlAddressStatsGrpCurrAvailAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 5),
    _AlAddressStatsGrpCurrAvailAddresses_Type()
)
alAddressStatsGrpCurrAvailAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpCurrAvailAddresses.setStatus("current")
_AlAddressStatsGrpMaxAddressesAssigned_Type = Gauge32
_AlAddressStatsGrpMaxAddressesAssigned_Object = MibTableColumn
alAddressStatsGrpMaxAddressesAssigned = _AlAddressStatsGrpMaxAddressesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 6),
    _AlAddressStatsGrpMaxAddressesAssigned_Type()
)
alAddressStatsGrpMaxAddressesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpMaxAddressesAssigned.setStatus("current")
_AlAddressStatsGrpHeldAddresses_Type = Gauge32
_AlAddressStatsGrpHeldAddresses_Object = MibTableColumn
alAddressStatsGrpHeldAddresses = _AlAddressStatsGrpHeldAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 3, 1, 7),
    _AlAddressStatsGrpHeldAddresses_Type()
)
alAddressStatsGrpHeldAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldAddresses.setStatus("current")
_AlAddressStatsHeldTable_Object = MibTable
alAddressStatsHeldTable = _AlAddressStatsHeldTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4)
)
if mibBuilder.loadTexts:
    alAddressStatsHeldTable.setStatus("current")
_AlAddressStatsHeldEntry_Object = MibTableRow
alAddressStatsHeldEntry = _AlAddressStatsHeldEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4, 1)
)
alAddressStatsHeldEntry.setIndexNames(
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldPoolId"),
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldAddrIndex"),
)
if mibBuilder.loadTexts:
    alAddressStatsHeldEntry.setStatus("current")


class _AlAddressStatsHeldPoolId_Type(Integer32):
    """Custom type alAddressStatsHeldPoolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsHeldPoolId_Type.__name__ = "Integer32"
_AlAddressStatsHeldPoolId_Object = MibTableColumn
alAddressStatsHeldPoolId = _AlAddressStatsHeldPoolId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4, 1, 1),
    _AlAddressStatsHeldPoolId_Type()
)
alAddressStatsHeldPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsHeldPoolId.setStatus("current")


class _AlAddressStatsHeldAddrIndex_Type(Integer32):
    """Custom type alAddressStatsHeldAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsHeldAddrIndex_Type.__name__ = "Integer32"
_AlAddressStatsHeldAddrIndex_Object = MibTableColumn
alAddressStatsHeldAddrIndex = _AlAddressStatsHeldAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4, 1, 2),
    _AlAddressStatsHeldAddrIndex_Type()
)
alAddressStatsHeldAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsHeldAddrIndex.setStatus("current")
_AlAddressStatsHeldAddress_Type = IpAddress
_AlAddressStatsHeldAddress_Object = MibTableColumn
alAddressStatsHeldAddress = _AlAddressStatsHeldAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4, 1, 3),
    _AlAddressStatsHeldAddress_Type()
)
alAddressStatsHeldAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsHeldAddress.setStatus("current")


class _AlAddressStatsHeldTimeLeft_Type(Integer32):
    """Custom type alAddressStatsHeldTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlAddressStatsHeldTimeLeft_Type.__name__ = "Integer32"
_AlAddressStatsHeldTimeLeft_Object = MibTableColumn
alAddressStatsHeldTimeLeft = _AlAddressStatsHeldTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4, 1, 4),
    _AlAddressStatsHeldTimeLeft_Type()
)
alAddressStatsHeldTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsHeldTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    alAddressStatsHeldTimeLeft.setUnits("seconds")
_AlAddressStatsHeldReason_Type = IPAddressHeldReason
_AlAddressStatsHeldReason_Object = MibTableColumn
alAddressStatsHeldReason = _AlAddressStatsHeldReason_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 4, 1, 5),
    _AlAddressStatsHeldReason_Type()
)
alAddressStatsHeldReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsHeldReason.setStatus("current")
_AlAddressStatsGrpHeldTable_Object = MibTable
alAddressStatsGrpHeldTable = _AlAddressStatsGrpHeldTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5)
)
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldTable.setStatus("current")
_AlAddressStatsGrpHeldEntry_Object = MibTableRow
alAddressStatsGrpHeldEntry = _AlAddressStatsGrpHeldEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1)
)
alAddressStatsGrpHeldEntry.setIndexNames(
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldId"),
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldPoolId"),
    (0, "ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldAddrIndex"),
)
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldEntry.setStatus("current")


class _AlAddressStatsGrpHeldId_Type(Integer32):
    """Custom type alAddressStatsGrpHeldId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsGrpHeldId_Type.__name__ = "Integer32"
_AlAddressStatsGrpHeldId_Object = MibTableColumn
alAddressStatsGrpHeldId = _AlAddressStatsGrpHeldId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1, 1),
    _AlAddressStatsGrpHeldId_Type()
)
alAddressStatsGrpHeldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldId.setStatus("current")


class _AlAddressStatsGrpHeldPoolId_Type(Integer32):
    """Custom type alAddressStatsGrpHeldPoolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsGrpHeldPoolId_Type.__name__ = "Integer32"
_AlAddressStatsGrpHeldPoolId_Object = MibTableColumn
alAddressStatsGrpHeldPoolId = _AlAddressStatsGrpHeldPoolId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1, 2),
    _AlAddressStatsGrpHeldPoolId_Type()
)
alAddressStatsGrpHeldPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldPoolId.setStatus("current")


class _AlAddressStatsGrpHeldAddrIndex_Type(Integer32):
    """Custom type alAddressStatsGrpHeldAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlAddressStatsGrpHeldAddrIndex_Type.__name__ = "Integer32"
_AlAddressStatsGrpHeldAddrIndex_Object = MibTableColumn
alAddressStatsGrpHeldAddrIndex = _AlAddressStatsGrpHeldAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1, 3),
    _AlAddressStatsGrpHeldAddrIndex_Type()
)
alAddressStatsGrpHeldAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldAddrIndex.setStatus("current")
_AlAddressStatsGrpHeldAddress_Type = IpAddress
_AlAddressStatsGrpHeldAddress_Object = MibTableColumn
alAddressStatsGrpHeldAddress = _AlAddressStatsGrpHeldAddress_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1, 4),
    _AlAddressStatsGrpHeldAddress_Type()
)
alAddressStatsGrpHeldAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldAddress.setStatus("current")


class _AlAddressStatsGrpHeldTimeLeft_Type(Integer32):
    """Custom type alAddressStatsGrpHeldTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlAddressStatsGrpHeldTimeLeft_Type.__name__ = "Integer32"
_AlAddressStatsGrpHeldTimeLeft_Object = MibTableColumn
alAddressStatsGrpHeldTimeLeft = _AlAddressStatsGrpHeldTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1, 5),
    _AlAddressStatsGrpHeldTimeLeft_Type()
)
alAddressStatsGrpHeldTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldTimeLeft.setUnits("seconds")
_AlAddressStatsGrpHeldReason_Type = IPAddressHeldReason
_AlAddressStatsGrpHeldReason_Object = MibTableColumn
alAddressStatsGrpHeldReason = _AlAddressStatsGrpHeldReason_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 19, 5, 1, 6),
    _AlAddressStatsGrpHeldReason_Type()
)
alAddressStatsGrpHeldReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAddressStatsGrpHeldReason.setStatus("current")

# Managed Objects groups

altigaAddressStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 19, 2)
)
altigaAddressStatsGroup.setObjects(
      *(("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsPoolId"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsTotalPoolAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsCurrAllocAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsCurrAvailAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsMaxAddressesAssigned"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpId"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpPoolId"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpTotalPoolAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpCurrAllocAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpCurrAvailAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpMaxAddressesAssigned"))
)
if mibBuilder.loadTexts:
    altigaAddressStatsGroup.setStatus("current")

altigaAddressStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 19, 3)
)
altigaAddressStatsGroupSup1.setObjects(
      *(("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldAddresses"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldPoolId"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldAddrIndex"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldAddress"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldTimeLeft"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsHeldReason"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldId"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldPoolId"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldAddrIndex"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldAddress"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldTimeLeft"),
        ("ALTIGA-ADDRESS-STATS-MIB", "alAddressStatsGrpHeldReason"))
)
if mibBuilder.loadTexts:
    altigaAddressStatsGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaAddressStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 24, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaAddressStatsMibCompliance.setStatus(
        "deprecated"
    )

altigaAddressStatsMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 24, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    altigaAddressStatsMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-ADDRESS-STATS-MIB",
    **{"IPAddressHeldReason": IPAddressHeldReason,
       "altigaAddressStatsMibModule": altigaAddressStatsMibModule,
       "altigaAddressStatsMibConformance": altigaAddressStatsMibConformance,
       "altigaAddressStatsMibCompliances": altigaAddressStatsMibCompliances,
       "altigaAddressStatsMibCompliance": altigaAddressStatsMibCompliance,
       "altigaAddressStatsMibComplianceRev1": altigaAddressStatsMibComplianceRev1,
       "altigaAddressStatsGroup": altigaAddressStatsGroup,
       "altigaAddressStatsGroupSup1": altigaAddressStatsGroupSup1,
       "alAddressStatsGlobal": alAddressStatsGlobal,
       "alAddressStatsPoolTable": alAddressStatsPoolTable,
       "alAddressStatsPoolEntry": alAddressStatsPoolEntry,
       "alAddressStatsPoolId": alAddressStatsPoolId,
       "alAddressStatsTotalPoolAddresses": alAddressStatsTotalPoolAddresses,
       "alAddressStatsCurrAllocAddresses": alAddressStatsCurrAllocAddresses,
       "alAddressStatsCurrAvailAddresses": alAddressStatsCurrAvailAddresses,
       "alAddressStatsMaxAddressesAssigned": alAddressStatsMaxAddressesAssigned,
       "alAddressStatsHeldAddresses": alAddressStatsHeldAddresses,
       "alAddressStatsPoolGroupTable": alAddressStatsPoolGroupTable,
       "alAddressStatsPoolGroupEntry": alAddressStatsPoolGroupEntry,
       "alAddressStatsGrpId": alAddressStatsGrpId,
       "alAddressStatsGrpPoolId": alAddressStatsGrpPoolId,
       "alAddressStatsGrpTotalPoolAddresses": alAddressStatsGrpTotalPoolAddresses,
       "alAddressStatsGrpCurrAllocAddresses": alAddressStatsGrpCurrAllocAddresses,
       "alAddressStatsGrpCurrAvailAddresses": alAddressStatsGrpCurrAvailAddresses,
       "alAddressStatsGrpMaxAddressesAssigned": alAddressStatsGrpMaxAddressesAssigned,
       "alAddressStatsGrpHeldAddresses": alAddressStatsGrpHeldAddresses,
       "alAddressStatsHeldTable": alAddressStatsHeldTable,
       "alAddressStatsHeldEntry": alAddressStatsHeldEntry,
       "alAddressStatsHeldPoolId": alAddressStatsHeldPoolId,
       "alAddressStatsHeldAddrIndex": alAddressStatsHeldAddrIndex,
       "alAddressStatsHeldAddress": alAddressStatsHeldAddress,
       "alAddressStatsHeldTimeLeft": alAddressStatsHeldTimeLeft,
       "alAddressStatsHeldReason": alAddressStatsHeldReason,
       "alAddressStatsGrpHeldTable": alAddressStatsGrpHeldTable,
       "alAddressStatsGrpHeldEntry": alAddressStatsGrpHeldEntry,
       "alAddressStatsGrpHeldId": alAddressStatsGrpHeldId,
       "alAddressStatsGrpHeldPoolId": alAddressStatsGrpHeldPoolId,
       "alAddressStatsGrpHeldAddrIndex": alAddressStatsGrpHeldAddrIndex,
       "alAddressStatsGrpHeldAddress": alAddressStatsGrpHeldAddress,
       "alAddressStatsGrpHeldTimeLeft": alAddressStatsGrpHeldTimeLeft,
       "alAddressStatsGrpHeldReason": alAddressStatsGrpHeldReason}
)
