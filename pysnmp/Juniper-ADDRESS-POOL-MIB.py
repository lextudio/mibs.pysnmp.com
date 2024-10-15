# SNMP MIB module (Juniper-ADDRESS-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ADDRESS-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:38 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(juniRouterName,) = mibBuilder.importSymbols(
    "Juniper-ROUTER-MIB",
    "juniRouterName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniAddressPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21)
)
juniAddressPoolMIB.setRevisions(
        ("2005-02-11 21:35",
         "2004-09-17 22:37",
         "2003-11-03 22:37",
         "2002-09-16 21:44",
         "2002-05-06 18:38",
         "2001-05-02 11:57",
         "2001-04-27 15:00",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniAddressPoolObjects_ObjectIdentity = ObjectIdentity
juniAddressPoolObjects = _JuniAddressPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1)
)
_JuniAddressPool_ObjectIdentity = ObjectIdentity
juniAddressPool = _JuniAddressPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1)
)
_JuniAddressPoolTable_Object = MibTable
juniAddressPoolTable = _JuniAddressPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniAddressPoolTable.setStatus("current")
_JuniAddressPoolEntry_Object = MibTableRow
juniAddressPoolEntry = _JuniAddressPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1)
)
juniAddressPoolEntry.setIndexNames(
    (0, "Juniper-ADDRESS-POOL-MIB", "juniAddressPoolIndex"),
)
if mibBuilder.loadTexts:
    juniAddressPoolEntry.setStatus("current")


class _JuniAddressPoolIndex_Type(Integer32):
    """Custom type juniAddressPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniAddressPoolIndex_Type.__name__ = "Integer32"
_JuniAddressPoolIndex_Object = MibTableColumn
juniAddressPoolIndex = _JuniAddressPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 1),
    _JuniAddressPoolIndex_Type()
)
juniAddressPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAddressPoolIndex.setStatus("current")
_JuniAddressPoolRowStatus_Type = RowStatus
_JuniAddressPoolRowStatus_Object = MibTableColumn
juniAddressPoolRowStatus = _JuniAddressPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 2),
    _JuniAddressPoolRowStatus_Type()
)
juniAddressPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolRowStatus.setStatus("current")


class _JuniAddressPoolName_Type(OctetString):
    """Custom type juniAddressPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_JuniAddressPoolName_Type.__name__ = "OctetString"
_JuniAddressPoolName_Object = MibTableColumn
juniAddressPoolName = _JuniAddressPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 3),
    _JuniAddressPoolName_Type()
)
juniAddressPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolName.setStatus("current")


class _JuniAddressPoolStart_Type(IpAddress):
    """Custom type juniAddressPoolStart based on IpAddress"""
    defaultValue = 0


_JuniAddressPoolStart_Object = MibTableColumn
juniAddressPoolStart = _JuniAddressPoolStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 4),
    _JuniAddressPoolStart_Type()
)
juniAddressPoolStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolStart.setStatus("deprecated")


class _JuniAddressPoolEnd_Type(IpAddress):
    """Custom type juniAddressPoolEnd based on IpAddress"""
    defaultValue = 0


_JuniAddressPoolEnd_Object = MibTableColumn
juniAddressPoolEnd = _JuniAddressPoolEnd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 5),
    _JuniAddressPoolEnd_Type()
)
juniAddressPoolEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolEnd.setStatus("deprecated")
_JuniAddressPoolSize_Type = Integer32
_JuniAddressPoolSize_Object = MibTableColumn
juniAddressPoolSize = _JuniAddressPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 6),
    _JuniAddressPoolSize_Type()
)
juniAddressPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolSize.setStatus("deprecated")
_JuniAddressPoolInUse_Type = Integer32
_JuniAddressPoolInUse_Object = MibTableColumn
juniAddressPoolInUse = _JuniAddressPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 7),
    _JuniAddressPoolInUse_Type()
)
juniAddressPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolInUse.setStatus("deprecated")


class _JuniAddressPoolHighUtilThreshold_Type(Integer32):
    """Custom type juniAddressPoolHighUtilThreshold based on Integer32"""
    defaultValue = 85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniAddressPoolHighUtilThreshold_Type.__name__ = "Integer32"
_JuniAddressPoolHighUtilThreshold_Object = MibTableColumn
juniAddressPoolHighUtilThreshold = _JuniAddressPoolHighUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 8),
    _JuniAddressPoolHighUtilThreshold_Type()
)
juniAddressPoolHighUtilThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolHighUtilThreshold.setStatus("current")


class _JuniAddressPoolAbatedUtilThreshold_Type(Integer32):
    """Custom type juniAddressPoolAbatedUtilThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniAddressPoolAbatedUtilThreshold_Type.__name__ = "Integer32"
_JuniAddressPoolAbatedUtilThreshold_Object = MibTableColumn
juniAddressPoolAbatedUtilThreshold = _JuniAddressPoolAbatedUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 9),
    _JuniAddressPoolAbatedUtilThreshold_Type()
)
juniAddressPoolAbatedUtilThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolAbatedUtilThreshold.setStatus("current")


class _JuniAddressPoolUtilPct_Type(Integer32):
    """Custom type juniAddressPoolUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniAddressPoolUtilPct_Type.__name__ = "Integer32"
_JuniAddressPoolUtilPct_Object = MibTableColumn
juniAddressPoolUtilPct = _JuniAddressPoolUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 10),
    _JuniAddressPoolUtilPct_Type()
)
juniAddressPoolUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolUtilPct.setStatus("current")


class _JuniAddressPoolTrapEnable_Type(TruthValue):
    """Custom type juniAddressPoolTrapEnable based on TruthValue"""


_JuniAddressPoolTrapEnable_Object = MibTableColumn
juniAddressPoolTrapEnable = _JuniAddressPoolTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 11),
    _JuniAddressPoolTrapEnable_Type()
)
juniAddressPoolTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolTrapEnable.setStatus("current")


class _JuniAddressPoolNextPoolProfileIndex_Type(Integer32):
    """Custom type juniAddressPoolNextPoolProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAddressPoolNextPoolProfileIndex_Type.__name__ = "Integer32"
_JuniAddressPoolNextPoolProfileIndex_Object = MibTableColumn
juniAddressPoolNextPoolProfileIndex = _JuniAddressPoolNextPoolProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 1, 1, 12),
    _JuniAddressPoolNextPoolProfileIndex_Type()
)
juniAddressPoolNextPoolProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolNextPoolProfileIndex.setStatus("current")


class _JuniAddressPoolNextPoolIndex_Type(Integer32):
    """Custom type juniAddressPoolNextPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAddressPoolNextPoolIndex_Type.__name__ = "Integer32"
_JuniAddressPoolNextPoolIndex_Object = MibScalar
juniAddressPoolNextPoolIndex = _JuniAddressPoolNextPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 2),
    _JuniAddressPoolNextPoolIndex_Type()
)
juniAddressPoolNextPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolNextPoolIndex.setStatus("current")
_JuniAddressPoolProfileTable_Object = MibTable
juniAddressPoolProfileTable = _JuniAddressPoolProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniAddressPoolProfileTable.setStatus("current")
_JuniAddressPoolProfileEntry_Object = MibTableRow
juniAddressPoolProfileEntry = _JuniAddressPoolProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1)
)
juniAddressPoolProfileEntry.setIndexNames(
    (0, "Juniper-ADDRESS-POOL-MIB", "juniAddressPoolIndex"),
    (0, "Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileIndex"),
)
if mibBuilder.loadTexts:
    juniAddressPoolProfileEntry.setStatus("current")


class _JuniAddressPoolProfileIndex_Type(Integer32):
    """Custom type juniAddressPoolProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniAddressPoolProfileIndex_Type.__name__ = "Integer32"
_JuniAddressPoolProfileIndex_Object = MibTableColumn
juniAddressPoolProfileIndex = _JuniAddressPoolProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 1),
    _JuniAddressPoolProfileIndex_Type()
)
juniAddressPoolProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAddressPoolProfileIndex.setStatus("current")
_JuniAddressPoolProfileRowStatus_Type = RowStatus
_JuniAddressPoolProfileRowStatus_Object = MibTableColumn
juniAddressPoolProfileRowStatus = _JuniAddressPoolProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 2),
    _JuniAddressPoolProfileRowStatus_Type()
)
juniAddressPoolProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolProfileRowStatus.setStatus("current")
_JuniAddressPoolProfileStart_Type = IpAddress
_JuniAddressPoolProfileStart_Object = MibTableColumn
juniAddressPoolProfileStart = _JuniAddressPoolProfileStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 3),
    _JuniAddressPoolProfileStart_Type()
)
juniAddressPoolProfileStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolProfileStart.setStatus("current")
_JuniAddressPoolProfileEnd_Type = IpAddress
_JuniAddressPoolProfileEnd_Object = MibTableColumn
juniAddressPoolProfileEnd = _JuniAddressPoolProfileEnd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 4),
    _JuniAddressPoolProfileEnd_Type()
)
juniAddressPoolProfileEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressPoolProfileEnd.setStatus("current")
_JuniAddressPoolProfileSize_Type = Integer32
_JuniAddressPoolProfileSize_Object = MibTableColumn
juniAddressPoolProfileSize = _JuniAddressPoolProfileSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 5),
    _JuniAddressPoolProfileSize_Type()
)
juniAddressPoolProfileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolProfileSize.setStatus("current")
_JuniAddressPoolProfileInUse_Type = Integer32
_JuniAddressPoolProfileInUse_Object = MibTableColumn
juniAddressPoolProfileInUse = _JuniAddressPoolProfileInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 3, 1, 6),
    _JuniAddressPoolProfileInUse_Type()
)
juniAddressPoolProfileInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressPoolProfileInUse.setStatus("current")
_JuniAddressAliasTable_Object = MibTable
juniAddressAliasTable = _JuniAddressAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniAddressAliasTable.setStatus("current")
_JuniAddressAliasEntry_Object = MibTableRow
juniAddressAliasEntry = _JuniAddressAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 4, 1)
)
juniAddressAliasEntry.setIndexNames(
    (1, "Juniper-ADDRESS-POOL-MIB", "juniAddressAliasName"),
)
if mibBuilder.loadTexts:
    juniAddressAliasEntry.setStatus("current")


class _JuniAddressAliasName_Type(DisplayString):
    """Custom type juniAddressAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_JuniAddressAliasName_Type.__name__ = "DisplayString"
_JuniAddressAliasName_Object = MibTableColumn
juniAddressAliasName = _JuniAddressAliasName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 4, 1, 1),
    _JuniAddressAliasName_Type()
)
juniAddressAliasName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAddressAliasName.setStatus("current")
_JuniAddressAliasRowStatus_Type = RowStatus
_JuniAddressAliasRowStatus_Object = MibTableColumn
juniAddressAliasRowStatus = _JuniAddressAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 4, 1, 2),
    _JuniAddressAliasRowStatus_Type()
)
juniAddressAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressAliasRowStatus.setStatus("current")


class _JuniAddressAliasPoolName_Type(DisplayString):
    """Custom type juniAddressAliasPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_JuniAddressAliasPoolName_Type.__name__ = "DisplayString"
_JuniAddressAliasPoolName_Object = MibTableColumn
juniAddressAliasPoolName = _JuniAddressAliasPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 4, 1, 3),
    _JuniAddressAliasPoolName_Type()
)
juniAddressAliasPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressAliasPoolName.setStatus("current")
_JuniAddressSharedPoolTable_Object = MibTable
juniAddressSharedPoolTable = _JuniAddressSharedPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5)
)
if mibBuilder.loadTexts:
    juniAddressSharedPoolTable.setStatus("current")
_JuniAddressSharedPoolEntry_Object = MibTableRow
juniAddressSharedPoolEntry = _JuniAddressSharedPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5, 1)
)
juniAddressSharedPoolEntry.setIndexNames(
    (0, "Juniper-ADDRESS-POOL-MIB", "juniAddressSharedPoolIndex"),
)
if mibBuilder.loadTexts:
    juniAddressSharedPoolEntry.setStatus("current")


class _JuniAddressSharedPoolIndex_Type(Integer32):
    """Custom type juniAddressSharedPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniAddressSharedPoolIndex_Type.__name__ = "Integer32"
_JuniAddressSharedPoolIndex_Object = MibTableColumn
juniAddressSharedPoolIndex = _JuniAddressSharedPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5, 1, 1),
    _JuniAddressSharedPoolIndex_Type()
)
juniAddressSharedPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAddressSharedPoolIndex.setStatus("current")
_JuniAddressSharedPoolRowStatus_Type = RowStatus
_JuniAddressSharedPoolRowStatus_Object = MibTableColumn
juniAddressSharedPoolRowStatus = _JuniAddressSharedPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5, 1, 2),
    _JuniAddressSharedPoolRowStatus_Type()
)
juniAddressSharedPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressSharedPoolRowStatus.setStatus("current")


class _JuniAddressSharedPoolName_Type(OctetString):
    """Custom type juniAddressSharedPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_JuniAddressSharedPoolName_Type.__name__ = "OctetString"
_JuniAddressSharedPoolName_Object = MibTableColumn
juniAddressSharedPoolName = _JuniAddressSharedPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5, 1, 3),
    _JuniAddressSharedPoolName_Type()
)
juniAddressSharedPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressSharedPoolName.setStatus("current")


class _JuniAddressSharedPoolDhcpPoolName_Type(OctetString):
    """Custom type juniAddressSharedPoolDhcpPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JuniAddressSharedPoolDhcpPoolName_Type.__name__ = "OctetString"
_JuniAddressSharedPoolDhcpPoolName_Object = MibTableColumn
juniAddressSharedPoolDhcpPoolName = _JuniAddressSharedPoolDhcpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5, 1, 4),
    _JuniAddressSharedPoolDhcpPoolName_Type()
)
juniAddressSharedPoolDhcpPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAddressSharedPoolDhcpPoolName.setStatus("current")
_JuniAddressSharedPoolInUse_Type = Integer32
_JuniAddressSharedPoolInUse_Object = MibTableColumn
juniAddressSharedPoolInUse = _JuniAddressSharedPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 1, 1, 5, 1, 5),
    _JuniAddressSharedPoolInUse_Type()
)
juniAddressSharedPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAddressSharedPoolInUse.setStatus("current")
_JuniAddressPoolTraps_ObjectIdentity = ObjectIdentity
juniAddressPoolTraps = _JuniAddressPoolTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3)
)
_JuniAddressPoolTrapPrefix_ObjectIdentity = ObjectIdentity
juniAddressPoolTrapPrefix = _JuniAddressPoolTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0)
)
_JuniAddressPoolMIBConformance_ObjectIdentity = ObjectIdentity
juniAddressPoolMIBConformance = _JuniAddressPoolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4)
)
_JuniAddressPoolMIBCompliances_ObjectIdentity = ObjectIdentity
juniAddressPoolMIBCompliances = _JuniAddressPoolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1)
)
_JuniAddressPoolMIBGroups_ObjectIdentity = ObjectIdentity
juniAddressPoolMIBGroups = _JuniAddressPoolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2)
)

# Managed Objects groups

juniAddressPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 1)
)
juniAddressPoolGroup.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolStart"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolEnd"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolInUse"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolIndex"))
)
if mibBuilder.loadTexts:
    juniAddressPoolGroup.setStatus("obsolete")

juniAddressPoolGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 2)
)
juniAddressPoolGroup2.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolStart"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolEnd"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolInUse"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolIndex"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolHighUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolAbatedUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolUtilPct"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolTrapEnable"))
)
if mibBuilder.loadTexts:
    juniAddressPoolGroup2.setStatus("obsolete")

juniAddressPoolGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 4)
)
juniAddressPoolGroup3.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolIndex"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolHighUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolAbatedUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolUtilPct"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolTrapEnable"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileStart"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileEnd"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileInUse"))
)
if mibBuilder.loadTexts:
    juniAddressPoolGroup3.setStatus("current")

juniAddressPoolDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 5)
)
juniAddressPoolDeprecatedGroup.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolStart"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolEnd"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolInUse"))
)
if mibBuilder.loadTexts:
    juniAddressPoolDeprecatedGroup.setStatus("deprecated")

juniAddressAliasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 6)
)
juniAddressAliasGroup.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressAliasRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressAliasPoolName"))
)
if mibBuilder.loadTexts:
    juniAddressAliasGroup.setStatus("current")

juniAddressPoolGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 7)
)
juniAddressPoolGroup4.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolIndex"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolHighUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolAbatedUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolUtilPct"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolTrapEnable"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileStart"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileEnd"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileInUse"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolProfileIndex"))
)
if mibBuilder.loadTexts:
    juniAddressPoolGroup4.setStatus("obsolete")

juniAddressPoolGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 8)
)
juniAddressPoolGroup5.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolIndex"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolHighUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolAbatedUtilThreshold"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolUtilPct"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolTrapEnable"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileStart"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileEnd"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolProfileInUse"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNextPoolProfileIndex"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressSharedPoolRowStatus"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressSharedPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressSharedPoolDhcpPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressSharedPoolInUse"))
)
if mibBuilder.loadTexts:
    juniAddressPoolGroup5.setStatus("current")


# Notification objects

juniAddressPoolHighAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0, 1)
)
juniAddressPoolHighAddrUtil.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolInUse"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolUtilPct"))
)
if mibBuilder.loadTexts:
    juniAddressPoolHighAddrUtil.setStatus(
        "current"
    )

juniAddressPoolAbatedAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0, 2)
)
juniAddressPoolAbatedAddrUtil.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolSize"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolInUse"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolUtilPct"))
)
if mibBuilder.loadTexts:
    juniAddressPoolAbatedAddrUtil.setStatus(
        "current"
    )

juniAddressPoolNoAddresses = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 3, 0, 3)
)
juniAddressPoolNoAddresses.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolName"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolSize"))
)
if mibBuilder.loadTexts:
    juniAddressPoolNoAddresses.setStatus(
        "current"
    )


# Notifications groups

juniAddressPoolTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 2, 3)
)
juniAddressPoolTrapGroup.setObjects(
      *(("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolHighAddrUtil"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolAbatedAddrUtil"),
        ("Juniper-ADDRESS-POOL-MIB", "juniAddressPoolNoAddresses"))
)
if mibBuilder.loadTexts:
    juniAddressPoolTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniAddressPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniAddressPoolCompliance.setStatus(
        "obsolete"
    )

juniAddressPoolCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniAddressPoolCompliance2.setStatus(
        "obsolete"
    )

juniAddressPoolCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniAddressPoolCompliance3.setStatus(
        "obsolete"
    )

juniAddressPoolCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniAddressPoolCompliance4.setStatus(
        "obsolete"
    )

juniAddressPoolCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniAddressPoolCompliance5.setStatus(
        "obsolete"
    )

juniAddressPoolCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniAddressPoolCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ADDRESS-POOL-MIB",
    **{"juniAddressPoolMIB": juniAddressPoolMIB,
       "juniAddressPoolObjects": juniAddressPoolObjects,
       "juniAddressPool": juniAddressPool,
       "juniAddressPoolTable": juniAddressPoolTable,
       "juniAddressPoolEntry": juniAddressPoolEntry,
       "juniAddressPoolIndex": juniAddressPoolIndex,
       "juniAddressPoolRowStatus": juniAddressPoolRowStatus,
       "juniAddressPoolName": juniAddressPoolName,
       "juniAddressPoolStart": juniAddressPoolStart,
       "juniAddressPoolEnd": juniAddressPoolEnd,
       "juniAddressPoolSize": juniAddressPoolSize,
       "juniAddressPoolInUse": juniAddressPoolInUse,
       "juniAddressPoolHighUtilThreshold": juniAddressPoolHighUtilThreshold,
       "juniAddressPoolAbatedUtilThreshold": juniAddressPoolAbatedUtilThreshold,
       "juniAddressPoolUtilPct": juniAddressPoolUtilPct,
       "juniAddressPoolTrapEnable": juniAddressPoolTrapEnable,
       "juniAddressPoolNextPoolProfileIndex": juniAddressPoolNextPoolProfileIndex,
       "juniAddressPoolNextPoolIndex": juniAddressPoolNextPoolIndex,
       "juniAddressPoolProfileTable": juniAddressPoolProfileTable,
       "juniAddressPoolProfileEntry": juniAddressPoolProfileEntry,
       "juniAddressPoolProfileIndex": juniAddressPoolProfileIndex,
       "juniAddressPoolProfileRowStatus": juniAddressPoolProfileRowStatus,
       "juniAddressPoolProfileStart": juniAddressPoolProfileStart,
       "juniAddressPoolProfileEnd": juniAddressPoolProfileEnd,
       "juniAddressPoolProfileSize": juniAddressPoolProfileSize,
       "juniAddressPoolProfileInUse": juniAddressPoolProfileInUse,
       "juniAddressAliasTable": juniAddressAliasTable,
       "juniAddressAliasEntry": juniAddressAliasEntry,
       "juniAddressAliasName": juniAddressAliasName,
       "juniAddressAliasRowStatus": juniAddressAliasRowStatus,
       "juniAddressAliasPoolName": juniAddressAliasPoolName,
       "juniAddressSharedPoolTable": juniAddressSharedPoolTable,
       "juniAddressSharedPoolEntry": juniAddressSharedPoolEntry,
       "juniAddressSharedPoolIndex": juniAddressSharedPoolIndex,
       "juniAddressSharedPoolRowStatus": juniAddressSharedPoolRowStatus,
       "juniAddressSharedPoolName": juniAddressSharedPoolName,
       "juniAddressSharedPoolDhcpPoolName": juniAddressSharedPoolDhcpPoolName,
       "juniAddressSharedPoolInUse": juniAddressSharedPoolInUse,
       "juniAddressPoolTraps": juniAddressPoolTraps,
       "juniAddressPoolTrapPrefix": juniAddressPoolTrapPrefix,
       "juniAddressPoolHighAddrUtil": juniAddressPoolHighAddrUtil,
       "juniAddressPoolAbatedAddrUtil": juniAddressPoolAbatedAddrUtil,
       "juniAddressPoolNoAddresses": juniAddressPoolNoAddresses,
       "juniAddressPoolMIBConformance": juniAddressPoolMIBConformance,
       "juniAddressPoolMIBCompliances": juniAddressPoolMIBCompliances,
       "juniAddressPoolCompliance": juniAddressPoolCompliance,
       "juniAddressPoolCompliance2": juniAddressPoolCompliance2,
       "juniAddressPoolCompliance3": juniAddressPoolCompliance3,
       "juniAddressPoolCompliance4": juniAddressPoolCompliance4,
       "juniAddressPoolCompliance5": juniAddressPoolCompliance5,
       "juniAddressPoolCompliance6": juniAddressPoolCompliance6,
       "juniAddressPoolMIBGroups": juniAddressPoolMIBGroups,
       "juniAddressPoolGroup": juniAddressPoolGroup,
       "juniAddressPoolGroup2": juniAddressPoolGroup2,
       "juniAddressPoolTrapGroup": juniAddressPoolTrapGroup,
       "juniAddressPoolGroup3": juniAddressPoolGroup3,
       "juniAddressPoolDeprecatedGroup": juniAddressPoolDeprecatedGroup,
       "juniAddressAliasGroup": juniAddressAliasGroup,
       "juniAddressPoolGroup4": juniAddressPoolGroup4,
       "juniAddressPoolGroup5": juniAddressPoolGroup5}
)
