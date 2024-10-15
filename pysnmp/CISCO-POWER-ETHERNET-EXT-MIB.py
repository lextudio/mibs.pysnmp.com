# SNMP MIB module (CISCO-POWER-ETHERNET-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-POWER-ETHERNET-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:02 2024
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

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

(pethMainPseGroupIndex,
 pethPsePortEntry,
 pethPsePortGroupIndex,
 pethPsePortIndex) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseGroupIndex",
    "pethPsePortEntry",
    "pethPsePortGroupIndex",
    "pethPsePortIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoPowerEthernetExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402)
)
ciscoPowerEthernetExtMIB.setRevisions(
        ("2013-07-10 00:00",
         "2011-07-18 00:00",
         "2009-12-04 00:00",
         "2007-04-12 00:00",
         "2007-02-02 00:00",
         "2005-06-10 00:00",
         "2004-04-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpeExtLldpPwrType(Integer32, TextualConvention):
    status = "current"
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
        *(("type1Pd", 1),
          ("type1Pse", 2),
          ("type2Pd", 3),
          ("type2Pse", 4))
    )



class CpeExtLldpPwrSrc(Integer32, TextualConvention):
    status = "current"
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
        *(("backupSrc", 4),
          ("local", 2),
          ("primarySrc", 5),
          ("pse", 3),
          ("pseAndLocal", 1),
          ("unknown", 6))
    )



class CpeExtPwrPriority(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 1),
          ("high", 2),
          ("low", 3),
          ("unknown", 4))
    )



class CpeExtLldpPwrClassOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CpeExtMIBNotifs_ObjectIdentity = ObjectIdentity
cpeExtMIBNotifs = _CpeExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 0)
)
_CpeExtMIBObjects_ObjectIdentity = ObjectIdentity
cpeExtMIBObjects = _CpeExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1)
)
_CpeExtDefaultAllocation_Type = Unsigned32
_CpeExtDefaultAllocation_Object = MibScalar
cpeExtDefaultAllocation = _CpeExtDefaultAllocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 1),
    _CpeExtDefaultAllocation_Type()
)
cpeExtDefaultAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtDefaultAllocation.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtDefaultAllocation.setUnits("milliwatts")
_CpeExtPsePortTable_Object = MibTable
cpeExtPsePortTable = _CpeExtPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2)
)
if mibBuilder.loadTexts:
    cpeExtPsePortTable.setStatus("current")
_CpeExtPsePortEntry_Object = MibTableRow
cpeExtPsePortEntry = _CpeExtPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpeExtPsePortEntry.setStatus("current")


class _CpeExtPsePortEnable_Type(Integer32):
    """Custom type cpeExtPsePortEnable based on Integer32"""
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
        *(("auto", 1),
          ("disable", 4),
          ("limit", 3),
          ("static", 2))
    )


_CpeExtPsePortEnable_Type.__name__ = "Integer32"
_CpeExtPsePortEnable_Object = MibTableColumn
cpeExtPsePortEnable = _CpeExtPsePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 1),
    _CpeExtPsePortEnable_Type()
)
cpeExtPsePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPsePortEnable.setStatus("current")


class _CpeExtPsePortDiscoverMode_Type(Integer32):
    """Custom type cpeExtPsePortDiscoverMode based on Integer32"""
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
        *(("cisco", 4),
          ("ieee", 3),
          ("ieeeAndCisco", 5),
          ("off", 2),
          ("unknown", 1))
    )


_CpeExtPsePortDiscoverMode_Type.__name__ = "Integer32"
_CpeExtPsePortDiscoverMode_Object = MibTableColumn
cpeExtPsePortDiscoverMode = _CpeExtPsePortDiscoverMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 2),
    _CpeExtPsePortDiscoverMode_Type()
)
cpeExtPsePortDiscoverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortDiscoverMode.setStatus("current")
_CpeExtPsePortDeviceDetected_Type = TruthValue
_CpeExtPsePortDeviceDetected_Object = MibTableColumn
cpeExtPsePortDeviceDetected = _CpeExtPsePortDeviceDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 3),
    _CpeExtPsePortDeviceDetected_Type()
)
cpeExtPsePortDeviceDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortDeviceDetected.setStatus("current")
_CpeExtPsePortIeeePd_Type = TruthValue
_CpeExtPsePortIeeePd_Object = MibTableColumn
cpeExtPsePortIeeePd = _CpeExtPsePortIeeePd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 4),
    _CpeExtPsePortIeeePd_Type()
)
cpeExtPsePortIeeePd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortIeeePd.setStatus("current")


class _CpeExtPsePortAdditionalStatus_Type(Bits):
    """Custom type cpeExtPsePortAdditionalStatus based on Bits"""
    namedValues = NamedValues(
        *(("deny", 0),
          ("overdraw", 1),
          ("overdrawLog", 2))
    )

_CpeExtPsePortAdditionalStatus_Type.__name__ = "Bits"
_CpeExtPsePortAdditionalStatus_Object = MibTableColumn
cpeExtPsePortAdditionalStatus = _CpeExtPsePortAdditionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 5),
    _CpeExtPsePortAdditionalStatus_Type()
)
cpeExtPsePortAdditionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortAdditionalStatus.setStatus("current")
_CpeExtPsePortPwrMax_Type = Unsigned32
_CpeExtPsePortPwrMax_Object = MibTableColumn
cpeExtPsePortPwrMax = _CpeExtPsePortPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 6),
    _CpeExtPsePortPwrMax_Type()
)
cpeExtPsePortPwrMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrMax.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrMax.setUnits("milliwatts")
_CpeExtPsePortPwrAllocated_Type = Unsigned32
_CpeExtPsePortPwrAllocated_Object = MibTableColumn
cpeExtPsePortPwrAllocated = _CpeExtPsePortPwrAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 7),
    _CpeExtPsePortPwrAllocated_Type()
)
cpeExtPsePortPwrAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrAllocated.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrAllocated.setUnits("milliwatts")
_CpeExtPsePortPwrAvailable_Type = Unsigned32
_CpeExtPsePortPwrAvailable_Object = MibTableColumn
cpeExtPsePortPwrAvailable = _CpeExtPsePortPwrAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 8),
    _CpeExtPsePortPwrAvailable_Type()
)
cpeExtPsePortPwrAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrAvailable.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrAvailable.setUnits("milliwatts")
_CpeExtPsePortPwrConsumption_Type = Unsigned32
_CpeExtPsePortPwrConsumption_Object = MibTableColumn
cpeExtPsePortPwrConsumption = _CpeExtPsePortPwrConsumption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 9),
    _CpeExtPsePortPwrConsumption_Type()
)
cpeExtPsePortPwrConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrConsumption.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrConsumption.setUnits("milliwatts")
_CpeExtPsePortMaxPwrDrawn_Type = Unsigned32
_CpeExtPsePortMaxPwrDrawn_Object = MibTableColumn
cpeExtPsePortMaxPwrDrawn = _CpeExtPsePortMaxPwrDrawn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 10),
    _CpeExtPsePortMaxPwrDrawn_Type()
)
cpeExtPsePortMaxPwrDrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortMaxPwrDrawn.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortMaxPwrDrawn.setUnits("milliwatts")
_CpeExtPsePortEntPhyIndex_Type = EntPhysicalIndexOrZero
_CpeExtPsePortEntPhyIndex_Object = MibTableColumn
cpeExtPsePortEntPhyIndex = _CpeExtPsePortEntPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 11),
    _CpeExtPsePortEntPhyIndex_Type()
)
cpeExtPsePortEntPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortEntPhyIndex.setStatus("current")
_CpeExtPsePortPolicingCapable_Type = TruthValue
_CpeExtPsePortPolicingCapable_Object = MibTableColumn
cpeExtPsePortPolicingCapable = _CpeExtPsePortPolicingCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 12),
    _CpeExtPsePortPolicingCapable_Type()
)
cpeExtPsePortPolicingCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortPolicingCapable.setStatus("current")


class _CpeExtPsePortPolicingEnable_Type(Integer32):
    """Custom type cpeExtPsePortPolicingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CpeExtPsePortPolicingEnable_Type.__name__ = "Integer32"
_CpeExtPsePortPolicingEnable_Object = MibTableColumn
cpeExtPsePortPolicingEnable = _CpeExtPsePortPolicingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 13),
    _CpeExtPsePortPolicingEnable_Type()
)
cpeExtPsePortPolicingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPsePortPolicingEnable.setStatus("current")


class _CpeExtPsePortPolicingAction_Type(Integer32):
    """Custom type cpeExtPsePortPolicingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("logOnly", 2))
    )


_CpeExtPsePortPolicingAction_Type.__name__ = "Integer32"
_CpeExtPsePortPolicingAction_Object = MibTableColumn
cpeExtPsePortPolicingAction = _CpeExtPsePortPolicingAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 14),
    _CpeExtPsePortPolicingAction_Type()
)
cpeExtPsePortPolicingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPsePortPolicingAction.setStatus("current")
_CpeExtPsePortPwrManAlloc_Type = Unsigned32
_CpeExtPsePortPwrManAlloc_Object = MibTableColumn
cpeExtPsePortPwrManAlloc = _CpeExtPsePortPwrManAlloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 15),
    _CpeExtPsePortPwrManAlloc_Type()
)
cpeExtPsePortPwrManAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrManAlloc.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortPwrManAlloc.setUnits("milliwatts")


class _CpeExtPsePortCapabilities_Type(Bits):
    """Custom type cpeExtPsePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("poePlus", 1),
          ("policing", 0))
    )

_CpeExtPsePortCapabilities_Type.__name__ = "Bits"
_CpeExtPsePortCapabilities_Object = MibTableColumn
cpeExtPsePortCapabilities = _CpeExtPsePortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 16),
    _CpeExtPsePortCapabilities_Type()
)
cpeExtPsePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortCapabilities.setStatus("current")
_CpeExtMainPseTable_Object = MibTable
cpeExtMainPseTable = _CpeExtMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3)
)
if mibBuilder.loadTexts:
    cpeExtMainPseTable.setStatus("current")
_CpeExtMainPseEntry_Object = MibTableRow
cpeExtMainPseEntry = _CpeExtMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1)
)
cpeExtMainPseEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    cpeExtMainPseEntry.setStatus("current")
_CpeExtMainPseEntPhyIndex_Type = EntPhysicalIndexOrZero
_CpeExtMainPseEntPhyIndex_Object = MibTableColumn
cpeExtMainPseEntPhyIndex = _CpeExtMainPseEntPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1, 1),
    _CpeExtMainPseEntPhyIndex_Type()
)
cpeExtMainPseEntPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtMainPseEntPhyIndex.setStatus("current")
_CpeExtMainPseDescr_Type = SnmpAdminString
_CpeExtMainPseDescr_Object = MibTableColumn
cpeExtMainPseDescr = _CpeExtMainPseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1, 2),
    _CpeExtMainPseDescr_Type()
)
cpeExtMainPseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtMainPseDescr.setStatus("current")
_CpeExtMainPsePwrMonitorCapable_Type = TruthValue
_CpeExtMainPsePwrMonitorCapable_Object = MibTableColumn
cpeExtMainPsePwrMonitorCapable = _CpeExtMainPsePwrMonitorCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1, 3),
    _CpeExtMainPsePwrMonitorCapable_Type()
)
cpeExtMainPsePwrMonitorCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtMainPsePwrMonitorCapable.setStatus("current")
_CpeExtPdStatistics_ObjectIdentity = ObjectIdentity
cpeExtPdStatistics = _CpeExtPdStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4)
)
_CpeExtPdStatsTotalDevices_Type = Unsigned32
_CpeExtPdStatsTotalDevices_Object = MibScalar
cpeExtPdStatsTotalDevices = _CpeExtPdStatsTotalDevices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 1),
    _CpeExtPdStatsTotalDevices_Type()
)
cpeExtPdStatsTotalDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPdStatsTotalDevices.setStatus("current")
_CpeExtPdStatsTable_Object = MibTable
cpeExtPdStatsTable = _CpeExtPdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cpeExtPdStatsTable.setStatus("current")
_CpeExtPdStatsEntry_Object = MibTableRow
cpeExtPdStatsEntry = _CpeExtPdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2, 1)
)
cpeExtPdStatsEntry.setIndexNames(
    (0, "CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsClass"),
)
if mibBuilder.loadTexts:
    cpeExtPdStatsEntry.setStatus("current")


class _CpeExtPdStatsClass_Type(Integer32):
    """Custom type cpeExtPdStatsClass based on Integer32"""
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
        *(("cisco", 1),
          ("class0", 2),
          ("class1", 3),
          ("class2", 4),
          ("class3", 5),
          ("class4", 6))
    )


_CpeExtPdStatsClass_Type.__name__ = "Integer32"
_CpeExtPdStatsClass_Object = MibTableColumn
cpeExtPdStatsClass = _CpeExtPdStatsClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2, 1, 1),
    _CpeExtPdStatsClass_Type()
)
cpeExtPdStatsClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpeExtPdStatsClass.setStatus("current")
_CpeExtPdStatsDeviceCount_Type = Unsigned32
_CpeExtPdStatsDeviceCount_Object = MibTableColumn
cpeExtPdStatsDeviceCount = _CpeExtPdStatsDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2, 1, 2),
    _CpeExtPdStatsDeviceCount_Type()
)
cpeExtPdStatsDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPdStatsDeviceCount.setStatus("current")
_CpeExtPolicingNotifEnable_Type = TruthValue
_CpeExtPolicingNotifEnable_Object = MibScalar
cpeExtPolicingNotifEnable = _CpeExtPolicingNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 5),
    _CpeExtPolicingNotifEnable_Type()
)
cpeExtPolicingNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPolicingNotifEnable.setStatus("current")
_CpeExtPowerPriorityEnable_Type = TruthValue
_CpeExtPowerPriorityEnable_Object = MibScalar
cpeExtPowerPriorityEnable = _CpeExtPowerPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 6),
    _CpeExtPowerPriorityEnable_Type()
)
cpeExtPowerPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeExtPowerPriorityEnable.setStatus("current")
_CpeExtPsePortLldpTable_Object = MibTable
cpeExtPsePortLldpTable = _CpeExtPsePortLldpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7)
)
if mibBuilder.loadTexts:
    cpeExtPsePortLldpTable.setStatus("current")
_CpeExtPsePortLldpEntry_Object = MibTableRow
cpeExtPsePortLldpEntry = _CpeExtPsePortLldpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1)
)
cpeExtPsePortLldpEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    cpeExtPsePortLldpEntry.setStatus("current")
_CpeExtPsePortLldpPwrType_Type = CpeExtLldpPwrType
_CpeExtPsePortLldpPwrType_Object = MibTableColumn
cpeExtPsePortLldpPwrType = _CpeExtPsePortLldpPwrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 1),
    _CpeExtPsePortLldpPwrType_Type()
)
cpeExtPsePortLldpPwrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrType.setStatus("current")
_CpeExtPsePortLldpPdPwrType_Type = CpeExtLldpPwrType
_CpeExtPsePortLldpPdPwrType_Object = MibTableColumn
cpeExtPsePortLldpPdPwrType = _CpeExtPsePortLldpPdPwrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 2),
    _CpeExtPsePortLldpPdPwrType_Type()
)
cpeExtPsePortLldpPdPwrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrType.setStatus("current")
_CpeExtPsePortLldpPwrSrc_Type = CpeExtLldpPwrSrc
_CpeExtPsePortLldpPwrSrc_Object = MibTableColumn
cpeExtPsePortLldpPwrSrc = _CpeExtPsePortLldpPwrSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 3),
    _CpeExtPsePortLldpPwrSrc_Type()
)
cpeExtPsePortLldpPwrSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrSrc.setStatus("current")
_CpeExtPsePortLldpPdPwrSrc_Type = CpeExtLldpPwrSrc
_CpeExtPsePortLldpPdPwrSrc_Object = MibTableColumn
cpeExtPsePortLldpPdPwrSrc = _CpeExtPsePortLldpPdPwrSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 4),
    _CpeExtPsePortLldpPdPwrSrc_Type()
)
cpeExtPsePortLldpPdPwrSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrSrc.setStatus("current")
_CpeExtPsePortLldpPwrPriority_Type = CpeExtPwrPriority
_CpeExtPsePortLldpPwrPriority_Object = MibTableColumn
cpeExtPsePortLldpPwrPriority = _CpeExtPsePortLldpPwrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 5),
    _CpeExtPsePortLldpPwrPriority_Type()
)
cpeExtPsePortLldpPwrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrPriority.setStatus("current")
_CpeExtPsePortLldpPdPwrPriority_Type = CpeExtPwrPriority
_CpeExtPsePortLldpPdPwrPriority_Object = MibTableColumn
cpeExtPsePortLldpPdPwrPriority = _CpeExtPsePortLldpPdPwrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 6),
    _CpeExtPsePortLldpPdPwrPriority_Type()
)
cpeExtPsePortLldpPdPwrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrPriority.setStatus("current")
_CpeExtPsePortLldpPwrReq_Type = Unsigned32
_CpeExtPsePortLldpPwrReq_Object = MibTableColumn
cpeExtPsePortLldpPwrReq = _CpeExtPsePortLldpPwrReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 7),
    _CpeExtPsePortLldpPwrReq_Type()
)
cpeExtPsePortLldpPwrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrReq.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrReq.setUnits("milliwatts")
_CpeExtPsePortLldpPdPwrReq_Type = Unsigned32
_CpeExtPsePortLldpPdPwrReq_Object = MibTableColumn
cpeExtPsePortLldpPdPwrReq = _CpeExtPsePortLldpPdPwrReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 8),
    _CpeExtPsePortLldpPdPwrReq_Type()
)
cpeExtPsePortLldpPdPwrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrReq.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrReq.setUnits("milliwatts")
_CpeExtPsePortLldpPwrAlloc_Type = Unsigned32
_CpeExtPsePortLldpPwrAlloc_Object = MibTableColumn
cpeExtPsePortLldpPwrAlloc = _CpeExtPsePortLldpPwrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 9),
    _CpeExtPsePortLldpPwrAlloc_Type()
)
cpeExtPsePortLldpPwrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrAlloc.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrAlloc.setUnits("milliwatts")
_CpeExtPsePortLldpPdPwrAlloc_Type = Unsigned32
_CpeExtPsePortLldpPdPwrAlloc_Object = MibTableColumn
cpeExtPsePortLldpPdPwrAlloc = _CpeExtPsePortLldpPdPwrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 10),
    _CpeExtPsePortLldpPdPwrAlloc_Type()
)
cpeExtPsePortLldpPdPwrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrAlloc.setStatus("current")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrAlloc.setUnits("milliwatts")
_CpeExtPsePortLldpPwrClass_Type = CpeExtLldpPwrClassOrZero
_CpeExtPsePortLldpPwrClass_Object = MibTableColumn
cpeExtPsePortLldpPwrClass = _CpeExtPsePortLldpPwrClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 11),
    _CpeExtPsePortLldpPwrClass_Type()
)
cpeExtPsePortLldpPwrClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPwrClass.setStatus("current")
_CpeExtPsePortLldpPdPwrClass_Type = CpeExtLldpPwrClassOrZero
_CpeExtPsePortLldpPdPwrClass_Object = MibTableColumn
cpeExtPsePortLldpPdPwrClass = _CpeExtPsePortLldpPdPwrClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 12),
    _CpeExtPsePortLldpPdPwrClass_Type()
)
cpeExtPsePortLldpPdPwrClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrClass.setStatus("current")


class _CpeExtPsePortLldpPdPwrSupport_Type(Bits):
    """Custom type cpeExtPsePortLldpPdPwrSupport based on Bits"""
    namedValues = NamedValues(
        *(("portClass", 0),
          ("pseMdiPwrState", 2),
          ("pseMdiPwrSupport", 1),
          ("psePairCtrlAbility", 3))
    )

_CpeExtPsePortLldpPdPwrSupport_Type.__name__ = "Bits"
_CpeExtPsePortLldpPdPwrSupport_Object = MibTableColumn
cpeExtPsePortLldpPdPwrSupport = _CpeExtPsePortLldpPdPwrSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 13),
    _CpeExtPsePortLldpPdPwrSupport_Type()
)
cpeExtPsePortLldpPdPwrSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrSupport.setStatus("current")


class _CpeExtPsePortLldpPdPwrPairsOrZero_Type(Integer32):
    """Custom type cpeExtPsePortLldpPdPwrPairsOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("spare", 2),
          ("unknown", 0))
    )


_CpeExtPsePortLldpPdPwrPairsOrZero_Type.__name__ = "Integer32"
_CpeExtPsePortLldpPdPwrPairsOrZero_Object = MibTableColumn
cpeExtPsePortLldpPdPwrPairsOrZero = _CpeExtPsePortLldpPdPwrPairsOrZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 14),
    _CpeExtPsePortLldpPdPwrPairsOrZero_Type()
)
cpeExtPsePortLldpPdPwrPairsOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPdPwrPairsOrZero.setStatus("current")
_CpeExtMIBConformance_ObjectIdentity = ObjectIdentity
cpeExtMIBConformance = _CpeExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2)
)
_CpeExtMIBCompliances_ObjectIdentity = ObjectIdentity
cpeExtMIBCompliances = _CpeExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1)
)
_CpeExtMIBGroups_ObjectIdentity = ObjectIdentity
cpeExtMIBGroups = _CpeExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2)
)
pethPsePortEntry.registerAugmentions(
    ("CISCO-POWER-ETHERNET-EXT-MIB",
     "cpeExtPsePortEntry")
)
cpeExtPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())

# Managed Objects groups

cpeExtPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 1)
)
cpeExtPsePortGroup.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortEnable"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortDiscoverMode"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortDeviceDetected"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortIeeePd"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortAdditionalStatus"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrMax"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrAllocated"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrAvailable"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrConsumption"))
)
if mibBuilder.loadTexts:
    cpeExtPsePortGroup.setStatus("current")

cpeExtPsePortGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 2)
)
cpeExtPsePortGlobalConfigGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtDefaultAllocation")
)
if mibBuilder.loadTexts:
    cpeExtPsePortGlobalConfigGroup.setStatus("current")

cpeExtPsePortPwrMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 3)
)
cpeExtPsePortPwrMonitorGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortMaxPwrDrawn")
)
if mibBuilder.loadTexts:
    cpeExtPsePortPwrMonitorGroup.setStatus("current")

cpeExtMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 4)
)
cpeExtMainPseGroup.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseEntPhyIndex"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseDescr"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPsePwrMonitorCapable"))
)
if mibBuilder.loadTexts:
    cpeExtMainPseGroup.setStatus("deprecated")

cpeExtPortEntityIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 5)
)
cpeExtPortEntityIndexGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortEntPhyIndex")
)
if mibBuilder.loadTexts:
    cpeExtPortEntityIndexGroup.setStatus("current")

cpeExtPortPolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 6)
)
cpeExtPortPolicingGroup.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingCapable"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingEnable"))
)
if mibBuilder.loadTexts:
    cpeExtPortPolicingGroup.setStatus("current")

cpeExtPdStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 7)
)
cpeExtPdStatsGroup.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsTotalDevices"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsDeviceCount"))
)
if mibBuilder.loadTexts:
    cpeExtPdStatsGroup.setStatus("current")

cpeExtMainPseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 8)
)
cpeExtMainPseGroup2.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseEntPhyIndex"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseDescr"))
)
if mibBuilder.loadTexts:
    cpeExtMainPseGroup2.setStatus("current")

cpeExtPseGrpPwrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 9)
)
cpeExtPseGrpPwrGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPsePwrMonitorCapable")
)
if mibBuilder.loadTexts:
    cpeExtPseGrpPwrGroup.setStatus("current")

cpeExtPortPolicingActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 10)
)
cpeExtPortPolicingActionGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingAction")
)
if mibBuilder.loadTexts:
    cpeExtPortPolicingActionGroup.setStatus("current")

cpeExtPortPwrManAllocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 11)
)
cpeExtPortPwrManAllocGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrManAlloc")
)
if mibBuilder.loadTexts:
    cpeExtPortPwrManAllocGroup.setStatus("current")

cpeExtPolicingNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 12)
)
cpeExtPolicingNotifEnableGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifEnable")
)
if mibBuilder.loadTexts:
    cpeExtPolicingNotifEnableGroup.setStatus("current")

cpeExtPowerPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 14)
)
cpeExtPowerPriorityGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPowerPriorityEnable")
)
if mibBuilder.loadTexts:
    cpeExtPowerPriorityGroup.setStatus("current")

cpeExtPsePortLldpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 15)
)
cpeExtPsePortLldpGroup.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrType"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrType"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrSrc"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrSrc"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrPriority"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrPriority"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrReq"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrReq"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrAlloc"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrAlloc"))
)
if mibBuilder.loadTexts:
    cpeExtPsePortLldpGroup.setStatus("current")

cpeExtPsePortCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 16)
)
cpeExtPsePortCapabilitiesGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortCapabilities")
)
if mibBuilder.loadTexts:
    cpeExtPsePortCapabilitiesGroup.setStatus("current")

cpeExtPsePortLldpPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 17)
)
cpeExtPsePortLldpPowerGroup.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrClass"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrClass"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrSupport"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrPairsOrZero"))
)
if mibBuilder.loadTexts:
    cpeExtPsePortLldpPowerGroup.setStatus("current")


# Notification objects

cpeExtPolicingNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 0, 1)
)
cpeExtPolicingNotif.setObjects(
      *(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingAction"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortAdditionalStatus"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrAllocated"),
        ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortMaxPwrDrawn"))
)
if mibBuilder.loadTexts:
    cpeExtPolicingNotif.setStatus(
        "current"
    )


# Notifications groups

cpeExtPolicingNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 13)
)
cpeExtPolicingNotifGroup.setObjects(
    ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotif")
)
if mibBuilder.loadTexts:
    cpeExtPolicingNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cpeExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpeExtMIBCompliance.setStatus(
        "deprecated"
    )

cpeExtMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cpeExtMIBCompliance2.setStatus(
        "deprecated"
    )

cpeExtMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cpeExtMIBCompliance3.setStatus(
        "deprecated"
    )

cpeExtMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cpeExtMIBCompliance4.setStatus(
        "deprecated"
    )

cpeExtMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cpeExtMIBCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-POWER-ETHERNET-EXT-MIB",
    **{"CpeExtLldpPwrType": CpeExtLldpPwrType,
       "CpeExtLldpPwrSrc": CpeExtLldpPwrSrc,
       "CpeExtPwrPriority": CpeExtPwrPriority,
       "CpeExtLldpPwrClassOrZero": CpeExtLldpPwrClassOrZero,
       "ciscoPowerEthernetExtMIB": ciscoPowerEthernetExtMIB,
       "cpeExtMIBNotifs": cpeExtMIBNotifs,
       "cpeExtPolicingNotif": cpeExtPolicingNotif,
       "cpeExtMIBObjects": cpeExtMIBObjects,
       "cpeExtDefaultAllocation": cpeExtDefaultAllocation,
       "cpeExtPsePortTable": cpeExtPsePortTable,
       "cpeExtPsePortEntry": cpeExtPsePortEntry,
       "cpeExtPsePortEnable": cpeExtPsePortEnable,
       "cpeExtPsePortDiscoverMode": cpeExtPsePortDiscoverMode,
       "cpeExtPsePortDeviceDetected": cpeExtPsePortDeviceDetected,
       "cpeExtPsePortIeeePd": cpeExtPsePortIeeePd,
       "cpeExtPsePortAdditionalStatus": cpeExtPsePortAdditionalStatus,
       "cpeExtPsePortPwrMax": cpeExtPsePortPwrMax,
       "cpeExtPsePortPwrAllocated": cpeExtPsePortPwrAllocated,
       "cpeExtPsePortPwrAvailable": cpeExtPsePortPwrAvailable,
       "cpeExtPsePortPwrConsumption": cpeExtPsePortPwrConsumption,
       "cpeExtPsePortMaxPwrDrawn": cpeExtPsePortMaxPwrDrawn,
       "cpeExtPsePortEntPhyIndex": cpeExtPsePortEntPhyIndex,
       "cpeExtPsePortPolicingCapable": cpeExtPsePortPolicingCapable,
       "cpeExtPsePortPolicingEnable": cpeExtPsePortPolicingEnable,
       "cpeExtPsePortPolicingAction": cpeExtPsePortPolicingAction,
       "cpeExtPsePortPwrManAlloc": cpeExtPsePortPwrManAlloc,
       "cpeExtPsePortCapabilities": cpeExtPsePortCapabilities,
       "cpeExtMainPseTable": cpeExtMainPseTable,
       "cpeExtMainPseEntry": cpeExtMainPseEntry,
       "cpeExtMainPseEntPhyIndex": cpeExtMainPseEntPhyIndex,
       "cpeExtMainPseDescr": cpeExtMainPseDescr,
       "cpeExtMainPsePwrMonitorCapable": cpeExtMainPsePwrMonitorCapable,
       "cpeExtPdStatistics": cpeExtPdStatistics,
       "cpeExtPdStatsTotalDevices": cpeExtPdStatsTotalDevices,
       "cpeExtPdStatsTable": cpeExtPdStatsTable,
       "cpeExtPdStatsEntry": cpeExtPdStatsEntry,
       "cpeExtPdStatsClass": cpeExtPdStatsClass,
       "cpeExtPdStatsDeviceCount": cpeExtPdStatsDeviceCount,
       "cpeExtPolicingNotifEnable": cpeExtPolicingNotifEnable,
       "cpeExtPowerPriorityEnable": cpeExtPowerPriorityEnable,
       "cpeExtPsePortLldpTable": cpeExtPsePortLldpTable,
       "cpeExtPsePortLldpEntry": cpeExtPsePortLldpEntry,
       "cpeExtPsePortLldpPwrType": cpeExtPsePortLldpPwrType,
       "cpeExtPsePortLldpPdPwrType": cpeExtPsePortLldpPdPwrType,
       "cpeExtPsePortLldpPwrSrc": cpeExtPsePortLldpPwrSrc,
       "cpeExtPsePortLldpPdPwrSrc": cpeExtPsePortLldpPdPwrSrc,
       "cpeExtPsePortLldpPwrPriority": cpeExtPsePortLldpPwrPriority,
       "cpeExtPsePortLldpPdPwrPriority": cpeExtPsePortLldpPdPwrPriority,
       "cpeExtPsePortLldpPwrReq": cpeExtPsePortLldpPwrReq,
       "cpeExtPsePortLldpPdPwrReq": cpeExtPsePortLldpPdPwrReq,
       "cpeExtPsePortLldpPwrAlloc": cpeExtPsePortLldpPwrAlloc,
       "cpeExtPsePortLldpPdPwrAlloc": cpeExtPsePortLldpPdPwrAlloc,
       "cpeExtPsePortLldpPwrClass": cpeExtPsePortLldpPwrClass,
       "cpeExtPsePortLldpPdPwrClass": cpeExtPsePortLldpPdPwrClass,
       "cpeExtPsePortLldpPdPwrSupport": cpeExtPsePortLldpPdPwrSupport,
       "cpeExtPsePortLldpPdPwrPairsOrZero": cpeExtPsePortLldpPdPwrPairsOrZero,
       "cpeExtMIBConformance": cpeExtMIBConformance,
       "cpeExtMIBCompliances": cpeExtMIBCompliances,
       "cpeExtMIBCompliance": cpeExtMIBCompliance,
       "cpeExtMIBCompliance2": cpeExtMIBCompliance2,
       "cpeExtMIBCompliance3": cpeExtMIBCompliance3,
       "cpeExtMIBCompliance4": cpeExtMIBCompliance4,
       "cpeExtMIBCompliance5": cpeExtMIBCompliance5,
       "cpeExtMIBGroups": cpeExtMIBGroups,
       "cpeExtPsePortGroup": cpeExtPsePortGroup,
       "cpeExtPsePortGlobalConfigGroup": cpeExtPsePortGlobalConfigGroup,
       "cpeExtPsePortPwrMonitorGroup": cpeExtPsePortPwrMonitorGroup,
       "cpeExtMainPseGroup": cpeExtMainPseGroup,
       "cpeExtPortEntityIndexGroup": cpeExtPortEntityIndexGroup,
       "cpeExtPortPolicingGroup": cpeExtPortPolicingGroup,
       "cpeExtPdStatsGroup": cpeExtPdStatsGroup,
       "cpeExtMainPseGroup2": cpeExtMainPseGroup2,
       "cpeExtPseGrpPwrGroup": cpeExtPseGrpPwrGroup,
       "cpeExtPortPolicingActionGroup": cpeExtPortPolicingActionGroup,
       "cpeExtPortPwrManAllocGroup": cpeExtPortPwrManAllocGroup,
       "cpeExtPolicingNotifEnableGroup": cpeExtPolicingNotifEnableGroup,
       "cpeExtPolicingNotifGroup": cpeExtPolicingNotifGroup,
       "cpeExtPowerPriorityGroup": cpeExtPowerPriorityGroup,
       "cpeExtPsePortLldpGroup": cpeExtPsePortLldpGroup,
       "cpeExtPsePortCapabilitiesGroup": cpeExtPsePortCapabilitiesGroup,
       "cpeExtPsePortLldpPowerGroup": cpeExtPsePortLldpPowerGroup}
)
