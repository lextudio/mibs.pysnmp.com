# SNMP MIB module (MPLS-FRR-FACILITY-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-FRR-FACILITY-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:55 2024
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

(mplsFrrGeneralConstraintsGroup,
 mplsFrrGeneralScalarGroup,
 mplsFrrGeneralTunnelARHopGroup) = mibBuilder.importSymbols(
    "MPLS-FRR-GENERAL-STD-MIB",
    "mplsFrrGeneralConstraintsGroup",
    "mplsFrrGeneralScalarGroup",
    "mplsFrrGeneralTunnelARHopGroup")

(MplsBitRate,
 MplsLsrIdentifier,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate",
    "MplsLsrIdentifier",
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mplsFrrFacilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 204)
)
mplsFrrFacilityMIB.setRevisions(
        ("2011-11-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsFrrFacilityNotifications_ObjectIdentity = ObjectIdentity
mplsFrrFacilityNotifications = _MplsFrrFacilityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 204, 0)
)
_MplsFrrFacilityObjects_ObjectIdentity = ObjectIdentity
mplsFrrFacilityObjects = _MplsFrrFacilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 204, 1)
)


class _MplsFrrConfiguredInterfaces_Type(Integer32):
    """Custom type mplsFrrConfiguredInterfaces based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsFrrConfiguredInterfaces_Type.__name__ = "Integer32"
_MplsFrrConfiguredInterfaces_Object = MibScalar
mplsFrrConfiguredInterfaces = _MplsFrrConfiguredInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 1),
    _MplsFrrConfiguredInterfaces_Type()
)
mplsFrrConfiguredInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrConfiguredInterfaces.setStatus("current")


class _MplsFrrActiveInterfaces_Type(Gauge32):
    """Custom type mplsFrrActiveInterfaces based on Gauge32"""
    defaultValue = 0


_MplsFrrActiveInterfaces_Object = MibScalar
mplsFrrActiveInterfaces = _MplsFrrActiveInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 2),
    _MplsFrrActiveInterfaces_Type()
)
mplsFrrActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrActiveInterfaces.setStatus("current")


class _MplsFrrConfiguredBypassTunnels_Type(Gauge32):
    """Custom type mplsFrrConfiguredBypassTunnels based on Gauge32"""
    defaultValue = 0


_MplsFrrConfiguredBypassTunnels_Object = MibScalar
mplsFrrConfiguredBypassTunnels = _MplsFrrConfiguredBypassTunnels_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 3),
    _MplsFrrConfiguredBypassTunnels_Type()
)
mplsFrrConfiguredBypassTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrConfiguredBypassTunnels.setStatus("current")


class _MplsFrrActiveBypassTunnels_Type(Gauge32):
    """Custom type mplsFrrActiveBypassTunnels based on Gauge32"""
    defaultValue = 0


_MplsFrrActiveBypassTunnels_Object = MibScalar
mplsFrrActiveBypassTunnels = _MplsFrrActiveBypassTunnels_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 4),
    _MplsFrrActiveBypassTunnels_Type()
)
mplsFrrActiveBypassTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrActiveBypassTunnels.setStatus("current")


class _MplsFrrFacilityNotificationsEnabled_Type(TruthValue):
    """Custom type mplsFrrFacilityNotificationsEnabled based on TruthValue"""


_MplsFrrFacilityNotificationsEnabled_Object = MibScalar
mplsFrrFacilityNotificationsEnabled = _MplsFrrFacilityNotificationsEnabled_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 5),
    _MplsFrrFacilityNotificationsEnabled_Type()
)
mplsFrrFacilityNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsFrrFacilityNotificationsEnabled.setStatus("current")


class _MplsFrrFacilityNotificationsMaxRate_Type(Gauge32):
    """Custom type mplsFrrFacilityNotificationsMaxRate based on Gauge32"""
    defaultValue = 0


_MplsFrrFacilityNotificationsMaxRate_Object = MibScalar
mplsFrrFacilityNotificationsMaxRate = _MplsFrrFacilityNotificationsMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 6),
    _MplsFrrFacilityNotificationsMaxRate_Type()
)
mplsFrrFacilityNotificationsMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsFrrFacilityNotificationsMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsFrrFacilityNotificationsMaxRate.setUnits("Notifications per Second")
_MplsFrrFacilityDBTable_Object = MibTable
mplsFrrFacilityDBTable = _MplsFrrFacilityDBTable_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7)
)
if mibBuilder.loadTexts:
    mplsFrrFacilityDBTable.setStatus("current")
_MplsFrrFacilityDBEntry_Object = MibTableRow
mplsFrrFacilityDBEntry = _MplsFrrFacilityDBEntry_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1)
)
mplsFrrFacilityDBEntry.setIndexNames(
    (0, "MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityProtectedIfIndex"),
    (0, "MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityProtectingTunnelIndex"),
    (0, "MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityBackupTunnelIndex"),
    (0, "MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityBackupTunnelInstance"),
    (0, "MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityBackupTunnelIngressLSRId"),
    (0, "MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityBackupTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    mplsFrrFacilityDBEntry.setStatus("current")
_MplsFrrFacilityProtectedIfIndex_Type = InterfaceIndex
_MplsFrrFacilityProtectedIfIndex_Object = MibTableColumn
mplsFrrFacilityProtectedIfIndex = _MplsFrrFacilityProtectedIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 1),
    _MplsFrrFacilityProtectedIfIndex_Type()
)
mplsFrrFacilityProtectedIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrFacilityProtectedIfIndex.setStatus("current")
_MplsFrrFacilityProtectingTunnelIndex_Type = MplsTunnelIndex
_MplsFrrFacilityProtectingTunnelIndex_Object = MibTableColumn
mplsFrrFacilityProtectingTunnelIndex = _MplsFrrFacilityProtectingTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 2),
    _MplsFrrFacilityProtectingTunnelIndex_Type()
)
mplsFrrFacilityProtectingTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrFacilityProtectingTunnelIndex.setStatus("current")
_MplsFrrFacilityBackupTunnelIndex_Type = MplsTunnelIndex
_MplsFrrFacilityBackupTunnelIndex_Object = MibTableColumn
mplsFrrFacilityBackupTunnelIndex = _MplsFrrFacilityBackupTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 3),
    _MplsFrrFacilityBackupTunnelIndex_Type()
)
mplsFrrFacilityBackupTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrFacilityBackupTunnelIndex.setStatus("current")
_MplsFrrFacilityBackupTunnelInstance_Type = MplsTunnelInstanceIndex
_MplsFrrFacilityBackupTunnelInstance_Object = MibTableColumn
mplsFrrFacilityBackupTunnelInstance = _MplsFrrFacilityBackupTunnelInstance_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 4),
    _MplsFrrFacilityBackupTunnelInstance_Type()
)
mplsFrrFacilityBackupTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrFacilityBackupTunnelInstance.setStatus("current")
_MplsFrrFacilityBackupTunnelIngressLSRId_Type = MplsLsrIdentifier
_MplsFrrFacilityBackupTunnelIngressLSRId_Object = MibTableColumn
mplsFrrFacilityBackupTunnelIngressLSRId = _MplsFrrFacilityBackupTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 5),
    _MplsFrrFacilityBackupTunnelIngressLSRId_Type()
)
mplsFrrFacilityBackupTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrFacilityBackupTunnelIngressLSRId.setStatus("current")
_MplsFrrFacilityBackupTunnelEgressLSRId_Type = MplsLsrIdentifier
_MplsFrrFacilityBackupTunnelEgressLSRId_Object = MibTableColumn
mplsFrrFacilityBackupTunnelEgressLSRId = _MplsFrrFacilityBackupTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 6),
    _MplsFrrFacilityBackupTunnelEgressLSRId_Type()
)
mplsFrrFacilityBackupTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrFacilityBackupTunnelEgressLSRId.setStatus("current")
_MplsFrrFacilityDBNumProtectingTunnelOnIf_Type = Gauge32
_MplsFrrFacilityDBNumProtectingTunnelOnIf_Object = MibTableColumn
mplsFrrFacilityDBNumProtectingTunnelOnIf = _MplsFrrFacilityDBNumProtectingTunnelOnIf_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 7),
    _MplsFrrFacilityDBNumProtectingTunnelOnIf_Type()
)
mplsFrrFacilityDBNumProtectingTunnelOnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrFacilityDBNumProtectingTunnelOnIf.setStatus("current")
_MplsFrrFacilityDBNumProtectedLspOnIf_Type = Gauge32
_MplsFrrFacilityDBNumProtectedLspOnIf_Object = MibTableColumn
mplsFrrFacilityDBNumProtectedLspOnIf = _MplsFrrFacilityDBNumProtectedLspOnIf_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 8),
    _MplsFrrFacilityDBNumProtectedLspOnIf_Type()
)
mplsFrrFacilityDBNumProtectedLspOnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrFacilityDBNumProtectedLspOnIf.setStatus("current")
_MplsFrrFacilityDBNumProtectedTunnels_Type = Gauge32
_MplsFrrFacilityDBNumProtectedTunnels_Object = MibTableColumn
mplsFrrFacilityDBNumProtectedTunnels = _MplsFrrFacilityDBNumProtectedTunnels_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 9),
    _MplsFrrFacilityDBNumProtectedTunnels_Type()
)
mplsFrrFacilityDBNumProtectedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrFacilityDBNumProtectedTunnels.setStatus("current")


class _MplsFrrFacilityDBProtectingTunnelStatus_Type(Integer32):
    """Custom type mplsFrrFacilityDBProtectingTunnelStatus based on Integer32"""
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


_MplsFrrFacilityDBProtectingTunnelStatus_Type.__name__ = "Integer32"
_MplsFrrFacilityDBProtectingTunnelStatus_Object = MibTableColumn
mplsFrrFacilityDBProtectingTunnelStatus = _MplsFrrFacilityDBProtectingTunnelStatus_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 10),
    _MplsFrrFacilityDBProtectingTunnelStatus_Type()
)
mplsFrrFacilityDBProtectingTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrFacilityDBProtectingTunnelStatus.setStatus("current")
_MplsFrrFacilityDBProtectingTunnelResvBw_Type = MplsBitRate
_MplsFrrFacilityDBProtectingTunnelResvBw_Object = MibTableColumn
mplsFrrFacilityDBProtectingTunnelResvBw = _MplsFrrFacilityDBProtectingTunnelResvBw_Object(
    (1, 3, 6, 1, 2, 1, 204, 1, 7, 1, 11),
    _MplsFrrFacilityDBProtectingTunnelResvBw_Type()
)
mplsFrrFacilityDBProtectingTunnelResvBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrFacilityDBProtectingTunnelResvBw.setStatus("current")
if mibBuilder.loadTexts:
    mplsFrrFacilityDBProtectingTunnelResvBw.setUnits("kilobits per second")
_MplsFrrFacilityConformance_ObjectIdentity = ObjectIdentity
mplsFrrFacilityConformance = _MplsFrrFacilityConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 204, 2)
)
_MplsFrrFacilityCompliances_ObjectIdentity = ObjectIdentity
mplsFrrFacilityCompliances = _MplsFrrFacilityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 204, 2, 1)
)
_MplsFrrFacilityGroups_ObjectIdentity = ObjectIdentity
mplsFrrFacilityGroups = _MplsFrrFacilityGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 204, 2, 2)
)

# Managed Objects groups

mplsFrrFacilityScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 204, 2, 2, 1)
)
mplsFrrFacilityScalarGroup.setObjects(
      *(("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrConfiguredInterfaces"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrActiveInterfaces"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrConfiguredBypassTunnels"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrActiveBypassTunnels"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityNotificationsEnabled"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityNotificationsMaxRate"))
)
if mibBuilder.loadTexts:
    mplsFrrFacilityScalarGroup.setStatus("current")

mplsFrrFacilityDBGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 204, 2, 2, 2)
)
mplsFrrFacilityDBGroup.setObjects(
      *(("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectingTunnelOnIf"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectedLspOnIf"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectedTunnels"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBProtectingTunnelStatus"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBProtectingTunnelResvBw"))
)
if mibBuilder.loadTexts:
    mplsFrrFacilityDBGroup.setStatus("current")


# Notification objects

mplsFrrFacilityInitialBackupTunnelInvoked = NotificationType(
    (1, 3, 6, 1, 2, 1, 204, 0, 1)
)
mplsFrrFacilityInitialBackupTunnelInvoked.setObjects(
      *(("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectingTunnelOnIf"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectedLspOnIf"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectedTunnels"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBProtectingTunnelStatus"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBProtectingTunnelResvBw"))
)
if mibBuilder.loadTexts:
    mplsFrrFacilityInitialBackupTunnelInvoked.setStatus(
        "current"
    )

mplsFrrFacilityFinalTunnelRestored = NotificationType(
    (1, 3, 6, 1, 2, 1, 204, 0, 2)
)
mplsFrrFacilityFinalTunnelRestored.setObjects(
      *(("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectingTunnelOnIf"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectedLspOnIf"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBNumProtectedTunnels"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBProtectingTunnelStatus"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityDBProtectingTunnelResvBw"))
)
if mibBuilder.loadTexts:
    mplsFrrFacilityFinalTunnelRestored.setStatus(
        "current"
    )


# Notifications groups

mplsFrrFacilityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 204, 2, 2, 3)
)
mplsFrrFacilityNotificationsGroup.setObjects(
      *(("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityInitialBackupTunnelInvoked"),
        ("MPLS-FRR-FACILITY-STD-MIB", "mplsFrrFacilityFinalTunnelRestored"))
)
if mibBuilder.loadTexts:
    mplsFrrFacilityNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsFrrFacilityModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 204, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsFrrFacilityModuleFullCompliance.setStatus(
        "current"
    )

mplsFrrFacilityModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 204, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsFrrFacilityModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-FRR-FACILITY-STD-MIB",
    **{"mplsFrrFacilityMIB": mplsFrrFacilityMIB,
       "mplsFrrFacilityNotifications": mplsFrrFacilityNotifications,
       "mplsFrrFacilityInitialBackupTunnelInvoked": mplsFrrFacilityInitialBackupTunnelInvoked,
       "mplsFrrFacilityFinalTunnelRestored": mplsFrrFacilityFinalTunnelRestored,
       "mplsFrrFacilityObjects": mplsFrrFacilityObjects,
       "mplsFrrConfiguredInterfaces": mplsFrrConfiguredInterfaces,
       "mplsFrrActiveInterfaces": mplsFrrActiveInterfaces,
       "mplsFrrConfiguredBypassTunnels": mplsFrrConfiguredBypassTunnels,
       "mplsFrrActiveBypassTunnels": mplsFrrActiveBypassTunnels,
       "mplsFrrFacilityNotificationsEnabled": mplsFrrFacilityNotificationsEnabled,
       "mplsFrrFacilityNotificationsMaxRate": mplsFrrFacilityNotificationsMaxRate,
       "mplsFrrFacilityDBTable": mplsFrrFacilityDBTable,
       "mplsFrrFacilityDBEntry": mplsFrrFacilityDBEntry,
       "mplsFrrFacilityProtectedIfIndex": mplsFrrFacilityProtectedIfIndex,
       "mplsFrrFacilityProtectingTunnelIndex": mplsFrrFacilityProtectingTunnelIndex,
       "mplsFrrFacilityBackupTunnelIndex": mplsFrrFacilityBackupTunnelIndex,
       "mplsFrrFacilityBackupTunnelInstance": mplsFrrFacilityBackupTunnelInstance,
       "mplsFrrFacilityBackupTunnelIngressLSRId": mplsFrrFacilityBackupTunnelIngressLSRId,
       "mplsFrrFacilityBackupTunnelEgressLSRId": mplsFrrFacilityBackupTunnelEgressLSRId,
       "mplsFrrFacilityDBNumProtectingTunnelOnIf": mplsFrrFacilityDBNumProtectingTunnelOnIf,
       "mplsFrrFacilityDBNumProtectedLspOnIf": mplsFrrFacilityDBNumProtectedLspOnIf,
       "mplsFrrFacilityDBNumProtectedTunnels": mplsFrrFacilityDBNumProtectedTunnels,
       "mplsFrrFacilityDBProtectingTunnelStatus": mplsFrrFacilityDBProtectingTunnelStatus,
       "mplsFrrFacilityDBProtectingTunnelResvBw": mplsFrrFacilityDBProtectingTunnelResvBw,
       "mplsFrrFacilityConformance": mplsFrrFacilityConformance,
       "mplsFrrFacilityCompliances": mplsFrrFacilityCompliances,
       "mplsFrrFacilityModuleFullCompliance": mplsFrrFacilityModuleFullCompliance,
       "mplsFrrFacilityModuleReadOnlyCompliance": mplsFrrFacilityModuleReadOnlyCompliance,
       "mplsFrrFacilityGroups": mplsFrrFacilityGroups,
       "mplsFrrFacilityScalarGroup": mplsFrrFacilityScalarGroup,
       "mplsFrrFacilityDBGroup": mplsFrrFacilityDBGroup,
       "mplsFrrFacilityNotificationsGroup": mplsFrrFacilityNotificationsGroup}
)
