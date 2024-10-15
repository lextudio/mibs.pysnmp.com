# SNMP MIB module (HUAWEI-DISMAN-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DISMAN-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:34 2024
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

(pingCtlEntry,
 pingCtlOwnerIndex,
 pingCtlTestName) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlEntry",
    "pingCtlOwnerIndex",
    "pingCtlTestName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "Unsigned32")


# MODULE-IDENTITY

hwDismanPing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_HwPingObjects_ObjectIdentity = ObjectIdentity
hwPingObjects = _HwPingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1)
)
_HwPingMIBVersion_Type = DisplayString
_HwPingMIBVersion_Object = MibScalar
hwPingMIBVersion = _HwPingMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 1),
    _HwPingMIBVersion_Type()
)
hwPingMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingMIBVersion.setStatus("current")
_HwPingCtlTable_Object = MibTable
hwPingCtlTable = _HwPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2)
)
if mibBuilder.loadTexts:
    hwPingCtlTable.setStatus("current")
_HwPingCtlEntry_Object = MibTableRow
hwPingCtlEntry = _HwPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwPingCtlEntry.setStatus("current")


class _HwpingCtlTargetPort_Type(Integer32):
    """Custom type hwpingCtlTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwpingCtlTargetPort_Type.__name__ = "Integer32"
_HwpingCtlTargetPort_Object = MibTableColumn
hwpingCtlTargetPort = _HwpingCtlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 1),
    _HwpingCtlTargetPort_Type()
)
hwpingCtlTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlTargetPort.setStatus("current")


class _HwpingCtlSourcePort_Type(Integer32):
    """Custom type hwpingCtlSourcePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwpingCtlSourcePort_Type.__name__ = "Integer32"
_HwpingCtlSourcePort_Object = MibTableColumn
hwpingCtlSourcePort = _HwpingCtlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 2),
    _HwpingCtlSourcePort_Type()
)
hwpingCtlSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlSourcePort.setStatus("current")


class _HwpingCtlTTL_Type(Integer32):
    """Custom type hwpingCtlTTL based on Integer32"""
    defaultValue = 20


_HwpingCtlTTL_Object = MibTableColumn
hwpingCtlTTL = _HwpingCtlTTL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 3),
    _HwpingCtlTTL_Type()
)
hwpingCtlTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlTTL.setStatus("current")


class _HwpingCtlJitterAdminInterval_Type(Integer32):
    """Custom type hwpingCtlJitterAdminInterval based on Integer32"""
    defaultValue = 20


_HwpingCtlJitterAdminInterval_Object = MibTableColumn
hwpingCtlJitterAdminInterval = _HwpingCtlJitterAdminInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 4),
    _HwpingCtlJitterAdminInterval_Type()
)
hwpingCtlJitterAdminInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlJitterAdminInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwpingCtlJitterAdminInterval.setUnits("milliseconds")


class _HwpingCtlJitterAdminNumPackets_Type(Integer32):
    """Custom type hwpingCtlJitterAdminNumPackets based on Integer32"""
    defaultValue = 10


_HwpingCtlJitterAdminNumPackets_Object = MibTableColumn
hwpingCtlJitterAdminNumPackets = _HwpingCtlJitterAdminNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 5),
    _HwpingCtlJitterAdminNumPackets_Type()
)
hwpingCtlJitterAdminNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlJitterAdminNumPackets.setStatus("current")


class _HwpingCtlHttpOperationType_Type(Integer32):
    """Custom type hwpingCtlHttpOperationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("post", 2))
    )


_HwpingCtlHttpOperationType_Type.__name__ = "Integer32"
_HwpingCtlHttpOperationType_Object = MibTableColumn
hwpingCtlHttpOperationType = _HwpingCtlHttpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 6),
    _HwpingCtlHttpOperationType_Type()
)
hwpingCtlHttpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlHttpOperationType.setStatus("current")


class _HwpingCtlHttpOperationString_Type(DisplayString):
    """Custom type hwpingCtlHttpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_HwpingCtlHttpOperationString_Type.__name__ = "DisplayString"
_HwpingCtlHttpOperationString_Object = MibTableColumn
hwpingCtlHttpOperationString = _HwpingCtlHttpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 7),
    _HwpingCtlHttpOperationString_Type()
)
hwpingCtlHttpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlHttpOperationString.setStatus("current")


class _HwpingCtlFtpOperationType_Type(Integer32):
    """Custom type hwpingCtlFtpOperationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_HwpingCtlFtpOperationType_Type.__name__ = "Integer32"
_HwpingCtlFtpOperationType_Object = MibTableColumn
hwpingCtlFtpOperationType = _HwpingCtlFtpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 8),
    _HwpingCtlFtpOperationType_Type()
)
hwpingCtlFtpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlFtpOperationType.setStatus("current")


class _HwpingCtlFtpUsername_Type(DisplayString):
    """Custom type hwpingCtlFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwpingCtlFtpUsername_Type.__name__ = "DisplayString"
_HwpingCtlFtpUsername_Object = MibTableColumn
hwpingCtlFtpUsername = _HwpingCtlFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 9),
    _HwpingCtlFtpUsername_Type()
)
hwpingCtlFtpUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlFtpUsername.setStatus("current")


class _HwpingCtlFtpPassword_Type(DisplayString):
    """Custom type hwpingCtlFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwpingCtlFtpPassword_Type.__name__ = "DisplayString"
_HwpingCtlFtpPassword_Object = MibTableColumn
hwpingCtlFtpPassword = _HwpingCtlFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 10),
    _HwpingCtlFtpPassword_Type()
)
hwpingCtlFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlFtpPassword.setStatus("current")


class _HwpingCtlFtpOperationString_Type(DisplayString):
    """Custom type hwpingCtlFtpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_HwpingCtlFtpOperationString_Type.__name__ = "DisplayString"
_HwpingCtlFtpOperationString_Object = MibTableColumn
hwpingCtlFtpOperationString = _HwpingCtlFtpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 11),
    _HwpingCtlFtpOperationString_Type()
)
hwpingCtlFtpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlFtpOperationString.setStatus("current")


class _HwpingCtlVPNInstance_Type(DisplayString):
    """Custom type hwpingCtlVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwpingCtlVPNInstance_Type.__name__ = "DisplayString"
_HwpingCtlVPNInstance_Object = MibTableColumn
hwpingCtlVPNInstance = _HwpingCtlVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 2, 1, 12),
    _HwpingCtlVPNInstance_Type()
)
hwpingCtlVPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingCtlVPNInstance.setStatus("current")
_HwpingResultsTable_Object = MibTable
hwpingResultsTable = _HwpingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3)
)
if mibBuilder.loadTexts:
    hwpingResultsTable.setStatus("current")
_HwpingResultsEntry_Object = MibTableRow
hwpingResultsEntry = _HwpingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1)
)
hwpingResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hwpingResultsEntry.setStatus("current")
_HwpingResultsRttNumDisconnects_Type = Gauge32
_HwpingResultsRttNumDisconnects_Object = MibTableColumn
hwpingResultsRttNumDisconnects = _HwpingResultsRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 1),
    _HwpingResultsRttNumDisconnects_Type()
)
hwpingResultsRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttNumDisconnects.setStatus("current")
_HwpingResultsRttTimeouts_Type = Gauge32
_HwpingResultsRttTimeouts_Object = MibTableColumn
hwpingResultsRttTimeouts = _HwpingResultsRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 2),
    _HwpingResultsRttTimeouts_Type()
)
hwpingResultsRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttTimeouts.setStatus("current")
_HwpingResultsRttBusies_Type = Gauge32
_HwpingResultsRttBusies_Object = MibTableColumn
hwpingResultsRttBusies = _HwpingResultsRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 3),
    _HwpingResultsRttBusies_Type()
)
hwpingResultsRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttBusies.setStatus("current")
_HwpingResultsRttNoConnections_Type = Gauge32
_HwpingResultsRttNoConnections_Object = MibTableColumn
hwpingResultsRttNoConnections = _HwpingResultsRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 4),
    _HwpingResultsRttNoConnections_Type()
)
hwpingResultsRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttNoConnections.setStatus("current")
_HwpingResultsRttDrops_Type = Gauge32
_HwpingResultsRttDrops_Object = MibTableColumn
hwpingResultsRttDrops = _HwpingResultsRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 5),
    _HwpingResultsRttDrops_Type()
)
hwpingResultsRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttDrops.setStatus("current")
_HwpingResultsRttSequenceErrors_Type = Gauge32
_HwpingResultsRttSequenceErrors_Object = MibTableColumn
hwpingResultsRttSequenceErrors = _HwpingResultsRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 6),
    _HwpingResultsRttSequenceErrors_Type()
)
hwpingResultsRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttSequenceErrors.setStatus("current")
_HwpingResultsRttStatsErrors_Type = Gauge32
_HwpingResultsRttStatsErrors_Object = MibTableColumn
hwpingResultsRttStatsErrors = _HwpingResultsRttStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 7),
    _HwpingResultsRttStatsErrors_Type()
)
hwpingResultsRttStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsRttStatsErrors.setStatus("current")
_HwpingResultsMaxDelaySD_Type = Gauge32
_HwpingResultsMaxDelaySD_Object = MibTableColumn
hwpingResultsMaxDelaySD = _HwpingResultsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 8),
    _HwpingResultsMaxDelaySD_Type()
)
hwpingResultsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    hwpingResultsMaxDelaySD.setUnits("milliseconds")
_HwpingResultsMaxDelayDS_Type = Gauge32
_HwpingResultsMaxDelayDS_Object = MibTableColumn
hwpingResultsMaxDelayDS = _HwpingResultsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 9),
    _HwpingResultsMaxDelayDS_Type()
)
hwpingResultsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    hwpingResultsMaxDelayDS.setUnits("milliseconds")
_HwpingResultsLostPacketRatio_Type = Gauge32
_HwpingResultsLostPacketRatio_Object = MibTableColumn
hwpingResultsLostPacketRatio = _HwpingResultsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 3, 1, 10),
    _HwpingResultsLostPacketRatio_Type()
)
hwpingResultsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwpingResultsLostPacketRatio.setStatus("current")
if mibBuilder.loadTexts:
    hwpingResultsLostPacketRatio.setUnits("milliseconds")
_HwPingJitterStatsTable_Object = MibTable
hwPingJitterStatsTable = _HwPingJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4)
)
if mibBuilder.loadTexts:
    hwPingJitterStatsTable.setStatus("current")
_HwPingJitterStatsEntry_Object = MibTableRow
hwPingJitterStatsEntry = _HwPingJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1)
)
hwPingJitterStatsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hwPingJitterStatsEntry.setStatus("current")
_HwPingJitterStatsNumOfRTT_Type = Counter32
_HwPingJitterStatsNumOfRTT_Object = MibTableColumn
hwPingJitterStatsNumOfRTT = _HwPingJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 1),
    _HwPingJitterStatsNumOfRTT_Type()
)
hwPingJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsNumOfRTT.setStatus("current")
_HwPingJitterStatsMinOfPositivesSD_Type = Gauge32
_HwPingJitterStatsMinOfPositivesSD_Object = MibTableColumn
hwPingJitterStatsMinOfPositivesSD = _HwPingJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 2),
    _HwPingJitterStatsMinOfPositivesSD_Type()
)
hwPingJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMinOfPositivesSD.setStatus("current")
_HwPingJitterStatsMaxOfPositivesSD_Type = Gauge32
_HwPingJitterStatsMaxOfPositivesSD_Object = MibTableColumn
hwPingJitterStatsMaxOfPositivesSD = _HwPingJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 3),
    _HwPingJitterStatsMaxOfPositivesSD_Type()
)
hwPingJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMaxOfPositivesSD.setStatus("current")
_HwPingJitterStatsNumOfPositivesSD_Type = Gauge32
_HwPingJitterStatsNumOfPositivesSD_Object = MibTableColumn
hwPingJitterStatsNumOfPositivesSD = _HwPingJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 4),
    _HwPingJitterStatsNumOfPositivesSD_Type()
)
hwPingJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsNumOfPositivesSD.setStatus("current")
_HwPingJitterStatsSumOfPositivesSD_Type = Gauge32
_HwPingJitterStatsSumOfPositivesSD_Object = MibTableColumn
hwPingJitterStatsSumOfPositivesSD = _HwPingJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 5),
    _HwPingJitterStatsSumOfPositivesSD_Type()
)
hwPingJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSumOfPositivesSD.setStatus("current")
_HwPingJitterStatsSum2PositivesSD_Type = Gauge32
_HwPingJitterStatsSum2PositivesSD_Object = MibTableColumn
hwPingJitterStatsSum2PositivesSD = _HwPingJitterStatsSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 6),
    _HwPingJitterStatsSum2PositivesSD_Type()
)
hwPingJitterStatsSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSum2PositivesSD.setStatus("current")
_HwPingJitterStatsMinOfNegativesSD_Type = Gauge32
_HwPingJitterStatsMinOfNegativesSD_Object = MibTableColumn
hwPingJitterStatsMinOfNegativesSD = _HwPingJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 7),
    _HwPingJitterStatsMinOfNegativesSD_Type()
)
hwPingJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMinOfNegativesSD.setStatus("current")
_HwPingJitterStatsMaxOfNegativesSD_Type = Gauge32
_HwPingJitterStatsMaxOfNegativesSD_Object = MibTableColumn
hwPingJitterStatsMaxOfNegativesSD = _HwPingJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 8),
    _HwPingJitterStatsMaxOfNegativesSD_Type()
)
hwPingJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMaxOfNegativesSD.setStatus("current")
_HwPingJitterStatsNumOfNegativesSD_Type = Gauge32
_HwPingJitterStatsNumOfNegativesSD_Object = MibTableColumn
hwPingJitterStatsNumOfNegativesSD = _HwPingJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 9),
    _HwPingJitterStatsNumOfNegativesSD_Type()
)
hwPingJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsNumOfNegativesSD.setStatus("current")
_HwPingJitterStatsSumOfNegativesSD_Type = Gauge32
_HwPingJitterStatsSumOfNegativesSD_Object = MibTableColumn
hwPingJitterStatsSumOfNegativesSD = _HwPingJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 10),
    _HwPingJitterStatsSumOfNegativesSD_Type()
)
hwPingJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSumOfNegativesSD.setStatus("current")
_HwPingJitterStatsSum2NegativesSD_Type = Gauge32
_HwPingJitterStatsSum2NegativesSD_Object = MibTableColumn
hwPingJitterStatsSum2NegativesSD = _HwPingJitterStatsSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 11),
    _HwPingJitterStatsSum2NegativesSD_Type()
)
hwPingJitterStatsSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSum2NegativesSD.setStatus("current")
_HwPingJitterStatsMinOfPositivesDS_Type = Gauge32
_HwPingJitterStatsMinOfPositivesDS_Object = MibTableColumn
hwPingJitterStatsMinOfPositivesDS = _HwPingJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 12),
    _HwPingJitterStatsMinOfPositivesDS_Type()
)
hwPingJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMinOfPositivesDS.setStatus("current")
_HwPingJitterStatsMaxOfPositivesDS_Type = Gauge32
_HwPingJitterStatsMaxOfPositivesDS_Object = MibTableColumn
hwPingJitterStatsMaxOfPositivesDS = _HwPingJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 13),
    _HwPingJitterStatsMaxOfPositivesDS_Type()
)
hwPingJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMaxOfPositivesDS.setStatus("current")
_HwPingJitterStatsNumOfPositivesDS_Type = Gauge32
_HwPingJitterStatsNumOfPositivesDS_Object = MibTableColumn
hwPingJitterStatsNumOfPositivesDS = _HwPingJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 14),
    _HwPingJitterStatsNumOfPositivesDS_Type()
)
hwPingJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsNumOfPositivesDS.setStatus("current")
_HwPingJitterStatsSumOfPositivesDS_Type = Gauge32
_HwPingJitterStatsSumOfPositivesDS_Object = MibTableColumn
hwPingJitterStatsSumOfPositivesDS = _HwPingJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 15),
    _HwPingJitterStatsSumOfPositivesDS_Type()
)
hwPingJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSumOfPositivesDS.setStatus("current")
_HwPingJitterStatsSum2PositivesDS_Type = Gauge32
_HwPingJitterStatsSum2PositivesDS_Object = MibTableColumn
hwPingJitterStatsSum2PositivesDS = _HwPingJitterStatsSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 16),
    _HwPingJitterStatsSum2PositivesDS_Type()
)
hwPingJitterStatsSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSum2PositivesDS.setStatus("current")
_HwPingJitterStatsMinOfNegativesDS_Type = Gauge32
_HwPingJitterStatsMinOfNegativesDS_Object = MibTableColumn
hwPingJitterStatsMinOfNegativesDS = _HwPingJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 17),
    _HwPingJitterStatsMinOfNegativesDS_Type()
)
hwPingJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMinOfNegativesDS.setStatus("current")
_HwPingJitterStatsMaxOfNegativesDS_Type = Gauge32
_HwPingJitterStatsMaxOfNegativesDS_Object = MibTableColumn
hwPingJitterStatsMaxOfNegativesDS = _HwPingJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 18),
    _HwPingJitterStatsMaxOfNegativesDS_Type()
)
hwPingJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsMaxOfNegativesDS.setStatus("current")
_HwPingJitterStatsNumOfNegativesDS_Type = Gauge32
_HwPingJitterStatsNumOfNegativesDS_Object = MibTableColumn
hwPingJitterStatsNumOfNegativesDS = _HwPingJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 19),
    _HwPingJitterStatsNumOfNegativesDS_Type()
)
hwPingJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsNumOfNegativesDS.setStatus("current")
_HwPingJitterStatsSumOfNegativesDS_Type = Gauge32
_HwPingJitterStatsSumOfNegativesDS_Object = MibTableColumn
hwPingJitterStatsSumOfNegativesDS = _HwPingJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 20),
    _HwPingJitterStatsSumOfNegativesDS_Type()
)
hwPingJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSumOfNegativesDS.setStatus("current")
_HwPingJitterStatsSum2NegativesDS_Type = Gauge32
_HwPingJitterStatsSum2NegativesDS_Object = MibTableColumn
hwPingJitterStatsSum2NegativesDS = _HwPingJitterStatsSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 21),
    _HwPingJitterStatsSum2NegativesDS_Type()
)
hwPingJitterStatsSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsSum2NegativesDS.setStatus("current")
_HwPingJitterStatsPacketLossSD_Type = Gauge32
_HwPingJitterStatsPacketLossSD_Object = MibTableColumn
hwPingJitterStatsPacketLossSD = _HwPingJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 22),
    _HwPingJitterStatsPacketLossSD_Type()
)
hwPingJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsPacketLossSD.setStatus("current")
_HwPingJitterStatsPacketLossDS_Type = Gauge32
_HwPingJitterStatsPacketLossDS_Object = MibTableColumn
hwPingJitterStatsPacketLossDS = _HwPingJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 23),
    _HwPingJitterStatsPacketLossDS_Type()
)
hwPingJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsPacketLossDS.setStatus("current")
_HwPingJitterStatsAvePositivesSD_Type = Gauge32
_HwPingJitterStatsAvePositivesSD_Object = MibTableColumn
hwPingJitterStatsAvePositivesSD = _HwPingJitterStatsAvePositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 24),
    _HwPingJitterStatsAvePositivesSD_Type()
)
hwPingJitterStatsAvePositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsAvePositivesSD.setStatus("current")
_HwPingJitterStatsAveNegativesSD_Type = Gauge32
_HwPingJitterStatsAveNegativesSD_Object = MibTableColumn
hwPingJitterStatsAveNegativesSD = _HwPingJitterStatsAveNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 25),
    _HwPingJitterStatsAveNegativesSD_Type()
)
hwPingJitterStatsAveNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsAveNegativesSD.setStatus("current")
_HwPingJitterStatsAvePositivesDS_Type = Gauge32
_HwPingJitterStatsAvePositivesDS_Object = MibTableColumn
hwPingJitterStatsAvePositivesDS = _HwPingJitterStatsAvePositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 26),
    _HwPingJitterStatsAvePositivesDS_Type()
)
hwPingJitterStatsAvePositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsAvePositivesDS.setStatus("current")
_HwPingJitterStatsAveNegativesDS_Type = Gauge32
_HwPingJitterStatsAveNegativesDS_Object = MibTableColumn
hwPingJitterStatsAveNegativesDS = _HwPingJitterStatsAveNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 27),
    _HwPingJitterStatsAveNegativesDS_Type()
)
hwPingJitterStatsAveNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsAveNegativesDS.setStatus("current")
_HwPingJitterStatsPktLossUnknown_Type = Gauge32
_HwPingJitterStatsPktLossUnknown_Object = MibTableColumn
hwPingJitterStatsPktLossUnknown = _HwPingJitterStatsPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 4, 1, 28),
    _HwPingJitterStatsPktLossUnknown_Type()
)
hwPingJitterStatsPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPingJitterStatsPktLossUnknown.setStatus("current")
if mibBuilder.loadTexts:
    hwPingJitterStatsPktLossUnknown.setUnits("milliseconds")


class _HwPingAgentEnable_Type(Integer32):
    """Custom type hwPingAgentEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwPingAgentEnable_Type.__name__ = "Integer32"
_HwPingAgentEnable_Object = MibScalar
hwPingAgentEnable = _HwPingAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 5),
    _HwPingAgentEnable_Type()
)
hwPingAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPingAgentEnable.setStatus("current")
_HwPingTcpServerTable_Object = MibTable
hwPingTcpServerTable = _HwPingTcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 6)
)
if mibBuilder.loadTexts:
    hwPingTcpServerTable.setStatus("current")
_HwPingTcpServerEntry_Object = MibTableRow
hwPingTcpServerEntry = _HwPingTcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 6, 1)
)
hwPingTcpServerEntry.setIndexNames(
    (0, "HUAWEI-DISMAN-PING-MIB", "hwPingTcpServerIpAddress"),
    (0, "HUAWEI-DISMAN-PING-MIB", "hwPingTcpServerPort"),
    (0, "HUAWEI-DISMAN-PING-MIB", "hwpingTcpServerVPNInstance"),
)
if mibBuilder.loadTexts:
    hwPingTcpServerEntry.setStatus("current")


class _HwPingTcpServerIpAddress_Type(InetAddress):
    """Custom type hwPingTcpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_HwPingTcpServerIpAddress_Object = MibTableColumn
hwPingTcpServerIpAddress = _HwPingTcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 6, 1, 1),
    _HwPingTcpServerIpAddress_Type()
)
hwPingTcpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPingTcpServerIpAddress.setStatus("current")


class _HwPingTcpServerPort_Type(Integer32):
    """Custom type hwPingTcpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPingTcpServerPort_Type.__name__ = "Integer32"
_HwPingTcpServerPort_Object = MibTableColumn
hwPingTcpServerPort = _HwPingTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 6, 1, 2),
    _HwPingTcpServerPort_Type()
)
hwPingTcpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPingTcpServerPort.setStatus("current")


class _HwpingTcpServerVPNInstance_Type(DisplayString):
    """Custom type hwpingTcpServerVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwpingTcpServerVPNInstance_Type.__name__ = "DisplayString"
_HwpingTcpServerVPNInstance_Object = MibTableColumn
hwpingTcpServerVPNInstance = _HwpingTcpServerVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 6, 1, 3),
    _HwpingTcpServerVPNInstance_Type()
)
hwpingTcpServerVPNInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwpingTcpServerVPNInstance.setStatus("current")
_HwpingTcpServerRowStatus_Type = RowStatus
_HwpingTcpServerRowStatus_Object = MibTableColumn
hwpingTcpServerRowStatus = _HwpingTcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 6, 1, 4),
    _HwpingTcpServerRowStatus_Type()
)
hwpingTcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingTcpServerRowStatus.setStatus("current")
_HwPingUdpServerTable_Object = MibTable
hwPingUdpServerTable = _HwPingUdpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 7)
)
if mibBuilder.loadTexts:
    hwPingUdpServerTable.setStatus("current")
_HwPingUdpServerEntry_Object = MibTableRow
hwPingUdpServerEntry = _HwPingUdpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 7, 1)
)
hwPingUdpServerEntry.setIndexNames(
    (0, "HUAWEI-DISMAN-PING-MIB", "hwPingUdpServerIpAddress"),
    (0, "HUAWEI-DISMAN-PING-MIB", "hwPingUdpServerPort"),
    (0, "HUAWEI-DISMAN-PING-MIB", "hwpingUdpServerVPNInstance"),
)
if mibBuilder.loadTexts:
    hwPingUdpServerEntry.setStatus("current")


class _HwPingUdpServerIpAddress_Type(InetAddress):
    """Custom type hwPingUdpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_HwPingUdpServerIpAddress_Object = MibTableColumn
hwPingUdpServerIpAddress = _HwPingUdpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 7, 1, 1),
    _HwPingUdpServerIpAddress_Type()
)
hwPingUdpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPingUdpServerIpAddress.setStatus("current")


class _HwPingUdpServerPort_Type(Integer32):
    """Custom type hwPingUdpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPingUdpServerPort_Type.__name__ = "Integer32"
_HwPingUdpServerPort_Object = MibTableColumn
hwPingUdpServerPort = _HwPingUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 7, 1, 2),
    _HwPingUdpServerPort_Type()
)
hwPingUdpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPingUdpServerPort.setStatus("current")


class _HwpingUdpServerVPNInstance_Type(DisplayString):
    """Custom type hwpingUdpServerVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwpingUdpServerVPNInstance_Type.__name__ = "DisplayString"
_HwpingUdpServerVPNInstance_Object = MibTableColumn
hwpingUdpServerVPNInstance = _HwpingUdpServerVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 7, 1, 3),
    _HwpingUdpServerVPNInstance_Type()
)
hwpingUdpServerVPNInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwpingUdpServerVPNInstance.setStatus("current")
_HwpingUdpServerRowStatus_Type = RowStatus
_HwpingUdpServerRowStatus_Object = MibTableColumn
hwpingUdpServerRowStatus = _HwpingUdpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 7, 1, 4),
    _HwpingUdpServerRowStatus_Type()
)
hwpingUdpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwpingUdpServerRowStatus.setStatus("current")


class _HwPingServerEnable_Type(Integer32):
    """Custom type hwPingServerEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwPingServerEnable_Type.__name__ = "Integer32"
_HwPingServerEnable_Object = MibScalar
hwPingServerEnable = _HwPingServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 1, 8),
    _HwPingServerEnable_Type()
)
hwPingServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPingServerEnable.setStatus("current")
_HwPingImplementationTypeDomains_ObjectIdentity = ObjectIdentity
hwPingImplementationTypeDomains = _HwPingImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2)
)
_HwpingUdpEcho_ObjectIdentity = ObjectIdentity
hwpingUdpEcho = _HwpingUdpEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 1)
)
if mibBuilder.loadTexts:
    hwpingUdpEcho.setStatus("current")
_HwpingTcpconnect_ObjectIdentity = ObjectIdentity
hwpingTcpconnect = _HwpingTcpconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 2)
)
if mibBuilder.loadTexts:
    hwpingTcpconnect.setStatus("current")
_Hwpingjitter_ObjectIdentity = ObjectIdentity
hwpingjitter = _Hwpingjitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 3)
)
if mibBuilder.loadTexts:
    hwpingjitter.setStatus("current")
_HwpingHttp_ObjectIdentity = ObjectIdentity
hwpingHttp = _HwpingHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 4)
)
if mibBuilder.loadTexts:
    hwpingHttp.setStatus("current")
_Hwpingdlsw_ObjectIdentity = ObjectIdentity
hwpingdlsw = _Hwpingdlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 5)
)
if mibBuilder.loadTexts:
    hwpingdlsw.setStatus("current")
_Hwpingdhcp_ObjectIdentity = ObjectIdentity
hwpingdhcp = _Hwpingdhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 6)
)
if mibBuilder.loadTexts:
    hwpingdhcp.setStatus("current")
_Hwpingftp_ObjectIdentity = ObjectIdentity
hwpingftp = _Hwpingftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 28, 2, 7)
)
if mibBuilder.loadTexts:
    hwpingftp.setStatus("current")
pingCtlEntry.registerAugmentions(
    ("HUAWEI-DISMAN-PING-MIB",
     "hwPingCtlEntry")
)
hwPingCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DISMAN-PING-MIB",
    **{"InetAddress": InetAddress,
       "hwDismanPing": hwDismanPing,
       "hwPingObjects": hwPingObjects,
       "hwPingMIBVersion": hwPingMIBVersion,
       "hwPingCtlTable": hwPingCtlTable,
       "hwPingCtlEntry": hwPingCtlEntry,
       "hwpingCtlTargetPort": hwpingCtlTargetPort,
       "hwpingCtlSourcePort": hwpingCtlSourcePort,
       "hwpingCtlTTL": hwpingCtlTTL,
       "hwpingCtlJitterAdminInterval": hwpingCtlJitterAdminInterval,
       "hwpingCtlJitterAdminNumPackets": hwpingCtlJitterAdminNumPackets,
       "hwpingCtlHttpOperationType": hwpingCtlHttpOperationType,
       "hwpingCtlHttpOperationString": hwpingCtlHttpOperationString,
       "hwpingCtlFtpOperationType": hwpingCtlFtpOperationType,
       "hwpingCtlFtpUsername": hwpingCtlFtpUsername,
       "hwpingCtlFtpPassword": hwpingCtlFtpPassword,
       "hwpingCtlFtpOperationString": hwpingCtlFtpOperationString,
       "hwpingCtlVPNInstance": hwpingCtlVPNInstance,
       "hwpingResultsTable": hwpingResultsTable,
       "hwpingResultsEntry": hwpingResultsEntry,
       "hwpingResultsRttNumDisconnects": hwpingResultsRttNumDisconnects,
       "hwpingResultsRttTimeouts": hwpingResultsRttTimeouts,
       "hwpingResultsRttBusies": hwpingResultsRttBusies,
       "hwpingResultsRttNoConnections": hwpingResultsRttNoConnections,
       "hwpingResultsRttDrops": hwpingResultsRttDrops,
       "hwpingResultsRttSequenceErrors": hwpingResultsRttSequenceErrors,
       "hwpingResultsRttStatsErrors": hwpingResultsRttStatsErrors,
       "hwpingResultsMaxDelaySD": hwpingResultsMaxDelaySD,
       "hwpingResultsMaxDelayDS": hwpingResultsMaxDelayDS,
       "hwpingResultsLostPacketRatio": hwpingResultsLostPacketRatio,
       "hwPingJitterStatsTable": hwPingJitterStatsTable,
       "hwPingJitterStatsEntry": hwPingJitterStatsEntry,
       "hwPingJitterStatsNumOfRTT": hwPingJitterStatsNumOfRTT,
       "hwPingJitterStatsMinOfPositivesSD": hwPingJitterStatsMinOfPositivesSD,
       "hwPingJitterStatsMaxOfPositivesSD": hwPingJitterStatsMaxOfPositivesSD,
       "hwPingJitterStatsNumOfPositivesSD": hwPingJitterStatsNumOfPositivesSD,
       "hwPingJitterStatsSumOfPositivesSD": hwPingJitterStatsSumOfPositivesSD,
       "hwPingJitterStatsSum2PositivesSD": hwPingJitterStatsSum2PositivesSD,
       "hwPingJitterStatsMinOfNegativesSD": hwPingJitterStatsMinOfNegativesSD,
       "hwPingJitterStatsMaxOfNegativesSD": hwPingJitterStatsMaxOfNegativesSD,
       "hwPingJitterStatsNumOfNegativesSD": hwPingJitterStatsNumOfNegativesSD,
       "hwPingJitterStatsSumOfNegativesSD": hwPingJitterStatsSumOfNegativesSD,
       "hwPingJitterStatsSum2NegativesSD": hwPingJitterStatsSum2NegativesSD,
       "hwPingJitterStatsMinOfPositivesDS": hwPingJitterStatsMinOfPositivesDS,
       "hwPingJitterStatsMaxOfPositivesDS": hwPingJitterStatsMaxOfPositivesDS,
       "hwPingJitterStatsNumOfPositivesDS": hwPingJitterStatsNumOfPositivesDS,
       "hwPingJitterStatsSumOfPositivesDS": hwPingJitterStatsSumOfPositivesDS,
       "hwPingJitterStatsSum2PositivesDS": hwPingJitterStatsSum2PositivesDS,
       "hwPingJitterStatsMinOfNegativesDS": hwPingJitterStatsMinOfNegativesDS,
       "hwPingJitterStatsMaxOfNegativesDS": hwPingJitterStatsMaxOfNegativesDS,
       "hwPingJitterStatsNumOfNegativesDS": hwPingJitterStatsNumOfNegativesDS,
       "hwPingJitterStatsSumOfNegativesDS": hwPingJitterStatsSumOfNegativesDS,
       "hwPingJitterStatsSum2NegativesDS": hwPingJitterStatsSum2NegativesDS,
       "hwPingJitterStatsPacketLossSD": hwPingJitterStatsPacketLossSD,
       "hwPingJitterStatsPacketLossDS": hwPingJitterStatsPacketLossDS,
       "hwPingJitterStatsAvePositivesSD": hwPingJitterStatsAvePositivesSD,
       "hwPingJitterStatsAveNegativesSD": hwPingJitterStatsAveNegativesSD,
       "hwPingJitterStatsAvePositivesDS": hwPingJitterStatsAvePositivesDS,
       "hwPingJitterStatsAveNegativesDS": hwPingJitterStatsAveNegativesDS,
       "hwPingJitterStatsPktLossUnknown": hwPingJitterStatsPktLossUnknown,
       "hwPingAgentEnable": hwPingAgentEnable,
       "hwPingTcpServerTable": hwPingTcpServerTable,
       "hwPingTcpServerEntry": hwPingTcpServerEntry,
       "hwPingTcpServerIpAddress": hwPingTcpServerIpAddress,
       "hwPingTcpServerPort": hwPingTcpServerPort,
       "hwpingTcpServerVPNInstance": hwpingTcpServerVPNInstance,
       "hwpingTcpServerRowStatus": hwpingTcpServerRowStatus,
       "hwPingUdpServerTable": hwPingUdpServerTable,
       "hwPingUdpServerEntry": hwPingUdpServerEntry,
       "hwPingUdpServerIpAddress": hwPingUdpServerIpAddress,
       "hwPingUdpServerPort": hwPingUdpServerPort,
       "hwpingUdpServerVPNInstance": hwpingUdpServerVPNInstance,
       "hwpingUdpServerRowStatus": hwpingUdpServerRowStatus,
       "hwPingServerEnable": hwPingServerEnable,
       "hwPingImplementationTypeDomains": hwPingImplementationTypeDomains,
       "hwpingUdpEcho": hwpingUdpEcho,
       "hwpingTcpconnect": hwpingTcpconnect,
       "hwpingjitter": hwpingjitter,
       "hwpingHttp": hwpingHttp,
       "hwpingdlsw": hwpingdlsw,
       "hwpingdhcp": hwpingdhcp,
       "hwpingftp": hwpingftp}
)
