# SNMP MIB module (ALTIGA-FILTER-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-FILTER-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:10 2024
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

(alFilterMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alFilterMibModule")

(alFilterGroup,
 alStatsFilter) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alFilterGroup",
    "alStatsFilter")

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

altigaFilterStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 14, 2)
)
altigaFilterStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaFilterStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaFilterStatsMibConformance = _AltigaFilterStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 14, 2, 1)
)
_AltigaFilterStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaFilterStatsMibCompliances = _AltigaFilterStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 14, 2, 1, 1)
)
_AlStatsFilterGlobal_ObjectIdentity = ObjectIdentity
alStatsFilterGlobal = _AlStatsFilterGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 1)
)
_AlFilterStatsTable_Object = MibTable
alFilterStatsTable = _AlFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    alFilterStatsTable.setStatus("current")
_AlFilterStatsEntry_Object = MibTableRow
alFilterStatsEntry = _AlFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1)
)
alFilterStatsEntry.setIndexNames(
    (0, "ALTIGA-FILTER-STATS-MIB", "alFilterStatsInterfaceId"),
)
if mibBuilder.loadTexts:
    alFilterStatsEntry.setStatus("current")


class _AlFilterStatsInterfaceId_Type(Integer32):
    """Custom type alFilterStatsInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlFilterStatsInterfaceId_Type.__name__ = "Integer32"
_AlFilterStatsInterfaceId_Object = MibTableColumn
alFilterStatsInterfaceId = _AlFilterStatsInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 1),
    _AlFilterStatsInterfaceId_Type()
)
alFilterStatsInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInterfaceId.setStatus("current")
_AlFilterStatsStartTime_Type = TimeTicks
_AlFilterStatsStartTime_Object = MibTableColumn
alFilterStatsStartTime = _AlFilterStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 2),
    _AlFilterStatsStartTime_Type()
)
alFilterStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsStartTime.setStatus("current")
_AlFilterStatsInPktsFiltered_Type = Counter32
_AlFilterStatsInPktsFiltered_Object = MibTableColumn
alFilterStatsInPktsFiltered = _AlFilterStatsInPktsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 3),
    _AlFilterStatsInPktsFiltered_Type()
)
alFilterStatsInPktsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInPktsFiltered.setStatus("current")
_AlFilterStatsOutPktsFiltered_Type = Counter32
_AlFilterStatsOutPktsFiltered_Object = MibTableColumn
alFilterStatsOutPktsFiltered = _AlFilterStatsOutPktsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 4),
    _AlFilterStatsOutPktsFiltered_Type()
)
alFilterStatsOutPktsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutPktsFiltered.setStatus("current")
_AlFilterStatsInPktsRx_Type = Counter32
_AlFilterStatsInPktsRx_Object = MibTableColumn
alFilterStatsInPktsRx = _AlFilterStatsInPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 5),
    _AlFilterStatsInPktsRx_Type()
)
alFilterStatsInPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInPktsRx.setStatus("current")
_AlFilterStatsOutPktsRx_Type = Counter32
_AlFilterStatsOutPktsRx_Object = MibTableColumn
alFilterStatsOutPktsRx = _AlFilterStatsOutPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 6),
    _AlFilterStatsOutPktsRx_Type()
)
alFilterStatsOutPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutPktsRx.setStatus("current")
_AlFilterStatsInPktsTx_Type = Counter32
_AlFilterStatsInPktsTx_Object = MibTableColumn
alFilterStatsInPktsTx = _AlFilterStatsInPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 7),
    _AlFilterStatsInPktsTx_Type()
)
alFilterStatsInPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInPktsTx.setStatus("current")
_AlFilterStatsOutPktsTx_Type = Counter32
_AlFilterStatsOutPktsTx_Object = MibTableColumn
alFilterStatsOutPktsTx = _AlFilterStatsOutPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 8),
    _AlFilterStatsOutPktsTx_Type()
)
alFilterStatsOutPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutPktsTx.setStatus("current")
_AlFilterStatsInShortTcpHdr_Type = Counter32
_AlFilterStatsInShortTcpHdr_Object = MibTableColumn
alFilterStatsInShortTcpHdr = _AlFilterStatsInShortTcpHdr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 9),
    _AlFilterStatsInShortTcpHdr_Type()
)
alFilterStatsInShortTcpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInShortTcpHdr.setStatus("current")
_AlFilterStatsOutShortTcpHdr_Type = Counter32
_AlFilterStatsOutShortTcpHdr_Object = MibTableColumn
alFilterStatsOutShortTcpHdr = _AlFilterStatsOutShortTcpHdr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 10),
    _AlFilterStatsOutShortTcpHdr_Type()
)
alFilterStatsOutShortTcpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutShortTcpHdr.setStatus("current")
_AlFilterStatsInShortUdpHdr_Type = Counter32
_AlFilterStatsInShortUdpHdr_Object = MibTableColumn
alFilterStatsInShortUdpHdr = _AlFilterStatsInShortUdpHdr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 11),
    _AlFilterStatsInShortUdpHdr_Type()
)
alFilterStatsInShortUdpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInShortUdpHdr.setStatus("current")
_AlFilterStatsOutShortUdpHdr_Type = Counter32
_AlFilterStatsOutShortUdpHdr_Object = MibTableColumn
alFilterStatsOutShortUdpHdr = _AlFilterStatsOutShortUdpHdr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 12),
    _AlFilterStatsOutShortUdpHdr_Type()
)
alFilterStatsOutShortUdpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutShortUdpHdr.setStatus("current")
_AlFilterStatsInTcpFragDiscard_Type = Counter32
_AlFilterStatsInTcpFragDiscard_Object = MibTableColumn
alFilterStatsInTcpFragDiscard = _AlFilterStatsInTcpFragDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 13),
    _AlFilterStatsInTcpFragDiscard_Type()
)
alFilterStatsInTcpFragDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInTcpFragDiscard.setStatus("current")
_AlFilterStatsOutTcpFragDiscard_Type = Counter32
_AlFilterStatsOutTcpFragDiscard_Object = MibTableColumn
alFilterStatsOutTcpFragDiscard = _AlFilterStatsOutTcpFragDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 14),
    _AlFilterStatsOutTcpFragDiscard_Type()
)
alFilterStatsOutTcpFragDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutTcpFragDiscard.setStatus("current")
_AlFilterStatsInIcmpFragDiscard_Type = Counter32
_AlFilterStatsInIcmpFragDiscard_Object = MibTableColumn
alFilterStatsInIcmpFragDiscard = _AlFilterStatsInIcmpFragDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 15),
    _AlFilterStatsInIcmpFragDiscard_Type()
)
alFilterStatsInIcmpFragDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsInIcmpFragDiscard.setStatus("current")
_AlFilterStatsOutIcmpFragDiscard_Type = Counter32
_AlFilterStatsOutIcmpFragDiscard_Object = MibTableColumn
alFilterStatsOutIcmpFragDiscard = _AlFilterStatsOutIcmpFragDiscard_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 9, 2, 1, 16),
    _AlFilterStatsOutIcmpFragDiscard_Type()
)
alFilterStatsOutIcmpFragDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alFilterStatsOutIcmpFragDiscard.setStatus("current")

# Managed Objects groups

altigaFilterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 9, 2)
)
altigaFilterStatsGroup.setObjects(
      *(("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInterfaceId"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsStartTime"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInPktsFiltered"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutPktsFiltered"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInPktsRx"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutPktsRx"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInPktsTx"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutPktsTx"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInShortTcpHdr"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutShortTcpHdr"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInShortUdpHdr"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutShortUdpHdr"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInTcpFragDiscard"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutTcpFragDiscard"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsInIcmpFragDiscard"),
        ("ALTIGA-FILTER-STATS-MIB", "alFilterStatsOutIcmpFragDiscard"))
)
if mibBuilder.loadTexts:
    altigaFilterStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaFilterStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 14, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaFilterStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-FILTER-STATS-MIB",
    **{"altigaFilterStatsMibModule": altigaFilterStatsMibModule,
       "altigaFilterStatsMibConformance": altigaFilterStatsMibConformance,
       "altigaFilterStatsMibCompliances": altigaFilterStatsMibCompliances,
       "altigaFilterStatsMibCompliance": altigaFilterStatsMibCompliance,
       "altigaFilterStatsGroup": altigaFilterStatsGroup,
       "alStatsFilterGlobal": alStatsFilterGlobal,
       "alFilterStatsTable": alFilterStatsTable,
       "alFilterStatsEntry": alFilterStatsEntry,
       "alFilterStatsInterfaceId": alFilterStatsInterfaceId,
       "alFilterStatsStartTime": alFilterStatsStartTime,
       "alFilterStatsInPktsFiltered": alFilterStatsInPktsFiltered,
       "alFilterStatsOutPktsFiltered": alFilterStatsOutPktsFiltered,
       "alFilterStatsInPktsRx": alFilterStatsInPktsRx,
       "alFilterStatsOutPktsRx": alFilterStatsOutPktsRx,
       "alFilterStatsInPktsTx": alFilterStatsInPktsTx,
       "alFilterStatsOutPktsTx": alFilterStatsOutPktsTx,
       "alFilterStatsInShortTcpHdr": alFilterStatsInShortTcpHdr,
       "alFilterStatsOutShortTcpHdr": alFilterStatsOutShortTcpHdr,
       "alFilterStatsInShortUdpHdr": alFilterStatsInShortUdpHdr,
       "alFilterStatsOutShortUdpHdr": alFilterStatsOutShortUdpHdr,
       "alFilterStatsInTcpFragDiscard": alFilterStatsInTcpFragDiscard,
       "alFilterStatsOutTcpFragDiscard": alFilterStatsOutTcpFragDiscard,
       "alFilterStatsInIcmpFragDiscard": alFilterStatsInIcmpFragDiscard,
       "alFilterStatsOutIcmpFragDiscard": alFilterStatsOutIcmpFragDiscard}
)
