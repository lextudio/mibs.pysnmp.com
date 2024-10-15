# SNMP MIB module (ASCEND-MIBBWALLOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBBWALLOC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:18 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibbandwidthAllocProfile_ObjectIdentity = ObjectIdentity
mibbandwidthAllocProfile = _MibbandwidthAllocProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 29)
)
_MibbandwidthAllocProfileTable_Object = MibTable
mibbandwidthAllocProfileTable = _MibbandwidthAllocProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 1)
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfileTable.setStatus("mandatory")
_MibbandwidthAllocProfileEntry_Object = MibTableRow
mibbandwidthAllocProfileEntry = _MibbandwidthAllocProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 1, 1)
)
mibbandwidthAllocProfileEntry.setIndexNames(
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfileEntry.setStatus("mandatory")
_BandwidthAllocProfile_Index_o_Type = Integer32
_BandwidthAllocProfile_Index_o_Object = MibScalar
bandwidthAllocProfile_Index_o = _BandwidthAllocProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 1, 1, 1),
    _BandwidthAllocProfile_Index_o_Type()
)
bandwidthAllocProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_Index_o.setStatus("mandatory")


class _BandwidthAllocProfile_Action_o_Type(Integer32):
    """Custom type bandwidthAllocProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_BandwidthAllocProfile_Action_o_Type.__name__ = "Integer32"
_BandwidthAllocProfile_Action_o_Object = MibScalar
bandwidthAllocProfile_Action_o = _BandwidthAllocProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 1, 1, 2),
    _BandwidthAllocProfile_Action_o_Type()
)
bandwidthAllocProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_Action_o.setStatus("mandatory")
_MibbandwidthAllocProfile_TrafficShapersTable_Object = MibTable
mibbandwidthAllocProfile_TrafficShapersTable = _MibbandwidthAllocProfile_TrafficShapersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2)
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfile_TrafficShapersTable.setStatus("mandatory")
_MibbandwidthAllocProfile_TrafficShapersEntry_Object = MibTableRow
mibbandwidthAllocProfile_TrafficShapersEntry = _MibbandwidthAllocProfile_TrafficShapersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1)
)
mibbandwidthAllocProfile_TrafficShapersEntry.setIndexNames(
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-TrafficShapers-Index-o"),
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-TrafficShapers-Index1-o"),
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfile_TrafficShapersEntry.setStatus("mandatory")
_BandwidthAllocProfile_TrafficShapers_Index_o_Type = Integer32
_BandwidthAllocProfile_TrafficShapers_Index_o_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_Index_o = _BandwidthAllocProfile_TrafficShapers_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 1),
    _BandwidthAllocProfile_TrafficShapers_Index_o_Type()
)
bandwidthAllocProfile_TrafficShapers_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_Index_o.setStatus("mandatory")
_BandwidthAllocProfile_TrafficShapers_Index1_o_Type = Integer32
_BandwidthAllocProfile_TrafficShapers_Index1_o_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_Index1_o = _BandwidthAllocProfile_TrafficShapers_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 2),
    _BandwidthAllocProfile_TrafficShapers_Index1_o_Type()
)
bandwidthAllocProfile_TrafficShapers_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_Index1_o.setStatus("mandatory")


class _BandwidthAllocProfile_TrafficShapers_Enabled_Type(Integer32):
    """Custom type bandwidthAllocProfile_TrafficShapers_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BandwidthAllocProfile_TrafficShapers_Enabled_Type.__name__ = "Integer32"
_BandwidthAllocProfile_TrafficShapers_Enabled_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_Enabled = _BandwidthAllocProfile_TrafficShapers_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 3),
    _BandwidthAllocProfile_TrafficShapers_Enabled_Type()
)
bandwidthAllocProfile_TrafficShapers_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_Enabled.setStatus("mandatory")
_BandwidthAllocProfile_TrafficShapers_BitRate_Type = Integer32
_BandwidthAllocProfile_TrafficShapers_BitRate_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_BitRate = _BandwidthAllocProfile_TrafficShapers_BitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 4),
    _BandwidthAllocProfile_TrafficShapers_BitRate_Type()
)
bandwidthAllocProfile_TrafficShapers_BitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_BitRate.setStatus("mandatory")
_BandwidthAllocProfile_TrafficShapers_PeakRate_Type = Integer32
_BandwidthAllocProfile_TrafficShapers_PeakRate_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_PeakRate = _BandwidthAllocProfile_TrafficShapers_PeakRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 5),
    _BandwidthAllocProfile_TrafficShapers_PeakRate_Type()
)
bandwidthAllocProfile_TrafficShapers_PeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_PeakRate.setStatus("mandatory")
_BandwidthAllocProfile_TrafficShapers_MaxBurstSize_Type = Integer32
_BandwidthAllocProfile_TrafficShapers_MaxBurstSize_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_MaxBurstSize = _BandwidthAllocProfile_TrafficShapers_MaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 6),
    _BandwidthAllocProfile_TrafficShapers_MaxBurstSize_Type()
)
bandwidthAllocProfile_TrafficShapers_MaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_MaxBurstSize.setStatus("mandatory")


class _BandwidthAllocProfile_TrafficShapers_Aggregate_Type(Integer32):
    """Custom type bandwidthAllocProfile_TrafficShapers_Aggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BandwidthAllocProfile_TrafficShapers_Aggregate_Type.__name__ = "Integer32"
_BandwidthAllocProfile_TrafficShapers_Aggregate_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_Aggregate = _BandwidthAllocProfile_TrafficShapers_Aggregate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 7),
    _BandwidthAllocProfile_TrafficShapers_Aggregate_Type()
)
bandwidthAllocProfile_TrafficShapers_Aggregate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_Aggregate.setStatus("mandatory")
_BandwidthAllocProfile_TrafficShapers_Priority_Type = Integer32
_BandwidthAllocProfile_TrafficShapers_Priority_Object = MibScalar
bandwidthAllocProfile_TrafficShapers_Priority = _BandwidthAllocProfile_TrafficShapers_Priority_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 2, 1, 8),
    _BandwidthAllocProfile_TrafficShapers_Priority_Type()
)
bandwidthAllocProfile_TrafficShapers_Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_TrafficShapers_Priority.setStatus("mandatory")
_MibbandwidthAllocProfile_BandwidthConfigTable_Object = MibTable
mibbandwidthAllocProfile_BandwidthConfigTable = _MibbandwidthAllocProfile_BandwidthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 4)
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfile_BandwidthConfigTable.setStatus("mandatory")
_MibbandwidthAllocProfile_BandwidthConfigEntry_Object = MibTableRow
mibbandwidthAllocProfile_BandwidthConfigEntry = _MibbandwidthAllocProfile_BandwidthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 4, 1)
)
mibbandwidthAllocProfile_BandwidthConfigEntry.setIndexNames(
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-BandwidthConfig-Index-o"),
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-BandwidthConfig-Index1-o"),
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfile_BandwidthConfigEntry.setStatus("mandatory")
_BandwidthAllocProfile_BandwidthConfig_Index_o_Type = Integer32
_BandwidthAllocProfile_BandwidthConfig_Index_o_Object = MibScalar
bandwidthAllocProfile_BandwidthConfig_Index_o = _BandwidthAllocProfile_BandwidthConfig_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 4, 1, 1),
    _BandwidthAllocProfile_BandwidthConfig_Index_o_Type()
)
bandwidthAllocProfile_BandwidthConfig_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_BandwidthConfig_Index_o.setStatus("mandatory")
_BandwidthAllocProfile_BandwidthConfig_Index1_o_Type = Integer32
_BandwidthAllocProfile_BandwidthConfig_Index1_o_Object = MibScalar
bandwidthAllocProfile_BandwidthConfig_Index1_o = _BandwidthAllocProfile_BandwidthConfig_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 4, 1, 2),
    _BandwidthAllocProfile_BandwidthConfig_Index1_o_Type()
)
bandwidthAllocProfile_BandwidthConfig_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_BandwidthConfig_Index1_o.setStatus("mandatory")
_BandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth_Type = Integer32
_BandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth_Object = MibScalar
bandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth = _BandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 4, 1, 3),
    _BandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth_Type()
)
bandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth.setStatus("mandatory")
_BandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth_Type = Integer32
_BandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth_Object = MibScalar
bandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth = _BandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 4, 1, 4),
    _BandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth_Type()
)
bandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth.setStatus("mandatory")
_MibbandwidthAllocProfile_SlotVpiVciRangeTable_Object = MibTable
mibbandwidthAllocProfile_SlotVpiVciRangeTable = _MibbandwidthAllocProfile_SlotVpiVciRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 5)
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfile_SlotVpiVciRangeTable.setStatus("mandatory")
_MibbandwidthAllocProfile_SlotVpiVciRangeEntry_Object = MibTableRow
mibbandwidthAllocProfile_SlotVpiVciRangeEntry = _MibbandwidthAllocProfile_SlotVpiVciRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 5, 1)
)
mibbandwidthAllocProfile_SlotVpiVciRangeEntry.setIndexNames(
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-SlotVpiVciRange-Index-o"),
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthAllocProfile-SlotVpiVciRange-Index1-o"),
)
if mibBuilder.loadTexts:
    mibbandwidthAllocProfile_SlotVpiVciRangeEntry.setStatus("mandatory")
_BandwidthAllocProfile_SlotVpiVciRange_Index_o_Type = Integer32
_BandwidthAllocProfile_SlotVpiVciRange_Index_o_Object = MibScalar
bandwidthAllocProfile_SlotVpiVciRange_Index_o = _BandwidthAllocProfile_SlotVpiVciRange_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 5, 1, 1),
    _BandwidthAllocProfile_SlotVpiVciRange_Index_o_Type()
)
bandwidthAllocProfile_SlotVpiVciRange_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_SlotVpiVciRange_Index_o.setStatus("mandatory")
_BandwidthAllocProfile_SlotVpiVciRange_Index1_o_Type = Integer32
_BandwidthAllocProfile_SlotVpiVciRange_Index1_o_Object = MibScalar
bandwidthAllocProfile_SlotVpiVciRange_Index1_o = _BandwidthAllocProfile_SlotVpiVciRange_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 5, 1, 2),
    _BandwidthAllocProfile_SlotVpiVciRange_Index1_o_Type()
)
bandwidthAllocProfile_SlotVpiVciRange_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_SlotVpiVciRange_Index1_o.setStatus("mandatory")


class _BandwidthAllocProfile_SlotVpiVciRange_Type(Integer32):
    """Custom type bandwidthAllocProfile_SlotVpiVciRange based on Integer32"""
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
        *(("notApplicable", 5),
          ("vpi015Vci32127", 3),
          ("vpi01Vci321023", 6),
          ("vpi031Vci3263", 4),
          ("vpi03Vci32511", 1),
          ("vpi07Vci32255", 2))
    )


_BandwidthAllocProfile_SlotVpiVciRange_Type.__name__ = "Integer32"
_BandwidthAllocProfile_SlotVpiVciRange_Object = MibScalar
bandwidthAllocProfile_SlotVpiVciRange = _BandwidthAllocProfile_SlotVpiVciRange_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 29, 5, 1, 3),
    _BandwidthAllocProfile_SlotVpiVciRange_Type()
)
bandwidthAllocProfile_SlotVpiVciRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocProfile_SlotVpiVciRange.setStatus("mandatory")
_MibbandwidthStatsProfile_ObjectIdentity = ObjectIdentity
mibbandwidthStatsProfile = _MibbandwidthStatsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 64)
)
_MibbandwidthStatsProfileTable_Object = MibTable
mibbandwidthStatsProfileTable = _MibbandwidthStatsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1)
)
if mibBuilder.loadTexts:
    mibbandwidthStatsProfileTable.setStatus("mandatory")
_MibbandwidthStatsProfileEntry_Object = MibTableRow
mibbandwidthStatsProfileEntry = _MibbandwidthStatsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1, 1)
)
mibbandwidthStatsProfileEntry.setIndexNames(
    (0, "ASCEND-MIBBWALLOC-MIB", "bandwidthStatsProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibbandwidthStatsProfileEntry.setStatus("mandatory")
_BandwidthStatsProfile_Index_o_Type = Integer32
_BandwidthStatsProfile_Index_o_Object = MibScalar
bandwidthStatsProfile_Index_o = _BandwidthStatsProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1, 1, 1),
    _BandwidthStatsProfile_Index_o_Type()
)
bandwidthStatsProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthStatsProfile_Index_o.setStatus("mandatory")
_BandwidthStatsProfile_MaxUpstreamBandwidth_Type = Integer32
_BandwidthStatsProfile_MaxUpstreamBandwidth_Object = MibScalar
bandwidthStatsProfile_MaxUpstreamBandwidth = _BandwidthStatsProfile_MaxUpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1, 1, 2),
    _BandwidthStatsProfile_MaxUpstreamBandwidth_Type()
)
bandwidthStatsProfile_MaxUpstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthStatsProfile_MaxUpstreamBandwidth.setStatus("mandatory")
_BandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks_Type = Integer32
_BandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks_Object = MibScalar
bandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks = _BandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1, 1, 3),
    _BandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks_Type()
)
bandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks.setStatus("mandatory")
_BandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks_Type = Integer32
_BandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks_Object = MibScalar
bandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks = _BandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1, 1, 4),
    _BandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks_Type()
)
bandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks.setStatus("mandatory")


class _BandwidthStatsProfile_Action_o_Type(Integer32):
    """Custom type bandwidthStatsProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_BandwidthStatsProfile_Action_o_Type.__name__ = "Integer32"
_BandwidthStatsProfile_Action_o_Object = MibScalar
bandwidthStatsProfile_Action_o = _BandwidthStatsProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 64, 1, 1, 5),
    _BandwidthStatsProfile_Action_o_Type()
)
bandwidthStatsProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthStatsProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBBWALLOC-MIB",
    **{"DisplayString": DisplayString,
       "mibbandwidthAllocProfile": mibbandwidthAllocProfile,
       "mibbandwidthAllocProfileTable": mibbandwidthAllocProfileTable,
       "mibbandwidthAllocProfileEntry": mibbandwidthAllocProfileEntry,
       "bandwidthAllocProfile-Index-o": bandwidthAllocProfile_Index_o,
       "bandwidthAllocProfile-Action-o": bandwidthAllocProfile_Action_o,
       "mibbandwidthAllocProfile-TrafficShapersTable": mibbandwidthAllocProfile_TrafficShapersTable,
       "mibbandwidthAllocProfile-TrafficShapersEntry": mibbandwidthAllocProfile_TrafficShapersEntry,
       "bandwidthAllocProfile-TrafficShapers-Index-o": bandwidthAllocProfile_TrafficShapers_Index_o,
       "bandwidthAllocProfile-TrafficShapers-Index1-o": bandwidthAllocProfile_TrafficShapers_Index1_o,
       "bandwidthAllocProfile-TrafficShapers-Enabled": bandwidthAllocProfile_TrafficShapers_Enabled,
       "bandwidthAllocProfile-TrafficShapers-BitRate": bandwidthAllocProfile_TrafficShapers_BitRate,
       "bandwidthAllocProfile-TrafficShapers-PeakRate": bandwidthAllocProfile_TrafficShapers_PeakRate,
       "bandwidthAllocProfile-TrafficShapers-MaxBurstSize": bandwidthAllocProfile_TrafficShapers_MaxBurstSize,
       "bandwidthAllocProfile-TrafficShapers-Aggregate": bandwidthAllocProfile_TrafficShapers_Aggregate,
       "bandwidthAllocProfile-TrafficShapers-Priority": bandwidthAllocProfile_TrafficShapers_Priority,
       "mibbandwidthAllocProfile-BandwidthConfigTable": mibbandwidthAllocProfile_BandwidthConfigTable,
       "mibbandwidthAllocProfile-BandwidthConfigEntry": mibbandwidthAllocProfile_BandwidthConfigEntry,
       "bandwidthAllocProfile-BandwidthConfig-Index-o": bandwidthAllocProfile_BandwidthConfig_Index_o,
       "bandwidthAllocProfile-BandwidthConfig-Index1-o": bandwidthAllocProfile_BandwidthConfig_Index1_o,
       "bandwidthAllocProfile-BandwidthConfig-AllowMaxUpStreamBandwidth": bandwidthAllocProfile_BandwidthConfig_AllowMaxUpStreamBandwidth,
       "bandwidthAllocProfile-BandwidthConfig-AllowGuaranteedUpStreamBandwidth": bandwidthAllocProfile_BandwidthConfig_AllowGuaranteedUpStreamBandwidth,
       "mibbandwidthAllocProfile-SlotVpiVciRangeTable": mibbandwidthAllocProfile_SlotVpiVciRangeTable,
       "mibbandwidthAllocProfile-SlotVpiVciRangeEntry": mibbandwidthAllocProfile_SlotVpiVciRangeEntry,
       "bandwidthAllocProfile-SlotVpiVciRange-Index-o": bandwidthAllocProfile_SlotVpiVciRange_Index_o,
       "bandwidthAllocProfile-SlotVpiVciRange-Index1-o": bandwidthAllocProfile_SlotVpiVciRange_Index1_o,
       "bandwidthAllocProfile-SlotVpiVciRange": bandwidthAllocProfile_SlotVpiVciRange,
       "mibbandwidthStatsProfile": mibbandwidthStatsProfile,
       "mibbandwidthStatsProfileTable": mibbandwidthStatsProfileTable,
       "mibbandwidthStatsProfileEntry": mibbandwidthStatsProfileEntry,
       "bandwidthStatsProfile-Index-o": bandwidthStatsProfile_Index_o,
       "bandwidthStatsProfile-MaxUpstreamBandwidth": bandwidthStatsProfile_MaxUpstreamBandwidth,
       "bandwidthStatsProfile-ActiveUpstreamBandwidthOnTrunks": bandwidthStatsProfile_ActiveUpstreamBandwidthOnTrunks,
       "bandwidthStatsProfile-StandbyUpstreamBandwidthOnTrunks": bandwidthStatsProfile_StandbyUpstreamBandwidthOnTrunks,
       "bandwidthStatsProfile-Action-o": bandwidthStatsProfile_Action_o}
)
