# SNMP MIB module (VDSL-LINE-EXT-SCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VDSL-LINE-EXT-SCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:05 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vdslLineConfProfileName,) = mibBuilder.importSymbols(
    "VDSL-LINE-MIB",
    "vdslLineConfProfileName")


# MODULE-IDENTITY

vdslExtSCMMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 228)
)
vdslExtSCMMIB.setRevisions(
        ("2005-04-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VdslSCMBandId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("firstDownstreamBand", 2),
          ("firstUpstreamBand", 3),
          ("optionalBand", 1),
          ("secondDownstreamBand", 4),
          ("secondUpstreamBand", 5),
          ("thirdDownstreamBand", 6),
          ("thirdUpstreamBand", 7))
    )



# MIB Managed Objects in the order of their OIDs

_VdslLineExtSCMMib_ObjectIdentity = ObjectIdentity
vdslLineExtSCMMib = _VdslLineExtSCMMib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 228, 1)
)
_VdslLineExtSCMMibObjects_ObjectIdentity = ObjectIdentity
vdslLineExtSCMMibObjects = _VdslLineExtSCMMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1)
)
_VdslLineSCMConfProfileBandTable_Object = MibTable
vdslLineSCMConfProfileBandTable = _VdslLineSCMConfProfileBandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandTable.setStatus("current")
_VdslLineSCMConfProfileBandEntry_Object = MibTableRow
vdslLineSCMConfProfileBandEntry = _VdslLineSCMConfProfileBandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1)
)
vdslLineSCMConfProfileBandEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
    (0, "VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandId"),
)
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandEntry.setStatus("current")
_VdslLineSCMConfProfileBandId_Type = VdslSCMBandId
_VdslLineSCMConfProfileBandId_Object = MibTableColumn
vdslLineSCMConfProfileBandId = _VdslLineSCMConfProfileBandId_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 1),
    _VdslLineSCMConfProfileBandId_Type()
)
vdslLineSCMConfProfileBandId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandId.setStatus("current")
_VdslLineSCMConfProfileBandInUse_Type = TruthValue
_VdslLineSCMConfProfileBandInUse_Object = MibTableColumn
vdslLineSCMConfProfileBandInUse = _VdslLineSCMConfProfileBandInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 2),
    _VdslLineSCMConfProfileBandInUse_Type()
)
vdslLineSCMConfProfileBandInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandInUse.setStatus("current")
_VdslLineSCMConfProfileBandCenterFrequency_Type = Unsigned32
_VdslLineSCMConfProfileBandCenterFrequency_Object = MibTableColumn
vdslLineSCMConfProfileBandCenterFrequency = _VdslLineSCMConfProfileBandCenterFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 3),
    _VdslLineSCMConfProfileBandCenterFrequency_Type()
)
vdslLineSCMConfProfileBandCenterFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandCenterFrequency.setUnits("Hz")
_VdslLineSCMConfProfileBandSymbolRate_Type = Unsigned32
_VdslLineSCMConfProfileBandSymbolRate_Object = MibTableColumn
vdslLineSCMConfProfileBandSymbolRate = _VdslLineSCMConfProfileBandSymbolRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 4),
    _VdslLineSCMConfProfileBandSymbolRate_Type()
)
vdslLineSCMConfProfileBandSymbolRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandSymbolRate.setUnits("baud")


class _VdslLineSCMConfProfileBandConstellationSize_Type(Unsigned32):
    """Custom type vdslLineSCMConfProfileBandConstellationSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VdslLineSCMConfProfileBandConstellationSize_Type.__name__ = "Unsigned32"
_VdslLineSCMConfProfileBandConstellationSize_Object = MibTableColumn
vdslLineSCMConfProfileBandConstellationSize = _VdslLineSCMConfProfileBandConstellationSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 5),
    _VdslLineSCMConfProfileBandConstellationSize_Type()
)
vdslLineSCMConfProfileBandConstellationSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandConstellationSize.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandConstellationSize.setUnits("log2")
_VdslLineSCMConfProfileBandTransmitPSDLevel_Type = Unsigned32
_VdslLineSCMConfProfileBandTransmitPSDLevel_Object = MibTableColumn
vdslLineSCMConfProfileBandTransmitPSDLevel = _VdslLineSCMConfProfileBandTransmitPSDLevel_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 6),
    _VdslLineSCMConfProfileBandTransmitPSDLevel_Type()
)
vdslLineSCMConfProfileBandTransmitPSDLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandTransmitPSDLevel.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandTransmitPSDLevel.setUnits("-0.25 dBm/Hz")
_VdslLineSCMConfProfileBandRowStatus_Type = RowStatus
_VdslLineSCMConfProfileBandRowStatus_Object = MibTableColumn
vdslLineSCMConfProfileBandRowStatus = _VdslLineSCMConfProfileBandRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 1, 1, 7),
    _VdslLineSCMConfProfileBandRowStatus_Type()
)
vdslLineSCMConfProfileBandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vdslLineSCMConfProfileBandRowStatus.setStatus("current")
_VdslLineSCMPhysBandTable_Object = MibTable
vdslLineSCMPhysBandTable = _VdslLineSCMPhysBandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandTable.setStatus("current")
_VdslLineSCMPhysBandEntry_Object = MibTableRow
vdslLineSCMPhysBandEntry = _VdslLineSCMPhysBandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1)
)
vdslLineSCMPhysBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandId"),
)
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandEntry.setStatus("current")
_VdslLineSCMPhysBandId_Type = VdslSCMBandId
_VdslLineSCMPhysBandId_Object = MibTableColumn
vdslLineSCMPhysBandId = _VdslLineSCMPhysBandId_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 1),
    _VdslLineSCMPhysBandId_Type()
)
vdslLineSCMPhysBandId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandId.setStatus("current")
_VdslLineSCMPhysBandInUse_Type = TruthValue
_VdslLineSCMPhysBandInUse_Object = MibTableColumn
vdslLineSCMPhysBandInUse = _VdslLineSCMPhysBandInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 2),
    _VdslLineSCMPhysBandInUse_Type()
)
vdslLineSCMPhysBandInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandInUse.setStatus("current")
_VdslLineSCMPhysBandCurrCenterFrequency_Type = Unsigned32
_VdslLineSCMPhysBandCurrCenterFrequency_Object = MibTableColumn
vdslLineSCMPhysBandCurrCenterFrequency = _VdslLineSCMPhysBandCurrCenterFrequency_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 3),
    _VdslLineSCMPhysBandCurrCenterFrequency_Type()
)
vdslLineSCMPhysBandCurrCenterFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrCenterFrequency.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrCenterFrequency.setUnits("Hz")
_VdslLineSCMPhysBandCurrSymbolRate_Type = Unsigned32
_VdslLineSCMPhysBandCurrSymbolRate_Object = MibTableColumn
vdslLineSCMPhysBandCurrSymbolRate = _VdslLineSCMPhysBandCurrSymbolRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 4),
    _VdslLineSCMPhysBandCurrSymbolRate_Type()
)
vdslLineSCMPhysBandCurrSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrSymbolRate.setUnits("baud")


class _VdslLineSCMPhysBandCurrConstellationSize_Type(Unsigned32):
    """Custom type vdslLineSCMPhysBandCurrConstellationSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VdslLineSCMPhysBandCurrConstellationSize_Type.__name__ = "Unsigned32"
_VdslLineSCMPhysBandCurrConstellationSize_Object = MibTableColumn
vdslLineSCMPhysBandCurrConstellationSize = _VdslLineSCMPhysBandCurrConstellationSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 5),
    _VdslLineSCMPhysBandCurrConstellationSize_Type()
)
vdslLineSCMPhysBandCurrConstellationSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrConstellationSize.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrConstellationSize.setUnits("log2")
_VdslLineSCMPhysBandCurrPSDLevel_Type = Unsigned32
_VdslLineSCMPhysBandCurrPSDLevel_Object = MibTableColumn
vdslLineSCMPhysBandCurrPSDLevel = _VdslLineSCMPhysBandCurrPSDLevel_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 6),
    _VdslLineSCMPhysBandCurrPSDLevel_Type()
)
vdslLineSCMPhysBandCurrPSDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrPSDLevel.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrPSDLevel.setUnits("- 0.25 dBm/Hz")
_VdslLineSCMPhysBandCurrSnrMgn_Type = Integer32
_VdslLineSCMPhysBandCurrSnrMgn_Object = MibTableColumn
vdslLineSCMPhysBandCurrSnrMgn = _VdslLineSCMPhysBandCurrSnrMgn_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 7),
    _VdslLineSCMPhysBandCurrSnrMgn_Type()
)
vdslLineSCMPhysBandCurrSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrSnrMgn.setUnits("0.25 dB")


class _VdslLineSCMPhysBandCurrAtn_Type(Unsigned32):
    """Custom type vdslLineSCMPhysBandCurrAtn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VdslLineSCMPhysBandCurrAtn_Type.__name__ = "Unsigned32"
_VdslLineSCMPhysBandCurrAtn_Object = MibTableColumn
vdslLineSCMPhysBandCurrAtn = _VdslLineSCMPhysBandCurrAtn_Object(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 1, 2, 1, 8),
    _VdslLineSCMPhysBandCurrAtn_Type()
)
vdslLineSCMPhysBandCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    vdslLineSCMPhysBandCurrAtn.setUnits("0.25 dB")
_VdslLineExtSCMConformance_ObjectIdentity = ObjectIdentity
vdslLineExtSCMConformance = _VdslLineExtSCMConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 2)
)
_VdslLineExtSCMGroups_ObjectIdentity = ObjectIdentity
vdslLineExtSCMGroups = _VdslLineExtSCMGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 1)
)
_VdslLineExtSCMCompliances_ObjectIdentity = ObjectIdentity
vdslLineExtSCMCompliances = _VdslLineExtSCMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 2)
)

# Managed Objects groups

vdslLineExtSCMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 1, 1)
)
vdslLineExtSCMGroup.setObjects(
      *(("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandInUse"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandTransmitPSDLevel"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandSymbolRate"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandConstellationSize"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandCenterFrequency"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMConfProfileBandRowStatus"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandInUse"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrPSDLevel"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrSymbolRate"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrConstellationSize"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrCenterFrequency"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrSnrMgn"),
        ("VDSL-LINE-EXT-SCM-MIB", "vdslLineSCMPhysBandCurrAtn"))
)
if mibBuilder.loadTexts:
    vdslLineExtSCMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vdslLineExtSCMMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 228, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vdslLineExtSCMMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VDSL-LINE-EXT-SCM-MIB",
    **{"VdslSCMBandId": VdslSCMBandId,
       "vdslExtSCMMIB": vdslExtSCMMIB,
       "vdslLineExtSCMMib": vdslLineExtSCMMib,
       "vdslLineExtSCMMibObjects": vdslLineExtSCMMibObjects,
       "vdslLineSCMConfProfileBandTable": vdslLineSCMConfProfileBandTable,
       "vdslLineSCMConfProfileBandEntry": vdslLineSCMConfProfileBandEntry,
       "vdslLineSCMConfProfileBandId": vdslLineSCMConfProfileBandId,
       "vdslLineSCMConfProfileBandInUse": vdslLineSCMConfProfileBandInUse,
       "vdslLineSCMConfProfileBandCenterFrequency": vdslLineSCMConfProfileBandCenterFrequency,
       "vdslLineSCMConfProfileBandSymbolRate": vdslLineSCMConfProfileBandSymbolRate,
       "vdslLineSCMConfProfileBandConstellationSize": vdslLineSCMConfProfileBandConstellationSize,
       "vdslLineSCMConfProfileBandTransmitPSDLevel": vdslLineSCMConfProfileBandTransmitPSDLevel,
       "vdslLineSCMConfProfileBandRowStatus": vdslLineSCMConfProfileBandRowStatus,
       "vdslLineSCMPhysBandTable": vdslLineSCMPhysBandTable,
       "vdslLineSCMPhysBandEntry": vdslLineSCMPhysBandEntry,
       "vdslLineSCMPhysBandId": vdslLineSCMPhysBandId,
       "vdslLineSCMPhysBandInUse": vdslLineSCMPhysBandInUse,
       "vdslLineSCMPhysBandCurrCenterFrequency": vdslLineSCMPhysBandCurrCenterFrequency,
       "vdslLineSCMPhysBandCurrSymbolRate": vdslLineSCMPhysBandCurrSymbolRate,
       "vdslLineSCMPhysBandCurrConstellationSize": vdslLineSCMPhysBandCurrConstellationSize,
       "vdslLineSCMPhysBandCurrPSDLevel": vdslLineSCMPhysBandCurrPSDLevel,
       "vdslLineSCMPhysBandCurrSnrMgn": vdslLineSCMPhysBandCurrSnrMgn,
       "vdslLineSCMPhysBandCurrAtn": vdslLineSCMPhysBandCurrAtn,
       "vdslLineExtSCMConformance": vdslLineExtSCMConformance,
       "vdslLineExtSCMGroups": vdslLineExtSCMGroups,
       "vdslLineExtSCMGroup": vdslLineExtSCMGroup,
       "vdslLineExtSCMCompliances": vdslLineExtSCMCompliances,
       "vdslLineExtSCMMibCompliance": vdslLineExtSCMMibCompliance}
)
