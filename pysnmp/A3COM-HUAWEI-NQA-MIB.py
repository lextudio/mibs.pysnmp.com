# SNMP MIB module (A3COM-HUAWEI-NQA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-NQA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:43 2024
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

(huaweiDatacomm,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiDatacomm")

(pingCtlDescr,
 pingCtlEntry,
 pingCtlOwnerIndex,
 pingCtlTargetAddress,
 pingCtlTargetAddressType,
 pingCtlTestName,
 pingCtlType) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlDescr",
    "pingCtlEntry",
    "pingCtlOwnerIndex",
    "pingCtlTargetAddress",
    "pingCtlTargetAddressType",
    "pingCtlTestName",
    "pingCtlType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwNqa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwNqaObjects_ObjectIdentity = ObjectIdentity
hwNqaObjects = _HwNqaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1)
)
_HwNqaMIBVersion_Type = DisplayString
_HwNqaMIBVersion_Object = MibScalar
hwNqaMIBVersion = _HwNqaMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 1),
    _HwNqaMIBVersion_Type()
)
hwNqaMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaMIBVersion.setStatus("current")
_HwNqaCtlTable_Object = MibTable
hwNqaCtlTable = _HwNqaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2)
)
if mibBuilder.loadTexts:
    hwNqaCtlTable.setStatus("current")
_HwNqaCtlEntry_Object = MibTableRow
hwNqaCtlEntry = _HwNqaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwNqaCtlEntry.setStatus("current")


class _HwNqaCtlTargetPort_Type(Integer32):
    """Custom type hwNqaCtlTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwNqaCtlTargetPort_Type.__name__ = "Integer32"
_HwNqaCtlTargetPort_Object = MibTableColumn
hwNqaCtlTargetPort = _HwNqaCtlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 1),
    _HwNqaCtlTargetPort_Type()
)
hwNqaCtlTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlTargetPort.setStatus("current")


class _HwNqaCtlSourcePort_Type(Integer32):
    """Custom type hwNqaCtlSourcePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwNqaCtlSourcePort_Type.__name__ = "Integer32"
_HwNqaCtlSourcePort_Object = MibTableColumn
hwNqaCtlSourcePort = _HwNqaCtlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 2),
    _HwNqaCtlSourcePort_Type()
)
hwNqaCtlSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlSourcePort.setStatus("current")


class _HwNqaCtlTTL_Type(Integer32):
    """Custom type hwNqaCtlTTL based on Integer32"""
    defaultValue = 20


_HwNqaCtlTTL_Object = MibTableColumn
hwNqaCtlTTL = _HwNqaCtlTTL_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 3),
    _HwNqaCtlTTL_Type()
)
hwNqaCtlTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlTTL.setStatus("current")


class _HwNqaCtlJitterAdminInterval_Type(Integer32):
    """Custom type hwNqaCtlJitterAdminInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwNqaCtlJitterAdminInterval_Type.__name__ = "Integer32"
_HwNqaCtlJitterAdminInterval_Object = MibTableColumn
hwNqaCtlJitterAdminInterval = _HwNqaCtlJitterAdminInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 4),
    _HwNqaCtlJitterAdminInterval_Type()
)
hwNqaCtlJitterAdminInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlJitterAdminInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaCtlJitterAdminInterval.setUnits("milliseconds")


class _HwNqaCtlJitterAdminNumPackets_Type(Integer32):
    """Custom type hwNqaCtlJitterAdminNumPackets based on Integer32"""
    defaultValue = 10


_HwNqaCtlJitterAdminNumPackets_Object = MibTableColumn
hwNqaCtlJitterAdminNumPackets = _HwNqaCtlJitterAdminNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 5),
    _HwNqaCtlJitterAdminNumPackets_Type()
)
hwNqaCtlJitterAdminNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlJitterAdminNumPackets.setStatus("current")


class _HwNqaCtlHttpOperationType_Type(Integer32):
    """Custom type hwNqaCtlHttpOperationType based on Integer32"""
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


_HwNqaCtlHttpOperationType_Type.__name__ = "Integer32"
_HwNqaCtlHttpOperationType_Object = MibTableColumn
hwNqaCtlHttpOperationType = _HwNqaCtlHttpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 6),
    _HwNqaCtlHttpOperationType_Type()
)
hwNqaCtlHttpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlHttpOperationType.setStatus("current")


class _HwNqaCtlHttpOperationString_Type(DisplayString):
    """Custom type hwNqaCtlHttpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNqaCtlHttpOperationString_Type.__name__ = "DisplayString"
_HwNqaCtlHttpOperationString_Object = MibTableColumn
hwNqaCtlHttpOperationString = _HwNqaCtlHttpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 7),
    _HwNqaCtlHttpOperationString_Type()
)
hwNqaCtlHttpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlHttpOperationString.setStatus("current")


class _HwNqaCtlFtpOperationType_Type(Integer32):
    """Custom type hwNqaCtlFtpOperationType based on Integer32"""
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


_HwNqaCtlFtpOperationType_Type.__name__ = "Integer32"
_HwNqaCtlFtpOperationType_Object = MibTableColumn
hwNqaCtlFtpOperationType = _HwNqaCtlFtpOperationType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 8),
    _HwNqaCtlFtpOperationType_Type()
)
hwNqaCtlFtpOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlFtpOperationType.setStatus("current")


class _HwNqaCtlFtpUsername_Type(DisplayString):
    """Custom type hwNqaCtlFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNqaCtlFtpUsername_Type.__name__ = "DisplayString"
_HwNqaCtlFtpUsername_Object = MibTableColumn
hwNqaCtlFtpUsername = _HwNqaCtlFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 9),
    _HwNqaCtlFtpUsername_Type()
)
hwNqaCtlFtpUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlFtpUsername.setStatus("current")


class _HwNqaCtlFtpPassword_Type(DisplayString):
    """Custom type hwNqaCtlFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNqaCtlFtpPassword_Type.__name__ = "DisplayString"
_HwNqaCtlFtpPassword_Object = MibTableColumn
hwNqaCtlFtpPassword = _HwNqaCtlFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 10),
    _HwNqaCtlFtpPassword_Type()
)
hwNqaCtlFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlFtpPassword.setStatus("current")


class _HwNqaCtlFtpOperationString_Type(DisplayString):
    """Custom type hwNqaCtlFtpOperationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNqaCtlFtpOperationString_Type.__name__ = "DisplayString"
_HwNqaCtlFtpOperationString_Object = MibTableColumn
hwNqaCtlFtpOperationString = _HwNqaCtlFtpOperationString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 11),
    _HwNqaCtlFtpOperationString_Type()
)
hwNqaCtlFtpOperationString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlFtpOperationString.setStatus("current")


class _HwNqaCtlVPNInstance_Type(DisplayString):
    """Custom type hwNqaCtlVPNInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNqaCtlVPNInstance_Type.__name__ = "DisplayString"
_HwNqaCtlVPNInstance_Object = MibTableColumn
hwNqaCtlVPNInstance = _HwNqaCtlVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 12),
    _HwNqaCtlVPNInstance_Type()
)
hwNqaCtlVPNInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlVPNInstance.setStatus("current")


class _HwNqaCtlHistoryKeptTime_Type(Integer32):
    """Custom type hwNqaCtlHistoryKeptTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_HwNqaCtlHistoryKeptTime_Type.__name__ = "Integer32"
_HwNqaCtlHistoryKeptTime_Object = MibTableColumn
hwNqaCtlHistoryKeptTime = _HwNqaCtlHistoryKeptTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 13),
    _HwNqaCtlHistoryKeptTime_Type()
)
hwNqaCtlHistoryKeptTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlHistoryKeptTime.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaCtlHistoryKeptTime.setUnits("minutes")


class _HwNqaCtlHistoryEnable_Type(Integer32):
    """Custom type hwNqaCtlHistoryEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwNqaCtlHistoryEnable_Type.__name__ = "Integer32"
_HwNqaCtlHistoryEnable_Object = MibTableColumn
hwNqaCtlHistoryEnable = _HwNqaCtlHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 14),
    _HwNqaCtlHistoryEnable_Type()
)
hwNqaCtlHistoryEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlHistoryEnable.setStatus("current")


class _HwNqaCtlICPIFAdvFactor_Type(Integer32):
    """Custom type hwNqaCtlICPIFAdvFactor based on Integer32"""
    defaultValue = 0


_HwNqaCtlICPIFAdvFactor_Object = MibTableColumn
hwNqaCtlICPIFAdvFactor = _HwNqaCtlICPIFAdvFactor_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 15),
    _HwNqaCtlICPIFAdvFactor_Type()
)
hwNqaCtlICPIFAdvFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlICPIFAdvFactor.setStatus("current")


class _HwNqaCtlCodecType_Type(Integer32):
    """Custom type hwNqaCtlCodecType based on Integer32"""
    defaultValue = 1

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
        *(("g711Alaw", 2),
          ("g711Ulaw", 3),
          ("g729A", 4),
          ("icmpTimestamp", 5),
          ("notDefined", 1))
    )


_HwNqaCtlCodecType_Type.__name__ = "Integer32"
_HwNqaCtlCodecType_Object = MibTableColumn
hwNqaCtlCodecType = _HwNqaCtlCodecType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 2, 1, 16),
    _HwNqaCtlCodecType_Type()
)
hwNqaCtlCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlCodecType.setStatus("current")
_HwNqaResultsTable_Object = MibTable
hwNqaResultsTable = _HwNqaResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3)
)
if mibBuilder.loadTexts:
    hwNqaResultsTable.setStatus("current")
_HwNqaResultsEntry_Object = MibTableRow
hwNqaResultsEntry = _HwNqaResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1)
)
hwNqaResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hwNqaResultsEntry.setStatus("current")
_HwNqaResultsRttNumDisconnects_Type = Unsigned32
_HwNqaResultsRttNumDisconnects_Object = MibTableColumn
hwNqaResultsRttNumDisconnects = _HwNqaResultsRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 1),
    _HwNqaResultsRttNumDisconnects_Type()
)
hwNqaResultsRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttNumDisconnects.setStatus("current")
_HwNqaResultsRttTimeouts_Type = Unsigned32
_HwNqaResultsRttTimeouts_Object = MibTableColumn
hwNqaResultsRttTimeouts = _HwNqaResultsRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 2),
    _HwNqaResultsRttTimeouts_Type()
)
hwNqaResultsRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttTimeouts.setStatus("current")
_HwNqaResultsRttBusies_Type = Unsigned32
_HwNqaResultsRttBusies_Object = MibTableColumn
hwNqaResultsRttBusies = _HwNqaResultsRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 3),
    _HwNqaResultsRttBusies_Type()
)
hwNqaResultsRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttBusies.setStatus("current")
_HwNqaResultsRttNoConnections_Type = Unsigned32
_HwNqaResultsRttNoConnections_Object = MibTableColumn
hwNqaResultsRttNoConnections = _HwNqaResultsRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 4),
    _HwNqaResultsRttNoConnections_Type()
)
hwNqaResultsRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttNoConnections.setStatus("current")
_HwNqaResultsRttDrops_Type = Unsigned32
_HwNqaResultsRttDrops_Object = MibTableColumn
hwNqaResultsRttDrops = _HwNqaResultsRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 5),
    _HwNqaResultsRttDrops_Type()
)
hwNqaResultsRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttDrops.setStatus("current")
_HwNqaResultsRttSequenceErrors_Type = Unsigned32
_HwNqaResultsRttSequenceErrors_Object = MibTableColumn
hwNqaResultsRttSequenceErrors = _HwNqaResultsRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 6),
    _HwNqaResultsRttSequenceErrors_Type()
)
hwNqaResultsRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttSequenceErrors.setStatus("current")
_HwNqaResultsRttStatsErrors_Type = Unsigned32
_HwNqaResultsRttStatsErrors_Object = MibTableColumn
hwNqaResultsRttStatsErrors = _HwNqaResultsRttStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 7),
    _HwNqaResultsRttStatsErrors_Type()
)
hwNqaResultsRttStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttStatsErrors.setStatus("current")
_HwNqaResultsMaxDelaySD_Type = Unsigned32
_HwNqaResultsMaxDelaySD_Object = MibTableColumn
hwNqaResultsMaxDelaySD = _HwNqaResultsMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 8),
    _HwNqaResultsMaxDelaySD_Type()
)
hwNqaResultsMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsMaxDelaySD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaResultsMaxDelaySD.setUnits("milliseconds")
_HwNqaResultsMaxDelayDS_Type = Unsigned32
_HwNqaResultsMaxDelayDS_Object = MibTableColumn
hwNqaResultsMaxDelayDS = _HwNqaResultsMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 9),
    _HwNqaResultsMaxDelayDS_Type()
)
hwNqaResultsMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsMaxDelayDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaResultsMaxDelayDS.setUnits("milliseconds")
_HwNqaResultsLostPacketRatio_Type = Unsigned32
_HwNqaResultsLostPacketRatio_Object = MibTableColumn
hwNqaResultsLostPacketRatio = _HwNqaResultsLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 10),
    _HwNqaResultsLostPacketRatio_Type()
)
hwNqaResultsLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsLostPacketRatio.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaResultsLostPacketRatio.setUnits("milliseconds")
_HwNqaResultsPacketLateArrival_Type = Unsigned32
_HwNqaResultsPacketLateArrival_Object = MibTableColumn
hwNqaResultsPacketLateArrival = _HwNqaResultsPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 11),
    _HwNqaResultsPacketLateArrival_Type()
)
hwNqaResultsPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsPacketLateArrival.setStatus("current")
_HwNqaResultsRttSum_Type = Unsigned32
_HwNqaResultsRttSum_Object = MibTableColumn
hwNqaResultsRttSum = _HwNqaResultsRttSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 12),
    _HwNqaResultsRttSum_Type()
)
hwNqaResultsRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsRttSum.setStatus("current")
_HwNqaResultsNumOfDelaySD_Type = Unsigned32
_HwNqaResultsNumOfDelaySD_Object = MibTableColumn
hwNqaResultsNumOfDelaySD = _HwNqaResultsNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 13),
    _HwNqaResultsNumOfDelaySD_Type()
)
hwNqaResultsNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsNumOfDelaySD.setStatus("current")
_HwNqaResultsMinDelaySD_Type = Unsigned32
_HwNqaResultsMinDelaySD_Object = MibTableColumn
hwNqaResultsMinDelaySD = _HwNqaResultsMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 14),
    _HwNqaResultsMinDelaySD_Type()
)
hwNqaResultsMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsMinDelaySD.setStatus("current")
_HwNqaResultsSumDelaySD_Type = Unsigned32
_HwNqaResultsSumDelaySD_Object = MibTableColumn
hwNqaResultsSumDelaySD = _HwNqaResultsSumDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 15),
    _HwNqaResultsSumDelaySD_Type()
)
hwNqaResultsSumDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsSumDelaySD.setStatus("current")
_HwNqaResultsSum2DelaySD_Type = Unsigned32
_HwNqaResultsSum2DelaySD_Object = MibTableColumn
hwNqaResultsSum2DelaySD = _HwNqaResultsSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 16),
    _HwNqaResultsSum2DelaySD_Type()
)
hwNqaResultsSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsSum2DelaySD.setStatus("current")
_HwNqaResultsNumOfDelayDS_Type = Unsigned32
_HwNqaResultsNumOfDelayDS_Object = MibTableColumn
hwNqaResultsNumOfDelayDS = _HwNqaResultsNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 17),
    _HwNqaResultsNumOfDelayDS_Type()
)
hwNqaResultsNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsNumOfDelayDS.setStatus("current")
_HwNqaResultsMinDelayDS_Type = Unsigned32
_HwNqaResultsMinDelayDS_Object = MibTableColumn
hwNqaResultsMinDelayDS = _HwNqaResultsMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 18),
    _HwNqaResultsMinDelayDS_Type()
)
hwNqaResultsMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsMinDelayDS.setStatus("current")
_HwNqaResultsSumDelayDS_Type = Unsigned32
_HwNqaResultsSumDelayDS_Object = MibTableColumn
hwNqaResultsSumDelayDS = _HwNqaResultsSumDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 19),
    _HwNqaResultsSumDelayDS_Type()
)
hwNqaResultsSumDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsSumDelayDS.setStatus("current")
_HwNqaResultsSum2DelayDS_Type = Unsigned32
_HwNqaResultsSum2DelayDS_Object = MibTableColumn
hwNqaResultsSum2DelayDS = _HwNqaResultsSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 3, 1, 20),
    _HwNqaResultsSum2DelayDS_Type()
)
hwNqaResultsSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaResultsSum2DelayDS.setStatus("current")
_HwNqaJitterStatsTable_Object = MibTable
hwNqaJitterStatsTable = _HwNqaJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4)
)
if mibBuilder.loadTexts:
    hwNqaJitterStatsTable.setStatus("current")
_HwNqaJitterStatsEntry_Object = MibTableRow
hwNqaJitterStatsEntry = _HwNqaJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1)
)
hwNqaJitterStatsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    hwNqaJitterStatsEntry.setStatus("current")
_HwNqaJitterStatsNumOfRTT_Type = Counter32
_HwNqaJitterStatsNumOfRTT_Object = MibTableColumn
hwNqaJitterStatsNumOfRTT = _HwNqaJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 1),
    _HwNqaJitterStatsNumOfRTT_Type()
)
hwNqaJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsNumOfRTT.setStatus("current")
_HwNqaJitterStatsMinOfPositivesSD_Type = Gauge32
_HwNqaJitterStatsMinOfPositivesSD_Object = MibTableColumn
hwNqaJitterStatsMinOfPositivesSD = _HwNqaJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 2),
    _HwNqaJitterStatsMinOfPositivesSD_Type()
)
hwNqaJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMinOfPositivesSD.setStatus("current")
_HwNqaJitterStatsMaxOfPositivesSD_Type = Gauge32
_HwNqaJitterStatsMaxOfPositivesSD_Object = MibTableColumn
hwNqaJitterStatsMaxOfPositivesSD = _HwNqaJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 3),
    _HwNqaJitterStatsMaxOfPositivesSD_Type()
)
hwNqaJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMaxOfPositivesSD.setStatus("current")
_HwNqaJitterStatsNumOfPositivesSD_Type = Gauge32
_HwNqaJitterStatsNumOfPositivesSD_Object = MibTableColumn
hwNqaJitterStatsNumOfPositivesSD = _HwNqaJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 4),
    _HwNqaJitterStatsNumOfPositivesSD_Type()
)
hwNqaJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsNumOfPositivesSD.setStatus("current")
_HwNqaJitterStatsSumOfPositivesSD_Type = Gauge32
_HwNqaJitterStatsSumOfPositivesSD_Object = MibTableColumn
hwNqaJitterStatsSumOfPositivesSD = _HwNqaJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 5),
    _HwNqaJitterStatsSumOfPositivesSD_Type()
)
hwNqaJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSumOfPositivesSD.setStatus("current")
_HwNqaJitterStatsSum2PositivesSD_Type = Gauge32
_HwNqaJitterStatsSum2PositivesSD_Object = MibTableColumn
hwNqaJitterStatsSum2PositivesSD = _HwNqaJitterStatsSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 6),
    _HwNqaJitterStatsSum2PositivesSD_Type()
)
hwNqaJitterStatsSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSum2PositivesSD.setStatus("current")
_HwNqaJitterStatsMinOfNegativesSD_Type = Gauge32
_HwNqaJitterStatsMinOfNegativesSD_Object = MibTableColumn
hwNqaJitterStatsMinOfNegativesSD = _HwNqaJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 7),
    _HwNqaJitterStatsMinOfNegativesSD_Type()
)
hwNqaJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMinOfNegativesSD.setStatus("current")
_HwNqaJitterStatsMaxOfNegativesSD_Type = Gauge32
_HwNqaJitterStatsMaxOfNegativesSD_Object = MibTableColumn
hwNqaJitterStatsMaxOfNegativesSD = _HwNqaJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 8),
    _HwNqaJitterStatsMaxOfNegativesSD_Type()
)
hwNqaJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMaxOfNegativesSD.setStatus("current")
_HwNqaJitterStatsNumOfNegativesSD_Type = Gauge32
_HwNqaJitterStatsNumOfNegativesSD_Object = MibTableColumn
hwNqaJitterStatsNumOfNegativesSD = _HwNqaJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 9),
    _HwNqaJitterStatsNumOfNegativesSD_Type()
)
hwNqaJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsNumOfNegativesSD.setStatus("current")
_HwNqaJitterStatsSumOfNegativesSD_Type = Gauge32
_HwNqaJitterStatsSumOfNegativesSD_Object = MibTableColumn
hwNqaJitterStatsSumOfNegativesSD = _HwNqaJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 10),
    _HwNqaJitterStatsSumOfNegativesSD_Type()
)
hwNqaJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSumOfNegativesSD.setStatus("current")
_HwNqaJitterStatsSum2NegativesSD_Type = Gauge32
_HwNqaJitterStatsSum2NegativesSD_Object = MibTableColumn
hwNqaJitterStatsSum2NegativesSD = _HwNqaJitterStatsSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 11),
    _HwNqaJitterStatsSum2NegativesSD_Type()
)
hwNqaJitterStatsSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSum2NegativesSD.setStatus("current")
_HwNqaJitterStatsMinOfPositivesDS_Type = Gauge32
_HwNqaJitterStatsMinOfPositivesDS_Object = MibTableColumn
hwNqaJitterStatsMinOfPositivesDS = _HwNqaJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 12),
    _HwNqaJitterStatsMinOfPositivesDS_Type()
)
hwNqaJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMinOfPositivesDS.setStatus("current")
_HwNqaJitterStatsMaxOfPositivesDS_Type = Gauge32
_HwNqaJitterStatsMaxOfPositivesDS_Object = MibTableColumn
hwNqaJitterStatsMaxOfPositivesDS = _HwNqaJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 13),
    _HwNqaJitterStatsMaxOfPositivesDS_Type()
)
hwNqaJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMaxOfPositivesDS.setStatus("current")
_HwNqaJitterStatsNumOfPositivesDS_Type = Gauge32
_HwNqaJitterStatsNumOfPositivesDS_Object = MibTableColumn
hwNqaJitterStatsNumOfPositivesDS = _HwNqaJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 14),
    _HwNqaJitterStatsNumOfPositivesDS_Type()
)
hwNqaJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsNumOfPositivesDS.setStatus("current")
_HwNqaJitterStatsSumOfPositivesDS_Type = Gauge32
_HwNqaJitterStatsSumOfPositivesDS_Object = MibTableColumn
hwNqaJitterStatsSumOfPositivesDS = _HwNqaJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 15),
    _HwNqaJitterStatsSumOfPositivesDS_Type()
)
hwNqaJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSumOfPositivesDS.setStatus("current")
_HwNqaJitterStatsSum2PositivesDS_Type = Gauge32
_HwNqaJitterStatsSum2PositivesDS_Object = MibTableColumn
hwNqaJitterStatsSum2PositivesDS = _HwNqaJitterStatsSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 16),
    _HwNqaJitterStatsSum2PositivesDS_Type()
)
hwNqaJitterStatsSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSum2PositivesDS.setStatus("current")
_HwNqaJitterStatsMinOfNegativesDS_Type = Gauge32
_HwNqaJitterStatsMinOfNegativesDS_Object = MibTableColumn
hwNqaJitterStatsMinOfNegativesDS = _HwNqaJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 17),
    _HwNqaJitterStatsMinOfNegativesDS_Type()
)
hwNqaJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMinOfNegativesDS.setStatus("current")
_HwNqaJitterStatsMaxOfNegativesDS_Type = Gauge32
_HwNqaJitterStatsMaxOfNegativesDS_Object = MibTableColumn
hwNqaJitterStatsMaxOfNegativesDS = _HwNqaJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 18),
    _HwNqaJitterStatsMaxOfNegativesDS_Type()
)
hwNqaJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsMaxOfNegativesDS.setStatus("current")
_HwNqaJitterStatsNumOfNegativesDS_Type = Gauge32
_HwNqaJitterStatsNumOfNegativesDS_Object = MibTableColumn
hwNqaJitterStatsNumOfNegativesDS = _HwNqaJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 19),
    _HwNqaJitterStatsNumOfNegativesDS_Type()
)
hwNqaJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsNumOfNegativesDS.setStatus("current")
_HwNqaJitterStatsSumOfNegativesDS_Type = Gauge32
_HwNqaJitterStatsSumOfNegativesDS_Object = MibTableColumn
hwNqaJitterStatsSumOfNegativesDS = _HwNqaJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 20),
    _HwNqaJitterStatsSumOfNegativesDS_Type()
)
hwNqaJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSumOfNegativesDS.setStatus("current")
_HwNqaJitterStatsSum2NegativesDS_Type = Gauge32
_HwNqaJitterStatsSum2NegativesDS_Object = MibTableColumn
hwNqaJitterStatsSum2NegativesDS = _HwNqaJitterStatsSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 21),
    _HwNqaJitterStatsSum2NegativesDS_Type()
)
hwNqaJitterStatsSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsSum2NegativesDS.setStatus("current")
_HwNqaJitterStatsPacketLossSD_Type = Gauge32
_HwNqaJitterStatsPacketLossSD_Object = MibTableColumn
hwNqaJitterStatsPacketLossSD = _HwNqaJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 22),
    _HwNqaJitterStatsPacketLossSD_Type()
)
hwNqaJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsPacketLossSD.setStatus("current")
_HwNqaJitterStatsPacketLossDS_Type = Gauge32
_HwNqaJitterStatsPacketLossDS_Object = MibTableColumn
hwNqaJitterStatsPacketLossDS = _HwNqaJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 23),
    _HwNqaJitterStatsPacketLossDS_Type()
)
hwNqaJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsPacketLossDS.setStatus("current")
_HwNqaJitterStatsAvePositivesSD_Type = Gauge32
_HwNqaJitterStatsAvePositivesSD_Object = MibTableColumn
hwNqaJitterStatsAvePositivesSD = _HwNqaJitterStatsAvePositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 24),
    _HwNqaJitterStatsAvePositivesSD_Type()
)
hwNqaJitterStatsAvePositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsAvePositivesSD.setStatus("current")
_HwNqaJitterStatsAveNegativesSD_Type = Gauge32
_HwNqaJitterStatsAveNegativesSD_Object = MibTableColumn
hwNqaJitterStatsAveNegativesSD = _HwNqaJitterStatsAveNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 25),
    _HwNqaJitterStatsAveNegativesSD_Type()
)
hwNqaJitterStatsAveNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsAveNegativesSD.setStatus("current")
_HwNqaJitterStatsAvePositivesDS_Type = Gauge32
_HwNqaJitterStatsAvePositivesDS_Object = MibTableColumn
hwNqaJitterStatsAvePositivesDS = _HwNqaJitterStatsAvePositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 26),
    _HwNqaJitterStatsAvePositivesDS_Type()
)
hwNqaJitterStatsAvePositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsAvePositivesDS.setStatus("current")
_HwNqaJitterStatsAveNegativesDS_Type = Gauge32
_HwNqaJitterStatsAveNegativesDS_Object = MibTableColumn
hwNqaJitterStatsAveNegativesDS = _HwNqaJitterStatsAveNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 27),
    _HwNqaJitterStatsAveNegativesDS_Type()
)
hwNqaJitterStatsAveNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsAveNegativesDS.setStatus("current")
_HwNqaJitterStatsPktLossUnknown_Type = Gauge32
_HwNqaJitterStatsPktLossUnknown_Object = MibTableColumn
hwNqaJitterStatsPktLossUnknown = _HwNqaJitterStatsPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 28),
    _HwNqaJitterStatsPktLossUnknown_Type()
)
hwNqaJitterStatsPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsPktLossUnknown.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaJitterStatsPktLossUnknown.setUnits("milliseconds")
_HwNqaJitterStatsOperOfICPIF_Type = Gauge32
_HwNqaJitterStatsOperOfICPIF_Object = MibTableColumn
hwNqaJitterStatsOperOfICPIF = _HwNqaJitterStatsOperOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 29),
    _HwNqaJitterStatsOperOfICPIF_Type()
)
hwNqaJitterStatsOperOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsOperOfICPIF.setStatus("current")
_HwNqaJitterStatsOperOfMOS_Type = Gauge32
_HwNqaJitterStatsOperOfMOS_Object = MibTableColumn
hwNqaJitterStatsOperOfMOS = _HwNqaJitterStatsOperOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 4, 1, 30),
    _HwNqaJitterStatsOperOfMOS_Type()
)
hwNqaJitterStatsOperOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaJitterStatsOperOfMOS.setStatus("current")


class _HwNqaAgentEnable_Type(Integer32):
    """Custom type hwNqaAgentEnable based on Integer32"""
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


_HwNqaAgentEnable_Type.__name__ = "Integer32"
_HwNqaAgentEnable_Object = MibScalar
hwNqaAgentEnable = _HwNqaAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 5),
    _HwNqaAgentEnable_Type()
)
hwNqaAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNqaAgentEnable.setStatus("current")
_HwNqaTcpServerTable_Object = MibTable
hwNqaTcpServerTable = _HwNqaTcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 6)
)
if mibBuilder.loadTexts:
    hwNqaTcpServerTable.setStatus("current")
_HwNqaTcpServerEntry_Object = MibTableRow
hwNqaTcpServerEntry = _HwNqaTcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 6, 1)
)
hwNqaTcpServerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaTcpServerIpAddress"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaTcpServerPort"),
)
if mibBuilder.loadTexts:
    hwNqaTcpServerEntry.setStatus("current")


class _HwNqaTcpServerIpAddress_Type(InetAddress):
    """Custom type hwNqaTcpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_HwNqaTcpServerIpAddress_Object = MibTableColumn
hwNqaTcpServerIpAddress = _HwNqaTcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 6, 1, 1),
    _HwNqaTcpServerIpAddress_Type()
)
hwNqaTcpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaTcpServerIpAddress.setStatus("current")


class _HwNqaTcpServerPort_Type(Integer32):
    """Custom type hwNqaTcpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwNqaTcpServerPort_Type.__name__ = "Integer32"
_HwNqaTcpServerPort_Object = MibTableColumn
hwNqaTcpServerPort = _HwNqaTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 6, 1, 2),
    _HwNqaTcpServerPort_Type()
)
hwNqaTcpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaTcpServerPort.setStatus("current")
_HwNqaTcpServerRowStatus_Type = RowStatus
_HwNqaTcpServerRowStatus_Object = MibTableColumn
hwNqaTcpServerRowStatus = _HwNqaTcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 6, 1, 3),
    _HwNqaTcpServerRowStatus_Type()
)
hwNqaTcpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaTcpServerRowStatus.setStatus("current")
_HwNqaUdpServerTable_Object = MibTable
hwNqaUdpServerTable = _HwNqaUdpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 7)
)
if mibBuilder.loadTexts:
    hwNqaUdpServerTable.setStatus("current")
_HwNqaUdpServerEntry_Object = MibTableRow
hwNqaUdpServerEntry = _HwNqaUdpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 7, 1)
)
hwNqaUdpServerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaUdpServerIpAddress"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaUdpServerPort"),
)
if mibBuilder.loadTexts:
    hwNqaUdpServerEntry.setStatus("current")


class _HwNqaUdpServerIpAddress_Type(InetAddress):
    """Custom type hwNqaUdpServerIpAddress based on InetAddress"""
    defaultHexValue = ""


_HwNqaUdpServerIpAddress_Object = MibTableColumn
hwNqaUdpServerIpAddress = _HwNqaUdpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 7, 1, 1),
    _HwNqaUdpServerIpAddress_Type()
)
hwNqaUdpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaUdpServerIpAddress.setStatus("current")


class _HwNqaUdpServerPort_Type(Integer32):
    """Custom type hwNqaUdpServerPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwNqaUdpServerPort_Type.__name__ = "Integer32"
_HwNqaUdpServerPort_Object = MibTableColumn
hwNqaUdpServerPort = _HwNqaUdpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 7, 1, 2),
    _HwNqaUdpServerPort_Type()
)
hwNqaUdpServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaUdpServerPort.setStatus("current")
_HwNqaUdpServerRowStatus_Type = RowStatus
_HwNqaUdpServerRowStatus_Object = MibTableColumn
hwNqaUdpServerRowStatus = _HwNqaUdpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 7, 1, 3),
    _HwNqaUdpServerRowStatus_Type()
)
hwNqaUdpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaUdpServerRowStatus.setStatus("current")


class _HwNqaServerEnable_Type(Integer32):
    """Custom type hwNqaServerEnable based on Integer32"""
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


_HwNqaServerEnable_Type.__name__ = "Integer32"
_HwNqaServerEnable_Object = MibScalar
hwNqaServerEnable = _HwNqaServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 8),
    _HwNqaServerEnable_Type()
)
hwNqaServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNqaServerEnable.setStatus("current")
_HwNqaStatsMaxGroupNumber_Type = Integer32
_HwNqaStatsMaxGroupNumber_Object = MibScalar
hwNqaStatsMaxGroupNumber = _HwNqaStatsMaxGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 9),
    _HwNqaStatsMaxGroupNumber_Type()
)
hwNqaStatsMaxGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatsMaxGroupNumber.setStatus("current")
_HwNqaStatisticsCtlTable_Object = MibTable
hwNqaStatisticsCtlTable = _HwNqaStatisticsCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10)
)
if mibBuilder.loadTexts:
    hwNqaStatisticsCtlTable.setStatus("current")
_HwNqaStatisticsCtlEntry_Object = MibTableRow
hwNqaStatisticsCtlEntry = _HwNqaStatisticsCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hwNqaStatisticsCtlEntry.setStatus("current")
_HwNqaCtlStatisticsInterval_Type = Unsigned32
_HwNqaCtlStatisticsInterval_Object = MibTableColumn
hwNqaCtlStatisticsInterval = _HwNqaCtlStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10, 1, 1),
    _HwNqaCtlStatisticsInterval_Type()
)
hwNqaCtlStatisticsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlStatisticsInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaCtlStatisticsInterval.setUnits("minutes")


class _HwNqaCtlStatisticsGroupNumber_Type(Unsigned32):
    """Custom type hwNqaCtlStatisticsGroupNumber based on Unsigned32"""
    defaultValue = 2


_HwNqaCtlStatisticsGroupNumber_Object = MibTableColumn
hwNqaCtlStatisticsGroupNumber = _HwNqaCtlStatisticsGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10, 1, 2),
    _HwNqaCtlStatisticsGroupNumber_Type()
)
hwNqaCtlStatisticsGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlStatisticsGroupNumber.setStatus("current")


class _HwNqaCtlStatisticsKeptTime_Type(Unsigned32):
    """Custom type hwNqaCtlStatisticsKeptTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_HwNqaCtlStatisticsKeptTime_Type.__name__ = "Unsigned32"
_HwNqaCtlStatisticsKeptTime_Object = MibTableColumn
hwNqaCtlStatisticsKeptTime = _HwNqaCtlStatisticsKeptTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10, 1, 3),
    _HwNqaCtlStatisticsKeptTime_Type()
)
hwNqaCtlStatisticsKeptTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlStatisticsKeptTime.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaCtlStatisticsKeptTime.setUnits("minutes")
_HwNqaCtlBeginTime_Type = DateAndTime
_HwNqaCtlBeginTime_Object = MibTableColumn
hwNqaCtlBeginTime = _HwNqaCtlBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10, 1, 4),
    _HwNqaCtlBeginTime_Type()
)
hwNqaCtlBeginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlBeginTime.setStatus("current")


class _HwNqaCtlLifeTime_Type(Unsigned32):
    """Custom type hwNqaCtlLifeTime based on Unsigned32"""
    defaultValue = 0


_HwNqaCtlLifeTime_Object = MibTableColumn
hwNqaCtlLifeTime = _HwNqaCtlLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 10, 1, 5),
    _HwNqaCtlLifeTime_Type()
)
hwNqaCtlLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaCtlLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaCtlLifeTime.setUnits("seconds")
_HwNqaStatisticsResultsTable_Object = MibTable
hwNqaStatisticsResultsTable = _HwNqaStatisticsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11)
)
if mibBuilder.loadTexts:
    hwNqaStatisticsResultsTable.setStatus("current")
_HwNqaStatisticsResultsEntry_Object = MibTableRow
hwNqaStatisticsResultsEntry = _HwNqaStatisticsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1)
)
hwNqaStatisticsResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaStatResIndex"),
)
if mibBuilder.loadTexts:
    hwNqaStatisticsResultsEntry.setStatus("current")


class _HwNqaStatResIndex_Type(Unsigned32):
    """Custom type hwNqaStatResIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwNqaStatResIndex_Type.__name__ = "Unsigned32"
_HwNqaStatResIndex_Object = MibTableColumn
hwNqaStatResIndex = _HwNqaStatResIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 1),
    _HwNqaStatResIndex_Type()
)
hwNqaStatResIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaStatResIndex.setStatus("current")


class _HwNqaStatResIpTargetAddressType_Type(InetAddressType):
    """Custom type hwNqaStatResIpTargetAddressType based on InetAddressType"""


_HwNqaStatResIpTargetAddressType_Object = MibTableColumn
hwNqaStatResIpTargetAddressType = _HwNqaStatResIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 2),
    _HwNqaStatResIpTargetAddressType_Type()
)
hwNqaStatResIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResIpTargetAddressType.setStatus("current")


class _HwNqaStatResIpTargetAddress_Type(InetAddress):
    """Custom type hwNqaStatResIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_HwNqaStatResIpTargetAddress_Object = MibTableColumn
hwNqaStatResIpTargetAddress = _HwNqaStatResIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 3),
    _HwNqaStatResIpTargetAddress_Type()
)
hwNqaStatResIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResIpTargetAddress.setStatus("current")
_HwNqaStatResMinRtt_Type = Gauge32
_HwNqaStatResMinRtt_Object = MibTableColumn
hwNqaStatResMinRtt = _HwNqaStatResMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 4),
    _HwNqaStatResMinRtt_Type()
)
hwNqaStatResMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatResMinRtt.setUnits("milliseconds")
_HwNqaStatResMaxRtt_Type = Gauge32
_HwNqaStatResMaxRtt_Object = MibTableColumn
hwNqaStatResMaxRtt = _HwNqaStatResMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 5),
    _HwNqaStatResMaxRtt_Type()
)
hwNqaStatResMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatResMaxRtt.setUnits("milliseconds")
_HwNqaStatResAverageRtt_Type = Gauge32
_HwNqaStatResAverageRtt_Object = MibTableColumn
hwNqaStatResAverageRtt = _HwNqaStatResAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 6),
    _HwNqaStatResAverageRtt_Type()
)
hwNqaStatResAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatResAverageRtt.setUnits("milliseconds")
_HwNqaStatResProbeResponses_Type = Counter32
_HwNqaStatResProbeResponses_Object = MibTableColumn
hwNqaStatResProbeResponses = _HwNqaStatResProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 7),
    _HwNqaStatResProbeResponses_Type()
)
hwNqaStatResProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResProbeResponses.setStatus("current")
_HwNqaStatResSentProbes_Type = Counter32
_HwNqaStatResSentProbes_Object = MibTableColumn
hwNqaStatResSentProbes = _HwNqaStatResSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 8),
    _HwNqaStatResSentProbes_Type()
)
hwNqaStatResSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatResSentProbes.setUnits("probes")
_HwNqaStatResRttSumOfSquares_Type = Counter32
_HwNqaStatResRttSumOfSquares_Object = MibTableColumn
hwNqaStatResRttSumOfSquares = _HwNqaStatResRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 9),
    _HwNqaStatResRttSumOfSquares_Type()
)
hwNqaStatResRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatResRttSumOfSquares.setUnits("milliseconds")
_HwNqaStatResStartTime_Type = DateAndTime
_HwNqaStatResStartTime_Object = MibTableColumn
hwNqaStatResStartTime = _HwNqaStatResStartTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 10),
    _HwNqaStatResStartTime_Type()
)
hwNqaStatResStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResStartTime.setStatus("current")
_HwNqaStatResInterval_Type = Gauge32
_HwNqaStatResInterval_Object = MibTableColumn
hwNqaStatResInterval = _HwNqaStatResInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 11),
    _HwNqaStatResInterval_Type()
)
hwNqaStatResInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatResInterval.setUnits("seconds")
_HwNqaStatResRttNumDisconnects_Type = Counter32
_HwNqaStatResRttNumDisconnects_Object = MibTableColumn
hwNqaStatResRttNumDisconnects = _HwNqaStatResRttNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 12),
    _HwNqaStatResRttNumDisconnects_Type()
)
hwNqaStatResRttNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttNumDisconnects.setStatus("current")
_HwNqaStatResRttTimeouts_Type = Counter32
_HwNqaStatResRttTimeouts_Object = MibTableColumn
hwNqaStatResRttTimeouts = _HwNqaStatResRttTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 13),
    _HwNqaStatResRttTimeouts_Type()
)
hwNqaStatResRttTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttTimeouts.setStatus("current")
_HwNqaStatResRttBusies_Type = Counter32
_HwNqaStatResRttBusies_Object = MibTableColumn
hwNqaStatResRttBusies = _HwNqaStatResRttBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 14),
    _HwNqaStatResRttBusies_Type()
)
hwNqaStatResRttBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttBusies.setStatus("current")
_HwNqaStatResRttNoConnections_Type = Counter32
_HwNqaStatResRttNoConnections_Object = MibTableColumn
hwNqaStatResRttNoConnections = _HwNqaStatResRttNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 15),
    _HwNqaStatResRttNoConnections_Type()
)
hwNqaStatResRttNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttNoConnections.setStatus("current")
_HwNqaStatResRttDrops_Type = Counter32
_HwNqaStatResRttDrops_Object = MibTableColumn
hwNqaStatResRttDrops = _HwNqaStatResRttDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 16),
    _HwNqaStatResRttDrops_Type()
)
hwNqaStatResRttDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttDrops.setStatus("current")
_HwNqaStatResRttSequenceErrors_Type = Counter32
_HwNqaStatResRttSequenceErrors_Object = MibTableColumn
hwNqaStatResRttSequenceErrors = _HwNqaStatResRttSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 17),
    _HwNqaStatResRttSequenceErrors_Type()
)
hwNqaStatResRttSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttSequenceErrors.setStatus("current")
_HwNqaStatResRttErrors_Type = Counter32
_HwNqaStatResRttErrors_Object = MibTableColumn
hwNqaStatResRttErrors = _HwNqaStatResRttErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 18),
    _HwNqaStatResRttErrors_Type()
)
hwNqaStatResRttErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttErrors.setStatus("current")
_HwNqaStatResLostPacketRatio_Type = Gauge32
_HwNqaStatResLostPacketRatio_Object = MibTableColumn
hwNqaStatResLostPacketRatio = _HwNqaStatResLostPacketRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 19),
    _HwNqaStatResLostPacketRatio_Type()
)
hwNqaStatResLostPacketRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResLostPacketRatio.setStatus("current")
_HwNqaStatResPacketLateArrival_Type = Counter32
_HwNqaStatResPacketLateArrival_Object = MibTableColumn
hwNqaStatResPacketLateArrival = _HwNqaStatResPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 20),
    _HwNqaStatResPacketLateArrival_Type()
)
hwNqaStatResPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResPacketLateArrival.setStatus("current")
_HwNqaStatResRttSum_Type = Counter32
_HwNqaStatResRttSum_Object = MibTableColumn
hwNqaStatResRttSum = _HwNqaStatResRttSum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 21),
    _HwNqaStatResRttSum_Type()
)
hwNqaStatResRttSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResRttSum.setStatus("current")
_HwNqaStatResNumOfDelaySD_Type = Counter32
_HwNqaStatResNumOfDelaySD_Object = MibTableColumn
hwNqaStatResNumOfDelaySD = _HwNqaStatResNumOfDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 22),
    _HwNqaStatResNumOfDelaySD_Type()
)
hwNqaStatResNumOfDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResNumOfDelaySD.setStatus("current")
_HwNqaStatResMinDelaySD_Type = Gauge32
_HwNqaStatResMinDelaySD_Object = MibTableColumn
hwNqaStatResMinDelaySD = _HwNqaStatResMinDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 23),
    _HwNqaStatResMinDelaySD_Type()
)
hwNqaStatResMinDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResMinDelaySD.setStatus("current")
_HwNqaStatResMaxDelaySD_Type = Gauge32
_HwNqaStatResMaxDelaySD_Object = MibTableColumn
hwNqaStatResMaxDelaySD = _HwNqaStatResMaxDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 24),
    _HwNqaStatResMaxDelaySD_Type()
)
hwNqaStatResMaxDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResMaxDelaySD.setStatus("current")
_HwNqaStatResSumDelaySD_Type = Counter32
_HwNqaStatResSumDelaySD_Object = MibTableColumn
hwNqaStatResSumDelaySD = _HwNqaStatResSumDelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 25),
    _HwNqaStatResSumDelaySD_Type()
)
hwNqaStatResSumDelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResSumDelaySD.setStatus("current")
_HwNqaStatResSum2DelaySD_Type = Counter32
_HwNqaStatResSum2DelaySD_Object = MibTableColumn
hwNqaStatResSum2DelaySD = _HwNqaStatResSum2DelaySD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 26),
    _HwNqaStatResSum2DelaySD_Type()
)
hwNqaStatResSum2DelaySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResSum2DelaySD.setStatus("current")
_HwNqaStatResNumOfDelayDS_Type = Counter32
_HwNqaStatResNumOfDelayDS_Object = MibTableColumn
hwNqaStatResNumOfDelayDS = _HwNqaStatResNumOfDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 27),
    _HwNqaStatResNumOfDelayDS_Type()
)
hwNqaStatResNumOfDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResNumOfDelayDS.setStatus("current")
_HwNqaStatResMinDelayDS_Type = Gauge32
_HwNqaStatResMinDelayDS_Object = MibTableColumn
hwNqaStatResMinDelayDS = _HwNqaStatResMinDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 28),
    _HwNqaStatResMinDelayDS_Type()
)
hwNqaStatResMinDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResMinDelayDS.setStatus("current")
_HwNqaStatResMaxDelayDS_Type = Gauge32
_HwNqaStatResMaxDelayDS_Object = MibTableColumn
hwNqaStatResMaxDelayDS = _HwNqaStatResMaxDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 29),
    _HwNqaStatResMaxDelayDS_Type()
)
hwNqaStatResMaxDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResMaxDelayDS.setStatus("current")
_HwNqaStatResSumDelayDS_Type = Counter32
_HwNqaStatResSumDelayDS_Object = MibTableColumn
hwNqaStatResSumDelayDS = _HwNqaStatResSumDelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 30),
    _HwNqaStatResSumDelayDS_Type()
)
hwNqaStatResSumDelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResSumDelayDS.setStatus("current")
_HwNqaStatResSum2DelayDS_Type = Counter32
_HwNqaStatResSum2DelayDS_Object = MibTableColumn
hwNqaStatResSum2DelayDS = _HwNqaStatResSum2DelayDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 11, 1, 31),
    _HwNqaStatResSum2DelayDS_Type()
)
hwNqaStatResSum2DelayDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatResSum2DelayDS.setStatus("current")
_HwNqaGroupStatsJitterTable_Object = MibTable
hwNqaGroupStatsJitterTable = _HwNqaGroupStatsJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12)
)
if mibBuilder.loadTexts:
    hwNqaGroupStatsJitterTable.setStatus("current")
_HwNqaGroupStatsJitterEntry_Object = MibTableRow
hwNqaGroupStatsJitterEntry = _HwNqaGroupStatsJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1)
)
hwNqaGroupStatsJitterEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaStatJitterIndex"),
)
if mibBuilder.loadTexts:
    hwNqaGroupStatsJitterEntry.setStatus("current")


class _HwNqaStatJitterIndex_Type(Unsigned32):
    """Custom type hwNqaStatJitterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwNqaStatJitterIndex_Type.__name__ = "Unsigned32"
_HwNqaStatJitterIndex_Object = MibTableColumn
hwNqaStatJitterIndex = _HwNqaStatJitterIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 1),
    _HwNqaStatJitterIndex_Type()
)
hwNqaStatJitterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaStatJitterIndex.setStatus("current")
_HwNqaStatJitterMinOfPosSD_Type = Gauge32
_HwNqaStatJitterMinOfPosSD_Object = MibTableColumn
hwNqaStatJitterMinOfPosSD = _HwNqaStatJitterMinOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 2),
    _HwNqaStatJitterMinOfPosSD_Type()
)
hwNqaStatJitterMinOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfPosSD.setUnits("milliseconds")
_HwNqaStatJitterMaxOfPosSD_Type = Gauge32
_HwNqaStatJitterMaxOfPosSD_Object = MibTableColumn
hwNqaStatJitterMaxOfPosSD = _HwNqaStatJitterMaxOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 3),
    _HwNqaStatJitterMaxOfPosSD_Type()
)
hwNqaStatJitterMaxOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfPosSD.setUnits("milliseconds")
_HwNqaStatJitterNumOfPosSD_Type = Counter32
_HwNqaStatJitterNumOfPosSD_Object = MibTableColumn
hwNqaStatJitterNumOfPosSD = _HwNqaStatJitterNumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 4),
    _HwNqaStatJitterNumOfPosSD_Type()
)
hwNqaStatJitterNumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterNumOfPosSD.setStatus("current")
_HwNqaStatJitterSumOfPosSD_Type = Counter32
_HwNqaStatJitterSumOfPosSD_Object = MibTableColumn
hwNqaStatJitterSumOfPosSD = _HwNqaStatJitterSumOfPosSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 5),
    _HwNqaStatJitterSumOfPosSD_Type()
)
hwNqaStatJitterSumOfPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfPosSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfPosSD.setUnits("milliseconds")
_HwNqaStatJitterSumOfSquarePosSD_Type = Counter32
_HwNqaStatJitterSumOfSquarePosSD_Object = MibTableColumn
hwNqaStatJitterSumOfSquarePosSD = _HwNqaStatJitterSumOfSquarePosSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 6),
    _HwNqaStatJitterSumOfSquarePosSD_Type()
)
hwNqaStatJitterSumOfSquarePosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquarePosSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquarePosSD.setUnits("milliseconds")
_HwNqaStatJitterMinOfNegSD_Type = Gauge32
_HwNqaStatJitterMinOfNegSD_Object = MibTableColumn
hwNqaStatJitterMinOfNegSD = _HwNqaStatJitterMinOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 7),
    _HwNqaStatJitterMinOfNegSD_Type()
)
hwNqaStatJitterMinOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfNegSD.setUnits("milliseconds")
_HwNqaStatJitterMaxOfNegSD_Type = Gauge32
_HwNqaStatJitterMaxOfNegSD_Object = MibTableColumn
hwNqaStatJitterMaxOfNegSD = _HwNqaStatJitterMaxOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 8),
    _HwNqaStatJitterMaxOfNegSD_Type()
)
hwNqaStatJitterMaxOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfNegSD.setUnits("milliseconds")
_HwNqaStatJitterNumOfNegSD_Type = Counter32
_HwNqaStatJitterNumOfNegSD_Object = MibTableColumn
hwNqaStatJitterNumOfNegSD = _HwNqaStatJitterNumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 9),
    _HwNqaStatJitterNumOfNegSD_Type()
)
hwNqaStatJitterNumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterNumOfNegSD.setStatus("current")
_HwNqaStatJitterSumOfNegSD_Type = Counter32
_HwNqaStatJitterSumOfNegSD_Object = MibTableColumn
hwNqaStatJitterSumOfNegSD = _HwNqaStatJitterSumOfNegSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 10),
    _HwNqaStatJitterSumOfNegSD_Type()
)
hwNqaStatJitterSumOfNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfNegSD.setUnits("milliseconds")
_HwNqaStatJitterSumOfSquareNegSD_Type = Counter32
_HwNqaStatJitterSumOfSquareNegSD_Object = MibTableColumn
hwNqaStatJitterSumOfSquareNegSD = _HwNqaStatJitterSumOfSquareNegSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 11),
    _HwNqaStatJitterSumOfSquareNegSD_Type()
)
hwNqaStatJitterSumOfSquareNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquareNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquareNegSD.setUnits("milliseconds")
_HwNqaStatJitterMinOfPosDS_Type = Gauge32
_HwNqaStatJitterMinOfPosDS_Object = MibTableColumn
hwNqaStatJitterMinOfPosDS = _HwNqaStatJitterMinOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 12),
    _HwNqaStatJitterMinOfPosDS_Type()
)
hwNqaStatJitterMinOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfPosDS.setUnits("milliseconds")
_HwNqaStatJitterMaxOfPosDS_Type = Gauge32
_HwNqaStatJitterMaxOfPosDS_Object = MibTableColumn
hwNqaStatJitterMaxOfPosDS = _HwNqaStatJitterMaxOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 13),
    _HwNqaStatJitterMaxOfPosDS_Type()
)
hwNqaStatJitterMaxOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfPosDS.setUnits("milliseconds")
_HwNqaStatJitterNumOfPosDS_Type = Counter32
_HwNqaStatJitterNumOfPosDS_Object = MibTableColumn
hwNqaStatJitterNumOfPosDS = _HwNqaStatJitterNumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 14),
    _HwNqaStatJitterNumOfPosDS_Type()
)
hwNqaStatJitterNumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterNumOfPosDS.setStatus("current")
_HwNqaStatJitterSumOfPosDS_Type = Counter32
_HwNqaStatJitterSumOfPosDS_Object = MibTableColumn
hwNqaStatJitterSumOfPosDS = _HwNqaStatJitterSumOfPosDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 15),
    _HwNqaStatJitterSumOfPosDS_Type()
)
hwNqaStatJitterSumOfPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfPosDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfPosDS.setUnits("milliseconds")
_HwNqaStatJitterSumOfSquarePosDS_Type = Counter32
_HwNqaStatJitterSumOfSquarePosDS_Object = MibTableColumn
hwNqaStatJitterSumOfSquarePosDS = _HwNqaStatJitterSumOfSquarePosDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 16),
    _HwNqaStatJitterSumOfSquarePosDS_Type()
)
hwNqaStatJitterSumOfSquarePosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquarePosDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquarePosDS.setUnits("milliseconds")
_HwNqaStatJitterMinOfNegDS_Type = Gauge32
_HwNqaStatJitterMinOfNegDS_Object = MibTableColumn
hwNqaStatJitterMinOfNegDS = _HwNqaStatJitterMinOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 17),
    _HwNqaStatJitterMinOfNegDS_Type()
)
hwNqaStatJitterMinOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfNegDS.setUnits("milliseconds")
_HwNqaStatJitterMaxOfNegDS_Type = Gauge32
_HwNqaStatJitterMaxOfNegDS_Object = MibTableColumn
hwNqaStatJitterMaxOfNegDS = _HwNqaStatJitterMaxOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 18),
    _HwNqaStatJitterMaxOfNegDS_Type()
)
hwNqaStatJitterMaxOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfNegDS.setUnits("milliseconds")
_HwNqaStatJitterNumOfNegDS_Type = Counter32
_HwNqaStatJitterNumOfNegDS_Object = MibTableColumn
hwNqaStatJitterNumOfNegDS = _HwNqaStatJitterNumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 19),
    _HwNqaStatJitterNumOfNegDS_Type()
)
hwNqaStatJitterNumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterNumOfNegDS.setStatus("current")
_HwNqaStatJitterSumOfNegDS_Type = Counter32
_HwNqaStatJitterSumOfNegDS_Object = MibTableColumn
hwNqaStatJitterSumOfNegDS = _HwNqaStatJitterSumOfNegDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 20),
    _HwNqaStatJitterSumOfNegDS_Type()
)
hwNqaStatJitterSumOfNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfNegDS.setUnits("milliseconds")
_HwNqaStatJitterSumOfSquareNegDS_Type = Counter32
_HwNqaStatJitterSumOfSquareNegDS_Object = MibTableColumn
hwNqaStatJitterSumOfSquareNegDS = _HwNqaStatJitterSumOfSquareNegDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 21),
    _HwNqaStatJitterSumOfSquareNegDS_Type()
)
hwNqaStatJitterSumOfSquareNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquareNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterSumOfSquareNegDS.setUnits("milliseconds")
_HwNqaStatJitterPacketLossSD_Type = Counter32
_HwNqaStatJitterPacketLossSD_Object = MibTableColumn
hwNqaStatJitterPacketLossSD = _HwNqaStatJitterPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 22),
    _HwNqaStatJitterPacketLossSD_Type()
)
hwNqaStatJitterPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterPacketLossSD.setStatus("current")
_HwNqaStatJitterPacketLossDS_Type = Counter32
_HwNqaStatJitterPacketLossDS_Object = MibTableColumn
hwNqaStatJitterPacketLossDS = _HwNqaStatJitterPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 23),
    _HwNqaStatJitterPacketLossDS_Type()
)
hwNqaStatJitterPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterPacketLossDS.setStatus("current")
_HwNqaStatJitterAvePosSD_Type = Gauge32
_HwNqaStatJitterAvePosSD_Object = MibTableColumn
hwNqaStatJitterAvePosSD = _HwNqaStatJitterAvePosSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 24),
    _HwNqaStatJitterAvePosSD_Type()
)
hwNqaStatJitterAvePosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterAvePosSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterAvePosSD.setUnits("milliseconds")
_HwNqaStatJitterAveNegSD_Type = Gauge32
_HwNqaStatJitterAveNegSD_Object = MibTableColumn
hwNqaStatJitterAveNegSD = _HwNqaStatJitterAveNegSD_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 25),
    _HwNqaStatJitterAveNegSD_Type()
)
hwNqaStatJitterAveNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterAveNegSD.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterAveNegSD.setUnits("milliseconds")
_HwNqaStatJitterAvePosDS_Type = Gauge32
_HwNqaStatJitterAvePosDS_Object = MibTableColumn
hwNqaStatJitterAvePosDS = _HwNqaStatJitterAvePosDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 26),
    _HwNqaStatJitterAvePosDS_Type()
)
hwNqaStatJitterAvePosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterAvePosDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterAvePosDS.setUnits("milliseconds")
_HwNqaStatJitterAveNegDS_Type = Gauge32
_HwNqaStatJitterAveNegDS_Object = MibTableColumn
hwNqaStatJitterAveNegDS = _HwNqaStatJitterAveNegDS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 27),
    _HwNqaStatJitterAveNegDS_Type()
)
hwNqaStatJitterAveNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterAveNegDS.setStatus("current")
if mibBuilder.loadTexts:
    hwNqaStatJitterAveNegDS.setUnits("milliseconds")
_HwNqaStatJitterPktLossUnknown_Type = Counter32
_HwNqaStatJitterPktLossUnknown_Object = MibTableColumn
hwNqaStatJitterPktLossUnknown = _HwNqaStatJitterPktLossUnknown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 28),
    _HwNqaStatJitterPktLossUnknown_Type()
)
hwNqaStatJitterPktLossUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterPktLossUnknown.setStatus("current")
_HwNqaStatJitterMaxOfICPIF_Type = Gauge32
_HwNqaStatJitterMaxOfICPIF_Object = MibTableColumn
hwNqaStatJitterMaxOfICPIF = _HwNqaStatJitterMaxOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 29),
    _HwNqaStatJitterMaxOfICPIF_Type()
)
hwNqaStatJitterMaxOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfICPIF.setStatus("current")
_HwNqaStatJitterMinOfICPIF_Type = Gauge32
_HwNqaStatJitterMinOfICPIF_Object = MibTableColumn
hwNqaStatJitterMinOfICPIF = _HwNqaStatJitterMinOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 30),
    _HwNqaStatJitterMinOfICPIF_Type()
)
hwNqaStatJitterMinOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfICPIF.setStatus("current")
_HwNqaStatJitterMaxOfMOS_Type = Gauge32
_HwNqaStatJitterMaxOfMOS_Object = MibTableColumn
hwNqaStatJitterMaxOfMOS = _HwNqaStatJitterMaxOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 31),
    _HwNqaStatJitterMaxOfMOS_Type()
)
hwNqaStatJitterMaxOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMaxOfMOS.setStatus("current")
_HwNqaStatJitterMinOfMOS_Type = Gauge32
_HwNqaStatJitterMinOfMOS_Object = MibTableColumn
hwNqaStatJitterMinOfMOS = _HwNqaStatJitterMinOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 12, 1, 32),
    _HwNqaStatJitterMinOfMOS_Type()
)
hwNqaStatJitterMinOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatJitterMinOfMOS.setStatus("current")
_HwNqaReactionTable_Object = MibTable
hwNqaReactionTable = _HwNqaReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13)
)
if mibBuilder.loadTexts:
    hwNqaReactionTable.setStatus("current")
_HwNqaReactionEntry_Object = MibTableRow
hwNqaReactionEntry = _HwNqaReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1)
)
hwNqaReactionEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
)
if mibBuilder.loadTexts:
    hwNqaReactionEntry.setStatus("current")


class _HwNqaReactOwnerIndex_Type(SnmpAdminString):
    """Custom type hwNqaReactOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNqaReactOwnerIndex_Type.__name__ = "SnmpAdminString"
_HwNqaReactOwnerIndex_Object = MibTableColumn
hwNqaReactOwnerIndex = _HwNqaReactOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 1),
    _HwNqaReactOwnerIndex_Type()
)
hwNqaReactOwnerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwNqaReactOwnerIndex.setStatus("current")


class _HwNqaReactTestName_Type(SnmpAdminString):
    """Custom type hwNqaReactTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNqaReactTestName_Type.__name__ = "SnmpAdminString"
_HwNqaReactTestName_Object = MibTableColumn
hwNqaReactTestName = _HwNqaReactTestName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 2),
    _HwNqaReactTestName_Type()
)
hwNqaReactTestName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwNqaReactTestName.setStatus("current")


class _HwNqaReactItemIndex_Type(Unsigned32):
    """Custom type hwNqaReactItemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwNqaReactItemIndex_Type.__name__ = "Unsigned32"
_HwNqaReactItemIndex_Object = MibTableColumn
hwNqaReactItemIndex = _HwNqaReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 3),
    _HwNqaReactItemIndex_Type()
)
hwNqaReactItemIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwNqaReactItemIndex.setStatus("current")


class _HwNqaReactCheckedElement_Type(Integer32):
    """Custom type hwNqaReactCheckedElement based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("icpif", 7),
          ("jitterOwdDS", 10),
          ("jitterOwdSD", 9),
          ("jitterds", 6),
          ("jitterpacketloss", 4),
          ("jitterrtt", 3),
          ("jittersd", 5),
          ("mos", 8),
          ("probefailure", 2),
          ("probetime", 1))
    )


_HwNqaReactCheckedElement_Type.__name__ = "Integer32"
_HwNqaReactCheckedElement_Object = MibTableColumn
hwNqaReactCheckedElement = _HwNqaReactCheckedElement_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 4),
    _HwNqaReactCheckedElement_Type()
)
hwNqaReactCheckedElement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactCheckedElement.setStatus("current")


class _HwNqaReactThresholdUpperLimit_Type(Unsigned32):
    """Custom type hwNqaReactThresholdUpperLimit based on Unsigned32"""
    defaultValue = 0


_HwNqaReactThresholdUpperLimit_Object = MibTableColumn
hwNqaReactThresholdUpperLimit = _HwNqaReactThresholdUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 5),
    _HwNqaReactThresholdUpperLimit_Type()
)
hwNqaReactThresholdUpperLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactThresholdUpperLimit.setStatus("current")


class _HwNqaReactThresholdLowerLimit_Type(Unsigned32):
    """Custom type hwNqaReactThresholdLowerLimit based on Unsigned32"""
    defaultValue = 0


_HwNqaReactThresholdLowerLimit_Object = MibTableColumn
hwNqaReactThresholdLowerLimit = _HwNqaReactThresholdLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 6),
    _HwNqaReactThresholdLowerLimit_Type()
)
hwNqaReactThresholdLowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactThresholdLowerLimit.setStatus("current")


class _HwNqaReactThresholdType_Type(Integer32):
    """Custom type hwNqaReactThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accumulative", 3),
          ("average", 1),
          ("consecutive", 2),
          ("invalid", 0))
    )


_HwNqaReactThresholdType_Type.__name__ = "Integer32"
_HwNqaReactThresholdType_Object = MibTableColumn
hwNqaReactThresholdType = _HwNqaReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 7),
    _HwNqaReactThresholdType_Type()
)
hwNqaReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactThresholdType.setStatus("current")


class _HwNqaReactThresholdConsecNum_Type(Unsigned32):
    """Custom type hwNqaReactThresholdConsecNum based on Unsigned32"""
    defaultValue = 0


_HwNqaReactThresholdConsecNum_Object = MibTableColumn
hwNqaReactThresholdConsecNum = _HwNqaReactThresholdConsecNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 8),
    _HwNqaReactThresholdConsecNum_Type()
)
hwNqaReactThresholdConsecNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactThresholdConsecNum.setStatus("current")


class _HwNqaReactThresholdAccumNum_Type(Unsigned32):
    """Custom type hwNqaReactThresholdAccumNum based on Unsigned32"""
    defaultValue = 0


_HwNqaReactThresholdAccumNum_Object = MibTableColumn
hwNqaReactThresholdAccumNum = _HwNqaReactThresholdAccumNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 9),
    _HwNqaReactThresholdAccumNum_Type()
)
hwNqaReactThresholdAccumNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactThresholdAccumNum.setStatus("current")


class _HwNqaReactActionType_Type(Integer32):
    """Custom type hwNqaReactActionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trapAndTrigger", 3),
          ("trapOnly", 1),
          ("triggerOnly", 2))
    )


_HwNqaReactActionType_Type.__name__ = "Integer32"
_HwNqaReactActionType_Object = MibTableColumn
hwNqaReactActionType = _HwNqaReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 10),
    _HwNqaReactActionType_Type()
)
hwNqaReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactActionType.setStatus("current")


class _HwNqaReactCurrentStatus_Type(Integer32):
    """Custom type hwNqaReactCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("belowThreshold", 3),
          ("invalid", 1),
          ("overThreshold", 2))
    )


_HwNqaReactCurrentStatus_Type.__name__ = "Integer32"
_HwNqaReactCurrentStatus_Object = MibTableColumn
hwNqaReactCurrentStatus = _HwNqaReactCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 11),
    _HwNqaReactCurrentStatus_Type()
)
hwNqaReactCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaReactCurrentStatus.setStatus("current")
_HwNqaReactRowStatus_Type = RowStatus
_HwNqaReactRowStatus_Object = MibTableColumn
hwNqaReactRowStatus = _HwNqaReactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 12),
    _HwNqaReactRowStatus_Type()
)
hwNqaReactRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNqaReactRowStatus.setStatus("current")


class _HwNqaReactCheckedNum_Type(Unsigned32):
    """Custom type hwNqaReactCheckedNum based on Unsigned32"""
    defaultValue = 0


_HwNqaReactCheckedNum_Object = MibTableColumn
hwNqaReactCheckedNum = _HwNqaReactCheckedNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 13),
    _HwNqaReactCheckedNum_Type()
)
hwNqaReactCheckedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaReactCheckedNum.setStatus("current")


class _HwNqaReactThresholdNum_Type(Unsigned32):
    """Custom type hwNqaReactThresholdNum based on Unsigned32"""
    defaultValue = 0


_HwNqaReactThresholdNum_Object = MibTableColumn
hwNqaReactThresholdNum = _HwNqaReactThresholdNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 13, 1, 14),
    _HwNqaReactThresholdNum_Type()
)
hwNqaReactThresholdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaReactThresholdNum.setStatus("current")
_HwNqaStatisticsReactionTable_Object = MibTable
hwNqaStatisticsReactionTable = _HwNqaStatisticsReactionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14)
)
if mibBuilder.loadTexts:
    hwNqaStatisticsReactionTable.setStatus("current")
_HwNqaStatisticsReactionEntry_Object = MibTableRow
hwNqaStatisticsReactionEntry = _HwNqaStatisticsReactionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1)
)
hwNqaStatisticsReactionEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaStatReactOwnerIndex"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaStatReactTestName"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaStatReactIndex"),
    (0, "A3COM-HUAWEI-NQA-MIB", "hwNqaStatReactItemIndex"),
)
if mibBuilder.loadTexts:
    hwNqaStatisticsReactionEntry.setStatus("current")


class _HwNqaStatReactOwnerIndex_Type(SnmpAdminString):
    """Custom type hwNqaStatReactOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNqaStatReactOwnerIndex_Type.__name__ = "SnmpAdminString"
_HwNqaStatReactOwnerIndex_Object = MibTableColumn
hwNqaStatReactOwnerIndex = _HwNqaStatReactOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1, 1),
    _HwNqaStatReactOwnerIndex_Type()
)
hwNqaStatReactOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaStatReactOwnerIndex.setStatus("current")


class _HwNqaStatReactTestName_Type(SnmpAdminString):
    """Custom type hwNqaStatReactTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwNqaStatReactTestName_Type.__name__ = "SnmpAdminString"
_HwNqaStatReactTestName_Object = MibTableColumn
hwNqaStatReactTestName = _HwNqaStatReactTestName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1, 2),
    _HwNqaStatReactTestName_Type()
)
hwNqaStatReactTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaStatReactTestName.setStatus("current")


class _HwNqaStatReactIndex_Type(Unsigned32):
    """Custom type hwNqaStatReactIndex based on Unsigned32"""
    defaultValue = 0


_HwNqaStatReactIndex_Object = MibTableColumn
hwNqaStatReactIndex = _HwNqaStatReactIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1, 3),
    _HwNqaStatReactIndex_Type()
)
hwNqaStatReactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaStatReactIndex.setStatus("current")


class _HwNqaStatReactItemIndex_Type(Unsigned32):
    """Custom type hwNqaStatReactItemIndex based on Unsigned32"""
    defaultValue = 0


_HwNqaStatReactItemIndex_Object = MibTableColumn
hwNqaStatReactItemIndex = _HwNqaStatReactItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1, 4),
    _HwNqaStatReactItemIndex_Type()
)
hwNqaStatReactItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNqaStatReactItemIndex.setStatus("current")


class _HwNqaStatReactCheckedNum_Type(Counter32):
    """Custom type hwNqaStatReactCheckedNum based on Counter32"""
    defaultValue = 0


_HwNqaStatReactCheckedNum_Object = MibTableColumn
hwNqaStatReactCheckedNum = _HwNqaStatReactCheckedNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1, 5),
    _HwNqaStatReactCheckedNum_Type()
)
hwNqaStatReactCheckedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatReactCheckedNum.setStatus("current")


class _HwNqaStatReactThresholdNum_Type(Counter32):
    """Custom type hwNqaStatReactThresholdNum based on Counter32"""
    defaultValue = 0


_HwNqaStatReactThresholdNum_Object = MibTableColumn
hwNqaStatReactThresholdNum = _HwNqaStatReactThresholdNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 1, 14, 1, 6),
    _HwNqaStatReactThresholdNum_Type()
)
hwNqaStatReactThresholdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNqaStatReactThresholdNum.setStatus("current")
_HwNqaImplementationTypeDomains_ObjectIdentity = ObjectIdentity
hwNqaImplementationTypeDomains = _HwNqaImplementationTypeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2)
)
_HwNqaUdpEcho_ObjectIdentity = ObjectIdentity
hwNqaUdpEcho = _HwNqaUdpEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 1)
)
if mibBuilder.loadTexts:
    hwNqaUdpEcho.setStatus("current")
_HwNqaTcpconnect_ObjectIdentity = ObjectIdentity
hwNqaTcpconnect = _HwNqaTcpconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 2)
)
if mibBuilder.loadTexts:
    hwNqaTcpconnect.setStatus("current")
_HwNqajitter_ObjectIdentity = ObjectIdentity
hwNqajitter = _HwNqajitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 3)
)
if mibBuilder.loadTexts:
    hwNqajitter.setStatus("current")
_HwNqaHttp_ObjectIdentity = ObjectIdentity
hwNqaHttp = _HwNqaHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 4)
)
if mibBuilder.loadTexts:
    hwNqaHttp.setStatus("current")
_HwNqadlsw_ObjectIdentity = ObjectIdentity
hwNqadlsw = _HwNqadlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 5)
)
if mibBuilder.loadTexts:
    hwNqadlsw.setStatus("current")
_HwNqadhcp_ObjectIdentity = ObjectIdentity
hwNqadhcp = _HwNqadhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 6)
)
if mibBuilder.loadTexts:
    hwNqadhcp.setStatus("current")
_HwNqaftp_ObjectIdentity = ObjectIdentity
hwNqaftp = _HwNqaftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 2, 7)
)
if mibBuilder.loadTexts:
    hwNqaftp.setStatus("current")
_HwNqaNotifications_ObjectIdentity = ObjectIdentity
hwNqaNotifications = _HwNqaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3)
)
pingCtlEntry.registerAugmentions(
    ("A3COM-HUAWEI-NQA-MIB",
     "hwNqaCtlEntry")
)
hwNqaCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions(
    ("A3COM-HUAWEI-NQA-MIB",
     "hwNqaStatisticsCtlEntry")
)
hwNqaStatisticsCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hwNqaProbeTimeOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 1)
)
hwNqaProbeTimeOverThreshold.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactThresholdType"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaProbeTimeOverThreshold.setStatus(
        "current"
    )

hwNqaJitterRTTOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 2)
)
hwNqaJitterRTTOverThreshold.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactThresholdType"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaJitterRTTOverThreshold.setStatus(
        "current"
    )

hwNqaProbeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 3)
)
hwNqaProbeFailure.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactThresholdType"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaProbeFailure.setStatus(
        "current"
    )

hwNqaJitterPacketLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 4)
)
hwNqaJitterPacketLoss.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactThresholdType"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaJitterPacketLoss.setStatus(
        "current"
    )

hwNqaJitterSDOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 5)
)
hwNqaJitterSDOverThreshold.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactThresholdType"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaJitterSDOverThreshold.setStatus(
        "current"
    )

hwNqaJitterDSOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 6)
)
hwNqaJitterDSOverThreshold.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactThresholdType"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaJitterDSOverThreshold.setStatus(
        "current"
    )

hwNqaICPIFOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 7)
)
hwNqaICPIFOverThreshold.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaICPIFOverThreshold.setStatus(
        "current"
    )

hwNqaMOSOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 28, 3, 8)
)
hwNqaMOSOverThreshold.setObjects(
      *(("A3COM-HUAWEI-NQA-MIB", "hwNqaReactOwnerIndex"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactTestName"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactItemIndex"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddressType"),
        ("DISMAN-PING-MIB", "pingCtlTargetAddress"),
        ("DISMAN-PING-MIB", "pingCtlType"),
        ("DISMAN-PING-MIB", "pingCtlDescr"),
        ("A3COM-HUAWEI-NQA-MIB", "hwNqaReactCurrentStatus"))
)
if mibBuilder.loadTexts:
    hwNqaMOSOverThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-NQA-MIB",
    **{"hwNqa": hwNqa,
       "hwNqaObjects": hwNqaObjects,
       "hwNqaMIBVersion": hwNqaMIBVersion,
       "hwNqaCtlTable": hwNqaCtlTable,
       "hwNqaCtlEntry": hwNqaCtlEntry,
       "hwNqaCtlTargetPort": hwNqaCtlTargetPort,
       "hwNqaCtlSourcePort": hwNqaCtlSourcePort,
       "hwNqaCtlTTL": hwNqaCtlTTL,
       "hwNqaCtlJitterAdminInterval": hwNqaCtlJitterAdminInterval,
       "hwNqaCtlJitterAdminNumPackets": hwNqaCtlJitterAdminNumPackets,
       "hwNqaCtlHttpOperationType": hwNqaCtlHttpOperationType,
       "hwNqaCtlHttpOperationString": hwNqaCtlHttpOperationString,
       "hwNqaCtlFtpOperationType": hwNqaCtlFtpOperationType,
       "hwNqaCtlFtpUsername": hwNqaCtlFtpUsername,
       "hwNqaCtlFtpPassword": hwNqaCtlFtpPassword,
       "hwNqaCtlFtpOperationString": hwNqaCtlFtpOperationString,
       "hwNqaCtlVPNInstance": hwNqaCtlVPNInstance,
       "hwNqaCtlHistoryKeptTime": hwNqaCtlHistoryKeptTime,
       "hwNqaCtlHistoryEnable": hwNqaCtlHistoryEnable,
       "hwNqaCtlICPIFAdvFactor": hwNqaCtlICPIFAdvFactor,
       "hwNqaCtlCodecType": hwNqaCtlCodecType,
       "hwNqaResultsTable": hwNqaResultsTable,
       "hwNqaResultsEntry": hwNqaResultsEntry,
       "hwNqaResultsRttNumDisconnects": hwNqaResultsRttNumDisconnects,
       "hwNqaResultsRttTimeouts": hwNqaResultsRttTimeouts,
       "hwNqaResultsRttBusies": hwNqaResultsRttBusies,
       "hwNqaResultsRttNoConnections": hwNqaResultsRttNoConnections,
       "hwNqaResultsRttDrops": hwNqaResultsRttDrops,
       "hwNqaResultsRttSequenceErrors": hwNqaResultsRttSequenceErrors,
       "hwNqaResultsRttStatsErrors": hwNqaResultsRttStatsErrors,
       "hwNqaResultsMaxDelaySD": hwNqaResultsMaxDelaySD,
       "hwNqaResultsMaxDelayDS": hwNqaResultsMaxDelayDS,
       "hwNqaResultsLostPacketRatio": hwNqaResultsLostPacketRatio,
       "hwNqaResultsPacketLateArrival": hwNqaResultsPacketLateArrival,
       "hwNqaResultsRttSum": hwNqaResultsRttSum,
       "hwNqaResultsNumOfDelaySD": hwNqaResultsNumOfDelaySD,
       "hwNqaResultsMinDelaySD": hwNqaResultsMinDelaySD,
       "hwNqaResultsSumDelaySD": hwNqaResultsSumDelaySD,
       "hwNqaResultsSum2DelaySD": hwNqaResultsSum2DelaySD,
       "hwNqaResultsNumOfDelayDS": hwNqaResultsNumOfDelayDS,
       "hwNqaResultsMinDelayDS": hwNqaResultsMinDelayDS,
       "hwNqaResultsSumDelayDS": hwNqaResultsSumDelayDS,
       "hwNqaResultsSum2DelayDS": hwNqaResultsSum2DelayDS,
       "hwNqaJitterStatsTable": hwNqaJitterStatsTable,
       "hwNqaJitterStatsEntry": hwNqaJitterStatsEntry,
       "hwNqaJitterStatsNumOfRTT": hwNqaJitterStatsNumOfRTT,
       "hwNqaJitterStatsMinOfPositivesSD": hwNqaJitterStatsMinOfPositivesSD,
       "hwNqaJitterStatsMaxOfPositivesSD": hwNqaJitterStatsMaxOfPositivesSD,
       "hwNqaJitterStatsNumOfPositivesSD": hwNqaJitterStatsNumOfPositivesSD,
       "hwNqaJitterStatsSumOfPositivesSD": hwNqaJitterStatsSumOfPositivesSD,
       "hwNqaJitterStatsSum2PositivesSD": hwNqaJitterStatsSum2PositivesSD,
       "hwNqaJitterStatsMinOfNegativesSD": hwNqaJitterStatsMinOfNegativesSD,
       "hwNqaJitterStatsMaxOfNegativesSD": hwNqaJitterStatsMaxOfNegativesSD,
       "hwNqaJitterStatsNumOfNegativesSD": hwNqaJitterStatsNumOfNegativesSD,
       "hwNqaJitterStatsSumOfNegativesSD": hwNqaJitterStatsSumOfNegativesSD,
       "hwNqaJitterStatsSum2NegativesSD": hwNqaJitterStatsSum2NegativesSD,
       "hwNqaJitterStatsMinOfPositivesDS": hwNqaJitterStatsMinOfPositivesDS,
       "hwNqaJitterStatsMaxOfPositivesDS": hwNqaJitterStatsMaxOfPositivesDS,
       "hwNqaJitterStatsNumOfPositivesDS": hwNqaJitterStatsNumOfPositivesDS,
       "hwNqaJitterStatsSumOfPositivesDS": hwNqaJitterStatsSumOfPositivesDS,
       "hwNqaJitterStatsSum2PositivesDS": hwNqaJitterStatsSum2PositivesDS,
       "hwNqaJitterStatsMinOfNegativesDS": hwNqaJitterStatsMinOfNegativesDS,
       "hwNqaJitterStatsMaxOfNegativesDS": hwNqaJitterStatsMaxOfNegativesDS,
       "hwNqaJitterStatsNumOfNegativesDS": hwNqaJitterStatsNumOfNegativesDS,
       "hwNqaJitterStatsSumOfNegativesDS": hwNqaJitterStatsSumOfNegativesDS,
       "hwNqaJitterStatsSum2NegativesDS": hwNqaJitterStatsSum2NegativesDS,
       "hwNqaJitterStatsPacketLossSD": hwNqaJitterStatsPacketLossSD,
       "hwNqaJitterStatsPacketLossDS": hwNqaJitterStatsPacketLossDS,
       "hwNqaJitterStatsAvePositivesSD": hwNqaJitterStatsAvePositivesSD,
       "hwNqaJitterStatsAveNegativesSD": hwNqaJitterStatsAveNegativesSD,
       "hwNqaJitterStatsAvePositivesDS": hwNqaJitterStatsAvePositivesDS,
       "hwNqaJitterStatsAveNegativesDS": hwNqaJitterStatsAveNegativesDS,
       "hwNqaJitterStatsPktLossUnknown": hwNqaJitterStatsPktLossUnknown,
       "hwNqaJitterStatsOperOfICPIF": hwNqaJitterStatsOperOfICPIF,
       "hwNqaJitterStatsOperOfMOS": hwNqaJitterStatsOperOfMOS,
       "hwNqaAgentEnable": hwNqaAgentEnable,
       "hwNqaTcpServerTable": hwNqaTcpServerTable,
       "hwNqaTcpServerEntry": hwNqaTcpServerEntry,
       "hwNqaTcpServerIpAddress": hwNqaTcpServerIpAddress,
       "hwNqaTcpServerPort": hwNqaTcpServerPort,
       "hwNqaTcpServerRowStatus": hwNqaTcpServerRowStatus,
       "hwNqaUdpServerTable": hwNqaUdpServerTable,
       "hwNqaUdpServerEntry": hwNqaUdpServerEntry,
       "hwNqaUdpServerIpAddress": hwNqaUdpServerIpAddress,
       "hwNqaUdpServerPort": hwNqaUdpServerPort,
       "hwNqaUdpServerRowStatus": hwNqaUdpServerRowStatus,
       "hwNqaServerEnable": hwNqaServerEnable,
       "hwNqaStatsMaxGroupNumber": hwNqaStatsMaxGroupNumber,
       "hwNqaStatisticsCtlTable": hwNqaStatisticsCtlTable,
       "hwNqaStatisticsCtlEntry": hwNqaStatisticsCtlEntry,
       "hwNqaCtlStatisticsInterval": hwNqaCtlStatisticsInterval,
       "hwNqaCtlStatisticsGroupNumber": hwNqaCtlStatisticsGroupNumber,
       "hwNqaCtlStatisticsKeptTime": hwNqaCtlStatisticsKeptTime,
       "hwNqaCtlBeginTime": hwNqaCtlBeginTime,
       "hwNqaCtlLifeTime": hwNqaCtlLifeTime,
       "hwNqaStatisticsResultsTable": hwNqaStatisticsResultsTable,
       "hwNqaStatisticsResultsEntry": hwNqaStatisticsResultsEntry,
       "hwNqaStatResIndex": hwNqaStatResIndex,
       "hwNqaStatResIpTargetAddressType": hwNqaStatResIpTargetAddressType,
       "hwNqaStatResIpTargetAddress": hwNqaStatResIpTargetAddress,
       "hwNqaStatResMinRtt": hwNqaStatResMinRtt,
       "hwNqaStatResMaxRtt": hwNqaStatResMaxRtt,
       "hwNqaStatResAverageRtt": hwNqaStatResAverageRtt,
       "hwNqaStatResProbeResponses": hwNqaStatResProbeResponses,
       "hwNqaStatResSentProbes": hwNqaStatResSentProbes,
       "hwNqaStatResRttSumOfSquares": hwNqaStatResRttSumOfSquares,
       "hwNqaStatResStartTime": hwNqaStatResStartTime,
       "hwNqaStatResInterval": hwNqaStatResInterval,
       "hwNqaStatResRttNumDisconnects": hwNqaStatResRttNumDisconnects,
       "hwNqaStatResRttTimeouts": hwNqaStatResRttTimeouts,
       "hwNqaStatResRttBusies": hwNqaStatResRttBusies,
       "hwNqaStatResRttNoConnections": hwNqaStatResRttNoConnections,
       "hwNqaStatResRttDrops": hwNqaStatResRttDrops,
       "hwNqaStatResRttSequenceErrors": hwNqaStatResRttSequenceErrors,
       "hwNqaStatResRttErrors": hwNqaStatResRttErrors,
       "hwNqaStatResLostPacketRatio": hwNqaStatResLostPacketRatio,
       "hwNqaStatResPacketLateArrival": hwNqaStatResPacketLateArrival,
       "hwNqaStatResRttSum": hwNqaStatResRttSum,
       "hwNqaStatResNumOfDelaySD": hwNqaStatResNumOfDelaySD,
       "hwNqaStatResMinDelaySD": hwNqaStatResMinDelaySD,
       "hwNqaStatResMaxDelaySD": hwNqaStatResMaxDelaySD,
       "hwNqaStatResSumDelaySD": hwNqaStatResSumDelaySD,
       "hwNqaStatResSum2DelaySD": hwNqaStatResSum2DelaySD,
       "hwNqaStatResNumOfDelayDS": hwNqaStatResNumOfDelayDS,
       "hwNqaStatResMinDelayDS": hwNqaStatResMinDelayDS,
       "hwNqaStatResMaxDelayDS": hwNqaStatResMaxDelayDS,
       "hwNqaStatResSumDelayDS": hwNqaStatResSumDelayDS,
       "hwNqaStatResSum2DelayDS": hwNqaStatResSum2DelayDS,
       "hwNqaGroupStatsJitterTable": hwNqaGroupStatsJitterTable,
       "hwNqaGroupStatsJitterEntry": hwNqaGroupStatsJitterEntry,
       "hwNqaStatJitterIndex": hwNqaStatJitterIndex,
       "hwNqaStatJitterMinOfPosSD": hwNqaStatJitterMinOfPosSD,
       "hwNqaStatJitterMaxOfPosSD": hwNqaStatJitterMaxOfPosSD,
       "hwNqaStatJitterNumOfPosSD": hwNqaStatJitterNumOfPosSD,
       "hwNqaStatJitterSumOfPosSD": hwNqaStatJitterSumOfPosSD,
       "hwNqaStatJitterSumOfSquarePosSD": hwNqaStatJitterSumOfSquarePosSD,
       "hwNqaStatJitterMinOfNegSD": hwNqaStatJitterMinOfNegSD,
       "hwNqaStatJitterMaxOfNegSD": hwNqaStatJitterMaxOfNegSD,
       "hwNqaStatJitterNumOfNegSD": hwNqaStatJitterNumOfNegSD,
       "hwNqaStatJitterSumOfNegSD": hwNqaStatJitterSumOfNegSD,
       "hwNqaStatJitterSumOfSquareNegSD": hwNqaStatJitterSumOfSquareNegSD,
       "hwNqaStatJitterMinOfPosDS": hwNqaStatJitterMinOfPosDS,
       "hwNqaStatJitterMaxOfPosDS": hwNqaStatJitterMaxOfPosDS,
       "hwNqaStatJitterNumOfPosDS": hwNqaStatJitterNumOfPosDS,
       "hwNqaStatJitterSumOfPosDS": hwNqaStatJitterSumOfPosDS,
       "hwNqaStatJitterSumOfSquarePosDS": hwNqaStatJitterSumOfSquarePosDS,
       "hwNqaStatJitterMinOfNegDS": hwNqaStatJitterMinOfNegDS,
       "hwNqaStatJitterMaxOfNegDS": hwNqaStatJitterMaxOfNegDS,
       "hwNqaStatJitterNumOfNegDS": hwNqaStatJitterNumOfNegDS,
       "hwNqaStatJitterSumOfNegDS": hwNqaStatJitterSumOfNegDS,
       "hwNqaStatJitterSumOfSquareNegDS": hwNqaStatJitterSumOfSquareNegDS,
       "hwNqaStatJitterPacketLossSD": hwNqaStatJitterPacketLossSD,
       "hwNqaStatJitterPacketLossDS": hwNqaStatJitterPacketLossDS,
       "hwNqaStatJitterAvePosSD": hwNqaStatJitterAvePosSD,
       "hwNqaStatJitterAveNegSD": hwNqaStatJitterAveNegSD,
       "hwNqaStatJitterAvePosDS": hwNqaStatJitterAvePosDS,
       "hwNqaStatJitterAveNegDS": hwNqaStatJitterAveNegDS,
       "hwNqaStatJitterPktLossUnknown": hwNqaStatJitterPktLossUnknown,
       "hwNqaStatJitterMaxOfICPIF": hwNqaStatJitterMaxOfICPIF,
       "hwNqaStatJitterMinOfICPIF": hwNqaStatJitterMinOfICPIF,
       "hwNqaStatJitterMaxOfMOS": hwNqaStatJitterMaxOfMOS,
       "hwNqaStatJitterMinOfMOS": hwNqaStatJitterMinOfMOS,
       "hwNqaReactionTable": hwNqaReactionTable,
       "hwNqaReactionEntry": hwNqaReactionEntry,
       "hwNqaReactOwnerIndex": hwNqaReactOwnerIndex,
       "hwNqaReactTestName": hwNqaReactTestName,
       "hwNqaReactItemIndex": hwNqaReactItemIndex,
       "hwNqaReactCheckedElement": hwNqaReactCheckedElement,
       "hwNqaReactThresholdUpperLimit": hwNqaReactThresholdUpperLimit,
       "hwNqaReactThresholdLowerLimit": hwNqaReactThresholdLowerLimit,
       "hwNqaReactThresholdType": hwNqaReactThresholdType,
       "hwNqaReactThresholdConsecNum": hwNqaReactThresholdConsecNum,
       "hwNqaReactThresholdAccumNum": hwNqaReactThresholdAccumNum,
       "hwNqaReactActionType": hwNqaReactActionType,
       "hwNqaReactCurrentStatus": hwNqaReactCurrentStatus,
       "hwNqaReactRowStatus": hwNqaReactRowStatus,
       "hwNqaReactCheckedNum": hwNqaReactCheckedNum,
       "hwNqaReactThresholdNum": hwNqaReactThresholdNum,
       "hwNqaStatisticsReactionTable": hwNqaStatisticsReactionTable,
       "hwNqaStatisticsReactionEntry": hwNqaStatisticsReactionEntry,
       "hwNqaStatReactOwnerIndex": hwNqaStatReactOwnerIndex,
       "hwNqaStatReactTestName": hwNqaStatReactTestName,
       "hwNqaStatReactIndex": hwNqaStatReactIndex,
       "hwNqaStatReactItemIndex": hwNqaStatReactItemIndex,
       "hwNqaStatReactCheckedNum": hwNqaStatReactCheckedNum,
       "hwNqaStatReactThresholdNum": hwNqaStatReactThresholdNum,
       "hwNqaImplementationTypeDomains": hwNqaImplementationTypeDomains,
       "hwNqaUdpEcho": hwNqaUdpEcho,
       "hwNqaTcpconnect": hwNqaTcpconnect,
       "hwNqajitter": hwNqajitter,
       "hwNqaHttp": hwNqaHttp,
       "hwNqadlsw": hwNqadlsw,
       "hwNqadhcp": hwNqadhcp,
       "hwNqaftp": hwNqaftp,
       "hwNqaNotifications": hwNqaNotifications,
       "hwNqaProbeTimeOverThreshold": hwNqaProbeTimeOverThreshold,
       "hwNqaJitterRTTOverThreshold": hwNqaJitterRTTOverThreshold,
       "hwNqaProbeFailure": hwNqaProbeFailure,
       "hwNqaJitterPacketLoss": hwNqaJitterPacketLoss,
       "hwNqaJitterSDOverThreshold": hwNqaJitterSDOverThreshold,
       "hwNqaJitterDSOverThreshold": hwNqaJitterDSOverThreshold,
       "hwNqaICPIFOverThreshold": hwNqaICPIFOverThreshold,
       "hwNqaMOSOverThreshold": hwNqaMOSOverThreshold}
)
