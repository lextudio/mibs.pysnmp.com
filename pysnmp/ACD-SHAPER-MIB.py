# SNMP MIB module (ACD-SHAPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-SHAPER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:24 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

acdShaper = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10)
)
acdShaper.setRevisions(
        ("2009-11-01 01:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdShaper1_ObjectIdentity = ObjectIdentity
acdShaper1 = _AcdShaper1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1)
)
_AcdShaper1MIBObjects_ObjectIdentity = ObjectIdentity
acdShaper1MIBObjects = _AcdShaper1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1)
)
_AcdShaper1Config_ObjectIdentity = ObjectIdentity
acdShaper1Config = _AcdShaper1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 1)
)
_AcdShaper1Stats_ObjectIdentity = ObjectIdentity
acdShaper1Stats = _AcdShaper1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2)
)
_AcdShaper1CodePointStatsTable_Object = MibTable
acdShaper1CodePointStatsTable = _AcdShaper1CodePointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsTable.setStatus("current")
_AcdShaper1CodePointStatsEntry_Object = MibTableRow
acdShaper1CodePointStatsEntry = _AcdShaper1CodePointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1)
)
acdShaper1CodePointStatsEntry.setIndexNames(
    (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsDstID"),
    (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsSrcID"),
    (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsColorID"),
    (0, "ACD-SHAPER-MIB", "acdShaper1CodePointStatsPcpID"),
)
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsEntry.setStatus("current")


class _AcdShaper1CodePointStatsDstID_Type(Unsigned32):
    """Custom type acdShaper1CodePointStatsDstID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdShaper1CodePointStatsDstID_Type.__name__ = "Unsigned32"
_AcdShaper1CodePointStatsDstID_Object = MibTableColumn
acdShaper1CodePointStatsDstID = _AcdShaper1CodePointStatsDstID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 1),
    _AcdShaper1CodePointStatsDstID_Type()
)
acdShaper1CodePointStatsDstID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDstID.setStatus("current")


class _AcdShaper1CodePointStatsSrcID_Type(Unsigned32):
    """Custom type acdShaper1CodePointStatsSrcID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdShaper1CodePointStatsSrcID_Type.__name__ = "Unsigned32"
_AcdShaper1CodePointStatsSrcID_Object = MibTableColumn
acdShaper1CodePointStatsSrcID = _AcdShaper1CodePointStatsSrcID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 2),
    _AcdShaper1CodePointStatsSrcID_Type()
)
acdShaper1CodePointStatsSrcID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsSrcID.setStatus("current")


class _AcdShaper1CodePointStatsColorID_Type(Integer32):
    """Custom type acdShaper1CodePointStatsColorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_AcdShaper1CodePointStatsColorID_Type.__name__ = "Integer32"
_AcdShaper1CodePointStatsColorID_Object = MibTableColumn
acdShaper1CodePointStatsColorID = _AcdShaper1CodePointStatsColorID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 3),
    _AcdShaper1CodePointStatsColorID_Type()
)
acdShaper1CodePointStatsColorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsColorID.setStatus("current")


class _AcdShaper1CodePointStatsPcpID_Type(Unsigned32):
    """Custom type acdShaper1CodePointStatsPcpID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdShaper1CodePointStatsPcpID_Type.__name__ = "Unsigned32"
_AcdShaper1CodePointStatsPcpID_Object = MibTableColumn
acdShaper1CodePointStatsPcpID = _AcdShaper1CodePointStatsPcpID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 4),
    _AcdShaper1CodePointStatsPcpID_Type()
)
acdShaper1CodePointStatsPcpID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsPcpID.setStatus("current")
_AcdShaper1CodePointStatsFwdOctets_Type = Counter64
_AcdShaper1CodePointStatsFwdOctets_Object = MibTableColumn
acdShaper1CodePointStatsFwdOctets = _AcdShaper1CodePointStatsFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 5),
    _AcdShaper1CodePointStatsFwdOctets_Type()
)
acdShaper1CodePointStatsFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsFwdOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsFwdOctets.setUnits("Octets")
_AcdShaper1CodePointStatsFwdPkts_Type = Counter64
_AcdShaper1CodePointStatsFwdPkts_Object = MibTableColumn
acdShaper1CodePointStatsFwdPkts = _AcdShaper1CodePointStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 6),
    _AcdShaper1CodePointStatsFwdPkts_Type()
)
acdShaper1CodePointStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsFwdPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsFwdPkts.setUnits("Packets")
_AcdShaper1CodePointStatsFwdRate_Type = Gauge32
_AcdShaper1CodePointStatsFwdRate_Object = MibTableColumn
acdShaper1CodePointStatsFwdRate = _AcdShaper1CodePointStatsFwdRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 7),
    _AcdShaper1CodePointStatsFwdRate_Type()
)
acdShaper1CodePointStatsFwdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsFwdRate.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsFwdRate.setUnits("Mbps")
_AcdShaper1CodePointStatsDelayedOctets_Type = Counter64
_AcdShaper1CodePointStatsDelayedOctets_Object = MibTableColumn
acdShaper1CodePointStatsDelayedOctets = _AcdShaper1CodePointStatsDelayedOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 8),
    _AcdShaper1CodePointStatsDelayedOctets_Type()
)
acdShaper1CodePointStatsDelayedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDelayedOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDelayedOctets.setUnits("Octets")
_AcdShaper1CodePointStatsDelayedPkts_Type = Counter64
_AcdShaper1CodePointStatsDelayedPkts_Object = MibTableColumn
acdShaper1CodePointStatsDelayedPkts = _AcdShaper1CodePointStatsDelayedPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 9),
    _AcdShaper1CodePointStatsDelayedPkts_Type()
)
acdShaper1CodePointStatsDelayedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDelayedPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDelayedPkts.setUnits("Packets")
_AcdShaper1CodePointStatsDelayedRate_Type = Gauge32
_AcdShaper1CodePointStatsDelayedRate_Object = MibTableColumn
acdShaper1CodePointStatsDelayedRate = _AcdShaper1CodePointStatsDelayedRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 10),
    _AcdShaper1CodePointStatsDelayedRate_Type()
)
acdShaper1CodePointStatsDelayedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDelayedRate.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsDelayedRate.setUnits("Mbps")
_AcdShaper1CodePointStatsOverflowOctets_Type = Counter64
_AcdShaper1CodePointStatsOverflowOctets_Object = MibTableColumn
acdShaper1CodePointStatsOverflowOctets = _AcdShaper1CodePointStatsOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 11),
    _AcdShaper1CodePointStatsOverflowOctets_Type()
)
acdShaper1CodePointStatsOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsOverflowOctets.setUnits("Octets")
_AcdShaper1CodePointStatsOverflowPkts_Type = Counter64
_AcdShaper1CodePointStatsOverflowPkts_Object = MibTableColumn
acdShaper1CodePointStatsOverflowPkts = _AcdShaper1CodePointStatsOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 12),
    _AcdShaper1CodePointStatsOverflowPkts_Type()
)
acdShaper1CodePointStatsOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsOverflowPkts.setUnits("Packets")
_AcdShaper1CodePointStatsOverflowRate_Type = Gauge32
_AcdShaper1CodePointStatsOverflowRate_Object = MibTableColumn
acdShaper1CodePointStatsOverflowRate = _AcdShaper1CodePointStatsOverflowRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 13),
    _AcdShaper1CodePointStatsOverflowRate_Type()
)
acdShaper1CodePointStatsOverflowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsOverflowRate.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsOverflowRate.setUnits("Mbps")
_AcdShaper1CodePointStatsQMgmtDropOctets_Type = Counter64
_AcdShaper1CodePointStatsQMgmtDropOctets_Object = MibTableColumn
acdShaper1CodePointStatsQMgmtDropOctets = _AcdShaper1CodePointStatsQMgmtDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 14),
    _AcdShaper1CodePointStatsQMgmtDropOctets_Type()
)
acdShaper1CodePointStatsQMgmtDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsQMgmtDropOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsQMgmtDropOctets.setUnits("Octets")
_AcdShaper1CodePointStatsQMgmtDropPkts_Type = Counter64
_AcdShaper1CodePointStatsQMgmtDropPkts_Object = MibTableColumn
acdShaper1CodePointStatsQMgmtDropPkts = _AcdShaper1CodePointStatsQMgmtDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 15),
    _AcdShaper1CodePointStatsQMgmtDropPkts_Type()
)
acdShaper1CodePointStatsQMgmtDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsQMgmtDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsQMgmtDropPkts.setUnits("Packets")
_AcdShaper1CodePointStatsQMgmtDropRate_Type = Gauge32
_AcdShaper1CodePointStatsQMgmtDropRate_Object = MibTableColumn
acdShaper1CodePointStatsQMgmtDropRate = _AcdShaper1CodePointStatsQMgmtDropRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 1, 2, 1, 1, 16),
    _AcdShaper1CodePointStatsQMgmtDropRate_Type()
)
acdShaper1CodePointStatsQMgmtDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsQMgmtDropRate.setStatus("current")
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsQMgmtDropRate.setUnits("Mbps")
_AcdShaper1Conformance_ObjectIdentity = ObjectIdentity
acdShaper1Conformance = _AcdShaper1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2)
)
_AcdShaper1Compliances_ObjectIdentity = ObjectIdentity
acdShaper1Compliances = _AcdShaper1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 1)
)
_AcdShaper1Groups_ObjectIdentity = ObjectIdentity
acdShaper1Groups = _AcdShaper1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 2)
)

# Managed Objects groups

acdShaper1CodePointStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 2, 1)
)
acdShaper1CodePointStatsGroup.setObjects(
      *(("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdOctets"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdPkts"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsFwdRate"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedOctets"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedPkts"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsDelayedRate"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowOctets"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowPkts"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsOverflowRate"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropOctets"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropPkts"),
        ("ACD-SHAPER-MIB", "acdShaper1CodePointStatsQMgmtDropRate"))
)
if mibBuilder.loadTexts:
    acdShaper1CodePointStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdShaper1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdShaper1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-SHAPER-MIB",
    **{"acdShaper": acdShaper,
       "acdShaper1": acdShaper1,
       "acdShaper1MIBObjects": acdShaper1MIBObjects,
       "acdShaper1Config": acdShaper1Config,
       "acdShaper1Stats": acdShaper1Stats,
       "acdShaper1CodePointStatsTable": acdShaper1CodePointStatsTable,
       "acdShaper1CodePointStatsEntry": acdShaper1CodePointStatsEntry,
       "acdShaper1CodePointStatsDstID": acdShaper1CodePointStatsDstID,
       "acdShaper1CodePointStatsSrcID": acdShaper1CodePointStatsSrcID,
       "acdShaper1CodePointStatsColorID": acdShaper1CodePointStatsColorID,
       "acdShaper1CodePointStatsPcpID": acdShaper1CodePointStatsPcpID,
       "acdShaper1CodePointStatsFwdOctets": acdShaper1CodePointStatsFwdOctets,
       "acdShaper1CodePointStatsFwdPkts": acdShaper1CodePointStatsFwdPkts,
       "acdShaper1CodePointStatsFwdRate": acdShaper1CodePointStatsFwdRate,
       "acdShaper1CodePointStatsDelayedOctets": acdShaper1CodePointStatsDelayedOctets,
       "acdShaper1CodePointStatsDelayedPkts": acdShaper1CodePointStatsDelayedPkts,
       "acdShaper1CodePointStatsDelayedRate": acdShaper1CodePointStatsDelayedRate,
       "acdShaper1CodePointStatsOverflowOctets": acdShaper1CodePointStatsOverflowOctets,
       "acdShaper1CodePointStatsOverflowPkts": acdShaper1CodePointStatsOverflowPkts,
       "acdShaper1CodePointStatsOverflowRate": acdShaper1CodePointStatsOverflowRate,
       "acdShaper1CodePointStatsQMgmtDropOctets": acdShaper1CodePointStatsQMgmtDropOctets,
       "acdShaper1CodePointStatsQMgmtDropPkts": acdShaper1CodePointStatsQMgmtDropPkts,
       "acdShaper1CodePointStatsQMgmtDropRate": acdShaper1CodePointStatsQMgmtDropRate,
       "acdShaper1Conformance": acdShaper1Conformance,
       "acdShaper1Compliances": acdShaper1Compliances,
       "acdShaper1Compliance": acdShaper1Compliance,
       "acdShaper1Groups": acdShaper1Groups,
       "acdShaper1CodePointStatsGroup": acdShaper1CodePointStatsGroup}
)
