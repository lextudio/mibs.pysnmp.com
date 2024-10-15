# SNMP MIB module (CISCO-IETF-FRR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-FRR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:33 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(MplsBitRate,
 MplsLsrIdentifier,
 MplsTunnelAffinity,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate",
    "MplsLsrIdentifier",
    "MplsTunnelAffinity",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

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

cmplsFrrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98)
)
cmplsFrrMIB.setRevisions(
        ("2008-04-29 12:00",
         "2002-11-05 12:00",
         "2002-11-01 12:00",
         "2002-03-22 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsFrrDetourIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CmplsFrrNotif_ObjectIdentity = ObjectIdentity
cmplsFrrNotif = _CmplsFrrNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 0)
)
_CmplsFrrScalars_ObjectIdentity = ObjectIdentity
cmplsFrrScalars = _CmplsFrrScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1)
)


class _CmplsFrrDetourIncoming_Type(Unsigned32):
    """Custom type cmplsFrrDetourIncoming based on Unsigned32"""
    defaultValue = 0


_CmplsFrrDetourIncoming_Object = MibScalar
cmplsFrrDetourIncoming = _CmplsFrrDetourIncoming_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 1),
    _CmplsFrrDetourIncoming_Type()
)
cmplsFrrDetourIncoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrDetourIncoming.setStatus("current")


class _CmplsFrrDetourOutgoing_Type(Unsigned32):
    """Custom type cmplsFrrDetourOutgoing based on Unsigned32"""
    defaultValue = 0


_CmplsFrrDetourOutgoing_Object = MibScalar
cmplsFrrDetourOutgoing = _CmplsFrrDetourOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 2),
    _CmplsFrrDetourOutgoing_Type()
)
cmplsFrrDetourOutgoing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrDetourOutgoing.setStatus("current")


class _CmplsFrrDetourOriginating_Type(Unsigned32):
    """Custom type cmplsFrrDetourOriginating based on Unsigned32"""
    defaultValue = 0


_CmplsFrrDetourOriginating_Object = MibScalar
cmplsFrrDetourOriginating = _CmplsFrrDetourOriginating_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 3),
    _CmplsFrrDetourOriginating_Type()
)
cmplsFrrDetourOriginating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrDetourOriginating.setStatus("current")


class _CmplsFrrSwitchover_Type(Unsigned32):
    """Custom type cmplsFrrSwitchover based on Unsigned32"""
    defaultValue = 0


_CmplsFrrSwitchover_Object = MibScalar
cmplsFrrSwitchover = _CmplsFrrSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 4),
    _CmplsFrrSwitchover_Type()
)
cmplsFrrSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrSwitchover.setStatus("current")


class _CmplsFrrNumOfConfIfs_Type(Unsigned32):
    """Custom type cmplsFrrNumOfConfIfs based on Unsigned32"""
    defaultValue = 0


_CmplsFrrNumOfConfIfs_Object = MibScalar
cmplsFrrNumOfConfIfs = _CmplsFrrNumOfConfIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 5),
    _CmplsFrrNumOfConfIfs_Type()
)
cmplsFrrNumOfConfIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrNumOfConfIfs.setStatus("current")


class _CmplsFrrActProtectedIfs_Type(Unsigned32):
    """Custom type cmplsFrrActProtectedIfs based on Unsigned32"""
    defaultValue = 0


_CmplsFrrActProtectedIfs_Object = MibScalar
cmplsFrrActProtectedIfs = _CmplsFrrActProtectedIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 6),
    _CmplsFrrActProtectedIfs_Type()
)
cmplsFrrActProtectedIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrActProtectedIfs.setStatus("current")


class _CmplsFrrConfProtectingTuns_Type(Unsigned32):
    """Custom type cmplsFrrConfProtectingTuns based on Unsigned32"""
    defaultValue = 0


_CmplsFrrConfProtectingTuns_Object = MibScalar
cmplsFrrConfProtectingTuns = _CmplsFrrConfProtectingTuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 7),
    _CmplsFrrConfProtectingTuns_Type()
)
cmplsFrrConfProtectingTuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrConfProtectingTuns.setStatus("current")


class _CmplsFrrActProtectedTuns_Type(Unsigned32):
    """Custom type cmplsFrrActProtectedTuns based on Unsigned32"""
    defaultValue = 0


_CmplsFrrActProtectedTuns_Object = MibScalar
cmplsFrrActProtectedTuns = _CmplsFrrActProtectedTuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 8),
    _CmplsFrrActProtectedTuns_Type()
)
cmplsFrrActProtectedTuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrActProtectedTuns.setStatus("current")


class _CmplsFrrActProtectedLSPs_Type(Unsigned32):
    """Custom type cmplsFrrActProtectedLSPs based on Unsigned32"""
    defaultValue = 0


_CmplsFrrActProtectedLSPs_Object = MibScalar
cmplsFrrActProtectedLSPs = _CmplsFrrActProtectedLSPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 9),
    _CmplsFrrActProtectedLSPs_Type()
)
cmplsFrrActProtectedLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrActProtectedLSPs.setStatus("current")


class _CmplsFrrConstProtectionMethod_Type(Integer32):
    """Custom type cmplsFrrConstProtectionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("facilityBackup", 1),
          ("oneToOneBackup", 0))
    )


_CmplsFrrConstProtectionMethod_Type.__name__ = "Integer32"
_CmplsFrrConstProtectionMethod_Object = MibScalar
cmplsFrrConstProtectionMethod = _CmplsFrrConstProtectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 10),
    _CmplsFrrConstProtectionMethod_Type()
)
cmplsFrrConstProtectionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsFrrConstProtectionMethod.setStatus("current")


class _CmplsFrrNotifsEnabled_Type(TruthValue):
    """Custom type cmplsFrrNotifsEnabled based on TruthValue"""


_CmplsFrrNotifsEnabled_Object = MibScalar
cmplsFrrNotifsEnabled = _CmplsFrrNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 11),
    _CmplsFrrNotifsEnabled_Type()
)
cmplsFrrNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsFrrNotifsEnabled.setStatus("current")


class _CmplsFrrLogTableMaxEntries_Type(Unsigned32):
    """Custom type cmplsFrrLogTableMaxEntries based on Unsigned32"""
    defaultValue = 0


_CmplsFrrLogTableMaxEntries_Object = MibScalar
cmplsFrrLogTableMaxEntries = _CmplsFrrLogTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 12),
    _CmplsFrrLogTableMaxEntries_Type()
)
cmplsFrrLogTableMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsFrrLogTableMaxEntries.setStatus("current")
_CmplsFrrLogTableCurrEntries_Type = Counter32
_CmplsFrrLogTableCurrEntries_Object = MibScalar
cmplsFrrLogTableCurrEntries = _CmplsFrrLogTableCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 13),
    _CmplsFrrLogTableCurrEntries_Type()
)
cmplsFrrLogTableCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrLogTableCurrEntries.setStatus("current")


class _CmplsFrrNotifMaxRate_Type(Unsigned32):
    """Custom type cmplsFrrNotifMaxRate based on Unsigned32"""
    defaultValue = 0


_CmplsFrrNotifMaxRate_Object = MibScalar
cmplsFrrNotifMaxRate = _CmplsFrrNotifMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 1, 14),
    _CmplsFrrNotifMaxRate_Type()
)
cmplsFrrNotifMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsFrrNotifMaxRate.setStatus("current")
_CmplsFrrObjects_ObjectIdentity = ObjectIdentity
cmplsFrrObjects = _CmplsFrrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2)
)
_CmplsFrrGeneralObjects_ObjectIdentity = ObjectIdentity
cmplsFrrGeneralObjects = _CmplsFrrGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1)
)
_CmplsFrrConstTable_Object = MibTable
cmplsFrrConstTable = _CmplsFrrConstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmplsFrrConstTable.setStatus("current")
_CmplsFrrConstEntry_Object = MibTableRow
cmplsFrrConstEntry = _CmplsFrrConstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1)
)
cmplsFrrConstEntry.setIndexNames(
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrConstIfIndex"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrConstTunnelIndex"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrConstTunnelInstance"),
)
if mibBuilder.loadTexts:
    cmplsFrrConstEntry.setStatus("current")
_CmplsFrrConstIfIndex_Type = InterfaceIndexOrZero
_CmplsFrrConstIfIndex_Object = MibTableColumn
cmplsFrrConstIfIndex = _CmplsFrrConstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 1),
    _CmplsFrrConstIfIndex_Type()
)
cmplsFrrConstIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrConstIfIndex.setStatus("current")
_CmplsFrrConstTunnelIndex_Type = MplsTunnelIndex
_CmplsFrrConstTunnelIndex_Object = MibTableColumn
cmplsFrrConstTunnelIndex = _CmplsFrrConstTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 2),
    _CmplsFrrConstTunnelIndex_Type()
)
cmplsFrrConstTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrConstTunnelIndex.setStatus("current")
_CmplsFrrConstTunnelInstance_Type = MplsTunnelInstanceIndex
_CmplsFrrConstTunnelInstance_Object = MibTableColumn
cmplsFrrConstTunnelInstance = _CmplsFrrConstTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 3),
    _CmplsFrrConstTunnelInstance_Type()
)
cmplsFrrConstTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrConstTunnelInstance.setStatus("current")


class _CmplsFrrConstSetupPrio_Type(Unsigned32):
    """Custom type cmplsFrrConstSetupPrio based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmplsFrrConstSetupPrio_Type.__name__ = "Unsigned32"
_CmplsFrrConstSetupPrio_Object = MibTableColumn
cmplsFrrConstSetupPrio = _CmplsFrrConstSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 4),
    _CmplsFrrConstSetupPrio_Type()
)
cmplsFrrConstSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstSetupPrio.setStatus("current")


class _CmplsFrrConstHoldingPrio_Type(Unsigned32):
    """Custom type cmplsFrrConstHoldingPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CmplsFrrConstHoldingPrio_Type.__name__ = "Unsigned32"
_CmplsFrrConstHoldingPrio_Object = MibTableColumn
cmplsFrrConstHoldingPrio = _CmplsFrrConstHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 5),
    _CmplsFrrConstHoldingPrio_Type()
)
cmplsFrrConstHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstHoldingPrio.setStatus("current")


class _CmplsFrrConstInclAnyAffinity_Type(MplsTunnelAffinity):
    """Custom type cmplsFrrConstInclAnyAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_CmplsFrrConstInclAnyAffinity_Object = MibTableColumn
cmplsFrrConstInclAnyAffinity = _CmplsFrrConstInclAnyAffinity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 6),
    _CmplsFrrConstInclAnyAffinity_Type()
)
cmplsFrrConstInclAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstInclAnyAffinity.setStatus("current")


class _CmplsFrrConstInclAllAffinity_Type(MplsTunnelAffinity):
    """Custom type cmplsFrrConstInclAllAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_CmplsFrrConstInclAllAffinity_Object = MibTableColumn
cmplsFrrConstInclAllAffinity = _CmplsFrrConstInclAllAffinity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 7),
    _CmplsFrrConstInclAllAffinity_Type()
)
cmplsFrrConstInclAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstInclAllAffinity.setStatus("current")


class _CmplsFrrConstExclAllAffinity_Type(MplsTunnelAffinity):
    """Custom type cmplsFrrConstExclAllAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_CmplsFrrConstExclAllAffinity_Object = MibTableColumn
cmplsFrrConstExclAllAffinity = _CmplsFrrConstExclAllAffinity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 8),
    _CmplsFrrConstExclAllAffinity_Type()
)
cmplsFrrConstExclAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstExclAllAffinity.setStatus("current")


class _CmplsFrrConstHopLimit_Type(Unsigned32):
    """Custom type cmplsFrrConstHopLimit based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmplsFrrConstHopLimit_Type.__name__ = "Unsigned32"
_CmplsFrrConstHopLimit_Object = MibTableColumn
cmplsFrrConstHopLimit = _CmplsFrrConstHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 9),
    _CmplsFrrConstHopLimit_Type()
)
cmplsFrrConstHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstHopLimit.setStatus("current")


class _CmplsFrrConstBandwidth_Type(MplsBitRate):
    """Custom type cmplsFrrConstBandwidth based on MplsBitRate"""
    defaultValue = 1


_CmplsFrrConstBandwidth_Object = MibTableColumn
cmplsFrrConstBandwidth = _CmplsFrrConstBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 10),
    _CmplsFrrConstBandwidth_Type()
)
cmplsFrrConstBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstBandwidth.setStatus("current")
_CmplsFrrConstRowStatus_Type = RowStatus
_CmplsFrrConstRowStatus_Object = MibTableColumn
cmplsFrrConstRowStatus = _CmplsFrrConstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 11),
    _CmplsFrrConstRowStatus_Type()
)
cmplsFrrConstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrConstRowStatus.setStatus("current")
_CmplsFrrConstNumProtectingTunOnIf_Type = Gauge32
_CmplsFrrConstNumProtectingTunOnIf_Object = MibTableColumn
cmplsFrrConstNumProtectingTunOnIf = _CmplsFrrConstNumProtectingTunOnIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 12),
    _CmplsFrrConstNumProtectingTunOnIf_Type()
)
cmplsFrrConstNumProtectingTunOnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrConstNumProtectingTunOnIf.setStatus("current")
_CmplsFrrConstNumProtectedTunOnIf_Type = Gauge32
_CmplsFrrConstNumProtectedTunOnIf_Object = MibTableColumn
cmplsFrrConstNumProtectedTunOnIf = _CmplsFrrConstNumProtectedTunOnIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 1, 1, 13),
    _CmplsFrrConstNumProtectedTunOnIf_Type()
)
cmplsFrrConstNumProtectedTunOnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrConstNumProtectedTunOnIf.setStatus("current")
_CmplsFrrLogTable_Object = MibTable
cmplsFrrLogTable = _CmplsFrrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cmplsFrrLogTable.setStatus("current")
_CmplsFrrLogEntry_Object = MibTableRow
cmplsFrrLogEntry = _CmplsFrrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1)
)
cmplsFrrLogEntry.setIndexNames(
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrLogIndex"),
)
if mibBuilder.loadTexts:
    cmplsFrrLogEntry.setStatus("current")
_CmplsFrrLogIndex_Type = Unsigned32
_CmplsFrrLogIndex_Object = MibTableColumn
cmplsFrrLogIndex = _CmplsFrrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 1),
    _CmplsFrrLogIndex_Type()
)
cmplsFrrLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrLogIndex.setStatus("current")
_CmplsFrrLogEventTime_Type = TimeStamp
_CmplsFrrLogEventTime_Object = MibTableColumn
cmplsFrrLogEventTime = _CmplsFrrLogEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 2),
    _CmplsFrrLogEventTime_Type()
)
cmplsFrrLogEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrLogEventTime.setStatus("current")
_CmplsFrrLogInterface_Type = InterfaceIndexOrZero
_CmplsFrrLogInterface_Object = MibTableColumn
cmplsFrrLogInterface = _CmplsFrrLogInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 3),
    _CmplsFrrLogInterface_Type()
)
cmplsFrrLogInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrLogInterface.setStatus("current")


class _CmplsFrrLogEventType_Type(Integer32):
    """Custom type cmplsFrrLogEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("protected", 2))
    )


_CmplsFrrLogEventType_Type.__name__ = "Integer32"
_CmplsFrrLogEventType_Object = MibTableColumn
cmplsFrrLogEventType = _CmplsFrrLogEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 4),
    _CmplsFrrLogEventType_Type()
)
cmplsFrrLogEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrLogEventType.setStatus("current")
_CmplsFrrLogEventDuration_Type = TimeTicks
_CmplsFrrLogEventDuration_Object = MibTableColumn
cmplsFrrLogEventDuration = _CmplsFrrLogEventDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 5),
    _CmplsFrrLogEventDuration_Type()
)
cmplsFrrLogEventDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrLogEventDuration.setStatus("current")


class _CmplsFrrLogEventReasonString_Type(OctetString):
    """Custom type cmplsFrrLogEventReasonString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_CmplsFrrLogEventReasonString_Type.__name__ = "OctetString"
_CmplsFrrLogEventReasonString_Object = MibTableColumn
cmplsFrrLogEventReasonString = _CmplsFrrLogEventReasonString_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 1, 2, 1, 6),
    _CmplsFrrLogEventReasonString_Type()
)
cmplsFrrLogEventReasonString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrLogEventReasonString.setStatus("current")
_CmplsFrr1to1Objects_ObjectIdentity = ObjectIdentity
cmplsFrr1to1Objects = _CmplsFrr1to1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 2)
)
_CmplsFrrFacObjects_ObjectIdentity = ObjectIdentity
cmplsFrrFacObjects = _CmplsFrrFacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3)
)
_CmplsFrrFacRouteDBTable_Object = MibTable
cmplsFrrFacRouteDBTable = _CmplsFrrFacRouteDBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cmplsFrrFacRouteDBTable.setStatus("current")
_CmplsFrrFacRouteDBEntry_Object = MibTableRow
cmplsFrrFacRouteDBEntry = _CmplsFrrFacRouteDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1)
)
cmplsFrrFacRouteDBEntry.setIndexNames(
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedIfIndex"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectingTunIndex"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunIndex"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunInstance"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunIngressLSRId"),
    (0, "CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsFrrFacRouteDBEntry.setStatus("current")
_CmplsFrrFacRouteProtectedIfIndex_Type = InterfaceIndex
_CmplsFrrFacRouteProtectedIfIndex_Object = MibTableColumn
cmplsFrrFacRouteProtectedIfIndex = _CmplsFrrFacRouteProtectedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 1),
    _CmplsFrrFacRouteProtectedIfIndex_Type()
)
cmplsFrrFacRouteProtectedIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectedIfIndex.setStatus("current")
_CmplsFrrFacRouteProtectingTunIndex_Type = MplsTunnelIndex
_CmplsFrrFacRouteProtectingTunIndex_Object = MibTableColumn
cmplsFrrFacRouteProtectingTunIndex = _CmplsFrrFacRouteProtectingTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 2),
    _CmplsFrrFacRouteProtectingTunIndex_Type()
)
cmplsFrrFacRouteProtectingTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectingTunIndex.setStatus("current")
_CmplsFrrFacRouteProtectedTunIndex_Type = MplsTunnelIndex
_CmplsFrrFacRouteProtectedTunIndex_Object = MibTableColumn
cmplsFrrFacRouteProtectedTunIndex = _CmplsFrrFacRouteProtectedTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 3),
    _CmplsFrrFacRouteProtectedTunIndex_Type()
)
cmplsFrrFacRouteProtectedTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectedTunIndex.setStatus("current")
_CmplsFrrFacRouteProtectedTunInstance_Type = MplsTunnelInstanceIndex
_CmplsFrrFacRouteProtectedTunInstance_Object = MibTableColumn
cmplsFrrFacRouteProtectedTunInstance = _CmplsFrrFacRouteProtectedTunInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 4),
    _CmplsFrrFacRouteProtectedTunInstance_Type()
)
cmplsFrrFacRouteProtectedTunInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectedTunInstance.setStatus("current")
_CmplsFrrFacRouteProtectedTunIngressLSRId_Type = MplsLsrIdentifier
_CmplsFrrFacRouteProtectedTunIngressLSRId_Object = MibTableColumn
cmplsFrrFacRouteProtectedTunIngressLSRId = _CmplsFrrFacRouteProtectedTunIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 5),
    _CmplsFrrFacRouteProtectedTunIngressLSRId_Type()
)
cmplsFrrFacRouteProtectedTunIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectedTunIngressLSRId.setStatus("current")
_CmplsFrrFacRouteProtectedTunEgressLSRId_Type = MplsLsrIdentifier
_CmplsFrrFacRouteProtectedTunEgressLSRId_Object = MibTableColumn
cmplsFrrFacRouteProtectedTunEgressLSRId = _CmplsFrrFacRouteProtectedTunEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 6),
    _CmplsFrrFacRouteProtectedTunEgressLSRId_Type()
)
cmplsFrrFacRouteProtectedTunEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectedTunEgressLSRId.setStatus("current")


class _CmplsFrrFacRouteProtectedTunStatus_Type(Integer32):
    """Custom type cmplsFrrFacRouteProtectedTunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("partial", 3),
          ("ready", 2))
    )


_CmplsFrrFacRouteProtectedTunStatus_Type.__name__ = "Integer32"
_CmplsFrrFacRouteProtectedTunStatus_Object = MibTableColumn
cmplsFrrFacRouteProtectedTunStatus = _CmplsFrrFacRouteProtectedTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 7),
    _CmplsFrrFacRouteProtectedTunStatus_Type()
)
cmplsFrrFacRouteProtectedTunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectedTunStatus.setStatus("current")
_CmplsFrrFacRouteProtectingTunResvBw_Type = MplsBitRate
_CmplsFrrFacRouteProtectingTunResvBw_Object = MibTableColumn
cmplsFrrFacRouteProtectingTunResvBw = _CmplsFrrFacRouteProtectingTunResvBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 8),
    _CmplsFrrFacRouteProtectingTunResvBw_Type()
)
cmplsFrrFacRouteProtectingTunResvBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectingTunResvBw.setStatus("current")


class _CmplsFrrFacRouteProtectingTunProtectionType_Type(Integer32):
    """Custom type cmplsFrrFacRouteProtectingTunProtectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkProtection", 0),
          ("nodeProtection", 1))
    )


_CmplsFrrFacRouteProtectingTunProtectionType_Type.__name__ = "Integer32"
_CmplsFrrFacRouteProtectingTunProtectionType_Object = MibTableColumn
cmplsFrrFacRouteProtectingTunProtectionType = _CmplsFrrFacRouteProtectingTunProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 2, 3, 1, 1, 9),
    _CmplsFrrFacRouteProtectingTunProtectionType_Type()
)
cmplsFrrFacRouteProtectingTunProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmplsFrrFacRouteProtectingTunProtectionType.setStatus("current")
_CmplsFrrConformance_ObjectIdentity = ObjectIdentity
cmplsFrrConformance = _CmplsFrrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3)
)
_CmplsFrrGroups_ObjectIdentity = ObjectIdentity
cmplsFrrGroups = _CmplsFrrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1)
)
_CmplsFrrCompliances_ObjectIdentity = ObjectIdentity
cmplsFrrCompliances = _CmplsFrrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 2)
)

# Managed Objects groups

cmplsFrrScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 1)
)
cmplsFrrScalarGroup.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrDetourIncoming"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrDetourOutgoing"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrDetourOriginating"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrSwitchover"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrNumOfConfIfs"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrActProtectedIfs"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConfProtectingTuns"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrActProtectedTuns"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrActProtectedLSPs"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstProtectionMethod"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrNotifsEnabled"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrLogTableMaxEntries"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrLogTableCurrEntries"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrNotifMaxRate"))
)
if mibBuilder.loadTexts:
    cmplsFrrScalarGroup.setStatus("current")

cmplsFrrConstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 2)
)
cmplsFrrConstGroup.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrConstProtectionMethod"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstSetupPrio"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstHoldingPrio"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstInclAnyAffinity"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstInclAllAffinity"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstExclAllAffinity"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstHopLimit"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstBandwidth"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstRowStatus"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectingTunOnIf"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectedTunOnIf"))
)
if mibBuilder.loadTexts:
    cmplsFrrConstGroup.setStatus("current")

cmplsFrrLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 4)
)
cmplsFrrLogGroup.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventTime"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrLogInterface"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventType"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventDuration"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrLogEventReasonString"))
)
if mibBuilder.loadTexts:
    cmplsFrrLogGroup.setStatus("current")

cmplsFrrFacRouteDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 6)
)
cmplsFrrFacRouteDBGroup.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectedTunStatus"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectingTunResvBw"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrFacRouteProtectingTunProtectionType"))
)
if mibBuilder.loadTexts:
    cmplsFrrFacRouteDBGroup.setStatus("current")


# Notification objects

cmplsFrrProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 0, 1)
)
cmplsFrrProtected.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectingTunOnIf"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectedTunOnIf"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstBandwidth"))
)
if mibBuilder.loadTexts:
    cmplsFrrProtected.setStatus(
        "current"
    )

cmplsFrrUnProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 0, 2)
)
cmplsFrrUnProtected.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectingTunOnIf"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstNumProtectedTunOnIf"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrConstBandwidth"))
)
if mibBuilder.loadTexts:
    cmplsFrrUnProtected.setStatus(
        "current"
    )


# Notifications groups

cmplsFrrNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 7)
)
cmplsFrrNotifGroup.setObjects(
    ("CISCO-IETF-FRR-MIB", "cmplsFrrProtected")
)
if mibBuilder.loadTexts:
    cmplsFrrNotifGroup.setStatus(
        "deprecated"
    )

cmplsFrrNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 1, 8)
)
cmplsFrrNotifGroupRev1.setObjects(
      *(("CISCO-IETF-FRR-MIB", "cmplsFrrProtected"),
        ("CISCO-IETF-FRR-MIB", "cmplsFrrUnProtected"))
)
if mibBuilder.loadTexts:
    cmplsFrrNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmplsFrrModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cmplsFrrModuleCompliance.setStatus(
        "deprecated"
    )

cmplsFrrModuleComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 98, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cmplsFrrModuleComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-FRR-MIB",
    **{"MplsFrrDetourIndex": MplsFrrDetourIndex,
       "cmplsFrrMIB": cmplsFrrMIB,
       "cmplsFrrNotif": cmplsFrrNotif,
       "cmplsFrrProtected": cmplsFrrProtected,
       "cmplsFrrUnProtected": cmplsFrrUnProtected,
       "cmplsFrrScalars": cmplsFrrScalars,
       "cmplsFrrDetourIncoming": cmplsFrrDetourIncoming,
       "cmplsFrrDetourOutgoing": cmplsFrrDetourOutgoing,
       "cmplsFrrDetourOriginating": cmplsFrrDetourOriginating,
       "cmplsFrrSwitchover": cmplsFrrSwitchover,
       "cmplsFrrNumOfConfIfs": cmplsFrrNumOfConfIfs,
       "cmplsFrrActProtectedIfs": cmplsFrrActProtectedIfs,
       "cmplsFrrConfProtectingTuns": cmplsFrrConfProtectingTuns,
       "cmplsFrrActProtectedTuns": cmplsFrrActProtectedTuns,
       "cmplsFrrActProtectedLSPs": cmplsFrrActProtectedLSPs,
       "cmplsFrrConstProtectionMethod": cmplsFrrConstProtectionMethod,
       "cmplsFrrNotifsEnabled": cmplsFrrNotifsEnabled,
       "cmplsFrrLogTableMaxEntries": cmplsFrrLogTableMaxEntries,
       "cmplsFrrLogTableCurrEntries": cmplsFrrLogTableCurrEntries,
       "cmplsFrrNotifMaxRate": cmplsFrrNotifMaxRate,
       "cmplsFrrObjects": cmplsFrrObjects,
       "cmplsFrrGeneralObjects": cmplsFrrGeneralObjects,
       "cmplsFrrConstTable": cmplsFrrConstTable,
       "cmplsFrrConstEntry": cmplsFrrConstEntry,
       "cmplsFrrConstIfIndex": cmplsFrrConstIfIndex,
       "cmplsFrrConstTunnelIndex": cmplsFrrConstTunnelIndex,
       "cmplsFrrConstTunnelInstance": cmplsFrrConstTunnelInstance,
       "cmplsFrrConstSetupPrio": cmplsFrrConstSetupPrio,
       "cmplsFrrConstHoldingPrio": cmplsFrrConstHoldingPrio,
       "cmplsFrrConstInclAnyAffinity": cmplsFrrConstInclAnyAffinity,
       "cmplsFrrConstInclAllAffinity": cmplsFrrConstInclAllAffinity,
       "cmplsFrrConstExclAllAffinity": cmplsFrrConstExclAllAffinity,
       "cmplsFrrConstHopLimit": cmplsFrrConstHopLimit,
       "cmplsFrrConstBandwidth": cmplsFrrConstBandwidth,
       "cmplsFrrConstRowStatus": cmplsFrrConstRowStatus,
       "cmplsFrrConstNumProtectingTunOnIf": cmplsFrrConstNumProtectingTunOnIf,
       "cmplsFrrConstNumProtectedTunOnIf": cmplsFrrConstNumProtectedTunOnIf,
       "cmplsFrrLogTable": cmplsFrrLogTable,
       "cmplsFrrLogEntry": cmplsFrrLogEntry,
       "cmplsFrrLogIndex": cmplsFrrLogIndex,
       "cmplsFrrLogEventTime": cmplsFrrLogEventTime,
       "cmplsFrrLogInterface": cmplsFrrLogInterface,
       "cmplsFrrLogEventType": cmplsFrrLogEventType,
       "cmplsFrrLogEventDuration": cmplsFrrLogEventDuration,
       "cmplsFrrLogEventReasonString": cmplsFrrLogEventReasonString,
       "cmplsFrr1to1Objects": cmplsFrr1to1Objects,
       "cmplsFrrFacObjects": cmplsFrrFacObjects,
       "cmplsFrrFacRouteDBTable": cmplsFrrFacRouteDBTable,
       "cmplsFrrFacRouteDBEntry": cmplsFrrFacRouteDBEntry,
       "cmplsFrrFacRouteProtectedIfIndex": cmplsFrrFacRouteProtectedIfIndex,
       "cmplsFrrFacRouteProtectingTunIndex": cmplsFrrFacRouteProtectingTunIndex,
       "cmplsFrrFacRouteProtectedTunIndex": cmplsFrrFacRouteProtectedTunIndex,
       "cmplsFrrFacRouteProtectedTunInstance": cmplsFrrFacRouteProtectedTunInstance,
       "cmplsFrrFacRouteProtectedTunIngressLSRId": cmplsFrrFacRouteProtectedTunIngressLSRId,
       "cmplsFrrFacRouteProtectedTunEgressLSRId": cmplsFrrFacRouteProtectedTunEgressLSRId,
       "cmplsFrrFacRouteProtectedTunStatus": cmplsFrrFacRouteProtectedTunStatus,
       "cmplsFrrFacRouteProtectingTunResvBw": cmplsFrrFacRouteProtectingTunResvBw,
       "cmplsFrrFacRouteProtectingTunProtectionType": cmplsFrrFacRouteProtectingTunProtectionType,
       "cmplsFrrConformance": cmplsFrrConformance,
       "cmplsFrrGroups": cmplsFrrGroups,
       "cmplsFrrScalarGroup": cmplsFrrScalarGroup,
       "cmplsFrrConstGroup": cmplsFrrConstGroup,
       "cmplsFrrLogGroup": cmplsFrrLogGroup,
       "cmplsFrrFacRouteDBGroup": cmplsFrrFacRouteDBGroup,
       "cmplsFrrNotifGroup": cmplsFrrNotifGroup,
       "cmplsFrrNotifGroupRev1": cmplsFrrNotifGroupRev1,
       "cmplsFrrCompliances": cmplsFrrCompliances,
       "cmplsFrrModuleCompliance": cmplsFrrModuleCompliance,
       "cmplsFrrModuleComplianceRev1": cmplsFrrModuleComplianceRev1}
)
