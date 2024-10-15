# SNMP MIB module (CISCO-CAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:53 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoCarMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113)
)
ciscoCarMIB.setRevisions(
        ("1997-07-18 00:00",
         "1900-02-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PacketSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



class RateLimitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("quickAcc", 2),
          ("standardAcc", 3))
    )



class RateLimitAction(Integer32, TextualConvention):
    status = "current"
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
        *(("continue", 3),
          ("drop", 1),
          ("precedCont", 5),
          ("precedXmit", 4),
          ("xmit", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCarMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCarMIBObjects = _CiscoCarMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1)
)
_CcarConfigs_ObjectIdentity = ObjectIdentity
ccarConfigs = _CcarConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1)
)
_CcarConfigTable_Object = MibTable
ccarConfigTable = _CcarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccarConfigTable.setStatus("current")
_CcarConfigEntry_Object = MibTableRow
ccarConfigEntry = _CcarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1)
)
ccarConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CAR-MIB", "ccarConfigDirection"),
    (0, "CISCO-CAR-MIB", "ccarConfigRowIndex"),
)
if mibBuilder.loadTexts:
    ccarConfigEntry.setStatus("current")
_CcarConfigDirection_Type = PacketSource
_CcarConfigDirection_Object = MibTableColumn
ccarConfigDirection = _CcarConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 1),
    _CcarConfigDirection_Type()
)
ccarConfigDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccarConfigDirection.setStatus("current")


class _CcarConfigRowIndex_Type(Integer32):
    """Custom type ccarConfigRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcarConfigRowIndex_Type.__name__ = "Integer32"
_CcarConfigRowIndex_Object = MibTableColumn
ccarConfigRowIndex = _CcarConfigRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 2),
    _CcarConfigRowIndex_Type()
)
ccarConfigRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccarConfigRowIndex.setStatus("current")
_CcarConfigType_Type = RateLimitType
_CcarConfigType_Object = MibTableColumn
ccarConfigType = _CcarConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 3),
    _CcarConfigType_Type()
)
ccarConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigType.setStatus("current")
_CcarConfigAccIdx_Type = Integer32
_CcarConfigAccIdx_Object = MibTableColumn
ccarConfigAccIdx = _CcarConfigAccIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 4),
    _CcarConfigAccIdx_Type()
)
ccarConfigAccIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigAccIdx.setStatus("current")
_CcarConfigRate_Type = Integer32
_CcarConfigRate_Object = MibTableColumn
ccarConfigRate = _CcarConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 5),
    _CcarConfigRate_Type()
)
ccarConfigRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigRate.setStatus("current")
if mibBuilder.loadTexts:
    ccarConfigRate.setUnits("bits/second")
_CcarConfigLimit_Type = Integer32
_CcarConfigLimit_Object = MibTableColumn
ccarConfigLimit = _CcarConfigLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 6),
    _CcarConfigLimit_Type()
)
ccarConfigLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigLimit.setStatus("current")
if mibBuilder.loadTexts:
    ccarConfigLimit.setUnits("bytes")
_CcarConfigExtLimit_Type = Integer32
_CcarConfigExtLimit_Object = MibTableColumn
ccarConfigExtLimit = _CcarConfigExtLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 7),
    _CcarConfigExtLimit_Type()
)
ccarConfigExtLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigExtLimit.setStatus("current")
if mibBuilder.loadTexts:
    ccarConfigExtLimit.setUnits("bytes")
_CcarConfigConformAction_Type = RateLimitAction
_CcarConfigConformAction_Object = MibTableColumn
ccarConfigConformAction = _CcarConfigConformAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 8),
    _CcarConfigConformAction_Type()
)
ccarConfigConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigConformAction.setStatus("current")
_CcarConfigExceedAction_Type = RateLimitAction
_CcarConfigExceedAction_Object = MibTableColumn
ccarConfigExceedAction = _CcarConfigExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 1, 1, 1, 9),
    _CcarConfigExceedAction_Type()
)
ccarConfigExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarConfigExceedAction.setStatus("current")
_CcarStats_ObjectIdentity = ObjectIdentity
ccarStats = _CcarStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2)
)
_CcarStatTable_Object = MibTable
ccarStatTable = _CcarStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccarStatTable.setStatus("current")
_CcarStatEntry_Object = MibTableRow
ccarStatEntry = _CcarStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccarStatEntry.setStatus("current")
_CcarStatSwitchedPkts_Type = Counter32
_CcarStatSwitchedPkts_Object = MibTableColumn
ccarStatSwitchedPkts = _CcarStatSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 1),
    _CcarStatSwitchedPkts_Type()
)
ccarStatSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatSwitchedPkts.setUnits("packets")
_CcarStatSwitchedBytes_Type = Counter32
_CcarStatSwitchedBytes_Object = MibTableColumn
ccarStatSwitchedBytes = _CcarStatSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 2),
    _CcarStatSwitchedBytes_Type()
)
ccarStatSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatSwitchedBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatSwitchedBytes.setUnits("bytes")
_CcarStatFilteredPkts_Type = Counter32
_CcarStatFilteredPkts_Object = MibTableColumn
ccarStatFilteredPkts = _CcarStatFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 3),
    _CcarStatFilteredPkts_Type()
)
ccarStatFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatFilteredPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatFilteredPkts.setUnits("packets")
_CcarStatFilteredBytes_Type = Counter32
_CcarStatFilteredBytes_Object = MibTableColumn
ccarStatFilteredBytes = _CcarStatFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 4),
    _CcarStatFilteredBytes_Type()
)
ccarStatFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatFilteredBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatFilteredBytes.setUnits("bytes")
_CcarStatCurBurst_Type = Gauge32
_CcarStatCurBurst_Object = MibTableColumn
ccarStatCurBurst = _CcarStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 5),
    _CcarStatCurBurst_Type()
)
ccarStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatCurBurst.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatCurBurst.setUnits("bytes")
_CcarStatSwitchedPktsOverflow_Type = Counter32
_CcarStatSwitchedPktsOverflow_Object = MibTableColumn
ccarStatSwitchedPktsOverflow = _CcarStatSwitchedPktsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 6),
    _CcarStatSwitchedPktsOverflow_Type()
)
ccarStatSwitchedPktsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatSwitchedPktsOverflow.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatSwitchedPktsOverflow.setUnits("packets")
_CcarStatSwitchedBytesOverflow_Type = Counter32
_CcarStatSwitchedBytesOverflow_Object = MibTableColumn
ccarStatSwitchedBytesOverflow = _CcarStatSwitchedBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 7),
    _CcarStatSwitchedBytesOverflow_Type()
)
ccarStatSwitchedBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatSwitchedBytesOverflow.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatSwitchedBytesOverflow.setUnits("bytes")
_CcarStatFilteredPktsOverflow_Type = Counter32
_CcarStatFilteredPktsOverflow_Object = MibTableColumn
ccarStatFilteredPktsOverflow = _CcarStatFilteredPktsOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 8),
    _CcarStatFilteredPktsOverflow_Type()
)
ccarStatFilteredPktsOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatFilteredPktsOverflow.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatFilteredPktsOverflow.setUnits("packets")
_CcarStatFilteredBytesOverflow_Type = Counter32
_CcarStatFilteredBytesOverflow_Object = MibTableColumn
ccarStatFilteredBytesOverflow = _CcarStatFilteredBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 9),
    _CcarStatFilteredBytesOverflow_Type()
)
ccarStatFilteredBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatFilteredBytesOverflow.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatFilteredBytesOverflow.setUnits("bytes")
_CcarStatHCSwitchedPkts_Type = Counter64
_CcarStatHCSwitchedPkts_Object = MibTableColumn
ccarStatHCSwitchedPkts = _CcarStatHCSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 10),
    _CcarStatHCSwitchedPkts_Type()
)
ccarStatHCSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatHCSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatHCSwitchedPkts.setUnits("packets")
_CcarStatHCSwitchedBytes_Type = Counter64
_CcarStatHCSwitchedBytes_Object = MibTableColumn
ccarStatHCSwitchedBytes = _CcarStatHCSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 11),
    _CcarStatHCSwitchedBytes_Type()
)
ccarStatHCSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatHCSwitchedBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatHCSwitchedBytes.setUnits("bytes")
_CcarStatHCFilteredPkts_Type = Counter64
_CcarStatHCFilteredPkts_Object = MibTableColumn
ccarStatHCFilteredPkts = _CcarStatHCFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 12),
    _CcarStatHCFilteredPkts_Type()
)
ccarStatHCFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatHCFilteredPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatHCFilteredPkts.setUnits("packets")
_CcarStatHCFilteredBytes_Type = Counter64
_CcarStatHCFilteredBytes_Object = MibTableColumn
ccarStatHCFilteredBytes = _CcarStatHCFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 1, 2, 1, 1, 13),
    _CcarStatHCFilteredBytes_Type()
)
ccarStatHCFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccarStatHCFilteredBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccarStatHCFilteredBytes.setUnits("bytes")
_CiscoCarMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCarMIBConformance = _CiscoCarMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3)
)
_CiscoCarMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCarMIBCompliances = _CiscoCarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 1)
)
_CiscoCarMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCarMIBGroups = _CiscoCarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 2)
)
ccarConfigEntry.registerAugmentions(
    ("CISCO-CAR-MIB",
     "ccarStatEntry")
)
ccarStatEntry.setIndexNames(*ccarConfigEntry.getIndexNames())

# Managed Objects groups

ciscoCarMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 2, 1)
)
ciscoCarMIBGroup.setObjects(
      *(("CISCO-CAR-MIB", "ccarConfigType"),
        ("CISCO-CAR-MIB", "ccarConfigAccIdx"),
        ("CISCO-CAR-MIB", "ccarConfigRate"),
        ("CISCO-CAR-MIB", "ccarConfigLimit"),
        ("CISCO-CAR-MIB", "ccarConfigExtLimit"),
        ("CISCO-CAR-MIB", "ccarConfigConformAction"),
        ("CISCO-CAR-MIB", "ccarConfigExceedAction"),
        ("CISCO-CAR-MIB", "ccarStatSwitchedPkts"),
        ("CISCO-CAR-MIB", "ccarStatSwitchedBytes"),
        ("CISCO-CAR-MIB", "ccarStatFilteredPkts"),
        ("CISCO-CAR-MIB", "ccarStatFilteredBytes"),
        ("CISCO-CAR-MIB", "ccarStatCurBurst"))
)
if mibBuilder.loadTexts:
    ciscoCarMIBGroup.setStatus("current")

ciscoCarMIBHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 2, 2)
)
ciscoCarMIBHCGroup.setObjects(
      *(("CISCO-CAR-MIB", "ccarStatSwitchedPktsOverflow"),
        ("CISCO-CAR-MIB", "ccarStatSwitchedBytesOverflow"),
        ("CISCO-CAR-MIB", "ccarStatFilteredPktsOverflow"),
        ("CISCO-CAR-MIB", "ccarStatFilteredBytesOverflow"),
        ("CISCO-CAR-MIB", "ccarStatHCSwitchedPkts"),
        ("CISCO-CAR-MIB", "ccarStatHCSwitchedBytes"),
        ("CISCO-CAR-MIB", "ccarStatHCFilteredPkts"),
        ("CISCO-CAR-MIB", "ccarStatHCFilteredBytes"))
)
if mibBuilder.loadTexts:
    ciscoCarMIBHCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCarMIBCompliance.setStatus(
        "current"
    )

ciscoCarMIBComplianceHCCounters = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 113, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCarMIBComplianceHCCounters.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAR-MIB",
    **{"PacketSource": PacketSource,
       "RateLimitType": RateLimitType,
       "RateLimitAction": RateLimitAction,
       "ciscoCarMIB": ciscoCarMIB,
       "ciscoCarMIBObjects": ciscoCarMIBObjects,
       "ccarConfigs": ccarConfigs,
       "ccarConfigTable": ccarConfigTable,
       "ccarConfigEntry": ccarConfigEntry,
       "ccarConfigDirection": ccarConfigDirection,
       "ccarConfigRowIndex": ccarConfigRowIndex,
       "ccarConfigType": ccarConfigType,
       "ccarConfigAccIdx": ccarConfigAccIdx,
       "ccarConfigRate": ccarConfigRate,
       "ccarConfigLimit": ccarConfigLimit,
       "ccarConfigExtLimit": ccarConfigExtLimit,
       "ccarConfigConformAction": ccarConfigConformAction,
       "ccarConfigExceedAction": ccarConfigExceedAction,
       "ccarStats": ccarStats,
       "ccarStatTable": ccarStatTable,
       "ccarStatEntry": ccarStatEntry,
       "ccarStatSwitchedPkts": ccarStatSwitchedPkts,
       "ccarStatSwitchedBytes": ccarStatSwitchedBytes,
       "ccarStatFilteredPkts": ccarStatFilteredPkts,
       "ccarStatFilteredBytes": ccarStatFilteredBytes,
       "ccarStatCurBurst": ccarStatCurBurst,
       "ccarStatSwitchedPktsOverflow": ccarStatSwitchedPktsOverflow,
       "ccarStatSwitchedBytesOverflow": ccarStatSwitchedBytesOverflow,
       "ccarStatFilteredPktsOverflow": ccarStatFilteredPktsOverflow,
       "ccarStatFilteredBytesOverflow": ccarStatFilteredBytesOverflow,
       "ccarStatHCSwitchedPkts": ccarStatHCSwitchedPkts,
       "ccarStatHCSwitchedBytes": ccarStatHCSwitchedBytes,
       "ccarStatHCFilteredPkts": ccarStatHCFilteredPkts,
       "ccarStatHCFilteredBytes": ccarStatHCFilteredBytes,
       "ciscoCarMIBConformance": ciscoCarMIBConformance,
       "ciscoCarMIBCompliances": ciscoCarMIBCompliances,
       "ciscoCarMIBCompliance": ciscoCarMIBCompliance,
       "ciscoCarMIBComplianceHCCounters": ciscoCarMIBComplianceHCCounters,
       "ciscoCarMIBGroups": ciscoCarMIBGroups,
       "ciscoCarMIBGroup": ciscoCarMIBGroup,
       "ciscoCarMIBHCGroup": ciscoCarMIBHCGroup}
)
