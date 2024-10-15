# SNMP MIB module (Nortel-MsCarrier-MscPassport-PppMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-PppMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:58 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 InterfaceIndex,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscPpp_ObjectIdentity = ObjectIdentity
mscPpp = _MscPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102)
)
_MscPppRowStatusTable_Object = MibTable
mscPppRowStatusTable = _MscPppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 1)
)
if mibBuilder.loadTexts:
    mscPppRowStatusTable.setStatus("mandatory")
_MscPppRowStatusEntry_Object = MibTableRow
mscPppRowStatusEntry = _MscPppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 1, 1)
)
mscPppRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
)
if mibBuilder.loadTexts:
    mscPppRowStatusEntry.setStatus("mandatory")
_MscPppRowStatus_Type = RowStatus
_MscPppRowStatus_Object = MibTableColumn
mscPppRowStatus = _MscPppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 1, 1, 1),
    _MscPppRowStatus_Type()
)
mscPppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppRowStatus.setStatus("mandatory")
_MscPppComponentName_Type = DisplayString
_MscPppComponentName_Object = MibTableColumn
mscPppComponentName = _MscPppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 1, 1, 2),
    _MscPppComponentName_Type()
)
mscPppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppComponentName.setStatus("mandatory")
_MscPppStorageType_Type = StorageType
_MscPppStorageType_Object = MibTableColumn
mscPppStorageType = _MscPppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 1, 1, 4),
    _MscPppStorageType_Type()
)
mscPppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppStorageType.setStatus("mandatory")


class _MscPppIndex_Type(Integer32):
    """Custom type mscPppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscPppIndex_Type.__name__ = "Integer32"
_MscPppIndex_Object = MibTableColumn
mscPppIndex = _MscPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 1, 1, 10),
    _MscPppIndex_Type()
)
mscPppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppIndex.setStatus("mandatory")
_MscPppLnk_ObjectIdentity = ObjectIdentity
mscPppLnk = _MscPppLnk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2)
)
_MscPppLnkRowStatusTable_Object = MibTable
mscPppLnkRowStatusTable = _MscPppLnkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 1)
)
if mibBuilder.loadTexts:
    mscPppLnkRowStatusTable.setStatus("mandatory")
_MscPppLnkRowStatusEntry_Object = MibTableRow
mscPppLnkRowStatusEntry = _MscPppLnkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 1, 1)
)
mscPppLnkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLnkIndex"),
)
if mibBuilder.loadTexts:
    mscPppLnkRowStatusEntry.setStatus("mandatory")
_MscPppLnkRowStatus_Type = RowStatus
_MscPppLnkRowStatus_Object = MibTableColumn
mscPppLnkRowStatus = _MscPppLnkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 1, 1, 1),
    _MscPppLnkRowStatus_Type()
)
mscPppLnkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkRowStatus.setStatus("mandatory")
_MscPppLnkComponentName_Type = DisplayString
_MscPppLnkComponentName_Object = MibTableColumn
mscPppLnkComponentName = _MscPppLnkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 1, 1, 2),
    _MscPppLnkComponentName_Type()
)
mscPppLnkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkComponentName.setStatus("mandatory")
_MscPppLnkStorageType_Type = StorageType
_MscPppLnkStorageType_Object = MibTableColumn
mscPppLnkStorageType = _MscPppLnkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 1, 1, 4),
    _MscPppLnkStorageType_Type()
)
mscPppLnkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkStorageType.setStatus("mandatory")
_MscPppLnkIndex_Type = NonReplicated
_MscPppLnkIndex_Object = MibTableColumn
mscPppLnkIndex = _MscPppLnkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 1, 1, 10),
    _MscPppLnkIndex_Type()
)
mscPppLnkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppLnkIndex.setStatus("mandatory")
_MscPppLnkProvTable_Object = MibTable
mscPppLnkProvTable = _MscPppLnkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10)
)
if mibBuilder.loadTexts:
    mscPppLnkProvTable.setStatus("mandatory")
_MscPppLnkProvEntry_Object = MibTableRow
mscPppLnkProvEntry = _MscPppLnkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1)
)
mscPppLnkProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLnkIndex"),
)
if mibBuilder.loadTexts:
    mscPppLnkProvEntry.setStatus("mandatory")


class _MscPppLnkConfigInitialMru_Type(Unsigned32):
    """Custom type mscPppLnkConfigInitialMru based on Unsigned32"""
    defaultValue = 18000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 18000),
    )


_MscPppLnkConfigInitialMru_Type.__name__ = "Unsigned32"
_MscPppLnkConfigInitialMru_Object = MibTableColumn
mscPppLnkConfigInitialMru = _MscPppLnkConfigInitialMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 1),
    _MscPppLnkConfigInitialMru_Type()
)
mscPppLnkConfigInitialMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkConfigInitialMru.setStatus("mandatory")


class _MscPppLnkConfigMagicNumber_Type(Integer32):
    """Custom type mscPppLnkConfigMagicNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppLnkConfigMagicNumber_Type.__name__ = "Integer32"
_MscPppLnkConfigMagicNumber_Object = MibTableColumn
mscPppLnkConfigMagicNumber = _MscPppLnkConfigMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 4),
    _MscPppLnkConfigMagicNumber_Type()
)
mscPppLnkConfigMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkConfigMagicNumber.setStatus("mandatory")


class _MscPppLnkRestartTimer_Type(Unsigned32):
    """Custom type mscPppLnkRestartTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_MscPppLnkRestartTimer_Type.__name__ = "Unsigned32"
_MscPppLnkRestartTimer_Object = MibTableColumn
mscPppLnkRestartTimer = _MscPppLnkRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 6),
    _MscPppLnkRestartTimer_Type()
)
mscPppLnkRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkRestartTimer.setStatus("mandatory")


class _MscPppLnkContinuityMonitor_Type(Integer32):
    """Custom type mscPppLnkContinuityMonitor based on Integer32"""
    defaultValue = 1

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


_MscPppLnkContinuityMonitor_Type.__name__ = "Integer32"
_MscPppLnkContinuityMonitor_Object = MibTableColumn
mscPppLnkContinuityMonitor = _MscPppLnkContinuityMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 7),
    _MscPppLnkContinuityMonitor_Type()
)
mscPppLnkContinuityMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkContinuityMonitor.setStatus("mandatory")


class _MscPppLnkNegativeAckTries_Type(Unsigned32):
    """Custom type mscPppLnkNegativeAckTries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLnkNegativeAckTries_Type.__name__ = "Unsigned32"
_MscPppLnkNegativeAckTries_Object = MibTableColumn
mscPppLnkNegativeAckTries = _MscPppLnkNegativeAckTries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 8),
    _MscPppLnkNegativeAckTries_Type()
)
mscPppLnkNegativeAckTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkNegativeAckTries.setStatus("mandatory")


class _MscPppLnkQualityThreshold_Type(Unsigned32):
    """Custom type mscPppLnkQualityThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_MscPppLnkQualityThreshold_Type.__name__ = "Unsigned32"
_MscPppLnkQualityThreshold_Object = MibTableColumn
mscPppLnkQualityThreshold = _MscPppLnkQualityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 9),
    _MscPppLnkQualityThreshold_Type()
)
mscPppLnkQualityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkQualityThreshold.setStatus("mandatory")


class _MscPppLnkQualityWindow_Type(Unsigned32):
    """Custom type mscPppLnkQualityWindow based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400),
    )


_MscPppLnkQualityWindow_Type.__name__ = "Unsigned32"
_MscPppLnkQualityWindow_Object = MibTableColumn
mscPppLnkQualityWindow = _MscPppLnkQualityWindow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 10),
    _MscPppLnkQualityWindow_Type()
)
mscPppLnkQualityWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkQualityWindow.setStatus("mandatory")


class _MscPppLnkTerminateRequestTries_Type(Unsigned32):
    """Custom type mscPppLnkTerminateRequestTries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLnkTerminateRequestTries_Type.__name__ = "Unsigned32"
_MscPppLnkTerminateRequestTries_Object = MibTableColumn
mscPppLnkTerminateRequestTries = _MscPppLnkTerminateRequestTries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 11),
    _MscPppLnkTerminateRequestTries_Type()
)
mscPppLnkTerminateRequestTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkTerminateRequestTries.setStatus("mandatory")


class _MscPppLnkConfigureRequestTries_Type(Unsigned32):
    """Custom type mscPppLnkConfigureRequestTries based on Unsigned32"""
    defaultValue = 1000000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLnkConfigureRequestTries_Type.__name__ = "Unsigned32"
_MscPppLnkConfigureRequestTries_Object = MibTableColumn
mscPppLnkConfigureRequestTries = _MscPppLnkConfigureRequestTries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 10, 1, 12),
    _MscPppLnkConfigureRequestTries_Type()
)
mscPppLnkConfigureRequestTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLnkConfigureRequestTries.setStatus("mandatory")
_MscPppLnkOperTable_Object = MibTable
mscPppLnkOperTable = _MscPppLnkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11)
)
if mibBuilder.loadTexts:
    mscPppLnkOperTable.setStatus("mandatory")
_MscPppLnkOperEntry_Object = MibTableRow
mscPppLnkOperEntry = _MscPppLnkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1)
)
mscPppLnkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLnkIndex"),
)
if mibBuilder.loadTexts:
    mscPppLnkOperEntry.setStatus("mandatory")


class _MscPppLnkOperState_Type(Integer32):
    """Custom type mscPppLnkOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppLnkOperState_Type.__name__ = "Integer32"
_MscPppLnkOperState_Object = MibTableColumn
mscPppLnkOperState = _MscPppLnkOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 1),
    _MscPppLnkOperState_Type()
)
mscPppLnkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkOperState.setStatus("mandatory")


class _MscPppLnkLineCondition_Type(Integer32):
    """Custom type mscPppLnkLineCondition based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("badLineCondition", 4),
          ("looped", 1),
          ("noClock", 3),
          ("ok", 0))
    )


_MscPppLnkLineCondition_Type.__name__ = "Integer32"
_MscPppLnkLineCondition_Object = MibTableColumn
mscPppLnkLineCondition = _MscPppLnkLineCondition_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 2),
    _MscPppLnkLineCondition_Type()
)
mscPppLnkLineCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkLineCondition.setStatus("mandatory")
_MscPppLnkBadAddresses_Type = Counter32
_MscPppLnkBadAddresses_Object = MibTableColumn
mscPppLnkBadAddresses = _MscPppLnkBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 4),
    _MscPppLnkBadAddresses_Type()
)
mscPppLnkBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkBadAddresses.setStatus("mandatory")
_MscPppLnkBadControls_Type = Counter32
_MscPppLnkBadControls_Object = MibTableColumn
mscPppLnkBadControls = _MscPppLnkBadControls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 5),
    _MscPppLnkBadControls_Type()
)
mscPppLnkBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkBadControls.setStatus("mandatory")
_MscPppLnkPacketTooLongs_Type = Counter32
_MscPppLnkPacketTooLongs_Object = MibTableColumn
mscPppLnkPacketTooLongs = _MscPppLnkPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 6),
    _MscPppLnkPacketTooLongs_Type()
)
mscPppLnkPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkPacketTooLongs.setStatus("mandatory")
_MscPppLnkBadFcss_Type = Counter32
_MscPppLnkBadFcss_Object = MibTableColumn
mscPppLnkBadFcss = _MscPppLnkBadFcss_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 7),
    _MscPppLnkBadFcss_Type()
)
mscPppLnkBadFcss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkBadFcss.setStatus("mandatory")


class _MscPppLnkLocalMru_Type(Unsigned32):
    """Custom type mscPppLnkLocalMru based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_MscPppLnkLocalMru_Type.__name__ = "Unsigned32"
_MscPppLnkLocalMru_Object = MibTableColumn
mscPppLnkLocalMru = _MscPppLnkLocalMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 8),
    _MscPppLnkLocalMru_Type()
)
mscPppLnkLocalMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkLocalMru.setStatus("mandatory")


class _MscPppLnkRemoteMru_Type(Unsigned32):
    """Custom type mscPppLnkRemoteMru based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_MscPppLnkRemoteMru_Type.__name__ = "Unsigned32"
_MscPppLnkRemoteMru_Object = MibTableColumn
mscPppLnkRemoteMru = _MscPppLnkRemoteMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 9),
    _MscPppLnkRemoteMru_Type()
)
mscPppLnkRemoteMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkRemoteMru.setStatus("mandatory")


class _MscPppLnkTransmitFcsSize_Type(Unsigned32):
    """Custom type mscPppLnkTransmitFcsSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscPppLnkTransmitFcsSize_Type.__name__ = "Unsigned32"
_MscPppLnkTransmitFcsSize_Object = MibTableColumn
mscPppLnkTransmitFcsSize = _MscPppLnkTransmitFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 16),
    _MscPppLnkTransmitFcsSize_Type()
)
mscPppLnkTransmitFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkTransmitFcsSize.setStatus("mandatory")


class _MscPppLnkReceiveFcsSize_Type(Unsigned32):
    """Custom type mscPppLnkReceiveFcsSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MscPppLnkReceiveFcsSize_Type.__name__ = "Unsigned32"
_MscPppLnkReceiveFcsSize_Object = MibTableColumn
mscPppLnkReceiveFcsSize = _MscPppLnkReceiveFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 2, 11, 1, 17),
    _MscPppLnkReceiveFcsSize_Type()
)
mscPppLnkReceiveFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLnkReceiveFcsSize.setStatus("mandatory")
_MscPppLqm_ObjectIdentity = ObjectIdentity
mscPppLqm = _MscPppLqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3)
)
_MscPppLqmRowStatusTable_Object = MibTable
mscPppLqmRowStatusTable = _MscPppLqmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 1)
)
if mibBuilder.loadTexts:
    mscPppLqmRowStatusTable.setStatus("mandatory")
_MscPppLqmRowStatusEntry_Object = MibTableRow
mscPppLqmRowStatusEntry = _MscPppLqmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 1, 1)
)
mscPppLqmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLqmIndex"),
)
if mibBuilder.loadTexts:
    mscPppLqmRowStatusEntry.setStatus("mandatory")
_MscPppLqmRowStatus_Type = RowStatus
_MscPppLqmRowStatus_Object = MibTableColumn
mscPppLqmRowStatus = _MscPppLqmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 1, 1, 1),
    _MscPppLqmRowStatus_Type()
)
mscPppLqmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmRowStatus.setStatus("mandatory")
_MscPppLqmComponentName_Type = DisplayString
_MscPppLqmComponentName_Object = MibTableColumn
mscPppLqmComponentName = _MscPppLqmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 1, 1, 2),
    _MscPppLqmComponentName_Type()
)
mscPppLqmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmComponentName.setStatus("mandatory")
_MscPppLqmStorageType_Type = StorageType
_MscPppLqmStorageType_Object = MibTableColumn
mscPppLqmStorageType = _MscPppLqmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 1, 1, 4),
    _MscPppLqmStorageType_Type()
)
mscPppLqmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmStorageType.setStatus("mandatory")
_MscPppLqmIndex_Type = NonReplicated
_MscPppLqmIndex_Object = MibTableColumn
mscPppLqmIndex = _MscPppLqmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 1, 1, 10),
    _MscPppLqmIndex_Type()
)
mscPppLqmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppLqmIndex.setStatus("mandatory")
_MscPppLqmProvTable_Object = MibTable
mscPppLqmProvTable = _MscPppLqmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 10)
)
if mibBuilder.loadTexts:
    mscPppLqmProvTable.setStatus("mandatory")
_MscPppLqmProvEntry_Object = MibTableRow
mscPppLqmProvEntry = _MscPppLqmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 10, 1)
)
mscPppLqmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLqmIndex"),
)
if mibBuilder.loadTexts:
    mscPppLqmProvEntry.setStatus("mandatory")


class _MscPppLqmConfigPeriod_Type(Unsigned32):
    """Custom type mscPppLqmConfigPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MscPppLqmConfigPeriod_Type.__name__ = "Unsigned32"
_MscPppLqmConfigPeriod_Object = MibTableColumn
mscPppLqmConfigPeriod = _MscPppLqmConfigPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 10, 1, 1),
    _MscPppLqmConfigPeriod_Type()
)
mscPppLqmConfigPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLqmConfigPeriod.setStatus("mandatory")


class _MscPppLqmConfigStatus_Type(Integer32):
    """Custom type mscPppLqmConfigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppLqmConfigStatus_Type.__name__ = "Integer32"
_MscPppLqmConfigStatus_Object = MibTableColumn
mscPppLqmConfigStatus = _MscPppLqmConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 10, 1, 2),
    _MscPppLqmConfigStatus_Type()
)
mscPppLqmConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLqmConfigStatus.setStatus("mandatory")
_MscPppLqmOperTable_Object = MibTable
mscPppLqmOperTable = _MscPppLqmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11)
)
if mibBuilder.loadTexts:
    mscPppLqmOperTable.setStatus("mandatory")
_MscPppLqmOperEntry_Object = MibTableRow
mscPppLqmOperEntry = _MscPppLqmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1)
)
mscPppLqmOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLqmIndex"),
)
if mibBuilder.loadTexts:
    mscPppLqmOperEntry.setStatus("mandatory")


class _MscPppLqmQuality_Type(Integer32):
    """Custom type mscPppLqmQuality based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("notDetermined", 3))
    )


_MscPppLqmQuality_Type.__name__ = "Integer32"
_MscPppLqmQuality_Object = MibTableColumn
mscPppLqmQuality = _MscPppLqmQuality_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1, 1),
    _MscPppLqmQuality_Type()
)
mscPppLqmQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmQuality.setStatus("mandatory")
_MscPppLqmInGoodOctets_Type = Counter32
_MscPppLqmInGoodOctets_Object = MibTableColumn
mscPppLqmInGoodOctets = _MscPppLqmInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1, 2),
    _MscPppLqmInGoodOctets_Type()
)
mscPppLqmInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmInGoodOctets.setStatus("mandatory")


class _MscPppLqmLocalPeriod_Type(Unsigned32):
    """Custom type mscPppLqmLocalPeriod based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MscPppLqmLocalPeriod_Type.__name__ = "Unsigned32"
_MscPppLqmLocalPeriod_Object = MibTableColumn
mscPppLqmLocalPeriod = _MscPppLqmLocalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1, 3),
    _MscPppLqmLocalPeriod_Type()
)
mscPppLqmLocalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmLocalPeriod.setStatus("mandatory")


class _MscPppLqmRemotePeriod_Type(Unsigned32):
    """Custom type mscPppLqmRemotePeriod based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MscPppLqmRemotePeriod_Type.__name__ = "Unsigned32"
_MscPppLqmRemotePeriod_Object = MibTableColumn
mscPppLqmRemotePeriod = _MscPppLqmRemotePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1, 4),
    _MscPppLqmRemotePeriod_Type()
)
mscPppLqmRemotePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmRemotePeriod.setStatus("mandatory")
_MscPppLqmOutLqrs_Type = Counter32
_MscPppLqmOutLqrs_Object = MibTableColumn
mscPppLqmOutLqrs = _MscPppLqmOutLqrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1, 5),
    _MscPppLqmOutLqrs_Type()
)
mscPppLqmOutLqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmOutLqrs.setStatus("mandatory")
_MscPppLqmInLqrs_Type = Counter32
_MscPppLqmInLqrs_Object = MibTableColumn
mscPppLqmInLqrs = _MscPppLqmInLqrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 3, 11, 1, 6),
    _MscPppLqmInLqrs_Type()
)
mscPppLqmInLqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLqmInLqrs.setStatus("mandatory")
_MscPppNcp_ObjectIdentity = ObjectIdentity
mscPppNcp = _MscPppNcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4)
)
_MscPppNcpRowStatusTable_Object = MibTable
mscPppNcpRowStatusTable = _MscPppNcpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 1)
)
if mibBuilder.loadTexts:
    mscPppNcpRowStatusTable.setStatus("mandatory")
_MscPppNcpRowStatusEntry_Object = MibTableRow
mscPppNcpRowStatusEntry = _MscPppNcpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 1, 1)
)
mscPppNcpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpRowStatusEntry.setStatus("mandatory")
_MscPppNcpRowStatus_Type = RowStatus
_MscPppNcpRowStatus_Object = MibTableColumn
mscPppNcpRowStatus = _MscPppNcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 1, 1, 1),
    _MscPppNcpRowStatus_Type()
)
mscPppNcpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpRowStatus.setStatus("mandatory")
_MscPppNcpComponentName_Type = DisplayString
_MscPppNcpComponentName_Object = MibTableColumn
mscPppNcpComponentName = _MscPppNcpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 1, 1, 2),
    _MscPppNcpComponentName_Type()
)
mscPppNcpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpComponentName.setStatus("mandatory")
_MscPppNcpStorageType_Type = StorageType
_MscPppNcpStorageType_Object = MibTableColumn
mscPppNcpStorageType = _MscPppNcpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 1, 1, 4),
    _MscPppNcpStorageType_Type()
)
mscPppNcpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpStorageType.setStatus("mandatory")
_MscPppNcpIndex_Type = NonReplicated
_MscPppNcpIndex_Object = MibTableColumn
mscPppNcpIndex = _MscPppNcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 1, 1, 10),
    _MscPppNcpIndex_Type()
)
mscPppNcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppNcpIndex.setStatus("mandatory")
_MscPppNcpBmcEntry_ObjectIdentity = ObjectIdentity
mscPppNcpBmcEntry = _MscPppNcpBmcEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2)
)
_MscPppNcpBmcEntryRowStatusTable_Object = MibTable
mscPppNcpBmcEntryRowStatusTable = _MscPppNcpBmcEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryRowStatusTable.setStatus("mandatory")
_MscPppNcpBmcEntryRowStatusEntry_Object = MibTableRow
mscPppNcpBmcEntryRowStatusEntry = _MscPppNcpBmcEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 1, 1)
)
mscPppNcpBmcEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpBmcEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryRowStatusEntry.setStatus("mandatory")
_MscPppNcpBmcEntryRowStatus_Type = RowStatus
_MscPppNcpBmcEntryRowStatus_Object = MibTableColumn
mscPppNcpBmcEntryRowStatus = _MscPppNcpBmcEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 1, 1, 1),
    _MscPppNcpBmcEntryRowStatus_Type()
)
mscPppNcpBmcEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryRowStatus.setStatus("mandatory")
_MscPppNcpBmcEntryComponentName_Type = DisplayString
_MscPppNcpBmcEntryComponentName_Object = MibTableColumn
mscPppNcpBmcEntryComponentName = _MscPppNcpBmcEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 1, 1, 2),
    _MscPppNcpBmcEntryComponentName_Type()
)
mscPppNcpBmcEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryComponentName.setStatus("mandatory")
_MscPppNcpBmcEntryStorageType_Type = StorageType
_MscPppNcpBmcEntryStorageType_Object = MibTableColumn
mscPppNcpBmcEntryStorageType = _MscPppNcpBmcEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 1, 1, 4),
    _MscPppNcpBmcEntryStorageType_Type()
)
mscPppNcpBmcEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryStorageType.setStatus("mandatory")


class _MscPppNcpBmcEntryMacTypeIndex_Type(Integer32):
    """Custom type mscPppNcpBmcEntryMacTypeIndex based on Integer32"""
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
        *(("ethernet", 1),
          ("fddi", 4),
          ("tokenBus", 2),
          ("tokenRing", 3))
    )


_MscPppNcpBmcEntryMacTypeIndex_Type.__name__ = "Integer32"
_MscPppNcpBmcEntryMacTypeIndex_Object = MibTableColumn
mscPppNcpBmcEntryMacTypeIndex = _MscPppNcpBmcEntryMacTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 1, 1, 10),
    _MscPppNcpBmcEntryMacTypeIndex_Type()
)
mscPppNcpBmcEntryMacTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryMacTypeIndex.setStatus("mandatory")
_MscPppNcpBmcEntryProvTable_Object = MibTable
mscPppNcpBmcEntryProvTable = _MscPppNcpBmcEntryProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryProvTable.setStatus("mandatory")
_MscPppNcpBmcEntryProvEntry_Object = MibTableRow
mscPppNcpBmcEntryProvEntry = _MscPppNcpBmcEntryProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 10, 1)
)
mscPppNcpBmcEntryProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpBmcEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryProvEntry.setStatus("mandatory")


class _MscPppNcpBmcEntryLocalStatus_Type(Integer32):
    """Custom type mscPppNcpBmcEntryLocalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("accept", 1)
    )


_MscPppNcpBmcEntryLocalStatus_Type.__name__ = "Integer32"
_MscPppNcpBmcEntryLocalStatus_Object = MibTableColumn
mscPppNcpBmcEntryLocalStatus = _MscPppNcpBmcEntryLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 2, 10, 1, 1),
    _MscPppNcpBmcEntryLocalStatus_Type()
)
mscPppNcpBmcEntryLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppNcpBmcEntryLocalStatus.setStatus("mandatory")
_MscPppNcpBmEntry_ObjectIdentity = ObjectIdentity
mscPppNcpBmEntry = _MscPppNcpBmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3)
)
_MscPppNcpBmEntryRowStatusTable_Object = MibTable
mscPppNcpBmEntryRowStatusTable = _MscPppNcpBmEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscPppNcpBmEntryRowStatusTable.setStatus("mandatory")
_MscPppNcpBmEntryRowStatusEntry_Object = MibTableRow
mscPppNcpBmEntryRowStatusEntry = _MscPppNcpBmEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 1, 1)
)
mscPppNcpBmEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpBmEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpBmEntryRowStatusEntry.setStatus("mandatory")
_MscPppNcpBmEntryRowStatus_Type = RowStatus
_MscPppNcpBmEntryRowStatus_Object = MibTableColumn
mscPppNcpBmEntryRowStatus = _MscPppNcpBmEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 1, 1, 1),
    _MscPppNcpBmEntryRowStatus_Type()
)
mscPppNcpBmEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmEntryRowStatus.setStatus("mandatory")
_MscPppNcpBmEntryComponentName_Type = DisplayString
_MscPppNcpBmEntryComponentName_Object = MibTableColumn
mscPppNcpBmEntryComponentName = _MscPppNcpBmEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 1, 1, 2),
    _MscPppNcpBmEntryComponentName_Type()
)
mscPppNcpBmEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmEntryComponentName.setStatus("mandatory")
_MscPppNcpBmEntryStorageType_Type = StorageType
_MscPppNcpBmEntryStorageType_Object = MibTableColumn
mscPppNcpBmEntryStorageType = _MscPppNcpBmEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 1, 1, 4),
    _MscPppNcpBmEntryStorageType_Type()
)
mscPppNcpBmEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmEntryStorageType.setStatus("mandatory")


class _MscPppNcpBmEntryMacTypeIndex_Type(Integer32):
    """Custom type mscPppNcpBmEntryMacTypeIndex based on Integer32"""
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
        *(("ethernet", 1),
          ("fddi", 4),
          ("tokenBus", 2),
          ("tokenRing", 3))
    )


_MscPppNcpBmEntryMacTypeIndex_Type.__name__ = "Integer32"
_MscPppNcpBmEntryMacTypeIndex_Object = MibTableColumn
mscPppNcpBmEntryMacTypeIndex = _MscPppNcpBmEntryMacTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 1, 1, 10),
    _MscPppNcpBmEntryMacTypeIndex_Type()
)
mscPppNcpBmEntryMacTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppNcpBmEntryMacTypeIndex.setStatus("mandatory")
_MscPppNcpBmEntryOperTable_Object = MibTable
mscPppNcpBmEntryOperTable = _MscPppNcpBmEntryOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscPppNcpBmEntryOperTable.setStatus("mandatory")
_MscPppNcpBmEntryOperEntry_Object = MibTableRow
mscPppNcpBmEntryOperEntry = _MscPppNcpBmEntryOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 10, 1)
)
mscPppNcpBmEntryOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpBmEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpBmEntryOperEntry.setStatus("mandatory")


class _MscPppNcpBmEntryLocalStatus_Type(Integer32):
    """Custom type mscPppNcpBmEntryLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dontAccept", 2))
    )


_MscPppNcpBmEntryLocalStatus_Type.__name__ = "Integer32"
_MscPppNcpBmEntryLocalStatus_Object = MibTableColumn
mscPppNcpBmEntryLocalStatus = _MscPppNcpBmEntryLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 10, 1, 2),
    _MscPppNcpBmEntryLocalStatus_Type()
)
mscPppNcpBmEntryLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmEntryLocalStatus.setStatus("mandatory")


class _MscPppNcpBmEntryRemoteStatus_Type(Integer32):
    """Custom type mscPppNcpBmEntryRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dontAccept", 2))
    )


_MscPppNcpBmEntryRemoteStatus_Type.__name__ = "Integer32"
_MscPppNcpBmEntryRemoteStatus_Object = MibTableColumn
mscPppNcpBmEntryRemoteStatus = _MscPppNcpBmEntryRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 3, 10, 1, 3),
    _MscPppNcpBmEntryRemoteStatus_Type()
)
mscPppNcpBmEntryRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBmEntryRemoteStatus.setStatus("mandatory")
_MscPppNcpBprovTable_Object = MibTable
mscPppNcpBprovTable = _MscPppNcpBprovTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 11)
)
if mibBuilder.loadTexts:
    mscPppNcpBprovTable.setStatus("mandatory")
_MscPppNcpBprovEntry_Object = MibTableRow
mscPppNcpBprovEntry = _MscPppNcpBprovEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 11, 1)
)
mscPppNcpBprovEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpBprovEntry.setStatus("mandatory")


class _MscPppNcpBConfigTinygram_Type(Integer32):
    """Custom type mscPppNcpBConfigTinygram based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppNcpBConfigTinygram_Type.__name__ = "Integer32"
_MscPppNcpBConfigTinygram_Object = MibTableColumn
mscPppNcpBConfigTinygram = _MscPppNcpBConfigTinygram_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 11, 1, 1),
    _MscPppNcpBConfigTinygram_Type()
)
mscPppNcpBConfigTinygram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppNcpBConfigTinygram.setStatus("mandatory")


class _MscPppNcpBConfigLanId_Type(Integer32):
    """Custom type mscPppNcpBConfigLanId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppNcpBConfigLanId_Type.__name__ = "Integer32"
_MscPppNcpBConfigLanId_Object = MibTableColumn
mscPppNcpBConfigLanId = _MscPppNcpBConfigLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 11, 1, 4),
    _MscPppNcpBConfigLanId_Type()
)
mscPppNcpBConfigLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppNcpBConfigLanId.setStatus("mandatory")
_MscPppNcpIpOperTable_Object = MibTable
mscPppNcpIpOperTable = _MscPppNcpIpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 12)
)
if mibBuilder.loadTexts:
    mscPppNcpIpOperTable.setStatus("mandatory")
_MscPppNcpIpOperEntry_Object = MibTableRow
mscPppNcpIpOperEntry = _MscPppNcpIpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 12, 1)
)
mscPppNcpIpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpIpOperEntry.setStatus("mandatory")


class _MscPppNcpIpOperState_Type(Integer32):
    """Custom type mscPppNcpIpOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppNcpIpOperState_Type.__name__ = "Integer32"
_MscPppNcpIpOperState_Object = MibTableColumn
mscPppNcpIpOperState = _MscPppNcpIpOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 12, 1, 1),
    _MscPppNcpIpOperState_Type()
)
mscPppNcpIpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpIpOperState.setStatus("mandatory")
_MscPppNcpBoperTable_Object = MibTable
mscPppNcpBoperTable = _MscPppNcpBoperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14)
)
if mibBuilder.loadTexts:
    mscPppNcpBoperTable.setStatus("mandatory")
_MscPppNcpBoperEntry_Object = MibTableRow
mscPppNcpBoperEntry = _MscPppNcpBoperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14, 1)
)
mscPppNcpBoperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpBoperEntry.setStatus("mandatory")


class _MscPppNcpBOperState_Type(Integer32):
    """Custom type mscPppNcpBOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppNcpBOperState_Type.__name__ = "Integer32"
_MscPppNcpBOperState_Object = MibTableColumn
mscPppNcpBOperState = _MscPppNcpBOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14, 1, 1),
    _MscPppNcpBOperState_Type()
)
mscPppNcpBOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBOperState.setStatus("mandatory")


class _MscPppNcpBLocalToRemoteTinygramComp_Type(Integer32):
    """Custom type mscPppNcpBLocalToRemoteTinygramComp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppNcpBLocalToRemoteTinygramComp_Type.__name__ = "Integer32"
_MscPppNcpBLocalToRemoteTinygramComp_Object = MibTableColumn
mscPppNcpBLocalToRemoteTinygramComp = _MscPppNcpBLocalToRemoteTinygramComp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14, 1, 3),
    _MscPppNcpBLocalToRemoteTinygramComp_Type()
)
mscPppNcpBLocalToRemoteTinygramComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBLocalToRemoteTinygramComp.setStatus("mandatory")


class _MscPppNcpBRemoteToLocalTinygramComp_Type(Integer32):
    """Custom type mscPppNcpBRemoteToLocalTinygramComp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppNcpBRemoteToLocalTinygramComp_Type.__name__ = "Integer32"
_MscPppNcpBRemoteToLocalTinygramComp_Object = MibTableColumn
mscPppNcpBRemoteToLocalTinygramComp = _MscPppNcpBRemoteToLocalTinygramComp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14, 1, 4),
    _MscPppNcpBRemoteToLocalTinygramComp_Type()
)
mscPppNcpBRemoteToLocalTinygramComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBRemoteToLocalTinygramComp.setStatus("mandatory")


class _MscPppNcpBLocalToRemoteLanId_Type(Integer32):
    """Custom type mscPppNcpBLocalToRemoteLanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppNcpBLocalToRemoteLanId_Type.__name__ = "Integer32"
_MscPppNcpBLocalToRemoteLanId_Object = MibTableColumn
mscPppNcpBLocalToRemoteLanId = _MscPppNcpBLocalToRemoteLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14, 1, 5),
    _MscPppNcpBLocalToRemoteLanId_Type()
)
mscPppNcpBLocalToRemoteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBLocalToRemoteLanId.setStatus("mandatory")


class _MscPppNcpBRemoteToLocalLanId_Type(Integer32):
    """Custom type mscPppNcpBRemoteToLocalLanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MscPppNcpBRemoteToLocalLanId_Type.__name__ = "Integer32"
_MscPppNcpBRemoteToLocalLanId_Object = MibTableColumn
mscPppNcpBRemoteToLocalLanId = _MscPppNcpBRemoteToLocalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 14, 1, 6),
    _MscPppNcpBRemoteToLocalLanId_Type()
)
mscPppNcpBRemoteToLocalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpBRemoteToLocalLanId.setStatus("mandatory")
_MscPppNcpOperTable_Object = MibTable
mscPppNcpOperTable = _MscPppNcpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 16)
)
if mibBuilder.loadTexts:
    mscPppNcpOperTable.setStatus("mandatory")
_MscPppNcpOperEntry_Object = MibTableRow
mscPppNcpOperEntry = _MscPppNcpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 16, 1)
)
mscPppNcpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppNcpIndex"),
)
if mibBuilder.loadTexts:
    mscPppNcpOperEntry.setStatus("mandatory")


class _MscPppNcpAppletalkOperState_Type(Integer32):
    """Custom type mscPppNcpAppletalkOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppNcpAppletalkOperState_Type.__name__ = "Integer32"
_MscPppNcpAppletalkOperState_Object = MibTableColumn
mscPppNcpAppletalkOperState = _MscPppNcpAppletalkOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 16, 1, 1),
    _MscPppNcpAppletalkOperState_Type()
)
mscPppNcpAppletalkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpAppletalkOperState.setStatus("mandatory")


class _MscPppNcpIpxOperState_Type(Integer32):
    """Custom type mscPppNcpIpxOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppNcpIpxOperState_Type.__name__ = "Integer32"
_MscPppNcpIpxOperState_Object = MibTableColumn
mscPppNcpIpxOperState = _MscPppNcpIpxOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 16, 1, 2),
    _MscPppNcpIpxOperState_Type()
)
mscPppNcpIpxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpIpxOperState.setStatus("mandatory")


class _MscPppNcpXnsOperState_Type(Integer32):
    """Custom type mscPppNcpXnsOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppNcpXnsOperState_Type.__name__ = "Integer32"
_MscPppNcpXnsOperState_Object = MibTableColumn
mscPppNcpXnsOperState = _MscPppNcpXnsOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 16, 1, 3),
    _MscPppNcpXnsOperState_Type()
)
mscPppNcpXnsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpXnsOperState.setStatus("mandatory")


class _MscPppNcpDecnetOperState_Type(Integer32):
    """Custom type mscPppNcpDecnetOperState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ackrcvd", 7),
          ("acksent", 8),
          ("closed", 2),
          ("closing", 4),
          ("initial", 0),
          ("opened", 9),
          ("reqsent", 6),
          ("starting", 1),
          ("stopped", 3),
          ("stopping", 5))
    )


_MscPppNcpDecnetOperState_Type.__name__ = "Integer32"
_MscPppNcpDecnetOperState_Object = MibTableColumn
mscPppNcpDecnetOperState = _MscPppNcpDecnetOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 4, 16, 1, 4),
    _MscPppNcpDecnetOperState_Type()
)
mscPppNcpDecnetOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppNcpDecnetOperState.setStatus("mandatory")
_MscPppFramer_ObjectIdentity = ObjectIdentity
mscPppFramer = _MscPppFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5)
)
_MscPppFramerRowStatusTable_Object = MibTable
mscPppFramerRowStatusTable = _MscPppFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 1)
)
if mibBuilder.loadTexts:
    mscPppFramerRowStatusTable.setStatus("mandatory")
_MscPppFramerRowStatusEntry_Object = MibTableRow
mscPppFramerRowStatusEntry = _MscPppFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 1, 1)
)
mscPppFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppFramerIndex"),
)
if mibBuilder.loadTexts:
    mscPppFramerRowStatusEntry.setStatus("mandatory")
_MscPppFramerRowStatus_Type = RowStatus
_MscPppFramerRowStatus_Object = MibTableColumn
mscPppFramerRowStatus = _MscPppFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 1, 1, 1),
    _MscPppFramerRowStatus_Type()
)
mscPppFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerRowStatus.setStatus("mandatory")
_MscPppFramerComponentName_Type = DisplayString
_MscPppFramerComponentName_Object = MibTableColumn
mscPppFramerComponentName = _MscPppFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 1, 1, 2),
    _MscPppFramerComponentName_Type()
)
mscPppFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerComponentName.setStatus("mandatory")
_MscPppFramerStorageType_Type = StorageType
_MscPppFramerStorageType_Object = MibTableColumn
mscPppFramerStorageType = _MscPppFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 1, 1, 4),
    _MscPppFramerStorageType_Type()
)
mscPppFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerStorageType.setStatus("mandatory")
_MscPppFramerIndex_Type = NonReplicated
_MscPppFramerIndex_Object = MibTableColumn
mscPppFramerIndex = _MscPppFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 1, 1, 10),
    _MscPppFramerIndex_Type()
)
mscPppFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppFramerIndex.setStatus("mandatory")
_MscPppFramerProvTable_Object = MibTable
mscPppFramerProvTable = _MscPppFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 10)
)
if mibBuilder.loadTexts:
    mscPppFramerProvTable.setStatus("mandatory")
_MscPppFramerProvEntry_Object = MibTableRow
mscPppFramerProvEntry = _MscPppFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 10, 1)
)
mscPppFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppFramerIndex"),
)
if mibBuilder.loadTexts:
    mscPppFramerProvEntry.setStatus("mandatory")
_MscPppFramerInterfaceName_Type = Link
_MscPppFramerInterfaceName_Object = MibTableColumn
mscPppFramerInterfaceName = _MscPppFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 10, 1, 1),
    _MscPppFramerInterfaceName_Type()
)
mscPppFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppFramerInterfaceName.setStatus("mandatory")
_MscPppFramerStateTable_Object = MibTable
mscPppFramerStateTable = _MscPppFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 12)
)
if mibBuilder.loadTexts:
    mscPppFramerStateTable.setStatus("mandatory")
_MscPppFramerStateEntry_Object = MibTableRow
mscPppFramerStateEntry = _MscPppFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 12, 1)
)
mscPppFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppFramerIndex"),
)
if mibBuilder.loadTexts:
    mscPppFramerStateEntry.setStatus("mandatory")


class _MscPppFramerAdminState_Type(Integer32):
    """Custom type mscPppFramerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscPppFramerAdminState_Type.__name__ = "Integer32"
_MscPppFramerAdminState_Object = MibTableColumn
mscPppFramerAdminState = _MscPppFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 12, 1, 1),
    _MscPppFramerAdminState_Type()
)
mscPppFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerAdminState.setStatus("mandatory")


class _MscPppFramerOperationalState_Type(Integer32):
    """Custom type mscPppFramerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscPppFramerOperationalState_Type.__name__ = "Integer32"
_MscPppFramerOperationalState_Object = MibTableColumn
mscPppFramerOperationalState = _MscPppFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 12, 1, 2),
    _MscPppFramerOperationalState_Type()
)
mscPppFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerOperationalState.setStatus("mandatory")


class _MscPppFramerUsageState_Type(Integer32):
    """Custom type mscPppFramerUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscPppFramerUsageState_Type.__name__ = "Integer32"
_MscPppFramerUsageState_Object = MibTableColumn
mscPppFramerUsageState = _MscPppFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 12, 1, 3),
    _MscPppFramerUsageState_Type()
)
mscPppFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerUsageState.setStatus("mandatory")
_MscPppFramerStatsTable_Object = MibTable
mscPppFramerStatsTable = _MscPppFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13)
)
if mibBuilder.loadTexts:
    mscPppFramerStatsTable.setStatus("mandatory")
_MscPppFramerStatsEntry_Object = MibTableRow
mscPppFramerStatsEntry = _MscPppFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1)
)
mscPppFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppFramerIndex"),
)
if mibBuilder.loadTexts:
    mscPppFramerStatsEntry.setStatus("mandatory")
_MscPppFramerFrmToIf_Type = Counter32
_MscPppFramerFrmToIf_Object = MibTableColumn
mscPppFramerFrmToIf = _MscPppFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 1),
    _MscPppFramerFrmToIf_Type()
)
mscPppFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerFrmToIf.setStatus("mandatory")
_MscPppFramerFrmFromIf_Type = Counter32
_MscPppFramerFrmFromIf_Object = MibTableColumn
mscPppFramerFrmFromIf = _MscPppFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 2),
    _MscPppFramerFrmFromIf_Type()
)
mscPppFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerFrmFromIf.setStatus("mandatory")
_MscPppFramerAborts_Type = Counter32
_MscPppFramerAborts_Object = MibTableColumn
mscPppFramerAborts = _MscPppFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 3),
    _MscPppFramerAborts_Type()
)
mscPppFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerAborts.setStatus("mandatory")
_MscPppFramerCrcErrors_Type = Counter32
_MscPppFramerCrcErrors_Object = MibTableColumn
mscPppFramerCrcErrors = _MscPppFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 4),
    _MscPppFramerCrcErrors_Type()
)
mscPppFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerCrcErrors.setStatus("mandatory")
_MscPppFramerLrcErrors_Type = Counter32
_MscPppFramerLrcErrors_Object = MibTableColumn
mscPppFramerLrcErrors = _MscPppFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 5),
    _MscPppFramerLrcErrors_Type()
)
mscPppFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerLrcErrors.setStatus("mandatory")
_MscPppFramerNonOctetErrors_Type = Counter32
_MscPppFramerNonOctetErrors_Object = MibTableColumn
mscPppFramerNonOctetErrors = _MscPppFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 6),
    _MscPppFramerNonOctetErrors_Type()
)
mscPppFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerNonOctetErrors.setStatus("mandatory")
_MscPppFramerOverruns_Type = Counter32
_MscPppFramerOverruns_Object = MibTableColumn
mscPppFramerOverruns = _MscPppFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 7),
    _MscPppFramerOverruns_Type()
)
mscPppFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerOverruns.setStatus("mandatory")
_MscPppFramerUnderruns_Type = Counter32
_MscPppFramerUnderruns_Object = MibTableColumn
mscPppFramerUnderruns = _MscPppFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 8),
    _MscPppFramerUnderruns_Type()
)
mscPppFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerUnderruns.setStatus("mandatory")
_MscPppFramerLargeFrmErrors_Type = Counter32
_MscPppFramerLargeFrmErrors_Object = MibTableColumn
mscPppFramerLargeFrmErrors = _MscPppFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 13, 1, 9),
    _MscPppFramerLargeFrmErrors_Type()
)
mscPppFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerLargeFrmErrors.setStatus("mandatory")
_MscPppFramerUtilTable_Object = MibTable
mscPppFramerUtilTable = _MscPppFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 14)
)
if mibBuilder.loadTexts:
    mscPppFramerUtilTable.setStatus("mandatory")
_MscPppFramerUtilEntry_Object = MibTableRow
mscPppFramerUtilEntry = _MscPppFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 14, 1)
)
mscPppFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppFramerIndex"),
)
if mibBuilder.loadTexts:
    mscPppFramerUtilEntry.setStatus("mandatory")


class _MscPppFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscPppFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscPppFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscPppFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscPppFramerNormPrioLinkUtilToIf = _MscPppFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 14, 1, 1),
    _MscPppFramerNormPrioLinkUtilToIf_Type()
)
mscPppFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscPppFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscPppFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscPppFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscPppFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscPppFramerNormPrioLinkUtilFromIf = _MscPppFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 5, 14, 1, 3),
    _MscPppFramerNormPrioLinkUtilFromIf_Type()
)
mscPppFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscPppLeq_ObjectIdentity = ObjectIdentity
mscPppLeq = _MscPppLeq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6)
)
_MscPppLeqRowStatusTable_Object = MibTable
mscPppLeqRowStatusTable = _MscPppLeqRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 1)
)
if mibBuilder.loadTexts:
    mscPppLeqRowStatusTable.setStatus("mandatory")
_MscPppLeqRowStatusEntry_Object = MibTableRow
mscPppLeqRowStatusEntry = _MscPppLeqRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 1, 1)
)
mscPppLeqRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLeqIndex"),
)
if mibBuilder.loadTexts:
    mscPppLeqRowStatusEntry.setStatus("mandatory")
_MscPppLeqRowStatus_Type = RowStatus
_MscPppLeqRowStatus_Object = MibTableColumn
mscPppLeqRowStatus = _MscPppLeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 1, 1, 1),
    _MscPppLeqRowStatus_Type()
)
mscPppLeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLeqRowStatus.setStatus("mandatory")
_MscPppLeqComponentName_Type = DisplayString
_MscPppLeqComponentName_Object = MibTableColumn
mscPppLeqComponentName = _MscPppLeqComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 1, 1, 2),
    _MscPppLeqComponentName_Type()
)
mscPppLeqComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqComponentName.setStatus("mandatory")
_MscPppLeqStorageType_Type = StorageType
_MscPppLeqStorageType_Object = MibTableColumn
mscPppLeqStorageType = _MscPppLeqStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 1, 1, 4),
    _MscPppLeqStorageType_Type()
)
mscPppLeqStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqStorageType.setStatus("mandatory")
_MscPppLeqIndex_Type = NonReplicated
_MscPppLeqIndex_Object = MibTableColumn
mscPppLeqIndex = _MscPppLeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 1, 1, 10),
    _MscPppLeqIndex_Type()
)
mscPppLeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscPppLeqIndex.setStatus("mandatory")
_MscPppLeqProvTable_Object = MibTable
mscPppLeqProvTable = _MscPppLeqProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 10)
)
if mibBuilder.loadTexts:
    mscPppLeqProvTable.setStatus("mandatory")
_MscPppLeqProvEntry_Object = MibTableRow
mscPppLeqProvEntry = _MscPppLeqProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 10, 1)
)
mscPppLeqProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLeqIndex"),
)
if mibBuilder.loadTexts:
    mscPppLeqProvEntry.setStatus("mandatory")


class _MscPppLeqMaxPackets_Type(Unsigned32):
    """Custom type mscPppLeqMaxPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MscPppLeqMaxPackets_Type.__name__ = "Unsigned32"
_MscPppLeqMaxPackets_Object = MibTableColumn
mscPppLeqMaxPackets = _MscPppLeqMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 10, 1, 1),
    _MscPppLeqMaxPackets_Type()
)
mscPppLeqMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLeqMaxPackets.setStatus("mandatory")


class _MscPppLeqMaxMsecData_Type(Unsigned32):
    """Custom type mscPppLeqMaxMsecData based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_MscPppLeqMaxMsecData_Type.__name__ = "Unsigned32"
_MscPppLeqMaxMsecData_Object = MibTableColumn
mscPppLeqMaxMsecData = _MscPppLeqMaxMsecData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 10, 1, 2),
    _MscPppLeqMaxMsecData_Type()
)
mscPppLeqMaxMsecData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLeqMaxMsecData.setStatus("mandatory")


class _MscPppLeqMaxPercentMulticast_Type(Unsigned32):
    """Custom type mscPppLeqMaxPercentMulticast based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscPppLeqMaxPercentMulticast_Type.__name__ = "Unsigned32"
_MscPppLeqMaxPercentMulticast_Object = MibTableColumn
mscPppLeqMaxPercentMulticast = _MscPppLeqMaxPercentMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 10, 1, 3),
    _MscPppLeqMaxPercentMulticast_Type()
)
mscPppLeqMaxPercentMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLeqMaxPercentMulticast.setStatus("mandatory")


class _MscPppLeqTimeToLive_Type(Unsigned32):
    """Custom type mscPppLeqTimeToLive based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_MscPppLeqTimeToLive_Type.__name__ = "Unsigned32"
_MscPppLeqTimeToLive_Object = MibTableColumn
mscPppLeqTimeToLive = _MscPppLeqTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 10, 1, 4),
    _MscPppLeqTimeToLive_Type()
)
mscPppLeqTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLeqTimeToLive.setStatus("mandatory")
_MscPppLeqStatsTable_Object = MibTable
mscPppLeqStatsTable = _MscPppLeqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 11)
)
if mibBuilder.loadTexts:
    mscPppLeqStatsTable.setStatus("mandatory")
_MscPppLeqStatsEntry_Object = MibTableRow
mscPppLeqStatsEntry = _MscPppLeqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 11, 1)
)
mscPppLeqStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLeqIndex"),
)
if mibBuilder.loadTexts:
    mscPppLeqStatsEntry.setStatus("mandatory")
_MscPppLeqTimedOutPkt_Type = Counter32
_MscPppLeqTimedOutPkt_Object = MibTableColumn
mscPppLeqTimedOutPkt = _MscPppLeqTimedOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 11, 1, 1),
    _MscPppLeqTimedOutPkt_Type()
)
mscPppLeqTimedOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqTimedOutPkt.setStatus("mandatory")
_MscPppLeqHardwareForcedPkt_Type = Counter32
_MscPppLeqHardwareForcedPkt_Object = MibTableColumn
mscPppLeqHardwareForcedPkt = _MscPppLeqHardwareForcedPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 11, 1, 2),
    _MscPppLeqHardwareForcedPkt_Type()
)
mscPppLeqHardwareForcedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqHardwareForcedPkt.setStatus("mandatory")
_MscPppLeqForcedPktDiscards_Type = Counter32
_MscPppLeqForcedPktDiscards_Object = MibTableColumn
mscPppLeqForcedPktDiscards = _MscPppLeqForcedPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 11, 1, 4),
    _MscPppLeqForcedPktDiscards_Type()
)
mscPppLeqForcedPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqForcedPktDiscards.setStatus("mandatory")
_MscPppLeqQueuePurgeDiscards_Type = Counter32
_MscPppLeqQueuePurgeDiscards_Object = MibTableColumn
mscPppLeqQueuePurgeDiscards = _MscPppLeqQueuePurgeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 11, 1, 5),
    _MscPppLeqQueuePurgeDiscards_Type()
)
mscPppLeqQueuePurgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqQueuePurgeDiscards.setStatus("mandatory")
_MscPppLeqTStatsTable_Object = MibTable
mscPppLeqTStatsTable = _MscPppLeqTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12)
)
if mibBuilder.loadTexts:
    mscPppLeqTStatsTable.setStatus("mandatory")
_MscPppLeqTStatsEntry_Object = MibTableRow
mscPppLeqTStatsEntry = _MscPppLeqTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12, 1)
)
mscPppLeqTStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLeqIndex"),
)
if mibBuilder.loadTexts:
    mscPppLeqTStatsEntry.setStatus("mandatory")
_MscPppLeqTotalPktHandled_Type = Counter32
_MscPppLeqTotalPktHandled_Object = MibTableColumn
mscPppLeqTotalPktHandled = _MscPppLeqTotalPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12, 1, 1),
    _MscPppLeqTotalPktHandled_Type()
)
mscPppLeqTotalPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqTotalPktHandled.setStatus("mandatory")
_MscPppLeqTotalPktForwarded_Type = Counter32
_MscPppLeqTotalPktForwarded_Object = MibTableColumn
mscPppLeqTotalPktForwarded = _MscPppLeqTotalPktForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12, 1, 2),
    _MscPppLeqTotalPktForwarded_Type()
)
mscPppLeqTotalPktForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqTotalPktForwarded.setStatus("mandatory")
_MscPppLeqTotalPktQueued_Type = Counter32
_MscPppLeqTotalPktQueued_Object = MibTableColumn
mscPppLeqTotalPktQueued = _MscPppLeqTotalPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12, 1, 3),
    _MscPppLeqTotalPktQueued_Type()
)
mscPppLeqTotalPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqTotalPktQueued.setStatus("mandatory")
_MscPppLeqTotalMulticastPkt_Type = Counter32
_MscPppLeqTotalMulticastPkt_Object = MibTableColumn
mscPppLeqTotalMulticastPkt = _MscPppLeqTotalMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12, 1, 4),
    _MscPppLeqTotalMulticastPkt_Type()
)
mscPppLeqTotalMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqTotalMulticastPkt.setStatus("mandatory")
_MscPppLeqTotalPktDiscards_Type = Counter32
_MscPppLeqTotalPktDiscards_Object = MibTableColumn
mscPppLeqTotalPktDiscards = _MscPppLeqTotalPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 12, 1, 8),
    _MscPppLeqTotalPktDiscards_Type()
)
mscPppLeqTotalPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqTotalPktDiscards.setStatus("mandatory")
_MscPppLeqCStatsTable_Object = MibTable
mscPppLeqCStatsTable = _MscPppLeqCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 13)
)
if mibBuilder.loadTexts:
    mscPppLeqCStatsTable.setStatus("mandatory")
_MscPppLeqCStatsEntry_Object = MibTableRow
mscPppLeqCStatsEntry = _MscPppLeqCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 13, 1)
)
mscPppLeqCStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLeqIndex"),
)
if mibBuilder.loadTexts:
    mscPppLeqCStatsEntry.setStatus("mandatory")


class _MscPppLeqCurrentPktQueued_Type(Gauge32):
    """Custom type mscPppLeqCurrentPktQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLeqCurrentPktQueued_Type.__name__ = "Gauge32"
_MscPppLeqCurrentPktQueued_Object = MibTableColumn
mscPppLeqCurrentPktQueued = _MscPppLeqCurrentPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 13, 1, 1),
    _MscPppLeqCurrentPktQueued_Type()
)
mscPppLeqCurrentPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqCurrentPktQueued.setStatus("mandatory")


class _MscPppLeqCurrentBytesQueued_Type(Gauge32):
    """Custom type mscPppLeqCurrentBytesQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLeqCurrentBytesQueued_Type.__name__ = "Gauge32"
_MscPppLeqCurrentBytesQueued_Object = MibTableColumn
mscPppLeqCurrentBytesQueued = _MscPppLeqCurrentBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 13, 1, 2),
    _MscPppLeqCurrentBytesQueued_Type()
)
mscPppLeqCurrentBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqCurrentBytesQueued.setStatus("mandatory")


class _MscPppLeqCurrentMulticastQueued_Type(Gauge32):
    """Custom type mscPppLeqCurrentMulticastQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLeqCurrentMulticastQueued_Type.__name__ = "Gauge32"
_MscPppLeqCurrentMulticastQueued_Object = MibTableColumn
mscPppLeqCurrentMulticastQueued = _MscPppLeqCurrentMulticastQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 13, 1, 3),
    _MscPppLeqCurrentMulticastQueued_Type()
)
mscPppLeqCurrentMulticastQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqCurrentMulticastQueued.setStatus("mandatory")
_MscPppLeqThrStatsTable_Object = MibTable
mscPppLeqThrStatsTable = _MscPppLeqThrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14)
)
if mibBuilder.loadTexts:
    mscPppLeqThrStatsTable.setStatus("mandatory")
_MscPppLeqThrStatsEntry_Object = MibTableRow
mscPppLeqThrStatsEntry = _MscPppLeqThrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1)
)
mscPppLeqThrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppLeqIndex"),
)
if mibBuilder.loadTexts:
    mscPppLeqThrStatsEntry.setStatus("mandatory")


class _MscPppLeqQueuePktThreshold_Type(Unsigned32):
    """Custom type mscPppLeqQueuePktThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLeqQueuePktThreshold_Type.__name__ = "Unsigned32"
_MscPppLeqQueuePktThreshold_Object = MibTableColumn
mscPppLeqQueuePktThreshold = _MscPppLeqQueuePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 1),
    _MscPppLeqQueuePktThreshold_Type()
)
mscPppLeqQueuePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqQueuePktThreshold.setStatus("mandatory")
_MscPppLeqPktThresholdExceeded_Type = Counter32
_MscPppLeqPktThresholdExceeded_Object = MibTableColumn
mscPppLeqPktThresholdExceeded = _MscPppLeqPktThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 2),
    _MscPppLeqPktThresholdExceeded_Type()
)
mscPppLeqPktThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqPktThresholdExceeded.setStatus("mandatory")


class _MscPppLeqQueueByteThreshold_Type(Unsigned32):
    """Custom type mscPppLeqQueueByteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLeqQueueByteThreshold_Type.__name__ = "Unsigned32"
_MscPppLeqQueueByteThreshold_Object = MibTableColumn
mscPppLeqQueueByteThreshold = _MscPppLeqQueueByteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 3),
    _MscPppLeqQueueByteThreshold_Type()
)
mscPppLeqQueueByteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqQueueByteThreshold.setStatus("mandatory")
_MscPppLeqByteThresholdExceeded_Type = Counter32
_MscPppLeqByteThresholdExceeded_Object = MibTableColumn
mscPppLeqByteThresholdExceeded = _MscPppLeqByteThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 4),
    _MscPppLeqByteThresholdExceeded_Type()
)
mscPppLeqByteThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqByteThresholdExceeded.setStatus("mandatory")


class _MscPppLeqQueueMulticastThreshold_Type(Unsigned32):
    """Custom type mscPppLeqQueueMulticastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscPppLeqQueueMulticastThreshold_Type.__name__ = "Unsigned32"
_MscPppLeqQueueMulticastThreshold_Object = MibTableColumn
mscPppLeqQueueMulticastThreshold = _MscPppLeqQueueMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 5),
    _MscPppLeqQueueMulticastThreshold_Type()
)
mscPppLeqQueueMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqQueueMulticastThreshold.setStatus("mandatory")
_MscPppLeqMulThresholdExceeded_Type = Counter32
_MscPppLeqMulThresholdExceeded_Object = MibTableColumn
mscPppLeqMulThresholdExceeded = _MscPppLeqMulThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 6),
    _MscPppLeqMulThresholdExceeded_Type()
)
mscPppLeqMulThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqMulThresholdExceeded.setStatus("mandatory")
_MscPppLeqMemThresholdExceeded_Type = Counter32
_MscPppLeqMemThresholdExceeded_Object = MibTableColumn
mscPppLeqMemThresholdExceeded = _MscPppLeqMemThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 6, 14, 1, 7),
    _MscPppLeqMemThresholdExceeded_Type()
)
mscPppLeqMemThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppLeqMemThresholdExceeded.setStatus("mandatory")
_MscPppCidDataTable_Object = MibTable
mscPppCidDataTable = _MscPppCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 20)
)
if mibBuilder.loadTexts:
    mscPppCidDataTable.setStatus("mandatory")
_MscPppCidDataEntry_Object = MibTableRow
mscPppCidDataEntry = _MscPppCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 20, 1)
)
mscPppCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
)
if mibBuilder.loadTexts:
    mscPppCidDataEntry.setStatus("mandatory")


class _MscPppCustomerIdentifier_Type(Unsigned32):
    """Custom type mscPppCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscPppCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscPppCustomerIdentifier_Object = MibTableColumn
mscPppCustomerIdentifier = _MscPppCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 20, 1, 1),
    _MscPppCustomerIdentifier_Type()
)
mscPppCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppCustomerIdentifier.setStatus("mandatory")
_MscPppIfEntryTable_Object = MibTable
mscPppIfEntryTable = _MscPppIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 21)
)
if mibBuilder.loadTexts:
    mscPppIfEntryTable.setStatus("mandatory")
_MscPppIfEntryEntry_Object = MibTableRow
mscPppIfEntryEntry = _MscPppIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 21, 1)
)
mscPppIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
)
if mibBuilder.loadTexts:
    mscPppIfEntryEntry.setStatus("mandatory")


class _MscPppIfAdminStatus_Type(Integer32):
    """Custom type mscPppIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscPppIfAdminStatus_Type.__name__ = "Integer32"
_MscPppIfAdminStatus_Object = MibTableColumn
mscPppIfAdminStatus = _MscPppIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 21, 1, 1),
    _MscPppIfAdminStatus_Type()
)
mscPppIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppIfAdminStatus.setStatus("mandatory")


class _MscPppIfIndex_Type(InterfaceIndex):
    """Custom type mscPppIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscPppIfIndex_Type.__name__ = "InterfaceIndex"
_MscPppIfIndex_Object = MibTableColumn
mscPppIfIndex = _MscPppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 21, 1, 2),
    _MscPppIfIndex_Type()
)
mscPppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppIfIndex.setStatus("mandatory")
_MscPppMpTable_Object = MibTable
mscPppMpTable = _MscPppMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 22)
)
if mibBuilder.loadTexts:
    mscPppMpTable.setStatus("mandatory")
_MscPppMpEntry_Object = MibTableRow
mscPppMpEntry = _MscPppMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 22, 1)
)
mscPppMpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
)
if mibBuilder.loadTexts:
    mscPppMpEntry.setStatus("mandatory")
_MscPppLinkToProtocolPort_Type = Link
_MscPppLinkToProtocolPort_Object = MibTableColumn
mscPppLinkToProtocolPort = _MscPppLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 22, 1, 1),
    _MscPppLinkToProtocolPort_Type()
)
mscPppLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscPppLinkToProtocolPort.setStatus("mandatory")
_MscPppStateTable_Object = MibTable
mscPppStateTable = _MscPppStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 23)
)
if mibBuilder.loadTexts:
    mscPppStateTable.setStatus("mandatory")
_MscPppStateEntry_Object = MibTableRow
mscPppStateEntry = _MscPppStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 23, 1)
)
mscPppStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
)
if mibBuilder.loadTexts:
    mscPppStateEntry.setStatus("mandatory")


class _MscPppAdminState_Type(Integer32):
    """Custom type mscPppAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscPppAdminState_Type.__name__ = "Integer32"
_MscPppAdminState_Object = MibTableColumn
mscPppAdminState = _MscPppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 23, 1, 1),
    _MscPppAdminState_Type()
)
mscPppAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppAdminState.setStatus("mandatory")


class _MscPppOperationalState_Type(Integer32):
    """Custom type mscPppOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscPppOperationalState_Type.__name__ = "Integer32"
_MscPppOperationalState_Object = MibTableColumn
mscPppOperationalState = _MscPppOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 23, 1, 2),
    _MscPppOperationalState_Type()
)
mscPppOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppOperationalState.setStatus("mandatory")


class _MscPppUsageState_Type(Integer32):
    """Custom type mscPppUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscPppUsageState_Type.__name__ = "Integer32"
_MscPppUsageState_Object = MibTableColumn
mscPppUsageState = _MscPppUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 23, 1, 3),
    _MscPppUsageState_Type()
)
mscPppUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppUsageState.setStatus("mandatory")
_MscPppOperStatusTable_Object = MibTable
mscPppOperStatusTable = _MscPppOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 24)
)
if mibBuilder.loadTexts:
    mscPppOperStatusTable.setStatus("mandatory")
_MscPppOperStatusEntry_Object = MibTableRow
mscPppOperStatusEntry = _MscPppOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 24, 1)
)
mscPppOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-PppMIB", "mscPppIndex"),
)
if mibBuilder.loadTexts:
    mscPppOperStatusEntry.setStatus("mandatory")


class _MscPppSnmpOperStatus_Type(Integer32):
    """Custom type mscPppSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscPppSnmpOperStatus_Type.__name__ = "Integer32"
_MscPppSnmpOperStatus_Object = MibTableColumn
mscPppSnmpOperStatus = _MscPppSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 102, 24, 1, 1),
    _MscPppSnmpOperStatus_Type()
)
mscPppSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscPppSnmpOperStatus.setStatus("mandatory")
_PppMIB_ObjectIdentity = ObjectIdentity
pppMIB = _PppMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33)
)
_PppGroup_ObjectIdentity = ObjectIdentity
pppGroup = _PppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 1)
)
_PppGroupCA_ObjectIdentity = ObjectIdentity
pppGroupCA = _PppGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 1, 1)
)
_PppGroupCA02_ObjectIdentity = ObjectIdentity
pppGroupCA02 = _PppGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 1, 1, 3)
)
_PppGroupCA02A_ObjectIdentity = ObjectIdentity
pppGroupCA02A = _PppGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 1, 1, 3, 2)
)
_PppCapabilities_ObjectIdentity = ObjectIdentity
pppCapabilities = _PppCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 3)
)
_PppCapabilitiesCA_ObjectIdentity = ObjectIdentity
pppCapabilitiesCA = _PppCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 3, 1)
)
_PppCapabilitiesCA02_ObjectIdentity = ObjectIdentity
pppCapabilitiesCA02 = _PppCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 3, 1, 3)
)
_PppCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
pppCapabilitiesCA02A = _PppCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 33, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-PppMIB",
    **{"mscPpp": mscPpp,
       "mscPppRowStatusTable": mscPppRowStatusTable,
       "mscPppRowStatusEntry": mscPppRowStatusEntry,
       "mscPppRowStatus": mscPppRowStatus,
       "mscPppComponentName": mscPppComponentName,
       "mscPppStorageType": mscPppStorageType,
       "mscPppIndex": mscPppIndex,
       "mscPppLnk": mscPppLnk,
       "mscPppLnkRowStatusTable": mscPppLnkRowStatusTable,
       "mscPppLnkRowStatusEntry": mscPppLnkRowStatusEntry,
       "mscPppLnkRowStatus": mscPppLnkRowStatus,
       "mscPppLnkComponentName": mscPppLnkComponentName,
       "mscPppLnkStorageType": mscPppLnkStorageType,
       "mscPppLnkIndex": mscPppLnkIndex,
       "mscPppLnkProvTable": mscPppLnkProvTable,
       "mscPppLnkProvEntry": mscPppLnkProvEntry,
       "mscPppLnkConfigInitialMru": mscPppLnkConfigInitialMru,
       "mscPppLnkConfigMagicNumber": mscPppLnkConfigMagicNumber,
       "mscPppLnkRestartTimer": mscPppLnkRestartTimer,
       "mscPppLnkContinuityMonitor": mscPppLnkContinuityMonitor,
       "mscPppLnkNegativeAckTries": mscPppLnkNegativeAckTries,
       "mscPppLnkQualityThreshold": mscPppLnkQualityThreshold,
       "mscPppLnkQualityWindow": mscPppLnkQualityWindow,
       "mscPppLnkTerminateRequestTries": mscPppLnkTerminateRequestTries,
       "mscPppLnkConfigureRequestTries": mscPppLnkConfigureRequestTries,
       "mscPppLnkOperTable": mscPppLnkOperTable,
       "mscPppLnkOperEntry": mscPppLnkOperEntry,
       "mscPppLnkOperState": mscPppLnkOperState,
       "mscPppLnkLineCondition": mscPppLnkLineCondition,
       "mscPppLnkBadAddresses": mscPppLnkBadAddresses,
       "mscPppLnkBadControls": mscPppLnkBadControls,
       "mscPppLnkPacketTooLongs": mscPppLnkPacketTooLongs,
       "mscPppLnkBadFcss": mscPppLnkBadFcss,
       "mscPppLnkLocalMru": mscPppLnkLocalMru,
       "mscPppLnkRemoteMru": mscPppLnkRemoteMru,
       "mscPppLnkTransmitFcsSize": mscPppLnkTransmitFcsSize,
       "mscPppLnkReceiveFcsSize": mscPppLnkReceiveFcsSize,
       "mscPppLqm": mscPppLqm,
       "mscPppLqmRowStatusTable": mscPppLqmRowStatusTable,
       "mscPppLqmRowStatusEntry": mscPppLqmRowStatusEntry,
       "mscPppLqmRowStatus": mscPppLqmRowStatus,
       "mscPppLqmComponentName": mscPppLqmComponentName,
       "mscPppLqmStorageType": mscPppLqmStorageType,
       "mscPppLqmIndex": mscPppLqmIndex,
       "mscPppLqmProvTable": mscPppLqmProvTable,
       "mscPppLqmProvEntry": mscPppLqmProvEntry,
       "mscPppLqmConfigPeriod": mscPppLqmConfigPeriod,
       "mscPppLqmConfigStatus": mscPppLqmConfigStatus,
       "mscPppLqmOperTable": mscPppLqmOperTable,
       "mscPppLqmOperEntry": mscPppLqmOperEntry,
       "mscPppLqmQuality": mscPppLqmQuality,
       "mscPppLqmInGoodOctets": mscPppLqmInGoodOctets,
       "mscPppLqmLocalPeriod": mscPppLqmLocalPeriod,
       "mscPppLqmRemotePeriod": mscPppLqmRemotePeriod,
       "mscPppLqmOutLqrs": mscPppLqmOutLqrs,
       "mscPppLqmInLqrs": mscPppLqmInLqrs,
       "mscPppNcp": mscPppNcp,
       "mscPppNcpRowStatusTable": mscPppNcpRowStatusTable,
       "mscPppNcpRowStatusEntry": mscPppNcpRowStatusEntry,
       "mscPppNcpRowStatus": mscPppNcpRowStatus,
       "mscPppNcpComponentName": mscPppNcpComponentName,
       "mscPppNcpStorageType": mscPppNcpStorageType,
       "mscPppNcpIndex": mscPppNcpIndex,
       "mscPppNcpBmcEntry": mscPppNcpBmcEntry,
       "mscPppNcpBmcEntryRowStatusTable": mscPppNcpBmcEntryRowStatusTable,
       "mscPppNcpBmcEntryRowStatusEntry": mscPppNcpBmcEntryRowStatusEntry,
       "mscPppNcpBmcEntryRowStatus": mscPppNcpBmcEntryRowStatus,
       "mscPppNcpBmcEntryComponentName": mscPppNcpBmcEntryComponentName,
       "mscPppNcpBmcEntryStorageType": mscPppNcpBmcEntryStorageType,
       "mscPppNcpBmcEntryMacTypeIndex": mscPppNcpBmcEntryMacTypeIndex,
       "mscPppNcpBmcEntryProvTable": mscPppNcpBmcEntryProvTable,
       "mscPppNcpBmcEntryProvEntry": mscPppNcpBmcEntryProvEntry,
       "mscPppNcpBmcEntryLocalStatus": mscPppNcpBmcEntryLocalStatus,
       "mscPppNcpBmEntry": mscPppNcpBmEntry,
       "mscPppNcpBmEntryRowStatusTable": mscPppNcpBmEntryRowStatusTable,
       "mscPppNcpBmEntryRowStatusEntry": mscPppNcpBmEntryRowStatusEntry,
       "mscPppNcpBmEntryRowStatus": mscPppNcpBmEntryRowStatus,
       "mscPppNcpBmEntryComponentName": mscPppNcpBmEntryComponentName,
       "mscPppNcpBmEntryStorageType": mscPppNcpBmEntryStorageType,
       "mscPppNcpBmEntryMacTypeIndex": mscPppNcpBmEntryMacTypeIndex,
       "mscPppNcpBmEntryOperTable": mscPppNcpBmEntryOperTable,
       "mscPppNcpBmEntryOperEntry": mscPppNcpBmEntryOperEntry,
       "mscPppNcpBmEntryLocalStatus": mscPppNcpBmEntryLocalStatus,
       "mscPppNcpBmEntryRemoteStatus": mscPppNcpBmEntryRemoteStatus,
       "mscPppNcpBprovTable": mscPppNcpBprovTable,
       "mscPppNcpBprovEntry": mscPppNcpBprovEntry,
       "mscPppNcpBConfigTinygram": mscPppNcpBConfigTinygram,
       "mscPppNcpBConfigLanId": mscPppNcpBConfigLanId,
       "mscPppNcpIpOperTable": mscPppNcpIpOperTable,
       "mscPppNcpIpOperEntry": mscPppNcpIpOperEntry,
       "mscPppNcpIpOperState": mscPppNcpIpOperState,
       "mscPppNcpBoperTable": mscPppNcpBoperTable,
       "mscPppNcpBoperEntry": mscPppNcpBoperEntry,
       "mscPppNcpBOperState": mscPppNcpBOperState,
       "mscPppNcpBLocalToRemoteTinygramComp": mscPppNcpBLocalToRemoteTinygramComp,
       "mscPppNcpBRemoteToLocalTinygramComp": mscPppNcpBRemoteToLocalTinygramComp,
       "mscPppNcpBLocalToRemoteLanId": mscPppNcpBLocalToRemoteLanId,
       "mscPppNcpBRemoteToLocalLanId": mscPppNcpBRemoteToLocalLanId,
       "mscPppNcpOperTable": mscPppNcpOperTable,
       "mscPppNcpOperEntry": mscPppNcpOperEntry,
       "mscPppNcpAppletalkOperState": mscPppNcpAppletalkOperState,
       "mscPppNcpIpxOperState": mscPppNcpIpxOperState,
       "mscPppNcpXnsOperState": mscPppNcpXnsOperState,
       "mscPppNcpDecnetOperState": mscPppNcpDecnetOperState,
       "mscPppFramer": mscPppFramer,
       "mscPppFramerRowStatusTable": mscPppFramerRowStatusTable,
       "mscPppFramerRowStatusEntry": mscPppFramerRowStatusEntry,
       "mscPppFramerRowStatus": mscPppFramerRowStatus,
       "mscPppFramerComponentName": mscPppFramerComponentName,
       "mscPppFramerStorageType": mscPppFramerStorageType,
       "mscPppFramerIndex": mscPppFramerIndex,
       "mscPppFramerProvTable": mscPppFramerProvTable,
       "mscPppFramerProvEntry": mscPppFramerProvEntry,
       "mscPppFramerInterfaceName": mscPppFramerInterfaceName,
       "mscPppFramerStateTable": mscPppFramerStateTable,
       "mscPppFramerStateEntry": mscPppFramerStateEntry,
       "mscPppFramerAdminState": mscPppFramerAdminState,
       "mscPppFramerOperationalState": mscPppFramerOperationalState,
       "mscPppFramerUsageState": mscPppFramerUsageState,
       "mscPppFramerStatsTable": mscPppFramerStatsTable,
       "mscPppFramerStatsEntry": mscPppFramerStatsEntry,
       "mscPppFramerFrmToIf": mscPppFramerFrmToIf,
       "mscPppFramerFrmFromIf": mscPppFramerFrmFromIf,
       "mscPppFramerAborts": mscPppFramerAborts,
       "mscPppFramerCrcErrors": mscPppFramerCrcErrors,
       "mscPppFramerLrcErrors": mscPppFramerLrcErrors,
       "mscPppFramerNonOctetErrors": mscPppFramerNonOctetErrors,
       "mscPppFramerOverruns": mscPppFramerOverruns,
       "mscPppFramerUnderruns": mscPppFramerUnderruns,
       "mscPppFramerLargeFrmErrors": mscPppFramerLargeFrmErrors,
       "mscPppFramerUtilTable": mscPppFramerUtilTable,
       "mscPppFramerUtilEntry": mscPppFramerUtilEntry,
       "mscPppFramerNormPrioLinkUtilToIf": mscPppFramerNormPrioLinkUtilToIf,
       "mscPppFramerNormPrioLinkUtilFromIf": mscPppFramerNormPrioLinkUtilFromIf,
       "mscPppLeq": mscPppLeq,
       "mscPppLeqRowStatusTable": mscPppLeqRowStatusTable,
       "mscPppLeqRowStatusEntry": mscPppLeqRowStatusEntry,
       "mscPppLeqRowStatus": mscPppLeqRowStatus,
       "mscPppLeqComponentName": mscPppLeqComponentName,
       "mscPppLeqStorageType": mscPppLeqStorageType,
       "mscPppLeqIndex": mscPppLeqIndex,
       "mscPppLeqProvTable": mscPppLeqProvTable,
       "mscPppLeqProvEntry": mscPppLeqProvEntry,
       "mscPppLeqMaxPackets": mscPppLeqMaxPackets,
       "mscPppLeqMaxMsecData": mscPppLeqMaxMsecData,
       "mscPppLeqMaxPercentMulticast": mscPppLeqMaxPercentMulticast,
       "mscPppLeqTimeToLive": mscPppLeqTimeToLive,
       "mscPppLeqStatsTable": mscPppLeqStatsTable,
       "mscPppLeqStatsEntry": mscPppLeqStatsEntry,
       "mscPppLeqTimedOutPkt": mscPppLeqTimedOutPkt,
       "mscPppLeqHardwareForcedPkt": mscPppLeqHardwareForcedPkt,
       "mscPppLeqForcedPktDiscards": mscPppLeqForcedPktDiscards,
       "mscPppLeqQueuePurgeDiscards": mscPppLeqQueuePurgeDiscards,
       "mscPppLeqTStatsTable": mscPppLeqTStatsTable,
       "mscPppLeqTStatsEntry": mscPppLeqTStatsEntry,
       "mscPppLeqTotalPktHandled": mscPppLeqTotalPktHandled,
       "mscPppLeqTotalPktForwarded": mscPppLeqTotalPktForwarded,
       "mscPppLeqTotalPktQueued": mscPppLeqTotalPktQueued,
       "mscPppLeqTotalMulticastPkt": mscPppLeqTotalMulticastPkt,
       "mscPppLeqTotalPktDiscards": mscPppLeqTotalPktDiscards,
       "mscPppLeqCStatsTable": mscPppLeqCStatsTable,
       "mscPppLeqCStatsEntry": mscPppLeqCStatsEntry,
       "mscPppLeqCurrentPktQueued": mscPppLeqCurrentPktQueued,
       "mscPppLeqCurrentBytesQueued": mscPppLeqCurrentBytesQueued,
       "mscPppLeqCurrentMulticastQueued": mscPppLeqCurrentMulticastQueued,
       "mscPppLeqThrStatsTable": mscPppLeqThrStatsTable,
       "mscPppLeqThrStatsEntry": mscPppLeqThrStatsEntry,
       "mscPppLeqQueuePktThreshold": mscPppLeqQueuePktThreshold,
       "mscPppLeqPktThresholdExceeded": mscPppLeqPktThresholdExceeded,
       "mscPppLeqQueueByteThreshold": mscPppLeqQueueByteThreshold,
       "mscPppLeqByteThresholdExceeded": mscPppLeqByteThresholdExceeded,
       "mscPppLeqQueueMulticastThreshold": mscPppLeqQueueMulticastThreshold,
       "mscPppLeqMulThresholdExceeded": mscPppLeqMulThresholdExceeded,
       "mscPppLeqMemThresholdExceeded": mscPppLeqMemThresholdExceeded,
       "mscPppCidDataTable": mscPppCidDataTable,
       "mscPppCidDataEntry": mscPppCidDataEntry,
       "mscPppCustomerIdentifier": mscPppCustomerIdentifier,
       "mscPppIfEntryTable": mscPppIfEntryTable,
       "mscPppIfEntryEntry": mscPppIfEntryEntry,
       "mscPppIfAdminStatus": mscPppIfAdminStatus,
       "mscPppIfIndex": mscPppIfIndex,
       "mscPppMpTable": mscPppMpTable,
       "mscPppMpEntry": mscPppMpEntry,
       "mscPppLinkToProtocolPort": mscPppLinkToProtocolPort,
       "mscPppStateTable": mscPppStateTable,
       "mscPppStateEntry": mscPppStateEntry,
       "mscPppAdminState": mscPppAdminState,
       "mscPppOperationalState": mscPppOperationalState,
       "mscPppUsageState": mscPppUsageState,
       "mscPppOperStatusTable": mscPppOperStatusTable,
       "mscPppOperStatusEntry": mscPppOperStatusEntry,
       "mscPppSnmpOperStatus": mscPppSnmpOperStatus,
       "pppMIB": pppMIB,
       "pppGroup": pppGroup,
       "pppGroupCA": pppGroupCA,
       "pppGroupCA02": pppGroupCA02,
       "pppGroupCA02A": pppGroupCA02A,
       "pppCapabilities": pppCapabilities,
       "pppCapabilitiesCA": pppCapabilitiesCA,
       "pppCapabilitiesCA02": pppCapabilitiesCA02,
       "pppCapabilitiesCA02A": pppCapabilitiesCA02A}
)
