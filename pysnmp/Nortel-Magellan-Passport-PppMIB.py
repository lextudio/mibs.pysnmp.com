# SNMP MIB module (Nortel-Magellan-Passport-PppMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-PppMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:18 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102)
)
_PppRowStatusTable_Object = MibTable
pppRowStatusTable = _PppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 1)
)
if mibBuilder.loadTexts:
    pppRowStatusTable.setStatus("mandatory")
_PppRowStatusEntry_Object = MibTableRow
pppRowStatusEntry = _PppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 1, 1)
)
pppRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
)
if mibBuilder.loadTexts:
    pppRowStatusEntry.setStatus("mandatory")
_PppRowStatus_Type = RowStatus
_PppRowStatus_Object = MibTableColumn
pppRowStatus = _PppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 1, 1, 1),
    _PppRowStatus_Type()
)
pppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppRowStatus.setStatus("mandatory")
_PppComponentName_Type = DisplayString
_PppComponentName_Object = MibTableColumn
pppComponentName = _PppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 1, 1, 2),
    _PppComponentName_Type()
)
pppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppComponentName.setStatus("mandatory")
_PppStorageType_Type = StorageType
_PppStorageType_Object = MibTableColumn
pppStorageType = _PppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 1, 1, 4),
    _PppStorageType_Type()
)
pppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppStorageType.setStatus("mandatory")


class _PppIndex_Type(Integer32):
    """Custom type pppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppIndex_Type.__name__ = "Integer32"
_PppIndex_Object = MibTableColumn
pppIndex = _PppIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 1, 1, 10),
    _PppIndex_Type()
)
pppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppIndex.setStatus("mandatory")
_PppLnk_ObjectIdentity = ObjectIdentity
pppLnk = _PppLnk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2)
)
_PppLnkRowStatusTable_Object = MibTable
pppLnkRowStatusTable = _PppLnkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 1)
)
if mibBuilder.loadTexts:
    pppLnkRowStatusTable.setStatus("mandatory")
_PppLnkRowStatusEntry_Object = MibTableRow
pppLnkRowStatusEntry = _PppLnkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 1, 1)
)
pppLnkRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLnkIndex"),
)
if mibBuilder.loadTexts:
    pppLnkRowStatusEntry.setStatus("mandatory")
_PppLnkRowStatus_Type = RowStatus
_PppLnkRowStatus_Object = MibTableColumn
pppLnkRowStatus = _PppLnkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 1, 1, 1),
    _PppLnkRowStatus_Type()
)
pppLnkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkRowStatus.setStatus("mandatory")
_PppLnkComponentName_Type = DisplayString
_PppLnkComponentName_Object = MibTableColumn
pppLnkComponentName = _PppLnkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 1, 1, 2),
    _PppLnkComponentName_Type()
)
pppLnkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkComponentName.setStatus("mandatory")
_PppLnkStorageType_Type = StorageType
_PppLnkStorageType_Object = MibTableColumn
pppLnkStorageType = _PppLnkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 1, 1, 4),
    _PppLnkStorageType_Type()
)
pppLnkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkStorageType.setStatus("mandatory")
_PppLnkIndex_Type = NonReplicated
_PppLnkIndex_Object = MibTableColumn
pppLnkIndex = _PppLnkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 1, 1, 10),
    _PppLnkIndex_Type()
)
pppLnkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppLnkIndex.setStatus("mandatory")
_PppLnkProvTable_Object = MibTable
pppLnkProvTable = _PppLnkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10)
)
if mibBuilder.loadTexts:
    pppLnkProvTable.setStatus("mandatory")
_PppLnkProvEntry_Object = MibTableRow
pppLnkProvEntry = _PppLnkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1)
)
pppLnkProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLnkIndex"),
)
if mibBuilder.loadTexts:
    pppLnkProvEntry.setStatus("mandatory")


class _PppLnkConfigInitialMru_Type(Unsigned32):
    """Custom type pppLnkConfigInitialMru based on Unsigned32"""
    defaultValue = 18000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 18000),
    )


_PppLnkConfigInitialMru_Type.__name__ = "Unsigned32"
_PppLnkConfigInitialMru_Object = MibTableColumn
pppLnkConfigInitialMru = _PppLnkConfigInitialMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 1),
    _PppLnkConfigInitialMru_Type()
)
pppLnkConfigInitialMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkConfigInitialMru.setStatus("mandatory")


class _PppLnkConfigMagicNumber_Type(Integer32):
    """Custom type pppLnkConfigMagicNumber based on Integer32"""
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


_PppLnkConfigMagicNumber_Type.__name__ = "Integer32"
_PppLnkConfigMagicNumber_Object = MibTableColumn
pppLnkConfigMagicNumber = _PppLnkConfigMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 4),
    _PppLnkConfigMagicNumber_Type()
)
pppLnkConfigMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkConfigMagicNumber.setStatus("mandatory")


class _PppLnkRestartTimer_Type(Unsigned32):
    """Custom type pppLnkRestartTimer based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_PppLnkRestartTimer_Type.__name__ = "Unsigned32"
_PppLnkRestartTimer_Object = MibTableColumn
pppLnkRestartTimer = _PppLnkRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 6),
    _PppLnkRestartTimer_Type()
)
pppLnkRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkRestartTimer.setStatus("mandatory")


class _PppLnkContinuityMonitor_Type(Integer32):
    """Custom type pppLnkContinuityMonitor based on Integer32"""
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


_PppLnkContinuityMonitor_Type.__name__ = "Integer32"
_PppLnkContinuityMonitor_Object = MibTableColumn
pppLnkContinuityMonitor = _PppLnkContinuityMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 7),
    _PppLnkContinuityMonitor_Type()
)
pppLnkContinuityMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkContinuityMonitor.setStatus("mandatory")


class _PppLnkNegativeAckTries_Type(Unsigned32):
    """Custom type pppLnkNegativeAckTries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLnkNegativeAckTries_Type.__name__ = "Unsigned32"
_PppLnkNegativeAckTries_Object = MibTableColumn
pppLnkNegativeAckTries = _PppLnkNegativeAckTries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 8),
    _PppLnkNegativeAckTries_Type()
)
pppLnkNegativeAckTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkNegativeAckTries.setStatus("mandatory")


class _PppLnkQualityThreshold_Type(Unsigned32):
    """Custom type pppLnkQualityThreshold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 99),
    )


_PppLnkQualityThreshold_Type.__name__ = "Unsigned32"
_PppLnkQualityThreshold_Object = MibTableColumn
pppLnkQualityThreshold = _PppLnkQualityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 9),
    _PppLnkQualityThreshold_Type()
)
pppLnkQualityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkQualityThreshold.setStatus("mandatory")


class _PppLnkQualityWindow_Type(Unsigned32):
    """Custom type pppLnkQualityWindow based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400),
    )


_PppLnkQualityWindow_Type.__name__ = "Unsigned32"
_PppLnkQualityWindow_Object = MibTableColumn
pppLnkQualityWindow = _PppLnkQualityWindow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 10),
    _PppLnkQualityWindow_Type()
)
pppLnkQualityWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkQualityWindow.setStatus("mandatory")


class _PppLnkTerminateRequestTries_Type(Unsigned32):
    """Custom type pppLnkTerminateRequestTries based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLnkTerminateRequestTries_Type.__name__ = "Unsigned32"
_PppLnkTerminateRequestTries_Object = MibTableColumn
pppLnkTerminateRequestTries = _PppLnkTerminateRequestTries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 11),
    _PppLnkTerminateRequestTries_Type()
)
pppLnkTerminateRequestTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkTerminateRequestTries.setStatus("mandatory")


class _PppLnkConfigureRequestTries_Type(Unsigned32):
    """Custom type pppLnkConfigureRequestTries based on Unsigned32"""
    defaultValue = 1000000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLnkConfigureRequestTries_Type.__name__ = "Unsigned32"
_PppLnkConfigureRequestTries_Object = MibTableColumn
pppLnkConfigureRequestTries = _PppLnkConfigureRequestTries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 10, 1, 12),
    _PppLnkConfigureRequestTries_Type()
)
pppLnkConfigureRequestTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLnkConfigureRequestTries.setStatus("mandatory")
_PppLnkOperTable_Object = MibTable
pppLnkOperTable = _PppLnkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11)
)
if mibBuilder.loadTexts:
    pppLnkOperTable.setStatus("mandatory")
_PppLnkOperEntry_Object = MibTableRow
pppLnkOperEntry = _PppLnkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1)
)
pppLnkOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLnkIndex"),
)
if mibBuilder.loadTexts:
    pppLnkOperEntry.setStatus("mandatory")


class _PppLnkOperState_Type(Integer32):
    """Custom type pppLnkOperState based on Integer32"""
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


_PppLnkOperState_Type.__name__ = "Integer32"
_PppLnkOperState_Object = MibTableColumn
pppLnkOperState = _PppLnkOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 1),
    _PppLnkOperState_Type()
)
pppLnkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkOperState.setStatus("mandatory")


class _PppLnkLineCondition_Type(Integer32):
    """Custom type pppLnkLineCondition based on Integer32"""
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


_PppLnkLineCondition_Type.__name__ = "Integer32"
_PppLnkLineCondition_Object = MibTableColumn
pppLnkLineCondition = _PppLnkLineCondition_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 2),
    _PppLnkLineCondition_Type()
)
pppLnkLineCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkLineCondition.setStatus("mandatory")
_PppLnkBadAddresses_Type = Counter32
_PppLnkBadAddresses_Object = MibTableColumn
pppLnkBadAddresses = _PppLnkBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 4),
    _PppLnkBadAddresses_Type()
)
pppLnkBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkBadAddresses.setStatus("mandatory")
_PppLnkBadControls_Type = Counter32
_PppLnkBadControls_Object = MibTableColumn
pppLnkBadControls = _PppLnkBadControls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 5),
    _PppLnkBadControls_Type()
)
pppLnkBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkBadControls.setStatus("mandatory")
_PppLnkPacketTooLongs_Type = Counter32
_PppLnkPacketTooLongs_Object = MibTableColumn
pppLnkPacketTooLongs = _PppLnkPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 6),
    _PppLnkPacketTooLongs_Type()
)
pppLnkPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkPacketTooLongs.setStatus("mandatory")
_PppLnkBadFcss_Type = Counter32
_PppLnkBadFcss_Object = MibTableColumn
pppLnkBadFcss = _PppLnkBadFcss_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 7),
    _PppLnkBadFcss_Type()
)
pppLnkBadFcss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkBadFcss.setStatus("mandatory")


class _PppLnkLocalMru_Type(Unsigned32):
    """Custom type pppLnkLocalMru based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_PppLnkLocalMru_Type.__name__ = "Unsigned32"
_PppLnkLocalMru_Object = MibTableColumn
pppLnkLocalMru = _PppLnkLocalMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 8),
    _PppLnkLocalMru_Type()
)
pppLnkLocalMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkLocalMru.setStatus("mandatory")


class _PppLnkRemoteMru_Type(Unsigned32):
    """Custom type pppLnkRemoteMru based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_PppLnkRemoteMru_Type.__name__ = "Unsigned32"
_PppLnkRemoteMru_Object = MibTableColumn
pppLnkRemoteMru = _PppLnkRemoteMru_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 9),
    _PppLnkRemoteMru_Type()
)
pppLnkRemoteMru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkRemoteMru.setStatus("mandatory")


class _PppLnkTransmitFcsSize_Type(Unsigned32):
    """Custom type pppLnkTransmitFcsSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLnkTransmitFcsSize_Type.__name__ = "Unsigned32"
_PppLnkTransmitFcsSize_Object = MibTableColumn
pppLnkTransmitFcsSize = _PppLnkTransmitFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 16),
    _PppLnkTransmitFcsSize_Type()
)
pppLnkTransmitFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkTransmitFcsSize.setStatus("mandatory")


class _PppLnkReceiveFcsSize_Type(Unsigned32):
    """Custom type pppLnkReceiveFcsSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLnkReceiveFcsSize_Type.__name__ = "Unsigned32"
_PppLnkReceiveFcsSize_Object = MibTableColumn
pppLnkReceiveFcsSize = _PppLnkReceiveFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 2, 11, 1, 17),
    _PppLnkReceiveFcsSize_Type()
)
pppLnkReceiveFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLnkReceiveFcsSize.setStatus("mandatory")
_PppLqm_ObjectIdentity = ObjectIdentity
pppLqm = _PppLqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3)
)
_PppLqmRowStatusTable_Object = MibTable
pppLqmRowStatusTable = _PppLqmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 1)
)
if mibBuilder.loadTexts:
    pppLqmRowStatusTable.setStatus("mandatory")
_PppLqmRowStatusEntry_Object = MibTableRow
pppLqmRowStatusEntry = _PppLqmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 1, 1)
)
pppLqmRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLqmIndex"),
)
if mibBuilder.loadTexts:
    pppLqmRowStatusEntry.setStatus("mandatory")
_PppLqmRowStatus_Type = RowStatus
_PppLqmRowStatus_Object = MibTableColumn
pppLqmRowStatus = _PppLqmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 1, 1, 1),
    _PppLqmRowStatus_Type()
)
pppLqmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmRowStatus.setStatus("mandatory")
_PppLqmComponentName_Type = DisplayString
_PppLqmComponentName_Object = MibTableColumn
pppLqmComponentName = _PppLqmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 1, 1, 2),
    _PppLqmComponentName_Type()
)
pppLqmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmComponentName.setStatus("mandatory")
_PppLqmStorageType_Type = StorageType
_PppLqmStorageType_Object = MibTableColumn
pppLqmStorageType = _PppLqmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 1, 1, 4),
    _PppLqmStorageType_Type()
)
pppLqmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmStorageType.setStatus("mandatory")
_PppLqmIndex_Type = NonReplicated
_PppLqmIndex_Object = MibTableColumn
pppLqmIndex = _PppLqmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 1, 1, 10),
    _PppLqmIndex_Type()
)
pppLqmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppLqmIndex.setStatus("mandatory")
_PppLqmProvTable_Object = MibTable
pppLqmProvTable = _PppLqmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 10)
)
if mibBuilder.loadTexts:
    pppLqmProvTable.setStatus("mandatory")
_PppLqmProvEntry_Object = MibTableRow
pppLqmProvEntry = _PppLqmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 10, 1)
)
pppLqmProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLqmIndex"),
)
if mibBuilder.loadTexts:
    pppLqmProvEntry.setStatus("mandatory")


class _PppLqmConfigPeriod_Type(Unsigned32):
    """Custom type pppLqmConfigPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppLqmConfigPeriod_Type.__name__ = "Unsigned32"
_PppLqmConfigPeriod_Object = MibTableColumn
pppLqmConfigPeriod = _PppLqmConfigPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 10, 1, 1),
    _PppLqmConfigPeriod_Type()
)
pppLqmConfigPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLqmConfigPeriod.setStatus("mandatory")


class _PppLqmConfigStatus_Type(Integer32):
    """Custom type pppLqmConfigStatus based on Integer32"""
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


_PppLqmConfigStatus_Type.__name__ = "Integer32"
_PppLqmConfigStatus_Object = MibTableColumn
pppLqmConfigStatus = _PppLqmConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 10, 1, 2),
    _PppLqmConfigStatus_Type()
)
pppLqmConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLqmConfigStatus.setStatus("mandatory")
_PppLqmOperTable_Object = MibTable
pppLqmOperTable = _PppLqmOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11)
)
if mibBuilder.loadTexts:
    pppLqmOperTable.setStatus("mandatory")
_PppLqmOperEntry_Object = MibTableRow
pppLqmOperEntry = _PppLqmOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1)
)
pppLqmOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLqmIndex"),
)
if mibBuilder.loadTexts:
    pppLqmOperEntry.setStatus("mandatory")


class _PppLqmQuality_Type(Integer32):
    """Custom type pppLqmQuality based on Integer32"""
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


_PppLqmQuality_Type.__name__ = "Integer32"
_PppLqmQuality_Object = MibTableColumn
pppLqmQuality = _PppLqmQuality_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1, 1),
    _PppLqmQuality_Type()
)
pppLqmQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmQuality.setStatus("mandatory")
_PppLqmInGoodOctets_Type = Counter32
_PppLqmInGoodOctets_Object = MibTableColumn
pppLqmInGoodOctets = _PppLqmInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1, 2),
    _PppLqmInGoodOctets_Type()
)
pppLqmInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInGoodOctets.setStatus("mandatory")


class _PppLqmLocalPeriod_Type(Unsigned32):
    """Custom type pppLqmLocalPeriod based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PppLqmLocalPeriod_Type.__name__ = "Unsigned32"
_PppLqmLocalPeriod_Object = MibTableColumn
pppLqmLocalPeriod = _PppLqmLocalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1, 3),
    _PppLqmLocalPeriod_Type()
)
pppLqmLocalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmLocalPeriod.setStatus("mandatory")


class _PppLqmRemotePeriod_Type(Unsigned32):
    """Custom type pppLqmRemotePeriod based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PppLqmRemotePeriod_Type.__name__ = "Unsigned32"
_PppLqmRemotePeriod_Object = MibTableColumn
pppLqmRemotePeriod = _PppLqmRemotePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1, 4),
    _PppLqmRemotePeriod_Type()
)
pppLqmRemotePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmRemotePeriod.setStatus("mandatory")
_PppLqmOutLqrs_Type = Counter32
_PppLqmOutLqrs_Object = MibTableColumn
pppLqmOutLqrs = _PppLqmOutLqrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1, 5),
    _PppLqmOutLqrs_Type()
)
pppLqmOutLqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmOutLqrs.setStatus("mandatory")
_PppLqmInLqrs_Type = Counter32
_PppLqmInLqrs_Object = MibTableColumn
pppLqmInLqrs = _PppLqmInLqrs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 3, 11, 1, 6),
    _PppLqmInLqrs_Type()
)
pppLqmInLqrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLqmInLqrs.setStatus("mandatory")
_PppNcp_ObjectIdentity = ObjectIdentity
pppNcp = _PppNcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4)
)
_PppNcpRowStatusTable_Object = MibTable
pppNcpRowStatusTable = _PppNcpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 1)
)
if mibBuilder.loadTexts:
    pppNcpRowStatusTable.setStatus("mandatory")
_PppNcpRowStatusEntry_Object = MibTableRow
pppNcpRowStatusEntry = _PppNcpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 1, 1)
)
pppNcpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
)
if mibBuilder.loadTexts:
    pppNcpRowStatusEntry.setStatus("mandatory")
_PppNcpRowStatus_Type = RowStatus
_PppNcpRowStatus_Object = MibTableColumn
pppNcpRowStatus = _PppNcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 1, 1, 1),
    _PppNcpRowStatus_Type()
)
pppNcpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpRowStatus.setStatus("mandatory")
_PppNcpComponentName_Type = DisplayString
_PppNcpComponentName_Object = MibTableColumn
pppNcpComponentName = _PppNcpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 1, 1, 2),
    _PppNcpComponentName_Type()
)
pppNcpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpComponentName.setStatus("mandatory")
_PppNcpStorageType_Type = StorageType
_PppNcpStorageType_Object = MibTableColumn
pppNcpStorageType = _PppNcpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 1, 1, 4),
    _PppNcpStorageType_Type()
)
pppNcpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpStorageType.setStatus("mandatory")
_PppNcpIndex_Type = NonReplicated
_PppNcpIndex_Object = MibTableColumn
pppNcpIndex = _PppNcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 1, 1, 10),
    _PppNcpIndex_Type()
)
pppNcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppNcpIndex.setStatus("mandatory")
_PppNcpBmcEntry_ObjectIdentity = ObjectIdentity
pppNcpBmcEntry = _PppNcpBmcEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2)
)
_PppNcpBmcEntryRowStatusTable_Object = MibTable
pppNcpBmcEntryRowStatusTable = _PppNcpBmcEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pppNcpBmcEntryRowStatusTable.setStatus("mandatory")
_PppNcpBmcEntryRowStatusEntry_Object = MibTableRow
pppNcpBmcEntryRowStatusEntry = _PppNcpBmcEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 1, 1)
)
pppNcpBmcEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpBmcEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    pppNcpBmcEntryRowStatusEntry.setStatus("mandatory")
_PppNcpBmcEntryRowStatus_Type = RowStatus
_PppNcpBmcEntryRowStatus_Object = MibTableColumn
pppNcpBmcEntryRowStatus = _PppNcpBmcEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 1, 1, 1),
    _PppNcpBmcEntryRowStatus_Type()
)
pppNcpBmcEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppNcpBmcEntryRowStatus.setStatus("mandatory")
_PppNcpBmcEntryComponentName_Type = DisplayString
_PppNcpBmcEntryComponentName_Object = MibTableColumn
pppNcpBmcEntryComponentName = _PppNcpBmcEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 1, 1, 2),
    _PppNcpBmcEntryComponentName_Type()
)
pppNcpBmcEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmcEntryComponentName.setStatus("mandatory")
_PppNcpBmcEntryStorageType_Type = StorageType
_PppNcpBmcEntryStorageType_Object = MibTableColumn
pppNcpBmcEntryStorageType = _PppNcpBmcEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 1, 1, 4),
    _PppNcpBmcEntryStorageType_Type()
)
pppNcpBmcEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmcEntryStorageType.setStatus("mandatory")


class _PppNcpBmcEntryMacTypeIndex_Type(Integer32):
    """Custom type pppNcpBmcEntryMacTypeIndex based on Integer32"""
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


_PppNcpBmcEntryMacTypeIndex_Type.__name__ = "Integer32"
_PppNcpBmcEntryMacTypeIndex_Object = MibTableColumn
pppNcpBmcEntryMacTypeIndex = _PppNcpBmcEntryMacTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 1, 1, 10),
    _PppNcpBmcEntryMacTypeIndex_Type()
)
pppNcpBmcEntryMacTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppNcpBmcEntryMacTypeIndex.setStatus("mandatory")
_PppNcpBmcEntryProvTable_Object = MibTable
pppNcpBmcEntryProvTable = _PppNcpBmcEntryProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 10)
)
if mibBuilder.loadTexts:
    pppNcpBmcEntryProvTable.setStatus("mandatory")
_PppNcpBmcEntryProvEntry_Object = MibTableRow
pppNcpBmcEntryProvEntry = _PppNcpBmcEntryProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 10, 1)
)
pppNcpBmcEntryProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpBmcEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    pppNcpBmcEntryProvEntry.setStatus("mandatory")


class _PppNcpBmcEntryLocalStatus_Type(Integer32):
    """Custom type pppNcpBmcEntryLocalStatus based on Integer32"""
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


_PppNcpBmcEntryLocalStatus_Type.__name__ = "Integer32"
_PppNcpBmcEntryLocalStatus_Object = MibTableColumn
pppNcpBmcEntryLocalStatus = _PppNcpBmcEntryLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 2, 10, 1, 1),
    _PppNcpBmcEntryLocalStatus_Type()
)
pppNcpBmcEntryLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppNcpBmcEntryLocalStatus.setStatus("mandatory")
_PppNcpBmEntry_ObjectIdentity = ObjectIdentity
pppNcpBmEntry = _PppNcpBmEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3)
)
_PppNcpBmEntryRowStatusTable_Object = MibTable
pppNcpBmEntryRowStatusTable = _PppNcpBmEntryRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 1)
)
if mibBuilder.loadTexts:
    pppNcpBmEntryRowStatusTable.setStatus("mandatory")
_PppNcpBmEntryRowStatusEntry_Object = MibTableRow
pppNcpBmEntryRowStatusEntry = _PppNcpBmEntryRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 1, 1)
)
pppNcpBmEntryRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpBmEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    pppNcpBmEntryRowStatusEntry.setStatus("mandatory")
_PppNcpBmEntryRowStatus_Type = RowStatus
_PppNcpBmEntryRowStatus_Object = MibTableColumn
pppNcpBmEntryRowStatus = _PppNcpBmEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 1, 1, 1),
    _PppNcpBmEntryRowStatus_Type()
)
pppNcpBmEntryRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmEntryRowStatus.setStatus("mandatory")
_PppNcpBmEntryComponentName_Type = DisplayString
_PppNcpBmEntryComponentName_Object = MibTableColumn
pppNcpBmEntryComponentName = _PppNcpBmEntryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 1, 1, 2),
    _PppNcpBmEntryComponentName_Type()
)
pppNcpBmEntryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmEntryComponentName.setStatus("mandatory")
_PppNcpBmEntryStorageType_Type = StorageType
_PppNcpBmEntryStorageType_Object = MibTableColumn
pppNcpBmEntryStorageType = _PppNcpBmEntryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 1, 1, 4),
    _PppNcpBmEntryStorageType_Type()
)
pppNcpBmEntryStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmEntryStorageType.setStatus("mandatory")


class _PppNcpBmEntryMacTypeIndex_Type(Integer32):
    """Custom type pppNcpBmEntryMacTypeIndex based on Integer32"""
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


_PppNcpBmEntryMacTypeIndex_Type.__name__ = "Integer32"
_PppNcpBmEntryMacTypeIndex_Object = MibTableColumn
pppNcpBmEntryMacTypeIndex = _PppNcpBmEntryMacTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 1, 1, 10),
    _PppNcpBmEntryMacTypeIndex_Type()
)
pppNcpBmEntryMacTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppNcpBmEntryMacTypeIndex.setStatus("mandatory")
_PppNcpBmEntryOperTable_Object = MibTable
pppNcpBmEntryOperTable = _PppNcpBmEntryOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 10)
)
if mibBuilder.loadTexts:
    pppNcpBmEntryOperTable.setStatus("mandatory")
_PppNcpBmEntryOperEntry_Object = MibTableRow
pppNcpBmEntryOperEntry = _PppNcpBmEntryOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 10, 1)
)
pppNcpBmEntryOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpBmEntryMacTypeIndex"),
)
if mibBuilder.loadTexts:
    pppNcpBmEntryOperEntry.setStatus("mandatory")


class _PppNcpBmEntryLocalStatus_Type(Integer32):
    """Custom type pppNcpBmEntryLocalStatus based on Integer32"""
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


_PppNcpBmEntryLocalStatus_Type.__name__ = "Integer32"
_PppNcpBmEntryLocalStatus_Object = MibTableColumn
pppNcpBmEntryLocalStatus = _PppNcpBmEntryLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 10, 1, 2),
    _PppNcpBmEntryLocalStatus_Type()
)
pppNcpBmEntryLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmEntryLocalStatus.setStatus("mandatory")


class _PppNcpBmEntryRemoteStatus_Type(Integer32):
    """Custom type pppNcpBmEntryRemoteStatus based on Integer32"""
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


_PppNcpBmEntryRemoteStatus_Type.__name__ = "Integer32"
_PppNcpBmEntryRemoteStatus_Object = MibTableColumn
pppNcpBmEntryRemoteStatus = _PppNcpBmEntryRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 3, 10, 1, 3),
    _PppNcpBmEntryRemoteStatus_Type()
)
pppNcpBmEntryRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBmEntryRemoteStatus.setStatus("mandatory")
_PppNcpBprovTable_Object = MibTable
pppNcpBprovTable = _PppNcpBprovTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 11)
)
if mibBuilder.loadTexts:
    pppNcpBprovTable.setStatus("mandatory")
_PppNcpBprovEntry_Object = MibTableRow
pppNcpBprovEntry = _PppNcpBprovEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 11, 1)
)
pppNcpBprovEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
)
if mibBuilder.loadTexts:
    pppNcpBprovEntry.setStatus("mandatory")


class _PppNcpBConfigTinygram_Type(Integer32):
    """Custom type pppNcpBConfigTinygram based on Integer32"""
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


_PppNcpBConfigTinygram_Type.__name__ = "Integer32"
_PppNcpBConfigTinygram_Object = MibTableColumn
pppNcpBConfigTinygram = _PppNcpBConfigTinygram_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 11, 1, 1),
    _PppNcpBConfigTinygram_Type()
)
pppNcpBConfigTinygram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppNcpBConfigTinygram.setStatus("mandatory")


class _PppNcpBConfigLanId_Type(Integer32):
    """Custom type pppNcpBConfigLanId based on Integer32"""
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


_PppNcpBConfigLanId_Type.__name__ = "Integer32"
_PppNcpBConfigLanId_Object = MibTableColumn
pppNcpBConfigLanId = _PppNcpBConfigLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 11, 1, 4),
    _PppNcpBConfigLanId_Type()
)
pppNcpBConfigLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppNcpBConfigLanId.setStatus("mandatory")
_PppNcpIpOperTable_Object = MibTable
pppNcpIpOperTable = _PppNcpIpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 12)
)
if mibBuilder.loadTexts:
    pppNcpIpOperTable.setStatus("mandatory")
_PppNcpIpOperEntry_Object = MibTableRow
pppNcpIpOperEntry = _PppNcpIpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 12, 1)
)
pppNcpIpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
)
if mibBuilder.loadTexts:
    pppNcpIpOperEntry.setStatus("mandatory")


class _PppNcpIpOperState_Type(Integer32):
    """Custom type pppNcpIpOperState based on Integer32"""
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


_PppNcpIpOperState_Type.__name__ = "Integer32"
_PppNcpIpOperState_Object = MibTableColumn
pppNcpIpOperState = _PppNcpIpOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 12, 1, 1),
    _PppNcpIpOperState_Type()
)
pppNcpIpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpIpOperState.setStatus("mandatory")
_PppNcpBoperTable_Object = MibTable
pppNcpBoperTable = _PppNcpBoperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14)
)
if mibBuilder.loadTexts:
    pppNcpBoperTable.setStatus("mandatory")
_PppNcpBoperEntry_Object = MibTableRow
pppNcpBoperEntry = _PppNcpBoperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14, 1)
)
pppNcpBoperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
)
if mibBuilder.loadTexts:
    pppNcpBoperEntry.setStatus("mandatory")


class _PppNcpBOperState_Type(Integer32):
    """Custom type pppNcpBOperState based on Integer32"""
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


_PppNcpBOperState_Type.__name__ = "Integer32"
_PppNcpBOperState_Object = MibTableColumn
pppNcpBOperState = _PppNcpBOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14, 1, 1),
    _PppNcpBOperState_Type()
)
pppNcpBOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBOperState.setStatus("mandatory")


class _PppNcpBLocalToRemoteTinygramComp_Type(Integer32):
    """Custom type pppNcpBLocalToRemoteTinygramComp based on Integer32"""
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


_PppNcpBLocalToRemoteTinygramComp_Type.__name__ = "Integer32"
_PppNcpBLocalToRemoteTinygramComp_Object = MibTableColumn
pppNcpBLocalToRemoteTinygramComp = _PppNcpBLocalToRemoteTinygramComp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14, 1, 3),
    _PppNcpBLocalToRemoteTinygramComp_Type()
)
pppNcpBLocalToRemoteTinygramComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBLocalToRemoteTinygramComp.setStatus("mandatory")


class _PppNcpBRemoteToLocalTinygramComp_Type(Integer32):
    """Custom type pppNcpBRemoteToLocalTinygramComp based on Integer32"""
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


_PppNcpBRemoteToLocalTinygramComp_Type.__name__ = "Integer32"
_PppNcpBRemoteToLocalTinygramComp_Object = MibTableColumn
pppNcpBRemoteToLocalTinygramComp = _PppNcpBRemoteToLocalTinygramComp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14, 1, 4),
    _PppNcpBRemoteToLocalTinygramComp_Type()
)
pppNcpBRemoteToLocalTinygramComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBRemoteToLocalTinygramComp.setStatus("mandatory")


class _PppNcpBLocalToRemoteLanId_Type(Integer32):
    """Custom type pppNcpBLocalToRemoteLanId based on Integer32"""
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


_PppNcpBLocalToRemoteLanId_Type.__name__ = "Integer32"
_PppNcpBLocalToRemoteLanId_Object = MibTableColumn
pppNcpBLocalToRemoteLanId = _PppNcpBLocalToRemoteLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14, 1, 5),
    _PppNcpBLocalToRemoteLanId_Type()
)
pppNcpBLocalToRemoteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBLocalToRemoteLanId.setStatus("mandatory")


class _PppNcpBRemoteToLocalLanId_Type(Integer32):
    """Custom type pppNcpBRemoteToLocalLanId based on Integer32"""
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


_PppNcpBRemoteToLocalLanId_Type.__name__ = "Integer32"
_PppNcpBRemoteToLocalLanId_Object = MibTableColumn
pppNcpBRemoteToLocalLanId = _PppNcpBRemoteToLocalLanId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 14, 1, 6),
    _PppNcpBRemoteToLocalLanId_Type()
)
pppNcpBRemoteToLocalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpBRemoteToLocalLanId.setStatus("mandatory")
_PppNcpOperTable_Object = MibTable
pppNcpOperTable = _PppNcpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 16)
)
if mibBuilder.loadTexts:
    pppNcpOperTable.setStatus("mandatory")
_PppNcpOperEntry_Object = MibTableRow
pppNcpOperEntry = _PppNcpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 16, 1)
)
pppNcpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppNcpIndex"),
)
if mibBuilder.loadTexts:
    pppNcpOperEntry.setStatus("mandatory")


class _PppNcpAppletalkOperState_Type(Integer32):
    """Custom type pppNcpAppletalkOperState based on Integer32"""
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


_PppNcpAppletalkOperState_Type.__name__ = "Integer32"
_PppNcpAppletalkOperState_Object = MibTableColumn
pppNcpAppletalkOperState = _PppNcpAppletalkOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 16, 1, 1),
    _PppNcpAppletalkOperState_Type()
)
pppNcpAppletalkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpAppletalkOperState.setStatus("mandatory")


class _PppNcpIpxOperState_Type(Integer32):
    """Custom type pppNcpIpxOperState based on Integer32"""
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


_PppNcpIpxOperState_Type.__name__ = "Integer32"
_PppNcpIpxOperState_Object = MibTableColumn
pppNcpIpxOperState = _PppNcpIpxOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 16, 1, 2),
    _PppNcpIpxOperState_Type()
)
pppNcpIpxOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpIpxOperState.setStatus("mandatory")


class _PppNcpXnsOperState_Type(Integer32):
    """Custom type pppNcpXnsOperState based on Integer32"""
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


_PppNcpXnsOperState_Type.__name__ = "Integer32"
_PppNcpXnsOperState_Object = MibTableColumn
pppNcpXnsOperState = _PppNcpXnsOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 16, 1, 3),
    _PppNcpXnsOperState_Type()
)
pppNcpXnsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpXnsOperState.setStatus("mandatory")


class _PppNcpDecnetOperState_Type(Integer32):
    """Custom type pppNcpDecnetOperState based on Integer32"""
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


_PppNcpDecnetOperState_Type.__name__ = "Integer32"
_PppNcpDecnetOperState_Object = MibTableColumn
pppNcpDecnetOperState = _PppNcpDecnetOperState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 4, 16, 1, 4),
    _PppNcpDecnetOperState_Type()
)
pppNcpDecnetOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNcpDecnetOperState.setStatus("mandatory")
_PppFramer_ObjectIdentity = ObjectIdentity
pppFramer = _PppFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5)
)
_PppFramerRowStatusTable_Object = MibTable
pppFramerRowStatusTable = _PppFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 1)
)
if mibBuilder.loadTexts:
    pppFramerRowStatusTable.setStatus("mandatory")
_PppFramerRowStatusEntry_Object = MibTableRow
pppFramerRowStatusEntry = _PppFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 1, 1)
)
pppFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppFramerIndex"),
)
if mibBuilder.loadTexts:
    pppFramerRowStatusEntry.setStatus("mandatory")
_PppFramerRowStatus_Type = RowStatus
_PppFramerRowStatus_Object = MibTableColumn
pppFramerRowStatus = _PppFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 1, 1, 1),
    _PppFramerRowStatus_Type()
)
pppFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerRowStatus.setStatus("mandatory")
_PppFramerComponentName_Type = DisplayString
_PppFramerComponentName_Object = MibTableColumn
pppFramerComponentName = _PppFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 1, 1, 2),
    _PppFramerComponentName_Type()
)
pppFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerComponentName.setStatus("mandatory")
_PppFramerStorageType_Type = StorageType
_PppFramerStorageType_Object = MibTableColumn
pppFramerStorageType = _PppFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 1, 1, 4),
    _PppFramerStorageType_Type()
)
pppFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerStorageType.setStatus("mandatory")
_PppFramerIndex_Type = NonReplicated
_PppFramerIndex_Object = MibTableColumn
pppFramerIndex = _PppFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 1, 1, 10),
    _PppFramerIndex_Type()
)
pppFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppFramerIndex.setStatus("mandatory")
_PppFramerProvTable_Object = MibTable
pppFramerProvTable = _PppFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 10)
)
if mibBuilder.loadTexts:
    pppFramerProvTable.setStatus("mandatory")
_PppFramerProvEntry_Object = MibTableRow
pppFramerProvEntry = _PppFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 10, 1)
)
pppFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppFramerIndex"),
)
if mibBuilder.loadTexts:
    pppFramerProvEntry.setStatus("mandatory")
_PppFramerInterfaceName_Type = Link
_PppFramerInterfaceName_Object = MibTableColumn
pppFramerInterfaceName = _PppFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 10, 1, 1),
    _PppFramerInterfaceName_Type()
)
pppFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppFramerInterfaceName.setStatus("mandatory")
_PppFramerStateTable_Object = MibTable
pppFramerStateTable = _PppFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 12)
)
if mibBuilder.loadTexts:
    pppFramerStateTable.setStatus("mandatory")
_PppFramerStateEntry_Object = MibTableRow
pppFramerStateEntry = _PppFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 12, 1)
)
pppFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppFramerIndex"),
)
if mibBuilder.loadTexts:
    pppFramerStateEntry.setStatus("mandatory")


class _PppFramerAdminState_Type(Integer32):
    """Custom type pppFramerAdminState based on Integer32"""
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


_PppFramerAdminState_Type.__name__ = "Integer32"
_PppFramerAdminState_Object = MibTableColumn
pppFramerAdminState = _PppFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 12, 1, 1),
    _PppFramerAdminState_Type()
)
pppFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerAdminState.setStatus("mandatory")


class _PppFramerOperationalState_Type(Integer32):
    """Custom type pppFramerOperationalState based on Integer32"""
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


_PppFramerOperationalState_Type.__name__ = "Integer32"
_PppFramerOperationalState_Object = MibTableColumn
pppFramerOperationalState = _PppFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 12, 1, 2),
    _PppFramerOperationalState_Type()
)
pppFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerOperationalState.setStatus("mandatory")


class _PppFramerUsageState_Type(Integer32):
    """Custom type pppFramerUsageState based on Integer32"""
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


_PppFramerUsageState_Type.__name__ = "Integer32"
_PppFramerUsageState_Object = MibTableColumn
pppFramerUsageState = _PppFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 12, 1, 3),
    _PppFramerUsageState_Type()
)
pppFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerUsageState.setStatus("mandatory")
_PppFramerStatsTable_Object = MibTable
pppFramerStatsTable = _PppFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13)
)
if mibBuilder.loadTexts:
    pppFramerStatsTable.setStatus("mandatory")
_PppFramerStatsEntry_Object = MibTableRow
pppFramerStatsEntry = _PppFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1)
)
pppFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppFramerIndex"),
)
if mibBuilder.loadTexts:
    pppFramerStatsEntry.setStatus("mandatory")
_PppFramerFrmToIf_Type = Counter32
_PppFramerFrmToIf_Object = MibTableColumn
pppFramerFrmToIf = _PppFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 1),
    _PppFramerFrmToIf_Type()
)
pppFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerFrmToIf.setStatus("mandatory")
_PppFramerFrmFromIf_Type = Counter32
_PppFramerFrmFromIf_Object = MibTableColumn
pppFramerFrmFromIf = _PppFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 2),
    _PppFramerFrmFromIf_Type()
)
pppFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerFrmFromIf.setStatus("mandatory")
_PppFramerAborts_Type = Counter32
_PppFramerAborts_Object = MibTableColumn
pppFramerAborts = _PppFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 3),
    _PppFramerAborts_Type()
)
pppFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerAborts.setStatus("mandatory")
_PppFramerCrcErrors_Type = Counter32
_PppFramerCrcErrors_Object = MibTableColumn
pppFramerCrcErrors = _PppFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 4),
    _PppFramerCrcErrors_Type()
)
pppFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerCrcErrors.setStatus("mandatory")
_PppFramerLrcErrors_Type = Counter32
_PppFramerLrcErrors_Object = MibTableColumn
pppFramerLrcErrors = _PppFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 5),
    _PppFramerLrcErrors_Type()
)
pppFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerLrcErrors.setStatus("mandatory")
_PppFramerNonOctetErrors_Type = Counter32
_PppFramerNonOctetErrors_Object = MibTableColumn
pppFramerNonOctetErrors = _PppFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 6),
    _PppFramerNonOctetErrors_Type()
)
pppFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerNonOctetErrors.setStatus("mandatory")
_PppFramerOverruns_Type = Counter32
_PppFramerOverruns_Object = MibTableColumn
pppFramerOverruns = _PppFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 7),
    _PppFramerOverruns_Type()
)
pppFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerOverruns.setStatus("mandatory")
_PppFramerUnderruns_Type = Counter32
_PppFramerUnderruns_Object = MibTableColumn
pppFramerUnderruns = _PppFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 8),
    _PppFramerUnderruns_Type()
)
pppFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerUnderruns.setStatus("mandatory")
_PppFramerLargeFrmErrors_Type = Counter32
_PppFramerLargeFrmErrors_Object = MibTableColumn
pppFramerLargeFrmErrors = _PppFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 13, 1, 9),
    _PppFramerLargeFrmErrors_Type()
)
pppFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerLargeFrmErrors.setStatus("mandatory")
_PppFramerUtilTable_Object = MibTable
pppFramerUtilTable = _PppFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 14)
)
if mibBuilder.loadTexts:
    pppFramerUtilTable.setStatus("mandatory")
_PppFramerUtilEntry_Object = MibTableRow
pppFramerUtilEntry = _PppFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 14, 1)
)
pppFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppFramerIndex"),
)
if mibBuilder.loadTexts:
    pppFramerUtilEntry.setStatus("mandatory")


class _PppFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type pppFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_PppFramerNormPrioLinkUtilToIf_Object = MibTableColumn
pppFramerNormPrioLinkUtilToIf = _PppFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 14, 1, 1),
    _PppFramerNormPrioLinkUtilToIf_Type()
)
pppFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _PppFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type pppFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PppFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_PppFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
pppFramerNormPrioLinkUtilFromIf = _PppFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 5, 14, 1, 3),
    _PppFramerNormPrioLinkUtilFromIf_Type()
)
pppFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_PppLeq_ObjectIdentity = ObjectIdentity
pppLeq = _PppLeq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6)
)
_PppLeqRowStatusTable_Object = MibTable
pppLeqRowStatusTable = _PppLeqRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 1)
)
if mibBuilder.loadTexts:
    pppLeqRowStatusTable.setStatus("mandatory")
_PppLeqRowStatusEntry_Object = MibTableRow
pppLeqRowStatusEntry = _PppLeqRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 1, 1)
)
pppLeqRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLeqIndex"),
)
if mibBuilder.loadTexts:
    pppLeqRowStatusEntry.setStatus("mandatory")
_PppLeqRowStatus_Type = RowStatus
_PppLeqRowStatus_Object = MibTableColumn
pppLeqRowStatus = _PppLeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 1, 1, 1),
    _PppLeqRowStatus_Type()
)
pppLeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLeqRowStatus.setStatus("mandatory")
_PppLeqComponentName_Type = DisplayString
_PppLeqComponentName_Object = MibTableColumn
pppLeqComponentName = _PppLeqComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 1, 1, 2),
    _PppLeqComponentName_Type()
)
pppLeqComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqComponentName.setStatus("mandatory")
_PppLeqStorageType_Type = StorageType
_PppLeqStorageType_Object = MibTableColumn
pppLeqStorageType = _PppLeqStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 1, 1, 4),
    _PppLeqStorageType_Type()
)
pppLeqStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqStorageType.setStatus("mandatory")
_PppLeqIndex_Type = NonReplicated
_PppLeqIndex_Object = MibTableColumn
pppLeqIndex = _PppLeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 1, 1, 10),
    _PppLeqIndex_Type()
)
pppLeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppLeqIndex.setStatus("mandatory")
_PppLeqProvTable_Object = MibTable
pppLeqProvTable = _PppLeqProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 10)
)
if mibBuilder.loadTexts:
    pppLeqProvTable.setStatus("mandatory")
_PppLeqProvEntry_Object = MibTableRow
pppLeqProvEntry = _PppLeqProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 10, 1)
)
pppLeqProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLeqIndex"),
)
if mibBuilder.loadTexts:
    pppLeqProvEntry.setStatus("mandatory")


class _PppLeqMaxPackets_Type(Unsigned32):
    """Custom type pppLeqMaxPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PppLeqMaxPackets_Type.__name__ = "Unsigned32"
_PppLeqMaxPackets_Object = MibTableColumn
pppLeqMaxPackets = _PppLeqMaxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 10, 1, 1),
    _PppLeqMaxPackets_Type()
)
pppLeqMaxPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLeqMaxPackets.setStatus("mandatory")


class _PppLeqMaxMsecData_Type(Unsigned32):
    """Custom type pppLeqMaxMsecData based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_PppLeqMaxMsecData_Type.__name__ = "Unsigned32"
_PppLeqMaxMsecData_Object = MibTableColumn
pppLeqMaxMsecData = _PppLeqMaxMsecData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 10, 1, 2),
    _PppLeqMaxMsecData_Type()
)
pppLeqMaxMsecData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLeqMaxMsecData.setStatus("mandatory")


class _PppLeqMaxPercentMulticast_Type(Unsigned32):
    """Custom type pppLeqMaxPercentMulticast based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PppLeqMaxPercentMulticast_Type.__name__ = "Unsigned32"
_PppLeqMaxPercentMulticast_Object = MibTableColumn
pppLeqMaxPercentMulticast = _PppLeqMaxPercentMulticast_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 10, 1, 3),
    _PppLeqMaxPercentMulticast_Type()
)
pppLeqMaxPercentMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLeqMaxPercentMulticast.setStatus("mandatory")


class _PppLeqTimeToLive_Type(Unsigned32):
    """Custom type pppLeqTimeToLive based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_PppLeqTimeToLive_Type.__name__ = "Unsigned32"
_PppLeqTimeToLive_Object = MibTableColumn
pppLeqTimeToLive = _PppLeqTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 10, 1, 4),
    _PppLeqTimeToLive_Type()
)
pppLeqTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLeqTimeToLive.setStatus("mandatory")
_PppLeqStatsTable_Object = MibTable
pppLeqStatsTable = _PppLeqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 11)
)
if mibBuilder.loadTexts:
    pppLeqStatsTable.setStatus("mandatory")
_PppLeqStatsEntry_Object = MibTableRow
pppLeqStatsEntry = _PppLeqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 11, 1)
)
pppLeqStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLeqIndex"),
)
if mibBuilder.loadTexts:
    pppLeqStatsEntry.setStatus("mandatory")
_PppLeqTimedOutPkt_Type = Counter32
_PppLeqTimedOutPkt_Object = MibTableColumn
pppLeqTimedOutPkt = _PppLeqTimedOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 11, 1, 1),
    _PppLeqTimedOutPkt_Type()
)
pppLeqTimedOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqTimedOutPkt.setStatus("mandatory")
_PppLeqHardwareForcedPkt_Type = Counter32
_PppLeqHardwareForcedPkt_Object = MibTableColumn
pppLeqHardwareForcedPkt = _PppLeqHardwareForcedPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 11, 1, 2),
    _PppLeqHardwareForcedPkt_Type()
)
pppLeqHardwareForcedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqHardwareForcedPkt.setStatus("mandatory")
_PppLeqForcedPktDiscards_Type = Counter32
_PppLeqForcedPktDiscards_Object = MibTableColumn
pppLeqForcedPktDiscards = _PppLeqForcedPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 11, 1, 4),
    _PppLeqForcedPktDiscards_Type()
)
pppLeqForcedPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqForcedPktDiscards.setStatus("mandatory")
_PppLeqQueuePurgeDiscards_Type = Counter32
_PppLeqQueuePurgeDiscards_Object = MibTableColumn
pppLeqQueuePurgeDiscards = _PppLeqQueuePurgeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 11, 1, 5),
    _PppLeqQueuePurgeDiscards_Type()
)
pppLeqQueuePurgeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqQueuePurgeDiscards.setStatus("mandatory")
_PppLeqTStatsTable_Object = MibTable
pppLeqTStatsTable = _PppLeqTStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12)
)
if mibBuilder.loadTexts:
    pppLeqTStatsTable.setStatus("mandatory")
_PppLeqTStatsEntry_Object = MibTableRow
pppLeqTStatsEntry = _PppLeqTStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12, 1)
)
pppLeqTStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLeqIndex"),
)
if mibBuilder.loadTexts:
    pppLeqTStatsEntry.setStatus("mandatory")
_PppLeqTotalPktHandled_Type = Counter32
_PppLeqTotalPktHandled_Object = MibTableColumn
pppLeqTotalPktHandled = _PppLeqTotalPktHandled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12, 1, 1),
    _PppLeqTotalPktHandled_Type()
)
pppLeqTotalPktHandled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqTotalPktHandled.setStatus("mandatory")
_PppLeqTotalPktForwarded_Type = Counter32
_PppLeqTotalPktForwarded_Object = MibTableColumn
pppLeqTotalPktForwarded = _PppLeqTotalPktForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12, 1, 2),
    _PppLeqTotalPktForwarded_Type()
)
pppLeqTotalPktForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqTotalPktForwarded.setStatus("mandatory")
_PppLeqTotalPktQueued_Type = Counter32
_PppLeqTotalPktQueued_Object = MibTableColumn
pppLeqTotalPktQueued = _PppLeqTotalPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12, 1, 3),
    _PppLeqTotalPktQueued_Type()
)
pppLeqTotalPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqTotalPktQueued.setStatus("mandatory")
_PppLeqTotalMulticastPkt_Type = Counter32
_PppLeqTotalMulticastPkt_Object = MibTableColumn
pppLeqTotalMulticastPkt = _PppLeqTotalMulticastPkt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12, 1, 4),
    _PppLeqTotalMulticastPkt_Type()
)
pppLeqTotalMulticastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqTotalMulticastPkt.setStatus("mandatory")
_PppLeqTotalPktDiscards_Type = Counter32
_PppLeqTotalPktDiscards_Object = MibTableColumn
pppLeqTotalPktDiscards = _PppLeqTotalPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 12, 1, 8),
    _PppLeqTotalPktDiscards_Type()
)
pppLeqTotalPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqTotalPktDiscards.setStatus("mandatory")
_PppLeqCStatsTable_Object = MibTable
pppLeqCStatsTable = _PppLeqCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 13)
)
if mibBuilder.loadTexts:
    pppLeqCStatsTable.setStatus("mandatory")
_PppLeqCStatsEntry_Object = MibTableRow
pppLeqCStatsEntry = _PppLeqCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 13, 1)
)
pppLeqCStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLeqIndex"),
)
if mibBuilder.loadTexts:
    pppLeqCStatsEntry.setStatus("mandatory")


class _PppLeqCurrentPktQueued_Type(Gauge32):
    """Custom type pppLeqCurrentPktQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLeqCurrentPktQueued_Type.__name__ = "Gauge32"
_PppLeqCurrentPktQueued_Object = MibTableColumn
pppLeqCurrentPktQueued = _PppLeqCurrentPktQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 13, 1, 1),
    _PppLeqCurrentPktQueued_Type()
)
pppLeqCurrentPktQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqCurrentPktQueued.setStatus("mandatory")


class _PppLeqCurrentBytesQueued_Type(Gauge32):
    """Custom type pppLeqCurrentBytesQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLeqCurrentBytesQueued_Type.__name__ = "Gauge32"
_PppLeqCurrentBytesQueued_Object = MibTableColumn
pppLeqCurrentBytesQueued = _PppLeqCurrentBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 13, 1, 2),
    _PppLeqCurrentBytesQueued_Type()
)
pppLeqCurrentBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqCurrentBytesQueued.setStatus("mandatory")


class _PppLeqCurrentMulticastQueued_Type(Gauge32):
    """Custom type pppLeqCurrentMulticastQueued based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLeqCurrentMulticastQueued_Type.__name__ = "Gauge32"
_PppLeqCurrentMulticastQueued_Object = MibTableColumn
pppLeqCurrentMulticastQueued = _PppLeqCurrentMulticastQueued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 13, 1, 3),
    _PppLeqCurrentMulticastQueued_Type()
)
pppLeqCurrentMulticastQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqCurrentMulticastQueued.setStatus("mandatory")
_PppLeqThrStatsTable_Object = MibTable
pppLeqThrStatsTable = _PppLeqThrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14)
)
if mibBuilder.loadTexts:
    pppLeqThrStatsTable.setStatus("mandatory")
_PppLeqThrStatsEntry_Object = MibTableRow
pppLeqThrStatsEntry = _PppLeqThrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1)
)
pppLeqThrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
    (0, "Nortel-Magellan-Passport-PppMIB", "pppLeqIndex"),
)
if mibBuilder.loadTexts:
    pppLeqThrStatsEntry.setStatus("mandatory")


class _PppLeqQueuePktThreshold_Type(Unsigned32):
    """Custom type pppLeqQueuePktThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLeqQueuePktThreshold_Type.__name__ = "Unsigned32"
_PppLeqQueuePktThreshold_Object = MibTableColumn
pppLeqQueuePktThreshold = _PppLeqQueuePktThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 1),
    _PppLeqQueuePktThreshold_Type()
)
pppLeqQueuePktThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqQueuePktThreshold.setStatus("mandatory")
_PppLeqPktThresholdExceeded_Type = Counter32
_PppLeqPktThresholdExceeded_Object = MibTableColumn
pppLeqPktThresholdExceeded = _PppLeqPktThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 2),
    _PppLeqPktThresholdExceeded_Type()
)
pppLeqPktThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqPktThresholdExceeded.setStatus("mandatory")


class _PppLeqQueueByteThreshold_Type(Unsigned32):
    """Custom type pppLeqQueueByteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLeqQueueByteThreshold_Type.__name__ = "Unsigned32"
_PppLeqQueueByteThreshold_Object = MibTableColumn
pppLeqQueueByteThreshold = _PppLeqQueueByteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 3),
    _PppLeqQueueByteThreshold_Type()
)
pppLeqQueueByteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqQueueByteThreshold.setStatus("mandatory")
_PppLeqByteThresholdExceeded_Type = Counter32
_PppLeqByteThresholdExceeded_Object = MibTableColumn
pppLeqByteThresholdExceeded = _PppLeqByteThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 4),
    _PppLeqByteThresholdExceeded_Type()
)
pppLeqByteThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqByteThresholdExceeded.setStatus("mandatory")


class _PppLeqQueueMulticastThreshold_Type(Unsigned32):
    """Custom type pppLeqQueueMulticastThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PppLeqQueueMulticastThreshold_Type.__name__ = "Unsigned32"
_PppLeqQueueMulticastThreshold_Object = MibTableColumn
pppLeqQueueMulticastThreshold = _PppLeqQueueMulticastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 5),
    _PppLeqQueueMulticastThreshold_Type()
)
pppLeqQueueMulticastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqQueueMulticastThreshold.setStatus("mandatory")
_PppLeqMulThresholdExceeded_Type = Counter32
_PppLeqMulThresholdExceeded_Object = MibTableColumn
pppLeqMulThresholdExceeded = _PppLeqMulThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 6),
    _PppLeqMulThresholdExceeded_Type()
)
pppLeqMulThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqMulThresholdExceeded.setStatus("mandatory")
_PppLeqMemThresholdExceeded_Type = Counter32
_PppLeqMemThresholdExceeded_Object = MibTableColumn
pppLeqMemThresholdExceeded = _PppLeqMemThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 6, 14, 1, 7),
    _PppLeqMemThresholdExceeded_Type()
)
pppLeqMemThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLeqMemThresholdExceeded.setStatus("mandatory")
_PppCidDataTable_Object = MibTable
pppCidDataTable = _PppCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 20)
)
if mibBuilder.loadTexts:
    pppCidDataTable.setStatus("mandatory")
_PppCidDataEntry_Object = MibTableRow
pppCidDataEntry = _PppCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 20, 1)
)
pppCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
)
if mibBuilder.loadTexts:
    pppCidDataEntry.setStatus("mandatory")


class _PppCustomerIdentifier_Type(Unsigned32):
    """Custom type pppCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_PppCustomerIdentifier_Type.__name__ = "Unsigned32"
_PppCustomerIdentifier_Object = MibTableColumn
pppCustomerIdentifier = _PppCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 20, 1, 1),
    _PppCustomerIdentifier_Type()
)
pppCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppCustomerIdentifier.setStatus("mandatory")
_PppIfEntryTable_Object = MibTable
pppIfEntryTable = _PppIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 21)
)
if mibBuilder.loadTexts:
    pppIfEntryTable.setStatus("mandatory")
_PppIfEntryEntry_Object = MibTableRow
pppIfEntryEntry = _PppIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 21, 1)
)
pppIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
)
if mibBuilder.loadTexts:
    pppIfEntryEntry.setStatus("mandatory")


class _PppIfAdminStatus_Type(Integer32):
    """Custom type pppIfAdminStatus based on Integer32"""
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


_PppIfAdminStatus_Type.__name__ = "Integer32"
_PppIfAdminStatus_Object = MibTableColumn
pppIfAdminStatus = _PppIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 21, 1, 1),
    _PppIfAdminStatus_Type()
)
pppIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppIfAdminStatus.setStatus("mandatory")


class _PppIfIndex_Type(InterfaceIndex):
    """Custom type pppIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppIfIndex_Type.__name__ = "InterfaceIndex"
_PppIfIndex_Object = MibTableColumn
pppIfIndex = _PppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 21, 1, 2),
    _PppIfIndex_Type()
)
pppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIfIndex.setStatus("mandatory")
_PppMpTable_Object = MibTable
pppMpTable = _PppMpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 22)
)
if mibBuilder.loadTexts:
    pppMpTable.setStatus("mandatory")
_PppMpEntry_Object = MibTableRow
pppMpEntry = _PppMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 22, 1)
)
pppMpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
)
if mibBuilder.loadTexts:
    pppMpEntry.setStatus("mandatory")
_PppLinkToProtocolPort_Type = Link
_PppLinkToProtocolPort_Object = MibTableColumn
pppLinkToProtocolPort = _PppLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 22, 1, 1),
    _PppLinkToProtocolPort_Type()
)
pppLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppLinkToProtocolPort.setStatus("mandatory")
_PppStateTable_Object = MibTable
pppStateTable = _PppStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 23)
)
if mibBuilder.loadTexts:
    pppStateTable.setStatus("mandatory")
_PppStateEntry_Object = MibTableRow
pppStateEntry = _PppStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 23, 1)
)
pppStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
)
if mibBuilder.loadTexts:
    pppStateEntry.setStatus("mandatory")


class _PppAdminState_Type(Integer32):
    """Custom type pppAdminState based on Integer32"""
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


_PppAdminState_Type.__name__ = "Integer32"
_PppAdminState_Object = MibTableColumn
pppAdminState = _PppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 23, 1, 1),
    _PppAdminState_Type()
)
pppAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppAdminState.setStatus("mandatory")


class _PppOperationalState_Type(Integer32):
    """Custom type pppOperationalState based on Integer32"""
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


_PppOperationalState_Type.__name__ = "Integer32"
_PppOperationalState_Object = MibTableColumn
pppOperationalState = _PppOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 23, 1, 2),
    _PppOperationalState_Type()
)
pppOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppOperationalState.setStatus("mandatory")


class _PppUsageState_Type(Integer32):
    """Custom type pppUsageState based on Integer32"""
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


_PppUsageState_Type.__name__ = "Integer32"
_PppUsageState_Object = MibTableColumn
pppUsageState = _PppUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 23, 1, 3),
    _PppUsageState_Type()
)
pppUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppUsageState.setStatus("mandatory")
_PppOperStatusTable_Object = MibTable
pppOperStatusTable = _PppOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 24)
)
if mibBuilder.loadTexts:
    pppOperStatusTable.setStatus("mandatory")
_PppOperStatusEntry_Object = MibTableRow
pppOperStatusEntry = _PppOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 24, 1)
)
pppOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-PppMIB", "pppIndex"),
)
if mibBuilder.loadTexts:
    pppOperStatusEntry.setStatus("mandatory")


class _PppSnmpOperStatus_Type(Integer32):
    """Custom type pppSnmpOperStatus based on Integer32"""
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


_PppSnmpOperStatus_Type.__name__ = "Integer32"
_PppSnmpOperStatus_Object = MibTableColumn
pppSnmpOperStatus = _PppSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 102, 24, 1, 1),
    _PppSnmpOperStatus_Type()
)
pppSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppSnmpOperStatus.setStatus("mandatory")
_PppMIB_ObjectIdentity = ObjectIdentity
pppMIB = _PppMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33)
)
_PppGroup_ObjectIdentity = ObjectIdentity
pppGroup = _PppGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 1)
)
_PppGroupBC_ObjectIdentity = ObjectIdentity
pppGroupBC = _PppGroupBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 1, 3)
)
_PppGroupBC02_ObjectIdentity = ObjectIdentity
pppGroupBC02 = _PppGroupBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 1, 3, 3)
)
_PppGroupBC02A_ObjectIdentity = ObjectIdentity
pppGroupBC02A = _PppGroupBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 1, 3, 3, 2)
)
_PppCapabilities_ObjectIdentity = ObjectIdentity
pppCapabilities = _PppCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 3)
)
_PppCapabilitiesBC_ObjectIdentity = ObjectIdentity
pppCapabilitiesBC = _PppCapabilitiesBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 3, 3)
)
_PppCapabilitiesBC02_ObjectIdentity = ObjectIdentity
pppCapabilitiesBC02 = _PppCapabilitiesBC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 3, 3, 3)
)
_PppCapabilitiesBC02A_ObjectIdentity = ObjectIdentity
pppCapabilitiesBC02A = _PppCapabilitiesBC02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 33, 3, 3, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-PppMIB",
    **{"ppp": ppp,
       "pppRowStatusTable": pppRowStatusTable,
       "pppRowStatusEntry": pppRowStatusEntry,
       "pppRowStatus": pppRowStatus,
       "pppComponentName": pppComponentName,
       "pppStorageType": pppStorageType,
       "pppIndex": pppIndex,
       "pppLnk": pppLnk,
       "pppLnkRowStatusTable": pppLnkRowStatusTable,
       "pppLnkRowStatusEntry": pppLnkRowStatusEntry,
       "pppLnkRowStatus": pppLnkRowStatus,
       "pppLnkComponentName": pppLnkComponentName,
       "pppLnkStorageType": pppLnkStorageType,
       "pppLnkIndex": pppLnkIndex,
       "pppLnkProvTable": pppLnkProvTable,
       "pppLnkProvEntry": pppLnkProvEntry,
       "pppLnkConfigInitialMru": pppLnkConfigInitialMru,
       "pppLnkConfigMagicNumber": pppLnkConfigMagicNumber,
       "pppLnkRestartTimer": pppLnkRestartTimer,
       "pppLnkContinuityMonitor": pppLnkContinuityMonitor,
       "pppLnkNegativeAckTries": pppLnkNegativeAckTries,
       "pppLnkQualityThreshold": pppLnkQualityThreshold,
       "pppLnkQualityWindow": pppLnkQualityWindow,
       "pppLnkTerminateRequestTries": pppLnkTerminateRequestTries,
       "pppLnkConfigureRequestTries": pppLnkConfigureRequestTries,
       "pppLnkOperTable": pppLnkOperTable,
       "pppLnkOperEntry": pppLnkOperEntry,
       "pppLnkOperState": pppLnkOperState,
       "pppLnkLineCondition": pppLnkLineCondition,
       "pppLnkBadAddresses": pppLnkBadAddresses,
       "pppLnkBadControls": pppLnkBadControls,
       "pppLnkPacketTooLongs": pppLnkPacketTooLongs,
       "pppLnkBadFcss": pppLnkBadFcss,
       "pppLnkLocalMru": pppLnkLocalMru,
       "pppLnkRemoteMru": pppLnkRemoteMru,
       "pppLnkTransmitFcsSize": pppLnkTransmitFcsSize,
       "pppLnkReceiveFcsSize": pppLnkReceiveFcsSize,
       "pppLqm": pppLqm,
       "pppLqmRowStatusTable": pppLqmRowStatusTable,
       "pppLqmRowStatusEntry": pppLqmRowStatusEntry,
       "pppLqmRowStatus": pppLqmRowStatus,
       "pppLqmComponentName": pppLqmComponentName,
       "pppLqmStorageType": pppLqmStorageType,
       "pppLqmIndex": pppLqmIndex,
       "pppLqmProvTable": pppLqmProvTable,
       "pppLqmProvEntry": pppLqmProvEntry,
       "pppLqmConfigPeriod": pppLqmConfigPeriod,
       "pppLqmConfigStatus": pppLqmConfigStatus,
       "pppLqmOperTable": pppLqmOperTable,
       "pppLqmOperEntry": pppLqmOperEntry,
       "pppLqmQuality": pppLqmQuality,
       "pppLqmInGoodOctets": pppLqmInGoodOctets,
       "pppLqmLocalPeriod": pppLqmLocalPeriod,
       "pppLqmRemotePeriod": pppLqmRemotePeriod,
       "pppLqmOutLqrs": pppLqmOutLqrs,
       "pppLqmInLqrs": pppLqmInLqrs,
       "pppNcp": pppNcp,
       "pppNcpRowStatusTable": pppNcpRowStatusTable,
       "pppNcpRowStatusEntry": pppNcpRowStatusEntry,
       "pppNcpRowStatus": pppNcpRowStatus,
       "pppNcpComponentName": pppNcpComponentName,
       "pppNcpStorageType": pppNcpStorageType,
       "pppNcpIndex": pppNcpIndex,
       "pppNcpBmcEntry": pppNcpBmcEntry,
       "pppNcpBmcEntryRowStatusTable": pppNcpBmcEntryRowStatusTable,
       "pppNcpBmcEntryRowStatusEntry": pppNcpBmcEntryRowStatusEntry,
       "pppNcpBmcEntryRowStatus": pppNcpBmcEntryRowStatus,
       "pppNcpBmcEntryComponentName": pppNcpBmcEntryComponentName,
       "pppNcpBmcEntryStorageType": pppNcpBmcEntryStorageType,
       "pppNcpBmcEntryMacTypeIndex": pppNcpBmcEntryMacTypeIndex,
       "pppNcpBmcEntryProvTable": pppNcpBmcEntryProvTable,
       "pppNcpBmcEntryProvEntry": pppNcpBmcEntryProvEntry,
       "pppNcpBmcEntryLocalStatus": pppNcpBmcEntryLocalStatus,
       "pppNcpBmEntry": pppNcpBmEntry,
       "pppNcpBmEntryRowStatusTable": pppNcpBmEntryRowStatusTable,
       "pppNcpBmEntryRowStatusEntry": pppNcpBmEntryRowStatusEntry,
       "pppNcpBmEntryRowStatus": pppNcpBmEntryRowStatus,
       "pppNcpBmEntryComponentName": pppNcpBmEntryComponentName,
       "pppNcpBmEntryStorageType": pppNcpBmEntryStorageType,
       "pppNcpBmEntryMacTypeIndex": pppNcpBmEntryMacTypeIndex,
       "pppNcpBmEntryOperTable": pppNcpBmEntryOperTable,
       "pppNcpBmEntryOperEntry": pppNcpBmEntryOperEntry,
       "pppNcpBmEntryLocalStatus": pppNcpBmEntryLocalStatus,
       "pppNcpBmEntryRemoteStatus": pppNcpBmEntryRemoteStatus,
       "pppNcpBprovTable": pppNcpBprovTable,
       "pppNcpBprovEntry": pppNcpBprovEntry,
       "pppNcpBConfigTinygram": pppNcpBConfigTinygram,
       "pppNcpBConfigLanId": pppNcpBConfigLanId,
       "pppNcpIpOperTable": pppNcpIpOperTable,
       "pppNcpIpOperEntry": pppNcpIpOperEntry,
       "pppNcpIpOperState": pppNcpIpOperState,
       "pppNcpBoperTable": pppNcpBoperTable,
       "pppNcpBoperEntry": pppNcpBoperEntry,
       "pppNcpBOperState": pppNcpBOperState,
       "pppNcpBLocalToRemoteTinygramComp": pppNcpBLocalToRemoteTinygramComp,
       "pppNcpBRemoteToLocalTinygramComp": pppNcpBRemoteToLocalTinygramComp,
       "pppNcpBLocalToRemoteLanId": pppNcpBLocalToRemoteLanId,
       "pppNcpBRemoteToLocalLanId": pppNcpBRemoteToLocalLanId,
       "pppNcpOperTable": pppNcpOperTable,
       "pppNcpOperEntry": pppNcpOperEntry,
       "pppNcpAppletalkOperState": pppNcpAppletalkOperState,
       "pppNcpIpxOperState": pppNcpIpxOperState,
       "pppNcpXnsOperState": pppNcpXnsOperState,
       "pppNcpDecnetOperState": pppNcpDecnetOperState,
       "pppFramer": pppFramer,
       "pppFramerRowStatusTable": pppFramerRowStatusTable,
       "pppFramerRowStatusEntry": pppFramerRowStatusEntry,
       "pppFramerRowStatus": pppFramerRowStatus,
       "pppFramerComponentName": pppFramerComponentName,
       "pppFramerStorageType": pppFramerStorageType,
       "pppFramerIndex": pppFramerIndex,
       "pppFramerProvTable": pppFramerProvTable,
       "pppFramerProvEntry": pppFramerProvEntry,
       "pppFramerInterfaceName": pppFramerInterfaceName,
       "pppFramerStateTable": pppFramerStateTable,
       "pppFramerStateEntry": pppFramerStateEntry,
       "pppFramerAdminState": pppFramerAdminState,
       "pppFramerOperationalState": pppFramerOperationalState,
       "pppFramerUsageState": pppFramerUsageState,
       "pppFramerStatsTable": pppFramerStatsTable,
       "pppFramerStatsEntry": pppFramerStatsEntry,
       "pppFramerFrmToIf": pppFramerFrmToIf,
       "pppFramerFrmFromIf": pppFramerFrmFromIf,
       "pppFramerAborts": pppFramerAborts,
       "pppFramerCrcErrors": pppFramerCrcErrors,
       "pppFramerLrcErrors": pppFramerLrcErrors,
       "pppFramerNonOctetErrors": pppFramerNonOctetErrors,
       "pppFramerOverruns": pppFramerOverruns,
       "pppFramerUnderruns": pppFramerUnderruns,
       "pppFramerLargeFrmErrors": pppFramerLargeFrmErrors,
       "pppFramerUtilTable": pppFramerUtilTable,
       "pppFramerUtilEntry": pppFramerUtilEntry,
       "pppFramerNormPrioLinkUtilToIf": pppFramerNormPrioLinkUtilToIf,
       "pppFramerNormPrioLinkUtilFromIf": pppFramerNormPrioLinkUtilFromIf,
       "pppLeq": pppLeq,
       "pppLeqRowStatusTable": pppLeqRowStatusTable,
       "pppLeqRowStatusEntry": pppLeqRowStatusEntry,
       "pppLeqRowStatus": pppLeqRowStatus,
       "pppLeqComponentName": pppLeqComponentName,
       "pppLeqStorageType": pppLeqStorageType,
       "pppLeqIndex": pppLeqIndex,
       "pppLeqProvTable": pppLeqProvTable,
       "pppLeqProvEntry": pppLeqProvEntry,
       "pppLeqMaxPackets": pppLeqMaxPackets,
       "pppLeqMaxMsecData": pppLeqMaxMsecData,
       "pppLeqMaxPercentMulticast": pppLeqMaxPercentMulticast,
       "pppLeqTimeToLive": pppLeqTimeToLive,
       "pppLeqStatsTable": pppLeqStatsTable,
       "pppLeqStatsEntry": pppLeqStatsEntry,
       "pppLeqTimedOutPkt": pppLeqTimedOutPkt,
       "pppLeqHardwareForcedPkt": pppLeqHardwareForcedPkt,
       "pppLeqForcedPktDiscards": pppLeqForcedPktDiscards,
       "pppLeqQueuePurgeDiscards": pppLeqQueuePurgeDiscards,
       "pppLeqTStatsTable": pppLeqTStatsTable,
       "pppLeqTStatsEntry": pppLeqTStatsEntry,
       "pppLeqTotalPktHandled": pppLeqTotalPktHandled,
       "pppLeqTotalPktForwarded": pppLeqTotalPktForwarded,
       "pppLeqTotalPktQueued": pppLeqTotalPktQueued,
       "pppLeqTotalMulticastPkt": pppLeqTotalMulticastPkt,
       "pppLeqTotalPktDiscards": pppLeqTotalPktDiscards,
       "pppLeqCStatsTable": pppLeqCStatsTable,
       "pppLeqCStatsEntry": pppLeqCStatsEntry,
       "pppLeqCurrentPktQueued": pppLeqCurrentPktQueued,
       "pppLeqCurrentBytesQueued": pppLeqCurrentBytesQueued,
       "pppLeqCurrentMulticastQueued": pppLeqCurrentMulticastQueued,
       "pppLeqThrStatsTable": pppLeqThrStatsTable,
       "pppLeqThrStatsEntry": pppLeqThrStatsEntry,
       "pppLeqQueuePktThreshold": pppLeqQueuePktThreshold,
       "pppLeqPktThresholdExceeded": pppLeqPktThresholdExceeded,
       "pppLeqQueueByteThreshold": pppLeqQueueByteThreshold,
       "pppLeqByteThresholdExceeded": pppLeqByteThresholdExceeded,
       "pppLeqQueueMulticastThreshold": pppLeqQueueMulticastThreshold,
       "pppLeqMulThresholdExceeded": pppLeqMulThresholdExceeded,
       "pppLeqMemThresholdExceeded": pppLeqMemThresholdExceeded,
       "pppCidDataTable": pppCidDataTable,
       "pppCidDataEntry": pppCidDataEntry,
       "pppCustomerIdentifier": pppCustomerIdentifier,
       "pppIfEntryTable": pppIfEntryTable,
       "pppIfEntryEntry": pppIfEntryEntry,
       "pppIfAdminStatus": pppIfAdminStatus,
       "pppIfIndex": pppIfIndex,
       "pppMpTable": pppMpTable,
       "pppMpEntry": pppMpEntry,
       "pppLinkToProtocolPort": pppLinkToProtocolPort,
       "pppStateTable": pppStateTable,
       "pppStateEntry": pppStateEntry,
       "pppAdminState": pppAdminState,
       "pppOperationalState": pppOperationalState,
       "pppUsageState": pppUsageState,
       "pppOperStatusTable": pppOperStatusTable,
       "pppOperStatusEntry": pppOperStatusEntry,
       "pppSnmpOperStatus": pppSnmpOperStatus,
       "pppMIB": pppMIB,
       "pppGroup": pppGroup,
       "pppGroupBC": pppGroupBC,
       "pppGroupBC02": pppGroupBC02,
       "pppGroupBC02A": pppGroupBC02A,
       "pppCapabilities": pppCapabilities,
       "pppCapabilitiesBC": pppCapabilitiesBC,
       "pppCapabilitiesBC02": pppCapabilitiesBC02,
       "pppCapabilitiesBC02A": pppCapabilitiesBC02A}
)
