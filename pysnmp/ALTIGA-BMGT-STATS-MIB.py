# SNMP MIB module (ALTIGA-BMGT-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-BMGT-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:04 2024
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

(alBwMgmtMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alBwMgmtMibModule")

(alBwMgmtGroup,
 alStatsBwMgmt) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alBwMgmtGroup",
    "alStatsBwMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

altigaBwMgmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 52, 2)
)
altigaBwMgmMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaBwMgmMibConformance_ObjectIdentity = ObjectIdentity
altigaBwMgmMibConformance = _AltigaBwMgmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 52, 2, 1)
)
_AltigaBwMgmMibCompliances_ObjectIdentity = ObjectIdentity
altigaBwMgmMibCompliances = _AltigaBwMgmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 52, 2, 1, 1)
)
_AlBwMgmtStatsGlobal_ObjectIdentity = ObjectIdentity
alBwMgmtStatsGlobal = _AlBwMgmtStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 1)
)
_AlBwMgmtStatTable_Object = MibTable
alBwMgmtStatTable = _AlBwMgmtStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2)
)
if mibBuilder.loadTexts:
    alBwMgmtStatTable.setStatus("current")
_AlBwMgmtStatEntry_Object = MibTableRow
alBwMgmtStatEntry = _AlBwMgmtStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1)
)
alBwMgmtStatEntry.setIndexNames(
    (0, "ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatIntfId"),
)
if mibBuilder.loadTexts:
    alBwMgmtStatEntry.setStatus("current")
_AlBwMgmtStatRowStatus_Type = RowStatus
_AlBwMgmtStatRowStatus_Object = MibTableColumn
alBwMgmtStatRowStatus = _AlBwMgmtStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 1),
    _AlBwMgmtStatRowStatus_Type()
)
alBwMgmtStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatRowStatus.setStatus("current")


class _AlBwMgmtStatIntfId_Type(Integer32):
    """Custom type alBwMgmtStatIntfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AlBwMgmtStatIntfId_Type.__name__ = "Integer32"
_AlBwMgmtStatIntfId_Object = MibTableColumn
alBwMgmtStatIntfId = _AlBwMgmtStatIntfId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 2),
    _AlBwMgmtStatIntfId_Type()
)
alBwMgmtStatIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatIntfId.setStatus("current")


class _AlBwMgmtStatGrpId_Type(Integer32):
    """Custom type alBwMgmtStatGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AlBwMgmtStatGrpId_Type.__name__ = "Integer32"
_AlBwMgmtStatGrpId_Object = MibTableColumn
alBwMgmtStatGrpId = _AlBwMgmtStatGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 3),
    _AlBwMgmtStatGrpId_Type()
)
alBwMgmtStatGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatGrpId.setStatus("current")
_AlBwMgmtStatInConformedRate_Type = Unsigned32
_AlBwMgmtStatInConformedRate_Object = MibTableColumn
alBwMgmtStatInConformedRate = _AlBwMgmtStatInConformedRate_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 4),
    _AlBwMgmtStatInConformedRate_Type()
)
alBwMgmtStatInConformedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatInConformedRate.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatInConformedRate.setUnits("kbytes")
_AlBwMgmtStatInDroppedRate_Type = Unsigned32
_AlBwMgmtStatInDroppedRate_Object = MibTableColumn
alBwMgmtStatInDroppedRate = _AlBwMgmtStatInDroppedRate_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 5),
    _AlBwMgmtStatInDroppedRate_Type()
)
alBwMgmtStatInDroppedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatInDroppedRate.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatInDroppedRate.setUnits("kbytes")
_AlBwMgmtStatInConformedBytes_Type = Counter32
_AlBwMgmtStatInConformedBytes_Object = MibTableColumn
alBwMgmtStatInConformedBytes = _AlBwMgmtStatInConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 6),
    _AlBwMgmtStatInConformedBytes_Type()
)
alBwMgmtStatInConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatInConformedBytes.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatInConformedBytes.setUnits("bytes")
_AlBwMgmtStatInDroppedBytes_Type = Counter32
_AlBwMgmtStatInDroppedBytes_Object = MibTableColumn
alBwMgmtStatInDroppedBytes = _AlBwMgmtStatInDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 7),
    _AlBwMgmtStatInDroppedBytes_Type()
)
alBwMgmtStatInDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatInDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatInDroppedBytes.setUnits("bytes")
_AlBwMgmtStatOutConformedRate_Type = Unsigned32
_AlBwMgmtStatOutConformedRate_Object = MibTableColumn
alBwMgmtStatOutConformedRate = _AlBwMgmtStatOutConformedRate_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 8),
    _AlBwMgmtStatOutConformedRate_Type()
)
alBwMgmtStatOutConformedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatOutConformedRate.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatOutConformedRate.setUnits("kbytes")
_AlBwMgmtStatOutDroppedRate_Type = Unsigned32
_AlBwMgmtStatOutDroppedRate_Object = MibTableColumn
alBwMgmtStatOutDroppedRate = _AlBwMgmtStatOutDroppedRate_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 9),
    _AlBwMgmtStatOutDroppedRate_Type()
)
alBwMgmtStatOutDroppedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatOutDroppedRate.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatOutDroppedRate.setUnits("kbytes")
_AlBwMgmtStatOutConformedBytes_Type = Counter32
_AlBwMgmtStatOutConformedBytes_Object = MibTableColumn
alBwMgmtStatOutConformedBytes = _AlBwMgmtStatOutConformedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 10),
    _AlBwMgmtStatOutConformedBytes_Type()
)
alBwMgmtStatOutConformedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatOutConformedBytes.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatOutConformedBytes.setUnits("bytes")
_AlBwMgmtStatOutDroppedBytes_Type = Counter32
_AlBwMgmtStatOutDroppedBytes_Object = MibTableColumn
alBwMgmtStatOutDroppedBytes = _AlBwMgmtStatOutDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 47, 2, 1, 11),
    _AlBwMgmtStatOutDroppedBytes_Type()
)
alBwMgmtStatOutDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alBwMgmtStatOutDroppedBytes.setStatus("current")
if mibBuilder.loadTexts:
    alBwMgmtStatOutDroppedBytes.setUnits("bytes")

# Managed Objects groups

alBwMgmtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 47, 2)
)
alBwMgmtStatsGroup.setObjects(
      *(("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatRowStatus"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatIntfId"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatGrpId"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatInConformedRate"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatInDroppedRate"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatInConformedBytes"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatInDroppedBytes"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatOutConformedRate"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatOutDroppedRate"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatOutConformedBytes"),
        ("ALTIGA-BMGT-STATS-MIB", "alBwMgmtStatOutDroppedBytes"))
)
if mibBuilder.loadTexts:
    alBwMgmtStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaBwMgmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 52, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaBwMgmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-BMGT-STATS-MIB",
    **{"altigaBwMgmMibModule": altigaBwMgmMibModule,
       "altigaBwMgmMibConformance": altigaBwMgmMibConformance,
       "altigaBwMgmMibCompliances": altigaBwMgmMibCompliances,
       "altigaBwMgmMibCompliance": altigaBwMgmMibCompliance,
       "alBwMgmtStatsGroup": alBwMgmtStatsGroup,
       "alBwMgmtStatsGlobal": alBwMgmtStatsGlobal,
       "alBwMgmtStatTable": alBwMgmtStatTable,
       "alBwMgmtStatEntry": alBwMgmtStatEntry,
       "alBwMgmtStatRowStatus": alBwMgmtStatRowStatus,
       "alBwMgmtStatIntfId": alBwMgmtStatIntfId,
       "alBwMgmtStatGrpId": alBwMgmtStatGrpId,
       "alBwMgmtStatInConformedRate": alBwMgmtStatInConformedRate,
       "alBwMgmtStatInDroppedRate": alBwMgmtStatInDroppedRate,
       "alBwMgmtStatInConformedBytes": alBwMgmtStatInConformedBytes,
       "alBwMgmtStatInDroppedBytes": alBwMgmtStatInDroppedBytes,
       "alBwMgmtStatOutConformedRate": alBwMgmtStatOutConformedRate,
       "alBwMgmtStatOutDroppedRate": alBwMgmtStatOutDroppedRate,
       "alBwMgmtStatOutConformedBytes": alBwMgmtStatOutConformedBytes,
       "alBwMgmtStatOutDroppedBytes": alBwMgmtStatOutDroppedBytes}
)
