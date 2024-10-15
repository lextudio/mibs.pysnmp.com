# SNMP MIB module (MPLS-FRR-ONE2ONE-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-FRR-ONE2ONE-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:58 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsFrrGeneralConstraintsGroup,
 mplsFrrGeneralScalarGroup,
 mplsFrrGeneralTunnelARHopGroup) = mibBuilder.importSymbols(
    "MPLS-FRR-GENERAL-STD-MIB",
    "mplsFrrGeneralConstraintsGroup",
    "mplsFrrGeneralScalarGroup",
    "mplsFrrGeneralTunnelARHopGroup")

(MplsLsrIdentifier,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
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

mplsFrrOne2OneMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 203)
)
mplsFrrOne2OneMIB.setRevisions(
        ("2011-11-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsFrrOne2OneObjects_ObjectIdentity = ObjectIdentity
mplsFrrOne2OneObjects = _MplsFrrOne2OneObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 203, 1)
)


class _MplsFrrIncomingDetourLSPs_Type(Integer32):
    """Custom type mplsFrrIncomingDetourLSPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsFrrIncomingDetourLSPs_Type.__name__ = "Integer32"
_MplsFrrIncomingDetourLSPs_Object = MibScalar
mplsFrrIncomingDetourLSPs = _MplsFrrIncomingDetourLSPs_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 1),
    _MplsFrrIncomingDetourLSPs_Type()
)
mplsFrrIncomingDetourLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrIncomingDetourLSPs.setStatus("current")


class _MplsFrrOutgoingDetourLSPs_Type(Integer32):
    """Custom type mplsFrrOutgoingDetourLSPs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsFrrOutgoingDetourLSPs_Type.__name__ = "Integer32"
_MplsFrrOutgoingDetourLSPs_Object = MibScalar
mplsFrrOutgoingDetourLSPs = _MplsFrrOutgoingDetourLSPs_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 2),
    _MplsFrrOutgoingDetourLSPs_Type()
)
mplsFrrOutgoingDetourLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOutgoingDetourLSPs.setStatus("current")


class _MplsFrrOne2OneDetourOriginating_Type(Integer32):
    """Custom type mplsFrrOne2OneDetourOriginating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsFrrOne2OneDetourOriginating_Type.__name__ = "Integer32"
_MplsFrrOne2OneDetourOriginating_Object = MibScalar
mplsFrrOne2OneDetourOriginating = _MplsFrrOne2OneDetourOriginating_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 3),
    _MplsFrrOne2OneDetourOriginating_Type()
)
mplsFrrOne2OneDetourOriginating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOne2OneDetourOriginating.setStatus("current")
_MplsFrrActiveProtectedLSPs_Type = Gauge32
_MplsFrrActiveProtectedLSPs_Object = MibScalar
mplsFrrActiveProtectedLSPs = _MplsFrrActiveProtectedLSPs_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 4),
    _MplsFrrActiveProtectedLSPs_Type()
)
mplsFrrActiveProtectedLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrActiveProtectedLSPs.setStatus("current")
_MplsFrrOne2OnePlrTable_Object = MibTable
mplsFrrOne2OnePlrTable = _MplsFrrOne2OnePlrTable_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5)
)
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrTable.setStatus("current")
_MplsFrrOne2OnePlrEntry_Object = MibTableRow
mplsFrrOne2OnePlrEntry = _MplsFrrOne2OnePlrEntry_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1)
)
mplsFrrOne2OnePlrEntry.setIndexNames(
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelIndex"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelDetourInstance"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelIngressLSRId"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelEgressLSRId"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrId"),
)
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrEntry.setStatus("current")
_MplsFrrOne2OnePlrTunnelIndex_Type = MplsTunnelIndex
_MplsFrrOne2OnePlrTunnelIndex_Object = MibTableColumn
mplsFrrOne2OnePlrTunnelIndex = _MplsFrrOne2OnePlrTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 1),
    _MplsFrrOne2OnePlrTunnelIndex_Type()
)
mplsFrrOne2OnePlrTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrTunnelIndex.setStatus("current")
_MplsFrrOne2OnePlrTunnelDetourInstance_Type = MplsTunnelInstanceIndex
_MplsFrrOne2OnePlrTunnelDetourInstance_Object = MibTableColumn
mplsFrrOne2OnePlrTunnelDetourInstance = _MplsFrrOne2OnePlrTunnelDetourInstance_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 2),
    _MplsFrrOne2OnePlrTunnelDetourInstance_Type()
)
mplsFrrOne2OnePlrTunnelDetourInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrTunnelDetourInstance.setStatus("current")
_MplsFrrOne2OnePlrTunnelIngressLSRId_Type = MplsLsrIdentifier
_MplsFrrOne2OnePlrTunnelIngressLSRId_Object = MibTableColumn
mplsFrrOne2OnePlrTunnelIngressLSRId = _MplsFrrOne2OnePlrTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 3),
    _MplsFrrOne2OnePlrTunnelIngressLSRId_Type()
)
mplsFrrOne2OnePlrTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrTunnelIngressLSRId.setStatus("current")
_MplsFrrOne2OnePlrTunnelEgressLSRId_Type = MplsLsrIdentifier
_MplsFrrOne2OnePlrTunnelEgressLSRId_Object = MibTableColumn
mplsFrrOne2OnePlrTunnelEgressLSRId = _MplsFrrOne2OnePlrTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 4),
    _MplsFrrOne2OnePlrTunnelEgressLSRId_Type()
)
mplsFrrOne2OnePlrTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrTunnelEgressLSRId.setStatus("current")
_MplsFrrOne2OnePlrId_Type = MplsLsrIdentifier
_MplsFrrOne2OnePlrId_Object = MibTableColumn
mplsFrrOne2OnePlrId = _MplsFrrOne2OnePlrId_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 5),
    _MplsFrrOne2OnePlrId_Type()
)
mplsFrrOne2OnePlrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrId.setStatus("current")


class _MplsFrrOne2OnePlrSenderAddrType_Type(InetAddressType):
    """Custom type mplsFrrOne2OnePlrSenderAddrType based on InetAddressType"""


_MplsFrrOne2OnePlrSenderAddrType_Object = MibTableColumn
mplsFrrOne2OnePlrSenderAddrType = _MplsFrrOne2OnePlrSenderAddrType_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 6),
    _MplsFrrOne2OnePlrSenderAddrType_Type()
)
mplsFrrOne2OnePlrSenderAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrSenderAddrType.setStatus("current")
_MplsFrrOne2OnePlrSenderAddr_Type = InetAddress
_MplsFrrOne2OnePlrSenderAddr_Object = MibTableColumn
mplsFrrOne2OnePlrSenderAddr = _MplsFrrOne2OnePlrSenderAddr_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 7),
    _MplsFrrOne2OnePlrSenderAddr_Type()
)
mplsFrrOne2OnePlrSenderAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrSenderAddr.setStatus("current")


class _MplsFrrOne2OnePlrAvoidNodeAddrType_Type(InetAddressType):
    """Custom type mplsFrrOne2OnePlrAvoidNodeAddrType based on InetAddressType"""


_MplsFrrOne2OnePlrAvoidNodeAddrType_Object = MibTableColumn
mplsFrrOne2OnePlrAvoidNodeAddrType = _MplsFrrOne2OnePlrAvoidNodeAddrType_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 8),
    _MplsFrrOne2OnePlrAvoidNodeAddrType_Type()
)
mplsFrrOne2OnePlrAvoidNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrAvoidNodeAddrType.setStatus("current")
_MplsFrrOne2OnePlrAvoidNodeAddr_Type = InetAddress
_MplsFrrOne2OnePlrAvoidNodeAddr_Object = MibTableColumn
mplsFrrOne2OnePlrAvoidNodeAddr = _MplsFrrOne2OnePlrAvoidNodeAddr_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 5, 1, 9),
    _MplsFrrOne2OnePlrAvoidNodeAddr_Type()
)
mplsFrrOne2OnePlrAvoidNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrAvoidNodeAddr.setStatus("current")
_MplsFrrOne2OneDetourTable_Object = MibTable
mplsFrrOne2OneDetourTable = _MplsFrrOne2OneDetourTable_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 6)
)
if mibBuilder.loadTexts:
    mplsFrrOne2OneDetourTable.setStatus("current")
_MplsFrrOne2OneDetourEntry_Object = MibTableRow
mplsFrrOne2OneDetourEntry = _MplsFrrOne2OneDetourEntry_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 6, 1)
)
mplsFrrOne2OneDetourEntry.setIndexNames(
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelIndex"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelDetourInstance"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelIngressLSRId"),
    (0, "MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    mplsFrrOne2OneDetourEntry.setStatus("current")
_MplsFrrOne2OneDetourActive_Type = TruthValue
_MplsFrrOne2OneDetourActive_Object = MibTableColumn
mplsFrrOne2OneDetourActive = _MplsFrrOne2OneDetourActive_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 6, 1, 1),
    _MplsFrrOne2OneDetourActive_Type()
)
mplsFrrOne2OneDetourActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOne2OneDetourActive.setStatus("current")


class _MplsFrrOne2OneDetourMergedStatus_Type(Integer32):
    """Custom type mplsFrrOne2OneDetourMergedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mergedWithDetour", 3),
          ("mergedWithProtectedTunnel", 2),
          ("notMerged", 1))
    )


_MplsFrrOne2OneDetourMergedStatus_Type.__name__ = "Integer32"
_MplsFrrOne2OneDetourMergedStatus_Object = MibTableColumn
mplsFrrOne2OneDetourMergedStatus = _MplsFrrOne2OneDetourMergedStatus_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 6, 1, 2),
    _MplsFrrOne2OneDetourMergedStatus_Type()
)
mplsFrrOne2OneDetourMergedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOne2OneDetourMergedStatus.setStatus("current")
_MplsFrrOne2OneDetourMergedDetourInst_Type = MplsTunnelInstanceIndex
_MplsFrrOne2OneDetourMergedDetourInst_Object = MibTableColumn
mplsFrrOne2OneDetourMergedDetourInst = _MplsFrrOne2OneDetourMergedDetourInst_Object(
    (1, 3, 6, 1, 2, 1, 203, 1, 6, 1, 3),
    _MplsFrrOne2OneDetourMergedDetourInst_Type()
)
mplsFrrOne2OneDetourMergedDetourInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrOne2OneDetourMergedDetourInst.setStatus("current")
_MplsFrrOne2OneConformance_ObjectIdentity = ObjectIdentity
mplsFrrOne2OneConformance = _MplsFrrOne2OneConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 203, 2)
)
_MplsFrrOne2OneCompliances_ObjectIdentity = ObjectIdentity
mplsFrrOne2OneCompliances = _MplsFrrOne2OneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 203, 2, 1)
)
_MplsFrrOne2OneGroups_ObjectIdentity = ObjectIdentity
mplsFrrOne2OneGroups = _MplsFrrOne2OneGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 203, 2, 2)
)

# Managed Objects groups

mplsFrrOne2OneScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 203, 2, 2, 1)
)
mplsFrrOne2OneScalarsGroup.setObjects(
      *(("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrIncomingDetourLSPs"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOutgoingDetourLSPs"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OneDetourOriginating"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrActiveProtectedLSPs"))
)
if mibBuilder.loadTexts:
    mplsFrrOne2OneScalarsGroup.setStatus("current")

mplsFrrOne2OnePLRDetourGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 203, 2, 2, 2)
)
mplsFrrOne2OnePLRDetourGroup.setObjects(
      *(("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OneDetourActive"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OneDetourMergedStatus"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OneDetourMergedDetourInst"))
)
if mibBuilder.loadTexts:
    mplsFrrOne2OnePLRDetourGroup.setStatus("current")

mplsFrrOne2OnePlrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 203, 2, 2, 3)
)
mplsFrrOne2OnePlrGroup.setObjects(
      *(("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrSenderAddrType"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrSenderAddr"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrAvoidNodeAddrType"),
        ("MPLS-FRR-ONE2ONE-STD-MIB", "mplsFrrOne2OnePlrAvoidNodeAddr"))
)
if mibBuilder.loadTexts:
    mplsFrrOne2OnePlrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsFrrOne2OneModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 203, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsFrrOne2OneModuleFullCompliance.setStatus(
        "current"
    )

mplsFrrOne2OneModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 203, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsFrrOne2OneModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-FRR-ONE2ONE-STD-MIB",
    **{"mplsFrrOne2OneMIB": mplsFrrOne2OneMIB,
       "mplsFrrOne2OneObjects": mplsFrrOne2OneObjects,
       "mplsFrrIncomingDetourLSPs": mplsFrrIncomingDetourLSPs,
       "mplsFrrOutgoingDetourLSPs": mplsFrrOutgoingDetourLSPs,
       "mplsFrrOne2OneDetourOriginating": mplsFrrOne2OneDetourOriginating,
       "mplsFrrActiveProtectedLSPs": mplsFrrActiveProtectedLSPs,
       "mplsFrrOne2OnePlrTable": mplsFrrOne2OnePlrTable,
       "mplsFrrOne2OnePlrEntry": mplsFrrOne2OnePlrEntry,
       "mplsFrrOne2OnePlrTunnelIndex": mplsFrrOne2OnePlrTunnelIndex,
       "mplsFrrOne2OnePlrTunnelDetourInstance": mplsFrrOne2OnePlrTunnelDetourInstance,
       "mplsFrrOne2OnePlrTunnelIngressLSRId": mplsFrrOne2OnePlrTunnelIngressLSRId,
       "mplsFrrOne2OnePlrTunnelEgressLSRId": mplsFrrOne2OnePlrTunnelEgressLSRId,
       "mplsFrrOne2OnePlrId": mplsFrrOne2OnePlrId,
       "mplsFrrOne2OnePlrSenderAddrType": mplsFrrOne2OnePlrSenderAddrType,
       "mplsFrrOne2OnePlrSenderAddr": mplsFrrOne2OnePlrSenderAddr,
       "mplsFrrOne2OnePlrAvoidNodeAddrType": mplsFrrOne2OnePlrAvoidNodeAddrType,
       "mplsFrrOne2OnePlrAvoidNodeAddr": mplsFrrOne2OnePlrAvoidNodeAddr,
       "mplsFrrOne2OneDetourTable": mplsFrrOne2OneDetourTable,
       "mplsFrrOne2OneDetourEntry": mplsFrrOne2OneDetourEntry,
       "mplsFrrOne2OneDetourActive": mplsFrrOne2OneDetourActive,
       "mplsFrrOne2OneDetourMergedStatus": mplsFrrOne2OneDetourMergedStatus,
       "mplsFrrOne2OneDetourMergedDetourInst": mplsFrrOne2OneDetourMergedDetourInst,
       "mplsFrrOne2OneConformance": mplsFrrOne2OneConformance,
       "mplsFrrOne2OneCompliances": mplsFrrOne2OneCompliances,
       "mplsFrrOne2OneModuleFullCompliance": mplsFrrOne2OneModuleFullCompliance,
       "mplsFrrOne2OneModuleReadOnlyCompliance": mplsFrrOne2OneModuleReadOnlyCompliance,
       "mplsFrrOne2OneGroups": mplsFrrOne2OneGroups,
       "mplsFrrOne2OneScalarsGroup": mplsFrrOne2OneScalarsGroup,
       "mplsFrrOne2OnePLRDetourGroup": mplsFrrOne2OnePLRDetourGroup,
       "mplsFrrOne2OnePlrGroup": mplsFrrOne2OnePlrGroup}
)
