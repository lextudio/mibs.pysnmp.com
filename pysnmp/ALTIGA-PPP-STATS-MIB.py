# SNMP MIB module (ALTIGA-PPP-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-PPP-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:18 2024
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

(alPppMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alPppMibModule")

(alPppGroup,
 alStatsPpp) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alPppGroup",
    "alStatsPpp")

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

altigaPppStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 11, 2)
)
altigaPppStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaPppStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaPppStatsMibConformance = _AltigaPppStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 11, 2, 1)
)
_AltigaPppStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaPppStatsMibCompliances = _AltigaPppStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 11, 2, 1, 1)
)
_AlStatsPppGlobal_ObjectIdentity = ObjectIdentity
alStatsPppGlobal = _AlStatsPppGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 1)
)
_AlPppStatsTable_Object = MibTable
alPppStatsTable = _AlPppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    alPppStatsTable.setStatus("current")
_AlPppStatsEntry_Object = MibTableRow
alPppStatsEntry = _AlPppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1)
)
alPppStatsEntry.setIndexNames(
    (0, "ALTIGA-PPP-STATS-MIB", "alPppStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alPppStatsEntry.setStatus("current")
_AlPppStatsRowStatus_Type = RowStatus
_AlPppStatsRowStatus_Object = MibTableColumn
alPppStatsRowStatus = _AlPppStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 1),
    _AlPppStatsRowStatus_Type()
)
alPppStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alPppStatsRowStatus.setStatus("current")


class _AlPppStatsIfIndex_Type(Integer32):
    """Custom type alPppStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlPppStatsIfIndex_Type.__name__ = "Integer32"
_AlPppStatsIfIndex_Object = MibTableColumn
alPppStatsIfIndex = _AlPppStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 2),
    _AlPppStatsIfIndex_Type()
)
alPppStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsIfIndex.setStatus("current")
_AlPppStatsOctetsSent_Type = Counter32
_AlPppStatsOctetsSent_Object = MibTableColumn
alPppStatsOctetsSent = _AlPppStatsOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 3),
    _AlPppStatsOctetsSent_Type()
)
alPppStatsOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsOctetsSent.setStatus("current")
_AlPppStatsOctetsRcvd_Type = Counter32
_AlPppStatsOctetsRcvd_Object = MibTableColumn
alPppStatsOctetsRcvd = _AlPppStatsOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 4),
    _AlPppStatsOctetsRcvd_Type()
)
alPppStatsOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsOctetsRcvd.setStatus("current")
_AlPppStatsPacketsSent_Type = Counter32
_AlPppStatsPacketsSent_Object = MibTableColumn
alPppStatsPacketsSent = _AlPppStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 5),
    _AlPppStatsPacketsSent_Type()
)
alPppStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsPacketsSent.setStatus("current")
_AlPppStatsPacketsRcvd_Type = Counter32
_AlPppStatsPacketsRcvd_Object = MibTableColumn
alPppStatsPacketsRcvd = _AlPppStatsPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 6),
    _AlPppStatsPacketsRcvd_Type()
)
alPppStatsPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsPacketsRcvd.setStatus("current")
_AlPppStatsMppcStatus_Type = TruthValue
_AlPppStatsMppcStatus_Object = MibTableColumn
alPppStatsMppcStatus = _AlPppStatsMppcStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 7),
    _AlPppStatsMppcStatus_Type()
)
alPppStatsMppcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcStatus.setStatus("current")
_AlPppStatsMppeStatus_Type = TruthValue
_AlPppStatsMppeStatus_Object = MibTableColumn
alPppStatsMppeStatus = _AlPppStatsMppeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 8),
    _AlPppStatsMppeStatus_Type()
)
alPppStatsMppeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppeStatus.setStatus("current")
_AlPppStatsMppcMppeReset_Type = Counter32
_AlPppStatsMppcMppeReset_Object = MibTableColumn
alPppStatsMppcMppeReset = _AlPppStatsMppcMppeReset_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 9),
    _AlPppStatsMppcMppeReset_Type()
)
alPppStatsMppcMppeReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcMppeReset.setStatus("current")
_AlPppStatsMppcOctSentAfterComp_Type = Counter32
_AlPppStatsMppcOctSentAfterComp_Object = MibTableColumn
alPppStatsMppcOctSentAfterComp = _AlPppStatsMppcOctSentAfterComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 10),
    _AlPppStatsMppcOctSentAfterComp_Type()
)
alPppStatsMppcOctSentAfterComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcOctSentAfterComp.setStatus("current")
_AlPppStatsMppcOctSentBeforeComp_Type = Counter32
_AlPppStatsMppcOctSentBeforeComp_Object = MibTableColumn
alPppStatsMppcOctSentBeforeComp = _AlPppStatsMppcOctSentBeforeComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 11),
    _AlPppStatsMppcOctSentBeforeComp_Type()
)
alPppStatsMppcOctSentBeforeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcOctSentBeforeComp.setStatus("current")
_AlPppStatsMppcOctSentUnComp_Type = Counter32
_AlPppStatsMppcOctSentUnComp_Object = MibTableColumn
alPppStatsMppcOctSentUnComp = _AlPppStatsMppcOctSentUnComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 12),
    _AlPppStatsMppcOctSentUnComp_Type()
)
alPppStatsMppcOctSentUnComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcOctSentUnComp.setStatus("current")
_AlPppStatsMppcOctRcvdBeforeDeComp_Type = Counter32
_AlPppStatsMppcOctRcvdBeforeDeComp_Object = MibTableColumn
alPppStatsMppcOctRcvdBeforeDeComp = _AlPppStatsMppcOctRcvdBeforeDeComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 13),
    _AlPppStatsMppcOctRcvdBeforeDeComp_Type()
)
alPppStatsMppcOctRcvdBeforeDeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcOctRcvdBeforeDeComp.setStatus("current")
_AlPppStatsMppcOctRcvdAfterDeComp_Type = Counter32
_AlPppStatsMppcOctRcvdAfterDeComp_Object = MibTableColumn
alPppStatsMppcOctRcvdAfterDeComp = _AlPppStatsMppcOctRcvdAfterDeComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 14),
    _AlPppStatsMppcOctRcvdAfterDeComp_Type()
)
alPppStatsMppcOctRcvdAfterDeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcOctRcvdAfterDeComp.setStatus("current")
_AlPppStatsMppcOctRcvdUnComp_Type = Counter32
_AlPppStatsMppcOctRcvdUnComp_Object = MibTableColumn
alPppStatsMppcOctRcvdUnComp = _AlPppStatsMppcOctRcvdUnComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 2, 1, 15),
    _AlPppStatsMppcOctRcvdUnComp_Type()
)
alPppStatsMppcOctRcvdUnComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsMppcOctRcvdUnComp.setStatus("current")
_AlStatsPppMppcGlobal_ObjectIdentity = ObjectIdentity
alStatsPppMppcGlobal = _AlStatsPppMppcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3)
)
_AlPppStatsGlobMppcMppeResetsRcvd_Type = Counter32
_AlPppStatsGlobMppcMppeResetsRcvd_Object = MibScalar
alPppStatsGlobMppcMppeResetsRcvd = _AlPppStatsGlobMppcMppeResetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 1),
    _AlPppStatsGlobMppcMppeResetsRcvd_Type()
)
alPppStatsGlobMppcMppeResetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcMppeResetsRcvd.setStatus("current")
_AlPppStatsGlobMppcMppeResetsSent_Type = Counter32
_AlPppStatsGlobMppcMppeResetsSent_Object = MibScalar
alPppStatsGlobMppcMppeResetsSent = _AlPppStatsGlobMppcMppeResetsSent_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 2),
    _AlPppStatsGlobMppcMppeResetsSent_Type()
)
alPppStatsGlobMppcMppeResetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcMppeResetsSent.setStatus("current")
_AlPppStatsGlobMppcOctSentAfterComp_Type = Counter32
_AlPppStatsGlobMppcOctSentAfterComp_Object = MibScalar
alPppStatsGlobMppcOctSentAfterComp = _AlPppStatsGlobMppcOctSentAfterComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 3),
    _AlPppStatsGlobMppcOctSentAfterComp_Type()
)
alPppStatsGlobMppcOctSentAfterComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcOctSentAfterComp.setStatus("current")
_AlPppStatsGlobMppcOctSentBeforeComp_Type = Counter32
_AlPppStatsGlobMppcOctSentBeforeComp_Object = MibScalar
alPppStatsGlobMppcOctSentBeforeComp = _AlPppStatsGlobMppcOctSentBeforeComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 4),
    _AlPppStatsGlobMppcOctSentBeforeComp_Type()
)
alPppStatsGlobMppcOctSentBeforeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcOctSentBeforeComp.setStatus("current")
_AlPppStatsGlobMppcOctSentUnComp_Type = Counter32
_AlPppStatsGlobMppcOctSentUnComp_Object = MibScalar
alPppStatsGlobMppcOctSentUnComp = _AlPppStatsGlobMppcOctSentUnComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 5),
    _AlPppStatsGlobMppcOctSentUnComp_Type()
)
alPppStatsGlobMppcOctSentUnComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcOctSentUnComp.setStatus("current")
_AlPppStatsGlobMppcOctRcvdBeforeDeComp_Type = Counter32
_AlPppStatsGlobMppcOctRcvdBeforeDeComp_Object = MibScalar
alPppStatsGlobMppcOctRcvdBeforeDeComp = _AlPppStatsGlobMppcOctRcvdBeforeDeComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 6),
    _AlPppStatsGlobMppcOctRcvdBeforeDeComp_Type()
)
alPppStatsGlobMppcOctRcvdBeforeDeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcOctRcvdBeforeDeComp.setStatus("current")
_AlPppStatsGlobMppcOctRcvdAfterDeComp_Type = Counter32
_AlPppStatsGlobMppcOctRcvdAfterDeComp_Object = MibScalar
alPppStatsGlobMppcOctRcvdAfterDeComp = _AlPppStatsGlobMppcOctRcvdAfterDeComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 7),
    _AlPppStatsGlobMppcOctRcvdAfterDeComp_Type()
)
alPppStatsGlobMppcOctRcvdAfterDeComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcOctRcvdAfterDeComp.setStatus("current")
_AlPppStatsGlobMppcOctRcvdUnComp_Type = Counter32
_AlPppStatsGlobMppcOctRcvdUnComp_Object = MibScalar
alPppStatsGlobMppcOctRcvdUnComp = _AlPppStatsGlobMppcOctRcvdUnComp_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 6, 3, 8),
    _AlPppStatsGlobMppcOctRcvdUnComp_Type()
)
alPppStatsGlobMppcOctRcvdUnComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPppStatsGlobMppcOctRcvdUnComp.setStatus("current")

# Managed Objects groups

altigaPppStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 6, 2)
)
altigaPppStatsGroup.setObjects(
      *(("ALTIGA-PPP-STATS-MIB", "alPppStatsRowStatus"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsIfIndex"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsOctetsSent"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsOctetsRcvd"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsPacketsSent"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsPacketsRcvd"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcStatus"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppeStatus"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcMppeReset"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcOctSentAfterComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcOctSentBeforeComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcOctSentUnComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcOctRcvdBeforeDeComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcOctRcvdAfterDeComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsMppcOctRcvdUnComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcMppeResetsRcvd"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcMppeResetsSent"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcOctSentAfterComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcOctSentBeforeComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcOctSentUnComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcOctRcvdBeforeDeComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcOctRcvdAfterDeComp"),
        ("ALTIGA-PPP-STATS-MIB", "alPppStatsGlobMppcOctRcvdUnComp"))
)
if mibBuilder.loadTexts:
    altigaPppStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaPppStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 11, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaPppStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-PPP-STATS-MIB",
    **{"altigaPppStatsMibModule": altigaPppStatsMibModule,
       "altigaPppStatsMibConformance": altigaPppStatsMibConformance,
       "altigaPppStatsMibCompliances": altigaPppStatsMibCompliances,
       "altigaPppStatsMibCompliance": altigaPppStatsMibCompliance,
       "altigaPppStatsGroup": altigaPppStatsGroup,
       "alStatsPppGlobal": alStatsPppGlobal,
       "alPppStatsTable": alPppStatsTable,
       "alPppStatsEntry": alPppStatsEntry,
       "alPppStatsRowStatus": alPppStatsRowStatus,
       "alPppStatsIfIndex": alPppStatsIfIndex,
       "alPppStatsOctetsSent": alPppStatsOctetsSent,
       "alPppStatsOctetsRcvd": alPppStatsOctetsRcvd,
       "alPppStatsPacketsSent": alPppStatsPacketsSent,
       "alPppStatsPacketsRcvd": alPppStatsPacketsRcvd,
       "alPppStatsMppcStatus": alPppStatsMppcStatus,
       "alPppStatsMppeStatus": alPppStatsMppeStatus,
       "alPppStatsMppcMppeReset": alPppStatsMppcMppeReset,
       "alPppStatsMppcOctSentAfterComp": alPppStatsMppcOctSentAfterComp,
       "alPppStatsMppcOctSentBeforeComp": alPppStatsMppcOctSentBeforeComp,
       "alPppStatsMppcOctSentUnComp": alPppStatsMppcOctSentUnComp,
       "alPppStatsMppcOctRcvdBeforeDeComp": alPppStatsMppcOctRcvdBeforeDeComp,
       "alPppStatsMppcOctRcvdAfterDeComp": alPppStatsMppcOctRcvdAfterDeComp,
       "alPppStatsMppcOctRcvdUnComp": alPppStatsMppcOctRcvdUnComp,
       "alStatsPppMppcGlobal": alStatsPppMppcGlobal,
       "alPppStatsGlobMppcMppeResetsRcvd": alPppStatsGlobMppcMppeResetsRcvd,
       "alPppStatsGlobMppcMppeResetsSent": alPppStatsGlobMppcMppeResetsSent,
       "alPppStatsGlobMppcOctSentAfterComp": alPppStatsGlobMppcOctSentAfterComp,
       "alPppStatsGlobMppcOctSentBeforeComp": alPppStatsGlobMppcOctSentBeforeComp,
       "alPppStatsGlobMppcOctSentUnComp": alPppStatsGlobMppcOctSentUnComp,
       "alPppStatsGlobMppcOctRcvdBeforeDeComp": alPppStatsGlobMppcOctRcvdBeforeDeComp,
       "alPppStatsGlobMppcOctRcvdAfterDeComp": alPppStatsGlobMppcOctRcvdAfterDeComp,
       "alPppStatsGlobMppcOctRcvdUnComp": alPppStatsGlobMppcOctRcvdUnComp}
)
