# SNMP MIB module (RBN-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:52 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rbnApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5)
)
rbnApsMIB.setRevisions(
        ("1999-05-07 23:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsK1K2(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_RbnApsMIBNotifications_ObjectIdentity = ObjectIdentity
rbnApsMIBNotifications = _RbnApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 0)
)
_RbnApsMIBObjects_ObjectIdentity = ObjectIdentity
rbnApsMIBObjects = _RbnApsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1)
)
_ApsConfig_ObjectIdentity = ObjectIdentity
apsConfig = _ApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1)
)
_ApsConfigGroups_Type = Counter32
_ApsConfigGroups_Object = MibScalar
apsConfigGroups = _ApsConfigGroups_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 1),
    _ApsConfigGroups_Type()
)
apsConfigGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsConfigGroups.setStatus("current")
_ApsConfigTable_Object = MibTable
apsConfigTable = _ApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apsConfigTable.setStatus("current")
_ApsConfigEntry_Object = MibTableRow
apsConfigEntry = _ApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1)
)
apsConfigEntry.setIndexNames(
    (1, "RBN-APS-MIB", "apsConfigName"),
)
if mibBuilder.loadTexts:
    apsConfigEntry.setStatus("current")


class _ApsConfigName_Type(DisplayString):
    """Custom type apsConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApsConfigName_Type.__name__ = "DisplayString"
_ApsConfigName_Object = MibTableColumn
apsConfigName = _ApsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 1),
    _ApsConfigName_Type()
)
apsConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsConfigName.setStatus("current")


class _ApsConfigMode_Type(Bits):
    """Custom type apsConfigMode based on Bits"""
    defaultHexValue = "1"

    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("extraTrafficAllowed", 4),
          ("onePlusOne", 0),
          ("oneToN", 1),
          ("revertive", 2))
    )

_ApsConfigMode_Type.__name__ = "Bits"
_ApsConfigMode_Object = MibTableColumn
apsConfigMode = _ApsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 2),
    _ApsConfigMode_Type()
)
apsConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigMode.setStatus("current")


class _ApsConfigSdBerThreshold_Type(Integer32):
    """Custom type apsConfigSdBerThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_ApsConfigSdBerThreshold_Type.__name__ = "Integer32"
_ApsConfigSdBerThreshold_Object = MibTableColumn
apsConfigSdBerThreshold = _ApsConfigSdBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 3),
    _ApsConfigSdBerThreshold_Type()
)
apsConfigSdBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigSdBerThreshold.setStatus("current")


class _ApsConfigSfBerThreshold_Type(Integer32):
    """Custom type apsConfigSfBerThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_ApsConfigSfBerThreshold_Type.__name__ = "Integer32"
_ApsConfigSfBerThreshold_Object = MibTableColumn
apsConfigSfBerThreshold = _ApsConfigSfBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 4),
    _ApsConfigSfBerThreshold_Type()
)
apsConfigSfBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigSfBerThreshold.setStatus("current")


class _ApsConfigWaitToRestore_Type(Integer32):
    """Custom type apsConfigWaitToRestore based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 720),
    )


_ApsConfigWaitToRestore_Type.__name__ = "Integer32"
_ApsConfigWaitToRestore_Object = MibTableColumn
apsConfigWaitToRestore = _ApsConfigWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 5),
    _ApsConfigWaitToRestore_Type()
)
apsConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigWaitToRestore.setStatus("current")
_ApsConfigRowStatus_Type = RowStatus
_ApsConfigRowStatus_Object = MibTableColumn
apsConfigRowStatus = _ApsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 1, 2, 1, 6),
    _ApsConfigRowStatus_Type()
)
apsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigRowStatus.setStatus("current")
_ApsCommandTable_Object = MibTable
apsCommandTable = _ApsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    apsCommandTable.setStatus("current")
_ApsCommandEntry_Object = MibTableRow
apsCommandEntry = _ApsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2, 1)
)
apsCommandEntry.setIndexNames(
    (1, "RBN-APS-MIB", "apsConfigName"),
)
if mibBuilder.loadTexts:
    apsCommandEntry.setStatus("current")
_ApsCommandSwitch_Type = Integer32
_ApsCommandSwitch_Object = MibTableColumn
apsCommandSwitch = _ApsCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2, 1, 1),
    _ApsCommandSwitch_Type()
)
apsCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCommandSwitch.setStatus("current")
_ApsCommandControl_Type = Integer32
_ApsCommandControl_Object = MibTableColumn
apsCommandControl = _ApsCommandControl_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 2, 1, 2),
    _ApsCommandControl_Type()
)
apsCommandControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCommandControl.setStatus("current")
_ApsStatusTable_Object = MibTable
apsStatusTable = _ApsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    apsStatusTable.setStatus("current")
_ApsStatusEntry_Object = MibTableRow
apsStatusEntry = _ApsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1)
)
apsStatusEntry.setIndexNames(
    (1, "RBN-APS-MIB", "apsConfigName"),
)
if mibBuilder.loadTexts:
    apsStatusEntry.setStatus("current")
_ApsStatusK1K2Rcv_Type = ApsK1K2
_ApsStatusK1K2Rcv_Object = MibTableColumn
apsStatusK1K2Rcv = _ApsStatusK1K2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 1),
    _ApsStatusK1K2Rcv_Type()
)
apsStatusK1K2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusK1K2Rcv.setStatus("current")
_ApsStatusK1K2Trans_Type = ApsK1K2
_ApsStatusK1K2Trans_Object = MibTableColumn
apsStatusK1K2Trans = _ApsStatusK1K2Trans_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 2),
    _ApsStatusK1K2Trans_Type()
)
apsStatusK1K2Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusK1K2Trans.setStatus("current")


class _ApsStatusCurrent_Type(Bits):
    """Custom type apsStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("channelMismatch", 1),
          ("extraTraffic", 3),
          ("modeMismatch", 0),
          ("psbf", 2))
    )

_ApsStatusCurrent_Type.__name__ = "Bits"
_ApsStatusCurrent_Object = MibTableColumn
apsStatusCurrent = _ApsStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 3),
    _ApsStatusCurrent_Type()
)
apsStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusCurrent.setStatus("current")
_ApsStatusModeMismatches_Type = Counter32
_ApsStatusModeMismatches_Object = MibTableColumn
apsStatusModeMismatches = _ApsStatusModeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 4),
    _ApsStatusModeMismatches_Type()
)
apsStatusModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusModeMismatches.setStatus("current")
_ApsStatusChannelMismatches_Type = Counter32
_ApsStatusChannelMismatches_Object = MibTableColumn
apsStatusChannelMismatches = _ApsStatusChannelMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 5),
    _ApsStatusChannelMismatches_Type()
)
apsStatusChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusChannelMismatches.setStatus("current")
_ApsStatusPSBFs_Type = Counter32
_ApsStatusPSBFs_Object = MibTableColumn
apsStatusPSBFs = _ApsStatusPSBFs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 6),
    _ApsStatusPSBFs_Type()
)
apsStatusPSBFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusPSBFs.setStatus("current")
_ApsStatusCreationTime_Type = TimeTicks
_ApsStatusCreationTime_Object = MibTableColumn
apsStatusCreationTime = _ApsStatusCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 3, 1, 7),
    _ApsStatusCreationTime_Type()
)
apsStatusCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusCreationTime.setStatus("current")
_ApsChan_ObjectIdentity = ObjectIdentity
apsChan = _ApsChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4)
)
_ApsChanLTEs_Type = Counter32
_ApsChanLTEs_Object = MibScalar
apsChanLTEs = _ApsChanLTEs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 1),
    _ApsChanLTEs_Type()
)
apsChanLTEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanLTEs.setStatus("current")
_ApsChanTable_Object = MibTable
apsChanTable = _ApsChanTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    apsChanTable.setStatus("current")
_ApsChanEntry_Object = MibTableRow
apsChanEntry = _ApsChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1)
)
apsChanEntry.setIndexNames(
    (0, "RBN-APS-MIB", "apsChanIfIndex"),
)
if mibBuilder.loadTexts:
    apsChanEntry.setStatus("current")
_ApsChanIfIndex_Type = InterfaceIndex
_ApsChanIfIndex_Object = MibTableColumn
apsChanIfIndex = _ApsChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 1),
    _ApsChanIfIndex_Type()
)
apsChanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsChanIfIndex.setStatus("current")


class _ApsChanGroupName_Type(DisplayString):
    """Custom type apsChanGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApsChanGroupName_Type.__name__ = "DisplayString"
_ApsChanGroupName_Object = MibTableColumn
apsChanGroupName = _ApsChanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 2),
    _ApsChanGroupName_Type()
)
apsChanGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsChanGroupName.setStatus("current")


class _ApsChanNumber_Type(Integer32):
    """Custom type apsChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ApsChanNumber_Type.__name__ = "Integer32"
_ApsChanNumber_Object = MibTableColumn
apsChanNumber = _ApsChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 3),
    _ApsChanNumber_Type()
)
apsChanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsChanNumber.setStatus("current")


class _ApsChanPriority_Type(Integer32):
    """Custom type apsChanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_ApsChanPriority_Type.__name__ = "Integer32"
_ApsChanPriority_Object = MibTableColumn
apsChanPriority = _ApsChanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 4),
    _ApsChanPriority_Type()
)
apsChanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsChanPriority.setStatus("current")


class _ApsChanStatus_Type(Bits):
    """Custom type apsChanStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3))
    )

_ApsChanStatus_Type.__name__ = "Bits"
_ApsChanStatus_Object = MibTableColumn
apsChanStatus = _ApsChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 5),
    _ApsChanStatus_Type()
)
apsChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatus.setStatus("current")
_ApsChanSignalDegrades_Type = Counter32
_ApsChanSignalDegrades_Object = MibTableColumn
apsChanSignalDegrades = _ApsChanSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 6),
    _ApsChanSignalDegrades_Type()
)
apsChanSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanSignalDegrades.setStatus("current")
_ApsChanSignalFailures_Type = Counter32
_ApsChanSignalFailures_Object = MibTableColumn
apsChanSignalFailures = _ApsChanSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 7),
    _ApsChanSignalFailures_Type()
)
apsChanSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanSignalFailures.setStatus("current")
_ApsChanSwitchovers_Type = Counter32
_ApsChanSwitchovers_Object = MibTableColumn
apsChanSwitchovers = _ApsChanSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 8),
    _ApsChanSwitchovers_Type()
)
apsChanSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanSwitchovers.setStatus("current")
_ApsChanLastSwitchover_Type = TimeTicks
_ApsChanLastSwitchover_Object = MibTableColumn
apsChanLastSwitchover = _ApsChanLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 1, 4, 2, 1, 9),
    _ApsChanLastSwitchover_Type()
)
apsChanLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanLastSwitchover.setStatus("current")
_RbnApsMIBConformance_ObjectIdentity = ObjectIdentity
rbnApsMIBConformance = _RbnApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2)
)
_ApsGroups_ObjectIdentity = ObjectIdentity
apsGroups = _ApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1)
)
_ApsCompliances_ObjectIdentity = ObjectIdentity
apsCompliances = _ApsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 2)
)

# Managed Objects groups

apsConfigGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 1)
)
apsConfigGeneral.setObjects(
      *(("RBN-APS-MIB", "apsConfigMode"),
        ("RBN-APS-MIB", "apsConfigSdBerThreshold"),
        ("RBN-APS-MIB", "apsConfigSfBerThreshold"),
        ("RBN-APS-MIB", "apsConfigRowStatus"))
)
if mibBuilder.loadTexts:
    apsConfigGeneral.setStatus("current")

apsConfigOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 2)
)
apsConfigOneToN.setObjects(
    ("RBN-APS-MIB", "apsConfigWaitToRestore")
)
if mibBuilder.loadTexts:
    apsConfigOneToN.setStatus("current")

apsCommandOnePlusOne = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 3)
)
apsCommandOnePlusOne.setObjects(
    ("RBN-APS-MIB", "apsCommandSwitch")
)
if mibBuilder.loadTexts:
    apsCommandOnePlusOne.setStatus("current")

apsCommandOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 4)
)
apsCommandOneToN.setObjects(
      *(("RBN-APS-MIB", "apsCommandSwitch"),
        ("RBN-APS-MIB", "apsCommandControl"))
)
if mibBuilder.loadTexts:
    apsCommandOneToN.setStatus("current")

apsStatusGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 5)
)
apsStatusGeneral.setObjects(
      *(("RBN-APS-MIB", "apsStatusK1K2Rcv"),
        ("RBN-APS-MIB", "apsStatusK1K2Trans"),
        ("RBN-APS-MIB", "apsStatusCurrent"),
        ("RBN-APS-MIB", "apsStatusModeMismatches"),
        ("RBN-APS-MIB", "apsStatusChannelMismatches"),
        ("RBN-APS-MIB", "apsStatusPSBFs"),
        ("RBN-APS-MIB", "apsStatusCreationTime"))
)
if mibBuilder.loadTexts:
    apsStatusGeneral.setStatus("current")

apsChanGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 6)
)
apsChanGeneral.setObjects(
      *(("RBN-APS-MIB", "apsChanGroupName"),
        ("RBN-APS-MIB", "apsChanNumber"),
        ("RBN-APS-MIB", "apsChanStatus"),
        ("RBN-APS-MIB", "apsChanSignalDegrades"),
        ("RBN-APS-MIB", "apsChanSignalFailures"),
        ("RBN-APS-MIB", "apsChanSwitchovers"),
        ("RBN-APS-MIB", "apsChanLastSwitchover"))
)
if mibBuilder.loadTexts:
    apsChanGeneral.setStatus("current")

apsChanOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 7)
)
apsChanOneToN.setObjects(
    ("RBN-APS-MIB", "apsChanPriority")
)
if mibBuilder.loadTexts:
    apsChanOneToN.setStatus("current")

apsTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 8)
)
apsTotalsGroup.setObjects(
      *(("RBN-APS-MIB", "apsConfigGroups"),
        ("RBN-APS-MIB", "apsChanLTEs"))
)
if mibBuilder.loadTexts:
    apsTotalsGroup.setStatus("current")


# Notification objects

apsTrapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 1)
)
apsTrapSwitchover.setObjects(
      *(("RBN-APS-MIB", "apsChanSwitchovers"),
        ("RBN-APS-MIB", "apsChanStatus"))
)
if mibBuilder.loadTexts:
    apsTrapSwitchover.setStatus(
        "current"
    )

apsTrapModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 2)
)
apsTrapModeMismatch.setObjects(
      *(("RBN-APS-MIB", "apsStatusModeMismatches"),
        ("RBN-APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsTrapModeMismatch.setStatus(
        "current"
    )

apsTrapChannelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 3)
)
apsTrapChannelMismatch.setObjects(
      *(("RBN-APS-MIB", "apsStatusChannelMismatches"),
        ("RBN-APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsTrapChannelMismatch.setStatus(
        "current"
    )

apsTrapPSBF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 0, 4)
)
apsTrapPSBF.setObjects(
      *(("RBN-APS-MIB", "apsStatusPSBFs"),
        ("RBN-APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsTrapPSBF.setStatus(
        "current"
    )


# Notifications groups

apsTrapOptional = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 1, 9)
)
apsTrapOptional.setObjects(
      *(("RBN-APS-MIB", "apsTrapSwitchover"),
        ("RBN-APS-MIB", "apsTrapModeMismatch"),
        ("RBN-APS-MIB", "apsTrapChannelMismatch"),
        ("RBN-APS-MIB", "apsTrapPSBF"))
)
if mibBuilder.loadTexts:
    apsTrapOptional.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

apsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    apsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-APS-MIB",
    **{"ApsK1K2": ApsK1K2,
       "rbnApsMIB": rbnApsMIB,
       "rbnApsMIBNotifications": rbnApsMIBNotifications,
       "apsTrapSwitchover": apsTrapSwitchover,
       "apsTrapModeMismatch": apsTrapModeMismatch,
       "apsTrapChannelMismatch": apsTrapChannelMismatch,
       "apsTrapPSBF": apsTrapPSBF,
       "rbnApsMIBObjects": rbnApsMIBObjects,
       "apsConfig": apsConfig,
       "apsConfigGroups": apsConfigGroups,
       "apsConfigTable": apsConfigTable,
       "apsConfigEntry": apsConfigEntry,
       "apsConfigName": apsConfigName,
       "apsConfigMode": apsConfigMode,
       "apsConfigSdBerThreshold": apsConfigSdBerThreshold,
       "apsConfigSfBerThreshold": apsConfigSfBerThreshold,
       "apsConfigWaitToRestore": apsConfigWaitToRestore,
       "apsConfigRowStatus": apsConfigRowStatus,
       "apsCommandTable": apsCommandTable,
       "apsCommandEntry": apsCommandEntry,
       "apsCommandSwitch": apsCommandSwitch,
       "apsCommandControl": apsCommandControl,
       "apsStatusTable": apsStatusTable,
       "apsStatusEntry": apsStatusEntry,
       "apsStatusK1K2Rcv": apsStatusK1K2Rcv,
       "apsStatusK1K2Trans": apsStatusK1K2Trans,
       "apsStatusCurrent": apsStatusCurrent,
       "apsStatusModeMismatches": apsStatusModeMismatches,
       "apsStatusChannelMismatches": apsStatusChannelMismatches,
       "apsStatusPSBFs": apsStatusPSBFs,
       "apsStatusCreationTime": apsStatusCreationTime,
       "apsChan": apsChan,
       "apsChanLTEs": apsChanLTEs,
       "apsChanTable": apsChanTable,
       "apsChanEntry": apsChanEntry,
       "apsChanIfIndex": apsChanIfIndex,
       "apsChanGroupName": apsChanGroupName,
       "apsChanNumber": apsChanNumber,
       "apsChanPriority": apsChanPriority,
       "apsChanStatus": apsChanStatus,
       "apsChanSignalDegrades": apsChanSignalDegrades,
       "apsChanSignalFailures": apsChanSignalFailures,
       "apsChanSwitchovers": apsChanSwitchovers,
       "apsChanLastSwitchover": apsChanLastSwitchover,
       "rbnApsMIBConformance": rbnApsMIBConformance,
       "apsGroups": apsGroups,
       "apsConfigGeneral": apsConfigGeneral,
       "apsConfigOneToN": apsConfigOneToN,
       "apsCommandOnePlusOne": apsCommandOnePlusOne,
       "apsCommandOneToN": apsCommandOneToN,
       "apsStatusGeneral": apsStatusGeneral,
       "apsChanGeneral": apsChanGeneral,
       "apsChanOneToN": apsChanOneToN,
       "apsTotalsGroup": apsTotalsGroup,
       "apsTrapOptional": apsTrapOptional,
       "apsCompliances": apsCompliances,
       "apsCompliance": apsCompliance}
)
