# SNMP MIB module (CISCO-CASA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CASA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:59 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoIpProtocol,
 CiscoPort) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol",
    "CiscoPort")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCasaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122)
)
ciscoCasaMIB.setRevisions(
        ("2002-09-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CasaFixedAffinityIndex(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCasaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCasaMIBObjects = _CiscoCasaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1)
)
_CCasaGlobal_ObjectIdentity = ObjectIdentity
cCasaGlobal = _CCasaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1)
)
_CCasaTable_Object = MibTable
cCasaTable = _CCasaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cCasaTable.setStatus("current")
_CCasaEntry_Object = MibTableRow
cCasaEntry = _CCasaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1)
)
cCasaEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
)
if mibBuilder.loadTexts:
    cCasaEntry.setStatus("current")


class _CCasaEntity_Type(Integer32):
    """Custom type cCasaEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("casaForwardingAgent", 1),
          ("casaGLoBalManager", 2),
          ("casaUnknownManager", 3))
    )


_CCasaEntity_Type.__name__ = "Integer32"
_CCasaEntity_Object = MibTableColumn
cCasaEntity = _CCasaEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 1),
    _CCasaEntity_Type()
)
cCasaEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaEntity.setStatus("current")


class _CCasaState_Type(Integer32):
    """Custom type cCasaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("casaActive", 3),
          ("casaEnabled", 2),
          ("casaNotEnabled", 1))
    )


_CCasaState_Type.__name__ = "Integer32"
_CCasaState_Object = MibTableColumn
cCasaState = _CCasaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 2),
    _CCasaState_Type()
)
cCasaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCasaState.setStatus("current")


class _CCasaStateNotificationEnabled_Type(TruthValue):
    """Custom type cCasaStateNotificationEnabled based on TruthValue"""


_CCasaStateNotificationEnabled_Object = MibTableColumn
cCasaStateNotificationEnabled = _CCasaStateNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 3),
    _CCasaStateNotificationEnabled_Type()
)
cCasaStateNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCasaStateNotificationEnabled.setStatus("current")
_CCasaCfgAddress_Type = IpAddress
_CCasaCfgAddress_Object = MibTableColumn
cCasaCfgAddress = _CCasaCfgAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 4),
    _CCasaCfgAddress_Type()
)
cCasaCfgAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCasaCfgAddress.setStatus("current")
_CCasaCfgAddressMask_Type = IpAddress
_CCasaCfgAddressMask_Object = MibTableColumn
cCasaCfgAddressMask = _CCasaCfgAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 5),
    _CCasaCfgAddressMask_Type()
)
cCasaCfgAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCasaCfgAddressMask.setStatus("obsolete")
_CCasaCfgMcastAddress_Type = IpAddress
_CCasaCfgMcastAddress_Object = MibTableColumn
cCasaCfgMcastAddress = _CCasaCfgMcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 6),
    _CCasaCfgMcastAddress_Type()
)
cCasaCfgMcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCasaCfgMcastAddress.setStatus("current")
_CCasaAddress_Type = IpAddress
_CCasaAddress_Object = MibTableColumn
cCasaAddress = _CCasaAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 7),
    _CCasaAddress_Type()
)
cCasaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAddress.setStatus("current")
_CCasaAddressMask_Type = IpAddress
_CCasaAddressMask_Object = MibTableColumn
cCasaAddressMask = _CCasaAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 8),
    _CCasaAddressMask_Type()
)
cCasaAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAddressMask.setStatus("obsolete")
_CCasaMcastAddress_Type = IpAddress
_CCasaMcastAddress_Object = MibTableColumn
cCasaMcastAddress = _CCasaMcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 1, 1, 1, 9),
    _CCasaMcastAddress_Type()
)
cCasaMcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaMcastAddress.setStatus("current")
_CCasaStats_ObjectIdentity = ObjectIdentity
cCasaStats = _CCasaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2)
)
_CCasaAffinityCacheStatsTable_Object = MibTable
cCasaAffinityCacheStatsTable = _CCasaAffinityCacheStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheStatsTable.setStatus("current")
_CCasaAffinityCacheStatsEntry_Object = MibTableRow
cCasaAffinityCacheStatsEntry = _CCasaAffinityCacheStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1)
)
cCasaAffinityCacheStatsEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheStatsEntry.setStatus("current")
_CCasaAffinityCacheNumOf_Type = Gauge32
_CCasaAffinityCacheNumOf_Object = MibTableColumn
cCasaAffinityCacheNumOf = _CCasaAffinityCacheNumOf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 1),
    _CCasaAffinityCacheNumOf_Type()
)
cCasaAffinityCacheNumOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheNumOf.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheNumOf.setUnits("affinities")
_CCasaAffinityCacheHiWtrMrk_Type = Unsigned32
_CCasaAffinityCacheHiWtrMrk_Object = MibTableColumn
cCasaAffinityCacheHiWtrMrk = _CCasaAffinityCacheHiWtrMrk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 2),
    _CCasaAffinityCacheHiWtrMrk_Type()
)
cCasaAffinityCacheHiWtrMrk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHiWtrMrk.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHiWtrMrk.setUnits("affinities")
_CCasaAffinityCacheHiWtrMrkReset_Type = TimeStamp
_CCasaAffinityCacheHiWtrMrkReset_Object = MibTableColumn
cCasaAffinityCacheHiWtrMrkReset = _CCasaAffinityCacheHiWtrMrkReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 3),
    _CCasaAffinityCacheHiWtrMrkReset_Type()
)
cCasaAffinityCacheHiWtrMrkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHiWtrMrkReset.setStatus("current")
_CCasaAffinityCacheNoStorageDrops_Type = Counter32
_CCasaAffinityCacheNoStorageDrops_Object = MibTableColumn
cCasaAffinityCacheNoStorageDrops = _CCasaAffinityCacheNoStorageDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 4),
    _CCasaAffinityCacheNoStorageDrops_Type()
)
cCasaAffinityCacheNoStorageDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheNoStorageDrops.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheNoStorageDrops.setUnits("affinities")
_CCasaAffinityCacheHits_Type = Counter32
_CCasaAffinityCacheHits_Object = MibTableColumn
cCasaAffinityCacheHits = _CCasaAffinityCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 5),
    _CCasaAffinityCacheHits_Type()
)
cCasaAffinityCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHits.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHits.setUnits("packets")
_CCasaAffinityCacheHCHits_Type = Counter64
_CCasaAffinityCacheHCHits_Object = MibTableColumn
cCasaAffinityCacheHCHits = _CCasaAffinityCacheHCHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 6),
    _CCasaAffinityCacheHCHits_Type()
)
cCasaAffinityCacheHCHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHCHits.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHCHits.setUnits("packets")
_CCasaAffinityCacheMisses_Type = Counter32
_CCasaAffinityCacheMisses_Object = MibTableColumn
cCasaAffinityCacheMisses = _CCasaAffinityCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 7),
    _CCasaAffinityCacheMisses_Type()
)
cCasaAffinityCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheMisses.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheMisses.setUnits("packets")
_CCasaAffinityCacheHCMisses_Type = Counter64
_CCasaAffinityCacheHCMisses_Object = MibTableColumn
cCasaAffinityCacheHCMisses = _CCasaAffinityCacheHCMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 8),
    _CCasaAffinityCacheHCMisses_Type()
)
cCasaAffinityCacheHCMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHCMisses.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheHCMisses.setUnits("packets")
_CCasaAffinityCacheIntrTimeouts_Type = Counter32
_CCasaAffinityCacheIntrTimeouts_Object = MibTableColumn
cCasaAffinityCacheIntrTimeouts = _CCasaAffinityCacheIntrTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 1, 1, 9),
    _CCasaAffinityCacheIntrTimeouts_Type()
)
cCasaAffinityCacheIntrTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheIntrTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAffinityCacheIntrTimeouts.setUnits("affinities")
_CCasaStatsTable_Object = MibTable
cCasaStatsTable = _CCasaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cCasaStatsTable.setStatus("current")
_CCasaStatsEntry_Object = MibTableRow
cCasaStatsEntry = _CCasaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 2, 1)
)
cCasaStatsEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
)
if mibBuilder.loadTexts:
    cCasaStatsEntry.setStatus("current")
_CCasaInterestPackets_Type = Counter32
_CCasaInterestPackets_Object = MibTableColumn
cCasaInterestPackets = _CCasaInterestPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 2, 1, 1),
    _CCasaInterestPackets_Type()
)
cCasaInterestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaInterestPackets.setStatus("current")
if mibBuilder.loadTexts:
    cCasaInterestPackets.setUnits("packets")
_CCasaInterestTickles_Type = Counter32
_CCasaInterestTickles_Object = MibTableColumn
cCasaInterestTickles = _CCasaInterestTickles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 2, 2, 1, 2),
    _CCasaInterestTickles_Type()
)
cCasaInterestTickles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaInterestTickles.setStatus("current")
if mibBuilder.loadTexts:
    cCasaInterestTickles.setUnits("packets")
_CCasaAdmin_ObjectIdentity = ObjectIdentity
cCasaAdmin = _CCasaAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3)
)
_CCasaAdminTable_Object = MibTable
cCasaAdminTable = _CCasaAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cCasaAdminTable.setStatus("current")
_CCasaAdminEntry_Object = MibTableRow
cCasaAdminEntry = _CCasaAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1, 1)
)
cCasaAdminEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
    (0, "CISCO-CASA-MIB", "cCasaAdminMcastPort"),
)
if mibBuilder.loadTexts:
    cCasaAdminEntry.setStatus("current")
_CCasaAdminMcastPort_Type = CiscoPort
_CCasaAdminMcastPort_Object = MibTableColumn
cCasaAdminMcastPort = _CCasaAdminMcastPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1, 1, 1),
    _CCasaAdminMcastPort_Type()
)
cCasaAdminMcastPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAdminMcastPort.setStatus("current")


class _CCasaAdminMcastPasswd_Type(DisplayString):
    """Custom type cCasaAdminMcastPasswd based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CCasaAdminMcastPasswd_Type.__name__ = "DisplayString"
_CCasaAdminMcastPasswd_Object = MibTableColumn
cCasaAdminMcastPasswd = _CCasaAdminMcastPasswd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1, 1, 2),
    _CCasaAdminMcastPasswd_Type()
)
cCasaAdminMcastPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cCasaAdminMcastPasswd.setStatus("current")


class _CCasaAdminMcastPasswdTimeout_Type(Unsigned32):
    """Custom type cCasaAdminMcastPasswdTimeout based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CCasaAdminMcastPasswdTimeout_Type.__name__ = "Unsigned32"
_CCasaAdminMcastPasswdTimeout_Object = MibTableColumn
cCasaAdminMcastPasswdTimeout = _CCasaAdminMcastPasswdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1, 1, 3),
    _CCasaAdminMcastPasswdTimeout_Type()
)
cCasaAdminMcastPasswdTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cCasaAdminMcastPasswdTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAdminMcastPasswdTimeout.setUnits("seconds")
_CCasaAdminMcastPasswdFailures_Type = Counter32
_CCasaAdminMcastPasswdFailures_Object = MibTableColumn
cCasaAdminMcastPasswdFailures = _CCasaAdminMcastPasswdFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1, 1, 4),
    _CCasaAdminMcastPasswdFailures_Type()
)
cCasaAdminMcastPasswdFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAdminMcastPasswdFailures.setStatus("current")
if mibBuilder.loadTexts:
    cCasaAdminMcastPasswdFailures.setUnits("failures")
_CCasaAdminRowStatus_Type = RowStatus
_CCasaAdminRowStatus_Object = MibTableColumn
cCasaAdminRowStatus = _CCasaAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 3, 1, 1, 5),
    _CCasaAdminRowStatus_Type()
)
cCasaAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cCasaAdminRowStatus.setStatus("current")
_CCasaAffinityCache_ObjectIdentity = ObjectIdentity
cCasaAffinityCache = _CCasaAffinityCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4)
)
_CCasaAffinityCacheSrcTable_Object = MibTable
cCasaAffinityCacheSrcTable = _CCasaAffinityCacheSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcTable.setStatus("current")
_CCasaAffinityCacheSrcEntry_Object = MibTableRow
cCasaAffinityCacheSrcEntry = _CCasaAffinityCacheSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1)
)
cCasaAffinityCacheSrcEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
    (0, "CISCO-CASA-MIB", "cCasaAffinityCacheSrcSourceAddr"),
    (0, "CISCO-CASA-MIB", "cCasaAffinityCacheSrcIndex"),
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcEntry.setStatus("current")
_CCasaAffinityCacheSrcSourceAddr_Type = IpAddress
_CCasaAffinityCacheSrcSourceAddr_Object = MibTableColumn
cCasaAffinityCacheSrcSourceAddr = _CCasaAffinityCacheSrcSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 1),
    _CCasaAffinityCacheSrcSourceAddr_Type()
)
cCasaAffinityCacheSrcSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcSourceAddr.setStatus("current")
_CCasaAffinityCacheSrcIndex_Type = CasaFixedAffinityIndex
_CCasaAffinityCacheSrcIndex_Object = MibTableColumn
cCasaAffinityCacheSrcIndex = _CCasaAffinityCacheSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 2),
    _CCasaAffinityCacheSrcIndex_Type()
)
cCasaAffinityCacheSrcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcIndex.setStatus("current")
_CCasaAffinityCacheSrcSourcePort_Type = CiscoPort
_CCasaAffinityCacheSrcSourcePort_Object = MibTableColumn
cCasaAffinityCacheSrcSourcePort = _CCasaAffinityCacheSrcSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 3),
    _CCasaAffinityCacheSrcSourcePort_Type()
)
cCasaAffinityCacheSrcSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcSourcePort.setStatus("current")
_CCasaAffinityCacheSrcDestAddr_Type = IpAddress
_CCasaAffinityCacheSrcDestAddr_Object = MibTableColumn
cCasaAffinityCacheSrcDestAddr = _CCasaAffinityCacheSrcDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 4),
    _CCasaAffinityCacheSrcDestAddr_Type()
)
cCasaAffinityCacheSrcDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcDestAddr.setStatus("current")
_CCasaAffinityCacheSrcDestPort_Type = CiscoPort
_CCasaAffinityCacheSrcDestPort_Object = MibTableColumn
cCasaAffinityCacheSrcDestPort = _CCasaAffinityCacheSrcDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 5),
    _CCasaAffinityCacheSrcDestPort_Type()
)
cCasaAffinityCacheSrcDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcDestPort.setStatus("current")
_CCasaAffinityCacheSrcProtocol_Type = CiscoIpProtocol
_CCasaAffinityCacheSrcProtocol_Object = MibTableColumn
cCasaAffinityCacheSrcProtocol = _CCasaAffinityCacheSrcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 6),
    _CCasaAffinityCacheSrcProtocol_Type()
)
cCasaAffinityCacheSrcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcProtocol.setStatus("current")
_CCasaAffinityCacheSrcDispAddr_Type = IpAddress
_CCasaAffinityCacheSrcDispAddr_Object = MibTableColumn
cCasaAffinityCacheSrcDispAddr = _CCasaAffinityCacheSrcDispAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 1, 1, 7),
    _CCasaAffinityCacheSrcDispAddr_Type()
)
cCasaAffinityCacheSrcDispAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheSrcDispAddr.setStatus("current")
_CCasaAffinityCacheDestTable_Object = MibTable
cCasaAffinityCacheDestTable = _CCasaAffinityCacheDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestTable.setStatus("current")
_CCasaAffinityCacheDestEntry_Object = MibTableRow
cCasaAffinityCacheDestEntry = _CCasaAffinityCacheDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1)
)
cCasaAffinityCacheDestEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
    (0, "CISCO-CASA-MIB", "cCasaAffinityCacheDestDestAddr"),
    (0, "CISCO-CASA-MIB", "cCasaAffinityCacheDestIndex"),
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestEntry.setStatus("current")
_CCasaAffinityCacheDestDestAddr_Type = IpAddress
_CCasaAffinityCacheDestDestAddr_Object = MibTableColumn
cCasaAffinityCacheDestDestAddr = _CCasaAffinityCacheDestDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 1),
    _CCasaAffinityCacheDestDestAddr_Type()
)
cCasaAffinityCacheDestDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestDestAddr.setStatus("current")
_CCasaAffinityCacheDestIndex_Type = CasaFixedAffinityIndex
_CCasaAffinityCacheDestIndex_Object = MibTableColumn
cCasaAffinityCacheDestIndex = _CCasaAffinityCacheDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 2),
    _CCasaAffinityCacheDestIndex_Type()
)
cCasaAffinityCacheDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestIndex.setStatus("current")
_CCasaAffinityCacheDestDestPort_Type = CiscoPort
_CCasaAffinityCacheDestDestPort_Object = MibTableColumn
cCasaAffinityCacheDestDestPort = _CCasaAffinityCacheDestDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 3),
    _CCasaAffinityCacheDestDestPort_Type()
)
cCasaAffinityCacheDestDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestDestPort.setStatus("current")
_CCasaAffinityCacheDestSourceAddr_Type = IpAddress
_CCasaAffinityCacheDestSourceAddr_Object = MibTableColumn
cCasaAffinityCacheDestSourceAddr = _CCasaAffinityCacheDestSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 4),
    _CCasaAffinityCacheDestSourceAddr_Type()
)
cCasaAffinityCacheDestSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestSourceAddr.setStatus("current")
_CCasaAffinityCacheDestSourcePort_Type = CiscoPort
_CCasaAffinityCacheDestSourcePort_Object = MibTableColumn
cCasaAffinityCacheDestSourcePort = _CCasaAffinityCacheDestSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 5),
    _CCasaAffinityCacheDestSourcePort_Type()
)
cCasaAffinityCacheDestSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestSourcePort.setStatus("current")
_CCasaAffinityCacheDestProtocol_Type = CiscoIpProtocol
_CCasaAffinityCacheDestProtocol_Object = MibTableColumn
cCasaAffinityCacheDestProtocol = _CCasaAffinityCacheDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 6),
    _CCasaAffinityCacheDestProtocol_Type()
)
cCasaAffinityCacheDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestProtocol.setStatus("current")
_CCasaAffinityCacheDestDispAddr_Type = IpAddress
_CCasaAffinityCacheDestDispAddr_Object = MibTableColumn
cCasaAffinityCacheDestDispAddr = _CCasaAffinityCacheDestDispAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 2, 1, 7),
    _CCasaAffinityCacheDestDispAddr_Type()
)
cCasaAffinityCacheDestDispAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDestDispAddr.setStatus("current")
_CCasaAffinityCacheDispatchTable_Object = MibTable
cCasaAffinityCacheDispatchTable = _CCasaAffinityCacheDispatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispatchTable.setStatus("current")
_CCasaAffinityCacheDispatchEntry_Object = MibTableRow
cCasaAffinityCacheDispatchEntry = _CCasaAffinityCacheDispatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1)
)
cCasaAffinityCacheDispatchEntry.setIndexNames(
    (0, "CISCO-CASA-MIB", "cCasaEntity"),
    (0, "CISCO-CASA-MIB", "cCasaAffinityCacheDispDispAddr"),
    (0, "CISCO-CASA-MIB", "cCasaAffinityCacheDispatchIndex"),
)
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispatchEntry.setStatus("current")
_CCasaAffinityCacheDispDispAddr_Type = IpAddress
_CCasaAffinityCacheDispDispAddr_Object = MibTableColumn
cCasaAffinityCacheDispDispAddr = _CCasaAffinityCacheDispDispAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 1),
    _CCasaAffinityCacheDispDispAddr_Type()
)
cCasaAffinityCacheDispDispAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispDispAddr.setStatus("current")
_CCasaAffinityCacheDispatchIndex_Type = CasaFixedAffinityIndex
_CCasaAffinityCacheDispatchIndex_Object = MibTableColumn
cCasaAffinityCacheDispatchIndex = _CCasaAffinityCacheDispatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 2),
    _CCasaAffinityCacheDispatchIndex_Type()
)
cCasaAffinityCacheDispatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispatchIndex.setStatus("current")
_CCasaAffinityCacheDispDestAddr_Type = IpAddress
_CCasaAffinityCacheDispDestAddr_Object = MibTableColumn
cCasaAffinityCacheDispDestAddr = _CCasaAffinityCacheDispDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 3),
    _CCasaAffinityCacheDispDestAddr_Type()
)
cCasaAffinityCacheDispDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispDestAddr.setStatus("current")
_CCasaAffinityCacheDispDestPort_Type = CiscoPort
_CCasaAffinityCacheDispDestPort_Object = MibTableColumn
cCasaAffinityCacheDispDestPort = _CCasaAffinityCacheDispDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 4),
    _CCasaAffinityCacheDispDestPort_Type()
)
cCasaAffinityCacheDispDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispDestPort.setStatus("current")
_CCasaAffinityCacheDispSourceAddr_Type = IpAddress
_CCasaAffinityCacheDispSourceAddr_Object = MibTableColumn
cCasaAffinityCacheDispSourceAddr = _CCasaAffinityCacheDispSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 5),
    _CCasaAffinityCacheDispSourceAddr_Type()
)
cCasaAffinityCacheDispSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispSourceAddr.setStatus("current")
_CCasaAffinityCacheDispSourcePort_Type = CiscoPort
_CCasaAffinityCacheDispSourcePort_Object = MibTableColumn
cCasaAffinityCacheDispSourcePort = _CCasaAffinityCacheDispSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 6),
    _CCasaAffinityCacheDispSourcePort_Type()
)
cCasaAffinityCacheDispSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispSourcePort.setStatus("current")
_CCasaAffinityCacheDispProtocol_Type = CiscoIpProtocol
_CCasaAffinityCacheDispProtocol_Object = MibTableColumn
cCasaAffinityCacheDispProtocol = _CCasaAffinityCacheDispProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 1, 4, 3, 1, 7),
    _CCasaAffinityCacheDispProtocol_Type()
)
cCasaAffinityCacheDispProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCasaAffinityCacheDispProtocol.setStatus("current")
_CiscoCasaMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoCasaMIBNotificationPrefix = _CiscoCasaMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 2)
)
_CiscoCasaMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoCasaMIBNotifications = _CiscoCasaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 2, 0)
)
_CiscoCasaMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCasaMIBConformance = _CiscoCasaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3)
)
_CiscoCasaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCasaMIBCompliances = _CiscoCasaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 1)
)
_CiscoCasaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCasaMIBGroups = _CiscoCasaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2)
)

# Managed Objects groups

ciscoCasaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2, 1)
)
ciscoCasaGroup.setObjects(
      *(("CISCO-CASA-MIB", "cCasaState"),
        ("CISCO-CASA-MIB", "cCasaStateNotificationEnabled"),
        ("CISCO-CASA-MIB", "cCasaCfgAddress"),
        ("CISCO-CASA-MIB", "cCasaCfgMcastAddress"),
        ("CISCO-CASA-MIB", "cCasaAddress"),
        ("CISCO-CASA-MIB", "cCasaMcastAddress"))
)
if mibBuilder.loadTexts:
    ciscoCasaGroup.setStatus("current")

ciscoCasaAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2, 2)
)
ciscoCasaAdminGroup.setObjects(
      *(("CISCO-CASA-MIB", "cCasaAdminMcastPasswd"),
        ("CISCO-CASA-MIB", "cCasaAdminMcastPasswdTimeout"),
        ("CISCO-CASA-MIB", "cCasaAdminMcastPasswdFailures"),
        ("CISCO-CASA-MIB", "cCasaAdminRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoCasaAdminGroup.setStatus("current")

ciscoCasaAffinityCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2, 3)
)
ciscoCasaAffinityCacheGroup.setObjects(
      *(("CISCO-CASA-MIB", "cCasaAffinityCacheNumOf"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheHiWtrMrk"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheHiWtrMrkReset"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheNoStorageDrops"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheHits"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheHCHits"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheMisses"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheHCMisses"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheIntrTimeouts"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheSrcSourcePort"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheSrcDestAddr"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheSrcDestPort"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheSrcProtocol"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheSrcDispAddr"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDestDestPort"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDestSourceAddr"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDestSourcePort"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDestProtocol"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDestDispAddr"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDispDestAddr"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDispDestPort"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDispSourceAddr"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDispSourcePort"),
        ("CISCO-CASA-MIB", "cCasaAffinityCacheDispProtocol"))
)
if mibBuilder.loadTexts:
    ciscoCasaAffinityCacheGroup.setStatus("current")

ciscoCasaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2, 4)
)
ciscoCasaStatsGroup.setObjects(
      *(("CISCO-CASA-MIB", "cCasaInterestPackets"),
        ("CISCO-CASA-MIB", "cCasaInterestTickles"))
)
if mibBuilder.loadTexts:
    ciscoCasaStatsGroup.setStatus("current")

ciscoCasaObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2, 5)
)
ciscoCasaObsoleteGroup.setObjects(
      *(("CISCO-CASA-MIB", "cCasaCfgAddressMask"),
        ("CISCO-CASA-MIB", "cCasaAddressMask"))
)
if mibBuilder.loadTexts:
    ciscoCasaObsoleteGroup.setStatus("obsolete")


# Notification objects

ciscoCasaStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 2, 1)
)
ciscoCasaStateChange.setObjects(
    ("CISCO-CASA-MIB", "cCasaState")
)
if mibBuilder.loadTexts:
    ciscoCasaStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoCasaNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 2, 6)
)
ciscoCasaNotifGroup.setObjects(
    ("CISCO-CASA-MIB", "ciscoCasaStateChange")
)
if mibBuilder.loadTexts:
    ciscoCasaNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCasaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 122, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCasaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CASA-MIB",
    **{"CasaFixedAffinityIndex": CasaFixedAffinityIndex,
       "ciscoCasaMIB": ciscoCasaMIB,
       "ciscoCasaMIBObjects": ciscoCasaMIBObjects,
       "cCasaGlobal": cCasaGlobal,
       "cCasaTable": cCasaTable,
       "cCasaEntry": cCasaEntry,
       "cCasaEntity": cCasaEntity,
       "cCasaState": cCasaState,
       "cCasaStateNotificationEnabled": cCasaStateNotificationEnabled,
       "cCasaCfgAddress": cCasaCfgAddress,
       "cCasaCfgAddressMask": cCasaCfgAddressMask,
       "cCasaCfgMcastAddress": cCasaCfgMcastAddress,
       "cCasaAddress": cCasaAddress,
       "cCasaAddressMask": cCasaAddressMask,
       "cCasaMcastAddress": cCasaMcastAddress,
       "cCasaStats": cCasaStats,
       "cCasaAffinityCacheStatsTable": cCasaAffinityCacheStatsTable,
       "cCasaAffinityCacheStatsEntry": cCasaAffinityCacheStatsEntry,
       "cCasaAffinityCacheNumOf": cCasaAffinityCacheNumOf,
       "cCasaAffinityCacheHiWtrMrk": cCasaAffinityCacheHiWtrMrk,
       "cCasaAffinityCacheHiWtrMrkReset": cCasaAffinityCacheHiWtrMrkReset,
       "cCasaAffinityCacheNoStorageDrops": cCasaAffinityCacheNoStorageDrops,
       "cCasaAffinityCacheHits": cCasaAffinityCacheHits,
       "cCasaAffinityCacheHCHits": cCasaAffinityCacheHCHits,
       "cCasaAffinityCacheMisses": cCasaAffinityCacheMisses,
       "cCasaAffinityCacheHCMisses": cCasaAffinityCacheHCMisses,
       "cCasaAffinityCacheIntrTimeouts": cCasaAffinityCacheIntrTimeouts,
       "cCasaStatsTable": cCasaStatsTable,
       "cCasaStatsEntry": cCasaStatsEntry,
       "cCasaInterestPackets": cCasaInterestPackets,
       "cCasaInterestTickles": cCasaInterestTickles,
       "cCasaAdmin": cCasaAdmin,
       "cCasaAdminTable": cCasaAdminTable,
       "cCasaAdminEntry": cCasaAdminEntry,
       "cCasaAdminMcastPort": cCasaAdminMcastPort,
       "cCasaAdminMcastPasswd": cCasaAdminMcastPasswd,
       "cCasaAdminMcastPasswdTimeout": cCasaAdminMcastPasswdTimeout,
       "cCasaAdminMcastPasswdFailures": cCasaAdminMcastPasswdFailures,
       "cCasaAdminRowStatus": cCasaAdminRowStatus,
       "cCasaAffinityCache": cCasaAffinityCache,
       "cCasaAffinityCacheSrcTable": cCasaAffinityCacheSrcTable,
       "cCasaAffinityCacheSrcEntry": cCasaAffinityCacheSrcEntry,
       "cCasaAffinityCacheSrcSourceAddr": cCasaAffinityCacheSrcSourceAddr,
       "cCasaAffinityCacheSrcIndex": cCasaAffinityCacheSrcIndex,
       "cCasaAffinityCacheSrcSourcePort": cCasaAffinityCacheSrcSourcePort,
       "cCasaAffinityCacheSrcDestAddr": cCasaAffinityCacheSrcDestAddr,
       "cCasaAffinityCacheSrcDestPort": cCasaAffinityCacheSrcDestPort,
       "cCasaAffinityCacheSrcProtocol": cCasaAffinityCacheSrcProtocol,
       "cCasaAffinityCacheSrcDispAddr": cCasaAffinityCacheSrcDispAddr,
       "cCasaAffinityCacheDestTable": cCasaAffinityCacheDestTable,
       "cCasaAffinityCacheDestEntry": cCasaAffinityCacheDestEntry,
       "cCasaAffinityCacheDestDestAddr": cCasaAffinityCacheDestDestAddr,
       "cCasaAffinityCacheDestIndex": cCasaAffinityCacheDestIndex,
       "cCasaAffinityCacheDestDestPort": cCasaAffinityCacheDestDestPort,
       "cCasaAffinityCacheDestSourceAddr": cCasaAffinityCacheDestSourceAddr,
       "cCasaAffinityCacheDestSourcePort": cCasaAffinityCacheDestSourcePort,
       "cCasaAffinityCacheDestProtocol": cCasaAffinityCacheDestProtocol,
       "cCasaAffinityCacheDestDispAddr": cCasaAffinityCacheDestDispAddr,
       "cCasaAffinityCacheDispatchTable": cCasaAffinityCacheDispatchTable,
       "cCasaAffinityCacheDispatchEntry": cCasaAffinityCacheDispatchEntry,
       "cCasaAffinityCacheDispDispAddr": cCasaAffinityCacheDispDispAddr,
       "cCasaAffinityCacheDispatchIndex": cCasaAffinityCacheDispatchIndex,
       "cCasaAffinityCacheDispDestAddr": cCasaAffinityCacheDispDestAddr,
       "cCasaAffinityCacheDispDestPort": cCasaAffinityCacheDispDestPort,
       "cCasaAffinityCacheDispSourceAddr": cCasaAffinityCacheDispSourceAddr,
       "cCasaAffinityCacheDispSourcePort": cCasaAffinityCacheDispSourcePort,
       "cCasaAffinityCacheDispProtocol": cCasaAffinityCacheDispProtocol,
       "ciscoCasaMIBNotificationPrefix": ciscoCasaMIBNotificationPrefix,
       "ciscoCasaMIBNotifications": ciscoCasaMIBNotifications,
       "ciscoCasaStateChange": ciscoCasaStateChange,
       "ciscoCasaMIBConformance": ciscoCasaMIBConformance,
       "ciscoCasaMIBCompliances": ciscoCasaMIBCompliances,
       "ciscoCasaMIBCompliance": ciscoCasaMIBCompliance,
       "ciscoCasaMIBGroups": ciscoCasaMIBGroups,
       "ciscoCasaGroup": ciscoCasaGroup,
       "ciscoCasaAdminGroup": ciscoCasaAdminGroup,
       "ciscoCasaAffinityCacheGroup": ciscoCasaAffinityCacheGroup,
       "ciscoCasaStatsGroup": ciscoCasaStatsGroup,
       "ciscoCasaObsoleteGroup": ciscoCasaObsoleteGroup,
       "ciscoCasaNotifGroup": ciscoCasaNotifGroup}
)
