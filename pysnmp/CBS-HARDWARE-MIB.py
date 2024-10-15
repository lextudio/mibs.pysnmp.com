# SNMP MIB module (CBS-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CBS-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:46 2024
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

(cbsMIBs,
 cbsMgmt,
 cbsTraps) = mibBuilder.importSymbols(
    "CROSSBEAM-SYSTEMS-MIB",
    "cbsMIBs",
    "cbsMgmt",
    "cbsTraps")

(KBytes,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "KBytes",
    "ProductID")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cbsHardwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 3, 2)
)
cbsHardwareMIB.setRevisions(
        ("2002-03-15 00:00",
         "2002-08-21 00:00",
         "2003-05-08 00:00",
         "2003-07-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperationalState(Integer32, TextualConvention):
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
        *(("down", 2),
          ("not-present", 3),
          ("up", 1))
    )



class ExistentialState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 2),
          ("present", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CbsHardware_ObjectIdentity = ObjectIdentity
cbsHardware = _CbsHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1)
)
_CbsHwSystem_ObjectIdentity = ObjectIdentity
cbsHwSystem = _CbsHwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 1)
)
_CbsHwSystemProductID_Type = ProductID
_CbsHwSystemProductID_Object = MibScalar
cbsHwSystemProductID = _CbsHwSystemProductID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 1),
    _CbsHwSystemProductID_Type()
)
cbsHwSystemProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemProductID.setStatus("current")
_CbsHwSystemDescription_Type = DisplayString
_CbsHwSystemDescription_Object = MibScalar
cbsHwSystemDescription = _CbsHwSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 2),
    _CbsHwSystemDescription_Type()
)
cbsHwSystemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemDescription.setStatus("current")
_CbsHwSystemSerialNumber_Type = DisplayString
_CbsHwSystemSerialNumber_Object = MibScalar
cbsHwSystemSerialNumber = _CbsHwSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 3),
    _CbsHwSystemSerialNumber_Type()
)
cbsHwSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemSerialNumber.setStatus("current")
_CbsHwSystemBackplaneRevision_Type = DisplayString
_CbsHwSystemBackplaneRevision_Object = MibScalar
cbsHwSystemBackplaneRevision = _CbsHwSystemBackplaneRevision_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 4),
    _CbsHwSystemBackplaneRevision_Type()
)
cbsHwSystemBackplaneRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemBackplaneRevision.setStatus("current")
_CbsHwSystemStatus_ObjectIdentity = ObjectIdentity
cbsHwSystemStatus = _CbsHwSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2)
)
_CbsHwSystemRedundentPowerSupplyStatus_Type = OperationalState
_CbsHwSystemRedundentPowerSupplyStatus_Object = MibScalar
cbsHwSystemRedundentPowerSupplyStatus = _CbsHwSystemRedundentPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 1),
    _CbsHwSystemRedundentPowerSupplyStatus_Type()
)
cbsHwSystemRedundentPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemRedundentPowerSupplyStatus.setStatus("obsolete")
_CbsHwSystemRedundentPowerFeedStatus_Type = OperationalState
_CbsHwSystemRedundentPowerFeedStatus_Object = MibScalar
cbsHwSystemRedundentPowerFeedStatus = _CbsHwSystemRedundentPowerFeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 2),
    _CbsHwSystemRedundentPowerFeedStatus_Type()
)
cbsHwSystemRedundentPowerFeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemRedundentPowerFeedStatus.setStatus("obsolete")


class _CbsHwSystemChassisTemp_Type(Integer32):
    """Custom type cbsHwSystemChassisTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 50),
    )


_CbsHwSystemChassisTemp_Type.__name__ = "Integer32"
_CbsHwSystemChassisTemp_Object = MibScalar
cbsHwSystemChassisTemp = _CbsHwSystemChassisTemp_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 3),
    _CbsHwSystemChassisTemp_Type()
)
cbsHwSystemChassisTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemChassisTemp.setStatus("current")
_CbsHwSystemUpperFanTray_Type = ExistentialState
_CbsHwSystemUpperFanTray_Object = MibScalar
cbsHwSystemUpperFanTray = _CbsHwSystemUpperFanTray_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 4),
    _CbsHwSystemUpperFanTray_Type()
)
cbsHwSystemUpperFanTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemUpperFanTray.setStatus("current")
_CbsHwSystemLowerFanTray_Type = ExistentialState
_CbsHwSystemLowerFanTray_Object = MibScalar
cbsHwSystemLowerFanTray = _CbsHwSystemLowerFanTray_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 5),
    _CbsHwSystemLowerFanTray_Type()
)
cbsHwSystemLowerFanTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemLowerFanTray.setStatus("current")


class _CbsHwSystemAlarm_Type(Integer32):
    """Custom type cbsHwSystemAlarm based on Integer32"""
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("none", 1))
    )


_CbsHwSystemAlarm_Type.__name__ = "Integer32"
_CbsHwSystemAlarm_Object = MibScalar
cbsHwSystemAlarm = _CbsHwSystemAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 6),
    _CbsHwSystemAlarm_Type()
)
cbsHwSystemAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemAlarm.setStatus("current")


class _CbsHwSystemPowerType_Type(Integer32):
    """Custom type cbsHwSystemPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("unknown", 3))
    )


_CbsHwSystemPowerType_Type.__name__ = "Integer32"
_CbsHwSystemPowerType_Object = MibScalar
cbsHwSystemPowerType = _CbsHwSystemPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 7),
    _CbsHwSystemPowerType_Type()
)
cbsHwSystemPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemPowerType.setStatus("current")
_CbsHwSystemRedundentACPowerSupplyStatus_Type = OperationalState
_CbsHwSystemRedundentACPowerSupplyStatus_Object = MibScalar
cbsHwSystemRedundentACPowerSupplyStatus = _CbsHwSystemRedundentACPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 8),
    _CbsHwSystemRedundentACPowerSupplyStatus_Type()
)
cbsHwSystemRedundentACPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemRedundentACPowerSupplyStatus.setStatus("current")
_CbsHwSystemRedundentACPowerFeedStatus_Type = OperationalState
_CbsHwSystemRedundentACPowerFeedStatus_Object = MibScalar
cbsHwSystemRedundentACPowerFeedStatus = _CbsHwSystemRedundentACPowerFeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 9),
    _CbsHwSystemRedundentACPowerFeedStatus_Type()
)
cbsHwSystemRedundentACPowerFeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemRedundentACPowerFeedStatus.setStatus("current")
_CbsHwSystemDCPowerFilterA_Type = ExistentialState
_CbsHwSystemDCPowerFilterA_Object = MibScalar
cbsHwSystemDCPowerFilterA = _CbsHwSystemDCPowerFilterA_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 10),
    _CbsHwSystemDCPowerFilterA_Type()
)
cbsHwSystemDCPowerFilterA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemDCPowerFilterA.setStatus("current")
_CbsHwSystemDCPowerFilterB_Type = ExistentialState
_CbsHwSystemDCPowerFilterB_Object = MibScalar
cbsHwSystemDCPowerFilterB = _CbsHwSystemDCPowerFilterB_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 11),
    _CbsHwSystemDCPowerFilterB_Type()
)
cbsHwSystemDCPowerFilterB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemDCPowerFilterB.setStatus("current")
_CbsHwSystemDCPowerFeedA_Type = ExistentialState
_CbsHwSystemDCPowerFeedA_Object = MibScalar
cbsHwSystemDCPowerFeedA = _CbsHwSystemDCPowerFeedA_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 12),
    _CbsHwSystemDCPowerFeedA_Type()
)
cbsHwSystemDCPowerFeedA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemDCPowerFeedA.setStatus("current")
_CbsHwSystemDCPowerFeedB_Type = ExistentialState
_CbsHwSystemDCPowerFeedB_Object = MibScalar
cbsHwSystemDCPowerFeedB = _CbsHwSystemDCPowerFeedB_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 13),
    _CbsHwSystemDCPowerFeedB_Type()
)
cbsHwSystemDCPowerFeedB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSystemDCPowerFeedB.setStatus("current")
_CbsFanStatusTable_Object = MibTable
cbsFanStatusTable = _CbsFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cbsFanStatusTable.setStatus("current")
_CbsFanStatusEntry_Object = MibTableRow
cbsFanStatusEntry = _CbsFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1)
)
cbsFanStatusEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsFanGroupIndex"),
    (0, "CBS-HARDWARE-MIB", "cbsFanIndex"),
)
if mibBuilder.loadTexts:
    cbsFanStatusEntry.setStatus("current")


class _CbsFanGroupIndex_Type(Integer32):
    """Custom type cbsFanGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_CbsFanGroupIndex_Type.__name__ = "Integer32"
_CbsFanGroupIndex_Object = MibTableColumn
cbsFanGroupIndex = _CbsFanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1, 1),
    _CbsFanGroupIndex_Type()
)
cbsFanGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsFanGroupIndex.setStatus("current")


class _CbsFanIndex_Type(Integer32):
    """Custom type cbsFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CbsFanIndex_Type.__name__ = "Integer32"
_CbsFanIndex_Object = MibTableColumn
cbsFanIndex = _CbsFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1, 2),
    _CbsFanIndex_Type()
)
cbsFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsFanIndex.setStatus("current")
_CbsFanStatus_Type = OperationalState
_CbsFanStatus_Object = MibTableColumn
cbsFanStatus = _CbsFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1, 3),
    _CbsFanStatus_Type()
)
cbsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsFanStatus.setStatus("current")
_CbsHwModuleTable_Object = MibTable
cbsHwModuleTable = _CbsHwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cbsHwModuleTable.setStatus("current")
_CbsHwModuleEntry_Object = MibTableRow
cbsHwModuleEntry = _CbsHwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1)
)
cbsHwModuleEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
)
if mibBuilder.loadTexts:
    cbsHwModuleEntry.setStatus("current")


class _CbsHwModuleID_Type(Integer32):
    """Custom type cbsHwModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CbsHwModuleID_Type.__name__ = "Integer32"
_CbsHwModuleID_Object = MibTableColumn
cbsHwModuleID = _CbsHwModuleID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 1),
    _CbsHwModuleID_Type()
)
cbsHwModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleID.setStatus("current")
_CbsHwModuleProductID_Type = ProductID
_CbsHwModuleProductID_Object = MibTableColumn
cbsHwModuleProductID = _CbsHwModuleProductID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 2),
    _CbsHwModuleProductID_Type()
)
cbsHwModuleProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleProductID.setStatus("current")
_CbsHwModuleDescription_Type = DisplayString
_CbsHwModuleDescription_Object = MibTableColumn
cbsHwModuleDescription = _CbsHwModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 3),
    _CbsHwModuleDescription_Type()
)
cbsHwModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleDescription.setStatus("current")
_CbsHwModuleBoardRevision_Type = DisplayString
_CbsHwModuleBoardRevision_Object = MibTableColumn
cbsHwModuleBoardRevision = _CbsHwModuleBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 4),
    _CbsHwModuleBoardRevision_Type()
)
cbsHwModuleBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleBoardRevision.setStatus("current")
_CbsHwModuleSerialNumber_Type = DisplayString
_CbsHwModuleSerialNumber_Object = MibTableColumn
cbsHwModuleSerialNumber = _CbsHwModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 5),
    _CbsHwModuleSerialNumber_Type()
)
cbsHwModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleSerialNumber.setStatus("current")
_CbsHwModuleBootStrapRev_Type = DisplayString
_CbsHwModuleBootStrapRev_Object = MibTableColumn
cbsHwModuleBootStrapRev = _CbsHwModuleBootStrapRev_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 6),
    _CbsHwModuleBootStrapRev_Type()
)
cbsHwModuleBootStrapRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleBootStrapRev.setStatus("current")
_CbsHwModuleBootloaderRev_Type = DisplayString
_CbsHwModuleBootloaderRev_Object = MibTableColumn
cbsHwModuleBootloaderRev = _CbsHwModuleBootloaderRev_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 7),
    _CbsHwModuleBootloaderRev_Type()
)
cbsHwModuleBootloaderRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleBootloaderRev.setStatus("current")
_CbsHwModuleDiagnosticsRev_Type = DisplayString
_CbsHwModuleDiagnosticsRev_Object = MibTableColumn
cbsHwModuleDiagnosticsRev = _CbsHwModuleDiagnosticsRev_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 8),
    _CbsHwModuleDiagnosticsRev_Type()
)
cbsHwModuleDiagnosticsRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleDiagnosticsRev.setStatus("current")
_CbsHwModuleSDRAMSize_Type = KBytes
_CbsHwModuleSDRAMSize_Object = MibTableColumn
cbsHwModuleSDRAMSize = _CbsHwModuleSDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 9),
    _CbsHwModuleSDRAMSize_Type()
)
cbsHwModuleSDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleSDRAMSize.setStatus("current")
_CbsHwModuleRDRAMSize_Type = KBytes
_CbsHwModuleRDRAMSize_Object = MibTableColumn
cbsHwModuleRDRAMSize = _CbsHwModuleRDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 10),
    _CbsHwModuleRDRAMSize_Type()
)
cbsHwModuleRDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleRDRAMSize.setStatus("current")
_CbsHwModuleDiskAPresent_Type = TruthValue
_CbsHwModuleDiskAPresent_Object = MibTableColumn
cbsHwModuleDiskAPresent = _CbsHwModuleDiskAPresent_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 11),
    _CbsHwModuleDiskAPresent_Type()
)
cbsHwModuleDiskAPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleDiskAPresent.setStatus("current")
_CbsHwModuleDiskBPresent_Type = TruthValue
_CbsHwModuleDiskBPresent_Object = MibTableColumn
cbsHwModuleDiskBPresent = _CbsHwModuleDiskBPresent_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 12),
    _CbsHwModuleDiskBPresent_Type()
)
cbsHwModuleDiskBPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleDiskBPresent.setStatus("current")
_CbsHwModuleDuartAPresent_Type = TruthValue
_CbsHwModuleDuartAPresent_Object = MibTableColumn
cbsHwModuleDuartAPresent = _CbsHwModuleDuartAPresent_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 13),
    _CbsHwModuleDuartAPresent_Type()
)
cbsHwModuleDuartAPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleDuartAPresent.setStatus("current")
_CbsHwModuleDuartBPresent_Type = TruthValue
_CbsHwModuleDuartBPresent_Object = MibTableColumn
cbsHwModuleDuartBPresent = _CbsHwModuleDuartBPresent_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 14),
    _CbsHwModuleDuartBPresent_Type()
)
cbsHwModuleDuartBPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleDuartBPresent.setStatus("current")
_CbsHwModuleAccelCard1Present_Type = TruthValue
_CbsHwModuleAccelCard1Present_Object = MibTableColumn
cbsHwModuleAccelCard1Present = _CbsHwModuleAccelCard1Present_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 15),
    _CbsHwModuleAccelCard1Present_Type()
)
cbsHwModuleAccelCard1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleAccelCard1Present.setStatus("current")
_CbsHwModuleAccelCard2Present_Type = TruthValue
_CbsHwModuleAccelCard2Present_Object = MibTableColumn
cbsHwModuleAccelCard2Present = _CbsHwModuleAccelCard2Present_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 16),
    _CbsHwModuleAccelCard2Present_Type()
)
cbsHwModuleAccelCard2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleAccelCard2Present.setStatus("current")
_CbsHwComponentRevTable_Object = MibTable
cbsHwComponentRevTable = _CbsHwComponentRevTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cbsHwComponentRevTable.setStatus("current")
_CbsHwComponentRevEntry_Object = MibTableRow
cbsHwComponentRevEntry = _CbsHwComponentRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1)
)
cbsHwComponentRevEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwModuleID"),
    (0, "CBS-HARDWARE-MIB", "cbsHwComponentIndex"),
)
if mibBuilder.loadTexts:
    cbsHwComponentRevEntry.setStatus("current")
_CbsHwComponentIndex_Type = Unsigned32
_CbsHwComponentIndex_Object = MibTableColumn
cbsHwComponentIndex = _CbsHwComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1, 1),
    _CbsHwComponentIndex_Type()
)
cbsHwComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsHwComponentIndex.setStatus("current")
_CbsHwComponentDescription_Type = DisplayString
_CbsHwComponentDescription_Object = MibTableColumn
cbsHwComponentDescription = _CbsHwComponentDescription_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1, 2),
    _CbsHwComponentDescription_Type()
)
cbsHwComponentDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwComponentDescription.setStatus("current")
_CbsHwComponentRevision_Type = OctetString
_CbsHwComponentRevision_Object = MibTableColumn
cbsHwComponentRevision = _CbsHwComponentRevision_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1, 3),
    _CbsHwComponentRevision_Type()
)
cbsHwComponentRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwComponentRevision.setStatus("current")
_CbsHwModuleStatusTable_Object = MibTable
cbsHwModuleStatusTable = _CbsHwModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cbsHwModuleStatusTable.setStatus("current")
_CbsHwModuleStatusEntry_Object = MibTableRow
cbsHwModuleStatusEntry = _CbsHwModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cbsHwModuleStatusEntry.setStatus("current")


class _CbsHwModuleStatus_Type(Integer32):
    """Custom type cbsHwModuleStatus based on Integer32"""
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
        *(("bootwait", 6),
          ("down", 2),
          ("initializing", 3),
          ("standby", 5),
          ("unavailable", 1),
          ("up", 4))
    )


_CbsHwModuleStatus_Type.__name__ = "Integer32"
_CbsHwModuleStatus_Object = MibTableColumn
cbsHwModuleStatus = _CbsHwModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 1),
    _CbsHwModuleStatus_Type()
)
cbsHwModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleStatus.setStatus("current")


class _CbsHwModuleCpuTemp_Type(Integer32):
    """Custom type cbsHwModuleCpuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 50),
    )


_CbsHwModuleCpuTemp_Type.__name__ = "Integer32"
_CbsHwModuleCpuTemp_Object = MibTableColumn
cbsHwModuleCpuTemp = _CbsHwModuleCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 2),
    _CbsHwModuleCpuTemp_Type()
)
cbsHwModuleCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleCpuTemp.setStatus("current")


class _CbsHwModuleFPGATemp_Type(Integer32):
    """Custom type cbsHwModuleFPGATemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 75),
    )


_CbsHwModuleFPGATemp_Type.__name__ = "Integer32"
_CbsHwModuleFPGATemp_Object = MibTableColumn
cbsHwModuleFPGATemp = _CbsHwModuleFPGATemp_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 3),
    _CbsHwModuleFPGATemp_Type()
)
cbsHwModuleFPGATemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleFPGATemp.setStatus("current")


class _CbsHwModuleInTemp_Type(Integer32):
    """Custom type cbsHwModuleInTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 75),
    )


_CbsHwModuleInTemp_Type.__name__ = "Integer32"
_CbsHwModuleInTemp_Object = MibTableColumn
cbsHwModuleInTemp = _CbsHwModuleInTemp_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 4),
    _CbsHwModuleInTemp_Type()
)
cbsHwModuleInTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleInTemp.setStatus("current")
_CbsHwModuleInTempAlarm_Type = TruthValue
_CbsHwModuleInTempAlarm_Object = MibTableColumn
cbsHwModuleInTempAlarm = _CbsHwModuleInTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 5),
    _CbsHwModuleInTempAlarm_Type()
)
cbsHwModuleInTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleInTempAlarm.setStatus("current")


class _CbsHwModuleExhaustTemp_Type(Integer32):
    """Custom type cbsHwModuleExhaustTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 75),
    )


_CbsHwModuleExhaustTemp_Type.__name__ = "Integer32"
_CbsHwModuleExhaustTemp_Object = MibTableColumn
cbsHwModuleExhaustTemp = _CbsHwModuleExhaustTemp_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 6),
    _CbsHwModuleExhaustTemp_Type()
)
cbsHwModuleExhaustTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleExhaustTemp.setStatus("current")
_CbsHwModuleExhaustTempAlarm_Type = TruthValue
_CbsHwModuleExhaustTempAlarm_Object = MibTableColumn
cbsHwModuleExhaustTempAlarm = _CbsHwModuleExhaustTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 7),
    _CbsHwModuleExhaustTempAlarm_Type()
)
cbsHwModuleExhaustTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleExhaustTempAlarm.setStatus("current")
_CbsHwModuleCPUVoltage_Type = Gauge32
_CbsHwModuleCPUVoltage_Object = MibTableColumn
cbsHwModuleCPUVoltage = _CbsHwModuleCPUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 8),
    _CbsHwModuleCPUVoltage_Type()
)
cbsHwModuleCPUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleCPUVoltage.setStatus("current")
_CbsHwModule1_8Voltage_Type = Gauge32
_CbsHwModule1_8Voltage_Object = MibScalar
cbsHwModule1_8Voltage = _CbsHwModule1_8Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 9),
    _CbsHwModule1_8Voltage_Type()
)
cbsHwModule1_8Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModule1_8Voltage.setStatus("current")
_CbsHwModule3_3Voltage_Type = Gauge32
_CbsHwModule3_3Voltage_Object = MibScalar
cbsHwModule3_3Voltage = _CbsHwModule3_3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 10),
    _CbsHwModule3_3Voltage_Type()
)
cbsHwModule3_3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModule3_3Voltage.setStatus("current")
_CbsHwModule2_5Voltage_Type = Gauge32
_CbsHwModule2_5Voltage_Object = MibScalar
cbsHwModule2_5Voltage = _CbsHwModule2_5Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 11),
    _CbsHwModule2_5Voltage_Type()
)
cbsHwModule2_5Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModule2_5Voltage.setStatus("current")
_CbsHwModuleControlLinkA_Type = OperationalState
_CbsHwModuleControlLinkA_Object = MibTableColumn
cbsHwModuleControlLinkA = _CbsHwModuleControlLinkA_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 12),
    _CbsHwModuleControlLinkA_Type()
)
cbsHwModuleControlLinkA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleControlLinkA.setStatus("current")
_CbsHwModuleControlLinkB_Type = OperationalState
_CbsHwModuleControlLinkB_Object = MibTableColumn
cbsHwModuleControlLinkB = _CbsHwModuleControlLinkB_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 13),
    _CbsHwModuleControlLinkB_Type()
)
cbsHwModuleControlLinkB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleControlLinkB.setStatus("current")
_CbsHwModuleActiveLED_Type = TruthValue
_CbsHwModuleActiveLED_Object = MibTableColumn
cbsHwModuleActiveLED = _CbsHwModuleActiveLED_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 14),
    _CbsHwModuleActiveLED_Type()
)
cbsHwModuleActiveLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleActiveLED.setStatus("current")
_CbsHwModuleStandbyLED_Type = TruthValue
_CbsHwModuleStandbyLED_Object = MibTableColumn
cbsHwModuleStandbyLED = _CbsHwModuleStandbyLED_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 15),
    _CbsHwModuleStandbyLED_Type()
)
cbsHwModuleStandbyLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleStandbyLED.setStatus("current")
_CbsHwModuleFailedLED_Type = TruthValue
_CbsHwModuleFailedLED_Object = MibTableColumn
cbsHwModuleFailedLED = _CbsHwModuleFailedLED_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 16),
    _CbsHwModuleFailedLED_Type()
)
cbsHwModuleFailedLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleFailedLED.setStatus("current")


class _CbsHwModuleCpu2Temp_Type(Integer32):
    """Custom type cbsHwModuleCpu2Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25, 50),
    )


_CbsHwModuleCpu2Temp_Type.__name__ = "Integer32"
_CbsHwModuleCpu2Temp_Object = MibTableColumn
cbsHwModuleCpu2Temp = _CbsHwModuleCpu2Temp_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 17),
    _CbsHwModuleCpu2Temp_Type()
)
cbsHwModuleCpu2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleCpu2Temp.setStatus("current")
_CbsHwModuleCPU2Voltage_Type = Gauge32
_CbsHwModuleCPU2Voltage_Object = MibTableColumn
cbsHwModuleCPU2Voltage = _CbsHwModuleCPU2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 18),
    _CbsHwModuleCPU2Voltage_Type()
)
cbsHwModuleCPU2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleCPU2Voltage.setStatus("current")
_CbsHwModuleFPGA1_8Voltage_Type = Gauge32
_CbsHwModuleFPGA1_8Voltage_Object = MibScalar
cbsHwModuleFPGA1_8Voltage = _CbsHwModuleFPGA1_8Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 19),
    _CbsHwModuleFPGA1_8Voltage_Type()
)
cbsHwModuleFPGA1_8Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModuleFPGA1_8Voltage.setStatus("current")
_CbsHwModule125Voltage_Type = Gauge32
_CbsHwModule125Voltage_Object = MibTableColumn
cbsHwModule125Voltage = _CbsHwModule125Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 20),
    _CbsHwModule125Voltage_Type()
)
cbsHwModule125Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwModule125Voltage.setStatus("current")
_CbsHwSdpStatusTable_Object = MibTable
cbsHwSdpStatusTable = _CbsHwSdpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cbsHwSdpStatusTable.setStatus("current")
_CbsHwSdpStatusEntry_Object = MibTableRow
cbsHwSdpStatusEntry = _CbsHwSdpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1)
)
cbsHwSdpStatusEntry.setIndexNames(
    (0, "CBS-HARDWARE-MIB", "cbsHwSdpNpmSlot"),
    (0, "CBS-HARDWARE-MIB", "cbsHwSdpRemoteSlot"),
)
if mibBuilder.loadTexts:
    cbsHwSdpStatusEntry.setStatus("current")


class _CbsHwSdpNpmSlot_Type(Unsigned32):
    """Custom type cbsHwSdpNpmSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CbsHwSdpNpmSlot_Type.__name__ = "Unsigned32"
_CbsHwSdpNpmSlot_Object = MibTableColumn
cbsHwSdpNpmSlot = _CbsHwSdpNpmSlot_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 1),
    _CbsHwSdpNpmSlot_Type()
)
cbsHwSdpNpmSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsHwSdpNpmSlot.setStatus("current")


class _CbsHwSdpRemoteSlot_Type(Unsigned32):
    """Custom type cbsHwSdpRemoteSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CbsHwSdpRemoteSlot_Type.__name__ = "Unsigned32"
_CbsHwSdpRemoteSlot_Object = MibTableColumn
cbsHwSdpRemoteSlot = _CbsHwSdpRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 2),
    _CbsHwSdpRemoteSlot_Type()
)
cbsHwSdpRemoteSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cbsHwSdpRemoteSlot.setStatus("current")
_CbsHwSdpNpmState_Type = OperationalState
_CbsHwSdpNpmState_Object = MibTableColumn
cbsHwSdpNpmState = _CbsHwSdpNpmState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 3),
    _CbsHwSdpNpmState_Type()
)
cbsHwSdpNpmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSdpNpmState.setStatus("current")
_CbsHwSdpRemoteState_Type = OperationalState
_CbsHwSdpRemoteState_Object = MibTableColumn
cbsHwSdpRemoteState = _CbsHwSdpRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 4),
    _CbsHwSdpRemoteState_Type()
)
cbsHwSdpRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsHwSdpRemoteState.setStatus("current")
_CbsHwTraps_ObjectIdentity = ObjectIdentity
cbsHwTraps = _CbsHwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1)
)
cbsHwModuleEntry.registerAugmentions(
    ("CBS-HARDWARE-MIB",
     "cbsHwModuleStatusEntry")
)
cbsHwModuleStatusEntry.setIndexNames(*cbsHwModuleEntry.getIndexNames())

# Managed Objects groups


# Notification objects

cbsHwPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cbsHwPowerSupplyFailed.setStatus(
        "current"
    )

cbsHwPowerSupplyRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cbsHwPowerSupplyRecovered.setStatus(
        "current"
    )

cbsHwPowerFeedFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 3)
)
if mibBuilder.loadTexts:
    cbsHwPowerFeedFailed.setStatus(
        "current"
    )

cbsHwPowerFeedRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 4)
)
if mibBuilder.loadTexts:
    cbsHwPowerFeedRecovered.setStatus(
        "current"
    )

cbsHwUpperFanTrayInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 5)
)
if mibBuilder.loadTexts:
    cbsHwUpperFanTrayInserted.setStatus(
        "current"
    )

cbsHwUpperFanTrayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 6)
)
if mibBuilder.loadTexts:
    cbsHwUpperFanTrayRemoved.setStatus(
        "current"
    )

cbsHwLowerFanTrayInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 7)
)
if mibBuilder.loadTexts:
    cbsHwLowerFanTrayInserted.setStatus(
        "current"
    )

cbsHwLowerFanTrayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 8)
)
if mibBuilder.loadTexts:
    cbsHwLowerFanTrayRemoved.setStatus(
        "current"
    )

cbsHwFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 9)
)
cbsHwFanFailed.setObjects(
    ("CBS-HARDWARE-MIB", "cbsFanStatus")
)
if mibBuilder.loadTexts:
    cbsHwFanFailed.setStatus(
        "current"
    )

cbsHwFanRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 10)
)
cbsHwFanRecovered.setObjects(
    ("CBS-HARDWARE-MIB", "cbsFanStatus")
)
if mibBuilder.loadTexts:
    cbsHwFanRecovered.setStatus(
        "current"
    )

cbsHwSystemAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 11)
)
cbsHwSystemAlarmTrap.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwSystemAlarm")
)
if mibBuilder.loadTexts:
    cbsHwSystemAlarmTrap.setStatus(
        "current"
    )

cbsHwChassisTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 12)
)
cbsHwChassisTempExceeded.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwSystemChassisTemp")
)
if mibBuilder.loadTexts:
    cbsHwChassisTempExceeded.setStatus(
        "current"
    )

cbsHwChassisTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 13)
)
cbsHwChassisTempNormal.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwSystemChassisTemp")
)
if mibBuilder.loadTexts:
    cbsHwChassisTempNormal.setStatus(
        "current"
    )

cbsHwModuleStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 14)
)
cbsHwModuleStatusChanged.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleStatus")
)
if mibBuilder.loadTexts:
    cbsHwModuleStatusChanged.setStatus(
        "current"
    )

cbsHwModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 15)
)
cbsHwModuleInserted.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsHwModuleInserted.setStatus(
        "current"
    )

cbsHwModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 16)
)
cbsHwModuleRemoved.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsHwModuleRemoved.setStatus(
        "current"
    )

cbsModuleTempExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 17)
)
cbsModuleTempExceeded.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleCpuTemp")
)
if mibBuilder.loadTexts:
    cbsModuleTempExceeded.setStatus(
        "current"
    )

cbsModuleTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 18)
)
cbsModuleTempNormal.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleCpuTemp")
)
if mibBuilder.loadTexts:
    cbsModuleTempNormal.setStatus(
        "current"
    )

cbsDbhaLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 19)
)
cbsDbhaLinkUp.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsDbhaLinkUp.setStatus(
        "current"
    )

cbsDbhaLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 1, 20)
)
cbsDbhaLinkDown.setObjects(
    ("CBS-HARDWARE-MIB", "cbsHwModuleID")
)
if mibBuilder.loadTexts:
    cbsDbhaLinkDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CBS-HARDWARE-MIB",
    **{"OperationalState": OperationalState,
       "ExistentialState": ExistentialState,
       "cbsHardware": cbsHardware,
       "cbsHwSystem": cbsHwSystem,
       "cbsHwSystemProductID": cbsHwSystemProductID,
       "cbsHwSystemDescription": cbsHwSystemDescription,
       "cbsHwSystemSerialNumber": cbsHwSystemSerialNumber,
       "cbsHwSystemBackplaneRevision": cbsHwSystemBackplaneRevision,
       "cbsHwSystemStatus": cbsHwSystemStatus,
       "cbsHwSystemRedundentPowerSupplyStatus": cbsHwSystemRedundentPowerSupplyStatus,
       "cbsHwSystemRedundentPowerFeedStatus": cbsHwSystemRedundentPowerFeedStatus,
       "cbsHwSystemChassisTemp": cbsHwSystemChassisTemp,
       "cbsHwSystemUpperFanTray": cbsHwSystemUpperFanTray,
       "cbsHwSystemLowerFanTray": cbsHwSystemLowerFanTray,
       "cbsHwSystemAlarm": cbsHwSystemAlarm,
       "cbsHwSystemPowerType": cbsHwSystemPowerType,
       "cbsHwSystemRedundentACPowerSupplyStatus": cbsHwSystemRedundentACPowerSupplyStatus,
       "cbsHwSystemRedundentACPowerFeedStatus": cbsHwSystemRedundentACPowerFeedStatus,
       "cbsHwSystemDCPowerFilterA": cbsHwSystemDCPowerFilterA,
       "cbsHwSystemDCPowerFilterB": cbsHwSystemDCPowerFilterB,
       "cbsHwSystemDCPowerFeedA": cbsHwSystemDCPowerFeedA,
       "cbsHwSystemDCPowerFeedB": cbsHwSystemDCPowerFeedB,
       "cbsFanStatusTable": cbsFanStatusTable,
       "cbsFanStatusEntry": cbsFanStatusEntry,
       "cbsFanGroupIndex": cbsFanGroupIndex,
       "cbsFanIndex": cbsFanIndex,
       "cbsFanStatus": cbsFanStatus,
       "cbsHwModuleTable": cbsHwModuleTable,
       "cbsHwModuleEntry": cbsHwModuleEntry,
       "cbsHwModuleID": cbsHwModuleID,
       "cbsHwModuleProductID": cbsHwModuleProductID,
       "cbsHwModuleDescription": cbsHwModuleDescription,
       "cbsHwModuleBoardRevision": cbsHwModuleBoardRevision,
       "cbsHwModuleSerialNumber": cbsHwModuleSerialNumber,
       "cbsHwModuleBootStrapRev": cbsHwModuleBootStrapRev,
       "cbsHwModuleBootloaderRev": cbsHwModuleBootloaderRev,
       "cbsHwModuleDiagnosticsRev": cbsHwModuleDiagnosticsRev,
       "cbsHwModuleSDRAMSize": cbsHwModuleSDRAMSize,
       "cbsHwModuleRDRAMSize": cbsHwModuleRDRAMSize,
       "cbsHwModuleDiskAPresent": cbsHwModuleDiskAPresent,
       "cbsHwModuleDiskBPresent": cbsHwModuleDiskBPresent,
       "cbsHwModuleDuartAPresent": cbsHwModuleDuartAPresent,
       "cbsHwModuleDuartBPresent": cbsHwModuleDuartBPresent,
       "cbsHwModuleAccelCard1Present": cbsHwModuleAccelCard1Present,
       "cbsHwModuleAccelCard2Present": cbsHwModuleAccelCard2Present,
       "cbsHwComponentRevTable": cbsHwComponentRevTable,
       "cbsHwComponentRevEntry": cbsHwComponentRevEntry,
       "cbsHwComponentIndex": cbsHwComponentIndex,
       "cbsHwComponentDescription": cbsHwComponentDescription,
       "cbsHwComponentRevision": cbsHwComponentRevision,
       "cbsHwModuleStatusTable": cbsHwModuleStatusTable,
       "cbsHwModuleStatusEntry": cbsHwModuleStatusEntry,
       "cbsHwModuleStatus": cbsHwModuleStatus,
       "cbsHwModuleCpuTemp": cbsHwModuleCpuTemp,
       "cbsHwModuleFPGATemp": cbsHwModuleFPGATemp,
       "cbsHwModuleInTemp": cbsHwModuleInTemp,
       "cbsHwModuleInTempAlarm": cbsHwModuleInTempAlarm,
       "cbsHwModuleExhaustTemp": cbsHwModuleExhaustTemp,
       "cbsHwModuleExhaustTempAlarm": cbsHwModuleExhaustTempAlarm,
       "cbsHwModuleCPUVoltage": cbsHwModuleCPUVoltage,
       "cbsHwModule1-8Voltage": cbsHwModule1_8Voltage,
       "cbsHwModule3-3Voltage": cbsHwModule3_3Voltage,
       "cbsHwModule2-5Voltage": cbsHwModule2_5Voltage,
       "cbsHwModuleControlLinkA": cbsHwModuleControlLinkA,
       "cbsHwModuleControlLinkB": cbsHwModuleControlLinkB,
       "cbsHwModuleActiveLED": cbsHwModuleActiveLED,
       "cbsHwModuleStandbyLED": cbsHwModuleStandbyLED,
       "cbsHwModuleFailedLED": cbsHwModuleFailedLED,
       "cbsHwModuleCpu2Temp": cbsHwModuleCpu2Temp,
       "cbsHwModuleCPU2Voltage": cbsHwModuleCPU2Voltage,
       "cbsHwModuleFPGA1-8Voltage": cbsHwModuleFPGA1_8Voltage,
       "cbsHwModule125Voltage": cbsHwModule125Voltage,
       "cbsHwSdpStatusTable": cbsHwSdpStatusTable,
       "cbsHwSdpStatusEntry": cbsHwSdpStatusEntry,
       "cbsHwSdpNpmSlot": cbsHwSdpNpmSlot,
       "cbsHwSdpRemoteSlot": cbsHwSdpRemoteSlot,
       "cbsHwSdpNpmState": cbsHwSdpNpmState,
       "cbsHwSdpRemoteState": cbsHwSdpRemoteState,
       "cbsHardwareMIB": cbsHardwareMIB,
       "cbsHwTraps": cbsHwTraps,
       "cbsHwPowerSupplyFailed": cbsHwPowerSupplyFailed,
       "cbsHwPowerSupplyRecovered": cbsHwPowerSupplyRecovered,
       "cbsHwPowerFeedFailed": cbsHwPowerFeedFailed,
       "cbsHwPowerFeedRecovered": cbsHwPowerFeedRecovered,
       "cbsHwUpperFanTrayInserted": cbsHwUpperFanTrayInserted,
       "cbsHwUpperFanTrayRemoved": cbsHwUpperFanTrayRemoved,
       "cbsHwLowerFanTrayInserted": cbsHwLowerFanTrayInserted,
       "cbsHwLowerFanTrayRemoved": cbsHwLowerFanTrayRemoved,
       "cbsHwFanFailed": cbsHwFanFailed,
       "cbsHwFanRecovered": cbsHwFanRecovered,
       "cbsHwSystemAlarmTrap": cbsHwSystemAlarmTrap,
       "cbsHwChassisTempExceeded": cbsHwChassisTempExceeded,
       "cbsHwChassisTempNormal": cbsHwChassisTempNormal,
       "cbsHwModuleStatusChanged": cbsHwModuleStatusChanged,
       "cbsHwModuleInserted": cbsHwModuleInserted,
       "cbsHwModuleRemoved": cbsHwModuleRemoved,
       "cbsModuleTempExceeded": cbsModuleTempExceeded,
       "cbsModuleTempNormal": cbsModuleTempNormal,
       "cbsDbhaLinkUp": cbsDbhaLinkUp,
       "cbsDbhaLinkDown": cbsDbhaLinkDown}
)
