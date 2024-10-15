# SNMP MIB module (CISCO-MPLS-TE-STD-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MPLS-TE-STD-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:56 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsTunnelARHopListIndex,
 mplsTunnelAdminStatus,
 mplsTunnelEgressLSRId,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance,
 mplsTunnelName,
 mplsTunnelOperStatus) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelARHopListIndex",
    "mplsTunnelAdminStatus",
    "mplsTunnelEgressLSRId",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance",
    "mplsTunnelName",
    "mplsTunnelOperStatus")

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

cmplsTeStdExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738)
)
cmplsTeStdExtMIB.setRevisions(
        ("2016-08-05 00:00",
         "2012-02-22 00:00",
         "2011-10-04 00:00",
         "2011-01-07 00:00",
         "2010-10-20 00:00",
         "2010-09-23 00:00",
         "2010-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CmplsTeTunnelDiag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bfdSessionBringupTimeout", 2),
          ("unknonw", 1))
    )



class CmplsTunnelBWPercent(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_CmplsTeStdExtMIBNotifs_ObjectIdentity = ObjectIdentity
cmplsTeStdExtMIBNotifs = _CmplsTeStdExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 0)
)
_CmplsTeStdExtMIBObjects_ObjectIdentity = ObjectIdentity
cmplsTeStdExtMIBObjects = _CmplsTeStdExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1)
)
_CmplsTunnelAutoBWTable_Object = MibTable
cmplsTunnelAutoBWTable = _CmplsTunnelAutoBWTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1)
)
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWTable.setStatus("current")
_CmplsTunnelAutoBWEntry_Object = MibTableRow
cmplsTunnelAutoBWEntry = _CmplsTunnelAutoBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1)
)
cmplsTunnelAutoBWEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWEntry.setStatus("current")


class _CmplsTunnelAutoBWStatus_Type(Integer32):
    """Custom type cmplsTunnelAutoBWStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoBWCollectOnlyMode", 3),
          ("autoBWDisabled", 1),
          ("autoBWEnabled", 2))
    )


_CmplsTunnelAutoBWStatus_Type.__name__ = "Integer32"
_CmplsTunnelAutoBWStatus_Object = MibTableColumn
cmplsTunnelAutoBWStatus = _CmplsTunnelAutoBWStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 1),
    _CmplsTunnelAutoBWStatus_Type()
)
cmplsTunnelAutoBWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWStatus.setStatus("current")


class _CmplsTunnelAutoBWMin_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWMin based on Unsigned32"""
    defaultValue = 0


_CmplsTunnelAutoBWMin_Object = MibTableColumn
cmplsTunnelAutoBWMin = _CmplsTunnelAutoBWMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 2),
    _CmplsTunnelAutoBWMin_Type()
)
cmplsTunnelAutoBWMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWMin.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWMin.setUnits("kbps")


class _CmplsTunnelAutoBWMax_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWMax based on Unsigned32"""
    defaultValue = 100


_CmplsTunnelAutoBWMax_Object = MibTableColumn
cmplsTunnelAutoBWMax = _CmplsTunnelAutoBWMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 3),
    _CmplsTunnelAutoBWMax_Type()
)
cmplsTunnelAutoBWMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWMax.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWMax.setUnits("kbps")


class _CmplsTunnelAutoBWAdjThreshPercs_Type(CmplsTunnelBWPercent):
    """Custom type cmplsTunnelAutoBWAdjThreshPercs based on CmplsTunnelBWPercent"""
    defaultValue = 10


_CmplsTunnelAutoBWAdjThreshPercs_Object = MibTableColumn
cmplsTunnelAutoBWAdjThreshPercs = _CmplsTunnelAutoBWAdjThreshPercs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 4),
    _CmplsTunnelAutoBWAdjThreshPercs_Type()
)
cmplsTunnelAutoBWAdjThreshPercs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWAdjThreshPercs.setStatus("current")


class _CmplsTunnelAutoBWAdjThreshBW_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWAdjThreshBW based on Unsigned32"""
    defaultValue = 10


_CmplsTunnelAutoBWAdjThreshBW_Object = MibTableColumn
cmplsTunnelAutoBWAdjThreshBW = _CmplsTunnelAutoBWAdjThreshBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 5),
    _CmplsTunnelAutoBWAdjThreshBW_Type()
)
cmplsTunnelAutoBWAdjThreshBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWAdjThreshBW.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWAdjThreshBW.setUnits("kbps")


class _CmplsTunnelAutoBWOverflowThreshPercs_Type(CmplsTunnelBWPercent):
    """Custom type cmplsTunnelAutoBWOverflowThreshPercs based on CmplsTunnelBWPercent"""
    defaultValue = 10


_CmplsTunnelAutoBWOverflowThreshPercs_Object = MibTableColumn
cmplsTunnelAutoBWOverflowThreshPercs = _CmplsTunnelAutoBWOverflowThreshPercs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 6),
    _CmplsTunnelAutoBWOverflowThreshPercs_Type()
)
cmplsTunnelAutoBWOverflowThreshPercs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWOverflowThreshPercs.setStatus("current")


class _CmplsTunnelAutoBWOverflowThreshBW_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWOverflowThreshBW based on Unsigned32"""
    defaultValue = 10


_CmplsTunnelAutoBWOverflowThreshBW_Object = MibTableColumn
cmplsTunnelAutoBWOverflowThreshBW = _CmplsTunnelAutoBWOverflowThreshBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 7),
    _CmplsTunnelAutoBWOverflowThreshBW_Type()
)
cmplsTunnelAutoBWOverflowThreshBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWOverflowThreshBW.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWOverflowThreshBW.setUnits("kbps")


class _CmplsTunnelAutoBWOverflowLimit_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWOverflowLimit based on Unsigned32"""
    defaultValue = 1


_CmplsTunnelAutoBWOverflowLimit_Object = MibTableColumn
cmplsTunnelAutoBWOverflowLimit = _CmplsTunnelAutoBWOverflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 8),
    _CmplsTunnelAutoBWOverflowLimit_Type()
)
cmplsTunnelAutoBWOverflowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWOverflowLimit.setStatus("current")


class _CmplsTunnelAutoBWUnderflowThreshPercs_Type(CmplsTunnelBWPercent):
    """Custom type cmplsTunnelAutoBWUnderflowThreshPercs based on CmplsTunnelBWPercent"""
    defaultValue = 10


_CmplsTunnelAutoBWUnderflowThreshPercs_Object = MibTableColumn
cmplsTunnelAutoBWUnderflowThreshPercs = _CmplsTunnelAutoBWUnderflowThreshPercs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 9),
    _CmplsTunnelAutoBWUnderflowThreshPercs_Type()
)
cmplsTunnelAutoBWUnderflowThreshPercs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowThreshPercs.setStatus("current")


class _CmplsTunnelAutoBWUnderflowThreshBW_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWUnderflowThreshBW based on Unsigned32"""
    defaultValue = 1


_CmplsTunnelAutoBWUnderflowThreshBW_Object = MibTableColumn
cmplsTunnelAutoBWUnderflowThreshBW = _CmplsTunnelAutoBWUnderflowThreshBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 10),
    _CmplsTunnelAutoBWUnderflowThreshBW_Type()
)
cmplsTunnelAutoBWUnderflowThreshBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowThreshBW.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowThreshBW.setUnits("kbps")


class _CmplsTunnelAutoBWUnderflowLimit_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWUnderflowLimit based on Unsigned32"""
    defaultValue = 1


_CmplsTunnelAutoBWUnderflowLimit_Object = MibTableColumn
cmplsTunnelAutoBWUnderflowLimit = _CmplsTunnelAutoBWUnderflowLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 11),
    _CmplsTunnelAutoBWUnderflowLimit_Type()
)
cmplsTunnelAutoBWUnderflowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowLimit.setStatus("current")


class _CmplsTunnelAutoBWApplicationFrequency_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWApplicationFrequency based on Unsigned32"""
    defaultValue = 300


_CmplsTunnelAutoBWApplicationFrequency_Object = MibTableColumn
cmplsTunnelAutoBWApplicationFrequency = _CmplsTunnelAutoBWApplicationFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 12),
    _CmplsTunnelAutoBWApplicationFrequency_Type()
)
cmplsTunnelAutoBWApplicationFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWApplicationFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWApplicationFrequency.setUnits("seconds")


class _CmplsTunnelAutoBWCollectionFrequency_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWCollectionFrequency based on Unsigned32"""
    defaultValue = 300


_CmplsTunnelAutoBWCollectionFrequency_Object = MibTableColumn
cmplsTunnelAutoBWCollectionFrequency = _CmplsTunnelAutoBWCollectionFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 13),
    _CmplsTunnelAutoBWCollectionFrequency_Type()
)
cmplsTunnelAutoBWCollectionFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWCollectionFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWCollectionFrequency.setUnits("seconds")
_CmplsTunnelAutoBWLastAppliedBW_Type = Unsigned32
_CmplsTunnelAutoBWLastAppliedBW_Object = MibTableColumn
cmplsTunnelAutoBWLastAppliedBW = _CmplsTunnelAutoBWLastAppliedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 14),
    _CmplsTunnelAutoBWLastAppliedBW_Type()
)
cmplsTunnelAutoBWLastAppliedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWLastAppliedBW.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWLastAppliedBW.setUnits("kbps")
_CmplsTunnelAutoBWApplications_Type = Counter32
_CmplsTunnelAutoBWApplications_Object = MibTableColumn
cmplsTunnelAutoBWApplications = _CmplsTunnelAutoBWApplications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 15),
    _CmplsTunnelAutoBWApplications_Type()
)
cmplsTunnelAutoBWApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWApplications.setStatus("current")


class _CmplsTunnelAutoBWLastApplicationTrigger_Type(Integer32):
    """Custom type cmplsTunnelAutoBWLastApplicationTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("applicationManual", 3),
          ("applicationNone", 1),
          ("applicationOverflow", 4),
          ("applicationPeriodic", 2),
          ("applicationUnderflow", 5))
    )


_CmplsTunnelAutoBWLastApplicationTrigger_Type.__name__ = "Integer32"
_CmplsTunnelAutoBWLastApplicationTrigger_Object = MibTableColumn
cmplsTunnelAutoBWLastApplicationTrigger = _CmplsTunnelAutoBWLastApplicationTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 16),
    _CmplsTunnelAutoBWLastApplicationTrigger_Type()
)
cmplsTunnelAutoBWLastApplicationTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWLastApplicationTrigger.setStatus("current")
_CmplsTunnelAutoBWOverflowApplications_Type = Counter32
_CmplsTunnelAutoBWOverflowApplications_Object = MibTableColumn
cmplsTunnelAutoBWOverflowApplications = _CmplsTunnelAutoBWOverflowApplications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 17),
    _CmplsTunnelAutoBWOverflowApplications_Type()
)
cmplsTunnelAutoBWOverflowApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWOverflowApplications.setStatus("current")
_CmplsTunnelAutoBWOverflowOccurrences_Type = Counter32
_CmplsTunnelAutoBWOverflowOccurrences_Object = MibTableColumn
cmplsTunnelAutoBWOverflowOccurrences = _CmplsTunnelAutoBWOverflowOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 18),
    _CmplsTunnelAutoBWOverflowOccurrences_Type()
)
cmplsTunnelAutoBWOverflowOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWOverflowOccurrences.setStatus("current")
_CmplsTunnelAutoBWUnderflowApplications_Type = Counter32
_CmplsTunnelAutoBWUnderflowApplications_Object = MibTableColumn
cmplsTunnelAutoBWUnderflowApplications = _CmplsTunnelAutoBWUnderflowApplications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 19),
    _CmplsTunnelAutoBWUnderflowApplications_Type()
)
cmplsTunnelAutoBWUnderflowApplications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowApplications.setStatus("current")
_CmplsTunnelAutoBWUnderflowOccurrences_Type = Counter32
_CmplsTunnelAutoBWUnderflowOccurrences_Object = MibTableColumn
cmplsTunnelAutoBWUnderflowOccurrences = _CmplsTunnelAutoBWUnderflowOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 20),
    _CmplsTunnelAutoBWUnderflowOccurrences_Type()
)
cmplsTunnelAutoBWUnderflowOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowOccurrences.setStatus("current")
_CmplsTunnelAutoBWUnderflowHighestBW_Type = Gauge32
_CmplsTunnelAutoBWUnderflowHighestBW_Object = MibTableColumn
cmplsTunnelAutoBWUnderflowHighestBW = _CmplsTunnelAutoBWUnderflowHighestBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 21),
    _CmplsTunnelAutoBWUnderflowHighestBW_Type()
)
cmplsTunnelAutoBWUnderflowHighestBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowHighestBW.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWUnderflowHighestBW.setUnits("kbps")
_CmplsTunnelAutoBWRequested_Type = Unsigned32
_CmplsTunnelAutoBWRequested_Object = MibTableColumn
cmplsTunnelAutoBWRequested = _CmplsTunnelAutoBWRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 22),
    _CmplsTunnelAutoBWRequested_Type()
)
cmplsTunnelAutoBWRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWRequested.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWRequested.setUnits("kpbs")
_CmplsTunnelAutoBWSignaled_Type = Unsigned32
_CmplsTunnelAutoBWSignaled_Object = MibTableColumn
cmplsTunnelAutoBWSignaled = _CmplsTunnelAutoBWSignaled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 23),
    _CmplsTunnelAutoBWSignaled_Type()
)
cmplsTunnelAutoBWSignaled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWSignaled.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWSignaled.setUnits("kpbs")
_CmplsTunnelAutoBWCollectOnlyRequested_Type = Unsigned32
_CmplsTunnelAutoBWCollectOnlyRequested_Object = MibTableColumn
cmplsTunnelAutoBWCollectOnlyRequested = _CmplsTunnelAutoBWCollectOnlyRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 24),
    _CmplsTunnelAutoBWCollectOnlyRequested_Type()
)
cmplsTunnelAutoBWCollectOnlyRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWCollectOnlyRequested.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWCollectOnlyRequested.setUnits("kpbs")
_CmplsTunnelAutoBWHighest_Type = Unsigned32
_CmplsTunnelAutoBWHighest_Object = MibTableColumn
cmplsTunnelAutoBWHighest = _CmplsTunnelAutoBWHighest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 25),
    _CmplsTunnelAutoBWHighest_Type()
)
cmplsTunnelAutoBWHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWHighest.setStatus("current")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWHighest.setUnits("kpbs")
_CmplsTunnelAutoBWCollectedSamples_Type = Counter32
_CmplsTunnelAutoBWCollectedSamples_Object = MibTableColumn
cmplsTunnelAutoBWCollectedSamples = _CmplsTunnelAutoBWCollectedSamples_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 26),
    _CmplsTunnelAutoBWCollectedSamples_Type()
)
cmplsTunnelAutoBWCollectedSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWCollectedSamples.setStatus("current")


class _CmplsTunnelAutoBWJitter_Type(Unsigned32):
    """Custom type cmplsTunnelAutoBWJitter based on Unsigned32"""
    defaultValue = 0


_CmplsTunnelAutoBWJitter_Object = MibTableColumn
cmplsTunnelAutoBWJitter = _CmplsTunnelAutoBWJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 27),
    _CmplsTunnelAutoBWJitter_Type()
)
cmplsTunnelAutoBWJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWJitter.setStatus("current")


class _CmplsTunnelAutoBWAppRejectReason_Type(Integer32):
    """Custom type cmplsTunnelAutoBWAppRejectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("applicationAllowed", 1),
          ("autoBWDisabled", 2),
          ("tunnelIsBackup", 5),
          ("tunnelIsDown", 3),
          ("tunnelIsFRR", 4),
          ("tunnelIsLockDown", 6))
    )


_CmplsTunnelAutoBWAppRejectReason_Type.__name__ = "Integer32"
_CmplsTunnelAutoBWAppRejectReason_Object = MibTableColumn
cmplsTunnelAutoBWAppRejectReason = _CmplsTunnelAutoBWAppRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 1, 1, 28),
    _CmplsTunnelAutoBWAppRejectReason_Type()
)
cmplsTunnelAutoBWAppRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTunnelAutoBWAppRejectReason.setStatus("current")
_CmplsTeTunnelReasonTable_Object = MibTable
cmplsTeTunnelReasonTable = _CmplsTeTunnelReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2)
)
if mibBuilder.loadTexts:
    cmplsTeTunnelReasonTable.setStatus("current")
_CmplsTeTunnelReasonEntry_Object = MibTableRow
cmplsTeTunnelReasonEntry = _CmplsTeTunnelReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1)
)
cmplsTeTunnelReasonEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsTeTunnelReasonEntry.setStatus("current")


class _CmplsTunnelReoptReason_Type(Integer32):
    """Custom type cmplsTunnelReoptReason based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("affinityPathVerificationFail", 18),
          ("autoBandwidth", 13),
          ("bandwidthAdjustment", 6),
          ("bandwidthCLIChange", 3),
          ("bandwidthChange", 12),
          ("bandwidthOverflow", 4),
          ("bandwidthUnderflow", 5),
          ("bfdSessionTypeChange", 26),
          ("cliRequest", 8),
          ("costLimitPathVerificationFail", 21),
          ("destChange", 25),
          ("dueToMaximumMetric", 15),
          ("fastReRoute", 7),
          ("iEPChange", 23),
          ("iEPEnableReoptimization", 17),
          ("linkupReopt", 22),
          ("metricTypeChange", 9),
          ("pathProtectionSwitchover", 16),
          ("periodicTimerExpiry", 2),
          ("poChange", 24),
          ("poSwitchoverTrigger", 11),
          ("preferredPathExists", 10),
          ("preferredTreeExists", 20),
          ("remergeError", 14),
          ("softPreemption", 19),
          ("unknown", 1))
    )


_CmplsTunnelReoptReason_Type.__name__ = "Integer32"
_CmplsTunnelReoptReason_Object = MibTableColumn
cmplsTunnelReoptReason = _CmplsTunnelReoptReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1, 1),
    _CmplsTunnelReoptReason_Type()
)
cmplsTunnelReoptReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTunnelReoptReason.setStatus("current")


class _CmplsTunnelInsuffBWFailedOperation_Type(Integer32):
    """Custom type cmplsTunnelInsuffBWFailedOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failedToReoptimize", 3),
          ("failedToSetup", 2),
          ("unknown", 1))
    )


_CmplsTunnelInsuffBWFailedOperation_Type.__name__ = "Integer32"
_CmplsTunnelInsuffBWFailedOperation_Object = MibTableColumn
cmplsTunnelInsuffBWFailedOperation = _CmplsTunnelInsuffBWFailedOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1, 2),
    _CmplsTunnelInsuffBWFailedOperation_Type()
)
cmplsTunnelInsuffBWFailedOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTunnelInsuffBWFailedOperation.setStatus("current")


class _CmplsTunnelPreemptionType_Type(Integer32):
    """Custom type cmplsTunnelPreemptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("frrSoftPreemption", 4),
          ("hardPreemption", 2),
          ("softPreemption", 3),
          ("unknown", 1))
    )


_CmplsTunnelPreemptionType_Type.__name__ = "Integer32"
_CmplsTunnelPreemptionType_Object = MibTableColumn
cmplsTunnelPreemptionType = _CmplsTunnelPreemptionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1, 3),
    _CmplsTunnelPreemptionType_Type()
)
cmplsTunnelPreemptionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTunnelPreemptionType.setStatus("current")
_CmplsTunnelPreemptionLinkAddrType_Type = InetAddressType
_CmplsTunnelPreemptionLinkAddrType_Object = MibTableColumn
cmplsTunnelPreemptionLinkAddrType = _CmplsTunnelPreemptionLinkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1, 4),
    _CmplsTunnelPreemptionLinkAddrType_Type()
)
cmplsTunnelPreemptionLinkAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTunnelPreemptionLinkAddrType.setStatus("current")
_CmplsTunnelPreemptionLinkAddr_Type = InetAddress
_CmplsTunnelPreemptionLinkAddr_Object = MibTableColumn
cmplsTunnelPreemptionLinkAddr = _CmplsTunnelPreemptionLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1, 5),
    _CmplsTunnelPreemptionLinkAddr_Type()
)
cmplsTunnelPreemptionLinkAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTunnelPreemptionLinkAddr.setStatus("current")


class _CmplsTunnelReRoutePendingClearReason_Type(Integer32):
    """Custom type cmplsTunnelReRoutePendingClearReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reinstated", 3),
          ("reoptimized", 2),
          ("unknown", 1))
    )


_CmplsTunnelReRoutePendingClearReason_Type.__name__ = "Integer32"
_CmplsTunnelReRoutePendingClearReason_Object = MibTableColumn
cmplsTunnelReRoutePendingClearReason = _CmplsTunnelReRoutePendingClearReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 2, 1, 6),
    _CmplsTunnelReRoutePendingClearReason_Type()
)
cmplsTunnelReRoutePendingClearReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTunnelReRoutePendingClearReason.setStatus("current")
_CmplsTeTunnelFailReasonTable_Object = MibTable
cmplsTeTunnelFailReasonTable = _CmplsTeTunnelFailReasonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 3)
)
if mibBuilder.loadTexts:
    cmplsTeTunnelFailReasonTable.setStatus("current")
_CmplsTeTunnelFailReasonEntry_Object = MibTableRow
cmplsTeTunnelFailReasonEntry = _CmplsTeTunnelFailReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 3, 1)
)
cmplsTeTunnelFailReasonEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopListIndex"),
)
if mibBuilder.loadTexts:
    cmplsTeTunnelFailReasonEntry.setStatus("current")


class _CmplsTeFailReasonType_Type(Integer32):
    """Custom type cmplsTeFailReasonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bfd", 2),
          ("generalTe", 3),
          ("unknown", 1))
    )


_CmplsTeFailReasonType_Type.__name__ = "Integer32"
_CmplsTeFailReasonType_Object = MibTableColumn
cmplsTeFailReasonType = _CmplsTeFailReasonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 3, 1, 1),
    _CmplsTeFailReasonType_Type()
)
cmplsTeFailReasonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeFailReasonType.setStatus("current")
_CmplsTeFailReason_Type = Integer32
_CmplsTeFailReason_Object = MibTableColumn
cmplsTeFailReason = _CmplsTeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 3, 1, 2),
    _CmplsTeFailReason_Type()
)
cmplsTeFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmplsTeFailReason.setStatus("deprecated")


class _CmplsTeFailReasonRev_Type(Integer32):
    """Custom type cmplsTeFailReasonRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              21)
        )
    )
    namedValues = NamedValues(
        *(("administrativelyDown", 7),
          ("bfdSessionBringupTimeout", 21),
          ("concatenatedPathDown", 6),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("forwardingPlaneReset", 4),
          ("neighborSignaledSessionDown", 3),
          ("noDiagnostic", 0),
          ("pathDown", 5),
          ("reverseConcatenatedPathDown", 8),
          ("unknown", 9))
    )


_CmplsTeFailReasonRev_Type.__name__ = "Integer32"
_CmplsTeFailReasonRev_Object = MibTableColumn
cmplsTeFailReasonRev = _CmplsTeFailReasonRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 3, 1, 3),
    _CmplsTeFailReasonRev_Type()
)
cmplsTeFailReasonRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmplsTeFailReasonRev.setStatus("current")
_CmplsTunnelLoadshareTable_Object = MibTable
cmplsTunnelLoadshareTable = _CmplsTunnelLoadshareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 4)
)
if mibBuilder.loadTexts:
    cmplsTunnelLoadshareTable.setStatus("current")
_CmplsTunnelLoadshareEntry_Object = MibTableRow
cmplsTunnelLoadshareEntry = _CmplsTunnelLoadshareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 4, 1)
)
cmplsTunnelLoadshareEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    cmplsTunnelLoadshareEntry.setStatus("current")


class _CmplsTunnelLoadShare_Type(Unsigned32):
    """Custom type cmplsTunnelLoadShare based on Unsigned32"""
    defaultValue = 0


_CmplsTunnelLoadShare_Object = MibTableColumn
cmplsTunnelLoadShare = _CmplsTunnelLoadShare_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 4, 1, 1),
    _CmplsTunnelLoadShare_Type()
)
cmplsTunnelLoadShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTunnelLoadShare.setStatus("current")
_CmplsTeStdExtMIBObjectsGlobal_ObjectIdentity = ObjectIdentity
cmplsTeStdExtMIBObjectsGlobal = _CmplsTeStdExtMIBObjectsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 5)
)


class _CmplsTeLoadshareBalance_Type(Integer32):
    """Custom type cmplsTeLoadshareBalance based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("equal", 0),
          ("unequal", 1))
    )


_CmplsTeLoadshareBalance_Type.__name__ = "Integer32"
_CmplsTeLoadshareBalance_Object = MibScalar
cmplsTeLoadshareBalance = _CmplsTeLoadshareBalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 1, 5, 1),
    _CmplsTeLoadshareBalance_Type()
)
cmplsTeLoadshareBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmplsTeLoadshareBalance.setStatus("current")
_CmplsTeStdExtMIBConform_ObjectIdentity = ObjectIdentity
cmplsTeStdExtMIBConform = _CmplsTeStdExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2)
)
_CmplsTeStdExtMIBCompliances_ObjectIdentity = ObjectIdentity
cmplsTeStdExtMIBCompliances = _CmplsTeStdExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 1)
)
_CmplsTeStdExtMIBGroups_ObjectIdentity = ObjectIdentity
cmplsTeStdExtMIBGroups = _CmplsTeStdExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2)
)

# Managed Objects groups

cmplsTeStdExtMIBAutoBWObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 1)
)
cmplsTeStdExtMIBAutoBWObjectGroup.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWStatus"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWMin"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWMax"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWAdjThreshPercs"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWAdjThreshBW"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWApplicationFrequency"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWCollectionFrequency"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWLastAppliedBW"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWApplications"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWLastApplicationTrigger"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWOverflowApplications"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWOverflowOccurrences"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWUnderflowApplications"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWUnderflowOccurrences"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWUnderflowHighestBW"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWRequested"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWSignaled"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWCollectOnlyRequested"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWHighest"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWCollectedSamples"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWAppRejectReason"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBAutoBWObjectGroup.setStatus("current")

cmplsTeStdExtMIBAutoBWOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 2)
)
cmplsTeStdExtMIBAutoBWOptionalGroup.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWOverflowThreshPercs"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWOverflowThreshBW"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWOverflowLimit"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWUnderflowThreshPercs"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWUnderflowThreshBW"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWUnderflowLimit"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelAutoBWJitter"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBAutoBWOptionalGroup.setStatus("current")

cmplsTeStdExtMIBTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 3)
)
cmplsTeStdExtMIBTrapObjectsGroup.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelReoptReason"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelInsuffBWFailedOperation"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionLinkAddrType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionLinkAddr"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBTrapObjectsGroup.setStatus("deprecated")

cmplsTeStdExtMIBTrapObjectsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 4)
)
cmplsTeStdExtMIBTrapObjectsGroupRev1.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelReoptReason"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelInsuffBWFailedOperation"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionLinkAddrType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionLinkAddr"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelReRoutePendingClearReason"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBTrapObjectsGroupRev1.setStatus("current")

cmplsTeStdExtMIBFailTeTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 7)
)
cmplsTeStdExtMIBFailTeTrapObjectsGroup.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTeFailReasonType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTeFailReason"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBFailTeTrapObjectsGroup.setStatus("deprecated")

cmplsTeStdExtMIBLoadShareObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 8)
)
cmplsTeStdExtMIBLoadShareObjectsGroup.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelLoadShare"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTeLoadshareBalance"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBLoadShareObjectsGroup.setStatus("current")

cmplsTeStdExtMIBFailTeTrapObjectsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 9)
)
cmplsTeStdExtMIBFailTeTrapObjectsGroupRev1.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTeFailReasonType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTeFailReasonRev"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBFailTeTrapObjectsGroupRev1.setStatus("current")


# Notification objects

cmplsTunnelPreempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 0, 1)
)
cmplsTunnelPreempt.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelName"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionLinkAddrType"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreemptionLinkAddr"))
)
if mibBuilder.loadTexts:
    cmplsTunnelPreempt.setStatus(
        "current"
    )

cmplsTunnelInsuffBW = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 0, 2)
)
cmplsTunnelInsuffBW.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelName"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelInsuffBWFailedOperation"))
)
if mibBuilder.loadTexts:
    cmplsTunnelInsuffBW.setStatus(
        "current"
    )

cmplsTunnelReRoutePending = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 0, 3)
)
cmplsTunnelReRoutePending.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelName"))
)
if mibBuilder.loadTexts:
    cmplsTunnelReRoutePending.setStatus(
        "current"
    )

cmplsTunnelReRoutePendingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 0, 4)
)
cmplsTunnelReRoutePendingClear.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelAdminStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelOperStatus"),
        ("MPLS-TE-STD-MIB", "mplsTunnelName"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelReRoutePendingClearReason"))
)
if mibBuilder.loadTexts:
    cmplsTunnelReRoutePendingClear.setStatus(
        "current"
    )

cmplsTunnelBringupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 0, 5)
)
cmplsTunnelBringupFail.setObjects(
      *(("MPLS-TE-STD-MIB", "mplsTunnelName"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTeFailReasonType"))
)
if mibBuilder.loadTexts:
    cmplsTunnelBringupFail.setStatus(
        "current"
    )


# Notifications groups

cmplsTeStdExtMIBTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 5)
)
cmplsTeStdExtMIBTrapGroup.setObjects(
      *(("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelPreempt"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelInsuffBW"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelReRoutePending"),
        ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelReRoutePendingClear"))
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBTrapGroup.setStatus(
        "current"
    )

cmplsTeStdExtMIBFailTeTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 2, 6)
)
cmplsTeStdExtMIBFailTeTrapGroup.setObjects(
    ("CISCO-MPLS-TE-STD-EXT-MIB", "cmplsTunnelBringupFail")
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBFailTeTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmplsTeStdExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBCompliance.setStatus(
        "deprecated"
    )

cmplsTeStdExtMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBCompliancesRev1.setStatus(
        "deprecated"
    )

cmplsTeStdExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBComplianceRev2.setStatus(
        "deprecated"
    )

cmplsTeStdExtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBComplianceRev3.setStatus(
        "deprecated"
    )

cmplsTeStdExtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 738, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cmplsTeStdExtMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MPLS-TE-STD-EXT-MIB",
    **{"CmplsTeTunnelDiag": CmplsTeTunnelDiag,
       "CmplsTunnelBWPercent": CmplsTunnelBWPercent,
       "cmplsTeStdExtMIB": cmplsTeStdExtMIB,
       "cmplsTeStdExtMIBNotifs": cmplsTeStdExtMIBNotifs,
       "cmplsTunnelPreempt": cmplsTunnelPreempt,
       "cmplsTunnelInsuffBW": cmplsTunnelInsuffBW,
       "cmplsTunnelReRoutePending": cmplsTunnelReRoutePending,
       "cmplsTunnelReRoutePendingClear": cmplsTunnelReRoutePendingClear,
       "cmplsTunnelBringupFail": cmplsTunnelBringupFail,
       "cmplsTeStdExtMIBObjects": cmplsTeStdExtMIBObjects,
       "cmplsTunnelAutoBWTable": cmplsTunnelAutoBWTable,
       "cmplsTunnelAutoBWEntry": cmplsTunnelAutoBWEntry,
       "cmplsTunnelAutoBWStatus": cmplsTunnelAutoBWStatus,
       "cmplsTunnelAutoBWMin": cmplsTunnelAutoBWMin,
       "cmplsTunnelAutoBWMax": cmplsTunnelAutoBWMax,
       "cmplsTunnelAutoBWAdjThreshPercs": cmplsTunnelAutoBWAdjThreshPercs,
       "cmplsTunnelAutoBWAdjThreshBW": cmplsTunnelAutoBWAdjThreshBW,
       "cmplsTunnelAutoBWOverflowThreshPercs": cmplsTunnelAutoBWOverflowThreshPercs,
       "cmplsTunnelAutoBWOverflowThreshBW": cmplsTunnelAutoBWOverflowThreshBW,
       "cmplsTunnelAutoBWOverflowLimit": cmplsTunnelAutoBWOverflowLimit,
       "cmplsTunnelAutoBWUnderflowThreshPercs": cmplsTunnelAutoBWUnderflowThreshPercs,
       "cmplsTunnelAutoBWUnderflowThreshBW": cmplsTunnelAutoBWUnderflowThreshBW,
       "cmplsTunnelAutoBWUnderflowLimit": cmplsTunnelAutoBWUnderflowLimit,
       "cmplsTunnelAutoBWApplicationFrequency": cmplsTunnelAutoBWApplicationFrequency,
       "cmplsTunnelAutoBWCollectionFrequency": cmplsTunnelAutoBWCollectionFrequency,
       "cmplsTunnelAutoBWLastAppliedBW": cmplsTunnelAutoBWLastAppliedBW,
       "cmplsTunnelAutoBWApplications": cmplsTunnelAutoBWApplications,
       "cmplsTunnelAutoBWLastApplicationTrigger": cmplsTunnelAutoBWLastApplicationTrigger,
       "cmplsTunnelAutoBWOverflowApplications": cmplsTunnelAutoBWOverflowApplications,
       "cmplsTunnelAutoBWOverflowOccurrences": cmplsTunnelAutoBWOverflowOccurrences,
       "cmplsTunnelAutoBWUnderflowApplications": cmplsTunnelAutoBWUnderflowApplications,
       "cmplsTunnelAutoBWUnderflowOccurrences": cmplsTunnelAutoBWUnderflowOccurrences,
       "cmplsTunnelAutoBWUnderflowHighestBW": cmplsTunnelAutoBWUnderflowHighestBW,
       "cmplsTunnelAutoBWRequested": cmplsTunnelAutoBWRequested,
       "cmplsTunnelAutoBWSignaled": cmplsTunnelAutoBWSignaled,
       "cmplsTunnelAutoBWCollectOnlyRequested": cmplsTunnelAutoBWCollectOnlyRequested,
       "cmplsTunnelAutoBWHighest": cmplsTunnelAutoBWHighest,
       "cmplsTunnelAutoBWCollectedSamples": cmplsTunnelAutoBWCollectedSamples,
       "cmplsTunnelAutoBWJitter": cmplsTunnelAutoBWJitter,
       "cmplsTunnelAutoBWAppRejectReason": cmplsTunnelAutoBWAppRejectReason,
       "cmplsTeTunnelReasonTable": cmplsTeTunnelReasonTable,
       "cmplsTeTunnelReasonEntry": cmplsTeTunnelReasonEntry,
       "cmplsTunnelReoptReason": cmplsTunnelReoptReason,
       "cmplsTunnelInsuffBWFailedOperation": cmplsTunnelInsuffBWFailedOperation,
       "cmplsTunnelPreemptionType": cmplsTunnelPreemptionType,
       "cmplsTunnelPreemptionLinkAddrType": cmplsTunnelPreemptionLinkAddrType,
       "cmplsTunnelPreemptionLinkAddr": cmplsTunnelPreemptionLinkAddr,
       "cmplsTunnelReRoutePendingClearReason": cmplsTunnelReRoutePendingClearReason,
       "cmplsTeTunnelFailReasonTable": cmplsTeTunnelFailReasonTable,
       "cmplsTeTunnelFailReasonEntry": cmplsTeTunnelFailReasonEntry,
       "cmplsTeFailReasonType": cmplsTeFailReasonType,
       "cmplsTeFailReason": cmplsTeFailReason,
       "cmplsTeFailReasonRev": cmplsTeFailReasonRev,
       "cmplsTunnelLoadshareTable": cmplsTunnelLoadshareTable,
       "cmplsTunnelLoadshareEntry": cmplsTunnelLoadshareEntry,
       "cmplsTunnelLoadShare": cmplsTunnelLoadShare,
       "cmplsTeStdExtMIBObjectsGlobal": cmplsTeStdExtMIBObjectsGlobal,
       "cmplsTeLoadshareBalance": cmplsTeLoadshareBalance,
       "cmplsTeStdExtMIBConform": cmplsTeStdExtMIBConform,
       "cmplsTeStdExtMIBCompliances": cmplsTeStdExtMIBCompliances,
       "cmplsTeStdExtMIBCompliance": cmplsTeStdExtMIBCompliance,
       "cmplsTeStdExtMIBCompliancesRev1": cmplsTeStdExtMIBCompliancesRev1,
       "cmplsTeStdExtMIBComplianceRev2": cmplsTeStdExtMIBComplianceRev2,
       "cmplsTeStdExtMIBComplianceRev3": cmplsTeStdExtMIBComplianceRev3,
       "cmplsTeStdExtMIBComplianceRev4": cmplsTeStdExtMIBComplianceRev4,
       "cmplsTeStdExtMIBGroups": cmplsTeStdExtMIBGroups,
       "cmplsTeStdExtMIBAutoBWObjectGroup": cmplsTeStdExtMIBAutoBWObjectGroup,
       "cmplsTeStdExtMIBAutoBWOptionalGroup": cmplsTeStdExtMIBAutoBWOptionalGroup,
       "cmplsTeStdExtMIBTrapObjectsGroup": cmplsTeStdExtMIBTrapObjectsGroup,
       "cmplsTeStdExtMIBTrapObjectsGroupRev1": cmplsTeStdExtMIBTrapObjectsGroupRev1,
       "cmplsTeStdExtMIBTrapGroup": cmplsTeStdExtMIBTrapGroup,
       "cmplsTeStdExtMIBFailTeTrapGroup": cmplsTeStdExtMIBFailTeTrapGroup,
       "cmplsTeStdExtMIBFailTeTrapObjectsGroup": cmplsTeStdExtMIBFailTeTrapObjectsGroup,
       "cmplsTeStdExtMIBLoadShareObjectsGroup": cmplsTeStdExtMIBLoadShareObjectsGroup,
       "cmplsTeStdExtMIBFailTeTrapObjectsGroupRev1": cmplsTeStdExtMIBFailTeTrapObjectsGroupRev1}
)
